"use strict";try{angular.module("wixTranslations")}catch(e){angular.module("wixTranslations",["pascalprecht.translate"])}angular.module("wixTranslations").config(["$translateProvider",function(a){var b={test:"test",page_title:"Error",header:{wix_com:"Wix.com",templates:"Templates",my_sites:"My Sites"},"500_title":"We're Just Fixing A<br/>Few Things!","500_message":"We hope to be back online very soon.<br/>Please try again in a few minutes.","500_support":"Still having problems? <a class='support-link' href='{{supportLink}}'> Contact Support <span class='link-arrow'></span></a>","400_title":"We Looked Everywhere<br/>For This Page!","400_message":"But maybe we can still help you find<br/>what you're looking for:","400_templates":"Check out our stunning templates <span class='pink-arrow'></span>","400_my_sites":"Manage your website <span class='pink-arrow'></span>","400_support":"Get in touch with our Support team <span class='pink-arrow'></span>",error_code:"(Error {{code}})",too_many_cookies_title:"Looks Like You Need<br/>to Clear Your Cookies!",too_many_cookies_message:"To get your site working again, clear the cookies in your browser by following the instructions <a class='instructions-link' href='{{instructionsLink}}'>here.</a>",too_many_cookies_more_help:"Need more help?",too_many_cookies_contact_support:"Please contact <a class='wix-support-link' href='{{supportLink}}'>Wix Support.</a>",unsupported_browser_title:"Looks Like It's Time<br/>To Update (It's Free!)",unsupported_browser_subtitle:"Your Browser Seems A Little Tired",unsupported_browser_message:"To enjoy Wix's latest features, all you need to do is update your browser. By the way, unsupported browsers are also slow and can put your security at risk.",unsupported_browser_install_browser:"Install latest <a class='support-link' href='{{link}}'>{{browserName}}</a> for free",unsupported_browser_continue:"Continue anyway",IE:"Internet Explorer",Safari:"Safari",Chrome:"Chrome",Firefox:"Firefox",not_published_title:"Don't Be Shy! Be Proud",not_published_message:"Share Your Beautiful Website<br/>With The World",not_published_here_is_how:"Here's How:",not_published_step1:"Go To <a class='my-sites-link' href='{{mySites}}'>My Sites</a>",not_published_step2:"Select Your Site",not_published_step3:"Click Publish",connect_your_ip_title:"Hey,<br/>We Know What<br/>You're Trying To Do :)",connect_your_ip_message:"But We Actually Need You To Type In<br/>The Website URL",connect_your_domain_title:"Looks Like This Domain Isn't<br/>Connected To A Website Yet!",connect_your_domain_message:"Is this your domain?<br/>Connect it to your Wix website in just a few easy steps:",connect_your_domain_more_help:"Need more help?",connect_your_domain_support:"Please contact our <a class='support-link' href='{{supportLink}}'>Support Team<span class='link-arrow'></span></a>",connect_your_domain_step1:"Go to <a class='support-link' href='{{wixLink}}'>Wix.com</a> > Subscriptions > Domains",connect_your_domain_step2:"Click Use a Domain You Already Own",connect_your_domain_step3:"Follow the steps to connect your domain to your website",undocumented_error_title:"An Undocumented Error",undocumented_error_message:"Well, this is unexpected.<br/>Please contact your system administrator.",published_not_available_secondary_title:"Treat Yourself!",published_not_available_title:"Congratulations,<br/>You Just Published Your Site",published_not_available_message:"Your website will be live in just a moment.<br/>Sit back, have a snack & refresh your browser.",invite_expired_title:"This Invite Has Expired","role-contributor":"Contributor","role-admin":"Admin","role-limitedAdmin":"Admin Limited","role-backOfficeManager":"Back Office Manager","role-blogManager":"Blog Writer","role-storeManager":"Store Manager","role-hotelManager":"Hotel Manager",non_branded_page_not_found_title:"PAGE NOT FOUND",non_branded_page_not_found_text:"We looked everywhere for this page. <br/>Are you sure the website URL is correct?<br/>Get in touch with the site owner.",non_branded_page_just_fixing_title:"We're Just Fixing<br/> A Few Things!",non_branded_page_just_fixing_text:"We hope to be back online very soon.<br/>Please try again in a few minutes.",non_branded_page_go_back_home:"Go Back Home",invite_expired_message:"Looks like your invite to become a {{role}} has expired.<div class='p-separator'></div>Contact the site owner, <a class='mail-link mail-to' href='mailto:{{ownerEmail}}'>{{ownerEmail}}</a><br/>to request a new invite",invite_expired_goto_wix:"Go to Wix.com <span class='pink-arrow'></span>",invite_expired_learn_more:"Learn more about Wix permissions <span class='pink-arrow'></span>",authorization_not_supported_title:"This page is only accessible to the site owner."};a.translations("en",b),a.translations(b),a.preferredLanguage&&a.preferredLanguage("en")}]).value("preferredLanguage","en");