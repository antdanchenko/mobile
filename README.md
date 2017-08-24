# Installation:

- brew install python
- cd to project's root and pip3 install -r requirements.txt

# Running tests:

- cd to tests folder
- py.test -m sanity

##### required parameter:
- --apk url/path to apk

##### optional parameters:

- -n int (number of parallel sessions)

##### Jenkins setup:

- install Sauce OnDemand plugin in /pluginManager/available
- add SAUCE_USERNAME, SAUCE_ACCESS_KEY in /configure, as "Environment variables"

- create new job (Freestyle project)
- add git to "Source Code Management" (https://github.com/antdanchenko/mobile.git) and select "Clean before checkout" in "Additional Behaviours"
- under "Build Environment" check "Sauce Labs Support"
- under "Sauce Labs Options" add Credentials (select Sauce Lab in dropdown "Kind")

- add build step (Execute shell): /usr/local/bin/python3 -m pytest -m sanity -n2 --apk http://url/application.apk --build ${JOB_NAME}__${BUILD_NUMBER}
- add post build action "Run Sauce Labs Test Publisher"
- add post build action "Publish JUnit test result report", enter *.xml into "Test report XMLs", click "Add" for "Additional test report features" and set "Job Visibility" - "Public"
