from PIL import Image
import matplotlib.pyplot as plt

img=Image.open('tiger.png')


def pixel_art(image, i_size, o_size): # i_size = input size, o_size = output size
    img=Image.open(image)

    #convert to small image
    small_img=img.resize(i_size,Image.BILINEAR)

    #resize to output size - (enlarging each pixel)
    res=small_img.resize(img.size, Image.NEAREST)

    #Save output image
    filename=f'tiger_{i_size[0]}x{i_size[1]}.png'
    res.save(filename)

    #Display images side by side
    plt.figure(figsize=(16,10))


    #original image
    plt.subplot(1,2,1)     
    plt.title('Original image', size=18)
    plt.imshow(img)   #display image
    plt.axis('off')   #hide axis

    #pixelated image
    plt.subplot(1,2,2)
    plt.title(f'Pixel Art {i_size[0]}x{i_size[1]}', size=18)
    plt.imshow(res)
    plt.axis('off')
    plt.savefig('temp.png')
    plt.show()
    

pixel_art(image='tiger.png',i_size=(80,80),o_size=img.size)

