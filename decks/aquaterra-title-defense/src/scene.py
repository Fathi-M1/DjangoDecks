# v8 illustrated ocean scene (inline SVG, offline). Art lives at edges/bottom; slide text sits on a frosted sheet above it.
import random
random.seed(8)
def kelp(x,h,w=26,c="#1fbf8f",d=0):
    # wavy strand from (x,1080) up h px
    pts=[];n=6
    p=f"M{x},1080 "
    for i in range(1,n+1):
        y=1080-h*i/n;dx=(w if i%2 else -w)
        p+=f"Q{x+dx},{y+h/n/2} {x},{y} "
    return f'<path class="kelp" style="animation-delay:{-d}s;animation-duration:{6+d%4}s" d="{p}" fill="none" stroke="{c}" stroke-width="14" stroke-linecap="round" opacity=".9"/>'
def branch(x,y,s,c,ang=0):
    # branching coral: trunk + 2 levels
    out=[]
    def br(x0,y0,l,a,depth):
        import math
        x1=x0+l*math.sin(a);y1=y0-l*math.cos(a)
        out.append(f'<line x1="{x0:.0f}" y1="{y0:.0f}" x2="{x1:.0f}" y2="{y1:.0f}" stroke="{c}" stroke-width="{4+depth*5}" stroke-linecap="round"/>')
        if depth>0:
            br(x1,y1,l*.72,a-.5,depth-1);br(x1,y1,l*.72,a+.45,depth-1)
    br(x,y,60*s,ang,3)
    return f'<g class="cor">{"".join(out)}</g>'
def fan(x,y,r,c):
    import math
    ls="".join(f'<line x1="{x}" y1="{y}" x2="{x+r*math.cos(a):.0f}" y2="{y-r*math.sin(a):.0f}" stroke="{c}" stroke-width="3"/>' for a in [math.pi*(0.12+0.76*i/12) for i in range(13)])
    return f'<g opacity=".95">{ls}<path d="M{x-r},{y} A{r},{r} 0 0 1 {x+r},{y}" fill="{c}" opacity=".35"/></g>'
def brain(x,y,r,c,c2):
    return f'<ellipse cx="{x}" cy="{y}" rx="{r}" ry="{r*.7:.0f}" fill="{c}"/><path d="M{x-r*.7:.0f},{y} q{r*.35:.0f},-{r*.4:.0f} {r*.7:.0f},0 t{r*.7:.0f},0" fill="none" stroke="{c2}" stroke-width="4" stroke-linecap="round"/><path d="M{x-r*.5:.0f},{y-r*.3:.0f} q{r*.25:.0f},-{r*.25:.0f} {r*.5:.0f},0 t{r*.5:.0f},0" fill="none" stroke="{c2}" stroke-width="4" stroke-linecap="round"/>'
def anemone(x,y,c):
    import math
    t="".join(f'<line class="ten" x1="{x}" y1="{y}" x2="{x+38*math.cos(a):.0f}" y2="{y-38*math.sin(a):.0f}" stroke="{c}" stroke-width="7" stroke-linecap="round"/>' for a in [math.pi*(0.1+0.8*i/9) for i in range(10)])
    return f'<g class="anem">{t}</g>'
# far + mid seafloor silhouettes (full width, mostly behind the sheet; visible in the bottom band)
far='<path d="M0,900 C200,860 320,930 520,890 S900,850 1100,900 S1500,860 1700,890 S1880,870 1920,880 V1080 H0Z" fill="#0b3a74" opacity=".9"/>'
mid='<path d="M0,980 C160,940 300,1000 470,965 S820,940 980,985 S1380,950 1560,975 S1820,950 1920,965 V1080 H0Z" fill="#0e4c8c"/>'
sand='<path d="M0,1040 C300,1020 600,1050 960,1035 S1600,1020 1920,1040 V1080 H0Z" fill="#2a6aa8"/>'
rocks='<ellipse cx="120" cy="1050" rx="150" ry="70" fill="#123d6e"/><ellipse cx="300" cy="1068" rx="110" ry="50" fill="#16477e"/><ellipse cx="1810" cy="1050" rx="170" ry="75" fill="#123d6e"/><ellipse cx="1600" cy="1070" rx="110" ry="45" fill="#16477e"/>'
L=[branch(70,1040,1.5,"#ff5fa2"),branch(210,1060,1.1,"#9b6bff",.2),fan(330,1050,90,"#ff8a3d"),brain(150,1060,60,"#ffb347","#e07a1f"),anemone(420,1068,"#ff7ab6"),branch(30,960,.9,"#ff8a3d",-.3)]
R=[branch(1850,1040,1.5,"#9b6bff"),branch(1710,1060,1.15,"#ff5fa2",-.2),fan(1590,1050,95,"#2fd3e0"),brain(1780,1065,58,"#ff8fbf","#d4507f"),anemone(1500,1070,"#ffb347"),branch(1895,950,.9,"#ff5fa2",.3)]
K=[kelp(18,560,22,"#1fbf8f",1),kelp(48,420,18,"#3fd39a",3),kelp(250,300,20,"#17a67c",2),kelp(1902,600,22,"#1fbf8f",2.5),kelp(1872,440,18,"#3fd39a",.5),kelp(1660,320,20,"#17a67c",3.5),kelp(620,170,16,"#17a67c",1.5),kelp(1300,180,16,"#1fbf8f",4)]
turtle='''<svg id="turtle" width="150" height="138" viewBox="-130 -120 260 240"><g class="tw"><g transform="scale(.9)">
<path class="fl fl1" d="M40,-30 C10,-95 -40,-110 -60,-95 C-40,-70 -10,-45 20,-25Z" fill="#5fbf8a"/>
<path class="fl fl2" d="M40,30 C10,95 -40,110 -60,95 C-40,70 -10,45 20,25Z" fill="#4aa877"/>
<path d="M-70,-12 C-95,-22 -110,-10 -112,0 C-110,10 -95,22 -70,12Z" fill="#4aa877"/>
<ellipse cx="0" cy="0" rx="85" ry="62" fill="#7a5a2e"/>
<ellipse cx="0" cy="0" rx="76" ry="54" fill="#a8783c"/>
<path d="M-40,-30 L0,-44 L40,-30 L40,30 L0,44 L-40,30Z M-40,-30 L-70,0 L-40,30 M40,-30 L72,0 L40,30 M0,-44 V44 M-40,0 H40" fill="none" stroke="#6b4a22" stroke-width="5" stroke-linejoin="round"/>
<ellipse cx="112" cy="0" rx="34" ry="26" fill="#6cc796"/><circle cx="125" cy="-9" r="5" fill="#0b2a3c"/><circle cx="127" cy="-11" r="1.6" fill="#fff"/>
</g></g></svg>'''
def jelly(x,y,c,s=1,d=0):
    tent="".join(f'<path d="M{-24+i*12},0 q6,30 0,60 t0,60" fill="none" stroke="{c}" stroke-width="3" opacity=".7"/>' for i in range(5))
    return f'<svg class="jel" style="left:{x-50}px;top:{y-60}px;animation-delay:{-d}s" width="100" height="200" viewBox="-50 -60 100 200"><g transform="scale({s})"><path d="M-36,0 C-36,-46 36,-46 36,0 Q24,8 12,0 Q0,8 -12,0 Q-24,8 -36,0Z" fill="{c}" opacity=".75"/><ellipse cx="-10" cy="-22" rx="10" ry="6" fill="#fff" opacity=".45"/>{tent}</g></svg>'
rays="".join(f'<div class="ray" style="left:{x}px;width:{w}px;transform:rotate({r}deg);animation-duration:{d}s;animation-delay:-{d/3:.0f}s"></div>' for x,w,r,d in [(250,220,22,18),(640,160,16,23),(980,280,12,20),(1320,180,8,26),(1620,240,4,21),(1820,140,2,28)])
AMB=f'''<div id="amb"><div class="glow"></div>
<div class="par" data-d="10" style="inset:0">{rays}</div>
<div class="caus par" data-d="6"></div>
<svg class="floor" width="1920" height="1080" viewBox="0 0 1920 1080">{far}{mid}</svg>
{jelly(1885,330,"#ff8fd1",.9,0)}{jelly(34,560,"#b18cff",.75,6)}
<svg class="reef" width="1920" height="1080" viewBox="0 0 1920 1080">{sand}{rocks}{''.join(K)}{''.join(L)}{''.join(R)}</svg>
{turtle}
<canvas id="fish" width="1920" height="1080"></canvas>
<div class="surf"></div></div>'''
