#!groovy

node {

    try {
    	stage('Checkout'){
	    checkout scm
            echo "Started"
	    }
	    
	stage('Test'){	 
            echo "HOla"
	    echo "jaja"
	    }

    catch (err) {
        echo "Build failed :face_with_head_bandage: \n`${env.JOB_NAME}#${env.BUILD_NUMBER}` <${env.BUILD_URL}|Open in Jenkins>"

        throw err
    }

}

