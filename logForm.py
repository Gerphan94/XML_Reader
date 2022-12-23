from PyQt5 import QtCore, QtGui, QtWidgets


class logForm():
    def __init__(self, log_ar):
        self.log_list = log_ar

    def setupUi(self, Form):

        Form.setObjectName("logform")
        Form.setWindowTitle("Log")
        Form.setMinimumSize(800, 670)

        self.TREE = QtWidgets.QTreeWidget()
        self.TREE.setColumnCount(1)

        main_l = QtWidgets.QVBoxLayout(Form)
        main_l.addWidget(self.TREE)
        self.init_tree()


    def init_tree(self):
        root = self.TREE.rootIndex()
        for k, log in enumerate(self.log_list):
            ma_lk = log[0]
            detail = log[1]
            item = QtWidgets.QTreeWidgetItem()
            item.setFirstColumnSpanned(True)
            item.setText(0, ma_lk)
            for i, ele in enumerate(detail, start=1):
                if (len(ele) != 0):
                    errors = ele
                    child1 = QtWidgets.QTreeWidgetItem()
                    child1.setText(0, f"XML{i}")
                    
                    if (len(errors) !=0):
                        
                        for ele in errors:
                            child2 = QtWidgets.QTreeWidgetItem()    
                            child2.setText(0, ele)
                            child1.addChild(child2)
                    item.addChild(child1)
            self.TREE.addTopLevelItem(item)
        self.TREE.expandToDepth(1)
           

                
    

    
