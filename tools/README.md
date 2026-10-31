# tools

维护脚本目录。**不参与 mod 运行**，只用来生成数据补丁与文档。

| 脚本 | 作用 | 用法 |
|---|---|---|
| `_reroll_stone_patch.py` | 生成 v0.6.06「洗练石」的三处数据改动：`misc.txt`（新增物品行）、`cubemain.txt`（重铸配方）、`item-names.json`（字符串） | `python _reroll_stone_patch.py` 干跑预览；`--apply` 才写入，写入前自动 `.bak` 备份 |
| `_build_changelog_0606.py` | 从零生成 v0.6.06 更新日志 docx，排版沿用 0.6.05 | `python _build_changelog_0606.py` |

## 使用前提

- 两个脚本里的 `MOD` / `REPO` / `WS` 都是**作者本机绝对路径**，换机器必须先改
- `_build_changelog_0606.py` 依赖 `python-docx`
- `_reroll_stone_patch.py` 会直接改写 `mods/shu/shu.mpq/Data/global/excel/` 下的表，**改完必须让游戏重新编译（`d2rl compile shu`）才生效**

## 关于洗练石的四个坑

这些是 v0.6.06 开发中实际踩到的，脚本注释里也重复写了：

1. **`type` 不能用 `misc`** —— `itemtypes.txt` 里 Miscellaneous 的 `StorePage` 为空，商人永远不会进货。必须用挂 `misc` 商店页的类型（`elix` / `key` / `scro` / `book` / `gem`）。
2. **`usetype` 以 input 1 为模板** —— 把洗练石放在 input 1，游戏会去生成「暗金版洗练石」，生成失败后两个输入都被消耗，装备直接消失。装备必须在 input 1。
3. **自制物品代码没有图标映射** —— D2R 的物品图标由引擎内部「代码 → HD 模型」映射决定，`invfile` 填什么都不管用，显示空白。只能复用原版代码（当前复用 `elx`，即原版闲置的 Elixir）。
4. **excel 表必须 UTF-8 无 BOM** —— 带 BOM 会让表头第一列变成 `\ufeffname`，编译后整列失效（v0.6.05 的暗金名字问题就是它）。

## 随机孔数的写法

```text
output = "usetype,<品质>"
mod 1  = sock
mod 1 min = 1
mod 1 max = 6
```

不需要 `,mod` 后缀。孔数上限由底材与物品等级自动截断（戒指/项链/珠宝/护身符上限为 0）。
