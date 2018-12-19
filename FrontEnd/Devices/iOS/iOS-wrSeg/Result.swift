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
    var originalImage: UIImage?
    // Parameters.
    var threshold: Double
    var noise: Double
    var useGauss: Bool
    // Advanced settings.
    var maxColumnSep: Double
    var maxSep: Double
    var minScale: Double
    var maxLines: Double
    // Result coordonates.
    var results: [[Int]] = []
    
    //MARK: Constants
    
    static let DEFAULT_THRESHOLD: Double = 0.2
    static let DEFAULT_NOISE: Double = 8.0
    static let DEFAULT_USE_GAUSS: Bool = false
    static let DEFAULT_MAX_COLUMN_SEP: Double = 3
    static let DEFAULT_MAX_SEP: Double = 0
    static let DEFAULT_MIN_SCALE: Double = 12
    static let DEFAULT_MAX_LINES: Double = 300
    
    //MARK: Archiving Paths
    
    static let DocumentsDirectory = FileManager().urls(for: .documentDirectory, in: .userDomainMask).first!
    static let ArchiveURL = DocumentsDirectory.appendingPathComponent("results")
    
    //MARK: Types
    
    struct PropertyKey {
        static let title = "title"
        static let originalImage = "originalImage"
        static let threshold = "threshold"
        static let noise = "noise"
        static let useGauss = "useGauss"
        static let maxColumnSep = "maxColumnSep"
        static let maxSep = "maxSep"
        static let minScale = "minScale"
        static let maxLines = "maxLines"
    }
    
    init?(title: String, originalImage: UIImage?, threshold: Double, noise: Double, useGauss: Bool, maxColumnSep: Double, maxSep: Double, minScale: Double, maxLines: Double) {
        
        // Fail if we don't have title.
        guard !title.isEmpty else {
            return nil
        }
        
        // Fail if we don't have image.
        guard originalImage != nil else {
            return nil
        }
        
        self.title = title
        self.originalImage = originalImage
        self.threshold = threshold
        self.noise = noise
        self.useGauss = useGauss
        self.maxColumnSep = maxColumnSep
        self.maxSep = maxSep
        self.minScale = minScale
        self.maxLines = maxLines
        
    }
    
    //MARK: NSCoding
    
    func encode(with aCoder: NSCoder) {
        aCoder.encode(title, forKey: PropertyKey.title)
        aCoder.encode(originalImage, forKey: PropertyKey.originalImage)
        aCoder.encode(threshold, forKey: PropertyKey.threshold)
        aCoder.encode(noise, forKey: PropertyKey.noise)
        aCoder.encode(useGauss, forKey: PropertyKey.useGauss)
        aCoder.encode(maxColumnSep, forKey: PropertyKey.maxColumnSep)
        aCoder.encode(maxSep, forKey: PropertyKey.maxSep)
        aCoder.encode(minScale, forKey: PropertyKey.minScale)
        aCoder.encode(maxLines, forKey: PropertyKey.maxLines)
        
    }
    
    required convenience init?(coder aDecoder: NSCoder) {
        
        guard let title = aDecoder.decodeObject(forKey: PropertyKey.title) as? String else {
            os_log("Unable to decode the title for a Result object.", log: OSLog.default, type: .debug)
            return nil
        }

        guard let originalImage = aDecoder.decodeObject(forKey: PropertyKey.originalImage) as? UIImage? else {
            os_log("Unable to decode the image for a Result object.", log: OSLog.default, type: .debug)
            return nil
        }
        
        guard let threshold = aDecoder.decodeObject(forKey: PropertyKey.threshold) as? Double! else {
            os_log("Unable to decode the threshold for a Result object.", log: OSLog.default, type: .debug)
            return nil
        }
        
        guard let noise = aDecoder.decodeObject(forKey: PropertyKey.noise) as? Double! else {
            os_log("Unable to decode the noise for a Result object.", log: OSLog.default, type: .debug)
            return nil
        }
        
        guard let useGauss = aDecoder.decodeObject(forKey: PropertyKey.useGauss) as? Bool! else {
            os_log("Unable to decode the useGauss for a Result object.", log: OSLog.default, type: .debug)
            return nil
        }
        
        guard let maxColumnSep = aDecoder.decodeObject(forKey: PropertyKey.maxColumnSep) as? Double! else {
            os_log("Unable to decode the maxColumnSep for a Result object.", log: OSLog.default, type: .debug)
            return nil
        }
        
        guard let maxSep = aDecoder.decodeObject(forKey: PropertyKey.maxSep) as? Double! else {
            os_log("Unable to decode the maxSep for a Result object.", log: OSLog.default, type: .debug)
            return nil
        }
        
        guard let minScale = aDecoder.decodeObject(forKey: PropertyKey.minScale) as? Double! else {
            os_log("Unable to decode the minScale for a Result object.", log: OSLog.default, type: .debug)
            return nil
        }
        
        guard let maxLines = aDecoder.decodeObject(forKey: PropertyKey.maxLines) as? Double! else {
            os_log("Unable to decode the maxLines for a Result object.", log: OSLog.default, type: .debug)
            return nil
        }
        
        self.init(title: title, originalImage: originalImage, threshold: threshold, noise: noise, useGauss: useGauss, maxColumnSep: maxColumnSep, maxSep: maxSep, minScale: minScale, maxLines: maxLines)
        
    }
    

}
