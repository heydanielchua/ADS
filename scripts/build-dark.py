#!/usr/bin/env python3
"""Regenerate tokens/semantic-dark.json from semantic-light.json via the symmetry rule.
Neutrals: dark = grey(105 - light), white<->black. Chromatic: dark = step(110 - light)."""
import json, os
from collections import OrderedDict

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
prim = json.load(open(os.path.join(BASE, 'tokens', 'colors.json')))['color']
light = json.load(open(os.path.join(BASE, 'tokens', 'semantic-light.json')))['semantic']

def nearest(steps, t): return min(steps, key=lambda s: abs(s - t))

def mirror_ref(ref):
    parts = ref.strip('{}').split('.')
    if parts[:1] != ['color']:
        return ref
    body = parts[1:]
    if body == ['white']: return '{color.black}'
    if body == ['black']: return '{color.white}'
    if len(body) == 2:
        fam, step = body[0], int(body[1])
        if fam == 'grey':
            return '{color.grey.%d}' % (105 - step)
        steps = [int(k) for k in prim[fam].keys()] if fam in prim and '$value' not in prim[fam] else []
        t = 110 - step
        return '{color.%s.%d}' % (fam, nearest(steps, t) if steps else t)
    return ref

def build(node):
    if isinstance(node, dict):
        if '$value' in node and node.get('$type') == 'color':
            nd = OrderedDict(node)
            v = node['$value']
            nd['$value'] = mirror_ref(v) if isinstance(v, str) and v.startswith('{') else v
            return nd
        return OrderedDict((k, build(v)) for k, v in node.items())
    return node

out = OrderedDict([('$mode', 'dark'), ('semantic', build(light))])
json.dump(out, open(os.path.join(BASE, 'tokens', 'semantic-dark.json'), 'w'), indent=2)
print('Regenerated tokens/semantic-dark.json')
