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
        git(poll: true, url: 'https://github.com/williamyao1982/verification.git', branch: 'master')
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
        sh 'echo "python"'
        sh 'python --version'
      }
    }
    stage('final check') {
      steps {
        sh 'pwd'
      }
    }
  }
}