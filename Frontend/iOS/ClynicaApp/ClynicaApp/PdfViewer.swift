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
    
    @IBAction func printAction(_ sender: UIButton) {
        if let guide_url = Bundle.main.url(forResource: "sample", withExtension: "pdf"){
            if UIPrintInteractionController.canPrint(guide_url) {
                let printInfo = UIPrintInfo(dictionary: nil)
                printInfo.jobName = guide_url.lastPathComponent
                printInfo.outputType = .photo

                let printController = UIPrintInteractionController.shared
                printController.printInfo = printInfo
                printController.showsNumberOfCopies = false

                printController.printingItem = guide_url

                printController.present(animated: true, completionHandler: nil)
            }
        }
    }
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
