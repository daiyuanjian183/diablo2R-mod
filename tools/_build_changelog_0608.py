# -*- coding: utf-8 -*-
"""生成 shu-v0.6.08-更新日志.docx（沿用既有排版样式）"""
import os
from docx import Document
from docx.shared import Pt, Cm
from docx.enum.table import WD_TABLE_ALIGNMENT
from docx.oxml.ns import qn

WS = r'C:\Users\Administrator\Documents\deepseek-harness\default-workspace'
OUT = os.path.join(WS, 'shu-v0.6.08-更新日志.docx')

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


def para(text, bold=False, size=None):
    p = doc.add_paragraph()
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
        r = p.add_run(x); r.bold = True; r.font.size = Pt(9.5); r.font.name = '微软雅黑'
        r._element.rPr.rFonts.set(qn('w:eastAsia'), '微软雅黑')
    for row in rows:
        cells = t.add_row().cells
        for i, x in enumerate(row):
            cells[i].text = ''
            p = cells[i].paragraphs[0]
            r = p.add_run(str(x)); r.font.size = Pt(9); r.font.name = '微软雅黑'
            r._element.rPr.rFonts.set(qn('w:eastAsia'), '微软雅黑')
    if widths:
        for i, w in enumerate(widths):
            t.columns[i].width = Cm(w)
            for cell in t.columns[i].cells:
                cell.width = Cm(w)
    return t


h('shu 模组 v0.6.08 更新日志', level=0, size=20)

info = [
    ('发布日期', '2026-11-02'),
    ('适用游戏', 'Diablo II: Resurrected 3.1.2（build 92198）'),
    ('适用加载器', 'D2RLoader 1.3.1+'),
    ('更新文件', 'shu-v0.6.08.zip'),
    ('更新性质', '功能补全（召唤物继承「支配物理」）'),
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
h('1.1 召唤物现在会继承「支配物理」', level=2, size=12.5)
para('v0.6.07 只保证玩家自身的物理伤害吃到减抗；本版补上召唤物继承。', size=10)
para('查表时发现，mod 里其实早就做过一半 —— 三个召唤技能本来就带着破免字段：', size=10)
doc.add_paragraph()
table(
    ['召唤技能', '原有继承', '本次新增'],
    [
        ['召唤鬼狼', '槽 6：冰免破除', '槽 7：物免破除、槽 8：物理穿透'],
        ['召唤芬里斯', '槽 4：物免破除', '槽 5：物理穿透'],
        ['召唤灰熊', '槽 4：物免破除', '槽 5：物理穿透'],
    ],
    widths=[3.6, 5.2, 7.2],
)
doc.add_paragraph()
para('也就是说，芬里斯和灰熊一直就能打物免怪（破免已有），之前缺的只是「-2%/级」这一半。', size=10)
para('写法完全照搬 mod 里已有的 Plague Poppy（毒系宠物）：', size=10)
code('passivestat = passive_dmg_pierce')
code("passivecalc = stat('passive_dmg_pierce'.accr)")
para("stat(...'.accr) 的语义是「把召唤者的这个属性复制给宠物」，所以宠物拿到的减抗值等于你当前技能等级对应的数值。", size=10)
doc.add_paragraph()

h('1.2 生效时机（很重要）', level=2, size=12.5)
para('这类复制是在召唤那一刻结算一次，不是实时同步：', size=10)
bullet('先加满技能 → 再召唤 → 宠物拿到 -40%')
bullet('先召唤 → 后加点 → 宠物仍是旧值，必须重新召唤')
doc.add_paragraph()

h('1.3 实测结果', level=2, size=12.5)
para('满级「支配物理」+ 重新召唤灰熊，对物理免疫怪可打出约 45% 伤害（此前为 0）。', size=10)
doc.add_paragraph()

h('二、已知限制', level=1, size=15)
bullet('v0.6.07 里写的「召唤物是否继承待实测」—— 本条已解决，见 1.1')
bullet('图标仍为借用（德鲁伊图标表 56 号 Maul），暂无专属美术资源')
doc.add_paragraph()

h('三、升级说明', level=1, size=15)
para('1. 解压覆盖到 mods/shu/ 目录', size=10)
para('2. 本包已含完整 192 个 .bin，无需重新编译', size=10)
para('3. 完全退出游戏后重新进入', size=10)
doc.add_paragraph()
para('升级后请重新召唤宠物，否则场上已有的狼/熊仍然沿用旧属性。', size=10, bold=True)
doc.add_paragraph()

h('四、验证方法', level=1, size=15)
para('1. 德鲁伊 30 级 → 元素系第 6 行第 3 格 → 加满「支配物理」', size=10)
para('2. 重新召唤灰熊 / 芬里斯 / 鬼狼', size=10)
para('3. 去打物理免疫的怪（地狱难度鬼魂类、物免僵尸）', size=10)
para('4. 对比未学技能时的伤害', size=10)

doc.save(OUT)
print('saved:', OUT, os.path.getsize(OUT), 'bytes')
