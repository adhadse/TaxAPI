# TaxAPI in Flask
A Flask API example with PyTest

Currently, this is a bare-bone implementation with Tax Payer, Tax Accountant, and Admin
models written. Apart from that, I have also written validators for the above models + 
for Country and State (storing individual tax value).

I have also set up the API end points for adding Tax Payer, Tax Accountant, Country 
and State and modifying them. Plus some perfectly running unittests.

I wasn't able to fulfill each and every requirements because of time constraints.
I also wasn't able to test the docker file as Docker seems to have issue on my latop. So instead run the unittests as per these instructions for the time being.

To run unit test, first install requirements.
```
pip install -r requirements.txt
```

and then run unittests using this command (doesn't require running acutal instance)
```
py -m unittest discover test -p '*_test.py'
```

Incase you want to run an actual server:
```
py manage.py db init
py manage.py db migrate
py manage.py db upgrade

py manage.py run
```