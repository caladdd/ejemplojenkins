node{
try{
    	stage('Checkout'){
	    checkout scm
	    sh 'git log HEAD^..HEAD --pretty="%h %an - %s" > GIT_CHANGES'
	    def lastChanges = readFile('GIT_CHANGES')
	    echo "Started `${env.JOB_NAME}#${env.BUILD_NUMBER}`\n\n_The changes:_\n${lastChanges}"
            echo "Started"
	    }
	stage('Test'){	 
            echo "HOla"
	    echo "jaja"
	    }

} catch (Exception e) {
  	stage("mal"){
	    echo "mal"
	}
}
}

