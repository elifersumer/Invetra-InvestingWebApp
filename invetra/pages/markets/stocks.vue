<template>
    <div class="h-full bg-lightblue bg-repeat font-oswald">
        <Navbar/>
        <Markets/>
        <Footer/>
    </div>
</template>

<script>
import Navbar from '@/components/Navbar.vue'
import Footer from '@/components/Footer.vue'
    export default {
        components:{
            Navbar,
            Footer
        }
    }
</script>

<style scoped>

</style>