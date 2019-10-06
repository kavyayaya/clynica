//
//  Canv.swift
//  ClynicaApp
//
//  Created by Hrishikesh Bhattu on 06/10/19.
//  Copyright © 2019 Beauth. All rights reserved.
//

import UIKit

class Canv :  UIViewController {


    @IBOutlet weak var weightView: CanvasView!
    @IBOutlet weak var summaryView: CanvasView!
    @IBOutlet weak var medView: CanvasView!
    @IBOutlet weak var durationView: CanvasView!
    
    @IBOutlet weak var addNotesView: CanvasView!
    
    @IBAction func clearButton(_ sender: Any) {
        weightView.clearCanvas()
        summaryView.clearCanvas()
        medView.clearCanvas()
        durationView.clearCanvas()
        addNotesView.clearCanvas()
    }
    override func viewDidLoad() {
    super.viewDidLoad()
    // Do any additional setup after loading the view.
    
}
    
}
