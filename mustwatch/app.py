from flask import Flask, render_template, request, redirect, url_for
from mustwatch.models.item import Item
from mustwatch.models.database import init_db
app = Flask(__name__)

init_db()

@app.route('/')
def home():
    return render_template('home.html', titulo='Must Watch')

@app.route('/lista', methods=['GET', 'POST'])
def lista():
    if request.method == 'POST':
        titulo = request.form['titulo']
        tipo = request.form['tipo']
        indicado_por = request.form['indicado_por']
        Item(titulo, tipo, indicado_por).salvar_item()

    itens = Item.obter_itens()
    return render_template('lista.html', titulo='Must Watch', itens=itens)

@app.route('/delete/<int:idItem>')
def delete(idItem):
    Item.id(idItem).excluir_item()
    return redirect(url_for('lista'))

@app.route('/update/<int:idItem>', methods=['GET', 'POST'])
def update(idItem):
    if request.method == 'POST':
        titulo = request.form['titulo']
        tipo = request.form['tipo']
        indicado_por = request.form['indicado_por']
        Item(titulo, tipo, indicado_por, idItem).atualizar_item()
        return redirect(url_for('lista'))

    return render_template(
        'lista.html',
        titulo=f'Editando item {idItem}',
        itens=Item.obter_itens(),
        item_selecionado=Item.id(idItem)
    )

if __name__ == '__main__':
    app.run(debug=True)