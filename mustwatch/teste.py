from mustwatch.models.item import Item
from mustwatch.models.database import init_db

init_db()

item = Item(
    titulo="Interestelar",
    tipo="Filme",
    indicado_por="Ednaldo Pereira"
)

item.salvar_item()

itens = Item.obter_itens()
for i in itens:
    print(i)