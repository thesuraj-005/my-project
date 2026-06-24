import cv2

image=cv2.imread('qr1.png')
detector=cv2.QRCodeDetector()
data,vertices_array,binary_qrcode=detector.detectAndDecode(image)

if vertices_array is not None and data:
    print(f"QR Data :{data}")
else:
    print("No data found")   
