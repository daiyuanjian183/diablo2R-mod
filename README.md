# shu

**一个面向《暗黑破坏神 2：重制版》的深度玩法改造模组**
*A deep gameplay overhaul for Diablo II: Resurrected*

[![D2RLoader](https://img.shields.io/badge/D2RLoader-1.3.1-blue)](https://d2rloader.net)
[![D2R](https://img.shields.io/badge/D2R-3.1.2-green)]()
[![Version](https://img.shields.io/badge/version-0.6.01-orange)]()

---

## 简介 / Overview

**中文**

shu 是一个以"重做佣兵体系"和"打通抗性穿透"为核心的大型玩法模组。它不改变游戏的整体框架，而是重写了五大佣兵的技能构成，并为六个伤害系别提供了可成长、可破免的抗性穿透手段。

**English**

shu is a large-scale gameplay overhaul built around two ideas: rebuilding the five mercenary archetypes from the ground up, and giving every damage type a scalable path through enemy resistances.

---

## 核心特性 / Features

### 一、五大佣兵全面重做 / Five mercenaries reworked

| 幕 / Act | 佣兵 / Mercenary | 核心机制 / Core mechanics |
| --- | --- | --- |
| 1 | 罗格射手 / Rogue Scout | 内视索敌 + 魔法箭 / 连珠箭 + 救赎 / 狂热光环 |
| 2 | 沙漠佣兵 / Desert Mercenary | 戳刺 + 偷取生命诅咒 + 六系光环 + 30% 压碎性打击 |
| 3 | 铁狼法师 / Eastern Sorceror | 拯救光环 + 五技能 + 寒冰护甲 + 元素精通 |
| 4 | 死灵法师 / Act IV Necromancer | 审判光环 + 诅咒 + 骨系输出 + 盾牌槽 |
| 5 | 野蛮人 / Barbarian | 专注光环 + 战斗体制 + 狂战士 + 全装备槽 |

**所有佣兵可装备 10 个物品槽位，含盾牌。**
*Every mercenary can equip up to 10 item slots, shields included.*

### 二、六系抗性穿透 / Resistance pierce on six damage types

| 系 / Type | 技能 / Skill | 效果 / Effect |
| --- | --- | --- |
| 火 / Fire | 火焰支配、毁天灭地 | 每级 -2% 敌人火抗 + 破火免疫 |
| 冰 / Cold | 飓风 | 每级 -2% 敌人冰抗 + 破冰免疫 |
| 电 / Lightning | 闪电支配 | 每级 -2% 敌人电抗 + 破电免疫 |
| 毒 / Poison | 剧毒藤蔓 | 每级 -2% 敌人毒抗 + 破毒免疫 |
| 物理 / Physical | 钢铁之肤 | 每级 -2% 敌人物抗 + 破物免疫 |

### 三、八大职业束缚恶魔 / Bind Demon for all classes

**术士的束缚恶魔作为独立技能提供给其余七个职业，位于各自技能树第 6 行（等级 30 解锁），共享同一套恶魔类型。**

*The Warlock's Bind Demon is provided as an independent skill for the other seven classes, on row 6 of each skill tree (unlocks at level 30). All variants share the same demon type.*

### 四、其他改动 / Other changes

- 背包扩容至 13 × 8 / Inventory expanded to 13 × 8
- 鉴定书、传送书堆叠上限 100 / Tomes stack to 100
- 佣兵可装备盾牌 / Mercenaries can equip shields
- 德鲁伊毒素伤害上限提升 50% / Druid poison damage ceiling +50%

---

## 安装 / Installation

**中文**

1. 安装 [D2RLoader](https://d2rloader.net) 1.3.1 或更高版本到游戏目录
2. 将本模组解压到 `Diablo II Resurrected\mods\`，确保目录结构为 `mods\shu\shu.mpq`
3. 启动 `D2RLoader.exe`，在设置中选择默认模组为 `shu`
4. **首次使用前请备份存档**（见下方存档兼容性说明）

**English**

1. Install [D2RLoader](https://d2rloader.net) 1.3.1 or newer into your game directory
2. Extract this mod into `Diablo II Resurrected\mods\` so the structure is `mods\shu\shu.mpq`
3. Launch `D2RLoader.exe` and set the default mod to `shu`
4. **Back up your saves before first use** (see save compatibility below)

---

## ⚠️ 存档兼容性 / Save compatibility

**中文：本模组使用 `extended` 存档格式。在切换回原版或其他模组之前，请务必备份角色存档，否则可能无法读回。**

**English: This mod uses the extended save format. Back up your characters before switching back to vanilla or another mod, or they may become unreadable.**

**存档位置 / Save location:**
`%USERPROFILE%\Saved Games\Diablo II Resurrected\`

---

## 第三方组件 / Third-party components

**本模组打包分发了以下第三方 D2RLoader 插件。它们由各自作者开发，版权归原作者所有，此处仅为整合分发，遵循原始许可条款。**

**This mod bundles the following third-party D2RLoader plugins. Each is developed and owned by its respective author and is redistributed here as part of an integrated package, subject to the original terms.**

| 插件 / Plugin | 版本 / Version | 作者 / Author |
| --- | --- | --- |
| Bind And Summon | 1.4.4-embedded110 | yinyin333333 |
| Multi Mercenary | 0.4.11 | yinyin333333 |
| Monster Display | 1.5.8-altf4-teardown-fix | yinyin333333 |
| RuffnecKk MapSense | 2.1.1 | RuffnecKk |
| RuffnecKkMapSenseMapgen.exe | （MapSense 组件 / MapSense component） | RuffnecKk |

**如果你希望只使用本模组自身的改动，可以删除 `shu\d2rloader\plugins\` 下的插件文件，并在 `shu\d2rloader\config\` 中移除对应配置。**

**If you prefer to use only this mod's own changes, delete the plugin files under `shu\d2rloader\plugins\` and remove the matching configs under `shu\d2rloader\config\`.**

### 插件功能说明 / What each plugin does

- **Bind And Summon** — 让束缚恶魔与召唤物在退出游戏后保留 / persists bound demons and summons across sessions
- **Multi Mercenary** — 支持多个佣兵 / support for multiple mercenaries
- **Monster Display** — 怪物信息显示增强 / enhanced monster information display
- **RuffnecKk MapSense** — 地图与小地图增强 / automap and minimap enhancements

---

## 兼容性 / Compatibility

| 项目 / Item | 版本 / Version |
| --- | --- |
| Diablo II: Resurrected | 3.1.2（build 92198） |
| D2RLoader | 1.3.1 或更高 |
| 存档格式 / Save format | extended |

**注意：本模组依赖 3.1.x 的数据表结构。游戏大版本更新后可能需要重新适配。**

**Note: this mod depends on the 3.1.x data table structure and may need adaptation after major game updates.**

---

## 已知限制 / Known limitations

**中文**

1. **克隆版束缚恶魔的恶魔不会存入存档** —— `BindAndSummon` 插件按技能名识别，只对术士原版生效。其余七个职业每次进游戏需重新束缚。
2. **佣兵面板只显示 3 个技能图标** —— 这是界面限制，技能本身（最多 5~6 个）全部生效。
3. **部分技能图标为借用** —— 数据层无法为新技能提供专属图标，只能指向同职业图标集中语义最接近的一格。

**English**

1. **Bound demons from cloned skills do not persist.** The BindAndSummon plugin identifies skills by name and only recognizes the Warlock's original. The other seven classes must re-bind each session.
2. **The mercenary panel shows only 3 skill icons.** This is a UI limit; all skills (up to 5–6) are active.
3. **Some skill icons are borrowed.** The data layer cannot supply new icons, so cloned skills point to the closest existing icon in the same class icon sheet.

---

## 致谢 / Credits

- **yinyin333333** — D2RLoader 本体及多个插件
- **RuffnecKk** — MapSense 地图增强
- **D2RLoader 社区** — 插件 SDK 与文档

---

## 联系 / Contact

- GitHub: [@daiyuanjian183](https://github.com/daiyuanjian183)
- 问题反馈请使用 [Issues](../../issues)

---

## 免责声明 / Disclaimer

**本模组为玩家自制（fan-made）内容，与 Blizzard Entertainment 无任何关联，未获其授权或认可。使用本模组需要你拥有合法的《暗黑破坏神 2：重制版》游戏副本。本模组不包含任何 Blizzard 的原始游戏资源。**

*This is fan-made content, not affiliated with, authorized, or endorsed by Blizzard Entertainment. Using it requires a legitimate copy of Diablo II: Resurrected. This mod contains no original Blizzard game assets.*
