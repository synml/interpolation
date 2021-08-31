import os
import time
import cv2

# 보간 배수입니다. 현재는 4배로 설정되어 있습니다.
scale_factor = 4

# 입력 이미지 불러오기
if not os.path.isfile('img/0input.jpg'):
    print('입력 이미지를 찾을 수 없습니다. 파일명과 경로를 확인해주세요.')
    os.system('pause')
    exit(1)
src = cv2.imread('img/0input.jpg', cv2.IMREAD_COLOR)

# 보간법 실행
start_time = time.time()
nearest = cv2.resize(src, dsize=(0, 0), fx=scale_factor, fy=scale_factor, interpolation=cv2.INTER_NEAREST)
nearest_time = (time.time() - start_time) * 1000

start_time = time.time()
bilinear = cv2.resize(src, dsize=(0, 0), fx=scale_factor, fy=scale_factor, interpolation=cv2.INTER_LINEAR)
bilinear_time = (time.time() - start_time) * 1000

start_time = time.time()
bicubic = cv2.resize(src, dsize=(0, 0), fx=scale_factor, fy=scale_factor, interpolation=cv2.INTER_CUBIC)
bicubic_time = (time.time() - start_time) * 1000

start_time = time.time()
lanczos = cv2.resize(src, dsize=(0, 0), fx=scale_factor, fy=scale_factor, interpolation=cv2.INTER_LANCZOS4)
lanczos_time = (time.time() - start_time) * 1000

# 보간 결과 저장
cv2.imwrite('img/1nearest.jpg', nearest)
cv2.imwrite('img/2bilinear.jpg', bilinear)
cv2.imwrite('img/3bicubic.jpg', bicubic)
cv2.imwrite('img/4lanczos.jpg', lanczos)
print('보간 결과를 img 폴더에 저장했습니다.')

# 보간 처리 시간 저장
with open('처리 시간.txt', mode='w', encoding='utf-8') as f:
    f.write('최근접 이웃 보간법, 양선형 보간법, 3차원 회선 보간법, lanczos 보간법\n')
    f.write(f'{nearest_time:.4f}ms, {bilinear_time:.4f}ms, {bicubic_time:.4f}ms, {lanczos_time:.4f}ms\n')
print('보간 처리 시간을 csv 파일로 저장했습니다.')
os.system('pause')
