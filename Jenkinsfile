pipeline {
    agent any

    stages {
        stage('Hello') {
            steps {
                sh 'pip3 install pdfplumber' 
                sh "python3 acc_create.py ${params.fams}"
            }
        }
    }
}
