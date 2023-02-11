import { Component, OnInit } from '@angular/core';
import { IProduct } from './models/product.model';
import { ProductsService } from 'src/app/services/products.service';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.scss']
})
export class AppComponent {

  products: IProduct[] = [];

  constructor (
    private productsService: ProductsService
  ){}

  ngOnInit(){
    this.productsService.getAllProducts()
    .subscribe(data => {
      this.products = data;
    });
  }


  /*
  imgParent: string = 'https://www.giantbomb.com/a/uploads/scale_small/9/93770/2419553-397060_386577108098888_427807760_n.jpg';
  showImg: boolean = true;
  onLoaded(img: string){
    console.log("I have just received the confirmation of the image loaded from the child component img.\n" + img)
  };

  toggleImg(): void{
    this.showImg = !this.showImg;
  }
  */
}
