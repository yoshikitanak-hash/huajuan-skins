# 画作来源 · Credits & Provenance

## 制作分工

| 主题 | 画面 | 主题设计与制作 |
| --- | --- | --- |
| 纸墨 / Paper & Ink | Claude Code 用程序生成的矢量画：水墨远山、朱日、飞鸟、小舟、流雾、纸纹 | Claude Code |
| 夜航 | Claude Code 用程序生成的矢量画：星空、新月、云海、河湾、芦苇、萤火、提灯的小船 | Claude Code |
| 星笺 | Codex 用 OpenAI 图像生成画出 | Claude Code |
| 天体 | Codex 用 OpenAI 图像生成画出 | Claude Code |
| 青林 | Codex 用 OpenAI 图像生成画出 | Claude Code |
| 雾湖来信 | Codex 用 OpenAI 图像生成画出 | Claude Code |

星笺、天体、青林、雾湖来信的方向由项目发起人决定：发起人提供参考素材，Codex 先画多张概念稿，发起人挑选后，再由 Claude Code 做成主题。

## AI 生成说明

星笺、天体、青林、雾湖来信的画作由 AI 生成。每套的完整生成描述（prompt）放在 `themes/<主题>/prompt.txt`。

- 参考素材只用来确定氛围、光色和笔触方向，没有复制、描摹或放进仓库。画作都是新构图，不含任何现成作品、角色或标志。
- 按 OpenAI 使用条款，生成内容的权利归使用者所有。本项目以 CC BY 4.0 发布这些画作。条款不保证生成内容的独占性，也不保证各地都受版权保护。

## 制作中的处理

- **星笺、天体**：先从生成的画作中切出四角装饰，重新排成 16:9，左侧装饰右移避开侧栏。这样收起侧栏时，左侧会露出装饰的直线切边和一片空白。于是再请 Codex 以这一版为底稿向左续画，让左上、左下的装饰自然延伸到窗口左缘。续画的描述见 `themes/<主题>/prompt-extend.txt`；输出 1672×941，等比放大到 2400×1350。
- **青林**：从 2400×1500 裁成 16:9。
- **雾湖来信**：原画 1672×941，水平镜像，让小船落在右下、输入框上方；等比放大到 2400×1350；左侧叠一层渐散的晨雾，让侧栏文字在画面上也看得清。
- **纸墨、夜航**：矢量场景直接渲染成 2400×1350。

## 平台

主题运行在 [Codex Dream Skin](https://github.com/Fei-Away/Codex-Dream-Skin)（MIT）上，它也是本项目的灵感来源。本仓库没有包含或修改它的代码。

---

**English summary.** Paper & Ink and Night are procedurally generated vector scenes by Claude Code. Folio, Celestial, Grove and Mist Lake Letter are AI-generated paintings made by Codex with OpenAI image generation; their prompts are in `themes/<theme>/prompt.txt`. For Folio and Celestial, Codex also extended the left-hand decorations to the window edge (`prompt-extend.txt`). The project's initiator chose each direction from reference material, which was used only for mood and was not copied or included. Claude Code designed and built all seven themes, including the recomposition steps listed above.
