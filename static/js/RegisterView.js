(window.webpackJsonp=window.webpackJsonp||[]).push([[2],{NPtU:function(e,t,r){"use strict";r.r(t),r.d(t,"AppBar",(function(){return D}));var a=r("q1tI"),n=r.n(a),i=r("X78M"),o=r("V4z/"),l=r("NZDO"),s=r("PQzt"),u=r("Gqia"),m=r("WNlj"),c=r("z6Y5"),f=r("uVCN"),p=r("5I82"),d=r("/MKj"),g=r("zfIj"),b=r("UGp+"),y=r("KYPV"),h=r("hS4W"),v=r.n(h),x=r("vDqi"),E=r.n(x),w=r("7QZ+"),S=r("sDGz"),T=r("UFE9");function O(e){return O="function"==typeof Symbol&&"symbol"==typeof Symbol.iterator?function(e){return typeof e}:function(e){return e&&"function"==typeof Symbol&&e.constructor===Symbol&&e!==Symbol.prototype?"symbol":typeof e},O(e)}function j(e,t){return function(e){if(Array.isArray(e))return e}(e)||function(e,t){var r=null==e?null:"undefined"!=typeof Symbol&&e[Symbol.iterator]||e["@@iterator"];if(null!=r){var a,n,i,o,l=[],s=!0,u=!1;try{if(i=(r=r.call(e)).next,0===t){if(Object(r)!==r)return;s=!1}else for(;!(s=(a=i.call(r)).done)&&(l.push(a.value),l.length!==t);s=!0);}catch(e){u=!0,n=e}finally{try{if(!s&&null!=r.return&&(o=r.return(),Object(o)!==o))return}finally{if(u)throw n}}return l}}(e,t)||function(e,t){if(!e)return;if("string"==typeof e)return C(e,t);var r=Object.prototype.toString.call(e).slice(8,-1);"Object"===r&&e.constructor&&(r=e.constructor.name);if("Map"===r||"Set"===r)return Array.from(e);if("Arguments"===r||/^(?:Ui|I)nt(?:8|16|32)(?:Clamped)?Array$/.test(r))return C(e,t)}(e,t)||function(){throw new TypeError("Invalid attempt to destructure non-iterable instance.\nIn order to be iterable, non-array objects must have a [Symbol.iterator]() method.")}()}function C(e,t){(null==t||t>e.length)&&(t=e.length);for(var r=0,a=new Array(t);r<t;r++)a[r]=e[r];return a}function A(e,t,r){return(t=function(e){var t=function(e,t){if("object"!==O(e)||null===e)return e;var r=e[Symbol.toPrimitive];if(void 0!==r){var a=r.call(e,t||"default");if("object"!==O(a))return a;throw new TypeError("@@toPrimitive must return a primitive value.")}return("string"===t?String:Number)(e)}(e,"string");return"symbol"===O(t)?t:String(t)}(t))in e?Object.defineProperty(e,t,{value:r,enumerable:!0,configurable:!0,writable:!0}):e[t]=r,e}var I=Object(i.a)((function(e){var t;return{submitProgress:{position:"absolute",top:"50%",left:"50%",marginTop:-12,marginLeft:-12},mainBlock:A({minWidth:"400px",margin:"0",padding:"0"},e.breakpoints.down("sm"),{minWidth:"300px"}),avatarLogo:A({width:200,height:72,position:"absolute",top:"50%",left:"33%"},e.breakpoints.down("sm"),{left:"20%",top:"30%"}),title:A({fontFamily:"Montserrat",fontWeight:"700",fontSize:"72px",textAlign:"center",lineHeight:"87.7px",color:"#FFFFFF",margin:"auto",marginTop:"50vh",marginBottom:"auto"},e.breakpoints.down("sm"),{marginTop:"10vh"}),rightSide:(t={width:"100%",height:"100vh",backgroundColor:"#F5F5F5",display:"flex",flexDirection:"column",justifyContent:"center",alignItems:"center",margin:"0",paddingRight:"200px",padding:"0"},A(t,e.breakpoints.up("md"),{paddingLeft:"244px"}),A(t,e.breakpoints.down("sm"),{width:"100%",paddingLeft:"0",justifyContent:"center",alignItems:"center",paddingRight:"0px",marginTop:"-100px"}),t)}})),N=function(){var e=I(),t=Object(o.p)(),r=Object(d.b)(),i=j(Object(a.useState)({isAlert:!1,alertTitle:"",alertText:"",severity:""}),2),s=i[0],m=i[1];return n.a.createElement(n.a.Fragment,null,n.a.createElement(l.a,{className:e.mainBlock},s.isAlert?n.a.createElement(g.a,{open:s.isAlert,severity:s.severity,alertTitle:s.alertTitle,alertText:s.alertText,onClose:function(){return m({isAlert:!1,alertTitle:"",alertText:"",severity:""})}}):null,n.a.createElement(l.a,{display:"flex",flexDirection:"column",height:"100%",justifyContent:"center"},n.a.createElement(y.b,{initialValues:{email:"",password:""},validationSchema:b.d().shape({email:b.f().email("Must be a valid email").max(255).required("Email is required"),password:b.f().max(255).required("Password is required")}),onSubmit:function(e,a){var n=a.setSubmitting,i=a.resetForm,o=w.a.login,l={headers:{"X-CSRFToken":v.a.get("csrftoken")}};E.a.post(o,e,l).then((function(a){var i;200===a.status&&(window.sessionStorage.setItem("token",null===(i=a.data)||void 0===i||null===(i=i.data)||void 0===i?void 0:i.token),n(!1),r(Object(S.b)(e.taxYear)),t("/"))})).catch((function(e){400===e.response.status?(m({isAlert:!0,alertText:"Invalid credentials",severity:"error",alertTitle:"Error"}),n(!1)):(m({isAlert:!0,alertText:"Something went wrong",severity:"error",alertTitle:"Error"}),i(),n(!1))}))}},(function(e){var t=e.errors,r=e.handleBlur,a=e.handleChange,i=e.handleSubmit,o=e.isSubmitting,s=e.touched,m=e.values;return n.a.createElement("form",{autoComplete:"off",onSubmit:i},n.a.createElement(l.a,{mb:3},n.a.createElement(u.a,{color:"textPrimary",variant:"h4"},"SIGN IN TO YOUR ACCOUNT")),n.a.createElement(T.a,{attribute:"Email Address",is_required:!0,error:Boolean(s.email&&t.email),fullWidth:!0,helperText:s.email&&t.email,margin:"normal",name:"email",onBlur:r,onChange:a,type:"email",value:m.email,variant:"outlined"}),n.a.createElement(T.a,{attribute:"Password",is_required:!0,error:Boolean(s.password&&t.password),fullWidth:!0,helperText:s.password&&t.password,margin:"normal",name:"password",onBlur:r,onChange:a,type:"password",value:m.password,variant:"outlined"}),n.a.createElement(l.a,{my:2},n.a.createElement(p.a,{color:"primary",disabled:o,fullWidth:!0,size:"large",type:"submit",variant:"contained"},"Sign in now")))})))))},k=r("yXLF");function P(e){return P="function"==typeof Symbol&&"symbol"==typeof Symbol.iterator?function(e){return typeof e}:function(e){return e&&"function"==typeof Symbol&&e.constructor===Symbol&&e!==Symbol.prototype?"symbol":typeof e},P(e)}function q(e,t){return function(e){if(Array.isArray(e))return e}(e)||function(e,t){var r=null==e?null:"undefined"!=typeof Symbol&&e[Symbol.iterator]||e["@@iterator"];if(null!=r){var a,n,i,o,l=[],s=!0,u=!1;try{if(i=(r=r.call(e)).next,0===t){if(Object(r)!==r)return;s=!1}else for(;!(s=(a=i.call(r)).done)&&(l.push(a.value),l.length!==t);s=!0);}catch(e){u=!0,n=e}finally{try{if(!s&&null!=r.return&&(o=r.return(),Object(o)!==o))return}finally{if(u)throw n}}return l}}(e,t)||function(e,t){if(!e)return;if("string"==typeof e)return B(e,t);var r=Object.prototype.toString.call(e).slice(8,-1);"Object"===r&&e.constructor&&(r=e.constructor.name);if("Map"===r||"Set"===r)return Array.from(e);if("Arguments"===r||/^(?:Ui|I)nt(?:8|16|32)(?:Clamped)?Array$/.test(r))return B(e,t)}(e,t)||function(){throw new TypeError("Invalid attempt to destructure non-iterable instance.\nIn order to be iterable, non-array objects must have a [Symbol.iterator]() method.")}()}function B(e,t){(null==t||t>e.length)&&(t=e.length);for(var r=0,a=new Array(t);r<t;r++)a[r]=e[r];return a}function W(e,t,r){return(t=function(e){var t=function(e,t){if("object"!==P(e)||null===e)return e;var r=e[Symbol.toPrimitive];if(void 0!==r){var a=r.call(e,t||"default");if("object"!==P(a))return a;throw new TypeError("@@toPrimitive must return a primitive value.")}return("string"===t?String:Number)(e)}(e,"string");return"symbol"===P(t)?t:String(t)}(t))in e?Object.defineProperty(e,t,{value:r,enumerable:!0,configurable:!0,writable:!0}):e[t]=r,e}var F=Object(i.a)((function(e){return{submitProgress:{position:"absolute",top:"50%",left:"50%",marginTop:-12,marginLeft:-12},mainBlock:W({minWidth:"400px",margin:"0",padding:"0"},e.breakpoints.down("sm"),{minWidth:"300px"})}})),M=function(){var e=F(),t=(Object(o.p)(),Object(d.b)(),q(Object(a.useState)({isAlert:!1,alertTitle:"",alertText:"",severity:""}),2)),r=t[0],i=t[1],s=q(Object(a.useState)(!1),2),m=(s[0],s[1]),c=q(Object(a.useState)({email:""}),2),f=c[0],b=c[1],y=q(Object(a.useState)(!1),2),h=y[0],x=y[1];return n.a.createElement(l.a,{className:e.mainBlock},r.isAlert?n.a.createElement(g.a,{open:r.isAlert,severity:r.severity,alertTitle:r.alertTitle,alertText:r.alertText,onClose:function(){return i({isAlert:!1,alertTitle:"",alertText:"",severity:""})}}):null,n.a.createElement(l.a,{display:"flex",flexDirection:"column",height:"100%",justifyContent:"center"},n.a.createElement(l.a,{mb:3},n.a.createElement(u.a,{color:"textPrimary",variant:"h4"},"FORGOT PASSWORD?")),n.a.createElement(T.a,{autoFocus:!0,margin:"dense",id:"name",attribute:"Email ID (User ID)",is_required:!0,type:"email",fullWidth:!0,autoComplete:"off",value:f.email,onChange:function(e){return b({email:e.target.value})}}),n.a.createElement(l.a,{my:2},n.a.createElement(p.a,{onClick:function(){var e=w.a.forgotPassword;x(!0);var t={headers:{"X-CSRFToken":v.a.get("csrftoken")}};E.a.post(e,f,t).then((function(e){i({isAlert:!0,alertText:e.data.message,severity:"success"}),m(!1),x(!1),b({email:""})})).catch((function(e){console.log(e.response),i({isAlert:!0,alertText:e.response.data.message,severity:"error",alertTitle:"Error"}),m(!1),x(!1),b({email:""})}))},color:"primary",disabled:h,fullWidth:!0,size:"large",type:"submit",variant:"contained"},"Reset Password",h&&n.a.createElement(k.a,{size:24,className:e.submitProgress})))))};function z(e){return z="function"==typeof Symbol&&"symbol"==typeof Symbol.iterator?function(e){return typeof e}:function(e){return e&&"function"==typeof Symbol&&e.constructor===Symbol&&e!==Symbol.prototype?"symbol":typeof e},z(e)}function R(e,t,r){return(t=function(e){var t=function(e,t){if("object"!==z(e)||null===e)return e;var r=e[Symbol.toPrimitive];if(void 0!==r){var a=r.call(e,t||"default");if("object"!==z(a))return a;throw new TypeError("@@toPrimitive must return a primitive value.")}return("string"===t?String:Number)(e)}(e,"string");return"symbol"===z(t)?t:String(t)}(t))in e?Object.defineProperty(e,t,{value:r,enumerable:!0,configurable:!0,writable:!0}):e[t]=r,e}var L=Object(i.a)((function(e){var t;return{box:R({border:"1px solid #000000",padding:"20px",marginBottom:"20px",backgroundColor:"#f7f7f7",display:"flex",flexDirection:"column",justifyContent:"center",alignItems:"center",minHeight:"300px"},e.breakpoints.down("sm"),{minHeight:"280px",padding:"20px 10px"}),logoAvatar:(t={},R(t,e.breakpoints.up("sm"),{marginRight:"auto"}),R(t,e.breakpoints.down("sm"),{marginLeft:"auto",marginRight:"150px"}),t)}})),D=function(){var e=L();return n.a.createElement(l.a,{sx:{display:"flex",justifyContent:"space-between",backgroundColor:"#fafafa",padding:"5px 20px"}},n.a.createElement(l.a,{sx:{display:{xs:"none",sm:"block"}}},n.a.createElement(l.a,{sx:{display:"flex"}},n.a.createElement(s.a,{variant:"square",src:"/static/img/onecall-logo.png",sx:{height:50,width:140,marginBottom:"10px"},className:e.logoAvatar}),n.a.createElement(u.a,{variant:"h6",sx:{fontSize:"16px",marginTop:"12px",marginLeft:"20px"}},"WE MAKE TAX SIMPLE")),n.a.createElement(u.a,{variant:"body2",sx:{fontSize:"16px"}},n.a.createElement("strong",null,"Phone:")," (248) 971-3300"),n.a.createElement(u.a,{variant:"body2",sx:{fontSize:"16px"}},n.a.createElement("strong",null,"E-mail:")," Onecalltaxservices.digital@gmail.com")),n.a.createElement(s.a,{variant:"square",src:"/static/img/irs_image.jpg",sx:{width:"81px",height:"83px",display:{xs:"none",sm:"flex"}}}),n.a.createElement(l.a,{sx:{display:{xs:"block",sm:"none"}}},n.a.createElement(s.a,{variant:"square",src:"/static/img/onecall-logo.png",sx:{height:50,width:140,marginTop:"12px",marginBottom:"10px"},className:e.logoAvatar}),n.a.createElement(u.a,{variant:"h6",sx:{fontSize:"16px"}},"WE MAKE TAX SIMPLE")))};t.default=function(){var e=L(),t=Object(o.p)();return n.a.createElement(f.a,{title:"Login"},n.a.createElement(l.a,{sx:{height:"100vh",backgroundImage:"url(/static/img/green_bg.jpg)",paddingTop:"8%",backgroundRepeat:"no-repeat",backgroundSize:"100% 100%"}},n.a.createElement(m.a,{maxWidth:"lg"},n.a.createElement(l.a,{sx:{backgroundColor:"#fafafa",padding:"5px 5px 30px"}},n.a.createElement(D,null),n.a.createElement(l.a,{sx:{padding:{xs:0,sm:"20px 30px"}}},n.a.createElement(c.a,{container:!0,spacing:2},n.a.createElement(c.a,{item:!0,xs:12,sm:6},n.a.createElement(l.a,{className:e.box},n.a.createElement(N,null))),n.a.createElement(c.a,{item:!0,xs:12,sm:6},n.a.createElement(l.a,{className:e.box},n.a.createElement(M,null)))),n.a.createElement(l.a,{sx:{display:"flex",justifyContent:"center",alignItems:"center"}},n.a.createElement(u.a,{variant:"h5"},"New Client? Please"),n.a.createElement(s.a,{onClick:function(){return t("/register")},variant:"square",src:"/static/img/register.png",sx:{height:33,width:99,marginLeft:"10px"}})))))))}},SuzI:function(e,t,r){"use strict";r.r(t);var a=r("q1tI"),n=r.n(a),i=r("V4z/"),o=r("NZDO"),l=r("WNlj"),s=r("Gqia"),u=r("LutX"),m=r("5I82"),c=r("X78M"),f=r("UFE9"),p=r("NPtU"),d=r("zfIj"),g=r("UGp+"),b=r("KYPV"),y=r("hS4W"),h=r.n(y),v=r("vDqi"),x=r.n(v),E=r("7QZ+"),w=r("uVCN");r("cuOD");function S(e){return S="function"==typeof Symbol&&"symbol"==typeof Symbol.iterator?function(e){return typeof e}:function(e){return e&&"function"==typeof Symbol&&e.constructor===Symbol&&e!==Symbol.prototype?"symbol":typeof e},S(e)}function T(e,t){return function(e){if(Array.isArray(e))return e}(e)||function(e,t){var r=null==e?null:"undefined"!=typeof Symbol&&e[Symbol.iterator]||e["@@iterator"];if(null!=r){var a,n,i,o,l=[],s=!0,u=!1;try{if(i=(r=r.call(e)).next,0===t){if(Object(r)!==r)return;s=!1}else for(;!(s=(a=i.call(r)).done)&&(l.push(a.value),l.length!==t);s=!0);}catch(e){u=!0,n=e}finally{try{if(!s&&null!=r.return&&(o=r.return(),Object(o)!==o))return}finally{if(u)throw n}}return l}}(e,t)||function(e,t){if(!e)return;if("string"==typeof e)return O(e,t);var r=Object.prototype.toString.call(e).slice(8,-1);"Object"===r&&e.constructor&&(r=e.constructor.name);if("Map"===r||"Set"===r)return Array.from(e);if("Arguments"===r||/^(?:Ui|I)nt(?:8|16|32)(?:Clamped)?Array$/.test(r))return O(e,t)}(e,t)||function(){throw new TypeError("Invalid attempt to destructure non-iterable instance.\nIn order to be iterable, non-array objects must have a [Symbol.iterator]() method.")}()}function O(e,t){(null==t||t>e.length)&&(t=e.length);for(var r=0,a=new Array(t);r<t;r++)a[r]=e[r];return a}function j(e,t,r){return(t=function(e){var t=function(e,t){if("object"!==S(e)||null===e)return e;var r=e[Symbol.toPrimitive];if(void 0!==r){var a=r.call(e,t||"default");if("object"!==S(a))return a;throw new TypeError("@@toPrimitive must return a primitive value.")}return("string"===t?String:Number)(e)}(e,"string");return"symbol"===S(t)?t:String(t)}(t))in e?Object.defineProperty(e,t,{value:r,enumerable:!0,configurable:!0,writable:!0}):e[t]=r,e}var C=Object(c.a)((function(e){return{root:{backgroundColor:e.palette.background.dark,height:"100%"},alert:j({position:"absolute",right:50,top:50},e.breakpoints.down("sm"),{right:20,maxWidth:250}),logo:{width:100},menuPaper:{maxHeight:200},mainBlock:j({padding:"10px 50px 20px",margin:"20px",border:"1px solid #000000",minWidth:"500px"},e.breakpoints.down("sm"),{minWidth:"350px",padding:"10px 0 10px 5px",margin:"10px 0"})}}));t.default=function(){var e=C(),t=Object(i.p)(),r=Object(i.n)(),c=(r.pathname,r.search),y=new URLSearchParams(c),v=T(Object(a.useState)({isAlert:!1,alertTitle:"",alertText:"",severity:""}),2),S=v[0],O=v[1];return n.a.createElement(w.a,{title:"Register"},n.a.createElement(o.a,{sx:{height:"100vh",backgroundImage:"url(/static/img/green_bg.jpg)",paddingTop:"5%",backgroundRepeat:"no-repeat",backgroundSize:"100% 100%"}},n.a.createElement(l.a,{maxWidth:"lg"},n.a.createElement(o.a,{sx:{backgroundColor:"#f7f7f7"}},n.a.createElement(p.AppBar,null),n.a.createElement(o.a,{className:e.mainBlock},S.isAlert?n.a.createElement(d.a,{open:S.isAlert,severity:S.severity,alertTitle:S.alertTitle,alertText:S.alertText,onClose:function(){return O({isAlert:!1,alertTitle:"",alertText:"",severity:""})}}):null,n.a.createElement(o.a,{sx:{width:{xs:"100%",sm:"60%"}}},n.a.createElement(b.b,{initialValues:{firstName:"",lastName:"",gender:"",email:y.get("email"),password:"",passwordConfirmation:"",referralId:y.get("referralId"),role:"CLIENT"},validationSchema:g.d().shape({firstName:g.f().max(255).required("First Name is required"),lastName:g.f().max(255).required("Last Name is required"),gender:g.f().required("Gender is required"),email:g.f().email("Must be a valid email").max(255).required("Email is required"),password:g.f().required("Please enter your password").matches(/^.*(?=.{8,})((?=.*[!@#$%^&*()\-_=+{};:,<.>]){1})(?=.*\d)((?=.*[a-z]){1})((?=.*[A-Z]){1}).*$/,"Password must contain at least 8 characters, one uppercase, one number and one special case character"),passwordConfirmation:g.f().when("password",{is:function(e){return!!(e&&e.length>0)},then:g.f().oneOf([g.e("password")],"Both password need to be the same")})}),onSubmit:function(e,t){var r=t.setSubmitting,a=t.resetForm,n=E.a.signup,i={headers:{"X-CSRFToken":h.a.get("csrftoken")}};x.a.post(n,e,i).then((function(e){200===e.status&&(O({isAlert:!0,alertText:"Your are successfully registered.",severity:"success"}),r(!1),a())})).catch((function(e){if(e.response){var t=e.response.data;O({isAlert:!0,alertText:null==t?void 0:t.message,severity:"error",alertTitle:"Error"}),r(!1)}}))}},(function(e){var t=e.errors,r=e.handleBlur,a=e.handleChange,i=e.handleSubmit,l=e.isSubmitting,c=e.touched,p=e.values;return n.a.createElement("form",{autoComplete:"off",onSubmit:i},n.a.createElement(s.a,{color:"textPrimary",variant:"h4",sx:{marginBottom:"12px"}},"NEW USER REGISTRATION"),n.a.createElement(f.a,{error:Boolean(c.firstName&&t.firstName),fullWidth:!0,helperText:c.firstName&&t.firstName,is_required:!0,attribute:"First Name",margin:"normal",name:"firstName",onBlur:r,onChange:a,value:p.firstName,variant:"outlined"}),n.a.createElement(f.a,{error:Boolean(c.lastName&&t.lastName),fullWidth:!0,helperText:c.lastName&&t.lastName,is_required:!0,attribute:"Last Name",margin:"normal",name:"lastName",onBlur:r,onChange:a,value:p.lastName,variant:"outlined"}),n.a.createElement(f.a,{error:Boolean(c.gender&&t.gender),select:!0,fullWidth:!0,helperText:c.gender&&t.gender,is_required:!0,attribute:"Gender",margin:"normal",name:"gender",onBlur:r,onChange:a,value:p.gender,variant:"outlined"},n.a.createElement(u.a,{value:"MALE"},"Male"),n.a.createElement(u.a,{value:"FEMALE"},"Female"),n.a.createElement(u.a,{value:"Other"},"Other")),n.a.createElement(f.a,{error:Boolean(c.email&&t.email),fullWidth:!0,helperText:c.email&&t.email,is_required:!0,attribute:"Email Address",margin:"normal",name:"email",onBlur:r,onChange:a,type:"email",value:p.email,variant:"outlined"}),n.a.createElement(f.a,{error:Boolean(c.password&&t.password),fullWidth:!0,helperText:c.password&&t.password,is_required:!0,attribute:"Password",margin:"normal",name:"password",onBlur:r,onChange:a,type:"password",value:p.password,variant:"outlined"}),n.a.createElement(f.a,{error:Boolean(c.passwordConfirmation&&t.passwordConfirmation),fullWidth:!0,helperText:c.passwordConfirmation&&t.passwordConfirmation,is_required:!0,attribute:"Confirm Password",margin:"normal",name:"passwordConfirmation",onBlur:r,onChange:a,type:"password",value:p.passwordConfirmation,variant:"outlined"}),n.a.createElement(f.a,{error:Boolean(c.referralId&&t.referralId),fullWidth:!0,helperText:c.referralId&&t.referralId,is_required:!1,attribute:"Referral Id (Optional)",margin:"normal",name:"referralId",onBlur:r,onChange:a,value:p.referralId,variant:"outlined"}),n.a.createElement(o.a,{my:2},n.a.createElement(m.a,{color:"primary",disabled:l,fullWidth:!0,size:"large",type:"submit",variant:"contained"},"Register")))})),n.a.createElement(s.a,{color:"textSecondary",variant:"body1",sx:{textAlign:"center"}},"Have an account?"," ",n.a.createElement(m.a,{component:"span",onClick:function(){return t("/login")}},"Sign in"))))))))}},UFE9:function(e,t,r){"use strict";var a=r("q1tI"),n=r.n(a),i=r("z6Y5"),o=r("NZDO"),l=r("Gqia"),s=r("MGIy"),u=r("17x9"),m=r.n(u),c=["attribute","is_required","attributeTextAlign","attributeMarginTop"];function f(){return f=Object.assign?Object.assign.bind():function(e){for(var t=1;t<arguments.length;t++){var r=arguments[t];for(var a in r)Object.prototype.hasOwnProperty.call(r,a)&&(e[a]=r[a])}return e},f.apply(this,arguments)}function p(e,t){if(null==e)return{};var r,a,n=function(e,t){if(null==e)return{};var r,a,n={},i=Object.keys(e);for(a=0;a<i.length;a++)r=i[a],t.indexOf(r)>=0||(n[r]=e[r]);return n}(e,t);if(Object.getOwnPropertySymbols){var i=Object.getOwnPropertySymbols(e);for(a=0;a<i.length;a++)r=i[a],t.indexOf(r)>=0||Object.prototype.propertyIsEnumerable.call(e,r)&&(n[r]=e[r])}return n}var d=["Middle Initial","Email Address","Password","Email ID (User ID)","Confirm Password","Referral ID (Optional)","Preferrable Time","Time Zone"],g=function(e){var t=e.attribute,r=e.is_required,a=e.attributeTextAlign,u=e.attributeMarginTop,m=p(e,c);return n.a.createElement(i.a,{item:!0,xs:12,sx:{maxHeight:"60px"}},n.a.createElement(i.a,{container:!0},n.a.createElement(i.a,{item:!0,xs:4,sx:{marginTop:u||"24px"}},n.a.createElement(o.a,{sx:{display:"flex",alignItems:"center",marginRight:{xs:0,sm:a?"5px":0},justifyContent:{xs:"flex-start",sm:a?"flex-end":"flex-start"}}},n.a.createElement(l.a,{variant:"body1",sx:{whiteSpace:d.includes(t)?"nowrap":"pre-wrap"}},t),r&&n.a.createElement(l.a,{sx:{color:"red",fontSize:"0.875rem",marginLeft:"3px"}},"*")," :")),n.a.createElement(i.a,{item:!0,xs:"Income Amount"===t?4:8},n.a.createElement(s.a,f({},m,{sx:{"& .MuiOutlinedInput-root":{"& fieldset":{borderRadius:"2px"}},"& .MuiOutlinedInput-root .MuiOutlinedInput-notchedOutline":{border:"0.1px solid #bdbdbd"},"& .MuiOutlinedInput-input":{padding:"10px",backgroundColor:"rgba(255,255,255,1)"},width:"90%"}})))))};g.prototype={is_required:m.a.bool,attribute:m.a.string,attributeTextAlign:m.a.string,attributeMarginTop:m.a.string},t.a=g},uVCN:function(e,t,r){"use strict";var a=r("q1tI"),n=r.n(a),i=r("qhky"),o=r("17x9"),l=r.n(o),s=["children","title"];function u(){return u=Object.assign?Object.assign.bind():function(e){for(var t=1;t<arguments.length;t++){var r=arguments[t];for(var a in r)Object.prototype.hasOwnProperty.call(r,a)&&(e[a]=r[a])}return e},u.apply(this,arguments)}function m(e,t){if(null==e)return{};var r,a,n=function(e,t){if(null==e)return{};var r,a,n={},i=Object.keys(e);for(a=0;a<i.length;a++)r=i[a],t.indexOf(r)>=0||(n[r]=e[r]);return n}(e,t);if(Object.getOwnPropertySymbols){var i=Object.getOwnPropertySymbols(e);for(a=0;a<i.length;a++)r=i[a],t.indexOf(r)>=0||Object.prototype.propertyIsEnumerable.call(e,r)&&(n[r]=e[r])}return n}var c=Object(a.forwardRef)((function(e,t){var r=e.children,a=e.title,o=void 0===a?"":a,l=m(e,s);return n.a.createElement("div",u({ref:t},l),n.a.createElement(i.a,null,n.a.createElement("title",null,o)),r)}));c.propTypes={children:l.a.node.isRequired,title:l.a.string},t.a=c},zfIj:function(e,t,r){"use strict";var a=r("q1tI"),n=r.n(a),i=r("X78M"),o=r("H/m6"),l=r("w+1Z"),s=r("rzlW"),u=r("17x9"),m=r.n(u),c=Object(i.a)((function(e){return{root:{marginTop:e.spacing(10),boxShadow:"-2px 5px 15px -2px rgba(0,0,0,0.71)"},alertContainer:{minWidth:350}}})),f=function(e){var t=e.open,r=e.severity,a=e.alertTitle,i=e.alertText,u=e.onClose,m=c();return n.a.createElement(o.a,{anchorOrigin:{vertical:"top",horizontal:"right"},open:t,autoHideDuration:6e3,onClose:u,className:m.root},n.a.createElement(l.a,{severity:r,onClose:u,className:m.alertContainer},a?n.a.createElement(s.a,null,a):null,i,"!"))};f.prototype={open:m.a.bool,severity:m.a.string,alertText:m.a.string,alertTitle:m.a.string,onClose:m.a.func},t.a=f}}]);
//# sourceMappingURL=RegisterView.js.map