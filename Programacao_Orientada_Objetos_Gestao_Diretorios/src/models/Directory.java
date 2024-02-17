package models;
import java.util.*;

public class Directory {
    private final String name;
    private final Map<String, DirectoryBookmark> bookmarks = new HashMap<>();
    private final Map<String, Directory> directories = new HashMap<>();
    public Directory(String name) {
        this.name = name;
    }

    public String getName() {
        return this.name;
    }

    public void addBookmark(String bookmarkName, User addingUser, User creator, Bookmark bookmark) {
        bookmarks.put(bookmarkName,new DirectoryBookmark(addingUser, creator, bookmark));
    }

    public boolean hasBookmark(String bookmarkName) {
        return bookmarks.containsKey(bookmarkName);
    }

    public void removeBookmark(String bookmarkName) {
        bookmarks.remove(bookmarkName);
    }

    public void addDirectory(String directoryName) {
        this.directories.put(directoryName, new Directory(directoryName));
    }

    public void printBookmarksAndPath(String path){
        path += getName();
        if(!bookmarks.isEmpty()){
            for(DirectoryBookmark bookmark : getBookmarksByDate()){
                System.out.println(path + " : " + bookmark.getBookmark().getName() + " " + bookmark.getCreator().getID() + " " + bookmark.getAddingUser().getID() + " [" + bookmark.getBookmark().getURL() + "]");
            }
        }
        for(Directory directory : getDirectoryCollection()){
            path += " > ";
            directory.printBookmarksAndPath(path);
        }
        }

    private Collection<Directory> getDirectoryCollection() {
        return directories.values();
    }


    public Map<String, Directory> getDirectories() {
        return directories;
    }

    public void checkNextDirectory(String bookmarkName) {
        for (Directory directory: directories.values()) {
            if (directory.hasBookmark(bookmarkName)) {
                directory.removeBookmark(bookmarkName);
            }
            else{
                directory.checkNextDirectory(bookmarkName);
            }
        }
    }

    public ArrayList<DirectoryBookmark> getBookmarks() {
        return new ArrayList<>(bookmarks.values());
    }

    public ArrayList<DirectoryBookmark> getSortedBookmarks() {
        var bookmarks = getBookmarks();
        Comparator<DirectoryBookmark> compareByName = Comparator.comparing(DirectoryBookmark::getBookmarkName);
        bookmarks.sort(compareByName);
        return bookmarks;
    }

    private Collection<DirectoryBookmark> getBookmarksByDate() {
        var bookmarksByDate = getSortedBookmarks();
        Comparator<DirectoryBookmark> compareByDate = Comparator.comparing(DirectoryBookmark::getBookmarkDate);
        bookmarksByDate.sort(compareByDate);
        return bookmarksByDate;
    }

}
