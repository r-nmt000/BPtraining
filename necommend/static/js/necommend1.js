angular.module('necommend1', [])
  .controller('necommendController', function(){
    this.test = function test() {
      window.alert("hello");
      console.log("hello");
    };
 });
