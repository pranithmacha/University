(function(){

	var macsite = angular.module('macsite', ['ngMaterial','ngRoute']);

    macsite.config(function($interpolateProvider) {
        $interpolateProvider.startSymbol('{$');
        $interpolateProvider.endSymbol('$}');
    });
    macsite.controller('macsiteController',function($scope){
        $scope.value="navya";
    })

})();