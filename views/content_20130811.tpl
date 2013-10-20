%rebase layout nav_collapse_status='content'


<div class="container">
  <div class="row">
    <div class="span12">

      <table class="table table-striped table-bordered">
        <thead>
        <tr>
          <th>事件类型</th>
          <th>地址</th>
          <th>投诉主体</th>
          <th>肇事人或单位</th>
          <th>相关资料</th>
        </tr>
        </thead>  
        <tbody>
        <tr>
        %for row in rows:
        <tr>
          <th>{{row[1]}}</th>
          <th>{{row[2]}}</th>
          <th>{{row[3]}}</th>
          <th>{{row[4]}}</th>
          <th>&nbsp;<a href="{{row[5]}}" target="_blank">连接</a>&nbsp;<a href="{{row[6]}}" target="_blank">截图</a></th>
        </tr>
        %end
        </tbody>
        </table>


  <div class="row">
    <div class="span6">
    <div class="hero-unit">
        <p>本站旨在曝光不合理社会事实，它们无法通过法律手段以及信访途径得到有效解决。在中国，信访是一件很普遍的事情，这跟特殊的国情有关系，本站希望唤起大家对社会现实的持续关注。</p>

        <p>只要你在网络上看到相应的新闻，截图，或照片欢迎寄给我们。来信请寄到 petitionfail.org@gmail.com 。 或者在右边提交相关网址。</p>

        <p>欢迎律师给予法律上的建议。</p>
    </div>
    </div>


  <div class="span6">
    <form class="well form-vertical" action="/report" method="post">
      <h2><label><strong>提交线索</strong></label></h2>
      <label>
      <script type="text/javascript"
         src="http://www.google.com/recaptcha/api/challenge?k=6LdnjeUSAAAAAHnWgiJa3IK3_A5ueVFNvubdYd2d">
      </script>
      <noscript>
         <iframe src="http://www.google.com/recaptcha/api/noscript?k=6LdnjeUSAAAAAHnWgiJa3IK3_A5ueVFNvubdYd2d"
             height="300" width="500" frameborder="0"></iframe><br>
         <textarea name="recaptcha_challenge_field" rows="3" cols="40" />
         <input type="hidden" name="recaptcha_response_field" value="manual_challenge">
      </noscript><br>
      </label>
      <label>
      <input type="text" name="url" class="span3" placeholder="请输入提交网址">
      </label>
    <button type="submit" class="btn btn-primary">提交线索</button>
    </form>
   </div>
  </div>
  </div>
  </div>
  
</div>
  
