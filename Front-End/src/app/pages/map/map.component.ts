import { Component, OnInit } from '@angular/core';

@Component({
  selector: 'app-map',
  templateUrl: './map.component.html',
  styleUrls: ['./map.component.css']
})
export class MapComponent implements OnInit {
  lat: number = 47.173998;
  lng: number = 27.574912;
  constructor() { }

  ngOnInit() {
  }

}
