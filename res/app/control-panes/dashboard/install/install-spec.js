describe('InstallCtrl', function() {
    beforeEach(angular.mock.module(require('./').name))

    var scope, ctrl

    beforeEach(inject(function($rootScope, $controller) {
        scope = $rootScope.$new()
        ctrl = $controller('InstallCtrl', {$scope: scope})
    }))

    it('should ...', inject(function() {
        expect(1).toEqual(1)
    }))
})
