from models.database import Database

# Teste do gerenciador de contexto
with Database() as db:
    db.executar(
        'INSERT INTO entretenimento (titulo_entretenimento, tipo_entretenimento) VALUES (?, ?);', 
        ('Usar o gerenciador de contexto',)
    )