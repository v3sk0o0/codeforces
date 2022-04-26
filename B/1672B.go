package main

import (
	"fmt"
)

func main() {

	var testcase int
	fmt.Scan(&testcase)

	for i := 0; i < testcase; i++ {

		var inputString string
		fmt.Scan(&inputString)

		numberOfA := 0
		numberOfB := 0

		if len(inputString) < 2 {
			fmt.Println("NO")
			continue
		}

		raisedFlag := false
		for _, char := range inputString {

			if string(char) == "A" {
				numberOfA += 1
			}
			if string(char) == "B" {
				numberOfB += 1
			}

			if numberOfB > numberOfA {
				fmt.Println("NO")
				raisedFlag = true
				break
			}

		}
		if raisedFlag == true {
			continue
		}

		if string(inputString[len(inputString)-1:]) == "B" {
			fmt.Println("YES")
		} else {
			fmt.Println("No")
		}
	}

}
