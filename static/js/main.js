!function(e){function t(t){for(var n,i,l=t[0],c=t[1],p=t[2],s=0,d=[];s<l.length;s++)i=l[s],Object.prototype.hasOwnProperty.call(o,i)&&o[i]&&d.push(o[i][0]),o[i]=0;for(n in c)Object.prototype.hasOwnProperty.call(c,n)&&(e[n]=c[n]);for(u&&u(t);d.length;)d.shift()();return a.push.apply(a,p||[]),r()}function r(){for(var e,t=0;t<a.length;t++){for(var r=a[t],n=!0,l=1;l<r.length;l++){var c=r[l];0!==o[c]&&(n=!1)}n&&(a.splice(t--,1),e=i(i.s=r[0]))}return e}var n={},o={1:0},a=[];function i(t){if(n[t])return n[t].exports;var r=n[t]={i:t,l:!1,exports:{}};return e[t].call(r.exports,r,r.exports,i),r.l=!0,r.exports}i.e=function(e){var t=[],r=o[e];if(0!==r)if(r)t.push(r[2]);else{var n=new Promise((function(t,n){r=o[e]=[t,n]}));t.push(r[2]=n);var a,l=document.createElement("script");l.charset="utf-8",l.timeout=120,i.nc&&l.setAttribute("nonce",i.nc),l.src=function(e){return i.p+""+({2:"LoginView",3:"RegisterView",4:"ResetPasswordView",5:"index",6:"profile.page"}[e]||e)+".js"}(e);var c=new Error;a=function(t){l.onerror=l.onload=null,clearTimeout(p);var r=o[e];if(0!==r){if(r){var n=t&&("load"===t.type?"missing":t.type),a=t&&t.target&&t.target.src;c.message="Loading chunk "+e+" failed.\n("+n+": "+a+")",c.name="ChunkLoadError",c.type=n,c.request=a,r[1](c)}o[e]=void 0}};var p=setTimeout((function(){a({type:"timeout",target:l})}),12e4);l.onerror=l.onload=a,document.head.appendChild(l)}return Promise.all(t)},i.m=e,i.c=n,i.d=function(e,t,r){i.o(e,t)||Object.defineProperty(e,t,{enumerable:!0,get:r})},i.r=function(e){"undefined"!=typeof Symbol&&Symbol.toStringTag&&Object.defineProperty(e,Symbol.toStringTag,{value:"Module"}),Object.defineProperty(e,"__esModule",{value:!0})},i.t=function(e,t){if(1&t&&(e=i(e)),8&t)return e;if(4&t&&"object"==typeof e&&e&&e.__esModule)return e;var r=Object.create(null);if(i.r(r),Object.defineProperty(r,"default",{enumerable:!0,value:e}),2&t&&"string"!=typeof e)for(var n in e)i.d(r,n,function(t){return e[t]}.bind(null,n));return r},i.n=function(e){var t=e&&e.__esModule?function(){return e.default}:function(){return e};return i.d(t,"a",t),t},i.o=function(e,t){return Object.prototype.hasOwnProperty.call(e,t)},i.p="/static/js/",i.oe=function(e){throw console.error(e),e};var l=window.webpackJsonp=window.webpackJsonp||[],c=l.push.bind(l);l.push=t,l=l.slice();for(var p=0;p<l.length;p++)t(l[p]);var u=c;a.push([0,0]),r()}({0:function(e,t,r){r("201c"),e.exports=r("Kme2")},"20nU":function(e,t,r){"use strict";t.a={basename:"",defaultPath:"/app/profile",defaultPathID:"home",fontFamily:"Roboto",textTransform:"uppercase",fontSize:15,color:"#474747",backgroundColor:"#fafafa",borderColor:"#ede6df",borderRadius:10,borderRadiusSmall:4,gridSpacing:3,gridSpacingSm:2}},"7QZ+":function(e,t,r){"use strict";t.a={login:"/api/v1/login/",signup:"/api/v1/signup/",logout:"/api/v1/logout/",profile:"/api/v1/profile/",forgotPassword:"/api/v1/forgot-password/",resetPassword:"/api/v1/reset-password/",myServices:"/api/v1/my_services/",choiceData:"/api/v1/choice_data/",taxYears:"/api/v1/tax_years/",taxFiling:"/api/v1/tax_filing/",personalContactDetails:"/api/v1/personal_contact_details/",spouseDetails:"/api/v1/spouse_details",dependantDetails:"/api/v1/dependant_details/",bankDetails:"/api/v1/bank_details/",incomeDetails:"/api/v1/income_details/",uploadTaxDocs:"/api/v1/upload_tax_docs/",confirmDetails:"/api/v1/confirm_details/",downloadTaxDocsFile:"/api/v1/download_tax_docs/",deleteTaxDocsFile:"/api/v1/delete_tax_docs/",bookAppointment:"/api/v1/book_appointment/",appointmentDetails:"/api/v1/appointment_details/",deleteAppointment:"/api/v1/delete_appointment/",makeReferal:"/api/v1/make_referal/",referalDetails:"/api/v1/referal_details/"}},Kme2:function(e,t,r){"use strict";r.r(t);var n=r("q1tI"),o=r.n(n),a=r("EbEg"),i=r("V4z/"),l=r("4WJT"),c=r("X78M"),p=Object(c.a)((function(e){return{root:{position:"fixed",top:0,left:0,zIndex:1301,width:"100%","& > * + *":{marginTop:e.spacing(2)}}}})),u=function(){var e=p();return o.a.createElement("div",{className:e.root},o.a.createElement(l.a,{color:"primary"}))},s=function(e){return function(t){return o.a.createElement(n.Suspense,{fallback:o.a.createElement(u,null)},o.a.createElement(e,t))}},d=r("nxaZ"),m=r("/MKj"),f=r("NZDO"),g=(r("z6Y5"),r("PQzt")),b=r("5I82"),x=(Object(c.a)((function(e){return{mainBlock:{backgroundImage:"url(/static/img/header.png)",backgroundSize:"100% 100%",padding:"20px 0"},logoAvatar:{marginLeft:"auto",marginRight:"auto",height:"42px",width:"120px"}}})),r("17x9")),y=r.n(x),h=r("qoR1"),v=r.n(h),k=r("Gqia"),S=r("H9le"),O=r("ZvkB"),E=r("8lqF"),w=r("mkGA"),j=r("T4Ez"),z=r("L9aa"),M=r("gXYC"),P=r("QOiN"),T=r("OGDC"),D=r("6EZ2"),C=r("DAza"),I=r.n(C),L=r("uj0N"),A=r.n(L),R=r("yGo1"),_=r.n(R),B=r("7QZ+");function W(e){return W="function"==typeof Symbol&&"symbol"==typeof Symbol.iterator?function(e){return typeof e}:function(e){return e&&"function"==typeof Symbol&&e.constructor===Symbol&&e!==Symbol.prototype?"symbol":typeof e},W(e)}function F(){return F=Object.assign?Object.assign.bind():function(e){for(var t=1;t<arguments.length;t++){var r=arguments[t];for(var n in r)Object.prototype.hasOwnProperty.call(r,n)&&(e[n]=r[n])}return e},F.apply(this,arguments)}function N(e,t){return function(e){if(Array.isArray(e))return e}(e)||function(e,t){var r=null==e?null:"undefined"!=typeof Symbol&&e[Symbol.iterator]||e["@@iterator"];if(null!=r){var n,o,a,i,l=[],c=!0,p=!1;try{if(a=(r=r.call(e)).next,0===t){if(Object(r)!==r)return;c=!1}else for(;!(c=(n=a.call(r)).done)&&(l.push(n.value),l.length!==t);c=!0);}catch(e){p=!0,o=e}finally{try{if(!c&&null!=r.return&&(i=r.return(),Object(i)!==i))return}finally{if(p)throw o}}return l}}(e,t)||function(e,t){if(!e)return;if("string"==typeof e)return Z(e,t);var r=Object.prototype.toString.call(e).slice(8,-1);"Object"===r&&e.constructor&&(r=e.constructor.name);if("Map"===r||"Set"===r)return Array.from(e);if("Arguments"===r||/^(?:Ui|I)nt(?:8|16|32)(?:Clamped)?Array$/.test(r))return Z(e,t)}(e,t)||function(){throw new TypeError("Invalid attempt to destructure non-iterable instance.\nIn order to be iterable, non-array objects must have a [Symbol.iterator]() method.")}()}function Z(e,t){(null==t||t>e.length)&&(t=e.length);for(var r=0,n=new Array(t);r<t;r++)n[r]=e[r];return n}function G(e,t,r){return(t=function(e){var t=function(e,t){if("object"!==W(e)||null===e)return e;var r=e[Symbol.toPrimitive];if(void 0!==r){var n=r.call(e,t||"default");if("object"!==W(n))return n;throw new TypeError("@@toPrimitive must return a primitive value.")}return("string"===t?String:Number)(e)}(e,"string");return"symbol"===W(t)?t:String(t)}(t))in e?Object.defineProperty(e,t,{value:r,enumerable:!0,configurable:!0,writable:!0}):e[t]=r,e}var q=Object(c.a)((function(e){var t;return{mainBlock:{backgroundImage:"url(/static/img/header.png)",backgroundSize:"100% 100%",padding:"10px 0"},logoAvatar:(t={},G(t,e.breakpoints.up("sm"),{marginLeft:"200px",marginRight:"auto"}),G(t,e.breakpoints.down("sm"),{marginLeft:"auto",marginRight:"150px"}),t),account:{display:"flex",flexDirection:"column",alignItems:"center",marginTop:"30px"}}})),H=["PROFILE","REFER","LOGOUT"],K=[_.a,I.a,A.a];function Y(e){var t=e.window,r=N(n.useState(!1),2),o=r[0],a=r[1],l=q(),c=Object(i.p)(),p=function(){a((function(e){return!e}))};var u,s=function(e){var t=e;"logout"===t?Object(d.c)(B.a.logout).then((function(e){204===e.status&&(sessionStorage.removeItem("token"),c("/"))})).catch((function(e){console.log("Error",e)})):c(t)},m=n.createElement(f.a,{onClick:p,sx:{textAlign:"center"}},n.createElement(f.a,{className:l.account},n.createElement(g.a,F({},1===(u="Kuntolla Pavan Kumar").split(" ").length?{children:"".concat(u.split(" ")[0][0])}:{children:"".concat(u.split(" ")[0][0]).concat(u.split(" ")[1][0])},{sx:{width:"75px",height:"75px",fontSize:"24px",color:"white",backgroundColor:"rgb(0,76,153,0.8)"}})),n.createElement(k.a,{className:l.title,variant:"h6",sx:{my:2}},"Kuntolla Pavan Kumar")),n.createElement("hr",null),n.createElement(S.a,null,H.map((function(e,t){return n.createElement(O.a,{key:e,disablePadding:!0},n.createElement(E.a,{sx:{textAlign:"start"}},n.createElement(w.a,null,n.createElement(K[t])),n.createElement(j.a,{primary:e,onClick:function(){return s(e.toLowerCase())}})))})))),x=void 0!==t?function(){return t().document.body}:void 0;return n.createElement(f.a,{sx:{display:"flex",justifyContent:"center"}},n.createElement(z.a,null),n.createElement(M.a,{component:"nav",className:l.mainBlock},n.createElement(P.a,null,n.createElement(T.a,{color:"#000000","aria-label":"open drawer",edge:"start",onClick:p,sx:{mr:2,display:{sm:"none"}}},n.createElement(v.a,null)),n.createElement(g.a,{variant:"square",src:"/static/img/onecall-logo.png",sx:{height:42,width:120},className:l.logoAvatar}),n.createElement(f.a,{sx:{display:{xs:"none",sm:"flex"},minWidth:"50%",flexWrap:"wrap",justifyContent:"space-around",marginRight:"80px"}},H.map((function(e,t){return n.createElement(b.a,{key:e,sx:{color:"primary",fontSize:"16px"},onClick:function(){return s(e.toLowerCase())}},n.createElement(K[t],{sx:{marginRight:1}}),e)}))))),n.createElement("nav",null,n.createElement(D.a,{container:x,variant:"temporary",open:o,onClose:p,ModalProps:{keepMounted:!0},sx:{display:{xs:"block",sm:"none"},"& .MuiDrawer-paper":{boxSizing:"border-box",width:240}}},m)),n.createElement(f.a,{component:"main",sx:{p:3}},n.createElement(P.a,null)))}Y.propTypes={window:y.a.func};var V=Y,J=Object(c.a)((function(e){return{}})),Q=function(){J();var e=Object(m.c)((function(e){return e.app})).initialAppLoading;Object(m.b)(),Object(i.n)();return o.a.createElement(o.a.Fragment,null,!e&&o.a.createElement("div",null,o.a.createElement("div",{style:{position:"relative"}},o.a.createElement(V,null),o.a.createElement(i.b,null))))},U=r("20nU"),X=s(Object(n.lazy)((function(){return Promise.all([r.e(0),r.e(5)]).then(r.bind(null,"JcIb"))}))),$=s(Object(n.lazy)((function(){return Promise.all([r.e(0),r.e(2)]).then(r.bind(null,"1ZOe"))}))),ee=s(Object(n.lazy)((function(){return Promise.all([r.e(0),r.e(3)]).then(r.bind(null,"SuzI"))}))),te=s(Object(n.lazy)((function(){return Promise.all([r.e(0),r.e(6)]).then(r.bind(null,"2C1f"))}))),re=s(Object(n.lazy)((function(){return Promise.all([r.e(0),r.e(5)]).then(r.bind(null,"4/hu"))}))),ne=s(Object(n.lazy)((function(){return Promise.all([r.e(0),r.e(4)]).then(r.bind(null,"ZF52"))}))),oe=function(){return o.a.createElement(i.e,null,o.a.createElement(i.c,{path:"/",element:o.a.createElement(i.a,{replace:!0,to:U.a.defaultPath})}),o.a.createElement(i.c,{path:"app",element:o.a.createElement(d.a,null,o.a.createElement(Q,null))},o.a.createElement(i.c,{path:"tax-filing/:year/:id/:action",element:o.a.createElement(X,null)}),o.a.createElement(i.c,{path:"profile",element:o.a.createElement(te,null)}),o.a.createElement(i.c,{path:"refer",element:o.a.createElement(re,null)})),o.a.createElement(i.c,{path:"/login",element:o.a.createElement($,null)}),o.a.createElement(i.c,{path:"/register",element:o.a.createElement(ee,null)}),o.a.createElement(i.c,{path:"/reset-password/:uidb64/:token",element:o.a.createElement(ne,null)}))},ae=r("b4iY"),ie=r("WfXV"),le=r("sD0r"),ce=function(e){return{MuiPaper:{defaultProps:{elevation:0},styleOverrides:{root:{backgroundImage:"none"},rounded:{borderRadius:e.customization.borderRadius+"px"}}},MuiButton:{styleOverrides:{sizeMedium:{paddingTop:"8px",paddingBottom:"9px"}}},MuiTableCell:{styleOverrides:{root:{borderColor:"#e7ddd1",padding:"18px 15px"}}},MuiTablePagination:{styleOverrides:{root:{borderTop:"1px solid ".concat(e.customization.borderColor)},selectLabel:{marginTop:0,marginBottom:0},displayedRows:{marginTop:0,marginBottom:0},toolbar:{paddingTop:"5px"}}},MuiAppBar:{styleOverrides:{root:{padding:"5px 0",boxShadow:"rgb(0 0 0 / 6%) 0px 3px 8px"}}},MuiCardHeader:{styleOverrides:{root:{color:e.colors.textDark,padding:"24px"},title:{fontSize:"1.125rem"}}},MuiCardContent:{styleOverrides:{root:{padding:"24px"}}},MuiCardActions:{styleOverrides:{root:{padding:"24px"}}},MuiListItemButton:{styleOverrides:{root:{color:e.darkTextPrimary,paddingTop:"10px",paddingBottom:"10px","&.Mui-selected":{color:e.menuSelected,backgroundColor:e.menuSelectedBack,"&:hover":{backgroundColor:e.menuSelectedBack},"& .MuiListItemIcon-root":{color:e.menuSelected}},"&:hover":{backgroundColor:e.menuSelectedBack,color:e.menuSelected,"& .MuiListItemIcon-root":{color:e.menuSelected}}}}},MuiListItemIcon:{styleOverrides:{root:{color:e.darkTextPrimary,minWidth:"36px"}}},MuiListItemText:{styleOverrides:{primary:{color:e.textDark}}},MuiInputBase:{styleOverrides:{input:{color:e.textDark,"&::placeholder":{color:e.darkTextSecondary}}}},MuiOutlinedInput:{styleOverrides:{root:{background:e.colors.grey50,borderRadius:e.customization.borderRadius+"px","& .MuiOutlinedInput-notchedOutline":{borderColor:e.colors.grey400},"&:hover $notchedOutline":{borderColor:e.colors.primaryLight},"&.MuiInputBase-multiline":{padding:1}},input:{fontWeight:500,background:e.colors.grey50,padding:"15.5px 14px",borderRadius:e.customization.borderRadius+"px","&.MuiInputBase-inputSizeSmall":{padding:"10px 14px","&.MuiInputBase-inputAdornedStart":{paddingLeft:0}}},inputAdornedStart:{paddingLeft:4},notchedOutline:{borderRadius:e.customization.borderRadius+"px"}}},MuiSlider:{styleOverrides:{root:{"&.Mui-disabled":{color:e.colors.grey300}},mark:{backgroundColor:e.paper,width:"4px"},valueLabel:{color:e.colors.primaryLight}}},MuiDivider:{styleOverrides:{root:{borderColor:e.divider,opacity:1}}},MuiAvatar:{styleOverrides:{root:{color:e.colors.primaryMain,background:e.colors.primary100}}},MuiChip:{styleOverrides:{root:{"&.MuiChip-deletable .MuiChip-deleteIcon":{color:"inherit"}}}},MuiTooltip:{styleOverrides:{tooltip:{color:e.paper,background:e.colors.grey700}}},MuiMenuItem:{styleOverrides:{root:{minHeight:"25px"}}},MuiDialogTitle:{styleOverrides:{root:{fontWeight:600,fontSize:"16px",lineHeight:"22px",color:e.colors.primaryMain}}},MuiAutocomplete:{styleOverrides:{root:{position:"relative"},tag:{maxWidth:"100px"}}}}},pe={paper:"#ffffff",darkPaper:"#000000",primaryLight:"#4c87df",primaryMain:"#2069D8",primaryDark:"#164997",primary200:"#91cfff",primary800:"#206ad8",secondaryLight:"#f7b74f",secondaryMain:"#F5A623",secondaryDark:"#ab7418",secondary200:"#fdf39b",secondary800:"#f5a523",successLight:"#81c784",successMain:"#2e7d32",successDark:"#1b5e20",success200:"#a5d6a7",success800:"#859303",errorLight:"#ef9a9a",errorMain:"#f44336",errorDark:"#c62828",orangeLight:"#fbe9e7",orangeMain:"#ffab91",orangeDark:"#d84315",warningLight:"#fff8e1",warningMain:"#ffe57f",warningDark:"#ffc107",grey50:"#fafafa",grey100:"#f5f5f5",grey200:"#eeeeee",grey300:"#e0e0e0",grey400:"#bdbdbd",grey500:"#9e9e9e",grey600:"#757575",grey700:"#616161",grey800:"#333333",grey900:"#212121"},ue=function(e){return{common:{black:e.colors.darkPaper,white:e.colors.paper},primary:{main:e.colors.primaryMain,light:e.colors.primaryLight,dark:e.colors.primaryDark},secondary:{main:e.colors.secondaryMain,light:e.colors.secondaryLight,dark:e.colors.secondaryDark},error:{main:e.colors.errorMain,light:e.colors.errorLight,dark:e.colors.errorDark},warning:{main:e.colors.warningMain,light:e.colors.warningLight,dark:e.colors.warningDark},success:{main:e.colors.successMain,light:e.colors.successLight,dark:e.colors.successDark},grey:{50:e.colors.grey50,100:e.colors.grey100,500:e.colors.grey500,600:e.colors.grey600,700:e.colors.grey700,800:e.colors.grey800,900:e.colors.grey900},text:{primary:e.darkTextPrimary,secondary:e.darkTextSecondary},background:{paper:e.colors.paper,default:e.backgroundDefault},action:{hover:e.customization.backgroundColor,focus:e.colors.secondaryDark}}},se=function(e){return{fontFamily:e.customization.fontFamily,fontSize:e.customization.fontSize,h6:{fontWeight:500,color:e.heading,fontSize:"0.75rem",letterSpacing:"0.2px"},h5:{fontSize:"0.875rem",color:e.heading,fontWeight:500,letterSpacing:"0.2px"},h4:{fontSize:"1rem",color:e.heading,fontWeight:600,letterSpacing:"0.2px"},h3:{fontSize:"1.25rem",color:e.heading,fontWeight:600,letterSpacing:"0.2px"},h2:{fontSize:"1.5rem",color:e.heading,fontWeight:700,letterSpacing:"0.2px"},h1:{fontSize:"2.125rem",color:e.heading,fontWeight:700,letterSpacing:"0.2px"},subtitle1:{fontSize:"0.875rem",fontWeight:500,color:e.textDark,letterSpacing:"0.2px"},subtitle2:{fontSize:"0.75rem",fontWeight:400,color:e.darkTextSecondary,letterSpacing:"0.2px"},caption:{fontSize:"0.75rem",color:e.darkTextSecondary,fontWeight:400},body1:{fontSize:"0.875rem",fontWeight:400,lineHeight:"1.334em"},body2:{fontWeight:400,lineHeight:"1.5em",color:e.darkTextPrimary},button:{textTransform:"capitalize"},customInput:{marginTop:8,marginBottom:8,"& > label":{top:"23px",left:0,color:e.grey500,'&[data-shrink="false"]':{top:"5px"}},"& > div > input":{padding:"30.5px 14px 11.5px !important"},"& legend":{display:"none"},"& fieldset":{top:0}},mainContent:{backgroundColor:"#f7f6f6",width:"100%",minHeight:"calc(100vh - 88px)",flexGrow:1,padding:"20px",marginTop:"88px",marginRight:"20px",letterSpacing:"0.2px",borderRadius:e.customization.borderRadius+"px"},menuCaption:{fontSize:"0.875rem",fontWeight:500,color:e.heading,padding:"6px",textTransform:"capitalize",marginTop:"10px"},subMenuCaption:{fontSize:"0.6875rem",fontWeight:500,color:e.darkTextSecondary,textTransform:"capitalize"},commonAvatar:{cursor:"pointer",borderRadius:"8px"},smallAvatar:{width:"22px",height:"22px",fontSize:"1rem"},mediumAvatar:{width:"34px",height:"34px",fontSize:"1.2rem"},largeAvatar:{width:"44px",height:"44px",fontSize:"1.5rem"}}},de=function(){var e={colors:pe,heading:pe.grey900,paper:pe.paper,backgroundDefault:U.a.backgroundColor,darkTextPrimary:pe.grey800,darkTextSecondary:pe.grey800,textDark:pe.grey900,menuSelected:pe.secondaryDark,menuSelectedBack:pe.secondaryLight,divider:U.a.borderColor,customization:U.a};return Object(le.a)({direction:"ltr",breakpoints:{values:{xs:0,sm:768,md:1024,lg:1280,xl:1400}},components:ce(e),palette:ue(e),typography:se(e),shadows:["rgba(99, 99, 99, 0.2) 0px 2px 8px 0px","rgba(0, 0, 0, 0.2) 0px 3px 9px","rgba(0, 0, 0, 0.2) 0px 3px 9px","rgba(0, 0, 0, 0.2) 0px 3px 9px","rgba(0, 0, 0, 0.2) 0px 3px 9px","rgba(0, 0, 0, 0.2) 0px 3px 9px","rgba(0, 0, 0, 0.2) 0px 3px 9px","rgba(0, 0, 0, 0.2) 0px 3px 9px","rgba(17, 17, 26, 0.09) 0px 4px 16px, rgba(17, 17, 26, 0.09) 0px 8px 32px","rgba(0, 0, 0, 0.2) 0px 3px 9px","rgba(0, 0, 0, 0.2) 0px 3px 9px","rgba(0, 0, 0, 0.2) 0px 3px 9px","rgba(0, 0, 0, 0.2) 0px 3px 9px","rgba(0, 0, 0, 0.2) 0px 3px 9px","rgba(0, 0, 0, 0.2) 0px 3px 9px","rgba(0, 0, 0, 0.2) 0px 3px 9px","rgba(0, 0, 0, 0.2) 0px 3px 9px","rgba(0, 0, 0, 0.2) 0px 3px 9px","rgba(0, 0, 0, 0.2) 0px 3px 9px","rgba(0, 0, 0, 0.2) 0px 3px 9px","rgba(0, 0, 0, 0.2) 0px 3px 9px","rgba(0, 0, 0, 0.2) 0px 3px 9px","rgba(0, 0, 0, 0.2) 0px 3px 9px","rgba(0, 0, 0, 0.2) 0px 3px 9px","rgba(0, 0, 0, 0.2) 0px 3px 9px"]})},me=function(){return o.a.createElement(ie.a,{injectFirst:!0},o.a.createElement(ae.a,{theme:de()},o.a.createElement(z.a,null),o.a.createElement(oe,null)))},fe=(r("+eM2"),r("SOjZ")),ge=r("i7Pf"),be=r("sDGz"),xe=Object(ge.a)({reducer:{app:be.a},middleware:function(e){return e()}}),ye=document.getElementById("root");Object(a.createRoot)(ye).render(o.a.createElement(m.a,{store:xe},o.a.createElement(fe.a,null,o.a.createElement(me,null))))},nxaZ:function(e,t,r){"use strict";r.d(t,"c",(function(){return s})),r.d(t,"b",(function(){return d}));var n=r("q1tI"),o=r.n(n),a=r("V4z/"),i=r("vDqi"),l=r.n(i);function c(e){return c="function"==typeof Symbol&&"symbol"==typeof Symbol.iterator?function(e){return typeof e}:function(e){return e&&"function"==typeof Symbol&&e.constructor===Symbol&&e!==Symbol.prototype?"symbol":typeof e},c(e)}function p(e,t){var r=Object.keys(e);if(Object.getOwnPropertySymbols){var n=Object.getOwnPropertySymbols(e);t&&(n=n.filter((function(t){return Object.getOwnPropertyDescriptor(e,t).enumerable}))),r.push.apply(r,n)}return r}function u(e,t,r){return(t=function(e){var t=function(e,t){if("object"!==c(e)||null===e)return e;var r=e[Symbol.toPrimitive];if(void 0!==r){var n=r.call(e,t||"default");if("object"!==c(n))return n;throw new TypeError("@@toPrimitive must return a primitive value.")}return("string"===t?String:Number)(e)}(e,"string");return"symbol"===c(t)?t:String(t)}(t))in e?Object.defineProperty(e,t,{value:r,enumerable:!0,configurable:!0,writable:!0}):e[t]=r,e}t.a=function(e){var t=e.children;return!!sessionStorage.getItem("token")?t:o.a.createElement(a.a,{to:"/login"})};var s=function(e){var t=arguments.length>1&&void 0!==arguments[1]?arguments[1]:{},r=arguments.length>2&&void 0!==arguments[2]?arguments[2]:{},n=sessionStorage.getItem("token");return l()(function(e){for(var t=1;t<arguments.length;t++){var r=null!=arguments[t]?arguments[t]:{};t%2?p(Object(r),!0).forEach((function(t){u(e,t,r[t])})):Object.getOwnPropertyDescriptors?Object.defineProperties(e,Object.getOwnPropertyDescriptors(r)):p(Object(r)).forEach((function(t){Object.defineProperty(e,t,Object.getOwnPropertyDescriptor(r,t))}))}return e}({method:"POST",url:e,headers:{"Content-Type":"application/json",Authorization:"Token ".concat(n)},data:t},r))},d=function(e){var t=sessionStorage.getItem("token");return l()({method:"GET",url:e,headers:{"Content-Type":"application/json",Authorization:"Token ".concat(t)}})}},sDGz:function(e,t,r){"use strict";r.d(t,"b",(function(){return a}));var n=r("i7Pf"),o=Object(n.b)({name:"app",initialState:{},reducers:{setTaxYear:function(e,t){e.taxYear=t.payload}}}),a=o.actions.setTaxYear;t.a=o.reducer}});
//# sourceMappingURL=main.js.map