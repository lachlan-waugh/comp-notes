Modelling with differential equations
---

Exponentially changing systems have the general form (with arbitrary $k$)
> $x(t) = x_0e^{kt}$

In terms of differential equations this is
>  $\Large \frac{dx}{dt} $$= kx(t), \quad x(0) = x_0$.



## First order dynamics

The rate of change of a quantity is proportional to the quantity itself

> $\Large\frac{dx}{dt}$$=kx(t)$



### What is $k$

> $\Large\frac{dx}{dt}$$=kx(t)$  $\rarr$   $\Large\frac{\text{\# of cells}}{\text{time}}$$=k(\text{\# of cells})$
>
> $k=\text{time}^{-1}$ (has the dimension, it is a **rate/frequency**) 



### How is $k$ determined

#### Half life

> $x(t_\frac{1}{2})=x(0)e^{kt_{1/2}}   \qquad   \Large\frac{1}{2}$$x(0)=x(0)e^{kt_{1/2}}$
>
> $k = − \Large\frac{ln(2)}{t_\frac{1}{2}}$

#### Doubling time

> $x (t_d)=x(0)e^{kt_{1/2}} \quad 2x(0)=x(0)e^{kt_{1/2}}$
>
> $k = − \Large\frac{ln(2)}{t_d}$



### Time constants

If we want to calculate $k$

> $\Large \frac{dN}{dt}=$$-kN(t)$
>
> $k = − \Large\frac{ln(2)}{t_\frac{1}{2}}$ or $k = − \Large\frac{1}{t_{av}}$



## Malthusian dynamics

> $\text{Net rate of change} = \text{Rate in} - \text{Rate out}$



The probability in the next time interval $\Delta t$, that any given individual

* produces offspring (where $b$ is the per-capita production/growth rate)

> $b(\Delta t)=O((\Delta)^2)$

* dies (where $d$ is the per-capita death/mortality rate)

> $d(\Delta t)=O((\Delta)^2)$



### Population $N$ at time $t + \Delta t$

>  $N(t + \Delta t) = N(t) + bN(t)\Delta t - dN(t)\Delta t$

Rearranging, and taking the limit $\Delta t \rarr 0$, 
> $\lim_{\Delta t \rarr 0} \Large\frac{N(t + \Delta t) − N(t)}{\Delta t}$$ = \lim_{\Delta t \rarr 0}(b − d )N(t)$
>
> $\Large \frac{dN}{dt}$$=(b-d)N(t) \qquad N(0)=N_0, \quad  N(t)=N_0e^{(b-d)t}$



where:

* growth rate (Malthusian parameter):  $r=(b-d)$

* the reproductive ratio: $R_0=$$\Large\frac{b}{d}$

* carrying capacity of an environment: $K$ where no population $N>K$ is sustainable



## Limits to growth

For carrying capacity, we require:

> $\Large\frac{dN}{dt}$$=gN$
    * $g(0)=0$
    * $g(N)>0 \text{ when } 0<N<K$
    * $g(N)<0 \text{ when } N>K$



### Logistic equation

>  $\Large\frac{dN}{dt}$$=rN(1-\Large\frac{N}{K})$
	* $r\geq0$: the intrinsic growth rate
	* $K\geq0$: the carry capacity
	* $-\Large\frac{r}{K}$$N^2$: detrimental effect of interaction between 2 individuals (population law of mass action)



Standard form

> $N(t)=\Large\frac{KN_0e^{rt}}{K-N_0+N_0e^{rt}}$



## Stability

* equilibrium/critical point (steady state): a constant solution ($f(x)=0$)

* stable critical point: 

  > $\forall \epsilon > 0 \quad \exists \delta >0$
  >
  > $|x_0-\bar x|<\delta \quad \rarr \quad x(0)=x_0 \text{ has solution } |x(t)-\bar x|<\epsilon \quad \forall t$

* asymptotically stable: critical point

  > $\lim_{t \rarr \infty} x(t) = \bar x$



A steady state $\bar x \in \mathbb{R}$ of $\Large \frac{dx}{dt}$$=f(x)$ is:

* asymptotically stable if $f'(\bar x)<0$
* unstable if $f'(\bar x)>0$



### Visualising solution curves

> $\Large \frac{dy}{dx}$$=f(x,y)$

1. Graph some curves in the $xy$-plane along which $f(x, y)$ is constant (curves of constant slope/isloines)
2. Along the isocline $f(x,y)=k=\text{constant}$ 
   1. draw a number of parallel short line segments with slope $k$
   2. direction field is all of the isoclines on the graph



### Dynamics

If the independent variable in our ODE is time $t$, the equation describes equation of unknown function $x$

> $\Large \frac{dx}{dt}$$=f(x,t)$

* autonomous: $f(x,t)$ isn't an explicit function of time



Autonomous: slopes in direction field don't change in time



## Harvesting

If population $N$ is harvested at rate $H$, population growth rate for N is:

> $\Large \frac{dN}{dt}$$=g(N,t)-H$
>
> * $g(N,t)$: growth rate for population in absence of harvesting
> * $H$: the harvesting function

or, if the harvesting is **constant effort**, harvest rate is proportional to population size

> $\Large \frac{dN}{dt}$$=g(N,t)-hN \quad h>0 \text{ is a harvesting proportionality constant}$



Example:

* Seek integrating factor $\mu t$ such that LHS: $\Large \frac{d}{dt}$$(\mu(t)y)$
* Multiply by $e^{at}$ (or $e^{-at}$)
* Clean up with the product rule
* Integrate both sides
* Check the initial conditions
