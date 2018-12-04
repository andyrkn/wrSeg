import { Injectable } from '@angular/core';
import { HttpClient, HttpHeaders } from '@angular/common/http';

@Injectable({
  providedIn: 'root'
})
export class FilesService {

  constructor(private httpClient: HttpClient) { }

  public upload(file) {
    const httpOptions = {
      headers: new HttpHeaders({
        'Allow-Origin': '*',
        'Access-Control-Allow-Origin': '*',
      })
    };

    const data: FormData = new FormData();
    data.append('file', file);
    return this.httpClient.post('http://localhost:8082/upload-file', data, httpOptions);
  }
}
