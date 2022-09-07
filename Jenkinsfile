stage('Upload Key') {
    agent { label 'master' }
    steps {
        script {
            // Uploads file via master node and stases it for other nodes to access
            def inputFile = input message: 'Upload file', parameters: [file(name: "key.p12")]
            new hudson.FilePath(new File("${workspace}/key.p12")).copyFrom(inputFile)
            inputFile.delete()
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
