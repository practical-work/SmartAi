function openImage(src){
    document.getElementById("imageModal").style.display="flex";
    document.getElementById("popupImage").src=src;
}

function closeImage(){
    document.getElementById("imageModal").style.display="none";
}
