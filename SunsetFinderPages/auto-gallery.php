<!DOCTYPE html>

<html>
  <head>
    <title>Images Archive</title>
    <meta charset="UTF-8">
    <meta name="author" content="Sunset Finder Team">
    <meta name="description" content="Images Archive">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" href="SunsetStyles.css">
    <style>
    .gallery{
      display: grid;
      grid-template-columns: repeat(5, 1fr);
      grid-gap: 5px;
    }
    
    @media screen and (max-width:640px){
      .gallery{grid-template-columns: repeat(3, 1fr);}
    }

    .gallery img{
      width: 100%;
      height: 200px;
      object-fit: cover;
      
    }

    .gallery img.full{
      position: fixed;
      top: 0; left: 0; z-index: 999;
      width: 100vw; height: 100vh;
      background: black;
      object-fit: scale-down;

    }

    .gallery img {transition: all 0.3s; }

    </style>
    <script>
      window.onload = () => {
        //Get Images
        var all = document.querySelectorAll(".gallery img");

        //Fullscreen Toggle
        if (all.length > 0) {for (let img of all){
          img.onclick = () => {img.classList.toggle("full"); };
        }}
      }
    </script>
    <script></script>
    </head>

  <body>

    <div class="headWords">
      <h1> Image Archive</h1>
    </div>
   <?php

   $dir = "/Applications/XAMPP/xamppfiles/htdocs/testing/sunsetFinder/nonLabeled/";
   $images = glob("$dir*.{jpg,jpeg}", GLOB_BRACE);

   //Sort Images

   sort($images);//Ascending
   ?>

    <div class="gallery"><?php
    //Output Images
        foreach($images as $i){
        printf("<img src='/testing/sunsetFinder/nonLabeled/%s'>", rawurlencode (basename($i)));
        }
    ?></div>
  
  <!--Buttons-->
    
 
  <a href="index.html">
      <button class="chiveButton">Home</button>
    </a>

    <a href="aboutUs.html">
      <button class="boutusButton"> About Us</button>
    </a>

  </body>
</html>