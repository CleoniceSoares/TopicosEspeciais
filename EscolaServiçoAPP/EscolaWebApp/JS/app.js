// Inicializar o módulo.
let nomeApp = 'EscolaWebApp'
let modulos = []
var app = angular.module(nomeApp, modulos);

// Estrutura básica para uma função no controller

let homeController = function($scope){
  $scope.nome = "";

  $scope.desejarBoasVindas = function() {
  let nome = $scope.nome;
  $scope.mensagem = "Olá, " + nome;
  }
}

app.controller('HomeController', homeController);

let alunoController = function($scope) {
    $scope.nome = "";
    $scope.matricula = "";
    $scope.cpf = "";
    $scope.nascimento = "";
    $scope.fk_id_endereco = 0;
    $scope.fk_id_curso = 0;
}

app.controller("AlunoController", alunoController);

let cursoController = function($scope) {
    $scope.nome = "";
    $scope.fk_id_turno = 0;
}

app.controller("CursoController", cursoController);

let disciplinaController = function($scope) {
    $scope.nome = "";
    $scope.fk_id_professor = 0;
}

app.controller("DisciplinaController", disciplinaController);

let turmaController = function($scope) {
    $scope.nome = "";
    $scope.fk_id_endereco = 0;
}

app.controller("TurmaController", turmaController);

let enderecoController = function($scope) {
    $scope.logradouro = "";
    $scope.complemento = "";
    $scope.bairro = "";
    $scope.cep = "";
    $scope.numero = 0;
}

app.controller("EnderecoController", enderecoController);

let escolaController = function($scope) {
    $scope.nome = "";
    $scope.fk_id_endereco = 0;
    $scope.fk_id_campus = 0;
}

app.controller("EscolaController", escolaController);

let campusController = function($scope) {
    $scope.sigla = "";
    $scope.cidade = "";
}

app.controller("CampusController", campusController);

let professorController = function($scope) {
    $scope.nome = "";
    $scope.fk_id_endereco = 0;
}

app.controller("ProfessorController", professorController);

let turnoController = function($scope) {
    $scope.nome = "";
}

app.controller("TurnoController", turnoController);
