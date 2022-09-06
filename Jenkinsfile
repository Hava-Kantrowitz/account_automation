pipeline {
    agent any

    stages {
        stage('Hello') {
            steps {
                sh 'pip3 install pdfplumber'
                echo $WORKSPACE
                sh "python3 acc_create.py $WORKSPACE/$fams"
            }
        }
    }
}
