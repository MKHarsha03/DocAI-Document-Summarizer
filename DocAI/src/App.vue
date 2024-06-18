<template>
  <heading/>
  <promptpad/>
</template>
<script>
  
</script>
<style>
  header{
    position:sticky;
    text-align:center;
    font-size:3vw;
  }
  .promptSection{
    display:block;
    padding:5px;
    width:100%;
    text-align:center;
    bottom:0;
    position:sticky;
  }
  textarea{
    resize: none;
    width:50%;
    height:1%;
    padding:5px;
    margin-right:5px;
    border-radius:5px;
  }
  .instructions{
    display:inline-block;
    width: 100%;
  }
  .instr_boxes{
    display:inline-block;
    border: 1px solid black;
    text-align:center;
    width:31%;
    margin:10px;
    padding:2px;
  }
  .chatscreen{
    overflow: auto;
  }
  .user_messages{
    border:2px solid green;
    border-radius:2px;
    padding:2px;
    width:100%;
    text-align:left;
    float:right;
    margin:15px;
    display:block;
  }
  .assistant_messages{
    border:2px solid blue;
    border-radius:2px;
    padding:2px;
    width:100%;
    text-align:left;
    float:right;
    margin:15px;
    display:block;
  }
</style>
