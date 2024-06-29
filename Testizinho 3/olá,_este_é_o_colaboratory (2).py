# -*- coding: utf-8 -*-
"""Olá, este é o Colaboratory

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/notebooks/intro.ipynb
"""

//1
package main

import "fmt"

func inverter(palavra string) string {
    invertida:=" " // armazenar palavra ao contrario
    for i:= len(palavra)-1; i>=0; i--{
        invertida+=string(palavra[i])
    }
    return invertida
}

func main() {
    var quantidade int
    fmt.Scan(&quantidade)//quantidade de palavras

    var palavras []string=make([]string,quantidade)
    for i:= 0; i<quantidade; i++{
        fmt.Scan(&palavras[i])
    }

    for i:= 0; i<quantidade; i++{
        palavraInvertida:=inverter(palavras[i])
        fmt.Println(palavraInvertida)
    }
}//inventer string, complicado demais

//2
package main

import "fmt"

func troca(vetor []int, x, y int) {//troca dois numeros(?) de um vetor
	vetor[x], vetor[y] = vetor[y], vetor[x]
}


func trocaOpostosSeMenor(vetor []int) {//verifica e ve se precisa trocar numeros(?) opostos
	n := len(vetor)
	for i := 0; i < n/2; i++ {
		oposto := n - 1 - i//cada numero i tá oposto ao elemento n-1-i
		if i < oposto && vetor[i] < vetor[oposto] {
			troca(vetor, i, oposto)
		}
	}
}

func main() {
	var numCasos int
	fmt.Scanln(&numCasos)

	for caso := 0; caso < numCasos; caso++ {//cada caso de teste
		var t int//tamanho
		fmt.Scanln(&t)

		vetor := make([]int, t)
		for i := 0; i < t; i++ {
			fmt.Scan(&vetor[i])
		}

		trocaOpostosSeMenor(vetor)

		for i := 0; i < t; i++ {//imprime resultado
			fmt.Printf("%d ", vetor[i])
		}
		fmt.Println() // Quebra de linha(?)
	}
}//muito difícil, slk
//precisei buscar ajuda

//3
package main

import(
    "fmt"
    "sort"
    )

func main(){
    var q int
    fmt.Scan(&q)

    ordem:=make([]int,q)

    for i:=0;i<q;i++{
        fmt.Scanln(&ordem[i])
    }

    sort.Ints(ordem)
    fmt.Print(ordem)

}