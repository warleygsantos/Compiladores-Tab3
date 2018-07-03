inicio
	varinicio
		B real;
		idade int;
		nome lit;
	varfim;

	escreva "Digite seu nome: ";
	leia nome;
	escreva "Digite sua idade: ";
	leia idade;
	escreva "Digite um numero: ";
	leia B;

	se(idade<18) entao
		escreva "Voce nao pode dirigir\n";
	fimse
	se(idade>=18) entao
		escreva "Voce ja pode ser preso\n";
		se(idade>100) entao
			escreva "Voce eh muito velho!\n";
		fimse
	fimse
	B<-idade + B;
	escreva B;
fim
