class Procedure:
    def __init__(self, proName, proDate, practitioner, charges, nameID):
        self.__procedure = proName
        self.__proDate = proDate
        self.__practitioner = practitioner
        self.__charges = int(charges)
        self.__id = int(nameID)

    def get_proName(self):
        return self.__procedure

    def get_proDate(self):
        return self.__proDate

    def get_practitioner(self):
        return self.__practitioner

    def get_charges(self):
        return self.__charges

    def get_nameID(self):
        return self.__id
