from .database import Database
from typing import Self, Optional
from sqlite3 import Cursor


#(cria uma instância de Item com quatro atributos) 
class Item:
    def __init__(
        self: Self,
        titulo: Optional[str],
        tipo: Optional[str],
        indicado_por: Optional[str] = None,
        id_item: Optional[int] = None
    ) -> None:
        
    #(atribui os valores dos parâmetros aos atributos da instância do Item.)
        self.titulo = titulo
        self.tipo = tipo
        self.indicado_por = indicado_por
        self.id_item = id_item


    #(método de classe usado para buscar um item pelo id.)
    @classmethod
    def id(cls, id: int) -> Self:
        with Database() as db:
            query = 'SELECT titulo, tipo, indicado_por FROM itens WHERE id = ?;'
            [[titulo, tipo, indicado_por]] = db.buscar_tudo(query, (id,))
        return cls(titulo, tipo, indicado_por, id)

    #(insere o item atual no banco de dados.)
    def salvar_item(self) -> None:
        with Database() as db:
            query = 'INSERT INTO itens (titulo, tipo, indicado_por) VALUES (?, ?, ?);'
            db.executar(query, (self.titulo, self.tipo, self.indicado_por))


    #(método de classe que retorna uma lista de todos os itens do banco.)
    @classmethod
    def obter_itens(cls) -> list[Self]:
        with Database() as db:
            query = 'SELECT titulo, tipo, indicado_por, id FROM itens;'
            resultados = db.buscar_tudo(query)
            return [cls(titulo, tipo, indicado, id) for titulo, tipo, indicado, id in resultados]

    #(remove o item do banco usando o id_item.)
    def excluir_item(self) -> Cursor:
        with Database() as db:
            return db.executar('DELETE FROM itens WHERE id = ?;', (self.id_item,))
    
    #(modifica os dados de um item existente no banco.)
    def atualizar_item(self) -> Cursor:
        with Database() as db:
            query = '''
UPDATE itens 
SET titulo = ?, tipo = ?, indicado_por = ?
WHERE id = ?;
            '''
            return db.executar(query, (self.titulo, self.tipo, self.indicado_por, self.id_item))