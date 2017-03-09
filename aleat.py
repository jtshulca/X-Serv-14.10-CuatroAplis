#!/usr/bin/python3

import webapp
import random

class aleat(webapp.app):
  
    def process(self, parsedRequest):
        return ("200 OK", "<html><body><h1>Generamos URL aleatorias:</h1>" +
                "<a href=http://localhost:1234/aleat/"
                + str(random.randint(0, 10000000000)) +
                ">dame una URL</a></body></html>")




