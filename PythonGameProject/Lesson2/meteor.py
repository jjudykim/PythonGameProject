import tkinter
import random

# 폰트 정의
fnt1 = ("Times New Roman", 24)
fnt2 = ("Times New Roman", 50)

index = 0
timer = 0
score = 0
bg_pos = 0

# 플레이어(우주선) 좌표
px = 240
py = 540

# 유성 수 & 유성 좌표 관리 리스트
METEO_MAX = 30
mx = [0] * METEO_MAX  # 0이 30개 채워진 리스트 생성
my = [0] * METEO_MAX

key = ""          # 키 값 변수
koff = False      # 키 Press 플래그 (평소에 False, 눌렀다 뗐을 때 True)

def key_down(e):
    global key, koff
    key = e.keysym
    koff = False

def key_up(e):
    global koff
    koff = True

def main():
    global key, koff, index, timer, score, bg_pos, px
    timer = timer + 1

    # 배경 우주 이미지 그리기
    bg_pos = (bg_pos + 1) % 640
    canvas.delete("SCREEN")
    canvas.create_image(240, bg_pos - 320, image=img_bg, tag="SCREEN")
    canvas.create_image(240, bg_pos + 320, image=img_bg, tag="SCREEN")

    # index 0 (타이틀 화면)
    if index == 0:
        canvas.create_text(240, 240, text="METEOR", fill="gold", font=fnt2, tag="")
        canvas.create_text(240, 480, text="Press [SPACE] Key", fill="lime", font=fnt1, tag="SCREEN")
        if key == "space":
            score = 0
            px = 240
            init_enemy()
            index = 1

    # index 1 (플레이 중 화면)
    if index == 1:
        score = score + 1
        move_player()
        move_enemy()

    # index 2 (게임 오버 화면)
    if index == 2:
        move_enemy()
        canvas.create_text(240, timer * 4, text="GAME OVER", fill="red", font=fnt2, tag="SCREEN")
        if timer == 60:
            index = 0
            timer = 0
    canvas.create_text(240, 30, text="SCORE " + str(score), fill="white", font=fnt1, tag="SCREEN")

    if koff == True:
        key = ""
        koff = False
    root.after(50, main)

# 충돌 체크 함수
def hit_check(x1, y1, x2, y2):
    if((x1 - x2) * (x1 - x2) + (y1 - y2) * (y1 - y2) < 36 * 36):
        return True
    return False

def init_enemy():
    for i in range(METEO_MAX):
        mx[i] = random.randint(0, 480)
        my[i] = random.randint(-640, 0)

def move_enemy():
    global index, timer
    for i in range(METEO_MAX):
        my[i] = my[i] + 6 + i / 5
        if my[i] > 660:
            mx[i] = random.randint(0, 480)
            my[i] = random.randint(-640, 0)
        if index == 1 and hit_check(px, py, mx[i], my[i]) == True:
            index = 2
            timer = 0
        canvas.create_image(mx[i], my[i], image=img_enemy, tag="SCREEN")

def move_player():
    global px
    if key == "Left" and px > 30:
        px = px - 10
    if key == "Right" and px < 450:
        px = px + 10
    canvas.create_image(px, py, image=img_player[timer % 2], tag="SCREEN")

root = tkinter.Tk()
root.title("Mini Game")
root.bind("<KeyPress>", key_down)
root.bind("<KeyRelease>", key_up)
canvas = tkinter.Canvas(width=480, height=640)
canvas.pack()
img_player=[
    tkinter.PhotoImage(file="starship0.png"),
    tkinter.PhotoImage(file="starship1.png")
]
img_enemy = tkinter.PhotoImage(file="meteo.png")
img_bg = tkinter.PhotoImage(file="cosmo.png")
main()
root.mainloop()