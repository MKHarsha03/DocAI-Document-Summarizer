<template>
  <heading/>
  <promptpad/>
</template>
<script></script>
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
    position:fixed;
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
    overflow-y: scroll;
  }
</style>
