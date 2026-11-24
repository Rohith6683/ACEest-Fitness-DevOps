pipeline {
    agent any

    triggers {
        pollSCM('H/2 * * * *')
    }

    environment {
        IMAGE = 'aceest-fitness'
    }

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Docker Build') {
            steps {
                sh 'docker build -t ${IMAGE}:build-${BUILD_NUMBER} .'
            }
        }

        stage('Pytest') {
            steps {
                sh 'docker run --rm ${IMAGE}:build-${BUILD_NUMBER} python -m pytest -v'
            }
        }

        stage('Archive Artifact') {
            steps {
                sh 'docker save ${IMAGE}:build-${BUILD_NUMBER} -o aceest-image.tar'
                archiveArtifacts artifacts: 'aceest-image.tar', fingerprint: true
            }
        }
    }

    post {
        success {
            echo 'CI Pipeline completed successfully'
        }
        failure {
            echo 'CI Pipeline failed'
        }
    }
}
