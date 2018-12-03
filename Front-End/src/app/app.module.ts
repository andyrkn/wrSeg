import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';
import { HttpClientModule } from '@angular/common/http';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { FileDropModule } from 'ngx-file-drop';

import { FileUploadComponent } from './file-upload/file-upload.component';
import { FileResolvedComponent } from './file-resolved/file-resolved.component';
import { FileMenuComponent } from './file-menu/file-menu.component';
import { HomeComponent } from './pages/home/home.component';
import { HeaderComponent } from './pages/header/header.component';
import { ContactComponent } from './pages/contact/contact.component';
import { SegmentComponent } from './pages/segment/segment.component';

@NgModule({
   declarations: [
      AppComponent,
      FileUploadComponent,
      FileResolvedComponent,
      FileMenuComponent,
      HomeComponent,
      HeaderComponent,
      ContactComponent,
      SegmentComponent
   ],
   imports: [
      BrowserModule,
      HttpClientModule,
      AppRoutingModule,
      FileDropModule
   ],
   providers: [],
   bootstrap: [
      AppComponent
   ]
})
export class AppModule { }
