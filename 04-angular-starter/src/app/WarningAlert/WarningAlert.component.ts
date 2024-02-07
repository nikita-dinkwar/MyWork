import { Component } from "@angular/core";

@Component({
    selector:'app-WarningAlert',
    template:'<p class="font">Warning Alert Works!</p>',
    styles:[`
        .font {
            color: red;
            padding: 10px;
            margin:10px;
            border:10px;
        
    
    }
    `]
})
export class WarningAlertComponent{

}