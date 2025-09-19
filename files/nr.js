import Fuse from 'https://cdn.jsdelivr.net/npm/fuse.js@7.1.0/dist/fuse.mjs';

var searchData = [];
var searchDataByKey = {};

function hideAfterDeadline() {
    var now = new Date();
    var elements = document.getElementsByClassName("hideAfterDeadline");
    for (var i = 0; i < elements.length; i++) {
        var deadline = new Date(elements[i].getAttribute("data-deadline"));
        if(now > deadline) {
            elements[i].style.display = "none";
        }
    }
}

async function loadSearchData() {
    await fetch('./search_data.json')
        .then((response) => response.json())
        .then((json) => {
            for(var key in json) {
                const item = json[key];
                item.id = key;
                searchData.push(item);
                searchDataByKey[key] = item;
            }
        });
}

function hideOrUnhideSearching(someHidden) {
    if(someHidden) {
        document.querySelectorAll('.hide-if-searching').forEach((el) => {
            el.style.display = 'none';
        });
    } else {
        document.querySelectorAll('.hide-if-searching').forEach((el) => {
            el.style.display = '';
        });
    }
}

function updatePublicationSearch(event) {
    const keywords = document.getElementById('publicationSearchKeywords').value.trim();
    const show_conf = document.getElementById('showConferencePapers').checked;
    const show_theses = document.getElementById('showTheses').checked;
    const show_only_pr = document.getElementById('showOnlyPR').checked;
    // first build a set of li elements that should be hidden based on the checkboxes
    document.querySelectorAll('li').forEach((li) => {
        if(li.id.startsWith('pub_')) {
            const thingId = li.id.substring(4);
            const thing = searchDataByKey[thingId];
            var showIt = true;
            if((!show_conf) && thing.conference) {
                showIt = false;
            }
            if((!show_theses) && thing.phd_thesis) {
                showIt = false;
            }
            if((show_only_pr) && (("peer_reviewed" in thing && thing.peer_reviewed==false) || thing.year=='Preprints')) {
                showIt = false;
            }
            if(showIt) {
                li.style.display = '';
            } else {
                li.style.display = 'none';
            }
        }
    });
    // then apply the text search on top of that
    if(keywords.length>0) {
        const options = {
            includeScore: true,
            threshold: 0.3, // empirically determined, smaller is more strict
            keys: ['abstract', 'title', 'authors', 'year', 'journal', 'doi'] // use these fields to search in
        }
        const fuse = new Fuse(searchData, options);
        const searchResults = fuse.search(keywords);
        var someHidden = false;
        document.querySelectorAll('li').forEach((li) => {
            if(li.id.startsWith('pub_')) {
                const thingId = li.id.substring(4);
                if(!searchResults.some(result => result.item.id === thingId)) {
                    someHidden = true;
                    li.style.display = 'none';
                }
            }
        });
        hideOrUnhideSearching(someHidden);
    } else {
        hideOrUnhideSearching(false);
    }
}

export async function thingsToDoOnLoad() {
    hideAfterDeadline();
    await loadSearchData();
    const publicationSearchKeywordsElement = document.getElementById('publicationSearchKeywords');
    if(publicationSearchKeywordsElement) {
        publicationSearchKeywordsElement.addEventListener('input', updatePublicationSearch);
        document.getElementById('showConferencePapers').addEventListener('change', updatePublicationSearch);
        document.getElementById('showTheses').addEventListener('change', updatePublicationSearch);
        document.getElementById('showOnlyPR').addEventListener('change', updatePublicationSearch);
        updatePublicationSearch(null);
    }
}