from flask import Flask, request, jsonify
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
    escolas = []
    for linha in cursor.fetchall():
        escola = {
            "id" : linha[0],
            "nome" : linha[1],
            "logradouro" : linha[2],
            "cidade" : linha[3]
        }
        escolas.append(escola)
    conn.close()
    return jsonify(escolas)

# listar escola pelo id
@app.route("/escolas/<int:id>", methods = ["GET"])
def getEscolasId(id):
    conn = sqlite3.connect("ifpb.db")
    cursor = conn.cursor()
    cursor.execute("""
        select * from tb_escola where id_escola = ?;
    """, (id, ))

    linha = cursor.fetchone()
    escola = {
        "id" : linha[0],
        "nome" : linha[1],
        "logradouro" : linha[2],
        "cidade" : linha[3]
    }

    conn.close()
    return jsonify(escola)

# cadastrar uma escola
@app.route("/escola", methods = ["POST"])
def setEscola():
    print("Cadastrando escola.")
    escola = request.get_json()
    nome = escola["nome"]
    logradouro = escola["logradouro"]
    cidade = escola["cidade"]
    conn = sqlite3.connect("ifpb.db")
    cursor = conn.cursor()

    cursor.execute("""
        insert into tb_escola(nome, logradouro, cidade)
        values(?,?,?);
    """, (nome, logradouro, cidade))
    conn.commit()
    conn.close()

    id = cursor.lastrowid
    escola["id"] = id

    return jsonify(escola)

# listar alunos cadastrados
@app.route("/alunos", methods = ["GET"])
def getAlunos():
    conn = sqlite3.connect("ifpb.db")
    cursor = conn.cursor()
    cursor.execute("""
        select * from tb_aluno;
    """)
    alunos = []
    for linha in cursor.fetchall():
        aluno = {
            "id" : linha[0],
            "nome" : linha[1],
            "matricula" : linha[2],
            "cpf" : linha[3],
            "nascimento" : linha[4]
        }
        alunos.append(aluno)
    conn.close()
    return jsonify(alunos)

# listar aluno pelo id
@app.route("/alunos/<int:id>", methods = ["GET"])
def getAlunosId(id):
    conn = sqlite3.connect("ifpb.db")
    cursor = conn.cursor()
    cursor.execute("""
        select * from tb_aluno where id_aluno = ?;
    """, (id, ))

    linha = cursor.fetchone()
    aluno = {
        "id" : linha[0],
        "nome" : linha[1],
        "matricula" : linha[2],
        "cpf" : linha[3],
        "nascimento" : linha[4]
    }

    conn.close()
    return jsonify(aluno)

# cadastrar um aluno
@app.route("/aluno", methods = ["POST"])
def setAluno():
    print("Cadastrando aluno.")
    aluno = request.get_json()
    nome = aluno["nome"]
    matricula = aluno["matricula"]
    cpf = aluno["cpf"]
    nascimento = aluno["nascimento"]
    conn = sqlite3.connect("ifpb.db")
    cursor = conn.cursor()
    cursor.execute("""
        insert into tb_aluno(nome, matricula, cpf, nascimento)
        values(?,?,?,?);
    """, (nome, matricula, cpf, nascimento))
    conn.commit()
    conn.close()
    id = cursor.lastrowid
    aluno["id"] = id
    return jsonify(aluno)

# listar todos os cursos
@app.route("/cursos", methods = ["GET"])
def getCursos():
    conn = sqlite3.connect("ifpb.db")
    cursor = conn.cursor()
    cursor.execute("""
        select * from tb_curso;
    """)
    cursos = []
    for linha in cursor.fetchall():
        curso = {
            "id" : linha[0],
            "nome" : linha[1],
            "turno" : linha[2]
        }
        cursos.append(curso)
    conn.close()
    return jsonify(cursos)

# listar curso pelo id
@app.route("/cursos/<int:id>", methods = ["GET"])
def getCursosId(id):
    conn = sqlite3.connect("ifpb.db")
    cursor = conn.cursor()
    cursor.execute("""
        select * from tb_curso where id_curso = ?;
    """, (id, ))
    linha = cursor.fetchone()
    curso = {
        "id" : linha[0],
        "nome" : linha[1],
        "turno" : linha[2]
    }
    conn.close()
    return jsonify(curso)

# cadastrar um curso
@app.route("/curso", methods = ["POST"])
def setCurso():
    print("Cadastrando curso.")
    curso = request.get_json()
    nome = curso["nome"]
    turno = curso["turno"]
    conn = sqlite3.connect("ifpb.db")
    cursor = conn.cursor()
    cursor.execute("""
        insert into tb_curso(nome, turno)
        values(?,?);
    """, (nome, turno))
    conn.commit()
    conn.close()
    id = cursor.lastrowid
    curso["id"] = id
    return jsonify(curso)

# listar todas as turmas
@app.route("/turmas", methods = ["GET"])
def getTurmas():
    conn = sqlite3.connect("ifpb.db")
    cursor = conn.cursor()
    cursor.execute("""
        select * from tb_turma;
    """)
    turmas = []
    for linha in cursor.fetchall():
        turma = {
            "id" : linha[0],
            "nome" : linha[1],
            "curso" : linha[2]
        }
        turmas.append(turma)
    conn.close()
    return jsonify(turmas)

# listar turma pelo id
@app.route("/turmas/<int:id>", methods = ["GET"])
def getTurmasId(id):
    conn = sqlite3.connect("ifpb.db")
    cursor = conn.cursor()
    cursor.execute("""
        select * from tb_turma where id_turma = ?;
    """, (id, ))
    linha = cursor.fetchone()
    turma = {
        "id" : linha[0],
        "nome" : linha[1],
        "curso" : linha[2]
    }
    conn.close()
    return jsonify(turma)

# cadastrar uma turma
@app.route("/turma", methods = ["POST"])
def setTurma():
    print("Cadastrando turma.")
    turma = request.get_json()
    conn = sqlite3.connect("ifpb.db")
    cursor = conn.cursor()
    nome = turma["nome"]
    curso = turma["curso"]
    cursor = conn.cursor()
    cursor.execute("""
        insert into tb_turma(nome, curso)
        values(?,?);
    """, (nome, curso))
    conn.commit()
    conn.close()

    id = cursor.lastrowid
    turma["id"] = id

    return jsonify(turma)

# listar todas as disciplinas
@app.route("/disciplinas", methods = ["GET"])
def getDisciplinas():
    conn = sqlite3.connect("ifpb.db")
    cursor = conn.cursor()
    cursor.execute("""
        select * from tb_disciplina;
    """)
    disciplinas = []
    for linha in cursor.fetchall():
        disciplina = {
            "id" : linha[0],
            "nome" : linha[1]
        }
        disciplinas.append(disciplina)
    conn.close()
    return jsonify(disciplinas)

# listar disciplina pelo id
@app.route("/disciplinas/<int:id>", methods = ["GET"])
def getDisciplinasId(id):
    conn = sqlite3.connect("ifpb.db")
    cursor = conn.cursor()
    cursor.execute("""
        select * from tb_disciplina where id_disciplina = ?;
    """, (id, ))

    linha = cursor.fetchone()
    disciplina = {
        "id" : linha[0],
        "nome" : linha[1]
    }
    conn.close()
    return jsonify(disciplina)

# cadastrar uma disciplina
@app.route("/disciplina", methods = ["POST"])
def setDisciplina():
    print("Cadastrando disciplina.")
    disciplina = request.get_json()
    conn = sqlite3.connect("ifpb.db")
    cursor = conn.cursor()
    nome = disciplina["nome"]
    cursor.execute("""
        insert into tb_disciplina(nome)
        values(?);
    """, (nome, ))
    conn.commit()
    conn.close()
    id = cursor.lastrowid
    disciplina["id"] = id
    return jsonify(disciplina)

if(__name__ == '__main__'):
    app.run(host='0.0.0.0', debug=True, use_reloader=True)
