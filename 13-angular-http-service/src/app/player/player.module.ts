import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { AddPlayerComponent } from './add-player/add-player.component';
import { ListPlayerComponent } from './list-player/list-player.component';
import { PlayerService } from './player.service';
import { FormsModule } from '@angular/forms';
import { HttpClientModule } from '@angular/common/http';



@NgModule({
  declarations: [
    AddPlayerComponent,
    ListPlayerComponent,
    
  ],
  imports: [
    CommonModule,
    FormsModule,
    HttpClientModule
  ],
  exports:[AddPlayerComponent,ListPlayerComponent],
  providers:[PlayerService]
})
export class PlayerModule { }
