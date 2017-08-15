# Installation:

brew install python
cd to project's root and pip3 install -r requirements.txt

nano ~/.bash_profile
export SAUCE_USERNAME=your username
export SAUCE_ACCESS_KEY=your access key
source ~/.bash_profile

# Running tests:

cd to tests folder
python3 -m pytest tests_sanity.py

##### required parameter:
--apk url/path to apk

##### optional parameters:

--repeat int (number of repeating failed tests before final verdict)
-n int (number of parallel sessions)