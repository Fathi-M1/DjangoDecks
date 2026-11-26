# Two-slide animated data-flow pipeline (Section V overview)
import math
def hd(num,kick,h):
    return f'<div class="hd"><div class="num">{num}</div><div><div class="kick">{kick}</div><h2 style="margin-top:12px">{h}</h2></div></div>'
def sh(n,lab,line): return f'<div class="sh"><b><i>{n}</i>{lab}</b><span>{line}</span></div>'
def notes(t): return f'<aside class="notes">{t.strip()}</aside>'
def T(x,y,s,size=13,fill="#3c5a6b",w=500,anchor="start",cls="",d=None,extra=""):
    st=f' style="--d:{d}s"' if d is not None else ''
    c=f' class="{cls}"' if cls else ''
    return f'<text x="{x}" y="{y}" font-size="{size}" font-weight="{w}" fill="{fill}" text-anchor="{anchor}"{c}{st}{extra}>{s}</text>'
ILL='<span class="ill" style="position:absolute;right:16px;top:14px;font-size:11px;padding:4px 7px">ILLUSTRATIVE</span>'
# ================= SLIDE A =================
SRC=[("#0e8f86","PSA OpenSTAT","Landings and value by province × species × quarter","Palawan · snapper · 2025 Q4 → 1,220.96 mt","psa"),
("#1f9d6b","Landsat satellite imagery","Mangrove cover derived from 30 m imagery, by year","e.g. Province A, 2020 → 12,950 ha","gmw"),
("#2f7fd6","NASA IMERG","Rainfall from satellites","e.g. → 610 mm in the quarter","rain"),
("#d9822b","NOAA OISST","Sea surface temperature","e.g. → 27.9 °C quarterly mean","sst"),
("#8a5bd6","NOAA IBTrACS","Typhoon tracks","e.g. → 2 typhoons passed near, prior quarter","typh")]
ICON={"psa":'<rect x="8" y="26" width="7" height="12" rx="1.5"/><rect x="19" y="18" width="7" height="20" rx="1.5"/><rect x="30" y="10" width="7" height="28" rx="1.5"/>',
"gmw":'<path d="M23 8 C12 10 9 20 14 26 C18 30 28 30 32 26 C37 20 34 10 23 8Z"/><path d="M23 26 V38 M23 32 L16 40 M23 32 L30 40" stroke="currentColor" stroke-width="2.5" fill="none"/>',
"rain":'<path d="M12 22 C10 14 18 9 24 12 C27 6 37 8 37 16 C42 17 42 24 36 24 H14 C10 24 10 22 12 22Z"/><path d="M15 30 l-2 6 M23 30 l-2 6 M31 30 l-2 6" stroke="currentColor" stroke-width="2.5"/>',
"sst":'<path d="M19 8 a4 4 0 0 1 8 0 v18 a8 8 0 1 1 -8 0Z"/><path d="M6 40 q5 -4 10 0 t10 0 t10 0" stroke="currentColor" stroke-width="2.5" fill="none"/>',
"typh":'<path d="M23 23 m-4 0 a4 4 0 1 0 8 0 a4 4 0 1 0 -8 0 M23 9 C33 9 38 15 37 21 M23 37 C13 37 8 31 9 25 M9 25 C9 17 15 13 21 13 M37 21 C37 29 31 33 25 33" stroke="currentColor" stroke-width="3" fill="none"/>'}
srch=""
for i,(c,n,w,sm,ic) in enumerate(SRC):
    srch+=f'<div class="src" style="--c:{c}"><svg width="46" height="46" viewBox="0 0 46 46" style="color:{c};fill:{c};flex:none">{ICON[ic]}</svg><div><b>{n}</b><small>{w}</small><code>{sm}</code></div></div>'
COLS=[("Province × fish","#a9bfc6",150),("Year","#a9bfc6",56),("Season","#a9bfc6",58),("Landings (mt)","#0e8f86",84),("Lag-4 landings","#0e8f86",80),
("Rain (mm)","#2f7fd6",66),("SST (°C)","#d9822b",58),("Mangrove (ha)","#1f9d6b",90),("Typhoons prior Q","#8a5bd6",90),("Price (₱/kg)","#0e8f86",78)]
E=["⋮"]*10
ROWS=[("train",["A · Cat 1","2002","Q1","412.0","—","610","27.9","12,950","0","168"]),
("train",["B · Cat 2","2002","Q1","96.4","—","540","28.1","3,120","1","241"]),
("train",E),
("train",["A · Cat 1","2019","Q4","535.2","498.7","980","28.6","12,410","2","176"]),
("train",["B · Cat 2","2019","Q4","118.9","121.3","1,020","28.8","3,050","2","255"]),
("tune",["A · Cat 1","2020","Q1","401.3","452.6","400","28.0","12,390","0","178"]),
("tune",E),
("tune",["B · Cat 2","2022","Q4","108.2","115.0","1,110","28.9","2,990","3","262"]),
("test",["A · Cat 1","2023","Q1","388.5","395.1","560","28.2","12,330","0","180"]),
("test",E),
("test",["B · Cat 2","2026","Q3","121.7","119.4","890","29.1","2,960","1","270"])]
th="".join(f'<div style="width:{w}px;--c:{c}">{n}</div>' for n,c,w in COLS)
tr=""
for r,(g,vals) in enumerate(ROWS):
    cells="".join(f'<div class="seq" style="width:{COLS[k][2]}px;--d:{0.35+k*0.09+r*0.03:.2f}s">{v}</div>' for k,v in enumerate(vals))
    tr+=f'<div class="ftr g-{g}{" ell" if vals is E else ""}">{cells}</div>'
# band geometry (relative to stage tops at 250): header 56, rows 40, split gaps 16
BANDS=[("train","Train","earliest quarters, e.g. 2002–2019. The model learns here.",134,200),
("tune","Tune","next quarters, e.g. 2020–2022. Settings are chosen here.",350,120),
("test","Test","latest quarters, e.g. 2023 onward. Locked: never seen until the final check.",486,120)]
bh="".join(f'<div class="band b-{k}" style="top:{t}px;height:{h}px"><b>{n}</b><span>{x}</span></div>' for k,n,x,t,h in BANDS)
# connector paths: card right edge -> table left edge
pa=""
for i in range(5):
    y0=250+78+50+i*110; y1=250+78+56+30+i*82
    pa+=f'<path class="fpath" data-to="2" data-c="{SRC[i][0]}" d="M540,{y0} C590,{y0} 590,{y1} 640,{y1}"/>'
for k,t,h in [(0,134,200),(1,350,120),(2,486,120)]:
    y=250+t+h/2;pa+=f'<path class="fpath" data-to="3" data-c="{["#0e8f86","#6f8b99","#d9822b"][k]}" d="M1474,{y} H1508"/>'
A=f'''<section class="slide uw flow" id="s-flowA" data-label="06" data-title="IV · Data flow 1/2 · Inputs → Split" data-sec="3" data-steps="2" data-q="algo">
<div class="rays" style="opacity:.55"></div>
{hd("04","IV · Algorithm Justification · data flow 1 of 2","Five sources become one <em>quarterly table</em>.")}
<button class="abs btn fplay" style="right:110px;top:118px">▶ Play the flow</button>
<div class="abs stg" id="fa-st1" data-st="1" style="left:110px;top:250px;width:430px;height:650px">{sh(1,"Inputs","Five public sources. Each adds one piece.")}<div style="margin-top:16px">{srch}</div></div>
<div class="abs stg" id="fa-st2" data-st="2" style="left:640px;top:250px;width:830px;height:690px">{sh(2,"Align","Matched into one table: one row = province × fish category × quarter.")}
 <span class="ill" style="position:absolute;right:0;top:0;font-size:11px;padding:4px 7px">ILLUSTRATIVE VALUES</span>
 <div id="fa-tab"><div class="fth">{th}</div>{tr}</div>
 <div class="small" style="position:absolute;left:0;top:640px;font-size:15px;width:830px">Lag-4 = same quarter last year (blank in the first year, so those rows drop) · price is carried for valuation only, never as a predictor</div></div>
<div class="abs stg" id="fa-st3" data-st="3" style="left:1510px;top:250px;width:300px;height:690px">{sh(3,"Time split","Split by time, not at random.")}{bh}
 <div style="position:absolute;left:0;top:626px"><button class="try" data-go="s-eval">Try the split slider · IV.3 →</button></div></div>
<svg class="abs flowsvg" width="1920" height="1080" style="left:0;top:0">{pa}<g class="parts"></g></svg>
{notes("""Here is the whole pipeline, from raw data to pesos, in two slides.
[Stage 1] We start with five public sources. PSA OpenSTAT gives quarterly landings, and the value records we use for prices, for each province and fish category. For example, Palawan snapper in the fourth quarter of 2025 was about 1,221 metric tons. Landsat satellite imagery gives mangrove cover: we derive the mangrove area for each province and year from the images. NASA IMERG gives rainfall. NOAA OISST gives sea surface temperature. NOAA IBTrACS gives typhoon tracks.
[→ Stage 2] We line everything up into one table. Each row is one province, one fish category, one quarter. The columns are that quarter's landings, landings in the same quarter last year, the season, rainfall, sea temperature, mangrove area, recent typhoons, and the price. Price is only carried along for the money step at the end; it is never used to predict landings.
[→ Stage 3] Then we split the rows by time, not at random. The earliest quarters train the model, the next quarters tune it, and the latest quarters are locked away as the test. The model never sees them until the final check. The years shown are an example.""")}
</section>'''
# ================= SLIDE B =================
POS={4:(110,250),5:(710,250),6:(1310,250),7:(110,620),8:(710,620),9:(1310,620)}
def panel(n,lab,line,svg,links):
    x,y=POS[n];lk="".join(f'<button class="try" data-go="{g}">{t} →</button>' for g,t in links)
    return f'<div class="abs stg pnl" data-st="{n}" style="left:{x}px;top:{y}px">{ILL}{sh(n,lab,line)}<svg class="pv" width="464" height="206" viewBox="0 0 464 206">{svg}</svg><div class="lk">{lk}</div></div>'
# --- 4 RF
rf=""
for i in range(5): rf+=f'<rect class="seq" style="--d:{0.1+i*0.06:.2f}s" x="0" y="{34+i*16}" width="56" height="11" rx="3" fill="#c4ebe5"/>'
rf+=T(28,130,"train rows",11,"#6f8b99",600,"middle")
rf+='<path d="M62,70 H84" stroke="#a9bfc6" stroke-width="2.5"/><path d="M84,65 l7,5 l-7,5Z" fill="#a9bfc6"/>'
for k,(cx,s) in enumerate([(108,1),(132,1.25),(156,1)]):
    rf+=f'<g class="seq" style="--d:{0.4+k*0.12:.2f}s"><path d="M{cx},{70-28*s} L{cx+14*s},{70} L{cx-14*s},{70}Z" fill="#1f9d6b"/><path d="M{cx},{58-22*s} L{cx+11*s},{82-22*s} L{cx-11*s},{82-22*s}Z" fill="#2fb383"/><rect x="{cx-2}" y="70" width="4" height="12" fill="#6b5a3a"/></g>'
rf+=T(132,100,"forest",11,"#6f8b99",600,"middle")
rf+='<path d="M172,70 H190" stroke="#a9bfc6" stroke-width="2.5"/><path d="M190,65 l7,5 l-7,5Z" fill="#a9bfc6"/>'
IMP=[("lagged landings",.92),("season",.78),("mangrove",.55),("SST",.44),("typhoons",.27),("rainfall",.18)]
for i,(n,v) in enumerate(IMP):
    y=14+i*24;top=i<4
    g=f'<g{"" if top else " class=\"fadeo\" style=\"--d:1.7s\""}>'
    g+=T(296,y+12,n,12.5,"#0b2a3c" if top else "#3c5a6b",600,"end")
    g+=f'<rect x="304" y="{y+1}" width="{v*112:.0f}" height="15" rx="3" fill="{"#0e8f86" if top else "#a5d8d0"}" class="grow" style="--d:{0.8+i*0.08:.2f}s"/>'
    if top:g+=T(304+v*112+6,y+13,"✓",13,"#0e8f86",800,cls="seq",d=1.9)
    rf+=g+'</g>'
rf+=f'<g class="seq" style="--d:2.1s"><rect x="40" y="160" width="384" height="30" rx="15" fill="#fff1d6" stroke="#d9822b" stroke-width="1.5"/>'+T(232,180,"picks predictors, not predictions",15,"#7a4a06",700,"middle")+'</g>'
rf+=T(232,203,"top 4 pass to GAMM · weaker ones are dropped",11.5,"#6f8b99",500,"middle")
# --- 5 GAMM
N=12
sea=[[-30,40,15,-25][t%4] for t in range(N)]
smo=[12*math.sin(t/1.7)-1.2*t for t in range(N)]
eff=[18]*N
def pth(vals,x0,w,y0,sc,mid):
    return "M"+" L".join(f"{x0+t*w/(N-1):.1f},{mid-v*sc:.1f}" for t,v in enumerate(vals))
g=""
g+=T(0,12,"seasonal curve · s(season)",11.5,"#0e8f86",700,cls="seq",d=0.2)
g+=f'<path class="draw" style="--d:.3s" d="{pth(sea,0,190,0,0.42,40)}" stroke="#0e8f86" stroke-width="2.5" fill="none"/>'
g+=T(95,72,"+",18,"#6f8b99",700,"middle",cls="seq",d=0.9)
g+=T(0,88,"smooth curves · lagged, mangrove, SST",11.5,"#8a5bd6",700,cls="seq",d=1.0)
for k,(c,ph) in enumerate([("#8a5bd6",0),("#1f9d6b",1.2),("#d9822b",2.4)]):
    v=[9*math.sin(t/1.7+ph)-0.4*t for t in range(N)]
    g+=f'<path class="draw" style="--d:{1.05+k*0.1:.2f}s" d="{pth(v,0,190,0,0.9,112)}" stroke="{c}" stroke-width="2" fill="none"/>'
g+=T(95,142,"+",18,"#6f8b99",700,"middle",cls="seq",d=1.6)
g+=T(0,158,"province / category effect",11.5,"#b07800",700,cls="seq",d=1.7)
for k,(lv,lab) in enumerate([(0,"A"),(-8,"B"),(7,"C")]):
    g+=f'<g class="seq" style="--d:{1.75+k*0.08:.2f}s"><rect x="{k*64}" y="{176-lv}" width="54" height="6" rx="3" fill="#f2b53a"/>'+T(k*64+27,200,"Prov "+lab,10.5,"#6f8b99",600,"middle")+'</g>'
g+=T(214,108,"=",26,"#0b2a3c",700,"middle",cls="seq",d=2.1)
g+='<rect x="238" y="8" width="226" height="186" rx="10" fill="#f3fbf9"/>'
base=100
s1=[base+sea[t] for t in range(N)];s2=[s1[t]+smo[t] for t in range(N)];s3=[s2[t]+eff[t] for t in range(N)]
def cp(v): return "M"+" L".join(f"{246+t*206/(N-1):.1f},{190-(x-40)*1.05:.1f}" for t,x in enumerate(v))
g+=f'<path class="draw" style="--d:.6s" d="{cp(s1)}" stroke="#0e8f86" stroke-width="1.6" stroke-dasharray="4 4" fill="none" opacity=".55"/>'
g+=f'<path class="draw" style="--d:1.4s" d="{cp(s2)}" stroke="#8a5bd6" stroke-width="1.8" fill="none" opacity=".55"/>'
g+=f'<path class="draw" style="--d:2.2s;--len:900" d="{cp(s3)}" stroke="#0b2a3c" stroke-width="3.5" fill="none"/>'
g+=T(452,26,"sum = forecast line",12,"#0b2a3c",800,"end",cls="seq",d=2.6)
# --- 6 FORECAST
hist=[s3[t]*3.9 for t in range(N)]  # ~ mt
fc=640;lo=560;hi=720
def fx(t): return 10+t*232/12
def fy(v): return 190-(v-200)*0.27
f='<rect x="0" y="6" width="282" height="196" rx="10" fill="#f6fbfa"/>'
f+=f'<path class="draw" style="--d:.2s" d="M'+" L".join(f"{fx(t):.1f},{fy(v):.1f}" for t,v in enumerate(hist))+'" stroke="#0e8f86" stroke-width="2.5" fill="none"/>'
f+=f'<path class="seq" style="--d:1.1s" d="M{fx(11):.1f},{fy(hist[11]):.1f} L{fx(12):.1f},{fy(hi):.1f} L{fx(12):.1f},{fy(lo):.1f}Z" fill="#d9822b" opacity=".22"/>'
f+=f'<path class="seq" style="--d:1.1s" d="M{fx(12)-6:.1f},{fy(hi):.1f} h12 M{fx(12):.1f},{fy(hi):.1f} V{fy(lo):.1f} M{fx(12)-6:.1f},{fy(lo):.1f} h12" stroke="#d9822b" stroke-width="2"/>'
f+=f'<path class="seq" style="--d:1.2s" d="M{fx(12):.1f},{fy(fc)-9:.1f} l9,9 l-9,9 l-9,-9Z" fill="#d9822b"/>'
f+=T(fx(12)-12,fy(hi)-8,"640 mt (560–720)",12,"#d9822b",800,"end",cls="seq",d=1.3)
f+=T(10,22,"Prov A · Cat 1 · history → next quarter",11,"#6f8b99",600)
f+=T(296,20,"next quarter, all combos",11,"#6f8b99",700)
FC=[("A · Cat 1",640),("B · Cat 2",300),("C · Cat 1",132),("D · Cat 2",190),("A · Cat 3",104)]
for i,(n,v) in enumerate(FC):
    y=44+i*32
    f+=f'<g class="seq" style="--d:{1.4+i*0.1:.2f}s">'+T(296,y,n,13,"#0b2a3c",600)+T(464,y,f"{v} mt",14,"#0b2a3c",800,"end")+T(464,y+13,f"range {round(v*.88)}–{round(v*1.12)}",10.5,"#6f8b99",500,"end")+'</g>'
# --- 7 CHECK
obs=[300,412,365,268,290,398];bl=[340,380,400,240,330,360];wf=[310,405,372,276,300,390]
def cx(t): return 18+t*48
def cy(v): return 176-(v-200)*0.62
c='<rect x="0" y="6" width="270" height="196" rx="10" fill="#fff8ea"/>'+T(10,22,"TEST · locked quarters",11,"#d9822b",800)
c+='<path class="draw" style="--d:.3s" d="M'+" L".join(f"{cx(t)},{cy(v):.1f}" for t,v in enumerate(bl))+'" stroke="#7a8fa0" stroke-width="2.2" stroke-dasharray="6 5" fill="none"/>'
c+='<path class="draw" style="--d:.8s" d="M'+" L".join(f"{cx(t)},{cy(v):.1f}" for t,v in enumerate(wf))+'" stroke="#0e8f86" stroke-width="3" fill="none"/>'
c+="".join(f'<circle cx="{cx(t)}" cy="{cy(v):.1f}" r="4" fill="#6f8b99"/>' for t,v in enumerate(obs))
c+=T(10,198,"● observed  - - baseline  — workflow",10.5,"#3c5a6b",600)
c+=T(372,22,"baseline",11,"#6f8b99",700,"middle")+T(432,22,"workflow",11,"#0e8f86",700,"middle")
for i,(m,a,b) in enumerate([("MAE (mt)","46.3","21.4"),("RMSE (mt)","53.1","27.0"),("MASE","1.08","0.49")]):
    y=56+i*36
    c+=f'<g class="seq" style="--d:{1.2+i*0.15:.2f}s">'+T(284,y,m,12.5,"#0b2a3c",700)+T(372,y,a,15,"#3c5a6b",700,"middle")+T(432,y,b+(" ✓" if i==2 else ""),15,"#0e8f86",800,"middle")+'</g>'
c+=f'<g class="seq" style="--d:1.8s"><rect x="282" y="146" width="182" height="46" rx="10" fill="#e6f7ef"/>'+T(373,165,"MASE &lt; 1 → beats the",12,"#0b5a3a",700,"middle")+T(373,182,"seasonal-naive baseline",12,"#0b5a3a",700,"middle")+'</g>'
# --- 8 SHORTFALL
SF=[("A·C1",820,640),("B·C2",410,300),("C·C1",150,132),("D·C2",260,190),("A·C3",95,104)]
def sy(p): return 170-p*120
s='<line x1="0" x2="464" y1="50" y2="50" stroke="#0b2a3c" stroke-width="2" stroke-dasharray="7 5" class="seq" style="--d:.2s"/>'
s+=T(0,40,"- - usual level for that season (benchmark)",11,"#0b2a3c",700,"start",cls="seq",d=0.2)
for i,(n,b,fv) in enumerate(SF):
    x=14+i*92;p=fv/b
    s+=f'<rect x="{x}" y="{sy(p):.1f}" width="44" height="{170-sy(p):.1f}" rx="4" fill="#0e8f86" class="growy" style="--d:{0.4+i*0.1:.2f}s"/>'
    if fv<b:
        s+=f'<rect x="{x}" y="50" width="44" height="{sy(p)-50:.1f}" fill="url(#hatch)" stroke="#d9822b" stroke-width="1.5" class="seq" style="--d:{1.2+i*0.1:.2f}s"/>'
        s+=T(x+50,max(64,(50+sy(p))/2+5),f"−{b-fv}",12.5,"#d9822b",800,cls="seq",d=1.3+i*0.1)
    else:
        s+=T(x+22,sy(p)-6,"none",11.5,"#0b8a5a",800,"middle",cls="seq",d=1.3)
    s+=T(x+22,188,n,11.5,"#3c5a6b",700,"middle")
s+=T(0,204,"bars = forecast as % of each combo's own benchmark · gap = shortfall (mt)",10.5,"#6f8b99",500)
s='<defs><pattern id="hatch" width="8" height="8" patternUnits="userSpaceOnUse" patternTransform="rotate(45)"><rect width="8" height="8" fill="#fff1d6"/><line x1="0" y1="0" x2="0" y2="8" stroke="#d9822b" stroke-width="3"/></pattern></defs>'+s
# --- 9 VALUE
v=f'<g class="seq" style="--d:.2s"><rect x="0" y="4" width="464" height="34" rx="10" fill="#0b2a3c"/>'+T(232,26,"180 mt × 1,000 kg/t × ₱180/kg = ₱32.4M",15,"#ffffff",700,"middle")+'</g>'
VR=[("A · Cat 1",32.4),("B · Cat 2",28.6),("D · Cat 2",9.8),("C · Cat 1",3.24),("A · Cat 3",0)]
for i,(n,val) in enumerate(VR):
    y=52+i*24
    v+=f'<g class="seq" style="--d:{0.6+i*0.12:.2f}s">'+T(0,y+13,str(i+1),14,"#0e8f86",800)+T(18,y+13,n,12.5,"#0b2a3c",600)
    v+=f'<rect x="100" y="{y+2}" width="270" height="14" rx="4" fill="#e6f6f3"/><rect x="100" y="{y+2}" width="{val/32.4*270:.0f}" height="14" rx="4" fill="#d9822b" class="grow" style="--d:{0.7+i*0.12:.2f}s"/>'
    v+=T(464,y+14,("₱%.1fM"%val if val>=5 else ("₱%.2fM"%val if val>0 else "₱0 (no shortfall)")),12.5,"#0b2a3c",800,"end")+'</g>'
v+=f'<g class="seq" style="--d:1.5s"><rect x="40" y="176" width="384" height="28" rx="14" fill="#fff7e0" stroke="#f2b53a" stroke-width="1.5"/>'+T(232,195,"gross value at stake, not income or profit loss",13,"#6b4a00",700,"middle")+'</g>'
pb='<path class="fpath" data-to="4" d="M40,420 H108"/>'
pb+='<path class="fpath" data-to="5" d="M612,420 H708"/><path class="fpath" data-to="6" d="M1212,420 H1308"/>'
pb+='<path class="fpath long" data-to="7" d="M1560,592 V606 H60 V790 H108"/>'
pb+='<path class="fpath" data-to="8" d="M612,790 H708"/><path class="fpath" data-to="9" data-c="#d9822b" d="M1212,790 H1308"/>'
for x,y,k in [(108,420,4),(708,420,5),(1308,420,6),(108,790,7),(708,790,8),(1308,790,9)]:
    pb+=f'<path class="fhead" data-to="{k}" d="M{x-9},{y-7} L{x+1},{y} L{x-9},{y+7}Z"/>'
B=f'''<section class="slide uw flow" id="s-flowB" data-label="07" data-title="IV · Data flow 2/2 · Random Forest → Value" data-sec="3" data-steps="5" data-q="algo">
<div class="rays" style="opacity:.55"></div>
{hd("04","IV · Algorithm Justification · data flow 2 of 2","<em>Random Forest</em> selects. <span class='c'>GAMM</span> forecasts.")}
<button class="abs btn fplay" style="right:110px;top:118px">▶ Play the flow</button>
<div class="abs small" style="left:22px;top:398px;width:84px;font:700 12px/1.25 IN;color:var(--sea);text-align:center">train rows<br>from 1/2</div>
{panel(4,"Random Forest","Ranks which columns help predict landings.",rf,[("s-rf","IV.1 Random Forest demo")])}
{panel(5,"GAMM","Adds simple curves together into the forecast.",g,[("s-gamm","IV.2 GAMM demo")])}
{panel(6,"Forecast","Next-quarter tons per province × fish category.",f,[("s-gamm","IV.2 forecast")])}
{panel(7,"Check","Must beat 'same quarter last year' on the test quarters.",c,[("s-eval","IV.3 baseline"),("s-contrib","IV.4 with / without")])}
{panel(8,"Shortfall","Forecast below the usual seasonal level = shortfall.",s,[("s-var","IV.5 builder")])}
{panel(9,"Value at risk","Shortfall tons × historical first-sale price = pesos.",v,[("s-var","IV.5 builder")])}
<svg class="abs flowsvg" width="1920" height="1080" style="left:0;top:0">{pb}<g class="parts"></g></svg>
{notes("""[Stage 4] Only the training rows go into Random Forest. Random Forest ranks which columns help predict landings. It picks predictors; it does not make the forecast. Here the top four move on, and the weaker ones are dropped. Price is not a predictor; we only use it at the end.
[→ Stage 5] GAMM builds the forecast by adding simple pieces: a seasonal curve, a smooth curve for each selected predictor, and a level shift for each province and fish category. Added together, they make the forecast line.
[→ Stage 6] The output is next quarter's landings in metric tons for each province and fish category, with a range that shows the uncertainty.
[→ Stage 7] Before we trust it, we check it on the locked test quarters against a simple baseline: the same quarter last year. We report MAE, RMSE and MASE. A MASE below one means we beat the seasonal-naive baseline. If we don't beat it, we say so.
[→ Stage 8] Next, we compare each forecast with the usual level for that season, our benchmark. If the forecast is below it, the gap in tons is the projected shortfall. If it is above, there is no shortfall.
[→ Stage 9] Finally, shortfall tons times the historical first-sale price gives pesos: gross landing value at risk. We rank the province–category combinations so planners know where to look first. This is gross value at stake, not lost income or profit. All numbers here are illustrative.""")}
</section>'''
FLOW=[A,B]
