PROJECT_NAME := "j2render"


e2e-test: build-amd64
    docker run --rm -v $(pwd)/data:/data -v $(pwd)/renderer/tests/assets:/data/assets --workdir /data alpine ./j2render_static.linux.amd64 -c assets/config.yaml

e2e-arm64-test: build-arm64
    docker run --rm -v $(pwd)/data:/data -v $(pwd)/renderer/tests/assets:/data/assets  --workdir /data alpine ./j2render_static.linux.arm64 -c assets/config.yaml

build-amd64:
	just build amd64

build-arm64:
	just build arm64

build arch:
	docker buildx build --platform linux/{{arch}} -t {{PROJECT_NAME}}:{{arch}} --output type=docker .
	docker run --rm -v $(pwd)/data:/data {{PROJECT_NAME}}:{{arch}} cp /usr/local/bin/{{PROJECT_NAME}} /data/{{PROJECT_NAME}}.linux.{{arch}}
	docker run --rm -v $(pwd)/data:/data {{PROJECT_NAME}}:{{arch}} cp /usr/local/bin/{{PROJECT_NAME}}_static /data/{{PROJECT_NAME}}_static.linux.{{arch}}

coverage:
    #!/usr/bin/env bash

    cd renderer/tests
    pytest --cov-report xml --cov=renderer .

    cp .coverage ../../
