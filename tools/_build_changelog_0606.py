# -*- coding: utf-8 -*-
"""生成 shu-v0.6.06-更新日志.docx（沿用 0.6.05 的排版样式）"""
import os
from docx import Document
from docx.shared import Pt, RGBColor, Cm
from docx.enum.table import WD_TABLE_ALIGNMENT
from docx.oxml.ns import qn

WS = r'C:\Users\Administrator\Documents\deepseek-harness\default-workspace'
OUT = os.path.join(WS, 'shu-v0.6.06-更新日志.docx')

doc = Document()

sec = doc.sections[0]
sec.top_margin = Cm(2.2)
sec.bottom_margin = Cm(2.2)
sec.left_margin = Cm(2.4)
sec.right_margin = Cm(2.4)

style = doc.styles['Normal']
style.font.name = '微软雅黑'
style.font.size = Pt(10.5)
style.element.rPr.rFonts.set(qn('w:eastAsia'), '微软雅黑')
style.paragraph_format.space_after = Pt(4)
style.paragraph_format.line_spacing = 1.35


def h(text, level=1, color=None, size=None):
    p = doc.add_heading('', level=level)
    r = p.add_run(text)
    r.font.name = '微软雅黑'
    r._element.rPr.rFonts.set(qn('w:eastAsia'), '微软雅黑')
    if size:
        r.font.size = Pt(size)
    if color:
        r.font.color.rgb = RGBColor(*color)
    return p


def para(text, bold=False, size=None, color=None, indent=0, space_before=0):
    p = doc.add_paragraph()
    if indent:
        p.paragraph_format.left_indent = Cm(indent)
    if space_before:
        p.paragraph_format.space_before = Pt(space_before)
    r = p.add_run(text)
    r.bold = bold
    r.font.name = '微软雅黑'
    r._element.rPr.rFonts.set(qn('w:eastAsia'), '微软雅黑')
    if size:
        r.font.size = Pt(size)
    if color:
        r.font.color.rgb = RGBColor(*color)
    return p


def bullet(text, indent=0.6):
    p = doc.add_paragraph(style='List Bullet')
    p.paragraph_format.left_indent = Cm(indent)
    p.paragraph_format.space_after = Pt(2)
    r = p.add_run(text)
    r.font.name = '微软雅黑'
    r._element.rPr.rFonts.set(qn('w:eastAsia'), '微软雅黑')
    return p


def code(text):
    p = doc.add_paragraph()
    p.paragraph_format.left_indent = Cm(0.8)
    p.paragraph_format.space_after = Pt(2)
    r = p.add_run(text)
    r.font.name = 'Consolas'
    r.font.size = Pt(9)
    return p


def table(headers, rows, widths=None):
    t = doc.add_table(rows=1, cols=len(headers))
    t.style = 'Light Grid Accent 1'
    t.alignment = WD_TABLE_ALIGNMENT.CENTER
    t.autofit = False
    tblPr = t._tbl.tblPr
    layout = tblPr.makeelement(qn('w:tblLayout'), {qn('w:type'): 'fixed'})
    tblPr.append(layout)

    hdr = t.rows[0].cells
    for i, x in enumerate(headers):
        hdr[i].text = ''
        p = hdr[i].paragraphs[0]
        r = p.add_run(x)
        r.bold = True
        r.font.size = Pt(9.5)
        r.font.name = '微软雅黑'
        r._element.rPr.rFonts.set(qn('w:eastAsia'), '微软雅黑')
    for row in rows:
        cells = t.add_row().cells
        for i, x in enumerate(row):
            cells[i].text = ''
            p = cells[i].paragraphs[0]
            r = p.add_run(str(x))
            r.font.size = Pt(9)
            r.font.name = '微软雅黑'
            r._element.rPr.rFonts.set(qn('w:eastAsia'), '微软雅黑')
    if widths:
        for i, w in enumerate(widths):
            t.columns[i].width = Cm(w)
            for cell in t.columns[i].cells:
                cell.width = Cm(w)
    return t


# ---------------- 标题 ----------------
h('shu 模组 v0.6.06 更新日志', level=0, size=20)

info = [
    ('发布日期', '2026-10-31'),
    ('适用游戏', 'Diablo II: Resurrected 3.1.2（build 92198）'),
    ('适用加载器', 'D2RLoader 1.3.1+'),
    ('更新文件', 'shu-v0.6.06.zip'),
    ('更新性质', '系统更新（新增「洗练石」装备重铸系统，复用原版闲置物品 Elixir 作为载体）'),
]
for k, v in info:
    p = doc.add_paragraph()
    p.paragraph_format.space_after = Pt(1)
    r1 = p.add_run('%-10s' % k)
    r1.bold = True
    r1.font.size = Pt(9.5)
    r1.font.name = '微软雅黑'
    r1._element.rPr.rFonts.set(qn('w:eastAsia'), '微软雅黑')
    r2 = p.add_run('：' + v)
    r2.font.size = Pt(9.5)
    r2.font.name = '微软雅黑'
    r2._element.rPr.rFonts.set(qn('w:eastAsia'), '微软雅黑')

doc.add_paragraph()

# ---------------- 一 ----------------
h('一、本次更新', level=1, size=15)

h('1.1 新增道具：洗练石', level=2, size=12.5)
table(
    ['项目', '内容'],
    [
        ['购买地点', '赫拉铁力（第三幕 铁匠）'],
        ['价格', '50,000 金币'],
        ['库存', '常驻 1 颗（PermStoreItem），可重复购买'],
        ['用途', '在赫拉迪姆方块中与装备合成，重铸该装备'],
        ['图标', '借用原版 Elixir（灵药）的白色小药水瓶'],
    ],
    widths=[3.0, 13.0],
)
doc.add_paragraph()
para('关于 Elixir：洗练石复用了原版闲置物品 Elixir（代码 elx）的数据行。该物品在本 mod 中从未出现在掉落表、赌徒表、词缀表，也不在任何商人货架，属于永远无法获得的死数据，改造不影响任何现有玩法。代价是灵药物品自此不存在。', size=10)
para('为什么不能新建物品代码：D2R 的物品图标由引擎内部「物品代码 → HD 模型」映射决定，自制代码不在映射表里，invfile 填什么都会显示空白，只能复用原版代码。', size=10)
doc.add_paragraph()

h('1.2 重铸规则', level=2, size=12.5)
table(
    ['放入方块', '结果'],
    [
        ['洗练石 + 任意暗金', '同底材暗金，所有变量重 roll'],
        ['洗练石 + 任意黄装（稀有）', '同底材黄装，所有词缀重 roll'],
        ['洗练石 + 任意蓝装（魔法）', '同底材蓝装，所有词缀重 roll'],
        ['洗练石 + 套装', '暂未启用（usetype,set 未验证）'],
    ],
    widths=[6.0, 10.0],
)
doc.add_paragraph()
para('带孔与不带孔的装备都能洗，因为已额外登记了 ,sock 变体配方。', size=10)
bullet('每次消耗 1 颗洗练石，装备被重新生成：底材不变、品质不变，变量 / 词缀 / 孔数全部重 roll')
bullet('孔数 1–6 随机，上限由底材与物品等级自动截断；戒指、项链、珠宝、护身符上限为 0，永远洗不出孔')
bullet('无孔的装备也能洗出孔，这是刻意设计，等于洗练石兼职打孔服务')
bullet('镶嵌物不保留：重铸会清空孔里的宝石与符文，洗之前请先抠出来')
doc.add_paragraph()

h('1.3 重要限制：多暗金底材会「变脸」', level=2, size=12.5)
para('重铸是按底材生成物品，不是按「具体哪一件暗金」。当一个底材对应多件暗金时，结果是同底材里的随机一件。', size=10)
para('本 mod 共 362 个暗金底材：347 个只有一件暗金（洗了就是原物换数值，安全），15 个是多暗金底材（会变成同底材的另一件）。', size=10)
doc.add_paragraph()
table(
    ['底材', '暗金件数', '说明'],
    [
        ['rin 戒指', '18', '乔丹之石、拿各、曼纳德、婚戒、乌鸦之霜、蛋白石脉…'],
        ['amu 项链', '14', '玛拉、大君、亚特玛、金属网格…'],
        ['cm3 大护身符', '14', '基德、破免符、工艺破免符…'],
        ['jew 珠宝', '8', '彩虹刻面（各色）'],
        ['cjw 巨型珠宝', '6', '守护者 / 保卫者系列'],
        ['cs2 工艺符', '6', '破免工艺系列'],
        ['uar / uhm / ulm / xsk', '各 2', '泰瑞尔之力、夜翼面纱、钢铁面罩…'],
        ['7wh / 7gm / 7cr / 7fl / 7sc', '各 2', '碎脑锤、光之军刀、碧蓝怒火…'],
    ],
    widths=[4.6, 2.0, 9.4],
)
doc.add_paragraph()
para('举例：乔丹之石（戒指底材，18 件暗金共用）洗一次，可能变成拿各或乌鸦之霜。这是引擎行为，数据层无法指定「就洗这一件」，请把这 15 个底材当作赌运气。', size=10)
doc.add_paragraph()

h('1.4 经济性', level=2, size=12.5)
para('买价 50,000，卖回商人仅 70 金币。买卖价差约 700 倍，无法通过回购刷金币，金币消耗是单向的。', size=10)
doc.add_paragraph()

# ---------------- 二 ----------------
h('二、已知问题', level=1, size=15)
bullet('套装重铸（usetype,set）未验证，暂未启用')
bullet('多暗金底材会随机成同底材的另一件（见 1.3），引擎限制，无法修复')
bullet('重铸会清空镶嵌物')
bullet('仅限单机使用，请勿在 Battle.net 官方服务器使用')
doc.add_paragraph()

# ---------------- 三 ----------------
h('三、升级说明', level=1, size=15)
para('1. 解压覆盖到 mods/shu/ 目录', size=10)
para('2. 进入游戏，在控制台执行 d2rl compile shu', size=10)
para('3. 完全退出游戏后重新进入', size=10)
doc.add_paragraph()
para('已有的旧装备不会自动获得新属性，洗练石需要重新购买。', size=10, bold=True)
doc.add_paragraph()

# ---------------- 四 ----------------
h('四、发版必做：d2rl compile shu 步骤', level=1, size=15)

h('4.1 为什么必须做', level=2, size=12.5)
para('本 mod 当前处于 TXT 模式：Data/global/excel 与 base 子目录下的 .bin 全部为 0 个，游戏每次启动都现场编译 188 张表（约 500 ms）。', size=10)
bullet('玩家每次启动要多等半秒')
bullet('改动只存在于 txt，换机器或重装容易被覆盖')
bullet('打包给别人时，对方也要每次重编译')
para('发版前必须编译成完整的 BIN 集。', size=10, bold=True)
doc.add_paragraph()

h('4.2 操作步骤', level=2, size=12.5)
code('1. 确认 mod 目录下没有任何 .bin（当前就是这个状态）')
code('2. 启动游戏（D2RLoader 加载 shu）')
code('3. 进入游戏界面后，按 Ctrl + ` 打开开发者控制台')
code('4. 输入：  d2rl compile shu')
code('5. 等待编译完成（控制台会输出编译结果，通常几秒）')
code('6. 完全退出游戏')
code('7. 验证 bin 数量')
doc.add_paragraph()

h('4.3 编译后的验证基准', level=2, size=12.5)
para('2026-10-31 实测结果（控制台报告 188 write operations, 0 failed）：', size=10)
table(
    ['位置', '数量', '官方 3.1.2 参考集'],
    [
        ['Data/global/excel/*.bin', '97 个', '97 个'],
        ['Data/global/excel/base/*.bin', '95 个', '95 个'],
        ['合计', '192 个', '192 个'],
    ],
    widths=[8.2, 3.0, 5.0],
)
doc.add_paragraph()
para('最可靠的验证方式：与官方参考集对比，数量一致即完整。参考集位置：', size=10)
code('d2rloader/data/compiler/3.1.2/data/global/excel/      ← 97 个 .bin')
code('d2rloader/data/compiler/3.1.2/data/global/excel/base/ ← 95 个 .bin')
para('控制台那句 188 write operations 指的是编译的表数（写入次数），磁盘上的文件是 192 个 —— 两者差 4 是因为少数表会拆成多个文件。不要拿 188 去数文件数。', size=10)
para('少于基准说明没编译完整，此时游戏会报「custom BIN set 不完整」并拒绝加载 —— 处理办法见 4.5。', size=10)
doc.add_paragraph()

h('4.4 前置条件检查', level=2, size=12.5)
table(
    ['检查项', '当前状态'],
    [
        ['Data/global/.DISABLE_DEBUG', '不存在（调试功能未被禁用）'],
        ['d2rloader.toml → [d2rloader.developer] enable_console', 'true（控制台可用）'],
    ],
    widths=[9.0, 7.0],
)
doc.add_paragraph()
para('这两项任一不满足，控制台都打不开或 d2rl 命令不可用。', size=10)
doc.add_paragraph()

h('4.5 出问题怎么退', level=2, size=12.5)
para('编译失败或游戏报 BIN 不完整时，删掉所有 .bin 回到 TXT 模式，游戏立刻能正常启动：', size=10)
code('删除 Data/global/excel/*.bin')
code('删除 Data/global/excel/base/*.bin')
para('本次改动前的完整 BIN 备份在：', size=10)
code('E:\\暗黑破坏神2MOD制作\\_bin备份_rerollstone_20261031_1119\\')
code('    ├─ 95 个（excel 根目录）')
code('    └─ base\\ 93 个')
para('注意：那份备份是改动前编译的，放回去等于把洗练石一起回退掉。', size=10, bold=True)
doc.add_paragraph()

h('4.6 编译后不要做的事', level=2, size=12.5)
para('编译完不要再手改 excel 里的 txt。D2R 优先读 .bin、不比较时间戳，改了 txt 等于没改（详见 00_说明.md 8.2）。', size=10)
doc.add_paragraph()

h('4.7 本节的可信度说明', level=2, size=12.5)
para('操作步骤依据 D2RLoader 官方说明与 00_说明.md 中的既有记录整理。', size=10)
para('2026-10-31 已实际执行过并验证成功：控制台输出 BIN compile complete, 188 write operations, 0 failed；编译后磁盘为 97 + 95 = 192 个 .bin，与官方 3.1.2 参考集数量完全一致。', size=10)
para('提醒：编译完成后 mod 进入 BIN 模式。此后任何 excel 下的 txt 改动都不会生效，必须重新执行 d2rl compile shu（或删光 .bin 回到 TXT 模式）。', size=10)
doc.add_paragraph()

# ---------------- 五 ----------------
h('五、维护者备注（实现细节，不进玩家公告）', level=1, size=15)
table(
    ['坑', '现象', '原因'],
    [
        ['商人不上架', '店里看不到洗练石', 'type 填了 misc，而 itemtypes 里 Miscellaneous 的 StorePage 为空；必须用挂 misc 商店页的类型（elix / key / scro / book / gem）'],
        ['合成后装备消失', '装备与石头都没了', 'usetype 以 input 1 为模板，把洗练石放 input 1 会去生成「暗金版洗练石」，失败后输入被消耗；装备必须在 input 1'],
        ['图标空白', '物品格空着但有名字', '自制代码没有 HD 模型映射，invfile 无效；必须复用原版代码'],
        ['带孔装备洗不了', '方块不认', '需要单独的 ,sock 变体配方'],
        ['随机孔数', '想要 1–6 孔', 'output = usetype,<品质> + mod 1 = sock、mod 1 min/max = 1/6，无需 ,mod 后缀'],
    ],
    widths=[3.2, 3.6, 9.2],
)
doc.add_paragraph()
para('补丁生成脚本：_reroll_stone_patch.py（干跑 / --apply 两种模式，内含全部踩坑注释）。', size=9.5)

doc.save(OUT)
print('saved:', OUT, os.path.getsize(OUT), 'bytes')
