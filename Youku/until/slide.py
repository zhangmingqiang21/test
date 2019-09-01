from appium import webdriver
import time
# 获取手机屏幕的大小
def swipe_up(dr,t=500):
    for i in range(1,10):
        l=dr.get_window_size()
        # 放缩手机屏幕
        x1=l['width']*0.5
        x2=l['width']*0.5
        y1=l['height']*0.5
        y2=l['height']*0.2
        dr.swipe(x1,y1,x2,y2,duration=t)
        time.sleep(1)

def swipe_down(dr,t=500):
    for i in range(1,100):
        l = dr.get_window_size()
        # 放缩手机屏幕
        x1 = l['width'] * 0.2
        x2 = l['width'] * 0.5
        y1 = l['height'] * 0.5
        y2 = l['height'] * 0.5
        dr.swipe(x1, y1, x2, y2, duration=t)
        time.sleep(1)


def swpie_left(dr,t=500):
    for i in range(1,50):
        l = dr.get_window_size()
        # 放缩手机屏幕
        x1 = l['width'] * 0.5
        x2 = l['width'] * 0.2
        y1 = l['height'] * 0.5
        y2 = l['height'] * 0.5
        dr.swipe(x1, y1, x2, y2, duration=t)
        time.sleep(5)
