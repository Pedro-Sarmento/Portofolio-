package models;

public class Bookmark {
    private final String date;
    private final String type;
    private final String name;
    private final String url;
    private final String creatorID;

    public Bookmark(String date, String bookmarkType, String bookmarkName, String url, String CreatorID) {
        this.creatorID = CreatorID;
        this.date = date;
        this.type = bookmarkType;
        this.name = bookmarkName;
        this.url = url;
    }
    public String getCreatorID(){return this.creatorID;}
    public String getName() {return this.name;}
    public String getData() {return this.date;}
    public String getURL() {return this.url;}
    public String getType() {return this.type;}
}
