import { Injectable } from '@angular/core';
import { HttpClient, HttpHeaders } from '@angular/common/http';
import { FileSharingService } from './file.sharing.service';

@Injectable({
    providedIn: 'root'
})
export class FileService {

    private threshHold = 0.2;

    constructor(
        private httpClient: HttpClient,
        private fileSharingService: FileSharingService) {

        this.fileSharingService.fileThreshHold.subscribe((data) => {
            this.threshHold = data;
        });

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
        return this.httpClient.post('http://192.168.202.130:8082/upload-file', data, httpOptions);
    }
}
