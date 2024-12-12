@echo off
curl -X GET ^
  "http://10.10.10.10:7819/RTCP/api/stubs/?domainName=Emirates&environment=LOCAL" ^
  -H "accept: application/json" ^
  -o response.txt

python parse_json.py response.json

pause