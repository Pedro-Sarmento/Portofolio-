package controllers;
import models.Bookmark;
import models.Project;
import models.Session;
import models.User;

import java.io.*;
import java.time.LocalDate;
import java.time.format.DateTimeFormatter;
import java.time.format.DateTimeParseException;
import java.util.*;

public class BookmarkManagement implements Serializable {
    public Map<String, User> users = new HashMap<>();
    private long useridGenerator = 1;

    public String registerUser(String userName) {
        String userID = Long.toString(useridGenerator++);
        final var user = new User(userName, userID);
        users.put(userID, user);
        return userID;}

    public Collection<User> getUsers(){
        return users.values();
    }

    public boolean hasUsers() {
        return users.isEmpty();
    }

    public boolean hasUserID(String userID) {
        return !users.containsKey(userID);
    }

    public boolean hasBookmarkName(String bookmarkName, String userID) {
        return users.get(userID).bookmarks.containsKey(bookmarkName);}

    public boolean checkDate(String date) {
        try{
            LocalDate.parse(date, DateTimeFormatter.BASIC_ISO_DATE);
            return true;}
        catch(DateTimeParseException ex) {return false;}}

    public boolean checkBookmarkType(String bookmarkType) {
        return bookmarkType.equals("Pessoal") || bookmarkType.equals("Trabalho") || bookmarkType.equals("Outro");
    }

    public void registerBookmark(String userID, String date, String bookmarkType, String bookmarkName, String url) {
        final var bookmark = new Bookmark(date, bookmarkType, bookmarkName, url, userID);
        users.get(userID).addBookmark(bookmark);}

    public boolean checkBookmarkPermissions(String userID, String bookmarkName, String bookmarkType) {
        return !users.get(userID).getBookmark(bookmarkName).getType().equals(bookmarkType);}

    public void shareBookmark(String userID, String shareUserId, String bookmarkName) {
        users.get(shareUserId).addBookmark(users.get(userID).bookmarks.get(bookmarkName));}

    public String createProject(String userID, String date, String projectName) {
        return users.get(userID).createNewProject(date, projectName);}


    public boolean hasProjectID(String projectID, String userID) {
        return users.get(userID).hasProject(projectID);
    }

    public void addMemberToProject(String userID, String projectID, String participatingUserId, String participantType) {
        users.get(userID).getProject(projectID).addMember(participatingUserId, participantType);
    }

    public void addBookmarkProject(String userID, String projectID, String participatingUserId, String userBookmarkID, String bookmarkName, String directoryLine) {
        users.get(userID).getProject(projectID).addBookmark(users.get(participatingUserId), users.get(userBookmarkID), users.get(userBookmarkID).getBookmark(bookmarkName), directoryLine);
    }

    public boolean checkBookmarkProjectAssociation(String userID, String projectID, String bookmarkName) {
        return users.get(userID).getProject(projectID).hasBookmark(bookmarkName);
    }

    public void removeBookmarkProject(String userID, String projectID, String participatingUserId, String userBookmarkID, String bookmarkName) {
        users.get(userID).getProject(projectID).removeBookmark(participatingUserId, userBookmarkID, bookmarkName);
    }

    public void addDirectoryToProject(String userID, String projectID, String participatingUserId, String directoryName) {
        users.get(userID).getProject(projectID).addDirectory(directoryName);
    }

    public void removeDirectoryProject(String userID, String projectID, String participatingUserId, String directoryName) {
        users.get(userID).getProject(projectID).removeDirectory(directoryName);
    }


    public boolean checkUserPermission(String userID, String projectID, String participatingUserId) {
        return users.get(userID).getProject(projectID).hasPermissions(participatingUserId);}

    public boolean hasDirectoryInProject(String userID, String projectID, String directoryName) {
        var directoryNameList = directoryName.split(" > ");
        return users.get(userID).getProject(projectID).hasDirectory(directoryNameList);
    }

    public boolean checkDirectoryHierarchy(String userID, String projectID, String directoryName) {
        return users.get(userID).getProject(projectID).checkHierarchy(directoryName);}

    public boolean hasSessionName(String userID, String sessionName) {
        return users.get(userID).hasSession(sessionName);}

    public void createSession(String userID, String date, String sessionName) {
        users.get(userID).createNewSession(date, sessionName);}

    public void addBookmarkSession(String userID, String sessionName, String userBookmarkID, String bookmarkName) {
        var bookmark = users.get(userID).getBookmark(bookmarkName);
        users.get(userID).getSession(sessionName).addBookmark(bookmarkName, bookmark);
    }

    public boolean checkBookmarkInSession(String userID, String sessionName, String bookmarkName) {
        return users.get(userID).getSession(sessionName).hasBookmark(bookmarkName);}

    public void removeBookmarkSession(String userID, String sessionName, String bookmarkName) {
        users.get(userID).getSession(sessionName).removeBookmark(bookmarkName);
    }

    public Session getUserSession(String userID, String sessionName) {
        return users.get(userID).getSession(sessionName);
    }

    public void save(String filename) {
        try {
            final var fileOutputStream = new FileOutputStream(filename);
            final var objectOutputStream = new ObjectOutputStream(fileOutputStream);
            objectOutputStream.writeObject(this);
            objectOutputStream.close();
        } catch(FileNotFoundException fnfe) {
            System.out.println("Ficheiro inexistente.");
        } catch(IOException ioe) {
            System.out.println("Erro na gravação de objetos.");
        }
    }

    public static BookmarkManagement load(String filename) throws FileNotFoundException {
        FileInputStream fileInputStream;
        fileInputStream = new FileInputStream(filename);
        ObjectInputStream objectInputStream = null;
        try {
            objectInputStream = new ObjectInputStream(fileInputStream);
        } catch(IOException e) {
            e.printStackTrace();
        }
        Object obj = null;
        try {
            obj = objectInputStream.readObject();
        } catch(IOException | ClassNotFoundException e) {
            e.printStackTrace();
        }
        return (BookmarkManagement) obj;
    }

    public Collection<User> sortedUsersID(){
        ArrayList<User> userArray = new ArrayList<>();
        userArray.addAll(users.values());
        Comparator<User> compareById = Comparator.comparing(User::getIdAsInt);
        userArray.sort(compareById);
        return userArray;
    }
    public Project getUserProject(String userID, String projectID) {
        return users.get(userID).getProject(projectID);
    }

}
