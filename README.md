# shu

**涓€涓潰鍚戙€婃殫榛戠牬鍧忕 2锛氶噸鍒剁増銆嬬殑娣卞害鐜╂硶鏀归€犳ā缁?*
*A deep gameplay overhaul for Diablo II: Resurrected*

[![D2RLoader](https://img.shields.io/badge/D2RLoader-1.3.1-blue)](https://d2rloader.net)
[![D2R](https://img.shields.io/badge/D2R-3.2.92777-green)]()
[![Version](https://img.shields.io/badge/version-0.6.17-orange)]()

---

## 绠€浠?/ Overview

**涓枃**

shu 鏄竴涓互"閲嶅仛浣ｅ叺浣撶郴"鍜?鎵撻€氭姉鎬х┛閫?涓烘牳蹇冪殑澶у瀷鐜╂硶妯＄粍銆傚畠涓嶆敼鍙樻父鎴忕殑鏁翠綋妗嗘灦锛岃€屾槸閲嶅啓浜嗕簲澶т剑鍏电殑鎶€鑳芥瀯鎴愶紝骞朵负鍏釜浼ゅ绯诲埆鎻愪緵浜嗗彲鎴愰暱銆佸彲鐮村厤鐨勬姉鎬х┛閫忔墜娈点€?

**English**

shu is a large-scale gameplay overhaul built around two ideas: rebuilding the five mercenary archetypes from the ground up, and giving every damage type a scalable path through enemy resistances.

---

## 鈿狅笍 浠呴檺鍗曟満浣跨敤 / Offline use only

> **鏈ā缁勪粎閫傜敤浜庣绾匡紙鍗曟満锛夋ā寮忋€?*
>
> **璇峰嬁鍦?Battle.net 瀹樻柟鏈嶅姟鍣ㄤ笂浣跨敤 鈥斺€?鍖呮嫭澶╂銆佸叕寮€娓告垙銆佺粍闃熴€佷互鍙婁换浣曡仈缃戝灞€銆侱2RLoader 浼氫慨鏀规父鎴忓唴瀛樹笌鏁版嵁琛紝瀹樻柟鏈嶅姟鍙兘妫€娴嬪埌寮傚父骞跺璐﹀彿閲囧彇澶勭悊鎺柦銆傝繖涓闄╃敱浣跨敤鑰呰嚜琛屾壙鎷呫€?*

> **This mod is for offline / single-player use only.**
>
> **Do not use it on official Battle.net servers 鈥?including ladder, public games, parties, or any online session. D2RLoader alters game memory and data tables; the official service may detect this and take action against your account. You assume this risk yourself.**

---

## 鈿狅笍 鍗囩骇蹇呭仛锛氶噸鏂扮紪璇?/ Recompile after updating

> **姣忔瑕嗙洊瀹夎鏂扮増鏈悗锛屽繀椤婚噸鏂扮紪璇戜竴娆℃暟鎹〃銆?* 鏈ā缁勫嚑涔庢瘡涓増鏈兘鍦ㄦ敼 `skills` / `skilldesc` 绛夋妧鑳借〃锛岃烦杩囩紪璇戜細璁╂父鎴忕户缁鍙栨棫 BIN锛岃〃鐜颁负銆屾煇浜涙妧鑳芥秷澶便€嶃€孨PC 鍔熻兘寮傚父銆嶈繖绫荤湅浼奸殢鏈虹殑闂銆?

> **After overwriting with a new version, you MUST recompile.** Almost every release changes `skills` / `skilldesc`; skipping it leaves the game reading stale BIN files, which shows up as "some skills are missing" or "NPC interactions broken".

**鎿嶄綔姝ラ / Steps**

1. 鍚姩娓告垙锛岃繘鍒颁富鑿滃崟 / Launch the game to the main menu
2. 鎸?`Ctrl + \`` 鎵撳紑鎺у埗鍙?/ Press `Ctrl + \`` to open the console
3. 杈撳叆骞跺洖杞?/ Type and press Enter锛歚d2rl compile shu`
4. 绛夊緟鍑虹幇缂栬瘧瀹屾垚鎻愮ず / Wait for the compile-finished message
5. **瀹屽叏閫€鍑烘父鎴?*锛堝叧闂繘绋嬶紝涓嶆槸鍥炰富鑿滃崟锛? **Fully quit the game** (close the process, not just the menu)
6. 閲嶆柊鍚姩娓告垙 / Launch the game again

**濡傛灉缂栬瘧鎶ラ敊锛屾垨缂栬瘧鍚庝粛涓嶆甯?/ If compiling fails or problems persist**

鎶?`mods\shu\shu.mpq\Data\global\excel\` 涓嬫墍鏈?`*.bin` 鏂囦欢绉诲埌鍒锛堜緥濡傛柊寤?`_binbak` 鏂囦欢澶癸級锛屽啀杩涙父鎴忊€斺€旀鏃舵父鎴忎細鐩存帴璇诲彇 TXT锛涚‘璁ゆ甯稿悗閲嶆柊鎵ц涓€娆?`d2rl compile shu` 鐢熸垚 BIN銆?

Move every `*.bin` out of `mods\shu\shu.mpq\Data\global\excel\` (e.g. into a new `_binbak` folder) and start the game 鈥?it will read the TXT files directly. Once confirmed working, run `d2rl compile shu` again to regenerate the BINs.

---

## 鏍稿績鐗规€?/ Features

### 涓€銆佷簲澶т剑鍏靛叏闈㈤噸鍋?/ Five mercenaries reworked

| 骞?/ Act | 浣ｅ叺 / Mercenary | 鏍稿績鏈哄埗 / Core mechanics |
| --- | --- | --- |
| 1 | 缃楁牸灏勬墜 / Rogue Scout | 鍐呰绱㈡晫 + 榄旀硶绠?/ 杩炵彔绠?+ 鏁戣祹 / 鐙傜儹鍏夌幆 |
| 2 | 娌欐紶浣ｅ叺 / Desert Mercenary | 鎴冲埡 + 鍋峰彇鐢熷懡璇呭拻 + 鍏郴鍏夌幆 + 30% 鍘嬬鎬ф墦鍑?|
| 3 | 閾佺嫾娉曞笀 / Eastern Sorceror | 鎷晳鍏夌幆 + 浜旀妧鑳?+ 瀵掑啺鎶ょ敳 + 鍏冪礌绮鹃€?|
| 4 | 姝荤伒娉曞笀 / Act IV Necromancer | 瀹″垽鍏夌幆 + 璇呭拻 + 楠ㄧ郴杈撳嚭 + 鐩剧墝妲?|
| 5 | 閲庤洰浜?/ Barbarian | 涓撴敞鍏夌幆 + 鎴樻枟浣撳埗 + 鐙傛垬澹?+ 鍏ㄨ澶囨Ы |

**鎵€鏈変剑鍏靛彲瑁呭 10 涓墿鍝佹Ы浣嶏紝鍚浘鐗屻€?*
*Every mercenary can equip up to 10 item slots, shields included.*

### 浜屻€佸叚绯绘姉鎬х┛閫?/ Resistance pierce on six damage types

| 绯?/ Type | 鎶€鑳?/ Skill | 鏁堟灉 / Effect |
| --- | --- | --- |
| 鐏?/ Fire | 鐏劙鏀厤銆佹瘉澶╃伃鍦?| 姣忕骇 -2% 鏁屼汉鐏姉 + 鐮寸伀鍏嶇柅 |
| 鍐?/ Cold | 椋撻 | 姣忕骇 -2% 鏁屼汉鍐版姉 + 鐮村啺鍏嶇柅 |
| 鐢?/ Lightning | 闂數鏀厤 | 姣忕骇 -2% 鏁屼汉鐢垫姉 + 鐮寸數鍏嶇柅 |
| 姣?/ Poison | 鍓ф瘨钘よ敁 | 姣忕骇 -2% 鏁屼汉姣掓姉 + 鐮存瘨鍏嶇柅 |
| 鐗╃悊 / Physical | 閽㈤搧涔嬭偆 | 姣忕骇 -2% 鏁屼汉鐗╂姉 + 鐮寸墿鍏嶇柅 |

### 涓夈€佸叓澶ц亴涓氭潫缂氭伓榄?/ Bind Demon for all classes

**鏈＋鐨勬潫缂氭伓榄斾綔涓虹嫭绔嬫妧鑳芥彁渚涚粰鍏朵綑涓冧釜鑱屼笟锛屼綅浜庡悇鑷妧鑳芥爲绗?6 琛岋紙绛夌骇 30 瑙ｉ攣锛夛紝鍏变韩鍚屼竴濂楁伓榄旂被鍨嬨€?*

*The Warlock's Bind Demon is provided as an independent skill for the other seven classes, on row 6 of each skill tree (unlocks at level 30). All variants share the same demon type.*

### 鍥涖€佸叾浠栨敼鍔?/ Other changes

- 鑳屽寘鎵╁鑷?13 脳 8 / Inventory expanded to 13 脳 8
- 閴村畾涔︺€佷紶閫佷功鍫嗗彔涓婇檺 100 / Tomes stack to 100
- 浣ｅ叺鍙澶囩浘鐗?/ Mercenaries can equip shields
- 寰烽瞾浼婃瘨绱犱激瀹充笂闄愭彁鍗?50% / Druid poison damage ceiling +50%

---

## 瀹夎 / Installation

**涓枃**

1. 瀹夎 [D2RLoader](https://d2rloader.net) 1.3.1 鎴栨洿楂樼増鏈埌娓告垙鐩綍
2. 灏嗘湰妯＄粍瑙ｅ帇鍒?`Diablo II Resurrected\mods\`锛岀‘淇濈洰褰曠粨鏋勪负 `mods\shu\shu.mpq`
3. 鍚姩 `D2RLoader.exe`锛屽湪璁剧疆涓€夋嫨榛樿妯＄粍涓?`shu`
4. **棣栨浣跨敤鍓嶈澶囦唤瀛樻。**锛堣涓嬫柟瀛樻。鍏煎鎬ц鏄庯級
5. **浠呭湪绂荤嚎妯″紡涓嬭繍琛?鈥斺€?涓嶈甯︾潃杩欎釜妯＄粍杩?Battle.net 瀹樻柟鏈嶅姟鍣?*

**English**

1. Install [D2RLoader](https://d2rloader.net) 1.3.1 or newer into your game directory
2. Extract this mod into `Diablo II Resurrected\mods\` so the structure is `mods\shu\shu.mpq`
3. Launch `D2RLoader.exe` and set the default mod to `shu`
4. **Back up your saves before first use** (see save compatibility below)
5. **Run offline only 鈥?never connect to official Battle.net with this mod loaded**

---

## 鈿狅笍 瀛樻。鍏煎鎬?/ Save compatibility

**涓枃锛氭湰妯＄粍浣跨敤 `extended` 瀛樻。鏍煎紡銆傚湪鍒囨崲鍥炲師鐗堟垨鍏朵粬妯＄粍涔嬪墠锛岃鍔″繀澶囦唤瑙掕壊瀛樻。锛屽惁鍒欏彲鑳芥棤娉曡鍥炪€?*

**English: This mod uses the extended save format. Back up your characters before switching back to vanilla or another mod, or they may become unreadable.**

**瀛樻。浣嶇疆 / Save location:**
`%USERPROFILE%\Saved Games\Diablo II Resurrected\`

---

## 绗笁鏂圭粍浠?/ Third-party components

**鏈ā缁勬墦鍖呭垎鍙戜簡浠ヤ笅绗笁鏂?D2RLoader 鎻掍欢銆傚畠浠敱鍚勮嚜浣滆€呭紑鍙戯紝鐗堟潈褰掑師浣滆€呮墍鏈夛紝姝ゅ浠呬负鏁村悎鍒嗗彂锛岄伒寰師濮嬭鍙潯娆俱€?*

**This mod bundles the following third-party D2RLoader plugins. Each is developed and owned by its respective author and is redistributed here as part of an integrated package, subject to the original terms.**

| 鎻掍欢 / Plugin | 鐗堟湰 / Version | 浣滆€?/ Author |
| --- | --- | --- |
| Bind And Summon | 1.4.4-embedded110 | yinyin333333 |
| Multi Mercenary | 0.4.11 | yinyin333333 |
| Monster Display | 1.5.8-altf4-teardown-fix | yinyin333333 |
| RuffnecKk MapSense | 2.1.1 | RuffnecKk |
| RuffnecKkMapSenseMapgen.exe | 锛圡apSense 缁勪欢 / MapSense component锛?| RuffnecKk |

**濡傛灉浣犲笇鏈涘彧浣跨敤鏈ā缁勮嚜韬殑鏀瑰姩锛屽彲浠ュ垹闄?`shu\d2rloader\plugins\` 涓嬬殑鎻掍欢鏂囦欢锛屽苟鍦?`shu\d2rloader\config\` 涓Щ闄ゅ搴旈厤缃€?*

**If you prefer to use only this mod's own changes, delete the plugin files under `shu\d2rloader\plugins\` and remove the matching configs under `shu\d2rloader\config\`.**

### 鎻掍欢鍔熻兘璇存槑 / What each plugin does

- **Bind And Summon** 鈥?璁╂潫缂氭伓榄斾笌鍙敜鐗╁湪閫€鍑烘父鎴忓悗淇濈暀 / persists bound demons and summons across sessions
- **Multi Mercenary** 鈥?鏀寔澶氫釜浣ｅ叺 / support for multiple mercenaries
- **Monster Display** 鈥?鎬墿淇℃伅鏄剧ず澧炲己 / enhanced monster information display
- **RuffnecKk MapSense** 鈥?鍦板浘涓庡皬鍦板浘澧炲己 / automap and minimap enhancements

---

## 鍏煎鎬?/ Compatibility

| 椤圭洰 / Item | 鐗堟湰 / Version |
| --- | --- |
| Diablo II: Resurrected | 3.1.2锛坆uild 92198锛?|
| D2RLoader | 1.3.1 鎴栨洿楂?|
| 瀛樻。鏍煎紡 / Save format | extended |

**娉ㄦ剰锛氭湰妯＄粍渚濊禆 3.1.x 鐨勬暟鎹〃缁撴瀯銆傛父鎴忓ぇ鐗堟湰鏇存柊鍚庡彲鑳介渶瑕侀噸鏂伴€傞厤銆?*

**Note: this mod depends on the 3.1.x data table structure and may need adaptation after major game updates.**

---

## 宸茬煡闄愬埗 / Known limitations

**涓枃**

1. **鍏嬮殕鐗堟潫缂氭伓榄旂殑鎭堕瓟涓嶄細瀛樺叆瀛樻。** 鈥斺€?`BindAndSummon` 鎻掍欢鎸夋妧鑳藉悕璇嗗埆锛屽彧瀵规湳澹師鐗堢敓鏁堛€傚叾浣欎竷涓亴涓氭瘡娆¤繘娓告垙闇€閲嶆柊鏉熺細銆?
2. **浣ｅ叺闈㈡澘鍙樉绀?3 涓妧鑳藉浘鏍?* 鈥斺€?杩欐槸鐣岄潰闄愬埗锛屾妧鑳芥湰韬紙鏈€澶?5~6 涓級鍏ㄩ儴鐢熸晥銆?
3. **閮ㄥ垎鎶€鑳藉浘鏍囦负鍊熺敤** 鈥斺€?鏁版嵁灞傛棤娉曚负鏂版妧鑳芥彁渚涗笓灞炲浘鏍囷紝鍙兘鎸囧悜鍚岃亴涓氬浘鏍囬泦涓涔夋渶鎺ヨ繎鐨勪竴鏍笺€?

**English**

1. **Bound demons from cloned skills do not persist.** The BindAndSummon plugin identifies skills by name and only recognizes the Warlock's original. The other seven classes must re-bind each session.
2. **The mercenary panel shows only 3 skill icons.** This is a UI limit; all skills (up to 5鈥?) are active.
3. **Some skill icons are borrowed.** The data layer cannot supply new icons, so cloned skills point to the closest existing icon in the same class icon sheet.

---

## 鑷磋阿 / Credits

- **yinyin333333** 鈥?D2RLoader 鏈綋鍙婂涓彃浠?
- **RuffnecKk** 鈥?MapSense 鍦板浘澧炲己
- **D2RLoader 绀惧尯** 鈥?鎻掍欢 SDK 涓庢枃妗?

---

## 鑱旂郴 / Contact

- GitHub: [@daiyuanjian183](https://github.com/daiyuanjian183)
- 闂鍙嶉璇蜂娇鐢?[Issues](../../issues)

---

## 鍏嶈矗澹版槑 / Disclaimer

**鏈ā缁勪负鐜╁鑷埗锛坒an-made锛夊唴瀹癸紝涓?Blizzard Entertainment 鏃犱换浣曞叧鑱旓紝鏈幏鍏舵巿鏉冩垨璁ゅ彲銆備娇鐢ㄦ湰妯＄粍闇€瑕佷綘鎷ユ湁鍚堟硶鐨勩€婃殫榛戠牬鍧忕 2锛氶噸鍒剁増銆嬫父鎴忓壇鏈€傛湰妯＄粍涓嶅寘鍚换浣?Blizzard 鐨勫師濮嬫父鎴忚祫婧愩€?*

*This is fan-made content, not affiliated with, authorized, or endorsed by Blizzard Entertainment. Using it requires a legitimate copy of Diablo II: Resurrected. This mod contains no original Blizzard game assets.*

---

## 寮€鍙戝熀鍑?/ Development Baseline

**閿佸畾鐗堟湰锛欴iablo II: Resurrected 3.2.92777**

| 椤圭洰 | 鍊?|
| --- | --- |
| 娓告垙鐗堟湰 | 3.2.92777 |
| 鏁版嵁鐗堟湰鏍囪 | `Data/global/dataversionbuild.txt` = 92777 |
| D2RLoader | 1.3.1 |
| 瀛樻。鏍煎紡 | extended |

寮€鍙戦搧寰嬶細

1. 涓€涓増鏈竴涓畨瑁咃紝3.1.2锛?2198锛夌幆澧冨凡閫€褰?
2. root 琛ㄤ笌 `base/` 琛ㄥ繀椤诲悓鐗堟湰锛宍base/` 蹇呴』鏄?3.2.92777 鍘熺増
3. 绂佹璺ㄧ増鏈嫹琛紙3.1 琛ㄦ嫹杩?3.2 浼氶€犳垚闅愭€ф崯鍧忥級
4. 鏀硅〃鍚庡繀椤婚噸鏂扮紪璇戯細娓告垙鍐?`d2rl compile shu`
5. 鎻愪氦鍓嶆鏌?`dataversionbuild.txt` 鏄惁涓?92777

鐗堟湰鍘嗗彶锛?

| 鐗堟湰 | 鍩哄噯 | 鐘舵€?|
| --- | --- | --- |
| 0.6.01 ~ 0.6.08 | 3.1.2 (92198) | 宸插彂甯冿紝宸插喕缁?|
| 0.6.17 | 3.2.92777 | 褰撳墠鐗堟湰 |

---
