(function(){
    'use strict';
    angular.module('scrumboard.demo', [])
    .controller('ScrumboardController', ['$scope','$http', ScrumboardController]);

    function ScrumboardController($scope, $http){
        $scope.add = function(list, title){
            var card = {
                list: list.id,
                title: title
            };
            $http.post('/scrumboard/card/', card)
            .then(function(response){
                list.cards.push(response.data);
            },function(){
                alert('Can not create card');
            });
        };
        $scope.data = []
        $http.get('/scrumboard/lists').then(function(response){
            $scope.data = response.data;
        });
    };
}());