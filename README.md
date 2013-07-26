FreezeSplineWarp2 - Nuke Warper Trick Automation, aka "FreezeWarp"
===============


This Nuke script will freeze the shapes of a SplineWarp on a desired frame, by deleting keyframes or using an expression.   

The video below will explain how to use the technique:
<iframe width="480" height="270" src="http://www.youtube.com/embed/rFP4jgfXpjM" frameborder="0" allowfullscreen></iframe>


If you like it, use it frequently, or want to support further development please consider a small donation to the author.   
<a href='http://www.pledgie.com/campaigns/21123'><img alt='Click here to lend your support to: VFX tools coding project and make a donation at www.pledgie.com !' src='http://www.pledgie.com/campaigns/21123.png?skin_name=chrome' border='0' /></a>

### SUPPORTED FEATURES: ###

* Shape position/animation (baked)
* Shape Opacity Animation
* Shape Motion Blur
* Shape Overlay Color
* Shape Blending Modes
* Shape Inverted attribute
* Shape Open/Closed
* Delete repeated baked keyframes when possible


#### KNOW LIMITATIONS ####

Multithreading can crash Nuke on some cases, disable it if you experience crashes


#### USAGE ####

Select a SplineWarp3 node and fill the freeze frame pop-up with the desired "Freezeframe"
Limitations: if the animated shape is inside a transformed layer or matrix, you may need to bake the shape points positions with 
the http://github.com/magnoborgo/RotoPaintToSplineWarp2

#### Licensing ####

This script is made avalable under a BSD Style license that is included in the package.
