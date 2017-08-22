# Installation:

- brew install python
- cd to project's root and pip3 install -r requirements.txt

# Running tests:

- cd to tests folder
- py.test -m sanity

##### required parameter:
- --apk url/path to apk

##### optional parameters:

- --repeat int (number of repeating failed tests before final verdict)
- -n int (number of parallel sessions)

##### Jenkins setup:

- add SAUCE_USERNAME=your_username, SAUCE_ACCESS_KEY=your_access_key in jenkins_url/configure, as "Environment variables"
- install Sauce OnDemand plugin in jenkins_url/pluginManager/available
- add build step (Execute shell)  py.test -m sanity -n2 -v --apk http://url/application.apk --build ${JOB_NAME}__${BUILD_NUMBER}
- add post build action "Run Sauce Labs Test Publisher"