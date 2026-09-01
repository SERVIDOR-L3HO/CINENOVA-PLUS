#!/usr/bin/env python3
"""Apply the football feature to an apktool-decoded CINENOVA tree.

The repository intentionally keeps the recovered APK outside the source tree.
This small, repeatable injector lets the checked-in apk-edit overlay and the
decoded base be rebuilt without committing the 100+ MB generated tree.
"""

from pathlib import Path
import sys


def replace_once(path: Path, old: str, new: str) -> None:
    text = path.read_text()
    if new in text:
        return
    if old not in text:
        raise SystemExit(f"Expected patch anchor was not found: {path}")
    path.write_text(text.replace(old, new, 1))


def keep_info_screen_open(root: Path) -> None:
    """Do not close the details screen when a metadata request fails.

    The recovered app used to finish both details activities from their
    network/JSON error callbacks.  On a normal phone this looked like a card
    tap that opened the details screen for a moment and then returned home.
    Keep the activity alive and show the same connection error toast used by
    the other callbacks.
    """

    callbacks = (
        (
            root / "smali/com/dpsteam/filmplus/activities/n.smali",
            "Lcom/dpsteam/filmplus/activities/n;->b:Lcom/dpsteam/filmplus/activities/InfoActivity;",
            1,
        ),
        (
            root / "smali/com/dpsteam/filmplus/activities/r.smali",
            "Lcom/dpsteam/filmplus/activities/r;->b:Lcom/dpsteam/filmplus/activities/InfoActivity2;",
            2,
        ),
    )
    for path, activity_field, callback_index in callbacks:
        text = path.read_text()
        if f"info_details_keep_open_{callback_index}" in text:
            continue

        network_error = f"""    :pswitch_0
    invoke-virtual {{p1}}, Ljava/lang/Throwable;->printStackTrace()V

    .line 31
    iget-object p1, p0, {activity_field}

    .line 33
    invoke-virtual {{p1}}, Landroid/app/Activity;->finish()V
"""
        if network_error not in text:
            raise SystemExit(
                f"Expected details network error anchor was not found: {path}"
            )
        network_replacement = f"""    :pswitch_0
    invoke-virtual {{p1}}, Ljava/lang/Throwable;->printStackTrace()V

    .line 31
    iget-object p1, p0, {activity_field}

    # info_details_keep_open_{callback_index}
    invoke-virtual {{p1}}, Landroidx/appcompat/app/AppCompatActivity;->getResources()Landroid/content/res/Resources;
    move-result-object v0
    const v1, 0x7f110107
    invoke-virtual {{v0, v1}}, Landroid/content/res/Resources;->getString(I)Ljava/lang/String;
    move-result-object v0
    const/4 v1, 0x1
    invoke-static {{p1, v0, v1}}, Landroid/widget/Toast;->makeText(Landroid/content/Context;Ljava/lang/CharSequence;I)Landroid/widget/Toast;
    move-result-object p1
    invoke-virtual {{p1}}, Landroid/widget/Toast;->show()V
"""
        text = text.replace(network_error, network_replacement, 1)

        if "InfoActivity;" in activity_field:
            detail_error = """    invoke-virtual {v1}, Landroid/app/Activity;->finish()V

    .line 273
    :goto_2
"""
            detail_replacement = """    # Keep the details screen visible when metadata JSON is incomplete.
    .line 273
    :goto_2
"""
        else:
            detail_error = """    invoke-virtual {v1}, Landroid/app/Activity;->finish()V

    .line 331
    :goto_4
"""
            detail_replacement = """    # Keep the details screen visible when metadata JSON is incomplete.
    .line 331
    :goto_4
"""
        if detail_error not in text:
            raise SystemExit(
                f"Expected details JSON error anchor was not found: {path}"
            )
        path.write_text(text.replace(detail_error, detail_replacement, 1))


def main() -> None:
    if len(sys.argv) != 2:
        raise SystemExit("usage: inject-football.py <decoded-apk-directory>")

    root = Path(sys.argv[1]).resolve()
    smali = root / "smali"

    keep_info_screen_open(root)

    media = smali / "com/dpsteam/filmplus/objects/Media.smali"
    replace_once(
        media,
        ".field type:I\n\n\n# direct methods",
        ".field type:I\n\n.field streamUrl:Ljava/lang/String;\n\n\n# direct methods",
    )
    replace_once(
        media,
        ".method public getType()I\n    .locals 1\n",
        """.method public getStreamUrl()Ljava/lang/String;
    .locals 1

    iget-object v0, p0, Lcom/dpsteam/filmplus/objects/Media;->streamUrl:Ljava/lang/String;
    return-object v0
.end method

.method public getType()I
    .locals 1
""",
    )
    replace_once(
        media,
        ".method public setType(I)V\n    .locals 0\n",
        """.method public setStreamUrl(Ljava/lang/String;)V
    .locals 0

    iput-object p1, p0, Lcom/dpsteam/filmplus/objects/Media;->streamUrl:Ljava/lang/String;
    return-void
.end method

.method public setType(I)V
    .locals 0
""",
    )

    home = smali / "y3/j.smali"
    replace_once(
        home,
        ".field public p0:Ljava/util/ArrayList;\n\n.field public q0",
        ".field public p0:Ljava/util/ArrayList;\n\n.field public x0:Ljava/util/ArrayList;\n\n.field public q0",
    )
    replace_once(
        home,
        """    iget-object v0, p0, Ly3/j;->p0:Ljava/util/ArrayList;

    .line 3
    const/4 v1, 0x0
""",
        """    iget-object v0, p0, Ly3/j;->x0:Ljava/util/ArrayList;
    if-eqz v0, :football_section_ready
    new-instance v1, Lcom/dpsteam/filmplus/objects/CustomList;
    const-string v2, "FÚTBOL EN VIVO"
    invoke-direct {v1, v2, v0}, Lcom/dpsteam/filmplus/objects/CustomList;-><init>(Ljava/lang/String;Ljava/util/ArrayList;)V
    iget-object v2, p0, Ly3/j;->p0:Ljava/util/ArrayList;
    const/4 v3, 0x1
    invoke-virtual {v2, v3, v1}, Ljava/util/ArrayList;->add(ILjava/lang/Object;)V
    const/4 v0, 0x0
    iput-object v0, p0, Ly3/j;->x0:Ljava/util/ArrayList;

    :football_section_ready
    iget-object v0, p0, Ly3/j;->p0:Ljava/util/ArrayList;

    .line 3
    const/4 v1, 0x0
""",
    )
    home_text = home.read_text()
    worker_block = """    new-instance v0, Lcom/dpsteam/filmplus/tools/FootballFeed;
    invoke-direct {v0, p0}, Lcom/dpsteam/filmplus/tools/FootballFeed;-><init>(Ly3/j;)V
    new-instance v1, Ljava/lang/Thread;
    invoke-direct {v1, v0}, Ljava/lang/Thread;-><init>(Ljava/lang/Runnable;)V
    invoke-virtual {v1}, Ljava/lang/Thread;->start()V

"""
    if worker_block in home_text:
        home.write_text(home_text.replace(worker_block, "", 1))

    delayed_loader = smali / "h7/i2.smali"
    delayed_text = delayed_loader.read_text()
    tv_worker_marker = "    invoke-virtual {v0}, Ly3/j;->R()V"
    tv_worker = """    new-instance v2, Lcom/dpsteam/filmplus/tools/FootballFeed;
    invoke-direct {v2, v0}, Lcom/dpsteam/filmplus/tools/FootballFeed;-><init>(Ly3/j;)V
    new-instance v3, Ljava/lang/Thread;
    invoke-direct {v3, v2}, Ljava/lang/Thread;-><init>(Ljava/lang/Runnable;)V
    invoke-virtual {v3}, Ljava/lang/Thread;->start()V
"""
    if "Lcom/dpsteam/filmplus/tools/FootballFeed;" not in delayed_text:
        if tv_worker_marker not in delayed_text:
            raise SystemExit(f"Expected TV load call was not found: {delayed_loader}")
        delayed_text = delayed_text.replace(
            tv_worker_marker,
            tv_worker_marker + "\n\n" + tv_worker,
            1,
        )
        delayed_loader.write_text(delayed_text)
    android_worker_block = """    invoke-virtual {v0}, Ly3/i;->S()V

    new-instance v2, Lcom/dpsteam/filmplus/tools/FootballFeedAndroid;
    invoke-direct {v2, v0}, Lcom/dpsteam/filmplus/tools/FootballFeedAndroid;-><init>(Ly3/i;)V
    new-instance v3, Ljava/lang/Thread;
    invoke-direct {v3, v2}, Ljava/lang/Thread;-><init>(Ljava/lang/Runnable;)V
    invoke-virtual {v3}, Ljava/lang/Thread;->start()V

"""
    delayed_text = delayed_loader.read_text()
    if "Lcom/dpsteam/filmplus/tools/FootballFeedAndroid;" not in delayed_text:
        anchor = "    invoke-virtual {v0}, Ly3/i;->S()V"
        if anchor not in delayed_text:
            raise SystemExit(f"Expected Android load call was not found: {delayed_loader}")
        delayed_loader.write_text(
            delayed_text.replace(anchor, android_worker_block.rstrip(), 1)
        )

    click = smali / "z3/e0.smali"
    if "0x5f5f" not in click.read_text():
        replace_once(
            click,
        """    const/16 v1, 0x1ab9

    .line 9
    iget-object v2, p0, Lz3/e0;->b:Lz3/g0;

    .line 11
    if-ne v0, v1, :cond_0
""",
        """    const/16 v1, 0x1ab9

    .line 9
    iget-object v2, p0, Lz3/e0;->b:Lz3/g0;

    .line 11
    const/16 v3, 0x5f5f
    if-ne v0, v3, :normal_media_click
    new-instance v0, Landroid/content/Intent;
    iget-object v1, v2, Lz3/g0;->e:Landroid/content/Context;
    const-class v3, Lcom/dpsteam/filmplus/activities/MediaActivity;
    invoke-direct {v0, v1, v3}, Landroid/content/Intent;-><init>(Landroid/content/Context;Ljava/lang/Class;)V
    const-string v1, "video"
    invoke-virtual {p1}, Lcom/dpsteam/filmplus/objects/Media;->getStreamUrl()Ljava/lang/String;
    move-result-object v3
    invoke-virtual {v0, v1, v3}, Landroid/content/Intent;->putExtra(Ljava/lang/String;Ljava/lang/String;)Landroid/content/Intent;
    const-string v1, "isVideo"
    const/4 v3, 0x1
    invoke-virtual {v0, v1, v3}, Landroid/content/Intent;->putExtra(Ljava/lang/String;Z)Landroid/content/Intent;
    const-string v1, "isLocal"
    const/4 v3, 0x0
    invoke-virtual {v0, v1, v3}, Landroid/content/Intent;->putExtra(Ljava/lang/String;Z)Landroid/content/Intent;
    const-string v1, "id"
    invoke-virtual {p1}, Lcom/dpsteam/filmplus/objects/Media;->getTitle()Ljava/lang/String;
    move-result-object v3
    invoke-virtual {v0, v1, v3}, Landroid/content/Intent;->putExtra(Ljava/lang/String;Ljava/lang/String;)Landroid/content/Intent;
    iget-object p1, v2, Lz3/g0;->e:Landroid/content/Context;
    invoke-virtual {p1, v0}, Landroid/content/Context;->startActivity(Landroid/content/Intent;)V
    return-void

    :normal_media_click
    if-ne v0, v1, :cond_0
""",
        )
    click_text = click.read_text()
    if 'const-string v1, "referer"' not in click_text:
        marker = "    invoke-virtual {v0, v1, v3}, Landroid/content/Intent;->putExtra(Ljava/lang/String;Ljava/lang/String;)Landroid/content/Intent;"
        click.write_text(
            click_text.replace(
                marker,
                marker
                + '\n    const-string v1, "referer"\n'
                + '    const-string v3, "https://ultrago-xi.vercel.app/"\n'
                + '    invoke-virtual {v0, v1, v3}, Landroid/content/Intent;->putExtra(Ljava/lang/String;Ljava/lang/String;)Landroid/content/Intent;',
                1,
            )
        )

    android_click = smali / "z3/b0.smali"
    android_click_text = android_click.read_text()
    if "0x5f5f" not in android_click_text:
        marker = "    iget-object v2, p0, Lz3/b0;->b:Lz3/s;"
        android_worker = """    const/16 v3, 0x5f5f
    if-ne v0, v3, :cond_0
    new-instance v0, Landroid/content/Intent;
    iget-object v1, v2, Lz3/s;->f:Ljava/lang/Object;
    check-cast v1, Landroid/content/Context;
    const-class v3, Lcom/dpsteam/filmplus/activities/MediaActivity;
    invoke-direct {v0, v1, v3}, Landroid/content/Intent;-><init>(Landroid/content/Context;Ljava/lang/Class;)V
    const-string v1, "video"
    invoke-virtual {p1}, Lcom/dpsteam/filmplus/objects/Media;->getStreamUrl()Ljava/lang/String;
    move-result-object v3
    invoke-virtual {v0, v1, v3}, Landroid/content/Intent;->putExtra(Ljava/lang/String;Ljava/lang/String;)Landroid/content/Intent;
    const-string v1, "isVideo"
    const/4 v3, 0x1
    invoke-virtual {v0, v1, v3}, Landroid/content/Intent;->putExtra(Ljava/lang/String;Z)Landroid/content/Intent;
    const-string v1, "isLocal"
    const/4 v3, 0x0
    invoke-virtual {v0, v1, v3}, Landroid/content/Intent;->putExtra(Ljava/lang/String;Z)Landroid/content/Intent;
    const-string v1, "id"
    invoke-virtual {p1}, Lcom/dpsteam/filmplus/objects/Media;->getTitle()Ljava/lang/String;
    move-result-object v3
    invoke-virtual {v0, v1, v3}, Landroid/content/Intent;->putExtra(Ljava/lang/String;Ljava/lang/String;)Landroid/content/Intent;
    const-string v1, "referer"
    const-string v3, "https://ultrago-xi.vercel.app/"
    invoke-virtual {v0, v1, v3}, Landroid/content/Intent;->putExtra(Ljava/lang/String;Ljava/lang/String;)Landroid/content/Intent;
    iget-object p1, v2, Lz3/s;->f:Ljava/lang/Object;
    check-cast p1, Landroid/content/Context;
    invoke-virtual {p1, v0}, Landroid/content/Context;->startActivity(Landroid/content/Intent;)V
    return-void
"""
        if marker not in android_click_text:
            raise SystemExit(f"Expected Android click anchor was not found: {android_click}")
        android_click.write_text(
            android_click_text.replace(
                marker,
                marker + "\n\n" + android_worker.rstrip(),
                1,
            )
        )

    card = root / "res/layout/media_raw.xml"
    card_text = card.read_text()
    if 'android:id="@id/tv_t_search"' not in card_text:
        title = """    <TextView android:textSize="11.0sp" android:textStyle="bold" android:textColor="@android:color/white" android:gravity="bottom" android:layout_gravity="bottom" android:paddingLeft="7.0dip" android:paddingRight="7.0dip" android:paddingBottom="20.0dip" android:ellipsize="end" android:maxLines="2" android:id="@id/tv_t_search" android:layout_width="fill_parent" android:layout_height="48.0dip" android:shadowColor="#ff000000" android:shadowDx="0.0" android:shadowDy="1.0" android:shadowRadius="3.0" />"""
        one_line = """    <TextView android:textSize="8.0sp" android:textStyle="bold" android:textColor="#e6ffffff" android:gravity="center" android:layout_gravity="bottom|center" android:layout_width="wrap_content" android:layout_height="22.0dip" android:text="CINENOVA BLUE" android:letterSpacing="0.16" />"""
        if one_line in card_text:
            card_text = card_text.replace(one_line, title + "\n" + one_line, 1)
        else:
            legacy_line = '        android:text="CINENOVA BLUE" />'
            if legacy_line not in card_text:
                raise SystemExit(f"Expected card anchor was not found: {card}")
            card_text = card_text.replace(legacy_line, title + "\n" + legacy_line, 1)
        card.write_text(card_text)

    for rel in (
        "smali/com/dpsteam/filmplus/tools/FootballFeed.smali",
        "smali/com/dpsteam/filmplus/tools/FootballFeedUpdate.smali",
        "smali/com/dpsteam/filmplus/tools/FootballFeedAndroidUpdate.smali",
    ):
        source = Path(__file__).resolve().parents[1] / "apk-edit" / rel
        destination = root / rel
        destination.parent.mkdir(parents=True, exist_ok=True)
        destination.write_text(source.read_text())

    # The TV home is Ly3/j, while the normal Android home is Ly3/i.  Keep the
    # feed parser shared by generating a descriptor-only Android variant from
    # the checked-in TV implementation, but give Android its own UI update
    # runnable because its adapter is z3/s rather than z3/w.
    feed_source = Path(__file__).resolve().parents[1] / "apk-edit" / "smali/com/dpsteam/filmplus/tools/FootballFeed.smali"
    feed_android = (
        feed_source.read_text()
        .replace("FootballFeed", "FootballFeedAndroid")
        .replace("Ly3/j", "Ly3/i")
    )
    (root / "smali/com/dpsteam/filmplus/tools/FootballFeedAndroid.smali").write_text(feed_android)


if __name__ == "__main__":
    main()