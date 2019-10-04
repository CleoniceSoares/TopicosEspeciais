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
