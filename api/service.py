from models import ItemModel

class ItemService:
    def __init__(self):
        self.model = ItemModel()
        
    def create_item(self, params):
        return self.model.create(params["title"], params["description"])