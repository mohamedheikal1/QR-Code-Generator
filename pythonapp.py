#install all the libraries needed
#create a function that collects a text and converts it to a qr code  
#save the qr code as an image 
#run the function

import qrcode
def generate_qrcode(text):

    qr =qrcode.QRCode(
        version = 1,
        error_correction = qrcode.constants.ERROR_CORRECT_L,
        box_size = 20,
        border = 1,
    )   
    
    qr.add_data(text)
    qr.make(fit=True)
    img = qr.make_image(fill_color=input("Enter fill color for your QR : ").lower(), back_color=input("Enter back color for your QR :  ").lower())
    img.save(input("Enter your QR image name : ") + ".png")
    print(" QR code generated successfully ")

#url = input("Enter the url: ")
while True:
    generate_qrcode(input("Enter your link to generate your QR code: "))