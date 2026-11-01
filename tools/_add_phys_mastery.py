# -*- coding: utf-8 -*-
"""
给 shu mod 的德鲁伊召唤系新增技能「支配物理」(Physical Domination)。

设计：
  - 被动技能，30 级可学，20 级上限
  - 每级 -2% 敌人物理抗性（passive_dmg_pierce = lvl*2）
  - 自带破物免：item_pierce_damage_immunity = 1（强制把物理免疫怪视为 95% 抗性）

改动三处：
  1. skills.txt      新增一行（克隆 Mace Mastery 的被动骨架）
  2. skilldesc.txt   新增一行（page1 row5 col1，图标复用锤系精通 IconCel=6）
  3. item-names.json 新增字符串（技能名 / 描述 / 抗性描述标签）

用法：
    python _add_phys_mastery.py           # 干跑
    python _add_phys_mastery.py --apply   # 写入（自动备份）

已知风险：
  - 技能名字符串表不在 mod 内（来自游戏本体 CASC），这里把 key 加进
    item-names.json 依赖「所有字符串表合并成全局 key 表」的机制。
    若游戏里技能名显示为空白，需要改用 CascView 提取本体 skills 字符串表。
  - 召唤物能否继承这个穿透，取决于引擎；本次先做玩家侧，宠物侧留待实测。
"""
import json
import os
import shutil
import sys
from datetime import datetime

MOD = r"E:\diablo2RTCP3.1.2\Diablo II Resurrected newwang\mods\shu\shu.mpq\Data"
EXCEL = os.path.join(MOD, "global", "excel")
STRINGS = os.path.join(MOD, "local", "lng", "strings")

SKILL_NAME = "Phys Mastery"        # 内部名
SKILL_ID = "436"                   # 全表最大 *Id 435 + 1
DESC_KEY = "physmastery"
REQ_LEVEL = "30"
MAX_LEVEL = "20"

STR_NAME = "Skillname_physmastery"
STR_LONG = "Skillld_physmastery"
STR_ALT = "Skillan_physmastery"
STR_PIERCE = "Moditemenresphyssk"

IDS = {STR_NAME: 520091, STR_LONG: 520092, STR_ALT: 520093, STR_PIERCE: 520094}

TEXTS = {
    STR_NAME: ("支配物理", "Physical Domination"),
    STR_LONG: (
        "被动：降低敌人的物理抗性，每级 2%。\n"
        "同时对物理免疫的敌人生效 —— 先将其物理抗性视为 95%，再计算本技能的减抗。",
        "Passive: reduces enemy physical resistance by 2% per level.\n"
        "Also breaks physical immunity: immune monsters are treated as 95% resistant first.",
    ),
    STR_ALT: ("支配物理", "Physical Domination"),
    STR_PIERCE: ("-%d%% 敌人的物理抗性", "-%d%% to Enemy Physical Resistance"),
}

APPLY = "--apply" in sys.argv


def read_text(path):
    raw = open(path, "rb").read()
    if raw[:3] == b"\xef\xbb\xbf":
        raise SystemExit("%s 带 BOM，excel 表不允许" % os.path.basename(path))
    return raw.decode("utf-8")


def backup(path):
    stamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    dst = "%s.bak-physmastery-%s" % (path, stamp)
    shutil.copy2(path, dst)
    return dst


def build_skills():
    path = os.path.join(EXCEL, "skills.txt")
    text = read_text(path)
    lines = text.split("\n")
    hdr = [h.rstrip("\r") for h in lines[0].split("\t")]
    ix = {h: i for i, h in enumerate(hdr)}

    tpl = None
    for ln in lines[1:]:
        f = ln.rstrip("\r").split("\t")
        if len(f) == len(hdr) and f[ix["skill"]] == "Mace Mastery":
            tpl = f
            break
    if tpl is None:
        raise SystemExit("找不到 Mace Mastery 模板行")

    row = list(tpl)
    # 清空武器限定与精通专属字段，否则只对钝器生效
    for k in ("passiveitype", "passivestat3", "passivecalc3",
              "Param1", "Param2", "Param3", "Param4", "Param5", "Param6",
              "reqskill1", "reqskill2", "reqskill3"):
        if k in ix:
            row[ix[k]] = ""
    for k in ("*Param1 Description", "*Param2 Description", "*Param3 Description",
              "*Param4 Description", "*Param5 Description", "*Param6 Description"):
        if k in ix:
            row[ix[k]] = ""

    over = {
        "skill": SKILL_NAME,
        "*Id": SKILL_ID,
        "charclass": "dru",
        "skilldesc": DESC_KEY,
        "reqlevel": REQ_LEVEL,
        "maxlvl": MAX_LEVEL,
        "passivestat1": "item_pierce_damage_immunity",
        "passivecalc1": "1",
        "passivestat2": "passive_dmg_pierce",
        "passivecalc2": "lvl*2",
        "passive": "1",
        "aura": "1",
    }
    for k, v in over.items():
        if k not in ix:
            raise SystemExit("skills.txt 缺少列: %s" % k)
        row[ix[k]] = v

    if len(row) != len(hdr):
        raise SystemExit("技能行列数异常")
    new_text = text.rstrip("\r\n") + "\n" + "\t".join(row) + "\n"
    return path, new_text, row, hdr


def build_skilldesc():
    path = os.path.join(EXCEL, "skilldesc.txt")
    text = read_text(path)
    lines = text.split("\n")
    hdr = [h.rstrip("\r") for h in lines[0].split("\t")]
    ix = {h: i for i, h in enumerate(hdr)}

    tpl = None
    for ln in lines[1:]:
        f = ln.rstrip("\r").split("\t")
        if len(f) == len(hdr) and f[ix["skilldesc"]] == "mace mastery":
            tpl = f
            break
    if tpl is None:
        raise SystemExit("找不到 mace mastery 的 skilldesc 模板行")

    row = list(tpl)
    # 清空原有的三条描述行（本来写的是锤系精通的攻速/伤害）
    for i in range(1, 6):
        for p in ("descline", "desctexta", "desctextb", "desccalca", "desccalcb"):
            k = "%s%d" % (p, i)
            if k in ix:
                row[ix[k]] = ""

    over = {
        "skilldesc": DESC_KEY,
        "SkillPage": "1",
        "SkillRow": "5",
        "SkillColumn": "1",
        "ListRow": "1",
        "IconCel": "6",          # 复用锤系精通图标
        "str name": STR_NAME,
        "str short": STR_LONG,
        "str long": STR_LONG,
        "str alt": STR_ALT,
        "descline1": "74",
        "desctexta1": STR_PIERCE,
        "desccalca1": "lvl*2",
    }
    for k, v in over.items():
        if k not in ix:
            raise SystemExit("skilldesc.txt 缺少列: %s" % k)
        row[ix[k]] = v

    if len(row) != len(hdr):
        raise SystemExit("skilldesc 行列数异常")
    new_text = text.rstrip("\r\n") + "\n" + "\t".join(row) + "\n"
    return path, new_text, row, hdr


def build_strings():
    path = os.path.join(STRINGS, "item-names.json")
    text = open(path, "rb").read().decode("utf-8-sig")

    used_ids, used_keys = set(), set()
    for fn in os.listdir(STRINGS):
        if not fn.endswith(".json"):
            continue
        try:
            data = json.loads(open(os.path.join(STRINGS, fn), "rb").read().decode("utf-8-sig"))
        except Exception:
            continue
        if isinstance(data, list):
            for e in data:
                if isinstance(e, dict):
                    if isinstance(e.get("id"), int):
                        used_ids.add(e["id"])
                    if isinstance(e.get("Key"), str):
                        used_keys.add(e["Key"].lower())

    for k in TEXTS:
        if k.lower() in used_keys:
            raise SystemExit("字符串 Key 已存在: %s" % k)
        if IDS[k] in used_ids:
            raise SystemExit("字符串 id 已被占用: %s -> %s" % (k, IDS[k]))

    entries = []
    for k, (zh, en) in TEXTS.items():
        entries.append({
            "id": IDS[k], "Key": k,
            "enUS": en, "zhTW": zh,
            "deDE": "", "esES": "", "frFR": "", "itIT": "", "koKR": "",
            "plPL": "", "esMX": "", "jaJP": "", "ptBR": "", "ruRU": "",
            "zhCN": zh,
        })

    body = text.rstrip()
    body = body[:-1].rstrip()
    blocks = []
    for e in entries:
        blk = json.dumps(e, ensure_ascii=False, indent=1).replace("\n", "\n ")
        blocks.append(" " + blk)
    new_text = body + ",\r\n" + ",\r\n".join(blocks) + "\r\n]\r\n"
    return path, new_text, entries


def main():
    s_path, s_new, s_row, s_hdr = build_skills()
    d_path, d_new, d_row, d_hdr = build_skilldesc()
    t_path, t_new, entries = build_strings()

    six = {h: i for i, h in enumerate(s_hdr)}
    dix = {h: i for i, h in enumerate(d_hdr)}

    print("=" * 74)
    print("1) skills.txt 新增技能行")
    for k in ("skill", "*Id", "charclass", "skilldesc", "reqlevel", "maxlvl",
              "passive", "aura", "passivestat1", "passivecalc1", "passivestat2", "passivecalc2"):
        print("   %-16s = %r" % (k, s_row[six[k]]))
    print("   武器限定 passiveitype = %r（应为空）" % s_row[six["passiveitype"]])
    print()
    print("2) skilldesc.txt 新增描述行")
    for k in ("skilldesc", "SkillPage", "SkillRow", "SkillColumn", "IconCel",
              "str name", "descline1", "desctexta1", "desccalca1"):
        print("   %-14s = %r" % (k, d_row[dix[k]]))
    print()
    print("3) 字符串 %d 条" % len(entries))
    for e in entries:
        print("   id=%-7s %-22s %s" % (e["id"], e["Key"], e["zhCN"][:24]))

    if not APPLY:
        print("\n干跑结束，加 --apply 写入。")
        return

    for p in (s_path, d_path, t_path):
        print("backup ->", os.path.basename(backup(p)))
    open(s_path, "wb").write(s_new.encode("utf-8"))
    open(d_path, "wb").write(d_new.encode("utf-8"))
    open(t_path, "wb").write(t_new.encode("utf-8"))
    print("写入完成。")


if __name__ == "__main__":
    main()
