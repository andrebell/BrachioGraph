---
layout: article
title: BrachioGraph Plotter
mode: immersive
header:
  theme: dark
article_header:
  type: cover
  image:
    src: /projects/brachiograph/images/brachiograph_plotter.jpg
key: project_brachigraph
sidebar:
  nav: brachiograph
---

<style>
  .swiper-construction {
    height: 300px;
    width: 400px;
  }
  .swiper-construction .swiper__slide {
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 3rem;
    color: #fff;
  }
</style>

This is a small image tour of our building session for the brachiograph plotter...

<div class="swiper swiper-construction mx-auto">
  <div class="swiper__wrapper">
    <div class="swiper__slide"><img src="images/01.jpeg"></div>
    <div class="swiper__slide"><img src="images/02.jpeg"></div>
    <div class="swiper__slide"><img src="images/03.jpeg"></div>
    <div class="swiper__slide"><img src="images/04.jpeg"></div>
    <div class="swiper__slide"><img src="images/05.jpeg"></div>
    <div class="swiper__slide"><img src="images/06.jpeg"></div>
    <div class="swiper__slide"><img src="images/07.jpeg"></div>
  </div>
  <div class="swiper__button swiper__button--prev fas fa-chevron-left"></div>
  <div class="swiper__button swiper__button--next fas fa-chevron-right"></div>
</div>

The first job has started...

<div class="mx-auto"><img src="images/08.jpeg"></div>

...and succeded with a great result. 😄

<div class="mx-auto"><img src="images/09.jpeg"></div>

<script>
  {%- include scripts/lib/swiper.js -%}
  var SOURCES = window.TEXT_VARIABLES.sources;
  window.Lazyload.js(SOURCES.jquery, function() {
    $('.swiper-construction').swiper();
  });
</script>

