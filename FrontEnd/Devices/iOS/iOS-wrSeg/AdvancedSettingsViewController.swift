//
//  AdvancedSettingsViewController.swift
//  iOS-wrSeg
//
//  Created by v7808911 on 05/12/2018.
//  Copyright © 2018 Amazon. All rights reserved.
//

import UIKit

class AdvancedSettingsViewController: UIViewController, UITextFieldDelegate {

    // MARK: Properties
    @IBOutlet weak var popupView: UIView!
    
    @IBOutlet weak var maxColumnSep: UITextField!
    @IBOutlet weak var maxSep: UITextField!
    @IBOutlet weak var minScale: UITextField!
    @IBOutlet weak var maxLines: UITextField!
    
    @IBOutlet weak var saveButton: UIButton!
    
    override func viewDidLoad() {
        super.viewDidLoad()
        
        maxColumnSep.delegate = self
        maxSep.delegate = self
        minScale.delegate = self
        maxLines.delegate = self

        popupView.layer.cornerRadius = 10
        popupView.layer.masksToBounds = true
        
        updateSaveButtonState()
        
        // Do any additional setup after loading the view.
    }

    override func didReceiveMemoryWarning() {
        super.didReceiveMemoryWarning()
        // Dispose of any resources that can be recreated.
    }
    

    @IBAction func goBackToMainView(_ sender: UIButton) {
        dismiss(animated: true, completion: nil)
    }
    
//    @IBAction func saveSettings(_ sender: Any) {
//        if maxColumnSep.text != "" || maxSep.text != "" || minScale.text != "" || maxLines.text != "" {
//            performSegue(withIdentifier: "segueBackFromSettings", sender: self)
//        }
//    }
    
    override func prepare(for segue: UIStoryboardSegue, sender: Any?) {
        let mainViewController = segue.destination as! ViewController
        
        if self.maxColumnSep.text != "" {
            mainViewController.maxColumnSep = Int(self.maxColumnSep.text!)!
        }
        if self.maxSep.text != "" {
            mainViewController.maxSep = Int(self.maxSep.text!)!
        }
        if self.minScale.text != "" {
            mainViewController.minScale = Float(self.minScale.text!)!
        }
        if self.maxLines.text != "" {
            mainViewController.maxLines = Int(self.maxLines.text!)!
        }
    }
    
    func textField(_ textField: UITextField, shouldChangeCharactersIn range: NSRange, replacementString string: String) -> Bool {
        let allowedCharacters = CharacterSet.decimalDigits
        let characterSet = CharacterSet(charactersIn: string)
        return allowedCharacters.isSuperset(of: characterSet)
    }
    
    func textFieldDidEndEditing(_ textField: UITextField) {
        updateSaveButtonState()
    }
    
    func textFieldShouldReturn(_ textField: UITextField) -> Bool {
        // Hide the keyboard.
        textField.resignFirstResponder()
        return true
    }
    
    private func updateSaveButtonState() {
        // Disable the Save button if the text field is empty.
        if self.maxColumnSep.text != "" || self.maxSep.text != "" || self.minScale.text != "" || self.maxLines.text != "" {
            saveButton.isEnabled = true
        } else {
            saveButton.isEnabled = false
        }
    }
}
