import numpy as np
import matplotlib.pyplot as plt
from matplotlib.image import imread

x = np.arange(0,6, 0.1)
y = np.sin(x)
img = imread("/home/jongkook/사진/스크린샷, 2022-05-17 17-06-20.png")
plt.imshow(img)
plt.show()


