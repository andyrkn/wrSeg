//
//  AdvancedSettingsViewController.swift
//  iOS-wrSeg
//
//  Created by v7808911 on 05/12/2018.
//  Copyright © 2018 Amazon. All rights reserved.
//

import UIKit

class AdvancedSettingsViewController: UIViewController {

    // MARK: Properties
    @IBOutlet weak var popupView: UIView!
    
    override func viewDidLoad() {
        super.viewDidLoad()

        popupView.layer.cornerRadius = 10
        popupView.layer.masksToBounds = true
        
        // Do any additional setup after loading the view.
    }

    override func didReceiveMemoryWarning() {
        super.didReceiveMemoryWarning()
        // Dispose of any resources that can be recreated.
    }
    

    @IBAction func goBackToMainView(_ sender: UIButton) {
        dismiss(animated: true, completion: nil)
    }
    

}
