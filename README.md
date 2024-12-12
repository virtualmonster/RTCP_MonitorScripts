# RTCP_MonitorScripts
Basic examples using RTCP APIs and commandline 

StartStub - uses IntegrationTester Cmd to start a stub

StopStub - yep..

getStubsList - uses Curl to call the API for a list of all stubs in  a domain and environment

getStubRates - uses python to retrieve a list of all stubs, attempts to parse them into categories (doesn't work perfectly) and gives the most recent TPS value for the last 30 second period
