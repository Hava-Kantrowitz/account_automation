def uploadedFile = 'fams'

//file is uploaded to $JENKINS_HOME/$PATH_TO_THE_JOB/build/$BUILD_ID

node('agent') {
    stage('Copy From controller') {
        sh 'echo $JENKINS_HOME/$PATH_TO_THE_JOB/build/$BUILD_ID
        def localFile = getContext(hudson.FilePath).child(uploadedFile)
        localFile.copyFrom(controllerFilePath)
        sh 'ls -al'
        archiveArtifacts uploadedFile
    }
}
