node {
    deleteDir()
    stage("upload") {
        new hudson.FilePath(new File("$workspace/fams"))
    }
    stage("checkout") {
        echo fileExists('fams').toString()
        sh 'ls'
    }
}
