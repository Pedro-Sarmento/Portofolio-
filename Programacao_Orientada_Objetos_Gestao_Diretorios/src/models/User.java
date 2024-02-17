package models;
import java.util.Collection;
import java.util.HashMap;
import java.util.Map;

public class User {
    private final String id;
    private final String name;
    public Map<String, Bookmark> bookmarks = new HashMap<>();
    private final Map<String, Project> projects = new HashMap<>();
    private final Map<String, Session> sessions = new HashMap<>();
    private long projectIdGenerator = 1;

    public User(String userName, String userID) {
        this.name = userName;
        this.id = userID;
    }
    public String getID() {return this.id;}

    public String getName() {
        return this.name;
    }

    public Collection<Bookmark> getBookmarks() {
        return bookmarks.values();
    }

    public void addBookmark(Bookmark bookmark) { bookmarks.put(bookmark.getName(), bookmark);
    }

    public Project getProject(String projectID){ return projects.get(projectID);}

    public String getBookmarkType(String bookMarkName) {
        return bookmarks.get(bookMarkName).getType();
    }

    public String createNewProject(String date, String projectName) {
        var project = new  Project(Long.toString(projectIdGenerator++), date, projectName);
        projects.put(project.getID(), project);
        return  project.getID();
    }

    public boolean hasProject(String projectID) {
        return projects.containsKey(projectID);
    }

    public void createNewSession(String date, String sessionName) {
        var session = new Session(date, sessionName);
        sessions.put(sessionName, session);
    }

    public int getIdAsInt(){
        String idStr = this.id;
        int number = Integer.parseInt(idStr);
        return number;
    }

    public boolean hasSession(String sessionName) {
        return sessions.containsKey(sessionName);
    }

    public Session getSession(String sessionName) {
        return sessions.get(sessionName);
    }

    public Bookmark getBookmark(String bookmarkName) {
        return bookmarks.get(bookmarkName);
    }
}