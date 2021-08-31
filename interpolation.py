import os
import cv2

# 보간 배수입니다. 현재는 4배로 설정되어 있습니다.
scale_factor = 4

if not os.path.isfile('img/0input.jpg'):
    print('입력 이미지를 찾을 수 없습니다. 파일명과 경로를 확인해주세요.')
    os.system('pause')
    exit(1)
src = cv2.imread('img/0input.jpg', cv2.IMREAD_COLOR)
nearest = cv2.resize(src, dsize=(0, 0), fx=scale_factor, fy=scale_factor, interpolation=cv2.INTER_NEAREST)
bilinear = cv2.resize(src, dsize=(0, 0), fx=scale_factor, fy=scale_factor, interpolation=cv2.INTER_LINEAR)
bicubic = cv2.resize(src, dsize=(0, 0), fx=scale_factor, fy=scale_factor, interpolation=cv2.INTER_CUBIC)
lanczos = cv2.resize(src, dsize=(0, 0), fx=scale_factor, fy=scale_factor, interpolation=cv2.INTER_LANCZOS4)

cv2.imwrite('img/1nearest.jpg', nearest)
cv2.imwrite('img/2bilinear.jpg', bilinear)
cv2.imwrite('img/3bicubic.jpg', bicubic)
cv2.imwrite('img/4lanczos.jpg', lanczos)
print('보간 결과를 img 폴더에 저장했습니다.')
os.system('pause')
