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
        git(poll: true, url: 'https://stash.it.control-tec.com:8443/scm/it/cn_deploymentweb.git', branch: 'master')
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
        sh 'python ./verification.py'
      }
    }
    stage('final check') {
      steps {
        sh 'pwd'
      }
    }
  }
}