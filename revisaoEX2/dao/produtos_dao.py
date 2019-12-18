from dao.base_dao import BaseDao
from model.produtos import Produtos


class ProdutosDao(BaseDao):
    def inserir_frutas(self, frutas, preco):
        # FRUTAS
        comando_sql_insert = f"""INSERT INTO produtos
        (produto, preco, fk_tipo)
        VALUES
        (
            '{frutas}'
            ,'{preco}'
            ,1
        )"""
        return super().inserir(comando_sql_insert)

    def inserir_legumes(self, legumes, preco):
        # legumes
        comando_sql_insert = f"""INSERT INTO produtos
        (produto, preco, fk_tipo)
        VALUES
        (
            '{legumes}'
            ,'{preco}'
            ,3
        )"""
        return super().inserir(comando_sql_insert)

    def inserir_verduras(self, verduras, preco):
        # verduras
        comando_sql_insert = f"""INSERT INTO produtos
        (produto, preco, fk_tipo)
        VALUES
        (
            '{verduras}'
            ,'{preco}'
            ,2
        )"""
        return super().inserir(comando_sql_insert)
    
    def has_nome(self,produto):
        comando_sql_buscar_nome = f"SELECT * from produtos where produto like '%{produto}%' limit 1 "
        a = super().buscar_por_id(comando_sql_buscar_nome)
        return(True if a else False)
