import json, re, os
import os
base=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
def load(n): return json.load(open(f'{base}/tokens/{n}'))

prim=load('colors.json')['color']
light=load('semantic-light.json')['semantic']
dark=load('semantic-dark.json')['semantic']
typ=load('typography.json'); spc=load('spacing.json'); ico=load('icon.json'); shd=load('shadow.json')

def kebab(*parts): return '-'.join(str(p) for p in parts)

def prim_vars():
    out=[]
    for fam,v in prim.items():
        if '$value' in v: out.append((f'--color-{fam}', v['$value']))
        else:
            for step,info in v.items(): out.append((f'--color-{fam}-{step}', info['$value']))
    return out

def ref_to_var(ref):
    p=ref.strip('{}').split('.')[1:]
    return 'var(--color-' + '-'.join(p) + ')'

def sem_vars(sem):
    out=[]
    def walk(d,pfx=''):
        for k,v in d.items():
            if isinstance(v,dict) and '$value' in v:
                out.append((f'--{pfx}{k}', ref_to_var(v['$value'])))
            elif isinstance(v,dict): walk(v,pfx+k+'-')
    walk(sem)
    return out

def scale_vars(node, prefix):
    out=[]
    def walk(d,pfx=''):
        for k,v in d.items():
            if isinstance(v,dict) and '$value' in v:
                val=v['$value']
                if isinstance(val,dict):  # composite (typography textStyle) - skip in CSS vars
                    continue
                out.append((f'--{prefix}-{pfx}{k}'.replace('--'+prefix+'-','--'+prefix+'-'), val))
            elif isinstance(v,dict): walk(v,pfx+k+'-')
    walk(node)
    return out

lines=['/* AUTO-GENERATED from /tokens. Do not edit by hand. */','']
# :root - primitives + scales + light semantic
lines.append(':root {')
lines.append('  /* primitives */')
for k,val in prim_vars(): lines.append(f'  {k}: {val};')
lines.append('  /* typography */')
for grp in ['family','weight','size','lineHeight']:
    for k,info in typ['font'][grp].items():
        lines.append(f'  --font-{("size" if grp=="size" else "lh" if grp=="lineHeight" else grp)}-{k}: {info["$value"]};')
lines.append('  /* spacing & radius */')
for k,info in spc['spacing'].items(): lines.append(f'  --spacing-{k}: {info["$value"]};')
for k,info in spc['radius'].items():
    if '$value' in info: lines.append(f'  --radius-{k}: {info["$value"]};')
lines.append('  /* icon sizes */')
for k,info in ico['icon']['size'].items(): lines.append(f'  --icon-size-{k}: {info["$value"]};')
lines.append('  /* shadow */')
sv=shd['shadow']['default']['$value']
lines.append(f'  --shadow-default: {sv["offsetX"]} {sv["offsetY"]} {sv["blur"]} {sv["color"]};')
lines.append('  /* semantic (light) */')
for k,val in sem_vars(light): lines.append(f'  {k}: {val};')
lines.append('}')
lines.append('')
lines.append('[data-theme="dark"] {')
lines.append('  /* semantic (dark) - derived by symmetry */')
for k,val in sem_vars(dark): lines.append(f'  {k}: {val};')
lines.append('}')

os.makedirs(f'{base}/dist',exist_ok=True)
open(f'{base}/dist/tokens.css','w').write('\n'.join(lines)+'\n')
print('Wrote dist/tokens.css')
print('  primitive vars:', len(prim_vars()))
print('  semantic vars :', len(sem_vars(light)), '(x2 themes)')
