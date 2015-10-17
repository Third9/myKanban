// $(function() {
    
//   });

// Boring event handlers
$(document).ready(function(){
    $( ".content, .cl-container-body" ).sortable().disableSelection();

    $(document).on('click','.btn.list_add', function () {
       alert('List Add.');
       $("#content").append(
        "<div class='cl-container'>"+
          "<a type='button' class='btn list_del'>List del</a>"+
          "<div class='cl-container-header'>"+
            "<h2>Title</h2>"+
            "<hr>"+
          "</div>"+
          "<ul class='cl-container-body'>"+
            "<input type='text' placeholder='Text' />"+
            "<button type='button' class='btn card_add'><i class='icon-plus'></i>Add</button>"+
          "</ul>"+
        "</div>");

       $( ".content, .cl-container-body" ).sortable().disableSelection();

    }).on('click', '.btn.list_del', function () {
       alert('List Del.');
       $(this).parent().remove()
    });

    $(document).on('click','.btn.card_add', function(){
        alert('card Add.');
        $(this).parent().append("<li >"+
                                    "test"+
                                    "<button class='btn card_delete'><i class='icon-plus'></i>Del</button>"+
                                "</li>")
    }).on('click', '.btn.card_delete', function(){
        alert('card Del.');
        $(this).parent().remove()
    })
});

