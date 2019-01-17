import { Component, OnInit } from '@angular/core';
import { FileSharingService } from 'src/app/common/services/file.sharing.service';

@Component({
    selector: 'app-segment',
    templateUrl: './segment.component.html',
    styleUrls: ['./segment.component.css']
})
export class SegmentComponent implements OnInit {

    private thresholdValue = 0.2;
    public maxcolseps = 100;
    public minscale = 0;
    public maxlines = 1000;
    public maxseps = 100;

    constructor(private fileSharingService: FileSharingService) {
    }

    ngOnInit() {
    }

    pitch(event: any) {
        this.fileSharingService.setThreshHold(event.value);
        this.thresholdValue = event.value;
    }

    updateColSeps(event: any) {
        this.maxcolseps = event.target.value;
        this.fileSharingService.setMaxColSeps(this.maxcolseps);
    }

    updateScale(event: any) {
        this.minscale = event.target.value;
        this.fileSharingService.setMinScale(this.minscale);
    }

    updateLines(event: any) {
        this.maxlines = event.target.value;
        this.fileSharingService.setMaxLines(this.maxlines);
    }

    updateSeps(event: any) {
        this.maxseps = event.target.value;
        this.fileSharingService.setMaxSeps(this.maxseps);
    }
}
