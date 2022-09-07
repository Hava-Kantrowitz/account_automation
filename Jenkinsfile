node { 
    stage('prep_env') { 
        library "jenkinsci-unstashParam-library"
        sh 'pip3 install pdfplumber'
        def file_in_workspace = unstashParam "fams"
        sh "cat ${file_in_workspace}" 
    }
    stage('assess_file') {
        sh "python3 acc_create.py $WORKSPACE/$fams" 
    }
}
