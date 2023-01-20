#과제 분담할 때 채점할 파일들만 남기고 삭제 
import os
count = 0
for (path,dir,files) in os.walk("C:/"):
    for filename in files:
        if filename.find("HW1") >= 0:
            count += 1
        else: #조건에 맞지 않는 파일은 삭제
            os.remove("%s%s"%(path,filename))
print(count)
