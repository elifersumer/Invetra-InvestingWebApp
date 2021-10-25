<template>
  <div class="h-myscreen bg-lightblue bg-repeat font-oswald">
    <Navbar/>
    <Home/>
    <Footer/>
  </div>
  
</template>

<script>
import Footer from '@/components/Footer.vue'
import Navbar from '@/components/Navbar.vue'

export default {
  components:{
    Navbar,Footer
  },
  
  
}
</script>
