(()=>{
const $=(s,r=document)=>r.querySelector(s),$$=(s,r=document)=>[...r.querySelectorAll(s)];
const NS='http://www.w3.org/2000/svg';
function el(tag,attrs,parent,txt){const e=document.createElementNS(NS,tag);for(const k in attrs)e.setAttribute(k,attrs[k]);if(txt!=null)e.textContent=txt;if(parent)parent.appendChild(e);return e}
function rng(seed){let s=seed>>>0||1;return()=>{s^=s<<13;s>>>=0;s^=s>>17;s^=s<<5;s>>>=0;return (s%100000)/100000}}
const fmt=(v,d=1)=>Number(v).toLocaleString('en-US',{minimumFractionDigits:d,maximumFractionDigits:d});
const stage=$('#stage'),slides=$$('.slide'),ctrl={};
let cur=0,step=0,returnTo=null,playT=null;
const steps=s=>+(s.dataset.steps||0);
function fit(){const k=Math.min(innerWidth/1920,innerHeight/1080);stage.style.transform=`translate(-50%,-50%) scale(${k})`}
addEventListener('resize',fit);fit();
function toast(t){const e=$('#toast');e.textContent=t;e.classList.add('show');clearTimeout(e._t);e._t=setTimeout(()=>e.classList.remove('show'),1600)}
function setStep(s){const sl=slides[cur];step=Math.max(0,Math.min(s,steps(sl)));
 $$('.rv[data-s]',sl).forEach(e=>e.classList.toggle('on',step>=+e.dataset.s));
 const c=ctrl[sl.id];if(c&&c.step)c.step(step);chrome()}
function go(i,s=0,keepReturn){i=Math.max(0,Math.min(i,slides.length-1));
 const old=slides[cur];if(ctrl[old.id]&&ctrl[old.id].leave)ctrl[old.id].leave();
 old.classList.remove('active');cur=i;const sl=slides[cur];sl.classList.add('active');
 if(!keepReturn){returnTo=null}
 $('#back').style.display=returnTo!=null?'block':'none';
 const c=ctrl[sl.id];if(c&&c.enter)c.enter();
 setStep(s==='max'?steps(sl):s);
 if($('#qov').classList.contains('show'))fillQ();if($('#rov').classList.contains('show'))fillR();
 history.replaceState(null,'','#'+sl.id)}
function goLabel(id,ret=true){const i=slides.findIndex(s=>s.id===id);if(i<0)return;const from=cur;closeAll();if(ret){returnTo=from}go(i,0,ret);if(ret)$('#back').textContent='← Back to '+(slides[from].dataset.label.startsWith('B')?slides[from].dataset.label:'slide '+(+slides[from].dataset.label))}
function next(){const sl=slides[cur];if(step<steps(sl))setStep(step+1);else if(cur<slides.length-1)go(cur+1)}
function prev(){if(step>0)setStep(step-1);else if(cur>0)go(cur-1,'max')}
const mainN=slides.filter(s=>!s.classList.contains('backup')).length;
function chrome(){const sl=slides[cur],bk=sl.classList.contains('backup');
 $('#counter').innerHTML=bk?`<b>${sl.dataset.label}</b> backup`:`<b>${sl.dataset.label}</b> / ${String(mainN-1).padStart(2,'0')}`;
 $('#progress').style.width=(bk?100:(cur/(mainN-1))*100)+'%';
 const sec=+sl.dataset.sec;$$('#rail .rs').forEach(e=>{const k=+e.dataset.sec;e.className='rs'+(k<sec?' done':k===sec?' on':'')});
 $('#seclab').innerHTML=sl.dataset.title;
 const n=steps(sl);$('#steps').innerHTML=Array.from({length:n},(_,k)=>`<span class="${k<step?'on':''}"></span>`).join('');
 $('#kq').classList.toggle('dim',!QA[sl.dataset.q]);
 const nt=$('aside.notes',sl);$('#ntxt').textContent=nt?nt.textContent.trim():'(No notes for this slide.)';
 $('#nlab').textContent='Speaker notes · '+sl.dataset.title.replace('&amp;','&')}
// overlays
function closeAll(){$$('.ov').forEach(o=>o.classList.remove('show'))}
function toggleOv(id){const o=$('#'+id),was=o.classList.contains('show');closeAll();if(!was){if(id==='qov')fillQ();if(id==='rov')fillR();if(id==='menu')fillMenu();o.classList.add('show')}}
function qaHTML(q,a,open,tag){return `<div class="qa${open?' open':''}"><button class="q"><i>Q</i><span>${q}</span></button>${tag?`<span class="tagc">${tag}</span>`:''}<div class="a">${a}</div></div>`}
function fillQ(){const sl=slides[cur],list=QA[sl.dataset.q];
 $('#qtitle').innerHTML=sl.dataset.title;
 $('#qbody').innerHTML=list?list.map((x,k)=>qaHTML(x[0],x[1],k===0)).join(''):'<p class="body" style="margin-top:20px">No section questions for this slide.</p>';
 $('#qbody').insertAdjacentHTML('beforeend','<p style="margin-top:22px"><span class="link" data-go="b-qbank">Open the full panel Q&amp;A bank →</span></p>')}
function fillR(){const sl=slides[cur],key=sl.dataset.r||sl.dataset.q,list=RT[key];
 let h='';if(list){h+=`<div class="lab" style="margin-top:14px;color:var(--sea)">${key==='bg'?'Relevant titles · click to read the summary':'Relevant to this section'}</div>`+list.map((r,k)=>`<div class="ref${k===0?' open':''}"><div class="ra">${r[0]}</div><div class="rt">${r[1]}</div><div class="rn">${r[2]}</div></div>`).join('')}
 h+=`<div class="lab" style="margin-top:26px">All references · APA 7</div>`+APA.map(a=>`<p class="apa" style="margin-top:12px;font-size:17px">${a}</p>`).join('');
 $('#rbody').innerHTML=h}
function fillMenu(){$('#mgrid').innerHTML=slides.map((s,k)=>`<button class="it${s.classList.contains('backup')?' bk':''}${k===cur?' cur':''}" data-k="${k}"><small>${s.dataset.label}</small>${s.dataset.title}</button>`).join('')}
document.addEventListener('click',e=>{
 const g=e.target.closest('[data-go]');if(g){e.preventDefault();goLabel(g.dataset.go);return}
 const q=e.target.closest('.qa .q');if(q){q.parentElement.classList.toggle('open');return}
 const r=e.target.closest('.ref');if(r){r.classList.toggle('open');return}
 const m=e.target.closest('#mgrid .it');if(m){closeAll();go(+m.dataset.k);return}
 if(e.target.classList.contains('ov'))closeAll();
 if(e.target.closest('.x'))closeAll()});
$$('#rail .rs').forEach(r=>r.onclick=()=>{const i=slides.findIndex(s=>+s.dataset.sec===+r.dataset.sec);if(i>=0){closeAll();go(i)}});
$('#back').onclick=()=>{if(returnTo!=null){const r=returnTo;returnTo=null;go(r)}};
$('#kq').onclick=()=>toggleOv('qov');$('#kr').onclick=()=>toggleOv('rov');$('#kb').onclick=()=>toggleOv('menu');
$('#kn').onclick=()=>$('#notes').classList.toggle('show');$('#kf').onclick=fs;$('#kh').onclick=()=>toggleOv('help');
$('#pv').onclick=prev;$('#nx').onclick=next;
function fs(){if(!document.fullscreenElement)document.documentElement.requestFullscreen&&document.documentElement.requestFullscreen().catch(()=>{});else document.exitFullscreen()}
addEventListener('keydown',e=>{
 if(e.target.tagName==='INPUT'&&e.target.type!=='range'){if(e.key==='Escape')e.target.blur();return}
 const k=e.key;
 if(['ArrowRight','PageDown',' '].includes(k)){e.preventDefault();next()}
 else if(['ArrowLeft','PageUp'].includes(k)){e.preventDefault();prev()}
 else if(k==='Home'){go(0)}else if(k==='End'){go(mainN-1)}
 else if(k==='m'||k==='M'){document.body.classList.toggle('nomo');toast&&toast(document.body.classList.contains('nomo')?'Motion off':'Motion on')}
 else if(k==='f'||k==='F')fs();else if(k==='n'||k==='N')$('#notes').classList.toggle('show');
 else if(k==='q'||k==='Q'){if(QA[slides[cur].dataset.q])toggleOv('qov');else toast('No section questions here · press B for the Q bank')}
 else if(k==='r'||k==='R')toggleOv('rov');else if('bBgG'.includes(k)&&k.length===1)toggleOv('menu');
 else if(k==='?'||k==='h'||k==='H')toggleOv('help');
 else if(k==='Escape'){closeAll();$('#notes').classList.remove('show')}});
// ---------- controllers ----------
// title terms
$$('#s-hook .term').forEach(b=>b.onclick=ev=>{ev.stopPropagation();const p=$('#pop-'+b.dataset.t),was=p.classList.contains('show');$$('#s-hook .pop').forEach(x=>x.classList.remove('show'));$$('#s-hook .term').forEach(x=>x.classList.remove('on'));if(!was){p.classList.add('show');b.classList.add('on')}});
$('#s-hook').addEventListener('click',e=>{if(!e.target.closest('.pop,.term')){$$('#s-hook .pop').forEach(x=>x.classList.remove('show'));$$('#s-hook .term').forEach(x=>x.classList.remove('on'))}});
ctrl['s-hook']={leave(){$$('#s-hook .pop').forEach(x=>x.classList.remove('show'));$$('#s-hook .term').forEach(x=>x.classList.remove('on'))}};
// background count-up
ctrl['s-bg']={done:false,step(s){const n=$('#oc-num'),l=$('#oc-line');
 if(s>=2&&!this.done){this.done=true;let t0=null;l.style.strokeDashoffset=0;const f=t=>{if(!t0)t0=t;const p=Math.min(1,(t-t0)/1100);n.textContent='~'+Math.round(45*p)+'M';if(p<1)requestAnimationFrame(f)};requestAnimationFrame(f)}
 if(s<2){this.done=false;n.textContent='~45M'}}};
// objectives: SOP <-> SO pairs
function pairSel(i){$$('#s-obj .pair').forEach((b,k)=>{b.classList.toggle('sel',k===i);b.classList.toggle('dim',i>=0&&k!==i)})}
$$('#s-obj .pair').forEach(b=>b.onclick=()=>{const i=+b.dataset.i;if(step<i+1)setStep(i+1);pairSel(i)});
ctrl['s-obj']={step(s){pairSel(s-1)}};
// research gaps
$$('#s-gaps .gap').forEach(b=>b.onclick=()=>{const i=+b.dataset.g;if(step<i+1)setStep(i+1);$$('#s-gaps .gap').forEach((g,k)=>g.classList.toggle('sel',k===i&&!g.classList.contains('sel')||false))});
ctrl['s-gaps']={step(s){$$('#s-gaps .gap').forEach((g,k)=>g.classList.toggle('sel',s>=1&&s<=4&&k===s-1))}};
// scope
function scopeView(v){$$('#sl-tog .chip').forEach(c=>c.classList.toggle('on',c.dataset.v===v));const A=$('#s-scope .colA'),B=$('#s-scope .colB');
 A.classList.toggle('dimc',v==='lim');B.classList.toggle('dimc',v==='scope');if(v!=='scope')B.classList.add('on')}
$$('#sl-tog .chip').forEach(c=>c.onclick=()=>{if(c.dataset.v!=='scope'&&step<2)setStep(2);scopeView(c.dataset.v)});
$$('#s-scope .lm').forEach(b=>b.onclick=()=>{const was=b.classList.contains('on');$$('#s-scope .lm').forEach(x=>x.classList.remove('on'));const B=$('#s-scope .colB');if(was)B.classList.remove('focus');else{b.classList.add('on');B.classList.add('focus')}});
ctrl['s-scope']={enter(){scopeView('both');$$('#s-scope .lm').forEach(x=>x.classList.remove('on'));$('#s-scope .colB').classList.remove('focus')}};
// data-flow pipeline (two slides)
const FL={'s-flowA':1,'s-flowB':5};let fRaf=null,fPlay=null,fLast=0;const fSpawn=new Map();
function flowStep(id,s){const sl=$('#'+id),cs=FL[id]+s;
 $$('.stg',sl).forEach(g=>{const k=+g.dataset.st;g.classList.toggle('show',k<=cs);g.classList.toggle('cur',k===cs);g.classList.toggle('past',k<cs)});
 $$('.fpath,.fhead',sl).forEach(p=>p.classList.toggle('on',+p.dataset.to<=cs));
 if(id==='s-flowA')$('#fa-tab').classList.toggle('split',cs>=3);sl._cs=cs}
function fLoop(t){const sl=slides[cur];if(!FL[sl.id]){fRaf=null;return}const dt=Math.min(60,t-(fLast||t));fLast=t;const G=$('.parts',sl);
 $$('.fpath.on',sl).forEach(p=>{const into=+p.dataset.to,curS=into===sl._cs,rate=curS?110:900;let acc=(fSpawn.get(p)||0)+dt;
  if(acc>rate){acc=0;const L=p.getTotalLength();const c=el('circle',{r:curS?5.5:4,fill:p.dataset.c||'#0e8f86',opacity:curS?.95:.5},G);c._p=p;c._L=L;c._s=0;c._v=p.classList.contains('long')?0.55:0.16}fSpawn.set(p,acc)});
 [...G.children].forEach(c=>{c._s+=dt*c._v;if(c._s>=c._L||!c._p.classList.contains('on')){c.remove();return}const q=c._p.getPointAtLength(c._s);c.setAttribute('cx',q.x);c.setAttribute('cy',q.y)});
 fRaf=requestAnimationFrame(fLoop)}
function fStart(){if(!fRaf){fLast=0;fRaf=requestAnimationFrame(fLoop)}}
function fStopRaf(){if(fRaf)cancelAnimationFrame(fRaf);fRaf=null;$$('.flow .parts').forEach(g=>g.innerHTML='')}
function fStop(){clearInterval(fPlay);fPlay=null;$$('.fplay').forEach(b=>b.textContent='▶ Play the flow')}
$$('.fplay').forEach(b=>b.onclick=()=>{if(fPlay){fStop();return}const sl=slides[cur];if(sl.id==='s-flowB'&&step>=steps(sl))setStep(0);
 $$('.fplay').forEach(x=>x.textContent='❚❚ Pause');fPlay=setInterval(()=>{const s2=slides[cur];if(!FL[s2.id]){fStop();return}
  if(step<steps(s2))setStep(step+1);else if(s2.id==='s-flowA')go(cur+1);else fStop()},2800)});
$$('.flow .stg').forEach(g=>g.addEventListener('click',e=>{if(e.target.closest('[data-go]'))return;const sl=g.closest('.slide');if(slides[cur]!==sl)return;setStep(+g.dataset.st-FL[sl.id])}));
for(const id in FL)ctrl[id]={enter:fStart,step(s){flowStep(id,s)},leave:fStopRaf};
$$('#s-flowA [data-seg]').forEach(b=>b.addEventListener('click',e=>{e.stopPropagation();if(step<2)setStep(2);const k=b.dataset.seg,t=$('#fa-tab'),was=t.dataset.hl===k;t.dataset.hl=was?'':k;$$('#s-flowA [data-seg]').forEach(x=>x.classList.toggle('on',!was&&x.dataset.seg===k))}));
$$('#s-flowB [data-env]').forEach(b=>b.addEventListener('click',e=>{e.stopPropagation();const on=b.dataset.env==='1';$$('#s-flowB [data-env]').forEach(x=>x.classList.toggle('on',x===b));$('#gterms').classList.toggle('noenv',!on);$('#genv').innerHTML=on?'Both versions will be compared on Test quarters.':'<b>Model A</b>: no weather terms. If B is not better, we will say so.'}));
$$('#s-flowB [data-pr]').forEach(b=>b.addEventListener('click',e=>{e.stopPropagation();const p=+b.dataset.pr;$$('#s-flowB [data-pr]').forEach(x=>x.classList.toggle('on',x===b));$('#vp').textContent='₱'+p+'/kg';$('#vres').textContent='₱'+(180*1000*p/1e6).toFixed(1)+'M'}));
// eval
const eR=rng(23),EN=96,eTrue=[],eObs=[],eWf=[];
const eYr=Array.from({length:24},()=>(eR()-.5)*70);for(let t=0;t<EN;t++){const v=eYr[Math.floor(t/4)]+300+[-60,80,40,-50][t%4]-t*0.6+(t>=85&&t<=87?-70:0)+(t%7===3?-25:0);eTrue.push(v);eObs.push(v+(eR()-.5)*36)}
for(let t=0;t<EN;t++)eWf.push(eTrue[t]+(eR()-.5)*30);
const qlab=t=>(2002+Math.floor(t/4))+' Q'+(t%4+1);let eRollT=null;
function eDraw(){const sp=+$('#e-split').value;$('#e-lab').textContent=qlab(sp);const svg=$('#e-chart');svg.innerHTML='';const W=1190,L=56,B=390,T=40;
 const X=t=>L+t*(W-L-20)/(EN-1),Y=v=>B-(v-120)/(440-120)*(B-T);const tu=Math.max(4,sp-14);
 el('rect',{x:L,y:T,width:X(tu)-L,height:B-T,fill:'#eef9f6'},svg);el('rect',{x:X(tu),y:T,width:X(sp)-X(tu),height:B-T,fill:'#e1f2ee'},svg);el('rect',{x:X(sp)-8,y:T,width:W-X(sp)+8,height:B-T,fill:'#fff7e6'},svg);
 el('text',{x:L+10,y:T-12,'font-size':19,'font-weight':700,fill:'#0e8f86'},svg,'TRAIN');el('text',{x:X(tu)+8,y:T-12,'font-size':19,'font-weight':700,fill:'#3c5a6b'},svg,'TUNE');el('text',{x:X(sp),y:T-12,'font-size':19,'font-weight':700,fill:'#d9822b'},svg,'TEST');
 for(let k=0;k<=4;k++){const v=120+80*k;el('line',{x1:L,x2:W-10,y1:Y(v),y2:Y(v),class:'ax'},svg);el('text',{x:L-8,y:Y(v)+5,'text-anchor':'end',class:'tick'},svg,v)}
 for(let t=0;t<EN;t+=16)el('text',{x:X(t),y:B+26,class:'tick','text-anchor':'middle'},svg,2002+t/4);el('text',{x:X(EN-1),y:B+26,class:'tick','text-anchor':'middle'},svg,'2025');
 let d='';eObs.forEach((v,t)=>d+=(t?'L':'M')+X(t)+','+Y(v));el('path',{d,stroke:'#a9bfc6','stroke-width':3,fill:'none'},svg);
 if(step>=1){let b='';for(let t=sp;t<EN;t++)b+=(t>sp?'L':'M')+X(t)+','+Y(eObs[t-4]);el('path',{d:b,stroke:'#7a8fa0','stroke-width':3,'stroke-dasharray':'8 6',fill:'none'},svg)}
 if(step>=2){let w='';for(let t=sp;t<EN;t++)w+=(t>sp?'L':'M')+X(t)+','+Y(eWf[t]);el('path',{d:w,stroke:'#0e8f86','stroke-width':4,fill:'none'},svg)}
 // metrics
 let sc=0,nn=0;for(let t=4;t<sp;t++){sc+=Math.abs(eObs[t]-eObs[t-4]);nn++}sc/=nn;
 const m=f=>{let a=0,r=0,n=0;for(let t=sp;t<EN;t++){const e=eObs[t]-f(t);a+=Math.abs(e);r+=e*e;n++}return{mae:a/n,rmse:Math.sqrt(r/n),mase:a/n/sc,n}};
 const mb=m(t=>eObs[t-4]),mw=m(t=>eWf[t]);const row=(lab,a,b,mx,d)=>`<div class="mt"><div class="mn"><span>${lab}</span></div>
 <div class="mr">baseline<div class="t"><div class="f" style="width:${step>=1?Math.min(100,a/mx*100):0}%;background:#7a8fa0"></div></div><b>${step>=1?fmt(a,d):'–'}</b></div>
 <div class="mr">workflow<div class="t"><div class="f" style="width:${step>=2?Math.min(100,b/mx*100):0}%;background:var(--sea)"></div></div><b>${step>=2?fmt(b,d):'–'}</b></div></div>`;
 $('#e-metrics').innerHTML=`<div class="small" style="margin-bottom:10px">${mb.n} test quarters · ${qlab(sp)} – ${qlab(EN-1)}</div>`+row('MAE (mt)',mb.mae,mw.mae,Math.max(mb.mae,mw.mae)*1.2,1)+row('RMSE (mt)',mb.rmse,mw.rmse,Math.max(mb.rmse,mw.rmse)*1.2,1)+row('MASE',mb.mase,mw.mase,Math.max(mb.mase,mw.mase,1)*1.2,2)
 +(step>=2?`<div style="font:600 19px/1.35 PF;color:var(--ink);margin-top:4px">${mw.mae<mb.mae?'Workflow beats the baseline on these quarters.':'Workflow does not beat the baseline: we would report that.'}</div>`:'')}
$('#e-split').oninput=()=>{if(step<1)setStep(1);eDraw()};
function eStop(){clearInterval(eRollT);eRollT=null;$('#e-roll').textContent='▶ Rolling origin'}
$('#e-roll').onclick=()=>{if(eRollT){eStop();return}if(step<2)setStep(2);const s=$('#e-split');s.value=70;eDraw();$('#e-roll').textContent='❚❚ Pause';eRollT=setInterval(()=>{if(+s.value>=88){eStop();return}s.value=+s.value+1;eDraw()},700)};
ctrl['s-eval']={step(){eDraw()},leave:eStop};
// value at risk
const VC=[["Province A · Cat 1",820,640,180,150],["Province B · Cat 2",410,300,260,290],["Province C · Cat 1",150,132,180,205],["Province D · Cat 2",260,190,140,175],["Province A · Cat 3",95,104,320,300]];
let vSel=0,vP='base';
$('#v-pick').innerHTML=VC.map((c,k)=>`<button class="chip" data-v="${k}" style="font-size:18px;padding:8px 13px">${c[0]}</button>`).join('');
const vVal=(c,p)=>Math.max(0,c[1]-c[2])*1000*(p==='proxy'?c[4]:c[3])*(1+ +$('#v-price').value/100);
const peso=v=>v>=1e6?'₱'+(v/1e6).toFixed(2)+'M':'₱'+Math.round(v).toLocaleString('en-US');
const vRank=$('#v-rank');vRank.innerHTML=VC.map((c,k)=>`<div class="rk" data-k="${k}"><div class="rn"></div><div class="rl">${c[0]}</div><div class="rt"><div class="rf"></div></div><div class="rv2"></div></div>`).join('');
function vDraw(){const c=VC[vSel],pct=+$('#v-price').value;$$('#v-pick .chip').forEach(b=>b.classList.toggle('on',+b.dataset.v===vSel));$$('#s-var [data-p]').forEach(b=>b.classList.toggle('on',b.dataset.p===vP));
 const sf=Math.max(0,c[1]-c[2]),pr=(vP==='proxy'?c[4]:c[3])*(1+pct/100);
 $('#v-sf').textContent=fmt(sf,0)+' mt';$('#v-pr').textContent='₱'+pr.toFixed(0)+'/kg';$('#v-prl').textContent=(vP==='proxy'?'unit-value proxy':'historical first-sale')+(pct?` · ${pct>0?'+':''}${pct}%`:'');$('#v-val').textContent=peso(vVal(c,vP));
 const svg=$('#v-chart');svg.innerHTML='';const W=710,B=164,T=24,mx=Math.max(c[1],c[2])*1.15,Y=v=>B-v/mx*(B-T);
 el('line',{x1:20,x2:W-20,y1:B,y2:B,class:'ax'},svg);
 el('rect',{x:150,y:Y(c[1]),width:150,height:B-Y(c[1]),fill:'#cfe6e1',rx:6},svg);el('text',{x:225,y:Y(c[1])-8,'text-anchor':'middle','font-size':18,'font-weight':700,fill:'#0b2a3c'},svg,fmt(c[1],0)+' mt');el('text',{x:225,y:B+22,'text-anchor':'middle',class:'tick'},svg,'Seasonal benchmark');
 el('rect',{x:410,y:Y(c[2]),width:150,height:B-Y(c[2]),fill:'#0e8f86',rx:6},svg);el('text',{x:485,y:Y(c[2])-8,'text-anchor':'middle','font-size':18,'font-weight':700,fill:'#0b2a3c'},svg,fmt(c[2],0)+' mt');el('text',{x:485,y:B+22,'text-anchor':'middle',class:'tick'},svg,'Next-quarter forecast');
 if(step>=1){if(sf>0){el('rect',{x:410,y:Y(c[1]),width:150,height:Y(c[2])-Y(c[1]),fill:'none',stroke:'#d9822b','stroke-width':3,'stroke-dasharray':'7 5',rx:4},svg);el('text',{x:575,y:(Y(c[1])+Y(c[2]))/2+6,'font-size':19,'font-weight':700,fill:'#d9822b'},svg,'shortfall')}else el('text',{x:575,y:Y(c[2])+20,'font-size':19,'font-weight':700,fill:'#0b8a5a'},svg,'no shortfall')}
 el('line',{x1:130,x2:580,y1:Y(c[1]),y2:Y(c[1]),stroke:'#6f8b99','stroke-dasharray':'4 4'},svg);
 // ranking
 const vals=VC.map(x=>vVal(x,vP)),order=vals.map((v,k)=>[v,k]).sort((a,b)=>b[0]-a[0]).map(x=>x[1]),mxv=Math.max(...vals)||1;
 $$('.rk',vRank).forEach(r=>{const k=+r.dataset.k,pos=order.indexOf(k);r.style.top=pos*86+'px';r.querySelector('.rn').textContent=pos+1;r.querySelector('.rf').style.width=vals[k]/mxv*100+'%';r.querySelector('.rv2').textContent=vals[k]?peso(vals[k]):'₱0';r.classList.toggle('sel',k===vSel)});
 const ob=VC.map(x=>vVal(x,'base')).map((v,k)=>[v,k]).sort((a,b)=>b[0]-a[0]).map(x=>x[1]),op=VC.map(x=>vVal(x,'proxy')).map((v,k)=>[v,k]).sort((a,b)=>b[0]-a[0]).map(x=>x[1]);
 const moved=ob.filter((k,i)=>op[i]!==k).length;$('#v-stab').innerHTML=`Price sensitivity: top-ranked combination ${ob[0]===op[0]?'<b>unchanged</b>':'<b style="color:var(--coral)">changes</b>'} under the proxy price; ${moved} of ${VC.length} positions shift. A uniform ±% change scales values but keeps the order.`}
$$('#v-pick .chip').forEach(b=>b.onclick=()=>{vSel=+b.dataset.v;vDraw()});$$('#s-var [data-p]').forEach(b=>b.onclick=()=>{vP=b.dataset.p;vDraw()});
$('#v-price').oninput=()=>{if(step<2)setStep(2);vDraw()};
ctrl['s-var']={step(){vDraw()}};
// Q bank
let qbCat=-1;
function qbDraw(){const term=($('#qb-search').value||'').toLowerCase();
 $('#qb-cats').innerHTML=`<button class="qcat${qbCat<0?' on':''}" data-c="-1">All questions<span>${QB.reduce((a,c)=>a+c[1].length,0)}</span></button>`+QB.map((c,k)=>`<button class="qcat${qbCat===k?' on':''}" data-c="${k}">${c[0]}<span>${c[1].length}</span></button>`).join('');
 let h='';QB.forEach((c,k)=>{if(qbCat>=0&&k!==qbCat)return;c[1].forEach(([q,a])=>{if(term&&!(q+' '+a).toLowerCase().includes(term))return;
  const extra=q.startsWith('How will you separate prediction')?'<p style="margin-top:10px"><span class="link" data-go="b-cause">Open the backup slide →</span></p>':'';h+=qaHTML(q,'<p>'+a+'</p>'+extra,false,c[0])})});
 $('#qb-list').innerHTML=h||'<p class="body">No matching questions.</p>';$$('#qb-cats .qcat').forEach(b=>b.onclick=()=>{qbCat=+b.dataset.c;qbDraw()})}
$('#qb-search').oninput=qbDraw;ctrl['b-qbank']={enter:qbDraw};
// init
const h=location.hash.slice(1),hi=slides.findIndex(s=>s.id===h);
slides[0].classList.add('active');go(hi>0?hi:0);
window.__deck={go,next,prev,setStep,goLabel,get cur(){return cur},get step(){return step},slides};
})();

/* v6 ambient: bubbles + gentle parallax */
(()=>{const a=document.getElementById('amb');if(!a)return;let r=7;const rnd=()=>(r=(r*9301+49297)%233280)/233280;
 const X=[18,40,62,84,30,70,1836,1858,1880,1846,1870,1894];
 X.forEach((x,i)=>{const b=document.createElement('i');b.className='bub';const s=8+rnd()*16;b.style.cssText=`left:${x}px;width:${s}px;height:${s}px;animation-duration:${22+rnd()*20}s;animation-delay:${-rnd()*40}s`;a.appendChild(b)});
 const st=document.getElementById('stage');addEventListener('mousemove',e=>{if(document.body.classList.contains('nomo')||matchMedia('(prefers-reduced-motion: reduce)').matches)return;const dx=e.clientX/innerWidth-.5,dy=e.clientY/innerHeight-.5;a.querySelectorAll('.par').forEach(p=>{const d=+p.dataset.d;p.style.transform=`translate(${-dx*d}px,${-dy*d}px)`})});
})();

/* v7: wandering fish (canvas, rAF, pauses when hidden / motion off) */
(()=>{const cv=document.getElementById('fish');if(!cv)return;const g=cv.getContext('2d'),W=1920,H=1080,st=document.getElementById('stage');
 let sd=11;const R=()=>(sd=(sd*16807)%2147483647)/2147483647;
 // z: 0 far .. 1 near
 const SP=[{z:.15,c:'#0a8fa0'},{z:.25,c:'#0a8fa0'},{z:.35,c:'#f08a3c',st:1},{z:.45,c:'#2a9fc2'},{z:.55,c:'#f2b53a'},{z:.7,c:'#f08a3c',st:1},{z:.85,c:'#0a8fa0'},{z:1,c:'#f08a3c',st:1}];
 const F=SP.map(s=>({...s,x:R()*W,y:120+R()*820,a:(R()<.5?0:Math.PI)+(R()-.5)*.4,len:40+s.z*110,v:.25+s.z*.55+R()*.15,ph:R()*6.28,wob:R()*6.28,alpha:.16+s.z*.26}));
 let mx=-1e4,my=-1e4;addEventListener('mousemove',e=>{const r=st.getBoundingClientRect(),k=r.width/W;mx=(e.clientX-r.left)/k;my=(e.clientY-r.top)/k});addEventListener('mouseleave',()=>{mx=my=-1e4});
 function fish(f,t){const L=f.len,dir=Math.cos(f.a)<0?-1:1,tilt=Math.max(-.35,Math.min(.35,Math.sin(f.a)*dir));
  g.save();g.translate(f.x,f.y);g.scale(dir,1);g.rotate(tilt*dir*dir);g.globalAlpha=f.alpha;
  if(f.z>.8)g.filter='blur(2px)';else if(f.z<.3)g.filter='blur(.6px)';else g.filter='none';
  const sw=Math.sin(t*0.006*(1+f.v)+f.ph)*0.28;
  // tail
  g.fillStyle=f.c;g.beginPath();g.moveTo(-L*.42,0);g.lineTo(-L*.78,-L*.26+sw*L*.2);g.quadraticCurveTo(-L*.68,sw*L*.1,-L*.78,L*.26+sw*L*.2);g.closePath();g.fill();
  // body
  g.beginPath();g.moveTo(L*.5,0);g.bezierCurveTo(L*.3,-L*.34,-L*.3,-L*.3,-L*.46,0);g.bezierCurveTo(-L*.3,L*.3,L*.3,L*.34,L*.5,0);g.fill();
  // dorsal fin
  g.beginPath();g.moveTo(L*.05,-L*.24);g.quadraticCurveTo(-L*.12,-L*.42,-L*.26,-L*.2);g.fill();
  if(f.st){g.save();g.beginPath();g.moveTo(L*.5,0);g.bezierCurveTo(L*.3,-L*.34,-L*.3,-L*.3,-L*.46,0);g.bezierCurveTo(-L*.3,L*.3,L*.3,L*.34,L*.5,0);g.clip();g.fillStyle='rgba(255,255,255,.85)';g.fillRect(L*.16,-L,L*.09,2*L);g.fillRect(-L*.16,-L,L*.1,2*L);g.restore()}
  g.fillStyle='rgba(11,42,60,.7)';g.beginPath();g.arc(L*.33,-L*.05,Math.max(1.5,L*.035),0,6.28);g.fill();
  g.restore()}
 function step(f,dt,t){f.wob+=dt*.0004;f.a+=Math.sin(f.wob*3+f.ph)*.0016*dt*.06;
  // keep mostly horizontal
  const h=Math.cos(f.a)<0?Math.PI:0;let d=Math.atan2(Math.sin(f.a-h),Math.cos(f.a-h));if(Math.abs(d)>.45)f.a-=Math.sign(d)*.002*dt;
  // soft vertical bounds
  if(f.y<110)f.a+=(Math.cos(f.a)>0?.002:-.002)*dt;if(f.y>960)f.a-=(Math.cos(f.a)>0?.002:-.002)*dt;
  // flee cursor
  const dx=f.x-mx,dy=f.y-my,dd=Math.hypot(dx,dy),fr=200+f.z*80;let boost=0;
  if(dd<fr){const want=Math.atan2(dy,dx),df=Math.atan2(Math.sin(want-f.a),Math.cos(want-f.a));f.a+=df*.004*dt;boost=(1-dd/fr)*1.6}
  const v=(f.v+boost)*dt*.06;f.x+=Math.cos(f.a)*v;f.y+=Math.sin(f.a)*v;
  const m=f.len+40;if(f.x>W+m){f.x=-m;f.y=140+R()*780}else if(f.x<-m){f.x=W+m;f.y=140+R()*780}}
 const still=()=>document.body.classList.contains('nomo')||matchMedia('(prefers-reduced-motion: reduce)').matches;
 let last=0,raf=0;function draw(t){g.clearRect(0,0,W,H);F.forEach(f=>fish(f,t))}
 function loop(t){raf=0;const dt=Math.min(50,last?t-last:16);last=t;if(still()){draw(t);return}F.forEach(f=>step(f,dt,t));draw(t);raf=requestAnimationFrame(loop)}
 const go=()=>{if(!raf&&!document.hidden&&!still()){last=0;raf=requestAnimationFrame(loop)}};
 document.addEventListener('visibilitychange',()=>{if(document.hidden){cancelAnimationFrame(raf);raf=0}else go()});
 new MutationObserver(go).observe(document.body,{attributes:true,attributeFilter:['class']});
 matchMedia('(prefers-reduced-motion: reduce)').addEventListener?.('change',go);
 window.__fish={F,running:()=>!!raf};go();
})();
