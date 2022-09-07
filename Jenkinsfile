node { 
    stage('prep_env') { 
        checkout scm
        sh "python3 acc_create.py /var/lib/jenkins/fams.pdf" 
    }
}
