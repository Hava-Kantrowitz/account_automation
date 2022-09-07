node { 
    stage('prep_env') { 
        checkout scm
        sh 'pwd' 
        sh "python3 acc_create.py $WORKSPACE/$fams" 
    }
}
