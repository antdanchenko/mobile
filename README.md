# Installation:

- brew install python
- brew install allure
- cd to project's root and pip3 install -r requirements.txt

- nano ~/.bash_profile
- export SAUCE_USERNAME=your_username
- export SAUCE_ACCESS_KEY=your_access_key
- source ~/.bash_profile

# Running tests:

- cd to tests folder
- python3 -m pytest tests_sanity.py

##### required parameter:
- --apk url/path to apk

##### optional parameters:

- --repeat int (number of repeating failed tests before final verdict)
- --alluredir path (path to store allure results)
- -n int (number of parallel sessions)

##### example:

- python3 -m pytest -m sanity --apk http://url/application.apk -n2 -v
