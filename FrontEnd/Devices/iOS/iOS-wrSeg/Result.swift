//
//  Result.swift
//  iOS-wrSeg
//
//  Created by v7808911 on 03/12/2018.
//  Copyright © 2018 Amazon. All rights reserved.
//

import UIKit
import Foundation
import os

class Result: NSObject, NSCoding {
    
    //MARK: Properties

    var title: String
    var image: UIImage?
    
    //MARK: Archiving Paths
    
    static let DocumentsDirectory = FileManager().urls(for: .documentDirectory, in: .userDomainMask).first!
    static let ArchiveURL = DocumentsDirectory.appendingPathComponent("results")
    
    //MARK: Types
    
    struct PropertyKey {
        static let title = "title"
        static let image = "image"
    }
    
    init?(title: String, image: UIImage?) {
        
        // Fail if we don't have title.
        guard !title.isEmpty else {
            return nil
        }
        
        // Fail if we don't have image.
        guard image != nil else {
            return nil
        }
        
        self.title = title
        self.image = image
        
    }
    
    //MARK: NSCoding
    
    func encode(with aCoder: NSCoder) {
        aCoder.encode(title, forKey: PropertyKey.title)
        aCoder.encode(image, forKey: PropertyKey.image)
    }
    
    required convenience init?(coder aDecoder: NSCoder) {
        
        guard let title = aDecoder.decodeObject(forKey: PropertyKey.title) as? String else {
            os_log("Unable to decode the title for a Result object.", log: OSLog.default, type: .debug)
            return nil
        }

        guard let image = aDecoder.decodeObject(forKey: PropertyKey.image) as? UIImage? else {
            os_log("Unable to decode the image for a Result object.", log: OSLog.default, type: .debug)
            return nil
        }
        
        self.init(title: title, image: image)
        
    }
    

}
