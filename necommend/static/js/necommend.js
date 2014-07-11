angular.module('necommend', [])
  .controller('necommendController', function(){
    var adCount = 0;
    var i = 0;
    this.test = function test() {
      console.log('angular test clicked');
    };
    this.insertAd = function insertAd(bunnerNum) {
      var a = Math.floor(Math.random()*100)%8;
      if (((adCount===0) && (bunnerNum===0))||
          ((adCount===1) && (bunnerNum===1))||
          ((adCount===2) && (bunnerNum===2)) ) {
        i++;
        console.log(i + " times");
        console.log("adCount is " + adCount);
        console.log("bunnerNum is " + bunnerNum);
        console.log("a is " + a);
        console.log("answer is " + (a===0));
        if ( a===0 ) {
          adCount++;
          console.log("return true");
          return true;
        }else{
          return false;
        }
      }
      else {
        return false;
      }
    };
    this.tellNecosUrl = function tellNecosUrl(url) {
      Rtoaster.track(url);
    };
  });

// angular.element(document.getElementsByClassName('slide')).on('transitionend webkitTransitionEnd oTransitionEnd otransitionend MSTransitionEnd', function() {
//   console.log('animation ended');});

// angular.element(document.getElementsByClassName('thumbnail')).on('click',
//     function() {console.log('clicked');}
// $(".testbutton").on("click", function(){console.log("clicked");});
$(function () {
     $('.slides').on('transitionend webkitTransitionEnd oTransitionEnd otransitionend MSTransitionEnd click','.slide',
         function(){console.log('clicked')});
});

     // $('testbutton').on('transitionend webkitTransitionEnd oTransitionEnd otransitionend MSTransitionEnd click',
     //     function(){console.log('clicked')});
