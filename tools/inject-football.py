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


def main() -> None:
    if len(sys.argv) != 2:
        raise SystemExit("usage: inject-football.py <decoded-apk-directory>")

    root = Path(sys.argv[1]).resolve()
    smali = root / "smali"

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
    replace_once(
        delayed_loader,
        """    invoke-virtual {v0}, Ly3/j;->R()V

    .line 130
    goto :goto_2
""",
        """    invoke-virtual {v0}, Ly3/j;->R()V

    new-instance v2, Lcom/dpsteam/filmplus/tools/FootballFeed;
    invoke-direct {v2, v0}, Lcom/dpsteam/filmplus/tools/FootballFeed;-><init>(Ly3/j;)V
    new-instance v3, Ljava/lang/Thread;
    invoke-direct {v3, v2}, Ljava/lang/Thread;-><init>(Ljava/lang/Runnable;)V
    invoke-virtual {v3}, Ljava/lang/Thread;->start()V

    .line 130
    goto :goto_2
""",
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
    if '"const-string v1, "referer"' not in click.read_text():
        replace_once(
            click,
        """    invoke-virtual {v0, v1, v3}, Landroid/content/Intent;->putExtra(Ljava/lang/String;Ljava/lang/String;)Landroid/content/Intent;
    iget-object p1, v2, Lz3/g0;->e:Landroid/content/Context;""",
        """    invoke-virtual {v0, v1, v3}, Landroid/content/Intent;->putExtra(Ljava/lang/String;Ljava/lang/String;)Landroid/content/Intent;
    const-string v1, "referer"
    const-string v3, "https://ultrago-xi.vercel.app/"
    invoke-virtual {v0, v1, v3}, Landroid/content/Intent;->putExtra(Ljava/lang/String;Ljava/lang/String;)Landroid/content/Intent;
    iget-object p1, v2, Lz3/g0;->e:Landroid/content/Context;""",
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
    ):
        source = Path(__file__).resolve().parents[1] / "apk-edit" / rel
        destination = root / rel
        destination.parent.mkdir(parents=True, exist_ok=True)
        destination.write_text(source.read_text())


if __name__ == "__main__":
    main()