#!/usr/bin/env python3
"""Create original 48kHz WAV foley with deterministic time-stamped event cues."""
from __future__ import annotations
import argparse
from array import array
import json,math,struct,wave
from pathlib import Path

ROOT=Path(__file__).resolve().parents[2]
TYPES={'pop','click','thump','whoosh','riser','success','tick'}

def noise(seed):
    return (1664525*seed+1013904223)&0xffffffff

def synth(cues:dict,output:Path)->Path:
    sr=int(cues.get('sample_rate',48000));duration=float(cues['duration'])
    if not 8000<=sr<=96000 or not 0<duration<=600:raise ValueError('Bad sample rate or duration')
    N=round(sr*duration);data=array('f',[0.0])*N
    for index,event in enumerate(cues['cues']):
        at=float(event['at']);kind=event['type'];gain=float(event.get('gain',0.4))
        if kind not in TYPES or not 0<=at<=duration or not 0<=gain<=1:raise ValueError('Invalid sound cue '+str(event))
        start=round(max(0,at-.015)*sr)
        length=round(sr*(.35 if kind in {'whoosh','riser','success'} else .20 if kind=='thump' else .12))
        state=0xF00D1234+index*17
        for j in range(min(length,max(0,N-start))):
            u=j/sr;phase=j/length
            state=noise(state);white=state/2147483648-1
            if kind in {'pop','click','tick'}:
                frequency={'pop':440,'click':1350,'tick':850}[kind]
                env=math.exp(-u*{'pop':29,'click':63,'tick':50}[kind]);s=math.sin(2*math.pi*frequency*u)*env
            elif kind=='thump':
                env=math.exp(-u*24);s=math.sin(2*math.pi*(72*u+110*u*u))*env
            elif kind=='whoosh':
                env=math.sin(math.pi*phase)**2;s=white*.55*env
            elif kind=='riser':
                env=phase**2;s=white*.25*env+math.sin(2*math.pi*(200*u+300*u*u))*.28*env
            else:
                env=math.exp(-u*12);s=(math.sin(2*math.pi*660*u)+.45*math.sin(2*math.pi*880*u))*env*.4
            data[start+j] += s*gain*.65
    peak=max(max(abs(v) for v in data),1e-9);scale=min(1,.86/peak)
    output=Path(output).expanduser().resolve();output.parent.mkdir(parents=True,exist_ok=True)
    with wave.open(str(output),'wb') as file:
        file.setnchannels(1);file.setsampwidth(2);file.setframerate(sr)
        # Chunk to avoid a giant list of Python integer samples.
        for i in range(0,N,16384):
            values=[int(max(-32768,min(32767,round(x*scale*32767)))) for x in data[i:i+16384]]
            file.writeframesraw(struct.pack('<'+'h'*len(values),*values))
    print(f'Generated {output} ({duration:.2f}s, {len(cues["cues"])} cues)')
    return output
if __name__=='__main__':
    a=argparse.ArgumentParser(description=__doc__)
    a.add_argument('--cues',type=Path,default=ROOT/'instagram-reels/examples/demo/sfx.json')
    a.add_argument('--output',type=Path,default=ROOT/'output/effects.wav')
    x=a.parse_args();synth(json.loads(x.cues.read_text(encoding='utf-8')),x.output)
