# -*- coding: utf-8 -*-
"""生成 shu-v0.6.07-更新日志.docx（沿用 0.6.05/0.6.06 的排版样式）"""
import os
from docx import Document
from docx.shared import Pt, RGBColor, Cm
from docx.enum.table import WD_TABLE_ALIGNMENT
from docx.oxml.ns import qn

WS = r'C:\Users\Administrator\Documents\deepseek-harness\default-workspace'
OUT = os.path.join(WS, 'shu-v0.6.07-更新日志.docx')

doc = Document()
sec = doc.sections[0]
sec.top_margin = Cm(2.2); sec.bottom_margin = Cm(2.2)
sec.left_margin = Cm(2.4); sec.right_margin = Cm(2.4)

style = doc.styles['Normal']
style.font.name = '微软雅黑'
style.font.size = Pt(10.5)
style.element.rPr.rFonts.set(qn('w:eastAsia'), '微软雅黑')
style.paragraph_format.space_after = Pt(4)
style.paragraph_format.line_spacing = 1.35


def h(text, level=1, size=None):
    p = doc.add_heading('', level=level)
    r = p.add_run(text)
    r.font.name = '微软雅黑'
    r._element.rPr.rFonts.set(qn('w:eastAsia'), '微软雅黑')
    if size:
        r.font.size = Pt(size)
    return p


def para(text, bold=False, size=None, indent=0):
    p = doc.add_paragraph()
    if indent:
        p.paragraph_format.left_indent = Cm(indent)
    r = p.add_run(text)
    r.bold = bold
    r.font.name = '微软雅黑'
    r._element.rPr.rFonts.set(qn('w:eastAsia'), '微软雅黑')
    if size:
        r.font.size = Pt(size)
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


h('shu 模组 v0.6.07 更新日志', level=0, size=20)

info = [
    ('发布日期', '2026-11-02'),
    ('适用游戏', 'Diablo II: Resurrected 3.1.2（build 92198）'),
    ('适用加载器', 'D2RLoader 1.3.1+'),
    ('更新文件', 'shu-v0.6.07.zip'),
    ('更新性质', '内容更新（德鲁伊新增被动技能「支配物理」）'),
]
for k, v in info:
    p = doc.add_paragraph()
    p.paragraph_format.space_after = Pt(1)
    r1 = p.add_run('%-10s' % k); r1.bold = True; r1.font.size = Pt(9.5); r1.font.name = '微软雅黑'
    r1._element.rPr.rFonts.set(qn('w:eastAsia'), '微软雅黑')
    r2 = p.add_run('：' + v); r2.font.size = Pt(9.5); r2.font.name = '微软雅黑'
    r2._element.rPr.rFonts.set(qn('w:eastAsia'), '微软雅黑')

doc.add_paragraph()

h('一、本次更新', level=1, size=15)
h('1.1 新增德鲁伊技能「支配物理」', level=2, size=12.5)
table(
    ['项目', '内容'],
    [
        ['技能类型', '被动（学会即生效，无需施放）'],
        ['学习等级', '30 级'],
        ['等级上限', '20 级'],
        ['技能树位置', '元素系 · 第 6 行第 3 格'],
        ['图标', '复用德鲁伊图标表 56 号（Maul 巨力挥击）'],
        ['核心效果', '每级 -2% 敌人物理抗性，20 级 = -40%'],
        ['破免机制', '自带物理免疫破除'],
    ],
    widths=[3.4, 12.6],
)
doc.add_paragraph()
para('设计动机：纯召唤流德鲁伊碰到物理免疫怪几乎无解 —— 召唤物打的都是物理伤害，物免怪直接免疫。这个被动让召唤流也有了自己的破免手段，不必依赖特定装备。', size=10)
doc.add_paragraph()

h('1.2 破免是怎么生效的', level=2, size=12.5)
para('普通减抗对「物理免疫」的怪是无效的，因为免疫是独立判定。本技能的处理顺序是：', size=10)
code('第一步  物免怪的物理抗性强制按 95% 计算（破免）')
code('第二步  再叠加本技能的 -2%/级')
doc.add_paragraph()

h('1.3 实际减抗数值', level=2, size=12.5)
table(
    ['技能等级', '本技能减抗', '对物理免疫怪的最终抗性', '实际承受伤害'],
    [
        ['1 级', '-2%', '93%', '7%'],
        ['5 级', '-10%', '85%', '15%'],
        ['10 级', '-20%', '75%', '25%'],
        ['15 级', '-30%', '65%', '35%'],
        ['20 级', '-40%', '55%', '45%'],
    ],
    widths=[3.0, 3.6, 5.4, 4.0],
)
doc.add_paragraph()
para('也就是说，满级的支配物理能让纯召德打出约 45% 的物理伤害，而不是 0。', size=10)
doc.add_paragraph()

h('1.4 实现方式（维护者参考）', level=2, size=12.5)
table(
    ['文件', '改动'],
    [
        ['skills.txt', '新增 Phys Mastery 行（*Id = 436），passive = 1'],
        ['skilldesc.txt', '新增 physmastery 行，SkillPage 3 / SkillRow 6 / SkillColumn 3'],
        ['item-names.json', '新增 4 条字符串（技能名、长描述、简称、抗性标签）'],
    ],
    widths=[4.0, 12.0],
)
doc.add_paragraph()
para('被动属性配置：', size=10)
code('passivestat1 = item_pierce_damage_immunity    calc = 1        ← 破物免')
code('passivestat2 = passive_dmg_pierce             calc = lvl*2    ← 每级 -2%')
para('写法与 Armageddon（火穿透）、Hurricane（冰穿透）一致，那两个技能已验证可用。', size=10)
doc.add_paragraph()

h('二、已知限制', level=1, size=15)
bullet('召唤物是否继承该减抗，制作时未能在实机确认。若实测发现狼/熊/灰熊的伤害没有变化，下个版本会给召唤技能补上继承字段（可参考 Raven 现有的 item_pierce_damage_immunity 写法）')
bullet('图标是借用的德鲁伊图标（56 号 Maul），没有专属美术资源')
bullet('技能树行序本身对应 1/6/12/18/24/30 级，本技能放在第 6 行，位置与学习等级一致')
doc.add_paragraph()

h('三、升级说明', level=1, size=15)
para('1. 解压覆盖到 mods/shu/ 目录', size=10)
para('2. 本包已含完整 192 个 .bin，无需重新编译', size=10)
para('3. 完全退出游戏后重新进入', size=10)
doc.add_paragraph()
para('已投入的技能点不受影响（技能 id 固定），本版只是新增了一个可选技能。', size=10, bold=True)
doc.add_paragraph()

h('四、如何验证', level=1, size=15)
para('1. 德鲁伊角色升到 30 级', size=10)
para('2. 打开技能树 → 元素页 → 最后一行最右格', size=10)
para('3. 图标应为「巨力挥击」样式，名称显示「支配物理」', size=10)
para('4. 加满后描述应显示 -40% 敌人的物理抗性', size=10)
para('5. 找一个物理免疫的怪（地狱难度鬼魂类/物免僵尸）实测伤害', size=10)

doc.save(OUT)
print('saved:', OUT, os.path.getsize(OUT), 'bytes')
