# ghostty-config

我的 [Ghostty](https://ghostty.org) 终端配置：Catppuccin Latte 亮色主题 + JetBrains Mono 字体，半透明模糊背景，带全局呼出的 quick terminal。

## 内容

```
config.ghostty                  # 主配置(macOS 放到 Application Support)
themes/ink-xuan                 # 可选:水墨·宣纸亮色主题
themes/ink-splash               # 可选:水墨·泼墨暗色主题
backgrounds/gen_ink_shanshui.py # 可选:生成水墨山水背景图的脚本(默认不用)
```

## 特性

- **主题**：`Catppuccin Latte`（Ghostty 内置，无需额外文件），`minimum-contrast = 1.3` 兜底可读性。
- **字体**：JetBrains Mono 14pt，开启 `font-thicken` 与连字（`calt`、`liga`）。
- **观感**：`background-opacity = 0.88` + `background-blur = 20`，标签式标题栏，未聚焦分屏轻微变暗，内边距 4。
- **Quick terminal**：`Cmd+\`` 全局呼出，从顶部滑出、占屏幕 50%，失焦自动隐藏。
- **窗口**：始终恢复上次窗口状态，新窗口继承工作目录和字号。
- **其他**：选中即复制到剪贴板、打字时隐藏鼠标、块状光标。

## 安装（macOS）

```bash
# 1) 字体
brew install --cask font-jetbrains-mono

# 2) 主配置
cp config.ghostty "$HOME/Library/Application Support/com.mitchellh.ghostty/config.ghostty"

# 3) (可选)水墨主题文件
mkdir -p ~/.config/ghostty/themes
cp themes/ink-xuan themes/ink-splash ~/.config/ghostty/themes/
```

> 在 Ghostty 内按 `Cmd+Shift+,` 重载；quick terminal 的全局快捷键需要重启 Ghostty，并在「系统设置 → 隐私与安全性 → 辅助功能」中允许 Ghostty。
>
> 可用 `ghostty +validate-config` 检查配置是否有误。

## 切换主题

改 `config.ghostty` 第一行：

| 想要 | 写成 |
|---|---|
| Catppuccin 亮色（当前） | `theme = Catppuccin Latte` |
| 跟随系统明暗自动切 | `theme = light:Catppuccin Latte,dark:Catppuccin Mocha` |
| 水墨·宣纸亮色 | `theme = ink-xuan`（需先复制主题文件） |
| 水墨·泼墨暗色 | `theme = ink-splash`（需先复制主题文件） |

水墨主题原本搭配霞鹜文楷等宽字体：`brew install --cask font-lxgw-wenkai`，再把 `font-family` 改为 `"LXGW WenKai Mono"`。

## 常用旋钮

- `minimum-contrast`：文字可读性兜底（当前 1.3）。
- `background-opacity` / `background-blur`：半透明与模糊程度。
- `quick-terminal-position` / `quick-terminal-size`：quick terminal 的位置和大小。

## 可选：水墨山水背景图

默认不用背景图。如想启用：

```bash
# 生成背景图(需 Pillow:pip install pillow)
python3 backgrounds/gen_ink_shanshui.py   # 输出到 ~/.config/ghostty/backgrounds/ink-shanshui.png

# 在 config.ghostty 中加一行
background-image = ~/.config/ghostty/backgrounds/ink-shanshui.png
```

> 生成的 PNG 体积较大且可随时重建，已在 `.gitignore` 中排除，不纳入版本控制。
