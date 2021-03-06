$(document).on('ready',inicio); // Js que nos permite gestionar el cobro del endoso de cancelación a declaración.

function inicio () { // Función que inicia las variables y los eventos de los controles
	activarMenu();
	buscarConstanciasCanceladas();
}

var activarMenu = function(){ // Función que agrega la clase active al menu principal para saber en que parte se esta trabajando del sistema
	$('.menu_principal li:first-child').removeClass('active');
	$('.menu_principal li:eq(27)').addClass('active');
}

var buscarConstanciasCanceladas = function(){ // Función que nos permite obtener la informacion de las constancias a declaración canceladas que se encuentran disponibles para pagar mediante la función obtener_constancias_canceladas_declaracion.
	Dajaxice.Cobranza.obtener_constancias_canceladas_declaracion(cargarConstanciasAPagar);
}

var cargarConstanciasAPagar = function(datosConstancias){ // Callback de la función buscarConstanciasCanceladas para mostrar en la lista la información de las constancias a declaración que fueron canceladas.
	var items = [];
	
	if(datosConstancias.constancias)
	{
		constancias = datosConstancias.constancias;
		
		for(rowArreglo=0;rowArreglo<constancias.length;rowArreglo++)
		{
			linkGenerarPagoPrima = "<a href='#' title='Generar cobro de prima en deposito' onclick='abrirCobroConstanciaCancelada($(this));'><img src='/static/img/usd.png' /></a>";
				items.push({IdEndosoCancelacion:constancias[rowArreglo][0], Constancia: "Constancia: " + constancias[rowArreglo][11], FolioEndoso: "Endoso: " + constancias[rowArreglo][2],
				FechaEndoso: "Fecha de Endoso: " + constancias[rowArreglo][1],Vigencia:"Vigencia: "+ (constancias[rowArreglo][4] + " al " + constancias[rowArreglo][5]),
				Moneda:"Moneda: " + constancias[rowArreglo][12],Nombre:"Nombre: "+constancias[rowArreglo][6],
				Rfc:"RFC: " + constancias[rowArreglo][7], Monto:"Monto: " + (constancias[rowArreglo][10]).toCurrencyString(),
				pagoPrima:linkGenerarPagoPrima});
		}
	}
	
	options = {
	        item: 	"<li><div style='display: none;'><span class='IdEndosoCancelacion'></span></div>" +
	        		"<div class='row'>" +
	        		"<span class='Constancia span3'></span>" +
	        		"<span class='FolioEndoso span3'></span>" +
	        		"<span class='Vigencia span4'></span>" +
	        		"<span class='pagoPrima'></span>" +
	        		"</div>" +	        		
	        		"<div class='row'><span class='FechaEndoso span3'></span>" +
	        		"<span class='Moneda span3'></span>"+
	        		"<span class='Monto span4'></span>" +
	        		"</div>" +
	        		"<div class='row'><span class='Nombre span6'></span>" +
	        		"<span class='Rfc span3'></span>" +
	        		"</div>" +
	        		"</li>",
	        valueNames: [ 'IdConstancia', 'Constancia', 'Solicitud', 'Vigencia', 'Moneda', 'Nombre', 'Rfc', 'Monto', 'pagoPrima'],
	        plugins: [
	            [ 'fuzzySearch' ]
	        ]
	};
	
    var featureList = new List('lovely-things-list', options, items);

    $('.search-fuzzy').keyup(function() {
        featureList.fuzzySearch($(this).val());
    });		
}

var abrirCobroConstanciaCancelada = function(pagoPrima){ // Función que nos permite abrir la plantilla cobroconstanciacancelada.html la cual le pasamos el id  del endoso.
	pagoSeleccionado = pagoPrima.closest("li");
	location.href = '/CobroEndosoCancelacion/' + pagoSeleccionado.children()[0].innerText;
}

Number.prototype.toCurrencyString = function(){
	return "$ " + Math.floor(this).toLocaleString() + (this % 1).toFixed(4).toLocaleString().replace(/^0/,''); 
}