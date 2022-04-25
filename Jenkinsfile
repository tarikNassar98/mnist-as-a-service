


pipeline {

  agent { label 'ec2-fleet' }
  environment {
    REGISTRY_URL = 'public.ecr.aws/r7m7o9d4/tarik-fp-ecr'
    ECR_REGION = 'us-east-1'
    K8S_NAMESPACE = ''
    K8S_CLUSTER_NAME = ''
    K8S_CLUSTER_REGION = ''
  }

  stages {
    stage('MNIST Web Server - build'){
//       when { branch "master" }
      steps {
          sh '''

          '''
      }
    }

    stage('MNIST Web Server - deploy'){
        when { branch "master" }
        steps {
            sh '''
            echo deploying ....
            '''
        }
    }


    stage('MNIST Predictor - build'){
//         when { branch "master" }
        steps {
            sh '''
            aws ecr-public get-login-password --region $ECR_REGION | docker login --username AWS --password-stdin $REGISTRY_URL
            IMAGE="mnist-predictor:$BUILD_NUMBER"
            cd ml_model
            docker build -t mnist-predictor:$BUILD_NUMBER  .
            docker tag mnist-predictor:$BUILD_NUMBER ${REGISTRY_URL}:mnist-predictor-$BUILD_TAG-$BUILD_NUMBER
            docker push ${REGISTRY_URL}:mnist-predictor-$BUILD_TAG-$BUILD_NUMBER
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
            sed -i "s/{{K8S_NAMESPACE}}/$K8S_NAMESPACE/g" mnist-predictor.yaml
            sed -i "s/{{IMG_NAME}}/$IMG_NAME/g" mnist-predictor.yaml

            # get kubeconfig creds
            aws eks --region $K8S_CLUSTER_REGION update-kubeconfig --name $K8S_CLUSTER_NAME

            # apply to your namespace
            kubectl apply -f mnist-predictor.yaml -n $K8S_NAMESPACE
            '''
        }
    }
  }
}


