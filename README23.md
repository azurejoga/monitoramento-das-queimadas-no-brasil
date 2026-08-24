# Monitoramento de Queimadas na Amazônia

Este projeto tem como objetivo monitorar as queimadas na Amazônia e apresentar informações diárias atualizadas sobre os focos de incêndio detectados. Abaixo, você pode visualizar as queimadas mais recentes, com detalhes sobre localização, satélite que realizou a detecção, e outros fatores relevantes.

## Estrutura dos Dados

Cada entrada na tabela representa um foco de incêndio com as seguintes informações:

- **ID:** Identificador único do foco de incêndio.
- **Latitude/Longitude:** Coordenadas geográficas do foco detectado. Para visualizar o local exato, insira estas coordenadas no Google Maps ou outro aplicativo de mapas.
- **Data/Hora GMT:** Data e hora da detecção em formato GMT (Greenwich Mean Time).
- **Satélite:** Satélite responsável pela detecção do foco de incêndio.
- **Município, Estado e País:** Localização administrativa do foco detectado.
- **Dias sem Chuva:** Número de dias consecutivos sem precipitação na região, o que pode indicar um aumento no risco de incêndio.
- **Precipitação:** Quantidade de chuva (em milímetros) registrada no local.
- **Risco de Fogo:** Índice que indica a probabilidade de ocorrência de incêndio, baseado em fatores como condições climáticas e quantidade de combustível disponível.
- **Bioma:** Bioma onde o foco foi identificado, como Amazônia, Cerrado, ou Mata Atlântica.
- **FRP (Fire Radiative Power):** Potência radiativa do fogo, que mede a intensidade do incêndio. Focos com FRP mais alto indicam incêndios mais intensos.

## Visualização Gráfica

Se você deseja visualizar de forma gráfica onde as queimadas estão ocorrendo, copie as coordenadas de latitude e longitude mais recentes e cole no Google Maps. Isso permite uma compreensão espacial mais clara da distribuição dos focos de incêndio. Alternativamente, você também pode usar a descrição de localização (Município, Estado e País) para identificar a região afetada.

## Informação Adicional

As queimadas na Amazônia não apenas afetam a biodiversidade local, mas também têm implicações globais, contribuindo para o aquecimento global e a emissão de gases de efeito estufa. O monitoramento contínuo é essencial para entender e mitigar os impactos desses incêndios, além de auxiliar na gestão de políticas ambientais e ações de preservação.

## Dados Diários - Página 23

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| f6e7222f-8428-3037-94c3-153fee78efd6 | -12.11692 | -50.62171 | 2026-08-24 04:27:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 24.8 |
| 2e4f6517-6047-31b9-8985-14c37b29adff | -16.41632 | -51.84585 | 2026-08-24 04:27:00 | NPP-375D | PIRANHAS | GOIÁS | Brasil | 5217203 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| eed6abce-eadf-365d-8637-f7a1b885b462 | -16.05481 | -50.4516 | 2026-08-24 04:27:00 | NPP-375D | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 07fb680f-6192-3743-86f4-a741c33091ff | -12.71735 | -48.41071 | 2026-08-24 04:27:00 | NPP-375D | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 6a224b96-3e31-34ce-b103-d67fc9533d17 | -17.42513 | -48.8408 | 2026-08-24 04:27:00 | NPP-375D | PIRACANJUBA | GOIÁS | Brasil | 5217104 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 5e225627-a943-30fb-94f6-60b5a4c75db8 | -13.10493 | -43.34731 | 2026-08-24 04:27:00 | NPP-375D | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Caatinga | 1.2 |
| f24a54d4-b78d-34a1-b383-74ea6273f528 | -15.0279 | -48.68814 | 2026-08-24 04:27:00 | NPP-375D | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 1c108cdd-8ee1-36e1-9671-d3d536baba6d | -17.17972 | -44.43432 | 2026-08-24 04:27:00 | NPP-375D | JEQUITAÍ | MINAS GERAIS | Brasil | 3135605 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| b952453b-0f3f-30cb-bcb8-bc07fa0246ad | -15.26234 | -52.86432 | 2026-08-24 04:27:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 70438fe5-e834-3c68-af33-bc717346625c | -17.97006 | -44.46058 | 2026-08-24 04:27:00 | NPP-375D | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| ffd3aa91-9628-3597-97f0-0693bf121292 | -18.44825 | -48.41706 | 2026-08-24 04:27:00 | NPP-375D | ARAGUARI | MINAS GERAIS | Brasil | 3103504 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 0c401cbf-f2ca-3e86-ad35-255dcb191bb0 | -12.09544 | -50.61764 | 2026-08-24 04:27:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 99c3ee6c-1072-3e80-86a1-de02beba4b52 | -15.25867 | -52.8579 | 2026-08-24 04:27:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 10ec0ecf-007b-3b2c-8945-0c68468befc8 | -12.73795 | -46.46411 | 2026-08-24 04:27:00 | NPP-375D | AURORA DO TOCANTINS | TOCANTINS | Brasil | 1702703 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 43a079fc-f44f-37f9-af42-243bd9fa17cb | -15.40343 | -55.77746 | 2026-08-24 04:27:00 | NPP-375D | CHAPADA DOS GUIMARÃES | MATO GROSSO | Brasil | 5103007 | 51 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 0596b5b1-14d8-3ba0-b6f8-6f2232e3c228 | -15.34011 | -52.79577 | 2026-08-24 04:27:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| cf9697ce-ce03-37b8-a22b-b91d646f9058 | -14.40405 | -51.77815 | 2026-08-24 04:27:00 | NPP-375D | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 5ad56f69-f519-39a0-8761-1f0deb2d928c | -15.29568 | -52.81713 | 2026-08-24 04:27:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 70a7c5e4-897b-3951-aa21-9a3a00e1c223 | -16.42198 | -49.92381 | 2026-08-24 04:27:00 | NPP-375D | ANICUNS | GOIÁS | Brasil | 5201306 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 7148a341-8278-3607-a3f3-a74990e4a357 | -19.89773 | -43.87991 | 2026-08-24 04:27:00 | NPP-375D | SABARÁ | MINAS GERAIS | Brasil | 3156700 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| e314d544-8c6a-360e-a4d0-9228bda943af | -15.26965 | -52.85676 | 2026-08-24 04:27:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 972206d0-5776-3789-a5d6-8252a72be458 | -16.0607 | -50.44165 | 2026-08-24 04:27:00 | NPP-375D | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 2acd0af9-087c-3117-9e6d-aac257c790ca | -19.00025 | -44.70183 | 2026-08-24 04:27:00 | NPP-375D | CURVELO | MINAS GERAIS | Brasil | 3120904 | 31 | 33 | nan | nan | nan | Cerrado | 0.3 |
| da1c934b-1f51-35e1-84b3-769029ec2140 | -15.43968 | -52.84019 | 2026-08-24 04:27:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 20d62540-6091-30a2-bdf9-7c3a34e5decc | -18.70796 | -43.02961 | 2026-08-24 04:27:00 | NPP-375D | SABINÓPOLIS | MINAS GERAIS | Brasil | 3156809 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 04ef5219-f74f-3ce9-bb27-ea91ccf7b760 | -15.23325 | -52.78683 | 2026-08-24 04:27:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| eeb1ab47-b20e-39bd-9c67-2798a4d8e8a2 | -11.91718 | -55.90574 | 2026-08-24 04:27:00 | NPP-375D | IPIRANGA DO NORTE | MATO GROSSO | Brasil | 5104526 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 83727834-7b17-3ccf-9a07-14000a51035b | -15.26811 | -52.83984 | 2026-08-24 04:27:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 882ec7cc-84bd-3ba1-9313-14e0938e6ef4 | -17.67158 | -46.41535 | 2026-08-24 04:27:00 | NPP-375D | LAGOA GRANDE | MINAS GERAIS | Brasil | 3137536 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 06a2c436-56c4-3385-861d-308b8f7b7808 | -15.32207 | -49.22413 | 2026-08-24 04:27:00 | NPP-375D | GOIANÉSIA | GOIÁS | Brasil | 5208608 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| de712dbd-5ca0-352a-88d2-8401e046a314 | -17.42293 | -48.83855 | 2026-08-24 04:27:00 | NPP-375D | PIRACANJUBA | GOIÁS | Brasil | 5217104 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 5d40eecb-53b8-34bb-9a47-7d31e6b21909 | -14.40604 | -51.77937 | 2026-08-24 04:27:00 | NPP-375D | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 02f6b9f4-d543-389e-8a10-20c9cd1ef473 | -12.86418 | -48.483 | 2026-08-24 04:27:00 | NPP-375D | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 34bc3957-5fdd-336a-a66a-3a1504c22f1e | -12.75528 | -48.37425 | 2026-08-24 04:27:00 | NPP-375D | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 5c991ecf-2130-33e9-95cb-51e19ce434f3 | -17.77547 | -49.13165 | 2026-08-24 04:27:00 | NPP-375D | MORRINHOS | GOIÁS | Brasil | 5213806 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 52e8fbd0-83e5-3c8c-924c-32f3b2a9d9fa | -19.28272 | -42.34681 | 2026-08-24 04:27:00 | NPP-375D | BUGRE | MINAS GERAIS | Brasil | 3109253 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 0fae856a-f004-3e56-8e38-0def16d23a3b | -16.42667 | -49.91974 | 2026-08-24 04:27:00 | NPP-375D | ANICUNS | GOIÁS | Brasil | 5201306 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 2c228dc3-0fcd-3ebf-ab98-987fa9df303e | -13.26973 | -51.44523 | 2026-08-24 04:27:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 5dd49234-3399-3fc6-b787-7c01c3ce36e0 | -15.40909 | -55.77868 | 2026-08-24 04:27:00 | NPP-375D | CHAPADA DOS GUIMARÃES | MATO GROSSO | Brasil | 5103007 | 51 | 33 | nan | nan | nan | Cerrado | 6.0 |
| ff5e1e13-ee03-319f-ba70-9958d5e5a808 | -12.60991 | -52.45938 | 2026-08-24 04:27:00 | NPP-375D | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| c97f01b1-904d-3719-9e66-8187ed954bf6 | -14.40764 | -51.78356 | 2026-08-24 04:27:00 | NPP-375D | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 8f44246c-1cb3-3117-afab-cd24bcfd61ce | -16.06151 | -50.44404 | 2026-08-24 04:27:00 | NPP-375D | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 4.3 |
| f9340df5-0178-3aff-9342-07ea23cfa10c | -12.05846 | -50.57654 | 2026-08-24 04:27:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 40ccc695-f456-312f-a064-61df70ac8a49 | -18.52104 | -47.16848 | 2026-08-24 04:27:00 | NPP-375D | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 0.2 |
| 3d2e6f3f-beba-36da-bf02-3ae5b0b0dead | -15.26601 | -52.85047 | 2026-08-24 04:27:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 7.0 |
| bdde6075-2425-32e6-816d-a8847b2fb3c2 | -12.1055 | -50.611 | 2026-08-24 04:27:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 6.9 |
| fce56780-a8a3-35b2-be35-5e6d6fc458af | -15.30138 | -52.81963 | 2026-08-24 04:27:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 5.4 |
| b4fe6876-e5dc-377c-85c1-4447680fcc5d | -15.26737 | -52.83788 | 2026-08-24 04:27:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 06a8cf8f-708d-3632-bf16-d17e2ccee30c | -12.89304 | -48.49384 | 2026-08-24 04:27:00 | NPP-375D | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| f934af14-8e13-3e7c-9ad2-1bf065b005f8 | -14.3454 | -51.75785 | 2026-08-24 04:27:00 | NPP-375D | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 7023e2a7-4b67-354a-a4db-d21e2932f21b | -15.27808 | -52.81412 | 2026-08-24 04:27:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 635a328b-a90e-382f-ae0e-8687659f06df | -13.27585 | -51.43718 | 2026-08-24 04:27:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| f90b453e-ab5d-36a5-922f-79449accf53e | -15.03157 | -48.68874 | 2026-08-24 04:27:00 | NPP-375D | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| baeadc3a-64a3-31e0-bd05-600012f201d2 | -15.2676 | -52.86716 | 2026-08-24 04:27:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| e63d0e2e-e03a-3168-885d-f7f1f609441d | -14.79206 | -48.77556 | 2026-08-24 04:27:00 | NPP-375D | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 8abe0732-fd20-3dcc-98c1-b99fe5e47800 | -15.26918 | -52.83442 | 2026-08-24 04:27:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 5dc445d7-de4d-3b03-919e-30d05572b923 | -16.05169 | -50.42299 | 2026-08-24 04:27:00 | NPP-375D | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 40181814-f634-3529-8bb0-ae2cf74684c4 | -15.27231 | -52.86808 | 2026-08-24 04:27:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| e918ac15-e62c-3d72-a6da-75c57af2c7ee | -14.7773 | -48.77295 | 2026-08-24 04:27:00 | NPP-375D | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c1bf9a4b-46d3-373c-9809-29426a5cba79 | -16.38835 | -51.82797 | 2026-08-24 04:27:00 | NPP-375D | PIRANHAS | GOIÁS | Brasil | 5217203 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 55a477ca-3b95-3d5b-86cf-11dde5a14d7a | -15.29662 | -52.81904 | 2026-08-24 04:27:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| a086faff-4c61-33bc-abc6-62e93f4a10e9 | -12.71894 | -48.40132 | 2026-08-24 04:27:00 | NPP-375D | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| cc77b7ae-bd3f-33df-9bf0-4568d3cb088d | -16.41203 | -51.84487 | 2026-08-24 04:27:00 | NPP-375D | PIRANHAS | GOIÁS | Brasil | 5217203 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| ef267b15-4b64-30c1-a60d-6ca89f655a4f | -15.2715 | -52.81608 | 2026-08-24 04:27:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 44e243b4-8378-3685-a32b-c35b5f1c67c1 | -14.98292 | -52.68474 | 2026-08-24 04:27:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 15591558-810b-3f96-95f7-9c1445211576 | -14.78837 | -48.77486 | 2026-08-24 04:27:00 | NPP-375D | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 402d608e-4756-3f09-9e5c-daae30bebbd9 | -15.44336 | -52.84634 | 2026-08-24 04:27:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 5823f65d-263e-3216-b9da-3cfa50b6b230 | -16.02465 | -45.52369 | 2026-08-24 04:27:00 | NPP-375D | URUCUIA | MINAS GERAIS | Brasil | 3170529 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 1347255b-86df-3c35-b0b8-3bee4fe29712 | -13.09309 | -43.35671 | 2026-08-24 04:27:00 | NPP-375D | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 9a51fbd4-1ae4-33ae-aacc-7f001201d6f2 | -14.44155 | -51.79973 | 2026-08-24 04:27:00 | NPP-375D | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ddb88a4c-9b76-30a8-947b-82baa21532a8 | -12.09114 | -50.61682 | 2026-08-24 04:27:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| a11714ae-3e03-3d59-ad80-4e4ee9899e29 | -14.79716 | -48.78999 | 2026-08-24 04:27:00 | NPP-375D | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| c726e314-d802-313c-b9d7-3fad1c609720 | -12.74328 | -46.45319 | 2026-08-24 04:27:00 | NPP-375D | AURORA DO TOCANTINS | TOCANTINS | Brasil | 1702703 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 234f40c6-7319-368c-9e61-0b0e28143daf | -14.78097 | -48.77367 | 2026-08-24 04:27:00 | NPP-375D | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 3.7 |
| b1fb23f8-1450-3693-8c64-c5fd0f7a18bf | -12.75072 | -46.45067 | 2026-08-24 04:27:00 | NPP-375D | AURORA DO TOCANTINS | TOCANTINS | Brasil | 1702703 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 8e886fb5-dbb1-37bd-b1c3-8bc44e87cadd | -12.0635 | -50.57323 | 2026-08-24 04:27:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 5ff331ad-a351-3da7-b2ea-c9e4801e65d2 | -15.97434 | -40.28061 | 2026-08-24 04:27:00 | NPP-375D | JORDÂNIA | MINAS GERAIS | Brasil | 3136504 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 52aae461-d805-3433-9073-85cfc89464f9 | -17.83199 | -44.47725 | 2026-08-24 04:27:00 | NPP-375D | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 287b79fc-fb46-337a-8686-74fc812f2758 | -16.41139 | -49.91651 | 2026-08-24 04:27:00 | NPP-375D | ANICUNS | GOIÁS | Brasil | 5201306 | 52 | 33 | nan | nan | nan | Cerrado | 3.9 |
| fae51d9e-3943-330e-a614-34e586c27ea5 | -13.27854 | -51.43553 | 2026-08-24 04:27:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 5309f1eb-e0d2-301f-8a85-efac2e77a194 | -16.39428 | -51.82029 | 2026-08-24 04:27:00 | NPP-375D | PIRANHAS | GOIÁS | Brasil | 5217203 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 96d7f8b0-ad16-3c58-a345-85ec2a93d910 | -15.27174 | -52.86631 | 2026-08-24 04:27:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 28126277-d480-3ef8-a850-0bb0c9837b90 | -15.27714 | -52.81207 | 2026-08-24 04:27:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 3.6 |
| a3ad599a-32d0-3dfb-8e7d-e90792e75eb1 | -12.11418 | -50.62043 | 2026-08-24 04:27:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 35.6 |
| 3a28d7b9-2c92-383f-85e9-16f3836bf5d8 | -16.41817 | -49.9229 | 2026-08-24 04:27:00 | NPP-375D | ANICUNS | GOIÁS | Brasil | 5201306 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 4b516407-7c16-3104-bbe1-363042c5ef37 | -12.11494 | -50.6163 | 2026-08-24 04:27:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 35.6 |
| 31e0469a-cfe8-373e-a011-76c40bc53970 | -17.42019 | -48.82659 | 2026-08-24 04:27:00 | NPP-375D | PIRACANJUBA | GOIÁS | Brasil | 5217104 | 52 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 9acfde60-7da1-34b2-83e3-c2115ece36da | -15.2864 | -52.81465 | 2026-08-24 04:27:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 9.8 |
| fe5f71c3-be6b-37d4-925a-47c58114b1f5 | -15.58366 | -56.00711 | 2026-08-24 04:27:00 | NPP-375D | CUIABÁ | MATO GROSSO | Brasil | 5103403 | 51 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 259f66d5-b00d-38e8-a6f4-cf1fdb767e3b | -17.43723 | -48.84125 | 2026-08-24 04:27:00 | NPP-375D | PIRACANJUBA | GOIÁS | Brasil | 5217104 | 52 | 33 | nan | nan | nan | Cerrado | 34.1 |
| 69826c56-2e7f-32ba-8d25-baaa13c8af92 | -18.65243 | -43.19044 | 2026-08-24 04:27:00 | NPP-375D | SABINÓPOLIS | MINAS GERAIS | Brasil | 3156809 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 9365948e-f3a0-3077-a6f6-4b86764fbd73 | -19.04589 | -45.00239 | 2026-08-24 04:27:00 | NPP-375D | POMPÉU | MINAS GERAIS | Brasil | 3152006 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 7e0711d3-7b23-3b8a-900a-cd7f3ad7b4f5 | -16.04676 | -50.42755 | 2026-08-24 04:27:00 | NPP-375D | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 85c66eb1-8999-39b1-a9d1-57e26ff86370 | -13.45083 | -43.84196 | 2026-08-24 04:27:00 | NPP-375D | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| a47a6875-8829-3f10-a0d7-4f4579045366 | -15.51303 | -49.83944 | 2026-08-24 04:27:00 | NPP-375D | CARMO DO RIO VERDE | GOIÁS | Brasil | 5205000 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 5fc0912d-fdee-36a4-8997-5bdd534e3828 | -12.11765 | -50.61758 | 2026-08-24 04:27:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 24.8 |
| 3bcef141-6c8b-3bc7-8843-c8c75f9118f5 | -13.16424 | -51.39204 | 2026-08-24 04:27:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 8f549718-b908-38f1-9ae3-d2edd2c163b4 | -15.22752 | -52.7913 | 2026-08-24 04:27:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| a26014c6-1e87-3610-8486-a5d53752be66 | -17.5439 | -42.53966 | 2026-08-24 04:27:00 | NPP-375D | CAPELINHA | MINAS GERAIS | Brasil | 3112307 | 31 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 22e87f76-5a24-39ed-9fd5-48c80014c363 | -16.19933 | -57.76575 | 2026-08-24 04:27:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.5 |


[Clique aqui para ver as próximas entradas](README24.md)
