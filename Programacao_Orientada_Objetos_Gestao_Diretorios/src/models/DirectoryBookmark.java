package models;

public class DirectoryBookmark {
    private User addingUser;
    private User creatorUser;
    private Bookmark bookmark;

    public DirectoryBookmark(User addingUser, User creator, Bookmark bookmark) {
        this.addingUser = addingUser;
        this.creatorUser = creator;
        this.bookmark = bookmark;
    }

    public String getBookmarkName(){ return this.bookmark.getName();}

    public String getBookmarkDate(){ return this.bookmark.getData();}

    public User getAddingUser() {
        return addingUser;
    }

    public User getCreator() {
        return creatorUser;
    }

    public Bookmark getBookmark() {
        return bookmark;
    }
}
