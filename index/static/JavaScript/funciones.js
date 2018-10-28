//LETRAS
function sololetras(e){
    key = e.keyCode || e.which;
    teclado = String.fromCharCode(key).toLowerCase();                 
    letras = "abcdefghijklmnñopqrstuvwxyz";
    especiales = "8-37-38-46-164";
    teclado_especial = false;

    for(var i in especiales){ 
        if (key==especiales[i]) {
            teclado_especial=true;
            break;
        }
    }

    if(letras.indexOf(teclado)== -1 && !teclado_especial) {
        return false;
    }
}
//NUMEROS
function solonumeros(e){
    key = e.keyCode || e.which;
    teclado = String.fromCharCode(key);
    numero = "0123456789";
    especiales = "8-37-38-46";
    teclado_especial = false;

    for(var i in especiales) {
        if (key == especiales){
            teclado_especial = true;
            break;
        }
    }

    if (numero.indexOf(teclado)== -1 && !teclado_especial){
        return false;
    }
}
//RUT 
function validarRut(){
    var rut = document.datos.rut.value;
    var arr = rut.split("");
    var largoArr = arr.length;
    var sumatoria = 0;
    var multiplo = 2;
    if(arr[largoArr-2] != "-"){
        alert("Rut invalido");
        return false;
    }
    else{
        for(x=largoArr-3; x>=0; x--){
        
            if(multiplo >= 8){
                multiplo = 2;
            }
            sumatoria = sumatoria + arr[x]*multiplo;
            multiplo++;
        
        }
        var verificador =11 - sumatoria%11;
        switch(verificador){
            case 10: //K
                if(arr[largoArr-1] == "k" || arr[largoArr-1] == "K"){
                    
                    //alert("digito verificador correcto");
                    return true;
                }
                else{
                    alert("digito verificador incorrecto");
                    return false;
                }
            break;


            case 11: //0
                if(arr[largoArr-1] == "0"){
                        //alert("digito verificador correcto");
                        return true;
                    }
                    else{
                        alert("digito verificador incorrecto");
                        return false;
                    }
            break;

            default:
                if(arr[largoArr-1] == verificador){
                        //alert("digito verificador correcto");
                        return true;
                    }
                    else{
                        alert("digito verificador incorrecto");
                        return false;
                    }
            break;
        }
    }            
}

//NUMEROS Y "K" DE RUT
function rutk(e){
    key = e.keyCode || e.which;
    teclado = String.fromCharCode(key);
    numero = "0123456789kK-";
    especiales = "8-37-38-46";
    teclado_especial = false;

    for(var i in especiales) {
        if (key == especiales){
            teclado_especial = true;
            break;
        }
    }

    if (numero.indexOf(teclado)== -1 && !teclado_especial){
        return false;
    }
}

//CARRUSEL
$(window).load(function() {
    $('.flexslider').flexslider({
        touch: true,
        pauseOnAction: false,
        pauseOnHover: false,
    });
});








