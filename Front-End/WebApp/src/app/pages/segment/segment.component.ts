import { Component, OnInit } from '@angular/core';
import { BehaviorSubject } from 'rxjs';
import { FileSharingService } from 'src/app/common/services/file.sharing.service';

@Component({
    selector: 'app-segment',
    templateUrl: './segment.component.html',
    styleUrls: ['./segment.component.css']
})
export class SegmentComponent implements OnInit {

    private thresholdValue = 0.2;

    constructor(private fileSharingService: FileSharingService) {
    }

    ngOnInit() {
    }

    public sliderChange(e) {
        console.log(e);
    }

    pitch(event: any) {
        this.fileSharingService.setThreshHold(event.value);
        this.thresholdValue = event.value;
    }
}
