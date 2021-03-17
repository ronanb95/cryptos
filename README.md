# cryptos

Hey there, welcome to my submission for the Crypto tracker assignment. 

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

By no means in depth, I have included a couple of unit tests to test some basic functionality of the application. Due to the time constraints I was unable to more in depth testing. 

