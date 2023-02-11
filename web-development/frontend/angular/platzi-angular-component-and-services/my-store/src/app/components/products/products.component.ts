import { Component, Input } from '@angular/core';
import { IProduct } from 'src/app/models/product.model';
import { StoreService } from 'src/app/services/store.service';

@Component({
  selector: 'app-products',
  templateUrl: './products.component.html',
  styleUrls: ['./products.component.scss']
})
export class ProductsComponent {
  @Input() products: IProduct[] = [{
    id: "",
    title: "",
    price: 0,
    image: "",
    description: "",
    category: ""
  },
]
  today = new Date();
  date = new Date(2020, 2, 16);
  totalShoppingCart: number = 0;
  shoppingCart: IProduct[] = [];

  constructor(
    private storeService: StoreService
  ){
    this.shoppingCart = this.storeService.getShoppingCart();
  };

  onAddedToCart(product: IProduct): void {
    this.storeService.addProduct(product);
    this.totalShoppingCart = this.storeService.getTotal();
  }
}
