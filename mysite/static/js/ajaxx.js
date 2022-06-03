$(document).ready(function(){
  
  $(".like-dislike").click(function(event){
    
     // event.preventDefault();
     var id = $(this).attr("value");
     var url = "/like/"+id+"/";
      
     $.ajax({
          type: 'POST',
          url:  url,
          data:{
             'id' : id,
            'csrfmiddlewaretoken': $("input[name=csrfmiddlewaretoken]").val()
          },
          success: function(response)

          { 
            
              console.log("Success!",response);  
              if (response.is_liked) {
                $(`#like-${id}`).text('Dislike');
                $(`#like-${id}`).removeClass("like-dislike btn btn-primary");
                $(`#like-${id}`).addClass("like-dislike btn btn-danger");
                $(`#like-${id}`).attr('id',`dislike-${id}`); 
                $(`#total_likes-${id}`).text(response.total_likes);
                
                // console.log (DISLIKE);
                // console.log('Show Dislike');
              }
              else {
                $(`#dislike-${id}`).text('Like');
                $(`#dislike-${id}`).removeClass("like-dislike btn btn-danger");
                $(`#dislike-${id}`).addClass("like-dislike btn btn-primary");
                $(`#dislike-${id}`).attr('id',`like-${id}`);
                $(`#total_likes-${id}`).text(response.total_likes);
                
                // console.log (LIKE);
                // console.log('Show like');
              }

              // data=$('#like').html(response['form'])
              // console.log (data);


          },
          error: function(rs, e)
          {
              console.log(rs.responseText);
          },  
      })
    })
})

