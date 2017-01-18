% include("header.tpl", title="Search Results")

% for proj in results.iterkeys():
    % if len(results[proj]) > 0:
        <div class="panel panel-default">
            <div class="panel-heading">
                <h3 class="panel-title">Results for Project {{proj}}</h3>
            </div>
            <div class="panel-body">
                <table class="table table-striped table-bordered">
                    <tr>
                        <th>Name</th>
                        <th>Submitted</th>
                        <th>Sender</th>
                        <th>MD5</th>
                        <th>Tags</th>
                    </tr>
                    % for res in results[proj]:
                        <tr>
                            <td><a href="/file/{{proj}}/{{res[3]}}">{{res[0]}}</a></td>
                            <td>{{res[1]}}</td>
                            <td>
                              <% for text in res[2]:
                                     try:
                                         txt = text.title.split('|')[2]
                                         txt = txt.split('<')[1]
                                         txt = str(txt.split('>')[0])
                                     except:
                                         txt = text.title
                                     end
                              %>
                              {{txt}}
                              % end
                            </td>
                            <td>{{res[4]}}</td>
                            <td>
                            % for tags in res[5]:
                            {{tags.tag}},
                            % end
                            </td>
                        </tr>
                    % end
                </table>
            </div>
        </div>
    % end
% end

% include("footer.tpl")
