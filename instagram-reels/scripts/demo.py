#!/usr/bin/env python3
"""One-command example: real contact sheet, frame render, original SFX, verified MP4."""
from __future__ import annotations
import argparse,json
from pathlib import Path
from contact_sheet import sheet
from render import render
from audio_synth import synth
from mux import mux
from verify import probe

ROOT=Path(__file__).resolve().parents[2]
SRC=ROOT/'instagram-reels/examples/demo'

def demo(draft=False,full=False):
    output=ROOT/'output';output.mkdir(parents=True,exist_ok=True)
    width,height,fps=(360,640,15) if draft else (1080,1920,30) if full else (540,960,24)
    path=output/('reel-draft.mp4' if draft else 'reel.mp4')
    silent=output/('silent-draft.mp4' if draft else 'silent.mp4')
    sheet(SRC/'scene.html',output/'contact-sheet.png',12,1.5,270,480)
    render(SRC/'scene.html',silent,12,fps,width,height)
    synth(json.loads((SRC/'sfx.json').read_text(encoding='utf-8')),output/'effects.wav')
    mux(silent,path,effects=output/'effects.wav')
    result=probe(path,width,height,True,min_duration=11.8)
    report={'rendered':True,'name':'Instagram Reels: motion-as-story demo','format':'9:16','resolution':f'{width}x{height}',
            'fps':fps,'duration_seconds':round(result['duration'],3),'audio':'Original procedural SFX only; no narration',
            'contact_sheet':'output/contact-sheet.png','video':str(path.relative_to(ROOT)),
            'limitations':['Storyboard stills not manually art-directed as a generated image','Sample demonstrates one editorial style, not all 12 style implementations']}
    (output/'report.json').write_text(json.dumps(report,indent=2)+'\n',encoding='utf-8')
    print('SUCCESS:',path,'AND',output/'contact-sheet.png')
    return path
if __name__=='__main__':
    a=argparse.ArgumentParser(description=__doc__);g=a.add_mutually_exclusive_group();g.add_argument('--draft',action='store_true');g.add_argument('--full',action='store_true');x=a.parse_args();demo(x.draft,x.full)
