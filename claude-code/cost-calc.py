#!/usr/bin/env python3
import sys, json

jsonl_path = sys.argv[1]
seen, ti, tc, tr, to = set(), 0, 0, 0, 0

try:
    with open(jsonl_path) as f:
        for line in f:
            try:
                o = json.loads(line)
                if o.get('type') == 'assistant' and 'message' in o:
                    mid = o['message'].get('id', '')
                    if mid and mid not in seen:
                        seen.add(mid)
                        u = o['message'].get('usage', {})
                        ti += u.get('input_tokens', 0)
                        tc += u.get('cache_creation_input_tokens', 0)
                        tr += u.get('cache_read_input_tokens', 0)
                        to += u.get('output_tokens', 0)
            except:
                pass
except:
    pass

print(f'{(ti*3 + tc*3.75 + tr*0.30 + to*15)/1e6:.4f}')
