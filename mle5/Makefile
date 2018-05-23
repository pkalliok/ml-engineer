
stamps/start-postgres: lib/docker-compose.yml
	docker-compose -f $< up -d
	touch $@

stamps/wait-postgres: lib/docker-compose.yml stamps/start-postgres
	until docker-compose -f $< run test-postgres-up >/dev/null 1>&2; do \
		echo -n .; sleep 1; done
	touch $@

.PHONY: stop
stop:
	docker-compose -f lib/docker-compose.yml down
	rm -f stamps/start-postgres

