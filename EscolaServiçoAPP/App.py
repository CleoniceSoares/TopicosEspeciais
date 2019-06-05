from flask import Flask, request
import sqlite3

app = Flask(__name__)

# listar todas as escolas cadastradas
@app.route("/escolas", methods = ["GET"])
def getEscolas():
    conn = sqlite3.connect("ifpb.db")
    cursor = conn.cursor()
    cursor.execute("""
        select * from tb_escola;
    """)
    for linha in cursor.fetchall():
        print (linha)
    conn.close()
    return("Escolas listadas com sucesso", 200)

# listar escola pelo id
@app.route("/escolas/<int:id>", methods = ["GET"])
def getEscolasId(id):
    conn = sqlite3.connect("ifpb.db")
    cursor = conn.cursor()
    cursor.execute("""
        select * from tb_escola where id_escola = ?;
    """, (id, ))

    for linha in cursor.fetchall():
        print (linha)
    conn.close()
    return("Escola listada com sucesso", 200)

# cadastrar uma escola
@app.route("/escola", methods = ["POST"])
def setEscola():
    print("Cadastrando escola.")
    id = request.form["id"]
    nome = request.form["nome"]
    logradouro = request.form["logradouro"]
    cidade = request.form["cidade"]
    conn = sqlite3.connect("ifpb.db")
    cursor = conn.cursor()
    cursor.execute("""
        insert into tb_escola(id_escola, nome, logradouro, cidade)
        values(?,?,?,?);
    """, (id, nome, logradouro, cidade))
    conn.commit()
    conn.close()
    return ("Dados cadastrados com sucesso.", 200)

# listar alunos cadastrados
@app.route("/alunos", methods = ["GET"])
def getAlunos():
    conn = sqlite3.connect("ifpb.db")
    cursor = conn.cursor()
    cursor.execute("""
        select * from tb_aluno;
    """)
    for linha in cursor.fetchall():
        print (linha)
    conn.close()
    return("Alunos listados com sucesso", 200)

# listar aluno pelo id
@app.route("/alunos/<int:id>", methods = ["GET"])
def getAlunosId(id):
    conn = sqlite3.connect("ifpb.db")
    cursor = conn.cursor()
    cursor.execute("""
        select * from tb_aluno where id_aluno = ?;
    """, (id, ))
    for linha in cursor.fetchall():
        print (linha)
    conn.close()
    return("Aluno listado com sucesso", 200)

# cadastrar um aluno
@app.route("/aluno", methods = ["POST"])
def setAluno():
    print("Cadastrando aluno.")
    id = request.form["id"]
    nome = request.form["nome"]
    matricula = request.form["matricula"]
    cpf = request.form["cpf"]
    nascimento = request.form["nascimento"]
    conn = sqlite3.connect("ifpb.db")
    cursor = conn.cursor()
    cursor.execute("""
        insert into tb_aluno(id_aluno, nome, matricula, cpf, nascimento)
        values(?,?,?,?,?);
    """, (id, nome, matricula, cpf, nascimento))
    conn.commit()
    conn.close()
    return ("Dados cadastrados com sucesso.", 200)

# listar todos os cursos
@app.route("/cursos", methods = ["GET"])
def getCursos():
    conn = sqlite3.connect("ifpb.db")
    cursor = conn.cursor()
    cursor.execute("""
        select * from tb_curso;
    """)
    for linha in cursor.fetchall():
        print (linha)
    conn.close()
    return("Cursos listados com sucesso", 200)

# listar curso pelo id
@app.route("/cursos/<int:id>", methods = ["GET"])
def getCursosId(id):
    conn = sqlite3.connect("ifpb.db")
    cursor = conn.cursor()
    cursor.execute("""
        select * from tb_curso where id_curso = ?;
    """, (id, ))
    for linha in cursor.fetchall():
        print (linha)
    conn.close()
    return("Curso listado com sucesso", 200)

# cadastrar um curso
@app.route("/curso", methods = ["POST"])
def setCurso():
    print("Cadastrando curso.")
    id = request.form["id"]
    nome = request.form["nome"]
    turno = request.form["turno"]
    conn = sqlite3.connect("ifpb.db")
    cursor = conn.cursor()
    cursor.execute("""
        insert into tb_curso(id_curso, nome, turno)
        values(?,?,?);
    """, (id, nome, turno))
    conn.commit()
    conn.close()
    return ("Dados cadastrados com sucesso.", 200)

# listar todas as turmas
@app.route("/turmas", methods = ["GET"])
def getTurmas():
    conn = sqlite3.connect("ifpb.db")
    cursor = conn.cursor()
    cursor.execute("""
        select * from tb_turma;
    """)
    for linha in cursor.fetchall():
        print (linha)
    conn.close()
    return("Turmas listadas com sucesso", 200)

# listar turma pelo id
@app.route("/turmas/<int:id>", methods = ["GET"])
def getTurmasId(id):
    conn = sqlite3.connect("ifpb.db")
    cursor = conn.cursor()
    cursor.execute("""
        select * from tb_turma where id_turma = ?;
    """, (id, ))
    for linha in cursor.fetchall():
        print (linha)
    conn.close()
    return("Turma listada com sucesso", 200)

# cadastrar uma turma
@app.route("/turma", methods = ["POST"])
def setTurma():
    print("Cadastrando turma.")
    conn = sqlite3.connect("ifpb.db")
    cursor = conn.cursor()
    id = request.form["id"]
    nome = request.form["nome"]
    curso = request.form["curso"]
    cursor = conn.cursor()
    cursor.execute("""
        insert into tb_turma(id_turma, nome, curso)
        values(?,?,?);
    """, (id, nome, curso))
    conn.commit()
    conn.close()
    return ("Dados cadastrados com sucesso.", 200)

# listar todas as disciplinas
@app.route("/disciplinas", methods = ["GET"])
def getDisciplinas():
    conn = sqlite3.connect("ifpb.db")
    cursor = conn.cursor()
    cursor.execute("""
        select * from tb_disciplina;
    """)
    for linha in cursor.fetchall():
        print (linha)
    conn.close()
    return("Disciplinas listadas com sucesso", 200)

# listar disciplina pelo id
@app.route("/disciplinas/<int:id>", methods = ["GET"])
def getDisciplinasId(id):
    conn = sqlite3.connect("ifpb.db")
    cursor = conn.cursor()
    cursor.execute("""
        select * from tb_disciplina where id_disciplina = ?;
    """, (id, ))
    for linha in cursor.fetchall():
        print (linha)
    conn.close()
    return("Disciplina listada com sucesso", 200)

# cadastrar uma disciplina
@app.route("/disciplina", methods = ["POST"])
def setDisciplina():
    print("Cadastrando disciplina.")
    conn = sqlite3.connect("ifpb.db")
    id = request.form["id"]
    nome = request.form["nome"]
    cursor = conn.cursor()
    cursor.execute("""
        insert into tb_disciplina(id_disciplina, nome)
        values(?,?);
    """,(id, nome))
    conn.commit()
    conn.close()
    return ("Dados cadastrados com sucesso.", 200)

if(__name__ == '__main__'):
    app.run(host='0.0.0.0', debug=True, use_reloader=True)
