pipeline {
  agent any

  environment {
    REGISTRY_URL = '352708296901.dkr.ecr.eu-west-2.amazonaws.com'
    REGION = 'eu-west-2'
  }

  stages {
        stage('MNIST Predictor - build'){
            when { branch "master" }
            steps {
                sh '''
                IMAGE="mnist-predictor:0.0.${BUILD_NUMBER}"
                cd ml_model
                aws ecr get-login-password --region $REGION | docker login --username AWS --password-stdin ${REGISTRY_URL}
                docker build -t ${IMAGE} .
                docker tag ${IMAGE} ${REGISTRY_URL}/${IMAGE}
                docker push ${REGISTRY_URL}/${IMAGE}
                '''
            }
        }

        stage('MNIST Web Server - build'){
            when { branch "master" }
            steps {
                sh '''ls'''
            }
        }

        stage('MNIST Predictor - deploy'){
            when { branch "master" }
            steps {
                sh '''
                cd infra/k8s
                sed -i 's/{{IMG_URL}}/${REGISTRY_URL}/g' mnist-predictor.yaml
                kubectl apply -f mnist-predictor.yaml
                '''
            }
        }
  }
}


