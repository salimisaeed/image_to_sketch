# AUTHOR : saeed salimi shad
# ID INSTAGRAM : saeedsalimi_shad
# ID GITHUB : salimisaeed
import cv2
import matplotlib.pyplot as plt
#-------------------------------------------------------------------------------
def image_to_sketch(photo, k_size):
    """ A function that takes a photo as
     input and draws it in black and white """
    #Read Image
    img=cv2.imread(photo)
    # Convert to Grey Image
    grey_img=cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # Invert Image
    invert_img=cv2.bitwise_not(grey_img)
    #invert_img=255-grey_img
    blur_img=cv2.GaussianBlur(invert_img, (k_size,k_size),0)
    # Invert Blurred Image
    invblur_img=cv2.bitwise_not(blur_img)
    #invblur_img=255-blur_img
    sketch_img=cv2.divide(grey_img,invblur_img, scale=256.0)
    cv2.imwrite('sketch.jpg', sketch_img) #Custom name
    # Display sketch
    cv2.imshow('sketch image',sketch_img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
#Function calling
#-------------------------------------------------------------------------------
image_to_sketch(photo='new_face.jpg', k_size=25) #Function call
#The name of the image in the current directory
