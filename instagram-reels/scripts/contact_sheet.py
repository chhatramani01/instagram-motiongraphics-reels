#!/usr/bin/env python3
"""Make honest visual QC storyboard PNG by sampling actual code-rendered frames."""
from __future__ import annotations
import argparse
from pathlib import Path
import tempfile
import subprocess
from playwright.sync_api import sync_playwright
from _runtime import open_scene, screenshot, ensure_dimensions

ROOT=Path(__file__).resolve().parents[2]

def sheet(scene:Path,output:Path,duration:float=12,step:float=1.5,width:int=270,height:int=480):
    ensure_dimensions(width,height)
    if duration<=0 or step<=0: raise ValueError('duration and step must be positive')
    output=Path(output).expanduser().resolve();output.parent.mkdir(parents=True,exist_ok=True)
    with tempfile.TemporaryDirectory() as td:
        folder=Path(td)
        with sync_playwright() as p:
            browser,context,page,server=open_scene(p,scene,width,height)
            try:
                n=0;t=0.0
                while t<duration-1e-8:
                    (folder/f'frame-{n:03d}.png').write_bytes(screenshot(page,t))
                    n+=1;t=n*step
            finally:context.close();browser.close();server.shutdown();server.server_close()
        cols=min(n,4);rows=(n+cols-1)//cols
        cmd=['ffmpeg','-hide_banner','-loglevel','error','-y',
             '-framerate','1','-i',str(folder/'frame-%03d.png'),
             '-vf',f'tile={cols}x{rows}:nb_frames={n}:padding=6:margin=8:color=0x172523',
             '-frames:v','1',str(output)]
        subprocess.run(cmd,check=True)
    if output.stat().st_size==0:raise RuntimeError('No contact sheet generated')
    print(f'Contact sheet: {output} ({n} frames)')
    return output

if __name__=='__main__':
    a=argparse.ArgumentParser(description=__doc__)
    a.add_argument('--scene',type=Path,default=ROOT/'instagram-reels/examples/demo/scene.html')
    a.add_argument('--output',type=Path,default=ROOT/'output/contact-sheet.png')
    a.add_argument('--duration',type=float,default=12)
    a.add_argument('--step',type=float,default=1.5)
    a.add_argument('--width',type=int,default=270)
    a.add_argument('--height',type=int,default=480)
    x=a.parse_args();sheet(x.scene,x.output,x.duration,x.step,x.width,x.height)
