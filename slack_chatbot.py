from jenkins_build_info import buildResult

build_name, build_result = buildResult()
print('Last Build', build_name, ":", build_result)
