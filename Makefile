env-encrypt:
	@echo "Encrypting .env file"
	@openssl enc -aes-256-cbc -salt -in .env -out .env.enc

env-decrypt:
	@echo "Decrypting .env.enc file"
	@openssl enc -aes-256-cbc -d -in .env.enc -out .env

run-local:
	@echo "Running local server"
	@uvicorn main:app --reload --host 0.0.0.0 --port 8000