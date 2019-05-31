import sqlite3
conn = sqlite3.connect('Escola.db')

cursor = conn.cursor()

cursor.execute("""
    create table tb_aluno(
        id_aluno integer not null primary key autoincrement,
        nome varchar(45) not null,
        matricula varchar(12) not null,
        cpf varchar(11) not null,
        nascimento date not null
        );
""")
cursor.execute("""
    create table tb_curso(
        id_curso integer not null primary key autoincrement,
        nome varchar(45),
        turno varchar(1)
        );
""")
cursor.execute("""
    create table tb_turma(
        id_turma integer not null primary key autoincrement,
        fk_id_curso integer
        );
""")
print ('Tabelas criadas com sucesso')

cursor.close()
