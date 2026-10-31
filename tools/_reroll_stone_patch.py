# -*- coding: utf-8 -*-
"""
为 shu mod 生成「洗练石」补丁（最终版，对应 2026-10-31 11:34 落盘状态）。

三处改动：
  1. misc.txt         追加 rrs 行：洗练石，Hratli 常驻，50000 金币，白色药水图标
  2. cubemain.txt     追加配方：unique / rare / rare-socketed / magic（set 先禁用）
  3. item-names.json  追加字符串（id 与 Key 全局查重）

用法：
    python _reroll_stone_patch.py            # 干跑，只打印计划
    python _reroll_stone_patch.py --apply    # 写入（自动 .bak 备份）

踩过的坑（别再踩）：
  * type 不能用 "misc"：itemtypes.txt 里 Miscellaneous 的 StorePage 为空，商人不进货。
  * usetype 以 input 1 为模板，装备必须放 input 1；放反了输出为空、两个输入都被消耗。
  * 图标不能用 toa（invtoa）：赦免之证是 HD 独占物品，没有经典 DC6，显示空白。
  * 本文件必须存为 UTF-8 无 BOM；用 PowerShell 的 Set-Content 改写会按 ANSI 读坏中文。
"""
import json
import os
import shutil
import sys
from datetime import datetime

MOD = r"E:\diablo2RTCP3.1.2\Diablo II Resurrected newwang\mods\shu\shu.mpq\Data"
EXCEL = os.path.join(MOD, "global", "excel")
STRINGS = os.path.join(MOD, "local", "lng", "strings")

CODE = "rrs"
NAME_EN = "Reroll Stone"
NAME_CN = "洗练石"
NAME_TW = "洗鍊石"
COST = "50000"
NEW_STR_ID = 520090

# (描述, input1 品质/类型, 输出, 启用)
RECIPES = [
    ("Reroll Stone + Unique -> same base Unique (reroll variables)", "any,uni", "usetype,uni", True),
    ("Reroll Stone + Set -> same base Set (reroll variables)", "any,set", "usetype,set", False),
    ("Reroll Stone + Magic -> same base Magic (reroll affixes)", "any,mag", "usetype,mag", True),
    ("Reroll Stone + Rare -> same base Rare (reroll affixes)", "any,rar", "usetype,rar", True),
    ("Reroll Stone + Rare socketed -> same base Rare", "any,rar,sock", "usetype,rar", True),
]

APPLY = "--apply" in sys.argv


def read_text(path):
    raw = open(path, "rb").read()
    if raw[:3] == b"\xef\xbb\xbf":
        raise SystemExit("%s 带 BOM，excel 表不允许" % os.path.basename(path))
    return raw.decode("utf-8")


def backup(path):
    stamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    dst = "%s.bak-rerollstone-%s" % (path, stamp)
    shutil.copy2(path, dst)
    return dst


def build_misc():
    path = os.path.join(EXCEL, "misc.txt")
    text = read_text(path)
    lines = text.split("\n")
    hdr = [h.rstrip("\r") for h in lines[0].split("\t")]
    idx = {h: i for i, h in enumerate(hdr)}

    def row_of(code):
        for ln in lines[1:]:
            f = ln.rstrip("\r").split("\t")
            if len(f) > idx["code"] and f[idx["code"]] == code:
                return f
        return None

    template = row_of("elx")          # Elixir：白色药水瓶
    if template is None:
        raise SystemExit("找不到 elx（Elixir）模板行")
    if len(template) != len(hdr):
        raise SystemExit("模板列数 %d != 表头 %d" % (len(template), len(hdr)))

    row = list(template)

    for h in hdr:  # 清空所有 NPC 库存 / 魔法生成列
        if h.endswith(("Min", "Max", "MagicMin", "MagicMax", "MagicLvl")) and h not in ("minstack", "maxstack"):
            row[idx[h]] = ""
    for h in ("spelldesc", "spelldescstr", "spelldescstr2", "spelldesccalc", "spelldesccolor",
              "pSpell", "spellicon", "state", "cstate1", "cstate2", "len",
              "stat1", "calc1", "stat2", "calc2", "stat3", "calc3"):
        row[idx[h]] = ""   # 清空 Elixir 自带的使用效果

    overrides = {
        "name": "Reroll Stone",
        "compactsave": "0",
        "version": "100",
        "level": "0",
        "ShowLevel": "1",
        "levelreq": "0",
        "reqstr": "0",
        "reqdex": "0",
        "rarity": "999",
        "spawnable": "1",
        "speed": "0",
        "nodurability": "1",
        "cost": COST,
        "code": CODE,
        "alternategfx": "elx",
        "namestr": CODE,
        "component": "16",
        "invwidth": "1",
        "invheight": "1",
        "hasinv": "0",
        "gemsockets": "0",
        "gemapplytype": "0",
        "flippyfile": "flppot",
        "invfile": "invpot",
        "uniqueinvfile": "",
        "Transmogrify": "0",
        "TMogType": "",
        "useable": "0",
        "type": "elix",
        "type2": "",
        "dropsound": "item_potion",
        "dropsfxframe": "14",
        "usesound": "item_potion_drink",
        "unique": "0",
        "transparent": "0",
        "transtbl": "5",
        "lightradius": "0",
        "belt": "0",
        "autobelt": "0",
        "stackable": "0",
        "quest": "0",
        "questdiffcheck": "0",
        "missiletype": "0",
        "durwarning": "0",
        "qntwarning": "0",
        "gemoffset": "0",
        "BetterGem": "non",
        "bitfield1": "0",
        "Transform": "0",
        "InvTrans": "0",
        "SkipName": "0",
        "NightmareUpgrade": "xxx",
        "HellUpgrade": "xxx",
        "PermStoreItem": "1",
        "multibuy": "1",
        "Nameable": "0",
        "EventItem": "0",
        "UICatOverride": "",
        "diablocloneweight": "0",
        "AdvancedStashStackable": "0",
        "UsageConditionCalc": "",
    }
    for k, v in overrides.items():
        if k not in idx:
            raise SystemExit("misc.txt 缺少列: %s" % k)
        row[idx[k]] = v

    row[idx["HratliMin"]] = "1"
    row[idx["HratliMax"]] = "1"
    row[idx["HratliMagicLvl"]] = "255"
    for vendor in ("Charsi", "Gheed", "Akara", "Fara", "Lysander", "Drognan", "Alkor",
                   "Ormus", "Elzix", "Asheara", "Cain", "Halbu", "Malah", "Larzuk",
                   "Anya", "Jamella"):
        row[idx[vendor + "MagicLvl"]] = "255"

    if len(row) != len(hdr):
        raise SystemExit("生成行列数异常")
    new_text = text.rstrip("\r\n") + "\n" + "\t".join(row) + "\n"
    return path, new_text, row, hdr


def build_cubemain():
    path = os.path.join(EXCEL, "cubemain.txt")
    text = read_text(path)
    hdr = [h.rstrip("\r") for h in text.split("\n")[0].split("\t")]
    idx = {h: i for i, h in enumerate(hdr)}
    n = len(hdr)

    rows = []
    for desc, target, out, enabled in RECIPES:
        row = [""] * n
        row[idx["description"]] = desc
        row[idx["enabled"]] = "1" if enabled else "0"
        row[idx["version"]] = "100"
        row[idx["numinputs"]] = "2"
        row[idx["input 1"]] = '"%s"' % target      # usetype 以 input 1 为模板
        row[idx["input 2"]] = '"%s"' % CODE
        row[idx["output"]] = '"%s"' % out
        row[idx["ilvl"]] = "99"
        row[idx["*eol"]] = "0"
        if len(row) != n:
            raise SystemExit("cubemain 行列数异常")
        rows.append("\t".join(row))

    new_text = text.rstrip("\r\n") + "\r\n" + "\r\n".join(rows) + "\r\n"
    return path, new_text, rows, hdr


def build_strings():
    path = os.path.join(STRINGS, "item-names.json")
    text = open(path, "rb").read().decode("utf-8-sig")

    used = set()
    for fn in os.listdir(STRINGS):
        if not fn.endswith(".json"):
            continue
        try:
            data = json.loads(open(os.path.join(STRINGS, fn), "rb").read().decode("utf-8-sig"))
        except Exception:
            continue
        if isinstance(data, list):
            for e in data:
                if isinstance(e, dict) and isinstance(e.get("id"), int):
                    used.add(e["id"])

    sid = NEW_STR_ID
    while sid in used:
        sid += 1

    entry = {
        "id": sid, "Key": CODE,
        "enUS": NAME_EN, "zhTW": NAME_TW,
        "deDE": "", "esES": "", "frFR": "", "itIT": "", "koKR": "",
        "plPL": "", "esMX": "", "jaJP": "", "ptBR": "", "ruRU": "",
        "zhCN": NAME_CN,
    }
    block = json.dumps(entry, ensure_ascii=False, indent=1).replace("\n", "\n ")
    body = text.rstrip()[:-1].rstrip()
    new_text = body + ",\r\n " + block + "\r\n]\r\n"
    return path, new_text, sid, entry


def main():
    m_path, m_new, m_row, m_hdr = build_misc()
    c_path, c_new, c_rows, c_hdr = build_cubemain()
    s_path, s_new, sid, entry = build_strings()

    print("=" * 72)
    print("1) misc.txt -> rrs")
    for k in ("name", "code", "type", "cost", "invfile", "flippyfile", "useable",
              "PermStoreItem", "HratliMin", "HratliMax"):
        print("   %-15s = %r" % (k, m_row[m_hdr.index(k)]))
    print("\n2) cubemain.txt -> %d 条" % len(c_rows))
    for r in c_rows:
        f = r.split("\t")
        print("   en=%s  %-12s + rrs -> %-12s" % (
            f[c_hdr.index("enabled")], f[c_hdr.index("input 1")], f[c_hdr.index("output")]))
    print("\n3) item-names.json -> id=%d Key=%s (%s)" % (sid, CODE, entry["zhCN"]))
    print()

    if not APPLY:
        print("干跑结束。加 --apply 才写入。")
        return

    for p in (m_path, c_path, s_path):
        print("backup ->", os.path.basename(backup(p)))
    open(m_path, "wb").write(m_new.encode("utf-8"))
    open(c_path, "wb").write(c_new.encode("utf-8"))
    open(s_path, "wb").write(s_new.encode("utf-8"))
    print("写入完成。本项目当前用 TXT 模式，游戏启动即重新编译。")


if __name__ == "__main__":
    main()
