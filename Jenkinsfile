library "jenkinsci-unstashParam-library"
node { 
    stage('prep_env') { 
        sh 'pip3 install pdfplumber'
        def file_in_workspace = unstashParam "fams"
        sh "pwd" 
        sh "ls"
    }
    stage('assess_file') {
        sh "python3 acc_create.py $WORKSPACE/$fams" 
    }
}
