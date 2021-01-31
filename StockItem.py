
class StockItem:
    def __init__(self, code, description, num_items):
        self.code = code
        self.description = description
        self.num_items = num_items

        print("created,", code, description, num_items)
    

    def update_Amount(self, newAmount):
        self.num_items = newAmount

        print("UPDATED AMOUNT:",self.code, self.description, self.num_items)

    def AddAmount(self, change):
        self.num_items = self.num_items + change

        print("ADDED AMOUNT:",self.code, self.description, self.num_items)

    def updateDescription(self, description):
        self.description = description

        print("UPDATED DESCRIPTION:",self.code, description)








