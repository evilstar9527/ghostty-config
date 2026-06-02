# ghostty-config

水墨风格的 [Ghostty](https://ghostty.org) 终端配置：霞鹜文楷等宽字体 + 自定义宣纸/泼墨配色 + 水墨山水背景图。

## 内容

```
config.ghostty            # 主配置(macOS 放到 Application Support)
themes/ink-xuan           # 宣纸亮色主题(墨/朱砂/赭石/花青等国画颜料色)
themes/ink-splash         # 泼墨暗色主题
backgrounds/shanshui.png        # 当前使用的水墨山水背景图
backgrounds/ink-shanshui.png    # 程序化生成的淡墨远山背景图(备用)
backgrounds/gen_ink_shanshui.py # 上图的 Pillow 生成脚本,可改参数重生成
```

## 特性

- **字体**：LXGW WenKai Mono（霞鹜文楷等宽），毛笔楷意，中英文皆可。
- **配色**：`ink-xuan`(宣纸亮) / `ink-splash`(泼墨暗)，全用低饱和国画颜料色，朱砂光标呼应印章。
- **背景**：水墨山水画，`background-image-opacity` 调淡至 0.15，文字区留白，靠 `minimum-contrast` 兜底可读性。
- 留白加大（padding 12）、半透明 + 模糊、quick-terminal 等。

## 安装（macOS）

```bash
# 1) 字体
brew install --cask font-lxgw-wenkai

# 2) 主题文件
mkdir -p ~/.config/ghostty/themes
cp themes/ink-xuan themes/ink-splash ~/.config/ghostty/themes/

# 3) 背景图
mkdir -p ~/.config/ghostty/backgrounds
cp backgrounds/* ~/.config/ghostty/backgrounds/

# 4) 主配置
cp config.ghostty "$HOME/Library/Application Support/com.mitchellh.ghostty/config.ghostty"
```

> ⚠️ `config.ghostty` 里的 `background-image` 是**绝对路径**（`/Users/<you>/.config/ghostty/backgrounds/shanshui.png`），
> 换机器需把用户名改成自己的。
>
> 在 Ghostty 内按 `Cmd+Shift+,` 重载，或重启生效。

## 常用旋钮

- `background-image-opacity`：画面浓淡（越小越淡，当前 0.15）。
- `minimum-contrast`：文字落到深墨处的可读性兜底（当前 1.5，可升到 1.8~2.0）。
- `background-image-fit`：`cover`(铺满裁切) / `contain`(完整显示+留白衬底)。
- 想换亮/暗自动切换：`theme = light:ink-xuan,dark:ink-splash`。
