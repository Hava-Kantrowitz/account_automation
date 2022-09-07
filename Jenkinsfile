library "jenkinsci-unstashParam-library"
node { 
    stage('prep_env') { 
        sh 'pip3 install pdfplumber'
        checkout scm
        def exists = fileExists params.fams
        while (!exists) {
            def file_in_workspace = unstashParam "fams"
        }
        sh "ls"
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
