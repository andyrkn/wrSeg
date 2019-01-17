import { Injectable } from '@angular/core';
import { HttpClient, HttpHeaders } from '@angular/common/http';
import { FileSharingService } from './file.sharing.service';

@Injectable({
    providedIn: 'root'
})
export class FileService {

    private threshHold = 0.2;
    private maxcolseps = 100;
    private minscale = 0;
    private maxlines = 1000;
    private maxseps = 100;

    constructor(
        private httpClient: HttpClient,
        private fileSharingService: FileSharingService) {

        this.fileSharingService.fileThreshHold.subscribe((data) => { this.threshHold = data; });
        this.fileSharingService.maxColSeps.subscribe((data) => { this.maxcolseps = data; });
        this.fileSharingService.minScale.subscribe((data) => { this.minscale = data; });
        this.fileSharingService.maxLines.subscribe((data) => { this.maxlines = data; });
        this.fileSharingService.maxSeps.subscribe((data) => { this.maxseps = data; });

    }

    public upload(file) {
        const httpOptions = {
            headers: new HttpHeaders({
                'Allow-Origin': '*',
                'Access-Control-Allow-Origin': '*',
            })
        };

        const data: FormData = new FormData();
        data.append('file', file);
        data.append('threshold', this.threshHold.toString());
        data.append('maxcolseps', this.maxcolseps.toString());
        data.append('maxseps', this.maxseps.toString());
        data.append('minscale', this.minscale.toString());
        data.append('maxlines', this.maxlines.toString());
        return this.httpClient.post('http://192.168.202.131:8082/upload-file', data, httpOptions);
    }
}
