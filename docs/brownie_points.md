# Brownie Point Algorithm

Brownie Points is a Bradley-Terry model based algorithm which focuses on creating a human intuitive rating system.

## Math

The algorithm takes two inputs, which we'll call i and j.
Then, there are two factors we must calculate, one we'll call s, or our scale factor, and one which we'll call k, our k factor.

![image](https://latex.codecogs.com/png.image?\dpi{110}S&space;=&space;\frac{(i&space;&plus;&space;j)}{(200&space;-&space;\frac{200k}{(i&space;&plus;&space;j)})})


![image](https://latex.codecogs.com/png.image?\dpi{110}K&space;=&space;\frac{\sqrt{i&space;&plus;&space;j}}{2})

Using these factors, we can find P, or the change in both i and j where i is the winner and j is the loser.

![image](https://latex.codecogs.com/png.image?\dpi{110}P&space;(i&space;\geq&space;&space;j)&space;=&space;K&space;(|S|&space;-&space;S))

## Examples

A javascript example:

```js
function points(i, j) {
  K = Math.sqrt(i + j)/2;
  S = ((i + j) / (200 - ((200 * k)/(i + j))));
  P = K * (S - Math.floor(S));
  return [i + P, j - P];
}
```
