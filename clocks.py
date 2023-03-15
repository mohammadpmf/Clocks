from tkinter import *
from datetime import datetime
import pytz

def update():
    timezone_south_africa       = pytz.timezone("Africa/Johannesburg")
    timezone_turkey             = pytz.timezone("Asia/Istanbul")
    timezone_tehran             = pytz.timezone("Asia/Tehran")
    timezone_japan              = pytz.timezone("Asia/Tokyo")
    timezone_canada_toronto     = pytz.timezone("America/Toronto")
    timezone_canada_vancouver   = pytz.timezone("America/Vancouver")
    timezone_germany            = pytz.timezone("Europe/Berlin")
    timezone_england            = pytz.timezone("Europe/London")
    timezone_russia             = pytz.timezone("Europe/Moscow")
    timezone_finland            = pytz.timezone("Europe/Helsinki")
    timezone_swedden            = pytz.timezone("Europe/Stockholm")
    timezone_usa_chicago        = pytz.timezone("America/Chicago")
    timezone_usa_denver         = pytz.timezone("America/Denver")
    timezone_usa_los_angeles    = pytz.timezone("America/Los_Angeles")
    timezone_usa_washington     = pytz.timezone("US/Eastern")
    timezone_usa_new_york       = pytz.timezone("America/New_York")

    time_turkey                 = datetime.now(timezone_turkey)                 .strftime("%H:%M")
    time_south_africa           = datetime.now(timezone_south_africa)           .strftime("%H:%M")
    time_tehran                 = datetime.now(timezone_tehran)                 .strftime("%H:%M")
    time_japan                  = datetime.now(timezone_japan)                  .strftime("%H:%M")
    time_canada_toronto         = datetime.now(timezone_canada_toronto)         .strftime("%H:%M")
    time_canada_vancouver       = datetime.now(timezone_canada_vancouver)       .strftime("%H:%M")
    time_germany                = datetime.now(timezone_germany)                .strftime("%H:%M")
    time_england                = datetime.now(timezone_england)                .strftime("%H:%M")
    time_russia                 = datetime.now(timezone_russia)                 .strftime("%H:%M")
    time_finland                = datetime.now(timezone_finland)                .strftime("%H:%M")
    time_swedden                = datetime.now(timezone_swedden)                .strftime("%H:%M")
    time_usa_chicago            = datetime.now(timezone_usa_chicago)            .strftime("%H:%M")
    time_usa_denver             = datetime.now(timezone_usa_denver)             .strftime("%H:%M")
    time_usa_los_angeles        = datetime.now(timezone_usa_los_angeles)        .strftime("%H:%M")
    time_usa_washington         = datetime.now(timezone_usa_washington)         .strftime("%H:%M")
    time_usa_new_york           = datetime.now(timezone_usa_new_york)           .strftime("%H:%M")

    label_turkey.config(text=time_turkey)
    label_south_aferica.config(text=time_south_africa)
    label_iran.config(text=time_tehran)
    label_japan.config(text=time_japan)
    label_canada_toronto.config(text=time_canada_toronto)
    label_canada_vancouver.config(text=time_canada_vancouver)
    label_germany.config(text=time_germany)
    label_england.config(text=time_england)
    label_russia.config(text=time_russia)
    label_finland.config(text=time_finland)
    label_swedden.config(text=time_swedden)
    label_usa_chicago.config(text=time_usa_chicago)
    label_usa_denver.config(text=time_usa_denver)
    label_usa_los_angeles.config(text=time_usa_los_angeles)
    label_usa_washington.config(text=time_usa_washington)
    label_usa_new_york.config(text=time_usa_new_york)
    root.after(60000, update)

root = Tk()
root.title("(: Mohammad Pourmohammadi Fallah :)")
root.config(background="#333333")
cnf = {
    'bg': "#333333",
    'fg': "orange",
    'font': ('', 14),
    'width': 10,
    'text': "00:00",
    'pady': 3
}
grid_cnf = {
    'pady': 2,
    'padx': 5,
    'row': 1,
    'column': 1,
    'sticky': 'news',
}
###################################    LabelFrames   ###################################
frame_iran                  = LabelFrame(root, cnf=cnf, labelanchor='n', text="ایران"             )
frame_england               = LabelFrame(root, cnf=cnf, labelanchor='n', text="انگلیس"            )
frame_japan                 = LabelFrame(root, cnf=cnf, labelanchor='n', text="ژاپن"              )
frame_russia                = LabelFrame(root, cnf=cnf, labelanchor='n', text="روسیه"             )
frame_canada                = LabelFrame(root, cnf=cnf, labelanchor='n', text="کانادا"           , font=('', 20) )
frame_usa                   = LabelFrame(root, cnf=cnf, labelanchor='n', text="آمریکا"           , font=('', 20) )
frame_south_aferica         = LabelFrame(root, cnf=cnf, labelanchor='n', text="آفریقای جنوبی"    )
frame_finland               = LabelFrame(root, cnf=cnf, labelanchor='n', text="فنلاند"             )
frame_swedden               = LabelFrame(root, cnf=cnf, labelanchor='n', text="سوئد - نروژ"       )
frame_germany               = LabelFrame(root, cnf=cnf, labelanchor='n', text="آلمان - فرانسه - ایتالیا - هلند - اسپانیا")
frame_turkey                = LabelFrame(root, cnf=cnf, labelanchor='n', text="ترکیه"             )

frame_canada_vancouver      = LabelFrame(frame_canada, cnf=cnf, labelanchor='n', text="ونکوور"    )
frame_canada_toronto        = LabelFrame(frame_canada, cnf=cnf, labelanchor='n', text="تورنتو - اتاوا"    )
frame_usa_new_york          = LabelFrame(frame_usa   , cnf=cnf, labelanchor='n', text="نیویورک"   )
frame_usa_washington        = LabelFrame(frame_usa   , cnf=cnf, labelanchor='n', text="واشینگتون" )
frame_usa_denver            = LabelFrame(frame_usa   , cnf=cnf, labelanchor='n', text="دنور"   )
frame_usa_chicago           = LabelFrame(frame_usa   , cnf=cnf, labelanchor='n', text="شیکاگو"   )
frame_usa_los_angeles       = LabelFrame(frame_usa   , cnf=cnf, labelanchor='n', text="لس آنجلس"   )


frame_iran            .grid(row=1,column=3, sticky='news',               padx=5,       )
frame_usa             .grid(row=2,column=1, sticky='news', columnspan=5, padx=5, pady=20)
frame_canada          .grid(row=3,column=1, sticky='news', columnspan=5, padx=5, pady=20)
frame_germany         .grid(row=4,column=1, sticky='news', columnspan=5, padx=5, pady=5)
frame_turkey          .grid(row=5,column=1, sticky='news',               padx=5, pady=5)
frame_swedden         .grid(row=5,column=2, sticky='news',               padx=5, pady=5)
frame_south_aferica   .grid(row=5,column=3, sticky='news',               padx=5, pady=5)
frame_japan           .grid(row=5,column=4, sticky='news',               padx=5, pady=5)
frame_england         .grid(row=5,column=5, sticky='news',               padx=5, pady=5)
frame_russia          .grid(row=6,column=1, sticky='news',               padx=5, pady=5)
frame_finland         .grid(row=6,column=2, sticky='news',               padx=5, pady=5)

frame_canada_vancouver.grid(row=1,column=1, sticky='news',               padx=5, pady=5)
frame_canada_toronto  .grid(row=1,column=2, sticky='news',               padx=5, pady=5)
frame_usa_new_york    .grid(row=1,column=1, sticky='news',               padx=5, pady=5)
frame_usa_washington  .grid(row=1,column=2, sticky='news',               padx=5, pady=5)
frame_usa_denver      .grid(row=1,column=3, sticky='news',               padx=5, pady=5)
frame_usa_chicago     .grid(row=1,column=4, sticky='news',               padx=5, pady=5)
frame_usa_los_angeles .grid(row=1,column=5, sticky='news',               padx=5, pady=5)
###################################    End LabelFrames   ###################################


###################################    Labels   ###################################
label_iran               = Label(frame_iran,            cnf=cnf)
label_england            = Label(frame_england,         cnf=cnf)
label_japan              = Label(frame_japan,           cnf=cnf)
label_russia             = Label(frame_russia,          cnf=cnf)
label_canada_vancouver   = Label(frame_canada_vancouver,cnf=cnf)
label_canada_toronto     = Label(frame_canada_toronto,  cnf=cnf)
label_usa_washington     = Label(frame_usa_washington,  cnf=cnf)
label_usa_new_york       = Label(frame_usa_new_york,    cnf=cnf)
label_usa_denver         = Label(frame_usa_denver,      cnf=cnf)
label_usa_chicago        = Label(frame_usa_chicago,     cnf=cnf)
label_usa_los_angeles    = Label(frame_usa_los_angeles, cnf=cnf)
label_south_aferica      = Label(frame_south_aferica,   cnf=cnf)
label_finland            = Label(frame_finland,         cnf=cnf)
label_swedden            = Label(frame_swedden,         cnf=cnf)
label_germany            = Label(frame_germany,         cnf=cnf)
label_turkey             = Label(frame_turkey,          cnf=cnf)

label_iran              .grid(cnf=grid_cnf)
label_england           .grid(cnf=grid_cnf)
label_japan             .grid(cnf=grid_cnf)
label_russia            .grid(cnf=grid_cnf)
label_canada_vancouver  .grid(cnf=grid_cnf)
label_canada_toronto    .grid(cnf=grid_cnf)
label_usa_washington    .grid(cnf=grid_cnf)
label_usa_denver        .grid(cnf=grid_cnf)
label_usa_chicago       .grid(cnf=grid_cnf)
label_usa_new_york      .grid(cnf=grid_cnf)
label_usa_los_angeles   .grid(cnf=grid_cnf)
label_south_aferica     .grid(cnf=grid_cnf)
label_finland           .grid(cnf=grid_cnf)
label_swedden           .grid(cnf=grid_cnf)
label_germany           .grid(cnf=grid_cnf)
label_turkey            .grid(cnf=grid_cnf)
###################################    End Labels   ###################################
update()
root.mainloop()