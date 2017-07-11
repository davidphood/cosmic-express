# cosmic-express

Cosmic Express Solver - Python Version

Initial thoughts on cost function:
* distance from exit - tier 1 - [1..width*height)
+ distance from each box - tier 2 - width*height * [1..width*height)
+ distance from each creature - tier 3 - width*height^2 * [1..width*height)

Use manhattan distance for working out distance between each object.

This doesn't really work very well once you've picked up a creature and you want to put them in a box but you have another creature waiting. Distance from box and creature might need to swap priority depending on whether the train is carrying something or not.
