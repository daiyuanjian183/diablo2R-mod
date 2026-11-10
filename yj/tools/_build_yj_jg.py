# -*- coding: utf-8 -*-
"""以 jg 为底座构建 yj mod"""
import os, json, re
from datetime import datetime

JG = r"E:\Diablo2rCHN\Diablo II Resurrectedone\mods\jg\jg.mpq"
SHU = r"E:\Diablo2rCHN\Diablo II Resurrectedone\mods\shu\shu.mpq"
DST = r"E:\Diablo2rCHN\Diablo II Resurrectedone\mods\yj\yj.mpq"
BASE_ID = 53101

RUNEWORDS = [
    dict(num=183, en="Dawn", cn="破晓", itype=["weap"], runes=["r07", "r10", "r09"], rused="TalThulOrt",
         props=[("dmg%", "", 60, 80), ("swing2", "", 20, 20), ("att", "", 50, 80)], lvl=23,
         tooltip="ÿc4\n武器\nÿc3+60-80% 强化伤害\n+20% 提高攻击速度\n+50-80 命中值\n\nÿcP优点:低阶符文、攻速+命中兼备\n适用:开荒期近战与远程物理"),
    dict(num=184, en="FrostWhisper", cn="霜语", itype=["armo"], runes=["r10", "r08", "r09", "r07"], rused="ThulRalOrtTal",
         props=[("res-all", "", 15, 25), ("hp", "", 30, 50), ("nofreeze", "", 1, 1)], lvl=23,
         tooltip="ÿc4\n护甲\nÿc3+15-25% 所有抗性\n+30-50 生命\n无法被冻结\n\nÿcP优点:全抗+生命+免冻\n适用:所有职业开荒防具"),
    dict(num=185, en="Hunter", cn="猎手", itype=["miss"], runes=["r05", "r13", "r03"], rused="EthShaelTir",
         props=[("dmg%", "", 40, 60), ("swing2", "", 20, 20), ("dmg-min", "", 5, 5)], lvl=23,
         tooltip="ÿc4\n弓、弩\nÿc3+40-60% 强化伤害\n+20% 提高攻击速度\n+5 最小伤害\n\nÿcP优点:极低造价、攻速成型快\n适用:前期弓系"),
    dict(num=186, en="Bedrock", cn="磐石", itype=["shld"], runes=["r09", "r08", "r07"], rused="OrtRalTal",
         props=[("res-all", "", 20, 30), ("ac", "", 50, 80), ("str", "", 10, 10)], lvl=23,
         tooltip="ÿc4\n盾牌\nÿc3+20-30% 所有抗性\n+50-80 防御\n+10 力量\n\nÿcP优点:三抗+力量，圣骑士与施法者都能用\n适用:开荒过渡盾"),
]

os.makedirs(os.path.dirname(DST), exist_ok=True)

# ---------- 1) runes.txt：以 shu 的 53 列原始表为底 ----------
rp = os.path.join(DST, r"Data\global\excel\runes.txt")
os.makedirs(os.path.dirname(rp), exist_ok=True)
src_rp = os.path.join(SHU, r"Data\global\excel\runes.txt")
raw = open(src_rp, "rb").read().decode("latin-1")
lines = raw.split("\n")
h = [x.rstrip("\r").replace("ï»¿", "") for x in lines[0].split("\t")]
ix = {c: i for i, c in enumerate(h)}
body = [l.rstrip("\r") for l in lines[1:] if l.strip()]

# Eternity → 3.4
for idx, l in enumerate(body):
    f = l.split("\t")
    if len(f) != len(h) or f[ix["*Rune Name"]] != "Eternity":
        continue
    for k in range(1, 8):
        for c in ("T1Code%d" % k, "T1Param%d" % k, "T1Min%d" % k, "T1Max%d" % k):
            f[ix[c]] = ""
    f[ix["itype1"]] = "mele"; f[ix["itype2"]] = "miss"; f[ix["itype3"]] = ""; f[ix["itype4"]] = ""
    for k, (code, par, mn, mx) in enumerate(
            [("dmg%", "", 300, 390), ("indestruct", "", 1, 1), ("slow", "", 33, 33),
             ("oskill", "Revive", 5, 5), ("swing2", "", 30, 30), ("dmg/lvl", "", 24, 24),
             ("nofreeze", "", 1, 1)], start=1):
        f[ix["T1Code%d" % k]] = code; f[ix["T1Param%d" % k]] = par
        f[ix["T1Min%d" % k]] = str(mn); f[ix["T1Max%d" % k]] = str(mx)
    body[idx] = "\t".join(f)
    break

# 新增 4 条
for rw in RUNEWORDS:
    f = [""] * len(h)
    f[ix["Name"]] = "Runeword%d" % rw["num"]
    f[ix["*Rune Name"]] = rw["en"]
    f[ix["complete"]] = "1"
    f[ix["*Patch Release"]] = "110"
    for k, t in enumerate(rw["itype"][:6], start=1):
        f[ix["itype%d" % k]] = t
    f[ix["*RunesUsed"]] = rw["rused"]
    for k, r in enumerate(rw["runes"][:6], start=1):
        f[ix["Rune%d" % k]] = r
    for k, (code, par, mn, mx) in enumerate(rw["props"][:7], start=1):
        f[ix["T1Code%d" % k]] = code; f[ix["T1Param%d" % k]] = par
        f[ix["T1Min%d" % k]] = str(mn); f[ix["T1Max%d" % k]] = str(mx)
    f[ix["*eol"]] = "0"
    body.append("\t".join(f))
open(rp, "wb").write(("\n".join([lines[0]] + body) + "\n").encode("latin-1"))
print("runes.txt: %d 行（含 4 条新符文，永恒已改 3.4）" % len(body))

# ---------- 2) 字符串 ----------
strdir = os.path.join(DST, r"Data\local\lng\strings")
os.makedirs(strdir, exist_ok=True)

# item-runes
ir = json.loads(open(os.path.join(JG, r"Data\local\lng\strings\item-runes.json"), "rb").read().decode("utf-8-sig"))
keys = {e.get("Key") for e in ir if isinstance(e, dict)}
ids = [e.get("id") for e in ir if isinstance(e, dict) and isinstance(e.get("id"), int)]
nid = max(ids) + 1
for rw in RUNEWORDS:
    k = "Runeword%d" % rw["num"]
    if k in keys: continue
    ir.append({"id": nid, "Key": k, "enUS": rw["en"], "zhTW": "ÿc4" + rw["cn"], "zhCN": "ÿc4" + rw["cn"],
               "deDE": "", "esES": "", "frFR": "", "itIT": "", "koKR": "", "plPL": "", "esMX": "",
               "jaJP": "", "ptBR": "", "ruRU": ""})
    nid += 1
open(os.path.join(strdir, "item-runes.json"), "wb").write(json.dumps(ir, ensure_ascii=False, indent=1).encode("utf-8"))
print("item-runes.json: %d 条" % len(ir))

# npcs
np_ = json.loads(open(os.path.join(JG, r"Data\local\lng\strings\npcs.json"), "rb").read().decode("utf-8-sig"))
keys2 = {e.get("Key") for e in np_ if isinstance(e, dict)}
ids2 = [e.get("id") for e in np_ if isinstance(e, dict) and isinstance(e.get("id"), int)]
nid2 = max(ids2) + 1
for i, rw in enumerate(RUNEWORDS):
    list_key = "jghelp%druneword%s" % (BASE_ID + i * 2, rw["en"])
    tip_key = "jghelp%drunewordtooltip%s" % (BASE_ID + i * 2 + 1, rw["en"])
    if list_key not in keys2:
        np_.append({"id": nid2, "Key": list_key, "zhCN": "%d ÿc4%s" % (rw["lvl"], rw["cn"]),
                    "zhTW": "%d ÿc4%s" % (rw["lvl"], rw["cn"]), "enUS": rw["en"],
                    "deDE": "", "esES": "", "frFR": "", "itIT": "", "koKR": "", "plPL": "",
                    "esMX": "", "jaJP": "", "ptBR": "", "ruRU": ""})
        nid2 += 1
    if tip_key not in keys2:
        np_.append({"id": nid2, "Key": tip_key, "zhCN": rw["tooltip"], "zhTW": rw["tooltip"], "enUS": rw["en"],
                    "deDE": "", "esES": "", "frFR": "", "itIT": "", "koKR": "", "plPL": "",
                    "esMX": "", "jaJP": "", "ptBR": "", "ruRU": ""})
        nid2 += 1
open(os.path.join(strdir, "npcs.json"), "wb").write(json.dumps(np_, ensure_ascii=False, indent=1).encode("utf-8"))
print("npcs.json: %d 条" % len(np_))

# ---------- 3) 百科面板：克隆 jg 的 Steel 块 ----------
pp = os.path.join(DST, r"Data\global\ui\layouts\runewordspanelhd.json")
os.makedirs(os.path.dirname(pp), exist_ok=True)
s = open(os.path.join(JG, r"Data\global\ui\layouts\runewordspanelhd.json"), "rb").read().decode("utf-8-sig")

i = s.find('"name": "WeaponRuneWordSteel"')
start = s.rfind("{", 0, i)
depth = 0; j = start; instr = False; esc = False
while j < len(s):
    ch = s[j]
    if instr:
        if esc: esc = False
        elif ch == "\\": esc = True
        elif ch == '"': instr = False
    else:
        if ch == '"': instr = True
        elif ch == "{": depth += 1
        elif ch == "}":
            depth -= 1
            if depth == 0:
                j += 1; break
    j += 1
steel = s[start:j]

RECTS = ["$RuneWordFirstRuneRect", "$RuneWordSecondRuneRect", "$RuneWordThirdRuneRect",
         "$RuneWordForthRuneRect", "$RuneWordFifthRuneRect"]


def rune_btn(rect, rid):
    return ('{"type": "ButtonWidget", "name": "Rune", "fields": {"rect": "%s", "filename": "$FileRune%s",'
            ' "hoveredFrame": 0, "pressedFrame": 0, "tooltipString": "$TooltipRune%s"}}') % (rect, rid, rid)


def make_block(rw, idx, y):
    list_key = "jghelp%druneword%s" % (BASE_ID + idx * 2, rw["en"])
    tip_key = "jghelp%drunewordtooltip%s" % (BASE_ID + idx * 2 + 1, rw["en"])
    runes = ", ".join(rune_btn(RECTS[k], r) for k, r in enumerate(rw["runes"]))
    return ('{ "type": "Widget", "name": "WeaponRuneWord%s", "fields": { "rect": { "x": 10, "y": %d } }, '
            '"children": [ { "type": "Widget", "name": "RuneWord", "fields": { "rect": "$RuneWordNameWidgetRect" }, '
            '"children": [ { "type": "TextBoxWidget", "name": "RuneWordText", "fields": { '
            '"rect": "$RuneWordNameWidgetRect", "text": "@%s", "style": "$RuneWordTextBoxWidgetStyle" }, '
            '"children": [ { "type": "FocusableWidget", "name": "Tooltip", "fields": { "fitToParent": true, '
            '"tooltipString": "@Runeword%d@%s", "tooltipStyle": "$StandardToolTipStyle" } } ] } ] }, '
            '{ "type": "Widget", "name": "RuneWordRunes", "fields": { "rect": "$RuneWordRunesWidgetRect" }, '
            '"children": [ %s ] } ] }') % (rw["en"], y, list_key, rw["num"], tip_key, runes)


ys = [int(x) for x in re.findall(r'"y":\s*(\d+)', s)]
y0 = (max(ys) if ys else 0) + 60
blocks = [make_block(rw, k, y0 + k * 60) for k, rw in enumerate(RUNEWORDS)]

# 在最后一个条目之后插入
last = None
for m in re.finditer(r'"name": "WeaponRuneWord', s):
    last = m
start2 = s.rfind("{", 0, last.start())
depth = 0; j = start2; instr = False; esc = False
while j < len(s):
    ch = s[j]
    if instr:
        if esc: esc = False
        elif ch == "\\": esc = True
        elif ch == '"': instr = False
    else:
        if ch == '"': instr = True
        elif ch == "{": depth += 1
        elif ch == "}":
            depth -= 1
            if depth == 0:
                j += 1; break
    j += 1
s2 = s[:j] + ",\n\n" + ",\n\n".join(blocks) + s[j:]
open(pp, "wb").write(s2.encode("utf-8-sig"))
print("面板: 新增 %d 条（y 从 %d 起）" % (len(blocks), y0))

# ---------- 4) 版本标记 + modinfo ----------
gv = os.path.join(DST, r"Data\global\dataversionbuild.txt")
os.makedirs(os.path.dirname(gv), exist_ok=True)
open(gv, "wb").write(b"95039")
mi = os.path.join(DST, "modinfo.json")
open(mi, "wb").write(json.dumps({"name": "yj", "savepath": "../"}, ensure_ascii=False, indent=2).encode("utf-8"))
print("dataversionbuild=95039，modinfo 写入完成")
print("完成")
