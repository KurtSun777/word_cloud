#!/usr/bin/env python
# coding: utf-8

# In[1]:


from PIL import Image 
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from collections import Counter
import wordcloud
from PIL import Image
from scipy.ndimage import gaussian_gradient_magnitude
from wordcloud import WordCloud,ImageColorGenerator
import matplotlib.pyplot as plt
import imageio
from matplotlib import colors


# In[4]:


with open('106_xword.csv', 'r', encoding = 'utf-8') as f:
    text = f.read()
print(type(text))


# In[5]:


mk = imageio.imread("2.jpeg")

# 使用wordcloud.WordCloud類，並傳入相關的引數
wc = wordcloud.WordCloud(background_color="white",
                         prefer_horizontal=0.5,
                         repeat=True,
                         min_font_size = 1,
                         mask=mk,
                         font_path='SNsanafonMugiV260.ttf',
                         contour_width=2,
                         contour_color='pink',
                         collocation_threshold=100,
                         )



# 將string變數傳入w的generate()方法，給詞雲輸入文字
wc.generate(text)

# 儲存圖片
wc.to_file('test.png')


# In[6]:


mk = imageio.imread("2.jpeg")


wc = WordCloud(  
 max_font_size=30, #最大字號 
 background_color='white', #設定背景顏色 
 font_path='SNsanafonMugiV260.ttf',
 mask = mk,
 height=500,
 width=500,
 scale=1,
 margin=1
 ) 
wc.generate(text) # 從文字生成wordcloud 
# wc.generate_from_text(text) #用這種表達方式也可以  
# 顯示影象 
plt.imshow(wc,interpolation='bilinear') 
plt.axis('off') 
plt.tight_layout() 
wc.to_file('1.png') # 儲存影象 
plt.savefig('標籤雲效果圖.png',dpi=500) #用這個可以指定畫素 
plt.show() 


# In[ ]:





# In[ ]:




