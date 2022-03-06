#!/usr/bin/env python
# coding: utf-8

# In[224]:


# Import Splinter and BeautifulSoup
from splinter import Browser
from bs4 import BeautifulSoup as soup
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd


# In[225]:


executable_path = {'executable_path': ChromeDriverManager().install()}
browser = Browser('chrome', **executable_path, headless=False)


# In[207]:


# Visit the mars nasa news site
url = 'https://redplanetscience.com'
browser.visit(url)
# Optional delay for loading the page
browser.is_element_present_by_css('div.list_text', wait_time=1)


# In[208]:


html = browser.html
news_soup = soup(html, 'html.parser')
slide_elem = news_soup.select_one('div.list_text')


# In[209]:


for x in range(1, 6):
    html = browser.html
    quote_soup = soup(html, 'html.parser')
    quotes = quote_soup.find_all('span', class_='text')
    for quote in quotes:
        print('page:', x, '----------')
        print(quote.text)
        browser.links.find_by_partial_text('Next').click()


# In[210]:


slide_elem.find('div', class_='content_title')


# In[211]:


# Use the parent element to find the first `a` tag and save it as `news_title`
news_title = slide_elem.find('div', class_='content_title').get_text()
news_title


# In[212]:


# Use the parent element to find the paragraph text
news_p = slide_elem.find('div', class_='article_teaser_body').get_text()
news_p


# ### Featured Images

# In[213]:


# Visit URL
url = 'https://spaceimages-mars.com'
browser.visit(url)


# In[214]:


# Find and click the full image button
full_image_elem = browser.find_by_tag('button')[1]
full_image_elem.click()


# In[215]:


# Parse the resulting html with soup
html = browser.html
img_soup = soup(html, 'html.parser')


# In[216]:


# Find the relative image url
img_url_rel = img_soup.find('img', class_='fancybox-image').get('src')
img_url_rel


# In[217]:


# Use the base URL to create an absolute URL
img_url = f'https://spaceimages-mars.com/{img_url_rel}'
img_url


# In[218]:


df = pd.read_html('https://galaxyfacts-mars.com')[0]
df.columns=['description', 'Mars', 'Earth']
df.set_index('description', inplace=True)
df


# In[219]:


df.to_html()


# ## Mars Hemisphere

# In[226]:


url = 'https://marshemispheres.com'
browser.visit(url)


# In[229]:


# 2. Create a list to hold the images and titles.
hemisphere_image_urls = []

# 3. Write code to retrieve the image urls and titles for each hemisphere.
for i in range(4):
    # Browse through each article
    browser.links.find_by_partial_text('Hemisphere')[i].click()
    
    # Parse the HTML
    html = browser.html
    hemi_soup = soup(html,'html.parser')
    
    # Scraping
    hemi_img_title = hemi_soup.find('h2', class_='title').text
    hemi_img_url_rel = hemi_soup.find('li').a.get('href')
    
#     # Store findings into a dictionary and append to list
#     hemispheres = {}
    hemi_img_url = f'https://marshemispheres.com/{hemi_img_url_rel}'
#     hemispheres['title'] = title
#     hemisphere_image_urls.append(hemispheres)
    
    hemispheres = {
        'hemi_img_url': hemi_img_url,
        'hemi_img_title':hemi_img_title
         
    }
    hemisphere_image_urls.append(hemispheres)
    # Browse back to repeat
    browser.back()




# In[230]:


browser.quit()


# In[231]:


hemisphere_image_urls


# In[ ]:




