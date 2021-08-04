import { JupyterFrontEnd, JupyterFrontEndPlugin, ILayoutRestorer } from '@jupyterlab/application';
import { ILauncher } from '@jupyterlab/launcher';
import { PageConfig } from '@jupyterlab/coreutils';
import { IFrame, MainAreaWidget, WidgetTracker } from '@jupyterlab/apputils';

import '../style/index.css';

function newRSessionProxyWidget(id: string, url: string, text: string): MainAreaWidget<IFrame> {
  const content = new IFrame({
    sandbox: ['allow-same-origin', 'allow-scripts', 'allow-popups', 'allow-forms'],
  });
  content.title.label = "RStudio";
  content.title.closable = true;
  content.url = url;
  content.addClass('jp-RSessionProxy');
  content.id = id;
  const widget = new MainAreaWidget({ content });
  widget.addClass('jp-RSessionProxy');
  return widget;
}

async function activate(app: JupyterFrontEnd, launcher: ILauncher, restorer: ILayoutRestorer) : Promise<void> {
  const { commands, shell } = app;

  const namespace = 'rsession-proxy';
  const tracker = new WidgetTracker<MainAreaWidget<IFrame>>({
    namespace
  });
  const command = namespace + ':' + 'open';

  if (restorer) {
    void restorer.restore(tracker, {
      command: command,
      args: widget => ({
        url: widget.content.url,
        title: widget.content.title.label,
        newBrowserTab: false,
        id: widget.content.id
      }),
      name: widget => widget.content.id
    });
  }

  commands.addCommand(command, {
    label: args => args['title'] as string,
    execute: args => {
      const id = args['id'] as string;
      const title = args['title'] as string;
      const url = args['url'] as string;
      const newBrowserTab = args['newBrowserTab'] as boolean;
      if (newBrowserTab) {
        window.open(url, '_blank');
        return;
      }
      let widget = tracker.find((widget) => { return widget.content.id == id; });
      if(!widget){
        widget = newRSessionProxyWidget(id, url, title);
      }
      if (!tracker.has(widget)) {
        void tracker.add(widget);
      }
      if (!widget.isAttached) {
        shell.add(widget);
        return widget;
      } else {
        shell.activateById(widget.id);
      }
    }
  });

  const url = PageConfig.getBaseUrl() + 'rstudio/';
  const title = 'RStudio';
  const newBrowserTab = true;
  const id = namespace + ':' + 'RStudio';
  const icon_url = PageConfig.getBaseUrl() + 'rsession-proxy/icon/rstudio';
  const launcher_item : ILauncher.IItemOptions = {
    command: command,
    args: {
      url: url,
      title: title + ' [↗]',
      newBrowserTab: newBrowserTab,
      id: id,
    },
    kernelIconUrl: icon_url,
    category: 'Notebook'
  };

  launcher.add(launcher_item);
}

/**
 * Initialization data for the jupyterlab-rsession-proxy extension.
 */
const extension: JupyterFrontEndPlugin<void> = {
  id: 'jupyterlab-rsession-proxy',
  autoStart: true,
  requires: [ILauncher, ILayoutRestorer],
  activate: activate
};

export default extension;
