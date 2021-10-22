<template>
  <div>
    <Navbar/>
    <div class="flex flex-row">
      <Hero/>
      <Widget/>
    </div>
      <Video/>
  </div>
</template>

<script>
import Navbar from "@/components/Navbar.vue"
import Hero from "@/components/Hero.vue"
import Video from "@/components/Video.vue"
import Widget from '@/components/Widget.vue'
export default {
  components:{
    Navbar,
    Hero,
    Video,
    Widget
  }
}
</script>
