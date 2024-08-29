generate_key:
	@echo "Generating API key..."
	@python3 -c 'import random; import string; key = "".join(random.choices(string.ascii_lowercase + string.digits, k=26)); print(key)' > apikey.txt

update_env:
	@key=$$(cat apikey.txt); \
	echo "Key to be used: $$key"; \
	if grep -q '^ZAP_API_KEY=' file.env; then \
		sed -i "s/^ZAP_API_KEY=.*/ZAP_API_KEY=$$key/" file.env; \
	else \
		echo "ZAP_API_KEY=$$key" >> file.env; \
	fi
	@echo "file.env updated successfully!"
	rm apikey.txt

run: generate_key update_env
	@echo "Starting services with new API key..."
	docker compose --env-file file.env up --build --force-recreate -d
	docker compose exec framework sh -c "cp /app/input_data/$(FILE) /shared_data"
