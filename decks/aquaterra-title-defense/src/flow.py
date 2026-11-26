# Two-slide algorithm section (v5): A = data -> table -> 70/15/15 split -> evaluation; B = RF + GAMM -> shortfall -> value at risk
def hd(num,kick,h):
    return f'<div class="hd"><div class="num">{num}</div><div><div class="kick">{kick}</div><h2 style="margin-top:12px">{h}</h2></div></div>'
def sh(n,lab,line): return f'<div class="sh"><b><i>{n}</i>{lab}</b><span>{line}</span></div>'
def notes(t): return f'<aside class="notes">{t.strip()}</aside>'
ILL='<span class="ill" style="position:absolute;right:18px;top:16px">ILLUSTRATIVE</span>'
# split arithmetic: 2002 Q1-2025 Q4 = 96 quarters; 70/15/15 -> 67/14/15
def ql(i): return f"{2002+i//4} Q{i%4+1}"
NQ=96; NTR=round(NQ*.70); NTU=round(NQ*.15); NTE=NQ-NTR-NTU
SPLIT=dict(train=(ql(0),ql(NTR-1),NTR),tune=(ql(NTR),ql(NTR+NTU-1),NTU),test=(ql(NTR+NTU),ql(NQ-1),NTE))
assert (NTR,NTU,NTE)==(67,14,15) and SPLIT['test'][0]=="2022 Q2" and SPLIT['train'][1]=="2018 Q3"
ICON={"psa":'<rect x="8" y="26" width="7" height="12" rx="1.5"/><rect x="19" y="18" width="7" height="20" rx="1.5"/><rect x="30" y="10" width="7" height="28" rx="1.5"/>',
"rain":'<path d="M12 22 C10 14 18 9 24 12 C27 6 37 8 37 16 C42 17 42 24 36 24 H14 C10 24 10 22 12 22Z"/><path d="M15 30 l-2 6 M23 30 l-2 6 M31 30 l-2 6" stroke="currentColor" stroke-width="2.5"/>',
"sst":'<path d="M19 8 a4 4 0 0 1 8 0 v18 a8 8 0 1 1 -8 0Z"/><path d="M6 40 q5 -4 10 0 t10 0 t10 0" stroke="currentColor" stroke-width="2.5" fill="none"/>',
"typh":'<path d="M23 23 m-4 0 a4 4 0 1 0 8 0 a4 4 0 1 0 -8 0 M23 9 C33 9 38 15 37 21 M23 37 C13 37 8 31 9 25 M9 25 C9 17 15 13 21 13 M37 21 C37 29 31 33 25 33" stroke="currentColor" stroke-width="3" fill="none"/>'}
SRC=[("#0e8f86","PSA OpenSTAT","Landings &amp; value · 31 categories","PSA (2026)","psa"),
("#2f7fd6","NASA IMERG","Rainfall","Huffman et al. (2023)","rain"),
("#d9822b","NOAA OISST","Sea surface temperature","Huang et al. (2021)","sst"),
("#8a5bd6","NOAA IBTrACS","Typhoon tracks","Gahtan et al. (2024)","typh")]
srch="".join(f'<div class="src2" style="--c:{c}"><svg width="40" height="40" viewBox="0 0 46 46" style="color:{c};fill:{c};flex:none">{ICON[ic]}</svg><div><b>{n}</b><small>{w}</small></div><em>{ct}</em></div>' for c,n,w,ct,ic in SRC)
COLS=[("Province × fish","#a9bfc6",210),("Quarter","#a9bfc6",120),("Landings (t)","#0e8f86",140),("Lag-4 (t)","#0e8f86",120),("Rain (mm)","#2f7fd6",120),("SST (°C)","#d9822b",110),("Typhoons","#8a5bd6",120)]
E=["⋮"]*7
tr_,tu_,te_=SPLIT['train'],SPLIT['tune'],SPLIT['test']
ROWS=[("train",["A · Cat 1",tr_[0],"412.0","—","610","27.9","0"]),
("tune",["A · Cat 1",tu_[0],"401.3","452.6","400","28.0","0"]),
("test",["A · Cat 1",te_[0],"388.5","395.1","560","28.6","0"]),("test",["B · Cat 2",te_[1],"121.7","119.4","890","28.9","1"])]
th="".join(f'<div style="width:{w}px;--c:{c}">{n}</div>' for n,c,w in COLS)
tr=""
for r,(g,vals) in enumerate(ROWS):
    cells="".join(f'<div class="seq" style="width:{COLS[k][2]}px;--d:{0.3+k*0.07+r*0.03:.2f}s">{v}</div>' for k,v in enumerate(vals))
    tr+=f'<div class="ftr g-{g}{" ell" if vals is E else ""}">{cells}</div>'
W=536
segw={k:round(W*SPLIT[k][2]/NQ) for k in SPLIT}
seg="".join(f'<button class="seg s-{k}" data-seg="{k}" style="width:{segw[k]}px">{ {"train":70,"tune":15,"test":15}[k]}%</button>' for k in ("train","tune","test"))
NAMES={"train":"Train","tune":"Tune","test":"Test"}
segl="".join(f'<button class="segl s-{k}" data-seg="{k}"><b>{NAMES[k]}</b><span>{a} – {b} · {n} quarters</span></button>' for k,(a,b,n) in [(k,SPLIT[k]) for k in ("train","tune","test")])
def ul(items): return '<ul class="mlist">'+"".join(f"<li>{x}</li>" for x in items)+'</ul>'
def nxt(t): return f'<div class="abs nextl">→ <b>Next:</b> {t}</div>'
pa=('<path class="fpath" data-to="2" data-c="#0e8f86" d="M630,410 H660"/>'
    '<path class="fpath" data-to="3" data-c="#0e8f86" d="M1200,410 H1230"/>'
    '<path class="fpath" data-to="4" data-c="#6f8b99" d="M1520,590 C1520,602 420,598 420,610"/>'
    '<path class="fpath" data-to="5" data-c="#d9822b" d="M730,770 H760"/>')
A=f'''<section class="slide uw flow f2" id="s-flowA" data-label="06" data-title="VI · Methodology 1/3 · Data preparation" data-sec="3" data-steps="4" data-q="data" data-r="data">
{hd("06","VI · Methodology · 1 of 3","Methodology: <em>Data Preparation</em>")}
<button class="abs btn fplay" style="right:110px;top:118px">▶ Play the flow</button>
<div class="abs stg card2" data-st="1" style="left:110px;top:250px;width:520px;height:340px">{sh(1,"Sources","Four public datasets, 2002 Q1 – 2025 Q4")}<div style="margin-top:10px" class="srcs">{srch}</div></div>
<div class="abs stg card2" data-st="2" style="left:660px;top:250px;width:540px;height:340px">{sh(2,"Collect and clean","Keep usable histories; log every exclusion")}
 {ul(["Standardize names, units, dates","Drop duplicates and annual totals","Log missing shares and gaps","Gaps stay visible, never zero"])}<div class="cite">PSA (2026)</div></div>
<div class="abs stg card2" data-st="3" style="left:1230px;top:250px;width:580px;height:340px">{sh(3,"Time split · ~70 / 15 / 15","Split by time before filling any gaps")}
 <div class="segbar" style="margin-top:10px;height:44px">{seg}</div><div class="segls v">{segl}</div><div class="cite">Hewamalage et al. (2023)</div></div>
<div class="abs stg card2" data-st="4" style="left:110px;top:610px;width:620px;height:332px">{sh(4,"Impute and validate","Test on known values before filling real gaps")}
 {ul(["Compare SEADEC and Kalman structural imputation","KSSA: hide known blocks, rebuild, score error","Pick the lowest-error method; flag estimates","Long unsupported gaps stay unfilled"])}<div class="cite">Benavides et al. (2023)</div></div>
<div class="abs stg card2" data-st="5" style="left:760px;top:610px;width:1050px;height:332px">{sh(5,"Align and join","One row = province × fish category × quarter")}
 <span class="ill" style="position:absolute;right:18px;top:16px">ILLUSTRATIVE VALUES</span>
 <div class="rules"><span>Rain → quarterly total</span><span>SST → quarterly mean</span><span>Typhoons → distinct storms</span><span>Prices → valuation only</span></div>
 <div id="fa-tab"><div class="fth">{th}</div>{tr}</div></div>
<svg class="abs flowsvg" width="1920" height="1080" style="left:0;top:0">{pa}<g class="parts"></g></svg>
{nxt("Forecasting and Value at Risk")}
{notes(f"""Our methodology has three parts: data preparation, forecasting and value at risk, then evaluation. This slide is data preparation.
[Stage 1] We will use four public datasets from 2002 Q1 to 2025 Q4: PSA OpenSTAT quarterly marine municipal landings and value for the five MIMAROPA provinces and 31 fish categories (PSA, 2026), NASA IMERG rainfall (Huffman et al., 2023), NOAA OISST sea surface temperature (Huang et al., 2021) and NOAA IBTrACS typhoon tracks (Gahtan et al., 2024).
[→ Stage 2] We will collect PSA landing volumes and compatible historical prices, then standardize names, units and quarterly dates, remove duplicates and annual totals, and log missing shares and consecutive gaps. Any category we exclude for insufficient coverage will be documented with the reason. Missing quarters will stay on the calendar; an unavailable value is not a zero landing.
[→ Stage 3] Before filling any missing values, we will split the 96 quarters by time, about 70/15/15 after whole-quarter rounding: Train {tr_[0]} to {tr_[1]} ({tr_[2]} quarters), Tune or validation {tu_[0]} to {tu_[1]} ({tu_[2]}), Test {te_[0]} to {te_[1]} ({te_[2]}). At each forecast date, preparation will use only information available by then, so later test quarters cannot leak into earlier estimates (Hewamalage et al., 2023). The ratio is our design choice.
[→ Stage 4] We will compare SEADEC and structural time-series imputation with Kalman-based estimation, which performed well on marine landing series in Benavides et al. (2023); we will revalidate them on our quarterly data. KSSA will temporarily hide known blocks inside the training history, rebuild them and compare with the true values; we will pick the lowest-error method per series, flag every estimate, and leave long unsupported gaps unfilled.
[→ Stage 5] Finally we will align everything to one row per province, fish category and quarter: rainfall as quarterly totals, SST as quarterly means, typhoons as counts of distinct qualifying storms. Prices will be matched by unit and kept for the valuation step only, never as a predictor. Table values are illustrative. Next: forecasting and value at risk.""")}
</section>'''
IMP=[("Lagged landings",.92),("Season",.78),("SST",.52),("Rainfall",.40),("Typhoons",.22)]
bars="".join(f'<div class="ib{" lo" if v<.3 else ""}"><span>{n}</span><i><s class="grow" style="width:{v*100:.0f}%;--d:{0.5+k*.1:.2f}s"></s></i></div>' for k,(n,v) in enumerate(IMP))
TERMS=[("s(season)","#0e8f86",0),("s(lagged landings)","#0e8f86",0),("s(SST)","#d9822b",1),("s(rainfall)","#2f7fd6",1),("s(typhoons)","#8a5bd6",1),("+ province","#36546a",0),("+ fish category","#36546a",0)]
terms="".join(f'<span class="gt{" env" if e else ""}" style="--c:{c}">{t}</span>' for t,c,e in TERMS)
pb=('<path class="fpath" data-to="7" data-c="#0e8f86" d="M650,460 H700"/>'
    '<path class="fpath" data-to="8" data-c="#8a5bd6" d="M1260,460 H1310"/>'
    '<path class="fpath" data-to="9" data-c="#d9822b" d="M1560,688 V712"/>')
B=f'''<section class="slide uw flow f2" id="s-flowB" data-label="07" data-title="VI · Methodology 2/3 · Forecasting and value at risk" data-sec="3" data-steps="3" data-q="value" data-r="algo">
{hd("07","VI · Methodology · 2 of 3","Methodology: <em>Forecasting and Value at Risk</em>")}
<button class="abs btn fplay" style="right:110px;top:118px">▶ Play the flow</button>
<div class="abs stg card2" data-st="6" style="left:110px;top:250px;width:540px;height:438px">{sh(1,"Random Forest","Input: the joined table; will select predictors")}
 {ILL}<p class="b22" style="margin-top:10px">Shuffling a useful predictor will raise the error.</p>
 <div class="ibars">{bars}</div><div class="cite">Nesslage et al. (2021)</div></div>
<div class="abs stg card2" data-st="7" style="left:700px;top:250px;width:560px;height:438px">{sh(2,"Generalized Additive Mixed Model (GAMM)","Will forecast each province × fish category")}
 <div class="gterms" id="gterms">{terms}</div>
 <div style="display:flex;gap:10px;margin-top:12px"><button class="chip on" data-env="1">With weather</button><button class="chip" data-env="0">Without</button></div>
 <p class="b22" id="genv" style="margin-top:8px">Both versions will be compared.</p>
 <div class="cite">Holmes et al. (2021)</div></div>
<div class="abs stg card2" data-st="8" style="left:1310px;top:250px;width:500px;height:438px">{sh(3,"Shortfall flag","Forecast compared with the seasonal benchmark")}{ILL}
 <svg width="460" height="230" style="margin-top:8px"><line x1="20" y1="200" x2="440" y2="200" stroke="#cfe0dc" stroke-width="2"/>
  <rect class="growy" style="--d:.3s" x="60" y="40" width="130" height="160" rx="8" fill="#cfe6e1"/><rect class="growy" style="--d:.5s" x="260" y="75" width="130" height="125" rx="8" fill="#0e8f86"/>
  <rect class="seq" style="--d:1.1s" x="260" y="40" width="130" height="35" rx="6" fill="none" stroke="#d9822b" stroke-width="3" stroke-dasharray="7 5"/>
  <text x="125" y="30" text-anchor="middle" font-size="20" font-weight="700" fill="#0d2b45">820 t</text><text x="325" y="66" text-anchor="middle" font-size="18" font-weight="700" fill="#d9822b" class="seq" style="--d:1.1s">−180 t</text>
  <text x="325" y="105" text-anchor="middle" font-size="20" font-weight="700" fill="#fff">640 t</text>
  <text x="125" y="224" text-anchor="middle" font-size="18" fill="#36546a">benchmark</text><text x="325" y="224" text-anchor="middle" font-size="18" fill="#36546a">forecast</text></svg>
 <p class="b22" style="margin-top:4px">Below benchmark = shortfall flagged.</p></div>
<div class="abs stg card2" data-st="9" style="left:110px;top:712px;width:1700px;height:222px">{sh(4,"Gross landing value at risk","Shortfall × historical first-sale price, then ranked by province × fish category")}{ILL}
 <div class="vrow"><span>180 t × 1,000 kg</span><i>×</i><span id="vp">₱180/kg</span><i>=</i><span class="vres" id="vres">₱32.4M</span>
  <div class="vtog"><button class="chip on" data-pr="180">First-sale price</button><button class="chip" data-pr="150">Unit-value proxy</button></div></div>
 <p class="b22" id="vnote" style="margin-top:10px">Gross value at stake, not profit or income.</p></div>
<svg class="abs flowsvg" width="1920" height="1080" style="left:0;top:0">{pb}<g class="parts"></g></svg>
{nxt("Evaluation")}
{notes("""Part two: forecasting and value at risk. The joined table from data preparation is the input.
[Stage 1] Random Forest, an ensemble of decision trees, will learn only from the Train quarters and rank predictors by permutation importance: if shuffling a predictor raises the error, it matters. It will select predictors; it will not make the final forecast. Using Random Forest importance to guide a GAMM follows Nesslage et al. (2021). Bars are illustrative.
[→ Stage 2] The Generalized Additive Mixed Model, or GAMM, will forecast next-quarter landings for each province and fish category, adding smooth curves for the season, lagged landings and each selected predictor, plus random effects for province and fish category (Holmes et al., 2021). Toggle 'Without' to see the version without weather terms.
[→ Stage 3] Each forecast will be compared with the seasonal benchmark, the usual level for that province, category and quarter. If the forecast falls below it, the gap is flagged as a projected shortfall. Numbers are illustrative.
[→ Stage 4] Shortfall tonnes times 1,000 times the historical first-sale price gives the gross landing value at risk in pesos. We will rank province × fish-category combinations by that value. It is gross value at stake, not profit or income. Values are illustrative. Next: how we will evaluate all of this.""")}
</section>'''
EV=[("Held-out test quarters",f"<b>{te_[0]} – {te_[1]}</b> · {te_[2]} quarters, locked until the final check. Train and Tune quarters will be used only for fitting and selection.","Hewamalage et al. (2023)"),
("Forecast accuracy","<b>MAE, RMSE and MASE</b> against a seasonal-naive baseline (the same quarter last year). MASE below 1 will mean the workflow beats the baseline.","Hyndman &amp; Athanasopoulos (2021)"),
("Do weather predictors help?","Forecasts <b>with vs without</b> typhoon, rainfall and SST predictors; contribution = the reduction in MAE on held-out quarters. Prediction, not cause.","Holmes et al. (2021); Nesslage et al. (2021)"),
("Are value rankings stable?","<b>Price sensitivity:</b> first-sale price vs a unit-value proxy. <b>Ranking stability:</b> whether the top province × category combinations keep their places.","")]
pos=[(110,250),(980,250),(110,600),(980,600)]
evh="".join(f'<div class="abs card2 ev8{" rv" if i else ""}" {f"data-s={i}" if i else ""} style="left:{x}px;top:{y}px;width:830px;height:320px"><div class="sh"><b><i>{i+1}</i>{t}</b></div><p class="b22" style="margin-top:14px">{d}</p>{f"<div class=cite>{c}</div>" if c else ""}</div>' for i,((t,d,c),(x,y)) in enumerate(zip(EV,pos)))
C=f'''<section class="slide uw f2" id="s-eval8" data-label="08" data-title="VI · Methodology 3/3 · Evaluation" data-sec="3" data-steps="3" data-q="algo" data-r="algo">
{hd("08","VI · Methodology · 3 of 3","Methodology: <em>Evaluation</em>")}
{evh}
{nxt("Potential Clients")}
{notes(f"""Part three: evaluation.
[1] We will lock the Test quarters, {te_[0]} to {te_[1]}, {te_[2]} quarters, until the final check; Train and Tune quarters will be used only for fitting and selecting models (Hewamalage et al., 2023).
[→ 2] Forecast accuracy will be measured with MAE, RMSE and MASE against a seasonal-naive baseline, which simply repeats the same quarter last year (Hyndman & Athanasopoulos, 2021). A MASE below 1 will mean our workflow beats that baseline.
[→ 3] To answer SOP 2, we will run the forecasts with and without the typhoon, rainfall and SST predictors and measure the reduction in MAE on held-out quarters. If they don't help, we will report that. This is prediction, not cause.
[→ 4] For value at risk, we will swap the historical first-sale price for a unit-value proxy and check whether the top-ranked province × fish-category combinations keep their places. Next: who could use these results.""")}
</section>'''
FLOW=[A,B,C]
