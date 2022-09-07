library "jenkinsci-unstashParam-library"
node { 
    stage('prep_env') { 
        sh 'pip3 install pdfplumber'
        retry(5) {
            def file_in_workspace = unstashParam "fams"
            sh "echo 'we in here'"
            checkout scm
            sh "cp $fams fam_test"
        }
        sh 'ls'
    }
    stage('assess_file') {
        sh "python3 acc_create.py $WORKSPACE/$fams" 
    }
    stage('cleanup'){
        cleanWs()
    }
}
