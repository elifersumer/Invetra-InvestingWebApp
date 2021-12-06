<template>
    <div class="h-full bg-lightblue bg-repeat font-oswald">
        <Navbar/>
        <Criptos/>
        <Footer/>
    </div>
</template>

<script>
import Criptos from "@/components/Criptos.vue"
import Navbar from '@/components/Navbar.vue'
import Footer from '@/components/Footer.vue'
    export default {
        components:{
            Navbar,
            Criptos,
            Footer
        }
    }
</script>

<style scoped>

</style>