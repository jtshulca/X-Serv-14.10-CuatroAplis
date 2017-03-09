#!/usr/bin/python3

import webapp

class suma(webapp.app):
    def parse(self, request, rest):
        return rest.split('/')[1:]
    
    def process(self, parsedRequest):
	        
        num1 = int(parsedRequest[0])
        num2 = int(parsedRequest[1])    
        suma = num1 + num2
        return ("200 OK", "<html><body><h1>La suma es: " +
				str(num1) + " + " + str(num2) + " = " +
				str(suma) + "</h1></body></html>")
		
