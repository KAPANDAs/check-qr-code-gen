import sys
import time


class Check(object):
    dateTime: str = None
    operationType: str = None
    fiscalNumber: str = None
    fiscalSign: str = None
    fiscalDocument: str = None
    fiscalSumm: str = None
    fiscalString: str = None

    def __init__(self, test):
        """
        Creating check entinty
        """
        self.operationType = "1"
        if test:
            self.setTestValues()
        else:
            self.setDateOfCheck()
            self.setFiscalSumm()
            self.setFiscalNumber()
            self.setFiscalDocument()
            self.setFiscalSign()
        self.fiscalString = f"t={self.dateTime}&s={self.fiscalSumm}&fn={self.fiscalNumber}&i={self.fiscalDocument}&fp={self.fiscalSign}&n={self.operationType}"

    def setDateOfCheck(self):
        """
        Setting up date of check
        """
        print("Введите дату и время чека (ГОД МЕСЯЦ ДЕНЬ . ЧАСЫ МИНУТЫ):\n")
        self.dateTime = input()
        self.dateTime = self.dateTime.replace(" ", "")
        self.dateTime = self.dateTime.replace(".", "T")
        self.dateTime += "00"

    def setFiscalNumber(self):
        """
        Setting up fiscal number of check
        """
        print("Введите номер фискального накопителя (ФН на чеке):\n")
        self.fiscalNumber = input()

    def setFiscalDocument(self):
        """
        Setting up fiscal document number
        """
        print("Введите номер фискального документа (ФД на чеке):\n")
        self.fiscalDocument = input()

    def setFiscalSign(self):
        """
        Setting up fiscal sign number
        """
        print("Введите фискальный признак (ФП на чеке):\n")
        self.fiscalSign = input()

    def setFiscalSumm(self):
        """
        Setting up summ of check
        """
        print("Введите сумму чека:\n")
        self.fiscalSumm = input()

    def setTestValues(self):
        """
        Test values for debugging
        """
        self.dateTime = "20190706T214300"
        self.fiscalSumm = "243.97"
        self.fiscalDocument = "148845"
        self.fiscalSign = "1778932019"
        self.fiscalNumber = "9282000100194184"

    def getFiscalString(self):
        """
        Returning string for QR Code FNS format 
        """
        return self.fiscalString
