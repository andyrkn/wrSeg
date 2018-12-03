//
//  HistoryTableViewCell.swift
//  iOS-wrSeg
//
//  Created by v7808911 on 03/12/2018.
//  Copyright © 2018 Amazon. All rights reserved.
//

import UIKit

class HistoryTableViewCell: UITableViewCell {

    //MARK: Properties
    
    @IBOutlet weak var titleLabel: UILabel!
    @IBOutlet weak var imgView: UIImageView!

    
    override func awakeFromNib() {
        super.awakeFromNib()
        // Initialization code
    }
    
    override func setSelected(_ selected: Bool, animated: Bool) {
        super.setSelected(selected, animated: animated)
        
        // Configure the view for the selected state
    }
}
