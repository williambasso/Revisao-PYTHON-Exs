class Produto:

    @property
    def frutas(self):
        return self.__frutas
    @frutas.setter
    def frutas(self,frutas):
        self.__frutas = frutas

    @property
    def verduras(self):
        return self.__verduras

    @verduras.setter
    def verduras(self,verduras):
        self.__verduras = verduras

    @property
    def legumes(self):
        return self.__legumes

    @legumes.setter
    def legumes(self,legumes):
        self.__legumes = legumes
    
    @property
    def preco(self):
        return self.__preco
    
    @preco.setter
    def preco(self,preco):
        self.__preco = preco
    
    

