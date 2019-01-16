import { Component, OnInit } from '@angular/core';
import { sanitizeStyle } from '@angular/core/src/sanitization/sanitization';
declare function setStyle():any;
@Component({
  selector: 'app-contact',
  templateUrl: './contact.component.html',
  styleUrls: ['./contact.component.css']
})
export class ContactComponent implements OnInit {

  constructor() { }

  ngOnInit() {
    setStyle();
  }

}
