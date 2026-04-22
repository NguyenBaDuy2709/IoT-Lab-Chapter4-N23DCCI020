from sense_emu import SenseHat
import random, time

sense = SenseHat()
sense.clear()

# Vị trí nhân vật (Trắng) và mục tiêu (Xanh)
px, py = 3, 3
tx, ty = random.randint(0,7), random.randint(0,7)
score = 0

def draw():
    sense.clear()
    sense.set_pixel(tx, ty, [0, 255, 0])     # Mục tiêu = xanh
    sense.set_pixel(px, py, [0,0,0]) # Nhân vật = trắng

draw()

while True:
    for event in sense.stick.get_events():
        if event.action == 'pressed':
            # Di chuyển nhân vật
            if event.direction == 'up' and py > 0:
                py -= 1
            elif event.direction == 'down' and py < 7:
                py += 1
            elif event.direction == 'left' and px > 0:
                px -= 1
            elif event.direction == 'right' and px < 7:
                px += 1
            elif event.direction == 'middle':
                # Nhấn nút giữa để xem điểm số hiện tại
                sense.show_message(str(score), text_colour=[255, 255, 0])

            # Kiểm tra ăn điểm
            if px == tx and py == ty:
                score += 1
                print(f'Ghi ban! Diem: {score}')
                # Hiệu ứng Flash vàng khi ghi điểm
                sense.clear([255, 255, 0])
                time.sleep(0.3)
                # Tạo mục tiêu mới ngẫu nhiên
                tx = random.randint(0, 7)
                ty = random.randint(0, 7)

            draw()
    time.sleep(0.05)
