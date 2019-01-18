import { Component, OnInit } from '@angular/core';
import { FileSharingService } from 'src/app/common/services/file.sharing.service';

@Component({
    selector: 'app-segment',
    templateUrl: './segment.component.html',
    styleUrls: ['./segment.component.css']
})
export class SegmentComponent implements OnInit {

    public jsonContent = "{\"employee\":{ \"name\":\"John\", \"age\":30, \"city\":\"New York\" }}";

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
        this.maxcolseps = event.value;
        this.fileSharingService.setMaxColSeps(this.maxcolseps);
    }

    updateScale(event: any) {
        this.minscale = event.value;
        this.fileSharingService.setMinScale(this.minscale);
    }

    updateLines(event: any) {
        this.maxlines = event.value;
        this.fileSharingService.setMaxLines(this.maxlines);
    }

    updateSeps(event: any) {
        this.maxseps = event.value;
        this.fileSharingService.setMaxSeps(this.maxseps);
    }
}
