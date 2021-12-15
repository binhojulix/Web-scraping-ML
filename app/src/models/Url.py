class URL:

  
    def __init__(self):
 
    
    @staticmethod
    def proxima(page_number):
        num_pages = 5
        num_items = 50
  
        current_page = (page_number-1) * num_items+1
        if(page_number<=1):
            uri = "Desde_{}_".format(current_page)
        return "https://celulares.mercadolibre.com.ar/celular-smarphones_{}NoIndex_True".format(uri)