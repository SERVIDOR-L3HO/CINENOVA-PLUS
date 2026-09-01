.class public final Lcom/dpsteam/filmplus/tools/ServerBranding;
.super Ljava/lang/Object;


.method public static displayName(Ljava/lang/String;)Ljava/lang/String;
    .locals 1

    const-string v0, "Ultra"
    invoke-virtual {p0, v0}, Ljava/lang/String;->equals(Ljava/lang/Object;)Z
    move-result v0
    if-eqz v0, :cond_0
    const-string p0, "CineFlow"
    return-object p0

    :cond_0
    const-string v0, "Zeus"
    invoke-virtual {p0, v0}, Ljava/lang/String;->equals(Ljava/lang/Object;)Z
    move-result v0
    if-eqz v0, :cond_1
    const-string p0, "TitanReel"
    return-object p0

    :cond_1
    const-string v0, "Fast"
    invoke-virtual {p0, v0}, Ljava/lang/String;->equals(Ljava/lang/Object;)Z
    move-result v0
    if-eqz v0, :cond_2
    const-string p0, "FlashReel"
    return-object p0

    :cond_2
    const-string v0, "Pegasus"
    invoke-virtual {p0, v0}, Ljava/lang/String;->equals(Ljava/lang/Object;)Z
    move-result v0
    if-eqz v0, :cond_3
    const-string p0, "SkyReel"
    return-object p0

    :cond_3
    const-string v0, "Turbo"
    invoke-virtual {p0, v0}, Ljava/lang/String;->equals(Ljava/lang/Object;)Z
    move-result v0
    if-eqz v0, :cond_4
    const-string p0, "TurboFrame"
    return-object p0

    :cond_4
    const-string v0, "Ares"
    invoke-virtual {p0, v0}, Ljava/lang/String;->equals(Ljava/lang/Object;)Z
    move-result v0
    if-eqz v0, :cond_5
    const-string p0, "ActionReel"
    return-object p0

    :cond_5
    const-string v0, "Poseidon"
    invoke-virtual {p0, v0}, Ljava/lang/String;->equals(Ljava/lang/Object;)Z
    move-result v0
    if-eqz v0, :cond_6
    const-string p0, "AquaReel"
    return-object p0

    :cond_6
    const-string v0, "Vip"
    invoke-virtual {p0, v0}, Ljava/lang/String;->equals(Ljava/lang/Object;)Z
    move-result v0
    if-eqz v0, :cond_7
    const-string p0, "LuxeReel"
    return-object p0

    :cond_7
    const-string v0, "Odin"
    invoke-virtual {p0, v0}, Ljava/lang/String;->equals(Ljava/lang/Object;)Z
    move-result v0
    if-eqz v0, :cond_8
    const-string p0, "PrimeFrame"
    return-object p0

    :cond_8
    const-string v0, "Kraken"
    invoke-virtual {p0, v0}, Ljava/lang/String;->equals(Ljava/lang/Object;)Z
    move-result v0
    if-eqz v0, :cond_9
    const-string p0, "DeepReel"
    return-object p0

    :cond_9
    const-string v0, "Hydra"
    invoke-virtual {p0, v0}, Ljava/lang/String;->equals(Ljava/lang/Object;)Z
    move-result v0
    if-eqz v0, :cond_a
    const-string p0, "HydraFrame"
    return-object p0

    :cond_a
    const-string v0, "Cerberus"
    invoke-virtual {p0, v0}, Ljava/lang/String;->equals(Ljava/lang/Object;)Z
    move-result v0
    if-eqz v0, :cond_b
    const-string p0, "GuardReel"
    return-object p0

    :cond_b
    return-object p0
.end method