import json, os, sys, urllib.request as U

E = os.environ["MAKEFUN_ENV_URL"]
def P(p, b={}):
 return json.load(U.urlopen(U.Request(E + p, data=json.dumps(b).encode(), headers={"content-type": "application/json"})))

V = {'P':100,'N':320,'B':330,'R':500,'Q':900,'K':0}
KN = (33,31,18,14,-33,-31,-18,-14)
KG = (1,-1,16,-16,17,-17,15,-15)
RD = (1,-1,16,-16); BD = (17,-17,15,-15)
def T(s): return [(ord(c)-100) for c in s]
PI = [
(0,0,0,0,0,0,0,0,1,2,2,-4,-4,2,2,1,1,-1,-2,0,0,-2,-1,1,0,0,0,4,4,0,0,0,1,1,2,5,5,2,1,1,2,2,4,6,6,4,2,2,10,10,10,10,10,10,10,10,0,0,0,0,0,0,0,0),
(-10,-8,-6,-6,-6,-6,-8,-10,-8,-4,0,1,1,0,-4,-8,-6,1,2,3,3,2,1,-6,-6,0,3,4,4,3,0,-6,-6,1,3,4,4,3,1,-6,-6,0,2,3,3,2,0,-6,-8,-4,0,0,0,0,-4,-8,-10,-8,-6,-6,-6,-6,-8,-10),
(-4,-2,-2,-2,-2,-2,-2,-4,-2,1,0,0,0,0,1,-2,-2,2,2,2,2,2,2,-2,-2,0,2,2,2,2,0,-2,-2,1,1,2,2,1,1,-2,-2,0,1,2,2,1,0,-2,-2,0,0,0,0,0,0,-2,-4,-2,-2,-2,-2,-2,-2,-4),
(0,0,0,1,1,0,0,0,-1,0,0,0,0,0,0,-1,-1,0,0,0,0,0,0,-1,-1,0,0,0,0,0,0,-1,-1,0,0,0,0,0,0,-1,-1,0,0,0,0,0,0,-1,1,2,2,2,2,2,2,1,0,0,0,0,0,0,0,0),
(-4,-2,-2,-1,-1,-2,-2,-4,-2,0,1,0,0,0,0,-2,-2,1,1,1,1,1,0,-2,0,0,1,1,1,1,0,-1,-1,0,1,1,1,1,0,-1,-2,0,1,1,1,1,0,-2,-2,0,0,0,0,0,0,-2,-4,-2,-2,-1,-1,-2,-2,-4),
(4,6,2,0,0,2,6,4,4,4,0,0,0,0,4,4,-2,-4,-4,-4,-4,-4,-4,-2,-4,-6,-6,-8,-8,-6,-6,-4,-6,-8,-8,-10,-10,-8,-8,-6,-6,-8,-8,-10,-10,-8,-8,-6,-6,-8,-8,-10,-10,-8,-8,-6,-6,-8,-8,-10,-10,-8,-8,-6)
]
CH = "PNBRQK"
PA = (0, 0, 4, 8, 14, 24, 40, 0)
PC = (0, 0, 0, 10, 15, 10, 5, 0)
PB = (0, 5, 10, 20, 35, 60, 100)
def IX(q): return (q>>4)*8+(q&15)
def MI(i): return (7-i//8)*8+i%8

class C:
 def __init__(s, f):
  t = f.split(); s.b = [' ']*128; i = 112
  for c in t[0]:
   if c == '/': i = (i&112)-16
   elif c.isdigit(): i += int(c)
   else: s.b[i] = c; i += 1
  s.w = t[1] == 'w'; s.c = '' if t[2] == '-' else t[2]
  e = t[3]; s.e = -1 if e == '-' else (int(e[1])-1)*16+ord(e[0])-97

def AT(b, q, W):
 p = 'P' if W else 'p'
 for d in ((-15,-17) if W else (15,17)):
  s = q+d
  if not s&0x88 and b[s] == p: return 1
 p = 'N' if W else 'n'
 for d in KN:
  s = q+d
  if not s&0x88 and b[s] == p: return 1
 p = 'K' if W else 'k'
 for d in KG:
  s = q+d
  if not s&0x88 and b[s] == p: return 1
 for ds, pc in ((RD,'RQ' if W else 'rq'), (BD,'BQ' if W else 'bq')):
  for d in ds:
   s = q+d
   while not s&0x88:
    r = b[s]
    if r != ' ':
     if r in pc: return 1
     break
    s += d

def KS(b, W): return b.index('K' if W else 'k')

def GN(p, O=0):
 b, W, c, e = p.b, p.w, p.c, p.e; M = []
 for q in range(128):
  if q&0x88: continue
  s = b[q]
  if s == ' ' or s.isupper() != W: continue
  x = s.upper(); f = q&15
  if x == 'P':
   d = 16 if W else -16; t = q+d; pr = (q>>4) == (6 if W else 1)
   if not t&0x88 and b[t] == ' ':
    if pr:
     for z in 'qrbn': M.append((q,t,z))
    elif not O:
     M.append((q,t,''))
     if (q>>4) == (1 if W else 6) and b[t+d] == ' ': M.append((q,t+d,''))
   for v in (-1,1):
    if 0 <= f+v < 8:
     t = q+d+v
     if not t&0x88:
      y = b[t]
      if y != ' ' and y.isupper() != W:
       if pr:
        for z in 'qrbn': M.append((q,t,z))
       else: M.append((q,t,''))
      elif t == e and e >= 0: M.append((q,t,''))
  elif x in 'NK':
   for d in (KN if x == 'N' else KG):
    t = q+d
    if not t&0x88:
     y = b[t]
     if y == ' ':
      if not O: M.append((q,t,''))
     elif y.isupper() != W: M.append((q,t,''))
   if x == 'K' and not O:
    if ('K' if W else 'k') in c and b[q+1] == ' ' and b[q+2] == ' ' and not AT(b,q,not W) and not AT(b,q+1,not W) and not AT(b,q+2,not W): M.append((q,q+2,'c'))
    if ('Q' if W else 'q') in c and b[q-1] == ' ' and b[q-2] == ' ' and b[q-3] == ' ' and not AT(b,q,not W) and not AT(b,q-1,not W) and not AT(b,q-2,not W): M.append((q,q-2,'c'))
  else:
   for d in (RD if x == 'R' else BD if x == 'B' else KG):
    t = q+d
    while not t&0x88:
     y = b[t]
     if y == ' ':
      if not O: M.append((q,t,''))
     else:
      if y.isupper() != W: M.append((q,t,''))
      break
     t += d
 return M

def MV(p, m):
 a, t, z = m; b = p.b; s = b[a]; y = b[t]; r = (a,t,z,s,y,p.c,p.e); e = p.e
 b[a] = ' '
 if z == 'c':
  k = 'R' if p.w else 'r'
  if t > a: b[a+1] = k; b[a+3] = ' '
  else: b[a-1] = k; b[a-4] = ' '
  b[t] = s
 elif z: b[t] = z.upper() if p.w else z
 else:
  b[t] = s
  if s in 'Pp' and t == e and e >= 0 and y == ' ': b[t-16 if p.w else t+16] = ' '
 if s in 'Kk': p.c = (p.c.replace('K','').replace('Q','') if p.w else p.c.replace('k','').replace('q',''))
 if a == 0 or t == 0: p.c = p.c.replace('Q','')
 if a == 7 or t == 7: p.c = p.c.replace('K','')
 if a == 112 or t == 112: p.c = p.c.replace('q','')
 if a == 119 or t == 119: p.c = p.c.replace('k','')
 p.e = -1
 if s in 'Pp' and abs(t-a) == 32: p.e = (a+t)//2
 p.w = not p.w
 return r

def UM(p, r):
 a, t, z, s, y, c, e = r; b = p.b; p.w = not p.w; W = p.w
 if z == 'c':
  k = 'R' if W else 'r'; b[a] = s; b[t] = ' '
  if t > a: b[a+3] = k; b[a+1] = ' '
  else: b[a-4] = k; b[a-1] = ' '
 else:
  b[a] = s; b[t] = y
  if s in 'Pp' and t == e and y == ' ' and (t&15) != (a&15): b[t-16 if W else t+16] = 'p' if W else 'P'
 p.c = c; p.e = e

def LG(p):
 R = []
 for m in GN(p):
  r = MV(p,m)
  if not AT(p.b, KS(p.b, not p.w), p.w): R.append(m)
  UM(p, r)
 return R

def IC(p): return AT(p.b, KS(p.b, p.w), not p.w)

def EV(p):
 b = p.b; s = 0; wb = bb = 0; np = 0
 kw = kb = 0
 for q in range(128):
  r = b[q]
  if r == ' ': continue
  if q&0x88: continue
  rk = q>>4; f = q&15
  if r == 'P':
   s += 100+PA[rk]+(PC[rk] if f == 3 or f == 4 else 0)
  elif r == 'p':
   s -= 100+PA[7-rk]+(PC[7-rk] if f == 3 or f == 4 else 0)
  elif r == 'N':
   c = min(f, 7-f)+min(rk, 7-rk); s += 320+6*c-20; np += 320
  elif r == 'n':
   c = min(f, 7-f)+min(7-rk, rk); s -= 320+6*c-20; np += 320
  elif r == 'B':
   c = min(f, 7-f)+min(rk, 7-rk); s += 330+4*c-8; np += 330; wb += 1
  elif r == 'b':
   c = min(f, 7-f)+min(7-rk, rk); s -= 330+4*c-8; np += 330; bb += 1
  elif r == 'R':
   s += 500+(15 if rk == 6 else 0)+(5 if rk == 0 and (f == 3 or f == 4) else 0)
   np += 500
   t = f
   while t < 128:
    if b[t] in 'Pp': break
    t += 16
   else: s += 12
  elif r == 'r':
   s -= 500+(15 if 7-rk == 6 else 0)+(5 if 7-rk == 0 and (f == 3 or f == 4) else 0)
   np += 500
   t = f
   while t < 128:
    if b[t] in 'Pp': break
    t += 16
   else: s -= 12
  elif r == 'Q':
   c = min(f, 7-f)+min(rk, 7-rk); s += 900+2*c-6; np += 900
  elif r == 'q':
   c = min(f, 7-f)+min(7-rk, rk); s -= 900+2*c-6; np += 900
  elif r == 'K': kw = rk
  else: kb = 7-rk
 ph = np if np < 6400 else 6400
 for rk, sg in ((kw, 1), (kb, -1)):
  kk = [20, 25, 10, 0, 0, 10, 25, 20][rk] if rk == 0 else max(-50, -15*rk)
  ee = 8*(min(rk, 7-rk)*2)-24
  s += sg*((kk*ph+ee*(6400-ph))//6400)
 if wb >= 2: s += 30
 if bb >= 2: s -= 30
 return s if p.w else -s

N = 0; KILN = 0; KIL = {}; HIS = {}; TT = {}; PH = []; TTM = None; GAMEH = set()
def HV(p, m):
 if m == TTM: return 10000000
 a, t, z = m; y = p.b[t]
 if y != ' ': return 1000000+10*V[y.upper()]-V[p.b[a].upper()]
 if z and z != 'c': return 1000000+V[z.upper()]
 if m in KIL.get(PL,()): return 900000
 return HIS.get(m, 0)

def QS(p, A, B, q=0):
 global N
 N += 1; k = IC(p); L = 0
 M = GN(p) if k and q < 4 else GN(p, 1)
 if not k:
  s = EV(p)
  if s >= B: return B
  if s > A: A = s
 for m in sorted(M, key=lambda m: HV(p, m), reverse=1):
  r = MV(p, m)
  if AT(p.b, KS(p.b, not p.w), p.w): UM(p, r); continue
  L = 1
  v = -QS(p, -B, -A, q+1); UM(p, r)
  if v >= B: return B
  if v > A: A = v
 if k and not L: return -100000+q
 return A

class TO(Exception): pass
PL = 0
BUD = 40000
def NX(p, d, A, B, pv, pl=0):
 global N, PL, TTM
 if N >= BUD: raise TO()
 N += 1
 key = (tuple(p.b), p.w, p.c, p.e)
 if pl > 0 and key in GAMEH:
  N += 1
  return 0
 PH.append(key)
 TTM = None
 tte = TT.get(key)
 if tte:
  TTM = tte[3]
  if tte[0] >= d and pl > 0:
   v = tte[1]
   if v > 90000: v -= pl
   elif v < -90000: v += pl
   if v > 100200: v = 100200
   elif v < -100200: v = -100200
   if tte[2] == 0 or (tte[2] == 1 and v <= A) or (tte[2] == 2 and v >= B):
    PH.pop(); return v
 k = IC(p)
 if k and pl < 24: d += 1
 if d <= 0:
  PH.pop(); TTM = None
  return QS(p, A, B)
 if not k and d >= 3 and pl > 0 and abs(A) < 90000:
  e, c = p.e, p.c; p.e = -1; p.w = not p.w
  v = -NX(p, d-3, -B, -B+1, pv, pl+1)
  p.w = not p.w; p.e, p.c = e, c
  if v >= B:
   PH.pop()
   if -90000 < B < 90000: TT[key] = (d, B, 2, None)
   return B
 M = GN(p); PL = pl; M.sort(key=lambda m: HV(p, m), reverse=1)
 b = -10**9; L = 0; bm = None; fl = 0; a0 = A
 i = 0
 for m in M:
  r = MV(p, m)
  if AT(p.b, KS(p.b, not p.w), p.w): UM(p, r); continue
  L = 1
  quiet = r[4] == ' ' and not m[2]
  if i == 0:
   v = -NX(p, d-1, -B, -A, pv, pl+1)
  else:
   red = d >= 3 and i >= 4 and quiet and not k and abs(A) < 90000
   v = -NX(p, d-1-(1 if red else 0), -A-1, -A, [], pl+1)
   if A < v < B: v = -NX(p, d-1, -B, -A, [], pl+1)
  UM(p, r)
  i += 1
  if v > b:
   b = v; bm = m
   if v > A:
    A = v
    if pl == 0: pv[:] = [m]
  if A >= B:
   if HV(p, m) < 900000:
    kl = KIL.setdefault(pl, [])
    if m not in kl: kl.insert(0, m); del kl[2:]
    HIS[m] = HIS.get(m, 0)+d*d
   fl = 2
   break
 PH.pop(); TTM = None
 if not L: return -100000+pl if k else 0
 if b >= 90000: st = b+pl
 elif b <= -90000: st = b-pl
 else: st = b
 if b <= a0: fl = 1
 elif b >= B: fl = 2
 TT[key] = (d, st, fl, bm)
 if len(TT) > 500000: TT.clear()
 return b

def SR(p, budget, hkeys=()):
 global N, KIL, HIS, PH, TTM, BUD
 N = 0; KIL = {}; HIS = {}; PH = []; BUD = budget; bm = None; GAMEH.clear()
 for k in hkeys: GAMEH.add(k)
 prev = None
 for d in range(1, int(os.environ.get("ENGINE_MAXDEPTH", "32"))):
  N = 0; pv = []
  try:
   if prev is None or abs(prev) > 90000 or d < 3:
    v = NX(p, d, -10**9, 10**9, pv)
   else:
    v = NX(p, d, prev-60, prev+60, pv)
    if v <= prev-60 or v >= prev+60:
     N = 0; pv = []
     v = NX(p, d, -10**9, 10**9, pv)
  except TO:
   PH = []
   break
  if pv: bm = pv[0]
  prev = v
  if N > budget or v > 90000 or v < -90000: break
 return bm

def SN(q): return "abcdefgh"[q&15]+str((q>>4)+1)
def BM(fen, legal, budget, hkeys=()):
 p = C(fen); ms = LG(p); ls = set(legal)
 c = [m for m in ms if SN(m[0])+SN(m[1])+m[2] in ls]
 m = SR(p, budget, hkeys)
 u = SN(m[0])+SN(m[1])+m[2] if m else None
 return u if u in ls else legal[0]

if __name__ == "__main__":
 HIST = []
 while 1:
  g = P("/game", {})
  if g["status"] == "done":
   print(f"done: {g.get('wins')}w {g.get('draws')}d {g.get('losses')}l", file=sys.stderr)
   break
  while g["status"] == "your_move":
   _q = C(g["fen"]); HIST.append((tuple(_q.b), _q.w, _q.c, _q.e))
   _u = BM(g["fen"], g["legal_moves"], int(os.environ.get("ENGINE_NODES", "40000")), HIST)
   g = P("/move", {"game": g["game"], "move": _u})
