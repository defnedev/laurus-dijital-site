// Laurus 3D showcase: real-looking phones and laptops, floating in a gold-dust studio,
// screens cycling through real client work.
import * as THREE from './three-0170.min.js';
import { RoundedBoxGeometry } from './rbox-0170.js';
import { RoomEnvironment } from './roomenv-0170.js';

const host = document.querySelector('.h3d');
const hero = host && host.closest('.hero3');
if (host && hero) start();

function start() {
  const RM = matchMedia('(prefers-reduced-motion: reduce)').matches;
  const mobile = innerWidth < 760;
  let renderer;
  try { renderer = new THREE.WebGLRenderer({ antialias: true, alpha: true, powerPreference: 'high-performance' }); }
  catch (e) { return; }
  renderer.setPixelRatio(Math.min(devicePixelRatio || 1, mobile ? 1.6 : 1.8));
  renderer.outputColorSpace = THREE.SRGBColorSpace;
  renderer.toneMapping = THREE.ACESFilmicToneMapping;
  renderer.toneMappingExposure = 1.05;
  host.appendChild(renderer.domElement);

  const scene = new THREE.Scene();
  scene.fog = new THREE.Fog(0x0b120e, 20, 42);
  const pmrem = new THREE.PMREMGenerator(renderer);
  scene.environment = pmrem.fromScene(new RoomEnvironment(), 0.04).texture;
  const camera = new THREE.PerspectiveCamera(32, 1, 0.1, 100);
  const target = new THREE.Vector3();

  const key = new THREE.DirectionalLight(0xffe0a6, 2.2); key.position.set(7, 9, 8); scene.add(key);
  const rim = new THREE.DirectionalLight(0x9bc59d, 1.4); rim.position.set(-9, 3, -7); scene.add(rim);
  const fill = new THREE.DirectionalLight(0xffffff, 0.5); fill.position.set(-4, -2, 9); scene.add(fill);
  scene.add(new THREE.AmbientLight(0x22302a, 0.6));

  // ---------- helpers ----------
  const C = (w, h, draw) => { const c = document.createElement('canvas'); c.width = w; c.height = h; draw(c.getContext('2d'), w, h); return new THREE.CanvasTexture(c); };
  const rr = (g, x, y, w, h, r) => { g.beginPath(); g.roundRect(x, y, w, h, r); g.fill(); };
  const mask = (w, h, r) => C(w, h, (g) => { g.fillStyle = '#000'; g.fillRect(0, 0, w, h); g.fillStyle = '#fff'; rr(g, 1, 1, w - 2, h - 2, r); });
  const logoTex = C(256, 256, (g) => {
    g.save(); g.scale(6.4, 6.4);
    g.fillStyle = '#D9B24C'; rr(g, 0, 0, 40, 40, 11);
    g.fillStyle = '#0D1611'; g.fill(new Path2D('M11 8h5.6v18.4H29V32H11z')); g.fill(new Path2D('M20.5 21.5c.2-6.4 3.6-11 9.5-13 .4 6.3-3.1 11.2-9.5 13z'));
    g.fillStyle = '#D9B24C'; g.fill(new Path2D('M21.6 20.4c1.6-3.4 3.8-6.2 6.9-8.6-.2.4-3.6 4.8-6.9 8.6z')); g.restore();
  });
  logoTex.colorSpace = THREE.SRGBColorSpace;
  const keysTex = C(1024, 400, (g, w, h) => {
    g.fillStyle = '#16191a'; g.fillRect(0, 0, w, h);
    const rows = 6, kh = h / rows;
    for (let r = 0; r < rows; r++) { const n = r === 0 ? 14 : 13, kw = w / n;
      for (let k = 0; k < n; k++) { g.fillStyle = '#0b0d0e'; rr(g, k * kw + 4, r * kh + 4, kw - 8, kh - 8, 8); } }
  });
  const loader = new THREE.TextureLoader(); const cache = {};
  function fitCover(t) {
    const a = t.image.width / t.image.height, ta = t.userData.aspect || a;
    t.repeat.set(1, 1); t.offset.set(0, 0);
    if (a > ta) { t.repeat.x = ta / a; t.offset.x = (1 - t.repeat.x) / 2; }
    else { t.repeat.y = a / ta; t.offset.y = 1 - t.repeat.y; }
    t.needsUpdate = true;
  }
  function screenTex(src, aspect) {
    const k = src + '|' + aspect; if (cache[k]) return cache[k];
    const t = loader.load(src, (t) => fitCover(t)); t.userData.aspect = aspect;
    t.colorSpace = THREE.SRGBColorSpace; t.anisotropy = 8; cache[k] = t; return t;
  }

  const finishes = {
    graphite: { color: 0x2b2f2e, metalness: 0.9, roughness: 0.3 },
    titanium: { color: 0xa7a196, metalness: 0.95, roughness: 0.34 },
    gold: { color: 0xc9a65a, metalness: 1, roughness: 0.28 },
    green: { color: 0x2c4536, metalness: 0.85, roughness: 0.32 },
    silver: { color: 0xc3c6c8, metalness: 0.95, roughness: 0.36 },
    space: { color: 0x55595c, metalness: 0.92, roughness: 0.38 },
  };
  const metal = (f) => new THREE.MeshPhysicalMaterial({ ...finishes[f], clearcoat: 0.5, clearcoatRoughness: 0.25, envMapIntensity: 1.2 });
  const glassBlack = new THREE.MeshPhysicalMaterial({ color: 0x030405, metalness: 0, roughness: 0.06, clearcoat: 1, clearcoatRoughness: 0.03, envMapIntensity: 1.4 });
  const lensMat = new THREE.MeshPhysicalMaterial({ color: 0x07090c, metalness: 0.2, roughness: 0.05, clearcoat: 1, envMapIntensity: 2 });
  const ringMat = new THREE.MeshPhysicalMaterial({ color: 0x9aa0a3, metalness: 1, roughness: 0.2 });

  const PW = 1.5, PH = 3.1, PD = 0.17;
  const SPW = 1.36, SPH = 2.96;
  const mP = mask(272, 592, 34), mIsland = mask(128, 36, 18), mL = mask(640, 400, 10), mBez = mask(460, 300, 14);
  const screens = [];

  function screenPair(w, h, m, list, aspect, z, group, y = 0) {
    const geo = new THREE.PlaneGeometry(w, h);
    const a = new THREE.MeshBasicMaterial({ map: screenTex(list[0], aspect), alphaMap: m, transparent: true, toneMapped: false });
    const b = new THREE.MeshBasicMaterial({ map: screenTex(list[1 % list.length], aspect), alphaMap: m, transparent: true, opacity: 0, toneMapped: false, depthWrite: false });
    const ma = new THREE.Mesh(geo, a), mb = new THREE.Mesh(geo, b);
    ma.position.set(0, y, z); mb.position.set(0, y, z + 0.0008);
    group.add(ma); group.add(mb);
    screens.push({ a, b, list, aspect, i: 0, fade: -1, next: 4 + Math.random() * 5 });
    return ma;
  }

  function makePhone(finish, list) {
    const g = new THREE.Group(); const body = metal(finish);
    g.add(new THREE.Mesh(new RoundedBoxGeometry(PW, PH, PD, 6, 0.22), body));
    const glass = new THREE.Mesh(new THREE.PlaneGeometry(PW - 0.035, PH - 0.035), glassBlack.clone());
    glass.material.alphaMap = mask(300, 620, 44); glass.material.transparent = true; glass.position.z = PD / 2 + 0.001; g.add(glass);
    const scr = screenPair(SPW, SPH, mP, list, SPW / SPH, PD / 2 + 0.002, g);
    const isl = new THREE.Mesh(new THREE.PlaneGeometry(0.42, 0.12), new THREE.MeshBasicMaterial({ color: 0x000000, alphaMap: mIsland, transparent: true }));
    isl.position.set(0, SPH / 2 - 0.14, PD / 2 + 0.0035); g.add(isl);
    [[PW / 2 + 0.008, 0.75, 0.42], [-PW / 2 - 0.008, 0.95, 0.22], [-PW / 2 - 0.008, 0.55, 0.32], [-PW / 2 - 0.008, 0.15, 0.32]].forEach(([x, y, h]) => {
      const bt = new THREE.Mesh(new RoundedBoxGeometry(0.03, h, 0.07, 2, 0.012), body); bt.position.set(x, y, 0); g.add(bt);
    });
    const bump = new THREE.Mesh(new RoundedBoxGeometry(0.66, 0.66, 0.05, 4, 0.13), body);
    bump.position.set(-0.34, 1.07, -PD / 2 - 0.018); g.add(bump);
    [[-0.5, 1.23], [-0.5, 0.91], [-0.2, 1.07]].forEach(([x, y]) => {
      const ring = new THREE.Mesh(new THREE.CylinderGeometry(0.12, 0.12, 0.05, 32), ringMat); ring.rotation.x = Math.PI / 2; ring.position.set(x, y, -PD / 2 - 0.05); g.add(ring);
      const lens = new THREE.Mesh(new THREE.CylinderGeometry(0.095, 0.095, 0.052, 32), lensMat); lens.rotation.x = Math.PI / 2; lens.position.set(x, y, -PD / 2 - 0.052); g.add(lens);
    });
    const logo = new THREE.Mesh(new THREE.PlaneGeometry(0.42, 0.42), new THREE.MeshStandardMaterial({ map: logoTex, transparent: true, alphaMap: mask(128, 128, 36), metalness: 0.6, roughness: 0.3 }));
    logo.rotation.y = Math.PI; logo.position.set(0, 0, -PD / 2 - 0.001); g.add(logo);
    g.userData.screen = scr; return g;
  }

  function makeLaptop(finish, list) {
    const g = new THREE.Group(); const body = metal(finish);
    const W = 4.7, D = 3.2, T = 0.13;
    g.add(new THREE.Mesh(new RoundedBoxGeometry(W, T, D, 4, 0.06), body));
    const keys = new THREE.Mesh(new THREE.PlaneGeometry(3.9, 1.5), new THREE.MeshStandardMaterial({ map: keysTex, roughness: 0.7, metalness: 0.1 }));
    keys.rotation.x = -Math.PI / 2; keys.position.set(0, T / 2 + 0.002, -0.55); g.add(keys);
    const pad = new THREE.Mesh(new THREE.PlaneGeometry(1.7, 1.05), new THREE.MeshPhysicalMaterial({ ...finishes[finish], roughness: 0.22, clearcoat: 0.8, alphaMap: mask(170, 105, 14), transparent: true }));
    pad.rotation.x = -Math.PI / 2; pad.position.set(0, T / 2 + 0.002, 0.88); g.add(pad);
    const hinge = new THREE.Group(); hinge.position.set(0, T / 2, -D / 2 + 0.04); g.add(hinge);
    const LH = 3.05, LD = 0.075;
    const lid = new THREE.Mesh(new RoundedBoxGeometry(W, LH, LD, 4, 0.05), body); lid.position.set(0, LH / 2, 0); hinge.add(lid);
    const bez = new THREE.Mesh(new THREE.PlaneGeometry(W - 0.08, LH - 0.08), glassBlack.clone()); bez.material.alphaMap = mBez; bez.material.transparent = true;
    bez.position.set(0, LH / 2, LD / 2 + 0.001); hinge.add(bez);
    const sw = 4.42, sh = sw / 1.6;
    const scr = screenPair(sw, sh, mL, list, 1.6, LD / 2 + 0.002, hinge, LH / 2 - 0.02);
    const logo = new THREE.Mesh(new THREE.PlaneGeometry(0.62, 0.62), new THREE.MeshStandardMaterial({ map: logoTex, transparent: true, alphaMap: mask(128, 128, 36), metalness: 0.7, roughness: 0.25 }));
    logo.rotation.y = Math.PI; logo.position.set(0, LH / 2, -LD / 2 - 0.001); hinge.add(logo);
    hinge.rotation.x = -0.26;
    g.userData.screen = scr; return g;
  }

  // ---------- staging ----------
  const P = (s) => '/img/' + s + '.webp';
  const phoneShots = ['app/lp-m', 'app/os-world', 'app/sb-home', 'app/nf-main', 'app/cn-home', 'real/nil-ig', 'app/sk-sekiz', 'app/seven-m', 'app/feronya-m'].map(P);
  const deskShots = ['real/nil-site', 'app/seven-d', 'app/feronya-d', 'app/sorbi-d', 'app/ohsame-d', 'app/lp-d', 'real/nil-galeri'].map(P);
  const rot = (arr, k) => arr.slice(k).concat(arr.slice(0, k));
  const plan = [
    { t: 'L', f: 'silver', l: rot(deskShots, 0), p: [0.3, -1.55, 0], r: [0.05, -0.38, 0], s: 1.18 },
    { t: 'L', f: 'space', l: rot(deskShots, 3), p: [5.2, 0.9, -3.6], r: [0.12, -0.78, 0.02], s: 0.95, m: false },
    { t: 'P', f: 'gold', l: rot(phoneShots, 0), p: [-2.75, -0.55, 2.2], r: [0, 0.42, 0.05], s: 1 },
    { t: 'P', f: 'graphite', l: rot(phoneShots, 1), p: [3.35, -1.05, 2.5], r: [0, -0.48, -0.05], s: 1 },
    { t: 'P', f: 'titanium', l: rot(phoneShots, 2), p: [-1.5, 2.35, -1.4], r: [0.1, 0.3, 0.06], s: 0.92, m: false },
    { t: 'P', f: 'green', l: rot(phoneShots, 3), p: [2.1, 2.55, 0.8], r: [0.05, -0.25, -0.1], s: 0.95 },
    { t: 'P', f: 'graphite', l: rot(phoneShots, 4), p: [6.6, -1.3, 0.6], r: [0, -0.72, 0.04], s: 0.95, m: false },
  ];
  const stage = new THREE.Group(); scene.add(stage);
  const devs = [];
  plan.forEach((d, i) => {
    if (mobile && d.m === false) return;
    const g = d.t === 'L' ? makeLaptop(d.f, d.l) : makePhone(d.f, d.l);
    const holder = new THREE.Group(); holder.add(g); stage.add(holder);
    holder.position.set(...d.p); g.rotation.set(...d.r); holder.scale.setScalar(0.001);
    holder.userData = { base: new THREE.Vector3(...d.p), rot: new THREE.Euler(...d.r), s: d.s, ph: i * 1.7, t0: 0.15 + i * 0.12, g, hov: 0, spinAt: d.t === 'P' ? 6 + i * 4.3 : 1e9 };
    devs.push(holder);
  });

  // gold dust
  const PC = mobile ? 700 : 1600;
  const pos = new Float32Array(PC * 3), spd = new Float32Array(PC);
  for (let i = 0; i < PC; i++) { pos[i * 3] = (Math.random() - 0.5) * 40; pos[i * 3 + 1] = (Math.random() - 0.5) * 20; pos[i * 3 + 2] = (Math.random() - 0.5) * 30 - 4; spd[i] = 0.06 + Math.random() * 0.2; }
  const pg = new THREE.BufferGeometry(); pg.setAttribute('position', new THREE.BufferAttribute(pos, 3));
  const dot = C(64, 64, (g) => { const gr = g.createRadialGradient(32, 32, 0, 32, 32, 32); gr.addColorStop(0, 'rgba(255,236,170,1)'); gr.addColorStop(.35, 'rgba(217,178,76,.5)'); gr.addColorStop(1, 'rgba(217,178,76,0)'); g.fillStyle = gr; g.fillRect(0, 0, 64, 64); });
  const pm = new THREE.PointsMaterial({ size: mobile ? 0.12 : 0.1, map: dot, transparent: true, opacity: 0, depthWrite: false, blending: THREE.AdditiveBlending, toneMapped: false });
  scene.add(new THREE.Points(pg, pm));

  // ---------- layout ----------
  let W = 1, H = 1, ox = 0, oy = 0, sc = 1;
  function size() {
    const r = host.getBoundingClientRect(); W = r.width || innerWidth; H = r.height || innerHeight;
    renderer.setSize(W, H, false); camera.aspect = W / H; camera.updateProjectionMatrix();
    if (W >= 1000) { ox = 4.6; oy = 0.25; sc = 0.82; } else if (W >= 760) { ox = 3.8; oy = 0; sc = 0.7; } else { ox = 0.2; oy = 4.6; sc = 0.6; }
    stage.position.set(ox, oy, 0); stage.scale.setScalar(sc);
  }
  size(); addEventListener('resize', size);

  // ---------- input ----------
  let mx = 0, my = 0, cx = 0, cy = 0, px = -9, py = -9;
  addEventListener('pointermove', (e) => { mx = e.clientX / innerWidth * 2 - 1; my = e.clientY / innerHeight * 2 - 1;
    const r = host.getBoundingClientRect(); px = (e.clientX - r.left) / r.width * 2 - 1; py = -((e.clientY - r.top) / r.height) * 2 + 1; }, { passive: true });
  const ray = new THREE.Raycaster(), v2 = new THREE.Vector2(); let hovered = null;
  const scrMeshes = devs.map((h) => h.userData.g.userData.screen);
  hero.addEventListener('click', (e) => {
    if (!hovered || e.target.closest('a,button')) return;
    const a = document.createElement('a'); a.href = '/calismalar'; a.setAttribute('data-pt', 'Çalışmalar'); a.style.display = 'none'; document.body.appendChild(a); a.click();
  });

  let visible = true;
  new IntersectionObserver((es) => { visible = es[0].isIntersecting; if (visible) loop(); }).observe(hero);
  document.addEventListener('visibilitychange', () => { if (!document.hidden) loop(); });

  const clock = new THREE.Clock(); let T = 0, running = false;
  hero.classList.add('h3d-on');
  const ease = (t) => 1 - Math.pow(1 - Math.min(1, Math.max(0, t)), 3);
  const eio = (t) => { t = Math.min(1, Math.max(0, t)); return t < .5 ? 4 * t * t * t : 1 - Math.pow(-2 * t + 2, 3) / 2; };

  function frame() {
    const dt = Math.min(clock.getDelta(), 0.05); T += dt;
    const sp = Math.min(1, Math.max(0, scrollY / (hero.offsetHeight || 1)));
    devs.forEach((h) => {
      const u = h.userData, k = ease((T - u.t0) / 1.8);
      const fl = RM ? 0 : Math.sin(T * 0.55 + u.ph) * 0.14;
      h.position.set(u.base.x, u.base.y + fl - (1 - k) * 3.5, u.base.z + (1 - k) * 2);
      u.hov += ((hovered === h ? 1 : 0) - u.hov) * 0.1;
      h.scale.setScalar(Math.max(0.001, u.s * (0.7 + 0.3 * k) * (1 + u.hov * 0.06)));
      let spin = 0;
      if (!RM && T > u.spinAt) { const q = (T - u.spinAt) / 2.6; if (q >= 1) u.spinAt += 26 + u.ph * 2; else spin = eio(q) * Math.PI * 2; }
      u.g.rotation.set(u.rot.x + (RM ? 0 : Math.sin(T * 0.4 + u.ph) * 0.05), u.rot.y * (1 - u.hov * 0.8) + (RM ? 0 : Math.sin(T * 0.3 + u.ph) * 0.16) + spin, u.rot.z);
    });
    screens.forEach((s) => {
      if (RM) return;
      if (s.fade < 0 && T > s.next) s.fade = 0;
      if (s.fade >= 0) {
        s.fade += dt / 0.9; s.b.opacity = Math.min(1, s.fade);
        if (s.fade >= 1) { s.i = (s.i + 1) % s.list.length; s.a.map = screenTex(s.list[s.i], s.aspect); s.b.opacity = 0;
          s.b.map = screenTex(s.list[(s.i + 1) % s.list.length], s.aspect); s.fade = -1; s.next = T + 5 + Math.random() * 3; }
      }
    });
    const kk = ease(T / 2.4); pm.opacity = 0.8 * kk;
    if (!RM) { const p = pg.attributes.position.array; for (let i = 0; i < PC; i++) { p[i * 3 + 1] += spd[i] * dt; if (p[i * 3 + 1] > 10) p[i * 3 + 1] = -10; } pg.attributes.position.needsUpdate = true; }
    cx += (mx - cx) * 0.045; cy += (my - cy) * 0.045;
    stage.rotation.set(cy * 0.06 + sp * 0.12, cx * 0.16 - sp * 0.35, 0);
    camera.position.set(cx * 0.9, 1.1 - cy * 0.5 + sp * 1.2, (mobile ? 19 : 17.5) - sp * 5 + (1 - kk) * 3);
    target.set(ox * 0.32 + cx * 0.2, oy * 0.2 + sp * 0.5, 0); camera.lookAt(target);
    hovered = null;
    if (!mobile && px > -2) {
      v2.set(px, py); ray.setFromCamera(v2, camera);
      const hit = ray.intersectObjects(scrMeshes, false)[0];
      if (hit) { let o = hit.object; while (o && !devs.includes(o)) o = o.parent; hovered = o || null; }
    }
    hero.classList.toggle('h3d-hov', !!hovered);
    host.style.opacity = String(1 - sp * 0.7);
    renderer.render(scene, camera);
  }
  function loop() {
    if (running) return; running = true; clock.getDelta();
    (function tick() {
      if (!visible || document.hidden) { running = false; return; }
      frame();
      if (RM && T > 2.6) { running = false; return; }
      requestAnimationFrame(tick);
    })();
  }
  loop();
}
