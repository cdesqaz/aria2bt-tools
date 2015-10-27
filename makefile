###################################################################
# Installing aria2bt-tools                                        #
###################################################################

PREFIX=/usr

install:
	cp aria2bt-main.py $(PREFIX)/bin
	cp aria2bt-run.py $(PREFIX)/bin
	cp aria2bt-config.py $(PREFIX)/bin
	cp desktop/aria2bt-tools.desktop $(PREFIX)/share/applications
	cp icon/aria2.png $(PREFIX)/share/icons
	chmod +x $(PREFIX)/bin/aria2bt-main.py
	chmod +x $(PREFIX)/bin/aria2bt-run.py
	chmod +x $(PREFIX)/bin/aria2bt-config.py
	chmod +x $(PREFIX)/share/applications/aria2bt-tools.desktop
	
uninstall:
	rm $(PREFIX)/bin/aria2bt-main.py
	rm $(PREFIX)/bin/aria2bt-run.py
	rm $(PREFIX)/bin/aria2bt-config.py
	rm $(PREFIX)/share/applications/aria2bt-tools.desktop
	rm $(PREFIX)/share/icons/aria2.png

