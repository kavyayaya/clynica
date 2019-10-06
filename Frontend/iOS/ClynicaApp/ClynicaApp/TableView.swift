//
//  TableView.swift
//  ClynicaApp
//
//  Created by Hrishikesh Bhattu on 06/10/19.
//  Copyright © 2019 Beauth. All rights reserved.
//

import Foundation
import UIKit

class TableView: UIViewController, UITableViewDelegate, UITableViewDataSource {
    
    let list = ["Crocin", "Combiflam", "Azithral"]

    
    func tableView(_ tableView: UITableView, numberOfRowsInSection section: Int) -> Int {
        return(list.count)
    }
    
    func tableView(_ tableView: UITableView, cellForRowAt indexPath: IndexPath) -> UITableViewCell {
        let cell = UITableViewCell(style: UITableViewCell.CellStyle.default, reuseIdentifier: "cell")
        cell.textLabel?.text = list[indexPath.row]
        
        return(cell)
    }
    
    
}
