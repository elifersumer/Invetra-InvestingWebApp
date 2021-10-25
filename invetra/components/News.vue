<template>
    <div>
        <New :newList="newList"/>
    </div>
</template>

<script>
import New from '@/components/New.vue'
import axios from 'axios'
    export default {
        components:{
            New
        },
        data(){
            return{
                newList: [],
            newListFirst6:[],
            key: "",
            url: "",
            description: "",
            image: "",
            name: "",
            source: ""
            }
            
        },
        mounted(){
            axios.get("https://api.collectapi.com/news/getNews?country=tr&tag=economy",{'headers':{
                    'Authorization':'apikey 75QONL8eURuIZP2plBWd0z:6mqlbUxZAJnsl5DQxXFqOq',
                    'Content-type':'application/json'
            }})
                .then(response=>{
                        response.data.result.forEach((res, idx) => {
                        this.newList.push({
                            id: idx,
                            url: res.url,
                            description: res.description,
                            image: res.image,
                            name: res.name,
                            source: res.source
                        });
                    });
                })
                .catch(e=>{
                     console.log(e)
                })

                console.log(this.newList)
        }
    }
</script>

<style scoped>

</style>