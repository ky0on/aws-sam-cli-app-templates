#
# Usage:
#   make deploy CONFIG_ENV=production
#   export CONFIG_ENV=production && make deploy
#

.PHONY: build deploy

CONFIG_ENV ?= default

build:
	sam build

deploy:
	sam build
	sam deploy --config-env $(CONFIG_ENV)
	# sam deploy --config-env $(CONFIG_ENV) --resolve-image-repos

deploy-no-build:
	sam deploy --config-env $(CONFIG_ENV)
	# sam deploy --config-env $(CONFIG_ENV) --resolve-image-repos

# remote-invoke:
# 	sam remote invoke --stack-name YOUR_STACK_NAME --event '{"mode":"hourly"}'