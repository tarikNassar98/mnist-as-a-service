


pipeline {

  agent { label 'ec2-fleet' }
  environment {
    REGISTRY_URL = 'public.ecr.aws/r7m7o9d4/tarik-fp-ecr'
    ECR_REGION = 'us-east-1'
    K8S_NAMESPACE = 'tarik-nassar'
    K8S_CLUSTER_NAME = 'devops-alfnar-k8s'
    K8S_CLUSTER_REGION = 'eu-north-1'
  }

  stages {
    stage('MNIST Web Server - build'){
//       when { branch "master" }
      steps {
          sh '''
            IMAGE="mnist-web-server"
            TAG="${IMAGE}-${BRANCH_NAME}-${BUILD_NUMBER}"
            aws ecr-public get-login-password --region ${ECR_REGION} | docker login --username AWS --password-stdin ${REGISTRY_URL}
            docker build -t ${IMAGE}:0.0.${BUILD_NUMBER} ./webserver
            docker tag  ${IMAGE}:0.0.${BUILD_NUMBER} ${REGISTRY_URL}:${TAG}
            docker push ${REGISTRY_URL}:${TAG}
          '''
      }
    }
//
//     stage('MNIST Web Server - deploy'){
//         //when { branch "master" }
//         steps {
//             sh '''
//             echo deploying ....
//
//             cd infra/k8s
//             IMG_NAME="mnist-web-server-${BRANCH_NAME}-${BUILD_NUMBER}"
//
//             # replace registry url and image name placeholders in yaml
//             sed -i "s|{{REGISTRY_URL}}|$REGISTRY_URL|g" mnist-web-server.yaml
//             sed -i "s|{{K8S_NAMESPACE}}|$K8S_NAMESPACE|g" mnist-web-server.yaml
//             sed -i "s|{{IMG_NAME}}|$IMG_NAME|g" mnist-web-server.yaml
//
//             # get kubeconfig creds
//             aws eks --region $K8S_CLUSTER_REGION update-kubeconfig --name $K8S_CLUSTER_NAME
//
//             # apply to your namespace
//             echo ${K8S_NAMESPACE}
//             kubectl apply -f mnist-web-server.yaml --validate=false -n=${K8S_NAMESPACE}
//             '''
//         }
//     }


    stage('MNIST Predictor - build'){
//         when { branch "master" }
        steps {
            sh '''
            IMAGE="mnist-predictor"
            TAG="${IMAGE}-${BRANCH_NAME}-${BUILD_NUMBER}"
            cd ml_model
            aws ecr-public get-login-password --region ${ECR_REGION} | docker login --username AWS --password-stdin ${REGISTRY_URL}
            docker build -t ${IMAGE}:0.0.${BUILD_NUMBER}  .
            docker tag  ${IMAGE}:0.0.${BUILD_NUMBER} ${REGISTRY_URL}:${TAG}
            docker push ${REGISTRY_URL}:${TAG}
            '''
        }
    }

    stage('MNIST Predictor - deploy'){
        //when { branch "master" }
        steps {
            sh '''
            cd infra/k8s
            IMG_NAME="mnist-predictor-${BRANCH_NAME}-${BUILD_NUMBER}"
            # replace registry url and image name placeholders in yaml
             sed -i "s|{{REGISTRY_URL}}|$REGISTRY_URL|g" mnist-predictor.yaml
             sed -i "s|{{K8S_NAMESPACE}}|$K8S_NAMESPACE|g" mnist-predictor.yaml
             sed -i "s|{{IMG_NAME}}|$IMG_NAME|g" mnist-predictor.yaml

            # get kubeconfig creds
            aws eks --region $K8S_CLUSTER_REGION update-kubeconfig --name $K8S_CLUSTER_NAME

            # apply to your namespace
            kubectl apply -f mnist-predictor.yaml  --validate=false --namespace=$K8S_NAMESPACE
            '''
        }
    }
  }
}


