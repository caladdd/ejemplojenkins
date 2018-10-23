node{
try{
    	stage('Checkout'){
	    checkout scm
	    sh 'git log HEAD^..HEAD --pretty="%h %an - %s" > GIT_CHANGES'
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

