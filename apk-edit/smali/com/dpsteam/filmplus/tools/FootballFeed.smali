.class public final Lcom/dpsteam/filmplus/tools/FootballFeed;
.super Ljava/lang/Object;
.source "FootballFeed.java"

# interfaces
.implements Ljava/lang/Runnable;

# instance fields
.field private final fragment:Ly3/j;

# direct methods
.method public constructor <init>(Ly3/j;)V
    .locals 0

    invoke-direct {p0}, Ljava/lang/Object;-><init>()V
    iput-object p1, p0, Lcom/dpsteam/filmplus/tools/FootballFeed;->fragment:Ly3/j;
    return-void
.end method

.method private static readPage(Ljava/lang/String;)Ljava/lang/String;
    .locals 9

    :try_start_0
    new-instance v0, Ljava/net/URL;
    invoke-direct {v0, p0}, Ljava/net/URL;-><init>(Ljava/lang/String;)V
    invoke-virtual {v0}, Ljava/net/URL;->openConnection()Ljava/net/URLConnection;
    move-result-object v0
    check-cast v0, Ljava/net/HttpURLConnection;

    const/16 v1, 0x2ee0
    invoke-virtual {v0, v1}, Ljava/net/URLConnection;->setConnectTimeout(I)V
    const/16 v1, 0x3a98
    invoke-virtual {v0, v1}, Ljava/net/URLConnection;->setReadTimeout(I)V
    const-string v1, "User-Agent"
    const-string v2, "Mozilla/5.0 (Linux; Android 10) AppleWebKit/537.36 Chrome/120 Mobile Safari/537.36"
    invoke-virtual {v0, v1, v2}, Ljava/net/URLConnection;->setRequestProperty(Ljava/lang/String;Ljava/lang/String;)V
    const-string v1, "Referer"
    const-string v2, "https://ultrago-xi.vercel.app/"
    invoke-virtual {v0, v1, v2}, Ljava/net/URLConnection;->setRequestProperty(Ljava/lang/String;Ljava/lang/String;)V

    invoke-virtual {v0}, Ljava/net/URLConnection;->getInputStream()Ljava/io/InputStream;
    move-result-object v1
    new-instance v2, Ljava/io/BufferedReader;
    new-instance v3, Ljava/io/InputStreamReader;
    const-string v4, "UTF-8"
    invoke-direct {v3, v1, v4}, Ljava/io/InputStreamReader;-><init>(Ljava/io/InputStream;Ljava/lang/String;)V
    invoke-direct {v2, v3}, Ljava/io/BufferedReader;-><init>(Ljava/io/Reader;)V
    new-instance v3, Ljava/lang/StringBuilder;
    invoke-direct {v3}, Ljava/lang/StringBuilder;-><init>()V

    :read_loop
    invoke-virtual {v2}, Ljava/io/BufferedReader;->readLine()Ljava/lang/String;
    move-result-object v4
    if-eqz v4, :read_done
    invoke-virtual {v3, v4}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;
    const/16 v5, 0xa
    invoke-virtual {v3, v5}, Ljava/lang/StringBuilder;->append(C)Ljava/lang/StringBuilder;
    invoke-virtual {v3}, Ljava/lang/StringBuilder;->length()I
    move-result v5
    const v6, 0x5f5e100
    if-ge v5, v6, :read_done
    goto :read_loop

    :read_done
    invoke-virtual {v2}, Ljava/io/BufferedReader;->close()V
    invoke-virtual {v0}, Ljava/net/HttpURLConnection;->disconnect()V
    invoke-virtual {v3}, Ljava/lang/StringBuilder;->toString()Ljava/lang/String;
    move-result-object v0
    return-object v0
    :try_end_0
    .catch Ljava/lang/Throwable; {:try_start_0 .. :try_end_0} :catch_0

    :catch_0
    const/4 v0, 0x0
    return-object v0
.end method

.method private static resolveStream(Ljava/lang/String;I)Ljava/lang/String;
    .locals 8

    if-eqz p0, :resolve_none
    const/4 v0, 0x2
    if-ge p1, v0, :resolve_none

    invoke-static {p0}, Lcom/dpsteam/filmplus/tools/FootballFeed;->readPage(Ljava/lang/String;)Ljava/lang/String;
    move-result-object v0
    if-eqz v0, :resolve_none

    const-string v1, "https?://[^\"'\\s]+\\.m3u8[^\"'\\s]*"
    invoke-static {v1}, Ljava/util/regex/Pattern;->compile(Ljava/lang/String;)Ljava/util/regex/Pattern;
    move-result-object v1
    invoke-virtual {v1, v0}, Ljava/util/regex/Pattern;->matcher(Ljava/lang/CharSequence;)Ljava/util/regex/Matcher;
    move-result-object v1
    invoke-virtual {v1}, Ljava/util/regex/Matcher;->find()Z
    move-result v2
    if-eqz v2, :find_iframe
    const/4 v2, 0x0
    invoke-virtual {v1, v2}, Ljava/util/regex/Matcher;->group(I)Ljava/lang/String;
    move-result-object v1
    return-object v1

    :find_iframe
    const-string v1, "(?i)<iframe[^>]+src=[\"']([^\"']+)"
    invoke-static {v1}, Ljava/util/regex/Pattern;->compile(Ljava/lang/String;)Ljava/util/regex/Pattern;
    move-result-object v1
    invoke-virtual {v1, v0}, Ljava/util/regex/Pattern;->matcher(Ljava/lang/CharSequence;)Ljava/util/regex/Matcher;
    move-result-object v1
    invoke-virtual {v1}, Ljava/util/regex/Matcher;->find()Z
    move-result v2
    if-eqz v2, :resolve_none
    const/4 v2, 0x1
    invoke-virtual {v1, v2}, Ljava/util/regex/Matcher;->group(I)Ljava/lang/String;
    move-result-object v1
    :try_start_0
    new-instance v2, Ljava/net/URL;
    invoke-direct {v2, p0}, Ljava/net/URL;-><init>(Ljava/lang/String;)V
    new-instance v3, Ljava/net/URL;
    invoke-direct {v3, v2, v1}, Ljava/net/URL;-><init>(Ljava/net/URL;Ljava/lang/String;)V
    invoke-virtual {v3}, Ljava/net/URL;->toString()Ljava/lang/String;
    move-result-object v1
    add-int/lit8 p1, p1, 0x1
    invoke-static {v1, p1}, Lcom/dpsteam/filmplus/tools/FootballFeed;->resolveStream(Ljava/lang/String;I)Ljava/lang/String;
    move-result-object v1
    return-object v1
    :try_end_0
    .catch Ljava/lang/Throwable; {:try_start_0 .. :try_end_0} :resolve_none

    :resolve_none
    const/4 v0, 0x0
    return-object v0
.end method

.method public final run()V
    .locals 15

    :try_start_0
    const-string v0, "https://ultrago-xi.vercel.app/gol-3"
    invoke-static {v0}, Lcom/dpsteam/filmplus/tools/FootballFeed;->readPage(Ljava/lang/String;)Ljava/lang/String;
    move-result-object v0
    if-eqz v0, :feed_done

    new-instance v1, Lorg/json/JSONObject;
    invoke-direct {v1, v0}, Lorg/json/JSONObject;-><init>(Ljava/lang/String;)V
    const-string v0, "transmisiones"
    invoke-virtual {v1, v0}, Lorg/json/JSONObject;->optJSONArray(Ljava/lang/String;)Lorg/json/JSONArray;
    move-result-object v1
    if-eqz v1, :feed_done

    new-instance v2, Ljava/util/ArrayList;
    invoke-direct {v2}, Ljava/util/ArrayList;-><init>()V
    const/4 v3, 0x0

    :event_loop
    invoke-virtual {v1}, Lorg/json/JSONArray;->length()I
    move-result v4
    if-ge v3, v4, :events_done
    invoke-virtual {v2}, Ljava/util/ArrayList;->size()I
    move-result v4
    const/16 v5, 0x12
    if-ge v4, v5, :events_done

    invoke-virtual {v1, v3}, Lorg/json/JSONArray;->optJSONObject(I)Lorg/json/JSONObject;
    move-result-object v4
    add-int/lit8 v3, v3, 0x1
    if-eqz v4, :event_loop

    const-string v5, "titulo"
    invoke-virtual {v4, v5}, Lorg/json/JSONObject;->optString(Ljava/lang/String;)Ljava/lang/String;
    move-result-object v5
    const-string v6, "liga"
    invoke-virtual {v4, v6}, Lorg/json/JSONObject;->optString(Ljava/lang/String;)Ljava/lang/String;
    move-result-object v6
    new-instance v7, Ljava/lang/StringBuilder;
    invoke-direct {v7, v5}, Ljava/lang/StringBuilder;-><init>(Ljava/lang/String;)V
    const-string v8, " "
    invoke-virtual {v7, v8}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;
    invoke-virtual {v7, v6}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;
    invoke-virtual {v7}, Ljava/lang/StringBuilder;->toString()Ljava/lang/String;
    move-result-object v7
    invoke-virtual {v7}, Ljava/lang/String;->toLowerCase()Ljava/lang/String;
    move-result-object v7

    const-string v8, "hockey"
    invoke-virtual {v7, v8}, Ljava/lang/String;->contains(Ljava/lang/CharSequence;)Z
    move-result v8
    if-nez v8, :event_loop
    const-string v8, "tenis"
    invoke-virtual {v7, v8}, Ljava/lang/String;->contains(Ljava/lang/CharSequence;)Z
    move-result v8
    if-nez v8, :event_loop
    const-string v8, "tennis"
    invoke-virtual {v7, v8}, Ljava/lang/String;->contains(Ljava/lang/CharSequence;)Z
    move-result v8
    if-nez v8, :event_loop
    const-string v8, "golf"
    invoke-virtual {v7, v8}, Ljava/lang/String;->contains(Ljava/lang/CharSequence;)Z
    move-result v8
    if-nez v8, :event_loop
    const-string v8, "mlb"
    invoke-virtual {v7, v8}, Ljava/lang/String;->contains(Ljava/lang/CharSequence;)Z
    move-result v8
    if-nez v8, :event_loop

    const-string v8, "canales"
    invoke-virtual {v4, v8}, Lorg/json/JSONObject;->optJSONArray(Ljava/lang/String;)Lorg/json/JSONArray;
    move-result-object v8
    if-eqz v8, :event_loop
    const/4 v9, 0x0
    const/4 v10, 0x0
    :channel_loop
    invoke-virtual {v8}, Lorg/json/JSONArray;->length()I
    move-result v11
    if-ge v9, v11, :channel_done
    invoke-virtual {v8, v9}, Lorg/json/JSONArray;->optJSONObject(I)Lorg/json/JSONObject;
    move-result-object v11
    add-int/lit8 v9, v9, 0x1
    if-eqz v11, :channel_loop
    const-string v12, "link"
    invoke-virtual {v11, v12}, Lorg/json/JSONObject;->optString(Ljava/lang/String;)Ljava/lang/String;
    move-result-object v10
    if-eqz v10, :channel_loop
    invoke-virtual {v10}, Ljava/lang/String;->length()I
    move-result v12
    if-lez v12, :channel_loop
    const-string v12, "http"
    invoke-virtual {v10, v12}, Ljava/lang/String;->startsWith(Ljava/lang/String;)Z
    move-result v12
    if-eqz v12, :channel_loop
    goto :channel_done
    :channel_done
    if-eqz v10, :event_loop

    const/4 v11, 0x0
    invoke-static {v10, v11}, Lcom/dpsteam/filmplus/tools/FootballFeed;->resolveStream(Ljava/lang/String;I)Ljava/lang/String;
    move-result-object v11
    if-eqz v11, :keep_original
    move-object v10, v11
    :keep_original

    new-instance v11, Lcom/dpsteam/filmplus/objects/Media;
    invoke-direct {v11}, Lcom/dpsteam/filmplus/objects/Media;-><init>()V
    const-string v12, "fecha"
    invoke-virtual {v4, v12}, Lorg/json/JSONObject;->optString(Ljava/lang/String;)Ljava/lang/String;
    move-result-object v12
    invoke-virtual {v11, v12}, Lcom/dpsteam/filmplus/objects/Media;->setDate(Ljava/lang/String;)V
    const-string v12, "hora"
    invoke-virtual {v4, v12}, Lorg/json/JSONObject;->optString(Ljava/lang/String;)Ljava/lang/String;
    move-result-object v12
    invoke-virtual {v11, v12}, Lcom/dpsteam/filmplus/objects/Media;->setRelease(Ljava/lang/String;)V
    invoke-virtual {v11, v5}, Lcom/dpsteam/filmplus/objects/Media;->setTitle(Ljava/lang/String;)V
    const-string v12, "estado"
    invoke-virtual {v4, v12}, Lorg/json/JSONObject;->optString(Ljava/lang/String;)Ljava/lang/String;
    move-result-object v12
    new-instance v13, Ljava/lang/StringBuilder;
    invoke-direct {v13, v6}, Ljava/lang/StringBuilder;-><init>(Ljava/lang/String;)V
    const-string v14, "  •  "
    invoke-virtual {v13, v14}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;
    invoke-virtual {v13, v12}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;
    invoke-virtual {v13}, Ljava/lang/StringBuilder;->toString()Ljava/lang/String;
    move-result-object v13
    invoke-virtual {v11, v13}, Lcom/dpsteam/filmplus/objects/Media;->setGenere(Ljava/lang/String;)V
    const-string v12, "logoUrl"
    invoke-virtual {v4, v12}, Lorg/json/JSONObject;->optString(Ljava/lang/String;)Ljava/lang/String;
    move-result-object v12
    invoke-virtual {v11, v12}, Lcom/dpsteam/filmplus/objects/Media;->setImg(Ljava/lang/String;)V
    invoke-virtual {v11, v12}, Lcom/dpsteam/filmplus/objects/Media;->setBackdrop(Ljava/lang/String;)V
    const-string v12, "futbol:"
    invoke-virtual {v11, v12}, Lcom/dpsteam/filmplus/objects/Media;->setTmdb(Ljava/lang/String;)V
    const/16 v12, 0x5f5f
    invoke-virtual {v11, v12}, Lcom/dpsteam/filmplus/objects/Media;->setType(I)V
    invoke-virtual {v11, v10}, Lcom/dpsteam/filmplus/objects/Media;->setStreamUrl(Ljava/lang/String;)V
    invoke-virtual {v2, v11}, Ljava/util/ArrayList;->add(Ljava/lang/Object;)Z
    goto :event_loop

    :events_done
    invoke-virtual {v2}, Ljava/util/ArrayList;->isEmpty()Z
    move-result v0
    if-eqz v0, :post_feed
    goto :feed_done
    :post_feed
    new-instance v0, Landroid/os/Handler;
    invoke-static {}, Landroid/os/Looper;->getMainLooper()Landroid/os/Looper;
    move-result-object v1
    invoke-direct {v0, v1}, Landroid/os/Handler;-><init>(Landroid/os/Looper;)V
    new-instance v1, Lcom/dpsteam/filmplus/tools/FootballFeedUpdate;
    iget-object v3, p0, Lcom/dpsteam/filmplus/tools/FootballFeed;->fragment:Ly3/j;
    invoke-direct {v1, v3, v2}, Lcom/dpsteam/filmplus/tools/FootballFeedUpdate;-><init>(Ly3/j;Ljava/util/ArrayList;)V
    invoke-virtual {v0, v1}, Landroid/os/Handler;->post(Ljava/lang/Runnable;)Z
    :try_end_0
    .catch Ljava/lang/Throwable; {:try_start_0 .. :try_end_0} :feed_error

    :feed_done
    return-void
    :feed_error
    move-exception v0
    const-string v1, "FootballFeed"
    const-string v2, "No se pudo cargar el carrusel de fútbol"
    invoke-static {v1, v2, v0}, Landroid/util/Log;->e(Ljava/lang/String;Ljava/lang/String;Ljava/lang/Throwable;)I
    return-void
.end method