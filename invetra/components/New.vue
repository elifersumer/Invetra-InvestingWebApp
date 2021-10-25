<template>
<div class="flex flex-col font-oswald h-full mx-auto relative">
    <p class="mt-20 text-lg font-bold text-darkblue m-auto underline cursor-default">DAILY ECONOMY NEWS</p>
    <div class="grid grid-cols-2 m-4 gap-x-4 font-bold">
        <div id="cripto" v-for="(item, idx) in newList" :key="idx">
            <div class="flex flex-row bg-white shadow rounded w-full mb-8 p-4">
                <img :src="item.image" class="w-auto h-40">
                <div class="flex flex-col justify-between">
                    <a class="ml-2 text-left text-md text-darkblue hover:underline hover:text-blue" 
                    :href="item.url">{{item.name}}</a>
                    <p class="mt-2 ml-2 text-left text-darkblue text-sm">{{item.description}}</p>
                    <p class="mt-4 ml-2 text-left text-gray-400 text-xxs"><u>Source:</u> {{item.source}}</p>
                    <a class="self-end text-xxs text-blue hover:underline" :href="item.url">For more...</a>
                </div>
            </div>
        </div>
    </div>
</div>

    
</template>

<script>
    export default {
        props:['newList']
    }
</script>

<style scoped>

</style>