import type {paths} from "./types.ts";
import {client} from "./apiClient.ts";


type MakersResponse = paths['/makers']['get']['responses']['200']['content']['application/json'];

export const fetchMakers = async (): Promise<MakersResponse | undefined> => {
    const {data, error} = await client.GET('/makers')

    if (error) {
        console.error('API Error:', error)
        return
    }
    return data
}

type MakerDetailResponse= paths['/makers/{maker_id}']['get']['responses']['200']['content']['application/json']

export const fetchMakerDetail = async (makerID: number) :Promise<MakerDetailResponse | undefined> => {
    const { data, error } = await client.GET('/makers/{maker_id}', {
        params: { path: {maker_id: makerID }}
    })
    if ( error ){
        console.error('API Error:', error)
        return
    }
    return data
}

type MakerCreateRequest = paths['/makers']['post']['requestBody']['content']['application/json'];
type MakerCreateResponse = paths['/makers']['post']['responses']['201']['content']['application/json'];


export const createMaker = async (maker: MakerCreateRequest): Promise<MakerCreateResponse | undefined> => {
    const {data, error} = await client.POST('/makers', {
        body: maker,
    })

    if (error) {
        console.error('API Error', error)
        return
    }

    return data

}


type MakerUpdateRequest = paths['/makers/{maker_id}']['put']['requestBody']['content']['application/json'];
type MakerUpdateResponse = paths['/makers/{maker_id}']['put']['responses']['200']['content']['application/json'];


export const updateMaker = async (
    makerID: number,
    maker: MakerUpdateRequest): Promise<MakerUpdateResponse | undefined> => {
    const {data, error} = await client.PUT('/makers/{maker_id}', {
        params: {path: {maker_id: makerID}},
        body: maker,
    })
    if (error) {
        console.error('API Error', error)
        return
    }
    return data

}


export const deleteMaker = async (makerID: number) :Promise<void> => {
    const { error } = await client.DELETE('/makers/{maker_id}', {
        params: { path: {maker_id: makerID }}
    })
    if ( error ){
        console.error('API Error:', error)
        return
    }
    return
}