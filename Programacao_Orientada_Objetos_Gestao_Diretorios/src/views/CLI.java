package views;

import controllers.BookmarkManagement;
import models.*;
import java.io.FileNotFoundException;
import java.util.Arrays;
import java.util.Scanner;
import java.util.Collection;

public class CLI {
    public CLI() {
        BookmarkManagement bookmarkManagement = new BookmarkManagement();
        final var scanner = new Scanner(System.in);
        while(true) {
            final var line = scanner.nextLine();
            if(line.isBlank()) {
                break;
            }
            final var commands = line.split(" ");

            switch (commands[0]) {
                case "UR":
                    var userName = "";

                    if (commands.length != 2) for (int i = 2; i < commands.length; i++) {
                        commands[1] += " " + commands[i];
                    }
                    userName = commands[1];
                    String userID = bookmarkManagement.registerUser(userName);
                    System.out.println("Utilizador registado com identificador " + userID + ".");
                    break;
                case "UL":
                    if(bookmarkManagement.hasUsers()) {
                        System.out.println("Sem utilizadores registados.");

                        } else {
                            Collection<User> users = bookmarkManagement.sortedUsersID();

                            for(final var user : users) {
                                System.out.println(user.getID()+ " " + user.getName());
                            }
                        }
                    break;
                case "BR":
                    userID = commands[1];
                    var date = commands[2];
                    var bookmarkType = commands[3];
                    var bookmarkName = scanner.nextLine();
                    var url = scanner.nextLine();
                    if(bookmarkManagement.hasUserID(userID)) {
                        System.out.println("Utilizador inexistente.");
                    }

                    else if(bookmarkManagement.hasBookmarkName(bookmarkName, userID)) {
                        System.out.println("Bookmark existente.");
                    }

                    else if(!bookmarkManagement.checkDate(date)) {
                        System.out.println("Data inválida.");
                    }
                    else if(!bookmarkManagement.checkBookmarkType(bookmarkType)) {
                        System.out.println("Tipo inválido.");
                    }
                    else {
                        bookmarkManagement.registerBookmark(userID, date, bookmarkType, bookmarkName, url);
                        System.out.println("Bookmark registado com sucesso.");

                    }
                    break;

                case "BP":
                    userID = commands[1];
                    var shareUserId = commands[2];
                    bookmarkName = scanner.nextLine();
                    if(bookmarkManagement.hasUserID(userID) || bookmarkManagement.hasUserID(shareUserId)) {
                        System.out.println("Utilizador inexistente.");
                    }

                    else if(!bookmarkManagement.hasBookmarkName(bookmarkName, userID)) {
                        System.out.println("Bookmark inexistente.");
                    }

                    else if(!bookmarkManagement.checkBookmarkPermissions(userID, bookmarkName, "Pessoal")) {
                        System.out.println("Sem permissões.");
                    }
                    else {
                        bookmarkManagement.shareBookmark(userID, shareUserId, bookmarkName);
                        System.out.println("Bookmark partilhado com sucesso.");
                    }
                    break;

                case "PR":
                    userID = commands[1];
                    date = commands[2];
                    var projectName = scanner.nextLine();
                    if(bookmarkManagement.hasUserID(userID)) {
                        System.out.println("Utilizador inexistente.");
                    }

                    else if(!bookmarkManagement.checkDate(date)) {
                        System.out.println("Data inválida.");
                    }

                    else {
                        var projectID = bookmarkManagement.createProject(userID, date, projectName);
                        bookmarkManagement.addMemberToProject(userID, projectID, userID, "Gestor");
                        System.out.println("Projeto registado com o identificador " + projectID + ".");
                    }
                    break;

                case "PAP":
                    userID = commands[1];
                    var projectID = commands[2];
                    var participatingUserId = commands[3];
                    var participantType = commands[4];
                    if(bookmarkManagement.hasUserID(userID) || bookmarkManagement.hasUserID(participatingUserId)) {
                        System.out.println("Utilizador inexistente.");
                    }

                    else if(!bookmarkManagement.hasProjectID(projectID, userID)) {
                        System.out.println("Projeto inexistente.");
                    }

                    else {
                        bookmarkManagement.addMemberToProject(userID, projectID, participatingUserId, participantType);
                        System.out.println("Utilizador adicionado a projeto com sucesso.");
                    }
                    break;

                case "PC":
                    userID = commands[1];
                    projectID = commands[2];
                    if(bookmarkManagement.hasUserID(userID)) {
                        System.out.println("Utilizador inexistente.");
                    }
                    else if(!bookmarkManagement.hasProjectID(projectID, userID)) {
                        System.out.println("Projeto inexistente.");
                    }
                    else{
                        var project = bookmarkManagement.getUserProject(userID, projectID);
                        System.out.println(project.getName());
                        if (!project.isBookmarksEmpty()){
                            for(ProjectBookmark bookmark : project.getBookmarksByDate()){
                                System.out.println(bookmark.getBookmark().getName() + " " + bookmark.getCreator().getID() + " " + bookmark.getAddingUser().getID() + " [" + bookmark.getBookmark().getURL() + "]");
                            }
                        }
                        for(Directory directory : project.getFamily()){
                            var path = "";
                            directory.printBookmarksAndPath(path);
                        }
                    }
                    break;
                case "PAB":
                    var bookmarkLine = scanner.nextLine();
                    var commandsBookmark = bookmarkLine.split(" ");
                    StringBuilder bookmarkNameCompleted = new StringBuilder();
                    for (int i = 1; i < commandsBookmark.length; i++) {
                        if (i == commandsBookmark.length - 1) {
                            bookmarkNameCompleted.append(commandsBookmark[i]);
                        }
                        else {
                            bookmarkNameCompleted.append(commandsBookmark[i]).append(" ");
                        }
                    }

                    final var directoryLine = scanner.nextLine();

                    userID = commands[1];
                    projectID = commands[2];
                    participatingUserId = commands[3];

                    var userBookmarkID = commandsBookmark[0];
                    bookmarkName = bookmarkNameCompleted.toString();



                    if(bookmarkManagement.hasUserID(userID)) {
                        System.out.println("Utilizador inexistente.");
                    }

                    else if(!bookmarkManagement.hasProjectID(projectID, userID)) {
                        System.out.println("Projeto inexistente.");
                    }

                    else if(!bookmarkManagement.hasBookmarkName(bookmarkName, userID)) {
                        System.out.println("Bookmark inexistente.");
                    }

                    else if(!bookmarkManagement.checkBookmarkPermissions(projectID, bookmarkName, "Pessoal")) {
                       System.out.println("Sem permissões.");
                    }

                    else {
                        bookmarkManagement.addBookmarkProject(userID, projectID, participatingUserId, userBookmarkID, bookmarkName, directoryLine);
                        System.out.println("Bookmark associado a projeto com sucesso.");
                    }
                    break;

                case "PRB":
                    userID = commands[1];
                    projectID = commands[2];
                    participatingUserId = commands[3];
                    userBookmarkID = scanner.nextLine();
                    bookmarkName = commands[1];

                    if(bookmarkManagement.hasUserID(userID)) {
                        System.out.println("Utilizador inexistente.");
                    }

                    else if(!bookmarkManagement.hasProjectID(projectID, userID)) {
                        System.out.println("Projeto inexistente.");
                    }

                    else if(!bookmarkManagement.checkBookmarkProjectAssociation(userID, projectID, bookmarkName)) {
                        System.out.println("Bookmark inexistente no projeto.");
                    }

                    else {
                        bookmarkManagement.removeBookmarkProject(userID, projectID, participatingUserId, userBookmarkID, bookmarkName);
                        System.out.println("Bookmark removido de projeto com sucesso.");
                    }
                    break;

                case "PAD":
                    userID = commands[1];
                    projectID = commands[2];
                    participatingUserId = commands[3];
                    var directoryName = scanner.nextLine();

                    if(bookmarkManagement.hasUserID(userID) || bookmarkManagement.hasUserID(participatingUserId)) {
                        System.out.println("Utilizador inexistente.");
                    }

                    else if(!bookmarkManagement.hasProjectID(projectID, userID)) {
                        System.out.println("Projeto inexistente.");
                    }

                    else if(!bookmarkManagement.checkUserPermission(userID, projectID, participatingUserId)) {
                        System.out.println("Sem permissões.");
                    }

                    else if(bookmarkManagement.hasDirectoryInProject(userID, projectID, directoryName)) {
                        System.out.println("Diretório existente no projeto.");
                    }

                    else if(!bookmarkManagement.checkDirectoryHierarchy(userID, projectID, directoryName)) {
                        System.out.println("Hierarquia de diretórios inválida.");
                    }

                    else {
                       bookmarkManagement.addDirectoryToProject(userID, projectID, participatingUserId, directoryName);
                       System.out.println("Diretório criado com sucesso.");
                    }

                    break;

                case "PRD":
                    userID = commands[1];
                    projectID = commands[2];
                    participatingUserId = commands[3];

                    directoryName = scanner.nextLine();
                    if(bookmarkManagement.hasUserID(userID)) {
                        System.out.println("Utilizador inexistente.");
                    }

                    else if(!bookmarkManagement.hasProjectID(projectID, userID)) {
                        System.out.println("Projeto inexistente.");
                    }

                    else if(!bookmarkManagement.checkUserPermission(userID, projectID, participatingUserId)) {
                        System.out.println("Sem permissões.");
                    }

                    else if(!bookmarkManagement.hasDirectoryInProject(userID, projectID, directoryName)) {
                        System.out.println("Diretório inexistente no projeto.");
                    }

                    else if(!bookmarkManagement.checkDirectoryHierarchy(userID,projectID, directoryName)) {
                        System.out.println("Hierarquia de diretórios inválida.");
                    }

                    else {
                        bookmarkManagement.removeDirectoryProject(userID, projectID, participatingUserId, directoryName);
                        System.out.println("Diretório removido com sucesso.");
                    }
                    break;

                case "SR":
                    userID = commands[1];
                    date = commands[2];
                    var sessionName = scanner.nextLine();
                    if(bookmarkManagement.hasUserID(userID)) {
                        System.out.println("Utilizador inexistente.");
                    }

                    else if(!bookmarkManagement.checkDate(date)) {
                        System.out.println("Data inválida.");
                    }

                    else if(bookmarkManagement.hasSessionName(userID, sessionName)) {
                        System.out.println("Sessão existente.");
                    }

                    else {
                        bookmarkManagement.createSession(userID, date, sessionName);
                        System.out.println("Sessão criada com sucesso.");
                    }
                    break;

                case "SC":
                    userID = commands[1];
                    sessionName = scanner.nextLine();
                    if(bookmarkManagement.hasUserID(userID)) {
                        System.out.println("Utilizador inexistente.");
                    }

                    else if(!bookmarkManagement.hasSessionName(userID, sessionName)) {
                        System.out.println("Sessão inexistente.");
                    }

                    else {
                        Session session = bookmarkManagement.getUserSession(userID, sessionName);
                        System.out.println(session.getDate());
                        for(final var bookmark : session.getSortedBookmarks()) {
                           System.out.println(bookmark.getName() + " [" + bookmark.getURL() + "]");
                        }

                    }
                    break;

                case "SAB":
                    sessionName = scanner.nextLine();
                    bookmarkLine = scanner.nextLine();
                    commandsBookmark = bookmarkLine.split(" ");
                    userID = commands[1];
                    StringBuilder bookmarkNameCompleted2 = new StringBuilder();
                    for (int i = 1; i < commandsBookmark.length; i++) {
                        if (i == commandsBookmark.length - 1) {
                            bookmarkNameCompleted2.append(commandsBookmark[i]);
                        }
                        else {
                            bookmarkNameCompleted2.append(commandsBookmark[i]).append(" ");
                        }
                    }
                    userBookmarkID = commandsBookmark[0];
                    bookmarkName = bookmarkNameCompleted2.toString();

                    if(bookmarkManagement.hasUserID(userID)) {
                        System.out.println("Utilizador inexistente.");
                    }

                    else if(!bookmarkManagement.hasSessionName(userID, sessionName)) {
                        System.out.println("Sessão inexistente.");
                    }

                    else if(!bookmarkManagement.hasBookmarkName(bookmarkName, userID)) {
                        System.out.println("Bookmark inexistente.");
                    }

                    else if(!bookmarkManagement.checkBookmarkPermissions(userID, bookmarkName, "Outro")) {
                        System.out.println("Sem permissões.");
                    }

                    else {
                        bookmarkManagement.addBookmarkSession(userID, sessionName, userBookmarkID, bookmarkName);
                        System.out.println("Bookmark associado a sessão com sucesso.");
                    }
                    break;

                case "SRB":
                    sessionName = scanner.nextLine();
                    bookmarkLine = scanner.nextLine();
                    commandsBookmark = bookmarkLine.split(" ");
                    userID = commands[1];
                    StringBuilder bookmarkNameCompleted3 = new StringBuilder();
                    for (int i = 1; i < commandsBookmark.length; i++) {
                        if (i == commandsBookmark.length - 1) {
                            bookmarkNameCompleted3.append(commandsBookmark[i]);
                        }
                        else {
                            bookmarkNameCompleted3.append(commandsBookmark[i]).append(" ");
                        }
                    }
                    bookmarkName = bookmarkNameCompleted3.toString();

                    if(bookmarkManagement.hasUserID(userID)) {
                        System.out.println("Utilizador inexistente.");
                    }

                    else if(!bookmarkManagement.hasSessionName(userID, sessionName)) {
                        System.out.println("Sessão inexistente.");
                    }

                    else if(!bookmarkManagement.checkBookmarkInSession(userID, sessionName, bookmarkName)) {
                        System.out.println("Bookmark inexistente na sessão.");
                    }

                    else {
                        bookmarkManagement.removeBookmarkSession(userID, sessionName, bookmarkName);
                        System.out.println("Bookmark removido de sessão com sucesso.");
                    }
                    break;

                case "G":
                    var filename = commands[1];
                    bookmarkManagement.save(filename);
                    System.out.println("Ficheiro gravado com sucesso.");
                    break;

                case "L":
                    filename = commands[2];

                    try {
                        bookmarkManagement = BookmarkManagement.load(filename);
                    } catch(FileNotFoundException e) {
                        System.out.println("Ficheiro inexistente.");
                    }

                    break;

                default:
                    System.out.println("Instrução inválida.");
            }
        }
    }
}