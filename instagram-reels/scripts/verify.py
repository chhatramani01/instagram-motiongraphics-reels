#!/usr/bin/env python3
"""Verify output with ffprobe: streams, codecs, pixel format, duration, dimensions."""
from __future__ import annotations
import argparse,json,subprocess
from pathlib import Path

def probe(path:Path,expected_width:int|None=None,expected_height:int|None=None,audio=True,min_duration=0.2):
    r=subprocess.run(['ffprobe','-v','error','-show_streams','-show_format','-of','json',str(path)],capture_output=True,text=True,check=True)
    j=json.loads(r.stdout);ss=j.get('streams',[])
    v=next((s for s in ss if s.get('codec_type')=='video'),None)
    a=next((s for s in ss if s.get('codec_type')=='audio'),None)
    if not v or v.get('codec_name')!='h264':raise ValueError('Missing H.264 stream')
    if v.get('pix_fmt')!='yuv420p':raise ValueError('Wrong pixel format: '+str(v.get('pix_fmt')))
    if audio and (not a or a.get('codec_name')!='aac'):raise ValueError('Missing AAC audio stream')
    if expected_width is not None and v.get('width')!=expected_width:raise ValueError('Wrong video width')
    if expected_height is not None and v.get('height')!=expected_height:raise ValueError('Wrong video height')
    d=float(j.get('format',{}).get('duration') or 0)
    if d<min_duration:raise ValueError('Video too short')
    print('PASS:',path,'video',v.get('width'),v.get('height'),v['codec_name'],v['pix_fmt'],'audio',a.get('codec_name') if a else 'none','duration',round(d,3))
    return {'width':v['width'],'height':v['height'],'duration':d,'audio':bool(a)}
if __name__=='__main__':
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('file',type=Path);p.add_argument('--width',type=int);p.add_argument('--height',type=int);p.add_argument('--no-audio',action='store_true')
    x=p.parse_args();probe(x.file,x.width,x.height,not x.no_audio)
