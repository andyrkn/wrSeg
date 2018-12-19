import { Component, OnInit } from '@angular/core';
import { FileSharingService } from 'src/app/common/services/file.sharing.service';

@Component({
    selector: 'app-file-resolved',
    templateUrl: './file-resolved.component.html',
    styleUrls: ['./file-resolved.component.css']
})
export class FileResolvedComponent implements OnInit {

    public coordinates: any = {};

    constructor(private fileSharingService: FileSharingService) {

    }

    ngOnInit() {
        this.fileSharingService.coordinates.subscribe((data) => this.coordinates = data);
        this.fileSharingService.file.subscribe((data) => this.updatebg(data));
    }

    updatebg(file) {
        const coords: any = this.coordinates;
        const canvas: any = document.getElementById('canvas');
        const ctx = canvas.getContext('2d');

        const newimg = new Image();

        const reader = new FileReader();
        reader.onload = ((elem) => {
            return (e) => {
                newimg.src = e.target.result;
            };
        })(canvas);
        reader.readAsDataURL(file);

        newimg.onload = function () {
            ctx.fillStyle = 'white';
            ctx.fillRect(0, 0, canvas.width, canvas.height);

            canvas.width = newimg.width;
            canvas.height = newimg.height;
            ctx.drawImage(newimg, 0, 0, newimg.width, newimg.height, 0, 0, canvas.width, canvas.height);

            // console.log(coords);
            ctx.fillStyle = 'rgba(66, 244, 241, 0.3)';
            for (const area of coords.Content) {
                ctx.fillRect(area[0], area[1], area[2] - area[0], area[3] - area[1]);
            }

            ctx.fillStyle = 'rgba(212, 0, 255, 0.3)';
            for (const area of coords.Footer) {
                ctx.fillRect(area[0], area[1], area[2] - area[0], area[3] - area[1]);
            }

            ctx.fillStyle = 'rgba(0, 255, 106, 0.3)';
            for (const area of coords.Title) {
                ctx.fillRect(area[0], area[1], area[2] - area[0], area[3] - area[1]);
            }

            ctx.fillStyle = 'rgba(0, 255, 233, 0.3)';
            for (const area of coords.PageNumber) {
                ctx.fillRect(area[0], area[1], area[2] - area[0], area[3] - area[1]);
            }

            ctx.fillStyle = 'rgba(0, 255, 233, 0.3)';
            for (const area of coords.Adnotation) {
                ctx.fillRect(area[0], area[1], area[2] - area[0], area[3] - area[1]);
            }
        };

    }
}
