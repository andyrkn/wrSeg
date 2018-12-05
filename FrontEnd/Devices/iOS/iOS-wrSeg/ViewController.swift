//
//  ViewController.swift
//  iOS-wrSeg
//
//  Created by v7808911 on 03/12/2018.
//  Copyright © 2018 Amazon. All rights reserved.
//

import UIKit
import os

class ViewController: UIViewController, UITextFieldDelegate, UIImagePickerControllerDelegate, UINavigationControllerDelegate {
    
    // MARK: Properties
    
    @IBOutlet weak var photoImageView: UIImageView!
    @IBOutlet weak var treshholdLabel: UILabel!
    @IBOutlet weak var treshholdSlider: UISlider!
    @IBOutlet weak var noiseLabel: UILabel!
    @IBOutlet weak var noiseSlider: UISlider!
    @IBOutlet weak var useGaussSwitch: UISwitch!
    @IBOutlet weak var advancedSettingsButton: UIButton!
    @IBOutlet weak var submitButton: UIButton!
    @IBOutlet weak var historyButton: UIBarButtonItem!
    @IBOutlet weak var resultButton: UIBarButtonItem!
    
    override func viewDidLoad() {
        super.viewDidLoad()
        
        // Initialize Treshold slider and label.
        let tresholdValue = Float(0.5)
        treshholdSlider.value = tresholdValue
        treshholdLabel.text = String(tresholdValue)
        
        // Initialize Noise slider and label.
        let noiseValue = Float(50)
        noiseSlider.value = noiseValue
        noiseLabel.text = String(noiseValue)
        
        // Initialize Use Gauss switch.
        useGaussSwitch.isOn = false
        
        historyButton.isEnabled = true
        resultButton.isEnabled = false
    }
    
    // To make navigation buttons be enabled.
    override func viewWillAppear(_ animated: Bool) {
        super.viewWillAppear(animated)
        
        // To make navigation buttons be enabled after navigation to other view.
        self.navigationController?.navigationBar.tintAdjustmentMode = .normal
        self.navigationController?.navigationBar.tintAdjustmentMode = .automatic
    }
    
    override func didReceiveMemoryWarning() {
        super.didReceiveMemoryWarning()
        // Dispose of any resources that can be recreated.
    }
    
    // This method lets you configure a view controller before it's presented.
    override func prepare(for segue: UIStoryboardSegue, sender: Any?) {
        super.prepare(for: segue, sender: sender)
        
        
        
    }
    
    //MARK: UIImagePickerControllerDelegate
    
    func imagePickerControllerDidCancel(_ picker: UIImagePickerController) {
        // Dismiss the picker if the user canceled.
        dismiss(animated: true, completion: nil)
    }
    
    func imagePickerController(_ picker: UIImagePickerController, didFinishPickingMediaWithInfo info: [String : Any]) {
        
        // The info dictionary may contain multiple representations of the image. You want to use the original.
        guard let selectedImage = info[UIImagePickerControllerOriginalImage] as? UIImage else {
            fatalError("Expected a dictionary containing an image, but was provided the following: \(info)")
        }
        
        // Set photoImageView to display the selected image.
        photoImageView.image = selectedImage
        
        // Dismiss the picker.
        dismiss(animated: true, completion: nil)
    }
    
    func startIndicatorView() {
        let alert = UIAlertController(title: nil, message: "Please wait...", preferredStyle: .alert)
        
        let loadingIndicator = UIActivityIndicatorView(frame: CGRect(x: 10, y: 5, width: 50, height: 50))
        loadingIndicator.hidesWhenStopped = true
        loadingIndicator.activityIndicatorViewStyle = UIActivityIndicatorViewStyle.gray
        loadingIndicator.startAnimating();
        
        alert.view.addSubview(loadingIndicator)
        present(alert, animated: true, completion: nil)
    }
    
    @objc func stopIndicatorView() {
        dismiss(animated: false, completion: nil)
    }
    
    //MARK: Actions
    
    @IBAction func selectImageFromPhotoLibrary(_ sender: Any) {
        let image = UIImagePickerController()
        image.delegate = self
        image.sourceType = .photoLibrary
        present(image, animated: true, completion: nil)
    }
    
    @IBAction func selectValueForTrashold(_ sender: UISlider) {
        self.treshholdLabel.text = String(sender.value)
    }
    
    @IBAction func selectValueForNoise(_ sender: UISlider) {
        self.noiseLabel.text = String(sender.value)
    }
    
    @IBAction func submitNewPhoto(_ sender: Any) {
        
        // MAKE REQUEST TO SERVER HERE
        
        print("Treshold: " + String(treshholdSlider.value))
        print("Noise: " + String(noiseSlider.value))
        print("Gause: " + String(useGaussSwitch.isOn))
        
        resultButton.isEnabled = true
        
        startIndicatorView()
        
        // Set timer to delete indicator.
        Timer.scheduledTimer(timeInterval: 3.0, target: self, selector: #selector(stopIndicatorView), userInfo: nil, repeats: false);
        
    }
}
