pipleline{
    agent any
    {
        stages{
            stage('')
            {
                steps{
                    git branch:'main', url='https://github.com/mahesh-007p/question6.git'
                }
            }

            stage('Checkout'){
                parallel{
                    stage('Frontend Check'){
                        steps{
                            bat 'python frontend_check.py'
                            archiveArtifacts artifacts: 'frontend_report.txt'
                        }
                    }
                    stage('Install Dependencies'){
                        steps{
                        bat 'python backend_check.py'
                        archiveArtifacts artifacts: 'backend_report.txt'
                        }
                    }
                }
            }
            stage('Run Unit Test'){
                steps{
                    echo 'Both Frontend and Backend checks are complete.'
                }
            }
        }
    }

}