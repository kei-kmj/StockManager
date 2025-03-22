import type {paths} from "./types.ts";
import {client} from "./apiClient.ts";


type ItemsResponse = paths['/items']['get']['responses']['200']['content']['application/json'];

export const fetchItems = async (): Promise<ItemsResponse | undefined> => {
    const {data, error} = await client.GET('/items')

    if (error) {
        console.error('API Error:', error)
        return
    }
    return data
}

type ItemDetailResponse= paths['/items/{item_id}']['get']['responses']['200']['content']['application/json']

export const fetchItemDetail = async (itemID: number) :Promise<ItemDetailResponse | undefined> => {
    const { data, error } = await client.GET('/items/{item_id}', {
        params: { path: {item_id: itemID }}
    })
    if ( error ){
        console.error('API Error:', error)
        return
    }
    return data
}

type ItemCreateRequest = paths['/items']['post']['requestBody']['content']['application/json'];
type ItemCreateResponse = paths['/items']['post']['responses']['201']['content']['application/json'];


export const createItem = async (item: ItemCreateRequest): Promise<ItemCreateResponse | undefined> => {
    const {data, error} = await client.POST('/items', {
        body: item,
    })

    if (error) {
        console.error('API Error', error)
        return
    }

    return data

}


type ItemUpdateRequest = paths['/items/{item_id}']['put']['requestBody']['content']['application/json'];
type ItemUpdateResponse = paths['/items/{item_id}']['put']['responses']['200']['content']['application/json'];


export const updateItem = async (
    itemID: number,
    item: ItemUpdateRequest): Promise<ItemUpdateResponse | undefined> => {
    const {data, error} = await client.PUT('/items/{item_id}', {
        params: {path: {item_id: itemID}},
        body: item,
    })
    if (error) {
        console.error('API Error', error)
        return
    }
    return data

}


export const deleteItem = async (itemID: number) :Promise<void> => {
    const {error } = await client.DELETE('/items/{item_id}', {
        params: { path: {item_id: itemID }}
    })
    if ( error ){
        console.error('API Error:', error)
        return
    }
    return
}