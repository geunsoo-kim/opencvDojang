#함수 스타일로 코딩

import cv2,sys
import numpy as np
import os
from glob import glob
import shutil
from enum import Enum

#클래스에 내장될 기능을 번호로 설정
class funcNum(Enum):
    resize=1
    rotate=2
    hflip=3
    vflip=4
    crop=5
    
dataPath = os.path.join(os.getcwd(),'DataAug')
dataOrg=os.path.join(dataPath,'org')

DEBUG=True

#전역변수
dsize=(224,224)

#input:dataPath
#output:dataPath안에 jpg파일의 리스트를 가져오기
#확장하려면 기능추가 :img_type=['jpg','png','gif']
def getFileList(dataPath):
    fileNames=glob(os.path.join(dataPath,'*.jpg'))
    if DEBUG:
        print(fileNames)
    if fileNames is None:
        print("filelist nope")
    
    return fileNames
#이미지를 불러오는 함수
def readImg(image_path):
    img=cv2.imread(image_path)
    
    if img is None:
        sys.exit('image load failed')
    return img

#input:원본 파일명
#output:새로생성될 파일명
def getFileName(imgName):
        #파일명 생성
    #"airPod_white.jpg"
    #경로를 제외한 파일명만  올려낸다.abs
    baseName=os.path.basename(imgName)
    #확장자만 분리
    baseNameSplit=os.path.splitext(baseName)[0]
    resizeName=baseNameSplit+'_resize'+str(dsize[0])+'.jpg'
    return resizeName

def resize(img=None,dsize=dsize,imgName=None):
    if img is None:
        print("image path is none")
        
    dst=cv2.resize(img, dsize,interpolation=cv2.INTER_AREA)
    #샐로 만들 파일명 가져오기
    resizeName=getFileName(imgName)
    cv2.imwrite(resizeName,dst)
    return dst
    #파일 저장

classList=['blue','bluearm','brown','brownarm','gray','green','red']

def createFolder():
    for classname in classList:
        #기존에 폴더가 있으면 삭제하고, 새로 생성
        #폴더안에 파일이 존재하더라도, 파일과 폴더를 모두 삭제
        classPath=os.path.join(dataPath,classname)
        print(classPath)
        if os.path.isdir(classPath):
            shutil.rmtree(classPath)
        os.makedirs(classPath,exist_ok=True)
    
def main():
    createFolder()
    fileNames=getFileList(dataOrg)
    for fileNames in fileNames:
        
        img=readImg(fileNames)
        dst=resize(img,dsize,fileNames)
        cv2.imshow('img',dst)
        cv2.waitKey()
        break
    cv2.destroyAllWindows()
    
if __name__=="__main__":
    main()

