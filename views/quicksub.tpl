%rebase layout nav_collapse_status='quicksub'


<div class="container">
    <form class="well form-vertical" action="/report" method="post">
     <a class="btn  btn-inverse">{{tip}}</a>
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
  

