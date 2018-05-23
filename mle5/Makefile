
stamps/start-postgres: lib/docker-compose.yml
	docker-compose -f $< up -d
	touch $@

stamps/wait-postgres: lib/docker-compose.yml stamps/start-postgres
	until docker-compose -f $< run test-postgres-up >/dev/null 1>&2; do \
		echo -n .; sleep 1; done
	touch $@

stamps/import-postgres: adult_dump.sql stamps/wait-postgres
	cat $< | docker-compose -f lib/docker-compose.yml run psql

.PHONY: psql
psql:
	docker-compose -f lib/docker-compose.yml run psql

.PHONY: stop
stop:
	docker-compose -f lib/docker-compose.yml down
	rm -f stamps/start-postgres

