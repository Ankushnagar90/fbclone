// $(document).ready(function(){
//  debugger	
//   $('.comment-form').click(function(event){
//     debugger
//     // const url = "/home/detail/"+id+"/";
//     post_id=pk;
//     $.ajax({
//       type: 'POST',
//       url:  'http:8000/home/detail/id/',
//       dataType: 'json',
//       beforeSend: function() {
//         $("#myModal").modal("show");
//       }, 
//       success: function(response) {
//         debugger
//         console.log("Success!",response);
//         $("#myModal .modal-content").html(response['context']);
//       }
//     });
//   });

// });

$(document).ready(function(){
 
  $("#submit-comment").click(function(event){
  	debugger
     event.preventDefault();
     var id = $(this).attr("value");
     var url = "/home/detail/"+id+"/";
     var dataPosted = $("#mainSubmit").serialize();
     
     $.ajax({
          type: 'POST',
          url:  url,
          data: dataPosted,
          success:function(data)
          {
              console.log("Success!",data);
              if(data.status === "success") 
              {
                 var output = "";
                  output= `<div class="row mt-3">
                    <div class="col-lg-8 offset-lg-3 " ><strong><h2>
                      Comment{{ comments.count }}</h2></strong>
                      <span class="badge badge-dark ml-2">{{ comments.count }}</span>
                    </div>
                    {% for comment in comments %}
                    <div class="col-lg-6 offset-lg-3">
                      <div class="card p-2">
                        <div class="row">
                          <div class="col-12">
                            <strong>{{ user.username }}</strong> 
                          </div>
                          <div class="col-12">
                            <p class="m-1 mt-3">{{ comment.content }}</p>
                            <p class="text-right text-muted"><small>{{ comment.created }}</small></p>
                          </div>
                        </div>
                      </div>
                    </div>
                    {% endfor %}
                  </div>`
              } $('.commetingg').append(output);
              
          }


          
            error: function(rs, e)
            {
            console.log(rs.responseText);
        	}
       });
   });
})
       		// $('#commenting').text(response['content']);


        	// $("#myModal.modal-content").html(response['context']);





  







