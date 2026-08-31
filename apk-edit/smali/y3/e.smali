.class public Ly3/e;
.super Landroidx/fragment/app/t;
.source "r8-map-id-7df6f08584a1d9bec3ce3fcb352136c7dc949a7f921bb4d7cd3337f932b6f794"

# interfaces
.implements Landroid/view/View$OnClickListener;


# instance fields
.field public m0:Landroid/view/View;

.field public n0:Landroidx/fragment/app/FragmentActivity;

.field public o0:Landroid/widget/FrameLayout;

.field public p0:Landroid/widget/FrameLayout;

.field public q0:Landroid/widget/FrameLayout;


# direct methods
.method public constructor <init>()V
    .locals 0

    .line 1
    invoke-direct {p0}, Landroidx/fragment/app/t;-><init>()V

    .line 4
    return-void
.end method


# virtual methods
.method public onClick(Landroid/view/View;)V
    .locals 3

    .line 1
    invoke-virtual {p1}, Landroid/view/View;->getId()I

    .line 4
    move-result p1

    .line 5
    const v0, 0x7f080119

    .line 8
    if-ne p1, v0, :cond_0

    .line 10
    new-instance p1, Landroid/content/Intent;

    .line 12
    const-string v0, "android.intent.action.VIEW"

    .line 14
    invoke-direct {p1, v0}, Landroid/content/Intent;-><init>(Ljava/lang/String;)V

    .line 17
    const-string v0, "https://t.me/l3hointeractive"

    .line 25
    invoke-static {v0}, Landroid/net/Uri;->parse(Ljava/lang/String;)Landroid/net/Uri;

    .line 28
    move-result-object v0

    .line 29
    invoke-virtual {p1, v0}, Landroid/content/Intent;->setData(Landroid/net/Uri;)Landroid/content/Intent;

    .line 32
    invoke-virtual {p0, p1}, Landroidx/fragment/app/t;->Q(Landroid/content/Intent;)V

    .line 35
    return-void

    .line 36
    :cond_0
    const v0, 0x7f080112

    .line 39
    if-ne p1, v0, :cond_1

    .line 41
    new-instance p1, Landroid/content/Intent;

    .line 43
    iget-object v0, p0, Ly3/e;->n0:Landroidx/fragment/app/FragmentActivity;

    .line 45
    const-class v1, Lcom/dpsteam/filmplus/activities/FilesActivity;

    .line 47
    invoke-direct {p1, v0, v1}, Landroid/content/Intent;-><init>(Landroid/content/Context;Ljava/lang/Class;)V

    .line 50
    invoke-virtual {p0, p1}, Landroidx/fragment/app/t;->Q(Landroid/content/Intent;)V

    .line 53
    return-void

    .line 54
    :cond_1
    const v0, 0x7f080117

    .line 57
    if-ne p1, v0, :cond_2

    .line 59
    new-instance p1, Landroid/content/Intent;

    .line 61
    iget-object v0, p0, Ly3/e;->n0:Landroidx/fragment/app/FragmentActivity;

    .line 63
    const-class v1, Lcom/dpsteam/filmplus/activities/ConfigurationActivity;

    .line 65
    invoke-direct {p1, v0, v1}, Landroid/content/Intent;-><init>(Landroid/content/Context;Ljava/lang/Class;)V

    .line 68
    invoke-virtual {p0, p1}, Landroidx/fragment/app/t;->Q(Landroid/content/Intent;)V

    .line 71
    return-void

    .line 72
    :cond_2
    const v0, 0x7f080118

    .line 75
    if-ne p1, v0, :cond_3

    .line 77
    .line 85
    new-instance v0, Landroid/content/Intent;

    .line 87
    const-string v1, "android.intent.action.SEND"

    .line 89
    invoke-direct {v0, v1}, Landroid/content/Intent;-><init>(Ljava/lang/String;)V

    .line 92
    const-string v1, "text/plain"

    .line 94
    invoke-virtual {v0, v1}, Landroid/content/Intent;->setType(Ljava/lang/String;)Landroid/content/Intent;

    .line 97
    const-string p1, "CINENOVA BLUE es algo mejor: disfruta tus pel\u00edculas y series favoritas con una experiencia r\u00e1pida, c\u00f3moda y hecha para ti. \u00a1Comp\u00e1rtelo!"

    .line 111
    const-string v1, "android.intent.extra.TEXT"

    .line 113
    invoke-virtual {v0, v1, p1}, Landroid/content/Intent;->putExtra(Ljava/lang/String;Ljava/lang/String;)Landroid/content/Intent;

    .line 116
    const-string p1, "android.intent.extra.TITLE"

    .line 118
    const-string v1, "Compartir"

    .line 120
    invoke-virtual {v0, p1, v1}, Landroid/content/Intent;->putExtra(Ljava/lang/String;Ljava/lang/String;)Landroid/content/Intent;

    .line 123
    invoke-static {v0, v1}, Landroid/content/Intent;->createChooser(Landroid/content/Intent;Ljava/lang/CharSequence;)Landroid/content/Intent;

    .line 126
    move-result-object p1

    .line 127
    invoke-virtual {p0, p1}, Landroidx/fragment/app/t;->Q(Landroid/content/Intent;)V

    .line 130
    :cond_3
    return-void
.end method

.method public final w(Landroid/os/Bundle;)V
    .locals 0

    .line 1
    invoke-super {p0, p1}, Landroidx/fragment/app/t;->w(Landroid/os/Bundle;)V

    .line 4
    invoke-virtual {p0}, Landroidx/fragment/app/t;->j()Landroidx/fragment/app/FragmentActivity;

    .line 7
    move-result-object p1

    .line 8
    iput-object p1, p0, Ly3/e;->n0:Landroidx/fragment/app/FragmentActivity;

    .line 10
    return-void
.end method

.method public final y(Landroid/view/LayoutInflater;Landroid/view/ViewGroup;)Landroid/view/View;
    .locals 2

    .line 1
    const v0, 0x7f0b004a

    .line 4
    const/4 v1, 0x0

    .line 5
    invoke-virtual {p1, v0, p2, v1}, Landroid/view/LayoutInflater;->inflate(ILandroid/view/ViewGroup;Z)Landroid/view/View;

    .line 8
    move-result-object p1

    .line 9
    iput-object p1, p0, Ly3/e;->m0:Landroid/view/View;

    .line 11
    const p2, 0x7f080119

    .line 14
    invoke-virtual {p1, p2}, Landroid/view/View;->findViewById(I)Landroid/view/View;

    .line 17
    move-result-object p1

    .line 18
    check-cast p1, Landroid/widget/FrameLayout;

    .line 20
    iput-object p1, p0, Ly3/e;->o0:Landroid/widget/FrameLayout;

    .line 22
    iget-object p1, p0, Ly3/e;->m0:Landroid/view/View;

    .line 24
    const p2, 0x7f080112

    .line 27
    invoke-virtual {p1, p2}, Landroid/view/View;->findViewById(I)Landroid/view/View;

    .line 30
    move-result-object p1

    .line 31
    check-cast p1, Landroid/widget/FrameLayout;

    .line 33
    iput-object p1, p0, Ly3/e;->p0:Landroid/widget/FrameLayout;

    .line 35
    iget-object p1, p0, Ly3/e;->m0:Landroid/view/View;

    .line 37
    const p2, 0x7f080117

    .line 40
    invoke-virtual {p1, p2}, Landroid/view/View;->findViewById(I)Landroid/view/View;

    .line 43
    move-result-object p1

    .line 44
    check-cast p1, Landroid/widget/FrameLayout;

    .line 46
    iput-object p1, p0, Ly3/e;->q0:Landroid/widget/FrameLayout;

    .line 48
    iget-object p1, p0, Ly3/e;->m0:Landroid/view/View;

    .line 50
    const p2, 0x7f080118

    .line 53
    invoke-virtual {p1, p2}, Landroid/view/View;->findViewById(I)Landroid/view/View;

    .line 56
    move-result-object p1

    .line 57
    check-cast p1, Landroid/widget/FrameLayout;

    .line 59
    invoke-virtual {p1, p0}, Landroid/view/View;->setOnClickListener(Landroid/view/View$OnClickListener;)V

    .line 62
    iget-object p1, p0, Ly3/e;->q0:Landroid/widget/FrameLayout;

    .line 64
    invoke-virtual {p1, p0}, Landroid/view/View;->setOnClickListener(Landroid/view/View$OnClickListener;)V

    .line 67
    iget-object p1, p0, Ly3/e;->p0:Landroid/widget/FrameLayout;

    .line 69
    invoke-virtual {p1, p0}, Landroid/view/View;->setOnClickListener(Landroid/view/View$OnClickListener;)V

    .line 72
    iget-object p1, p0, Ly3/e;->o0:Landroid/widget/FrameLayout;

    .line 74
    invoke-virtual {p1, p0}, Landroid/view/View;->setOnClickListener(Landroid/view/View$OnClickListener;)V

    .line 77
    iget-object p1, p0, Ly3/e;->m0:Landroid/view/View;

    .line 79
    return-object p1
.end method
