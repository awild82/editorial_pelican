########
Elements
########

:slug: elements
:title: Example elements for this theme
:date: 2016-12-03 10:20
:authors: A.N. Other, John Doe
:category: Information
:splash_url: images/pic06.jpg
:summary: This article contains an example of all the elements in a page for this theme

.. class:: row

Sample Content
==============

Praesent ac adipiscing ullamcorper semper ut amet ac risus. Lorem sapien ut
odio odio nunc. Ac adipiscing nibh porttitor erat risus justo adipiscing
adipiscing amet placerat accumsan. Vis. Faucibus odio magna tempus adipiscing a
non. In mi primis arcu ut non accumsan vivamus ac blandit adipiscing adipiscing
arcu metus praesent turpis eu ac lacinia nunc ac commodo gravida adipiscing
eget accumsan ac nunc adipiscing adipiscing lorem ipsum dolor sit amet nullam
veroeros adipiscing.

.. class:: col-6 col-12-small

Sem turpis amet semper
----------------------

Nunc lacinia ante nunc ac lobortis. Interdum adipiscing gravida odio porttitor
sem non mi integer non faucibus ornare mi ut ante amet placerat aliquet.
Volutpat commodo eu sed ante lacinia. Sapien a lorem in integer ornare praesent
commodo adipiscing arcu in massa commodo lorem accumsan at odio massa ac ac.
Semper adipiscing varius montes viverra nibh in adipiscing blandit tempus
accumsan.

.. class:: col-6 col-12-small

Magna odio tempus commodo
-------------------------

In arcu accumsan arcu adipiscing accumsan orci ac. Felis id enim aliquet.
Accumsan ac integer lobortis commodo ornare aliquet accumsan erat tempus amet
porttitor. Ante commodo blandit adipiscing integer semper orci eget. Faucibus
commodo adipiscing mi eu nullam accumsan morbi arcu ornare odio mi adipiscing
nascetur lacus ac interdum morbi accumsan vis mi accumsan.

.. class:: col-4 col-12-medium

Interdum sapien gravida
-----------------------

Nunc lacinia ante nunc ac lobortis. Interdum adipiscing gravida odio porttitor
sem non mi integer non faucibus ornare mi ut ante amet placerat aliquet.
Volutpat eu sed ante lacinia sapien lorem accumsan varius montes viverra nibh
in adipiscing blandit.

.. class:: col-4 col-12-medium

Faucibus consequat lorem
------------------------

Nunc lacinia ante nunc ac lobortis. Interdum adipiscing gravida odio porttitor
sem non mi integer non faucibus ornare mi ut ante amet placerat aliquet.
Volutpat eu sed ante lacinia sapien lorem accumsan varius montes viverra nibh
in adipiscing blandit.

.. class:: col-4 col-12-medium

Accumsan montes viverra
-----------------------

Nunc lacinia ante nunc ac lobortis. Interdum adipiscing gravida odio porttitor
sem non mi integer non faucibus ornare mi ut ante amet placerat aliquet.
Volutpat eu sed ante lacinia sapien lorem accumsan varius montes viverra nibh
in adipiscing blandit.


------------------------------------------------------------------------------

.. class:: row

Elements
========

Praesent ac adipiscing ullamcorper semper ut amet ac risus. Lorem sapien ut
odio odio nunc. Ac adipiscing nibh porttitor erat risus justo adipiscing
adipiscing amet placerat accumsan. Vis. Faucibus odio magna tempus adipiscing a
non. In mi primis arcu ut non accumsan vivamus ac blandit adipiscing adipiscing
arcu metus praesent turpis eu ac lacinia nunc ac commodo gravida adipiscing
eget accumsan ac nunc adipiscing adipiscing lorem ipsum dolor sit amet nullam
veroeros adipiscing.

.. class:: col-6 col-12-small

Textual
-------

Text
++++

.. role:: rust(code)
  :language: rust
  :class: highlight

.. role:: underline
  :class: underline

This is **bold** and this is :strong:`strong`. This is *italic* and this is
:emphasis:`emphasized`. This is :sup:`superscript` text and this is
:sub:`subscript` text. This is code :rust:`for i in 0..3 { println!(i); }`.
This is :underline:`underlined`, and finally this is `a link <#>`_.


Heading level 4
+++++++++++++++
Dolor etiam magna etiam.

Heading level 5
^^^^^^^^^^^^^^^
Dolor etiam magna etiam.

------------------------------------------------------------------------------


.. class:: row

Lists
+++++

Nunc lacinia ante nunc ac lobortis. Interdum adipiscing gravida odio porttitor
sem non mi integer non faucibus ornare mi ut ante amet placerat aliquet.
Volutpat eu sed ante lacinia sapien lorem accumsan varius montes viverra nibh
in adipiscing blandit tempus accumsan.

.. class:: col-6 col-12-small

Unordered
^^^^^^^^^

* Dolor etiam magna etiam.
* Sagittis lorem eleifend.
* Felis dolore viverra.

.. class:: col-6 col-12-small

Ordered
^^^^^^^

1. Dolor etiam magna etiam.
2. Etiam vel lorem sed viverra.
3. Felis dolore viverra.
4. Dolor etiam magna etiam.

Block quote
+++++++++++

    Lorem ipsum dolor vestibulum ante ipsum primis in faucibus vestibulum.
    Blandit adipiscing eu felis iaculis volutpat ac adipiscing accumsan eu
    faucibus. Integer ac pellentesque praesent. Lorem ipsum dolor. Lorem ipsum
    dolor vestibulum ante ipsum primis in faucibus vestibulum. Blandit
    adipiscing eu felis iaculis volutpat ac adipiscing accumsan eu faucibus.

Table
+++++

Default
^^^^^^^

====== ============================================== =========
 Name        Description                                Price
====== ============================================== =========
Item1  Ante turpis integer aliquet porttitor.           29.99
Item2  Vis ac commodo adipiscing arcu aliquet.          19.99
Item3  Morbi faucibus arcu accumsan lorem.              29.99
Item4  Vitae integer tempus condimentum.                19.99
Item5  Ante turpis integer aliquet porttitor.           29.99
====== ============================================== =========

Alternative
^^^^^^^^^^^

.. class:: alt

====== ============================================== =========
 Name        Description                                Price
====== ============================================== =========
Item1  Ante turpis integer aliquet porttitor.           29.99
Item2  Vis ac commodo adipiscing arcu aliquet.          19.99
Item3  Morbi faucibus arcu accumsan lorem.              29.99
Item4  Vitae integer tempus condimentum.                19.99
Item5  Ante turpis integer aliquet porttitor.           29.99
====== ============================================== =========

Preformatted
++++++++++++

.. code:: python
  :class: highlight
  :number-lines:

  def fun(msg):
      print(msg)

  if __name__ == '__main__':
    fun('Hello world!')

.. class:: col-6 col-12-small

Graphical
---------

Images
++++++

.. SINGLE PICTURE
.. container:: image fit

  .. image:: {static}/images/main.jpg


.. GRID 

.. container:: box alt

  .. container:: row gtr-50 gtr-uniform

    .. container:: col-4
    
      .. container:: image fit 
    
        .. image:: {static}/images/pic06.jpg
    
    .. container:: col-4
    
      .. container:: image fit
    
        .. image:: {static}/images/pic05.jpg
    
    .. container:: col-4
    
      .. container:: image fit
    
        .. image:: {static}/images/pic04.jpg
    
    .. container:: col-4
    
      .. container:: image fit
    
        .. image:: {static}/images/pic04.jpg
    
    .. container:: col-4
    
      .. container:: image fit
    
        .. image:: {static}/images/pic06.jpg

    .. container:: col-4
    
      .. container:: image fit
    
        .. image:: {static}/images/pic05.jpg

    .. container:: col-4
    
      .. container:: image fit
    
        .. image:: {static}/images/pic05.jpg
    
    .. container:: col-4
    
      .. container:: image fit
    
        .. image:: {static}/images/pic04.jpg
    
    .. container:: col-4
    
      .. container:: image fit
    
        .. image:: {static}/images/pic06.jpg
    
Left & Right
++++++++++++

.. container:: image left
  
  .. image:: {static}/images/pic06.jpg

Lorem ipsum dolor sit accumsan interdum nisi, quis tincidunt felis sagittis
eget. tempus euismod. Vestibulum ante ipsum primis in faucibus vestibulum.
Blandit adipiscing eu felis iaculis volutpat ac adipiscing accumsan eu
faucibus. Integer ac pellentesque praesent tincidunt felis sagittis eget.
tempus euismod. Vestibulum ante ipsum primis sagittis eget. tempus euismod.
Vestibulum ante ipsum primis in faucibus vestibulum. Blandit adipiscing eu
felis iaculis volutpat ac adipiscing accumsan eu faucibus. Integer ac
pellentesque praesent.

.. container:: image right
  
  .. image:: {static}/images/pic05.jpg

Lorem ipsum dolor sit accumsan interdum nisi, quis tincidunt felis sagittis
eget. tempus euismod. Vestibulum ante ipsum primis in faucibus vestibulum.
Blandit adipiscing eu felis iaculis volutpat ac adipiscing accumsan eu
faucibus. Integer ac pellentesque praesent tincidunt felis sagittis eget.
tempus euismod. Vestibulum ante ipsum primis sagittis eget. tempus euismod.
Vestibulum ante ipsum primis in faucibus vestibulum. Blandit adipiscing eu
felis iaculis volutpat ac adipiscing accumsan eu faucibus. Integer ac
pellentesque praesent.

Math
++++

.. math::

  i \hbar \frac{\partial}{\partial t}\Psi(t) = \hat{H}(t) \Psi(t)

  \boldsymbol{H} = \begin{bmatrix}
    \boldsymbol{H}^{\alpha \alpha} & \boldsymbol{H}^{\alpha \beta} \\
    \boldsymbol{H}^{\beta \alpha} & \boldsymbol{H}^{\beta \beta}
    \end{bmatrix}



.. class:: row

Box
---

Lorem ipsum dolor sit accumsan interdum nisi, quis tincidunt felis sagittis
eget. tempus euismod. Vestibulum ante ipsum primis in faucibus vestibulum.
Blandit adipiscing eu felis iaculis volutpat ac adipiscing accumsan eu
faucibus.

.. class:: col-4 col-12-medium

Colored Bad
+++++++++++

.. warning::
  Felis sagittis eget tempus primis in faucibus vestibulum. Blandit adipiscing
  eu felis iaculis volutpat ac adipiscing accumsan eu faucibus. 

.. danger::
  Integer ac pellentesque praesent tincidunt felis sagittis eget. tempus
  euismod. Magna sed etiam ante ipsum primis in faucibus vestibulum.

.. class:: col-4 col-12-medium

Colored Good
++++++++++++

.. tip::
  Vestibulum ante ipsum primis in faucibus vestibulum. Blandit adipiscing eu
  felis iaculis volutpat ac adipiscing accumsan eu faucibus.

.. important::
  Lorem ipsum dolor sit accumsan interdum nisi, quis tincidunt felis sagittis
  eget. tempus euismod.
  
.. admonition:: Custom title with coloring
  :class: tip

  Vestibulum ante ipsum primis in faucibus vestibulum. Blandit adipiscing eu
  felis iaculis volutpat ac adipiscing accumsan eu faucibus.


.. class:: col-4 col-12-medium

Uncolored
+++++++++

.. note::
  Magna sed etiam ante ipsum primis in faucibus vestibulum.

.. admonition:: Custom block title

  Blandit adipiscing eu felis iaculis volutpat ac adipiscing accumsan eu
  faucibus.
