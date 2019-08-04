import check
import pyqrcode as QR
import png
import tkinter
import interface


class Main:
    def __init__(self):
        # print('it works')
        checkStr = check.Check(test=True).getFiscalString()

        interface.UserInterface()

        # PNG TRYING
        # with open("./output/QR.png", "wb") as outputFile:
        #     qr = QR.create(checkStr)
        #     qr.png(outputFile, scale=4)

        # SVG TRYING
        with open("./output/QR.svg", "wb") as outputFile:
            qr = QR.QRCode(checkStr)
            qr.svg(file=outputFile, scale=4)


if __name__ == "__main__":
    Main()
    print("PROGRAM FINISH")
