pipeline {
    agent any

    environment {
        DOCKERHUB_CREDENTIALS = credentials('dockerhub-credentials')
        IMAGE_NAME = 'fontysuser/monitoring-app'
    }

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Build Docker Image') {
            steps {
                sh 'docker build -t $IMAGE_NAME:$BUILD_NUMBER .'
                sh 'docker tag $IMAGE_NAME:$BUILD_NUMBER $IMAGE_NAME:latest'
            }
        }

        stage('Push to Docker Hub') {
            steps {
                sh 'echo $DOCKERHUB_CREDENTIALS_PSW | docker login -u $DOCKERHUB_CREDENTIALS_USR --password-stdin'
                sh 'docker push $IMAGE_NAME:$BUILD_NUMBER'
                sh 'docker push $IMAGE_NAME:latest'
            }
        }

        stage('Deploy') {
            steps {
                sh 'docker stop monitoring-app-flask-app-1 || true'
                sh 'docker rm monitoring-app-flask-app-1 || true'
                sh 'docker run -d --name monitoring-app-flask-app-1 --network monitoring-app_default -p 5000:5000 -e DB_HOST=postgres -e DB_NAME=monitoring -e DB_USER=admin -e DB_PASSWORD=password $IMAGE_NAME:latest'
            }
        }
    }
}
