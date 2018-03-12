MODULES_ADD += af_packet overlay squashfs
colaboot:
	@echo "Adding support for CoLaBoot ..."
	@put-file "$(ROOTDIR)" $(COLABOOT_FILES)
	@put-tree "$(ROOTDIR)" $(COLABOOT_DATADIR)

pack: colaboot
