# for some of them I used different pages https://www.wowhead.com/
zul_bar_id_locator = '//*[@id="zul-bar"]'
div_locator = '//div'
patch_content_locator = '//*[@id="main-contents"]/div[5]/div[2]/div[3]/h2'
zul_bar_locator = "//div[contains(@class, 'zul-bar')]"
zul_bar_span_locator = "//div[@class='zul-bar-mobile-menu-back-row']//span"
zul_bar_span_locator_css = "div.zul-bar-mobile-menu-back-row span"
zul_bar_mobile_menu_locator = "//div[@class='zul-bar-mobile-menu-back-row']" \
                              "//div[@class='zul-bar-mobile-menu-back-title']"
zul_bar_mobile_menu_locator_css = "div.zul-bar-mobile-menu-back-row div.zul-bar-mobile-menu-back-title"
text_input_locator = "//input[@type='text']"
text_input_locator_css = "input[type='text']"
news_mobile_toc_links_second_td_locator = "//table[@class='news-mobile-toc-links']//td[2]"
menu_item_spans_locator = "//div[@class='menu-item']/*/span"
last_list_item_locator = "//ul/li[last()]"
last_list_item_locator_css = "ul li:last-child"
elements_with_id_inside_div_locator = "//div[@id='select-all-hosts-input-container']//child::*"
elements_with_id_inside_div_locator_css = "div#select-all-hosts-input-container *"
zul_bar_family_elements_following_locator = "//div[@class ='zul-bar-mobile-content']//following-sibling::div"
zul_bar_mobile_locator = "//div[@class='zul-bar-mobile-content']/following::div"
log_in_bnet_button_locator = "//a[contains(@class, 'header-user-bnet') and contains(@class, 'btn')" \
                             " and contains(@class, 'btn-blizzard')]"
classes_wildcard_locator = "//a[contains(@class, 'header-nav-classes') and contains(@class, 'first-4')" \
                           " and contains(@class, 'second-1') and @href='/classes']"
classes_axes_locator = "//a[@class='header-nav-text header-nav-classes first-4 second-1' and @href='/classes']"
teaser_image_locator = "//div[@class='news-list-card']/descendant::a[@class='news-list-card-teaser-image']"
teaser_image_locator_css = "div.news-list-card a.news-list-card-teaser-image"
prof_vendor_update_in_patch_10_333877_link_locator = "//a[@href='/news/new-profession-vendor-converts-knowledge-into" \
                                                     "-artisans-mettle-coming-in-patch-10-333877']"
warcraft3_news_locator = "//a[contains(@class, 'news-type-color-')]/span[text()='Warcraft III']"
page_3_pagination_button_locator = "//a[@class='news-pagination-pages-page' and @href='/news?page=3']"
next_page_pagination_button_locator = "//a[contains(@href, '/news?page=2')][@rel='next'][@aria-label='Next']"
last_page_pagination_button_locator = "//a[@href='/news?page=1142' and @rel='last' and @aria-label='Last']"
footer_wowhead_logo_locator = "//section[@class='footer-navigation-bar-logo-link']"
talents_menu_item_locator = "//a[contains(@href, '/guide/dragonriding/talent-traits')]/span"
talents_menu_item_locator_css = "a[href*='/guide/dragonriding/talent-traits'] > span"
the_unshackled_img_locator = "//img[@src='https://wow.zamimg.com/images/wow/icons/medium/inv_faction_unshackled.jpg']"
the_unshackled_img_locator_css = "img[src='https://wow.zamimg.com/images/wow/icons/medium/inv_faction_unshackled.jpg']"
status_widgets_locator = "//div[contains(@class, 'status-widget-slider')]/div[@class='slider-labels']" \
                         "/span[@class='slider-labels-values']"
twitch_social_link_locator = "//a[@class='author-social-links-button' and @href='https://www.twitch.tv/tettles' " \
                             "and @target='_blank' and @data-social-platform='twitch']"
report_article_button_locator = "//button[@class='btn btn-small btn-site fa fa-exclamation-triangle']" \
                                "[@onclick='ContactTool.show.call(ContactTool, {mode: 6, guide: 18554})']"
report_article_button_locator_css = "button.btn.btn-small.btn-site.fa.fa-exclamation-triangle" \
                                    "[onclick='ContactTool.show.call(ContactTool, {mode: 6, guide: 18554})']"
patch_notes_10_1_button_locator = "//a[contains(@class, 'cta-button')][@href='https://www.wowhead.com/news/" \
                                  "dragonflight-patch-10-1-embers-of-neltharion-patch-notes-332645']" \
                                  "[@data-border='strong']"
ptr_10_1_overview_locator = "//a[contains(@class, 'data-env-link')][contains(@href, " \
                            "'dragonflight-patch-10-1-embers-of-neltharion-overview')][contains(text(), 'PTR')]"
ptr_10_1_overview_locator_css = "a.data-env-link[href*='dragonflight-patch-10-1-embers-of-neltharion-overview']" \
                                ":contains('PTR')"
