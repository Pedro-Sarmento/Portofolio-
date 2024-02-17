package models;
import java.util.*;

public class Session {
    private final String name;
    private final String date;
    private final Map<String, Bookmark> bookmarks = new HashMap<>();
    public Session(String date, String sessionName) {
        this.date = date;
        this.name = sessionName;
    }

    public void addBookmark(String bookmarkName, Bookmark bookmark) {
        bookmarks.put(bookmarkName, bookmark);
    }

    public boolean hasBookmark(String bookmarkName) {
        return bookmarks.containsKey(bookmarkName);
    }

    public void removeBookmark(String bookmarkName) {
        bookmarks.remove(bookmarkName);
    }

    public String getDate() {
        return this.date;
    }

    public ArrayList<Bookmark> getBookmarksUnsorted() {
        return new ArrayList<>(bookmarks.values());
    }

    private ArrayList<Bookmark> getBookmarksByTpye() {
        var bookmarksByType = getBookmarksUnsorted();
        Comparator<Bookmark> compareByType = Comparator.comparing(Bookmark::getType);
        bookmarksByType.sort(compareByType);
        return bookmarksByType;
    }

    public ArrayList<Bookmark> getBookmarksByName() {
        var bookmarksByName = getBookmarksByTpye();
        Comparator<Bookmark> compareByName = Comparator.comparing(Bookmark::getName);
        bookmarksByName.sort(compareByName);
        return bookmarksByName;
    }

    public ArrayList<Bookmark> getSortedBookmarks(){
        var finalBookmarkList = getBookmarksByName();
        Comparator<Bookmark> compareByID = Comparator.comparing(Bookmark::getCreatorID);
        finalBookmarkList.sort(compareByID);
        return  finalBookmarkList;
    }

    public String getName() {
        return this.name;
    }
}
