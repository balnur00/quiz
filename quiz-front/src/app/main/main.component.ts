import { Component, OnInit } from '@angular/core';
import {ProviderService} from '../shared/services/provider.service';
import {IPost} from '../shared/model';

@Component({
  selector: 'app-main',
  templateUrl: './main.component.html',
  styleUrls: ['./main.component.css']
})
export class MainComponent implements OnInit {

  constructor(private provider: ProviderService ) {}
  public logged = false;
  public username: any;
  public password: any;
  public post: IPost[] = [];
  public title: any;

  ngOnInit() {
    if (this.logged) {
      this.provider.getPosts().then(res => {
        this.post = res;
      });
    }
  }
  showBody(post: IPost) {
    // {{post.body}}
  }
  getPostFromList(post: IPost) {
    this.provider.getPosts().then(res => {
      this.post = res;
    });
  }
  updatePost(post: IPost) {
    this.provider.updatePost(post).then(res => {
      console.log('updated');
    });
  }
  deletePost(post: IPost) {
    this.provider.deletePost(post).then(res => {
      console.log('deleted');
    });
  }
  createPost(post: IPost) {
    if (this.title !== '') {
      this.provider.createPost(this.title).then(res => {
        this.title = '';
        this.post.push(res);
      });
    }
  }
  auth() {
    if (this.username !== '' && this.password !== '') {
      this.provider.auth(this.username, this.password).then( res => {
        localStorage.setItem('token', res.token);
        this.logged = true;

        this.provider.getPosts().then(r => {
          this.post = r;
        });
        console.log('OK');
      });
    }
  }
  logout() {
    this.provider.logout().then( res => {
      localStorage.clear();
      this.logged = false;
    });
  }
}
