let app = angular.module('ericaSantosOsteopada', []);

app.controller('mainCtrl', function ($scope, $http, $window) {
    // Variables
    let nav_items = document.querySelectorAll(".nav-item");

    // Functions
    $scope.showNavMenu = function (nav_item_expansive_element) {
        nav_item_expansive_element.classList.add("expanded");
    };

    $scope.hideNavMenu = function (nav_item_expansive_element) {
       nav_item_expansive_element.classList.remove("expanded");
    };

    // Function Calls
    for (let i=0; i<nav_items.length; i++) {
        if (nav_items[i].classList.contains("nav-item-expansive")) {
          nav_items[i].addEventListener("mouseover", function () {$scope.showNavMenu(nav_items[i])});
          nav_items[i].addEventListener("mouseout", function () {$scope.hideNavMenu(nav_items[i])});
        }
    }

});