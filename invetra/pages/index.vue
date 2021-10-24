<template>
  <div class="h-myscreen font-oswald">
    <Navbar/>
    <router-view>
    </router-view>
  </div>
  
</template>

<script>
import Navbar from '@/components/Navbar.vue'

export default {
  components:{
    Navbar
  },
  
  
}
</script>
