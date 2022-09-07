stage('Upload Key') {
    agent { label 'master' }
    steps {
        script {
            // Uploads file via master node and stases it for other nodes to access
            new hudson.FilePath(new File("${workspace}/fams"))
        }
        stash name: 'key.p12' , includes: "key.p12"
    }
}
    stage('Register') {
        steps {
            ws (sanitizedWorkspaceName) {
                echo "Registering"
                unstash 'key.p12'
            }
        }
    }
