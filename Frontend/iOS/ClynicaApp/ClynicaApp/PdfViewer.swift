//
//  PdfViewer.swift
//  ClynicaApp
//
//  Created by Hrishikesh Bhattu on 06/10/19.
//  Copyright © 2019 Beauth. All rights reserved.
//

import UIKit
import PDFKit

@available(iOS 11.0, *)
class PdfViewer: UIViewController {
    
    @IBOutlet weak var PdfView: PDFView!
    
    
    override func viewDidLoad() {
        super.viewDidLoad()
        // Do any additional setup after loading the view, typically from a nib.
        
        if let path = Bundle.main.path(forResource: "sample", ofType: "pdf") {
            
            if let pdfDocument = PDFDocument(url: URL(fileURLWithPath: path)) {
                PdfView.displayMode = .singlePageContinuous
                PdfView.autoScales = true
                PdfView.displayDirection = .vertical
                PdfView.document = pdfDocument
            }
        }
    }

    override func didReceiveMemoryWarning() {
        super.didReceiveMemoryWarning()
        // Dispose of any resources that can be recreated.
    }


}
