pipeline {
    agent any
    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Check Config Dates') {
            steps {
                script {
                    // 找出這次 commit 有變動的 config 檔
                    def changedFiles = sh(script: "git diff --name-only origin/main...HEAD | grep -E '\\.ya?ml$|\\.json$' || true", returnStdout: true).trim()

                    if (changedFiles) {
                        echo "Changed config files:\n${changedFiles}"

                        // 跑 check_date.py
                        sh """
                            python3 check_date.py ${changedFiles}
                        """
                    } else {
                        echo "No config files changed."
                    }
                }
            }
        }
    }
}
