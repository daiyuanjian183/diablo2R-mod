# shu mod 备份

## 2026-11-16 · 修正「誓约 / Oath」百科显示 0%

### 问题
百科里誓约的第一条属性显示成「0% 几率在击中时施放20级骨灵」，
实际官方数据是 **30%**。

原因是颜色码把数字吃掉了：

```
原文  ÿc30% 几率在击中时施放20级骨灵
解析  ÿc3（颜色码） + "0%"   → 显示 0%
正确  ÿc330%  → ÿc3（颜色码） + "30%"
```

### 修改
| 文件 | 键 | 改动 |
| --- | --- | --- |
| `npcs-3.2.json` | `jghelp50444runewordtooltipOath` | `ÿc30%` → `ÿc330%` |
| `npcs-guofu.json` | `jghelp50444runewordtooltipOath` | `ÿc30%` → `ÿc330%` |

两个文件分别是：
- `npcs-3.2.json`：3.2 单机版 shu 的 `Data/local/lng/strings/npcs.json`
- `npcs-guofu.json`：国服版 shu 的同名文件

### 恢复方法
把对应文件覆盖回 `mods/shu/shu.mpq/Data/local/lng/strings/npcs.json`，重启游戏即可。

### 顺带检查
- yj mod 的誓约说明原本就是正确的 `ÿc330%`
- 全库扫描「ÿc3 后直接跟 0%」的情况：只有 shu 的这两处
