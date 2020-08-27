import jenkins

#Jenkins 마지막 빌드 결과 확인
def buildResult():
    server = jenkins.Jenkins('http://localhost:8080', username='admin', password='admin')
    last_build_number = server.get_job_info('test')['lastCompletedBuild']['number']
    build_info = server.get_build_info('test', last_build_number)
    build_result = build_info['result']
    build_name = build_info['displayName']
    return build_name, build_result
