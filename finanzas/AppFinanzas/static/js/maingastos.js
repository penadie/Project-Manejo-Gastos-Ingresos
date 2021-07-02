
// tabla y storage local... solo me funciona la parte de que es una tabla. HALP

var formatoMonto= new RegExp("^[0-9]{3,15}$");
var formatoTipo= new RegExp("^[a-z A-Z]{4,25}$");  
function parseDate(str) {
function pad(x){return (((''+x).length==2) ? '' : '0') + x; }
var m = str.match(/^(\d{1,2})\/(\d{1,2})\/(\d{4})$/)
  , d = (m) ? new Date(m[3], m[2]-1, m[1]) : null
  , matchesPadded = (d&&(str==[pad(d.getDate()),pad(d.getMonth()+1),d.getFullYear()].join('/')))
  , matchesNonPadded = (d&&(str==[d.getDate(),d.getMonth()+1,d.getFullYear()].join('/')));
return (matchesPadded || matchesNonPadded) ? d : null;
}
$(
  function(){
    render();
    $("#formG").submit (
      function(e){
        e.preventDefault();
        var valido = true;
        const fechaG = document.getElementById('fechaG')        
        if(!validaTexto("#montoG", formatoMonto)) {
          valido = false;
          $("#montoG").addClass("errorFormT");
          $("#hMontoG").show();
        }if (parseDate(fechaG.value)==null) {
          valido = false;
          $("#fechaG").addClass("errorFormT");
          $("#hFechaG").show();
        }if (!validaTexto("#tipoG", formatoTipo)) {
          valido = false;
          $("#tipoG").addClass("errorFormT");
          $("#hTipoG").show();
        }if(!valido){
          $("#alert").show();
          e.preventDefault();
        }
        else{
          const montoG = document.getElementById('montoG');
          const tipoG = document.getElementById('tipoG');
          alert("Datos Fueron ingresados en la tabla");
          const gastosText = [tipoG.value,fechaG.value,montoG.value];
          montoG.value = '';
          fechaG.value = '';
          tipoG.value = '';
          gastos.push(gastosText);
          actualizaIng(gastos);
          render();
        }
      }
    );
    $("#montoG").focusin(
        function(){
          $("#alert").hide();
          $("#montoG").removeClass("errorFormT");
          $("#hMontoG").hide();
      }
    );
    $("#fechaG").focusin(
        function(){
          $("#alert").hide();
          $("#fechaG").removeClass("errorFormT");
          $("#hFechaG").hide();
      }
    );
    $("#tipoG").focusin(
        function(){
          $("#alert").hide();
          $("#tipoG").removeClass("errorFormT");
          $("#hTipoG").hide();
      }
    );
  }
)