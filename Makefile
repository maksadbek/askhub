default:
	@echo "please choose command:"
	@echo "  dev-setup        development setup"
	@echo "  run              run application"

dev-setup:
	@echo "not implemented yet"

run:
	FLASK_ENV=development FLASK_DEBUG=true FLASK_APP=askhub.app flask run
