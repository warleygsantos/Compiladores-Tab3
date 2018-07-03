#include<stdio.h>
#include<stdlib.h>
typedef char literal[256];int main(){int T0;int T1;int T2;double T3;double B;int idade;literal nome;



printf("%s","Digite seu nome: ");scanf("%s",nome);printf("%s","Digite sua idade: ");scanf("%d",&idade);printf("%s","Digite um numero: ");scanf("%lf",&B);T0 = idade < 18;if(T0){printf("%s","Voce nao pode dirigir\n");}T1 = idade >= 18;if(T1){printf("%s","Voce ja pode ser preso\n");T2 = idade > 100;if(T2){printf("%s","Voce eh muito velho!\n");}}T3 = idade + B;B = T3;printf("%g",B);return 0;}