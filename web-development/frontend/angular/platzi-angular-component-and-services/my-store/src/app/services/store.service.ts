import { Injectable } from '@angular/core';
import { IProduct } from '../models/product.model';
import { BehaviorSubject } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class StoreService {

  private shoppingCart: IProduct[] = [];
  private productsInCart= new BehaviorSubject<IProduct[]>([]);

  productsInCart$ = this.productsInCart.asObservable();

  constructor() { }

  addProduct(product: IProduct): void{
    this.shoppingCart.push(product);
    this.productsInCart.next(this.shoppingCart);
  };

  getShoppingCart (){
    return this.shoppingCart;
  }

  getTotal(): number {
    return this.shoppingCart.reduce((sum, item) => sum + item.price, 0);
  }


}
