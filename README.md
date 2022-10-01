# Test connectivity to MSSQL
I had some connection issues in client's site. Had to test a certain type of connectivity using pymssql to an 
MSSQL server. To ease the check I created this docker file and test script which allows to quickly build and run
the test. It also allows to ask some other IT person to run the test.


1. Build the container: docker build .
2. Run the container:
```shell
docker run -it --rm --network=host -e DB_HOST=<DB host here> -e DB_USER=SA check-mssql
```

If the test is successful you should see the list of available databases. 
