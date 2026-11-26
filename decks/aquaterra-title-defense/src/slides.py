TITLE="AquaTerra: Forecasting Municipal Fish Landing Shortfalls and Estimating Gross Landing Value at Risk in Selected Philippine Coastal Provinces"
SUB="Forecasting Municipal Fish Landing Shortfalls and Estimating Gross Landing Value at Risk in Selected Philippine Coastal Provinces"
from flow import SPLIT
TR,TU,TE=SPLIT['train'],SPLIT['tune'],SPLIT['test']
def waveH(fill="#ffffff",h=120,flip=False,op=1):
    d="M0,60 C320,10 640,110 960,60 C1280,10 1600,110 1920,60 L1920,120 L0,120Z"
    t=' style="transform:scaleY(-1)"' if flip else ''
    return f'<svg viewBox="0 0 1920 120" preserveAspectRatio="none" width="1920" height="{h}"{t}><path d="{d}" fill="{fill}" opacity="{op}"/><path d="M0,74 C320,24 640,124 960,74 C1280,24 1600,124 1920,74" stroke="{fill}" stroke-opacity=".5" stroke-width="3" fill="none"/></svg>'
def hd(num,kick,h,extra=""):
    return f'<div class="hd"><div class="num">{num}</div><div><div class="kick">{kick}</div><h2 style="margin-top:12px">{h}</h2></div>{extra}</div>'
def notes(t): return f'<aside class="notes">{t.strip()}</aside>'
S=[]
# ================= COVER =================
terms=[("municipal","Municipal","Catch from <b>municipal waters</b>, up to <b>15 km from shore</b> (RA 10654, 2015), by fishers with no boat or boats of <b>3 gross tons or less</b>."),
("landings","Landings","Fish <b>brought ashore</b>, in tonnes, per province and quarter (PSA, 2026)."),
("quarter","Quarter","<b>Q1</b> Jan–Mar · <b>Q2</b> Apr–Jun · <b>Q3</b> Jul–Sep · <b>Q4</b> Oct–Dec."),
("var","Gross landing value at risk","<b>Projected shortfall × historical first-sale price</b>. Gross value at stake, not income, profit or damage.")]
chips="".join(f'<button class="chip term" data-t="{k}">{n}</button>' for k,n,_ in terms)
pops="".join(f'<div class="pop" id="pop-{k}" style="left:1110px;top:300px;width:700px"><div class="lab" style="color:var(--sea);margin-bottom:10px">{n}</div>{t}</div>' for k,n,t in terms)
S.append(f'''<section class="slide" id="s-hook" data-label="00" data-title="Cover · AquaTerra" data-sec="-1" data-steps="3" data-q="title">
<div class="abs" style="left:110px;top:96px;width:1120px">
 <p style="font:500 62px/1.16 PF;margin:0;color:var(--ink)">Fish feeds our families and supports coastal livelihoods.</p>
 <p class="rv" data-s="1" style="font:500 62px/1.16 PF;margin-top:30px;color:var(--ink)">Fishers, vendors and businesses depend on a steady supply.</p>
 <p class="rv" data-s="2" style="font:600 italic 80px/1.08 PF;margin-top:34px;color:var(--sea)">Can past data warn us when that supply will <span style="color:var(--coral)">fall short?</span></p>
</div>
<div class="abs glass" id="cov-id" style="left:1300px;top:96px;width:520px;padding:30px 34px">
 <div class="kick">Title Defense</div>
 <div style="font:600 40px/1.15 PF;color:var(--ink);margin-top:14px">Group DJANGO</div>
 <div style="font:500 23px/1.4 IN;color:var(--ink2);margin-top:10px">BS Computer Science – Data Science<br>FEU Institute of Technology (FEU Tech)</div>
 <div class="lab" style="margin-top:24px;color:var(--sea)">Members</div>
 <ul style="list-style:none;margin-top:10px;font:500 23px/1.6 IN;color:var(--ink)"><li>Chan, Reese Lauren C.</li><li>Ebrahim, Fathi Mahad</li><li>Pacate, Denienz A.</li><li>Whitty, Juan Angelo Roy B.</li></ul>
</div>
<div class="abs rv" data-s="3" style="left:0;right:0;bottom:0;height:330px">
 <div class="abs" style="top:0;left:0">{waveH("#e6f6f3",80)}</div>
 <div class="abs" style="top:78px;left:0;right:0;bottom:0;background:#e6f6f3"></div>
 <div class="abs" style="left:110px;top:44px;display:flex;gap:34px;align-items:flex-start;width:1700px">
  <div class="num" style="font-size:120px">00</div>
  <div style="padding-top:4px"><div class="kick">Our proposed study</div>
  <div style="font:700 54px/1 PF;color:var(--ink);margin-top:8px">AquaTerra<span style="color:var(--sea)">:</span></div><div style="font:500 25px/1.3 PF;color:var(--ink2);margin-top:8px;width:1540px">{SUB}</div>
  <div style="display:flex;flex-wrap:wrap;gap:12px;margin-top:14px;align-items:center"><span class="lab" style="margin-right:6px">Key terms · click</span>{chips}</div></div>
 </div>
</div>
{pops}
{notes("""Fish feeds our families and supports the livelihoods of coastal communities. [→] Behind every catch are fishers, vendors and businesses that depend on a steady supply. [→] Can historical fisheries and environmental data help us anticipate when that supply will fall short? [→] Good day, respected panelists. We are Group Django, and today we present our proposed study, 'AquaTerra: Forecasting Municipal Fish Landing Shortfalls and Estimating Gross Landing Value at Risk in Selected Philippine Coastal Provinces.'
'Municipal' fish means catch from municipal waters, up to 15 km from shore under RA 8550 as amended by RA 10654, by fishers using no boat or boats of three gross tons or less. 'Landings' means the catch brought ashore, in tonnes per province per quarter. (Click a key term to define it; press Q for panel questions.)""")}
</section>''')
# ================= I · BACKGROUND =================
S.append(f'''<section class="slide" id="s-bg" data-label="01" data-title="I · Background" data-sec="0" data-steps="4" data-q="bg" data-r="bg">
<div class="bgimg" style="background-image:url({{{{IMG:bangka}}}});bottom:auto;height:470px"></div>
<div class="full" style="bottom:auto;height:470px;background:linear-gradient(180deg,rgba(2,40,58,.6),rgba(2,40,58,.2))"></div>
<div class="abs" style="left:110px;top:62px;display:flex;gap:34px;align-items:flex-end;color:#fff">
 <div class="num w">01</div><div><div class="kick" style="color:#e6fff9">I · Background</div>
 <h2 style="margin-top:12px;color:#fff;font-size:62px">Background of the <em style="color:#ffcdbd">Study</em></h2></div></div>
<div class="abs" style="left:0;top:380px">{waveH("#ffffff",110)}</div>
<div class="abs" style="left:0;right:0;top:488px;bottom:0;background:#ffffff"></div>
<div class="abs rv bgc" data-s="1" style="left:110px;top:470px;width:530px">
 <div class="lab" style="color:var(--sea)">1 · Why it matters</div>
 <p class="b22">Fisheries are key to <b>food security and livelihoods</b>.</p><div class="cite">FAO (2024)</div>
 <p class="b22" style="margin-top:14px">2023 oil spill, <b>Naujan, Oriental Mindoro</b>: fishing banned, income lost.</p><div class="cite">Agaton et al. (2023)</div>
</div>
<div class="abs rv bgc" data-s="2" style="left:690px;top:470px;width:560px">
 <div class="lab" style="color:var(--coral)">2 · The decline</div>
 <div style="display:flex;align-items:baseline;gap:14px;margin-top:6px"><span style="font:700 100px/1 PF;color:var(--coral)" id="oc-num">~45M</span><span style="font:600 34px PF;color:var(--ink)">kg / year</span></div>
 <svg width="560" height="120" viewBox="0 0 560 120" style="margin-top:6px"><line x1="40" y1="34" x2="520" y2="34" class="ax"/><line x1="40" y1="90" x2="520" y2="90" class="ax"/>
 <path id="oc-line" d="M40,34 L520,90" stroke="var(--coral)" stroke-width="5" fill="none" stroke-dasharray="12 9"/>
 <circle cx="40" cy="34" r="9" fill="var(--sea)"/><circle cx="520" cy="90" r="9" fill="var(--coral)"/>
 <text x="30" y="20" font-size="22" font-weight="700" fill="#0b2a3c">2010 · 2.6M t</text><text x="530" y="118" font-size="22" font-weight="700" fill="#0b2a3c" text-anchor="end">2023 · 1.9M t</text></svg>
 <p class="b22" style="margin-top:4px">National capture fisheries, linked to overfishing and illegal fishing.</p><div class="cite">Oceana (2026)</div>
</div>
<div class="abs rv bgc" data-s="3" style="left:1300px;top:470px;width:510px">
 <div class="lab" style="color:var(--sea)">3 · Forecasting so far</div>
 <p class="b22">A <b>regional</b> forecasting model for Philippine fisheries, with environmental data.</p><div class="cite">Bokingkito et al. (2026)</div>
 <p class="b22" style="margin-top:14px"><b>Our starting point.</b></p>
</div>
<div class="abs rv" data-s="4" style="left:110px;right:110px;top:872px;padding:18px 28px;border-radius:16px;background:var(--ink);color:#fff;font:500 27px/1.35 IN">
 <span class="lab" style="color:var(--aqua)">The question&nbsp;&nbsp;</span>Can we see these drops coming, province by province?</div>
{notes("""When fish gets expensive at the palengke, it's usually because less fish came in. Fish isn't just food on our table; it supports jobs and income in coastal towns, and FAO points to fisheries as key to food security and livelihoods (FAO, 2024).
[→] We've seen what happens when supply is disrupted. After the February 2023 oil spill off Naujan, Oriental Mindoro, fishing was banned; the fisherfolk interviewed lost their main income, some up to about US$1,300 a week, and relief did not cover basic needs (Agaton et al., 2023).
[→] And the long-term trend is worrying: Oceana reports capture fisheries fell from about 2.6M mt in 2010 to 1.9M in 2023, roughly 45M kg lost every year, a national figure (Oceana, 2026). Oceana links the decline to governance gaps: overfishing, illegal fishing, commercial vessels entering municipal waters and weak enforcement.
[→] So can we see these drops coming? Bokingkito et al. (2026) built a regional forecasting model for Philippine fisheries using environmental data. That's our starting point.
[→] So what's still missing?""")}
</section>''')
# ================= II · RESEARCH GAPS =================
GAPS=[("Level","No seasonal shortfall forecasts by <b>province × fish category</b>, where local offices plan.","Forecast each combination and flag shortfalls.","Bokingkito et al. (2026)"),
("Value","Forecasts give <b>kilos, not value</b>.","Attach a historical first-sale price to each shortfall.","Bokingkito et al. (2026); PSA (2026)"),
("Checking","Shortfall flags and value rankings are <b>not yet checked</b>.","Test flag accuracy, and whether rankings hold when prices change.","Hewamalage et al. (2023)"),
("Weather","Typhoons, rain and sea temperature are linked to lower catch, but <b>few studies test</b> them in a provincial forecast.","Test with vs without; report it if they don't help. Prediction, not cause.","Noy et al. (2023); Holmes et al. (2021)")]
gpos=[(110,330),(980,330),(110,610),(980,610)]
gh="".join(f'<button class="abs gap rv" data-s="{i+1}" data-g="{i}" style="left:{x}px;top:{y}px"><div class="gn"><span>Gap {i+1}</span>{t}</div><p>{p}</p><p class="gw"><b>AquaTerra will:</b> {w}</p><div class="cite">{c}</div></button>' for i,((t,p,w,c),(x,y)) in enumerate(zip(GAPS,gpos)))
S.append(f'''<section class="slide" id="s-gaps" data-label="02" data-title="II · Research Gaps" data-sec="0" data-steps="5" data-q="gaps" data-r="gaps">
{hd("02","II · Research Gaps","Research <em>Gaps</em>")}
<div class="abs b22" style="left:110px;top:258px;width:1700px"><b>Existing forecasts</b> work at region and sector level and stop at <i>how much fish</i> to expect. <span class="cite" style="display:inline">Bokingkito et al. (2026)</span></div>
{gh}
<div class="abs rv" data-s="5" style="left:110px;width:1700px;top:892px;padding:16px 28px;border-radius:16px;background:var(--ink);color:#fff;font:500 27px/1.35 IN"><span class="lab" style="color:var(--aqua)">AquaTerra&nbsp;&nbsp;</span>turns forecasts into <b>shortfalls and their value</b>, province by province.</div>
{notes("""So here's what those studies already did. Existing forecasts like Bokingkito et al. (2026) work at the region and sector level, and they stop at how much fish to expect.
[→] Gap 1: there are no seasonal shortfall forecasts by province and fish category, the level where local offices plan. We will forecast each province and fish category and flag seasonal shortfalls.
[→] Gap 2: forecasts give kilos, not value. We will attach a historical first-sale price to each shortfall, using PSA value and volume records (PSA, 2026).
[→] Gap 3: shortfall flags and value rankings haven't been checked. We will test how accurate the flags are, and whether the rankings hold when prices change, on later quarters the model has not seen (Hewamalage et al., 2023).
[→] Gap 4: typhoons, rainfall and sea temperature are often linked to lower catch (Noy et al., 2023; Holmes et al., 2021), but few studies check whether they improve a provincial forecast. We will test that, and report it if they don't help. This is prediction, not cause.
[→] That's where AquaTerra fits: it fills the gap by turning forecasts into shortfalls and their value at province level. (Press R for the references behind each gap.)""")}
</section>''')
# ================= III · SOP <-> SO =================
SOP=["What seasonal benchmarks will identify landing shortfalls for each MIMAROPA province and fish category, using PSA quarterly records from 2002 to 2025?",
"How much will prior typhoon exposure, rainfall and sea surface temperature improve next-quarter landing forecasts from a Random Forest–GAMM workflow?",
"What gross landing value at risk will the projected shortfalls carry when priced at historical first-sale prices?",
f"How accurate will the forecasts be on held-out quarters ({TE[0]}–{TE[1]}), measured by MAE, RMSE and MASE against a seasonal-naive baseline?"]
SO=[f"Build seasonal benchmarks for each province × fish category from PSA quarterly landings, {TR[0]}–{TE[1]}.",
"Develop the Random Forest → GAMM workflow and measure the added value of typhoon, rainfall and SST predictors (with vs without).",
"Estimate the gross landing value at risk of each projected shortfall using historical first-sale prices, and rank the combinations.",
f"Evaluate the forecasts on held-out quarters ({TE[0]}–{TE[1]}) with MAE, RMSE and MASE vs the seasonal-naive baseline, plus price-sensitivity and ranking-stability checks."]
pairs="".join(f'<button class="abs pair rv" data-s="{i+1}" data-i="{i}" style="top:{452+i*130}px"><div class="pq"><span>SOP {i+1}</span>{q}</div><i>↔</i><div class="po"><span>SO {i+1}</span>To {o[0].lower()+o[1:]}</div></button>' for i,(q,o) in enumerate(zip(SOP,SO)))
S.append(f'''<section class="slide uw" id="s-obj" data-label="03" data-title="III · Problem and Objectives" data-sec="1" data-steps="4" data-q="obj" data-r="algo">
{hd("03","III · Research questions and objectives","Statement of the Problem and <em>Specific Objectives</em>")}
<div class="abs b22" style="left:110px;top:250px;width:1700px"><span class="lab" style="color:var(--sea)">General objective&nbsp;&nbsp;</span>AquaTerra will forecast next-quarter municipal fish landings, flag seasonal shortfalls and estimate their gross landing value at risk for five MIMAROPA provinces.</div>
<div class="abs algo" style="left:110px;top:330px"><b>Random Forest</b> will rank and select the predictors. <span class="cite" style="display:inline">Nesslage et al. (2021)</span></div>
<div class="abs algo" style="left:965px;top:330px"><b>GAMM</b> will forecast landings with smooth curves. <span class="cite" style="display:inline">Holmes et al. (2021)</span></div>
<div class="abs lab" style="left:110px;top:422px">Initial research questions (preliminary)</div><div class="abs lab" style="left:990px;top:422px">Specific objectives</div>
{pairs}
{notes(f"""Our general objective: AquaTerra will forecast next-quarter municipal fish landings, flag seasonal shortfalls and estimate their gross landing value at risk for the five MIMAROPA provinces.
Two algorithms, in one line each. Random Forest, many decision trees voting, will rank the candidate predictors and keep the useful ones (Nesslage et al., 2021). GAMM, a generalized additive mixed model, will add smooth curves for each selected predictor, plus province and fish-category effects, to forecast landings (Holmes et al., 2021).
These are our initial research questions; we expect to refine them. Each is paired with exactly one specific objective.
[→] SOP 1: {SOP[0]} SO 1: to {SO[0][0].lower()+SO[0][1:]}
[→] SOP 2: {SOP[1]} SO 2: to {SO[1][0].lower()+SO[1][1:]}
[→] SOP 3: {SOP[2]} SO 3: to {SO[2][0].lower()+SO[2][1:]}
[→] SOP 4: {SOP[3]} SO 4: to {SO[3][0].lower()+SO[3][1:]}
The dashboard and the consultation with DTI or a fisheries agency are part of our scope, not separate objectives. (Click a row to highlight its pair.)""")}
</section>''')
# ================= IV · SCOPE & LIMITATION =================
SC=[("Study area · MIMAROPA","Occidental Mindoro, Oriental Mindoro, Marinduque, Romblon, Palawan · 31 fish categories","PSA (2026)"),
("Municipal fish","Catch within municipal waters, up to 15 km from shore; boats of 3 gross tons or less","RA 10654 (2015)"),
(f"Public data · {TR[0]} – {TE[1]}","PSA OpenSTAT · NASA IMERG · NOAA OISST · NOAA IBTrACS",""),
("Forecast → shortfall → value","Next-quarter RF → GAMM forecasts, seasonal shortfalls, gross landing value at risk",""),
("Evaluation & dashboard","70/15/15 time split · web dashboard · consultation sought with DTI or a fisheries agency","")]
LM=[("Selected coverage","No commercial, aquaculture or inland fisheries; no field monitoring."),
("Next quarter only","Data gaps and delays may limit accuracy; fishing effort is not modeled."),
("No causal claims","Will test whether weather helps predict landings, not whether it causes shortfalls."),
("Gross value only","Historical prices; no price forecasts, income loss, profit or damage."),
("Research prototype","No guaranteed real-time updates; adoption is not guaranteed.")]
sch="".join(f'<div class="li"><i>✓</i><div><b>{a}</b><span>{b}{f" <em class=ct>{c}</em>" if c else ""}</span></div></div>' for a,b,c in SC)
lmh="".join(f'<button class="li lm" data-i="{i}"><i>✕</i><div><b>{a}</b><span>{b}</span></div></button>' for i,(a,b) in enumerate(LM))
S.append(f'''<section class="slide" id="s-scope" data-label="04" data-title="IV · Scope and Limitation" data-sec="2" data-steps="2" data-q="scope" data-r="scope">
<div class="abs" style="left:110px;top:56px;display:flex;gap:34px;align-items:flex-end"><div class="num">04</div><div><div class="kick">IV · Scope and Limitation</div><h2 style="margin-top:12px;font-size:58px;">Scope and <em>Limitations</em></h2></div></div>
<div class="abs" id="sl-tog" style="right:110px;top:222px;display:flex;gap:8px"><button class="chip" data-v="scope">Scope</button><button class="chip cor" data-v="lim">Limitation</button><button class="chip on" data-v="both">Both</button></div>
<div class="abs glass colA" data-s="1" style="left:110px;top:284px;width:830px;height:676px;padding:22px 30px"><div class="lab" style="color:var(--sea)">Scope</div>{sch}</div>
<div class="abs glass colB rv" data-s="2" style="left:980px;top:284px;width:830px;height:676px;padding:22px 30px"><div class="lab" style="color:var(--coral)">Limitation · click to focus</div>{lmh}</div>
{notes(f"""Scope. Our study area will be MIMAROPA: Occidental Mindoro, Oriental Mindoro, Marinduque, Romblon and Palawan, across the 31 named fish categories in PSA's marine municipal fisheries tables (PSA, 2026); PSA's 'Others' group will be left out. Municipal fish means catch within municipal waters, which under RA 8550 as amended by RA 10654 extend up to 15 km from the coastline, by fishers using no boat or boats of three gross tons or less (RA 10654, 2015). We will use public data from {TR[0]} to {TE[1]}: PSA OpenSTAT, NASA IMERG, NOAA OISST and NOAA IBTrACS. Random Forest will select predictors and GAMM will forecast the next quarter; we will compare forecasts with seasonal benchmarks, value shortfalls with historical first-sale prices, evaluate on a 70/15/15 time split, show results on a web dashboard, and seek consultation with DTI or a relevant fisheries agency.
[→] Limitations: selected provinces and marine municipal categories only; no commercial, aquaculture or inland fisheries and no field monitoring. Next quarter only; data gaps and delays may affect accuracy, and fishing effort and fuel costs will not be modeled. We will not establish causal effects of typhoons, rainfall or sea temperature. Gross landing value at risk will use historical prices, not income, profit or damage. The dashboard will be a research prototype, and adoption is not guaranteed.""")}
</section>''')
# ================= V · ALGORITHMS (2 slides) =================
from flow import FLOW
S.extend(FLOW)
# ================= VI · CLIENTS =================
CL=[("LGUs & fisheries offices","Primary potential users","see projected shortfalls early and prioritize monitoring"),
("BFAR","","supplementary information for monitoring and planning"),
("DTI","","exposure estimates for consultations with fisheries-related enterprises"),
("Fisherfolk associations","","seasonal supply outlooks for marketing and deliveries"),
("Traders, vendors & processors","","projected shortfalls for sourcing and inventory")]
pos=[(110,270),(700,270),(1290,270),(400,560),(990,560)]
clh="".join(f'<div class="abs glass cl rv" data-s="{i+1}" style="left:{x}px;top:{y}px">{f"<span class=tg>{t}</span>" if t else ""}<div class="ch">{h}</div><div class="cm">{m}</div></div>' for i,((h,t,m),(x,y)) in enumerate(zip(CL,pos)))
S.append(f'''<section class="slide" id="s-clients" data-label="08" data-title="VI · Potential Clients" data-sec="4" data-steps="5" data-q="clients">
<div class="abs" style="left:110px;top:56px;display:flex;gap:34px;align-items:flex-end"><div class="num">07</div><div><div class="kick">VI · Potential Clients</div><h2 style="margin-top:12px;font-size:58px">Potential <em>Clients</em></h2></div></div>
{clh}
<div class="abs" style="left:110px;right:110px;top:858px;padding:16px 26px;border-radius:14px;background:#fff7e0;border:2px solid var(--gold);font:600 23px/1.4 IN;color:#6b4a00">We will seek consultation with DTI or a relevant fisheries agency on data suitability and usefulness. Participation and adoption are not guaranteed.</div>
{notes("""Our primary potential users are LGUs and fisheries offices, which could use provincial and fish-category forecasts to see projected shortfalls early and prioritize monitoring. [→] BFAR could use the findings as supplementary information for monitoring and planning. [→] DTI could use exposure estimates in consultations with fisheries-related enterprises. [→] Fisherfolk associations and cooperatives could use seasonal supply outlooks for marketing and delivery coordination. [→] Traders, vendors and processors could use projected shortfalls for sourcing and inventory planning. We will seek consultation with DTI or a relevant agency; participation and adoption are not guaranteed.""")}
</section>''')
# ================= THANK YOU =================
S.append(f'''<section class="slide" id="s-end" data-label="09" data-title="Thank you" data-sec="5" data-steps="0">
<div class="abs" style="left:110px;right:110px;top:100px;text-align:center">
 <div class="kick">Group DJANGO · AquaTerra</div>
 <div style="font:600 170px/1 PF;margin-top:24px;color:var(--ink)">Thank you</div>
 <div style="font:400 italic 40px PF;color:var(--sea);margin-top:20px">We welcome your questions and recommendations.</div>
 <div style="display:flex;gap:16px;justify-content:center;margin-top:40px;flex-wrap:wrap">
  <button class="btn cor" data-go="b-qbank">? Panel Q&amp;A bank</button><button class="btn" data-go="b-cause">Prediction vs causation</button><button class="btn ghost" data-go="b-refs">References · APA 7</button></div>
</div>
<div class="abs imgframe" style="left:310px;top:640px;width:1300px;height:320px;background-image:url({{{{IMG:deep}}}})"></div>
{notes("""Thank you. We welcome your questions and recommendations. Backup slides: the panel Q&A bank, prediction vs causation, the evaluation demo, the value-at-risk builder, and the references (press B for the slide menu).""")}
</section>''')
# ================= B1 Q BANK =================
S.append('''<section class="slide backup uw" id="b-qbank" data-label="B1" data-title="Backup · Panel Q&amp;A bank" data-sec="6" data-steps="0">
<div class="hd"><div class="num" style="font-size:150px">B1</div><div><div class="kick">Backup</div><h2 style="margin-top:12px;font-size:54px">Panel Q&amp;A <em>Bank</em></h2></div></div>
<input id="qb-search" placeholder="Search questions…" style="position:absolute;right:110px;top:120px;width:420px;font:500 22px IN;padding:12px 18px;border-radius:12px;border:1.5px solid var(--line);background:#fff;color:var(--ink);outline:none">
<div class="abs" id="qb-cats" style="left:110px;top:260px;width:480px"></div>
<div class="abs" id="qb-list" style="left:630px;top:260px;width:1180px;height:690px;overflow:auto;padding-right:10px"></div>
<aside class="notes">Use the categories or search box to pull up a prepared answer.</aside>
</section>''')
# ================= B2 PREDICTION VS CAUSATION =================
S.append(f'''<section class="slide backup" id="b-cause" data-label="B2" data-title="Backup · Prediction vs causation" data-sec="6" data-steps="3">
<div class="hd"><div class="num" style="font-size:150px">B2</div><div><div class="kick" style="color:var(--coral)">Panel might ask</div><h2 style="margin-top:12px;font-size:52px">Prediction vs. <em>Causation</em></h2></div></div>
<div class="abs card" style="left:110px;top:270px;width:1700px;height:260px;padding:24px 30px">
 <div class="lab" style="color:var(--sea)">1 · The test we will run</div>
 <div style="display:flex;align-items:center;gap:20px;margin-top:16px">
  <div class="mb2"><b>Model A</b><span>past landings + season</span></div><div class="vs">vs</div>
  <div class="mb2 co"><b>Model B</b><span>A + typhoons + rain + SST</span></div>
  <div class="vs">→</div><div class="mb2"><b>Test quarters</b><span>MAE, RMSE, MASE</span></div>
  <div class="vs">→</div><div class="mb2 ok"><b>More accurate?</b><span>= useful for prediction only</span></div></div>
</div>
<div class="abs card rv" data-s="1" style="left:110px;top:560px;width:830px;height:390px;padding:24px 30px">
 <div class="lab" style="color:var(--coral)">2 · Why accuracy is not proof</div>
 <p class="b22" style="margin-top:12px">Other factors can move <b>with the weather</b> and change landings:</p>
 <div style="display:flex;flex-wrap:wrap;gap:10px;margin-top:14px"><span class="chip">Fishing effort</span><span class="chip">Fuel prices</span><span class="chip">Regulations</span><span class="chip">Reporting</span></div>
 <p class="b22" style="margin-top:14px">Proving cause needs <b>controlled or field studies</b>, outside our scope.</p>
</div>
<div class="abs card rv" data-s="2" style="left:980px;top:560px;width:830px;height:390px;padding:24px 30px">
 <div class="lab" style="color:var(--sea)">3 · How we will word results</div>
 <div class="say ok rv" data-s="2">✓ "Typhoon exposure <b>improves forecast accuracy</b> here."</div>
 <div class="say no rv" data-s="3">✕ "Typhoons <b>cause</b> lower landings."</div>
 <p class="b22" style="margin-top:14px">Same rule for rainfall, SST and any top-ranked predictor.</p>
</div>
{notes("""We will test whether environmental information improves forecast accuracy. We will compare a model with only past landings and seasonality against one with typhoon exposure, rainfall and sea temperature added, both evaluated on the held-out Test quarters. The gap: typhoons, rainfall and sea temperature are often linked to lower catch (Noy et al., 2023; Holmes et al., 2021), but few studies check whether they improve a provincial forecast. We will test that, and report it if they don't help. That is prediction, not cause.
[→] Better accuracy will mean predictive usefulness only. Fishing effort, fuel prices, regulations and reporting changes can move together with typhoons and weather and also affect landings. Proving cause would need controlled or field studies, which are outside our scope.
[→] So our results will say 'improves forecast accuracy', [→] never 'causes'.""")}
</section>''')
# ================= B3 EVALUATION DEMO (moved from main flow) =================
S.append(f'''<section class="slide backup uw" id="s-eval" data-label="B3" data-title="Backup · Evaluation demo (split slider)" data-sec="6" data-steps="2" data-q="algo" data-r="algo">
{hd("B3","Backup · Evaluation demo","Evaluation Against the <em>Seasonal-Naive Baseline</em>")}
<div class="abs card" style="left:110px;top:270px;width:1240px;height:690px;padding:20px 26px">
 <div style="display:flex;justify-content:space-between;align-items:center"><div class="lab">Landings (t) · one province × category</div><span class="ill">ILLUSTRATIVE</span></div>
 <svg id="e-chart" width="1190" height="430" style="margin-top:6px"></svg>
 <div style="display:flex;align-items:center;gap:18px;margin-top:8px;font:600 21px IN;color:var(--ink2)">Test starts <b id="e-lab" style="color:var(--coral);min-width:110px">{TE[0]}</b>
 <input type="range" id="e-split" min="60" max="88" value="81" style="flex:1"><button class="btn ghost" id="e-roll">▶ Rolling origin</button></div>
 <div style="display:flex;gap:22px;margin-top:12px;font:600 19px IN;color:var(--ink2)"><span><i class="lg" style="background:#a9bfc6"></i>observed</span><span class="rv" data-s="1"><i class="lg" style="background:#7a8fa0"></i>seasonal-naive = same quarter last year</span><span class="rv" data-s="2"><i class="lg" style="background:var(--sea)"></i>RF → GAMM</span></div>
</div>
<div class="abs card" style="left:1380px;top:270px;width:430px;height:680px;padding:22px 26px">
 <div class="lab" style="color:var(--sea)">Error on Test quarters</div>
 <div id="e-metrics" style="margin-top:12px"></div>
 <div class="cite" style="margin-top:10px">Hyndman &amp; Athanasopoulos (2021)</div>
</div>
{notes(f"""Default split is our proposed 70/15/15 by time: Train {TR[0]}–{TR[1]} ({TR[2]} quarters), Tune {TU[0]}–{TU[1]} ({TU[2]}), Test {TE[0]}–{TE[1]} ({TE[2]}). [→] The seasonal-naive baseline will forecast each quarter with the same quarter last year (Hyndman & Athanasopoulos, 2021). [→] The RF → GAMM workflow will be scored on the same Test quarters with MAE, RMSE and MASE; MASE below 1 means it beats the in-sample seasonal-naive error. Drag the slider to move the test start (Tune stays 14 quarters), or play a rolling-origin evaluation (Hewamalage et al., 2023). If the workflow does not beat the baseline, we will report that. Values are illustrative.""")}
</section>''')
# ================= B4 VALUE AT RISK BUILDER (moved from main flow) =================
S.append(f'''<section class="slide backup uw" id="s-var" data-label="B4" data-title="Backup · Value-at-risk builder" data-sec="6" data-steps="3" data-q="value">
{hd("B4","Backup · Valuation","Gross Landing <em>Value at Risk</em>")}
<div class="abs card" style="left:110px;top:260px;width:800px;height:700px;padding:22px 26px">
 <div style="display:flex;justify-content:space-between;align-items:center"><div class="lab">Pick a province × category</div><span class="ill">ILLUSTRATIVE</span></div>
 <div id="v-pick" style="display:flex;gap:8px;flex-wrap:wrap;margin-top:10px"></div>
 <svg id="v-chart" width="750" height="200" style="margin-top:8px"></svg>
 <div class="eqrow">
  <div class="eq rv" data-s="1"><div class="lab">Shortfall</div><div class="ev" id="v-sf">–</div><div class="small">below benchmark</div></div>
  <div class="op rv" data-s="2">×</div>
  <div class="eq rv" data-s="2"><div class="lab">Price</div><div class="ev" id="v-pr">–</div><input type="range" id="v-price" min="-30" max="30" value="0" style="width:160px;margin-top:6px"><div class="small" id="v-prl">first-sale</div></div>
  <div class="op rv" data-s="2">=</div>
  <div class="eq rv hl" data-s="2"><div class="lab" style="color:#fff">At risk</div><div class="ev" id="v-val" style="color:#fff">–</div><div class="small" style="color:#d9f6fa">not profit</div></div>
 </div>
</div>
<div class="abs card rv" data-s="3" style="left:940px;top:260px;width:870px;height:700px;padding:22px 26px">
 <div style="display:flex;justify-content:space-between;align-items:center"><div class="lab" style="color:var(--sea)">Ranking · price check</div>
 <div style="display:flex;gap:8px"><button class="chip on" data-p="base">First-sale</button><button class="chip" data-p="proxy">Proxy</button></div></div>
 <div id="v-rank" style="position:relative;height:450px;margin-top:16px"></div>
 <div class="small" id="v-stab"></div>
</div>
{notes("""Gross landing value: for each province and quarter, we will multiply the tonnes landed in each fish category by the matching historical first-sale price for the same period and province.
[→] Value at risk will work on the shortfall only: the seasonal benchmark minus the forecast, when the forecast is below it; otherwise zero.
[→] We will multiply the shortfall in tonnes, times 1,000 for kilograms, by the matching price. That is the gross landing value at risk: gross value at stake, not profit or household income loss. Where first-sale prices are missing, we will use unit-value proxies (production value divided by volume; PSA, 2026).
[→] Then we will rank the province–category combinations and check whether the ranking holds when we switch price source or move the price up or down. Values are illustrative.""")}
</section>''')
# ================= REFERENCES =================
APA=[
"Agaton, C. B., Guno, C. S., Labog, R. A., &amp; Collera, A. A. (2023). Immediate socioeconomic impacts of Mindoro oil spill on fisherfolk of Naujan, Philippines. <i>Resources, 12</i>(9), Article 102. https://doi.org/10.3390/resources12090102",
"Benavides, I. F., Santacruz, M., Romero-Leiton, J. P., Barreto, C., &amp; Selvaraj, J. J. (2023). Assessing methods for multiple imputation of systematic missing data in marine fisheries time series with a new validation algorithm. <i>Aquaculture and Fisheries</i>. https://doi.org/10.1016/j.aaf.2021.12.013",
"Bokingkito, P., Jaroensutasinee, K., &amp; Jaroensutasinee, M. (2026). Explainable AI-driven machine learning for forecasting marine fisheries production using environmental predictors. <i>Machine Learning and Knowledge Extraction, 8</i>(7), Article 197. https://doi.org/10.3390/make8070197",
"Food and Agriculture Organization of the United Nations. (2024). <i>The state of world fisheries and aquaculture 2024: Blue transformation in action</i>. FAO. https://doi.org/10.4060/cd0683en",
"Gahtan, J., Knapp, K. R., Schreck, C. J., III, Diamond, H. J., Kossin, J. P., &amp; Kruk, M. C. (2024). <i>International Best Track Archive for Climate Stewardship (IBTrACS) project, version 4r01</i> [Data set]. NOAA National Centers for Environmental Information. https://doi.org/10.25921/82ty-9e16",
"Hewamalage, H., Ackermann, K., &amp; Bergmeir, C. (2023). Forecast evaluation for data scientists: Common pitfalls and best practices. <i>Data Mining and Knowledge Discovery, 37</i>(2), 788–832. https://doi.org/10.1007/s10618-022-00894-5",
"Holmes, E. E., BR, S., Nimit, K., Maity, S., Checkley, D. M., Jr., Wells, M. L., &amp; Trainer, V. L. (2021). Improving landings forecasts using environmental covariates: A case study on the Indian oil sardine (<i>Sardinella longiceps</i>). <i>Fisheries Oceanography, 30</i>(6), 623–642. https://doi.org/10.1111/fog.12541",
"Huang, B., Liu, C., Banzon, V., Freeman, E., Graham, G., Hankins, B., Smith, T., &amp; Zhang, H.-M. (2021). Improvements of the Daily Optimum Interpolation Sea Surface Temperature (DOISST) version 2.1. <i>Journal of Climate, 34</i>(8), 2923–2939. https://doi.org/10.1175/JCLI-D-20-0166.1",
"Huffman, G. J., Stocker, E. F., Bolvin, D. T., Nelkin, E. J., &amp; Tan, J. (2023). <i>GPM IMERG Final Precipitation L3 Half Hourly 0.1 degree x 0.1 degree V07</i> [Data set]. NASA Goddard Earth Sciences Data and Information Services Center. https://doi.org/10.5067/GPM/IMERG/3B-HH/07",
"Hyndman, R. J., &amp; Athanasopoulos, G. (2021). <i>Forecasting: Principles and practice</i> (3rd ed.). OTexts. https://otexts.com/fpp3/",
"Nesslage, G., Lyubchich, V., Nitschke, P., Williams, E., Grimes, C., &amp; Wiedenmann, J. (2021). Environmental drivers of golden tilefish (<i>Lopholatilus chamaeleonticeps</i>) commercial landings and catch-per-unit-effort. <i>Fisheries Oceanography, 30</i>(5), 608–622. https://doi.org/10.1111/fog.12540",
"Noy, I., Lacheheb, M., &amp; Pundit, M. (2023). <i>The impact of tropical cyclones on fishing activities in the Philippines</i> [Working paper]. Asian Development Bank. https://doi.org/10.22617/wps230291-2",
"Oceana. (2026). <i>Net loss: How governance gaps are sinking Philippine fisheries</i> [Report]. Zenodo. https://doi.org/10.5281/zenodo.18320988",
"Philippine Statistics Authority. (2026). <i>Marine municipal fisheries: Volume and value of production by geolocation, species, year and quarter</i> [Data sets, Tables 0032E4GVMP0 and 0042E4GCMP0]. PSA OpenSTAT. https://openstat.psa.gov.ph/"]
FOUND=[
"Breiman, L. (2001). Random forests. <i>Machine Learning, 45</i>(1), 5–32. https://doi.org/10.1023/A:1010933404324",
"Hyndman, R. J., &amp; Koehler, A. B. (2006). Another look at measures of forecast accuracy. <i>International Journal of Forecasting, 22</i>(4), 679–688. https://doi.org/10.1016/j.ijforecast.2006.03.001",
"Republic Act No. 10654. (2015). <i>An act to prevent, deter and eliminate illegal, unreported and unregulated fishing, amending Republic Act No. 8550, otherwise known as \u201cThe Philippine Fisheries Code of 1998,\u201d and for other purposes</i>. https://lawphil.net/statutes/repacts/ra2015/ra_10654_2015.html",
"Wood, S. N. (2017). <i>Generalized additive models: An introduction with R</i> (2nd ed.). Chapman and Hall/CRC. https://doi.org/10.1201/9781315370279"]
half=7
r1="".join(f'<p class="apa">{a}</p>' for a in APA[:half]);r2="".join(f'<p class="apa">{a}</p>' for a in APA[half:])
rf="".join(f'<p class="apa">{a}</p>' for a in FOUND)
S.append(f'''<section class="slide backup" id="b-refs" data-label="B5" data-title="Backup · References (1/2)" data-sec="6" data-steps="0">
{hd("B5","Backup · References 1 of 2","References <em>(APA 7)</em>")}
<div class="abs" style="left:110px;top:250px;width:1700px;columns:2;column-gap:60px">{r1}</div>
<aside class="notes">Reference list, part 1 (A–Ho). All sources are 2020 or later. Holmes et al. (2021) is a method reference (Indian oil sardine), not a Philippine study.</aside>
</section>''')
S.append(f'''<section class="slide backup" id="b-refs2" data-label="B6" data-title="Backup · References (2/2)" data-sec="6" data-steps="0">
{hd("B6","Backup · References 2 of 2","References <em>(continued)</em>")}
<div class="abs" style="left:110px;top:250px;width:1700px;columns:2;column-gap:60px">{r2}</div>
<div class="abs" style="left:110px;top:760px;width:1700px"><div class="lab" style="color:var(--coral)">Foundational &amp; legal sources · pre-2020, listed separately</div>
<div style="columns:2;column-gap:60px;margin-top:12px">{rf}</div></div>
<aside class="notes">Part 2. The foundational sources (Breiman, 2001; Wood, 2017; Hyndman &amp; Koehler, 2006) and the law (RA 10654, 2015) predate our 2020+ rule; they are listed separately as original method and legal definitions. The slides cite 2020+ applications instead.</aside>
</section>''')
