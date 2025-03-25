env-encrypt:
	@echo "Encrypting .env file"
	@openssl enc -aes-256-cbc -salt -in .env -out .env.enc

env-decrypt:
	@echo "Decrypting .env.enc file"
	@openssl enc -aes-256-cbc -d -in .env.enc -out .env

run-local-ssl:
	@echo "Running local server"
	@uvicorn main:app --reload  --port 8443 --ssl-certfile=ssl/cert.pem --ssl-keyfile=ssl/key.pem


setup:
	@echo "Setting up environment"
	python3 -m venv .venv
	pip install -r requirements.txt
	@echo "Setup commonname as localhost:"
	openssl req -x509 -newkey rsa:4096 -keyout ssl/key.pem -out ssl/cert.pem -days 365