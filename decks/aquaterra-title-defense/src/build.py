import base64,json,os,re,sys
sys.path.insert(0,os.path.dirname(__file__))
import slides,data
D=os.path.dirname(os.path.abspath(__file__));IMG=os.path.join(D,'..','img')
def b64(p,m):return f"data:{m};base64,"+base64.b64encode(open(os.path.join(IMG,p),'rb').read()).decode()
css=open(os.path.join(D,'deck.css')).read()
for k in['pf','pfi','in']:css=css.replace('{{FONT:%s}}'%k,b64(k+'.woff2','font/woff2'))
html="\n".join(slides.S)
_n=[-1]
def _lab(m):
    if m.group(1).startswith('B'):return m.group(0)
    _n[0]+=1;return 'data-label="%02d"'%_n[0]
html=re.sub(r'data-label="([^"]+)"',_lab,html)
for k in['hero','bangka','reef','deep']:html=html.replace('{{IMG:%s}}'%k,b64(k+'.jpg','image/jpeg'))
assert '{{' not in html, re.findall(r'\{\{[^}]*\}\}',html)[:3]
chrome='''<div id="progress"></div>
<button class="back" id="back" style="display:none">← Back</button>
<div id="notes"><div class="lab" id="nlab">Speaker notes</div><div id="ntxt"></div></div>
<div id="bar"><div id="seclab"></div><div id="steps"></div><div class="sp"></div>
<button class="kb q" id="kq" title="Panel questions for this section"><b>Q</b>Panel asks</button>
<button class="kb r" id="kr" title="References"><b>R</b>Refs</button>
<button class="kb" id="kn" title="Speaker notes"><b>N</b></button><button class="kb" id="kb" title="Slide menu"><b>B</b></button><button class="kb" id="kf" title="Fullscreen"><b>F</b></button><button class="kb" id="kh"><b>?</b></button>
<button class="nav" id="pv" aria-label="Previous">‹</button><div id="counter"></div><button class="nav" id="nx" aria-label="Next">›</button></div>
<div class="ov" id="qov"><div class="drawer"><button class="x">✕</button><div class="kick" style="color:var(--coral)">Panel might ask</div><div class="dh" id="qtitle"></div><div id="qbody"></div></div></div>
<div class="ov" id="rov"><div class="drawer"><button class="x">✕</button><div class="kick">References</div><div class="dh">Sources for this section</div><div id="rbody"></div></div></div>
<div class="ov" id="menu"><div class="modal"><button class="x">✕</button><div class="kick">Jump to slide</div><div class="dh">AquaTerra · title defense</div><div id="mgrid"></div></div></div>
<div class="ov" id="help"><div class="modal" style="width:900px"><button class="x">✕</button><div class="kick">Keyboard</div><div class="dh">Controls</div><div class="keys">
<b>→ / Space</b><span>next step or slide</span><b>←</b><span>previous</span><b>Home / End</b><span>first / last main slide</span><b>F</b><span>fullscreen</span><b>N</b><span>speaker notes</span>
<b>Q</b><span>panel questions for this section</span><b>R</b><span>references</span><b>B / G</b><span>slide menu and backups</span><b>M</b><span>ambient motion on / off</span><b>Esc</b><span>close panels</span></div></div></div>
<div id="toast"></div>'''
AMB='<div id="amb"><div class="par" data-d="14" style="inset:0"><div class="ray"></div><div class="ray"></div><div class="ray"></div></div><div class="caus par" data-d="8"></div><svg class="wave" viewBox="0 0 3840 150" preserveAspectRatio="none"><path d="'+''.join(f'{"M" if i==0 else "Q"}' for i in range(0))+'M0,70 '+' '.join(f'Q{i*480+240},{30 if i%2 else 110} {i*480+480},70' for i in range(8))+' V150 H0Z" fill="#bfeef2"/></svg><canvas id="fish" width="1920" height="1080"></canvas></div>'
js=open(os.path.join(D,'deck.js')).read()
dat="const QA=%s,RT=%s,QB=%s,PSA=%s,APA=%s;"%tuple(json.dumps(x,ensure_ascii=False) for x in(data.QA,data.RT,data.QB,data.PSA,slides.APA))
out=f'''<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>AquaTerra: Forecasting Municipal Fish Landing Shortfalls and Estimating Gross Landing Value at Risk in Selected Philippine Coastal Provinces</title><style>{css}</style></head><body>
<div id="stage">{AMB}{html}{chrome}</div>
<script>{dat}
{js}</script></body></html>'''
p=os.path.join(D,'..','AquaTerra_Title_Defense.html');open(p,'w').write(out);print(p,round(len(out)/1e6,2),'MB')
