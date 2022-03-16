pipeline {
  agent any

  environment {
    REGISTRY_URL = '352708296901.dkr.ecr.eu-west-2.amazonaws.com'
    REGION = 'eu-west-2'
  }

  stages {
        stage('MNIST Predictor - build'){
            when { branch "dev1" }
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
            when { branch "dev" }
            steps {
                sh '''
                cd infra/k8s
                IMG_URL=$REGISTRY_URL\\/mnist-predictor:0.0.5
                sed -i "s/{{IMG_URL}}/$IMG_URL/g" mnist-predictor.yaml
                aws eks --region eu-north-1 update-kubeconfig --name devops-apr21-k8s
                kubectl apply -f mnist-predictor.yaml
                '''
            }
        }
  }
}


