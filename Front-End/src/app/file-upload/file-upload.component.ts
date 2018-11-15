import { Component, OnInit } from '@angular/core';
import { FilesService } from '../common/services/files.service';

@Component({
  selector: 'app-file-upload',
  templateUrl: './file-upload.component.html',
  styleUrls: ['./file-upload.component.css']
})
export class FileUploadComponent implements OnInit {

  constructor(private fileService: FilesService) { }

  ngOnInit() {
  }

  uploadFile() {
    const file: any = (<HTMLInputElement>document.getElementById('myfile')).files[0];
    this.fileService.upload(file).subscribe((data) => {
      console.log(data);
    });
  }
}
