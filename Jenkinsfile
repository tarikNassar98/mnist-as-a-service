    def id1 = '352708296901.dkr.ecr.eu-central-1.amazonaws.com'


pipeline {

  agent { label 'ec2-fleet' }
  environment {
    REGISTRY_URL = ''
    ECR_REGION = ''
    K8S_NAMESPACE = ''
  }

  stages {
    stage('MNIST Web Server - build'){
//       when { branch "master" }
      steps {
          sh '''
          echo building ...
                echo $BUILD_TAG
           aws ecr get-login-password --region eu-central-1 | docker login --username AWS --password-stdin $id
            docker build -t mnist-as-a-service:$BUILD_TAG ./webserver
            docker tag mnist-as-a-service:$BUILD_TAG $id/mnist-as-a-service:$BUILD_TAG
            docker push $id/mnist-as-a-service:$BUILD_TAG

          '''
      }
    }

    stage('MNIST Web Server - deploy'){
        when { branch "master" }
        steps {
            sh '''
            echo deploying
            '''
        }
    }


    stage('MNIST Predictor - build'){
        when { branch "master" }
        steps {
            sh '''
            IMAGE="mnist-predictor:0.0.${BUILD_NUMBER}"
            cd ml_model
            aws ecr get-login-password --region $ECR_REGION | docker login --username AWS --password-stdin ${REGISTRY_URL}
            docker build -t ${IMAGE} .
            docker tag ${IMAGE} ${REGISTRY_URL}/${IMAGE}
            docker push ${REGISTRY_URL}/${IMAGE}
            '''
        }
    }

    stage('MNIST Predictor - deploy'){
        when { branch "master" }
        steps {
            sh '''
            cd infra/k8s
            IMG_NAME=mnist-predictor:0.0.${BUILD_NUMBER}

            # replace registry url and image name placeholders in yaml
            sed -i "s/{{REGISTRY_URL}}/$REGISTRY_URL/g" mnist-predictor.yaml
            sed -i "s/{{IMG_NAME}}/$IMG_NAME/g" mnist-predictor.yaml

            # get kubeconfig creds
            aws eks --region eu-north-1 update-kubeconfig --name devops-apr21-k8s

            # apply to your namespace
            kubectl apply -f mnist-predictor.yaml -n $K8S_NAMESPACE
            '''
        }
    }
  }
}


