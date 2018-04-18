from Tkinter import *
import Pmw
def about(parent):

	Pmw.aboutversion('Beta')
	Pmw.aboutcopyright('Copyright Sysbio Group, Chalmers university, Sweden,\nAll rights reserved')
	Pmw.aboutcontact(
    'For information about this application contact:\n' +
    '  Subazini Thankaswamy Kosalai\n' +
    '  email: subazini@chalmers.se'
    )
	about = Pmw.AboutDialog(parent, applicationname='Batch analysis')
#about.withdraw()
if __name__ == '__main__':
	root = Tk()
	root.withdraw()
	Pmw.initialise(root, fontScheme = 'pmw1')
	about(root)
	root.mainloop()
	
