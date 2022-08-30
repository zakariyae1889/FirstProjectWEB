var CountDownDate=new Date("December 31,2022 00:00:00").getTime();


let time=setInterval(()=>{
    let count=document.querySelector("#clock");
    let Datenow=new Date().getTime();
    let distance=CountDownDate - Datenow;
    let day=Math.floor(distance / (1000*60*60*24));
    let hour=Math.floor(distance % (1000*60*60*24) / (1000*60*60));
    let minutse=Math.floor(distance % (1000*60*60) / (1000*60));
    let seconds=Math.floor(distance % (1000*60) / (1000));

    count.innerHTML="Day:" +"  "+ day + "   " + "Hours:"+"  "+ hour + "   "  + "Minutse:"+"  "+minutse+"   " +"Seconds:"+"  "+seconds

     if(distance<0){
       clearInterval(time);
       count.innerHTML="you are arrived late";
     }
},1000);


// winner

















