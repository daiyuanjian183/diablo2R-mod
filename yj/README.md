# yj mod（基于 JG-MOD 的覆盖层）

国服《暗黑破坏神2：重制版》用的数据/界面 mod。整体结构与 **JG-MOD** 相同，
在 jg 的基础上只改动了 9 个文件。

## 这个目录是什么

GitHub 里**不存 300 MB 的完整 mod**（体积太大），只存相对 jg 的差异文件。
完整包请自行用「jg + 本目录覆盖」生成，或用 Releases 里的打包版本。

## 相对 jg 改动的文件（9 个）

| 文件 | 改动 |
| --- | --- |
| `Data/Local/Lng/Strings/npcs.json` | MOD 信息页改为 YJ-MOD；永恒百科说明同步 3.4；其它页新增「第16赛季暗金调整」区块 |
| `Data/global/dataversionbuild.txt` | 93854 → **95039**（与国服 3.4 客户端对齐，避免启动警告） |
| `Data/global/ui/layouts/otherpanelhd.json` | 新增「第16赛季暗金调整（13件）」区块（标题 + 悬停列表） |
| `Data/global/excel/sounds.txt` | 高号符文掉落音效调大：`high_rune24~33` 音量/优先级拉满、改为 2D 不衰减 |
| `Data/global/ui/layouts/checknewmodhd.json` | 「查看MOD最新版本」按钮指向本项目 GitHub Releases |
| `Data/global/ui/layouts/linkmaxsockhd.json` | 去掉跳转 jg 踩蘑菇网站的链接 |
| `modinfo.json` | `name=yj`，`savepath=../` |

## 如何生成完整 yj

```text
1. 复制 mods/jg 整个文件夹 → mods/yj
2. 把本目录下的 Data/ 与 modinfo.json 覆盖进去
3. 启动参数：-mod yj -txt -assettestmode 1
```

## 数据范围

与 jg 相同，包含 9 张表：`armor / weapons / levels / monstats2 / objects /
overlay / sounds / states / levelgroups`。

**不包含**：`runes / gems / uniqueitems / monstats / treasureclassex`
（即不修改符文之语配方、宝石属性、独特物品、怪物属性与掉落概率）。

## 功能

- 怪物与精英头顶光源、危险怪物感叹号标识
- 掉落大号符文时的特殊提示音
- 关键路口方向指引
- 百科查询（符文之语 / 火眼金睛 / 配方手工 / 其它）
- 储藏箱符文之语标签、符文升级标签、自动合成
- 权冠地面投影、可拍卖物品提示
- 其它页新增「第16赛季暗金调整」说明

## 说明

- 本 mod 不改符文之语、宝石、独特物品与掉落数据，官方 3.4 内容保持原样
- 联机使用任何客户端文件修改都有风险，请自行判断
- 与 jg / shu 等其它 mod 不要同时启用

## 工具脚本

`tools/` 下是生成这些改动的脚本（Python），供以后调整时复用。
