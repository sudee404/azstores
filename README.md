# project_qr

#### WhereThePartyAt

This is a web application capable of hosting parties and finding parties near you 
It is still in its development stages but I hope to get it running when complete

## Features 
### Finding a party
The user should be able to find a party within their location and buy a ticket
to attend the said party .The ticket issued has a qr code that is scanned 
at the entry point.

### Hosting a party
The user should be able to host their party on the site and have people buy tickets
in order to attend. The host gets a qr code scanner to identify guests at the entry.

### Chat bot
To assist users who are new to the page, this feature and the previous are not yet implemented and will be done in due time

## Build and Use
To build the project, just install the requirements file suplied 
**pip install -r _requirements.txt_**

To run the project , open your editor (preferably vs code) . Navigate to the root folder (where 'manage.py' exists) and run the command below
**python manage.py runserver**

You can fill the site with dummy data using the 'populate_first_app.py' script
