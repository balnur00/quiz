export interface IPost {
  id: number;
  title: string;
  body: any;
  like_count: number;
  created_at: Date;
}

export interface IAuthResponse {
  token: string;
}
