
//Jenkinsfile (Declarative Pipeline)

pipeline {
    agent { docker 'python:3.7-alpine' }
    stages {
        stage('build') {
            steps {
                sh 'python --version'
            }
        }
    }
}

