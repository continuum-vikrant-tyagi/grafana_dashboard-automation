pipeline {
  agent {
    kubernetes {
      //cloud 'kubernetes'
      label 'grafanalib'
      yaml """
apiVersion: v1
kind: Pod
spec:
  containers:
  - name: grafanalib
    image: tyagivasu/grafana_lib_jinja2:v1
    command: ['cat']
    tty: true
    resources:
      limits:
        cpu: 200m
        memory: 256Mi
      requests:
        cpu: 100m
        memory: 128Mi
    volumeMounts:
      - name: aws-key
        mountPath: "/root/aws-key" 

  volumes:
    - name: aws-key
      secret:
        secretName: aws-key-int
        defaultMode: 256
"""
    }
  }
  parameters{
      string(name: 'title', defaultValue: 'dashboard title name', description: 'Write Dashboard Title Name')
      string(name: 'namespace', defaultValue: 'service namespace name', description: 'Write service namespace')
      string(name: 'consumergroup', defaultValue: 'cg', description: 'Write consumergroup name')
      string(name: 'topics', defaultValue: 'topics', description: 'Write topics name with comma seprate')
      choice(choices: ['no', 'yes'], description: 'Select yes cpu alert', name: 'cpualert')
      choice(choices: ['no', 'yes'], description: 'Select yes for memory alert', name: 'memoryalert')
      choice(choices: ['no', 'yes'], description: 'Select yes for cg_lag alert', name: 'cg_lagalert')
  }
  stages {
    stage('build-python') {
        steps {
            container('grafanalib') {
            sh "python $WORKSPACE/grafana_template.py"
            }
        }
    }
    // stage('generate-dashboard') {
    //     steps {
    //         container('grafanalib') {
    //          dir("$WORKSPACE") {
    //             sh "generate-dashboard -o ${params.title}.json ${params.title}"
    //             archiveArtifacts artifacts: "${params.title}.json, ${params.title}", fingerprint: true
    //             // sleep 300
    //          } 
    //         }
    //     }
    // }
  }
}