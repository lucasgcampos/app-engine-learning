var app = angular.module('', []);

app.directive('', [function () {
    return {
        restrict: '',
        templateUrl: '',
        scope: {},
        controller: function($scope) {

            promessa.success(function() {

            }) ;

            promessa.error(function(erros) {
               $scope.erros = erros;
               $scope.executandoSalvamento = false;
            });
        }
    };
}]);

filmeModulo.directive('filmeLinha', [function() {
    return {
        restrict: 'A',
        templateUrl: '',
        controller: function($scope, FilmeAPI) {

        }
    }
}]);