from sense_emu import SenseHat
import time

sense = SenseHat()

# Hàm chuyển đổi giá trị sang 0-8 cột LED
def map_value(val, in_min, in_max, out_max=8):
    result = int((val - in_min) / (in_max - in_min) * out_max)
    return max(0, min(out_max, result))

# Hàm vẽ thanh biểu đồ (Bar)
def draw_bar(y_start, y_end, cols, color):
    for y in range(y_start, y_end + 1):
        for x in range(8):
            sense.set_pixel(x, y, color if x < cols else [0, 0, 0])

try:
    while True:
        temp = sense.get_temperature()
        hum = sense.get_humidity()

        # Vẽ bar Nhiệt độ (Đỏ) ở hàng 0-2, dải 15-40 độ
        temp_cols = map_value(temp, 15, 40)
        draw_bar(0, 2, temp_cols, [255, 0, 0])

        # Vẽ bar Độ ẩm (Xanh dương) ở hàng 3-5, dải 20-90%
        hum_cols = map_value(hum, 20, 90)
        draw_bar(3, 5, hum_cols, [0, 0, 255])

        # Xác định trạng thái dựa trên ngưỡng (Hàng 6-7)
        if temp > 45 and hum > 80:
            status_color = [255, 0, 0]    # Đỏ = Nguy hiểm
        elif temp > 35 or hum > 80:
            status_color = [255, 255, 0]  # Vàng = Cảnh báo
        else:
            status_color = [0, 255, 0]    # Xanh lá = OK
        draw_bar(6, 7, 8, status_color)

        print(f'Temp: {temp:.1f}C ({temp_cols} cols) | Hum: {hum:.1f}% ({hum_cols} cols)')
        time.sleep(1)

except KeyboardInterrupt:
    sense.clear()
