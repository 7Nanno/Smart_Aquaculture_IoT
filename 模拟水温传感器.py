import time
import random
# 先在电脑上把养鱼监控的逻辑写出来，到时候硬件一接就能用了。
# 这里的逻辑是：读取水温,判断,报警
def main_loop():
    print("---------------------------------------")
    print("智慧水产监控系统 - 逻辑测试版 (V1.0)")
    print("状态：硬件未连接，进入模拟模式...")
    print("---------------------------------------")
    # 之前想用 while 1，后来查了下还是 while True 规范一点
    while True:
        # 模拟水温传感器数据 (DHT11还没到，先用随机数顶替)
        # 正常水温一般在25-28度，设置个波动范围
        current_temp = round(random.uniform(24.5, 31.5), 1)
        # 获取当前时间
        now_time = time.strftime('%H:%M:%S', time.localtime())
        print(f"[{now_time}] 实时水温: {current_temp}度")
        # --- 核心预警逻辑 ---
        if current_temp > 30.0:
            print("!!! 🚨 警告：温度过高 !!!")
            print("动作：尝试向串口发送指令启动散热扇...")
            # TODO: 硬件到了后这里写 ser.write(b'1')
        elif current_temp < 25.0:
            print("!!! 🚨 警告：温度过低 !!!")
            print("动作：尝试启动加热棒...")
            # TODO: 这里写加热控制逻辑
        else:
            print("状态：水温正常，运行中...")
        # 模拟每2秒测一次，不然屏幕刷新太快看不清
        time.sleep(2)
# 运行
if __name__ == "__main__":
    try:
        main_loop()
    except KeyboardInterrupt:
        # 这样按 Ctrl+C 退出的时候不会报一堆红字错误
        print("\n[退出] 监控停止，准备接入硬件...")
