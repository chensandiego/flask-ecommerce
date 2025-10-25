<template>
  <div class="p-4">
    <h2>User List</h2>
    <ul>
      <li v-for="user in users" :key="user.id">{{ user.name }}</li>
    </ul>

    <input v-model="newName" placeholder="Enter new user name" />
    <button @click="addNewUser">Add User</button>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import { useUserStore } from './store'

const store = useUserStore()
const newName = ref('')

onMounted(() => {
  store.fetchUsers()
})

const addNewUser = async () => {
  if (newName.value.trim()) {
    await store.addUser({ name: newName.value })
    newName.value = ''
  }
}

const users = store.$state.users
</script>
