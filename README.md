# ghostty-config

水墨风格的 [Ghostty](https://ghostty.org) 终端配置：霞鹜文楷等宽字体 + 自定义宣纸/泼墨配色。

## 内容

```
config.ghostty       # 主配置(macOS 放到 Application Support)
themes/ink-xuan      # 宣纸亮色主题(墨/朱砂/赭石/花青等国画颜料色)
themes/ink-splash    # 泼墨暗色主题
```

## 特性

- **字体**：LXGW WenKai Mono（霞鹜文楷等宽），毛笔楷意，中英文皆可。
- **配色**：`ink-xuan`(宣纸亮) / `ink-splash`(泼墨暗)，全用低饱和国画颜料色，朱砂光标呼应印章。
- **观感**：纯色半透明 + 模糊，留白加大（padding 12），无背景图，可读性优先。
- quick-terminal（`Cmd+\``呼出）、`copy-on-select`、光标不闪等。

## 安装（macOS）

```bash
# 1) 字体
brew install --cask font-lxgw-wenkai

# 2) 主题文件
mkdir -p ~/.config/ghostty/themes
cp themes/ink-xuan themes/ink-splash ~/.config/ghostty/themes/

# 3) 主配置
cp config.ghostty "$HOME/Library/Application Support/com.mitchellh.ghostty/config.ghostty"
```

> 在 Ghostty 内按 `Cmd+Shift+,` 重载，或重启生效。

## 切换主题

改 `config.ghostty` 第一行：

| 想要 | 写成 |
|---|---|
| 宣纸亮色（当前） | `theme = ink-xuan` |
| 泼墨暗色 | `theme = ink-splash` |
| 跟随系统明暗自动切 | `theme = light:ink-xuan,dark:ink-splash` |

## 常用旋钮

- `minimum-contrast`：文字可读性兜底（当前 1.5）。
- `background-opacity` / `background-blur`：半透明与模糊程度。
