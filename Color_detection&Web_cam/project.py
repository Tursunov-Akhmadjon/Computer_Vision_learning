import cv2 # Library for videos and images


cap = cv2.VideoCapture(0) # Activating a webcam

if not cap.isOpened(): #It gives an error if the webcam isn't working
    print("Error: Could not open webcam.")
    exit()

while True:
    # body 
    success, frame = cap.read() #2 variables 
   

    if not success: # If the read() function is not successfully executed, it throws an error.
        print("Error: Failed to capture image.")
        break

    mirrored_frame = cv2.flip(frame, 1) #The frame is flipped horizontally.   
    cv2.imshow('Webcam Feed', mirrored_frame) #Displaying frames

    
    if cv2.waitKey(1) & 0xFF == ord('s'): #Condition for stopping the process
        break


cap.release()
cv2.destroyAllWindows()
