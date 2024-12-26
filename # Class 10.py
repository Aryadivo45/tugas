# Class
class Pesawat:
    # Attribute
    def __init__(self, pd):
        self.Merek = ""
        self.Nama = ""
        self.pd = pd

    # Method 1
    def printPst(self):
        print("Merek Pesawat : ", self.Merek)
        print("Nama Pesawat : ", self.Nama)
        print("Jenis Pesawat : ", self.pd)
    
    # Method 2
    def Her(self, kondisi):
        print("Telah Siap Maintenance")
        print(kondisi)

# Objek
Pst1 = Pesawat("Boing")
Pst2 = Pesawat("Airbus")

# values
Pst1.Merek = "Boing"
Pst1.Nama = "Boing737"
Pst2.Merek = "AirbusA380"
Pst2.Nama = "Garuda"

# pemanggilan method
Pst2.printPst()
Pst2.Her("Telah Siap Maintenance")
        
