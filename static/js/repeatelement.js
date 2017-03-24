var el = $(".repeat-me").get(0);
var numRepeat = $(el).attr("numRepeat");

for(var i = 0;i < numRepeat;i++){    
    var newEl = $(el).after(el.cloneNode(true));   
}