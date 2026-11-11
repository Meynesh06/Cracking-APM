import { exportToSvg, convertToExcalidrawElements } from "@excalidraw/excalidraw";
window.renderScene = async (skeleton) => {
  await document.fonts.load("20px Excalifont"); await document.fonts.load("20px Cascadia");
  const elements = convertToExcalidrawElements(skeleton, { regenerateIds: false });
  const svg = await exportToSvg({
    elements,
    appState: { exportBackground: false, exportWithDarkMode: false, exportPadding: 18, exportEmbedScene: false },
    files: null,
  });
  return { svg: svg.outerHTML, elements };
};
window.__ready = true;
