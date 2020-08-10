Designed and developed a load balancer in Django which routes the requests from the clients based on the client HTTP_HOST.

Load balancer consists of 5 servers.

First two servers belongs to the host www.hostaddress1.com
- localhost:8081
- localhost:8082

The following two servers belongs to the host www.hostadress2.com
- localhost:9081
- localhost:9082

The following server belongs to the host www.hostadress3.com
- localhost:8083

The loadbalancer routes the request based on the host of the client request.

USAGE:
Use the following commands to build servers using docker.
1. docker-compose build
2. docker-compose up -d

pytest module is used for testing.
