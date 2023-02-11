import { Component, OnInit } from '@angular/core';
import { StoreService } from 'src/app/services/store.service';

@Component({
  selector: 'app-nav',
  templateUrl: './nav.component.html',
  styleUrls: ['./nav.component.scss']
})
export class NavComponent {
  constructor(
    private storeService: StoreService
  ){};

  showMenu: boolean = false;
  counter: number = 0;

  ngOnInit(){
    this.storeService.productsInCart$.subscribe(
      products => this.counter = products.length
    )};

  toggleMenu(): void {
    this.showMenu = !this.showMenu;
  }
}
