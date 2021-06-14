# MedCheck

A mobile application that lets users smartly diagnose their symptoms by providing the most likely condition for the symptom, a summary of the condition (using web-scraping and a medical database) and the nearest location to receive treatment (through a geolocation API).

## Inspiration

We were inspired to allow people to easily diagnose their medical symptoms and recieve the proper steps for treatment.

## What it does

The users input their symptoms into an autocomplete search bar and receive their most likely diagnosis and severity of the condition through a machine learning API. Next, a web-scraper scrapes a medical database to retrieve the most relevant information about the condition, and displays it for the user. Finally, an API filters for the nearest locations that can provide the necessary treatment and provides the address.

## How we built it

We used Vue for the front-end of the app, Django for the back-end, and Selenium for the web-scraping portion. The database we used was malacards.org. Our APIs consisted of the APIMedic and the HERE-geocoder API.

## Challenges we ran into

Portability was an issue we faced because we were trying to coordinate code on different machines with different dependencies, especially when trying to make the webscraper as robust as possible.
Accomplishments that we're proud of

We are proud to have programmed a fully-functional full-stack application in just twelve hours time.

## What we learned

We learned about developing a full-stack app, web-scraping in python, and general research practices to use when dealing with an API. We also got better at reading and understanding documentation.

## What's next for MedCheck

We plan to use machine learning to optimize our diagnosis, and to find a more robust API for providing diagnoses and symptoms.

## Built With

    apimedic
    django
    django-rest-framework
    nativescript
    python
    selenium
    vue
	here-geocoder

## Screenshots

<img src="https://github.com/antz22/MedCheck/blob/master/images/medcheck.png" width="300"> <img src="https://github.com/antz22/MedCheck/blob/master/images/home.png" width="300">
<img src="https://github.com/antz22/MedCheck/blob/master/images/logs.png" width="300"> <img src="https://github.com/antz22/MedCheck/blob/master/images/diagnosis.png" width="300">

:)