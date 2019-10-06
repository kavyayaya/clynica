//
//  ViewController.swift
//  ClynicaApp
//
//  Created by Winner 77 on 05/10/19.
//  Copyright © 2019 Beauth. All rights reserved.
//

import UIKit



class ViewController: UIViewController {

    @IBOutlet weak var roundedCornersButton: UIButton!
    
    override func viewDidLoad() {
        super.viewDidLoad()
        // Do any additional setup after loading the view.
        roundedCornersButton.layer.cornerRadius = 15
        
    }


}

