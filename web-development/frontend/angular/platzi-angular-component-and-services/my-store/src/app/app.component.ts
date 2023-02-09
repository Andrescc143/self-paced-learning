import { Component } from '@angular/core';
import { PRODUCTS } from './mocks/product.mock';
import { IProduct } from './models/product.model';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.scss']
})
export class AppComponent {
  imgParent: string = 'https://www.giantbomb.com/a/uploads/scale_small/9/93770/2419553-397060_386577108098888_427807760_n.jpg';

  products: IProduct[] = PRODUCTS;

  onLoaded(img: string){
    console.log("I have just received the confirmation of the image loaded from the child component img.\n" + img)
  }
}
