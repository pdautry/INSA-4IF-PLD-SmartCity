'use strict';

/**
 * @ngdoc function
 * @name smartCityFrontEndApp.controller:MapCtrl
 * @description
 * # MapCtrl
 * Controller of the smartCityFrontEndApp
 */
angular.module('smartCityFrontEndApp')
  .controller('MapCtrl', function ($scope) {
    $scope.displayedView = 0;
    $scope.prev = function() {
        if ($scope.displayedView > 0) {
            $scope.displayedView--;
        }
    };
    $scope.next = function() {
        if ($scope.displayedView < 2) {
            $scope.displayedView++;
        }
    };
  });
