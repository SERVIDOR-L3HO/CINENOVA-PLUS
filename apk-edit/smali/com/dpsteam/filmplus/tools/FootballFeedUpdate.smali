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
    .locals 3

    iget-object v0, p0, Lcom/dpsteam/filmplus/tools/FootballFeedUpdate;->fragment:Ly3/j;
    iget-object v1, p0, Lcom/dpsteam/filmplus/tools/FootballFeedUpdate;->items:Ljava/util/ArrayList;
    iput-object v1, v0, Ly3/j;->x0:Ljava/util/ArrayList;
    iget-object v2, v0, Ly3/j;->p0:Ljava/util/ArrayList;
    if-eqz v2, :done
    invoke-virtual {v0}, Ly3/j;->R()V

    :done
    return-void
.end method