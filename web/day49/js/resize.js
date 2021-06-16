/*获得页面宽度后动态修改html上的fontsize
* 320为iphone5设计稿下的页面宽度，如下设置后页面的页面在iphone5等宽屏幕上html
* 的font-size会变为100px，即 1rem = 100px    1px=0.01rem
* 所以设置元素尺寸的时候，如果测量设计稿 15px  则需设置尺寸为 (0.01*15)rem = 0.15rem   
*/

!(function (doc, win) {
    var docEle = doc.documentElement,
        evt = "onorientationchange" in window ? "orientationchange" : "resize",
        fn = function () {
            var width = docEle.clientWidth;
            console.log(width);
            width && (docEle.style.fontSize = 100 * (width / 375) + "px");
        };

    win.addEventListener(evt, fn, false);
    doc.addEventListener("DOMContentLoaded", fn, false);

}(document, window));