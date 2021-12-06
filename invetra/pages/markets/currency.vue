<template>
    <div class="h-full bg-lightblue bg-repeat font-oswald">
        <Navbar/>
        <Currencies/>
        <Footer/>
    </div>
</template>

<script>
import Currencies from "@/components/Currencies.vue"
import Navbar from '@/components/Navbar.vue'
import Footer from '@/components/Footer.vue'
    export default {
        components:{
            Currencies,
            Navbar,
            Footer
        }
    }
</script>

<style scoped>

</style>