This project aims to create a "0g" mouse that relies on image(colour) recognition for mouse movements
It consists of hardware:

  2 different colour led's , one for tracking mouse movement and other one for left click action
  
  Switches to control LED's
  
  an old glove to mount it on along with battery
  
  Webcam pointed from display down to table
  

![IMG_20241104_193752 (2)](https://github.com/user-attachments/assets/49940dcc-a477-4430-b08f-95d4290d4bc9)



Webcam is caliberated by using webcam software (i used camo studio) to decrease brightness of image so its easy to recognise distinct LED's

Project uses OpenCV, pip mouse and numpy library

Only a prototype, future improvements could be

  using apriltags to reallign image for better recognition
  
  decreasing brightness in python program itself
  
  better way for colour limits setting
  
First project, dont judge! :)
