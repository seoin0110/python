import pyautogui
#import time
#pyautogui.location() 위치 알려줌 
pyautogui.moveTo(1035,692) #x=1035,y=692로 마우스 포인터 이동

pyautogui.click(clicks=100,interval=0.1) #0.1초의 간격으로 100번 클
#pyautogui.doubleClick() 더블클릭
#time.sleep(1) 1초 쉼
#pyautogui.typewrite('Hello')
#pyautogui.typewrite(['enter']) 엔터 치고싶을 때
#pyautogui.typewrite(['a','b','c','enter']) abc와 엔터 입력됨 [] 안에 쓰려면 그 키를 눌러줌
#따라서 (['abc'])는 안됨
