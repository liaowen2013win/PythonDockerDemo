## 基于tonado框架的Python应用，使用docker部署配置

详情记录在Dockerfile里面
###docker打包命令和运行命令：
### 打包
docker build -t docker-tonado:0.1 .
### 运行
docker run -d --name docker_tonado_app -v $PWD/app:/app -p 9999:9999 docker-tonado:0.1

启动后，使用服务器 ip:9999 访问

