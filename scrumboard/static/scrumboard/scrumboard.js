(function(){
    angular.module('scrumboard.demo', [])
    .controller('ScrumboardController', ['$scope', ScrumboardController])

    function ScrumboardController($scope){
        $scope.data = [
            {
                name: 'Django Demo',
                cards: [
                    {
                        title: 'Create a Model'
                    },
                    {
                        title: 'Create Serializers and API'
                    }, 
                    {
                        title: 'Make Migrations'

                    }
                ]
            }, 
            {
                name: 'Angular Demo',
                cards: [
                    {
                        title: 'Create HTML'
                    }, 
                    {
                        title: 'Add JavaScript code'
                    },
                    {
                        title: 'Use REST Framework'
                    }
                ]
            }
        ]
        $scope.add = function(list, title){
            var card = {
                title: title
            }
            list.cards.push(card)
        }
    }
}())