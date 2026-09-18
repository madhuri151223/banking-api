pipeline {
    agent any

    environment {
        PACKAGE_NAME = 'banking-api.tar.gz'
    }

    stages {
        stage('Build') {
            steps {
                sh 'python3 -m py_compile app.py'
            }
        }

        stage('Unit Test') {
            steps {
                sh 'python3 -m pytest test_app.py -v'
            }
        }

        stage('Package') {
            steps {
                sh 'tar -czf $PACKAGE_NAME app.py deploy.sh deploy.conf'
            }
        }

        stage('Verify Package') {
            steps {
                sh 'test -f $PACKAGE_NAME'
                sh 'tar -tzf $PACKAGE_NAME'
            }
        }

        stage('Deploy Validation') {
            steps {
                sh 'bash deploy.sh'
            }
        }

        stage('Deploy') {
            steps {
                echo 'Production deployment started'
            }
        }
    }

    post {
        success {
            echo 'BANKING API PIPELINE SUCCESS'
        }

        failure {
            echo 'BANKING API PIPELINE FAILED'
        }
    }
}
