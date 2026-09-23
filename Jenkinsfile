pipleline{
    agent any
    {
        stages{
            stage('Checkout')
            {
                steps{
                    git branch:'main', url='https://github.com/mahesh-007p/question6.git'
                }
            }

            stage('Parallel Checks'){
                parallel{
                    stage('Frontend Check'){
                        steps{
                            bat 'python frontend_check.py'
                            archiveArtifacts artifacts: 'frontend_report.txt'
                        }
                    }
                    stage('Backend Check'){
                        steps{
                        bat 'python backend_check.py'
                        archiveArtifacts artifacts: 'backend_report.txt'
                        }
                    }
                }
            }
            stage('Archive Report'){
                steps{
                    echo 'Both Frontend and Backend checks are complete.'
                }
            }
        }
    }

}