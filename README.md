project/
│
├── backend/
│   ├── app.py
│   ├── requirements.txt
│
└── frontend/
    ├── index.html
    ├── vite.config.js
    ├── package.json
    ├── src/
    │   ├── main.js
    │   ├── store.js
    │   ├── App.vue
    │   ├── components/
    │   │   └── UserList.vue


docker-compose up --build
Flask backend: http://localhost:5000/api/users

Vue frontend: http://localhost:5173