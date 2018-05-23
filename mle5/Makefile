
stamps/start-postgres: lib/docker-compose.yml
	docker-compose -f $< up -d
	touch $@

.PHONY: stop
stop:
	docker-compose -f lib/docker-compose.yml down
	rm stamps/start-postgres

