import axios from 'axios';

// Create an instance of axios with default settings
const instance = axios.create({
    baseURL: 'http://localhost:8000/', // Your API base URL
    timeout: 1000, // Request timeout (optional)
    headers: {'Content-Type': 'application/json'}
});

export default instance;