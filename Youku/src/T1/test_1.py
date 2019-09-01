from appium import webdriver
import yaml,time
from until.slide import swipe_up
from until.slide import swipe_down
from until.slide import swpie_left
with open(file="C:\Youku\element\log.yaml", mode="r", encoding="utf-8") as f:
    e = yaml.load(f, Loader=yaml.FullLoader)

# 用例一:成功打开查看历史界面，并返回到主界面
def test_1(lian):
    lian.find_element_by_id(e['qq_id']).click()
    time.sleep(6)
    b = lian.find_element_by_id(e['xpy_id']).text
    assert b == "小朋友"
    #返回到主界面
    lian.find_element_by_id(e['back_id']).click()


# 用例二:成功打开收藏界面，并返回主界面
def test_2(lian):
    lian.find_element_by_id(e['qq_id']).click()
    time.sleep(6)
    c = lian.find_element_by_id(e['xpy_id']).text
    assert c == "小朋友"
    lian.find_element_by_id(e['shoucang_id']).click()
    time.sleep(5)
    lian.find_element_by_id(e['back_id']).click()


# 用例三：成功打开下载界面，并返回主界面
def test_3(lian):
    lian.find_element_by_id(e['qq_id']).click()
    time.sleep(6)
    a = lian.find_element_by_id(e['xpy_id']).text
    assert a == "小朋友"
    lian.find_element_by_id(e['down_id']).click()
    time.sleep(5)
    lian.find_element_by_id(e['back_id']).click()


# 用例四:成功进入搜素界面,并返回到主界面
def test_4(lian):
    lian.find_element_by_id(e['search_id']).click()
    time.sleep(5)
    c=lian.find_element_by_xpath(e['resou_xpath']).text
    assert c == "视频热搜TOP3"
    time.sleep(5)
    lian.find_element_by_id('com.youkuchild.android:id/back_btn').click()


# 用例五:成功进入筛选绘本界面滑动查看绘本
def test_5(lian):
    lian.find_element_by_id(e['search_id']).click()
    time.sleep(3)
    c = lian.find_element_by_xpath(e['resou_xpath']).text
    assert c == "视频热搜TOP3"
    time.sleep(3)
    lian.find_element_by_xpath(e['shaixuan_xpath']).click()
    time.sleep(3)
    swipe_up(lian)
    lian.find_element_by_id('com.youkuchild.android:id/back_btn').click()
    time.sleep(3)
    lian.find_element_by_id('com.youkuchild.android:id/back_btn').click()


# 用例六:主界面的星球顺时针可以成功滑动
def test_6(lian):
    swipe_up(lian)


# 用例七:主界面的星球逆时针可以成功滑动
def test_7(lian):
    swipe_down(lian)


# 用例八:成功打开《帽子戏法》绘本并可以翻页阅读
def test_8(lian):
    lian.find_element_by_id(e['search_id']).click()
    time.sleep(3)
    t=lian.find_element_by_id('com.youkuchild.android:id/page_recycler_container').find_elements_by_class_name('android.view.View')
    t[1].click()
    lian.find_element_by_id(e['yuedu_id']).click()
    time.sleep(6)
    swpie_left(lian)


# 用例九:成功打开《精灵叶罗丽 第七季》视频并可以正常观看
def test_9(lian):
    lian.find_element_by_id(e['search_id']).click()
    time.sleep(3)
    t = lian.find_element_by_id('com.youkuchild.android:id/page_recycler_container').find_elements_by_class_name('android.view.View')
    t[0].click()

















# a=lian.find_element_by_id("com.youkuchild.android:id/ball_name").text
#    assert a == "视 频"
# b = lian.find_element_by_id("com.youkuchild.android:id/child_uc_user_name").text
# assert b == "小朋友"