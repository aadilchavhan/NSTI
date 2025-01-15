                # Link Extractor and Saver

# import requests
# from bs4 import BeautifulSoup
# from urllib.parse import urljoin
 
# def urls_list(url):
 
#         response=requests.get(url)
       
#         soup=BeautifulSoup(response.text,"html.parser")
 
#         links=[]
#         for tag in soup.find_all('a',href=True):
#             url1=urljoin(url,tag['href'])
#             links.append(url1)
#         return links
 
# def xyz(links,filename):
#     with open(filename,'w') as file:
#           for link in links:
#                file.write(link)
#     print(f'Links saved : {filename}')
         
   
# if __name__=="__main__":
#     url="https://www.cricbuzz.com/"
#     links=urls_list(url)
#     if links:
#          xyz(links,"Aadil.txt")
#          print(f'Links: {links}')
#          for link in links:
#               print(link)

'''____________________________________________________________'''



                # Image Scraper and Downloader

# import os
# import requests
# from bs4 import BeautifulSoup
# from urllib.parse import urljoin

# def xyz(url):
#     response = requests.get(url)
#     soup = BeautifulSoup(response.text, "html.parser")

#     images = []
#     for image in soup.find_all('img', src=True):
#         img_url = urljoin(url, image['src'])
#         images.append(img_url)

#     return images

# def xyz1(images, directory):
#     if not os.path.exists(directory):
#         os.makedirs(directory)

#     for index, img_url in enumerate(images):
#         img_data = requests.get(img_url).content
#         name = f'image{index + 1}.jpeg'
#         path = os.path.join(directory, name)

#         with open(path, 'wb') as file:
#             file.write(img_data)

#         print(f'Image saved at: {path}')

# if __name__ == "__main__":
#     url = "https://dyavolx.com/"
#     images = xyz(url)
#     if images:
#         xyz1(images, 'Images')


'''____________________________________________________________'''


                # Image Scraper with Debugging

                
import os
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

def abcd(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # Print the HTML content for debugging
    print(f"HTML Content: {soup.prettify()}")  
    
    images = []
    for image in soup.find_all('img', src=True):
        img1 = urljoin(url, image['src'])
        images.append(img1)
    
    print(f'Images are: {images}')
    for image in images:
        print(image)
    
    return images  # Return the list of images

def abcd1(images, directory):
    if not os.path.exists(directory):
        os.makedirs(directory)
        print(f'Directory created: {directory}')
    
    for x, image1 in enumerate(images):
        img1 = requests.get(image1).content
        name = f'image{x+1}.jpeg'
        path = os.path.join(directory, name)
        
        with open(path, 'wb') as file1:
            file1.write(img1)
        
        print(f'Saved image: {path}')

if __name__ == "__main__":
    url = "https://aimicrodegree.org/"
    images = abcd(url)
    if images:
        abcd1(images, 'Images')
