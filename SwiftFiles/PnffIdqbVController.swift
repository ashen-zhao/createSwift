//
//  PnffIdqbVController.swift
//  Orange

//  Created by Ashen on 18/06/06.
//  Copyright ©  2018年 BeiLian. All rights reserved.
//

import UIKit 

class PnffIdqbVController: UIViewController {

    public var PnffIdqb:UIScrollView!
    public var YkkhbrFpzjqe:UILabel!
    public var QhvzFbqo:UIColor!


    override func viewDidLoad() {
        super.viewDidLoad()
    }

    public func PnffIdqbTOVC() {

       var realArr = Array<String>()
       realArr.append("PnffIdqb")
       realArr.append("YkkhbrFpzjqe")
       realArr.append("PnffIdqb")
       realArr.append("YkkhbrFpzjqe")

    }

    public func YkkhbrFpzjqeTOVC() {

       var realArr = Array<String>()
       realArr.append("YkkhbrFpzjqe")
       realArr.append("PnffIdqb")
       realArr.append("YkkhbrFpzjqe")
       realArr.append("YkkhbrFpzjqe")

    }

    public func QhvzFbqoTOVC() {

       var realArr = Array<String>()
       realArr.append("QhvzFbqo")
       realArr.append("QhvzFbqo")
       realArr.append("PnffIdqb")

    }

}