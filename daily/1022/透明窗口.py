#python 透明窗口.py
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel
from PyQt5.QtCore import Qt, QTimer
from PyQt5.QtGui import QPixmap, QImage
from PyQt5.QtWidgets import QMenu, QAction  # 如果原本有别的，直接加在后面就行

class DesktopPet(QWidget):
    def __init__(self):
        super().__init__()
        
        self.setWindowFlags(Qt.FramelessWindowHint | Qt.WindowStaysOnTopHint | Qt.Tool)
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.resize(150, 150)
        self.move(100, 100) # 固定在左上角，方便寻找
        
        self.label = QLabel(self)
        self.label.setGeometry(0, 0, 150, 150)
        self.label.setAlignment(Qt.AlignCenter)
        
        # 确保文件名正确
        self.sheet = QPixmap("ff13ae3f64df8b8d7aad4a2a31d32134.png") 
        
        self.frame_width = self.sheet.width() // 6
        self.frame_height = self.sheet.height() // 8
        
        self.current_frame = 0
        self.total_frames = 6
        
        self.timer = QTimer()
        self.timer.timeout.connect(self.update_animation)
        self.timer.start(200)
        
        self.update_animation()

    def update_animation(self):
        col = self.current_frame % 6
        row = 0 
        x = col * self.frame_width
        y = row * self.frame_height
    
    # 1. 直接切图（因为原图已经是透明的了，切出来自然也是透明的）
        cropped_pixmap = self.sheet.copy(x, y, self.frame_width, self.frame_height)
    
    # 2. 直接缩放
        scaled_pixmap = cropped_pixmap.scaled(100, 100, Qt.KeepAspectRatio, Qt.SmoothTransformation)
    
    # 3. 直接显示
        self.label.setPixmap(scaled_pixmap)
    
    # 4. 切换到下一帧
        self.current_frame = (self.current_frame + 1) % self.total_frames
    # 1. 鼠标按下事件：记录鼠标点击时的初始位置
    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
        # 记录当前窗口的左上角坐标，和鼠标点击的全局坐标
            self.dragPosition = event.globalPos() - self.frameGeometry().topLeft()
            event.accept()

    # 2. 鼠标移动事件：拖动窗口
    def mouseMoveEvent(self, event):
        if event.buttons() == Qt.LeftButton:
        # 让窗口移动到：当前鼠标位置 减去 刚才记录的偏移量
            self.move(event.globalPos() - self.dragPosition)
            event.accept()

    # 3. 鼠标松开事件：结束拖拽
    def mouseReleaseEvent(self, event):
        if event.button() == Qt.LeftButton:
            event.accept()
    # 4. 右键菜单事件
    def contextMenuEvent(self, event):
    # 1. 创建一个菜单对象
        menu = QMenu(self)
    
    # 2. 给菜单加上一个“退出”按钮（QAction）
        quit_action = QAction("退出桌宠", self)
    
    # 3. 点击这个按钮时，触发关闭程序的动作
        quit_action.triggered.connect(QApplication.quit) # 或者用 self.close()
    
    # 4. 把按钮放进菜单里
        menu.addAction(quit_action)
    
    # 5. 在鼠标点击的位置（全局坐标）弹出菜单
        menu.exec_(event.globalPos())


if __name__ == '__main__':
    app = QApplication(sys.argv)
    pet = DesktopPet()
    pet.show()
    sys.exit(app.exec_())