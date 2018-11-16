function enviardados(){
	if(document.dados.tx_nome.value=="" ){
		alert( "Preencha o campo NOME corretamente!" );
		document.dados.tx_nome.focus();
		return false;
	}
	if( document.dados.tx_email.value=="" || document.dados.tx_email.value.indexOf('@')==-1 || document.dados.tx_email.value.indexOf('.')==-1 ){
		alert( "Preencha o campo E-MAIL corretamente!" );
		document.dados.tx_email.focus();
		return false;
	}
	if (document.dados.tx_mensagem.value==""){
		alert( "Preencha o campo MENSAGEM!" );
		document.dados.tx_mensagem.focus();
		return false;
	}
	if (document.dados.tx_mensagem.value.length < 20 ){
		alert( "É necessario preencher o campo MENSAGEM com no minimo 20 caracteres!" );
		document.dados.tx_mensagem.focus();
		return false;
	}
	//Pssando nome para valor
	var valor = document.getElementById("fname").value;
	//Criar objeto do tipo Date()
	var data = new Date();
	//Configurando tempo de vida do cookie
	data.setTime(data.getTime() + 360000);
	//Criando a estrutura do cookie
	document.cookie = "cookie01="+valor+"; expires="+data.toUTCString()+"; path=/";
	//alert(valor);

	//var user = document.cookie.split("=");
	//alert("Valor: " + user[1]);
	alert( "Enviada com sucesso!" );
	return true;
}
