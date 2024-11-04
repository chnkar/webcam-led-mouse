import numpy as np 
import cv2
import mouse

  
  
# Capturing video through webcam 
webcam = cv2.VideoCapture(0) 

xpr = 0
ypr= 0
cnt=0
cntwhl = 0
#newl = 0

# Start a while loop 
while(1): 
      
    # Reading the video from the 
    # webcam in image frames 
    _, imageFrame = webcam.read() 
  
    # Convert the imageFrame in  
    # BGR(RGB color space) to  
    # HSV(hue-saturation-value) 
    # color space 
    hsvFrame = cv2.cvtColor(imageFrame, cv2.COLOR_BGR2HSV)
    
  
    # Set range for red color and  
    # define mask 

    red_lower = np.array([120, 70, 70], np.uint8) 
    red_upper = np.array([200, 255, 255], np.uint8) 
    red_mask = cv2.inRange(hsvFrame, red_lower, red_upper) 
        # Set range for green color and  
    # define mask 
    green_lower = np.array([25, 52, 15], np.uint8) 
    green_upper = np.array([102, 255, 255], np.uint8) 
    green_mask = cv2.inRange(hsvFrame, green_lower, green_upper) 
  
    # Set range for blue color and 
    # define mask 
    blue_lower = np.array([94, 80, 2], np.uint8) 
    blue_upper = np.array([120, 255, 255], np.uint8) 
    blue_mask = cv2.inRange(hsvFrame, blue_lower, blue_upper) 
      
    # Morphological Transform, Dilation 
    # for each color and bitwise_and operator 
    # between imageFrame and mask determines 
    # to detect only that particular color 
    kernel = np.ones((5, 5), "uint8") 
      
    # For red color 
    red_mask = cv2.dilate(red_mask, kernel) 
    res_red = cv2.bitwise_and(imageFrame, imageFrame,  
                              mask = red_mask) 
      
    # For green color 
    green_mask = cv2.dilate(green_mask, kernel) 
    res_green = cv2.bitwise_and(imageFrame, imageFrame, 
                                mask = green_mask) 
      
    # For blue color 
    blue_mask = cv2.dilate(blue_mask, kernel) 
    res_blue = cv2.bitwise_and(imageFrame, imageFrame, 
                               mask = blue_mask) 
   
    # Creating contour to track red color 
    contours, hierarchy = cv2.findContours(red_mask, 
                                           cv2.RETR_TREE, 
                                           cv2.CHAIN_APPROX_SIMPLE)

    
      
    for pic, contour in enumerate(contours): 
        area = cv2.contourArea(contour) 
        if(area > 100):
            #if (pic == 0):
            x, y, w, h = cv2.boundingRect(contour) 
            imageFrame = cv2.rectangle(imageFrame, (x, y),  
                                          (x + 80, y + 80),  
                                         (0, 0, 255), 2) 
              
            cv2.putText(imageFrame, "Red Colour", (x, y), 
                          cv2.FONT_HERSHEY_SIMPLEX, 1.0, 
                      (0, 0, 255))
            if (cntwhl-cnt > 1):
                 xpr = x
                 ypr = y
                 mouse.release(button='left')
                
            
            if (cntwhl-cnt == 1):
                    #mse.position =(nx + (x-xpr) , ny+(y - ypr))
                    if (pic == 0):
                        mouse.move((x-xpr)*4, (y-ypr)*0.2,absolute=False,duration=0.05)  
                        #print (x ,xpr,"\t",y ,ypr,"\t",nx,ny,"\n")
                        xpr = x
                        ypr = y
            
                
            cnt = cntwhl
            
            
  
    # Creating contour to track green color 
    contours, hierarchy = cv2.findContours(green_mask, 
                                           cv2.RETR_TREE, 
                                           cv2.CHAIN_APPROX_SIMPLE) 
    press = False  
    for pic, contour in enumerate(contours): 
        area = cv2.contourArea(contour) 
        if(area > 100):
            if (pic == 0):
                x, y, w, h = cv2.boundingRect(contour) 
                imageFrame = cv2.rectangle(imageFrame, (x, y),  
                                           (x + 80, y + 80), 
                                           (0, 255, 0), 2) 
              
                cv2.putText(imageFrame, "Green Colour", (x, y), 
                            cv2.FONT_HERSHEY_SIMPLEX,  
                            1.0, (0, 255, 0))
                #mouse.press(button='left')
                mouse.click(button='left')
                press = True 
  
   # if (press == False):
       # mouse.release(button='left')
    
    cntwhl += 1
    
    # Program Termination 
    cv2.imshow("Multiple Color Detection in Real-TIme", imageFrame) 
    if cv2.waitKey(10) & 0xFF == ord('q'): 
        webcam.release() 
        cv2.destroyAllWindows() 
        break
