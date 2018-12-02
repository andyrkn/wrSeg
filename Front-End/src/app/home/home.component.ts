import { Component, OnInit } from '@angular/core';

@Component({
  selector: 'app-home',
  templateUrl: './home.component.html',
  styleUrls: ['./home.component.css']
})
export class HomeComponent implements OnInit {

  constructor() {
  }

  ngOnInit() {
    this.setPageBackground();
  }

  setPageBackground() {
    const canvas = <HTMLCanvasElement>document.getElementById('background-gradient');
    const ctx = canvas.getContext('2d');

    // Create a linear gradient
    // The start gradient point is at x=20, y=0
    // The end gradient point is at x=220, y=0
    const gradient = ctx.createLinearGradient(298.000, 0.000, 2.000, 300.000);

    // Add three color stops
    gradient.addColorStop(0.000, 'rgba(152, 255, 252, 1.000)');
    gradient.addColorStop(0.477, 'rgba(62, 196, 255, 1.000)');
    gradient.addColorStop(1.000, 'rgba(65, 109, 255, 1.000)');

    // Set the fill style and draw a rectangle
    ctx.fillStyle = gradient;
    ctx.fillRect(0, 0, 300.000, 300.000);
  }

}
