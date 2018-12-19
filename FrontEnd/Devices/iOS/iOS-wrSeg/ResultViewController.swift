//
//  ResultViewController.swift
//  iOS-wrSeg
//
//  Created by v7808911 on 16/12/2018.
//  Copyright © 2018 Amazon. All rights reserved.
//

import UIKit

class ResultViewController: UIViewController, UITextFieldDelegate {
    
    // MARK: Properties
    
    @IBOutlet weak var titleTextField: UITextField!
    
    @IBOutlet weak var labelThreshold: UILabel!
    @IBOutlet weak var labelNoise: UILabel!
    @IBOutlet weak var labelUseGauss: UILabel!
    @IBOutlet weak var labelMaxColumnSep: UILabel!
    @IBOutlet weak var labelMaxSep: UILabel!
    @IBOutlet weak var labelMinScale: UILabel!
    @IBOutlet weak var labelMaxLines: UILabel!
    
    var saveButton: UIBarButtonItem = UIBarButtonItem()
    
    // Parameters.
    var threshold: Double = Result.DEFAULT_THRESHOLD
    var noise: Double = Result.DEFAULT_NOISE
    var useGauss: Bool = Result.DEFAULT_USE_GAUSS
    // Advanced settings.
    var maxColumnSep: Double = Result.DEFAULT_MAX_COLUMN_SEP
    var maxSep: Double = Result.DEFAULT_MAX_SEP
    var minScale: Double = Result.DEFAULT_MIN_SCALE
    var maxLines: Double = Result.DEFAULT_MAX_LINES
    // Result coordonates.
    var results: [[Int]] = []
    

    override func viewDidLoad() {
        super.viewDidLoad()
        
        titleTextField.delegate = self
        
        labelThreshold.text = String(threshold)
        labelNoise.text = String(noise)
        labelUseGauss.text = String(useGauss)
        labelMaxColumnSep.text = String(maxColumnSep)
        labelMaxSep.text = String(maxSep)
        labelMinScale.text = String(minScale)
        labelMaxLines.text = String(maxLines)

        // Do any additional setup after loading the view.
        saveButton.title = "Save"
        navigationItem.rightBarButtonItem = saveButton
        navigationItem.title = "Result"
        print("From result view controller!")
        print(results)
    }

    override func didReceiveMemoryWarning() {
        super.didReceiveMemoryWarning()
        // Dispose of any resources that can be recreated.
    }
    
    //MARK: UITextFieldDelegate
    func textFieldShouldReturn(_ textField: UITextField) -> Bool {
        // Hide the keyboard.
        textField.resignFirstResponder()
        return true
    }
    
    func textFieldDidEndEditing(_ textField: UITextField) {
        navigationItem.title = textField.text
    }
    
    @IBAction func backFromResult(_ sender: Any) {
        dismiss(animated: true, completion: nil)
    }
    
    // MARK: - Navigation

    // In a storyboard-based application, you will often want to do a little preparation before navigation
    override func prepare(for segue: UIStoryboardSegue, sender: Any?) {
        // Get the new view controller using segue.destinationViewController.
        // Pass the selected object to the new view controller.
    }

}
