<template>
    <div>
        <Navbar/>
        <BbAAPL/>
        <Footer/>
    </div>
</template>

<script>
import Navbar from "@/components/Navbar.vue"
import Footer from "@/components/Footer.vue"
import axios from "axios"
import BbAAPL from "@/components/BbAAPL.vue"
export default {
    components:{BbAAPL, Navbar, Footer},
    
}
</script>

<style>

</style>