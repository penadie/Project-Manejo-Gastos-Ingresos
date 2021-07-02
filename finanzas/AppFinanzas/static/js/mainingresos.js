
// regexp para validar datos ingresados en el formulario
var formatoMonto= new RegExp("^[0-9]{3,15}$");
const formatoFecha =  /^(((0[1-9]|[12]\d|3[01])\/(0[13578]|1[02])\/((19|[2-9]\d)\d{2}))|((0[1-9]|[12]\d|30)\/(0[13456789]|1[012])\/((19|[2-9]\d)\d{2}))|((0[1-9]|1\d|2[0-8])\/02\/((19|[2-9]\d)\d{2}))|(29\/02\/((1[6-9]|[2-9]\d)(0[48]|[2468][048]|[13579][26])|(([1][26]|[2468][048]|[3579][26])00))))$/g;
var formatoTipo= new RegExp("^[a-z A-Z]{4,25}$");

$(
  function(){
    render();
    $("#formulario").submit (
      function(e){
        e.preventDefault();
        var valido = true;
        if(!validaTexto("#monto", formatoMonto)) {
          valido = false;
          $("#monto").addClass("errorFormT");
          $("#hMonto").show();
        }if (!validaTexto("#fecha", formatoFecha)) {
          valido = false;
          $("#fecha").addClass("errorFormT");
          $("#hFecha").show();
        }if (!validaTexto("#tipo", formatoTipo)) {
          valido = false;
          $("#tipo").addClass("errorFormT");
          $("#hTipo").show();
        }if(!valido){
          $("#alert").show();
          e.preventDefault();
        }
        else{
          alert("Se ingresaron datos correctamente");
          const monto = document.getElementById('monto');
          const fecha = document.getElementById('fecha');
          const tipo = document.getElementById('tipo');
          const ingresoText = [tipo.value,fecha.value,monto.value];
          monto.value = '';
          fecha.value = '';
          tipo.value = '';
          ingresos.push(ingresoText);
          actualizaIng(ingresos);
          render();
        }
      }
    );
    $("#monto").focusin(
        function(){
          $("#alert").hide();
          $("#monto").removeClass("errorFormT");
          $("#hMonto").hide();
      }
    );
    $("#fecha").focusin(
        function(){
          $("#alert").hide();
          $("#fecha").removeClass("errorFormT");
          $("#hFecha").hide();
      }
    );
    $("#tipo").focusin(
        function(){
          $("#alert").hide();
          $("#tipo").removeClass("errorFormT");
          $("#hTipo").hide();
      }
    );
  }
)