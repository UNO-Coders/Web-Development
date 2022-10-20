package main

import(
	"net/http"
	"github.com/gin-gonic/gin"
)

type book struct{
	ID string`json:"id"`
	Name string`json:"name"`
}

var books = []book{
	{ID : "1", Name: "The Psychology of Money"},
	{ID :"2", Name: "Atomic Habits"},
}
func getBooks(c *gin.Context){
	c.IndentedJSON(http.StatusOK, books)
}

func main(){
	router:= gin.Default()
	
	//declare the endpoint
	router.GET("/books", getBooks)

	//declare the port number
	router.Run("localhost:9000")

}