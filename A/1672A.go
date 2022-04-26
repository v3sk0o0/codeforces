package main

import (
	"fmt"
)

func main() {

	var testcase int
	fmt.Scan(&testcase)

	for i := 0; i < testcase; i++ {
		var number int
		fmt.Scan(&number)

		a := make([]int, number)
		result := 0
		for j := 0; j < number; j++ {
			fmt.Scan(&a[j])
			result += a[j]
		}

		result -= number
		if result%2 == 0 {
			fmt.Println("maomao90")
		} else {
			fmt.Println("errorgorn")
		}
	}
}
