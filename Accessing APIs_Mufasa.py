import requests

def weather_forecast(Town):
    r = requests.get (
        f'https://api.openweathermap.org/data/2.5/forecast?q={Town}&appid=573380b70d3e53bcb847b1e742739545&units=metric')
    content = r.json ()
    Town = content['city']['name']
    Temperature = [content['list'][i]['main']['temp'] for i in range (0, len (content['list']))]
    Time_List = [content['list'][i]['dt_txt'] for i in range (0, len (content['list']))]
    Condition = [content['list'][i]['weather'][0]['description'] for i in range (0, len (content['list']))]

    with open("data.txt","a") as file:
        for i in range(0,len(Temperature)):
            file.write ("\n")
            file.write(f"{Town},{Time_List[i]},{Temperature[i]},{Condition[i]}")


weather_forecast("Idah")
