add-task:
	@python main.py -t '$(TASK)' -desc '$(DESC)' -s '$(STATUS)'

list:
	@python main.py -l

update-task:
	@python main.py -u '$(TID)' -s '$(STATUS)'

delete-task:
	@python main.py -d '$(TID)'

get-tid:
	@python main.py -gt '$(TASK)'