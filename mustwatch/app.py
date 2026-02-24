from flask import Flask, render_template, request, redirect, url_for
from mustwatch.models.item import Item
from mustwatch.models.database import init_db
app = Flask(__name__)

#(Inicializando o banco de dados)

init_db()

#(rota para a página inicial, renderizando o template home.html)

@app.route('/')
def home():
    return render_template('home.html', titulo='Must Watch')

#(rota para a página de lista, que lida com GET e POST para exibir e adicionar itens)

@app.route('/lista', methods=['GET', 'POST'])
def lista():
    if request.method == 'POST':
        titulo = request.form['titulo']
        tipo = request.form['tipo']
        indicado_por = request.form['indicado_por']
        Item(titulo, tipo, indicado_por).salvar_item()

    #(obtendo todos os itens do banco de dados e renderizando o template lista.html)

    itens = Item.obter_itens()
    return render_template('lista.html', titulo='Must Watch', itens=itens)


#(rota para deletar um item da lista usando o id do item)

@app.route('/delete/<int:idItem>')
def delete(idItem):
    Item.id(idItem).excluir_item()
    return redirect(url_for('lista'))

#(rota para atualizar um item da lista usando o id do item, lida com GET para exibir o formulário e POST para salvar as alterações)

@app.route('/update/<int:idItem>', methods=['GET', 'POST'])
def update(idItem):
    if request.method == 'POST':
        titulo = request.form['titulo']
        tipo = request.form['tipo']
        indicado_por = request.form['indicado_por']
        Item(titulo, tipo, indicado_por, idItem).atualizar_item()
        return redirect(url_for('lista'))
    
    #(obtendo o item selecionado pelo id e renderizando o template lista.html com os dados do item para edição)

    return render_template(
        'lista.html',
        titulo=f'Editando item {idItem}',
        itens=Item.obter_itens(),
        item_selecionado=Item.id(idItem)
    )

#(executando a aplicação Flask em modo debug)

if __name__ == '__main__':
    app.run(debug=True)