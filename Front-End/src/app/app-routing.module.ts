import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';
import { CommonModule } from '@angular/common';
import { HomeComponent } from './pages/home/home.component';
import { SegmentComponent } from './pages/segment/segment.component';
import { ContactComponent } from './pages/contact/contact.component';
const routes: Routes = [
  { path: 'home', component: HomeComponent },
  { path: 'segment', component: SegmentComponent },
  { path: 'contact', component: ContactComponent },
  { path: '', redirectTo: '/home', pathMatch: 'full' }
];

@NgModule({
  imports: [
    RouterModule.forRoot(routes),
    CommonModule
  ],
  exports: [
    RouterModule
  ],
  declarations: []
})

export class AppRoutingModule { }
