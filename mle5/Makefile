
JSON_FILES = adult.json adult1.json adult2.json

stamps/start-postgres: lib/docker-compose.yml
	docker-compose -f $< up -d
	touch $@

stamps/wait-postgres: lib/docker-compose.yml stamps/start-postgres
	until docker-compose -f $< run test-postgres-up >/dev/null 1>&2; do \
		echo -n .; sleep 1; done
	touch $@

stamps/import-postgres: adult_dump.sql stamps/wait-postgres
	cat $< | docker-compose -f lib/docker-compose.yml run psql

stamps/import-json: $(JSON_FILES) stamps/wait-postgres
	for f in $(JSON_FILES); do python3 lib/import_json.py $$f; done
	touch $@

.PHONY: psql
psql:
	docker-compose -f lib/docker-compose.yml run psql

.PHONY: stop
stop:
	docker-compose -f lib/docker-compose.yml down
	rm -f stamps/start-postgres

