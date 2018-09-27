# -*- coding: utf-8 -*-

import random

import os,sys

import string

#创建.swift文件

def createSwift(fileNmae,propertyNumber,methodArray):

    full_path =  sys.path[0] + '/SwiftFiles/' + fileNmae + '.swift'

    file = open(full_path, 'w')

    file.write('//\n//  '+fileNmae+'.swift\n//  BLQbank\n\n//  Created by Ashen on 18/09/27.\n//  Copyright ©  2018年 BeiLian. All rights reserved.\n//\n\n')

    file.write('import UIKit \n\n' + 'class '+fileNmae+': UIViewController {\n\n')
    
    propryNameArray = []

    for index in range(1,propertyNumber):

        propryNameArray.append(random.choice(array))

    propryNameArray = list(set(propryNameArray))

    for propertyName in propryNameArray:

        file.write('    public var '+propertyName+':'+random.choice(classArray)+'!\n')

    file.write('\n\n')
    
    file.write('    override func viewDidLoad() {\n        super.viewDidLoad()\n    }\n\n')
   

    for methodName in methodArray:

        file.write('    public func '+methodName+'_Method() {\n\n       var realArr = Array<String>()\n')

        number = random.randint(3, 10)

        for i in range(1,number):

            file.write('       realArr.append("'+random.choice(array)+'")\n')

        file.write('\n    }\n\n')

    file.write('}')

    file.close()

    print('Done')


def createClassName():
    
    first = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    second = "abcdefghijklmnopqrstuvwxyz"

    index = 0

    array = []

    # 设置生成多少个类
    classNumber = 7
    for i in range(classNumber):

        final=(random.choice(first))

        index = random.randint(3, 5)

        for i in range(index):

            final+=(random.choice(second))

        final += (random.choice(first))

        for i in range(index):

            final+=(random.choice(second))

        array.append(final)
    return array

#属性类型
classArray = ['UIColor','UILabel','UITableView','UISlider','UIScrollView','UIView','UIButton','UITextView']

array = createClassName()

array = list(set(array))


enterfileNmae = 'AAAAAAAAAAAAA_EnterVC'

full_path =  sys.path[0] + '/SwiftFiles/' + enterfileNmae + '.swift'

file = open(full_path, 'w')

file.write('//\n//  '+enterfileNmae+'.swift\n//  BLQbank\n\n//  Created by Ashen on 18/09/27.\n//  Copyright ©  2018年 BeiLian. All rights reserved.\n//\n\n')

file.write('import UIKit \n\n' + 'class '+enterfileNmae+': UIViewController {\n\n')

file.write('    override func viewDidLoad() {\n       super.viewDidLoad()\n  ')

for name in array:
    file.write('\n\n       let '+name+'_vc = '+name+'VCtler()')
    number = random.randint(3, 10)

    methodArray = []

    for i in range(1,5):

        methodArray.append(random.choice(array))

    methodArray = list(set(methodArray))#数组去重
    createSwift(name+'VCtler',number,methodArray)
    file.write('\n\n       '+name+'_vc.'+methodArray[0]+'_Method()')

file.write('\n    }\n\n')
file.write('}')

