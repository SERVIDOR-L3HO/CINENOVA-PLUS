.class public final Lcom/dpsteam/filmplus/tools/FootballFeedAndroidUpdate;
.super Ljava/lang/Object;
.source "FootballFeedAndroidUpdate.java"

# interfaces
.implements Ljava/lang/Runnable;

# instance fields
.field private final fragment:Ly3/i;

.field private final items:Ljava/util/ArrayList;

# direct methods
.method public constructor <init>(Ly3/i;Ljava/util/ArrayList;)V
    .locals 0

    invoke-direct {p0}, Ljava/lang/Object;-><init>()V
    iput-object p1, p0, Lcom/dpsteam/filmplus/tools/FootballFeedAndroidUpdate;->fragment:Ly3/i;
    iput-object p2, p0, Lcom/dpsteam/filmplus/tools/FootballFeedAndroidUpdate;->items:Ljava/util/ArrayList;
    return-void
.end method

# virtual methods
.method public final run()V
    .locals 5

    iget-object v0, p0, Lcom/dpsteam/filmplus/tools/FootballFeedAndroidUpdate;->fragment:Ly3/i;
    iget-object v1, p0, Lcom/dpsteam/filmplus/tools/FootballFeedAndroidUpdate;->items:Ljava/util/ArrayList;
    iget-object v2, v0, Ly3/i;->p0:Ljava/util/ArrayList;
    if-eqz v2, :done

    new-instance v3, Lcom/dpsteam/filmplus/objects/CustomList;
    const-string v4, "FÚTBOL EN VIVO"
    invoke-direct {v3, v4, v1}, Lcom/dpsteam/filmplus/objects/CustomList;-><init>(Ljava/lang/String;Ljava/util/ArrayList;)V
    const/4 v4, 0x1
    invoke-virtual {v2, v4, v3}, Ljava/util/ArrayList;->add(ILjava/lang/Object;)V

    iget-object v2, v0, Ly3/i;->w0:Lz3/s;
    if-eqz v2, :done
    invoke-virtual {v2}, Landroidx/recyclerview/widget/i0;->d()V

    :done
    return-void
.end method