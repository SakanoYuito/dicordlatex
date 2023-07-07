import re, requests, cv2, numpy, subprocess

def process(eq):
    url = f'https://latex.codecogs.com/png.latex?{eq}'
    r = requests.get(url, stream=True)

    # 透過画像
    with open('./img_t.png', 'wb') as f:
        f.write(r.content)

    # 白背景
    img = cv2.imread("./img_t.png", -1)
    idx = numpy.where(img[:, :, 3] == 0)
    img[idx] = [255, 255, 255, 255]
    img = cv2.resize(img, None, fx=0.3, fy=0.3, interpolation=cv2.INTER_AREA)
    img = cv2.copyMakeBorder(img, 5, 5, 5, 5, cv2.BORDER_CONSTANT, value=[255, 255, 255, 255])
    cv2.imwrite("img_w.png", img)