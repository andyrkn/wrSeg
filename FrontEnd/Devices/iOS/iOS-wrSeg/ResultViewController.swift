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
    @IBOutlet weak var resultImage: UIImageView!
    
    @IBOutlet weak var resultImageView: UIView!
    
    @IBOutlet weak var labelThreshold: UILabel!
    @IBOutlet weak var labelNoise: UILabel!
    @IBOutlet weak var labelUseGauss: UILabel!
    @IBOutlet weak var labelMaxColumnSep: UILabel!
    @IBOutlet weak var labelMaxSep: UILabel!
    @IBOutlet weak var labelMinScale: UILabel!
    @IBOutlet weak var labelMaxLines: UILabel!
    
    var saveButton: UIBarButtonItem = UIBarButtonItem()
    
    var result: Result = Result()

    override func viewDidLoad() {
        super.viewDidLoad()
        
        let backgroundImage = UIImageView(frame: resultImageView.bounds)
//        backgroundImage.image = UIImage(named: "No photo selected")
        backgroundImage.image = result.originalImage
        backgroundImage.contentMode = UIViewContentMode.scaleAspectFill
        resultImageView.insertSubview(backgroundImage, at: 0)
                
        resultImage.image = result.originalImage
        
        titleTextField.delegate = self
        
        labelThreshold.text = String(result.threshold)
        labelNoise.text = String(result.noise)
        labelUseGauss.text = String(result.useGauss)
        labelMaxColumnSep.text = String(result.maxColumnSep)
        labelMaxSep.text = String(result.maxSep)
        labelMinScale.text = String(result.minScale)
        labelMaxLines.text = String(result.maxLines)

        // Do any additional setup after loading the view.
        saveButton.title = "Save"
        navigationItem.rightBarButtonItem = saveButton
        navigationItem.title = "Result"
        print("From result view controller!")
        print(result.results)
        
        resultImage.image = drawRectangleOnImage(image: result.originalImage!)
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
    
    func drawRectangleOnImage(image: UIImage) -> UIImage {
        let imageSize = image.size
        let scale: CGFloat = 0
        UIGraphicsBeginImageContextWithOptions(imageSize, false, scale)
        
        image.draw(at: CGPoint.zero)
        
        for rectangle in result.results {
            let x1 = rectangle[0]
            let y1 = rectangle[1]
            let x2 = rectangle[2]
            let y2 = rectangle[3]
            print(x1, y1, x2, y2)
            
            let width = x2 - x1
            let height = y2 - y1
            
            let toDrawRect = CGRect(x: x1, y: y1, width: width, height: height)
            
            UIColor.blue.withAlphaComponent(0.5).setFill()

            UIRectFill(toDrawRect)
        }
        
        let newImage = UIGraphicsGetImageFromCurrentImageContext()
        UIGraphicsEndImageContext()
        return newImage!
    }
}
