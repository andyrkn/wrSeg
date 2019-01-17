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

    private _fileThreshHold: BehaviorSubject<number> = new BehaviorSubject<number>(0.2);
    private _maxColSeps: BehaviorSubject<number> = new BehaviorSubject<number>(100);
    private _minScale: BehaviorSubject<number> = new BehaviorSubject<number>(0);
    private _maxLines: BehaviorSubject<number> = new BehaviorSubject<number>(1000);
    private _maxSeps: BehaviorSubject<number> = new BehaviorSubject<number>(100);

    public get fileThreshHold() {
        return this._fileThreshHold.asObservable();
    }

    public get maxColSeps() {
        return this._maxColSeps.asObservable();
    }

    public setMaxColSeps(x) {
        this._maxColSeps.next(x);
    }

    public get minScale() {
        return this._minScale.asObservable();
    }

    public setMinScale(x) {
        this._minScale.next(x);
    }

    public get maxLines() {
        return this._maxLines.asObservable();
    }

    public setMaxLines(x) {
        this._maxLines.next(x);
    }

    public get maxSeps() {
        return this._maxSeps.asObservable();
    }

    public setMaxSeps(x) {
        this._maxSeps.next(x);
    }

    setImage(file: File) {
        this.fileSubject.next(file);
    }

    setxyinfo(data) {
        this.coordinatesSubject.next(data);
    }

    setThreshHold(x: number) {
        this._fileThreshHold.next(x);
    }
}
