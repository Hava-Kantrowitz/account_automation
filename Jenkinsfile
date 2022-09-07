node {
    deleteDir()
    stage("upload") {
        def inputFile = input message: 'Upload file', parameters: [file(name: 'data.zip')]
        new hudson.FilePath(new File("$workspace/data.zip")).copyFrom(inputFile)
        inputFile.delete()
    }
    stage("checkout") {
        echo fileExists('data.zip').toString()
    }
}
