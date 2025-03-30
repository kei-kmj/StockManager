import type {paths} from "./types";
import {client} from "./apiClient";


type UsersResponse = paths['/users']['get']['responses']['200']['content']['application/json'];

export const fetchUsers = async (): Promise<UsersResponse | undefined> => {
    const {data, error} = await client.GET('/users')

    if (error) {
        console.error('API Error:', error)
        return
    }
    return data
}

export type UserDetailResponse= paths['/users/{user_id}']['get']['responses']['200']['content']['application/json']

export const fetchUserDetail = async (userID: number) :Promise<UserDetailResponse | undefined> => {
    const { data, error } = await client.GET('/users/{user_id}', {
        params: { path: {user_id: userID }}
    })
    if ( error ){
        console.error('API Error:', error)
        return
    }
    return data
}

export type UserCreateRequest = paths['/users']['post']['requestBody']['content']['application/json'];
export type UserCreateResponse = paths['/users']['post']['responses']['201']['content']['application/json'];


export const createUser = async (user: UserCreateRequest): Promise<UserCreateResponse | undefined> => {
    const {data, error} = await client.POST('/users', {
        body: user,
    })

    if (error) {
        console.error('API Error', error)
        return
    }

    return data

}


export type UserUpdateRequest = paths['/users/{user_id}']['put']['requestBody']['content']['application/json'];
type UserUpdateResponse = paths['/users/{user_id}']['put']['responses']['200']['content']['application/json'];


export const updateUser = async (
  userID: number,
  user: UserUpdateRequest): Promise<UserUpdateResponse | undefined> => {
    const {data, error} = await client.PUT('/users/{user_id}', {
        params: {path: {user_id: userID}},
        body: user,
    })
    if (error) {
        console.error('API Error', error)
        return
    }
    return data

}


export const deleteUser = async (userID: number) :Promise<void> => {
    const {error } = await client.DELETE('/users/{user_id}', {
        params: { path: {user_id: userID }}
    })
    if ( error ){
        console.error('API Error:', error)
        return
    }
    return
}