import { defineStore } from 'pinia'
import axios from 'axios'

export const useUserStore = defineStore('user', {
  state: () => ({
    users: [],
  }),
  actions: {
    async fetchUsers() {
      const res = await axios.get('/api/users')
      this.users = res.data
    },
    async addUser(newUser) {
      const res = await axios.post('/api/users', newUser)
      this.users.push(res.data)
    },
  },
})
