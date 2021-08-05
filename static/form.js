var name,mail,sub,mobile,msg;

function abc() {
  name=document.querySelector("#name").value;
  mail=document.querySelector("#mail").value;
  sub=document.querySelector("#sub").value;
  mobile=document.querySelector("#mobile").value;
  msg=document.querySelector("#msg").value;
  giveInfo();

}
function giveInfo() {
  console.log(name);
  console.log(mail);
  console.log(sub);
  console.log(mobile);
  console.log(msg);
}
