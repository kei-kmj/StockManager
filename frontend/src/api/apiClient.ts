import createClient from 'openapi-fetch';
import type {paths} from './types.ts'


export const client = createClient<paths>({
    baseUrl: 'http://localhost:8000'
})



