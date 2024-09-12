# 파일에서 이미지를 읽어서 출력

import cv2
import sys
filename="data/cat.jpg"

#이미지를 불러오는 함수
img=cv2.imread(filename)
print(img.shape)
#예외처리 루틴:이미지를 읽어오지 못했을때
if img is None:
    print("Image load fail")
    #프로그램 종료
    sys.exit()
    
#창에 이미지를 출력
#창의 이름을 img
cv2.namedWindow('img')
#img창에 img배열을 출력
cv2.imshow('img',img)
#키보드 입력을 기다리는 함수
inkey=cv2.waitKey(  )
print(inkey)
#모든 창 닫기
cv2.destroyAllWindows()