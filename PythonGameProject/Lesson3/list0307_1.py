import tkinter
import random

# 키 입력
key = ""
koff = False

def key_down(e):
    global key, koff
    key = e.keysym
    koff = False

def key_up(e):
    # global koff       # Mac 용
    # koff = True       # Mac 용
     global key          # Windows 용
     key = ""            # Windows 용

DIR_UP = 0
DIR_DOWN = 1
DIR_LEFT = 2
DIR_RIGHT = 3
ANIMATION = [0, 1, 0, 2]

tmr = 0       # 타이머
score = 0     # 점수

pen_x = 90
pen_y = 90
pen_d = 0     # 펜펜 방향
pen_a = 0     # 펜펜 이미지 번호

red_x = 630
red_y = 450
red_d = 0
red_a = 0


# 맵 데이터
map_data = [
    [0, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 0],
    [0, 2, 3, 3, 2, 1, 1, 2, 3, 3, 2, 0],
    [0, 3, 0, 0, 3, 3, 3, 3, 0, 0, 3, 0],
    [0, 3, 1, 1, 3, 0, 0, 3, 1, 1, 3, 0],
    [0, 3, 2, 2, 3, 0, 0, 3, 2, 2, 3, 0],
    [0, 3, 0, 0, 3, 1, 1, 3, 0, 0, 3, 0],
    [0, 3, 1, 1, 3, 3, 3, 3, 1, 1, 3, 0],
    [0, 2, 3, 3, 2, 0, 0, 2, 3, 3, 2, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
]


# 그림자 포함 문자
def draw_txt(txt, x, y, siz, col):
    fnt = ("Times New Roman", siz, "bold")
    canvas.create_text(x + 2, y + 2, text=txt, fill="black", font=fnt, tag="SCREEN")
    canvas.create_text(x, y, text=txt, fill=col, font=fnt, tag="SCREEN")


# 게임 화면 그리기
def draw_screen():
    canvas.delete("SCREEN")
    for y in range(9):
        for x in range(12):
            canvas.create_image(x * 60 + 30, y * 60 + 30, image=img_bg[map_data[y][x]], tag="SCREEN")
    canvas.create_image(pen_x, pen_y, image=img_pen[pen_a], tag="SCREEN")
    canvas.create_image(red_x, red_y, image=img_red[red_a], tag="SCREEN")
    draw_txt("SCORE " + str(score), 200, 30, 30, "white")

# 각 방향에 벽 존재 여부 확인
def check_wall(cx, cy, di, dot):
    chk = False
    if di == DIR_UP:
        mx = int((cx-30) / 60)
        my = int((cy - 30 - dot) / 60)
        if map_data[my][mx] <= 1:    # 좌상
            chk = True
        mx = int((cx + 29) / 60)
        if map_data[my][mx] <= 1:    # 우상
            chk = True
    if di == DIR_DOWN:
        mx = int((cx-30) / 60)
        my = int((cy + 29 + dot) / 60)
        if map_data[my][mx] <= 1:    # 좌하
            chk = True
        mx = int((cx + 29) / 60)
        if map_data[my][mx] <= 1:    # 우하
            chk = True
    if di == DIR_LEFT:
        mx = int((cx - 30 - dot) / 60)
        my = int((cy -  30) / 60)
        if map_data[my][mx] <= 1:    # 좌상
            chk = True
        my = int((cy + 29) / 60)
        if map_data[my][mx] <= 1:    # 좌하
            chk = True
    if di == DIR_RIGHT:
        mx = int((cx + 29 + dot) / 60)
        my = int((cy - 30) / 60)
        if map_data[my][mx] <= 1:    # 우상
            chk = True
        my = int((cy + 29) / 60)
        if map_data[my][mx] <= 1:    # 우하
            chk = True
    return chk


# 펜펜 움직이기
def move_penpen():
    global score, pen_x, pen_y, pen_d, pen_a
    if key == "Up":
        pen_d = DIR_UP
        if check_wall(pen_x, pen_y, pen_d, 20) == False:
            pen_y = pen_y - 20
    if key == "Down":
        pen_d = DIR_DOWN
        if check_wall(pen_x, pen_y, pen_d, 20) == False:
            pen_y = pen_y + 20
    if key == "Left":
        pen_d = DIR_LEFT
        if check_wall(pen_x, pen_y, pen_d, 20) == False:
            pen_x = pen_x - 20
    if key == "Right":
        pen_d = DIR_RIGHT
        if check_wall(pen_x, pen_y, pen_d, 20) == False:
            pen_x = pen_x + 20
    pen_a = pen_d * 3 + ANIMATION[tmr % 4]
    mx = int(pen_x / 60)
    my = int(pen_y / 60)
    if map_data[my][mx] == 3:    # 사탕에 닿았는가?
        score = score + 100
        map_data[my][mx] = 2


# 레드 움직이기
def move_enemy():
    global red_x, red_y, red_d, red_a
    speed = 10
    if red_x % 60 == 30 and red_y % 60 == 30:
        red_d = random.randint(0, 3)
    if red_d == DIR_UP:
        if check_wall(red_x, red_y, red_d, speed) == False:
            red_y = red_y - speed
    if red_d == DIR_DOWN:
        if check_wall(red_x, red_y, red_d, speed) == False:
            red_y = red_y + speed
    if red_d == DIR_LEFT:
        if check_wall(red_x, red_y, red_d, speed) == False:
            red_x = red_x - speed
    if red_d == DIR_RIGHT:
        if check_wall(red_x, red_y, red_d, speed) == False:
            red_x = red_x + speed
    red_a = red_d * 3 + ANIMATION[tmr % 4]

# 메인 루프
def main():
    global key, koff, tmr
    tmr = tmr + 1
    draw_screen()
    move_penpen()
    move_enemy()
    # 다음은 Mac 용 키 입력 처리
    # if koff == True:
    #    key = ""
    #    koff = False
    root.after(100, main)


root = tkinter.Tk()

# 이미지 설정
img_bg = [
    tkinter.PhotoImage(file="image_penpen/chip00.png"),
    tkinter.PhotoImage(file="image_penpen/chip01.png"),
    tkinter.PhotoImage(file="image_penpen/chip02.png"),
    tkinter.PhotoImage(file="image_penpen/chip03.png")
]

img_pen = [
    tkinter.PhotoImage(file="image_penpen/pen00.png"),
    tkinter.PhotoImage(file="image_penpen/pen01.png"),
    tkinter.PhotoImage(file="image_penpen/pen02.png"),
    tkinter.PhotoImage(file="image_penpen/pen03.png"),
    tkinter.PhotoImage(file="image_penpen/pen04.png"),
    tkinter.PhotoImage(file="image_penpen/pen05.png"),
    tkinter.PhotoImage(file="image_penpen/pen06.png"),
    tkinter.PhotoImage(file="image_penpen/pen07.png"),
    tkinter.PhotoImage(file="image_penpen/pen08.png"),
    tkinter.PhotoImage(file="image_penpen/pen09.png"),
    tkinter.PhotoImage(file="image_penpen/pen10.png"),
    tkinter.PhotoImage(file="image_penpen/pen11.png"),
]

img_red=[
    tkinter.PhotoImage(file="image_penpen/red00.png"),
    tkinter.PhotoImage(file="image_penpen/red01.png"),
    tkinter.PhotoImage(file="image_penpen/red02.png"),
    tkinter.PhotoImage(file="image_penpen/red03.png"),
    tkinter.PhotoImage(file="image_penpen/red04.png"),
    tkinter.PhotoImage(file="image_penpen/red05.png"),
    tkinter.PhotoImage(file="image_penpen/red06.png"),
    tkinter.PhotoImage(file="image_penpen/red07.png"),
    tkinter.PhotoImage(file="image_penpen/red08.png"),
    tkinter.PhotoImage(file="image_penpen/red09.png"),
    tkinter.PhotoImage(file="image_penpen/red10.png"),
    tkinter.PhotoImage(file="image_penpen/red11.png")
]

root.title("아슬아슬 펭귄 미로")
root.resizable(False, False)
root.bind("<KeyPress>", key_down)
root.bind("<KeyRelease>", key_up)
canvas = tkinter.Canvas(width=720, height=540)
canvas.pack()
main()
root.mainloop()
