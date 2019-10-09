// Inicializar o módulo.
let nomeApp = 'EscolaWebApp'
let modulos = []
var app = angular.module(nomeApp, modulos);

// Estrutura básica para uma função no controller
let meuPrimeiroController = function($scope){
  $scope.logradouro = "Outro Valor";

  $scope.numero1 = 0;
  $scope.numero2 = 0;

  $scope.somar = function(numero1, numero2) {
    $scope.resultado = numero1 + numero2;
  }
}

app.controller('MeuPrimeiroController', meuPrimeiroController);

let meuSegundoController = function($scope){
}

app.controller('MeuSegundoController', meuSegundoController);

let alunoController = function() {
    $scope.nome = "Nome";
    $scope.matricula = "Matricula";
    $scope.cpf = "CPF";
    $scope.nascimento = ;
    $scope.fk_id_endereco = 0;
    $scope.fk_id_curso = 0;
}

app.controller("AlunoController", alunoController);

let cursoController = function() {
    $scope.nome = "Nome";
    $scope.fk_id_turno = 0;
}

app.controller("CursoController", cursoController);

let disciplinaController() {
    $scope.nome = "Nome";
    $scope.fk_id_professor = 0;
}

app.controller("DisciplinaController", disciplinaController);

let turmaController = function() {
    $scope.nome = "Nome";
    $scope.fk_id_endereco = 0;
}

app.controller("TurmaController", turmaController);

let enderecoController = function() {
    $scope.logradouro = "Logradouro";
    $scope.complemento = "Complemento";
    $scope.bairro = "Bairro";
    $scope.cep = "CEP";
    $scope.numero = 0;
}

app.controller("EnderecoController", enderecoController);

let escolaController = function() {
    $scope.nome = "Nome";
    $scope.fk_id_endereco = 0;
    $scope.fk_id_campus = 0;
}

app.controller("EscolaController", escolaController);

let campusController = function() {
    $scope.sigla = "Sigla";
    $scope.cidade = "Cidade";
}

app.controller("CampusController", campusController);

let professorController = function() {
    $scope.nome = "Nome";
    $scope.fk_id_endereco = 0;
}

app.controller("ProfessorController", professorController);

let turnoController = function() {
    $scope.nome = "Nome";
}

app.controller("TurnoController", turnoController);
