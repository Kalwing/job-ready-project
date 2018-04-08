op = {"clearButton": fullClear,
      "equalsButton": equals,
      }
arithmetic = {
      "addButton": add,
      "subtractButton": sub,
      "multiplyButton": mul,
      "divideButton": div,
      }

fullClear();

$("button").click(function() {
   if ($(this).attr('id') in op) { //If non arithmetic operation(clear or equal)
      op[$(this).attr('id')](); //execute the associated fonction
   }
   else if ($(this).attr('id') in arithmetic) { //If arithmetic operation (+-*/)
      if (lastOp) { //Print the result if an operation was already registered
                    //(ex: "1 + 3 -" will show "4" and continue with the "-"
                    //operation)
         equals()
      }
      lastNumber = $("#display").val();
      lastOp = arithmetic[$(this).attr('id')];
      toClear = true
   }
   else {
      if (toClear) {
         clear();
         toClear = false;
      }
      value = $(this).val();
      n = $("#display").val();
      $("#display").val(n + value)
   }
});

function clear(){
   $("#display").val("");
}
function fullClear(){
   lastNumber = "";
   lastOp = null;
   toClear = false;
   clear()
}
function equals(){
   if(lastOp != null) { //CHECK CASE 6
      $("#display").val(lastOp());
      toClear = true;
   }
}

function add() {
   x = lastNumber;
   y = $("#display").val();
   return parseInt(x) + parseInt(y);
}
function mul() {
   x = lastNumber;
   y = $("#display").val();
   return parseInt(x) * parseInt(y);
}
function div() {
   x = lastNumber;
   y = $("#display").val();
   return parseInt(x) / parseInt(y);
}
function sub() {
   x = lastNumber;
   y = $("#display").val();
   return parseInt(x) - parseInt(y);
}
