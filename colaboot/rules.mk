colaboot:
	@echo "Adding support for CoLaBoot ..."
	@put-file "$(ROOTDIR)" $(COLABOOT_FILES)
	@put-tree "$(ROOTDIR)" $(COLABOOT_DATADIR)
	@bash -c '[ -d "$$WORKDIR/img/lib/modules" ] && rm -rf "$$WORKDIR/img/lib/modules"; true; '
pack: colaboot
