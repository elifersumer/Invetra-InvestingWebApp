<template>
    <div class="container font-oswald fixed inset-0 mb-16 z-50">
        <div class="h-16 bg-primary w-screen flex flex-col pr-4">
            <div class="flex flex-row justify-between mx-3 mt-1 -mb-2 h-6">
                <div class="flex flex-row">
                    <img src="@/assets/Invetra.png" class="w-icon h-icon -mt-1">
                    <a class="text-lg text-white font-bold" href=#>INVETRA</a>
                </div>
                <input class="bg-secondary h-6 px-5 pr-16 rounded-lg text-sm focus:outline-none placeholder-gray" 
                            type="search" name="search" placeholder="Search">
                <div class="flex flex-row justify-center">
                    <button class=" font-bold text-xs text-white bg-orange active:bg-darkorange w-btn h-btn rounded align-middle mr-1">
                        Sign Up
                    </button>
                    <button href=# class="text-xs text-white bg-darkblue w-btn h-btn rounded align-middle active:bg-black">Sign In</button>
                    <img src="@/assets/british.png" class="w-flag h-flag mt-1 ml-1" alt="EN">
                </div>
            </div>
            <div class="flex flex-row justify-between text-white">
                <div class="h-6 w-screen flex flex-row justify-center font-semibold mt-3">
                   <router-link class="p-1 text-md my-auto mr-16 hover:bg-white hover:text-darkblue rounded-t-sm" to="/">Home</router-link>
                    <router-link class="p-1 text-md my-auto mr-16 hover:bg-white hover:text-darkblue rounded-t-sm" to="/markets">Markets</router-link>
                    <a class="p-1 text-md my-auto mr-16 hover:bg-white hover:text-darkblue rounded-t-sm" href=#>Watchlist</a>
                    <a class="p-1 text-md my-auto mr-16 hover:bg-white hover:text-darkblue rounded-t-sm" href=#>News</a>
                    <a class="p-1 text-md my-auto mr-16 hover:bg-white hover:text-darkblue rounded-t-sm" href=#>Analysis</a>
                    <a class="p-1 text-md my-auto mr-16 hover:bg-white hover:text-darkblue rounded-t-sm" href=#>Charts</a>
                    <a class="p-1 text-md my-auto mr-16 hover:bg-white hover:text-darkblue rounded-t-sm" href=#>Tools</a>
                    <a class="p-1 text-md my-auto hover:bg-white hover:text-darkblue rounded-t-sm" href=#>Robo Advisor</a>
                </div>
                <a class="text-xs mr-4 mt-5 text-gray" href="">HelpSupport</a>
            </div>
            
        </div>
    </div>
</template>

<script>
    export default {
        
    }
</script>

<style scoped>

</style>