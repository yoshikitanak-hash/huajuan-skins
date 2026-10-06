# 画卷 Huajuan

七套艺术主题（另有四套英文版），让 Codex 桌面版的工作区变成一幅画。需要配合 [Codex Dream Skin](https://github.com/Fei-Away/Codex-Dream-Skin) 使用：下载主题包，在 Dream Skin 里导入，一键换肤。

[English](#english)

> 非官方社区作品，与 OpenAI 没有隶属或背书关系。“Codex”只用于说明适用的软件。

![雾湖来信，真机截图](previews/real/mistlake-home.jpg)

## 主题

| | 主题 | 首页文字 | 风格 |
| --- | --- | --- | --- |
| <img src="previews/paper.jpg" width="240"> | **纸墨** | 研墨已备，从这里落笔 | 象牙纸、水墨远山、一轮朱日 |
| <img src="previews/folio.jpg" width="240"> | **星笺** | 纸页已展，等一个念头落下 | 米白纸面，橙红、灰绿、雾蓝的几何色块，一只蜻蜓 |
| <img src="previews/celestial.jpg" width="240"> | **天体** | 远处有星，眼前有一行 | 古典蓝米配色、月相、星图、植物与小鸟 |
| <img src="previews/grove.jpg" width="240"> | **青林** | 风过林间，念头渐渐清明 | 阳光下的林间溪畔，远处小路上的背影 |
| <img src="previews/night.jpg" width="240"> | **夜航** | 灯还亮着，思绪慢慢靠岸 | 深色主题：星空、新月、萤火、提灯的小船 |
| <img src="previews/mistlake.jpg" width="240"> | **雾湖来信** | 雾还未散，来信已到 | 晨雾湖面的油画，小船上有人在读信 |

**英文版**：画面和样式与中文版相同，只有名称和首页文字是英文。

| | 主题 | 首页文字 |
| --- | --- | --- |
| <img src="previews/mistlake-en.jpg" width="240"> | **Mist Lake Letter** | The mist lingers. A letter has come. |
| <img src="previews/night-en.jpg" width="240"> | **Night Voyage** | The lamp is still on. Thoughts drift ashore. |
| <img src="previews/grove-en.jpg" width="240"> | **Grove** | Wind through the trees. Thoughts grow clear. |
| <img src="previews/paper-en.jpg" width="240"> | **Paper & Ink** | The ink is ready. Begin here. |

表中预览图是用真实背景和配色画的示意，界面细节以实际效果为准。

### 真机截图

Windows 上的 Codex 桌面版，界面语言为繁体中文。截图里首页的主题名小标签已被作者本机的增强样式隐藏（见下方「说明」）。

| 主题 | 首页 | 对话 |
| --- | --- | --- |
| 雾湖来信 | <img src="previews/real/mistlake-home.jpg" width="400"> | <img src="previews/real/mistlake-chat.jpg" width="400"> |
| 夜航 | <img src="previews/real/night-home.jpg" width="400"> | <img src="previews/real/night-chat.jpg" width="400"> |
| 青林 | <img src="previews/real/grove-home.jpg" width="400"> | <img src="previews/real/grove-chat.jpg" width="400"> |
| 星笺 | <img src="previews/real/folio-home.jpg" width="400"> | <img src="previews/real/folio-chat.jpg" width="400"> |
| 天体 | <img src="previews/real/celestial-home.jpg" width="400"> | <img src="previews/real/celestial-chat.jpg" width="400"> |
| 纸墨 | <img src="previews/real/paper-home.jpg" width="400"><br><sub>首页的楷体标题来自作者本机的增强样式，默认显示系统字体</sub> | <img src="previews/real/paper-chat.jpg" width="400"> |

## 安装

1. 安装并启动 [Codex Dream Skin](https://github.com/Fei-Away/Codex-Dream-Skin)。本项目在 v1.5.19 上制作和测试。
2. 在 [Releases](https://github.com/yoshikitanak-hash/huajuan-skins/releases/latest) 页面（或 [`packages/`](packages/) 目录）下载想要的主题包，比如 `mistlake.zip`。不需要解压。
3. 右键任务栏右下角的 Dream Skin 托盘图标，选「导入主题 ZIP…」，选中刚下载的包。
4. 在托盘菜单里选择这个主题。

| 主题 | 主题包 |
| --- | --- |
| 纸墨 | `paper.zip` |
| Paper & Ink | `paper-en.zip` |
| 星笺 | `folio.zip` |
| 天体 | `celestial.zip` |
| 青林 | `grove.zip` |
| 夜航 | `night.zip` |
| 雾湖来信 | `mistlake.zip` |
| Mist Lake Letter | `mistlake-en.zip` |
| Night Voyage | `night-en.zip` |
| Grove（英文） | `grove-en.zip` |

每个包旁边的 `.sha256` 文件是校验值，可以用来确认下载完整。

## 说明

- 主题包是 Dream Skin 的标准格式，dreamskin.cc 的工作室也能直接导入。包里有 `theme.json`（名称、文字、配色）、`theme.css`（样式）、一张背景图，以及 `manifest.json`（版本、许可、AI 生成说明、文件校验值）和 `LICENSE.txt`。样式都符合 Dream Skin 的安全样式规则。`themes/` 目录里是同样的主题文件，方便直接查看；`tools/make_official_packages.py` 用来重新打包。
- 背景是 16:9 的宽图，Dream Skin 会让画面铺满整个窗口，侧栏为半透明。
- 对话字体沿用 Codex 自带的字体，不另外打包字体。
- 夜航是深色主题。Dream Skin 通常会自动切换 Codex 的深色外观。如果设置页的按钮或下拉框发白，到 Codex 设置的「外观」里手动选深色。
- 主要在 Windows、2560×1440 屏幕上测试。macOS 还没有实测。
- 作者本机另有一层增强样式（例如隐藏首页的主题名小标签），它依赖对 Dream Skin 本地文件的修改，没有收录在这里。不装它，主题照常使用。

## 鸣谢

- **Claude Code**（Anthropic）：主题设计与制作，纸墨、夜航的画面，配色、样式、背景合成与校验。
- **Codex**（OpenAI）：用图像生成画出星笺、天体、青林、雾湖来信的画作，并参与评审与测试。
- **[Codex Dream Skin](https://github.com/Fei-Away/Codex-Dream-Skin)**：灵感来源，也是这些主题运行的平台。有了它，导入一个包就能一键换肤。
- **项目发起人**：提出想法，提供参考素材和审美方向，挑选每一幅画，在真机上逐一试用。

画作来源和生成方式见 [CREDITS.md](CREDITS.md)。

## 许可

- 代码（`theme.css`、`theme.json` 等）：[MIT](LICENSE)。
- 画作（背景图、预览图与截图）：[CC BY 4.0](LICENSE-ART.md)。可以自由使用和改编，请注明出处。

---

## English

**Huajuan (画卷, "painted scroll")**: seven art themes for the Codex desktop app, for use with [Codex Dream Skin](https://github.com/Fei-Away/Codex-Dream-Skin). This is an unofficial community project, not affiliated with or endorsed by OpenAI.

English editions (same art and styling, English name and home-page line):

| Theme | Home-page line | Package |
| --- | --- | --- |
| Mist Lake Letter | The mist lingers. A letter has come. | `mistlake-en.zip` |
| Night Voyage (dark) | The lamp is still on. Thoughts drift ashore. | `night-en.zip` |
| Grove | Wind through the trees. Thoughts grow clear. | `grove-en.zip` |
| Paper & Ink | The ink is ready. Begin here. | `paper-en.zip` |

Chinese editions: Mist Lake Letter, Night, Grove, Paper & Ink, plus Folio and Celestial.

**Install**

1. Install and run Codex Dream Skin (built and tested with v1.5.19).
2. Download a package from [Releases](https://github.com/yoshikitanak-hash/huajuan-skins/releases/latest) (or [`packages/`](packages/)). Keep it zipped.
3. Right-click the Dream Skin tray icon, choose **Import theme ZIP...** and pick the file.
4. Select the theme from the tray menu.

**Notes**

- Packages use Dream Skin's official format (`manifest.json` with licence, AI-provenance and checksums, plus `theme.json`, `theme.css`, one background and `LICENSE.txt`), so they also import into the dreamskin.cc Studio. All styling stays within Dream Skin's safe-CSS rules.
- The backgrounds are 16:9, so Dream Skin shows the art across the whole window behind a translucent sidebar.
- Night is a dark theme. If controls on the settings page look white, set Codex's appearance to dark.
- Tested mainly on Windows at 2560×1440; macOS is untested.

**Credits**

- Claude Code designed and built the themes and drew Paper & Ink and Night.
- Codex generated the paintings for Folio, Celestial, Grove and Mist Lake Letter.
- Codex Dream Skin is the inspiration and the platform.
- The project's initiator came up with the idea, set the art direction and tested every theme.

See [CREDITS.md](CREDITS.md) for provenance.

**License**: code is [MIT](LICENSE); artwork is [CC BY 4.0](LICENSE-ART.md).
