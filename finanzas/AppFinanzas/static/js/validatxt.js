// validar patrones regexp

function validaTexto(idInput,patron){
    return $(idInput).val().match(patron) ? true : false;
  }