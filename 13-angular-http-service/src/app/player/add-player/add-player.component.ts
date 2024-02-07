import { Component } from '@angular/core';
import { PlayerService } from '../player.service';

@Component({
  selector: 'app-add-player',
  templateUrl: './add-player.component.html',
  styleUrl: './add-player.component.css',
  providers:[]
})
export class AddPlayerComponent {
  player:any={}
  id=''
  name=''
  age=''

constructor(private service:PlayerService){}
 
addPlayerHandler(){
  this.player.id = this.id
  // this.player.Id=this.Id;
  this.player.playerId=this.id;
  this.player.playerName=this.name;
  this.player.playerAge=this.age
  this.service.addPlayer(this.player).subscribe(() =>{
    alert('player added successfully');
  });
this.id=''
this.name=''
this.age=''
}


}
