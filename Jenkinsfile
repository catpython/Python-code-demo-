
Jenkinsfile (Declarative Pipeline)

pipeline {
    agent { docker 'python3.7-alpine' }
    stages {
        stage('build') {
            steps {
                sh 'python --version'
            }
        }
    }
}

