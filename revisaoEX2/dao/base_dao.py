import MySQLdb

class BaseDao:
    def __init__(self):
        self.conexao = MySQLdb.connect(host="mysql.topskills.study", database="topskills06", user="topskills06", passwd="William2019" )
        self.cursor = self.conexao.cursor()

    def inserir(self, comando_sql_insert):
        self.cursor.execute(comando_sql_insert)
        self.conexao.commit()
        id_gerado = self.cursor.lastrowid
        return id_gerado
    
    def buscar_por_id(self, comando_sql_buscar_id):
        self.cursor.execute(comando_sql_buscar_id)
        return self.cursor.fetchone()