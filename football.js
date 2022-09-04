
//document.write("noder")
$(document).ready(function(){
    $.ajax({
        type: "GET",
        url: "http://127.0.0.1:5000/matches",
        success: function (response){
            var teams=JSON.parse(response);
            //document.getElementById("test").innerHTML=response;
            autocomplete(document.getElementById("myInput"),teams,Object.keys(teams).length);
        }
    })
});

function autocomplete(inp, dict, length){
    var curr;
    inp.addEventListener("input",function(e){
        var a, b, i, val=this.value;
        closeAllLists();
        if(!val) {return false;}
        curr=-1;
        a = document.createElement("DIV");
        a.setAttribute("id", this.id + "autocomplete-list");
        a.setAttribute("class", "autocomplete-items");
        this.parentNode.appendChild(a);
        for (i=0;i<length;i++){
            if(dict[i][1].substr(0, val.length).toUpperCase()==val.toUpperCase()){
                b=document.createElement("DIV");
                b.innerHTML = "<strong>" + dict[i][1].substr(0, val.length) + "</strong>";
                b.innerHTML += dict[i][1].substr(val.length);
                b.innerHTML += "<input type='hidden' value='" + dict[i][1] + "'>";
                b.addEventListener("click",function (e){
                   inp.value=this.getElementsByTagName("input")[0].value;
                   closeAllLists();
                });
                a.appendChild(b);
            }
        }
    });
    inp.addEventListener("keydown", function(e){
        var x = document.getElementById(this.id + "autocomplete-list");
        if(x) x=x.getElementsByTagName("div");
        if(e.keyCode==40){
            curr++;
            addActive(x);
        }else if (e.keyCode==38){
            curr--;
            addActive(x);
        }else if (e.keyCode==13){
            e.preventDefault();
            if(curr>-1){
                if(x) x[curr].click();
            }
        }
    });
    function addActive(x){
        if (!x) return false;
        removeActive(x);
        if (current >= x.length) curr = 0;
        if (curr < 0) curr = (x.length - 1);
        x[curr].classList.add("autocomplete-active");
    }
    function removeActive(x){
        for (var i = 0; i < x.length; i++) {
            x[i].classList.remove("autocomplete-active");
        }
    }
    function closeAllLists(elmnt){
        var x = document.getElementsByClassName("autocomplete-items");
        for (var i = 0; i < x.length; i++) {
            if (elmnt != x[i] && elmnt != inp) {
                x[i].parentNode.removeChild(x[i]);
            }
        }
    }
    document.addEventListener("click",function(e){
        closeAllLists(e.target);
    });
}