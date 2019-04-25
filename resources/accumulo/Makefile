.PHONY: compile-proxy
compile-proxy:
	mkdir ./generated
	thrift --gen py -out ./generated ./proxy.thrift
	mv ./generated/accumulo/* ../../accumulo
	rm -rf ./generated