#!/bin/bash
echo url="https://www.duckdns.org/update?domains=jgc-server.duckdns.org&token=79729ec3-ed24-44b2-a52c-0b4a84e1b5ed&ip=" | curl -k -o ~/My_server/duckdns/duck.log -K -
