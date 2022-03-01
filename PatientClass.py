class Patient:
    def __init__(self, patID, patName, address, phone, vet_status):
        self.__id = int(patID)
        self.__patName = patName
        self.__address = address
        self.__phone = phone
        self.__vet_status = vet_status

    def get_patID(self):
        return self.__id

    def get_patName(self):
        return self.__patName

    def get_address(self):
        return self.__address

    def get_phone(self):
        return self.__phone

    def get_vet_status(self):
        return self.__vet_status
