#!/usr/bin/env python3
"""Mux SFX and optional licensed voice/music with full-duration audio into MP4."""
from __future__ import annotations
import argparse,json,subprocess
from pathlib import Path

ROOT=Path(__file__).resolve().parents[2]
def duration_of(path:Path):
    p=subprocess.run(['ffprobe','-v','error','-show_entries','format=duration','-of','json',str(path)],capture_output=True,text=True,check=True)
    return float(json.loads(p.stdout)['format']['duration'])

def mux(video:Path,output:Path,effects:Path|None=None,voice:Path|None=None,music:Path|None=None):
    video=Path(video).resolve();output=Path(output).resolve();output.parent.mkdir(parents=True,exist_ok=True)
    D=duration_of(video)
    if not any([effects,voice,music]): raise ValueError('An effects, voice or licensed music track is required; silent videos should not claim audio')
    inputs=['-i',str(video)];streams=[]
    for p,volume,label in [(effects,.60,'fx'),(voice,.92,'voice'),(music,.13,'music')]:
        if p is None:continue
        p=Path(p).resolve()
        if not p.is_file():raise FileNotFoundError(p)
        stream=len(streams)+1;inputs+=['-i',str(p)]
        streams.append((stream,volume,label))
    filters=[]
    for stream,volume,label in streams:
        filters.append(f'[{stream}:a:0]aresample=48000,volume={volume},apad,atrim=duration={D:.5f},asetpts=PTS-STARTPTS[{label}]')
    chained=''.join('['+x[2]+']' for x in streams)
    filters.append(f'{chained}amix=inputs={len(streams)}:duration=longest:normalize=0,alimiter=limit=0.95[out]')
    cmd=['ffmpeg','-hide_banner','-loglevel','error','-y',*inputs,'-filter_complex',';'.join(filters),
         '-map','0:v:0','-map','[out]','-c:v','copy','-c:a','aac','-b:a','192k',
         '-t',str(D),'-movflags','+faststart',str(output)]
    subprocess.run(cmd,check=True)
    print('Muxed',output,'duration',round(D,3),'tracks',','.join(x[2] for x in streams))
    return output
if __name__=='__main__':
    a=argparse.ArgumentParser(description=__doc__)
    a.add_argument('--video',type=Path,required=True);a.add_argument('--output',type=Path,default=ROOT/'output/reel.mp4')
    a.add_argument('--effects',type=Path);a.add_argument('--voice',type=Path);a.add_argument('--music',type=Path)
    x=a.parse_args();mux(x.video,x.output,x.effects,x.voice,x.music)
