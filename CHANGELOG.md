# 更新日志 / Changelog

本文件记录 shu 模组的版本变更。
*Version history for the shu mod.*

---

## v0.6.10 — 2026-11-03

### 修复 / Fixed

**第五幕野蛮人佣兵无法装备武器**

症状：任何武器拖到佣兵武器格都显示红色，护甲和头盔正常。

根因：`monstats.txt` 中佣兵的左右手物品类型被写成无效值：

| 字段 | 修复前 | 3.2 原版 |
| --- | --- | --- |
| rightArmItemType | afwe | swor |
| leftArmItemType | afwe | swor |
| act5hire2 rightArmItemType | slam | swor |

`afwe` 与 `slam` 在 `itemtypes.txt` 中不存在，引擎匹配不到任何物品，因此所有武器都被拒绝。护甲走 torso 判定，不受影响。

**佣兵可装备全部武器**

将各佣兵右手类型统一改为 `weap`（Weapon 总类），覆盖剑、斧、锤、长柄、长矛、弓、法杖、标枪：

| 佣兵 | 右手 | 左手 |
| --- | --- | --- |
| 第一幕 罗格 | 全部武器 | 标枪类 |
| 第二幕 沙漠 | 全部武器 | 无 |
| 第三幕 铁狼 | 全部武器 | 盾牌 |
| 第四幕 死灵 | 全部武器 | 盾牌 |
| 第五幕 野蛮人 | 全部武器 | 全部武器 |

**恢复佣兵 10 格装备面板**

| 项目 | 修复前 | 修复后 |
| --- | --- | --- |
| `isHireable` 写法 | 数字 `1`（引擎按布尔解析失败） | 布尔 `true` / `false` |
| 槽位数量 | 10 格但部分失效 | 10 格全部可用 |
| `inventory.txt` | 与 UI 不一致 | 与 UI 槽位一一对应 |

佣兵现在可装备：武器（左右手）、盾牌、头盔、护甲、项链、戒指、腰带、手套、靴子。

### 升级说明 / Upgrade

- 本次修改了 `inventory.txt` 与 `monstats.txt`，必须执行 `d2rl compile shu`
- 编译后核对 `Data/global/dataversionbuild.txt` 为 92777

---

## v0.6.09 — 2026-11-02

### 重点 / Highlight

**术士职业修复**

术士此前一放技能就崩溃。根因：`missiles.txt` 中 50 条术士飞弹的函数列为空。

| 字段 | 修复前 | 3.2 原版 |
| --- | --- | --- |
| pCltDoFunc | （空） | 1 |
| pSrvDoFunc | （空） | 1 / 41 |
| pSrvHitFunc | （空） | 41 |
| pSrvDmgFunc | （空） | 0 |

飞弹生成后引擎按空编号调用函数（RIP=0x0）导致崩溃。现已按 3.2 原版补齐 50 条飞弹，并补入 6 条 3.2 新增飞弹、`missilelimit` 状态与 `CompletionTotalRoomsOverride` 列，同时补齐 `warlock` / `submenu` 技能图标目录（游戏需要 9 个，此前只有 7 个）。

### 新增 / New

**封印戒指**：第 4 幕城镇贾梅拉出售，50,000 金币，单独放入方块开启随机暗金戒指（池内 18 种）。

**多佣兵**：携带「冥府乌鸦」可雇佣最多 5 名佣兵，面板左右箭头或 `[` `]` 翻页；护身符需求等级调整为 1 级。

**技能图标重制**：束缚恶魔（7 职业）改为银灰镣铐，支配物理改为银灰破碎护甲板，直接写入各职业 HD 图标图集。

### 3.2 适配 / Compatibility

数据表整体迁移到 3.2（build 92777），204 张表编译 0 失败；`base/` 基准表全部替换为 3.2 原版（89 张）。

### 开发基准 / Baseline

锁定 Diablo II: Resurrected **3.2.92777**，详见仓库 README 与 mod 内《开发基准.md》。

### 已知问题 / Known Issues

- 克隆版束缚恶魔不存入存档，每次进入游戏需重新绑定
- 佣兵面板只显示 3 个技能图标（技能本身全部生效）
- D2RLoader 启动器界面修改设置可能重置插件开关，导致主菜单「缺失的插件」红字

### 升级说明 / Upgrade

- **本版为 3.2 专用**，0.6.08 及以前为 3.1 专用，两者数据表不兼容
- 覆盖安装后必须执行 `d2rl compile shu`
- 编译后核对 `Data/global/dataversionbuild.txt` 为 92777

---

