import qrcode

source = input('Enter the text or URL: ')
file_name = input('Enter the filename: ')

img = qrcode.make(source)
img.save(f'{file_name}.png')
print(f'QR code generated and saved as {file_name}.png')