import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';
import { HttpClientModule } from '@angular/common/http';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';

import { FileUploadComponent } from './file-upload/file-upload.component';
import { FileResolvedComponent } from './file-resolved/file-resolved.component';
import { FileMenuComponent } from './file-menu/file-menu.component';
import { HomeComponent } from './home/home.component';
import { NotFoundComponent } from './shared/not-found/not-found.component';

@NgModule({
   declarations: [
      AppComponent,
      FileUploadComponent,
      FileResolvedComponent,
      FileMenuComponent,
      HomeComponent,
      NotFoundComponent
   ],
   imports: [
      BrowserModule,
      HttpClientModule,
      AppRoutingModule
   ],
   providers: [],
   bootstrap: [
      AppComponent
   ]
})
export class AppModule { }
