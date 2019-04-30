import { Injectable } from '@angular/core';
import {MainService} from './main.service';
import { IAuthResponse, IPost} from '../model';
import { HttpClient } from '@angular/common/http';

@Injectable({
  providedIn: 'root'
})
export class ProviderService extends MainService {

  constructor(http: HttpClient) {
    super(http);
  }

  getPosts(): Promise<IPost[]> {
    return this.get('http://localhost:8000/main/posts/', {});
  }

  createPost(title: any): Promise<IPost> {
    return this.post('http://localhost:8000/main/posts/', {
      title
    });
  }
  updatePost(tasklist: IPost): Promise<IPost> {
    return this.put(`http://localhost:8000/main/posts/${tasklist.id}/`, {
      title : tasklist.title
    });
  }
  deletePost(tasklist: IPost): Promise<IPost> {
    return this.delet(`http://localhost:8000/main/posts/${tasklist.id}/`, {});
  }
  auth(uname: any, pword: any): Promise<IAuthResponse> {
    return this.post('http://localhost:8000/main/login/', {
      username: uname,
      password: pword
    });
  }
  logout(): Promise<any> {
    return this.post(`http://localhost:8000/main/logout/`, {});
  }
}

