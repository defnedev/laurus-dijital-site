// Laurus Dijital — shared behaviour
const WA_NUMBER = "905434309702";
const wa = t => `https://wa.me/${WA_NUMBER}?text=${encodeURIComponent(t)}`;
const DEFAULT_MSG = "Merhaba, Laurus Dijital'in sitesinden yazıyorum. İşletmem için bilgi almak istiyorum.";

document.querySelectorAll(".js-wa").forEach(a => {
  a.href = wa(a.dataset.msg || DEFAULT_MSG); a.target = "_blank"; a.rel = "noopener";
});

// mobile menu
const burger = document.getElementById("burger"), menu = document.getElementById("menu");
if (burger && menu){
  burger.addEventListener("click", () => {
    const o = menu.classList.toggle("open");
    burger.setAttribute("aria-expanded", o);
    burger.setAttribute("aria-label", o ? "Menüyü kapat" : "Menüyü aç");
  });
}

// services dropdown
document.querySelectorAll(".dd").forEach(dd => {
  const btn = dd.querySelector("button"), panel = dd.querySelector(".dd-panel");
  const set = o => { panel.hidden = !o; btn.setAttribute("aria-expanded", o); };
  btn.addEventListener("click", e => { e.stopPropagation(); set(panel.hidden); });
  document.addEventListener("click", e => { if (!dd.contains(e.target)) set(false); });
  document.addEventListener("keydown", e => { if (e.key === "Escape"){ set(false); } });
});

// before / after toggle
document.querySelectorAll("[data-ba]").forEach(root => {
  const btns = root.querySelectorAll("[data-ba-set]");
  const views = root.querySelectorAll("[data-ba-view]");
  btns.forEach(b => b.addEventListener("click", () => {
    const v = b.dataset.baSet;
    btns.forEach(x => x.setAttribute("aria-pressed", String(x === b)));
    views.forEach(x => { x.hidden = x.dataset.baView !== v; });
  }));
});

// package buttons prefill form note
document.querySelectorAll("[data-plan]").forEach(b => b.addEventListener("click", () => {
  const n = document.getElementById("f-note"); if (n) n.value = b.dataset.plan + " ile ilgileniyorum.";
}));

// quick form -> WhatsApp
const form = document.getElementById("quick");
if (form){
  form.addEventListener("submit", e => {
    e.preventDefault();
    const err = document.getElementById("f-err");
    const name = form.fname.value.trim(), biz = form.biz.value.trim();
    if (!name || !biz){
      err.textContent = !name ? "Adını yaz, sana nasıl hitap edeceğimizi bilelim." : "İşletmenin adını yaz, önceden inceleyebilelim.";
      (!name ? form.fname : form.biz).focus(); return;
    }
    err.textContent = "";
    const lines = [`Merhaba, ben ${name}.`, `İşletme: ${biz}`, `İhtiyaç: ${form.need.value}`];
    if (form.note.value.trim()) lines.push(form.note.value.trim());
    const a = document.createElement("a"); a.href = wa(lines.join("\n")); a.target = "_blank"; a.rel = "noopener";
    document.body.appendChild(a); a.click(); a.remove();
  });
}

// tabs
document.querySelectorAll("[data-tabs]").forEach(root => {
  const btns = [...root.querySelectorAll(':scope > .tablist [role="tab"]')];
  const show = id => btns.forEach(b => {
    const on = b.getAttribute("aria-controls") === id;
    b.setAttribute("aria-selected", on); b.tabIndex = on ? 0 : -1;
    document.getElementById(b.getAttribute("aria-controls")).hidden = !on;
  });
  root._show = show;
  btns.forEach((b, i) => {
    b.addEventListener("click", () => show(b.getAttribute("aria-controls")));
    b.addEventListener("keydown", e => {
      const d = e.key === "ArrowRight" ? 1 : e.key === "ArrowLeft" ? -1 : 0; if (!d) return;
      const n = btns[(i + d + btns.length) % btns.length]; n.focus(); show(n.getAttribute("aria-controls"));
    });
  });
});
function openHash(){
  const id = decodeURIComponent(location.hash.slice(1)); if (!id) return;
  const el = document.getElementById(id); if (!el) return;
  const panel = el.closest('[role="tabpanel"]'); if (!panel) return;
  const root = panel.closest("[data-tabs]"); root._show(panel.id);
  setTimeout(() => root.scrollIntoView({behavior:"smooth", block:"start"}), 30);
}
window.addEventListener("hashchange", openHash); openHash();
document.querySelectorAll('a[href^="#"]').forEach(a => a.addEventListener("click", () => setTimeout(openHash, 0)));

// scale mock screens to their frame
const fitAll = () => document.querySelectorAll("[data-fit]").forEach(el => {
  const p = el.parentElement; if (!p.clientWidth) return;
  el.style.transform = `scale(${p.clientWidth / +el.dataset.fit})`;
});
fitAll(); window.addEventListener("resize", fitAll);
if ("ResizeObserver" in window) { const ro = new ResizeObserver(fitAll); document.querySelectorAll(".scr,.pscr").forEach(e => ro.observe(e)); }

// hero showcase rotation
document.querySelectorAll("[data-showcase]").forEach(sc => {
  const sets = [...sc.querySelectorAll("[data-show]")], btns = [...sc.querySelectorAll("[data-show-btn]")], caps = [...sc.querySelectorAll("[data-cap]")];
  let i = 0, timer; const DUR = 5000;
  const go = n => {
    i = (n + sets.length) % sets.length; const id = sets[i].dataset.show;
    sets.forEach(s => { const on = s.dataset.show === id; s.classList.toggle("on", on); s.setAttribute("aria-hidden", String(!on)); });
    caps.forEach(c => c.classList.toggle("on", c.dataset.cap === id));
    btns.forEach(b => b.setAttribute("aria-pressed", String(b.dataset.showBtn === id)));
    sets[i].querySelectorAll("img[loading=lazy]").forEach(im => im.loading = "eager");
    fitAll();
  };
  const reduce = matchMedia("(prefers-reduced-motion: reduce)").matches;
  const start = () => { if (reduce) return; clearInterval(timer); timer = setInterval(() => go(i + 1), DUR); sc.classList.remove("paused"); };
  const stop = () => { clearInterval(timer); sc.classList.add("paused"); };
  btns.forEach((b, n) => b.addEventListener("click", () => { go(n); start(); }));
  sc.querySelector("[data-show-prev]")?.addEventListener("click", () => { go(i - 1); start(); });
  sc.querySelector("[data-show-next]")?.addEventListener("click", () => { go(i + 1); start(); });
  sc.addEventListener("mouseenter", stop); sc.addEventListener("mouseleave", start);
  // preload next set's images shortly after load
  setTimeout(() => sets.forEach(s => s.querySelectorAll("img[loading=lazy]").forEach(im => im.loading = "eager")), 4000);
  setTimeout(start, document.documentElement.classList.contains("intro") ? 3600 : 0);
});

// works filter
document.querySelectorAll("[data-works]").forEach(w => {
  const btns = [...w.querySelectorAll("[data-filter]")], items = [...w.querySelectorAll("[data-cat]")], empty = w.querySelector(".wempty");
  btns.forEach(b => b.addEventListener("click", () => {
    const f = b.dataset.filter; let n = 0;
    btns.forEach(x => x.setAttribute("aria-pressed", String(x === b)));
    items.forEach(it => { const on = f === "hepsi" || it.dataset.cat === f; it.hidden = !on; if (on) n++; });
    if (empty) empty.hidden = n > 0;
    fitAll();
  }));
});

// intro skip
const skip = document.getElementById("in-skip");
if (skip) skip.addEventListener("click", () => document.documentElement.classList.add("skipped"));

// ===== v7 cinematics =====
const root = document.documentElement;
const reduceMo = matchMedia("(prefers-reduced-motion: reduce)").matches;
const isHome = document.body.classList.contains("pg-index");

// reveal on scroll
const rvs = document.querySelectorAll("[data-rv]");
if ("IntersectionObserver" in window && !reduceMo) {
  const io = new IntersectionObserver(es => es.forEach(e => { if (e.isIntersecting) { e.target.classList.add("in"); io.unobserve(e.target); } }), { rootMargin: "0px 0px -5% 0px", threshold: 0.04 });
  rvs.forEach(el => io.observe(el));
} else rvs.forEach(el => el.classList.add("in"));

// scroll-driven scenes
const mani = document.querySelector("[data-mani]"), maniSec = mani && mani.closest(".mani");
const words = mani ? [...mani.querySelectorAll("span")] : [];
const works = document.querySelector(".works3"), track = document.querySelector("[data-hscroll]"), hprog = document.querySelector("[data-hprog]");
const line = document.querySelector("[data-line]");
const hero = document.querySelector(".hero3");
const desk = () => innerWidth > 900;
let dist = 0;
const sizeWorks = () => {
  if (!works || !track) return;
  if (desk() && !reduceMo) { dist = Math.max(0, track.scrollWidth - innerWidth + 48); works.style.height = (innerHeight + dist / 1.8) + "px"; works.classList.add("pinned"); }
  else { works.style.height = ""; works.classList.remove("pinned"); track.style.transform = ""; }
};
const clamp = (v, a, b) => Math.min(b, Math.max(a, v));
let ticking = false;
const onScroll = () => {
  ticking = false; const y = scrollY, vh = innerHeight;
  root.classList.toggle("scrolled", y > 40);
  if (hero) { const p = clamp(y / vh, 0, 1); hero.style.setProperty("--hp", p.toFixed(3)); }
  if (maniSec && words.length) {
    const r = maniSec.getBoundingClientRect(); const span = maniSec.offsetHeight - vh;
    const p = reduceMo ? 1 : clamp((-r.top + vh * 0.25) / (span + vh * 0.15), 0, 1);
    const lit = Math.round(p * words.length);
    words.forEach((w, i) => w.classList.toggle("on", i < lit));
  }
  if (works && track && works.classList.contains("pinned")) {
    const r = works.getBoundingClientRect(); const p = clamp(-r.top / Math.max(1, dist / 1.8), 0, 1);
    track.style.transform = `translate3d(${-p * dist}px,0,0)`;
    if (hprog) hprog.style.transform = `scaleX(${p})`;
  } else if (track && hprog) {
    const p = track.scrollLeft / Math.max(1, track.scrollWidth - track.clientWidth); hprog.style.transform = `scaleX(${p})`;
  }
  if (line) { const r = line.getBoundingClientRect(); const p = clamp((vh * 0.85 - r.top) / (r.height + vh * 0.3), 0, 1); line.style.setProperty("--lp", p.toFixed(3)); }
};
const req = () => { if (!ticking) { ticking = true; requestAnimationFrame(onScroll); } };
addEventListener("scroll", req, { passive: true });
addEventListener("resize", () => { sizeWorks(); req(); });
if (track) track.addEventListener("scroll", req, { passive: true });
addEventListener("load", () => { sizeWorks(); req(); });
sizeWorks(); onScroll();

/* v10 app showcase */
(function(){
  var s=document.querySelector('[data-appshow]'); if(!s) return;
  var sc=[].slice.call(s.querySelectorAll('.as-scene')), tabs=[].slice.call(s.querySelectorAll('[data-as-tab]')), bar=s.querySelector('[data-as-bar]');
  var mq=window.matchMedia('(min-width: 901px)'), cur=-1, n=sc.length;
  function set(i){ if(i===cur) return; cur=i; sc.forEach(function(e,k){e.classList.toggle('on',k===i)}); tabs.forEach(function(t,k){t.setAttribute('aria-selected',k===i?'true':'false')}); }
  function tick(){
    if(!mq.matches) return;
    var r=s.getBoundingClientRect(), total=s.offsetHeight-window.innerHeight; if(total<=0) return;
    var p=Math.min(1,Math.max(0,-r.top/total)), i=Math.min(n-1,Math.floor(p*n));
    set(i); sc[i].style.setProperty('--sp',Math.min(1,p*n-i).toFixed(3));
    if(bar) bar.style.transform='scaleX('+p.toFixed(3)+')';
  }
  var raf=0; function onS(){ if(!raf){ raf=requestAnimationFrame(function(){raf=0;tick();}); } }
  tabs.forEach(function(t,k){ t.addEventListener('click',function(){
    var total=s.offsetHeight-window.innerHeight, top=s.getBoundingClientRect().top+window.pageYOffset;
    window.scrollTo({top:top+total*(k+0.35)/n,behavior:'smooth'});
  });});
  var io=null;
  function mode(){
    if(mq.matches){ if(io){io.disconnect();io=null;} cur=-1; tick(); if(cur<0) set(0); }
    else { sc.forEach(function(e){e.classList.remove('on')}); cur=-1;
      if('IntersectionObserver' in window){ io=new IntersectionObserver(function(es){es.forEach(function(e){ if(e.isIntersecting){e.target.classList.add('on'); io.unobserve(e.target);} })},{threshold:.22}); sc.forEach(function(e){io.observe(e)}); }
      else sc.forEach(function(e){e.classList.add('on')}); }
  }
  window.addEventListener('scroll',onS,{passive:true}); window.addEventListener('resize',onS);
  if(mq.addEventListener) mq.addEventListener('change',mode); mode();
})();

/* v16 live app mockups: lazy-load animation module near the showcase */
(function(){
  var s=document.querySelector('[data-appshow]'); if(!s) return;
  var done=false;
  function go(){ if(done) return; done=true; var sc=document.createElement('script'); sc.src='/assets/live.js?v=23d66ccb1f'; sc.async=true; document.head.appendChild(sc); }
  if('IntersectionObserver' in window){ var o=new IntersectionObserver(function(es){ if(es.some(function(e){return e.isIntersecting})){ o.disconnect(); go(); } },{rootMargin:'600px 0px'}); o.observe(s); } else go();
})();

/* v17 hide floating WhatsApp when the contact block or footer is on screen */
(function(){
  var f=document.querySelector('.wa-float'); if(!f||!('IntersectionObserver' in window)) return;
  var on=new Set(); var o=new IntersectionObserver(function(es){es.forEach(function(e){ if(e.isIntersecting) on.add(e.target); else on.delete(e.target); }); f.classList.toggle('wa-hide', on.size>0);},{threshold:.12});
  ['#iletisim','footer'].forEach(function(q){var el=document.querySelector(q); if(el) o.observe(el);});
})();
