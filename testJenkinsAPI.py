import jenkins

server = jenkins.Jenkins('http://localhost:8080', username='admin', password='admin')
#버전 정보 확인으로 Jenkins 서버 연결 확인
user = server.get_whoami()
version = server.get_version()
# print('Hello %s from Jenkins %s' % (user['fullName'], version))

#Jenkins 마지막 빌드 결과 확인
last_build_number = server.get_job_info('test')['lastCompletedBuild']['number']
build_info = server.get_build_info('test', last_build_number)
build_result = build_info['result']
buildName = build_info['displayName']
print('Last Build', buildName, ":", build_result)