
from StockItem import StockItem


class StockTracker(StockItem):
    def __init__(self, code, description, num_items):
        self.Storage = [] 
        super().__init__(code, description, num_items)                                        #lets stockitem class handle these paramters, so we dont need to repeat self.code, self.description etc.
    
    #Allows to create new stock item objects
    def Add_StockItem(self):
        self.Storage.append([self.code, self.description, self.num_items])