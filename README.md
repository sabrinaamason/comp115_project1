<h1>Sunrise Over a Maple Grove Python Turtle art</h1> 
<h2>Description</h2>
<p>This program uses the Python turtle module to draw the sun peeking out from between maple trees in the early fall. The sky alters colour as the sun is coming over the horizon, and each tree is littered with a random assortment of fall coloured maple leaves.</p>
<br>
<p>In this program, a mixture of functions, for loops, randomisation, geometric transformations, accumulator algorithms, and L-systems were used to complete the illustration.</p>
<br>
<h2>Code Overview</h2>
<h3>Functions</h3>
<p>The functions used in this illustration are:</p>
<h4>ground_fill(pens,y_start)</h4>
<p> - This function is used to create an ombre effect on the ground to simulate the early morning light cresting over the hills.</p>
<h4>draw_trees(pen,instructions,length)</h4>
<p> - This function is a modified L-system that is used to draw the tree variations that were made for this illustration (tree1_instruction, tree2_instruction, tree3_instruction).</p>
<h4>leaf_confetti(pen, pen_shape, leaf_per_colour, ymax, ymin, y_inup, y_inlow, xmax, xmin, x_inup, x_inlow)</h4>
<p> - This function stamps several colours of leaves randomly onto the in the designated areas of image (around the tree branches).</p>
<br>
<h3>Turtle Shape</h3>
<p>All turtle shapes that were used come from the turtle module itself, except for 1 (technically 4).</p>
<h4>Leafish pen shape</h4>
<p> the <i>Leafish</i> pen shape is actually 4 custom shapes that are the same design as one another but different sizes. The design was made by drawing a maple leaf and gathering the coordinates at each point and registering each shape to the module. This code can be seen under project1_leaf.py</p>
<br>
<h3>Other Drawings</h3>
<h4>Sky</h4>
<p>The sky is drawn using an accumulator algorithm with hand-picked colours to match a morning scene, and the sun is plopped on right onto it.</p>
<br>
<h2>Running the Program</h2>
<p><ol>
  <li>Clone/download this repository.</li>
  <li>Open the project file <strong>comp115_project1</strong></li>
  <li>Run the program <strong>sabrinamason_project1.py</strong></li>  
  <li>A window will open and the program will paint the fall sun rising over a maple grove.</li>
  <li>Click on the window to close it.</li>
</ol></p>
