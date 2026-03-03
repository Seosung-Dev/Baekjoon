package main

import "fmt"

func main() {
	var N int
	var F int

	fmt.Scan(&N, &F)

	var Base int = (N / 100) * 100
	var I int

	for I = 0; I < 100; I++ {
		if F == 0 || (Base+I)%F == 0 {
			fmt.Printf("%02d\n", I)
			return
		}
	}
}