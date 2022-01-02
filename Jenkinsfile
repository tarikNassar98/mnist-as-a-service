pipeline {
  agent any

// Don't forget to make use in the relevant places:
// copyArtifacts filter: '...your..terraform..state..path...', projectName: '${JOB_NAME}'
// archiveArtifacts artifacts: '...your..terraform..state..path...', onlyIfSuccessful: true

  stages {
    stage('Terraform Init & Plan'){
        when { anyOf {branch "master";branch "dev";changeRequest()} }
        steps {
            sh '''
            if [ "$BRANCH_NAME" = "master" ] || [ "$CHANGE_TARGET" = "master" ]; then
                cd infra/prod
            else
                cd infra/dev
            fi

            # YOUR COMMANDS HERE
            '''
        }
    }

    stage('Terraform Apply'){
        when { anyOf {branch "master";branch "dev"} }
        input {
            message "Do you want to proceed for infrastructure provisioning?"
        }
        steps {
            sh '''
            if [ "$BRANCH_NAME" = "master" ] || [ "$CHANGE_TARGET" = "master" ]; then
                INFRA_ENV=infra/prod
            else
                INFRA_ENV=infra/dev
            fi


            # YOUR COMMANDS HERE
            '''
        }
    }
  }
}


