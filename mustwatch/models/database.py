from sqlite3 import Connection, connect, Cursor
from types import TracebackType
from typing import Any, Self, Optional, Type
from dotenv import load_dotenv
import traceback
import os
   #^
   #|
   #|
#(importações)


#(variável de ambiente para o caminho do banco de dados, com um valor padrão se não estiver definido)
load_dotenv()
DB_PATH = os.getenv('DATABASE', './data/mustwatch.sqlite3')


 #(função para inicializar o banco de dados, criando a tabela "itens" se ela não existir)
def init_db(db_name: str = DB_PATH) -> None:
    with connect(db_name) as conn:
        conn.execute("""
CREATE TABLE IF NOT EXISTS itens (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    titulo TEXT NOT NULL,
    tipo TEXT NOT NULL,
    indicado_por TEXT
);
        """)


#(classe Database para gerenciar a conexão com o banco de dados e executar comandos SQL)
class Database:
    def __init__(self, db_name: str = DB_PATH) -> None:
        self.connection: Connection = connect(db_name)
        self.cursor: Cursor = self.connection.cursor()

    #executar um comando SQL, com parâmetros opcionais, e retornar o cursor para possíveis operações adicionais.

    def executar(self, query: str, params: tuple = ()) -> Cursor:
        self.cursor.execute(query, params)
        self.connection.commit()
        return self.cursor
    

    #buscar dados do banco de dados e retornar os resultados como uma lista.

    def buscar_tudo(self, query: str, params: tuple = ()) -> list[Any]:
        self.cursor.execute(query, params)
        return self.cursor.fetchall()
    

    #(fechar a conexão com o banco de dados.)
    def close(self) -> None:
        self.connection.close()

    #(implementação dos métodos de contexto para usar a classe com "with")

    def __enter__(self) -> Self:
        return self
    
    #(tratar exceções e garantir que a conexão seja fechada ao sair do bloco "with")
    
    def __exit__(
        self,
        exc_type: Optional[Type[BaseException]],
        exc_value: Optional[BaseException],
        tb: Optional[TracebackType]
    ) -> None:
        if exc_type:
            traceback.print_tb(tb)
        self.close()