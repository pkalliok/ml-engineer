
JSON_FILES = adult.json adult1.json adult2.json adult3.parquet adultxml.csv

.PHONY: imports
imports: stamps/import-postgres stamps/import-json

myenv:
	python3 -m venv myenv

stamps/install-binary-depends:
	sudo apt-get install libsnappy-dev
	touch $@

stamps/install-depends: myenv requirements.txt stamps/install-binary-depends
	./myenv/bin/pip install -r requirements.txt
	touch $@

stamps/start-postgres: lib/docker-compose.yml
	docker-compose -f $< up -d local-postgres
	touch $@

stamps/wait-postgres: lib/docker-compose.yml stamps/start-postgres
	until docker-compose -f $< run test-postgres-up >/dev/null 1>&2; do \
		echo -n .; sleep 1; done
	touch $@

stamps/import-postgres: adult_dump.sql stamps/wait-postgres
	cat $< | docker-compose -f lib/docker-compose.yml run psql
	touch $@

adultxml.csv: adult.xml lib/sanitise_adult_xml
	sed '/<\/item>/q' $< \
	| grep -o 'name="[^"]*' \
	| cut -d'"' -f2 \
	| tr \\012 , \
	| sed 's/,$$//' \
	> $@
	sed -f lib/sanitise_adult_xml $< \
	| xmlstarlet sel --text -t -m "//items/item" -n -m "*" -v . -o , \
	>> $@

stamps/import-json: $(JSON_FILES) stamps/wait-postgres stamps/install-depends
	for f in $(JSON_FILES); do \
		echo "Importing $$f..."; \
		./myenv/bin/python lib/import_json.py $$f; done
	touch $@

.PHONY: psql
psql:
	docker-compose -f lib/docker-compose.yml run psql

.PHONY: stop
stop:
	docker-compose -f lib/docker-compose.yml down
	rm -f stamps/start-postgres

.PHONY: clean
clean:
	rm -rf myenv/

