import { Injectable } from '@angular/core';
import { BehaviorSubject } from 'rxjs';

@Injectable({
    providedIn: 'root'
})
export class FileSharingService {
    constructor() { }

    private coordinatesSubject = new BehaviorSubject<any>({ 'a': 'b' });
    public coordinates = this.coordinatesSubject.asObservable();

    private fileSubject = new BehaviorSubject<File>(new File([], '123'));
    public file = this.fileSubject.asObservable();

    setImage(file: File) {
        this.fileSubject.next(file);
    }

    setxyinfo(data) {
        this.coordinatesSubject.next(data);
    }
}
