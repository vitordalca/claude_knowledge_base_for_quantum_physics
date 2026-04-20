---
type: "source"
title: "What's so special about Euler's number e? | Chapter 5, Essence of calculus"
source_type: "clipping"
url: "https://www.youtube.com/watch?v=m2MIpDrF7Es&list=PLZHQObOWTQDMsr9K-rj53DwVRMYO3t5Yr&index=5"
authors: "[[3Blue1Brown]]"
published: 2017-05-02
ingested: "2026-04-17T17:50:17-03:00"
description: "What is e?  And why are exponentials proportional to their own derivatives?Help fund future projects: https://www.patreon.com/3blue1brownAn equally valuable form of support is to simply share some o"
tags:
  - "clippings"
---
![](https://www.youtube.com/watch?v=m2MIpDrF7Es)

What is e? And why are exponentials proportional to their own derivatives?  
Help fund future projects: https://www.patreon.com/3blue1brown  
An equally valuable form of support is to simply share some of the videos.  
Special thanks to these supporters: http://3b1b.co/lessons/eulers-number#thanks  
Home page: https://www.3blue1brown.com  
  
Timestamps  
0:00 - Motivating example  
3:57 - Deriving the key proportionality property  
7:36 - What is e?  
8:48 - Natural logs  
11:23 - Writing e^ct is a choice  
  
  
Corrections:  
9:40 - I meant to say "\*the derivative of\* e to the power of some constant..."  
12:30 - What's written as "(1 + r)" should really just be r, by any usual convention for how to write an interest rate.  
  
  
  
  
Thanks to these viewers for their contributions to translations  
Hebrew: Omer Tuchfeld  
Italian: ang  
Vietnamese: @ngvutuan2811  
  
\------------------  
  
3blue1brown is a channel about animating math, in all senses of the word animate. And you know the drill with YouTube, if you want to stay posted about new videos, subscribe, and click the bell to receive notifications (if you're into that).  
  
If you are new to this channel and want to see more, a good place to start is this playlist: http://3b1b.co/recommended  
  
Various social media stuffs:  
Website: https://www.3blue1brown.com  
Twitter: https://twitter.com/3Blue1Brown  
Patreon: https://patreon.com/3blue1brown  
Facebook: https://www.facebook.com/3blue1brown  
Reddit: https://www.reddit.com/r/3Blue1Brown

## Transcript

### Motivating example

**0:14** · I've introduced a few derivative formulas, but a really important one that I left out was exponentials.

**0:20** · So here I want to talk about the derivatives of functions like 2 to the x, 7 to the x, and also to show why e to the x is arguably the most important of the exponentials.

**0:32** · First of all, to get an intuition, let's just focus on the function 2 to the x.

**0:36** · Let's think of that input as a time, t, maybe in days, and the output, 2 to the t, as a population size, perhaps of a particularly fertile band of pie creatures which doubles every single day.

**0:50** · And actually, instead of population size, which grows in discrete little jumps with each new baby pie creature, maybe let's think of 2 to the t as the total mass of the population.

**1:02** · I think that better reflects the continuity of this function, don't you?

**1:06** · So for example, at time t equals 0, the total mass is 2 to the 0 equals 1, for the mass of one creature.

**1:14** · At t equals 1 day, the population has grown to 2 to the 1 equals 2 creature masses.

**1:21** · At day t equals 2, it's t squared, or 4, and in general it just keeps doubling every day.

**1:28** · For the derivative, we want dm dt, the rate at which this population mass is growing, thought of as a tiny change in the mass, divided by a tiny change in time.

**1:39** · Let's start by thinking of the rate of change over a full day, say between day 3 and day 4.

**1:46** · In this case, it grows from 8 to 16, so that's 8 new creature masses added over the course of one day.

**1:55** · And notice, that rate of growth equals the population size at the start of the day.

**2:01** · Between day 4 and day 5, it grows from 16 to 32, so that's a rate of 16 new creature masses per day, which again equals the population size at the start of the day.

**2:13** · And in general, this rate of growth over a full day equals the population size at the start of that day.

**2:21** · So it might be tempting to say that this means the derivative of 2 to the t equals itself, that the rate of change of this function at a given time t is equal to the value of that function.

**2:34** · And this is definitely in the right direction, but it's not quite correct.

**2:39** · What we're doing here is making comparisons over a full day, considering the difference between 2 to the t plus 1 and 2 to the t.

**2:48** · But for the derivative, we need to ask what happens for smaller and smaller changes.

**2:53** · What's the growth over the course of a tenth of a day, a hundredth of a day, one one billionth of a day?

**2:59** · This is why I had us think of the function as representing population mass, since it makes sense to ask about a tiny change in mass over a tiny fraction of a day, but it doesn't make as much sense to ask about the tiny change in a discrete population size per second.

**3:15** · More abstractly, for a tiny change in time, dt, we want to understand the difference between 2 to the t plus dt and 2 to the t, all divided by dt.

**3:27** · The change in the function per unit time, but now we're looking very narrowly around a given point in time, rather than over the course of a full day.

**3:39** · And here's the thing, I would love if there was some very clear geometric picture that made everything that's about to follow just pop out, some diagram where you could point to one value and say, see, that part, that is the derivative of 2 to the t.

**3:54** · And if you know of one, please let me know.

### Deriving the key proportionality property

**3:57** · And while the goal here, as with the rest of the series, is to maintain a playful spirit of discovery, the type of play that follows will have more to do with finding numerical patterns rather than visual ones.

**4:08** · So start by just taking a very close look at this term, 2 to the t plus dt.

**4:14** · A core property of exponentials is that you can break this up as 2 to the t times 2 to the dt.

**4:21** · That really is the most important property of exponents.

**4:24** · If you add two values in that exponent, you can break up the output as a product of some kind.

**4:30** · This is what lets you relate additive ideas, things like tiny steps in time, to multiplicative ideas, things like rates and ratios.

**4:38** · I mean, just look at what happens here.

**4:40** · After that move, we can factor out the term 2 to the t, which is now just multiplied by 2 to the dt minus 1, all divided by dt.

**4:50** · And remember, the derivative of 2 to the t is whatever this whole expression approaches as dt approaches 0.

**4:58** · And at first glance, that might seem like an unimportant manipulation.

**5:02** · But a tremendously important fact is that this term on the right, where all of the dt stuff lives, is completely separate from the t term itself.

**5:11** · It doesn't depend on the actual time where we started.

**5:14** · You can go off to a calculator and plug in very small values for dt here, for example, maybe typing in 2 to the 0.001 minus 1 divided by 0.001.

**5:27** · What you'll find is that for smaller and smaller choices of dt, this value approaches a very specific number, around 0.6931.

**5:38** · Don't worry if that number seems mysterious, the central point is that this is some kind of constant.

**5:44** · Unlike derivatives of other functions, all of the stuff that depends on dt is separate from the value of t itself.

**5:52** · So the derivative of 2 to the t is just itself, but multiplied by some constant.

**5:59** · And that should make sense, because earlier it felt like the derivative for 2 to the t should be itself, at least when we were looking at changes over the course of a full day.

**6:09** · And evidently, the rate of change for this function over much smaller timescales is not quite equal to itself, but it's proportional to itself, with this very peculiar proportionality constant of 0.6931.

**6:29** · And there's not too much special about the number 2 here.

**6:32** · If instead we had dealt with the function 3 to the t, the exponential property would also have led us to the conclusion that the derivative of 3 to the t is proportional to itself, but this time it would have had a proportionality constant of 1.0986.

**6:49** · And for other bases to your exponent, you can have fun trying to see what the various proportionality constants are, maybe seeing if you can find a pattern in them.

**6:58** · For example, if you plug in 8 to the power of a very tiny number, minus 1, and divide by that same tiny number, you'd find that the relevant proportionality constant is around 2.079.

**7:12** · And maybe, just maybe, you would notice that this number happens to be exactly 3 times the constant associated with the base for 2.

**7:22** · So these numbers certainly aren't random, there is some kind of pattern, but what is it?

**7:28** · What does 2 have to do with the number 0.6931, and what does 8 have to do with the number 2.079?

### What is e?

**7:36** · Well, a second question that is ultimately going to explain these mystery constants is whether there's some base where that proportionality constant is 1, where the derivative of a to the power t is not just proportional to itself, but actually equal to itself.

**7:53** · And there is!

**7:55** · It's the special constant e around 2.71828.

**8:00** · In fact, it's not just that the number e happens to show up here, this is in a sense what defines the number e.

**8:08** · If you ask why does e of all numbers have this property, it's a little like asking why does pi of all numbers happen to be the ratio of the circumference of a circle to its diameter.

**8:18** · This is at its heart what defines this value.

**8:22** · All exponential functions are proportional to their own derivative, but e alone is the special number so that proportionality constant is 1, meaning e to the t actually equals its own derivative.

**8:35** · One way to think of that is that if you look at the graph of e to the t, it has the peculiar property that the slope of a tangent line to any point on this graph equals the height of that point above the horizontal axis.

### Natural logs

**8:48** · The existence of a function like this answers the question of the mystery constants, and it's because it gives a different way to think about functions that are proportional to their own derivative.

**8:59** · The key is to use the chain rule.

**9:01** · For example, what is the derivative of e to the 3t?

**9:06** · Well, you take the derivative of the outermost function, which due to this special nature of e is just itself, and multiply by the derivative of that inner function 3t, which is the constant 3.

**9:19** · Or rather than just applying a rule blindly, you could take this moment to practice the intuition for the chain rule that I talked through last video, thinking about how a slight nudge to t changes the value of 3t, and how that intermediate change nudges the final value of e to the 3t.

**9:38** · Either way, the point is e to the power of some constant times t is equal to that same constant times itself.

**9:47** · And from here, the question of those mystery constants really just comes down to a certain algebraic manipulation.

**9:56** · The number 2 can also be written as e to the natural log of 2.

**10:01** · There's nothing fancy here, this is just the definition of the natural log, it asks the question e to the what equals 2.

**10:10** · So the function 2 to the t is the same as the function e to the power of the natural log of 2 times t.

**10:20** · And from what we just saw, combining the fact that e to the t is its own derivative with the chain rule, the derivative of this function is proportional to itself, with a proportionality constant equal to the natural log of 2.

**10:34** · And indeed, if you go plug in the natural log of 2 to a calculator, you'll find that it's 0.6931, the mystery constant we ran into earlier.

**10:43** · And the same goes for all the other bases.

**10:46** · The mystery proportionality constant that pops up when taking derivatives is just the natural log of the base. The answer to the question e to the what equals that base.

**10:53** · In fact, throughout applications of calculus, you rarely see exponentials written as some base to a power t.

**11:08** · Instead, you almost always write the exponential as e to the power of some constant times t.

**11:14** · It's all equivalent, I mean any function like 2 to the t or 3 to the t can also be written as e to some constant times t.

### Writing e^ct is a choice

**11:24** · At the risk of staying overfocused on the symbols here, I want to emphasize that there are many ways to write down any particular exponential function.

**11:34** · And when you see something written as e to some constant times t, that's a choice we make to write it that way, and the number e is not fundamental to that function itself.

**11:45** · What is special about writing exponentials in terms of e like this is that it gives that constant in the exponent a nice readable meaning.

**11:54** · Here, let me show you what I mean.

**11:56** · All sorts of natural phenomena involve some rate of change that's proportional to the thing that's changing.

**12:03** · For example, the rate of growth of a population actually does tend to be proportional to the size of the population itself, assuming there isn't some limited resource slowing things down.

**12:14** · And if you put a cup of hot water in a cool room, the rate at which the water cools is proportional to the difference in temperature between the room and the water, or said a little differently, the rate at which that difference changes is proportional to itself.

**12:31** · If you invest your money, the rate at which it grows is proportional to the amount of money there at any time.

**12:39** · In all of these cases, where some variable's rate of change is proportional to itself, the function describing that variable over time is going to look like some kind of exponential.

**12:51** · And even though there are lots of ways to write any exponential function, it's very natural to choose to express these functions as e to the power of some constant times t, since that constant carries a very natural meaning.

**13:04** · It's the same as the proportionality constant between the size of the changing variable and the rate of change.

**13:14** · And as always, I want to thank those who have made this series possible.

**13:34** · Thank you.