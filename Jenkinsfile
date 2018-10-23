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
	stage('Email'){
	    notifyStarted()
	}

} catch (Exception e) {
  	stage("mal"){
	    echo "mal"
	}
}
}

def notifyStarted() {
  emailext (
      subject: "STARTED: Job '${env.JOB_NAME} [${env.BUILD_NUMBER}]'",
      body: """<p>STARTED: Job '${env.JOB_NAME} [${env.BUILD_NUMBER}]':</p>
        <p>Check console output at "<a href="${env.BUILD_URL}">${env.JOB_NAME} [${env.BUILD_NUMBER}]</a>"</p>""",
      recipientProviders: [[$class: 'DevelopersRecipientProvider']]
    )
}