import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';

@Injectable()
export class PlayerService {
  // players:any[]=[
  //   {playerId:10101,playerName:'MS Dhoni',playerAge:40,status:'inactive'},
  //   {playerId:21101,playerName:'virat kohli',playerAge:38,status:'active'},
  //   {playerId:21111,playerName:'Rohit Sharma',playerAge:38,status:'active'}
  //   ]

  constructor(private http:HttpClient) { }
  getAllPlayer(){
    return this.http.get<any[]>(' http://localhost:3000/players');
  }
  addPlayer(player:any){
    return this.http.post(' http://localhost:3000/players',player);
    // this.players.push(player);
  }
}
