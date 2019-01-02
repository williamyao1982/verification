pipeline {
  agent any
  stages {
    stage('Precheck') {
      steps {
        sh '''echo "Hello World!"
echo $PATH'''
      }
    }
    stage('Preparation') {
      steps {
        sh 'echo "Preparation"'
      }
    }
    stage('deployLeopard4') {
      steps {
        sh 'echo "Deployment"'
      }
    }
    stage('deployLeopard1') {
      steps {
        sh 'echo "Deployment2"'
      }
    }
    stage('Verification') {
      steps {
        git(url: 'https://github.com/williamyao1982/verification.git', poll: true, branch: 'master')
      }
    }
    stage('final check') {
      steps {
        sh 'pwd'
      }
    }
  }
}