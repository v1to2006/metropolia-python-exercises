import requests

class JokeGenerator:
	def __init__(self) -> None:
			self._base_link = "https://api.chucknorris.io/jokes/random"
	
	def get_random_joke(self):
		try:
			response = requests.get(self._base_link)
		except requests.exceptions.RequestException as error:
			print(error)
			return
		
		print(response.json()["value"])

def main():
	joke_generator = JokeGenerator()

	joke_generator.get_random_joke()

main()