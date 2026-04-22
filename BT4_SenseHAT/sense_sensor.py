from sense_emu import SenseHat
import time

sense = SenseHat()

try:
    while True:
        # Đọc dữ liệu từ 3 loại cảm biến
        temp = sense.get_temperature()
        hum = sense.get_humidity()
        press = sense.get_pressure()
        # In kết quả ra màn hình Terminal
        print(f'Temp: {temp:.1f}°C | Humidity: {hum:.1f}% | Pressure: {press:.1f} mbar')
        time.sleep(1)
except KeyboardInterrupt:
    sense.clear()
    print('Dừng đọc cảm biến.')

