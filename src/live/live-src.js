/* Laurus live app mockups: globe (oh same.), chart (Sorbi), eight (Sekiz8), tree (Çınar), nefes (Nefes) */
(function () {
  var RM = window.matchMedia && matchMedia('(prefers-reduced-motion: reduce)').matches;
  var NS = 'http://www.w3.org/2000/svg';

  // map natural image px -> css px inside .iph-scr (img uses object-fit:cover, object-position:top)
  function geom(img) {
    var w = img.clientWidth, h = img.clientHeight, nw = img.naturalWidth, nh = img.naturalHeight;
    var s = Math.max(w / nw, h / nh);
    return { s: s, x: img.offsetLeft + (w - nw * s) / 2, y: img.offsetTop, w: w, h: h, nw: nw, nh: nh };
  }
  function layer(img, cls) {
    var d = document.createElement('div');
    d.className = 'lv ' + (cls || '');
    d.setAttribute('aria-hidden', 'true');
    img.parentNode.appendChild(d);
    return d;
  }
  function svgOver(img) {
    var g = geom(img);
    var sv = document.createElementNS(NS, 'svg');
    sv.setAttribute('viewBox', '0 0 ' + g.nw + ' ' + g.nh);
    sv.setAttribute('preserveAspectRatio', 'xMidYMin slice');
    sv.setAttribute('class', 'lv lv-svg');
    sv.setAttribute('aria-hidden', 'true');
    img.parentNode.appendChild(sv);
    function fit() { var g = geom(img); sv.style.cssText = 'left:' + img.offsetLeft + 'px;top:' + img.offsetTop + 'px;width:' + g.w + 'px;height:' + g.h + 'px'; }
    fit(); onResize(img, fit);
    return sv;
  }
  function onResize(el, fn) {
    if ('ResizeObserver' in window) new ResizeObserver(fn).observe(el); else addEventListener('resize', fn);
  }
  function ready(img, fn) { if (img.complete && img.naturalWidth) fn(); else img.addEventListener('load', fn, { once: true }); }
  function active(el) { var sc = el.closest('.as-scene'); return !sc || sc.classList.contains('on'); }

  // ---------- oh same. globe ----------
  var CITIES = [[29, 41], [-0.1, 51.5], [2.3, 48.9], [13.4, 52.5], [-3.7, 40.4], [12.5, 41.9], [31.2, 30], [3.4, 6.5], [36.8, -1.3], [28, -26.2], [55.3, 25.2], [51.4, 35.7], [72.8, 19], [77.2, 28.6], [100.5, 13.7], [139.7, 35.7], [127, 37.6], [116.4, 39.9], [151.2, -33.9], [37.6, 55.8], [-74, 40.7], [-118.2, 34], [-99.1, 19.4], [-46.6, -23.5], [-58.4, -34.6], [-79.4, 43.7], [32.9, 39.9], [27.1, 38.4], [49.9, 40.4], [23.7, 38], [4.9, 52.4], [18, 59.3], [106.8, -6.2], [-77, -12], [-74, 4.7], [-7.6, 33.6], [46.7, 24.7], [67, 24.9], [30.5, 50.4], [10, 53.5], [-9.1, 38.7], [121.5, 31.2], [120.9, 14.6], [-43.2, -22.9], [18.4, -33.9]];
  var MOODS = ['#F28A3C', '#E8457A', '#A44CF0', '#7EB6F7', '#F5C84B', '#8FD9C2'];
  function globe(ph, img) {
    if (!window.D3G || !window.LAUR_LAND) return;
    var G = window.D3G, land = window.LAUR_LAND;
    var cv = document.createElement('canvas'); cv.className = 'lv lv-globe'; cv.setAttribute('aria-hidden', 'true');
    img.parentNode.appendChild(cv);
    var ctx = cv.getContext('2d'), dpr = Math.min(2, window.devicePixelRatio || 1);
    var CX = 389.5, CY = 379.5, R = 229, size = 0, proj = G.geoOrthographic().clipAngle(90), path = G.geoPath(proj, ctx), grat = G.geoGraticule10();
    var lights = CITIES.map(function (c, i) { return { c: c, col: MOODS[i % MOODS.length], per: 2.6 + (i * 7 % 13) / 2.5, ph: (i * 1.7) % 6.28 }; });
    function fit() {
      var g = geom(img), r = R * g.s; size = Math.round(r * 2 + 4);
      cv.style.cssText = 'left:' + (g.x + CX * g.s - r - 2) + 'px;top:' + (g.y + CY * g.s - r - 2) + 'px;width:' + size + 'px;height:' + size + 'px';
      cv.width = size * dpr; cv.height = size * dpr;
      proj.translate([size * dpr / 2, size * dpr / 2]).scale(r * dpr);
    }
    fit(); onResize(img, fit);
    var t0 = performance.now(), sphere = { type: 'Sphere' };
    function draw(now) {
      var t = RM ? 0 : (now - t0) / 1000, lon = -15 - t * 8;
      proj.rotate([lon, -24]);
      var W = cv.width; ctx.clearRect(0, 0, W, W);
      ctx.save(); ctx.beginPath(); path(sphere); ctx.clip();
      ctx.fillStyle = '#3C2C56'; ctx.fillRect(0, 0, W, W);
      ctx.beginPath(); path(grat); ctx.strokeStyle = 'rgba(170,150,235,.16)'; ctx.lineWidth = dpr * .7; ctx.stroke();
      ctx.beginPath(); path(land); ctx.fillStyle = '#54427A'; ctx.fill(); ctx.strokeStyle = 'rgba(190,170,255,.38)'; ctx.lineWidth = dpr * .7; ctx.stroke();
      // night side fixed in screen space (sun to the upper-left)
      var sunLon = -lon - 75, night = G.geoCircle().center([sunLon + 180, -12]).radius(90)();
      ctx.beginPath(); path(night); ctx.fillStyle = 'rgba(6,2,20,.66)'; ctx.fill();
      ctx.strokeStyle = 'rgba(236,196,128,.85)'; ctx.lineWidth = dpr * 1.1; ctx.stroke();
      // mood lights
      var cen = [-lon, 24];
      for (var i = 0; i < lights.length; i++) {
        var L = lights[i];
        if (G.geoDistance(L.c, cen) > 1.48) continue;
        var a = .5 + .5 * Math.sin(t * 6.283 / L.per + L.ph); a = a * a * a;
        if (a < .03) continue;
        var p = proj(L.c), rr = dpr * (1.1 + 2.6 * a);
        var gr = ctx.createRadialGradient(p[0], p[1], 0, p[0], p[1], rr * 2.6);
        gr.addColorStop(0, L.col); gr.addColorStop(.3, L.col); gr.addColorStop(1, 'rgba(0,0,0,0)');
        ctx.globalAlpha = Math.min(1, .15 + .85 * a); ctx.fillStyle = gr; ctx.beginPath(); ctx.arc(p[0], p[1], rr * 2.6, 0, 6.283); ctx.fill();
        ctx.globalAlpha = 1; ctx.fillStyle = '#fff'; ctx.beginPath(); ctx.arc(p[0], p[1], dpr * .9 * (.3 + a), 0, 6.283); ctx.fill();
      }
      ctx.restore();
      // rim
      ctx.beginPath(); path(sphere); ctx.strokeStyle = '#8F6CF2'; ctx.lineWidth = dpr * 2; ctx.stroke();
    }
    loop(ph, draw);
  }

  // shared rAF loop that only runs while the scene is active and on screen
  var jobs = [];
  var vis = new Set();
  var io = 'IntersectionObserver' in window ? new IntersectionObserver(function (es) { es.forEach(function (e) { if (e.isIntersecting) vis.add(e.target); else vis.delete(e.target); }); }, { rootMargin: '100px' }) : null;
  function loop(el, fn) { jobs.push({ el: el, fn: fn, drawn: false }); if (io) io.observe(el); else vis.add(el); if (jobs.length === 1) requestAnimationFrame(tick); }
  function tick(now) {
    for (var i = 0; i < jobs.length; i++) {
      var j = jobs[i];
      if (vis.has(j.el) && active(j.el) && !document.hidden && (!RM || !j.drawn)) { j.fn(now); j.drawn = true; }
    }
    requestAnimationFrame(tick);
  }

  // ---------- Sorbi chart: slowly turning sky + sweep + glowing planets ----------
  function chart(ph, img) {
    var CX = 397, CY = 532, R = 312;
    var d = layer(img, 'lv-chart');
    d.innerHTML = '<div class="lv-rot"><img alt="" src="' + img.currentSrc + '"><i class="lv-sweep"></i><b class="lv-pl" style="--x:-48;--y:-203"></b><b class="lv-pl" style="--x:204;--y:30;--d:-1.4s"></b></div>';
    var im2 = d.querySelector('img');
    function fit() {
      var g = geom(img), r = R * g.s;
      d.style.cssText = 'left:' + (g.x + CX * g.s - r) + 'px;top:' + (g.y + CY * g.s - r) + 'px;width:' + 2 * r + 'px;height:' + 2 * r + 'px;--s:' + g.s;
      im2.style.cssText = 'width:' + g.nw * g.s + 'px;height:' + g.nh * g.s + 'px;left:' + (-(CX - R) * g.s) + 'px;top:' + (-(CY - R) * g.s) + 'px';
    }
    fit(); onResize(img, fit);
  }

  // ---------- Sekiz8: shake with haptic buzz, a new answer each time ----------
  function eight(ph, img) {
    var srcs = ['sk-evet', 'sk-sec', 'sk-sekiz'];
    var base = img.currentSrc.replace(/sk-sekiz\.webp.*/, '');
    var imgs = [img].concat(srcs.slice(0, 2).map(function (s) { var x = new Image(); x.alt = ''; x.decoding = 'async'; x.src = base + s + '.webp'; x.className = 'lv-alt'; img.parentNode.insertBefore(x, img.nextSibling); return x; }));
    imgs.forEach(function (x, i) { x.classList.toggle('lv-on', i === 0); x.classList.add('lv-fade'); });
    var dev = ph.parentNode, waves = document.createElement('div');
    waves.className = 'lv-buzz'; waves.setAttribute('aria-hidden', 'true');
    waves.innerHTML = '<i class="l"></i><i class="l"></i><i class="r"></i><i class="r"></i>';
    dev.appendChild(waves);
    var k = 0, busy = false;
    function shake() {
      if (busy || !active(ph) || document.hidden || !vis.has(ph)) return;
      busy = true;
      ph.classList.add('lv-shaking'); waves.classList.add('on');
      imgs[k].classList.add('lv-dim');
      setTimeout(function () {
        imgs[k].classList.remove('lv-on', 'lv-dim'); k = (k + 1) % imgs.length; imgs[k].classList.add('lv-on');
      }, 620);
      setTimeout(function () { ph.classList.remove('lv-shaking'); waves.classList.remove('on'); busy = false; }, 900);
    }
    if (io) io.observe(ph); else vis.add(ph);
    if (!RM) setInterval(shake, 3200);
  }

  // ---------- Çınar: real 3D tree turning (pre-rendered loop) ----------
  function tree(ph, img) {
    var X = 0, Y = 106, S = 780, H = 716;
    var v = document.createElement('video');
    v.className = 'lv lv-video'; v.muted = true; v.loop = true; v.playsInline = true; v.setAttribute('playsinline', ''); v.setAttribute('muted', ''); v.preload = 'none'; v.setAttribute('aria-hidden', 'true');
    var base = img.currentSrc.replace(/img\/app\/.*/, 'img/app/');
    v.innerHTML = '<source src="' + base + 'cn-tree.webm" type="video/webm"><source src="' + base + 'cn-tree.mp4" type="video/mp4">';
    img.parentNode.appendChild(v);
    function fit() { var g = geom(img); v.style.cssText = 'left:' + (g.x + X * g.s) + 'px;top:' + (g.y + Y * g.s) + 'px;width:' + S * g.s + 'px;height:' + H * g.s + 'px'; }
    fit(); onResize(img, fit);
    v.addEventListener('playing', function () { v.classList.add('lv-on'); });
    if (RM) return;
    var started = false;
    loop(ph, function () {
      if (!started) { started = true; v.preload = 'auto'; v.load(); }
      if (v.paused) { var pr = v.play(); if (pr && pr.catch) pr.catch(function () {}); }
    });
    setInterval(function () { if (!v.paused && (!vis.has(ph) || !active(ph) || document.hidden)) v.pause(); }, 700);
  }

  // ---------- Nefes: sun glows, light travels along the day arc ----------
  function nefes(ph, img) {
    var sv = svgOver(img);
    sv.innerHTML =
      '<defs><radialGradient id="lvSun"><stop offset="0" stop-color="#FBE3A2" stop-opacity=".95"/><stop offset=".45" stop-color="#DDB866" stop-opacity=".45"/><stop offset="1" stop-color="#DDB866" stop-opacity="0"/></radialGradient></defs>' +
      '<path id="lvArc" d="M116,407 C150,370 175,350 240,300 S360,226 398,230 S462,240 480,250" fill="none" stroke="none"/>' +
      '<circle class="lv-halo" cx="480" cy="250" r="34" fill="url(#lvSun)"/>' +
      '<circle class="lv-ring" cx="480" cy="250" r="16" fill="none" stroke="#E9C47A" stroke-width="2"/>' +
      '<g class="lv-spark"><circle r="14" fill="url(#lvSun)"/><circle r="3.4" fill="#FFF3CC"/>' +
      (RM ? '' : '<animateMotion dur="4.2s" repeatCount="indefinite" keyPoints="0;1" keyTimes="0;1" calcMode="linear"><mpath href="#lvArc"/></animateMotion>') + '</g>';
  }

  var MAP = { globe: globe, chart: chart, eight: eight, tree: tree, nefes: nefes };
  document.querySelectorAll('[data-live]').forEach(function (ph) {
    var fn = MAP[ph.getAttribute('data-live')], img = ph.querySelector('.iph-scr img');
    if (fn && img) { img.loading = 'eager'; ready(img, function () { try { fn(ph, img); } catch (e) { } }); }
  });
})();
