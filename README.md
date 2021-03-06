## DJANGO BASED LOAD BALANCER

## REQUIREMENTS:
- DOCKER
- DJANGO

Designed and developed a load balancer in Django which routes the requests from the clients based on the client HTTP_HOST.

Load balancer consists of 5 servers.

First two servers belongs to the host 1 with DOMAIN : hostaddress1
- localhost:8081
- localhost:8082

The following two servers belongs to the host 2 with DOMAIN: hostadress2
- localhost:9081
- localhost:9082

The following server belongs to the host 3 with DOMAIN: hostadress3
- localhost:8083


## USAGE:
Use the following commands to build servers using docker.
1. docker-compose build
2. docker-compose up -d

pytest module is used for testing.


## Features:
 - The loadbalancer routes the request based on the host of the client request.
 - The loadbalancer allows 2 requests per server and if multiple requests are on the server loadbalancer redirects request based on the priority of the server. Also each server is allowed at most 2 requests at a time.
 
 ## Contributing
 
 Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.
