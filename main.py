import requests
from rich import print
from rich.markdown import Markdown

#Display current weather function

def display_current_weather(location):
  """Get the current weather and condition for a given location."""
  api_key = "f093ocaff400a6043tff45112437b840"
  api_url = f"https://api.shecodes.io/weather/v1/current?query={location}&key={api_key}&units=metric"

  response = requests.get(api_url)
  response_data = response.json()

  temperature = round(response_data['temperature']['current'])
  condition = response_data['condition']['description']


  print(f"The current temperature in {location} is {temperature} degrees celsius,{condition}")


#Generate itinerary function

def generate_itinerary(origin, destination, duration):
  """Generate an itinerary for a given origin, destination, and duration."""
  print(f"Generating itinerary from {origin} to {destination}...")


  prompt = f"Generate atravel itiniarary from {origin} to {destination} in {duration} days. This is a road, keep it short, less than 15 lines. Make it readable and nice, add some emojis"
  context = "You are a travel specialist"
  api_key = "f093ocaff400a6043tff45112437b840"
  api_url = f"https://api.shecodes.io/ai/v1/generate?prompt={prompt}&context={context}&key={api_key}"

  response = requests.get(api_url)
  response_data = response.json()
  itinerary = Markdown(response_data['answer'])

  print(itinerary)

def welcome():
  print("[bold magenta]Welcome to the AI Travel Itinerary Planner[/bold magenta]") 

def credit():
  print("[bold magenta]Thank you for using the AI Travel Itinerary Planner, we wish you a great trip ❤️[/bold magenta]")


welcome()

# User inputs
origin = input("What city does your trip originate from? ")
destination = input("What city does your trip go to? ")
duration = input("How long is your trip? (enter number only) ")


if origin and destination and duration.isdigit():
  display_current_weather(origin)
  display_current_weather(destination)
  generate_itinerary(origin, destination, duration)
  credit()
else:
  print("Please try again. Make sure you enter valid information.")

