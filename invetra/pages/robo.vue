<template>
    <div class="bg-lightblue bg-repeat font-oswald">
        <Navbar/>
        <Robo/>
        <Footer/>
    </div>
</template>

<script>
import Robo from '@/components/Robo.vue'
import Navbar from '@/components/Navbar.vue'
import Footer from '@/components/Footer.vue'
export default {
    components:{Robo, Navbar, Footer}
}
</script>