library "jenkinsci-unstashParam-library"
node { 
    stage('prep_env') { 
        retry(5) {
            cleanWs()
            sh 'pip3 install pdfplumber'
            def file_in_workspace = unstashParam "fams"
            checkout scm
            sh "cp $fams fam_test"
        }
    }
    stage('assess_file') {
        sh "python3 acc_create.py $WORKSPACE/$fams" 
    }
    stage('cleanup'){
        cleanWs()
    }
}
