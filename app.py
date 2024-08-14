import qrcode

url = input("Enter the URL: ")
file_name = input("Enter the file name: ")
img = qrcode.make(url)
img.save(file_name + ".png")
print(f"QR code generated successfully! File name: {file_name}")