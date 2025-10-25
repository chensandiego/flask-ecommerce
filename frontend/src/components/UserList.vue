<template>
  <div>
    <h2>User List</h2>
    <ul>
      <li v-for="user in userStore.users" :key="user.id">
        {{ user.name }}
      </li>
    </ul>

    <input v-model="newUser" placeholder="Enter name" />
    <button @click="addNewUser">Add User</button>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import { useUserStore } from '../stores/user'

const userStore = useUserStore()
const newUser = ref('')

onMounted(() => {
  userStore.fetchUsers()
})

async function addNewUser() {
  if (!newUser.value.trim()) return
  await userStore.addUser({ name: newUser.value })
  newUser.value = ''
}
</script>
