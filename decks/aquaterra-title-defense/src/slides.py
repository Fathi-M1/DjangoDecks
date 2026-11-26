TITLE="AquaTerra: Forecasting Municipal Fish Landing Shortfalls and Estimating Gross Landing Value at Risk in Selected Philippine Coastal Provinces"
SUB="Forecasting Municipal Fish Landing Shortfalls and Estimating Gross Landing Value at Risk in Selected Philippine Coastal Provinces"
def waveH(fill="#ffffff",h=120,flip=False,op=1):
    d="M0,60 C320,10 640,110 960,60 C1280,10 1600,110 1920,60 L1920,120 L0,120Z"
    t=' style="transform:scaleY(-1)"' if flip else ''
    return f'<svg viewBox="0 0 1920 120" preserveAspectRatio="none" width="1920" height="{h}"{t}><path d="{d}" fill="{fill}" opacity="{op}"/><path d="M0,74 C320,24 640,124 960,74 C1280,24 1600,124 1920,74" stroke="{fill}" stroke-opacity=".5" stroke-width="3" fill="none"/></svg>'
def hd(num,kick,h,extra=""):
    return f'<div class="hd"><div class="num">{num}</div><div><div class="kick">{kick}</div><h2 style="margin-top:12px">{h}</h2></div>{extra}</div>'
def notes(t): return f'<aside class="notes">{t.strip()}</aside>'
S=[]
# ---------------- 0 COVER / HOOK (also carries the title & key terms) ----------------
terms=[("municipal","Municipal","<b>Type of fishing operation</b>, not a location: fishing without boats or with boats of <b>3 gross tons or less</b> (PSA classification). Records are grouped by <b>province</b>."),
("landings","Landings","Fish caught at sea and <b>brought ashore</b>. We measure the <b>metric tons</b> landed in each province during each quarter."),
("quarter","Quarter","<b>Q1</b> Jan–Mar · <b>Q2</b> Apr–Jun · <b>Q3</b> Jul–Sep · <b>Q4</b> Oct–Dec. PSA publishes the records quarterly."),
("mangrove","Mangrove cover change","Historical increases or decreases in mangrove cover, derived from <b>Landsat satellite imagery</b>. Tested as a <b>predictor</b>; not assumed to cause anything."),
("var","Gross landing value at risk","<b>Projected shortfall × matching historical first-sale price</b>. Gross revenue tied to the missing landings, not income, profit or damage.")]
chips="".join(f'<button class="chip term" data-t="{k}">{n}</button>' for k,n,_ in terms)
pops="".join(f'<div class="pop" id="pop-{k}" style="left:1080px;top:330px;width:640px"><div class="lab" style="color:var(--sea);margin-bottom:8px">{n}</div>{t}</div>' for k,n,t in terms)
S.append(f'''<section class="slide" id="s-hook" data-label="00" data-title="Cover · AquaTerra" data-sec="-1" data-steps="3" data-q="title">
<div class="abs imgframe" style="left:1080px;top:70px;width:730px;height:540px;background-image:url({{{{IMG:hero}}}})"></div>
<div class="abs" style="left:110px;top:80px;width:910px">
 <div class="kick">Title Defense · Group DJANGO · BS CS – Data Science · FEU Tech</div>
 <p style="font:400 34px/1.35 PF;margin-top:40px;color:var(--ink)">Fish provides food for our families and supports the livelihoods of coastal communities.</p>
 <p class="rv" data-s="1" style="font:400 34px/1.35 PF;margin-top:20px;color:var(--ink)">Behind every catch are fishers, vendors, and businesses that depend on a steady supply.</p>
 <p class="rv" data-s="2" style="font:600 italic 50px/1.18 PF;margin-top:30px;color:var(--sea)">Can historical fisheries and environmental data help us anticipate when that supply may <span style="color:var(--coral)">fall short?</span></p>
</div>
<div class="abs rv" data-s="3" style="left:0;right:0;bottom:0;height:430px">
 <div class="abs" style="top:0;left:0">{waveH("#e6f6f3",120)}</div>
 <div class="abs" style="top:118px;left:0;right:0;bottom:0;background:#e6f6f3"></div>
 <div class="abs" style="left:110px;top:92px;display:flex;gap:44px;align-items:flex-start;width:1700px">
  <div class="num" style="font-size:190px">00</div>
  <div style="padding-top:14px"><div class="kick">Our proposed study</div>
  <div style="font:700 92px/1 PF;color:var(--ink);margin-top:10px">AquaTerra<span style="color:var(--sea)">:</span></div>
  <div style="font:500 30px/1.32 PF;color:var(--ink2);margin-top:12px;width:1320px">{SUB}</div>
  <div style="display:flex;flex-wrap:wrap;gap:10px;margin-top:16px;align-items:center"><span class="lab" style="margin-right:6px">Key terms · click</span>{chips}</div></div>
 </div>
</div>
{pops}
{notes("""Fish provides food for our families and supports the livelihoods of coastal communities. [→] Behind every catch are fishers, vendors, and businesses that depend on a steady supply. [→] This makes understanding changes in fish landings important. Can historical fisheries and environmental data help us anticipate periods when that supply may fall short? [→] Good day, respected panelists. We are Group Django, and today we present our proposed study, 'AquaTerra: Forecasting Municipal Fish Landing Shortfalls and Estimating Gross Landing Value at Risk in Selected Philippine Coastal Provinces.'
'Municipal' describes the type of fishing operation: no boat, or a small boat of three gross tons or less; our records are grouped by province. 'Landings' means the catch brought ashore, in metric tons per province per quarter. (Click a key term to define it; press Q for the panel questions on the title.)""")}
</section>''')
# ---------------- 3 BACKGROUND ----------------
S.append(f'''<section class="slide" id="s-bg" data-label="03" data-title="I · Background" data-sec="0" data-steps="4" data-q="bg" data-r="bg">
<div class="bgimg" style="background-image:url({{{{IMG:mangrove}}}});bottom:auto;height:470px"></div>
<div class="full" style="bottom:auto;height:470px;background:linear-gradient(180deg,rgba(2,40,58,.55),rgba(2,40,58,.15))"></div>
<div class="abs" style="left:110px;top:70px;display:flex;gap:34px;align-items:flex-end;color:#fff">
 <div class="num w">01</div><div><div class="kick" style="color:#e6fff9">I · Background</div>
 <h2 style="margin-top:12px;color:#fff;font-size:60px">Fish supports coastal livelihoods,<br>and national production <em style="color:#ffcdbd">is declining.</em></h2></div></div>
<div class="abs" style="left:0;top:380px">{waveH("#ffffff",110)}</div>
<div class="abs" style="left:0;right:0;top:488px;bottom:0;background:#ffffff"></div>
<div class="abs rv" data-s="1" style="left:110px;top:470px;width:520px">
 <div class="lab" style="color:var(--sea)">1 · Why it matters</div>
 <p class="body" style="margin-top:12px">Small-scale fisheries are an important source of <b>rural livelihoods</b>.</p><div class="cite">FAO (2024)</div>
 <p class="body" style="margin-top:16px">Municipal fisherfolk in <b>Magallanes, Sorsogon</b> faced income and food-security difficulties during COVID-19.</p><div class="cite">Dumilag et al. (2023)</div>
</div>
<div class="abs rv" data-s="2" style="left:690px;top:470px;width:560px">
 <div class="lab" style="color:var(--coral)">2 · The decline</div>
 <div style="display:flex;align-items:baseline;gap:14px;margin-top:6px"><span style="font:700 100px/1 PF;color:var(--coral)" id="oc-num">~45M</span><span style="font:600 34px PF;color:var(--ink)">kg / year</span></div>
 <p class="body" style="margin-top:4px">average decline in Philippine <b>capture fisheries production</b>, 2010–2023</p>
 <svg width="560" height="136" viewBox="0 0 560 136" style="margin-top:8px"><line x1="40" y1="40" x2="520" y2="40" class="ax"/><line x1="40" y1="100" x2="520" y2="100" class="ax"/>
 <path id="oc-line" d="M40,40 L520,100" stroke="var(--coral)" stroke-width="5" fill="none" stroke-dasharray="12 9"/>
 <circle cx="40" cy="40" r="9" fill="var(--sea)"/><circle cx="520" cy="100" r="9" fill="var(--coral)"/>
 <text x="30" y="22" font-size="21" font-weight="700" fill="#0b2a3c">2010 · 2.6M mt</text><text x="530" y="132" font-size="21" font-weight="700" fill="#0b2a3c" text-anchor="end">2023 · 1.9M mt</text></svg>
 <div class="cite">Oceana (2026) · national estimate, municipal + commercial; not province-level shortfalls</div>
</div>
<div class="abs rv" data-s="3" style="left:1310px;top:470px;width:500px">
 <div class="lab" style="color:var(--sea)">3 · Forecasting so far</div>
 <p class="body" style="margin-top:12px">A regional framework for commercial and marine municipal fisheries, comparing algorithms explained with SHAP.</p><div class="cite">Bokingkito et al. (2026)</div>
 <p class="body" style="margin-top:16px">Environmental predictors must be tested on <b>unseen observations</b>.</p><div class="cite">Holmes et al. (2021)</div>
</div>
<div class="abs rv" data-s="4" style="left:110px;right:110px;top:862px;padding:18px 28px;border-radius:16px;background:var(--ink);color:#fff;font:500 25px/1.4 IN">
 <span class="lab" style="color:var(--aqua)">The concern&nbsp;&nbsp;</span>Can forecasts reliably flag shortfall periods and the province–category combinations with the most value at stake?</div>
{notes("""Fishing provides food, employment and income for Philippine coastal communities. FAO (2024) identifies small-scale fisheries as an important source of rural livelihoods. In the Philippine setting, Dumilag et al. (2023) documented income and food-security difficulties among municipal fisherfolk in Magallanes, Sorsogon during COVID-19.
[→] The concern is reinforced by declining production. Oceana (2026) reports that Philippine capture fisheries production declined by about 45 million kilograms per year on average from 2010 to 2023, from about 2.6 to 1.9 million metric tons. This is a national estimate, municipal and commercial combined, separate from the province-level seasonal shortfalls we study.
[→] Bokingkito et al. (2026) developed a regional forecasting framework covering commercial and marine municipal fisheries, comparing algorithms and explaining outputs with SHAP. Holmes et al. (2021) show environmental predictors should be tested for their contribution on unseen observations.
[→] So the concern is whether forecasts can reliably identify shortfall periods and economically significant province–category combinations, using documented historical first-sale prices and sensitivity analysis.""")}
</section>''')
# ---------------- 4 OBJECTIVES ----------------
RQ=["What historical seasonal benchmarks identify landing shortfalls by province and fish category?",
"Which predictors are useful for GAMM forecasting, and do mangrove history and prior typhoon exposure improve accuracy?",
"What gross landing value is associated with projected shortfalls, using historical first-sale reference prices?",
"How reliably are economically significant shortfalls identified on unseen quarters, and how sensitive are estimates and rankings to alternative prices?"]
SO=[("Prepare","the dataset and seasonal benchmarks from quarterly landings, environmental information and historical reference prices"),
("Forecast & evaluate","against a seasonal baseline with MAE, RMSE and MASE, including the added predictive value of mangrove history and prior typhoon exposure"),
("Value exposure","calculate shortfalls, estimate gross landing value at risk, and rank province–category combinations"),
("Validate & present","shortfall detection and rankings on unseen quarters, alternative price assumptions, planning dashboard"),
("Seek collaboration","with DTI or a relevant fisheries agency to review data suitability and practical usefulness")]
rqh="".join(f'<button class="abs rq" data-i="{i}" style="left:110px;top:{372+i*132}px"><span>RQ{i+1}</span><div>{q}</div></button>' for i,q in enumerate(RQ))
soh="".join(f'<div class="abs so" data-i="{i}" style="left:1060px;top:{372+i*104}px"><span>{i+1}</span><div><b>{h}</b><div>{m}</div></div></div>' for i,(h,m) in enumerate(SO))
S.append(f'''<section class="slide uw" id="s-obj" data-label="04" data-title="II · Objectives" data-sec="1" data-steps="4" data-q="obj">
<div class="rays" style="opacity:.6"></div>
{hd("02","II · Objectives","Four questions, <em>five specific objectives.</em>")}
<div class="abs" style="left:110px;top:262px;width:1700px;font:400 22px/1.45 IN;color:var(--ink2)"><span class="lab" style="color:var(--sea)">General objective&nbsp;&nbsp;</span>Develop and evaluate <b>AquaTerra</b>, using Random Forest for predictor selection and GAMM for next-quarter municipal fish landing forecasts, then estimate supply shortfalls and gross landing value at risk to support planning in selected Philippine coastal provinces.</div>
<div class="abs lab" style="left:110px;top:345px">Research questions · click one</div><div class="abs lab" style="left:1060px;top:345px">Specific objectives</div>
{rqh}<svg class="abs" id="rqlines" style="left:880px;top:372px" width="180" height="540"></svg>{soh}
{notes("""The general objective is to develop and evaluate AquaTerra: Random Forest for predictor selection and GAMM for next-quarter forecasts, then estimate supply shortfalls and gross landing value at risk.
We answer four questions [click each]. RQ1: what seasonal benchmarks identify shortfalls. RQ2: which predictors help GAMM, and do mangrove history and prior typhoon exposure improve accuracy. RQ3: what gross landing value goes with projected shortfalls. RQ4: how reliably are significant shortfalls identified on unseen quarters, and how price-sensitive are the rankings.
Five specific objectives: prepare data and benchmarks; implement and evaluate the forecasting workflow; develop the economic exposure module; validate and present through a dashboard; and seek collaboration with DTI or a relevant fisheries agency.""")}
</section>''')
# ---------------- 5 SCOPE & LIMITATION ----------------
SC=[("Study area · marine municipal landings","Palawan, Misamis Occidental, Negros Oriental, Tawi-Tawi, Zamboanga del Norte, Davao de Oro × five fish categories; final coverage depends on complete, compatible records"),
("Public secondary data","PSA OpenSTAT · Landsat satellite imagery (mangrove cover) · NASA IMERG · NOAA OISST · NOAA IBTrACS"),
("RF → GAMM forecasts","next quarter; tests mangrove history and prior typhoon exposure beyond landings, seasonality, rainfall, SST"),
("Shortfalls & exposure","vs historical seasonal benchmarks × historical reference prices → exposure rankings"),
("Evaluation & dashboard","later quarters held out · web dashboard · consultation sought with DTI or a fisheries agency")]
LM=[("Selected coverage","Excludes commercial fisheries, aquaculture and inland municipal fisheries. No field catch monitoring, mangrove surveys or sensors."),
("Next quarter only","Data gaps, publication delays and inconsistent records may affect coverage and accuracy. Fishing effort, fuel costs and policy changes are not modeled where records are unavailable."),
("No causal claims","We test whether mangrove history and typhoon exposure help predict landings. That does not establish that they cause shortfalls."),
("Gross value only","Historical reference prices. No future price prediction, household income loss, business profit or disaster damage. Unit-value proxies may reflect catch composition and quality."),
("Research prototype","No guaranteed real-time updates or deployment. Consultation depends on agency availability; adoption is not guaranteed.")]
sch="".join(f'<div class="li"><i>✓</i><div><b>{a}</b><span>{b}</span></div></div>' for a,b in SC)
lmh="".join(f'<button class="li lm" data-i="{i}"><i>✕</i><div><b>{a}</b><span>{b}</span></div></button>' for i,(a,b) in enumerate(LM))
S.append(f'''<section class="slide" id="s-scope" data-label="05" data-title="III · Scope and Limitation" data-sec="2" data-steps="2" data-q="scope">
<div class="abs" style="left:110px;top:64px;display:flex;gap:34px;align-items:flex-end"><div class="num">03</div><div><div class="kick">III · Scope and Limitation</div><h2 style="margin-top:12px;font-size:56px">What we <em>cover</em>, and what we <span class="c">don't claim.</span></h2></div></div>
<div class="abs" id="sl-tog" style="right:110px;top:120px;display:flex;gap:8px"><button class="chip" data-v="scope">Scope</button><button class="chip cor" data-v="lim">Limitation</button><button class="chip on" data-v="both">Both</button></div>
<div class="abs glass colA" data-s="1" style="left:110px;top:290px;width:830px;height:640px;padding:26px 30px"><div class="lab" style="color:var(--sea)">Scope</div>{sch}</div>
<div class="abs glass colB rv" data-s="2" style="left:980px;top:290px;width:830px;height:640px;padding:26px 30px"><div class="lab" style="color:var(--coral)">Limitation · click an item to focus</div>{lmh}</div>
{notes("""Scope: forecasting marine municipal fish landings and assessing economic exposure in six Philippine coastal provinces (Palawan, Misamis Occidental, Negros Oriental, Tawi-Tawi, Zamboanga del Norte and Davao de Oro), using publicly accessible secondary data: PSA OpenSTAT, Landsat satellite imagery for mangrove cover, NASA IMERG, NOAA OISST and NOAA IBTrACS. Random Forest for predictor selection, then GAMM for next-quarter forecasts; compare with seasonal benchmarks, value shortfalls with historical reference prices, evaluate on later quarters, show results on a web dashboard, and seek consultation with DTI or a relevant fisheries agency.
[→] Limitations: selected provinces and marine municipal categories only; no commercial, aquaculture or inland; no field monitoring. Next quarter only; gaps and delays may affect accuracy. We will not establish causal effects of mangrove change or typhoons. Gross landing value at risk uses historical prices, not income, profit or damage. The dashboard is a research prototype and adoption is not guaranteed.""")}
</section>''')
# ---------------- 6–7 DATA-FLOW PIPELINE (two slides) ----------------
from flow import FLOW
S.extend(FLOW)
def demohd(k,h): return hd("04",f"IV · Algorithm Justification · {k}",h)
# ---------------- 7 RF DEMO ----------------
S.append(f'''<section class="slide uw" id="s-rf" data-label="07" data-title="IV.1 · Random Forest demo" data-sec="3" data-steps="3" data-q="algo">
<div class="rays" style="opacity:.5"></div>
{demohd("Random Forest","Many trees vote; <em>importance</em> ranks the predictors.")}
<div class="abs card" style="left:110px;top:270px;width:520px;height:600px;padding:26px 28px">
 <div class="lab" style="color:var(--sea)">How it works</div>
 <ol class="steps-l"><li data-k="1"><b>Grow the forest.</b> Each tree learns from a bootstrap sample of training quarters and a random subset of predictors.</li>
 <li data-k="2"><b>Rank predictors.</b> Shuffle one predictor at a time; the bigger the error increase, the more important it is.</li>
 <li data-k="3"><b>Pass the top ones on.</b> Only the selected predictors go into the GAMM.</li></ol>
 <div style="display:flex;gap:10px;margin-top:18px;flex-wrap:wrap"><button class="btn" id="rf-grow">🌳 Grow forest</button><button class="btn ghost" id="rf-rank">Rank</button><button class="btn ghost" id="rf-boot">New bootstrap</button></div>
 <div class="pnote" style="margin-top:18px">Importance = predictive usefulness, not cause</div>
</div>
<div class="abs card" style="left:660px;top:270px;width:1150px;height:600px;padding:22px 26px">
 <div style="display:flex;justify-content:space-between;align-items:center"><div class="lab">Forest · one example quarter</div><span class="ill">ILLUSTRATIVE</span></div>
 <svg id="rf-trees" width="1100" height="170" style="margin-top:4px"></svg>
 <div id="rf-vote" class="small" style="margin-top:0;height:28px;color:var(--ink2)"></div>
 <div style="display:flex;justify-content:space-between;align-items:center;margin-top:8px"><div class="lab">Predictor importance</div>
  <div style="display:flex;align-items:center;gap:12px;font:600 17px IN;color:var(--ink2)">Pass top <b id="rf-kv" style="font-size:22px;color:var(--coral)">4</b> to GAMM <input type="range" id="rf-k" min="1" max="7" value="4" style="width:200px"></div></div>
 <div id="rf-bars" style="position:relative;height:300px;margin-top:10px"></div>
</div>
{notes("""Random Forest is an ensemble of decision trees. [→ Grow] Each tree learns from a bootstrap sample of the training quarters and a random subset of predictors; the forest averages the trees' predictions.
[→ Rank] To rank predictors, we shuffle one predictor at a time and see how much the error increases; larger increases mean more useful predictors.
[→ Pass] The top predictors go to the GAMM. Correlations alone can miss nonlinear patterns, which is why Nesslage et al. (2021) used Random Forest importance to guide GAMM construction.
These numbers are illustrative. Importance means predictive usefulness, not cause.""")}
</section>''')
# ---------------- 8 GAMM DEMO ----------------
S.append(f'''<section class="slide uw" id="s-gamm" data-label="08" data-title="IV.2 · GAMM demo" data-sec="3" data-steps="4" data-q="algo">
<div class="rays" style="opacity:.5"></div>
{demohd("GAMM","Smooth curves <em>add up</em> to the forecast.")}
<div class="abs card" style="left:110px;top:270px;width:560px;height:600px;padding:22px 26px">
 <div class="lab" style="color:var(--sea)">Generalized Additive Mixed Model</div>
 <div id="g-formula" style="font:500 21px/1.6 IN;color:var(--ink2);margin-top:10px"></div>
 <div class="lab" style="margin-top:14px">Terms · click to add or remove</div>
 <div id="g-terms" style="display:grid;grid-template-columns:1fr 1fr;gap:10px;margin-top:10px"></div>
 <div class="lab" style="margin-top:16px">Random effects</div>
 <div style="display:flex;gap:10px;margin-top:8px;align-items:center"><button class="chip" id="g-re">Off</button><span class="small">level shifts per province & category</span></div>
 <div id="g-grp" style="display:flex;gap:8px;margin-top:10px;flex-wrap:wrap"></div>
</div>
<div class="abs card" style="left:700px;top:270px;width:1110px;height:600px;padding:20px 24px">
 <div style="display:flex;justify-content:space-between;align-items:center"><div class="lab" id="g-title">Landings (mt) · Province A · Category 1</div><span class="ill">ILLUSTRATIVE</span></div>
 <svg id="g-main" width="1060" height="330" style="margin-top:6px"></svg>
 <div style="display:flex;gap:14px;margin-top:4px" id="g-small"></div>
 <div style="display:flex;justify-content:space-between;margin-top:6px"><div class="small" id="g-err"></div><div class="small">dots = observed · line = model · <span style="color:var(--coral);font-weight:700">◆ next-quarter forecast</span></div></div>
</div>
{notes("""GAMM stands for Generalized Additive Mixed Model. [→] It adds a smooth seasonal curve for the quarter, [→] then smooth, possibly nonlinear curves for the predictors that Random Forest passed on, such as sea surface temperature, rainfall or lagged landings. [→] The 'mixed' part adds random effects, a level shift for each province and fish category, so groups can differ without fitting a separate model for each. [→] The sum gives the next-quarter forecast. All curves here are illustrative.""")}
</section>''')
# ---------------- 9 BASELINE vs MODEL ----------------
S.append(f'''<section class="slide uw" id="s-eval" data-label="09" data-title="IV.3 · Baseline vs model" data-sec="3" data-steps="2" data-q="algo">
<div class="rays" style="opacity:.5"></div>
{demohd("Evaluation","The workflow must beat the <span class='c'>seasonal baseline</span> on unseen quarters.")}
<div class="abs card" style="left:110px;top:270px;width:1240px;height:600px;padding:20px 26px">
 <div style="display:flex;justify-content:space-between;align-items:center"><div class="lab">Landings (mt) · one province × category</div><span class="ill">ILLUSTRATIVE</span></div>
 <svg id="e-chart" width="1190" height="400" style="margin-top:6px"></svg>
 <div style="display:flex;align-items:center;gap:18px;margin-top:6px;font:600 18px IN;color:var(--ink2)">Test starts at <b id="e-lab" style="color:var(--coral);min-width:90px">2024 Q1</b>
 <input type="range" id="e-split" min="12" max="24" value="20" style="flex:1"><button class="btn ghost" id="e-roll">▶ Rolling origin</button></div>
 <div style="display:flex;gap:22px;margin-top:10px;font:600 16px IN;color:var(--ink2)"><span><i class="lg" style="background:#a9bfc6"></i>observed</span><span class="rv" data-s="1"><i class="lg" style="background:#7a8fa0"></i>seasonal baseline = same quarter last year</span><span class="rv" data-s="2"><i class="lg" style="background:var(--sea)"></i>RF → GAMM workflow</span></div>
</div>
<div class="abs card" style="left:1380px;top:270px;width:430px;height:600px;padding:22px 26px">
 <div class="lab" style="color:var(--sea)">Error on test quarters</div>
 <div id="e-metrics" style="margin-top:12px"></div>
 <div class="small" style="margin-top:14px"><b>MAE</b>: typical miss in mt · <b>RMSE</b>: punishes big misses · <b>MASE</b> &lt; 1 beats the in-sample seasonal-naive error.</div>
 <div class="small" style="margin-top:10px">Selection and tuning stay inside training data. If the workflow doesn't beat the baseline, we report that.</div>
</div>
{notes("""We compare the complete workflow against a seasonal baseline: the observed landings from the same quarter of the previous year. [→] The test quarters are later quarters excluded from training and tuning; drag the slider to move the split, or play the rolling-origin evaluation. [→] MAE tells us the typical miss in metric tons, RMSE highlights larger mistakes, and MASE lets us compare across differently sized series. If the workflow adds little over the baseline, we would not recommend it for operational use. Values are illustrative.""")}
</section>''')
# ---------------- 10 WITH vs WITHOUT ----------------
S.append(f'''<section class="slide uw" id="s-contrib" data-label="10" data-title="IV.4 · Predictive contribution" data-sec="3" data-steps="2" data-q="algo">
<div class="rays" style="opacity:.5"></div>
{demohd("Contribution test","Do mangrove history and typhoons <em>improve the forecast?</em>")}
<div class="abs card" style="left:110px;top:270px;width:520px;height:600px;padding:24px 28px">
 <div class="lab" style="color:var(--sea)">Two models, same test quarters</div>
 <div class="mbox" id="c-A"><b>Model A</b><span>past landings · seasonality · rainfall · SST</span></div>
 <div class="mbox" id="c-B"><b>Model B</b><span>Model A <b style="color:var(--coral)">+ mangrove history + prior typhoon exposure</b></span></div>
 <div class="lab" style="margin-top:20px">Show</div>
 <div style="display:flex;gap:10px;margin-top:8px"><button class="chip" data-m="A">Without</button><button class="chip" data-m="B">With</button><button class="chip on" data-m="AB">Both</button></div>
 <div class="lab" style="margin-top:18px">Possible result</div>
 <div style="display:flex;gap:10px;margin-top:8px"><button class="chip on" data-r="help">They help</button><button class="chip" data-r="none">No improvement</button></div>
 <div class="pnote" style="margin-top:18px;display:flex">Predictive, not causal: better accuracy ≠ mangroves cause landings</div>
</div>
<div class="abs card" style="left:660px;top:270px;width:1150px;height:600px;padding:20px 24px">
 <div style="display:flex;justify-content:space-between;align-items:center"><div class="lab">Test quarters · forecasts vs observed</div><span class="ill">ILLUSTRATIVE</span></div>
 <svg id="c-chart" width="1100" height="330" style="margin-top:6px"></svg>
 <div id="c-bars" style="display:flex;gap:26px;margin-top:10px"></div>
 <div id="c-verdict" style="font:600 22px/1.35 PF;color:var(--ink);margin-top:12px"></div>
</div>
{notes("""To test predictive contribution we fit two models evaluated on the same unseen later quarters. [→] Model A uses past landings, seasonality, rainfall and SST. [→] Model B adds mangrove history and prior typhoon exposure. If Model B has lower MAE, RMSE and MASE, those predictors add predictive value. If not, we report that. Either way, better accuracy means predictive usefulness only. It does not prove mangroves or typhoons cause changes in landings. Values are illustrative.""")}
</section>''')
# ---------------- 11 VALUE AT RISK BUILDER ----------------
S.append(f'''<section class="slide uw" id="s-var" data-label="11" data-title="IV.5 · Value at risk builder" data-sec="3" data-steps="3" data-q="value">
<div class="rays" style="opacity:.5"></div>
{demohd("Valuation","Shortfall <span class='c'>×</span> historical price <em>=</em> gross landing value at risk.")}
<div class="abs card" style="left:110px;top:270px;width:760px;height:600px;padding:22px 26px">
 <div style="display:flex;justify-content:space-between;align-items:center"><div class="lab">Pick a province × category</div><span class="ill">ILLUSTRATIVE</span></div>
 <div id="v-pick" style="display:flex;gap:8px;flex-wrap:wrap;margin-top:10px"></div>
 <div style="margin-top:10px;font:500 15.5px/1.4 IN;color:var(--ink2);background:var(--mist);border-radius:10px;padding:8px 12px"><b style="color:var(--ink)">Gross landing value</b> = Σ landings per fish category × matching historical first-sale price (same period, same province)</div>
 <svg id="v-chart" width="710" height="190" style="margin-top:4px"></svg>
 <div class="eqrow">
  <div class="eq rv" data-s="1"><div class="lab">Shortfall</div><div class="ev" id="v-sf">–</div><div class="small">benchmark − forecast, if positive</div></div>
  <div class="op rv" data-s="2">×</div>
  <div class="eq rv" data-s="2"><div class="lab">Reference price</div><div class="ev" id="v-pr">–</div><input type="range" id="v-price" min="-30" max="30" value="0" style="width:180px;margin-top:6px"><div class="small" id="v-prl">historical first-sale</div></div>
  <div class="op rv" data-s="2">=</div>
  <div class="eq rv hl" data-s="2"><div class="lab" style="color:#fff">Value at risk</div><div class="ev" id="v-val" style="color:#fff">–</div><div class="small" style="color:#d9f6fa">not income or profit loss</div></div>
 </div>
</div>
<div class="abs card rv" data-s="3" style="left:900px;top:270px;width:910px;height:600px;padding:22px 26px">
 <div style="display:flex;justify-content:space-between;align-items:center"><div class="lab" style="color:var(--sea)">Exposure ranking · price sensitivity</div>
 <div style="display:flex;gap:8px"><button class="chip on" data-p="base">First-sale</button><button class="chip" data-p="proxy">Unit-value proxy</button></div></div>
 <div id="v-rank" style="position:relative;height:470px;margin-top:14px"></div>
 <div class="small" id="v-stab"></div>
</div>
{notes("""First, what is gross landing value? For each province and quarter, we take how much of each fish category was landed, multiply it by the matching historical first-sale price for the same period and province, and add it up.
[→] Value at risk works on the shortfall only. Our seasonal benchmark is the usual landing level for that province, fish category and quarter from earlier records. If the forecast is below it, the gap is the projected shortfall; if the forecast is above, the shortfall is zero.
[→] We multiply the shortfall in tons, times 1,000 for kilograms, by that same historical first-sale price. That is the gross landing value at risk: the gross revenue tied to the missing landings. It is not profit and not household income loss. Where first-sale prices are missing, we use unit-value proxies.
[→] Then we rank the province–category combinations. To defend the numbers, we switch price sources and move the price up or down, and check whether the ranking stays the same. Values here are illustrative.""")}
</section>''')
# ---------------- 13 CLIENTS ----------------
CL=[("LGUs & fisheries offices","Primary potential users","identify projected shortfalls, prioritize monitoring, and inform assessments of potential assistance needs"),
("BFAR","","supplementary information for fisheries monitoring and planning in the covered provinces"),
("DTI","","economic exposure estimates to inform consultations and planning for fisheries-related enterprises"),
("Fisherfolk associations & cooperatives","","seasonal supply outlooks for collective marketing, delivery coordination and discussions with agencies"),
("Traders, vendors & processors","","projected shortfalls to inform sourcing, purchasing and inventory planning")]
pos=[(110,280),(700,280),(1290,280),(400,560),(990,560)]
clh="".join(f'<div class="abs glass cl rv" data-s="{i+1}" style="left:{x}px;top:{y}px">{f"<span class=tg>{t}</span>" if t else ""}<div class="ch">{h}</div><div class="cm">{m}</div></div>' for i,((h,t,m),(x,y)) in enumerate(zip(CL,pos)))
S.append(f'''<section class="slide" id="s-clients" data-label="13" data-title="V · Potential Clients" data-sec="4" data-steps="5" data-q="clients">
<div class="abs" style="left:110px;top:64px;display:flex;gap:34px;align-items:flex-end"><div class="num">05</div><div><div class="kick">V · Potential Clients</div><h2 style="margin-top:12px;font-size:56px">Who could plan with <em>these estimates.</em></h2></div></div>
{clh}
<div class="abs" style="left:110px;right:110px;top:860px;padding:14px 24px;border-radius:14px;background:#fff7e0;border:2px solid var(--gold);font:600 21px/1.4 IN;color:#6b4a00">As stated in our proposal, we will seek consultation with DTI or a relevant fisheries agency to assess data suitability and practical usefulness. Participation and future adoption are not guaranteed.</div>
{notes("""Our primary potential users are LGUs and fisheries offices, which may use provincial and fish-category forecasts to identify projected shortfalls, prioritize monitoring and inform assessments of assistance needs. [→] BFAR may use the findings as supplementary information for monitoring and planning. [→] DTI may use exposure estimates to inform consultations with fisheries-related enterprises. [→] Fisherfolk associations and cooperatives may use seasonal supply outlooks for marketing and delivery coordination. [→] Traders, vendors and processors may use projected shortfalls for sourcing and inventory planning. We will seek consultation with DTI or a relevant agency; participation and adoption are not guaranteed.""")}
</section>''')
# ---------------- 14 THANK YOU ----------------
S.append(f'''<section class="slide" id="s-end" data-label="14" data-title="Thank you" data-sec="5" data-steps="0">
<div class="abs" style="left:0;right:0;top:120px;text-align:center">
 <div class="kick">Group DJANGO · AquaTerra</div>
 <div style="font:600 170px/1 PF;margin-top:24px;color:var(--ink)">Thank you</div>
 <div style="font:400 italic 38px PF;color:var(--sea);margin-top:20px">We welcome your questions and recommendations.</div>
 <div style="display:flex;gap:16px;justify-content:center;margin-top:44px">
  <button class="btn cor" data-go="b-qbank">? Panel Q&amp;A bank</button><button class="btn" data-go="b-cause">Prediction vs causation</button><button class="btn ghost" data-go="b-refs">References · APA 7</button></div>
</div>
<div class="abs imgframe" style="left:310px;top:640px;width:1300px;height:330px;background-image:url({{{{IMG:deep}}}})"></div>
{notes("""Thank you. We welcome your questions and recommendations. Backup slides: the panel Q&A bank, prediction vs causation, and the full reference list (press B for the slide menu).""")}
</section>''')
# ---------------- B1 Q BANK ----------------
S.append('''<section class="slide backup uw" id="b-qbank" data-label="B1" data-title="Backup · Panel Q&amp;A bank" data-sec="6" data-steps="0">
<div class="rays" style="opacity:.5"></div>
<div class="hd"><div class="num" style="font-size:150px">B1</div><div><div class="kick">Backup</div><h2 style="margin-top:12px;font-size:54px">Panel Q&amp;A bank, <em>grouped by theme.</em></h2></div></div>
<input id="qb-search" placeholder="Search questions…" style="position:absolute;right:110px;top:120px;width:420px;font:500 20px IN;padding:12px 18px;border-radius:12px;border:1.5px solid var(--line);background:#fff;color:var(--ink);outline:none">
<div class="abs" id="qb-cats" style="left:110px;top:270px;width:480px"></div>
<div class="abs" id="qb-list" style="left:630px;top:270px;width:1180px;height:640px;overflow:auto;padding-right:10px"></div>
<aside class="notes">Use the categories or search box to pull up a prepared answer.</aside>
</section>''')
# ---------------- B2 PREDICTION VS CAUSATION ----------------
S.append(f'''<section class="slide backup" id="b-cause" data-label="B2" data-title="Backup · Prediction vs causation" data-sec="6" data-steps="3">
<div class="hd"><div class="num" style="font-size:150px">B2</div><div><div class="kick" style="color:var(--coral)">Panel might ask</div><h2 style="margin-top:12px;font-size:52px">"How will you separate <em>prediction</em> from <span class="c">causation?</span>"</h2></div></div>
<div class="abs card" style="left:110px;top:280px;width:1700px;height:250px;padding:24px 30px">
 <div class="lab" style="color:var(--sea)">1 · The test we run</div>
 <div style="display:flex;align-items:center;gap:22px;margin-top:16px">
  <div class="mb2"><b>Model A</b><span>past landings + seasonality</span></div><div class="vs">vs</div>
  <div class="mb2 co"><b>Model B</b><span>Model A + mangrove history + prior typhoon exposure</span></div>
  <div class="vs">→</div><div class="mb2"><b>Unseen later quarters</b><span>compare MAE, RMSE, MASE</span></div>
  <div class="vs">→</div><div class="mb2 ok"><b>Better accuracy?</b><span>= predictive usefulness only</span></div></div>
</div>
<div class="abs card rv" data-s="1" style="left:110px;top:560px;width:830px;height:330px;padding:24px 30px">
 <div class="lab" style="color:var(--coral)">2 · Why accuracy is not proof of cause</div>
 <p class="body" style="margin-top:12px">Other factors can move <b>together with mangrove loss</b> and also change recorded landings:</p>
 <div style="display:flex;flex-wrap:wrap;gap:10px;margin-top:14px"><span class="chip">Fishing effort</span><span class="chip">Fuel prices</span><span class="chip">Regulations</span><span class="chip">Reporting changes</span></div>
 <p class="body" style="margin-top:14px">Proving cause would need <b>controlled or field studies</b>, which are outside our scope.</p>
</div>
<div class="abs card rv" data-s="2" style="left:980px;top:560px;width:830px;height:330px;padding:24px 30px">
 <div class="lab" style="color:var(--sea)">3 · How we will word results</div>
 <div class="say ok rv" data-s="2">✓ "Mangrove history <b>improves forecast accuracy</b> for these provinces and quarters."</div>
 <div class="say no rv" data-s="3">✕ "Mangrove loss <b>causes</b> lower landings."</div>
 <p class="small" style="margin-top:14px">Same rule for typhoon exposure, and for any predictor Random Forest ranks as important.</p>
</div>
{notes("""We test whether environmental information improves forecast accuracy. We compare a model with only past landings and seasonality against one with mangrove history and typhoon exposure added, both evaluated on unseen later quarters.
[→] Better accuracy means predictive usefulness only. Fishing effort, fuel prices, regulations and reporting changes can move together with mangrove loss and also affect landings. Proving cause would need controlled or field studies, which are outside our scope.
[→] So our results will say 'improves forecast accuracy', [→] never 'causes'.""")}
</section>''')
# ---------------- B3 REFERENCES ----------------
APA=[
"Benavides, I. F., Santacruz, M., Romero-Leiton, J. P., Barreto, C., &amp; Selvaraj, J. J. (2023). Assessing methods for multiple imputation of systematic missing data in marine fisheries time series with a new validation algorithm. <i>Aquaculture and Fisheries</i>. https://doi.org/10.1016/j.aaf.2021.12.013",
"Bokingkito, P., Jaroensutasinee, K., &amp; Jaroensutasinee, M. (2026). Explainable AI-driven machine learning for forecasting marine fisheries production using environmental predictors. <i>Machine Learning and Knowledge Extraction, 8</i>(7), Article 197. https://doi.org/10.3390/make8070197",
"Crawford, C. J., Roy, D. P., Arab, S., Barnes, C., Vermote, E., Hulley, G., Gerace, A., Choate, M., Engebretson, C., Micijevic, E., Schmidt, G., Anderson, C., Anderson, M., Bouchard, M., Cook, B., Dittmeier, R., Howard, D., Jenkerson, C., Kim, M., . . . Zahn, S. (2023). The 50-year Landsat collection 2 archive. <i>Science of Remote Sensing, 8</i>, Article 100103. https://doi.org/10.1016/j.srs.2023.100103",
"Dumilag, R. V., San Pablo, M. H., Malto, M. A. D., Longavela, M. R., Orgela, E. G., Belgica, T. H. R., Mendoza, L. C., Hibay, J. M., Bailon, J. D., Corral, L. E. H., Calaminos, F. P., Omoto, A. T., Chua, V. L., &amp; Berdin, L. D. (2023). COVID-19 impacts on food security and income of the fisherfolk in Magallanes, Sorsogon, Philippines. <i>NRCP Research Journal, 22</i>(1), 179–201. https://www.ejournals.ph/article.php?id=19903",
"Earth Resources Observation and Science (EROS) Center. (2020). <i>Landsat 8-9 Operational Land Imager / Thermal Infrared Sensor Level-2, Collection 2</i> [Data set]. U.S. Geological Survey. https://doi.org/10.5066/P9OGBGM6",
"Food and Agriculture Organization of the United Nations. (2024). <i>The state of world fisheries and aquaculture 2024: Blue transformation in action</i>. FAO. https://doi.org/10.4060/cd0683en",
"Hewamalage, H., Ackermann, K., &amp; Bergmeir, C. (2023). Forecast evaluation for data scientists: Common pitfalls and best practices. <i>Data Mining and Knowledge Discovery, 37</i>(2), 788–832. https://doi.org/10.1007/s10618-022-00894-5",
"Holmes, E. E., BR, S., Nimit, K., Maity, S., Checkley, D. M., Jr., Wells, M. L., &amp; Trainer, V. L. (2021). Improving landings forecasts using environmental covariates: A case study on the Indian oil sardine (<i>Sardinella longiceps</i>). <i>Fisheries Oceanography, 30</i>(6), 623–642. https://doi.org/10.1111/fog.12541",
"Nesslage, G., Lyubchich, V., Nitschke, P., Williams, E., Grimes, C., &amp; Wiedenmann, J. (2021). Environmental drivers of golden tilefish (<i>Lopholatilus chamaeleonticeps</i>) commercial landings and catch-per-unit-effort. <i>Fisheries Oceanography, 30</i>(5), 608–622. https://doi.org/10.1111/fog.12540",
"Oceana. (2026). <i>Net loss: How governance gaps are sinking Philippine fisheries</i> [Report]. Zenodo. https://doi.org/10.5281/zenodo.18320988",
"Philippine Statistics Authority. (n.d.). <i>Marine municipal fisheries: Volume of production by species, province and quarter</i> [Data set, Table 0032E4GVMP0]. PSA OpenSTAT. https://openstat.psa.gov.ph"]
refh="".join(f'<p class="apa">{a}</p>' for a in APA)
S.append(f'''<section class="slide backup" id="b-refs" data-label="B3" data-title="Backup · References" data-sec="6" data-steps="0">
<div class="hd"><div class="num" style="font-size:150px">B3</div><div><div class="kick">Backup</div><h2 style="margin-top:12px;font-size:54px">References <em>(APA 7)</em></h2></div></div>
<div class="abs" style="left:110px;top:270px;width:1700px;columns:2;column-gap:60px">{refh}</div>
<aside class="notes">Full reference list. Bokingkito et al. (2026) uses region–sector panels; Holmes et al. (2021) is a method reference (Indian oil sardine), not a Philippine study.</aside>
</section>''')
