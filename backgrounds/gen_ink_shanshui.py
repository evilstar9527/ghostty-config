#!/usr/bin/env python3
# 生成水墨「山水意境」背景图 —— 宣纸渐变 + 纸纹 + 三层淡墨远山 + 朱砂落款
# 与主题宣纸色同底,留白集中在上方(文字区),山影靠底部。极淡,可读性优先。
import math, random
from PIL import Image, ImageDraw, ImageFilter

random.seed(20)                      # 固定随机种子,结果可复现
W, H = 2560, 1600

def lerp(a, b, t):
    return tuple(round(a[i] + (b[i] - a[i]) * t) for i in range(3))

# 1) 宣纸竖向渐变:顶部薄雾偏亮 -> 底部略深
TOP = (246, 241, 230)   # #f6f1e6
BOT = (239, 231, 215)   # #efe7d7
base = Image.new("RGB", (W, H))
px = base.load()
for y in range(H):
    c = lerp(TOP, BOT, y / (H - 1))
    for x in range(W):
        px[x, y] = c

# 2) 宣纸纹理:低幅噪声,轻模糊,极低 alpha 叠加
noise = Image.new("L", (W, H))
npx = noise.load()
for y in range(H):
    for x in range(W):
        npx[x, y] = random.randint(0, 255)
noise = noise.filter(ImageFilter.GaussianBlur(0.6))
tex = Image.new("RGB", (W, H), (90, 80, 60))
base = Image.composite(tex, base, noise.point(lambda v: int(v * 0.05)))  # ~5% 强度

def ridge(y_base, amp, color, alpha, blur, rough=1.0):
    """画一条起伏山脊并填充其下方,返回 RGBA 图层。"""
    layer = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    d = ImageDraw.Draw(layer)
    # 几条正弦叠加 + 轻微随机扰动 -> 自然起伏
    phases = [random.uniform(0, math.tau) for _ in range(3)]
    freqs  = [1.1, 2.3, 4.7]
    weights = [1.0, 0.5, 0.25]
    pts = []
    step = 6
    for x in range(0, W + step, step):
        t = x / W
        dy = sum(weights[i] * math.sin(t * math.tau * freqs[i] + phases[i]) for i in range(3))
        dy += random.uniform(-0.12, 0.12) * rough
        y = y_base + dy * amp
        pts.append((x, y))
    poly = pts + [(W, H), (0, H)]
    d.polygon(poly, fill=color + (alpha,))
    if blur:
        layer = layer.filter(ImageFilter.GaussianBlur(blur))
    return layer

img = base.convert("RGBA")

# 3) 远山三层:越远越淡越靠上,柔边如云雾
# (y_base 用比例 * H)
far  = ridge(H * 0.58, H * 0.05, (220, 214, 200), 150, 26, rough=0.7)  # #dcd6c8 最淡
mid  = ridge(H * 0.70, H * 0.06, (205, 198, 180), 175, 16, rough=1.0)  # #cdc6b4
near = ridge(H * 0.82, H * 0.07, (187, 180, 160), 200, 9,  rough=1.3)  # #bbb4a0
for layer in (far, mid, near):
    img = Image.alpha_composite(img, layer)

# 4) 云带:山腰几道低 alpha 白色横向柔光
mist = Image.new("RGBA", (W, H), (0, 0, 0, 0))
md = ImageDraw.Draw(mist)
for (yc, h, a) in [(H*0.64, 46, 70), (H*0.74, 40, 60), (H*0.86, 52, 55)]:
    md.rectangle([0, yc - h/2, W, yc + h/2], fill=(252, 249, 242, a))
mist = mist.filter(ImageFilter.GaussianBlur(34))
img = Image.alpha_composite(img, mist)

# 5) 朱砂落款:右下角小印章(方框 + 两笔),呼应朱砂光标
seal = Image.new("RGBA", (W, H), (0, 0, 0, 0))
sd = ImageDraw.Draw(seal)
S = 96                      # 印章边长
mx, my = W - 150, H - 150   # 左上角坐标
red = (168, 66, 48)         # 朱砂 #a8423a
sd.rounded_rectangle([mx, my, mx + S, my + S], radius=10, outline=red + (210,), width=7)
# 内部两道竖笔意象
sd.line([mx + S*0.36, my + S*0.22, mx + S*0.36, my + S*0.78], fill=red + (190,), width=8)
sd.line([mx + S*0.62, my + S*0.22, mx + S*0.62, my + S*0.78], fill=red + (190,), width=8)
sd.line([mx + S*0.36, my + S*0.5, mx + S*0.62, my + S*0.5], fill=red + (170,), width=7)
seal = seal.filter(ImageFilter.GaussianBlur(0.6))
img = Image.alpha_composite(img, seal)

out = img.convert("RGB")
import os
dst = os.path.expanduser("~/.config/ghostty/backgrounds/ink-shanshui.png")
os.makedirs(os.path.dirname(dst), exist_ok=True)
out.save(dst, "PNG")
print("saved:", dst, out.size)
