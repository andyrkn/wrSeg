import { Component, OnInit } from '@angular/core';
import { UploadEvent, UploadFile, FileSystemFileEntry, FileSystemDirectoryEntry } from 'ngx-file-drop';
import { FileService } from 'src/app/common/services/files.service';
import { toDate } from '@angular/common/src/i18n/format_date';
import { FileSharingService } from 'src/app/common/services/file.sharing.service';

@Component({
    selector: 'app-file-upload',
    templateUrl: './file-upload.component.html',
    styleUrls: ['./file-upload.component.css']
})
export class FileUploadComponent implements OnInit {

    public bg: any;
    public files: UploadFile[] = [];

    public table = document.getElementById('tb1');

    constructor(
        private fileService: FileService,
        private fileSharingService: FileSharingService) { }

    ngOnInit() {
        this.fileSharingService.setImage(new File([], '123'));
    }

    public dropped(event: UploadEvent) {
        this.files = event.files;
        for (const droppedFile of event.files) {
            if (droppedFile.fileEntry.isFile) {
                const fileEntry = droppedFile.fileEntry as FileSystemFileEntry;
                fileEntry.file((file: File) => {

                    const element = document.getElementById('dragdrop');
                    // sorry its messy pls fix it

                    const reader = new FileReader();
                    reader.onload = ((elem) => {
                        return (e) => { elem.style.backgroundImage = 'url(' + e.target.result + ')'; };
                    })(element);
                    reader.readAsDataURL(file);

                    this.fileSharingService.setImage(new File([], '123'));

                    this.fileService.upload(file)
                        .subscribe(data => { this.fileSharingService.setxyinfo(data); this.fileSharingService.setImage(file); },
                            err => { console.log(err); });

                    // this.fileSharingService.setxyinfo(this.data); //call with coordinates from backend
                    // this.fileSharingService.setImage(file);
                });
            } else {
                const fileEntry = droppedFile.fileEntry as FileSystemDirectoryEntry;
                // console.log(droppedFile.relativePath, fileEntry);
            }
        }
    }

    public fileOver(event) {
        // console.log(event);
    }

    public fileLeave(event) {
        // console.log(event);
    }
}
