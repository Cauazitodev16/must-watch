from mustwatch.models.item import Item
from mustwatch.models.database import init_db

init_db()

#(Criando um item e salvando no banco de dados)

item = Item(
    titulo="Interestelar",
    tipo="Filme",
    indicado_por="Ednaldo Pereira"
)

 #Salvando o item no banco de dados usando o método salvar_item()

item.salvar_item()

itens = Item.obter_itens()
for i in itens:
    print(i)