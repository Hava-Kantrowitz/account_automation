library "jenkinsci-unstashParam-library"
node { 
    stage('prep_env') { 
        sh 'pip3 install pdfplumber'
        def exists = fileExists $fams
        while (!exists) {
            def file_in_workspace = unstashParam "fams"
        }
        sh "ls"
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
