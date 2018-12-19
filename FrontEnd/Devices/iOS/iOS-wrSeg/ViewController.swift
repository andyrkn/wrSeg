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
    
    var maxColumnSep = Result.DEFAULT_MAX_COLUMN_SEP
    var maxSep = Result.DEFAULT_MAX_SEP
    var minScale = Result.DEFAULT_MIN_SCALE
    var maxLines = Result.DEFAULT_MAX_LINES
    var results: [[Int]] = []
    
    override func viewDidLoad() {
        super.viewDidLoad()
        

        
        print("Max col sep: " + String(maxColumnSep))
        print("Max sep: " + String(maxSep))
        print("Min scale: " + String(minScale))
        print("Max lines: " + String(maxLines))
        
        // Initialize Treshold slider and label.
        let tresholdValue = Float(Result.DEFAULT_THRESHOLD)
        treshholdSlider.value = tresholdValue
        treshholdLabel.text = String(tresholdValue)
        
        // Initialize Noise slider and label.
        let noiseValue = Float(Result.DEFAULT_NOISE)
        noiseSlider.value = noiseValue
        noiseLabel.text = String(noiseValue)
        
        // Initialize Use Gauss switch.
        useGaussSwitch.isOn = Result.DEFAULT_USE_GAUSS
        
        historyButton.isEnabled = true
        resultButton.isEnabled = false
        submitButton.isEnabled = false
        
        // REMOVE
        self.resultButton.isEnabled = true

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
        
        if segue.identifier == "segueShowResult" {
            let resultViewController = segue.destination as! ResultViewController
            if !results.isEmpty {
                resultViewController.results = results
                resultViewController.threshold = Double(treshholdSlider.value)
                resultViewController.noise = Double(noiseSlider.value)
                resultViewController.useGauss = useGaussSwitch.isOn
                resultViewController.maxColumnSep = maxColumnSep
                resultViewController.maxSep = maxSep
                resultViewController.minScale = minScale
                resultViewController.maxLines = maxLines
                print("Results sent to ResultsViewContorller")
            }
        }
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
        updateSaveButtonState()
        
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
        print("\nI try to stop indicator view!\n")
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
    
    @IBAction func displayResults(_ sender: Any) {
//        if !results.isEmpty {
            performSegue(withIdentifier: "segueShowResult", sender: self)
//        }
    }
    
    @IBAction func submitNewPhoto(_ sender: Any) {
        startIndicatorView()
        
        print("Treshold: " + String(treshholdSlider.value))
        print("Noise: " + String(noiseSlider.value))
        print("Gauss: " + String(useGaussSwitch.isOn))
        
        //declare parameter as a dictionary which contains string as key and value combination. considering inputs are valid
        
        let parameters = ["treshold": String(treshholdSlider.value),
                          "noise": String(noiseSlider.value),
                          "gauss": String(useGaussSwitch.isOn)] as [String : String]
        
        //create the url with URL
        let url = URL(string: "http://localhost:8082/upload-file")! //change the url
        
        //create the session object
        let session = URLSession.shared
        
        //now create the URLRequest object using the url object
        var request = URLRequest(url: url)
        request.httpMethod = "POST" //set http method as POST
        
        let boundary = "Boundary-\(UUID().uuidString)"
        request.addValue("multipart/form-data; boundary=\(boundary)", forHTTPHeaderField: "Content-Type")
        request.addValue("application/json", forHTTPHeaderField: "Accept")
        
    
        request.httpBody = createBody(parameters: parameters,
                                boundary: boundary,
                                data: UIImageJPEGRepresentation(photoImageView.image!, 0.7)!,
                                mimeType: "image/jpg",
                                filename: "hello.jpg")
    
        
        
        //create dataTask using the session object to send data to the server
        let task = session.dataTask(with: request as URLRequest, completionHandler: { data, response, error in
            
            guard error == nil else {
                return
            }
            
            guard let data = data else {
                return
            }
            
            do {
                //create json object from data
                if let json: Dictionary = try JSONSerialization.jsonObject(with: data, options: .mutableContainers) as? [String: Any] {
                    self.extractJsonData(json: json)
                    self.stopIndicatorView()
                    self.resultButton.isEnabled = true
                }
            } catch let error {
                print(error.localizedDescription)
                self.stopIndicatorView()

            }
        })
        task.resume()
        
    }
    
    @IBAction func unwindToMainMenu(sender: UIStoryboardSegue) {
        
    }
    
    func createBody(parameters: [String: String],
                    boundary: String,
                    data: Data,
                    mimeType: String,
                    filename: String) -> Data {
        var body = Data()
        body.append(Data("foo".utf8))

        
        let boundaryPrefix = "--\(boundary)\r\n"
        
        for (key, value) in parameters {
            body.append(Data(boundaryPrefix.utf8))
            body.append(Data("Content-Disposition: form-data; name=\"\(key)\"\r\n\r\n".utf8))
            body.append(Data("\(value)\r\n".utf8))
        }
        
        body.append(Data(boundaryPrefix.utf8))
        body.append(Data("Content-Disposition: form-data; name=\"file\"; filename=\"\(filename)\"\r\n".utf8))
        body.append(Data("Content-Type: \(mimeType)\r\n\r\n".utf8))
        body.append(data)
        body.append(Data("\r\n".utf8))
        body.append(Data(("--".appending(boundary.appending("--"))).utf8))
        
        return body as Data
    }
    
    private func updateSaveButtonState() {
        // Disable the Save button if the text field is empty.
        let image = photoImageView.image ?? nil
        if image != nil {
            submitButton.isEnabled = true;
        } else {
            submitButton.isEnabled = false;
        }
    }
    
    func extractJsonData(json: Dictionary<String, Any>) {
        for (key, coordsArray) in json {
            if String(key) == "columns" {
                let coordsArrayCast = coordsArray as! NSMutableArray
                for coordArray in coordsArrayCast {
                    let coordArrayCast = coordArray as! NSMutableArray
                    print("Coord set: " + String(describing: coordArrayCast))
                    
                    var coords: [Int] = []
                    for coord in coordArrayCast {
                        let value = coord as! Int
                        coords.append(value)
                    }
                    results.append(coords)
                }
            }
        }
    }
}

extension Data {
    mutating func append(string: String) {
        let data = string.data(
            using: String.Encoding.utf8,
            allowLossyConversion: true)
        append(data!)
    }
}
