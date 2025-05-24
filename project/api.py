import requests

baseurl="https://pokeapi.co/api/v2/"
def getpokemoninfo(name):
    url=f"{baseurl}/pokemon/{name}"
    response=requests.get(url)
    if response.status_code==200:
        pokemondata=response.json()
        
        return pokemondata
    else:
        print(f"failed to retrieve data {response.status_code}")
   
pokemonname="Typhlosion"
pokemoninfo=getpokemoninfo(pokemonname)
if pokemoninfo:
    print(f"Name:{pokemoninfo['name'].capitalize() }")
    print(f"Id:{pokemoninfo['id'] }")
    print(f"Height:{pokemoninfo['height'] }")
    print(f"Weight:{pokemoninfo['weight'] }")
    
    