import check
import pyqrcode as QR
import png


class Main:
    def __init__(self):
        # print('it works')
        checkStr = check.Check(test=True).getFiscalString()

        # PNG TRYING
        # with open('./output/QR.png', 'wb') as outputFile:
        #     qr = QR.create(checkStr)
        #     qr.png(outputFile)

        # SVG TRYING
        with open("./output/QR.svg", "wb") as outputFile:
            qr = QR.QRCode(checkStr)
            qr.svg(file=outputFile)


if __name__ == "__main__":
    print("PROGRAM START")
    Main()
    print("PROGRAM FINISH")
