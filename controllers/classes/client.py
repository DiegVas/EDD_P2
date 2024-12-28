class client:
    def __init__(self, dpi, name, last_name, gender, phone, address):
        self.dpi:int = dpi
        self.name:str = name
        self.lastName:str = last_name
        self.gender:str = gender
        self.phone:int = phone
        self.address:str = address

    def setter(self, data: __init__):
        self.dpi = data.dpi
        self.name = data.name
        self.lastName = data.lastName
        self.gender = data.gender
        self.phone = data.phone
        self.address = data.address
