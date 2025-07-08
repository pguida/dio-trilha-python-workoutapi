run:
	@uvicorn workout_api.main:app --reload

create-migrations:
	@PYTHONPATH=$$PYTHONPATH:$(pwd) alembic revision --autogenerate -m "$(filter-out $@,$(MAKECMDGOALS))"

run-migrations:
	@PYTHONPATH=$PYTHONPATH:$(pwd) alembic upgrade head

%:
    @: