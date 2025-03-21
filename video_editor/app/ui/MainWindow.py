# Form implementation generated from reading ui file 'video_editor/app/ui/mainwindow.ui'
#
# Created by: PyQt6 UI code generator 6.8.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(705, 676)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(0, 0))
        MainWindow.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.frame = QtWidgets.QFrame(parent=self.centralwidget)
        self.frame.setFrameShape(QtWidgets.QFrame.Shape.NoFrame)
        self.frame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame.setObjectName("frame")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.frame)
        self.horizontalLayout_5.setContentsMargins(12, 0, 0, 0)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.btn_select = QtWidgets.QPushButton(parent=self.frame)
        icon = QtGui.QIcon.fromTheme("QIcon::ThemeIcon::DocumentOpen")
        self.btn_select.setIcon(icon)
        self.btn_select.setDefault(True)
        self.btn_select.setObjectName("btn_select")
        self.horizontalLayout_5.addWidget(self.btn_select)
        self.btn_export = QtWidgets.QPushButton(parent=self.frame)
        icon = QtGui.QIcon.fromTheme("QIcon::ThemeIcon::DocumentSave")
        self.btn_export.setIcon(icon)
        self.btn_export.setObjectName("btn_export")
        self.horizontalLayout_5.addWidget(self.btn_export)
        spacerItem = QtWidgets.QSpacerItem(562, 38, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem)
        self.label_fps = QtWidgets.QLabel(parent=self.frame)
        self.label_fps.setMinimumSize(QtCore.QSize(80, 0))
        self.label_fps.setObjectName("label_fps")
        self.horizontalLayout_5.addWidget(self.label_fps)
        self.label_resolution = QtWidgets.QLabel(parent=self.frame)
        self.label_resolution.setMinimumSize(QtCore.QSize(180, 0))
        self.label_resolution.setObjectName("label_resolution")
        self.horizontalLayout_5.addWidget(self.label_resolution)
        self.verticalLayout_2.addWidget(self.frame)
        self.frame_3 = QtWidgets.QFrame(parent=self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_3.sizePolicy().hasHeightForWidth())
        self.frame_3.setSizePolicy(sizePolicy)
        self.frame_3.setFrameShape(QtWidgets.QFrame.Shape.NoFrame)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_3.setObjectName("frame_3")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.frame_3)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_video = QtWidgets.QLabel(parent=self.frame_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.label_video.sizePolicy().hasHeightForWidth())
        self.label_video.setSizePolicy(sizePolicy)
        self.label_video.setMinimumSize(QtCore.QSize(0, 0))
        self.label_video.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.label_video.setAutoFillBackground(False)
        self.label_video.setTextFormat(QtCore.Qt.TextFormat.AutoText)
        self.label_video.setScaledContents(False)
        self.label_video.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_video.setObjectName("label_video")
        self.horizontalLayout_2.addWidget(self.label_video)
        self.scroll__area = QtWidgets.QScrollArea(parent=self.frame_3)
        self.scroll__area.setMinimumSize(QtCore.QSize(200, 0))
        self.scroll__area.setMaximumSize(QtCore.QSize(200, 16777215))
        self.scroll__area.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.scroll__area.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.SizeAdjustPolicy.AdjustToContents)
        self.scroll__area.setWidgetResizable(True)
        self.scroll__area.setObjectName("scroll__area")
        self.scrollAreaWidgetContents_2 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_2.setGeometry(QtCore.QRect(0, 0, 198, 443))
        self.scrollAreaWidgetContents_2.setObjectName("scrollAreaWidgetContents_2")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents_2)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_saturation = QtWidgets.QLabel(parent=self.scrollAreaWidgetContents_2)
        self.label_saturation.setMinimumSize(QtCore.QSize(150, 0))
        self.label_saturation.setMaximumSize(QtCore.QSize(150, 16777215))
        self.label_saturation.setObjectName("label_saturation")
        self.verticalLayout_3.addWidget(self.label_saturation)
        self.slider_saturation = QtWidgets.QSlider(parent=self.scrollAreaWidgetContents_2)
        self.slider_saturation.setMinimumSize(QtCore.QSize(150, 0))
        self.slider_saturation.setMaximumSize(QtCore.QSize(150, 16777215))
        self.slider_saturation.setMinimum(-100)
        self.slider_saturation.setMaximum(100)
        self.slider_saturation.setOrientation(QtCore.Qt.Orientation.Horizontal)
        self.slider_saturation.setTickPosition(QtWidgets.QSlider.TickPosition.NoTicks)
        self.slider_saturation.setObjectName("slider_saturation")
        self.verticalLayout_3.addWidget(self.slider_saturation)
        self.label_brightness = QtWidgets.QLabel(parent=self.scrollAreaWidgetContents_2)
        self.label_brightness.setMinimumSize(QtCore.QSize(150, 0))
        self.label_brightness.setMaximumSize(QtCore.QSize(150, 16777215))
        self.label_brightness.setObjectName("label_brightness")
        self.verticalLayout_3.addWidget(self.label_brightness)
        self.slider_brightness = QtWidgets.QSlider(parent=self.scrollAreaWidgetContents_2)
        self.slider_brightness.setMinimumSize(QtCore.QSize(150, 0))
        self.slider_brightness.setMaximumSize(QtCore.QSize(150, 16777215))
        self.slider_brightness.setMinimum(-100)
        self.slider_brightness.setMaximum(100)
        self.slider_brightness.setOrientation(QtCore.Qt.Orientation.Horizontal)
        self.slider_brightness.setObjectName("slider_brightness")
        self.verticalLayout_3.addWidget(self.slider_brightness)
        self.label_sepia = QtWidgets.QLabel(parent=self.scrollAreaWidgetContents_2)
        self.label_sepia.setMinimumSize(QtCore.QSize(150, 0))
        self.label_sepia.setMaximumSize(QtCore.QSize(150, 16777215))
        self.label_sepia.setObjectName("label_sepia")
        self.verticalLayout_3.addWidget(self.label_sepia)
        self.slider_sepia = QtWidgets.QSlider(parent=self.scrollAreaWidgetContents_2)
        self.slider_sepia.setMinimumSize(QtCore.QSize(150, 0))
        self.slider_sepia.setMaximumSize(QtCore.QSize(150, 16777215))
        self.slider_sepia.setMaximum(100)
        self.slider_sepia.setOrientation(QtCore.Qt.Orientation.Horizontal)
        self.slider_sepia.setObjectName("slider_sepia")
        self.verticalLayout_3.addWidget(self.slider_sepia)
        self.label_blur = QtWidgets.QLabel(parent=self.scrollAreaWidgetContents_2)
        self.label_blur.setMinimumSize(QtCore.QSize(150, 0))
        self.label_blur.setMaximumSize(QtCore.QSize(150, 16777215))
        self.label_blur.setObjectName("label_blur")
        self.verticalLayout_3.addWidget(self.label_blur)
        self.slider_blur = QtWidgets.QSlider(parent=self.scrollAreaWidgetContents_2)
        self.slider_blur.setMinimumSize(QtCore.QSize(150, 0))
        self.slider_blur.setMaximumSize(QtCore.QSize(150, 16777215))
        self.slider_blur.setMaximum(20)
        self.slider_blur.setOrientation(QtCore.Qt.Orientation.Horizontal)
        self.slider_blur.setTickPosition(QtWidgets.QSlider.TickPosition.NoTicks)
        self.slider_blur.setObjectName("slider_blur")
        self.verticalLayout_3.addWidget(self.slider_blur)
        self.label_canny = QtWidgets.QLabel(parent=self.scrollAreaWidgetContents_2)
        self.label_canny.setMinimumSize(QtCore.QSize(150, 0))
        self.label_canny.setMaximumSize(QtCore.QSize(150, 16777215))
        self.label_canny.setObjectName("label_canny")
        self.verticalLayout_3.addWidget(self.label_canny)
        self.slider_canny = QtWidgets.QSlider(parent=self.scrollAreaWidgetContents_2)
        self.slider_canny.setMinimumSize(QtCore.QSize(150, 0))
        self.slider_canny.setMaximumSize(QtCore.QSize(150, 16777215))
        self.slider_canny.setMaximum(255)
        self.slider_canny.setOrientation(QtCore.Qt.Orientation.Horizontal)
        self.slider_canny.setObjectName("slider_canny")
        self.verticalLayout_3.addWidget(self.slider_canny)
        self.label_sharpen = QtWidgets.QLabel(parent=self.scrollAreaWidgetContents_2)
        self.label_sharpen.setMinimumSize(QtCore.QSize(150, 0))
        self.label_sharpen.setMaximumSize(QtCore.QSize(150, 16777215))
        self.label_sharpen.setObjectName("label_sharpen")
        self.verticalLayout_3.addWidget(self.label_sharpen)
        self.slider_sharpen = QtWidgets.QSlider(parent=self.scrollAreaWidgetContents_2)
        self.slider_sharpen.setMinimumSize(QtCore.QSize(150, 0))
        self.slider_sharpen.setMaximumSize(QtCore.QSize(150, 16777215))
        self.slider_sharpen.setMaximum(5)
        self.slider_sharpen.setOrientation(QtCore.Qt.Orientation.Horizontal)
        self.slider_sharpen.setTickPosition(QtWidgets.QSlider.TickPosition.NoTicks)
        self.slider_sharpen.setObjectName("slider_sharpen")
        self.verticalLayout_3.addWidget(self.slider_sharpen)
        self.label_hue = QtWidgets.QLabel(parent=self.scrollAreaWidgetContents_2)
        self.label_hue.setMaximumSize(QtCore.QSize(150, 16777215))
        self.label_hue.setObjectName("label_hue")
        self.verticalLayout_3.addWidget(self.label_hue)
        self.dial_hue = QtWidgets.QDial(parent=self.scrollAreaWidgetContents_2)
        self.dial_hue.setMinimumSize(QtCore.QSize(170, 0))
        self.dial_hue.setMaximumSize(QtCore.QSize(170, 16777215))
        self.dial_hue.setMinimum(-180)
        self.dial_hue.setMaximum(180)
        self.dial_hue.setSliderPosition(0)
        self.dial_hue.setWrapping(True)
        self.dial_hue.setNotchesVisible(True)
        self.dial_hue.setObjectName("dial_hue")
        self.verticalLayout_3.addWidget(self.dial_hue)
        self.scroll__area.setWidget(self.scrollAreaWidgetContents_2)
        self.horizontalLayout_2.addWidget(self.scroll__area)
        self.verticalLayout_2.addWidget(self.frame_3)
        self.frame_2 = QtWidgets.QFrame(parent=self.centralwidget)
        self.frame_2.setFrameShape(QtWidgets.QFrame.Shape.NoFrame)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_2.setObjectName("frame_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.frame_2)
        self.horizontalLayout.setContentsMargins(12, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.btn_play_pause = QtWidgets.QPushButton(parent=self.frame_2)
        icon = QtGui.QIcon.fromTheme("QIcon::ThemeIcon::MediaPlaybackStart")
        self.btn_play_pause.setIcon(icon)
        self.btn_play_pause.setObjectName("btn_play_pause")
        self.horizontalLayout.addWidget(self.btn_play_pause)
        self.btn_stop = QtWidgets.QPushButton(parent=self.frame_2)
        icon = QtGui.QIcon.fromTheme("QIcon::ThemeIcon::MediaPlaybackStop")
        self.btn_stop.setIcon(icon)
        self.btn_stop.setObjectName("btn_stop")
        self.horizontalLayout.addWidget(self.btn_stop)
        self.slider_video = QtWidgets.QSlider(parent=self.frame_2)
        self.slider_video.setOrientation(QtCore.Qt.Orientation.Horizontal)
        self.slider_video.setObjectName("slider_video")
        self.horizontalLayout.addWidget(self.slider_video)
        self.label_time = QtWidgets.QLabel(parent=self.frame_2)
        self.label_time.setObjectName("label_time")
        self.horizontalLayout.addWidget(self.label_time)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.verticalLayout_2.addWidget(self.frame_2)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 705, 37))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setItalic(True)
        self.statusbar.setFont(font)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Video Editor"))
        self.btn_select.setText(_translate("MainWindow", "Select Video"))
        self.btn_export.setText(_translate("MainWindow", "Export"))
        self.label_fps.setText(_translate("MainWindow", "FPS: -"))
        self.label_resolution.setText(_translate("MainWindow", "Resolution: -"))
        self.label_video.setText(_translate("MainWindow", "No file selected"))
        self.label_saturation.setText(_translate("MainWindow", "Saturation"))
        self.label_brightness.setText(_translate("MainWindow", "Brightness"))
        self.label_sepia.setText(_translate("MainWindow", "Sepia"))
        self.label_blur.setText(_translate("MainWindow", "Blur"))
        self.label_canny.setText(_translate("MainWindow", "Canny"))
        self.label_sharpen.setText(_translate("MainWindow", "Sharpen"))
        self.label_hue.setText(_translate("MainWindow", "Hue"))
        self.btn_play_pause.setText(_translate("MainWindow", "Play"))
        self.btn_stop.setText(_translate("MainWindow", "Stop"))
        self.label_time.setText(_translate("MainWindow", "00:00 / 00:00"))
