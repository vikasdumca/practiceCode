









from lxml import etree
import sys
import time
import pycurl





















d= '''  <html>
<head>














<link rel="canonical" href="http://www.amazon.com/Multi-Angles-Leather-Protection-i-UniK-Blue/product-reviews/B007SBGF12" />


<title>Amazon.com: Customer Reviews: 7 Inch Multi-Angles Google Nexus 7 Tablet Leather Protection Case by i-UniK (Light Blue) - Colors Available: Hot Pink, Red, Lime Green, Light Blue, Expresso Black</title>











<script type="text/javascript">
  var loader = new Image();
  loader.src = "http://g-ecx.images-amazon.com/images/G/01/common/sprites/sprite-site-wide-2._V146303866_.png";

  function spriteLoaded() {
    if (typeof uet == 'function') { uet('cf'); }
  }
  loader.onLoad = spriteLoaded(); 

</script>














<script language="Javascript1.1" type="text/javascript">
<!--
function amz_js_PopWin(url,name,options){
  var ContextWindow = window.open(url,name,options);
  ContextWindow.focus();
  return false;
}
//-->
</script>




 
 




<link type='text/css' href='http://z-ecx.images-amazon.com/images/G/01/browser-scripts/us-site-wide-css-beacon/site-wide-6804619766._V1_.css' rel='stylesheet'>


<script type="text/javascript">

var amznJQ,jQueryPatchIPadOffset=false;
(function() {
  function f() {}
  function ch(y) {return String.fromCharCode(y);}
  amznJQ={
    addLogical:f,
    addStyle:f,
    addPL:f,
    available:f,
    chars:{EOL:ch(10), SQUOTE:ch(39), DQUOTE:ch(34), BACKSLASH:ch(92), YEN:ch(165)},
    completedStage:f,
    declareAvailable:f,
    onCompletion:f,
    onReady:f,
    strings:{}
  };
}());


</script>




























<link href='http://z-ecx.images-amazon.com/images/G/01/nav2/gamma/websiteGlobalCSS/websiteGlobalCSS-websiteGlobal-10346._V1_.css' type='text/css' rel='stylesheet'>
<style type="text/css"><!--

.sans, .small, .h1, .h3color, .big, .tiny, .tinyprice, .highlight, .eyebrow,
    a:active, a:visited, a:link, div.unified_widget p.seeMore,
    div.unified_widget .carat, div.left_nav .carat, div.left_nav, div.left_nav
    h2, div.left_nav h3, div.left_nav a:link, div.left_nav a:visited,
    .popover-tiny, .horizontal-search, .horizontal-websearch, .topnav,
    .topnav-active a:link, .tabon a, .tabon a:visited, .taboff a, .taboff
    a:visited div.leftnav_popover h2, .signInMsg{
  font-family: verdana,arial,helvetica,sans-serif;
}
.listprice {
  font-family: arial,verdana,helvetica,sans-serif;
}
.price {
  font-family: arial,verdana,helvetica,sans-serif;
}
.serif, .sans, .h1, div.unified_widget .headline{
  font-size: medium;
}
.big {
  font-size: xx-large;
}
.small, .h3color, .highlight, .horizontal-search {
  font-size: small;
}
.signInMsg {
  font-size: x-small;
}
.tiny, .tinyprice, .popover-tiny, .horizontal-websearch {
  font-size: x-small;
}
body, td, th {
  font-family: verdana,arial,helvetica,sans-serif;
  font-size: small;
}
.eyebrowBackGroundColor {
  background-color: ;
}
div.left_nav, div.left_nav a:link, div.left_nav a:visited {
  font-family: Arial, sans-serif;
}

body {
  color: #000000;
  margin-top: 0px;
}
--></style> 




<style type="text/css"><!--

.crAuthorInfo {
  font-family:               verdana;
  font-size:                 0.86em;
  margin-left:               80px;
}

.crAuthorInfoCredibility {
  font-family:               verdana;
  font-size:                 0.86em;
}

.crBlue-bevel {
  background:                url(http://g-ecx.images-amazon.com/images/G/01/x-locale/communities/reviews/sliced-box-tbevel._V192249888_.gif) repeat-x top;
  height:                    1.45em;
}

.crBlueBorder-tl {
  background:                url(http://g-ecx.images-amazon.com/images/G/01/x-locale/communities/reviews/border-box-tl._V192249923_.gif) no-repeat top left;
  width:                     1em;
}
                                                                                                                                                             
.crBlueBorder-tc {
  background:                url(http://g-ecx.images-amazon.com/images/G/01/x-locale/communities/reviews/border-box-tc._V192249922_.gif) repeat-x top;
}
                                                                                                                                                             
.crBlueBorder-tr {
  background:                url(http://g-ecx.images-amazon.com/images/G/01/x-locale/communities/reviews/border-box-tr._V192249949_.gif) no-repeat top right;
  width:                     1em;
}
                                                                                                                                                             
.crBlueBorder-bl {
  background:                url(http://g-ecx.images-amazon.com/images/G/01/x-locale/communities/reviews/border-box-bl._V192249926_.gif) no-repeat bottom left;
}
                                                                                                                                                             
.crBlueBorder-bc {
  background:                url(http://g-ecx.images-amazon.com/images/G/01/x-locale/communities/reviews/border-box-bc._V192249923_.gif) repeat-x bottom;
}
                                                                                                                                                             
.crBlueBorder-br {
  background:                url(http://g-ecx.images-amazon.com/images/G/01/x-locale/communities/reviews/border-box-br._V192249923_.gif) no-repeat bottom right;
}

.crBox {
  background:                #DFEDF7;
  padding:                   0.2em 1.5em 0.2em 1.5em;
}

.crBox-tl {
  background:                #DFEDF7 url(http://g-ecx.images-amazon.com/images/G/01/x-locale/communities/reviews/box-tl._V192249949_.gif) no-repeat top left;
}

.crBox-tc {
  background:                url(http://g-ecx.images-amazon.com/images/G/01/x-locale/communities/reviews/box-tc._V192249950_.gif) repeat-x top;
}

.crBox-tr {
  background:                url(http://g-ecx.images-amazon.com/images/G/01/x-locale/communities/reviews/box-tr._V192249948_.gif) no-repeat top right;
}

.crBox-bl {
  background:                #DFEDF7 url(http://g-ecx.images-amazon.com/images/G/01/x-locale/communities/reviews/box-bl._V192249921_.gif) no-repeat bottom left;
}

.crBox-bc {
  background:                url(http://g-ecx.images-amazon.com/images/G/01/x-locale/communities/reviews/box-bc._V192249923_.gif) repeat-x bottom;
}

.crBox-br {
  background:                url(http://g-ecx.images-amazon.com/images/G/01/x-locale/communities/reviews/box-br._V192249949_.gif) no-repeat bottom right;
}

.crColumnEndMarker {
  clear:                     both;
  height:                    13px;
  background-image:          url(http://g-ecx.images-amazon.com/images/G/01/x-locale/communities/people/column-bottom-edge._V192250335_.gif);
  background-repeat:         no-repeat;
}

.crColumnEndMarker .rightEdge {
  float:                     right;
  background-image:          url(http://g-ecx.images-amazon.com/images/G/01/x-locale/communities/people/column-bottom-edge-right._V192250334_.gif);
  background-position:       right top;
  background-repeat:         no-repeat;
  width:                     13px;
  height:                    13px;
}


.crCdDotsBottom {
  clear:                     both;
  padding:                   1px;;
  font-size:                 0.0625em;
  margin:                    0 0 5px 0;
  background-image:          url(http://g-ecx.images-amazon.com/images/G/01/x-locale/communities/people/dotborder._V192250320_.gif);
  background-repeat:         repeat-x;
  background-position:       center;
}

.crDescription {
  font-family:               verdana;
  margin-left:               80px;
}


.crErrorMsg {
  color:                     red;
  font-weight:               bold;
}

.crFanlink {
  text-decoration: 	     none; 
  border-top-width:          0; 
  border-right-width:        0; 
  border-bottom-width:       1px;
  border-left-width:         0;
  border-top-color:          #146EB4;
  border-right-color:        #146EB4;
  border-bottom-color:       #146EB4;
  border-left-color:         #146EB4;
  border-top-style:          none;
  border-right-style:        none;
  border-bottom-style:       dashed;
  border-left-style:         none;
  color:                     #003399; 
}

.crFinePrint {
  font-size:                 0.7em;
  margin-top:                0.7em;
}

.crForm {
  width:                     100%;
  display:                   block;
}

.crHeaderText {
  color:                     #CC6600;
  padding-left:              0;
  padding-bottom:            5px;
  font-family:               helvetica,
  font-size:                 13px;
  font-weight:               bold;
  float:                     top;
  float:                     left;
}

h2.crHeading {
  color:                     #E47911;
  font-family:               Verdana,Helvetica,sans-serif;
  font-size:                 130%;
  margin:                    0 0 3px;
  padding-left:              0px;
}

h3.crHeading {
  color:                     #E47911;
  font-family:               Verdana,Helvetica,sans-serif;
  font-size:                 100%;
  margin:                    0 0 10px;
}

.crHeading {
  color:                     #c60;
  font-family:               sans-serif;
  font-size:                 1.5em;
  font-weight:               bold;
  padding-bottom:            0.5em;
  padding-left:              0.5em;
}

.crInnerBox {
  padding:                   0.6em 2em 0.6em 2em;
  background:                #EFF5F9;
  clear:                     both;
}

.crInnerBox-tl {
  background:                #EFF5F9 url(http://g-ecx.images-amazon.com/images/G/01/x-locale/communities/reviews/innerbox-tl._V192249896_.gif) no-repeat top left;
  clear: both;
}

.crInnerBox-tr {
  background:                #EFF5F9 url(http://g-ecx.images-amazon.com/images/G/01/x-locale/communities/reviews/innerbox-tr._V192249895_.gif) no-repeat top right;
  clear: both;
}

.crInnerBox-bl {
  background:                #EFF5F9 url(http://g-ecx.images-amazon.com/images/G/01/x-locale/communities/reviews/innerbox-bl._V192249902_.gif) no-repeat bottom left;
}

.crInnerBox-br {
  background:                url(http://g-ecx.images-amazon.com/images/G/01/x-locale/communities/reviews/innerbox-br._V192249902_.gif) no-repeat bottom right;
}

.crInputTitle {
  font-weight:               bold;
  vertical-align:            middle; 
}

.crInputFinePrint {
  color:                     #6E6E6E; 
  font-size:                 0.7em;
  padding-bottom:            1.5em; 
}

.crInput {
  padding:                   0em 0em 1.5em 0em;
  vertical-align:            middle;
}

.crInputFormField {
  font-family:               arial, helvetica, sans-serif;
}

.crInstruction {
  padding-bottom:            0.4em;
  float:                     left;
}

.crProductLinks {
  padding-bottom:            0.4em;
  float:                     right;
  vertical-align:            top;  
}

.crLargerTitle {
  font-family:               verdana, arial, helvetica, sans-serif;
  font-size:                 1.6em;
  color:                     #c60;
  padding-bottom:            5px;
  padding-top:               10px;
}

.crLine {
  clear:                     both;
  border:                    0;
  height:                    2px;
  color:                     #CADFE9;
  background-color:          #CADFE9;
  noshade:                   noshade;
}

.crPrevLeftButton {
  padding-left:              15px; 
  margin-bottom:             0px;
}

.crPrevRightButton {
  margin-bottom:             0px;
}

.crPicture {
  clear:                     both;
  float:                     left;
  text-align:                center;
  width:                     80px;
  overflow:                  hidden;
  padding-top:               0.2em;
}

.crReviewHeader  {
  font-family:               Verdana, Arial, Helvetica, sans-serif;
  font-size:                 1.5em;
  font-weight:               bold;
  color:                     #e47911;
  margin-top:                5px;
}

.crReviewSumBox {
  height:                    36px;
  background-image:          url(http://g-ecx.images-amazon.com/images/G/01/x-locale/communities/people/column-eyebrow-visitor._V192250334_.gif);
  background-repeat:         no-repeat;
  font-family:               verdana;
  font-size:                 36px;
}

.crReviewSumBox .titleText {
  float:                     left;
  font-weight:               bold;
  padding-left:              10px;
  padding-top:               10px;
  font-size:                 13px;
  font-family:               verdana;
  color:                     #000000;
  white-space:               nowrap;
}

.crReviewSumBox .rightEdge {
  background-image:          url(http://g-ecx.images-amazon.com/images/G/01/x-locale/communities/people/column-eyebrow-visitor-right._V192250335_.gif);
  width:                     12px;
  height:                    36px;
  background-repeat:         no-repeat;
  padding:                   0;
  float:                     right;
}

.crSectionTitle {
  color:                     #E57310;
  font-size:                 16px;
  font-weight:               bold;
  margin-top:                5px;
  margin-bottom:             5px;
}

.crProductReviewsSummary .crSolicitation {
  margin-top:               -20px;
}

.crSideHeading {
  color:                     #c60;
  font-weight:               bold;
  text-align:                center;
  padding-top:               0.4em;
}

.crStepNum {
  vertical-align:            top;
  padding:                   0em 0.6em 1.5em 0em;
}


.crTanBorder-tl {
  background:                url(http://g-ecx.images-amazon.com/images/G/01/x-locale/communities/boxes/boxfill/innerbox-tl._V192251350_.gif) no-repeat top left;
  width:                     1em;
}
                                                                                                                                                             
.crTanBorder-tc {
  background:                url(http://g-ecx.images-amazon.com/images/G/01/x-locale/communities/boxes/boxfill/innerbox-tc._V192251344_.gif) repeat-x top;
}
                                                                                                                                                             
.crTanBorder-tr {
  background:                url(http://g-ecx.images-amazon.com/images/G/01/x-locale/communities/boxes/boxfill/innerbox-tr._V192244553_.gif) no-repeat top right;
  width:                     1em;
}
                                                                                                                                                             
.crTanBorder-bl {
  background:                url(http://g-ecx.images-amazon.com/images/G/01/x-locale/communities/boxes/boxfill/innerbox-bl._V192251348_.gif) no-repeat bottom left;
}
                                                                                                                                                             
.crTanBorder-bc {
  background:                url(http://g-ecx.images-amazon.com/images/G/01/x-locale/communities/boxes/boxfill/innerbox-bc._V192241903_.gif) repeat-x bottom;
}
                                                                                                                                                             
.crTanBorder-br {
  background:                url(http://g-ecx.images-amazon.com/images/G/01/x-locale/communities/boxes/boxfill/innerbox-br._V192241895_.gif) no-repeat bottom right;
}

.crTextAreaHeader {
  background:                #B6CFE5;
  padding:                   0.4em 0em 0.4em 0em;
  width:                     620px;
}

.crTextTab {
  width:                     30%;
  float:                     left;
  white-space:               nowrap;
}

.crTextTabHeading {
  padding:                   0.3em 0 0.7em 0.6em;
}

.crThreadHeader {
  color:                     #CC6600;
  font-weight:               bold;
  float:                     left;
}

.crTipsBoxHeader {
  font-size:                 0.90em;
  font-weight:               bold;
  margin-bottom:             10px;
  margin-top:                10px;
}

.crTipsBoxTitle {
  color:                     #CC6600;
  font-size:                 1.1em;
  font-weight:               bold;
  margin-bottom:             10px;
}

h1.crTitle {
  color:                     #E47911;
  font-family:               Arial, Helvetica, sans-serif;
  font-size:                 218%;
  letter-spacing:            -0.03em;
  margin:                    0;
  padding:                   0;
}

.crTitle {
  font-family:               verdana, arial, helvetica, sans-serif;
  font-size:                 1.4em;
  font-weight:               bold;
}

.crTab-tl {
  background:                #EFF5F9 url(http://g-ecx.images-amazon.com/images/G/01/x-locale/communities/reviews/innerbox-tl._V192249896_.gif) no-repeat top left;
}

.crTab-tr {
  background:                url(http://g-ecx.images-amazon.com/images/G/01/x-locale/communities/reviews/innerbox-tr._V192249895_.gif) no-repeat top right;
}

.crVideoUpload {
  background:                #FFFFFF;
  border:                    0.1em solid #7F9DB9;
  text-align:                center;
  padding:                   0.4em;
}

.crVidTab {
  width:                     70%;
  float:                     left;
  white-space:               nowrap;
}

.crVidTabHeading {
  padding:                   0.3em 0 0.7em 0.6em;
}

table.crDataGrid th {
  background-color:          #EEEEEE;
  font-weight:               normal;
  font-size:                 70%;
  text-align:                left;
  color:                     #666666;
}

table.crDataGrid td {
  border-bottom:            1px solid #CCCCCC;
}

table.crDataGrid .img {
  height:                   92px;
}

table.crDataGrid .crNum {
  text-align:               right;
}

table.crDataGrid .crNumPercentHelpful {
  text-align:               right;
  padding-right:20px;
}

table.crDataGrid .crNumFanVoters {
  text-align:               right;
  border-left: solid 1px #cccccc;
}

ul.crBigBullet {
  margin:                    0em;
  padding:                   0em;
  list-style-image:          url(http://g-ecx.images-amazon.com/images/G/01/x-locale/communities/reviews/big-bullet._V192249925_.gif);
}

ul.crSmallBullet {

  padding-left:              0;
  margin:                    0.4em 0em 0.6em 1.5em;
  list-style-image:          url(http://g-ecx.images-amazon.com/images/G/01/x-locale/communities/reviews/small-bullet._V192249889_.gif);
}


.srCreateReview td.name {
  padding-left: 9px;
}

.srCreateReview .srPopoverList table.srList td a {
  margin-left: 0px;
}

.srCreateReview .srPopoverList table.srList td.name span.newAttribute {
  margin-left: 0px;
  color:       #000000;
}

.srCreateReview .srPopoverFooter {
  padding-left: 9px;
  padding-top:  9px;
}

.srCreateReview .srPopoverContentSection .heading {
  font-weight: normal;
}

#structuredRatingsList .cBox {
  width: 375px;
}

.structuredRatingsVisibilityLink {
  line-height: 2.5em;
  font-size: 0.86em;
}

.structuredRatingsVisibilityLinkText {
  margin-left: 5px;
}

#structuredRatingsListHelp {
  font-size: 0.86em;
  font-weight: normal;
}

#structuredRatingsList .srpopover .scrollSection {
  height: 210px;
}

.crVerifiedNew {
  font-size: 0.86em;
  font-weight: bold;
  color: #009900;
  margin-right: 0.5em;
} 

.crVerifyLearnMore {
  margin-left: 0.5em;
}

.crVerifiedPurchaseInputs {
  display: block;
  margin-bottom: 1em;
}

.crVerifiedBackfillSuboption {
  display: block;
  margin-left: 2em;
}

div.crCommentThread .cmPage {
  margin-left: 5px;
}

div#cdNonReplyPostBoxButton {
  margin-bottom: 40px;
}

#rdpItemInfo .crAvgStars {
  font-size: 10px;
}

.crIneligibleHeader {
  padding: 15px 9px 0 6px;
  color:                     #E47911;
  font-weight: 	             bold;
  font-size:                 218%;
  margin:                    0;
}

.crIneligibleMessage {
  font-size: 12px;
  border: solid 1px #0071B5;
  position: relative;
  background-color: #ffffdd;
  border-color: #E47911;
  padding: 18px 50px 18px 20px;
  margin: 10px 0 40px 10px;
}
.crIneligibleMessageImage {
  position: absolute;
}
.crIneligibleMessageHeader {
  font-size: 18px;
  font-weight: bold;
  margin: 0 0 4px 45px;
  padding: 0;
}
.crIneligibleMessageText {
  font-size:13px;
  margin: 0 0 6px 45px;
  width: 100%;
}


.crIFrame {
  margin: 10px;
}

.crIFrameLogo {
  margin-bottom: 20px;
}

.crIFrameHeaderLeftColumn {
  float: left;
  margin-right: 20px;
}

.crIFrameHeaderTitle {
  font-size:      24px;
  letter-spacing: -1px;
}

.crIFrameHeaderHistogram {
  float: left;
}

.crIFrameError {
  border-top:    1px solid #D1E6F7;
  border-bottom: 1px solid #D1E6F7;

  text-align:          center;
  line-height:         24px;
  width:               360px;
  padding:             20px;
  margin-top:          20px;
}

.crIFrameErrorText {
  font-size:  14px;
  font-weight: bold;
}

.crIFrameCreateReview {
  margin-bottom:   3px;
  white-space:     nowrap;
}

.crIFrameCreateReviewButton {
  vertical-align:  middle;
}

.crIFrameAverageReviewText {
  align: left;
  font-weight: bold;
}

.crIFrameNumCustReviews {
   white-space: nowrap;
}

.crIFrameReviewList {
  width: 100%;
  clear: left;
}


.CMheadingBar {
  background:url(http://g-ecx.images-amazon.com/images/G/01/nav2/images/gui/tile-blue-bg._V46870869_.gif) repeat-x;
  border-top:1px solid #BADAE8;
  border-bottom:1px solid #BADAE8;
  padding:6px;
}

.CMpaginate {
  color:#666;
}

.CMpaginate .on {
  border:1px solid #CC6600;
  padding:3px;
  background-color:white;
  color:#CC6600;
  text-decoration:none;
}

.CMpaginate a:link,
.CMpaginate a:visited {
  padding:4px;
  text-decoration:none;
}

.CMpaginate a:hover {
  padding:3px;
  background-color:white;
  border:1px solid #CC6600;
  color:#CC6600;
}

a.areaLink, a.areaLink:visited {
  text-decoration: none;
  color: black;
  display: block;
}

.areaLink .innerLink {
  white-space: nowrap;
  text-decoration: underline;
  color: #039;
}

div.crVS {
  width:       46%;
  text-align:  center;
  white-space: nowrap;
}

.crClear { clear: both; }
.crLeft { float: left; }
.crRight { float: right; }

.attr-sheet { padding-left:5px; }
.attr-sheet ul { margin-left: 31px; padding: 0; list-style: none; border: solid 1px #eee; border-radius: 5px; }
.attr-sheet ul li { padding: 5px; }
.attr-sheet li.alt { background: #F8F5D8 }
.attr-sheet li .label { font-weight: bold }
.attr-sheet li .vm { vertical-align: middle; }
.attr-sheet li .option-line { width: 100%; line-height: 1.75em; }
.attr-sheet li .option-line .label { float: left; width: 35%; max-width: 300px }
.attr-sheet li .option-line .option { float: left; width: 30%; max-width: 200px }
.attr-sheet li .option-undo { float: right; font-size: xx-small; display:none; }
.attr-sheet li .textbar-text { margin-top: 2px; clear: both; }
.attr-sheet li .textbar .empty { width: 35%; max-width: 300px; float:left; }
.attr-sheet li .textbar input { width: 50%; margin-left:5px; float:left; }
.attr-sheet li .textbar .blur { color: #999; }
.attr-preview .boldLabel { font-weight: bold }
.attr-preview .head { padding: 20px 0 0 25px }
.attr-preview .head-detail { padding-top: 5px }
.attr-preview .line { padding: 5px 0 15px 0 }
.attr-preview .lines { padding: 10px 0 0 25px }

.rypWgtDiv { margin-bottom: 20px; }

.rypWgtImgLink { 
    display: block;
    width: 300px;
    height: 97px;
    background: url('http://g-ecx.images-amazon.com/images/G/01/x-locale/communities/reviews/ryp-page-image2sprite._V399712482_.png') top;
    text-indent: -10000px;
}
.rypWgtImgLink:hover {
	background-position: bottom;
} 


  /* MTOH specific CSS -- still needed after AUI launches */
  #mtoh-bucket {
    margin-top: 30px !important;
    width: 550px;
  }

  #mtoh-vote-prompt {
    float: left;
    width: 340px;
  }

  .mtoh-base-text {
    font-family: Arial,"Helvetica Neue",Helvetica,sans-serif;
    font-style: normal;
    font-size: 13px;
  }

  .mtoh-prompt-text {
    margin-bottom: 0;
  }

  .mtoh-button-valigned-text {
    line-height: 17px;
  }

  #mtoh-thank-you {
    display: none;
  }

  #mtoh-comment {
    display: none;
  }

  #mtoh-comment-input {
    padding: 5px 7px;
    width: 100%;
    margin-bottom: 10px;
  }

  #mtoh-comment-input-label {
    display: inline-block;
    padding-bottom: 2px;
    padding-left: 2px;
  }

  #mtoh-comment-input-optional-text {
    font-style: italic;
  }

  .mtoh-yes-no-button {
    margin-right: 10px;
    width: 60px;
    float: right;
  }

  #mtoh-comment-send-button {
    width: 100px;
    float: right;
  }

  #mtoh-no-thanks-link {
    float: right;
    margin-right: 20px;
    line-height: 33px;
    color: #004B91;
    cursor: pointer;
  }

  #mtoh-no-thanks-link a:focus, #mtoh-no-thanks-link a:hover, #mtoh-no-thanks-link a:active {
    color: #E47911;
    font-family: Arial,"Helvetica Neue",Helvetica,sans-serif;
  }

  .mtoh-aui-button, .mtoh-aui-button:hover {
    color: #111111;
    text-decoration: none !important;
  }

  .mtoh-aui-button:hover {
    border-color: #AAAAAA #9D9D9D #939393;
  }

  /* AUI copied class definitions -- switch to real AUI components and classes once it launches. */
  .mtoh-aui-size-small {
    font-size: 12px;
  }

  .mtoh-aui-row:after {
    clear: both;
  }

  .mtoh-aui-row:before, .mtoh-aui-row:after {
    content: "";
    display: table;
    font-size: 0;
    line-height: 0;
  }

  .mtoh-aui-row {
    width: 100%;
  }

  .mtoh-aui-box-group .mtoh-aui-box {
    -webkit-border-radius: 0;
    -moz-border-radius: 0;
    border-radius: 0 0 0 0;
    margin-top: -1px;
  }

  .mtoh-aui-box {
    display: block;
    overflow: hidden;
    -webkit-border-radius: 4px;
    -moz-border-radius: 4px;
    border-radius: 4px;
    border: 1px #dddddd solid;
    background-color: white;
  }

  .mtoh-aui-box-group .mtoh-aui-box.mtoh-aui-first {
    -webkit-border-top-left-radius: 4px;
    -webkit-border-top-right-radius: 4px;
    -webkit-border-bottom-right-radius: 0;
    -webkit-border-bottom-left-radius: 0;
    -moz-border-radius-topleft: 4px;
    -moz-border-radius-topright: 4px;
    -moz-border-radius-bottomright: 0;
    -moz-border-radius-bottomleft: 0;
    border-top-left-radius: 4px;
    border-top-right-radius: 4px;
    border-bottom-right-radius: 0;
    border-bottom-left-radius: 0;
    margin-top: 0; 
  }

  .mtoh-aui-box.mtoh-aui-box-title .mtoh-aui-box-inner {
    padding: 10px 18px;
    background: #efefef;
    background: #f9f9f9;
    /* Old browsers */
    background: -moz-linear-gradient(top, #fcfcfc, #f7f7f7);
    /* FF3.6+ */
    background: -webkit-gradient(linear, left top, left bottom, color-stop(0%, #fcfcfc), color-stop(100%, #f7f7f7));
    /* Chrome,Safari4+ */
    background: -webkit-linear-gradient(top, #fcfcfc, #f7f7f7);
    /* Chrome10+,Safari5.1+ */
    background: -o-linear-gradient(top, #fcfcfc, #f7f7f7);
    /* Opera 11.10+ */
    background: -ms-linear-gradient(top, #fcfcfc, #f7f7f7);
    /* IE10+ */
    background: linear-gradient(top, #fcfcfc, #f7f7f7);
    /* W3C */
    filter: progid:DXImageTransform.Microsoft.gradient(startColorstr='#fcfcfc', endColorstr='#f7f7f7',GradientType=0);
    /* IE6-8 */
    *zoom: 1;
    -webkit-box-shadow: 0 1px 0px rgba(255, 255, 255, 0.5) inset, 0 -1px 0px rgba(255, 255, 255, 0.4) inset;
    -moz-box-shadow: 0 1px 0px rgba(255, 255, 255, 0.5) inset, 0 -1px 0px rgba(255, 255, 255, 0.4) inset;
    box-shadow: 0 1px 0px rgba(255, 255, 255, 0.5) inset, 0 -1px 0px rgba(255, 255, 255, 0.4) inset; 
  }
  
  .mtoh-aui-box.mtoh-aui-box-title h4 {
    color: #737373;
    font-size: 11px;
    font-weight: bold;
    line-height: 14px;
    text-transform: uppercase;
    margin-bottom: 0px;
    margin-top: 0px;
  }

  .mtoh-aui-box .mtoh-aui-box-inner {
    padding: 14px 18px;
    overflow: hidden;
    -webkit-border-radius: 4px;
    -moz-border-radius: 4px;
    border-radius: 4px;
    position: relative;
  }

  .mtoh-aui-box h4:last-child {
    padding-bottom: 0;
  }

  .mtoh-aui-box-group .mtoh-aui-box.mtoh-aui-last {
    border-radius: 0 0 4px 4px;
  }
  
  /* AUI Buttons */
  .mtoh-aui-button {
    -moz-border-bottom-colors: none;
    -moz-border-left-colors: none;
    -moz-border-right-colors: none;
    -moz-border-top-colors: none;
    border-color: #B7B7B7 #AAAAAA #A0A0A0;
    border-image: none;
    border-radius: 3px 3px 3px 3px;
    border-style: solid;
    border-width: 1px;
    cursor: pointer;
    display: block;
    height: 31px;
    max-width: 100%;
    overflow: hidden;
    textlign: center;
    verticallign: middle;
  }

  .mtoh-aui-button {
    background: none repeat scroll 0 0 gainsboro;
  }

  .mtoh-aui-button .mtoh-aui-button-inner {
    background: #ececec;
    /* Old browsers */
    background: -moz-linear-gradient(top, whitesmoke, #e3e3e3);
    /* FF3.6+ */
    background: -webkit-gradient(linear, left top, left bottom, color-stop(0%, whitesmoke), color-stop(100%, #e3e3e3));
    /* Chrome,Safari4+ */
    background: -webkit-linear-gradient(top, whitesmoke, #e3e3e3);
    /* Chrome10+,Safari5.1+ */
    background: -o-linear-gradient(top, whitesmoke, #e3e3e3);
    /* Opera 11.10+ */
    background: -ms-linear-gradient(top, whitesmoke, #e3e3e3);
    /* IE10+ */
    background: linear-gradient(top, whitesmoke, #e3e3e3);
    /* W3C */
    filter: progid:DXImageTransform.Microsoft.gradient(startColorstr='whitesmoke', endColorstr='#e3e3e3',GradientType=0);
    /* IE6-8 */
    *zoom: 1; 
    border-radius: 3px 3px 3px 3px;
    box-shadow: 0 1px 0 rgba(255, 255, 255, 0.6) inset;
    height: 29px;
    overflow: hidden;
    padding: 0 10px 0 11px;
    position: relative;
  }

  .mtoh-aui-button .mtoh-aui-button-text {
    line-height: 28px;
    color: #111111;
    display: block;
    font-family: Arial,sans-serif;
    font-size: 13px;
    text-align: center;
    white-space: nowrap;
  }

  .mtoh-aui-button .mtoh-aui-button-text {
    line-height: 29px;
  }

  /* AUI button Hover */
  .mtoh-aui-button, .mtoh-aui-button:hover {
    color: #111111;
    text-decoration: none !important;
  }

  .mtoh-aui-button:hover {
    border-color: #AAAAAA #9D9D9D #939393;
  }

  .mtoh-aui-button .mtoh-aui-button-inner:hover {
    background: #dfdfdf;
    /* Old browsers */
    background: -moz-linear-gradient(top, #e8e8e8, #d6d6d6);
    /* FF3.6+ */
    background: -webkit-gradient(linear, left top, left bottom, color-stop(0%, #e8e8e8), color-stop(100%, #d6d6d6));
    /* Chrome,Safari4+ */
    background: -webkit-linear-gradient(top, #e8e8e8, #d6d6d6);
    /* Chrome10+,Safari5.1+ */
    background: -o-linear-gradient(top, #e8e8e8, #d6d6d6);
    /* Opera 11.10+ */
    background: -ms-linear-gradient(top, #e8e8e8, #d6d6d6);
    /* IE10+ */
    background: linear-gradient(top, #e8e8e8, #d6d6d6);
    /* W3C */
    filter: progid:DXImageTransform.Microsoft.gradient(startColorstr='#e8e8e8', endColorstr='#d6d6d6',GradientType=0);
    /* IE6-8 */
    *zoom: 1; 
   }

  /* AUI button Active */
  .mtoh-aui-button:active {
    border-color: #A0A0A0 #AAAAAAA #AAAAAA;
  }

  .mtoh-aui-button .mtoh-aui-button-inner:active {
    background-color: #E3E3E3;
    background-image: none;
    box-shadow: 0 1px 3px rgba(0, 0, 0, 0.2) inset;
  }

  .mtoh-aui-button .mtoh-aui-button-inner:active {
    background-color: #D9D9D9;
  }

  
.structured-not-helpful-container { display:none;border:1px solid #AAA; border-radius:6px;padding:0;overflow:hidden }
.structured-not-helpful-container-inner { padding: 1em; border-bottom: solid 1px #aaa; }
.structured-not-helpful-reason-list { list-style:none;padding:0.5em 0;margin:0; }
.structured-not-helpful-reason-list li { height: 20px; margin: 0 }
.structured-not-helpful-error { color:#B00;display:none;padding-left: 0.5em }
.structured-not-helpful-comment-div { display: none; }
.structured-not-helpful-comment-div input { width: 100%; }
  .structured-not-helpful-buttons { background: #f0f0f0; margin: 0; padding: 0; text-align: right; height: 46px;  }
  .structured-not-helpful-buttons button {
    border-radius: 6px;
    border-style: solid;
    border-width: 1px;
    height: 30px;
    overflow: hidden;
    padding: 0 10px 0 11px;
    margin: 8px 3px 8px 0;
    cursor:pointer;
  }

.structured-not-helpful-cancel, .structured-not-helpful-submit { float: right; margin: 0; margin-right: 3px; height: 30px; }
.structured-not-helpful-cancel button {
    background-color: #ddd;
    background: -moz-linear-gradient(center top, #FFFFFF, #DDDDDD) repeat scroll 0 0 #DDDDDD;
    background: -webkit-gradient(linear, left top, left bottom, color-stop(0%, #FFFFFF), color-stop(100%, #DDDDDD)); 
    background: -webkit-linear-gradient(top, #FFFFFF, #DDDDDD) repeat scroll 0 0 #DDDDDD;
    background: -o-linear-gradient(#fff, #ddd);
    filter: progid:DXImageTransform.Microsoft.gradient(startColorstr='#FFFFFF', endColorstr='#DDDDDD');
    -ms-filter: "progid:DXImageTransform.Microsoft.gradient(startColorstr='#FFFFFF', endColorstr='#DDDDDD')";
    background: linear-gradient(#fff, #ddd);
    border-color: #AAAAAA #888888 #888888 #AAAAAA;
}
.structured-not-helpful-submit button {
    background-color: #EEBA37;
    background: -moz-linear-gradient(center top, #FFEAB4, #F4BF3B) repeat scroll 0 0 #EEBA37; 
    background: -webkit-gradient(linear, left top, left bottom, color-stop(0%, #FFEAB4), color-stop(100%, #F4BF3B)); 
    background: -webkit-linear-gradient(top, #FFEAB4, #F4BF3B) repeat scroll 0 0 #EEBA37; 
    background: -o-linear-gradient(#FFEAB4, #F4BF3B);
    filter: progid:DXImageTransform.Microsoft.gradient(startColorstr='#FFEAB4', endColorstr='#F4BF3B');
    -ms-filter: "progid:DXImageTransform.Microsoft.gradient(startColorstr='#FFEAB4', endColorstr='#F4BF3B')";
    background: linear-gradient(#FFEAB4, #F4BF3B);
    border-color: #DBB75D #C5A964 #B88E27 #DBB75D;
}
.structured-not-helpful-thanks { color: green; }
.structured-not-helpful-container .optional { color: #888; }
.structured-not-helpful-reason-list li input {
    border: 0 none;
    height: 20px;
    line-height: 20px;
    margin: 0 0 0 0.5em;
    vertical-align: middle;
}
.structured-not-helpful-reason-list li label {
    color: #000000;
    height: 20px;
    line-height: 20px;
    vertical-align: middle;
}




--></style>








<link rel="stylesheet" type="text/css" href="http://z-ecx.images-amazon.com/images/G/01/browser-scripts/fruitCSS/US-combined-2621868138._V375438499_.css" />






</head>
<body>
<!-- BeginNav -->
<!-- From remote config --><style type="text/css"><!--
.nav-sprite {
  background-image: url(http://g-ecx.images-amazon.com/images/G/01/gno/beacon/BeaconSprite-US-01._V397411194_.png);
}
.nav_pop_h {
  background-image: url(http://g-ecx.images-amazon.com/images/G/01/gno/beacon/nav-pop-h-v2._V137157005_.png);
}
.nav_pop_v {
  background-image: url(http://g-ecx.images-amazon.com/images/G/01/gno/beacon/nav-pop-v-v2._V137157005_.png);
}
.nav_ie6 .nav_pop_h {
  background-image: url(http://g-ecx.images-amazon.com/images/G/01/gno/beacon/nav-pop-8bit-h._V155961234_.png);
}
.nav_ie6 .nav_pop_v {
  background-image: url(http://g-ecx.images-amazon.com/images/G/01/gno/beacon/nav-pop-8bit-v._V155961234_.png);
}
.nav-ajax-loading .nav-ajax-message {
  background: center center url(http://g-ecx.images-amazon.com/images/G/01/javascripts/lib/popover/images/snake._V192571611_.gif) no-repeat;
}
.iss-sprite {
  background-image: url(http://g-ecx.images-amazon.com/images/G/01/nav2/images/gui/beacon-sprite._V391206562_.png);
}
--></style>
<!-- From remote config v3-->
<script type="text/javascript"><!--
(function(d){var e=function(d){function b(f,c,b){f[b]=function(){a._replay.push(c.concat({m:b,a:[].slice.call(arguments)}))}}var a={};a._sourceName=d;a._replay=[];a.getNow=function(a,b){return b};a.when=function(){var a=[{m:"when",a:[].slice.call(arguments)}],c={};b(c,a,"run");b(c,a,"declare");b(c,a,"publish");b(c,a,"build");return c};b(a,[],"declare");b(a,[],"build");b(a,[],"publish");b(a,[],"importEvent");e._shims.push(a);return a};e._shims=[];if(!d.$Nav)d.$Nav=e("rcx-nav");if(!d.$Nav.make)d.$Nav.make=
e})(window);window.$Nav.when("exposeSBD.enable","img.horz","img.vert","img.spin","$popover","btf.full").run(function(d,e,j,b){function a(a){switch(typeof a){case "boolean":h=a;i=!0;break;case "function":g=a;c++;break;default:c++}i&&c>2&&g(h)}function f(a,b){var c=new Image;if(b)c.onload=b;c.src=a;return c}var c=0,g,h,i=!1;f(e,d&&a);f(j,d&&a);window.$Nav.declare("protectExposeSBD",a);window.$Nav.declare("preloadSpinner",function(){f(b)})});
window.amznJQ && amznJQ.available('navbarJS-beacon', function(){});
window._navbarSpriteUrl = 'http://g-ecx.images-amazon.com/images/G/01/gno/beacon/BeaconSprite-US-01._V397411194_.png';
$Nav.importEvent('navbarJS-beacon');
$Nav.importEvent('NavAuiJS');
$Nav.declare('exposeSBD.enable',false);
$Nav.declare('img.spin','http://g-ecx.images-amazon.com/images/G/01/javascripts/lib/popover/images/snake._V192571611_.gif');
$Nav.when('$').run(function($){
  var ie6 = $.browser.msie && parseInt($.browser.version) <= 6;
  $Nav.declare('img.horz', ie6 ?
    'http://g-ecx.images-amazon.com/images/G/01/gno/beacon/nav-pop-8bit-h._V155961234_.png' :
    'http://g-ecx.images-amazon.com/images/G/01/gno/beacon/nav-pop-h-v2._V137157005_.png');
  $Nav.declare('img.vert', ie6 ?
    'http://g-ecx.images-amazon.com/images/G/01/gno/beacon/nav-pop-8bit-v._V155961234_.png' :
    'http://g-ecx.images-amazon.com/images/G/01/gno/beacon/nav-pop-v-v2._V137157005_.png');
});
--></script>
<img src="http://g-ecx.images-amazon.com/images/G/01/gno/beacon/BeaconSprite-US-01._V397411194_.png" style="display:none" alt=""/>
<img src="http://g-ecx.images-amazon.com/images/G/01/x-locale/common/transparent-pixel._V386942464_.gif" style="display:none" alt="" id="nav_trans_pixel"/>
























<!--Pilu -->



<script type='text/javascript'><!--
    window.Navbar = function(options) {
      options = options || {};

      this._loadedCount = 0;
      this._hasUedata = (typeof uet == 'function');
      this._finishLoadQuota = options['finishLoadQuota'] || 2;
      this._startedLoading = false;

      this._btfFlyoutContents = [];

      this._saFlyoutHorizOffset = -16;
      this._saMaskHorizOffset = -17;

      this._sbd_config = {
        major_delay: 300,
        minor_delay: 100,
        target_slop: 25
      };
      window.$Nav && $Nav.declare('config.sbd', this._sbd_config);

      this.addToBtfFlyoutContents = function(content, callback) {
        this._btfFlyoutContents.push({content: content, callback: callback});
      }

      this.getBtfFlyoutContents = function() {
        return this._btfFlyoutContents;
      }

      this.loading = function() {
        if (!this._startedLoading && this._isReportingEvents()) {
          uet('ns');
        }

        this._startedLoading = true;
      }

      this.componentLoaded = function() {
        this._loadedCount++;
        if (this._startedLoading && this._isReportingEvents() && (this._loadedCount == this._finishLoadQuota)) {
          uet('ne');
        }
      }

      this._isReportingEvents = function() {
        return this._hasUedata;
      }

      this.browsepromos = {};

      this.issPromos = [];

      var le = {};

      this.logEv = function(d, o) {
      }
      window.$Nav && $Nav.declare('logEvent', this.logEv);

    }

    window._navbar = new Navbar({ finishLoadQuota: 1});
    _navbar.loading();


window.$Nav && $Nav.declare('config.lightningDeals', window._navbar._lightningDealsData || {});
window.$Nav && $Nav.declare('config.swmStyleData', window._navbar._swmStyleData || {});
_navbar._ajaxProximity = [141,7,60,150];
window.$Nav && $Nav.declare('config.ajaxProximity', window._navbar._ajaxProximity);

--></script>

  <!-- navp-g1B0pdPqTYhhAbbck/GtFt4jeHQLvoO8qkedbcfxyY37njlkpe0+Ipu5f6vJtyoFxt9HznBW0Ac= rid-0NSY087S35KR62AD2HD9 templated -->
  



  <style type="text/css"><!--
    .nav-searchfield-width {
      padding: 0 2px 0 43px;
    }

    #nav-search-in {
      width: 43px;
    }

  --></style>

<style type="text/css"><!--
    select#searchDropdownBox {
      visibility: visible;
      display: block;
    }
    div.nav-searchfield-width {
      padding-left: 200px;
    }
    span#nav-search-in {
      width: 200px;
    }
    #nav-search-in span#nav-search-in-content {
      display: none;
    }
--></style>

<header>
  <div id='navbar' role="navigation" class='nav-beacon nav-subnav nav-prime-menu nav-logo-large'>

    <div id='nav-cross-shop'>

      <a href='/' id='nav-logo' class='nav_a nav-sprite' alt='Amazon'>
        Amazon
        <span class='nav-prime-tag nav-sprite'></span>
      </a>
      <a href='/gp/prime/signup/videos' id='nav-prime-ttt' class='nav_a'>Join Prime</a>


      <ul id='nav-cross-shop-links' >
                      <li class='nav-xs-link first'><a href='/gp/yourstore/home' class='nav_a' id='nav-your-amazon'>Your Amazon.com</a></li>
                          <li class='nav-xs-link '><a href='/gp/goldbox' class='nav_a'>Today's Deals</a></li>
                          <li class='nav-xs-link '><a href='/b?ie=UTF8&node=3063530011' class='nav_a'>Gift Cards</a></li>
                          <li class='nav-xs-link '><a href='/gp/seller-account/mm-product-page.html?ie=UTF8&ld=AZSOAUSCSNavT' class='nav_a'>Sell</a></li>
                          <li class='nav-xs-link '><a href='/Help/b?ie=UTF8&node=508510' class='nav_a'>Help</a></li>
                    
      </ul>

      
        <div id='welcomeRowTable' style='height:50px'>
        <!--[if IE ]><div class='nav-ie-min-width' style='width: 770px'></div><![endif]-->
        <div id='nav-ad-background-style' style='background-position: -800px 0px; background-image: url(http://g-ecx.images-amazon.com/images/G/01/img13/toys-games/other/6-27_SWM-toys_300x50._V381589622_.jpg);  height: 56px; margin-bottom: -6px; position: relative;background-repeat: no-repeat;'>
          <div id='navSwmSlot'>
            <div id="navSwmHoliday" style="background-image: url(http://g-ecx.images-amazon.com/images/G/01/img13/toys-games/other/6-27_SWM-toys_300x50._V381589622_.jpg); width: 300px; height: 50px; overflow: hidden;"><img alt='Soak Up Summer' src='http://g-ecx.images-amazon.com/images/G/01/x-locale/common/transparent-pixel._V386942464_.gif' border='0' width='300px' height='50px' usemap='#nav-swm-holiday-map' /></div><div style="display: none;"><map id="nav-swm-holiday-map" name="nav-swm-holiday-map"><area shape="rect" coords="1,2,300,50" href ="/b?ie=UTF8&node=5163197011" alt ="Soak Up Summer" /></map></div>
          </div>
        </div>
      </div>

      <div style='clear: both;'></div>
    </div>

    <div id='nav-bar-outer'>

      <div id='nav-logo-borderfade'><div class='nav-fade-mask'></div><div class='nav-fade nav-sprite'></div></div>

      <div id='nav-bar-inner' class='nav-sprite'>

        <a id='nav-shop-all-button' href='/gp/site-directory' class='nav_a nav-button-outer nav-menu-inactive' alt='Shop By Department'>
          <span class='nav-button-mid nav-sprite'>
            <span class='nav-button-inner nav-sprite'>
              <span class='nav-button-title nav-button-line1'>Shop by</span>
              <span class='nav-button-title nav-button-line2'>Department</span>
            </span>
          </span>
          <span class='nav-down-arrow nav-sprite'></span>
        </a>

                  <label id='nav-search-label' for='twotabsearchtextbox'>
            Search
          </label>
        
        <div>
          <form
            action='/s'
            method='get' name='site-search'
            class='nav-searchbar-inner'
            role='search'
            accept-charset='utf-8'
          >
          

            <span id='nav-search-in' class='nav-sprite'>
              <span id='nav-search-in-content' data-value="search-alias=aps">
                All
              </span>
              <span class='nav-down-arrow nav-sprite'></span>
              <select data-nav-digest="0hnIRNWe1w1v7yzkl1voILPQhsM" data-nav-sel
ected="0"  name="url" id="searchDropdownBox" class="searchSelect" title="Search 
in"   ><option value="search-alias=aps" selected="selected">All Departments</opt
ion><option value="search-alias=instant-video">Amazon Instant Video</option><opt
ion value="search-alias=appliances">Appliances</option><option value="search-ali
as=mobile-apps">Apps for Android</option><option value="search-alias=arts-crafts
">Arts, Crafts & Sewing</option><option value="search-alias=automotive">Automoti
ve</option><option value="search-alias=baby-products">Baby</option><option value
="search-alias=beauty">Beauty</option><option value="search-alias=stripbooks">Bo
oks</option><option value="search-alias=mobile">Cell Phones & Accessories</optio
n><option value="search-alias=apparel">Clothing & Accessories</option><option va
lue="search-alias=collectibles">Collectibles</option><option value="search-alias
=computers">Computers</option><option value="search-alias=financial">Credit Card
s</option><option value="search-alias=electronics">Electronics</option><option v
alue="search-alias=gift-cards">Gift Cards Store</option><option value="search-al
ias=grocery">Grocery & Gourmet Food</option><option value="search-alias=hpc">Hea
lth & Personal Care</option><option value="search-alias=garden">Home & Kitchen</
option><option value="search-alias=industrial">Industrial & Scientific</option><
option value="search-alias=jewelry">Jewelry</option><option value="search-alias=
digital-text">Kindle Store</option><option value="search-alias=magazines">Magazi
ne Subscriptions</option><option value="search-alias=movies-tv">Movies & TV</opt
ion><option value="search-alias=digital-music">MP3 Music</option><option value="
search-alias=popular">Music</option><option value="search-alias=mi">Musical Inst
ruments</option><option value="search-alias=office-products">Office Products</op
tion><option value="search-alias=lawngarden">Patio, Lawn & Garden</option><optio
n value="search-alias=pets">Pet Supplies</option><option value="search-alias=sho
es">Shoes</option><option value="search-alias=software">Software</option><option
 value="search-alias=sporting">Sports & Outdoors</option><option value="search-a
lias=tools">Tools & Home Improvement</option><option value="search-alias=toys-an
d-games">Toys & Games</option><option value="search-alias=videogames">Video Game
s</option><option value="search-alias=watches">Watches</option></select>
            </span>

            <div class='nav-searchfield-outer nav-sprite'>
              <div class='nav-searchfield-inner nav-sprite'>
                <div class='nav-searchfield-width'>
                  <div id='nav-iss-attach'>
                    <input type='text' id='twotabsearchtextbox' title='Search For' value='' name='field-keywords' autocomplete='off'>
                  </div>
                </div>
                <!--[if IE ]><div class='nav-ie-min-width' style='width: 360px'></div><![endif]-->
              </div>
            </div>

            <div class='nav-submit-button nav-sprite'>
              <input
                type='submit'
                value='Go'
                class='nav-submit-input'
                title='Go'
              >
            </div>

          </form>
        </div>

        <a id='nav-your-account' href='https://www.amazon.com/ap/signin?_encoding=UTF8&openid.assoc_handle=usflex&openid.claimed_id=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.identity=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.mode=checkid_setup&openid.ns=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0&openid.ns.pape=http%3A%2F%2Fspecs.openid.net%2Fextensions%2Fpape%2F1.0&openid.pape.max_auth_age=0&openid.return_to=https%3A%2F%2Fwww.amazon.com%2Fgp%2Fcss%2Fhomepage.html%3Fie%3DUTF8%26ref_%3Dgno_yam_ya' class='nav_a nav-button-outer nav-menu-inactive' alt='Your Account'>
          <span class='nav-button-mid nav-sprite'>
            <span class='nav-button-inner nav-sprite'>
              <span id='nav-signin-title' class='nav-button-title nav-button-line1'  >
                Hello.
                <span id='nav-signin-text' class='nav-button-em'>Sign in</span>
              </span>
              <span class='nav-button-title nav-button-line2'>Your Account</span>
            </span>
          </span>
          <span class='nav-down-arrow nav-sprite'></span>
        </a>

          <span class='nav-divider nav-divider-prime'></span>

          <a id='nav-your-prime' href='/gp/prime/signup/videos' class='nav_a nav-button-outer nav-menu-inactive' alt='Join Prime'>
            <span class='nav-button-mid nav-sprite'>
              <span class='nav-button-inner nav-sprite'>
                <span class='nav-button-title nav-button-line1'>Join</span>
                <span class='nav-button-title nav-button-line2'>Prime</span>
              </span>
            </span>
            <span class='nav-down-arrow nav-sprite'></span>
          </a>

          <span class='nav-divider nav-divider-account'></span>

          <a id='nav-cart' href='/gp/cart/view.html' class='nav_a nav-button-outer nav-menu-inactive' alt='Shopping Cart'>
            <span class='nav-button-mid nav-sprite'>
              <span class='nav-button-inner nav-sprite'>

                <span class='nav-button-title nav-button-line1'> </span>
                <span class='nav-button-title nav-button-line2'>Cart</span>

                <span class='nav-cart-button nav-sprite'></span>
                <span id='nav-cart-count' class='nav-cart-0'>0</span>

              </span>
            </span>
            <span class='nav-down-arrow nav-sprite'></span>
          </a>

          <span class='nav-divider nav-divider-cart'></span>

          <a id='nav-wishlist' href='/gp/registry/wishlist' class='nav_a nav-button-outer nav-menu-inactive' alt='Wish List'>
            <span class='nav-button-mid nav-sprite'>
              <span class='nav-button-inner nav-sprite'>
                <span class='nav-button-title nav-button-line1'>Wish</span>
                <span class='nav-button-title nav-button-line2'>List</span>
              </span>
            </span>
            <span class='nav-down-arrow nav-sprite'></span>
          </a>

          <!-- nav-linktree-category -->
          <!-- nav-linktree-subnav -->
          <ul id='nav-subnav' data-digest='Wyx21Z+slTMg4nexefD0K+zGKcE'>
            <li class='nav-subnav-item nav-category-button'>
              <a href='/computer-pc-hardware-accessories-add-ons/b?ie=UTF8&node=541966' class='nav_a'>
                Computers
              </a>
            </li>

                <li class="nav-subnav-item">
                  <a href='/Computers/b?ie=UTF8&node=565118' class='nav_a'>
                   Brands
                  </a>
                </li>
                <li class="nav-subnav-item">
                  <a href='/gp/bestsellers/pc/541966' class='nav_a'>
                   Best Sellers
                  </a>
                </li>
                <li class="nav-subnav-item">
                  <a href='/Laptops-Tablets/b?ie=UTF8&node=2956501011' class='nav_a'>
                   Laptops &amp;&nbsp;Tablets
                  </a>
                </li>
                <li class="nav-subnav-item">
                  <a href='/Desktops/b?ie=UTF8&node=4972214011' class='nav_a'>
                   Desktops &amp;&nbsp;Monitors
                  </a>
                </li>
                <li class="nav-subnav-item">
                  <a href='/Hard-Drives-Storage/b?ie=UTF8&node=2248325011' class='nav_a'>
                   Hard&nbsp;Drives &amp;&nbsp;Storage
                  </a>
                </li>
                <li class="nav-subnav-item">
                  <a href='/Computer-Accessories/b?ie=UTF8&node=2956536011' class='nav_a'>
                   Computer Accessories
                  </a>
                </li>
                <li class="nav-subnav-item">
                  <a href='/Tablet-Accessories/b?ie=UTF8&node=2348628011' class='nav_a'>
                   Tablet Accessories
                  </a>
                </li>
                <li class="nav-subnav-item">
                  <a href='/PC-Parts-Components/b?ie=UTF8&node=193870011' class='nav_a'>
                   PC Components
                  </a>
                </li>
                <li class="nav-subnav-item">
                  <a href='/Printers-Office-Electronics/b?ie=UTF8&node=172635' class='nav_a'>
                   Printers &amp;&nbsp;Ink
                  </a>
                </li>
                <li class="nav-subnav-item">
                  <a href='/Deals-Computers/b?ie=UTF8&node=759498' class='nav_a'>
                   Deals
                  </a>
                </li>

          </ul>

      </div>
    </div>

    
  </div>
</header>




<script type="text/javascript"><!--
_navbar.dynamicMenuUrl = '/gp/navigation/ajax/dynamicmenu.html';
window.$Nav && $Nav.declare('config.dynamicMenuUrl', _navbar.dynamicMenuUrl);

_navbar.dismissNotificationUrl = '/gp/navigation/ajax/dismissnotification.html';
window.$Nav && $Nav.declare('config.dismissNotificationUrl', _navbar.dismissNotificationUrl);

_navbar.dynamicMenus = true;
window.$Nav && $Nav.declare('config.enableDynamicMenus', true);


_navbar.readyOnATF = false;
window.$Nav && $Nav.declare('config.readyOnATF', _navbar.readyOnATF);

_navbar.dynamicMenuArgs = {"isPrime":0,"primeMenuWidth":310};
window.$Nav && $Nav.declare('config.dynamicMenuArgs', _navbar.dynamicMenuArgs || {});

window.$Nav && $Nav.declare('config.signOutText', _navbar.signOutText);

window.$Nav && $Nav.declare('config.yourAccountPrimeURL', _navbar.yourAccountPrimer);

    _navbar._endSpriteImage = new Image();
    _navbar._endSpriteImage.onload = function() {_navbar.componentLoaded(); };
    _navbar._endSpriteImage.src = window._navbarSpriteUrl;

window.$Nav && $Nav.declare('config.autoFocus', false);


window.$Nav && $Nav.declare('config.responsiveGW', !!window._navbar.responsivegw);

    
    window.$Nav && $Nav.declare('config.browsePromos', window._navbar.browsepromos);
    window.amznJQ && amznJQ.declareAvailable('navbarPromosContent');

--></script>

<!--Tilu -->


<!-- EndNav -->


<script language="javascript">
  if (typeof uet == 'function') { uet('af'); }
</script>

<table width="100%" border="0" cellpadding="10" cellspacing="0">
<tr>
<td valign="top">
  
















































  
  











































<h1 class="sans-serif" style="margin:2px 0 0 0; font-size:140%;">
  <div style="color:#CC6600;">
    Customer Reviews
  </div>
  <div style="font-size:80%;text-decoration:underline;">
    






<a href="http://www.amazon.com/Multi-Angles-Leather-Protection-i-UniK-Blue/dp/B007SBGF12">7 Inch Multi-Angles Google Nexus 7 Tablet Leather Protection Case by i-UniK (Light Blue) - Colors Available: Hot Pink, Red, Lime Green, Light Blue, Expresso Black</a>

  </div>
</h1>
<br />
<table id="productSummary" border="0" cellspacing="0" cellpadding="0" width="100%">
  <tr>
    <td width="160">
      <div style="width:160px;">
        











































<div style="display:block; text-align:center; padding-bottom: 5px;" class="tiny">
  <b>62 Reviews</b>
</div>
<table border="0" cellspacing="1" cellpadding="0" align="left">
<tr>
<td align="left" style="padding-right:0.5em;padding-bottom:1px;white-space:nowrap;font-size:10px;">
  5 star:
</td>
<td style="min-width:60; background-color: #eeeecc" width="60" align="left" class="tiny" title="43%"><div style="background-color:#FFCC66; height:13px; width:43%;"></div></td>
<td align="right" style="font-family:Verdana,Arial,Helvetica,Sans-serif;;font-size:10px;">&nbsp;(27)</td>
</tr>
<tr>
<td align="left" style="padding-right:0.5em;padding-bottom:1px;white-space:nowrap;font-size:10px;">
  4 star:
</td>
<td style="min-width:60; background-color: #eeeecc" width="60" align="left" class="tiny" title="19%"><div style="background-color:#FFCC66; height:13px; width:19%;"></div></td>
<td align="right" style="font-family:Verdana,Arial,Helvetica,Sans-serif;;font-size:10px;">&nbsp;(12)</td>
</tr>
<tr>
<td align="left" style="padding-right:0.5em;padding-bottom:1px;white-space:nowrap;font-size:10px;">
  3 star:
</td>
<td style="min-width:60; background-color: #eeeecc" width="60" align="left" class="tiny" title="12%"><div style="background-color:#FFCC66; height:13px; width:12%;"></div></td>
<td align="right" style="font-family:Verdana,Arial,Helvetica,Sans-serif;;font-size:10px;">&nbsp;(8)</td>
</tr>
<tr>
<td align="left" style="padding-right:0.5em;padding-bottom:1px;white-space:nowrap;font-size:10px;">
  2 star:
</td>
<td style="min-width:60; background-color: #eeeecc" width="60" align="left" class="tiny" title="16%"><div style="background-color:#FFCC66; height:13px; width:16%;"></div></td>
<td align="right" style="font-family:Verdana,Arial,Helvetica,Sans-serif;;font-size:10px;">&nbsp;(10)</td>
</tr>
<tr>
<td align="left" style="padding-right:0.5em;padding-bottom:1px;white-space:nowrap;font-size:10px;">
  1 star:
</td>
<td style="min-width:60; background-color: #eeeecc" width="60" align="left" class="tiny" title="8%"><div style="background-color:#FFCC66; height:13px; width:8%;"></div></td>
<td align="right" style="font-family:Verdana,Arial,Helvetica,Sans-serif;;font-size:10px;">&nbsp;(5)</td>
</tr>
<tr><td>&nbsp;</td><td><div style="width:60px;">&nbsp;</div></td><td>&nbsp;</td></tr>
</table>

      </div>
    </td>
    <td width="20"><div style="width:20px;">&nbsp;</div>&nbsp;</td>
    <td valign="top" align="center">
      <div class="tiny" align="left">
        <div>
          <b>Average Customer Review</b>
        </div>
        <div style="white-space:nowrap;">
          <span class="crAvgStars" style="white-space:no-wrap;"><span class="asinReviewsSummary" name="B007SBGF12" ref="pr_all_summary_cm_cr_acr_pop_" >
               <a href="http://www.amazon.com/Multi-Angles-Leather-Protection-i-UniK-Blue/product-reviews/B007SBGF12" ><span class="swSprite s_star_3_5 " title="3.7 out of 5 stars" ><span>3.7 out of 5 stars</span></span></a>&nbsp;</span>(<a href="http://www.amazon.com/Multi-Angles-Leather-Protection-i-UniK-Blue/product-reviews/B007SBGF12" >62 customer reviews</a>)</span>
        </div>
        <div style="margin-top:10px;">
          <div style="margin-bottom:5px;">
            Share your thoughts with other customers
          </div>
          <a class="cmtySprite s_createYourOwnReviewTan " href="http://www.amazon.com/review/create-review?ie=UTF8&asin=B007SBGF12&channel=reviews-product&nodeID=" ><span>Create your own review</span></a>
        </div>
      </div>
    </td>
    <td><div style="width:20px;">&nbsp;</div>&nbsp;</td>
    <td valign="top" width="50%">
          


<div id="cdReviewsAskWidget"></div>

<script>
  amznJQ.onReady('jQuery', function() {
    jQuery(window).load(function() {
      jQuery.ajax({
        url      : '/gp/customer-forum/dynamic-update/reviews-ask-widget-handler.html',
        cache    : false,
        timeout  : 10000,
        dataType : "json",
        data     : { asin : 'B007SBGF12', requestID: '0NSY087S35KR62AD2HD9' },
        success  : function(response) {
                     if (!response.hasError) {
                       jQuery('#cdReviewsAskWidget').html(response.content);
                     }
                   }
      });
    });
  });
</script>



    </td>
  </tr>
</table>






























    








































<div class="cBox secEyebrow">
  <span class="cBoxTL"><!-- &nbsp; --></span>
  <span class="cBoxTR"><!-- &nbsp; --></span>
  <span class="cBoxR"><!-- &nbsp; --></span>
  <span class="cBoxBL"><!-- &nbsp; --></span>
  <span class="cBoxBR"><!-- &nbsp; --></span>
  <span class="cBoxB"><!-- &nbsp; --></span>
  <h2>
        <div class="crVS crLeft">
          The most helpful favorable review
        </div>
        <div class="crVS crRight">
          The most helpful critical review
        </div>
        <br class="crClear" />
      </h2>
  <div class="cBoxInner">
      <table class="viewpointBox" cellspacing="0" cellpadding="0" border="0" style="margin-top: -8px;">
        <tr>
          <td width="46%" valign="top">

















    
    











<!-- BOUNDARY -->
<a name="R1KIN1QMM9MAWN"></a><br />




<div>

      <div style="margin-bottom:0.5em;">
        <div class="tiny" style="">12 of 13 people found the following review helpful</div>
      </div>

        <div>
          <span><span class="swSprite s_star_5_0 " title="5.0 out of 5 stars" ><span>5.0 out of 5 stars</span></span> </span>
          <b>Just what I needed for my Google Nexus 7</b><br />
          The cover actually arrived before my Google Nexus 7, upon receiving my Google tab (Google Play is kind of slow), I have put it on immediately, it fits like a glove inside.<br />Quality: Well built, nice color, looks like photo shown on website, correct ports opening.<br />Functionality: Does the job nicely, hand free viewing both ways.<br />Price: Very reasonable,...
          <div> <a href="http://www.amazon.com/review/R1KIN1QMM9MAWN" title="Read the full review by James Moreno" ><b>Read the full review&nbsp;&rsaquo;</b></a> </div>
        </div>
        <div class="tiny" style="margin-top:5px; clear: both;">
          Published 11 months ago by James Moreno
        </div>

</div>




<br/></td>
          <td width="8%" align="center" valign="middle" style="font-size: 200%; font-weight: bold;
            background: transparent url(http://g-ecx.images-amazon.com/images/G/01/x-locale/communities/reviews/tile-vline._V192249891_.gif) repeat-y scroll
            center;"><img src="http://g-ecx.images-amazon.com/images/G/01/x-locale/communities/reviews/tile-vline-vs._V192249916_.gif" width="33" alt="versus" height="39" border="0" /></td>
          <td width="46%" valign="top">



























<!-- BOUNDARY -->
<a name="R4L02T5HZRFMY"></a><br />




<div>

      <div style="margin-bottom:0.5em;">
        <div class="tiny" style="">2 of 2 people found the following review helpful</div>
      </div>

        <div>
          <span><span class="swSprite s_star_2_0 " title="2.0 out of 5 stars" ><span>2.0 out of 5 stars</span></span> </span>
          <b>Shuts off device for me too.</b><br />
          I am having the same issue as the other review who found that it shuts off their device.  Nexus 7 shuts off at random times when using this case. Often, can not even turn the Nexus on, when you swipe the lock to the edge of the circle and let go it flashes on, then turns off immediately. It was baffling for a while, how on earth can a case be responsible for this? But...
          <div> <a href="http://www.amazon.com/review/R4L02T5HZRFMY" title="Read the full review by J. Skeoch" ><b>Read the full review&nbsp;&rsaquo;</b></a> </div>
        </div>
        <div class="tiny" style="margin-top:5px; clear: both;">
          Published 6 months ago by J. Skeoch
        </div>

</div>




<br/></td>
        </tr>
      </table></div>
</div>  


<br/>





















    














  





























































    





































<table class="CMheadingBar" border="0" cellpadding="0" cellspacing="0" width="100%">
  <tr>
    <td height="16" align="left" style="padding-left:4px;padding-right:4px;">
      <div class="CMpaginate" style="white-space:nowrap;">
        <span class="paging">&lsaquo; Previous |    <span class="on">1</span> <a href="http://www.amazon.com/Multi-Angles-Leather-Protection-i-UniK-Blue/product-reviews/B007SBGF12?pageNumber=2" >2</a> &hellip; <a href="http://www.amazon.com/Multi-Angles-Leather-Protection-i-UniK-Blue/product-reviews/B007SBGF12?pageNumber=7" >7</a>| <a href="http://www.amazon.com/Multi-Angles-Leather-Protection-i-UniK-Blue/product-reviews/B007SBGF12?pageNumber=2" >Next &rsaquo;</a> </span>
      </div>
    </td>
    <td height="16" align="right" style="padding-right:4px;">
      <div class="" style="white-space:nowrap;">
        <b class="on">Most Helpful First</b> | <b class="on">Newest First</b>
      </div>
    </td>
  </tr>
</table>


<table id="productReviews" width="100%" cellspacing="0" cellpadding="0">
<tr>
  <td width="90%">
    



























    
































<!-- BOUNDARY -->
<a name="R1KIN1QMM9MAWN"></a><br />


<div style="margin-left:0.5em;">
    
      <div style="margin-bottom:0.5em;">
        12 of 13 people found the following review helpful
      </div>
      <div style="margin-bottom:0.5em;">
        <span style="margin-right:5px;"><span class="swSprite s_star_5_0 " title="5.0 out of 5 stars" ><span>5.0 out of 5 stars</span></span> </span>
        <span style="vertical-align:middle;"><b>Just what I needed for my Google Nexus 7</b>, <nobr>July 19, 2012</nobr></span>
      </div>
      <div style="margin-bottom:0.5em;">
        <div><div style="float:left;">By&nbsp;</div><div style="float:left;"><a href="/gp/pdp/profile/A24XSZGSFS4KO8" ><span style = "font-weight: bold;">James Moreno</span></a>  - <a href="/gp/cdp/member-reviews/A24XSZGSFS4KO8?ie=UTF8&amp;sort_by=MostRecentReview">See all my reviews</a></div></div><div style="clear:both;"></div>
      </div>
      <div class="tiny" style="margin-bottom:0.5em;">
        <span class="crVerifiedStripe"><b class="h3color tiny" style="margin-right: 0.5em;">Amazon Verified Purchase</b><span class="tiny verifyWhatsThis">(<a href="http://www.amazon.com/gp/community-help/amazon-verified-purchase" target="AmazonHelp" onclick="amz_js_PopWin('http://www.amazon.com/gp/community-help/amazon-verified-purchase', 'AmazonHelp', 'width=400,height=500,resizable=1,scrollbars=1,toolbar=0,status=1');return false; ">What's this?</a>)</span></span>
      </div>
      <div class="tiny" style="margin-bottom:0.5em;">
        <b><span class="h3color tiny">This review is from: </span>7 Inch Multi-Angles Google Nexus 7 Tablet Leather Protection Case by i-UniK (Light Blue) - Colors Available: Hot Pink, Red, Lime Green, Light Blue, Expresso Black (Personal Computers)</b>
      </div>

The cover actually arrived before my Google Nexus 7, upon receiving my Google tab (Google Play is kind of slow), I have put it on immediately, it fits like a glove inside.<br />Quality: Well built, nice color, looks like photo shown on website, correct ports opening.<br />Functionality: Does the job nicely, hand free viewing both ways.<br />Price: Very reasonable, shipping was prompt.<br />Weight: Not bulky at all, great to carry around.<br />Verdict: Good buy, I won't spend too much on a tablet that cost even less than my smartphone!
      <div style="padding-top: 10px; clear: both; width: 100%;">

        <div class="reviews-voting-stripe" style="float:left; padding-right:15px; border-right:1px solid #CCCCCC"><div style="padding-bottom:5px;"><b class="tiny" style="color:#666666;white-space:nowrap;">Help other customers find the most helpful reviews</b>&nbsp;</div><div style="width:300px;">









<a name="R1KIN1QMM9MAWN.2115.Helpful.Reviews" style="font-size:1px;"> </a><span
class="crVotingButtons"><nobr><span class="votingPrompt">Was this review helpful to you?&nbsp;</span><a rel="nofollow" class="votingButtonReviews yesButton" href="http://www.amazon.com/gp/voting/cast/Reviews/2115/R1KIN1QMM9MAWN/Helpful/1?ie=UTF8&target=aHR0cDovL3d3dy5hbWF6b24uY29tL3Jldmlldy9CMDA3U0JHRjEy&token=AACD2B0CBE7BE09E33EB59704FB77E860F66CF09&voteAnchorName=R1KIN1QMM9MAWN.2115.Helpful.Reviews&voteSessionID=000-0000000-0000000"><span class="cmtySprite s_largeYes " ><span>Yes</span></span></a>
<a rel="nofollow" class="votingButtonReviews noButton" href="http://www.amazon.com/gp/voting/cast/Reviews/2115/R1KIN1QMM9MAWN/Helpful/-1?ie=UTF8&target=aHR0cDovL3d3dy5hbWF6b24uY29tL3Jldmlldy9CMDA3U0JHRjEy&token=AF19C28DD1A32CEBDD6361C06279AEE689FB00F5&voteAnchorName=R1KIN1QMM9MAWN.2115.Helpful.Reviews&voteSessionID=000-0000000-0000000"><span class="cmtySprite s_largeNo " ><span>No</span></span></a></nobr> <span class="votingMessage"></span></span>

</div></div><div style="float:left;"><div style="padding-left:15px;"><div style="white-space:nowrap;"><span class='tiny'>








<a name="R1KIN1QMM9MAWN.2115.Inappropriate.Reviews" style="font-size:1px;"> </a><span class="reportingButton"><nobr><a rel="nofollow" class="reportingButton" href="http://www.amazon.com/gp/voting/cast/Reviews/2115/R1KIN1QMM9MAWN/Inappropriate/1?ie=UTF8&target=aHR0cDovL3d3dy5hbWF6b24uY29tL3Jldmlldy9CMDA3U0JHRjEy&token=E7977BC2E8315436F6B4A3EB3EF902427F5C8F9E&voteAnchorName=R1KIN1QMM9MAWN.2115.Inappropriate.Reviews&voteSessionID=000-0000000-0000000"
>Report abuse</a></nobr></span>
</span> <span style="color:#CCCCCC;">|</span> <span class="tiny"><a href="http://www.amazon.com/review/R1KIN1QMM9MAWN" >Permalink</a></span></div><div style="white-space:nowrap;padding-left:-5px;padding-top:5px;"><a href="http://www.amazon.com/review/R1KIN1QMM9MAWN" ><span class="swSprite s_comment " ><span>Comment</span></span></a>&nbsp;<a href="http://www.amazon.com/review/R1KIN1QMM9MAWN" >Comment (1)</a></div></div></div><div style="clear:both;"></div>
      </div>
      <br />

</div>

  














































<!-- BOUNDARY -->
<a name="R2ER2U6PI18CYH"></a><br />


<div style="margin-left:0.5em;">
    
      <div style="margin-bottom:0.5em;">
        9 of 10 people found the following review helpful
      </div>
      <div style="margin-bottom:0.5em;">
        <span style="margin-right:5px;"><span class="swSprite s_star_5_0 " title="5.0 out of 5 stars" ><span>5.0 out of 5 stars</span></span> </span>
        <span style="vertical-align:middle;"><b>Great color, nice case</b>, <nobr>July 20, 2012</nobr></span>
      </div>
      <div style="margin-bottom:0.5em;">
        <div><div style="float:left;">By&nbsp;</div><div style="float:left;"><a href="/gp/pdp/profile/A1PZBIHQ4FFT53" ><span style = "font-weight: bold;">Devin Cotton</span></a>  - <a href="/gp/cdp/member-reviews/A1PZBIHQ4FFT53?ie=UTF8&amp;sort_by=MostRecentReview">See all my reviews</a></div></div><div style="clear:both;"></div>
      </div>
      <div class="tiny" style="margin-bottom:0.5em;">
        <span class="crVerifiedStripe"><b class="h3color tiny" style="margin-right: 0.5em;">Amazon Verified Purchase</b><span class="tiny verifyWhatsThis">(<a href="http://www.amazon.com/gp/community-help/amazon-verified-purchase" target="AmazonHelp" onclick="amz_js_PopWin('http://www.amazon.com/gp/community-help/amazon-verified-purchase', 'AmazonHelp', 'width=400,height=500,resizable=1,scrollbars=1,toolbar=0,status=1');return false; ">What's this?</a>)</span></span>
      </div>
      <div class="tiny" style="margin-bottom:0.5em;">
        <b><span class="h3color tiny">This review is from: </span><a href="http://www.amazon.com/Multi-Angles-Google-Leather-Protection-i-UniK/dp/B007SBGF1C">7 Inch Multi-Angles Google Nexus 7 Tablet Leather Protection Case by i-UniK (Lime Green) - Colors Available: Hot Pink, Red, Lime Green, Light Blue, Expresso Black (Personal Computers)</a></b>
      </div>

Received this case in no time, I ordered a green color case because that is my lucky color. First off, the case are made of pretty decent materials, I am well aware that is not real leather but surprising the quality of the PU leather is not bad with the price tag. It is detachable, can be used both with the base or without it; I have tried to view the tablet in both directions and so far so good. There is a strap in the front for you to secure the front cover. It has all the openings in place, no strange order and no loosen stitches. Will post a following review shortly afterward.
      <div style="padding-top: 10px; clear: both; width: 100%;">

        <div class="reviews-voting-stripe" style="float:left; padding-right:15px; border-right:1px solid #CCCCCC"><div style="padding-bottom:5px;"><b class="tiny" style="color:#666666;white-space:nowrap;">Help other customers find the most helpful reviews</b>&nbsp;</div><div style="width:300px;">









<a name="R2ER2U6PI18CYH.2115.Helpful.Reviews" style="font-size:1px;"> </a><span
class="crVotingButtons"><nobr><span class="votingPrompt">Was this review helpful to you?&nbsp;</span><a rel="nofollow" class="votingButtonReviews yesButton" href="http://www.amazon.com/gp/voting/cast/Reviews/2115/R2ER2U6PI18CYH/Helpful/1?ie=UTF8&target=aHR0cDovL3d3dy5hbWF6b24uY29tL3Jldmlldy9CMDA3U0JHRjEy&token=DE7EA14C843C27F5C68D225C5DE66727FB0EEAD6&voteAnchorName=R2ER2U6PI18CYH.2115.Helpful.Reviews&voteSessionID=000-0000000-0000000"><span class="cmtySprite s_largeYes " ><span>Yes</span></span></a>
<a rel="nofollow" class="votingButtonReviews noButton" href="http://www.amazon.com/gp/voting/cast/Reviews/2115/R2ER2U6PI18CYH/Helpful/-1?ie=UTF8&target=aHR0cDovL3d3dy5hbWF6b24uY29tL3Jldmlldy9CMDA3U0JHRjEy&token=25D48C73AEC63B68A4C29CE29E6079A86FB02159&voteAnchorName=R2ER2U6PI18CYH.2115.Helpful.Reviews&voteSessionID=000-0000000-0000000"><span class="cmtySprite s_largeNo " ><span>No</span></span></a></nobr> <span class="votingMessage"></span></span>

</div></div><div style="float:left;"><div style="padding-left:15px;"><div style="white-space:nowrap;"><span class='tiny'>








<a name="R2ER2U6PI18CYH.2115.Inappropriate.Reviews" style="font-size:1px;"> </a><span class="reportingButton"><nobr><a rel="nofollow" class="reportingButton" href="http://www.amazon.com/gp/voting/cast/Reviews/2115/R2ER2U6PI18CYH/Inappropriate/1?ie=UTF8&target=aHR0cDovL3d3dy5hbWF6b24uY29tL3Jldmlldy9CMDA3U0JHRjEy&token=0EB4B209EDED7642D552060A007D522DD5DD1A56&voteAnchorName=R2ER2U6PI18CYH.2115.Inappropriate.Reviews&voteSessionID=000-0000000-0000000"
>Report abuse</a></nobr></span>
</span> <span style="color:#CCCCCC;">|</span> <span class="tiny"><a href="http://www.amazon.com/review/R2ER2U6PI18CYH" >Permalink</a></span></div><div style="white-space:nowrap;padding-left:-5px;padding-top:5px;"><a href="http://www.amazon.com/review/R2ER2U6PI18CYH" ><span class="swSprite s_comment " ><span>Comment</span></span></a>&nbsp;<a href="http://www.amazon.com/review/R2ER2U6PI18CYH" >Comment</a></div></div></div><div style="clear:both;"></div>
      </div>
      <br />

</div>

  
































































<!-- BOUNDARY -->
<a name="R36MT6BMBDRAH7"></a><br />


<div style="margin-left:0.5em;">
    
      <div style="margin-bottom:0.5em;">
        6 of 6 people found the following review helpful
      </div>
      <div style="margin-bottom:0.5em;">
        <span style="margin-right:5px;"><span class="swSprite s_star_5_0 " title="5.0 out of 5 stars" ><span>5.0 out of 5 stars</span></span> </span>
        <span style="vertical-align:middle;"><b>Perfect!</b>, <nobr>August 22, 2012</nobr></span>
      </div>
      <div style="margin-bottom:0.5em;">
        <div><div style="float:left;">By&nbsp;</div><div style="float:left;"><a href="/gp/pdp/profile/A2RBIF8RQI04PO" ><span style = "font-weight: bold;">V. Evans "torybug"</span></a> (Baltimore, Maryland)  - <a href="/gp/cdp/member-reviews/A2RBIF8RQI04PO?ie=UTF8&amp;sort_by=MostRecentReview">See all my reviews</a><br />
<a href="http://www.amazon.com/gp/help/customer/display.html?ie=UTF8&nodeId=14279681&pop-up=1#RN" target="AmazonHelp" onclick="return amz_js_PopWin(this.href,'AmazonHelp','width=340,height=340,resizable=1,scrollbars=1,toolbar=1,status=1');"  ><span class="cmtySprite s_BadgeRealName " ><span>(REAL NAME)</span></span></a>
&nbsp;&nbsp;


</div></div><div style="clear:both;"></div>
      </div>
      <div class="tiny" style="margin-bottom:0.5em;">
        <span class="crVerifiedStripe"><b class="h3color tiny" style="margin-right: 0.5em;">Amazon Verified Purchase</b><span class="tiny verifyWhatsThis">(<a href="http://www.amazon.com/gp/community-help/amazon-verified-purchase" target="AmazonHelp" onclick="amz_js_PopWin('http://www.amazon.com/gp/community-help/amazon-verified-purchase', 'AmazonHelp', 'width=400,height=500,resizable=1,scrollbars=1,toolbar=0,status=1');return false; ">What's this?</a>)</span></span>
      </div>
      <div class="tiny" style="margin-bottom:0.5em;">
        <b><span class="h3color tiny">This review is from: </span>7 Inch Multi-Angles Google Nexus 7 Tablet Leather Protection Case by i-UniK (Light Blue) - Colors Available: Hot Pink, Red, Lime Green, Light Blue, Expresso Black (Personal Computers)</b>
      </div>

This is exactly what I needed for my new Nexus 7.  It fits perfectly, with holes in all the right spots for headphones, the camera, etc.  I was looking for a fancy dock, but this and a pair of cheap speakers I already have gave me exactly what I needed to watch youtube while I do the dishes!  Can't beat it for the price and I really like the light blue color.
      <div style="padding-top: 10px; clear: both; width: 100%;">

        <div class="reviews-voting-stripe" style="float:left; padding-right:15px; border-right:1px solid #CCCCCC"><div style="padding-bottom:5px;"><b class="tiny" style="color:#666666;white-space:nowrap;">Help other customers find the most helpful reviews</b>&nbsp;</div><div style="width:300px;">









<a name="R36MT6BMBDRAH7.2115.Helpful.Reviews" style="font-size:1px;"> </a><span
class="crVotingButtons"><nobr><span class="votingPrompt">Was this review helpful to you?&nbsp;</span><a rel="nofollow" class="votingButtonReviews yesButton" href="http://www.amazon.com/gp/voting/cast/Reviews/2115/R36MT6BMBDRAH7/Helpful/1?ie=UTF8&target=aHR0cDovL3d3dy5hbWF6b24uY29tL3Jldmlldy9CMDA3U0JHRjEy&token=BAEB89C21DA55E8EF2D9724F24CB2EE228DBEDE5&voteAnchorName=R36MT6BMBDRAH7.2115.Helpful.Reviews&voteSessionID=000-0000000-0000000"><span class="cmtySprite s_largeYes " ><span>Yes</span></span></a>
<a rel="nofollow" class="votingButtonReviews noButton" href="http://www.amazon.com/gp/voting/cast/Reviews/2115/R36MT6BMBDRAH7/Helpful/-1?ie=UTF8&target=aHR0cDovL3d3dy5hbWF6b24uY29tL3Jldmlldy9CMDA3U0JHRjEy&token=1A191C2CA8CBD7201358382823DBCEC8D074E5A6&voteAnchorName=R36MT6BMBDRAH7.2115.Helpful.Reviews&voteSessionID=000-0000000-0000000"><span class="cmtySprite s_largeNo " ><span>No</span></span></a></nobr> <span class="votingMessage"></span></span>

</div></div><div style="float:left;"><div style="padding-left:15px;"><div style="white-space:nowrap;"><span class='tiny'>








<a name="R36MT6BMBDRAH7.2115.Inappropriate.Reviews" style="font-size:1px;"> </a><span class="reportingButton"><nobr><a rel="nofollow" class="reportingButton" href="http://www.amazon.com/gp/voting/cast/Reviews/2115/R36MT6BMBDRAH7/Inappropriate/1?ie=UTF8&target=aHR0cDovL3d3dy5hbWF6b24uY29tL3Jldmlldy9CMDA3U0JHRjEy&token=7B1D8B74702E8D4B0B8619384DA53CFD225C2844&voteAnchorName=R36MT6BMBDRAH7.2115.Inappropriate.Reviews&voteSessionID=000-0000000-0000000"
>Report abuse</a></nobr></span>
</span> <span style="color:#CCCCCC;">|</span> <span class="tiny"><a href="http://www.amazon.com/review/R36MT6BMBDRAH7" >Permalink</a></span></div><div style="white-space:nowrap;padding-left:-5px;padding-top:5px;"><a href="http://www.amazon.com/review/R36MT6BMBDRAH7" ><span class="swSprite s_comment " ><span>Comment</span></span></a>&nbsp;<a href="http://www.amazon.com/review/R36MT6BMBDRAH7" >Comment</a></div></div></div><div style="clear:both;"></div>
      </div>
      <br />

</div>

  
























































<!-- BOUNDARY -->
<a name="R1NICTUHMR1M2M"></a><br />


<div style="margin-left:0.5em;">
    
      <div style="margin-bottom:0.5em;">
        6 of 7 people found the following review helpful
      </div>
      <div style="margin-bottom:0.5em;">
        <span style="margin-right:5px;"><span class="swSprite s_star_4_0 " title="4.0 out of 5 stars" ><span>4.0 out of 5 stars</span></span> </span>
        <span style="vertical-align:middle;"><b>Works OK</b>, <nobr>September 6, 2012</nobr></span>
      </div>
      <div style="margin-bottom:0.5em;">
        <div><div style="float:left;">By&nbsp;</div><div style="float:left;"><a href="/gp/pdp/profile/A37DZUY9XPHGRA" ><span style = "font-weight: bold;">J. Fried</span></a>  - <a href="/gp/cdp/member-reviews/A37DZUY9XPHGRA?ie=UTF8&amp;sort_by=MostRecentReview">See all my reviews</a><br />
<a href="http://www.amazon.com/gp/help/customer/display.html?ie=UTF8&nodeId=14279681&pop-up=1#RN" target="AmazonHelp" onclick="return amz_js_PopWin(this.href,'AmazonHelp','width=340,height=340,resizable=1,scrollbars=1,toolbar=1,status=1');"  ><span class="cmtySprite s_BadgeRealName " ><span>(REAL NAME)</span></span></a>
&nbsp;&nbsp;


</div></div><div style="clear:both;"></div>
      </div>
      <div class="tiny" style="margin-bottom:0.5em;">
        <span class="crVerifiedStripe"><b class="h3color tiny" style="margin-right: 0.5em;">Amazon Verified Purchase</b><span class="tiny verifyWhatsThis">(<a href="http://www.amazon.com/gp/community-help/amazon-verified-purchase" target="AmazonHelp" onclick="amz_js_PopWin('http://www.amazon.com/gp/community-help/amazon-verified-purchase', 'AmazonHelp', 'width=400,height=500,resizable=1,scrollbars=1,toolbar=0,status=1');return false; ">What's this?</a>)</span></span>
      </div>
      <div class="tiny" style="margin-bottom:0.5em;">
        <b><span class="h3color tiny">This review is from: </span><a href="http://www.amazon.com/Multi-Angles-Leather-Protection-i-UniK-Expresso/dp/B007SBGF0S">7 Inch Multi-Angles Google Nexus 7 Tablet Leather Protection Case by i-UniK (Expresso Black) - Colors Available: Hot Pink, Red, Lime Green, Light Blue, Expresso Black (Electronics)</a></b>
      </div>

This case is nothing fancy but works adequately. My Nexus 7 tablet fits snugly in the tablet holder. The snap which connects the tablet holder to the folder swivels a little too easily and the design of the multi angle stand is a little weak. The case does not activate the Nexus 7's automatic Sleep/Wake Function. I'm going to keep this case because it was reasonable priced and fits my current needs but I am considering purchasing a different brand in the future.<br /><br />FYI - this was was available via Amazon Prime 2-day free shipping.  I placed the order for this item at about 12:30 am on a Monday morning and it was on my doorstep on Monday afternoon. Sometimes its nice to live in a town with an Amazon warehouse. I love the convenience of and the range of products available on Amazon and I buy a lot of things from Amazon even though I may regret Amazon's existence one day if online shopping puts brick and mortar retailers out of business.
      <div style="padding-top: 10px; clear: both; width: 100%;">

        <div class="reviews-voting-stripe" style="float:left; padding-right:15px; border-right:1px solid #CCCCCC"><div style="padding-bottom:5px;"><b class="tiny" style="color:#666666;white-space:nowrap;">Help other customers find the most helpful reviews</b>&nbsp;</div><div style="width:300px;">









<a name="R1NICTUHMR1M2M.2115.Helpful.Reviews" style="font-size:1px;"> </a><span
class="crVotingButtons"><nobr><span class="votingPrompt">Was this review helpful to you?&nbsp;</span><a rel="nofollow" class="votingButtonReviews yesButton" href="http://www.amazon.com/gp/voting/cast/Reviews/2115/R1NICTUHMR1M2M/Helpful/1?ie=UTF8&target=aHR0cDovL3d3dy5hbWF6b24uY29tL3Jldmlldy9CMDA3U0JHRjEy&token=0820F968256A16216EB2BBEC3FE39374FDAB68E1&voteAnchorName=R1NICTUHMR1M2M.2115.Helpful.Reviews&voteSessionID=000-0000000-0000000"><span class="cmtySprite s_largeYes " ><span>Yes</span></span></a>
<a rel="nofollow" class="votingButtonReviews noButton" href="http://www.amazon.com/gp/voting/cast/Reviews/2115/R1NICTUHMR1M2M/Helpful/-1?ie=UTF8&target=aHR0cDovL3d3dy5hbWF6b24uY29tL3Jldmlldy9CMDA3U0JHRjEy&token=D33918AC4871CAB4F5BECD50277231BE5CDEB293&voteAnchorName=R1NICTUHMR1M2M.2115.Helpful.Reviews&voteSessionID=000-0000000-0000000"><span class="cmtySprite s_largeNo " ><span>No</span></span></a></nobr> <span class="votingMessage"></span></span>

</div></div><div style="float:left;"><div style="padding-left:15px;"><div style="white-space:nowrap;"><span class='tiny'>








<a name="R1NICTUHMR1M2M.2115.Inappropriate.Reviews" style="font-size:1px;"> </a><span class="reportingButton"><nobr><a rel="nofollow" class="reportingButton" href="http://www.amazon.com/gp/voting/cast/Reviews/2115/R1NICTUHMR1M2M/Inappropriate/1?ie=UTF8&target=aHR0cDovL3d3dy5hbWF6b24uY29tL3Jldmlldy9CMDA3U0JHRjEy&token=35EEDAFE249CFE13368DD3D9A566AC73EE5608FF&voteAnchorName=R1NICTUHMR1M2M.2115.Inappropriate.Reviews&voteSessionID=000-0000000-0000000"
>Report abuse</a></nobr></span>
</span> <span style="color:#CCCCCC;">|</span> <span class="tiny"><a href="http://www.amazon.com/review/R1NICTUHMR1M2M" >Permalink</a></span></div><div style="white-space:nowrap;padding-left:-5px;padding-top:5px;"><a href="http://www.amazon.com/review/R1NICTUHMR1M2M" ><span class="swSprite s_comment " ><span>Comment</span></span></a>&nbsp;<a href="http://www.amazon.com/review/R1NICTUHMR1M2M" >Comment</a></div></div></div><div style="clear:both;"></div>
      </div>
      <br />

</div>

  














































<!-- BOUNDARY -->
<a name="R2JDTD36803IBF"></a><br />


<div style="margin-left:0.5em;">
    
      <div style="margin-bottom:0.5em;">
        3 of 3 people found the following review helpful
      </div>
      <div style="margin-bottom:0.5em;">
        <span style="margin-right:5px;"><span class="swSprite s_star_5_0 " title="5.0 out of 5 stars" ><span>5.0 out of 5 stars</span></span> </span>
        <span style="vertical-align:middle;"><b>Real leather, colorful choices, this protector is doing its job</b>, <nobr>September 6, 2012</nobr></span>
      </div>
      <div style="margin-bottom:0.5em;">
        <div><div style="float:left;">By&nbsp;</div><div style="float:left;"><a href="/gp/pdp/profile/A2ERHE1S3S92X3" ><span style = "font-weight: bold;">Joy R Irvin "Go Bucks!"</span></a> (SE Georgia)  - <a href="/gp/cdp/member-reviews/A2ERHE1S3S92X3?ie=UTF8&amp;sort_by=MostRecentReview">See all my reviews</a></div></div><div style="clear:both;"></div>
      </div>
      <div class="tiny" style="margin-bottom:0.5em;">
        <span class="crVerifiedStripe"><b class="h3color tiny" style="margin-right: 0.5em;">Amazon Verified Purchase</b><span class="tiny verifyWhatsThis">(<a href="http://www.amazon.com/gp/community-help/amazon-verified-purchase" target="AmazonHelp" onclick="amz_js_PopWin('http://www.amazon.com/gp/community-help/amazon-verified-purchase', 'AmazonHelp', 'width=400,height=500,resizable=1,scrollbars=1,toolbar=0,status=1');return false; ">What's this?</a>)</span></span>
      </div>
      <div class="tiny" style="margin-bottom:0.5em;">
        <b><span class="h3color tiny">This review is from: </span><a href="http://www.amazon.com/Multi-Angles-Google-Leather-Protection-i-UniK/dp/B007SBGF1C">7 Inch Multi-Angles Google Nexus 7 Tablet Leather Protection Case by i-UniK (Lime Green) - Colors Available: Hot Pink, Red, Lime Green, Light Blue, Expresso Black (Personal Computers)</a></b>
      </div>

I researched a lot of products on many websites before choosing this. I just purchased a brand new Google Nexus 7 after dropping and rendering useless a less expensive Droid based tablet.  I wanted protection for my new device and I'm a girl - I wanted it to be pretty.  My niece spent $40 at Walmart for a green "leatherette" Nook cover - and I hsve borrowed it a number of times before getting my own tablet.  I like the product I purchased here much better, it has an intelligent design and it is holding up very well.
      <div style="padding-top: 10px; clear: both; width: 100%;">

        <div class="reviews-voting-stripe" style="float:left; padding-right:15px; border-right:1px solid #CCCCCC"><div style="padding-bottom:5px;"><b class="tiny" style="color:#666666;white-space:nowrap;">Help other customers find the most helpful reviews</b>&nbsp;</div><div style="width:300px;">









<a name="R2JDTD36803IBF.2115.Helpful.Reviews" style="font-size:1px;"> </a><span
class="crVotingButtons"><nobr><span class="votingPrompt">Was this review helpful to you?&nbsp;</span><a rel="nofollow" class="votingButtonReviews yesButton" href="http://www.amazon.com/gp/voting/cast/Reviews/2115/R2JDTD36803IBF/Helpful/1?ie=UTF8&target=aHR0cDovL3d3dy5hbWF6b24uY29tL3Jldmlldy9CMDA3U0JHRjEy&token=8939547AA0B02676F4A33D9CCF5E0EAE2CF528CD&voteAnchorName=R2JDTD36803IBF.2115.Helpful.Reviews&voteSessionID=000-0000000-0000000"><span class="cmtySprite s_largeYes " ><span>Yes</span></span></a>
<a rel="nofollow" class="votingButtonReviews noButton" href="http://www.amazon.com/gp/voting/cast/Reviews/2115/R2JDTD36803IBF/Helpful/-1?ie=UTF8&target=aHR0cDovL3d3dy5hbWF6b24uY29tL3Jldmlldy9CMDA3U0JHRjEy&token=1C50A925292253714292A98747AB408B1AA07278&voteAnchorName=R2JDTD36803IBF.2115.Helpful.Reviews&voteSessionID=000-0000000-0000000"><span class="cmtySprite s_largeNo " ><span>No</span></span></a></nobr> <span class="votingMessage"></span></span>

</div></div><div style="float:left;"><div style="padding-left:15px;"><div style="white-space:nowrap;"><span class='tiny'>








<a name="R2JDTD36803IBF.2115.Inappropriate.Reviews" style="font-size:1px;"> </a><span class="reportingButton"><nobr><a rel="nofollow" class="reportingButton" href="http://www.amazon.com/gp/voting/cast/Reviews/2115/R2JDTD36803IBF/Inappropriate/1?ie=UTF8&target=aHR0cDovL3d3dy5hbWF6b24uY29tL3Jldmlldy9CMDA3U0JHRjEy&token=38318DD6283179CBA2F9B00E94EDE8C8A7E72BA9&voteAnchorName=R2JDTD36803IBF.2115.Inappropriate.Reviews&voteSessionID=000-0000000-0000000"
>Report abuse</a></nobr></span>
</span> <span style="color:#CCCCCC;">|</span> <span class="tiny"><a href="http://www.amazon.com/review/R2JDTD36803IBF" >Permalink</a></span></div><div style="white-space:nowrap;padding-left:-5px;padding-top:5px;"><a href="http://www.amazon.com/review/R2JDTD36803IBF" ><span class="swSprite s_comment " ><span>Comment</span></span></a>&nbsp;<a href="http://www.amazon.com/review/R2JDTD36803IBF" >Comment</a></div></div></div><div style="clear:both;"></div>
      </div>
      <br />

</div>

  














































<!-- BOUNDARY -->
<a name="R39RQ6PZQ71DXI"></a><br />


<div style="margin-left:0.5em;">
    
      <div style="margin-bottom:0.5em;">
        5 of 6 people found the following review helpful
      </div>
      <div style="margin-bottom:0.5em;">
        <span style="margin-right:5px;"><span class="swSprite s_star_5_0 " title="5.0 out of 5 stars" ><span>5.0 out of 5 stars</span></span> </span>
        <span style="vertical-align:middle;"><b>Great</b>, <nobr>August 13, 2012</nobr></span>
      </div>
      <div style="margin-bottom:0.5em;">
        <div><div style="float:left;">By&nbsp;</div><div style="float:left;"><a href="/gp/pdp/profile/A24VJVDUO9CWMZ" ><span style = "font-weight: bold;">FARNAM AREZI</span></a> (MARIETTA, GA, US)  - <a href="/gp/cdp/member-reviews/A24VJVDUO9CWMZ?ie=UTF8&amp;sort_by=MostRecentReview">See all my reviews</a></div></div><div style="clear:both;"></div>
      </div>
      <div class="tiny" style="margin-bottom:0.5em;">
        <span class="crVerifiedStripe"><b class="h3color tiny" style="margin-right: 0.5em;">Amazon Verified Purchase</b><span class="tiny verifyWhatsThis">(<a href="http://www.amazon.com/gp/community-help/amazon-verified-purchase" target="AmazonHelp" onclick="amz_js_PopWin('http://www.amazon.com/gp/community-help/amazon-verified-purchase', 'AmazonHelp', 'width=400,height=500,resizable=1,scrollbars=1,toolbar=0,status=1');return false; ">What's this?</a>)</span></span>
      </div>
      <div class="tiny" style="margin-bottom:0.5em;">
        <b><span class="h3color tiny">This review is from: </span><a href="http://www.amazon.com/Multi-Angles-Leather-Protection-i-UniK-Expresso/dp/B007SBGF0S">7 Inch Multi-Angles Google Nexus 7 Tablet Leather Protection Case by i-UniK (Expresso Black) - Colors Available: Hot Pink, Red, Lime Green, Light Blue, Expresso Black (Electronics)</a></b>
      </div>

This is what I was really looking for it. Very good quality, and awesome. Thank you so much for the business.
      <div style="padding-top: 10px; clear: both; width: 100%;">

        <div class="reviews-voting-stripe" style="float:left; padding-right:15px; border-right:1px solid #CCCCCC"><div style="padding-bottom:5px;"><b class="tiny" style="color:#666666;white-space:nowrap;">Help other customers find the most helpful reviews</b>&nbsp;</div><div style="width:300px;">









<a name="R39RQ6PZQ71DXI.2115.Helpful.Reviews" style="font-size:1px;"> </a><span
class="crVotingButtons"><nobr><span class="votingPrompt">Was this review helpful to you?&nbsp;</span><a rel="nofollow" class="votingButtonReviews yesButton" href="http://www.amazon.com/gp/voting/cast/Reviews/2115/R39RQ6PZQ71DXI/Helpful/1?ie=UTF8&target=aHR0cDovL3d3dy5hbWF6b24uY29tL3Jldmlldy9CMDA3U0JHRjEy&token=B339E71EE60C311F96E9F2720CD4BA58D66B67B6&voteAnchorName=R39RQ6PZQ71DXI.2115.Helpful.Reviews&voteSessionID=000-0000000-0000000"><span class="cmtySprite s_largeYes " ><span>Yes</span></span></a>
<a rel="nofollow" class="votingButtonReviews noButton" href="http://www.amazon.com/gp/voting/cast/Reviews/2115/R39RQ6PZQ71DXI/Helpful/-1?ie=UTF8&target=aHR0cDovL3d3dy5hbWF6b24uY29tL3Jldmlldy9CMDA3U0JHRjEy&token=168C87215CFA9010B4B472A5910FBCC0DC33E658&voteAnchorName=R39RQ6PZQ71DXI.2115.Helpful.Reviews&voteSessionID=000-0000000-0000000"><span class="cmtySprite s_largeNo " ><span>No</span></span></a></nobr> <span class="votingMessage"></span></span>

</div></div><div style="float:left;"><div style="padding-left:15px;"><div style="white-space:nowrap;"><span class='tiny'>








<a name="R39RQ6PZQ71DXI.2115.Inappropriate.Reviews" style="font-size:1px;"> </a><span class="reportingButton"><nobr><a rel="nofollow" class="reportingButton" href="http://www.amazon.com/gp/voting/cast/Reviews/2115/R39RQ6PZQ71DXI/Inappropriate/1?ie=UTF8&target=aHR0cDovL3d3dy5hbWF6b24uY29tL3Jldmlldy9CMDA3U0JHRjEy&token=7A7BA0281B32FCBD56DD5B32BCFE816157D8DFCF&voteAnchorName=R39RQ6PZQ71DXI.2115.Inappropriate.Reviews&voteSessionID=000-0000000-0000000"
>Report abuse</a></nobr></span>
</span> <span style="color:#CCCCCC;">|</span> <span class="tiny"><a href="http://www.amazon.com/review/R39RQ6PZQ71DXI" >Permalink</a></span></div><div style="white-space:nowrap;padding-left:-5px;padding-top:5px;"><a href="http://www.amazon.com/review/R39RQ6PZQ71DXI" ><span class="swSprite s_comment " ><span>Comment</span></span></a>&nbsp;<a href="http://www.amazon.com/review/R39RQ6PZQ71DXI" >Comment</a></div></div></div><div style="clear:both;"></div>
      </div>
      <br />

</div>

  






















































<!-- BOUNDARY -->
<a name="R4L02T5HZRFMY"></a><br />


<div style="margin-left:0.5em;">
    
      <div style="margin-bottom:0.5em;">
        2 of 2 people found the following review helpful
      </div>
      <div style="margin-bottom:0.5em;">
        <span style="margin-right:5px;"><span class="swSprite s_star_2_0 " title="2.0 out of 5 stars" ><span>2.0 out of 5 stars</span></span> </span>
        <span style="vertical-align:middle;"><b>Shuts off device for me too.</b>, <nobr>January 8, 2013</nobr></span>
      </div>
      <div style="margin-bottom:0.5em;">
        <div><div style="float:left;">By&nbsp;</div><div style="float:left;"><a href="/gp/pdp/profile/A2IUYAM7VJI7O9" ><span style = "font-weight: bold;">J. Skeoch</span></a> (San Diego, CA USA)  - <a href="/gp/cdp/member-reviews/A2IUYAM7VJI7O9?ie=UTF8&amp;sort_by=MostRecentReview">See all my reviews</a><br />
<a href="http://www.amazon.com/gp/help/customer/display.html?ie=UTF8&nodeId=14279681&pop-up=1#RN" target="AmazonHelp" onclick="return amz_js_PopWin(this.href,'AmazonHelp','width=340,height=340,resizable=1,scrollbars=1,toolbar=1,status=1');"  ><span class="cmtySprite s_BadgeRealName " ><span>(REAL NAME)</span></span></a>
&nbsp;&nbsp;


</div></div><div style="clear:both;"></div>
      </div>
      <div class="tiny" style="margin-bottom:0.5em;">
        <b><span class="h3color tiny">This review is from: </span>7 Inch Multi-Angles Google Nexus 7 Tablet Leather Protection Case by i-UniK (Light Blue) - Colors Available: Hot Pink, Red, Lime Green, Light Blue, Expresso Black (Personal Computers)</b>
      </div>

I am having the same issue as the other review who found that it shuts off their
 device.  Nexus 7 shuts off at random times when using this case. Often, can not
 even turn the Nexus on, when you swipe the lock to the edge of the circle and l
et go it flashes on, then turns off immediately. It was baffling for a while, ho
w on earth can a case be responsible for this? But searching around I think I kn
ow what the issue is. There are magnets in the lid of this "smart case" which, w
hen laid on top of the nexus screen will turn of the device. I think the problem
 is that the magnets are perhaps too strong and are being detected through the b
ack of the Nexus 7 while the lid is open and wrapped around the back of the unit
. I confirmed this as follows. With the cover open and pressed against the back,
 the Nexus shuts off, then when removing the lid off the back of the Nexus, the 
devices turned on again. Seems to be more of a problem when the lid opens to the
 right (Asian style book) rather than left (Western style book).
      <div style="padding-top: 10px; clear: both; width: 100%;">

        <div class="reviews-voting-stripe" style="float:left; padding-right:15px; border-right:1px solid #CCCCCC"><div style="padding-bottom:5px;"><b class="tiny" style="color:#666666;white-space:nowrap;">Help other customers find the most helpful reviews</b>&nbsp;</div><div style="width:300px;">









<a name="R4L02T5HZRFMY.2115.Helpful.Reviews" style="font-size:1px;"> </a><span
class="crVotingButtons"><nobr><span class="votingPrompt">Was this review helpful to you?&nbsp;</span><a rel="nofollow" class="votingButtonReviews yesButton" href="http://www.amazon.com/gp/voting/cast/Reviews/2115/R4L02T5HZRFMY/Helpful/1?ie=UTF8&target=aHR0cDovL3d3dy5hbWF6b24uY29tL3Jldmlldy9CMDA3U0JHRjEy&token=D7F70122EB87D321C86A3FB65FAD94FCF5D8689C&voteAnchorName=R4L02T5HZRFMY.2115.Helpful.Reviews&voteSessionID=000-0000000-0000000"><span class="cmtySprite s_largeYes " ><span>Yes</span></span></a>
<a rel="nofollow" class="votingButtonReviews noButton" href="http://www.amazon.com/gp/voting/cast/Reviews/2115/R4L02T5HZRFMY/Helpful/-1?ie=UTF8&target=aHR0cDovL3d3dy5hbWF6b24uY29tL3Jldmlldy9CMDA3U0JHRjEy&token=3D2619D832436D43315BBE172537F00D3CB9F95A&voteAnchorName=R4L02T5HZRFMY.2115.Helpful.Reviews&voteSessionID=000-0000000-0000000"><span class="cmtySprite s_largeNo " ><span>No</span></span></a></nobr> <span class="votingMessage"></span></span>

</div></div><div style="float:left;"><div style="padding-left:15px;"><div style="white-space:nowrap;"><span class='tiny'>








<a name="R4L02T5HZRFMY.2115.Inappropriate.Reviews" style="font-size:1px;"> </a><span class="reportingButton"><nobr><a rel="nofollow" class="reportingButton" href="http://www.amazon.com/gp/voting/cast/Reviews/2115/R4L02T5HZRFMY/Inappropriate/1?ie=UTF8&target=aHR0cDovL3d3dy5hbWF6b24uY29tL3Jldmlldy9CMDA3U0JHRjEy&token=682E33AB2E417F286E72E98380A80946F1B088A4&voteAnchorName=R4L02T5HZRFMY.2115.Inappropriate.Reviews&voteSessionID=000-0000000-0000000"
>Report abuse</a></nobr></span>
</span> <span style="color:#CCCCCC;">|</span> <span class="tiny"><a href="http://www.amazon.com/review/R4L02T5HZRFMY" >Permalink</a></span></div><div style="white-space:nowrap;padding-left:-5px;padding-top:5px;"><a href="http://www.amazon.com/review/R4L02T5HZRFMY" ><span class="swSprite s_comment " ><span>Comment</span></span></a>&nbsp;<a href="http://www.amazon.com/review/R4L02T5HZRFMY" >Comment</a></div></div></div><div style="clear:both;"></div>
      </div>
      <br />

</div>

  






















































<!-- BOUNDARY -->
<a name="R3NNUPI6Y7VH3F"></a><br />


<div style="margin-left:0.5em;">
    
      <div style="margin-bottom:0.5em;">
        2 of 2 people found the following review helpful
      </div>
      <div style="margin-bottom:0.5em;">
        <span style="margin-right:5px;"><span class="swSprite s_star_4_0 " title="4.0 out of 5 stars" ><span>4.0 out of 5 stars</span></span> </span>
        <span style="vertical-align:middle;"><b>Very good for the money</b>, <nobr>December 1, 2012</nobr></span>
      </div>
      <div style="margin-bottom:0.5em;">
        <div><div style="float:left;">By&nbsp;</div><div style="float:left;"><a href="/gp/pdp/profile/AWPRRO7UEK5R8" ><span style = "font-weight: bold;">F. Silverman</span></a> (California)  - <a href="/gp/cdp/member-reviews/AWPRRO7UEK5R8?ie=UTF8&amp;sort_by=MostRecentReview">See all my reviews</a><br />
<a href="http://www.amazon.com/gp/help/customer/display.html?ie=UTF8&nodeId=14279681&pop-up=1#RN" target="AmazonHelp" onclick="return amz_js_PopWin(this.href,'AmazonHelp','width=340,height=340,resizable=1,scrollbars=1,toolbar=1,status=1');"  ><span class="cmtySprite s_BadgeRealName " ><span>(REAL NAME)</span></span></a>
&nbsp;&nbsp;


</div></div><div style="clear:both;"></div>
      </div>
      <div class="tiny" style="margin-bottom:0.5em;">
        <span class="crVerifiedStripe"><b class="h3color tiny" style="margin-right: 0.5em;">Amazon Verified Purchase</b><span class="tiny verifyWhatsThis">(<a href="http://www.amazon.com/gp/community-help/amazon-verified-purchase" target="AmazonHelp" onclick="amz_js_PopWin('http://www.amazon.com/gp/community-help/amazon-verified-purchase', 'AmazonHelp', 'width=400,height=500,resizable=1,scrollbars=1,toolbar=0,status=1');return false; ">What's this?</a>)</span></span>
      </div>
      <div class="tiny" style="margin-bottom:0.5em;">
        <b><span class="h3color tiny">This review is from: </span>7 Inch Multi-Angles Google Nexus 7 Tablet Leather Protection Case by i-UniK (Light Blue) - Colors Available: Hot Pink, Red, Lime Green, Light Blue, Expresso Black (Personal Computers)</b>
      </div>

I bought this case because I had just purchased my Nexus and we were going on a trip. Fits perfectly and I like the feel.  Doesn't work very well as a stand, because the creases aren't stiff enough. For me that's not a problem because I seldom watch things on it.  Overall its just fine for protecting my Nexus.  Delivery was in credibly fast and color matches the ad. thanks!
      <div style="padding-top: 10px; clear: both; width: 100%;">

        <div class="reviews-voting-stripe" style="float:left; padding-right:15px; border-right:1px solid #CCCCCC"><div style="padding-bottom:5px;"><b class="tiny" style="color:#666666;white-space:nowrap;">Help other customers find the most helpful reviews</b>&nbsp;</div><div style="width:300px;">









<a name="R3NNUPI6Y7VH3F.2115.Helpful.Reviews" style="font-size:1px;"> </a><span
class="crVotingButtons"><nobr><span class="votingPrompt">Was this review helpful to you?&nbsp;</span><a rel="nofollow" class="votingButtonReviews yesButton" href="http://www.amazon.com/gp/voting/cast/Reviews/2115/R3NNUPI6Y7VH3F/Helpful/1?ie=UTF8&target=aHR0cDovL3d3dy5hbWF6b24uY29tL3Jldmlldy9CMDA3U0JHRjEy&token=BA887DAE7D9BF3448B60F728608FDFBA5415B6AA&voteAnchorName=R3NNUPI6Y7VH3F.2115.Helpful.Reviews&voteSessionID=000-0000000-0000000"><span class="cmtySprite s_largeYes " ><span>Yes</span></span></a>
<a rel="nofollow" class="votingButtonReviews noButton" href="http://www.amazon.com/gp/voting/cast/Reviews/2115/R3NNUPI6Y7VH3F/Helpful/-1?ie=UTF8&target=aHR0cDovL3d3dy5hbWF6b24uY29tL3Jldmlldy9CMDA3U0JHRjEy&token=6257116C0F7332540CED9681A8BF8406AA18526F&voteAnchorName=R3NNUPI6Y7VH3F.2115.Helpful.Reviews&voteSessionID=000-0000000-0000000"><span class="cmtySprite s_largeNo " ><span>No</span></span></a></nobr> <span class="votingMessage"></span></span>

</div></div><div style="float:left;"><div style="padding-left:15px;"><div style="white-space:nowrap;"><span class='tiny'>








<a name="R3NNUPI6Y7VH3F.2115.Inappropriate.Reviews" style="font-size:1px;"> </a><span class="reportingButton"><nobr><a rel="nofollow" class="reportingButton" href="http://www.amazon.com/gp/voting/cast/Reviews/2115/R3NNUPI6Y7VH3F/Inappropriate/1?ie=UTF8&target=aHR0cDovL3d3dy5hbWF6b24uY29tL3Jldmlldy9CMDA3U0JHRjEy&token=C82FFA28E7C08CAEDC3B9F206BEB500674738C9B&voteAnchorName=R3NNUPI6Y7VH3F.2115.Inappropriate.Reviews&voteSessionID=000-0000000-0000000"
>Report abuse</a></nobr></span>
</span> <span style="color:#CCCCCC;">|</span> <span class="tiny"><a href="http://www.amazon.com/review/R3NNUPI6Y7VH3F" >Permalink</a></span></div><div style="white-space:nowrap;padding-left:-5px;padding-top:5px;"><a href="http://www.amazon.com/review/R3NNUPI6Y7VH3F" ><span class="swSprite s_comment " ><span>Comment</span></span></a>&nbsp;<a href="http://www.amazon.com/review/R3NNUPI6Y7VH3F" >Comment</a></div></div></div><div style="clear:both;"></div>
      </div>
      <br />

</div>

  














































<!-- BOUNDARY -->
<a name="RSHYRLGVXDLG9"></a><br />


<div style="margin-left:0.5em;">
    
      <div style="margin-bottom:0.5em;">
        2 of 2 people found the following review helpful
      </div>
      <div style="margin-bottom:0.5em;">
        <span style="margin-right:5px;"><span class="swSprite s_star_5_0 " title="5.0 out of 5 stars" ><span>5.0 out of 5 stars</span></span> </span>
        <span style="vertical-align:middle;"><b>i-unik Nexus case</b>, <nobr>September 11, 2012</nobr></span>
      </div>
      <div style="margin-bottom:0.5em;">
        <div><div style="float:left;">By&nbsp;</div><div style="float:left;"><a href="/gp/pdp/profile/A1Y33GCVRKAHLR" ><span style = "font-weight: bold;">Shopper1</span></a>  - <a href="/gp/cdp/member-reviews/A1Y33GCVRKAHLR?ie=UTF8&amp;sort_by=MostRecentReview">See all my reviews</a></div></div><div style="clear:both;"></div>
      </div>
      <div class="tiny" style="margin-bottom:0.5em;">
        <b><span class="h3color tiny">This review is from: </span><a href="http://www.amazon.com/i-UniK-Multi-Angles-Leather-Protection-Expresso/dp/B007SBGF1W">i-UniK Multi-Angles Google Nexus 7 Inch Tablet Leather Protection Case -Red,Hot Pink, Red, Lime Green, Light Blue, Expresso Black (Electronics)</a></b>
      </div>

I love this case! Fits perfect! Love the color and quality! I lost my order information after I ordered so I sent an e-mail through amazon to i-UniK for help. They helped me right away within minutes! I am so happy with their service and their product and will use them regularly!
      <div style="padding-top: 10px; clear: both; width: 100%;">

        <div class="reviews-voting-stripe" style="float:left; padding-right:15px; border-right:1px solid #CCCCCC"><div style="padding-bottom:5px;"><b class="tiny" style="color:#666666;white-space:nowrap;">Help other customers find the most helpful reviews</b>&nbsp;</div><div style="width:300px;">









<a name="RSHYRLGVXDLG9.2115.Helpful.Reviews" style="font-size:1px;"> </a><span
class="crVotingButtons"><nobr><span class="votingPrompt">Was this review helpful to you?&nbsp;</span><a rel="nofollow" class="votingButtonReviews yesButton" href="http://www.amazon.com/gp/voting/cast/Reviews/2115/RSHYRLGVXDLG9/Helpful/1?ie=UTF8&target=aHR0cDovL3d3dy5hbWF6b24uY29tL3Jldmlldy9CMDA3U0JHRjEy&token=D6D2558EEBEEBC2A4C3D4B8F5371867FAB857720&voteAnchorName=RSHYRLGVXDLG9.2115.Helpful.Reviews&voteSessionID=000-0000000-0000000"><span class="cmtySprite s_largeYes " ><span>Yes</span></span></a>
<a rel="nofollow" class="votingButtonReviews noButton" href="http://www.amazon.com/gp/voting/cast/Reviews/2115/RSHYRLGVXDLG9/Helpful/-1?ie=UTF8&target=aHR0cDovL3d3dy5hbWF6b24uY29tL3Jldmlldy9CMDA3U0JHRjEy&token=994E30C99A93EB0627262045E48E06C6B65DC3B1&voteAnchorName=RSHYRLGVXDLG9.2115.Helpful.Reviews&voteSessionID=000-0000000-0000000"><span class="cmtySprite s_largeNo " ><span>No</span></span></a></nobr> <span class="votingMessage"></span></span>

</div></div><div style="float:left;"><div style="padding-left:15px;"><div style="white-space:nowrap;"><span class='tiny'>








<a name="RSHYRLGVXDLG9.2115.Inappropriate.Reviews" style="font-size:1px;"> </a><span class="reportingButton"><nobr><a rel="nofollow" class="reportingButton" href="http://www.amazon.com/gp/voting/cast/Reviews/2115/RSHYRLGVXDLG9/Inappropriate/1?ie=UTF8&target=aHR0cDovL3d3dy5hbWF6b24uY29tL3Jldmlldy9CMDA3U0JHRjEy&token=DEB314AFE2BC2A5335DD17CB4C2A0CCF837E1657&voteAnchorName=RSHYRLGVXDLG9.2115.Inappropriate.Reviews&voteSessionID=000-0000000-0000000"
>Report abuse</a></nobr></span>
</span> <span style="color:#CCCCCC;">|</span> <span class="tiny"><a href="http://www.amazon.com/review/RSHYRLGVXDLG9" >Permalink</a></span></div><div style="white-space:nowrap;padding-left:-5px;padding-top:5px;"><a href="http://www.amazon.com/review/RSHYRLGVXDLG9" ><span class="swSprite s_comment " ><span>Comment</span></span></a>&nbsp;<a href="http://www.amazon.com/review/RSHYRLGVXDLG9" >Comment</a></div></div></div><div style="clear:both;"></div>
      </div>
      <br />

</div>

  














































<!-- BOUNDARY -->
<a name="R2X0EPFT993WOD"></a><br />


<div style="margin-left:0.5em;">
    
      <div style="margin-bottom:0.5em;">
        2 of 2 people found the following review helpful
      </div>
      <div style="margin-bottom:0.5em;">
        <span style="margin-right:5px;"><span class="swSprite s_star_5_0 " title="5.0 out of 5 stars" ><span>5.0 out of 5 stars</span></span> </span>
        <span style="vertical-align:middle;"><b>Tablet Cover</b>, <nobr>September 8, 2012</nobr></span>
      </div>
      <div style="margin-bottom:0.5em;">
        <div><div style="float:left;">By&nbsp;</div><div style="float:left;"><a href="/gp/pdp/profile/A167ZF59RL6TLA" ><span style = "font-weight: bold;">RRussell</span></a>  - <a href="/gp/cdp/member-reviews/A167ZF59RL6TLA?ie=UTF8&amp;sort_by=MostRecentReview">See all my reviews</a></div></div><div style="clear:both;"></div>
      </div>
      <div class="tiny" style="margin-bottom:0.5em;">
        <span class="crVerifiedStripe"><b class="h3color tiny" style="margin-right: 0.5em;">Amazon Verified Purchase</b><span class="tiny verifyWhatsThis">(<a href="http://www.amazon.com/gp/community-help/amazon-verified-purchase" target="AmazonHelp" onclick="amz_js_PopWin('http://www.amazon.com/gp/community-help/amazon-verified-purchase', 'AmazonHelp', 'width=400,height=500,resizable=1,scrollbars=1,toolbar=0,status=1');return false; ">What's this?</a>)</span></span>
      </div>
      <div class="tiny" style="margin-bottom:0.5em;">
        <b><span class="h3color tiny">This review is from: </span><a href="http://www.amazon.com/Multi-Angles-Leather-Protection-i-UniK-Expresso/dp/B007SBGF0S">7 Inch Multi-Angles Google Nexus 7 Tablet Leather Protection Case by i-UniK (Expresso Black) - Colors Available: Hot Pink, Red, Lime Green, Light Blue, Expresso Black (Electronics)</a></b>
      </div>

This is a very inexpensive, but nice quality case.  Product as promised and a very good value.  This appears to be a real leather product.
      <div style="padding-top: 10px; clear: both; width: 100%;">

        <div class="reviews-voting-stripe" style="float:left; padding-right:15px; border-right:1px solid #CCCCCC"><div style="padding-bottom:5px;"><b class="tiny" style="color:#666666;white-space:nowrap;">Help other customers find the most helpful reviews</b>&nbsp;</div><div style="width:300px;">









<a name="R2X0EPFT993WOD.2115.Helpful.Reviews" style="font-size:1px;"> </a><span
class="crVotingButtons"><nobr><span class="votingPrompt">Was this review helpful to you?&nbsp;</span><a rel="nofollow" class="votingButtonReviews yesButton" href="http://www.amazon.com/gp/voting/cast/Reviews/2115/R2X0EPFT993WOD/Helpful/1?ie=UTF8&target=aHR0cDovL3d3dy5hbWF6b24uY29tL3Jldmlldy9CMDA3U0JHRjEy&token=3BF7ABD961AE582A280DC028B54AABA72DFDF880&voteAnchorName=R2X0EPFT993WOD.2115.Helpful.Reviews&voteSessionID=000-0000000-0000000"><span class="cmtySprite s_largeYes " ><span>Yes</span></span></a>
<a rel="nofollow" class="votingButtonReviews noButton" href="http://www.amazon.com/gp/voting/cast/Reviews/2115/R2X0EPFT993WOD/Helpful/-1?ie=UTF8&target=aHR0cDovL3d3dy5hbWF6b24uY29tL3Jldmlldy9CMDA3U0JHRjEy&token=91DB809F9E35FE17A4BF39874058F48D59E395E4&voteAnchorName=R2X0EPFT993WOD.2115.Helpful.Reviews&voteSessionID=000-0000000-0000000"><span class="cmtySprite s_largeNo " ><span>No</span></span></a></nobr> <span class="votingMessage"></span></span>

</div></div><div style="float:left;"><div style="padding-left:15px;"><div style="white-space:nowrap;"><span class='tiny'>








<a name="R2X0EPFT993WOD.2115.Inappropriate.Reviews" style="font-size:1px;"> </a><span class="reportingButton"><nobr><a rel="nofollow" class="reportingButton" href="http://www.amazon.com/gp/voting/cast/Reviews/2115/R2X0EPFT993WOD/Inappropriate/1?ie=UTF8&target=aHR0cDovL3d3dy5hbWF6b24uY29tL3Jldmlldy9CMDA3U0JHRjEy&token=D168951E349EB2EC771E8045FFC2A6A4E631FCD7&voteAnchorName=R2X0EPFT993WOD.2115.Inappropriate.Reviews&voteSessionID=000-0000000-0000000"
>Report abuse</a></nobr></span>
</span> <span style="color:#CCCCCC;">|</span> <span class="tiny"><a href="http://www.amazon.com/review/R2X0EPFT993WOD" >Permalink</a></span></div><div style="white-space:nowrap;padding-left:-5px;padding-top:5px;"><a href="http://www.amazon.com/review/R2X0EPFT993WOD" ><span class="swSprite s_comment " ><span>Comment</span></span></a>&nbsp;<a href="http://www.amazon.com/review/R2X0EPFT993WOD" >Comment</a></div></div></div><div style="clear:both;"></div>
      </div>
      <br />

</div>

  



  </td>
  <td width="10%">
  </td>
</tr>
</table>
<br />




























<table class="CMheadingBar" border="0" cellpadding="0" cellspacing="0" width="100%">
  <tr>
    <td height="16" align="left" style="padding-left:4px;padding-right:4px;">
      <div class="CMpaginate" style="white-space:nowrap;">
        <span class="paging">&lsaquo; Previous |    <span class="on">1</span> <a href="http://www.amazon.com/Multi-Angles-Leather-Protection-i-UniK-Blue/product-reviews/B007SBGF12?pageNumber=2" >2</a> &hellip; <a href="http://www.amazon.com/Multi-Angles-Leather-Protection-i-UniK-Blue/product-reviews/B007SBGF12?pageNumber=7" >7</a>| <a href="http://www.amazon.com/Multi-Angles-Leather-Protection-i-UniK-Blue/product-reviews/B007SBGF12?pageNumber=2" >Next &rsaquo;</a> </span>
      </div>
    </td>
    <td height="16" align="right" style="padding-right:4px;">
      <div class="" style="white-space:nowrap;">
        <b class="on">Most Helpful First</b> | <b class="on">Newest First</b>
      </div>
    </td>
  </tr>
</table>





<script language="javascript">
  if (typeof uet == 'function') { uet('cf'); }
</script>








<!--AMZNJQSECTION-->












<div style="display: none">
  <div id="nav-prime-menu" class="nav-empty nav-flyout-content nav-ajax-prime-menu">
    <div class="nav_dynamic"></div>
    <div class="nav-ajax-message"></div>
    <div class="nav-ajax-error-msg">
      <p class="nav_p nav-bold">There's a problem loading this menu right now.</p>
      <p class="nav_p"><a href="/gp/prime" class="nav_a">Learn more about Amazon Prime.</a></p>
    </div>
  </div>
</div>







<style>
  #nav-prime-tooltip{
    padding: 0 20px 2px 20px;
    background-color: white;
    font-family: arial,sans-serif;
  }
  .nav-npt-text-title{
    font-family: arial,sans-serif;
    font-size: 18px;
    font-weight: bold;
    line-height: 21px;
    color: #E47923;
  }
  .nav-npt-text-detail, a.nav-npt-a{
    font-family: arial,sans-serif;
    font-size: 12px;
    line-height: 14px;
    color: #333333;
    white-space: nowrap;
    margin: 2px 0px;
  }
  a.nav-npt-a {
    text-decoration: underline;
  }
</style>

<div  style="display: none">
  <div id="nav-prime-tooltip">
    <div class="nav-npt-text-title"> Watch. Read. Shop. Relax. </div>
    <div class="nav-npt-text-detail"> Millions of Amazon Prime members enjoy instant videos, free Kindle books and unlimited free two-day shipping. </div>
    <div class="nav-npt-text-detail">
      &gt;
      <a class="nav-npt-a" href="https://www.amazon.com/gp/subs/primeclub/signup/handler.html?ie=UTF8&primeCampaignId=videos&primeMetadata=ref%3Dnav_tooltip_redirect&session-id=000-0000000-0000000">Get started</a>
    </div>
  </div>
</div>





      
      
<div style="display: none;">









<div id="nav_browse_flyout" >
  <div id="nav_subcats_wrap" class="nav_browse_wrap">
    <div id="nav_subcats">
      <div id="nav_subcats_0" data-nav-promo-id="instant-video"  class="nav_brow
se_subcat"><ul class="nav_browse_ul nav_browse_cat_ul"><li class="nav_pop_li nav
_browse_cat_head">Unlimited Instant Videos</li><li class="nav_first nav_taglined
 nav_subcat_link nav_pop_li"><a href="/b?ie=UTF8&amp;node=2676882011" class="nav
_a nav_item">Prime Instant Video</a><div class="nav_tag">Unlimited streaming of 
thousands of<br />movies and TV shows with Amazon Prime</div></li><li class="nav
_subcat_link nav_pop_li"><a href="/gp/video/primesignup?ie=UTF8&amp;redirectQuer
yParams=bm9kZT0yNjE1MjYwMDEx&amp;redirectURL=L2Iv" class="nav_a nav_item">Learn 
More About Amazon Prime</a></li><li class="nav_taglined nav_subcat_link nav_pop_
li nav_divider_before"><a href="/Instant-Video/b?ie=UTF8&amp;node=2858778011" cl
ass="nav_a nav_item">Amazon Instant Video Store</a><div class="nav_tag">Rent or 
buy hit movies and TV shows<br />to stream or download</div></li><li class="nav_
taglined nav_subcat_link nav_pop_li"><a href="/gp/video/library" class="nav_a na
v_item">Your Video Library</a><div class="nav_tag">Your movies and TV shows<br /
>stored in the cloud</div></li><li class="nav_taglined nav_subcat_link nav_pop_l
i"><a href="/gp/video/ontv/ontv" class="nav_a nav_item">Watch Anywhere</a><div c
lass="nav_tag">Watch instantly on your Kindle Fire,<br />TV, Blu-ray player, or 
set-top box</div></li></ul></div>
<div id="nav_subcats_1" data-nav-promo-id="mp3"  class="nav_browse_subcat"><ul c
lass="nav_browse_ul nav_browse_cat_ul"><li class="nav_pop_li nav_browse_cat_head
">MP3s & Cloud Player</li><li class="nav_first nav_taglined nav_subcat_link nav_
pop_li"><a href="/MP3-Music-Download/b?ie=UTF8&amp;node=163856011" class="nav_a 
nav_item">MP3 Music Store</a><div class="nav_tag">Shop over 20 million songs</di
v></li><li class="nav_taglined nav_subcat_link nav_pop_li"><a href="/gp/feature.
html?ie=UTF8&amp;docId=1000825251" class="nav_a nav_item">Music on Kindle Fire</
a><div class="nav_tag">Discover how to play your music</div></li><li class="nav_
taglined nav_subcat_link nav_pop_li"><a href="/gp/feature.html?ie=UTF8&amp;docId
=1001067901" class="nav_a nav_item">Cloud Player for PC</a><div class="nav_tag">
Play, manage and download your music</div></li><li class="nav_taglined nav_subca
t_link nav_pop_li"><a href="/gp/dmusic/marketing/CloudPlayerLaunchPage" class="n
av_a nav_item" target="_blank">Cloud Player for Web</a><div class="nav_tag">Play
 from any browser</div></li><li class="nav_taglined nav_subcat_link nav_pop_li">
<a href="/gp/feature.html?ie=UTF8&amp;docId=1000454841" class="nav_a nav_item">C
loud Player for Android</a><div class="nav_tag">For Android phones and tablets</
div></li><li class="nav_taglined nav_subcat_link nav_pop_li"><a href="/gp/featur
e.html?ie=UTF8&amp;docId=1000776061" class="nav_a nav_item">Cloud Player for iOS
</a><div class="nav_tag">For iPhone, iPad and iPod touch</div></li><li class="na
v_taglined nav_subcat_link nav_pop_li"><a href="/b?ie=UTF8&amp;node=2658409011" 
class="nav_a nav_item">Cloud Player for Home</a><div class="nav_tag">For Sonos a
nd Roku</div></li></ul></div>
<div id="nav_subcats_2" data-nav-promo-id="cloud-drive"  class="nav_browse_subca
t"><ul class="nav_browse_ul nav_browse_cat_ul"><li class="nav_pop_li nav_browse_
cat_head">Amazon Cloud Drive</li><li class="nav_first nav_taglined nav_subcat_li
nk nav_pop_li"><a href="/clouddrive" class="nav_a nav_item" target="_blank">Your
 Cloud Drive</a><div class="nav_tag">5 GB of free storage</div></li><li class="n
av_taglined nav_subcat_link nav_pop_li"><a href="/gp/feature.html?ie=UTF8&amp;do
cId=1000796781" class="nav_a nav_item">Get the Desktop App</a><div class="nav_ta
g">For Windows and Mac</div></li><li class="nav_taglined nav_subcat_link nav_pop
_li"><a href="/gp/feature.html?ie=UTF8&amp;docId=1000848741" class="nav_a nav_it
em">Cloud Drive Photos for Android</a><div class="nav_tag">For Android phones an
d tablets</div></li><li class="nav_taglined nav_subcat_link nav_pop_li"><a href=
"/gp/feature.html?ie=UTF8&amp;docId=1001206201" class="nav_a nav_item">Cloud Dri
ve Photos for iPhone</a><div class="nav_tag">For iPhone and iPod touch</div></li
><li class="nav_subcat_link nav_pop_li"><a href="/gp/feature.html?ie=UTF8&amp;do
cId=1000796931" class="nav_a nav_item">Learn More About Cloud Drive</a></li></ul
></div>
<div id="nav_subcats_3" data-nav-promo-id="kindle"  class="nav_browse_subcat nav
_super_cat"><ul class="nav_browse_ul nav_browse_cat_ul"><li class="nav_first nav
_pop_li nav_browse_cat_head">Kindle E-readers</li><li class="nav_first nav_tagli
ned nav_subcat_link nav_pop_li"><a href="/dp/B007HCCNJU" class="nav_a nav_item">
Kindle</a><div class="nav_tag">Small, light, perfect for reading</div></li><li c
lass="nav_taglined nav_subcat_link nav_pop_li"><a href="/dp/B007OZNZG0" class="n
av_a nav_item">Kindle Paperwhite</a><div class="nav_tag">World's most advanced e
-reader</div></li><li class="nav_taglined nav_subcat_link nav_pop_li"><a href="/
dp/B007OZNUCE" class="nav_a nav_item">Kindle Paperwhite 3G</a><div class="nav_ta
g">With free 3G wireless</div></li><li class="nav_taglined nav_subcat_link nav_p
op_li"><a href="/b?ie=UTF8&amp;node=5916440011" class="nav_a nav_item">Kindle E-
reader Accessories</a><div class="nav_tag">Covers, chargers, sleeves and more</d
iv></li><li class="nav_pop_li nav_browse_cat_head nav_divider_before">Kindle Sto
re</li><li class="nav_first nav_subcat_link nav_pop_li"><a href="/Kindle-eBooks/
b?ie=UTF8&amp;node=1286228011" class="nav_a nav_item">Kindle Books</a></li><li c
lass="nav_subcat_link nav_pop_li"><a href="/gp/digital/fiona/redirect/newsstand/
home/" class="nav_a nav_item">Newsstand</a></li><li class="nav_taglined nav_subc
at_link nav_pop_li"><a href="/gp/redirect.html?ie=UTF8&amp;location=%2Fkindlelen
dinglibrary" class="nav_a nav_item">Kindle Owners' Lending Library</a><div class
="nav_tag">With Prime, Kindle owners read for free</div></li></ul>
<ul class="nav_browse_ul nav_browse_cat2_ul">
<li class="nav_pop_li nav_browse_cat_head">Kindle Fire</li><li class="nav_first 
nav_taglined nav_subcat_link nav_pop_li"><a href="/dp/B0083Q04IQ" class="nav_a n
av_item">Fire</a><div class="nav_tag">All new--faster, twice the memory</div></l
i><li class="nav_taglined nav_subcat_link nav_pop_li"><a href="/dp/B0083PWAPW" c
lass="nav_a nav_item">Fire HD</a><div class="nav_tag">7", Dolby audio, ultra-fas
t Wi-Fi</div></li><li class="nav_taglined nav_subcat_link nav_pop_li"><a href="/
dp/B008GFRE5A" class="nav_a nav_item">Fire HD 8.9"</a><div class="nav_tag">8.9",
 Dolby audio, ultra-fast Wi-Fi</div></li><li class="nav_taglined nav_subcat_link
 nav_pop_li"><a href="/dp/B008GFRDL0" class="nav_a nav_item">Fire HD 8.9" 4G</a>
<div class="nav_tag">With ultra-fast 4G LTE wireless</div></li><li class="nav_ta
glined nav_subcat_link nav_pop_li"><a href="/b?ie=UTF8&amp;node=5916439011" clas
s="nav_a nav_item">Kindle Fire Accessories</a><div class="nav_tag">Cases, charge
rs, sleeves and more</div></li><li class="nav_pop_li nav_browse_cat_head nav_div
ider_before">Kindle Apps & Resources</li><li class="nav_first nav_taglined nav_s
ubcat_link nav_pop_li"><a href="https://www.amazon.com:443/gp/redirect.html?loca
tion=https://read.amazon.com/&amp;token=34AD60CFC4DCD7A97D4E2F4A4A7C4149FBEEF236
" class="nav_a nav_item">Kindle Cloud Reader</a><div class="nav_tag">Read your K
indle books in a browser</div></li><li class="nav_taglined nav_subcat_link nav_p
op_li"><a href="/gp/feature.html?ie=UTF8&amp;docId=1000493771" class="nav_a nav_
item">Free Kindle Reading Apps</a><div class="nav_tag">For PC, iPad, iPhone, And
roid, and more</div></li><li class="nav_subcat_link nav_pop_li"><a href="/gp/dig
ital/fiona/manage" class="nav_a nav_item">Manage Your Kindle</a></li></ul></div>

<div id="nav_subcats_4" data-nav-promo-id="android"  class="nav_browse_subcat"><
ul class="nav_browse_ul nav_browse_cat_ul"><li class="nav_pop_li nav_browse_cat_
head">Appstore for Android</li><li class="nav_first nav_subcat_link nav_pop_li">
<a href="/mobile-apps/b?ie=UTF8&amp;node=2350149011" class="nav_a nav_item">Apps
</a></li><li class="nav_subcat_link nav_pop_li"><a href="/b?ie=UTF8&amp;node=247
8844011" class="nav_a nav_item">Games</a></li><li class="nav_taglined nav_subcat
_link nav_pop_li nav_divider_before"><a href="/b?ie=UTF8&amp;node=3071729011" cl
ass="nav_a nav_item">Test Drive Apps</a><div class="nav_tag">Try thousands of ap
ps and games right now</div></li><li class="nav_taglined nav_subcat_link nav_pop
_li"><a href="/gp/feature.html?ie=UTF8&amp;docId=1000645111" class="nav_a nav_it
em">Amazon Apps</a><div class="nav_tag">Kindle, mobile shopping, MP3, and more</
div></li><li class="nav_taglined nav_subcat_link nav_pop_li"><a href="/gp/mas/yo
ur-account/myapps" class="nav_a nav_item">Your Apps and Devices</a><div class="n
av_tag">View your apps and manage your devices</div></li></ul></div>
<div id="nav_subcats_5" data-nav-promo-id="digital-games-software"  class="nav_browse_subcat"><ul class="nav_browse_ul nav_browse_cat_ul"><li class="nav_pop_li nav_browse_cat_head">Digital Games & Software</li><li class="nav_first nav_taglined nav_subcat_link nav_pop_li"><a href="/Game-Downloads/b?ie=UTF8&amp;node=979455011" class="nav_a nav_item">Digital Games</a><div class="nav_tag">For PC and Mac</div></li><li class="nav_taglined nav_subcat_link nav_pop_li"><a href="/b?ie=UTF8&amp;node=5267605011" class="nav_a nav_item">Free-to-Play Games</a><div class="nav_tag">For PC and Mac</div></li><li class="nav_taglined nav_subcat_link nav_pop_li"><a href="/pc-mac-software-downloads/b?ie=UTF8&amp;node=1233514011" class="nav_a nav_item">Digital Software</a><div class="nav_tag">For PC and Mac</div></li><li class="nav_subcat_link nav_pop_li"><a href="/gp/swvgdtt/your-account/manage-downloads.html" class="nav_a nav_item">Your Games & Software Library</a></li></ul></div>
<div id="nav_subcats_6" data-nav-promo-id="audible"  class="nav_browse_subcat"><
ul class="nav_browse_ul nav_browse_cat_ul"><li class="nav_pop_li nav_browse_cat_
head">Audible Audiobooks</li><li class="nav_first nav_taglined nav_subcat_link n
av_pop_li"><a href="/gp/audible/signup/display.html" class="nav_a nav_item">Audi
ble Membership</a><div class="nav_tag">Get to know Audible</div></li><li class="
nav_subcat_link nav_pop_li"><a href="/b?ie=UTF8&amp;node=2402172011" class="nav_
a nav_item">Audible Audiobooks & More</a></li><li class="nav_subcat_link nav_pop
_li"><a href="/gp/bestsellers/books/2402172011" class="nav_a nav_item">Bestselle
rs</a></li><li class="nav_subcat_link nav_pop_li"><a href="/b?ie=UTF8&amp;node=2
669348011" class="nav_a nav_item">New & Notable</a></li><li class="nav_subcat_li
nk nav_pop_li"><a href="/b?ie=UTF8&amp;node=2669344011" class="nav_a nav_item">L
istener Favorites</a></li><li class="nav_taglined nav_subcat_link nav_pop_li"><a
 href="/b?ie=UTF8&amp;node=5744819011" class="nav_a nav_item">Whispersync for Vo
ice</a><div class="nav_tag">Switch between reading and listening</div></li></ul>
</div>
<div id="nav_subcats_7" data-nav-promo-id="books"  class="nav_browse_subcat"><ul
 class="nav_browse_ul nav_browse_cat_ul"><li class="nav_pop_li nav_browse_cat_he
ad">Books</li><li class="nav_first nav_subcat_link nav_pop_li"><a href="/books-u
sed-books-textbooks/b?ie=UTF8&amp;node=283155" class="nav_a nav_item">Books</a><
/li><li class="nav_subcat_link nav_pop_li"><a href="/Kindle-eBooks/b?ie=UTF8&amp
;node=1286228011" class="nav_a nav_item">Kindle Books</a></li><li class="nav_sub
cat_link nav_pop_li"><a href="/Childrens-Books/b?ie=UTF8&amp;node=4" class="nav_
a nav_item">Children's Books</a></li><li class="nav_subcat_link nav_pop_li"><a h
ref="/New-Used-Textbooks-Books/b?ie=UTF8&amp;node=465600" class="nav_a nav_item"
>Textbooks</a></li><li class="nav_subcat_link nav_pop_li"><a href="/Audiobooks-B
ooks/b?ie=UTF8&amp;node=368395011" class="nav_a nav_item">Audiobooks</a></li><li
 class="nav_subcat_link nav_pop_li"><a href="/magazines/b?ie=UTF8&amp;node=59985
8" class="nav_a nav_item">Magazines</a></li><li class="nav_subcat_link nav_pop_l
i nav_divider_before"><a href="/Sell-Books/b?ie=UTF8&amp;node=2205237011" class=
"nav_a nav_item">Sell Your Books</a></li></ul></div>
<div id="nav_subcats_8" data-nav-promo-id="movies-music-games" data-nav-wt='1965
0' class="nav_browse_subcat"><ul class="nav_browse_ul nav_browse_cat_ul"><li cla
ss="nav_pop_li nav_browse_cat_head">Movies, Music & Games</li><li class="nav_fir
st nav_subcat_link nav_pop_li"><a href="/movies-tv-dvd-bluray/b?ie=UTF8&amp;node
=2625373011" class="nav_a nav_item">Movies & TV</a></li><li class="nav_subcat_li
nk nav_pop_li"><a href="/movies-tv-bluray-bluray3d/b?ie=UTF8&amp;node=2901953011
" class="nav_a nav_item">Blu-ray</a></li><li class="nav_subcat_link nav_pop_li">
<a href="/Instant-Video/b?ie=UTF8&amp;node=2858778011" class="nav_a nav_item">Am
azon Instant Video</a></li><li class="nav_subcat_link nav_pop_li nav_divider_bef
ore"><a href="/music-rock-classical-pop-jazz/b?ie=UTF8&amp;node=5174" class="nav
_a nav_item">Music</a></li><li class="nav_subcat_link nav_pop_li"><a href="/MP3-
Music-Download/b?ie=UTF8&amp;node=163856011" class="nav_a nav_item">MP3 Download
s</a></li><li class="nav_subcat_link nav_pop_li"><a href="/musical-instruments-a
ccessories-sound-recording/b?ie=UTF8&amp;node=11091801" class="nav_a nav_item">M
usical Instruments</a></li><li class="nav_subcat_link nav_pop_li nav_divider_bef
ore"><a href="/computer-video-games-hardware-accessories/b?ie=UTF8&amp;node=4686
42" class="nav_a nav_item">Video Games</a></li><li class="nav_subcat_link nav_po
p_li"><a href="/Game-Downloads/b?ie=UTF8&amp;node=979455011" class="nav_a nav_it
em">Digital Games</a></li></ul></div>
<div id="nav_subcats_9" data-nav-promo-id="electronics-computers"  class="nav_br
owse_subcat nav_super_cat"><ul class="nav_browse_ul nav_browse_cat_ul"><li class
="nav_first nav_pop_li nav_browse_cat_head">Electronics</li><li class="nav_first
 nav_subcat_link nav_pop_li"><a href="/Televisions-Video/b?ie=UTF8&amp;node=1266
092011" class="nav_a nav_item">TV & Video</a></li><li class="nav_subcat_link nav
_pop_li"><a href="/Home-Audio-Electronics/b?ie=UTF8&amp;node=667846011" class="n
av_a nav_item">Home Audio & Theater</a></li><li class="nav_subcat_link nav_pop_l
i"><a href="/Camera-Photo-Film-Canon-Sony/b?ie=UTF8&amp;node=502394" class="nav_
a nav_item">Camera, Photo & Video</a></li><li class="nav_subcat_link nav_pop_li"
><a href="/cell-phones-service-plans-accessories/b?ie=UTF8&amp;node=2335752011" 
class="nav_a nav_item">Cell Phones & Accessories</a></li><li class="nav_subcat_l
ink nav_pop_li"><a href="/computer-video-games-hardware-accessories/b?ie=UTF8&am
p;node=468642" class="nav_a nav_item">Video Games</a></li><li class="nav_subcat_
link nav_pop_li"><a href="/MP3-Players-Audio-Video/b?ie=UTF8&amp;node=172630" cl
ass="nav_a nav_item">MP3 Players & Accessories</a></li><li class="nav_subcat_lin
k nav_pop_li"><a href="/Car-Electronics/b?ie=UTF8&amp;node=1077068" class="nav_a
 nav_item">Car Electronics & GPS</a></li><li class="nav_subcat_link nav_pop_li">
<a href="/Appliances/b?ie=UTF8&amp;node=2619525011" class="nav_a nav_item">Appli
ances</a></li><li class="nav_subcat_link nav_pop_li"><a href="/musical-instrumen
ts-accessories-sound-recording/b?ie=UTF8&amp;node=11091801" class="nav_a nav_ite
m">Musical Instruments</a></li><li class="nav_subcat_link nav_pop_li"><a href="/
b?ie=UTF8&amp;node=5745855011" class="nav_a nav_item">Electronics Accessories</a
></li></ul>
<ul class="nav_browse_ul nav_browse_cat2_ul">
<li class="nav_pop_li nav_browse_cat_head">Computers</li><li class="nav_first na
v_subcat_link nav_pop_li"><a href="/Laptops-Tablets/b?ie=UTF8&amp;node=295650101
1" class="nav_a nav_item"> Laptops, Ultrabooks & Tablets</a></li><li class="nav_
subcat_link nav_pop_li"><a href="/Desktops/b?ie=UTF8&amp;node=4972214011" class=
"nav_a nav_item">Desktops & Monitors</a></li><li class="nav_taglined nav_subcat_
link nav_pop_li"><a href="/Computer-Accessories/b?ie=UTF8&amp;node=2956536011" c
lass="nav_a nav_item">Computer Accessories & Peripherals</a><div class="nav_tag"
>External drives, mice, networking & more</div></li><li class="nav_subcat_link n
av_pop_li"><a href="/PC-Parts-Components/b?ie=UTF8&amp;node=193870011" class="na
v_a nav_item">Computer Parts & Components</a></li><li class="nav_subcat_link nav
_pop_li"><a href="/design-download-business-education-software/b?ie=UTF8&amp;nod
e=229534" class="nav_a nav_item">Software</a></li><li class="nav_subcat_link nav
_pop_li"><a href="/PC-Games/b?ie=UTF8&amp;node=229575" class="nav_a nav_item">PC
 Games</a></li><li class="nav_subcat_link nav_pop_li"><a href="/Printers-Office-
Electronics/b?ie=UTF8&amp;node=172635" class="nav_a nav_item">Printers & Ink</a>
</li><li class="nav_subcat_link nav_pop_li"><a href="/office-products-supplies-e
lectronics-furniture/b?ie=UTF8&amp;node=1064954" class="nav_a nav_item">Office &
 School Supplies</a></li></ul></div>
<div id="nav_subcats_10" data-nav-promo-id="home-garden-tools"  class="nav_brows
e_subcat nav_super_cat"><ul class="nav_browse_ul nav_browse_cat_ul"><li class="n
av_first nav_pop_li nav_browse_cat_head">Home, Garden &amp; Pets</li><li class="
nav_first nav_subcat_link nav_pop_li"><a href="/kitchen-dining-small-appliances-
cookw'are/b?ie=UTF8&amp;node=284507" class="nav_a nav_item">Kitchen & Dining</a>
</li><li class="nav_subcat_link nav_pop_li"><a href="/furniture-decor-rugs-lamps
-beds-tv-stands/b?ie=UTF8&amp;node=1057794" class="nav_a nav_item">Furniture & D
\xe9cor</a></li><li class'="nav_subcat_link nav_pop_li"><a href="/bedding-bath-s
heets-towels/b?ie=UTF8&amp;node=1057792" class="nav_a nav_item">Bedding & Bath</
a></li><li class="nav_subcat_link nav_pop_li"><a href="/Appliances/b?ie=UTF8&amp
;node=2619525011" class="nav_a nav_item">Appliances</a></li><li class="nav_subca
t_link nav_pop_li"><a href="/Patio-Lawn-Garden/b?ie=UTF8&amp;node=2972638011" cl
ass="nav_a nav_item">Patio, Lawn & Garden</a></li><li class="nav_subcat_link nav
_pop_li"><a href="/Arts-Crafts-Sewing/b?ie=UTF8&amp;node=2617941011" class="nav_
a nav_item">Arts, Crafts & Sewing</a></li><li class="nav_subcat_link nav_pop_li"
><a href="/pet-supplies-dog-cat-food-bed-toy/b?ie=UTF8&amp;node=2619533011" clas
s="nav_a nav_item">Pet Supplies</a></li></ul>
<ul class="nav_browse_ul nav_browse_cat2_ul">
<li class="nav_pop_li nav_browse_cat_head">Tools, Home Improvement</li><li class="nav_first nav_subcat_link nav_pop_li"><a href="/Tools-and-Home-Improvement/b?ie=UTF8&amp;node=228013" class="nav_a nav_item">Home Improvement</a></li><li class="nav_subcat_link nav_pop_li"><a href="/Power-Tools-and-Hand-Tools/b?ie=UTF8&amp;node=328182011" class="nav_a nav_item">Power & Hand Tools</a></li><li class="nav_subcat_link nav_pop_li"><a href="/lighting-and-ceiling-fans/b?ie=UTF8&amp;node=495224" class="nav_a nav_item">Lamps & Light Fixtures</a></li><li class="nav_subcat_link nav_pop_li"><a href="/Kitchen-and-Bath-Fixtures/b?ie=UTF8&amp;node=3754161" class="nav_a nav_item">Kitchen & Bath Fixtures</a></li><li class="nav_subcat_link nav_pop_li"><a href="/Hardware-Locks-and-Fasteners/b?ie=UTF8&amp;node=511228" class="nav_a nav_item">Hardware</a></li><li class="nav_subcat_link nav_pop_li"><a href="/building-supplies/b?ie=UTF8&amp;node=551240" class="nav_a nav_item">Building Supplies</a></li></ul></div>
<div id="nav_subcats_11" data-nav-promo-id="grocery-health-beauty" data-nav-wt='
20600' class="nav_browse_subcat"><ul class="nav_browse_ul nav_browse_cat_ul"><li
 class="nav_pop_li nav_browse_cat_head">Grocery, Health & Beauty</li><li class="
nav_first nav_subcat_link nav_pop_li"><a href="/grocery-breakfast-foods-snacks-o
rganic/b?ie=UTF8&amp;node=16310101" class="nav_a nav_item">Grocery & Gourmet Foo
d</a></li><li class="nav_subcat_link nav_pop_li"><a href="/b?ie=UTF8&amp;node=29
83386011" class="nav_a nav_item">Wine</a></li><li class="nav_subcat_link nav_pop
_li"><a href="/Natural-Organic-Grocery/b?ie=UTF8&amp;node=51537011" class="nav_a
 nav_item">Natural & Organic</a></li><li class="nav_subcat_link nav_pop_li"><a h
ref="/health-personal-care-nutrition-fitness/b?ie=UTF8&amp;node=3760901" class="
nav_a nav_item">Health & Personal Care</a></li><li class="nav_subcat_link nav_po
p_li"><a href="/beauty-makeup-fragrance-skin-care/b?ie=UTF8&amp;node=3760911" cl
ass="nav_a nav_item">Beauty</a></li><li class="nav_subcat_link nav_pop_li"><a hr
ef="/b?ie=UTF8&amp;node=5856180011" class="nav_a nav_item">50+ Active & Healthy 
Living</a></li></ul></div>
<div id="nav_subcats_12" data-nav-promo-id="toys-kids-baby"  class="nav_browse_s
ubcat"><ul class="nav_browse_ul nav_browse_cat_ul"><li class="nav_pop_li nav_bro
wse_cat_head">Toys, Kids & Baby</li><li class="nav_first nav_subcat_link nav_pop
_li"><a href="/toys/b?ie=UTF8&amp;node=165793011" class="nav_a nav_item">Toys & 
Games</a></li><li class="nav_subcat_link nav_pop_li"><a href="/baby-car-seats-st
rollers-bedding/b?ie=UTF8&amp;node=165796011" class="nav_a nav_item">Baby</a></l
i><li class="nav_subcat_link nav_pop_li"><a href="/Kids-Baby-Clothing/b?ie=UTF8&
amp;node=1040662" class="nav_a nav_item">Kids' Clothing</a></li><li class="nav_s
ubcat_link nav_pop_li"><a href="/l/2402554011" class="nav_a nav_item">Baby Cloth
ing</a></li><li class="nav_subcat_link nav_pop_li"><a href="/Kids-Family/b?ie=UT
F8&amp;node=471306" class="nav_a nav_item">Video Games for Kids</a></li><li clas
s="nav_taglined nav_subcat_link nav_pop_li"><a href="/gp/mom/signup" class="nav_
a nav_item">Amazon Mom</a><div class="nav_tag">20% off diapers, free shipping an
d more</div></li><li class="nav_subcat_link nav_pop_li"><a href="/gp/registry/ba
by" class="nav_a nav_item">Baby Registry</a></li></ul></div>
<div id="nav_subcats_13" data-nav-promo-id="clothing-shoes-jewelry"  class="nav_
browse_subcat"><ul class="nav_browse_ul nav_browse_cat_ul"><li class="nav_pop_li
 nav_browse_cat_head">Clothing, Shoes & Jewelry</li><li class="nav_first nav_sub
cat_link nav_pop_li"><a href="/clothing-accessories-men-women-kids/b?ie=UTF8&amp
;node=1036592" class="nav_a nav_item">Clothing</a></li><li class="nav_subcat_lin
k nav_pop_li"><a href="/shoes-men-women-kids-baby/b?ie=UTF8&amp;node=672123011" 
class="nav_a nav_item">Shoes</a></li><li class="nav_subcat_link nav_pop_li"><a h
ref="/Handbags-Accessories-Clothing/b?ie=UTF8&amp;node=15743631" class="nav_a na
v_item">Handbags</a></li><li class="nav_subcat_link nav_pop_li"><a href="/Handba
gs-Designer-Sunglasses-iPod-Case/b?ie=UTF8&amp;node=1036700" class="nav_a nav_it
em">Accessories</a></li><li class="nav_subcat_link nav_pop_li"><a href="/Luggage
-Bags-Travel-Accessories-Clothing/b?ie=UTF8&amp;node=15743161" class="nav_a nav_
item">Luggage</a></li><li class="nav_subcat_link nav_pop_li"><a href="/jewelry-w
atches-engagement-rings-diamonds/b?ie=UTF8&amp;node=3367581" class="nav_a nav_it
em">Jewelry</a></li><li class="nav_subcat_link nav_pop_li"><a href="/Watches-Men
s-Womens-Kids-Accessories/b?ie=UTF8&amp;node=377110011" class="nav_a nav_item">W
atches</a></li></ul></div>
<div id="nav_subcats_14" data-nav-promo-id="sports-outdoors" data-nav-wt='18547'
 class="nav_browse_subcat"><ul class="nav_browse_ul nav_browse_cat_ul"><li class
="nav_pop_li nav_browse_cat_head">Sports & Outdoors</li><li class="nav_first nav
_subcat_link nav_pop_li"><a href="/Exercise-Fitness-Sports-Outdoors/b?ie=UTF8&am
p;node=3407731" class="nav_a nav_item">Exercise & Fitness</a></li><li class="nav
_subcat_link nav_pop_li"><a href="/Outdoor-Recreation/b?ie=UTF8&amp;node=7068140
11" class="nav_a nav_item">Outdoor Recreation</a></li><li class="nav_subcat_link
 nav_pop_li"><a href="/Hunting-Fishing/b?ie=UTF8&amp;node=706813011" class="nav_
a nav_item">Hunting &amp; Fishing</a></li><li class="nav_subcat_link nav_pop_li"
><a href="/cycling-bikes-bicycles-bike-sale/b?ie=UTF8&amp;node=3403201" class="n
av_a nav_item">Cycling</a></li><li class="nav_subcat_link nav_pop_li"><a href="/
Apparel/b?ie=UTF8&amp;node=2206626011" class="nav_a nav_item">Athletic & Outdoor
 Clothing</a></li><li class="nav_subcat_link nav_pop_li"><a href="/Boating-Water
-Sports-Outdoors/b?ie=UTF8&amp;node=3421331" class="nav_a nav_item">Boating & Wa
ter Sports</a></li><li class="nav_subcat_link nav_pop_li"><a href="/Team-Sports-
Outdoors/b?ie=UTF8&amp;node=706809011" class="nav_a nav_item">Team Sports</a></l
i><li class="nav_subcat_link nav_pop_li"><a href="/Fan-Shop-Sports-Outdoors/b?ie
=UTF8&amp;node=3386071" class="nav_a nav_item">Fan Shop</a></li><li class="nav_s
ubcat_link nav_pop_li"><a href="/Sports-Collectibles/b?ie=UTF8&amp;node=32506970
11" class="nav_a nav_item">Sports Collectibles</a></li><li class="nav_subcat_lin
k nav_pop_li"><a href="/Golf-Sports-Outdoors/b?ie=UTF8&amp;node=3410851" class="
nav_a nav_item">Golf</a></li><li class="nav_subcat_link nav_pop_li"><a href="/sp
orting-goods-clothing-cycling-exercise/b?ie=UTF8&amp;node=3375251" class="nav_a 
nav_item">All Sports & Outdoors</a></li></ul></div>
<div id="nav_subcats_15" data-nav-promo-id="automotive-industrial"  class="nav_b
rowse_subcat"><ul class="nav_browse_ul nav_browse_cat_ul"><li class="nav_first n
av_pop_li nav_browse_cat_head">Automotive</li><li class="nav_first nav_subcat_li
nk nav_pop_li"><a href="/automotive-auto-truck-replacements-parts/b?ie=UTF8&amp;
node=15684181" class="nav_a nav_item">Automotive Parts & Accessories</a></li><li
 class="nav_subcat_link nav_pop_li"><a href="/Tools-Equipment-Automotive/b?ie=UT
F8&amp;node=15706941" class="nav_a nav_item">Automotive Tools & Equipment</a></l
i><li class="nav_subcat_link nav_pop_li"><a href="/Car-Electronics/b?ie=UTF8&amp
;node=1077068" class="nav_a nav_item">Car Electronics & GPS</a></li><li class="n
av_subcat_link nav_pop_li"><a href="/b?ie=UTF8&amp;node=15706571" class="nav_a n
av_item">Tires & Wheels</a></li><li class="nav_subcat_link nav_pop_li"><a href="
/Motorcycle-ATV-Automotive/b?ie=UTF8&amp;node=346333011" class="nav_a nav_item">
Motorcycle & ATV</a></li><li class="nav_pop_li nav_browse_cat_head nav_divider_b
efore">Industrial & Scientific</li><li class="nav_first nav_subcat_link nav_pop_
li"><a href="/industrial-scientific-supplies/b?ie=UTF8&amp;node=16310091" class=
"nav_a nav_item">Industrial Supplies</a></li><li class="nav_subcat_link nav_pop_
li"><a href="/Lab-Scientific-Supplies/b?ie=UTF8&amp;node=317970011" class="nav_a
 nav_item">Lab & Scientific</a></li><li class="nav_subcat_link nav_pop_li"><a hr
ef="/b?ie=UTF8&amp;node=317971011" class="nav_a nav_item">Janitorial</a></li><li
 class="nav_subcat_link nav_pop_li"><a href="/b?ie=UTF8&amp;node=318135011" clas
s="nav_a nav_item">Safety</a></li></ul></div>

    </div>
    <div class="nav_subcats_div"></div>
    <div class="nav_subcats_div nav_subcats_div2"></div>
  </div>
  <div id="nav_cats_wrap" class="nav_browse_wrap">
    <ul id="nav_cats" class="nav_browse_ul">
      <li class="nav_first nav_pop_li nav_cat" id="nav_cat_0">Unlimited Instant 
Videos</li><li class="nav_taglined nav_pop_li nav_cat" id="nav_cat_1">MP3s & Clo
ud Player<div class="nav_tag">20 million songs, play anywhere</div></li><li clas
s="nav_taglined nav_pop_li nav_cat" id="nav_cat_2">Amazon Cloud Drive<div class=
"nav_tag">5 GB of free storage</div></li><li class="nav_pop_li nav_cat" id="nav_
cat_3">Kindle</li><li class="nav_taglined nav_pop_li nav_cat" id="nav_cat_4">App
store for Android<div class="nav_tag">Get a premium app for free today<span id="
nav_amabotandroid"></span></div></li><li class="nav_pop_li nav_cat" id="nav_cat_
5">Digital Games & Software</li><li class="nav_pop_li nav_cat" id="nav_cat_6">Au
dible Audiobooks</li><li class="nav_pop_li nav_cat nav_divider_before" id="nav_c
at_7">Books</li><li class="nav_pop_li nav_cat" id="nav_cat_8">Movies, Music & Ga
mes</li><li class="nav_pop_li nav_cat" id="nav_cat_9">Electronics & Computers</l
i><li class="nav_pop_li nav_cat" id="nav_cat_10">Home, Garden & Tools</li><li cl
ass="nav_pop_li nav_cat" id="nav_cat_11">Grocery, Health & Beauty</li><li class=
"nav_pop_li nav_cat" id="nav_cat_12">Toys, Kids & Baby</li><li class="nav_pop_li
 nav_cat" id="nav_cat_13">Clothing, Shoes & Jewelry</li><li class="nav_pop_li na
v_cat" id="nav_cat_14">Sports & Outdoors</li><li class="nav_pop_li nav_cat" id="
nav_cat_15">Automotive & Industrial</li><li class="nav_last nav_pop_li nav_divid
er_before nav_a_carat" id="nav_cat_16"><span class="nav_a_carat">&rsaquo;</span>
<a href="/gp/site-directory" class="nav_a">Full Store Directory</a></li>
    </ul>
    <div id="nav_cat_indicator" class="nav-sprite"></div>
  </div>
</div>












<div id="nav_your_account_flyout" class="nav-flyout-content">  <ul class="nav_pop_ul">
<li class="nav_pop_li nav_divider_after">
  <div><a href="https://www.amazon.com/ap/signin?_encoding=UTF8&openid.assoc_handle=usflex&openid.claimed_id=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.identity=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.mode=checkid_setup&openid.ns=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0&openid.ns.pape=http%3A%2F%2Fspecs.openid.net%2Fextensions%2Fpape%2F1.0&openid.pape.max_auth_age=0&openid.return_to=https%3A%2F%2Fwww.amazon.com%2Fgp%2Fyourstore%2Fhome%3Fie%3DUTF8%26ref_%3Dgno_signin" class="nav-action-button nav-sprite" rel="nofollow">
      <span class='nav-action-inner nav-sprite'>Sign in</span>
    </a></div>
  <div class="nav_pop_new_cust">New customer? <a href="https://www.amazon.com/ap/register?_encoding=UTF8&openid.assoc_handle=usflex&openid.claimed_id=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.identity=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.mode=checkid_setup&openid.ns=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0&openid.ns.pape=http%3A%2F%2Fspecs.openid.net%2Fextensions%2Fpape%2F1.0&openid.pape.max_auth_age=0&openid.return_to=https%3A%2F%2Fwww.amazon.com%2Fgp%2Fyourstore%2Fhome%3Fie%3DUTF8%26ref_%3Dgno_newcust" rel="nofollow" class="nav_a">Start here.</a></div>
</li>
<li class="nav_first nav_pop_li"><a href="https://www.amazon.com/gp/css/homepage
.html" class="nav_a nav_a">Your Account</a></li><li class="nav_pop_li"><a href="
https://www.amazon.com/gp/css/order-history" class="nav_a nav_a" id="nav_prefetc
h_yourorders">Your Orders</a></li><li class="nav_pop_li"><a href="/gp/registry/w
ishlist" class="nav_a nav_a">Your Wish List</a></li><li class="nav_pop_li"><a hr
ef="/gp/yourstore" class="nav_a nav_a">Your Recommendations</a></li><li class="n
av_pop_li"><a href="https://www.amazon.com/gp/subscribe-and-save/manager/viewsub
scriptions" class="nav_a nav_a">Your Subscribe & Save Items</a></li><li class="n
av_pop_li" id="nav_ya_your_collections"><a href="/gp/customers/me/collections" c
lass="nav_a nav_a">Your Collections</a></li><li class="nav_pop_li nav_divider_be
fore"><a href="/gp/digital/fiona/manage" class="nav_a nav_a">Manage Your Kindle<
/a></li><li class="nav_taglined nav_pop_li"><a href="/gp/dmusic/mp3/player" clas
s="nav_a nav_a">Your Cloud Player</a><div class="nav_tag">Play from any browser<
/div></li><li class="nav_taglined nav_pop_li"><a href="/clouddrive" class="nav_a
 nav_a">Your Cloud Drive</a><div class="nav_tag">5 GB of free storage</div></li>
<li class="nav_taglined nav_pop_li"><a href="/b?ie=UTF8&amp;node=2676882011" cla
ss="nav_a nav_a">Prime Instant Videos</a><div class="nav_tag">Unlimited streaming of thousands<br />of movies and TV shows</div></li><li class="nav_pop_li"><a href="/gp/video/library" class="nav_a nav_a">Your Video Library</a></li><li class="nav_pop_li"><a href="/gp/swvgdtt/your-account/manage-downloads.html" class="nav_a nav_a">Your Games & Software Library</a></li><li class="nav_last nav_pop_li"><a href="/gp/mas/your-account/myapps" class="nav_a nav_a">Your Android Apps & Devices</a></li>   </ul>   <!--[if IE ]>      <div class='nav-ie-min-width' style='width: 160px'></div>    <![endif]-->  </div>











<div id="nav_cart_flyout" class="nav-empty nav-flyout-content">
  <ul class='nav_dynamic'></ul>
  <div class='nav-ajax-message'></div>
  <div class='nav-dynamic-empty'>
    <p class='nav_p nav-bold nav-cart-empty'> Your Shopping Cart is empty.</p>
    <p class='nav_p '> Give it purpose&mdash;fill it with books, DVDs, clothes, electronics, and more.</p>
    <p class='nav_p '> If you already have an account, <a href="https://www.amazon.com/ap/signin?_encoding=UTF8&openid.assoc_handle=usflex&openid.claimed_id=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.identity=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.mode=checkid_setup&openid.ns=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0&openid.ns.pape=http%3A%2F%2Fspecs.openid.net%2Fextensions%2Fpape%2F1.0&openid.pape.max_auth_age=0&openid.return_to=https%3A%2F%2Fwww.amazon.com%2Fgp%2Fyourstore%2Fhome%3Fie%3DUTF8%26ref_%3Dgno_signin_cart" class="nav_a">sign in</a>.</p>
  </div>
  <div class='nav-ajax-error-msg'>
    <p class='nav_p nav-bold'> There's a problem previewing your cart right now.</p>
    <p class='nav_p '> Check your Internet connection and <a href="/gp/cart/view.html?ie=UTF8&hasWorkingJavascript=1" class="nav_a">go to your cart</a>, or <a href='javascript:void(0);' class='nav_a nav-try-again'>try again</a>.</p>
  </div>

      <a href="/gp/cart/view.html?ie=UTF8&hasWorkingJavascript=1" id="nav-cart-menu-button" class="nav-action-button nav-sprite"><span class="nav-action-inner nav-sprite">
      View Cart
      <span class='nav-ajax-success'>
        <span id='nav-cart-zero'>(<span class='nav-cart-count'>0</span> items)</span>
        <span id='nav-cart-one' style='display: none;'>(<span class='nav-cart-count'>0</span> item)</span>
        <span id='nav-cart-many' style='display: none;'>(<span class='nav-cart-count'>0</span> items)</span>
      </span>
    </span></a>
  
  
</div>









<div id="nav_wishlist_flyout" class="nav-empty nav-flyout-content">
  <div class='nav-ajax-message'></div>
  <ul class='nav_dynamic nav_pop_ul nav_divider_after'></ul>
  <ul class="nav_pop_ul">
    <li class="nav_first nav_pop_li nav-dynamic-empty"><a href="/gp/wishlist" class="nav_a nav_a">Create a Wish List</a></li><li class="nav_pop_li"><a href="/gp/gift-central" class="nav_a nav_a">Find a Wish List or Registry</a></li><li class="nav_taglined nav_pop_li"><a href="/wishlist/universal" class="nav_a nav_a">Wish from Any Website</a><div class="nav_tag">Add items to your List from anywhere</div></li><li class="nav_pop_li"><a href="/gp/wedding/homepage" class="nav_a nav_a">Wedding Registry</a></li><li class="nav_pop_li"><a href="/gp/registry/baby" class="nav_a nav_a">Baby Registry</a></li><li class="nav_pop_li"><a href="/gp/toys/birthday" class="nav_a nav_a">Kids' Birthdays</a></li><li class="nav_last nav_pop_li"><a href="/gp/gift-central/organizer" class="nav_a nav_a">Friends & Family Gifting</a></li>
  </ul>
</div>





<script type='text/html' id='nav-tpl-wishlist'>
  <# jQuery.each(wishlist, function (i, item) { #>
    <li class='nav_pop_li'>
      <a href='<#=item.url #>' class='nav_a'>
        <#=item.name #>
      </a>
      <div class='nav_tag'>
        <# if(typeof item.count !='undefined') { #>
          <#=
            (item.count == 1 ? "{count} item" : "{count} items")
              .replace("{count}", item.count)
          #>
        <# } #>
      </div>
    </li>
  <# }); #>
</script>
<script type='text/html' id='nav-tpl-cart'>
  <# jQuery.each(cart, function (i, item) { #>
    <li class='nav_cart_item'>
      <a href='<#=item.url #>' class='nav_a'>
        <img class='nav_cart_img' src='<#=item.img #>'/>
        <span class='nav-cart-title'><#=item.name #></span>
        <span class='nav-cart-quantity'>
          <# if(typeof item.wireless !== 'undefined') { #>
            <#= "Items: {count}".replace("{count}", item.qty) #>
          <# } else { #>
            <#= "Quantity: {count}".replace("{count}", item.qty) #>
          <# } #>
        </span>
      </a>
    </li>
  <# }); #>
</script>
<script type='text/html' id='nav-tpl-asin-promo'>
  <a href='<#=destination #>' class='nav_asin_promo'>
    <img src='<#=image #>' class='nav_asin_promo_img'/>
    <span class='nav_asin_promo_headline'><#=headline #></span>
    <span class='nav_asin_promo_info'>
      <span class='nav_asin_promo_title'><#=productTitle #></span>
      <span class='nav_asin_promo_title2'><#=productTitle2 #></span>
      <span class='nav_asin_promo_price'><#=price #></span>
    </span>
    <span class='nav_asin_promo_button nav-sprite'><#=button #></span>
  </a>
</script>












</div>
<script type='text/javascript'>window.$Nav.declare('config.prefetchUrls', ["http
://z-ecx.images-amazon.com/images/G/01/browser-scripts/fruitCSS/US-combined-2621
868138._V1_.css","http://z-ecx.images-amazon.com/images/G/01/browser-scripts/reg
istriesCSS/US-combined-545184966._V376148880_.css","https://images-na.ssl-images
-amazon.com/images/G/01/browser-scripts/us-site-wide-css-beacon/site-wide-680461
9766._V1_.css","https://images-na.ssl-images-amazon.com/images/G/01/browser-scri
pts/wcs-ya-homepage-beaconized/wcs-ya-homepage-beaconized-1899362992._V1_.css","
https://images-na.ssl-images-amazon.com/images/G/01/browser-scripts/wcs-ya-homep
age-beaconized/wcs-ya-homepage-beaconized-3515399030._V1_.js","https://images-na
.ssl-images-amazon.com/images/G/01/browser-scripts/wcs-ya-order-history-beaconiz
ed/wcs-ya-order-history-beaconized-2777963369._V1_.css","https://images-na.ssl-i
mages-amazon.com/images/G/01/gno/beacon/BeaconSprite-US-01._V397411194_.png","ht
tps://images-na.ssl-images-amazon.com/images/G/01/gno/images/general/navAmazonLo
goFooter._V169459313_.gif","https://images-na.ssl-images-amazon.com/images/G/01/
x-locale/common/transparent-pixel._V386942464_.gif","https://images-na.ssl-image
s-amazon.com/images/G/01/x-locale/communities/social/snwicons_v2._V369764580_.pn
g","https://images-na.ssl-images-amazon.com/images/G/01/x-locale/cs/css/images/a
mznbtn-sprite03._V387356454_.png","https://images-na.ssl-images-amazon.com/image
s/G/01/x-locale/cs/help/images/spotlight/kindle-family-02b._V386370244_.jpg","ht
tps://images-na.ssl-images-amazon.com/images/G/01/x-locale/cs/orders/images/acor
n._V192250692_.gif","https://images-na.ssl-images-amazon.com/images/G/01/x-local
e/cs/orders/images/amazon-gc-100._V192250695_.gif","https://images-na.ssl-images
-amazon.com/images/G/01/x-locale/cs/orders/images/amazon-gcs-100._V192250695_.gi
f","https://images-na.ssl-images-amazon.com/images/G/01/x-locale/cs/orders/image
s/btn-close._V192250694_.gif","https://images-na.ssl-images-amazon.com/images/G/
01/x-locale/cs/projects/text-trace/texttrace_typ._V381285749_.js","https://image
s-na.ssl-images-amazon.com/images/G/01/x-locale/cs/ya/images/new-link._V19225066
4_.gif","https://images-na.ssl-images-amazon.com/images/G/01/x-locale/cs/ya/imag
es/shipment_large_lt._V192250661_.gif"]);
_navbar = window._navbar || {};
_navbar.prefetch = function() { window.amznJQ && amznJQ.addPL(window.$Nav.getNow('config.prefetchUrls')); };
window.$Nav && $Nav.declare( 'config.prefetch', _navbar.prefetch );
    window.$Nav && $Nav.declare( 'config.flyoutURL', null );
    window.$Nav && $Nav.declare('btf.lite');
    window.amznJQ && amznJQ.declareAvailable('navbarBTFLite');
    window.$Nav && $Nav.declare('btf.full');
    window.amznJQ && amznJQ.declareAvailable('navbarBTF');
</script>








<script>
amznJQ.onReady('JQuery', function() {
  jQuery(window).load(function() {
    setTimeout(function() {
      amznJQ.available('lazyLoadLib', function() {
        jQuery('#product-discussion_divID').lazyLoadContent({
          url: '/review/dynamic/product-discussion?ie=UTF8&asin=B007SBGF12',
          metrics : true,
          name : 'product-discussion',
          cache : true
        });
      });
    }, 0); 
  });
});
</script>
<div id=product-discussion_divID>
</div>







<script>
amznJQ.onReady('JQuery', function() {
  jQuery(window).load(function() {
    setTimeout(function() {
      amznJQ.available('lazyLoadLib', function() {
        jQuery('#gallery-sponsored-links_divID').lazyLoadContent({
          url: '/review/dynamic/gallery-sponsored-links?ie=UTF8&asin=B007SBGF12&viewID=product',
          metrics : true,
          name : 'gallery-sponsored-links',
          cache : true
        });
      });
    }, 0); 
  });
});
</script>
<div id=gallery-sponsored-links_divID>
  <div id='cdLazyLoadThreadBTFNotLoaded' class='cdLazyLoadingIndicator'>
    <img src="http://g-ecx.images-amazon.com/images/G/01/ui/loadIndicators/loadIndicator-large._V192195480_.gif" width="100" height="124" border="0" />
  </div>
</div>

  <br />
</td>
<td valign="top" width="300px">
  





































  
  








  
  
  






  


















<div><img src="http://g-ecx.images-amazon.com/images/G/01/nav2/images/transp._V192548636_.gif" width="300" alt="" height="1" border="0" /></div>


<div class="cBox secEyebrow">
  <span class="cBoxTL"><!-- &nbsp; --></span>
  <span class="cBoxTR"><!-- &nbsp; --></span>
  <span class="cBoxR"><!-- &nbsp; --></span>
  <span class="cBoxBL"><!-- &nbsp; --></span>
  <span class="cBoxBR"><!-- &nbsp; --></span>
  <span class="cBoxB"><!-- &nbsp; --></span>
  <h2>This product</h2>
  <div class="cBoxInner">
<style>
  .crProductInfo .imageBlock {
    text-align:center;
    padding:13px 0 4px 0;
  }
  .crProductInfo .imageBlock img {
    border:0px;
  }
  .crProductInfo .headerBlock a {
    color:#039;
  }
  .crProductInfo a {
    text-decoration:underline;
    color:#963;
  }
  .crProductInfo .reviewSummaryLink {
    text-decoration:none;
  }
  .crProductInfo a:hover {
    color:#c60;
  }
  .crProductInfo .buyBlock a {
    text-decoration:underline;
  }
  .crProductInfo .buyBlock .buttonsBlock {
    margin-bottom: 5px;
  }
  .crProductInfo .buyBlock .price {
    font-weight:bold;
  }
  .crProductInfo .used .price {
    font-weight:normal;
  }
  .crProductInfo .avail
  {
    font-size:9px;
  }
</style>
<div class="crProductInfo">
<table><tr><td style="vertical-align:top;padding-top:5px;width:100px;">
   <div class="imageBlock" style="padding: 0 0 10px 0;">
    <a href="http://www.amazon.com/Multi-Angles-Leather-Protection-i-UniK-Blue/dp/B007SBGF12"><img src="http://ecx.images-amazon.com/images/I/41TmSYOcwXL._SL160_SL90_.jpg" width="70" alt="7 Inch Multi-Angles Google Nexus 7 Tablet Leather Protection Case by i-UniK (Light Blue) - Colors Available: Hot Pink, Red, Lime Green, Light Blue, Expresso Black" height="90" border="0" /></a>
  </div>
  </td>
  <td style="vertical-align:top;padding-top:5px;padding-left:10px">

  <div class="description"><a href="http://www.amazon.com/Multi-Angles-Leather-Protection-i-UniK-Blue/dp/B007SBGF12">7 Inch Multi-Angles Google Nexus 7 Tablet Leather Protection Case by i-UniK (Light Blue) - Colors Available: Hot Pink, Red, Lime Green, L...</a> by i-UniK</div>


  <div class="buyBlock">

    <div class="pricing">
      <span class="listprice">$29.99</span> <span class="price">$8.99</span>
      
      <br />
      
<span class="avail">In Stock</span>

      <br />
    </div>

</td></tr><tr><td colspan="2">
        <div class="buttonsBlock">
          <span style="padding-right:2px"><a href="http://www.amazon.com/gp/item
-dispatch?ie=UTF8&amp;asin.1=B007SBGF12&amp;offering-id.y1srxLH3ghK5wFeU1jzEfJHN
JS%252FuKH1D9QatKZFi7YOb3waquEHQi7T8V5UJh%252BDVSHfPkePXtDrGdACJ6o%252B7nzBapVVN
yCm%252B937HFozcL2jG771%252BWu%252BTxxXocAMwAVZ%252FzrUwJxfVas%252BOLXWaRp87ucU%
252FbSC9mcYo=1&amp;session-id=000-0000000-0000000&amp;submit.addToCart=addToCart
"><img src="http://g-ecx.images-amazon.com/images/G/01/x-locale/communities/rich
pub/addtocart_med._V192249904_.gif" width="111" vspace="2" alt="Add to cart" hei
ght="22" border="0" /></a></span> <span><a href="http://www.amazon.com/gp/item-d
ispatch?ie=UTF8&amp;asin.1=B007SBGF12&amp;offeringID.1=y1srxLH3ghK5wFeU1jzEfJHNJ
S%252FuKH1D9QatKZFi7YOb3waquEHQi7T8V5UJh%252BDVSHfPkePXtDrGdACJ6o%252B7nzBapVVNy
Cm%252B937HFozcL2jG771%252BWu%252BTxxXocAMwAVZ%252FzrUwJxfVas%252BOLXWaRp87ucU%2
52FbSC9mcYo&amp;sid=000-0000000-0000000&amp;submit.add-to-registry=addToRegistry
&amp;type=wishlist"><img src="http://g-ecx.images-amazon.com/images/G/01/x-local
e/communities/richpub/addtowl_med._V192249907_.gif" width="111" vspace="2" alt="
Add to wishlist" height="22" border="0" /></a></span>
        </div>
  </td><td>
</div>
</td></tr></table>
</div></div>
</div>  



















    
        


    







    



  <FORM method="GET" action="/gp/community-content-search/results/ref=cm_srch_q_rtr/" style="padding:0; margin:0;"> 
    <table border="0" cellpadding="0" cellspacing="0" style="" width="250">
        <tr>
            <td colspan="2" nowrap="nowrap" style="text-align:left;">
                <label for="search_rtr"><b class="tiny">Search Customer Reviews</b></label>
            </td>
        </tr>
        <tr>
                <td style="width: 100%">
                <input id="search_rtr" class="small" style="width: 100%;" type="text" name="query" value=""/>
                <input type="hidden" name="search-alias" value="community-reviews"/>
             
            </td>
            <td style="padding-left: 5px;"><input type="image" title="Go" alt="Go" border="0" class="swSprite s_goTan " id="" value="" name="Go" src="http://g-ecx.images-amazon.com/images/G/01/x-locale/common/transparent-pixel._V386942464_.gif"  /></td>
        </tr>
        <tr>
          <td colspan="2">
            <input type="checkbox" name="idx.asin" value="B007SBGF12" checked> <span class="tiny">Only search this product's reviews</span>
	  </td>
	</tr>
    </table>
  </FORM>












  
  
  

<div id="dc-display-right-ad-1" style="padding: 8px 0 0 0;"><script type='text/javascript'>var paCusRevAllURL = "http://product-ads-portal.amazon.com/gp/synd/?asin=B007SBGF12&pAsin=B007SBGF1M&gl=147&sq=&sa=&se=&noo=&pt=CustomerReviews&spt=ReadAll&sn=right-ad-1&pRID=0NSY087S35KR62AD2HD9&ts=1373278234&h=7E8EDE575CF07822ACEAF082C99403A90C0E7481";</script></div>







<script>
amznJQ.onReady('JQuery', function() {
  jQuery(window).load(function() {
    setTimeout(function() {
      amznJQ.available('lazyLoadLib', function() {
        jQuery('#sims-box_divID').lazyLoadContent({
          url: '/review/dynamic/sims-box?ie=UTF8&asin=B007SBGF12',
          metrics : true,
          name : 'sims-box',
          cache : true
        });
      });
    }, 0); 
  });
});
</script>
<div id=sims-box_divID>
  <div id='cdLazyLoadThreadBTFNotLoaded' class='cdLazyLoadingIndicator'>
    <img src="http://g-ecx.images-amazon.com/images/G/01/ui/loadIndicators/loadIndicator-large._V192195480_.gif" width="100" height="124" border="0" />
  </div>
</div>

  <br />
</td>
</tr>
</table>



    






    







































<div id="navFooter" role="contentinfo"><table class="navFooterThreeColumn" cells
pacing="0"><tr><td class="navFooterColSpacerOuter"></td><td class="navFooterLink
Col"><div class="navFooterColHead">Get to Know Us</div><ul><li class="nav_first"
><a href="/gp/jobs" class="nav_a">Careers</a></li><li><a href="/gp/redirect.html
?_encoding=UTF8&amp;location=http%3A%2F%2Fphx.corporate-ir.net%2Fphoenix.zhtml%3
Fc%3D97664%26p%3Dirol-irhome&amp;token=F9CAD8A11D4336B5E0B3C3B089FA066D0A467C1C"
 class="nav_a">Investor Relations</a></li><li><a href="/gp/redirect.html?_encodi
ng=UTF8&amp;location=http%3A%2F%2Fphx.corporate-ir.net%2Fphoenix.zhtml%3Fc%3D176
060%26p%3Dirol-mediaHome&amp;token=F9CAD8A11D4336B5E0B3C3B089FA066D0A467C1C" cla
ss="nav_a">Press Releases</a></li><li><a href="/b?ie=UTF8&amp;node=13786321" cla
ss="nav_a">Amazon and Our Planet</a></li><li class="nav_last"><a href="/b?ie=UTF
8&amp;node=13786411" class="nav_a">Amazon in the Community</a></li></ul></td><td
 class="navFooterColSpacerInner"></td><td class="navFooterLinkCol"><div class="n
avFooterColHead">Make Money with Us</div><ul><li class="nav_first"><a href="/gp/
redirect.html?_encoding=UTF8&amp;location=http%3A%2F%2Fwww.amazonservices.com%2F
content%2Fsell-on-amazon.htm%2Fref%3Dfooter_soa%3Fld%3DAZFSSOA&amp;token=1E60AB4
AC0ECCA00151B45353E21782E539DC601" class="nav_a">Sell on Amazon</a></li><li><a h
ref="https://affiliate-program.amazon.com" class="nav_a">Become an Affiliate</a>
</li><li><a href="http://services.amazon.com/content/product-ads-on-amazon.htm/r
ef=footer_pads?ld=AZPADSFooter" class="nav_a">Advertise Your Products</a></li><l
i><a href="/gp/seller-account/mm-summary-page.html?ie=UTF8&amp;ld=AZFooterSelfPu
blish&amp;topic=200260520" class="nav_a">Independently Publish with Us</a></li><
li class="nav_last nav_a_carat"><span class="nav_a_carat">&rsaquo;</span><a href
="/gp/seller-account/mm-landing.html?ie=UTF8&amp;ld=AZSOAviewallMakeM" class="na
v_a">See all</a></li></ul></td><td class="navFooterColSpacerInner"></td><td clas
s="navFooterLinkCol"><div class="navFooterColHead">Let Us Help You</div><ul><li 
class="nav_first"><a href="https://www.amazon.com/gp/css/homepage.html" class="n
av_a">Your Account</a></li><li><a href="/gp/help/customer/display.html?ie=UTF8&a
mp;nodeId=468520" class="nav_a">Shipping Rates & Policies</a></li><li><a href="/
gp/prime" class="nav_a">Amazon Prime</a></li><li><a href="/gp/css/returns/homepa
ge.html" class="nav_a">Returns Are Easy</a></li><li><a href="/gp/digital/fiona/m
anage" class="nav_a">Manage Your Kindle</a></li><li class="nav_last"><a href="/g
p/help/customer/display.html?ie=UTF8&amp;nodeId=508510" class="nav_a">Help</a></
li></ul></td><td class="navFooterColSpacerOuter"></td></tr></table>
<div class="navFooterLine navFooterLogoLine"><a href="/"><img src="http://g-ecx.images-amazon.com/images/G/01/gno/images/general/navAmazonLogoFooter._V169459313_.gif" width="126" alt="amazon.com" height="24" border="0" /></a></div>
<div class="navFooterLine navFooterLinkLine navFooterPadItemLine"><ul><li class="nav_first"><a href="http://www.amazon.com.br" class="nav_a">Brazil</a></li><li><a href="http://www.amazon.ca/" class="nav_a">Canada</a></li><li><a href="http://www.amazon.cn/" class="nav_a">China</a></li><li><a href="http://www.amazon.fr/" class="nav_a">France</a></li><li><a href="http://www.amazon.de/" class="nav_a">Germany</a></li><li><a href="http://www.amazon.in/" class="nav_a">India</a></li><li><a href="http://www.amazon.it/" class="nav_a">Italy</a></li><li><a href="http://www.amazon.co.jp/" class="nav_a">Japan</a></li><li><a href="http://www.amazon.es/" class="nav_a">Spain</a></li><li class="nav_last"><a href="http://www.amazon.co.uk/" class="nav_a">United Kingdom</a></li></ul></div>
<div class="navFooterLine navFooterLinkLine navFooterDescLine"><table cellspacing="0"><tr>
<td class="navFooterDescSpacer" style="width: 36.0%"></td>
<td class="navFooterDescItem"><a href="http://www.6pm.com/" class="nav_a">6pm<br/> <span class="navFooterDescText">Score deals<br/> on fashion brands</span></a></td>
<td class="navFooterDescSpacer" style="width: 4%"></td>
<td class="navFooterDescItem"><a href="http://www.abebooks.com/" class="nav_a">AbeBooks<br/> <span class="navFooterDescText">Rare Books<br/> & Textbooks</span></a></td>
<td cla'ss="navFooterDescSpacer" style="width: 4%"></td>\n<td class="navFooterDescItem"><a href="http://www.afterschool.com/" class="nav_a">AfterSchool.com<br/> <span class="navFooterDescText">Kids\x92 Sports, Outdoor<br/> & Dance Gear</span></a></td>\n<td class="navFo'oterDescSpacer" style="width: 4%"></td>
<td class="navFooterDescItem"><a href="http://fresh.amazon.com" class="nav_a">AmazonFresh<br/> <span class="navFooterDescText">Groceries & More<br/> Right To Your Door</span></a></td>
<td class="navFooterDescSpacer" style="width: 4%"></td>
<td class="navFooterDescItem"><a href="http://amazonlocal.com/" class="nav_a">AmazonLocal<br/> <span class="navFooterDescText">Great Local Deals<br/> in Your City</span></a></td>
<td class="navFooterDescSpacer" style="width: 4%"></td>
<td class="navFooterDescItem"><a href="http://www.amazonsupply.com/" class="nav_a">AmazonSupply<br/> <span class="navFooterDescText">Business, Industrial<br/> & Scientific Supplies</span></a></td>
<td class="navFooterDescSpacer" style="width: 4%"></td>
<td class="navFooterDescItem"><a href="http://aws.amazon.com/" class="nav_a">AmazonWebServices<br/> <span class="navFooterDescText">Scalable<br/> Cloud Services</span></a></td>
<td class="navFooterDescSpacer" style="width: 4%"></td>
<td class="navFooterDescItem"><a href="http://askville.amazon.com/" class="nav_a">Askville<br/> <span class="navFooterDescText">Community<br/> Answers</span></a></td>
<td class="navFooterDescSpacer" style="width: 36.0%"></td>
</tr>
<tr><td>&nbsp;</td></tr>
<tr>
<td class="navFooterDescSpacer" style="width: 36.0%"></td>
<td class="navFooterDescItem"><a href="http://www.audible.com/" class="nav_a">Audible<br/> <span class="navFooterDescText">Download<br/> Audio Books</span></a></td>
<td class="navFooterDescSpacer" style="width: 4%"></td>
<td class="navFooterDescItem"><a href="http://www.beautybar.com/" class="nav_a">BeautyBar.com<br/> <span class="navFooterDescText">Prestige Beauty<br/> Delivered</span></a></td>
<td class="navFooterDescSpacer" style="width: 4%"></td>
<td class="navFooterDescItem"><a href="http://www.bookdepository.com/" class="nav_a">Book Depository<br/> <span class="navFooterDescText">Books With Free<br/> Delivery Worldwide</span></a></td>
<td class="navFooterDescSpacer" style="width: 4%"></td>
<td class="navFooterDescItem"><a href="http://www.bookworm.com" class="nav_a">Bookworm.com<br/> <span class="navFooterDescText">Books For Children<br/> Of All Ages</span></a></td>
<td class="navFooterDescSpacer" style="width: 4%"></td>
<td class="navFooterDescItem"><a href="http://www.casa.com/" class="nav_a">Casa.com<br/> <span class="navFooterDescText">Kitchen, Storage<br/> & Everything Home</span></a></td>
<td class="navFooterDescSpacer" style="width: 4%"></td>
<td class="navFooterDescItem"><a href="http://www.createspace.com/" class="nav_a">CreateSpace<br/> <span class="navFooterDescText">Indie Print Publishing<br/> Made Easy</span></a></td>
<td class="navFooterDescSpacer" style="width: 4%"></td>
<td class="navFooterDescItem"><a href="http://www.diapers.com/" class="nav_a">Diapers.com<br/> <span class="navFooterDescText">Everything<br/> But The Baby</span></a></td>
<td class="navFooterDescSpacer" style="width: 4%"></td>
<td class="navFooterDescItem"><a href="http://www.dpreview.com/" class="nav_a">DPReview<br/> <span class="navFooterDescText">Digital<br/> Photography</span></a></td>
<td class="navFooterDescSpacer" style="width: 36.0%"></td>
</tr>
<tr><td>&nbsp;</td></tr>
<tr>
<td class="navFooterDescSpacer" style="width: 36.0%"></td>
<td class="navFooterDescItem"><a href="http://www.fabric.com/" class="nav_a">Fabric<br/> <span class="navFooterDescText">Sewing, Quilting<br/> & Knitting</span></a></td>
<td class="navFooterDescSpacer" style="width: 4%"></td>
<td class="navFooterDescItem"><a href="http://www.imdb.com/" class="nav_a">IMDb<br/> <span class="navFooterDescText">Movies, TV<br/> & Celebrities</span></a></td>
<td class="navFooterDescSpacer" style="width: 4%"></td>
<td class="navFooterDescItem"><a href="http://www.junglee.com/" class="nav_a">Junglee.com<br/> <span class="navFooterDescText">Shop Online<br/> in India</span></a></td>
<td class="navFooterDescSpacer" style="width: 4%"></td>
<td class="navFooterDescItem"><a href="http://kdp.amazon.com/" class="nav_a">Kindle Direct Publishing<br/> <span class="navFooterDescText">Indie Digital Publishing<br/> Made Easy
</span></a></td>
<td class="navFooterDescSpacer" style="width: 4%"></td>
<td class="navFooterDescItem"><a href="http://www.look.com/" class="nav_a">Look.com<br/> <span class="navFooterDescText">Kids' Clothing<br/> & Shoes</span></a></td>
<td class="navFooterDescSpacer" style="width: 4%"></td>
<td class="navFooterDescItem"><a href="http://www.myhabit.com/" class="nav_a">MYHABIT<br/> <span class="navFooterDescText">Private Fashion<br/> Designer Sales</span></a></td>
<td class="navFooterDescSpacer" style="width: 4%"></td>
<td class="navFooterDescItem"><a href="http://www.shopbop.com/welcome" class="nav_a">Shopbop<br/> <span class="navFooterDescText">Designer<br/> Fashion Brands</span></a></td>
<td class="navFooterDescSpacer" style="width: 4%"></td>
<td class="navFooterDescItem"><a href="http://www.soap.com/" class="nav_a">Soap.com<br/> <span class="navFooterDescText">Health, Beauty &<br/> Home Essentials</span></a></td>
<td class="navFooterDescSpacer" style="width: 36.0%"></td>
</tr>
<tr><td>&nbsp;</td></tr>
<tr>
<td class="navFooterDescSpacer" style="width: 36.0%"></td>
<td class="navFooterDescItem">&nbsp;</td>
<td class="navFooterDescSpacer" style="width: 4%"></td>
<td class="navFooterDescItem"><a href="http://www.vine.com/" class="nav_a">Vine.com<br/> <span class="navFooterDescText">Everything<br/> to Live Life Green</span></a></td>
<td class="navFooterDescSpacer" style="width: 4%"></td>
<td class="navFooterDescItem"><a href="http://www.wag.com/" class="nav_a">Wag.com<br/> <span class="navFooterDescText">Everything<br/> For Your Pet</span></a></td>
<td class="navFooterDescSpacer" style="width: 4%"></td>
<td class="navFooterDescItem"><a href="/b?ie=UTF8&amp;node=1267877011" class="nav_a">Warehouse Deals<br/> <span class="navFooterDescText">Open-Box<br/> Discounts</span></a></td>
<td class="navFooterDescSpacer" style="width: 4%"></td>
<td class="navFooterDescItem"><a href="http://www.woot.com/" class="nav_a">Woot<br/> <span class="navFooterDescText">Never Gonna<br/> Give You Up</span></a></td>
<td class="navFooterDescSpacer" style="width: 4%"></td>
<td class="navFooterDescItem"><a href="http://www.yoyo.com/" class="nav_a">Yoyo.com<br/> <span class="navFooterDescText">A Happy Place<br/> To Shop For Toys</span></a></td>
<td class="navFooterDescSpacer" style="width: 4%"></td>
<td class="navFooterDescItem"><a href="http://www.zappos.com/c/top-searches" class="nav_a">Zappos<br/> <span class="navFooterDescText">Shoes &<br/> Clothing</span></a></td>
<td class="navFooterDescSpacer" style="width: 4%"></td>
<td class="navFooterDescItem">&nbsp;</td>
<td class="navFooterDescSpacer" style="width: 36.0%"></td>
</tr>
</table></div>
<div class="navFooterLine navFooterLinkLine navFooterPadItemLine"><ul><li class=
"nav_first"><a href="/gp/help/customer/display.html?ie=UTF8&amp;nodeId=508088" c
lass="nav_a">Conditions of Use</a></li><li><a href="/gp/help/customer/display.ht
ml?ie=UTF8&amp;nodeId=468496" class="nav_a">Privacy Notice</a></li><li><a href="
/interestbasedads" class="nav_a">Interest-Based Ads'</a></li><li class="nav_last
">\xa9 1996-2013, Amazon.com, Inc. or its affiliates</li></ul></div>\n</div>\n<!
-- whfh-+qOiT9YjikZ95F2rTpcta0N10QwcEqW/qVjKObrNUNCf3Y1dmpEDRvH9ZODumvLE rid-0NS
Y087S35KR62AD2HD9 -->\n\n\n\n\n\n\n\n\n\n\n<div id="sis_pixel_r2"></div><script>
(fun'ction(a,b){a.attachEvent?a.attachEvent("onload",b):a.addEventListener&&a.ad
dEventListener("load",b,!1)})(window,function(){setTimeout(function(){var el=doc
ument.getElementById("sis_pixel_r2");el&&(el.innerHTML='<iframe id="DAsis" src="
//s.amazon-adsystem.com/iu3?d=amazon.com&slot=navFooter&a2=0101a1823ca3d5d46ce03
d4502edf28f095b20f780c29eddcddebefb2933fa9c1e98&old_oo=0&cb=1373278234456" width
="1" height="1" frameborder="0" marginwidth="0" marginheight="0" scrolling="no">
</iframe>')},300)});</script>









<!--AMZNJQFINAL-->


</body>
</html> '''


data = etree.HTML(d)

r = data.xpath("//nobr/text()")
#r=data.xpath("//td[1]/div[5]/text()")
print r








