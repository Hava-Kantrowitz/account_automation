library "jenkinsci-unstashParam-library"
node { 
    stage('prep_env') { 
        deleteDir()
        sh 'pip3 install pdfplumber'
        def file_in_workspace = unstashParam "fams"
        checkout scm
        sh "pwd" 
        sh "ls"
    }
    stage('assess_file') {
        sh "python3 acc_create.py $WORKSPACE/$fams" 
    }
    stage('cleanup'){
        cleanWs()
    }
}
