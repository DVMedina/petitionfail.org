%rebase layout nav_collapse_status='webref'

      <!-- Begin page content -->
<div class="container">
    <div class="page-header">
        <h2>网友举报</h2>
    </div>

<table class="table table-striped">

<tbody>
%for row in rows:
  <tr> <th><a href="{{row[1]}}" target="_blank"> {{row[2]}} </a></th> </tr>
%end
</tbody>


</table>



    <div id="push"></div>
    <hr>
</div>

