from .database import Database
from typing import Self, Any, Optional
from sqlite3 import Cursor

class Item:
    def __init__(
        self: Self,
        titulo: Optional[str],
        tipo: Optional[str],
        indicado_por: Optional[str] = None,
        id_item: Optional[int] = None
    ) -> None:
        self.titulo = titulo
        self.tipo = tipo
        self.indicado_por = indicado_por
        self.id_item = id_item

    @classmethod
    def id(cls, id: int) -> Self:
        with Database() as db:
            query = 'SELECT titulo, tipo, indicado_por FROM itens WHERE id = ?;'
            [[titulo, tipo, indicado_por]] = db.buscar_tudo(query, (id,))
        return cls(titulo, tipo, indicado_por, id)

    def salvar_item(self) -> None:
        with Database() as db:
            query = 'INSERT INTO itens (titulo, tipo, indicado_por) VALUES (?, ?, ?);'
            db.executar(query, (self.titulo, self.tipo, self.indicado_por))

    @classmethod
    def obter_itens(cls) -> list[Self]:
        with Database() as db:
            query = 'SELECT titulo, tipo, indicado_por, id FROM itens;'
            resultados = db.buscar_tudo(query)
            return [cls(titulo, tipo, indicado, id) for titulo, tipo, indicado, id in resultados]

    def excluir_item(self) -> Cursor:
        with Database() as db:
            return db.executar('DELETE FROM itens WHERE id = ?;', (self.id_item,))

    def atualizar_item(self) -> Cursor:
        with Database() as db:
            query = '''
UPDATE itens 
SET titulo = ?, tipo = ?, indicado_por = ?
WHERE id = ?;
            '''
            return db.executar(query, (self.titulo, self.tipo, self.indicado_por, self.id_item))