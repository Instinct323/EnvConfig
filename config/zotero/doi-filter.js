const TAG_QUEUE = "🍋 Queue";
const TAG_NO_DOI = "🥥 No DOI found";


function notify(msg, duration = 3000) {
    const pop = new Zotero.ProgressWindow();
    pop.changeHeadline("Info");
    pop.addDescription(msg);
    pop.show();
    pop.startCloseTimer(duration);
}


async function filterItemsWithoutDoi() {
    const items = Zotero.getActiveZoteroPane().getSelectedItems();

    for (const item of items) {
        item.addTag(TAG_QUEUE);
        await item.saveTx();
    }

    for (const item of items) {
        const doi = item.getField("DOI");

        if (!doi) {
            item.addTag(TAG_NO_DOI);
        }

        item.removeTag(TAG_QUEUE);
        await item.saveTx();
    }

    notify(`Processed ${items.length} items`);
}


await filterItemsWithoutDoi();
