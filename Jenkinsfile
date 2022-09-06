pipeline {
    agent any

    stages {
        stage('Hello') {
            steps {
                sh 'pip3 install pdfplumber'
                sh "echo ${/var/lib/jenkins/}"
                sh "python3 acc_create.py /var/lib/jenkins/"
            }
        }
    }
}
