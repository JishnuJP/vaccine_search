# vaccine_search
This project is an attempt to create a python app that can search for covid vaccine availability in any district in India. It uses the api setu of Indian govt to collect the data.
It can also send messages in telegram when an available slot is found in your locality.</br>

## Requirements

* python3.x </br>
* pandas==1.2.x </br>
* requests==2.24.x </br>

## How to use

This project is still WIP, I don't know if and how it's going to work on your computer. 
But you're more than welcome to open and issue and I'll try to help as much as I can.
1. Download the repo into your local machine
    >git clone https://github.com/JishnuJP/vaccine_search.git
2. Navigate into the repo.
    >cd vaccine_search/
3. (Optional)Change the default values if you want.
    * `defaults.py` has the default values for age, dose, district id's etc...
    * `telegram_token.txt` should have the telegram api-token in the first line and chat id in the second line.
4. Run the executable file.
    >./vaccineSearch.py 
     
  It will give an option to change the default setting and set new search parameters. Then it will start searching.
  It can be stopped by keyboard interruption `ctrl d`
  
## Note to developers and contributors
There are lot of functions in the [api setu](https://apisetu.gov.in/public/marketplace/api/cowin/cowin-protected-v2) 
which I haven't used here(like find by findByPin, findByLatLong etc). And also there is a lot of room for improvement like adding more filters, integrating a UI, 
making the telegram bot more interactive etc. </br>
For example there could be a window to change the settings (instead of terminal) or a provision for changing the settings through telegram bot and also there could be a filter based on the cost. </br>
All kinds of genuine PR's are welcome and feel free to clone and use the code for your projects also.  
