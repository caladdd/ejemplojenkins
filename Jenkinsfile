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
    	    try {
    		notifyBuild('STARTED')
		stage('SonarQube analysis') {
		    def scannerHome = tool 'Sonar1';
    		    withSonarQubeEnv('Sonarq') {
			echo "hola"
			echo "${scannerHome}"
			sh "${scannerHome}/bin/sonar-scanner"
  		    }			 
		}

		///////
		stage("Quality Gate"){
		    timeout(time: 1, unit: 'HOURS') { // Just in case something goes wrong, pipeline will be killed after a timeout
			def qg = waitForQualityGate() // Reuse taskId previously collected by withSonarQubeEnv
			if (qg.status != 'OK') {
			    error "Pipeline aborted due to quality gate failure: ${qg.status}"
			}
		    }
		}
		/////////////


		
    	    }catch (e) {
		
    		currentBuild.result = "FAILED"
    		throw e
    	    } finally {
		
    		notifyBuild(currentBuild.result)
    	    }
    	}
	
    } catch (Exception e) {
    	stage("mal"){
    	    echo "mal"
    	}
    }
}


def notifyBuild(String buildStatus = 'STARTED') {
    // build status of null means successful
    buildStatus =  buildStatus ?: 'SUCCESSFUL'
    
    // Default values
    def subject = "${buildStatus}: Job '${env.JOB_NAME} [${env.BUILD_NUMBER}]'"
    def summary = "${subject} (${env.BUILD_URL})"
    def details = """<p>STARTED: Job '${env.JOB_NAME} [${env.BUILD_NUMBER}]':</p>
    <p>Check console output at "<a href="${env.BUILD_URL}">${env.JOB_NAME} [${env.BUILD_NUMBER}]</a>"</p>"""
    
  // Send notifications
  emailext (
	subject: subject,
	body: details,
	recipientProviders: [[$class: 'DevelopersRecipientProvider']]
    )
}

