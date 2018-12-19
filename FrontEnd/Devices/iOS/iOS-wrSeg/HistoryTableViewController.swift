//
//  HistoryTableViewController.swift
//  iOS-wrSeg
//
//  Created by v7808911 on 03/12/2018.
//  Copyright © 2018 Amazon. All rights reserved.
//

import UIKit
import os

class HistoryTableViewController: UITableViewController {
    
    //MARK: Properties
    
    var results = [Result]()
    
    //MARK: Private Methods
    
    private func saveResults() {
        let isSuccessfulSave = NSKeyedArchiver.archiveRootObject(results, toFile: Result.ArchiveURL.path)
        
        if isSuccessfulSave {
            os_log("Results successfully saved.", log: OSLog.default, type: .debug)
        } else {
            os_log("Failed to save results...", log: OSLog.default, type: .error)
        }
    }
    
    private func loadSampleResults() {
        
        let image = UIImage(named: "Script")
        
        guard let result1 = Result(title: "title1",
                                   originalImage: image,
                                   threshold: Result.DEFAULT_THRESHOLD,
                                   noise: Double(Result.DEFAULT_NOISE),
                                   useGauss: Result.DEFAULT_USE_GAUSS,
                                   maxColumnSep: Result.DEFAULT_MAX_COLUMN_SEP,
                                   maxSep: Result.DEFAULT_MAX_SEP,
                                   minScale: Result.DEFAULT_MIN_SCALE,
                                   maxLines: Result.DEFAULT_MAX_LINES) else {
            fatalError("Unable to instantiate result1")
        }
        
        results += [result1, result1, result1, result1]
        
        
    }
    
    // To change the title of the edit button in delete.
    override func setEditing (_ editing:Bool, animated:Bool)
    {
        super.setEditing(editing,animated:animated)
        if(self.isEditing)
        {
            self.editButtonItem.title = "Done"
        } else {
            self.editButtonItem.title = "Delete"
        }
    }
    
    override func viewDidLoad() {
        super.viewDidLoad()
        
        self.tableView.rowHeight = 120.0
        
        // Use the edit button item provided by the table view controller.
        navigationItem.rightBarButtonItem = editButtonItem
        navigationItem.rightBarButtonItem?.title = "Delete"
        navigationItem.title = "History"
                
        // Load any saved results, otherwise load sample data.
        if let savedResults = loadResults() {
            results += savedResults
        } else {
            // Load the sample data.
            loadSampleResults()
        }
    }
    
    override func didReceiveMemoryWarning() {
        super.didReceiveMemoryWarning()
        // Dispose of any resources that can be recreated.
    }
    
    // MARK: - Table view data source
    
    override func numberOfSections(in tableView: UITableView) -> Int {
        return 1
    }
    
    override func tableView(_ tableView: UITableView, numberOfRowsInSection section: Int) -> Int {
        return results.count
    }
    
    override func tableView(_ tableView: UITableView, cellForRowAt indexPath: IndexPath) -> UITableViewCell {
        
        // Table view cells are reused and should be dequeued using a cell identifier.
        let cellIdentifier = "HistoryTableViewCell"
        
        guard let cell = tableView.dequeueReusableCell(withIdentifier: cellIdentifier, for: indexPath) as? HistoryTableViewCell  else {
            fatalError("The dequeued cell is not an instance of HistoryTableViewCell.")
        }
        
        // Fetches the appropriate meal for the data source layout.
        let result = results[indexPath.row]
        
        cell.titleLabel.text = result.title
        cell.imgView.image = result.originalImage
        
        return cell
    }
    
    
    // Override to support conditional editing of the table view.
    override func tableView(_ tableView: UITableView, canEditRowAt indexPath: IndexPath) -> Bool {
        // Return false if you do not want the specified item to be editable.
        return true
    }
    
    
    
    // Override to support editing the table view.
    override func tableView(_ tableView: UITableView, commit editingStyle: UITableViewCellEditingStyle, forRowAt indexPath: IndexPath) {
        if editingStyle == .delete {
            // Delete the row from the data source
            results.remove(at: indexPath.row)
            saveResults()
            
            tableView.deleteRows(at: [indexPath], with: .fade)
        } else if editingStyle == .insert {
            // Create a new instance of the appropriate class, insert it into the array, and add a new row to the table view
        }
    }
    
    
    
    
    /*
     // Override to support rearranging the table view.
     override func tableView(_ tableView: UITableView, moveRowAt fromIndexPath: IndexPath, to: IndexPath) {
     
     }
     */
    
    /*
     // Override to support conditional rearranging of the table view.
     override func tableView(_ tableView: UITableView, canMoveRowAt indexPath: IndexPath) -> Bool {
     // Return false if you do not want the item to be re-orderable.
     return true
     }
     */
    
    private func loadResults() -> [Result]? {
        return NSKeyedUnarchiver.unarchiveObject(withFile: Result.ArchiveURL.path) as? [Result]
    }

}
