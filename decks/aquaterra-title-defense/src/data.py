# generated v5 content (QA per section, RT references per section, QB panel bank)
B2='<p style="margin-top:10px"><span class="link" data-go="b-cause">Open the full answer: Prediction vs causation →</span></p>'
QA={'algo': [('How will you split the data?',
           '<ul><li><b>70/15/15 by time</b>, never shuffled, over the 96 quarters 2002 Q1–2025 Q4.</li><li><b>Train</b> 2002 Q1–2018 Q3 (67 quarters) · <b>Tune</b> 2018 Q4–2022 Q1 (14) · <b>Test</b> '
           '2022 Q2–2025 Q4 (15, locked until the final check).</li><li>Random Forest selection and GAMM tuning will stay inside Train and Tune, so later quarters cannot leak into decisions '
           '(Hewamalage et al., 2023). The 2002 rows have no lag-4 value and will drop from training. The ratio itself is our design choice.</li></ul>'),
          ('What is the seasonal-naive baseline, and what is MASE?',
           '<ul><li>The seasonal-naive forecast uses the <b>same quarter last year</b>. MASE divides the forecast error by the in-sample error of that baseline, so <b>MASE below 1</b> beats it '
           '(Hyndman &amp; Athanasopoulos, 2021).</li><li>We will also report MAE (typical miss, in tonnes) and RMSE (punishes large misses).</li></ul>'),
          ('Why Random Forest? Are there no other notable algorithms?',
           '<ul><li>Yes, there are. Bokingkito et al. (2026) evaluated alternatives including <b>XGBoost, Support Vector Regression and LSTM</b>, and performance differed across regions. We will not '
           'claim Random Forest is universally best.</li><li>Our justification is its role as a <b>predictor-selection tool before GAMM</b>. Nesslage et al. (2021) used Random Forest variable '
           'importance to guide more parsimonious GAMMs.</li><li>Selecting predictors with Pearson or Spearman correlations alone can miss nonlinear, nonmonotonic relationships.</li><li>We will '
           'evaluate the complete workflow against a seasonal baseline on unseen quarters.</li></ul>'),
          ('How did Nesslage et al. (2021) formulate their algorithm?',
           '<ol style="margin-left:24px"><li><b>Two outcomes</b>: annual commercial landings (northern stock) and monthly CPUE by fishing area.</li><li><b>Matched by time and place</b>: e.g. SST and '
           'wind averaged monthly in grid cells and assigned to nearby statistical areas.</li><li><b>Lagged predictors</b>: earlier climate conditions, up to seven years.</li><li><b>Random Forest '
           'ranked predictors</b> (Boruta and Altmann importance; kept the intersection, ordered by importance). It passed on <i>which predictors</i> to examine, not its predicted '
           'landings.</li><li><b>GAMM used the predictor values</b>, with selection checks, an AR(1) residual structure and square-root-transformed landings.</li><li><b>Evaluated</b> on later '
           'observations with MAE and RMSE.</li></ol><p style="margin-top:8px">What transfers to AquaTerra is the RF-guided GAMM workflow; their exact variables, lags and preprocessing are '
           'study-specific.</p>'),
          ('How will you separate prediction from causation?',
           '<p>We will test whether environmental information <b>improves forecast accuracy</b>. We will compare a model with only past landings and seasonality against one with prior typhoon '
           'exposure, rainfall and sea surface temperature added, both evaluated on <b>unseen later quarters</b>. Better accuracy means <b>predictive usefulness only</b>, because fishing effort, '
           'fuel prices, regulations and reporting changes can move together with typhoons or weather. Proving cause would need controlled or field studies, which are outside our scope. Our results '
           'will say “improves forecast accuracy”, never “causes”.</p><p style="margin-top:10px"><span class="link" data-go="b-cause">Open the full answer: Prediction vs causation →</span></p>')],
 'bg': [('Why is about 45 million kg lost every year?',
         '<ul><li>Oceana (2026, p. 10) reports capture fisheries production fell from <b>2.6M t (2010) to 1.9M t (2023)</b>: 591,136 t over 13 years, an average <b>45,472 t (≈45M kg) a year</b>. It '
         'is a national, municipal + commercial figure.</li><li>Oceana attributes the continuing decline to <b>governance gaps</b> (pp. 4–5): <b>overfishing</b> (about 88% of stocks assessed by NSAP '
         'in 2017 show overexploitation), <b>illegal fishing</b> (270,165 satellite-detected lights of apparent illegal fishing in municipal waters, Jan 2017–Jun 2024), <b>commercial vessels '
         'entering municipal waters</b> (174 of 930 coastal LGUs authorize commercial fishing in the 10.1–15 km zone; the 2024 Mercidar ruling), and <b>weak enforcement</b> (most LGUs have one '
         'fisheries technician; BFAR lost 28% of its workforce, 2017–2023). It also notes commercial fishing in municipal waters can destroy important marine habitats.</li><li>The report does not '
         'attribute the decline to climate. We will not claim any of these causes ourselves; the figure only shows the problem is real.</li></ul>'),
        ('Why the Naujan, Oriental Mindoro example?',
         '<ul><li>Agaton et al. (2023) interviewed fisherfolk in <b>Naujan, Oriental Mindoro</b> after the February 2023 oil spill. With fishing and other aquatic activities prohibited, participants '
         'lost <b>up to US$1,300 a week</b> in fishing income and had no alternative livelihood; food packs and cash aid did not cover food, utilities, education and health.</li><li>Caveat: a '
         'qualitative study with nine participants (snowball sampling), so it illustrates a supply disruption in MIMAROPA; it is not a provincial estimate.</li></ul>'),
        ('How is your study different from Bokingkito et al. (2026)?',
         '<table><tr><th></th><th>Bokingkito et al. (2026)</th><th>AquaTerra</th></tr><tr><td><b>Level</b></td><td>Regions</td><td>Five MIMAROPA provinces × 31 fish '
         'categories</td></tr><tr><td><b>Coverage</b></td><td>Commercial + marine municipal</td><td>Marine municipal only</td></tr><tr><td><b>Output</b></td><td>Production '
         'forecasts</td><td>Forecasts → seasonal shortfalls → gross landing value at risk</td></tr><tr><td><b>Environmental predictors</b></td><td>Used in the models</td><td>Typhoons, rainfall and '
         'SST tested for added value (with vs without)</td></tr><tr><td><b>Evaluation</b></td><td>Forecast accuracy</td><td>Shortfall detection and exposure rankings on unseen '
         'quarters</td></tr></table><p style="margin-top:10px">Our proposed contribution is an <b>evaluated connection</b> between provincial landing forecasts, seasonal shortfalls and economic '
         'planning information. Their work is our foundation.</p>')],
 'clients': [('What is the main benefit to your beneficiaries?',
              '<ul><li><b>LGUs</b>: earlier preparation of logistics. Fish is perishable and volumes swing with weather and sea conditions, so a forecast high-volume quarter could help prepare ice '
              'plants, cold storage and port logistics; a lean quarter could prompt local supply backups.</li><li><b>DTI</b>: getting ahead of supply shortages and price spikes by coordinating '
              'inter-provincial supply and giving traders and MSMEs a heads-up on expected volumes.</li><li>These are potential uses; we still need to consult these users.</li></ul>')],
 'data': [('How will you match the different datasets?',
           '<p>We will give the records consistent location identifiers and dates, then summarize environmental information for the relevant areas and periods. We will also test appropriate lags, '
           'since earlier conditions may inform later landings. Nesslage et al. (2021) found some relationships at three- to seven-year lags; we take that as a reason to investigate delayed '
           'relationships, not to apply the same lag to every predictor.</p>'),
          ('How will you handle the missing data?',
           '<p>To preserve the strong seasonality of fisheries production, we will apply <b>seasonal decomposition with Kalman smoothing</b> and <b>structural time series models with Kalman '
           'filters</b>, grounded in Benavides et al. (2023), whose study on marine fishery landings found these outperform simpler techniques for systematic, consecutive gaps. We will also use '
           'their <b>Known Sub-Sequence Algorithm (KSSA)</b> to select the lowest-error method on complete segments of our own series.</p>')],
 'gaps': [('What research gaps does AquaTerra address?',
           '<ol style="margin-left:24px"><li><b>Level:</b> no seasonal shortfall forecasts by province × fish category (Bokingkito et al., 2026, work at region–sector level).</li><li><b>Value:</b> '
           'forecasts give kilos, not value; we will attach a historical first-sale price.</li><li><b>Checking:</b> flags and rankings are not yet checked; we will test accuracy and price stability '
           '(Hewamalage et al., 2023).</li><li><b>Weather:</b> typhoons, rainfall and sea temperature are linked to lower catch (Noy et al., 2023; Holmes et al., 2021), but few studies test whether '
           'they improve a provincial forecast. We will test that and report it if they don\'t help. Prediction, not cause.</li></ol><p style="margin-top:10px"><span class="link" '
           'data-go="b-cause">Open the full answer: Prediction vs causation →</span></p>'),
          ('How do you know typhoons affect fishing?',
           '<ul><li>Noy et al. (2023, ADB) used satellite vessel data and found tropical cyclones reduced active fishing boats during and after storms; the Sibuyan Sea, Visayan Sea and Panay Gulf '
           'were most affected.</li><li>That is why we will test typhoon exposure as a predictor. We will not claim it causes a given shortfall.</li></ul>'),
          ('How is your study different from Bokingkito et al. (2026)?',
           '<table><tr><th></th><th>Bokingkito et al. (2026)</th><th>AquaTerra</th></tr><tr><td><b>Level</b></td><td>Regions</td><td>Five MIMAROPA provinces × 31 fish '
           'categories</td></tr><tr><td><b>Coverage</b></td><td>Commercial + marine municipal</td><td>Marine municipal only</td></tr><tr><td><b>Output</b></td><td>Production '
           'forecasts</td><td>Forecasts → seasonal shortfalls → gross landing value at risk</td></tr><tr><td><b>Environmental predictors</b></td><td>Used in the models</td><td>Typhoons, rainfall and '
           'SST tested for added value (with vs without)</td></tr><tr><td><b>Evaluation</b></td><td>Forecast accuracy</td><td>Shortfall detection and exposure rankings on unseen '
           'quarters</td></tr></table><p style="margin-top:10px">Our proposed contribution is an <b>evaluated connection</b> between provincial landing forecasts, seasonal shortfalls and economic '
           'planning information. Their work is our foundation.</p>')],
 'obj': [('What data will you examine, and what will you measure?',
          '<table><tr><th>Question</th><th>What will be measured</th></tr><tr><td><b>SOP 1 Benchmarks</b></td><td>Quarterly landing volumes (t) by province and fish category, 2002 Q1–2025 '
          'Q4.</td></tr><tr><td><b>SOP 2 Added value</b></td><td>Next-quarter forecast error with vs without typhoons, rainfall and SST. Predictive usefulness, not causation.</td></tr><tr><td><b>SOP '
          '3 Valuation</b></td><td>Shortfall = benchmark − forecast (if positive) × historical first-sale price.</td></tr><tr><td><b>SOP 4 Evaluation</b></td><td>MAE, RMSE, MASE vs seasonal-naive on '
          'Test quarters (2022 Q2–2025 Q4); shortfall-flag accuracy; ranking stability under alternative prices.</td></tr></table>'),
         ('Why are these called initial research questions?',
          '<ul><li>They are preliminary. We expect to refine wording and scope after data checks and adviser feedback, while keeping the one-to-one pairing with the specific objectives.</li></ul>'),
         ("What are your study's expected outputs?",
          '<ul><li><b>Landing forecast</b>: continuous, next-quarter metric tons</li><li><b>Projected shortfall</b>: continuous, metric tons below the seasonal benchmark</li><li><b>Economic '
          'exposure</b>: continuous, gross landing value in pesos</li><li><b>Shortfall indicator</b>: categorical, shortfall projected or not</li><li><b>Exposure ranking</b>: ordinal, province–fish '
          'combinations by exposure</li><li><b>Evaluation results</b>: accuracy, shortfall detection, ranking agreement, price sensitivity</li></ul>')],
 'scope': [('What counts as municipal waters?',
            '<ul><li><b>Municipal waters</b> extend up to <b>15 km from the general coastline</b> (equidistant where opposite shores are under 30 km apart), under RA 8550 as amended by RA 10654 '
            '(2015). <b>Municipal fishing</b> uses no boat or boats of <b>3 gross tons or less</b>.</li><li>Oceana (2026) uses the same 0–15 km definition.</li><li>Caveat: in December 2023 a Malabon '
            'RTC decision, left standing by the Supreme Court First Division in August 2024 on procedural grounds, declared key municipal-waters provisions unconstitutional for one commercial '
            "operator (the Mercidar case). The government's motion for reconsideration was still pending as of October 2026. We will follow the statutory definition and PSA's municipal "
            'classification of the landing records.</li></ul>'),
           ('What provinces will you cover?',
            "<ul><li>The five MIMAROPA provinces: <b>Occidental Mindoro, Oriental Mindoro, Marinduque, Romblon and Palawan</b>, as listed in PSA OpenSTAT's marine municipal fisheries tables (PSA, "
            '2026).</li><li>PSA has quarterly records for each from 2002 Q1; we will use 2002 Q1–2025 Q4. PSA also lists the City of Puerto Princesa separately, without separate values in this '
            'table.</li></ul>'),
           ('What fish categories will you cover?',
            "<ul><li>The <b>31 named species categories</b> in PSA's marine municipal fisheries tables (PSA, 2026): Acetes (alamang), anchovies (dilis), big-eyed scad (matangbaka), bigeye tuna, blue "
            'crab (alimasag), caesio (dalagang-bukid), cavalla (talakitok), crevalle (salay-salay), eastern little tuna, fimbriated sardines (tunsoy), flying fish (bolador), frigate tuna (tulingan), '
            'goatfish (saramulyete), grouper (lapu-lapu), hairtail (espada), Indian mackerel (alumahan), Bali sardinella (tamban), Indo-Pacific mackerel (hasa-hasa), mullet (kapak), parrotfish '
            '(loro), porgies (pargo), round herring (tulis), roundscad (galunggong), siganid (samaral), skipjack (gulyasan), slipmouth (sapsap), snapper (maya-maya), Spanish mackerel (tanigue), '
            "squid (pusit), threadfin bream (bisugo) and yellowfin tuna.</li><li>PSA's 'Others' group will be excluded. Final coverage depends on complete, compatible landing and price "
            'records.</li></ul>'),
           ('What does causal effects mean?',
            '<ul><li>A causal effect means a change in one factor <b>directly produces</b> a change in another, for example claiming that a typhoon caused fish landings to decrease.</li><li>Our '
            'study examines whether typhoon exposure, rainfall and SST <b>help predict</b> landings. Even if we find a relationship, that alone does not prove causation, because other factors may '
            'also explain the changes.</li></ul><p style="margin-top:10px"><span class="link" data-go="b-cause">Open the full answer: Prediction vs causation →</span></p>')],
 'title': [('What is municipal fish landings?',
            '<ul><li>Catch from <b>municipal waters</b> (up to 15 km from shore; RA 10654, 2015) by fishers with no boat or boats of <b>3 gross tons or less</b>, brought ashore.</li><li>We will '
            'measure the <b>tonnes</b> landed in each province during each quarter (PSA, 2026).</li></ul>'),
           ('So this is different from locations?',
            '<ul><li>Yes. ‘Municipal’ describes the <b>type of fishing operation</b> (no boat or a small boat). It does not mean our records are grouped by municipality.</li><li>Our records are '
            'grouped by <b>province</b>, the location being analyzed.</li></ul>'),
           ('How can you ensure this dataset only accounts for small-scale fisheries?',
            '<ul><li>We will use PSA’s dataset specifically labeled <b>Marine Municipal Fisheries</b> (no boat, or boats of 3 gross tons or less), selected separately from commercial fisheries and '
            'aquaculture records.</li><li>Our assurance comes from PSA’s documented survey coverage and classification. Since we will use published aggregate data, we will not independently verify '
            'every boat’s size.</li></ul>'),
           ('What is the period of a quarter?', '<ul><li><b>Q1</b>: January–March</li><li><b>Q2</b>: April–June</li><li><b>Q3</b>: July–September</li><li><b>Q4</b>: October–December</li></ul>'),
           ('What are the dependent and independent variables?',
            '<ul><li><b>Predictors (independent):</b> past landings and season, with prior typhoon exposure, rainfall and SST tested for added value.</li><li><b>Outcomes (dependent):</b> '
            'next-quarter landings, shortfalls and gross landing value at risk.</li><li>The link will be <b>predictive</b>: we will test whether the weather predictors improve forecasts, not whether '
            'they cause shortfalls.</li></ul><p style="margin-top:10px"><span class="link" data-go="b-cause">Open the full answer: Prediction vs causation →</span></p>')],
 'value': [('How will you calculate gross landing value at risk?',
            '<ol style="margin-left:24px"><li><b>Gross landing value.</b> For each province and quarter, multiply the quantity landed for each fish category (mt × 1,000 = kg) by the <b>matching '
            'historical first-sale price</b> (₱/kg) for the same period and province, then add across categories.</li><li><b>Value at risk.</b> Projected shortfall = seasonal benchmark − forecast, '
            '<b>only when the forecast is below</b> the benchmark (otherwise zero). Multiply that shortfall by the same matching price. <i>Example (illustrative): 180 mt × 1,000 × ₱180/kg = '
            '₱32.4M.</i></li><li><b>What it means.</b> It is the <b>gross revenue tied to the missing landings</b>. It is not profit, not household income loss and not disaster damage, because it '
            'ignores costs and how fishers, traders and buyers adjust.</li><li><b>How we defend it.</b> We repeat the calculation with <b>alternative price sources</b> (first-sale vs unit-value '
            'proxy) and a <b>± price range</b>, and check whether the <b>ranking of province–category combinations stays stable</b>. Units and coverage are matched before multiplying.</li></ol><p '
            'style="margin-top:8px"><span class="link" data-go="s-var">Open the IV.5 value-at-risk builder →</span></p>'),
           ('So is that amount money that will be lost?',
            '<ul><li>No. It is the <b>gross value at stake</b> if the projected shortfall happens, priced at historical first-sale prices.</li><li>Actual losses would need extra evidence: costs, '
            'prices responding to scarcity, catch switching to other species, and how much fishing activity really drops.</li></ul>'),
           ('Why the shortfall, and not a share of landings exposed to a hazard?',
            '<ul><li>In our study the “exposed” part of landings is the <b>projected shortfall itself</b>: the tons expected to be missing compared with the usual seasonal level.</li><li>We will not '
            'assume a hazard removes a fixed share of the catch. The forecast already uses prior typhoon exposure, rainfall and SST where they add predictive value, so the shortfall comes from the '
            'evaluated forecast rather than an assumed percentage.</li></ul>'),
           ('Why historical prices instead of forecasting prices?',
            '<ul><li>Price forecasting is outside our scope. Historical first-sale prices keep the valuation transparent and reproducible.</li><li>Price uncertainty will be handled by the '
            'sensitivity check (alternative sources and a ± range), and we will report whether the rankings change.</li></ul>')]}
RT={'algo': [('Nesslage et al. (2021)',
           'Environmental drivers of golden tilefish commercial landings and CPUE',
           'Random Forest importance used to choose covariates for parsimonious GAMMs: the basis of our RF → GAMM sequence.'),
          ('Holmes et al. (2021)',
           'Improving landings forecasts using environmental covariates (Indian oil sardine)',
           'GAMs on quarterly landings; only some environmental covariates improved out-of-sample forecasts. A method reference.'),
          ('Hewamalage et al. (2023)',
           'Forecast evaluation for data scientists: Common pitfalls and best practices',
           'Time-ordered evaluation, no leakage of future data; basis for our chronological split.'),
          ('Hyndman & Athanasopoulos (2021)', 'Forecasting: Principles and practice (3rd ed.)', 'Defines the seasonal-naive benchmark, MAE, RMSE and MASE.'),
          ('Bokingkito et al. (2026)',
           'Explainable AI-driven machine learning for forecasting marine fisheries production using environmental predictors',
           'Nine ML algorithms with SHAP on 32 region–sector panels, 2002–2025. Our starting point; works above province level.')],
 'bg': [('FAO (2024)', 'The state of world fisheries and aquaculture 2024', 'Aquatic foods are central to food security, nutrition and livelihoods.'),
        ('Agaton et al. (2023)',
         'Immediate socioeconomic impacts of Mindoro oil spill on fisherfolk of Naujan, Philippines',
         'Qualitative study (9 participants) after the 2023 spill: fishing banned, income lost up to US$1,300/week, aid insufficient. MIMAROPA example.'),
        ('Oceana (2026)',
         'Net loss: How governance gaps are sinking Philippine fisheries',
         'Capture fisheries fell 2.6M t (2010) → 1.9M t (2023), ≈45,472 t/yr; attributed to overfishing, illegal fishing, commercial intrusion into municipal waters and weak enforcement.'),
        ('Bokingkito et al. (2026)',
         'Explainable AI-driven machine learning for forecasting marine fisheries production using environmental predictors',
         'Nine ML algorithms with SHAP on 32 region–sector panels, 2002–2025. Our starting point; works above province level.')],
 'data': [('Nababa et al. (2026)', 'Artisanal fishery and their relationship with mangrove extent, rainfall, and sea surface temperature in the Niger Delta Region', 'Predictor rationale: a nonlinear association between mangrove extent and artisanal fish landings in Nigeria. Supports testing mangrove extent and change; does not establish forecast gains for MIMAROPA. https://doi.org/10.1016/j.rsma.2026.105071'),
          ('Holmes et al. (2021)', 'Improving landings forecasts using environmental covariates: A case study on the Indian oil sardine', 'Predictor rationale: selected rainfall and SST summaries improved out-of-sample forecasts; results depended on the covariate and season. https://doi.org/10.1111/fog.12541'),
          ('Noy et al. (2023)', 'The impact of tropical cyclones on fishing activities in the Philippines', 'Predictor rationale: satellite vessel data showed fewer active fishing boats during and after tropical cyclones. Supports testing cyclone exposure. https://doi.org/10.22617/wps230291-2'),
          ('PSA (2026)', 'Marine municipal fisheries: volume and value of production (OpenSTAT)', "Quarterly province × species records, 2002 onward; 31 named categories plus 'Others'."),
          ('Huffman et al. (2023)', 'GPM IMERG Final Precipitation V07', 'Satellite rainfall data set.'),
          ('Huang et al. (2021)', 'Improvements of the Daily OISST version 2.1', 'Sea surface temperature data set.'),
          ('Gahtan et al. (2024)', 'IBTrACS version 4r01', 'Global tropical cyclone best-track data set.'),
          ('Bunting et al. (2026)', 'Global Mangrove Watch (GMW) 4.1 + Landsat imagery', 'Annual GMW mangrove extent maps, paired with 16-day Landsat time series. GMW release 4.1.12: https://doi.org/10.5281/zenodo.21346457.'),
          ('Hewamalage et al. (2023)',
           'Forecast evaluation for data scientists: Common pitfalls and best practices',
           'Time-ordered evaluation, no leakage of future data; basis for our chronological split.'),
          ('Benavides et al. (2023)', 'Assessing methods for multiple imputation of systematic missing data in marine fisheries time series', 'Basis for our missing-data handling.')],
 'gaps': [('Bokingkito et al. (2026)',
           'Explainable AI-driven machine learning for forecasting marine fisheries production using environmental predictors',
           'Nine ML algorithms with SHAP on 32 region–sector panels, 2002–2025. Our starting point; works above province level.'),
          ('PSA (2026)', 'Marine municipal fisheries: volume and value of production (OpenSTAT)', "Quarterly province × species records, 2002 onward; 31 named categories plus 'Others'."),
          ('Hewamalage et al. (2023)',
           'Forecast evaluation for data scientists: Common pitfalls and best practices',
           'Time-ordered evaluation, no leakage of future data; basis for our chronological split.'),
          ('Noy et al. (2023)',
           'The impact of tropical cyclones on fishing activities in the Philippines',
           'ADB working paper: satellite vessel data show fewer active boats during and after cyclones (Sibuyan Sea, Visayan Sea, Panay Gulf).'),
          ('Holmes et al. (2021)',
           'Improving landings forecasts using environmental covariates (Indian oil sardine)',
           'GAMs on quarterly landings; only some environmental covariates improved out-of-sample forecasts. A method reference.')],
 'scope': [('PSA (2026)', 'Marine municipal fisheries: volume and value of production (OpenSTAT)', "Quarterly province × species records, 2002 onward; 31 named categories plus 'Others'."),
           ('RA 10654 (2015)', 'Amendment to the Philippine Fisheries Code (RA 8550)', 'Municipal waters: up to 15 km from the coastline; municipal fishing: boats ≤3 GT. Pre-2020 legal source.'),
           ('Oceana (2026)',
            'Net loss: How governance gaps are sinking Philippine fisheries',
            'Capture fisheries fell 2.6M t (2010) → 1.9M t (2023), ≈45,472 t/yr; attributed to overfishing, illegal fishing, commercial intrusion into municipal waters and weak enforcement.')]}
QB=[('Research problem & contribution',
  [('Why is about 45 million kg of fish lost every year?',
    'Oceana (2026, p. 10) reports capture fisheries production fell from 2.6M t (2010) to 1.9M t (2023): 591,136 t over 13 years, an average 45,472 t (≈45M kg) a year. It is a national, municipal + '
    'commercial figure. Oceana attributes the continuing decline to governance gaps (pp. 4–5): overfishing (about 88% of stocks assessed by NSAP in 2017 show overexploitation), illegal fishing '
    '(270,165 satellite-detected lights of apparent illegal fishing in municipal waters, Jan 2017–Jun 2024), commercial vessels entering municipal waters (174 of 930 coastal LGUs authorize '
    'commercial fishing in the 10.1–15 km zone; the 2024 Mercidar ruling), and weak enforcement (most LGUs have one fisheries technician; BFAR lost 28% of its workforce, 2017–2023). It also notes '
    'commercial fishing in municipal waters can destroy important marine habitats. The report does not attribute the decline to climate. We will not claim any of these causes ourselves; the figure '
    'only shows the problem is real.'),
   ('What research gaps does AquaTerra address?',
    'Level: no seasonal shortfall forecasts by province × fish category (Bokingkito et al., 2026, work at region–sector level). Value: forecasts give kilos, not value; we will attach a historical '
    'first-sale price. Checking: flags and rankings are not yet checked; we will test accuracy and price stability (Hewamalage et al., 2023). Weather: typhoons, rainfall and sea temperature are '
    "linked to lower catch (Noy et al., 2023; Holmes et al., 2021), but few studies test whether they improve a provincial forecast. We will test that and report it if they don't help. Prediction, "
    'not cause.Open the full answer: Prediction vs causation →'),
   ('Who would use these forecasts?',
    'DTI could use the estimates when consulting with fisheries-related businesses, while LGUs and fisheries offices could use them to prioritize monitoring. We still need to consult these potential '
    'users to understand how the results would fit their actual work.'),
   ('What makes your study different from existing forecasting research?',
    'Our contribution is connecting the forecasts to seasonal shortfalls and their estimated gross landing value. Beyond predicting a volume, we will test whether the framework can reliably identify '
    'shortfall periods and rank the province–category combinations that may need attention. Bokingkito et al. (2026) already provide a Philippine environmental forecasting foundation, which we '
    'acknowledge.'),
   ('Why forecast one quarter ahead?',
    'PSA publishes the records quarterly, so that is the level of detail our data supports. We chose the next quarter as a near-term planning horizon, although we still need to confirm with '
    'potential users whether that timing gives them enough time to act.')]),
 ('Data & scope',
  [('What counts as municipal waters?',
    'Municipal waters extend up to 15 km from the general coastline (equidistant where opposite shores are under 30 km apart), under RA 8550 as amended by RA 10654 (2015). Municipal fishing uses no '
    'boat or boats of 3 gross tons or less. Oceana (2026) uses the same 0–15 km definition. Caveat: in December 2023 a Malabon RTC decision, left standing by the Supreme Court First Division in '
    "August 2024 on procedural grounds, declared key municipal-waters provisions unconstitutional for one commercial operator (the Mercidar case). The government's motion for reconsideration was "
    "still pending as of October 2026. We will follow the statutory definition and PSA's municipal classification of the landing records."),
   ('What provinces and fish categories will you cover?',
    "The five MIMAROPA provinces (Occidental Mindoro, Oriental Mindoro, Marinduque, Romblon, Palawan) and the 31 named species categories in PSA's marine municipal fisheries tables, 2002 Q1–2025 Q4 "
    "(PSA, 2026). PSA's 'Others' group will be excluded."),
   ('What exactly is the landing volume?',
    'It is the weight of catch unloaded at municipal fish landing centers, measured in metric tons. It describes recorded unloadings, so we should not automatically treat it as the total amount of '
    'fish caught at sea.'),
   ('How will you match the different datasets?',
    'We will give the records consistent location identifiers and dates, then summarize the environmental information for the relevant areas and periods. We will also test appropriate lags, since '
    'earlier environmental conditions may provide information about later landings. Nesslage et al. (2021) found some relationships at three- to seven-year lags in golden tilefish; we take that as a '
    'reason to investigate delayed relationships, rather than applying the same lag to every predictor.'),
   ('How will you handle missing records and reporting changes?',
    'We will first check where the gaps occur and whether they are connected to changes in reporting or coverage. Small gaps may be suitable for carefully tested imputation, while long gaps may '
    'require shortening the period or excluding a particular province–category combination. We will keep the original records and document any changes we make.'),
   ('How do you know the environmental data represent the fishing grounds?',
    'At this stage, provincial landing records cannot tell us exactly where every fish was caught. We will document how we link environmental areas to landing records and seek fisheries-agency '
    'advice, but we also acknowledge that this connection may be imperfect.')]),
 ('Methods & validation',
  [('How will you split the data?',
    '70/15/15 by time, never shuffled, over the 96 quarters 2002 Q1–2025 Q4. Train 2002 Q1–2018 Q3 (67 quarters) · Tune 2018 Q4–2022 Q1 (14) · Test 2022 Q2–2025 Q4 (15, locked until the final '
    'check). Random Forest selection and GAMM tuning will stay inside Train and Tune, so later quarters cannot leak into decisions (Hewamalage et al., 2023). The 2002 rows have no lag-4 value and '
    'will drop from training. The ratio itself is our design choice.'),
   ('When would you issue the forecast?',
    'We need to set a consistent issue date before the quarter being forecast begins. We will then check which records would actually be available on that date, because the most recent quarter’s '
    'landing figures may not have been released yet.'),
   ('How will you avoid using future information?',
    'At each forecast date, we will only use records available up to that point. Predictor selection, data preparation and tuning will happen within the training periods, so later observations do '
    'not influence those decisions (Hewamalage et al., 2023).'),
   ('Why Random Forest and GAMM?',
    'We will use them together. Random Forest helps identify useful predictors, and GAMM uses those predictors to forecast landing volume while accounting for nonlinear relationships and differences '
    'among groups. The sequence is adapted from Nesslage et al. (2021). Our main comparison is the complete workflow against a seasonal forecasting baseline.'),
   ('What seasonal baseline will you use?',
    'The observed landing volume from the same quarter of the previous year. For example, the baseline forecast for Q1 is the previous year’s Q1 landings. It already captures seasonality, so our '
    'more complex workflow needs to show whether it adds value.'),
   ('How will testing reflect actual use?',
    'We will step through historical forecast dates and predict each target quarter using only earlier available information. That shows how the workflow performs across different periods instead of '
    'judging it from one forecast.'),
   ('What performance measures matter most?',
    'MAE tells us how far the forecasts typically miss in metric tons, while RMSE highlights larger mistakes. MASE helps compare errors across differently sized series. We will also check how often '
    'shortfall alerts are correct, how many actual shortfalls are missed, and whether the monetary rankings are reliable.'),
   ('What improvement would you consider useful?',
    'We have not set a numerical threshold yet. We need to consider whether the improvement is consistent and meaningful for users, especially when balancing missed shortfalls against false alerts. '
    'If the workflow adds little value over the seasonal baseline, we would not recommend it for operational use.'),
   ('What if overall results hide poor performance in some areas?',
    'We will break the results down by province, fish category and quarter, showing where the workflow performs well and where users should be more cautious, rather than relying on one overall '
    'accuracy figure.')]),
 ('Environmental interpretation',
  [('How will you separate prediction from causation?',
    'We will test whether environmental information <b>improves forecast accuracy</b>. We will compare a model with only past landings and seasonality against one with prior typhoon exposure, '
    'rainfall and sea surface temperature added, both evaluated on <b>unseen later quarters</b>. Better accuracy means <b>predictive usefulness only</b>, because fishing effort, fuel prices, '
    'regulations and reporting changes can move together with typhoons or weather. Proving cause would need controlled or field studies, which are outside our scope. Our results will say “improves '
    'forecast accuracy”, never “causes”.'),
   ('What does an important environmental variable tell you?',
    'It tells us that the variable provided useful information to the fitted model. We would still check its stability and its relationship with other predictors before interpreting it, and '
    'importance alone would not establish causation.'),
   ('Could environmental averages hide important details?',
    'Yes. A quarterly average could hide a short extreme event, and a provincial average could hide differences between coastal areas. One refinement is to test whether a small set of alternative, '
    'justified summaries changes the results, with those choices evaluated within training data.'),
   ('What if a relationship goes against established fisheries knowledge?',
    'We would first check whether it comes from a data problem, an unsuitable lag, geographic mismatch, or correlation with another predictor. We would also seek domain advice and check whether the '
    'pattern appears consistently before giving it an ecological interpretation.')]),
 ('Value at risk & dashboard',
  [('How will you calculate gross landing value at risk?',
    'Gross landing value. For each province and quarter, multiply the quantity landed for each fish category (mt × 1,000 = kg) by the matching historical first-sale price (₱/kg) for the same period '
    'and province, then add across categories. Value at risk. Projected shortfall = seasonal benchmark − forecast, only when the forecast is below the benchmark (otherwise zero). Multiply that '
    'shortfall by the same matching price. Example (illustrative): 180 mt × 1,000 × ₱180/kg = ₱32.4M. What it means. It is the gross revenue tied to the missing landings. It is not profit, not '
    'household income loss and not disaster damage, because it ignores costs and how fishers, traders and buyers adjust. How we defend it. We repeat the calculation with alternative price sources '
    '(first-sale vs unit-value proxy) and a ± price range, and check whether the ranking of province–category combinations stays stable. Units and coverage are matched before multiplying. '),
   ('What historical prices will you use?',
    'We prioritize compatible first-sale prices for the same province and fish category. Where those are unavailable, we may calculate historical unit-value proxies from matching marine municipal '
    'production-value and volume records. We will test alternative reference prices to see how much they change the estimates and rankings. PSA’s general farmgate-price table needs a coverage check '
    'before we apply it to marine municipal records.'),
   ('What does “at risk” mean here?',
    'It means the historical-price value associated with a projected landing shortfall. It is a planning estimate, so users should not interpret it as confirmed lost profit, household income loss or '
    'disaster damage.'),
   ('How will you show uncertainty?',
    'The exact method is not finalized yet. A useful addition would be a prediction range around each forecast, with its coverage checked on held-out observations. We would show alternative-price '
    'scenarios separately, because uncertainty in landing volume and sensitivity to price assumptions are different things.'),
   ('What decisions could the dashboard support?',
    'It could help users decide which areas to monitor more closely and where to begin discussions about sourcing, deliveries or possible supply gaps. Decisions about assistance eligibility, fishing '
    'restrictions or confirmed financial losses would need additional evidence.'),
   ('How will you know whether users understand the dashboard?',
    'We plan to seek agency feedback on its usefulness. One refinement is to ask users to interpret sample results and explain what action they would consider, which helps identify confusing labels '
    'or misleading interpretations. The participants and assessment procedure still need to be specified.')]),
 ('Limitations & pressure test',
  [('What is the biggest threat to your findings?',
    'Whether the datasets can be matched meaningfully. If the environmental summaries represent the wrong areas or the prices do not match the fisheries coverage, a sophisticated model would still '
    'be learning from poorly matched information.'),
   ('What if reports are missing during low landings or severe weather?',
    'That could bias the results, because the missing periods may be exactly the difficult situations we want to forecast. We need to examine when gaps occur and recognize that filling them '
    'automatically could hide real declines or make performance look better than it is.'),
   ('Could other factors explain the environmental patterns?',
    'Yes. Fishing effort, demand, regulations, fuel costs and reporting practices could also affect recorded landings. Where we cannot include suitable records for those factors, we will acknowledge '
    'them as alternative explanations.'),
   ('How will you show that improvements are reliable?',
    'We will keep selection and tuning inside training data and check performance across different chronological evaluation periods where feasible. We also limit model complexity and remember that '
    'our pooled rows share environmental histories, so they are not all independent observations (Hewamalage et al., 2023).'),
   ('What if the workflow does not outperform the baseline?',
    'Then that is what we will report. The study would still show whether the proposed predictors and workflow add value under our data conditions, and it could establish that a simpler seasonal '
    'method is the better option for the evaluated setting.'),
   ('What conclusion should agencies avoid?',
    'They should avoid saying that our forecast proves a typhoon or weather condition caused a particular monetary loss. Our results estimate future landings and benchmark-relative value, without '
    'establishing that causal connection.'),
   ('What would you improve first with another year?',
    'We would prioritize information linking landing records to actual fishing grounds and fishing effort. That would give a stronger basis for matching environmental conditions and understanding '
    'why recorded landings change.')]),
 ('Added answers',
  [('How will you handle the missing data? (method)',
    'To preserve strong seasonality, we will apply seasonal decomposition with Kalman smoothing and structural time series models with Kalman filters, grounded in Benavides et al. (2023), whose '
    'study on marine fishery landings found these outperform simpler techniques for systematic, consecutive gaps. We will also use their Known Sub-Sequence Algorithm (KSSA) to select the '
    'lowest-error method on complete segments of our own series.'),
   ('What is the main benefit to your beneficiaries?',
    'For LGUs, earlier preparation of logistics and less spoilage: knowing when a high-volume quarter is coming could help prepare ice plants, cold storage and port logistics; a lean quarter could '
    'prompt local supply backups. For DTI, getting ahead of supply shortages and price spikes by coordinating inter-provincial supply and giving traders and MSMEs a heads-up. These are potential '
    'uses that still need consultation.')])]
PSA={}
