Agenda em Python usando Flask
Este Projeto foi elaborado por Cauãzito, para permitir o aprendizado de conceitos como o padrão de projeto MVC (Model-View-Controller), framework Flask e seus componentes, variáveis de ambiente, paradigma de programação orientado a objetos e reforço de fundamentos da linguagem de programação Python.

Para implementar este projeto localmente, siga os seguintes passos:

Faça fork deste repositório, clicando no botão Fork

Clone seu repositório localmente:

git clone <url_repositorio>
Abra o projeto utilizando seu IDE preferido

Crie, preferencialmente, um ambiente virtual utilizando sua versão do Python >3.12.10

python -m venv .venv
Ative seu ambiente virtual.

 No bash:

 ~~~bashsource .venv/Scripts/activate
 ~~~ 

 No PowerShell:
 ~~~powershell
 .venv\Scripts\Activate.ps1
 ~~~
Instale todas as dependências constantes no arquivo requeriments.txt; ~~python pip install -r requeriments.txt

Copie o arquivo .env.example, cole na raiz do projeto e renomeie a copia para .env example

Edite o arquivo .env para defenir o caminho do seu banco de dados, na constante DATABASE

Rode a aplicação no Python utilizando o comando:

flask run
Acesse a aplicação no endereço de porta indicados no terminal. Exemplo: https://127.0.0.1:5000