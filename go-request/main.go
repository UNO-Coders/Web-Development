package main

import (
	"fmt"
	"io/ioutil"
	"log"
	"net/http"
)

func main() {
	//Creating a GET Request
	res, err := http.Get("Type in the URL of the api")
	//handle the error
	if err != nil {
		log.Fatal(err)
	}

	//read the body of the response from the API
	body, err := ioutil.ReadAll(res.Body)
	if err != nil {
		log.Fatal(err)
	}

	fmt.Printf("%+v", body)
}
