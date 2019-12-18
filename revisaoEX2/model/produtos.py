class Produtos:

    @property
    def frutas(self):
        return self.__frutas

    def set_frutas(self,frutas):
        self.__frutas = frutas

    @property
    def verduras(self):
        return self.__verduras
    
    def set_verduras(self,verduras):
        self.__verduras = verduras

    @property
    def legumes(self):
        return self.__legumes

    def set_legumes(self,legumes):
        self.__legumes = legumes
    
    @property
    def preco(self):
        return self.__preco

    def set_precos(self,preco):
        self.__preco = preco