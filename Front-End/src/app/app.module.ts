import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';
import { HttpClientModule } from '@angular/common/http';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { FileDropModule } from 'ngx-file-drop';

import { HomeComponent } from './pages/home/home.component';
import { HeaderComponent } from './pages/header/header.component';
import { ContactComponent } from './pages/contact/contact.component';
import { SegmentComponent } from './pages/segment/segment.component';

import { MapComponent } from './pages/map/map.component';
import { AgmCoreModule } from '@agm/core';

import { FileUploadComponent } from './pages/file-upload/file-upload.component';
import { FileResolvedComponent } from './pages/file-resolved/file-resolved.component';


@NgModule({
   declarations: [
      AppComponent,
      FileUploadComponent,
      FileResolvedComponent,
      HomeComponent,
      HeaderComponent,
      ContactComponent,
      SegmentComponent,
      MapComponent
   ],
   imports: [
      BrowserModule,
      HttpClientModule,
      AppRoutingModule,
      FileDropModule,
      AgmCoreModule.forRoot({
         apiKey: 'AIzaSyCRFb9Oetbz8bo3enqv7Dnxskop_cYyrNQ '
       })
   ],
   providers: [],
   bootstrap: [
      AppComponent
   ]
})
export class AppModule { }
