import { Component, OnInit } from '@angular/core';
import { PlayerService } from '../player.service';

@Component({
  selector: 'app-list-player',
  templateUrl: './list-player.component.html',
  styleUrl: './list-player.component.css'
})
export class ListPlayerComponent implements OnInit{
  players:any[]=[];
       service:PlayerService;
       constructor(service:PlayerService){
        this.service=service;
       }
       ngOnInit(): void {
         this.service.getAllPlayer().subscribe((data) => {
          this.players=data;
         });
         
       }
      }

