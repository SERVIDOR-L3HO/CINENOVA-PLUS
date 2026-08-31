.class public final Lcom/dpsteam/filmplus/tools/FootballFeedUpdate;
.super Ljava/lang/Object;
.source "FootballFeedUpdate.java"

# interfaces
.implements Ljava/lang/Runnable;

# instance fields
.field private final fragment:Ly3/j;

.field private final items:Ljava/util/ArrayList;

# direct methods
.method public constructor <init>(Ly3/j;Ljava/util/ArrayList;)V
    .locals 0

    invoke-direct {p0}, Ljava/lang/Object;-><init>()V
    iput-object p1, p0, Lcom/dpsteam/filmplus/tools/FootballFeedUpdate;->fragment:Ly3/j;
    iput-object p2, p0, Lcom/dpsteam/filmplus/tools/FootballFeedUpdate;->items:Ljava/util/ArrayList;
    return-void
.end method

# virtual methods
.method public final run()V
    .locals 5

    iget-object v0, p0, Lcom/dpsteam/filmplus/tools/FootballFeedUpdate;->fragment:Ly3/j;
    iget-object v1, p0, Lcom/dpsteam/filmplus/tools/FootballFeedUpdate;->items:Ljava/util/ArrayList;

    if-eqz v1, :done
    invoke-virtual {v1}, Ljava/util/ArrayList;->isEmpty()Z
    move-result v2
    if-eqz v2, :has_items
    goto :done

    :has_items
    iget-object v2, v0, Ly3/j;->p0:Ljava/util/ArrayList;
    if-eqz v2, :done
    invoke-virtual {v2}, Ljava/util/ArrayList;->isEmpty()Z
    move-result v4
    if-eqz v4, :add_section
    goto :done

    :add_section
    new-instance v3, Lcom/dpsteam/filmplus/objects/CustomList;
    const-string v4, "FÚTBOL EN VIVO"
    invoke-direct {v3, v4, v1}, Lcom/dpsteam/filmplus/objects/CustomList;-><init>(Ljava/lang/String;Ljava/util/ArrayList;)V
    const/4 v4, 0x1
    invoke-virtual {v2, v4, v3}, Ljava/util/ArrayList;->add(ILjava/lang/Object;)V
    invoke-virtual {v0}, Ly3/j;->R()V

    :done
    return-void
.end method