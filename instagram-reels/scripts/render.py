#!/usr/bin/env python3
"""Render pure-time Canvas frames through Chromium screenshot bytes into FFmpeg."""
from __future__ import annotations
import argparse
from pathlib import Path
import subprocess
import sys
from playwright.sync_api import sync_playwright
from _runtime import open_scene, screenshot, ensure_dimensions

ROOT = Path(__file__).resolve().parents[2]
DEFAULT_SCENE = ROOT/'instagram-reels/examples/demo/scene.html'


def render(scene:Path, output:Path, duration:float=12, fps:int=30, width:int=1080, height:int=1920):
    ensure_dimensions(width, height)
    if not (0 < duration <= 600 and 1 <= fps <= 120):
        raise ValueError('duration must be 0–600 seconds and fps 1–120')
    output = Path(output).expanduser().resolve()
    output.parent.mkdir(parents=True,exist_ok=True)
    args=['ffmpeg','-hide_banner','-loglevel','error','-y',
          '-f','image2pipe','-framerate',str(fps),'-vcodec','png','-i','-',
          '-an','-c:v','libx264','-preset','veryfast','-crf','18','-pix_fmt','yuv420p',
          '-movflags','+faststart',str(output)]
    n=round(duration*fps)
    with sync_playwright() as p:
        browser, context, page, server = open_scene(p,scene,width,height)
        process=None
        try:
            process=subprocess.Popen(args,stdin=subprocess.PIPE,stderr=subprocess.PIPE)
            try:
                for frame in range(n):
                    payload=screenshot(page,frame/fps)
                    process.stdin.write(payload)
                process.stdin.close()
                error=process.stderr.read().decode('utf-8','replace')
                code=process.wait(timeout=120)
                if code:
                    raise RuntimeError(f'FFmpeg failed ({code}): {error[-2500:]}')
            except Exception:
                if process.poll() is None: process.kill()
                process.wait()
                raise
        finally:
            context.close();browser.close();server.shutdown();server.server_close()
    if not output.is_file() or output.stat().st_size==0: raise RuntimeError('Output MP4 not created')
    print(f'Rendered {output} ({n} frames, {width}x{height}, {fps}fps)')
    return output


def main():
    a=argparse.ArgumentParser(description=__doc__)
    a.add_argument('--scene',type=Path,default=DEFAULT_SCENE)
    a.add_argument('--output',type=Path,default=ROOT/'output/silent.mp4')
    a.add_argument('--duration',type=float,default=12)
    a.add_argument('--fps',type=int,default=30)
    a.add_argument('--width',type=int,default=1080)
    a.add_argument('--height',type=int,default=1920)
    x=a.parse_args()
    render(x.scene,x.output,x.duration,x.fps,x.width,x.height)
if __name__=='__main__':main()
