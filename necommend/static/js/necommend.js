// document.write("<script type=\"text/javascript\" src=\"Rtoaster.js\"></script>");



angular.module('necommend', [])
  .controller('necommendController', function(){
    this.test = function test() {
      window.alert("hello");
      console.log("hello");
    };
    this.insertAd = function insertAd() {
      var a = Math.floor(Math.random()*100)%8;
      var b = (a===0) ? true:false;
      console.log(b);
      return b;
      // return true;
    };
    this.tellNecosUrl = function tellNecosUrl(url) {
      console.log(url);
      Rtoaster.track(url);
    };
 });
