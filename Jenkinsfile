node {checkout([$class: 'GitSCM', branches: [[name: '*/master']], doGenerateSubmoduleConfigurations: false, extensions: [], submoduleCfg: [], userRemoteConfigs: [[url: 'https://github.com/antdanchenko/mobile.git']]])
        sauce('6269510b-13f3-4019-b156-c2c835f3a408') {
            try {sh '/usr/local/bin/python3 -m pytest -m sanity -n5 --apk http://artifacts.status.im:8081/artifactory/nightlies-local/im.status.ethereum-6a56b6.apk --build ${JOB_NAME}__${BUILD_NUMBER}'
            }
            finally {
                saucePublisher()
                junit testDataPublishers: [[$class: 'SauceOnDemandReportPublisher', jobVisibility: 'public']], testResults: '*.xml' }
            }
}