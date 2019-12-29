import cv2

camera = cv2.VideoCapture(0)
a=0

while True:
    a=a+1
    check, frame = camera.read()
    print(check)
    print(frame)

    #gray=cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    #cv2.imshow("capturing",gray)
    cv2.imshow("capturing",frame)

    key =cv2.waitKey(1)
    if key == ord('y'):
        break

print(a)
camera.release()
cv2.destroyAllWindows
