!function(e){function t(t){for(var n,i,l=t[0],c=t[1],u=t[2],s=0,d=[];s<l.length;s++)i=l[s],Object.prototype.hasOwnProperty.call(a,i)&&a[i]&&d.push(a[i][0]),a[i]=0;for(n in c)Object.prototype.hasOwnProperty.call(c,n)&&(e[n]=c[n]);for(p&&p(t);d.length;)d.shift()();return o.push.apply(o,u||[]),r()}function r(){for(var e,t=0;t<o.length;t++){for(var r=o[t],n=!0,l=1;l<r.length;l++){var c=r[l];0!==a[c]&&(n=!1)}n&&(o.splice(t--,1),e=i(i.s=r[0]))}return e}var n={},a={1:0},o=[];function i(t){if(n[t])return n[t].exports;var r=n[t]={i:t,l:!1,exports:{}};return e[t].call(r.exports,r,r.exports,i),r.l=!0,r.exports}i.e=function(e){var t=[],r=a[e];if(0!==r)if(r)t.push(r[2]);else{var n=new Promise((function(t,n){r=a[e]=[t,n]}));t.push(r[2]=n);var o,l=document.createElement("script");l.charset="utf-8",l.timeout=120,i.nc&&l.setAttribute("nonce",i.nc),l.src=function(e){return i.p+""+({2:"RegisterView",3:"ResetPasswordView",4:"home.page",5:"index"}[e]||e)+".js"}(e);var c=new Error;o=function(t){l.onerror=l.onload=null,clearTimeout(u);var r=a[e];if(0!==r){if(r){var n=t&&("load"===t.type?"missing":t.type),o=t&&t.target&&t.target.src;c.message="Loading chunk "+e+" failed.\n("+n+": "+o+")",c.name="ChunkLoadError",c.type=n,c.request=o,r[1](c)}a[e]=void 0}};var u=setTimeout((function(){o({type:"timeout",target:l})}),12e4);l.onerror=l.onload=o,document.head.appendChild(l)}return Promise.all(t)},i.m=e,i.c=n,i.d=function(e,t,r){i.o(e,t)||Object.defineProperty(e,t,{enumerable:!0,get:r})},i.r=function(e){"undefined"!=typeof Symbol&&Symbol.toStringTag&&Object.defineProperty(e,Symbol.toStringTag,{value:"Module"}),Object.defineProperty(e,"__esModule",{value:!0})},i.t=function(e,t){if(1&t&&(e=i(e)),8&t)return e;if(4&t&&"object"==typeof e&&e&&e.__esModule)return e;var r=Object.create(null);if(i.r(r),Object.defineProperty(r,"default",{enumerable:!0,value:e}),2&t&&"string"!=typeof e)for(var n in e)i.d(r,n,function(t){return e[t]}.bind(null,n));return r},i.n=function(e){var t=e&&e.__esModule?function(){return e.default}:function(){return e};return i.d(t,"a",t),t},i.o=function(e,t){return Object.prototype.hasOwnProperty.call(e,t)},i.p="/static/js/",i.oe=function(e){throw console.error(e),e};var l=window.webpackJsonp=window.webpackJsonp||[],c=l.push.bind(l);l.push=t,l=l.slice();for(var u=0;u<l.length;u++)t(l[u]);var p=c;o.push([0,0]),r()}({0:function(e,t,r){r("201c"),e.exports=r("Kme2")},"20nU":function(e,t,r){"use strict";t.a={basename:"",defaultPath:"/app/home",defaultPathID:"home",fontFamily:"Roboto",textTransform:"uppercase",fontSize:15,color:"#474747",backgroundColor:"#fafafa",borderColor:"#ede6df",borderRadius:10,borderRadiusSmall:4,gridSpacing:3,gridSpacingSm:2}},"7QZ+":function(e,t,r){"use strict";t.a={login:"/api/v1/login/",signup:"/api/v1/signup/",logout:"/api/v1/logout/",profile:"/api/v1/profile/",forgotPassword:"/api/v1/forgot-password/",resetPassword:"/api/v1/reset-password/",myServices:"/api/v1/my_services/",choiceData:"/api/v1/choice_data/",taxYears:"/api/v1/tax_years/",taxFiling:"/api/v1/tax_filing/",personalContactDetails:"/api/v1/personal_contact_details/",spouseDetails:"/api/v1/spouse_details",dependantDetails:"/api/v1/dependant_details/",deleteDependant:"/api/v1/delete_dependant/",bankDetails:"/api/v1/bank_details/",incomeDetails:"/api/v1/income_details/",uploadTaxDocs:"/api/v1/upload_tax_docs/",confirmDetails:"/api/v1/confirm_details/",downloadTaxDocsFile:"/api/v1/download_tax_docs/",deleteTaxDocsFile:"/api/v1/delete_tax_docs/",bookAppointment:"/api/v1/book_appointment/",appointmentDetails:"/api/v1/appointment_details/",deleteAppointment:"/api/v1/delete_appointment/",makeReferal:"/api/v1/make_referal/",referalDetails:"/api/v1/referal_details/",templateDownload:"/api/v1/download_template"}},F5OB:function(e,t,r){"use strict";var n=r("q1tI"),a=r("17x9"),o=r.n(a),i=r("/MKj"),l=r("X78M"),c=r("qoR1"),u=r.n(c),p=r("V4z/"),s=r("NZDO"),d=r("PQzt"),m=r("Gqia"),f=r("H9le"),g=r("ZvkB"),x=r("8lqF"),b=r("mkGA"),y=r("T4Ez"),h=r("L9aa"),v=r("gXYC"),E=r("QOiN"),S=r("OGDC"),O=r("5I82"),k=r("6EZ2"),w=r("6KpO"),j=r.n(w),T=r("DAza"),z=r.n(T),C=r("uj0N"),M=r.n(C),P=r("nxaZ"),A=r("7QZ+");function D(e){return D="function"==typeof Symbol&&"symbol"==typeof Symbol.iterator?function(e){return typeof e}:function(e){return e&&"function"==typeof Symbol&&e.constructor===Symbol&&e!==Symbol.prototype?"symbol":typeof e},D(e)}function I(){return I=Object.assign?Object.assign.bind():function(e){for(var t=1;t<arguments.length;t++){var r=arguments[t];for(var n in r)Object.prototype.hasOwnProperty.call(r,n)&&(e[n]=r[n])}return e},I.apply(this,arguments)}function L(e,t){return function(e){if(Array.isArray(e))return e}(e)||function(e,t){var r=null==e?null:"undefined"!=typeof Symbol&&e[Symbol.iterator]||e["@@iterator"];if(null!=r){var n,a,o,i,l=[],c=!0,u=!1;try{if(o=(r=r.call(e)).next,0===t){if(Object(r)!==r)return;c=!1}else for(;!(c=(n=o.call(r)).done)&&(l.push(n.value),l.length!==t);c=!0);}catch(e){u=!0,a=e}finally{try{if(!c&&null!=r.return&&(i=r.return(),Object(i)!==i))return}finally{if(u)throw a}}return l}}(e,t)||function(e,t){if(!e)return;if("string"==typeof e)return _(e,t);var r=Object.prototype.toString.call(e).slice(8,-1);"Object"===r&&e.constructor&&(r=e.constructor.name);if("Map"===r||"Set"===r)return Array.from(e);if("Arguments"===r||/^(?:Ui|I)nt(?:8|16|32)(?:Clamped)?Array$/.test(r))return _(e,t)}(e,t)||function(){throw new TypeError("Invalid attempt to destructure non-iterable instance.\nIn order to be iterable, non-array objects must have a [Symbol.iterator]() method.")}()}function _(e,t){(null==t||t>e.length)&&(t=e.length);for(var r=0,n=new Array(t);r<t;r++)n[r]=e[r];return n}function R(e,t,r){return(t=function(e){var t=function(e,t){if("object"!==D(e)||null===e)return e;var r=e[Symbol.toPrimitive];if(void 0!==r){var n=r.call(e,t||"default");if("object"!==D(n))return n;throw new TypeError("@@toPrimitive must return a primitive value.")}return("string"===t?String:Number)(e)}(e,"string");return"symbol"===D(t)?t:String(t)}(t))in e?Object.defineProperty(e,t,{value:r,enumerable:!0,configurable:!0,writable:!0}):e[t]=r,e}var B=Object(l.a)((function(e){var t;return{mainBlock:{backgroundImage:"url(/static/img/header.png)",backgroundSize:"100% 100%",padding:"10px 0"},logoAvatar:(t={},R(t,e.breakpoints.up("sm"),{marginLeft:"200px",marginRight:"auto"}),R(t,e.breakpoints.down("sm"),{marginLeft:"auto",marginRight:"150px"}),t),account:{display:"flex",flexDirection:"column",alignItems:"center",marginTop:"30px"}}})),W=["HOME","REFER TO EARN","LOGOUT"],F=[j.a,z.a,M.a];function N(e){var t=e.window,r=L(n.useState(!1),2),a=r[0],o=r[1],l=Object(i.c)((function(e){return e.app})),c=B(),w=Object(p.p)(),j=function(){o((function(e){return!e}))};var T=function(e){var t=e;"logout"===t?Object(P.c)(A.a.logout).then((function(e){204===e.status&&(sessionStorage.removeItem("token"),w("/"))})).catch((function(e){console.log("Error",e)})):w("refer to earn"===t?"refer":t)};var z,C=n.createElement(s.a,{onClick:j,sx:{textAlign:"center"}},n.createElement(s.a,{className:c.account},n.createElement(d.a,I({},1==(z=l.first_name+l.last_name).split(" ").length?{children:"".concat(z.split(" ")[0][0])}:{children:"".concat(z.split(" ")[0][0]).concat(z.split(" ")[1][0])},{sx:{width:"75px",height:"75px",fontSize:"24px",color:"white",backgroundColor:"rgb(0,76,153,0.8)"}})),n.createElement(m.a,{className:c.title,variant:"h6",sx:{my:2}},l.first_name+" "+l.last_name)),n.createElement("hr",null),n.createElement(f.a,null,W.map((function(e,t){return n.createElement(g.a,{key:e,disablePadding:!0},n.createElement(x.a,{sx:{textAlign:"start"}},n.createElement(b.a,null,n.createElement(F[t])),n.createElement(y.a,{primary:e,onClick:function(){return T(e.toLowerCase())}})))})))),M=void 0!==t?function(){return t().document.body}:void 0;return n.createElement(s.a,{sx:{display:"flex",justifyContent:"center"}},n.createElement(h.a,null),n.createElement(v.a,{component:"nav",className:c.mainBlock},n.createElement(E.a,null,n.createElement(S.a,{color:"#000000","aria-label":"open drawer",edge:"start",onClick:j,sx:{mr:2,display:{sm:"none"}}},n.createElement(u.a,null)),n.createElement(d.a,{variant:"square",src:"/static/img/onecall-logo.png",sx:{height:42,width:120},className:c.logoAvatar}),n.createElement(s.a,{sx:{display:{xs:"none",sm:"flex"},minWidth:"50%",flexWrap:"wrap",justifyContent:"space-around",marginRight:"80px"}},W.map((function(e,t){return n.createElement(O.a,{key:e,sx:{color:"primary",fontSize:"16px"},onClick:function(){return T(e.toLowerCase())}},n.createElement(F[t],{sx:{marginRight:1}}),e)}))))),n.createElement("nav",null,n.createElement(k.a,{container:M,variant:"temporary",open:a,onClose:j,ModalProps:{keepMounted:!0},sx:{display:{xs:"block",sm:"none"},"& .MuiDrawer-paper":{boxSizing:"border-box",width:240}}},C)),n.createElement(s.a,{component:"main",sx:{p:3}},n.createElement(E.a,null)))}N.propTypes={window:o.a.func}},Kme2:function(e,t,r){"use strict";r.r(t);var n=r("q1tI"),a=r.n(n),o=r("EbEg"),i=r("V4z/"),l=r("4WJT"),c=r("X78M"),u=Object(c.a)((function(e){return{root:{position:"fixed",top:0,left:0,zIndex:1301,width:"100%","& > * + *":{marginTop:e.spacing(2)}}}})),p=function(){var e=u();return a.a.createElement("div",{className:e.root},a.a.createElement(l.a,{color:"primary"}))},s=function(e){return function(t){return a.a.createElement(n.Suspense,{fallback:a.a.createElement(p,null)},a.a.createElement(e,t))}},d=r("nxaZ"),m=r("/MKj"),f=(r("F5OB"),r("7QZ+")),g=r("NZDO"),x=r("yXLF"),b=r("sDGz"),y=r("17x9"),h=r.n(y),v=r("PQzt"),E=r("Gqia"),S=r("H9le"),O=r("ZvkB"),k=r("8lqF"),w=r("mkGA"),j=r("T4Ez"),T=r("WNlj"),z=r("5I82"),C=r("6KpO"),M=r.n(C),P=r("DAza"),A=r.n(P),D=r("uj0N"),I=r.n(D);function L(e){return L="function"==typeof Symbol&&"symbol"==typeof Symbol.iterator?function(e){return typeof e}:function(e){return e&&"function"==typeof Symbol&&e.constructor===Symbol&&e!==Symbol.prototype?"symbol":typeof e},L(e)}function _(){return _=Object.assign?Object.assign.bind():function(e){for(var t=1;t<arguments.length;t++){var r=arguments[t];for(var n in r)Object.prototype.hasOwnProperty.call(r,n)&&(e[n]=r[n])}return e},_.apply(this,arguments)}function R(e,t){return function(e){if(Array.isArray(e))return e}(e)||function(e,t){var r=null==e?null:"undefined"!=typeof Symbol&&e[Symbol.iterator]||e["@@iterator"];if(null!=r){var n,a,o,i,l=[],c=!0,u=!1;try{if(o=(r=r.call(e)).next,0===t){if(Object(r)!==r)return;c=!1}else for(;!(c=(n=o.call(r)).done)&&(l.push(n.value),l.length!==t);c=!0);}catch(e){u=!0,a=e}finally{try{if(!c&&null!=r.return&&(i=r.return(),Object(i)!==i))return}finally{if(u)throw a}}return l}}(e,t)||function(e,t){if(!e)return;if("string"==typeof e)return B(e,t);var r=Object.prototype.toString.call(e).slice(8,-1);"Object"===r&&e.constructor&&(r=e.constructor.name);if("Map"===r||"Set"===r)return Array.from(e);if("Arguments"===r||/^(?:Ui|I)nt(?:8|16|32)(?:Clamped)?Array$/.test(r))return B(e,t)}(e,t)||function(){throw new TypeError("Invalid attempt to destructure non-iterable instance.\nIn order to be iterable, non-array objects must have a [Symbol.iterator]() method.")}()}function B(e,t){(null==t||t>e.length)&&(t=e.length);for(var r=0,n=new Array(t);r<t;r++)n[r]=e[r];return n}function W(e,t,r){return(t=function(e){var t=function(e,t){if("object"!==L(e)||null===e)return e;var r=e[Symbol.toPrimitive];if(void 0!==r){var n=r.call(e,t||"default");if("object"!==L(n))return n;throw new TypeError("@@toPrimitive must return a primitive value.")}return("string"===t?String:Number)(e)}(e,"string");return"symbol"===L(t)?t:String(t)}(t))in e?Object.defineProperty(e,t,{value:r,enumerable:!0,configurable:!0,writable:!0}):e[t]=r,e}var F=Object(c.a)((function(e){var t;return{mainBlock:{backgroundImage:"url(/static/img/header.png)",backgroundSize:"100% 100%",padding:"10px 0"},logoAvatar:(t={},W(t,e.breakpoints.up("sm"),{marginRight:"auto"}),W(t,e.breakpoints.down("sm"),{marginLeft:"auto",marginRight:"150px"}),t),account:{display:"flex",flexDirection:"column",alignItems:"center",marginTop:"30px"}}})),N=["HOME","REFER","LOGOUT"],q=[M.a,A.a,I.a];function H(e){e.window;var t=R(n.useState(!1),2),r=(t[0],t[1]),a=Object(m.c)((function(e){return e.app})),o=F(),l=Object(i.p)();var c=function(e){var t=e;"logout"===t?Object(d.c)(f.a.logout).then((function(e){204===e.status&&(sessionStorage.removeItem("token"),l("/"))})).catch((function(e){console.log("Error",e)})):l("refer to earn"===t?"refer":t)};var u;g.a,g.a,o.account,v.a,_({},1==(u=a.first_name+a.last_name).split(" ").length?{children:"".concat(u.split(" ")[0][0])}:{children:"".concat(u.split(" ")[0][0]).concat(u.split(" ")[1][0])},{sx:{width:"75px",height:"75px",fontSize:"24px",color:"white",backgroundColor:"rgb(0,76,153,0.8)"}}),E.a,o.title,a.first_name,a.last_name,S.a,N.map((function(e,t){return n.createElement(O.a,{key:t,disablePadding:!0},n.createElement(k.a,{sx:{textAlign:"start"}},n.createElement(w.a,null,n.createElement(q[t])),n.createElement(j.a,{primary:e,onClick:function(){return c(e.toLowerCase())}})))}));return n.createElement(g.a,{sx:{marginTop:"10px"}},n.createElement(T.a,{maxWidth:"lg"},n.createElement(g.a,{sx:{display:{xs:"none",sm:"block"}}},n.createElement(g.a,{sx:{display:"flex",justifyContent:"space-between"}},n.createElement(g.a,null,n.createElement(g.a,{sx:{display:"flex"}},n.createElement(v.a,{variant:"square",src:"/static/img/onecall-logo.png",sx:{height:50,width:140,marginBottom:"10px"},className:o.logoAvatar}),n.createElement(E.a,{variant:"h6",sx:{fontSize:"16px",marginTop:"12px",marginLeft:"20px"}},"PERFECT PLACE TO FILE YOUR TAXES")),n.createElement(E.a,{variant:"body2",sx:{fontSize:"16px"}},n.createElement("strong",null,"Phone:")," (248) 971-3300"),n.createElement(E.a,{variant:"body2",sx:{fontSize:"16px"}},n.createElement("strong",null,"E-mail:")," Onecalltaxservices.digital@gmail.com")),n.createElement(v.a,{variant:"square",src:"/static/img/irs_image.jpg",sx:{width:"81px",height:"83px"}})),n.createElement(g.a,{sx:{display:"flex",justifyContent:"space-between",marginTop:"8px"}},n.createElement(E.a,{sx:{color:"rgb(255, 0, 0)"}},n.createElement("strong",null,"BEST WAY TO CONTACT US : PLEASE SEND AN EMAIL TO")," ","onecalltaxservices.digital@gmail.com"),n.createElement(E.a,{sx:{fontSize:"16px"}}," ",n.createElement("strong",null,"Welcome:")," ",a.email))),n.createElement(g.a,{sx:{display:{xs:"block",sm:"none"}}},n.createElement(v.a,{variant:"square",src:"/static/img/onecall-logo.png",sx:{height:50,width:140,marginTop:"12px",marginBottom:"10px"},className:o.logoAvatar}),n.createElement(E.a,{variant:"h6",sx:{fontSize:"16px"}},"PERFECT PLACE TO FILE YOUR TAXES")),n.createElement(g.a,{sx:{display:"flex",justifyContent:"space-between",marginTop:"10px"}},n.createElement(g.a,{sx:{display:"flex"}},n.createElement(z.a,{sx:{fontSize:"14px",fontWeight:"400",marginRight:"30px",maxHeight:"45px",padding:"6px 15px","&:hover":{backgroundColor:"#2069DB",color:"#ffffff"}},onClick:function(){return c("home")},variant:"contained"},"HOME"),n.createElement(z.a,{sx:{fontSize:"14px",fontWeight:"400",marginRight:"30px",maxHeight:"45px",padding:"6px 15px","&:hover":{backgroundColor:"#2069DB",color:"#ffffff"}},onClick:function(){return c("refer to earn")},variant:"contained"},"REFER TO EARN")),n.createElement(g.a,{sx:{alignItems:"end"}},n.createElement(z.a,{sx:{color:"#ffffff",fontSize:"14px",fontWeight:"400",backgroundColor:"red",maxHeight:"30px",padding:"6px 15px","&:hover":{backgroundColor:"lightcoral",color:"#ffffff"}},onClick:function(){return c("logout")}},"LOGOUT"))),n.createElement("hr",null)))}H.propTypes={window:h.a.func};var U=H;function Z(e,t){return function(e){if(Array.isArray(e))return e}(e)||function(e,t){var r=null==e?null:"undefined"!=typeof Symbol&&e[Symbol.iterator]||e["@@iterator"];if(null!=r){var n,a,o,i,l=[],c=!0,u=!1;try{if(o=(r=r.call(e)).next,0===t){if(Object(r)!==r)return;c=!1}else for(;!(c=(n=o.call(r)).done)&&(l.push(n.value),l.length!==t);c=!0);}catch(e){u=!0,a=e}finally{try{if(!c&&null!=r.return&&(i=r.return(),Object(i)!==i))return}finally{if(u)throw a}}return l}}(e,t)||function(e,t){if(!e)return;if("string"==typeof e)return G(e,t);var r=Object.prototype.toString.call(e).slice(8,-1);"Object"===r&&e.constructor&&(r=e.constructor.name);if("Map"===r||"Set"===r)return Array.from(e);if("Arguments"===r||/^(?:Ui|I)nt(?:8|16|32)(?:Clamped)?Array$/.test(r))return G(e,t)}(e,t)||function(){throw new TypeError("Invalid attempt to destructure non-iterable instance.\nIn order to be iterable, non-array objects must have a [Symbol.iterator]() method.")}()}function G(e,t){(null==t||t>e.length)&&(t=e.length);for(var r=0,n=new Array(t);r<t;r++)n[r]=e[r];return n}var Y=Object(c.a)((function(e){return{}})),V=function(){Y();var e=Object(m.c)((function(e){return e.app})).initialAppLoading,t=Object(m.b)(),r=(Object(i.n)(),Z(Object(n.useState)(!0),2)),o=r[0],l=r[1];return Object(n.useEffect)((function(){l(!0),Object(d.b)(f.a.profile).then((function(e){var r=e.status,n=e.data;200===r&&(console.log("data",n),t(Object(b.c)(null==n?void 0:n.data)),l(!1))})).catch((function(e){console.log("Error",e),l(!1)}))}),[]),a.a.createElement(a.a.Fragment,null,!e&&a.a.createElement("div",null,o?a.a.createElement(g.a,{display:"flex",height:"100%",width:"100%",justifyContent:"center",alignItems:"center",sx:{position:"absolute",zIndex:"10",left:0,top:0}},a.a.createElement(x.a,{size:30})):a.a.createElement("div",{style:{position:"relative"}},a.a.createElement(U,null),a.a.createElement(i.b,null))))},X=r("20nU"),K=s(Object(n.lazy)((function(){return Promise.all([r.e(0),r.e(4)]).then(r.bind(null,"JYAV"))}))),Q=s(Object(n.lazy)((function(){return Promise.all([r.e(0),r.e(5)]).then(r.bind(null,"JcIb"))}))),J=s(Object(n.lazy)((function(){return Promise.all([r.e(0),r.e(5)]).then(r.bind(null,"NPtU"))}))),$=s(Object(n.lazy)((function(){return Promise.all([r.e(0),r.e(2)]).then(r.bind(null,"SuzI"))}))),ee=s(Object(n.lazy)((function(){return Promise.all([r.e(0),r.e(5)]).then(r.bind(null,"4/hu"))}))),te=s(Object(n.lazy)((function(){return Promise.all([r.e(0),r.e(3)]).then(r.bind(null,"ZF52"))}))),re=function(){return a.a.createElement(i.e,null,a.a.createElement(i.c,{path:"/",element:a.a.createElement(i.a,{replace:!0,to:X.a.defaultPath})}),a.a.createElement(i.c,{path:"app",element:a.a.createElement(d.a,null,a.a.createElement(V,null))},a.a.createElement(i.c,{path:"home",element:a.a.createElement(K,null)}),a.a.createElement(i.c,{path:"tax-filing/:year/:id/:action",element:a.a.createElement(Q,null)}),a.a.createElement(i.c,{path:"refer",element:a.a.createElement(ee,null)})),a.a.createElement(i.c,{path:"/login",element:a.a.createElement(J,null)}),a.a.createElement(i.c,{path:"/register",element:a.a.createElement($,null)}),a.a.createElement(i.c,{path:"/reset-password/:uidb64/:token",element:a.a.createElement(te,null)}))},ne=r("b4iY"),ae=r("WfXV"),oe=r("L9aa"),ie=r("sD0r"),le=function(e){return{MuiPaper:{defaultProps:{elevation:0},styleOverrides:{root:{backgroundImage:"none"},rounded:{borderRadius:e.customization.borderRadius+"px"}}},MuiButton:{styleOverrides:{sizeMedium:{paddingTop:"8px",paddingBottom:"9px"}}},MuiTableCell:{styleOverrides:{root:{borderColor:"#e7ddd1",padding:"18px 15px"}}},MuiTablePagination:{styleOverrides:{root:{borderTop:"1px solid ".concat(e.customization.borderColor)},selectLabel:{marginTop:0,marginBottom:0},displayedRows:{marginTop:0,marginBottom:0},toolbar:{paddingTop:"5px"}}},MuiAppBar:{styleOverrides:{root:{padding:"5px 0",boxShadow:"rgb(0 0 0 / 6%) 0px 3px 8px"}}},MuiCardHeader:{styleOverrides:{root:{color:e.colors.textDark,padding:"24px"},title:{fontSize:"1.125rem"}}},MuiCardContent:{styleOverrides:{root:{padding:"24px"}}},MuiCardActions:{styleOverrides:{root:{padding:"24px"}}},MuiListItemButton:{styleOverrides:{root:{color:e.darkTextPrimary,paddingTop:"10px",paddingBottom:"10px","&.Mui-selected":{color:e.menuSelected,backgroundColor:e.menuSelectedBack,"&:hover":{backgroundColor:e.menuSelectedBack},"& .MuiListItemIcon-root":{color:e.menuSelected}},"&:hover":{backgroundColor:e.menuSelectedBack,color:e.menuSelected,"& .MuiListItemIcon-root":{color:e.menuSelected}}}}},MuiListItemIcon:{styleOverrides:{root:{color:e.darkTextPrimary,minWidth:"36px"}}},MuiListItemText:{styleOverrides:{primary:{color:e.textDark}}},MuiInputBase:{styleOverrides:{input:{color:e.textDark,"&::placeholder":{color:e.darkTextSecondary}}}},MuiOutlinedInput:{styleOverrides:{root:{background:e.colors.grey50,borderRadius:e.customization.borderRadius+"px","& .MuiOutlinedInput-notchedOutline":{borderColor:e.colors.grey400},"&:hover $notchedOutline":{borderColor:e.colors.primaryLight},"&.MuiInputBase-multiline":{padding:1}},input:{fontWeight:500,background:e.colors.grey50,padding:"15.5px 14px",borderRadius:e.customization.borderRadius+"px","&.MuiInputBase-inputSizeSmall":{padding:"10px 14px","&.MuiInputBase-inputAdornedStart":{paddingLeft:0}}},inputAdornedStart:{paddingLeft:4},notchedOutline:{borderRadius:e.customization.borderRadius+"px"}}},MuiSlider:{styleOverrides:{root:{"&.Mui-disabled":{color:e.colors.grey300}},mark:{backgroundColor:e.paper,width:"4px"},valueLabel:{color:e.colors.primaryLight}}},MuiDivider:{styleOverrides:{root:{borderColor:e.divider,opacity:1}}},MuiAvatar:{styleOverrides:{root:{color:e.colors.primaryMain,background:e.colors.primary100}}},MuiChip:{styleOverrides:{root:{"&.MuiChip-deletable .MuiChip-deleteIcon":{color:"inherit"}}}},MuiTooltip:{styleOverrides:{tooltip:{color:e.paper,background:e.colors.grey700}}},MuiMenuItem:{styleOverrides:{root:{minHeight:"25px"}}},MuiDialogTitle:{styleOverrides:{root:{fontWeight:600,fontSize:"16px",lineHeight:"22px",color:e.colors.primaryMain}}},MuiAutocomplete:{styleOverrides:{root:{position:"relative"},tag:{maxWidth:"100px"}}}}},ce={paper:"#ffffff",darkPaper:"#000000",primaryLight:"#4c87df",primaryMain:"#2069D8",primaryDark:"#164997",primary200:"#91cfff",primary800:"#206ad8",secondaryLight:"#f7b74f",secondaryMain:"#F5A623",secondaryDark:"#ab7418",secondary200:"#fdf39b",secondary800:"#f5a523",successLight:"#81c784",successMain:"#2e7d32",successDark:"#1b5e20",success200:"#a5d6a7",success800:"#859303",errorLight:"#ef9a9a",errorMain:"#f44336",errorDark:"#c62828",orangeLight:"#fbe9e7",orangeMain:"#ffab91",orangeDark:"#d84315",warningLight:"#fff8e1",warningMain:"#ffe57f",warningDark:"#ffc107",grey50:"#fafafa",grey100:"#f5f5f5",grey200:"#eeeeee",grey300:"#e0e0e0",grey400:"#bdbdbd",grey500:"#9e9e9e",grey600:"#757575",grey700:"#616161",grey800:"#333333",grey900:"#212121"},ue=function(e){return{common:{black:e.colors.darkPaper,white:e.colors.paper},primary:{main:e.colors.primaryMain,light:e.colors.primaryLight,dark:e.colors.primaryDark},secondary:{main:e.colors.secondaryMain,light:e.colors.secondaryLight,dark:e.colors.secondaryDark},error:{main:e.colors.errorMain,light:e.colors.errorLight,dark:e.colors.errorDark},warning:{main:e.colors.warningMain,light:e.colors.warningLight,dark:e.colors.warningDark},success:{main:e.colors.successMain,light:e.colors.successLight,dark:e.colors.successDark},grey:{50:e.colors.grey50,100:e.colors.grey100,500:e.colors.grey500,600:e.colors.grey600,700:e.colors.grey700,800:e.colors.grey800,900:e.colors.grey900},text:{primary:e.darkTextPrimary,secondary:e.darkTextSecondary},background:{paper:e.colors.paper,default:e.backgroundDefault},action:{hover:e.customization.backgroundColor,focus:e.colors.secondaryDark}}},pe=function(e){return{fontFamily:e.customization.fontFamily,fontSize:e.customization.fontSize,h6:{fontWeight:500,color:e.heading,fontSize:"0.75rem",letterSpacing:"0.2px"},h5:{fontSize:"0.875rem",color:e.heading,fontWeight:500,letterSpacing:"0.2px"},h4:{fontSize:"1rem",color:e.heading,fontWeight:600,letterSpacing:"0.2px"},h3:{fontSize:"1.25rem",color:e.heading,fontWeight:600,letterSpacing:"0.2px"},h2:{fontSize:"1.5rem",color:e.heading,fontWeight:700,letterSpacing:"0.2px"},h1:{fontSize:"2.125rem",color:e.heading,fontWeight:700,letterSpacing:"0.2px"},subtitle1:{fontSize:"0.875rem",fontWeight:500,color:e.textDark,letterSpacing:"0.2px"},subtitle2:{fontSize:"0.75rem",fontWeight:400,color:e.darkTextSecondary,letterSpacing:"0.2px"},caption:{fontSize:"0.75rem",color:e.darkTextSecondary,fontWeight:400},body1:{fontSize:"0.875rem",fontWeight:400,lineHeight:"1.334em"},body2:{fontWeight:400,lineHeight:"1.5em",color:e.darkTextPrimary},button:{textTransform:"capitalize"},customInput:{marginTop:8,marginBottom:8,"& > label":{top:"23px",left:0,color:e.grey500,'&[data-shrink="false"]':{top:"5px"}},"& > div > input":{padding:"30.5px 14px 11.5px !important"},"& legend":{display:"none"},"& fieldset":{top:0}},mainContent:{backgroundColor:"#f7f6f6",width:"100%",minHeight:"calc(100vh - 88px)",flexGrow:1,padding:"20px",marginTop:"88px",marginRight:"20px",letterSpacing:"0.2px",borderRadius:e.customization.borderRadius+"px"},menuCaption:{fontSize:"0.875rem",fontWeight:500,color:e.heading,padding:"6px",textTransform:"capitalize",marginTop:"10px"},subMenuCaption:{fontSize:"0.6875rem",fontWeight:500,color:e.darkTextSecondary,textTransform:"capitalize"},commonAvatar:{cursor:"pointer",borderRadius:"8px"},smallAvatar:{width:"22px",height:"22px",fontSize:"1rem"},mediumAvatar:{width:"34px",height:"34px",fontSize:"1.2rem"},largeAvatar:{width:"44px",height:"44px",fontSize:"1.5rem"}}},se=function(){var e={colors:ce,heading:ce.grey900,paper:ce.paper,backgroundDefault:X.a.backgroundColor,darkTextPrimary:ce.grey800,darkTextSecondary:ce.grey800,textDark:ce.grey900,menuSelected:ce.secondaryDark,menuSelectedBack:ce.secondaryLight,divider:X.a.borderColor,customization:X.a};return Object(ie.a)({direction:"ltr",breakpoints:{values:{xs:0,sm:768,md:1024,lg:1280,xl:1400}},components:le(e),palette:ue(e),typography:pe(e),shadows:["rgba(99, 99, 99, 0.2) 0px 2px 8px 0px","rgba(0, 0, 0, 0.2) 0px 3px 9px","rgba(0, 0, 0, 0.2) 0px 3px 9px","rgba(0, 0, 0, 0.2) 0px 3px 9px","rgba(0, 0, 0, 0.2) 0px 3px 9px","rgba(0, 0, 0, 0.2) 0px 3px 9px","rgba(0, 0, 0, 0.2) 0px 3px 9px","rgba(0, 0, 0, 0.2) 0px 3px 9px","rgba(17, 17, 26, 0.09) 0px 4px 16px, rgba(17, 17, 26, 0.09) 0px 8px 32px","rgba(0, 0, 0, 0.2) 0px 3px 9px","rgba(0, 0, 0, 0.2) 0px 3px 9px","rgba(0, 0, 0, 0.2) 0px 3px 9px","rgba(0, 0, 0, 0.2) 0px 3px 9px","rgba(0, 0, 0, 0.2) 0px 3px 9px","rgba(0, 0, 0, 0.2) 0px 3px 9px","rgba(0, 0, 0, 0.2) 0px 3px 9px","rgba(0, 0, 0, 0.2) 0px 3px 9px","rgba(0, 0, 0, 0.2) 0px 3px 9px","rgba(0, 0, 0, 0.2) 0px 3px 9px","rgba(0, 0, 0, 0.2) 0px 3px 9px","rgba(0, 0, 0, 0.2) 0px 3px 9px","rgba(0, 0, 0, 0.2) 0px 3px 9px","rgba(0, 0, 0, 0.2) 0px 3px 9px","rgba(0, 0, 0, 0.2) 0px 3px 9px","rgba(0, 0, 0, 0.2) 0px 3px 9px"]})},de=function(){return a.a.createElement(ae.a,{injectFirst:!0},a.a.createElement(ne.a,{theme:se()},a.a.createElement(oe.a,null),a.a.createElement(re,null)))},me=(r("+eM2"),r("SOjZ")),fe=r("i7Pf"),ge=Object(fe.a)({reducer:{app:b.a},middleware:function(e){return e()}}),xe=document.getElementById("root");Object(o.createRoot)(xe).render(a.a.createElement(m.a,{store:ge},a.a.createElement(me.a,null,a.a.createElement(de,null))))},nxaZ:function(e,t,r){"use strict";r.d(t,"c",(function(){return s})),r.d(t,"b",(function(){return d}));var n=r("q1tI"),a=r.n(n),o=r("V4z/"),i=r("vDqi"),l=r.n(i);function c(e){return c="function"==typeof Symbol&&"symbol"==typeof Symbol.iterator?function(e){return typeof e}:function(e){return e&&"function"==typeof Symbol&&e.constructor===Symbol&&e!==Symbol.prototype?"symbol":typeof e},c(e)}function u(e,t){var r=Object.keys(e);if(Object.getOwnPropertySymbols){var n=Object.getOwnPropertySymbols(e);t&&(n=n.filter((function(t){return Object.getOwnPropertyDescriptor(e,t).enumerable}))),r.push.apply(r,n)}return r}function p(e,t,r){return(t=function(e){var t=function(e,t){if("object"!==c(e)||null===e)return e;var r=e[Symbol.toPrimitive];if(void 0!==r){var n=r.call(e,t||"default");if("object"!==c(n))return n;throw new TypeError("@@toPrimitive must return a primitive value.")}return("string"===t?String:Number)(e)}(e,"string");return"symbol"===c(t)?t:String(t)}(t))in e?Object.defineProperty(e,t,{value:r,enumerable:!0,configurable:!0,writable:!0}):e[t]=r,e}t.a=function(e){var t=e.children;return!!sessionStorage.getItem("token")?t:a.a.createElement(o.a,{to:"/login"})};var s=function(e){var t=arguments.length>1&&void 0!==arguments[1]?arguments[1]:{},r=arguments.length>2&&void 0!==arguments[2]?arguments[2]:{},n=sessionStorage.getItem("token");return l()(function(e){for(var t=1;t<arguments.length;t++){var r=null!=arguments[t]?arguments[t]:{};t%2?u(Object(r),!0).forEach((function(t){p(e,t,r[t])})):Object.getOwnPropertyDescriptors?Object.defineProperties(e,Object.getOwnPropertyDescriptors(r)):u(Object(r)).forEach((function(t){Object.defineProperty(e,t,Object.getOwnPropertyDescriptor(r,t))}))}return e}({method:"POST",url:e,headers:{"Content-Type":"application/json",Authorization:"Token ".concat(n)},data:t},r))},d=function(e){var t=sessionStorage.getItem("token");return l()({method:"GET",url:e,headers:{"Content-Type":"application/json",Authorization:"Token ".concat(t)}})}},sDGz:function(e,t,r){"use strict";r.d(t,"b",(function(){return i})),r.d(t,"c",(function(){return l}));var n=r("i7Pf"),a=Object(n.b)({name:"app",initialState:{},reducers:{setTaxYear:function(e,t){e.taxYear=t.payload},setUserInfo:function(e,t){var r=t.payload,n=r.first_name,a=r.last_name,o=r.email,i=r.phone_no,l=r.gender,c=r.address;e.first_name=n,e.last_name=a,e.phone_no=i,e.email=o,e.gender=l,e.address=c}}}),o=a.actions,i=o.setTaxYear,l=o.setUserInfo;t.a=a.reducer}});
//# sourceMappingURL=main.js.map