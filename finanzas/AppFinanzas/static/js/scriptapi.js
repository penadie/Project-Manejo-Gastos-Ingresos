const fMonto =  /^-?[0-9]+([.])?([0-9]+)?$/;
//codigo funcionamiento api pagina.
$(
  function(){
    $("#clpTrans").submit(
      function(e){
        e.preventDefault();
        var validacion = true;
        if (!validaTexto("#clp", fMonto)){
            validacion = false;
            $("#clp").addClass("errorFormT");
            $("#hCLP").show();
        }if(!validacion){
          e.preventDefault();
        }else{
          $("#cInputClp").html("CLP$"+$("#clp").val());
          $.get('https://mindicador.cl/api', function(data){
            const valores = data;
            $("#clpToDolar").html("$"+parseFloat($("#clp").val()/valores.dolar.valor).toFixed(2));
            $("#clpToEuro").html("€"+parseFloat($("#clp").val()/valores.euro.valor).toFixed(2));
            $("#clpToUF").html(parseFloat($("#clp").val()/valores.uf.valor).toFixed(2)+"UF");
            $("#clpToBTC").html("BTC"+parseFloat(($("#clp").val()/valores.dolar.valor)/valores.bitcoin.valor).toFixed(5));
            $("#clp").val("");
          })
        }
      }
    );
    $("#dolarTrans").submit(
      function(e){
        e.preventDefault();
        var validacion = true;
        if (!validaTexto("#dolar", fMonto)){
            validacion = false;
            $("#dolar").addClass("errorFormT");
            $("#hDo").show();
        }if(!validacion){
          e.preventDefault();
        }else{
          $("#cInputDolar").html("USD$"+$("#dolar").val());
          $.get('https://mindicador.cl/api', function(data){
            const valD = data;
            $("#dolarToCLP").html("$"+parseFloat($("#dolar").val()*valD.dolar.valor).toFixed(2));
            $("#dolarToEuro").html("€"+parseFloat($("#dolar").val()*valD.dolar.valor/valD.euro.valor).toFixed(2));
            $("#dolarToUF").html(parseFloat($("#dolar").val()*valD.dolar.valor/valD.uf.valor).toFixed(2)+"UF");
            $("#dolarToBTC").html("BTC"+parseFloat(($("#dolar").val()/valD.bitcoin.valor)).toFixed(5));
            $("#dolar").val("");
          })
        }
      }
    );
    $("#euroTrans").submit(
      function(e){
        e.preventDefault();
        var validacion = true;
        if (!validaTexto("#euro", fMonto)){
            validacion = false;
            $("#euro").addClass("errorFormT");
            $("#hEu").show();
        }if(!validacion){
          e.preventDefault();
        }else{
          $("#cInputEu").html("€"+$("#euro").val());
          $.get('https://mindicador.cl/api', function(data){
            const valEu = data;
            $("#euroToCLP").html("CLP$"+parseFloat($("#euro").val()*valEu.euro.valor).toFixed(2));
            $("#euroToDolar").html("USD$"+parseFloat($("#euro").val()*valEu.euro.valor/valEu.dolar.valor).toFixed(2));
            $("#euroToUF").html(parseFloat($("#euro").val()*valEu.euro.valor/valEu.uf.valor).toFixed(2)+"$UF");
            $("#euroToBTC").html("BTC "+parseFloat(($("#euro").val()*valEu.euro.valor/valEu.dolar.valor/valEu.bitcoin.valor)).toFixed(5));
            $("#euro").val("");
          })
        }
      }
    );
    $("#clp").focusin(
      function(){
        $("#clp").removeClass("errorFormT");
        $("#hCLP").hide();
      }
    );
    $("#dolar").focusin(
        function(){
          $("#dolar").removeClass("errorFormT");
          $("#hDo").hide();
      }
    );
    $("#euro").focusin(
        function(){
          $("#euro").removeClass("errorFormT");
          $("#hEu").hide();
      }
    );
    
  }
);  

        