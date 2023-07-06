import re, requests, cv2, numpy, subprocess

def process():
    subprocess.run("pandoc -t html --webtex  main.md -o output.html", shell=True)

    with open("./output.html", "r") as f:
        l = f.read()
        m = re.match(r'.*src="(.*)".*\salt=.*', l)
        url = m.group(1)

    r = requests.get(url, stream=True)

    with open('./img_t.png', 'wb') as f:
        f.write(r.content)

    img = cv2.imread("./img_t.png", -1)
    idx = numpy.where(img[:, :, 3] == 0)
    img[idx] = [255, 255, 255, 255]
    img = cv2.copyMakeBorder(img, 10, 10, 10, 10, cv2.BORDER_CONSTANT, value=[255, 255, 255, 255])
    cv2.imwrite("img_w.png", img)