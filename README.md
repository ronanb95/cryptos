# cryptos

Hey there, welcome to my submission for the Crypto tracker assignment. I will now breakdown some of the decisions I took whilst working on this application. If you would like to skip to the instructions on how to install and run the application you can find them towards the bottom of this README. 

## Workflow Overview

I have attempted to document my workflow as clearly as possible. I have broken the process down into steps, each of which was performed in order and then pushed to this repository. Between some of these steps I performed some unit tests to make sure I hadn't done anything terrible. If I had a little more time I might have followed a more Test Driven Development approach. If you would like to see these steps you can check the commit history and you should be able to clearly see the steps I took in order. 

Generally speaking I broke the development process into two main parts, a part focusing on the creation of the customer content cards and a part focusing on the market table.

## Customers Cards 

I began by setting up a basic skeleton app, then added some basic templates with some css to get an idea of where everything would fit. I then began working on the backend functionality for the customers content cards. Once the backend functionality was complete I focused on styling the section.


## Market Table

I followed a similar approach for the market table. I first worked on the backend, 

## Installation

Pull the code from this repository by whatever means you prefer.

Then nativate into the base dir:

```bash
cd crypto
```

Make a fresh Python 3.7 virtual environment, & activate it. I am using conda on windows so my commands are as follows (Your OS may be different):

```bash
conda create -n newenv
conda activate newenv
```

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install required packages:

```bash
pip install -r requirements.txt
```

## Usage

To run the app: 

```bash
python manage.py runserver
```

Navigate to localhost:8000 to view site locally

## Testing

Whilst in the base dir which contains manage.py tests can be run by typing the following:

```bash
python manage.py test webApp
```

By no means in depth, I have included a couple of unit tests to test some basic functionality of the application. Due to the time constraints I was unable to perform more in depth testing. 

