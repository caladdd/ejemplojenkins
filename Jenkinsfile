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
		    
		    

		    
   		    // requires SonarQube Scanner 2.8+
		    def scannerHome = tool 'Sonar1';
    		    withSonarQubeEnv('Sonarq') {
			echo "hola"
			echo "${scannerHome}"
			sh "${scannerHome}/bin/sonar-scanne"
  		    }			 
		}		
		/* ... existing build steps ... */
		
	    } catch (e) {
		
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
    def colorName = 'RED'
    def colorCode = '#FF0000'
    def subject = "${buildStatus}: Job '${env.JOB_NAME} [${env.BUILD_NUMBER}]'"
    def summary = "${subject} (${env.BUILD_URL})"
    def details = """<p>STARTED: Job '${env.JOB_NAME} [${env.BUILD_NUMBER}]':</p>
    <p>Check console output at "<a href="${env.BUILD_URL}">${env.JOB_NAME} [${env.BUILD_NUMBER}]</a>"</p>"""
    
    // Override default values based on build status
    if (buildStatus == 'STARTED') {
	color = 'YELLOW'
	colorCode = '#FFFF00'
    } else if (buildStatus == 'SUCCESSFUL') {
	color = 'GREEN'
	colorCode = '#00FF00'
    } else {
	color = 'RED'
	colorCode = '#FF0000'
    }
    
  // Send notifications
  emailext (
	subject: subject,
	body: details,
	recipientProviders: [[$class: 'DevelopersRecipientProvider']]
    )
}

def getSonarBranchParameter(branch) {
    sonarBranchParam = ""
    if ("develop".equals(branch)) {
        echo "branch is develop, sonar.branch not mandatory"
    } else {
        echo "branch is not develop"
        sonarBranchParam="-Dsonar.branch=" + branch
    }
    return sonarBranchParam
}

def Properties getBuildProperties(filename) {
    def properties = new Properties()
    properties.load(new StringReader(readFile(filename)))
    return properties
}
