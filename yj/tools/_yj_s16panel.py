# -*- coding: utf-8 -*-
"""在百科「其它」页新增「第16赛季暗金调整」区块"""
import os, json, re

D = r"E:\Diablo2rCHN\Diablo II Resurrectedone\mods\yj\yj.mpq"
NP = os.path.join(D, r"Data\local\lng\strings\npcs.json")
LA = os.path.join(D, r"Data\global\ui\layouts\otherpanelhd.json")

ITEMS = [
    ("海蛇之王", "ED 40-80%、+15% 攻速、+5 最小伤害"),
    ("火精灵", "+3 火系技能、+4 火球、+10% 施法速度"),
    ("坦纳血杖", "ED 200-220%、+5-9% 偷血"),
    ("狰狞夺魂者", "ED 80-120%、偷蓝 5-9%"),
    ("刺穿者", "ED 170-240%、每 4 秒修 1 耐久"),
    ("冷杀", "冰伤 80-100、ED 160-200%"),
    ("震地者", "+3-5 烈火爪击（德鲁伊）"),
    ("惧焰亡灵", "死灵技能 +4、+3-5 火焰魔像"),
    ("剑卫", "全抗 20-30%、ED 180-230%、防御/级 7、+10-15 生命回复、攻击者受伤 15-25"),
    ("恶魔角尖", "+20% 攻速、+1 野蛮人技能"),
    ("钢铁面纱", "+2 全部技能、物理减伤 15-25%、魔法抗性 +20-40%"),
    ("无形之刃", "ED 220-260%、+40% 攻速、+2-198 最大伤害（按等级）"),
    ("劊子手的裁决", "ED 260-300%、+40% 攻速、25% 施放 13 级伤害加深、+15 击杀生命、+5 击杀法力"),
]

lines = ["ÿc4第 16 赛季暗金装备调整（官方 3.4，共 13 件）ÿc0", ""]
for name, chg in ITEMS:
    lines.append("ÿc4%sÿc0" % name)
    lines.append("  " + chg)
    lines.append("")
lines.append("ÿc;以上为官方第16赛季对既有暗金装备的数值调整，本 mod 不修改这些数据，仅作查询展示。")
TOOLTIP = "\n".join(lines)

TITLE = "第16赛季暗金调整（13件）"
ROW = "共 13 件暗金装备，鼠标移上来查看每件的改动"

# 1) 写字符串
arr = json.loads(open(NP, "rb").read().decode("utf-8-sig"))
have = {e.get("Key") for e in arr if isinstance(e, dict)}
ids = [e.get("id") for e in arr if isinstance(e, dict) and isinstance(e.get("id"), int)]
nid = max(ids) + 1
for k, v in (("jghelp53201S16UniqueTitle", TITLE),
             ("jghelp53202S16UniqueTooltip", TOOLTIP),
             ("jghelp53203S16UniqueRow", ROW)):
    if k in have:
        for e in arr:
            if isinstance(e, dict) and e.get("Key") == k:
                e["zhCN"] = v; e["zhTW"] = v; e["enUS"] = v
    else:
        arr.append({"id": nid, "Key": k, "zhCN": v, "zhTW": v, "enUS": v,
                    "deDE": "", "esES": "", "frFR": "", "itIT": "", "koKR": "", "plPL": "",
                    "esMX": "", "jaJP": "", "ptBR": "", "ruRU": ""})
        nid += 1
open(NP, "wb").write(json.dumps(arr, ensure_ascii=False, indent=1).encode("utf-8"))
print("字符串已写入 3 条")

# 2) 写布局
t = open(LA, "rb").read().decode("utf-8-sig")
i = t.find('"name": "WebLink"')
st = t.rfind("{", 0, i)
d = 0; j = st; ins = False; esc = False
while j < len(t):
    ch = t[j]
    if ins:
        if esc: esc = False
        elif ch == "\\": esc = True
        elif ch == '"': ins = False
    else:
        if ch == '"': ins = True
        elif ch == "{": d += 1
        elif ch == "}":
            d -= 1
            if d == 0:
                j += 1; break
    j += 1

section = ('{ "type": "Widget", "name": "S16Unique", "fields": { "rect": { "x": 0, "y": 680 } }, '
           '"children": [ '
           '{ "type": "Widget", "name": "Link", "fields": { "rect": { "x": 0, "y": 0 } }, "children": [ '
           '{ "type": "TextBoxWidget", "name": "S16UniqueTitle", "fields": { "rect": { "x": 0, "y": 0, "width": 600, "height": 80 }, '
           '"text": "@jghelp53201S16UniqueTitle", "style": { "fontColor": "$FontColorGoldYellow", "pointSize": "$XLargeFontSize", '
           '"alignment": { "h": "left", "v": "center" } } }, "children": [ '
           '{ "type": "FocusableWidget", "name": "Tooltip", "fields": { "fitToParent": true, '
           '"tooltipString": "@jghelp53202S16UniqueTooltip", "tooltipStyle": "$StandardLeftToolTipStyle" } } ] }, '
           '{ "type": "ImageWidget", "name": "Divider", "fields": { "rect": { "x": 0, "y": 64, "scale": 0.4 }, '
           '"filename": "PauseMenu\\\\Divider" } } ] }, '
           '{ "type": "Widget", "name": "Row1", "fields": { "rect": { "x": 0, "y": 80 } }, "children": [ '
           '{ "type": "TextBoxWidget", "name": "S16UniqueRowText", "fields": { "rect": { "x": 10, "y": 0, "width": 900, "height": 40 }, '
           '"text": "@jghelp53203S16UniqueRow", "style": { "fontColor": "$FontColorBlue", "pointSize": "$MediumFontSize" } }, "children": [ '
           '{ "type": "FocusableWidget", "name": "Tooltip", "fields": { "fitToParent": true, '
           '"tooltipString": "@jghelp53202S16UniqueTooltip", "tooltipStyle": "$StandardLeftToolTipStyle" } } ] } ] } ] }')

t2 = t[:j] + ",\n\n" + section + t[j:]
open(LA, "wb").write(t2.encode("utf-8-sig"))
print("布局：已在 WebLink 之后插入 S16Unique 区块")

# 3) 校验
t3 = open(LA, "rb").read().decode("utf-8-sig")
d = 0; ins = False; esc = False
for ch in t3:
    if ins:
        if esc: esc = False
        elif ch == "\\": esc = True
        elif ch == '"': ins = False
    else:
        if ch == '"': ins = True
        elif ch in "{[": d += 1
        elif ch in "}]": d -= 1
print("括号净深度:", d)
print("S16Unique 出现:", t3.count("S16Unique"))
print("tooltip 键:", t3.count("jghelp53202S16UniqueTooltip"))
