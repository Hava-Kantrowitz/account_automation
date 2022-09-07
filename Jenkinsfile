def uploadedFile = 'fams'

//file is uploaded to $JENKINS_HOME/$PATH_TO_THE_JOB/build/$BUILD_ID
def controllerFilePath = input message: 'Upload your archive', parameters: [file(description: 'archive', name: uploadedFile)]

node('agent') {
    stage('Copy From controller') {
        def localFile = getContext(hudson.FilePath).child(uploadedFile)
        localFile.copyFrom(controllerFilePath)
        sh 'ls -al'
        archiveArtifacts uploadedFile
    }
}
