import cv2
import dropbox
import time
import random

start_time=time.time()

def take_snapshot()
number=random.randint(0,100)
#initializing cv2
videoCaptureObject=cv2.VideoCapture(0)
result=True
while(result)
 #read the frames while the cmaera is on
 ret,frame=videoCaptureObject.read()
 #cv2.imwrite() method is used to save an image to any storage device
 img_name="img"+str(number)+".png"
 cv2.imwrite(img_name,frame)
 start_time=time.time
 result=False
return img_name
print("snapshot taken")
#release the camera
videoCaptureObject.release()
#closes all the windows
cv2.destroyAllWindows()

def upload_file(img_name):
    access_token="sl.A4T1x2s8D0qEG4gFKvEIE58qMFIC7IjFwZEk4GRlUY2h1KKXiG_SGXWQ9hQoQ7_GbdNzoXMR1bcGoQ0niXb61WgLOti2rWxVBzG1MT9RXYN84-4okVCjYrjELbEx4bZb9uSKW68"
    file=img_name
    file_from=file
    file_to="/testFolder"+(img_name)
    dbx= dropbox.Dropbox(access_token)

    with open(file_from , 'rb') as f:
        dbx.files_upload(f.read(), file_to_mode = dropbox.files.WriteMode.overwrite
        print("file Upload")
def main():
while(True):
    if((time.time() - start_time >= 300))
    name=take_snapshot()
upload_file(name)
main()