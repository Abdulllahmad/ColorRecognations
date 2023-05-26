import cv2

cap = cv2.VideoCapture(1)



while True:
    _, frame = cap.read()
    hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    height, width, _= frame.shape
    
    
    center_x = int(width / 2)
    center_y = int(height / 2)

    pixel_center_color = hsv_frame[center_y, center_x]
    color_h = pixel_center_color[0]
    color_s = pixel_center_color[1]
    color_v = pixel_center_color[2]

    color = "Undefined"

    if color_h < 5:
        color = "Red"
    elif color_s < 40:
        color = "White"
    elif color_v < 20:
        color = "Black"
    elif color_h < 22:
        color = "Orange"
    elif color_h < 43:
        color = "Yellow"
    elif color_h < 75:
        color = "Green"  
    elif color_h < 129:
        color = "Blue"
    elif color_h < 170:
        color = "Violet"
    else:
        color = "No Recognition"

    pixel_center_bgr = frame[center_y, center_x]
    b, g, r, = int(pixel_center_color[0]),int(pixel_center_color[1]),int(pixel_center_color[2])
    cv2.putText(frame, color, (40,90), 0, 4, (b, g, r), 4)


    
    
    print(pixel_center_color)
    cv2.circle(frame, (center_x, center_y), 10,(255,0,0), 6)


    cv2.imshow("Frame", frame)
    key = cv2.waitKey(1)
    if key == 27:
        break

cap.release()
cv2.destroyAllWindows()


