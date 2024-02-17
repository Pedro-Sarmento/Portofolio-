package models;

import java.util.*;


public class Project {
    private final String id;
    private final String date;
    private final String name;
    private final Map<String, String> usersInProject = new HashMap<>();
    private final Map<String, ProjectBookmark> bookmarks = new HashMap<>();
    private final Map<String, Directory> family = new HashMap<>();


    public Project(String projectID, String date, String projectName) {
        this.id = projectID;
        this.date = date;
        this.name = projectName;
    }

    public String getID() {
        return this.id;
    }

    public Collection<Directory> getFamily() {
        return family.values();
    }

    public void addMember(String participatingUserId, String participantType) {
        usersInProject.put(participatingUserId, participantType);
    }


    public boolean hasPermissions(String userId) {
        return usersInProject.get(userId).equals("Gestor");
    }

    public void addDirectory(String directoryPath) {
        final var directoryNameList = directoryPath.split(" > ");
        if(directoryNameList.length == 1){
            family.put(directoryNameList[0], new Directory(directoryNameList[0]));
        }
        else{
            getDirectoryParent(directoryNameList).addDirectory(directoryNameList[directoryNameList.length - 1]);
        }
    }

    private Directory getDirectory(String[] directoryNameList) {
        Directory directory = null;
        var directories = family;
        for (var dirName : directoryNameList) {
            directory = directories.get(dirName);
            directories = directory.getDirectories();
        }
        return directory;
    }

    public boolean hasDirectory(String[] directoryNameList) {
        try {
            getDirectory(directoryNameList);
        } catch (NullPointerException e) {
            return false;
        }
        return true;
    }

    private Directory getDirectoryParent(String[] directoryNameList) {
        return getDirectory(Arrays.copyOfRange(directoryNameList, 0, directoryNameList.length - 1));
    }

    public void removeDirectory(String directoryPath) {
        final var directoryNameList = directoryPath.split(" > ");
        if(directoryNameList.length == 1){
            family.remove(directoryNameList[0]);
        }
        else{
            getDirectoryParent(directoryNameList).removeBookmark(directoryNameList[directoryNameList.length - 1]);
        }
    }

    public void addBookmark(User participatingUser, User userBookmark, Bookmark bookmark, String directoryLine) {
        if (!directoryLine.equals("")) {
            var finalDirectoryList = directoryLine.split(" > ");
            var directory = getDirectory(finalDirectoryList);
            directory.addBookmark(bookmark.getName(), participatingUser, userBookmark, bookmark);
        } else {
            bookmarks.put(bookmark.getName(), new ProjectBookmark(participatingUser, userBookmark, bookmark));
        }
    }


    public boolean hasBookmark(String bookmarkName) {
        return bookmarks.containsKey(bookmarkName);
    }

    public void removeBookmark(String participatingUserId, String userBookmarkID, String bookmarkName) {
        if (bookmarks.containsKey(bookmarkName)) {
            bookmarks.remove(bookmarkName);
        } else {
            for (Directory directory : family.values()) {
                if (directory.hasBookmark(bookmarkName)) {
                    directory.removeBookmark(bookmarkName);
                } else {
                    directory.checkNextDirectory(bookmarkName);
                }
            }
        }
    }

    public boolean checkHierarchy(String directoryName) {
        var path = directoryName.split(" > ");
        var parentPath = Arrays.copyOfRange(path, 0 , path.length-1);
        if(parentPath.length == 0)
            return true;
        return hasDirectory(parentPath);
    }

    public String getName() {
        return this.name;
    }

    public boolean isBookmarksEmpty() {
        return bookmarks.isEmpty();
    }

    public ArrayList<ProjectBookmark> getBookmarks() {
        return new ArrayList<>(bookmarks.values());
    }

    public ArrayList<ProjectBookmark> getSortedBookmarks() {
        var bookmarks = getBookmarks();
        Comparator<ProjectBookmark> compareByName = Comparator.comparing(ProjectBookmark::getBookmarkName);
        bookmarks.sort(compareByName);
        return bookmarks;
    }

    public Collection<ProjectBookmark> getBookmarksByDate() {
        var bookmarksByDate = getSortedBookmarks();
        Comparator<ProjectBookmark> compareByDate = Comparator.comparing(ProjectBookmark::getBookmarkDate);
        Collections.sort(bookmarksByDate, compareByDate);
        return bookmarksByDate;
    }
}
