import axios from 'axios'
import camelcaseKeys from "camelcase-keys";

let token = 'Token 88d4e8aa182cede616f69313e07f8573f7ad1d88';
let api = axios.create({
    baseURL: 'http://localhost:8000/api/',
    headers: {
        common: {
            'Authorization': token
        }
    },
    transformResponse: [data => {
        if (data) {
            return (camelcaseKeys(JSON.parse(data), {deep: true}))
        }
    }]
});

export default api