
// Boring event handlers
$(document).ready(function(){
    refreshScreen()
    loadSortable()

    $(document).on('click','.btn.list_add', function(){
      refreshScreen()

      // list 정렬을 위해서 list 갯수 파악용으로 추가
      // 그러나 현재 크게 사용용도 없음
      order = $(".cl-container").length

      $.ajax({
        url : '/list/',
        type : 'post',
        data : {order_num:order},
        success: function(data){
          var jsonData = data;

          $("#content").append(
          "<div class='cl-container' id='"+jsonData.list_id+"'>"+
            "<button type='button' class='btn btn-default list_del'>List Del</button>"+
            "<div class='cl-container-header'>"+
              "<h2>"+
                "<label class='cl-list-title'>List</label>"+
              "</h2>"+
            "</div>"+
            "<div class='input-group' style='margin:10px; width:90%''>"+
              "<input type='text' class='form-control' placeholder='Card title'>"+
              "<span class='input-group-btn'>"+
                "<button class='btn btn-default card_add' type='button'>Add</button>"+
              "</span>"+
            "</div>"+
            "<ul class='cl-container-body'>"+
            "</ul>"+
          "</div>");
          // 동적으로 생성된 list에 sortable 기능을 부여하기 위한 함수 호출
          loadSortable()
        },error : function(data) {
          var jsonData = data;
          alert("List Add Error")
        }
      });
    }).on('click', '.btn.list_del', function () {
       // Ajax 연결 후에도 선택한 객체를 사용하기 위해서 선언
       var list_obj = $(this) 
       var list_id = $(this).parent()[0].id;

       $.ajax({
        url:'/list/',
        type:'delete',
        data: {list_id:list_id},
        success: function(data){
          var jsonData = data;
          list_obj.parent().remove()

        },error: function(data){
          var jsonData = data;
          alert("List Delete Error")
        }
       });
    });

    $(document).on('click','.card_add', function(){
        var card_obj = $(this) 
        var list_id = $(this).closest(".cl-container")[0].id
        var title = $(this).parent().parent().children('input').val()
        var order = $(this).closest(".cl-container").find(".cl-card").length

        $.ajax({
          url:'/card/',
          type:'post',
          data: {order:order, title:title, list_id:list_id},
          success: function(data){
            var jsonData = data;

            card_obj.closest(".cl-container").find('.cl-container-body').append(
                  "<li class='cl-card' id='"+jsonData.card_id+"''>"+
                      "<label>"+title+"</label>"+
                      "<button class='btn btn-default card_delete'>Del</button>"+
                  "</li>")

          },error: function(data){
            var jsonData = data;
            alert("Card Add Error")
          }
        });

        
    }).on('click', '.btn.card_delete', function(event){
        var card_obj = $(this) 
        var list_id = $(this).closest(".cl-container")[0].id
        var card_id = $(this).parent()[0].id;

        $.ajax({
          url:'/card/',
          type:'delete',
          data: {card_id:card_id, list_id:list_id},
          success: function(data){
            var jsonData = data;

            card_obj.parent().remove();

          },error: function(data){
            var jsonData = data;
            alert("Card Delete Error")
          }
        })
        event.stopPropagation();

    }).on('click', '.cl-card', function(){
        var card_obj = $(this) 
        var list_id = $(this).closest(".cl-container")[0].id
        var card_id = $(this)[0].id

        // modal 호출시에 modal에 hidden 타입 input에 값 선언
        // modal에서 데이터 수정 후 db 필터를 하기 위한 값
        $("#cardModal").find("input#modal-list_id").val(list_id)
        $("#cardModal").find("input#modal-card_id").val(card_id)

        // front의 html 코드 자체에서는 card의 내용값을 가지고 있지 않음
        // 카드 선택시에 get을 통해서 데이터를 가져와 보여줌
        $.ajax({
          url:'/card/',
          type:'get',
          data: {card_id:card_id, list_id:list_id},
          success: function(data){
            var jsonData = data;

            $("#cardModal").find("input#card-title").val(jsonData.title)
            $("#cardModal").find("input#description").val(jsonData.description)
            $("#cardModal").find("input#tag").val(jsonData.tag)

          },error: function(data){
            var jsonData = data;
            alert("Card Error")
          }
        })

        $("#cardModal").modal('show');

    }).on('click', '#card-submit', function(){
        var list_id = $("#cardModal").find("input#modal-list_id").val()
        var card_id = $("#cardModal").find("input#modal-card_id").val()
        var title = $("#cardModal").find("input#card-title").val()
        var description = $("#cardModal").find("input#description").val()
        var tag = $("#cardModal").find("input#tag").val()

        $.ajax({
          url : '/card/',
          type : 'put',
          data : {list_id:list_id, card_id:card_id, title:title, description:description, tag:tag},
          success: function(data){
            $(".cl-card#"+card_id+" label").text(title)
            $("#cardModal").modal("hide")
          },
          error : function(data) {
            alert("Error : "+data)
          }
        });
    })

});

function loadSortable(){
  // dnd를 통한 상황에서 정렬이 가능하도록 하기 위한 코드
  // 처음 화면 실행시와 list 생성시에 호출하도록 함
  $( ".content, .cl-container-body" ).sortable().disableSelection();
}

function refreshScreen(){
  // Board의 width 사이즈를 유동적으로 늘려주기 위해서 체크하는 코드
  // list 갯수와 list 추가 버튼은 같은 공간에 속함, 공간의 여유를 위해서+2의 양으로 늘려줌
  var list_cnt = $(".cl-container").length+2
  var list_width = $(".cl-container").width()
  
  if((list_cnt*list_width) > $(window).width()){
    $(".board").css("width", (list_cnt*list_width))
  }
}
