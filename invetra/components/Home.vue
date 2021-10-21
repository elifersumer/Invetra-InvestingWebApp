<template>
  <div>
      <Navbar/>
      <Hero/>
      
      <Video/>
  </div>
</template>

<script>
import Navbar from "@/components/Navbar.vue"
import Hero from "@/components/Hero.vue"
import Video from "@/components/Video.vue"
export default {
  components:{
    Navbar,
    Hero,
    Video
  }
}
</script>
