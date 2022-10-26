from django.shortcuts import render
import requests
import json

def index(request):
  r = requests.get('https://randomuser.me/api/')
  r = json.loads(r.text)["results"][0]
  context = {
    "nome": r["name"]["first"] + " " + r["name"]["last"],
    "cidade": r["location"]["city"],
    "email": r["email"],
    "username": r["login"]["username"],
    "idade": r["dob"]["age"],
    "celular": r["cell"],
    "foto": r["picture"]["large"],
  }

  return render(request, 'app/starter.html', context)
