import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cm as cm
from matplotlib.animation import FuncAnimation
import random
import PIL.Image
import PIL.ImageDraw
import PIL.ImageFont

##########CONFIG###########
# 動画の保存形式を選択
GIF = 0
MP4 = 1
PLT = 0
SAVEPATH = "boron"
text = "チンポ(ﾎﾞﾛﾝ"
###########################

# ------------------------------------------------------------------
def draw_text_at_center(img, text):
    draw = PIL.ImageDraw.Draw(img)
    font_ttf = "/mnt/c/Windows/Fonts/HGRME.TTC"
    draw.font = PIL.ImageFont.truetype(font_ttf, 80)

    img_size = np.array(img.size)
    txt_size = np.array(draw.font.getsize(text))
    pos = (img_size - txt_size) / 2
    print(img_size)
    print(txt_size)
    print(pos)
    print((X,Y))
    # exit()
    draw.text((0,0), text, (0, 0, 255))

# ------------------------------------------------------------------
X = 500
Y = 100
Back = (1,1,1)
def get_xy(text):
  img = PIL.Image.new("RGBA", (X, Y), Back)
  draw_text_at_center(img, text)
  dat_RGB = np.asarray(img)
  x_list = []
  y_list = []
  for x in range(X):
    for y in range(Y):
      if(dat_RGB[y][x][0] != 1):
        x_list.append(x)
        y_list.append(Y-y-1)
  return x_list, y_list

x_list,y_list = get_xy(text)




PRE = 100
FRAME = 100
ALL = PRE + FRAME

FRAME += 1

FRAME += 50

N = len(x_list)

vx = np.zeros((N,ALL+3))
vy = np.zeros((N,ALL+3))
for n in range(N):
  for frame in range(ALL):
    if(frame%2):
      vx[n][frame] = 2
      vy[n][frame] = 2
    else:
      vx[n][frame] = -2
      vy[n][frame] = -2
  random.shuffle(vx[n])
  random.shuffle(vy[n])

vy = np.concatenate([vy,vy], axis=1)
vx = np.concatenate([vx,vx], axis=1)

for frame in range(PRE):
  for n in range(N):
    x_list[n] += vx[n][frame]
    y_list[n] += vy[n][frame]
    x_list[n] %= X
    y_list[n] %= Y

# 基本的な部品を宣言  
fig = plt.figure()
ax = fig.add_subplot(111, fc="black")
# line, = ax.plot(x_list,y_list,".w", markersize=1)
line, = ax.plot(x_list,y_list,".w")
ax.axes.xaxis.set_visible(False)
ax.axes.yaxis.set_visible(False)
# plt.show()

print("used",PRE-1)

#### 画像更新用関数
def animate(frame):
  if(frame == 0):
    return
  for n in range(N):
    x_list[n] += vx[n][frame+PRE-1]
    y_list[n] += vy[n][frame+PRE-1]
    x_list[n] %= X
    y_list[n] %= Y
  
  print(frame+PRE)
  line.set_data(x_list, y_list)

ani = FuncAnimation(fig, animate, frames=FRAME
              , interval=200, repeat=False, blit=False)


if(GIF == 1):
    ani.save(SAVEPATH+".gif", writer='pillow')
if(MP4 == 1):
    ani.save(SAVEPATH+".mp4", writer="ffmpeg", fps=5)
if(PLT == 1):
    plt.show()