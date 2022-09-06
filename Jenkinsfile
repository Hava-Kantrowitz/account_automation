pipeline {
    agent any

    stages {
        stage('Hello') {
            steps {
                sh 'pip3 install pdfplumber'
                sh "echo $WORKSPACE"
                sh 'ls' 
                sh "python3 acc_create.py $WORKSPACE/$fams"
            }
        }
    }
}
