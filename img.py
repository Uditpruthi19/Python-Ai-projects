Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> 
def main():
    try:
        #Relative Path
        img = Image.open("C:\Users\Admin\Downloads\nt.jpg") 
        print img.mode
          
        #converting image to bitmap
        print img.tobitmap()
          
        print type(img.tobitmap())
    except IOError:
        pass
  
if __name__ == "__main__":
    main()