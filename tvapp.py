from PyQt4.QtCore import *
from PyQt4.QtGui import *
import urllib.request
import sys
import tvdownloader
import qdarkstyle

# this is a dictionary containing series, their seasons and episodes. The app will store their data in this form
boy = {
		"Arrow" : {
					"s01" :
						{
							"e01" : "http://3.bp.blogspot.com/-wJ5KwQSnrlM/VcVqpaWpcWI/AAAAAAAAAQg/QeJOjVEolMw/s1600/download_square.png",
							"e02" : "www.e02downloadlink.com",
							"e03" : "www.e03downloadlink.com",
							"e04" : "www.e04downloadlink.com",
						},
					"s02" :
						{
							"e01" : "www.e01downloadlink.com",
							"e02" : "www.e02downloadlink.com",
							"e03" : "www.e03downloadlink.com",
							"e04" : "www.e04downloadlink.com",
						},
					},

		"Vikings" : {
					"s01" :
						{
							"e01" : "www.e01downloadlink.com",
							"e02" : "www.e02downloadlink.com",
							"e03" : "www.e03downloadlink.com",
							"e04" : "www.e04downloadlink.com",
						},
					"s02" :
						{
							"e01" : "www.e01downloadlink.com",
							"e02" : "www.e02downloadlink.com",
							"e03" : "www.e03downloadlink.com",

							"e04" : "www.e04downloadlink.com",
						},
					},
		} 

class App(QMainWindow, tvdownloader.Ui_MainWindow):
	serName = ""
	seaName = ""
	episName = ""

	def __init__(self):
		QMainWindow.__init__(self)
		self.setupUi(self)
		self.openSeries()
		

		 
	def openSeries(self):
		series = []

		for i in boy:
			series.append(i)

		self.listWidget.addItems(sorted(series))
		self.listWidget.itemDoubleClicked.connect(self.openSeasons)
		
		
	def openSeasons(self, item):
		self.listWidget.itemDoubleClicked.disconnect(self.openSeasons)
		self.serName = item.text()
		seasons = []
		for i in boy[self.serName]:
			seasons.append(i)
		
		self.listWidget.clear()
		self.listWidget.addItems(sorted(seasons))
		self.listWidget.itemDoubleClicked.connect(self.openEpisodes)
	
	def openEpisodes(self, item):
		self.listWidget.itemDoubleClicked.disconnect(self.openEpisodes)
		self.seaName = item.text()
		episodes = []
		for i in boy[self.serName][self.seaName]:
			episodes.append(i)
		self.listWidget.clear()
		self.listWidget.addItems(sorted(episodes))
		self.listWidget.itemDoubleClicked.connect(self.download)

	def download(self, item):
		self.episName = item.text()
		url = boy[self.serName][self.seaName][self.episName]
		#print(url)
		#opens file dialog for savind download location
		save_file = QFileDialog.getSaveFileName(self, caption="Save File as", directory=".",
                                                filter="All files(*.*)")
        #save location in string format
		save_location = QDir.toNativeSeparators(save_file)

		try:
			urllib.request.urlretrieve(url, save_location, self.report)
		except Exception:
			QMessageBox.warning(self, "Warning", "The download failed")
			return

		QMessageBox.information(self, "Information", "The download is complete" )
		self.progressBar.setValue(0)
        

	def report(self, blocknum, blocksize, totalsize):
		readsofar = blocknum * blocksize
		if totalsize > 0:
			percent = readsofar * 100/totalsize
			self.progressBar.setValue(int(percent))


app = QApplication(sys.argv)
window = App()
app.setStyleSheet(qdarkstyle.load_stylesheet())
window.show()
app.exec_()
