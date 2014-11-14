var celulaModulo = angular.module('celula-modulo', ['celula-servico']);

celulaModulo.directive('celulaForm', [function() {
    return {
        restrict: 'E',
        templateUrl: '/static/celula-angular/html/form.html',
        scope: {celulaSalva: '&'},
        controller : function($scope, CelulaAPI) {
            $scope.celula = {nome: 'nome', endereco: 'endereco'}
            $scope.executandoSalvamento = false;
            $scope.erros = {};

            $scope.salvar = function() {
                $scope.executandoSalvamento = true;
                $scope.erros = {};

                var promessa = CelulaAPI.salvar($scope.celula);

                promessa.success(function(celula) {
                    $scope.executandoSalvamento = false;
                    if($scope.celulaSalva != null) {
                        $scope.celulaSalva({'celula': celula})
                    }
                });

                promessa.error(function(erros) {
                    $scope.executandoSalvamento = false;
                    $scope.erros = erros;
                });
            }
        }
    };
}]);

celulaModulo.directive('celulaLinha', [function() {
    return {
        restrict: 'A',
        replace: true,
        templateUrl: '/static/celula-angular/html/linha.html',
        scope: {
            celula: '=',
            celulaDeletada: '&'
        },
        controller: function($scope, CelulaAPI) {
            $scope.apagandoFlag = false;

            $scope.deletar = function() {
                $scope.apagandoFlag = true;
                CelulaAPI.deletar($scope.celula.id).success(function() {
                    $scope.apagandoFlag = false;
                    if($scope.celulaDeletada != null) {
                        $scope.celulaDeletada();
                    }
                })
            }
        }
    };
}]);
