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

## Dados Diários - Página 24

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 978b7253-345d-31f4-8e17-6cea5723e0d2 | -11.21327 | -54.91576 | 2026-08-05 05:23:00 | NPP-375D | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 77ae73af-452b-3627-ab69-bc73610192b2 | -6.61682 | -56.36604 | 2026-08-05 05:23:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 9f1e6277-210a-37aa-801d-c1f795350657 | -7.50499 | -49.7438 | 2026-08-05 05:23:00 | NPP-375D | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 98e0a285-33be-31b7-b926-2fe618fb03a9 | -11.1985 | -54.88607 | 2026-08-05 05:23:00 | NPP-375D | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f6f200a0-7fab-3d88-82cd-e5f88468fda7 | -6.72185 | -58.94613 | 2026-08-05 05:23:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7cfa9ab7-d568-3c5c-b590-2a429df6d03b | -11.19218 | -54.90349 | 2026-08-05 05:23:00 | NPP-375D | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 50242631-b32c-3431-8986-a668491173b4 | -12.58648 | -46.94836 | 2026-08-05 05:25:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 297ceafe-6d34-320a-85fc-3410dbaabe1c | -12.4551 | -50.37291 | 2026-08-05 05:25:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f7f605a3-aa2e-3e9a-8dad-63ce8fcbe628 | -12.20694 | -52.86704 | 2026-08-05 05:25:00 | NPP-375D | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 884baa6f-4d65-3215-821f-b5388e864355 | -12.59238 | -46.95339 | 2026-08-05 05:25:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 11.0 |
| 2037df71-1a0e-3d91-a957-480004dbd330 | -12.44885 | -50.38139 | 2026-08-05 05:25:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 733a8d08-2bef-3037-8f18-51e430f25147 | -13.25007 | -54.27143 | 2026-08-05 05:25:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7e7a4394-81ca-3dd3-aed5-dd6acf257b40 | -11.9159 | -55.9126 | 2026-08-05 05:25:00 | NPP-375D | IPIRANGA DO NORTE | MATO GROSSO | Brasil | 5104526 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| ea36140a-bd02-3702-9f55-c9ee0178848b | -12.32259 | -53.1766 | 2026-08-05 05:25:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 242038f1-eee6-32f2-8c68-093375e7e741 | -12.43706 | -50.51775 | 2026-08-05 05:25:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d2f6f17d-dcf5-3102-8303-77fa1c6ee751 | -11.9165 | -55.90848 | 2026-08-05 05:25:00 | NPP-375D | IPIRANGA DO NORTE | MATO GROSSO | Brasil | 5104526 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 8ccfbbc7-e3ba-3656-a387-69d3e4de5205 | -11.33923 | -62.21422 | 2026-08-05 05:25:00 | NPP-375D | ALVORADA D'OESTE | RONDÔNIA | Brasil | 1100346 | 11 | 33 | nan | nan | nan | Amazônia | 2.3 |
| aee8419f-c5ef-3e9f-99d2-1ca8f43bdfe5 | -12.59739 | -46.90977 | 2026-08-05 05:25:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| a94b5362-bf80-3788-9378-7909c0da3cb2 | -12.48464 | -50.38619 | 2026-08-05 05:25:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e3853eb2-8e33-3ba1-9b1e-60bfa26d435b | -20.44506 | -53.77499 | 2026-08-05 05:25:00 | NPP-375D | RIBAS DO RIO PARDO | MATO GROSSO DO SUL | Brasil | 5007109 | 50 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 4e441256-85f0-376c-ae9a-df50bdbe66f7 | -12.20845 | -52.86984 | 2026-08-05 05:25:00 | NPP-375D | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 83c75cd4-ec2b-3425-baed-5c7112deda2a | -11.24752 | -54.83781 | 2026-08-05 05:25:00 | NPP-375D | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b2b2f023-96c7-3bc0-8d10-373b1747b7a3 | -12.49344 | -45.54337 | 2026-08-05 05:25:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 31ac92f6-1927-3847-8cc6-9c000e09ea8e | -13.2468 | -54.26571 | 2026-08-05 05:25:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 509dfdba-7383-3efa-adcb-2dae0b5638e8 | -12.43669 | -50.52073 | 2026-08-05 05:25:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 875485eb-56cb-3350-8d7c-0c7b96039f41 | -11.92723 | -55.91004 | 2026-08-05 05:25:00 | NPP-375D | IPIRANGA DO NORTE | MATO GROSSO | Brasil | 5104526 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 550e5a71-d081-346a-8344-7e319e36b501 | -12.57957 | -46.95203 | 2026-08-05 05:25:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 38ad9af8-b237-3ec9-ad67-6b7b22ab7284 | -14.26222 | -45.29696 | 2026-08-05 05:25:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 495408d6-2668-3b04-9d21-33f76ffbfc27 | -12.32206 | -53.18054 | 2026-08-05 05:25:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| f8f1702c-8296-32d5-8cfc-8f3ef0a535ae | -11.34216 | -62.21926 | 2026-08-05 05:25:00 | NPP-375D | ALVORADA D'OESTE | RONDÔNIA | Brasil | 1100346 | 11 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 105e2d50-7cfb-36eb-9fa1-e7832c96d7bb | -12.58012 | -46.94724 | 2026-08-05 05:25:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| d0b287af-ef0e-3095-8c2d-b8576d4fed36 | -12.1709 | -59.75449 | 2026-08-05 05:25:00 | NPP-375D | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 001f0ee3-23c0-341d-8f88-d1bf2a96e22f | -12.58708 | -46.94304 | 2026-08-05 05:25:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 476eeb71-3c2e-3206-98aa-098a4084615e | -13.25478 | -54.26678 | 2026-08-05 05:25:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| c6c937d3-3857-36cd-a516-e7980ce8350c | -12.59298 | -46.94822 | 2026-08-05 05:25:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 0e1d0348-038f-3795-ad1b-9976bc492bd9 | -10.81645 | -65.08994 | 2026-08-05 05:25:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 75f104da-ecfa-34fe-80c0-62ec53cfaba0 | -11.92425 | -55.90541 | 2026-08-05 05:25:00 | NPP-375D | IPIRANGA DO NORTE | MATO GROSSO | Brasil | 5104526 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a585e9b2-3d07-3c49-a2e1-f0fcff1a09ba | -10.8201 | -65.09521 | 2026-08-05 05:25:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.1 |
| fddcb8b9-80b7-368e-9b2a-447ad0b90eb7 | -18.84523 | -47.92212 | 2026-08-05 05:25:00 | NPP-375D | INDIANÓPOLIS | MINAS GERAIS | Brasil | 3130705 | 31 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 9a203aff-0da8-3d0f-b2c7-d9d08795276e | -20.39034 | -49.30874 | 2026-08-05 05:25:00 | NPP-375D | NOVA GRANADA | SÃO PAULO | Brasil | 3533007 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 653f9ac4-7dff-397f-8dc0-846f9df1ffef | -11.91091 | -57.41185 | 2026-08-05 05:25:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 070cb0c4-6e59-309d-b726-5e842db9b456 | -12.58847 | -46.93092 | 2026-08-05 05:25:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| bdcb1cff-c017-3080-a850-8a3f04feb7df | -20.38565 | -49.30916 | 2026-08-05 05:25:00 | NPP-375D | NOVA GRANADA | SÃO PAULO | Brasil | 3533007 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.3 |
| 464c0d0f-c5a0-35e7-9b01-7b8dfcf8e25c | -12.59677 | -46.91521 | 2026-08-05 05:25:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 80a39f79-cccd-3593-a9ba-cf292cd6a1be | -11.92365 | -55.90953 | 2026-08-05 05:25:00 | NPP-375D | IPIRANGA DO NORTE | MATO GROSSO | Brasil | 5104526 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b03e8d56-10bf-3efd-a035-49f36a1a64aa | -12.43781 | -50.5118 | 2026-08-05 05:25:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 1cf63da2-a492-3056-8c60-a73677a8e978 | -12.88247 | -52.83242 | 2026-08-05 05:25:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| bb57fc43-bbde-3551-bc0d-f149965fc7f5 | -12.31838 | -53.176 | 2026-08-05 05:25:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 7e021be9-e553-3eef-96f9-3d07a81a87d7 | -12.44961 | -50.37528 | 2026-08-05 05:25:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 911d7182-c80c-36fc-a680-fd424d769884 | -12.59354 | -46.94332 | 2026-08-05 05:25:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 7d9fef5e-e1d7-3f43-8469-8f1b26ee6612 | -12.58772 | -46.9375 | 2026-08-05 05:25:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 28762723-534b-3a5f-8585-5d981bc8a49c | -12.13956 | -48.26207 | 2026-08-05 05:25:00 | NPP-375D | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 627d20d7-8ad9-3c4e-a32d-2644a53538a5 | -18.84619 | -47.91719 | 2026-08-05 05:25:00 | NPP-375D | INDIANÓPOLIS | MINAS GERAIS | Brasil | 3130705 | 31 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 3f2a4681-6fb8-36c7-b2b9-9c891537ad4a | -12.59544 | -46.92678 | 2026-08-05 05:25:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 2f01ce4b-dbe6-3f0f-84b2-f07123f2c8f7 | -12.59613 | -46.92076 | 2026-08-05 05:25:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 78a9fc50-798f-3c4f-86e1-cef1732ea321 | -12.58977 | -46.91953 | 2026-08-05 05:25:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| a26853c9-318a-313a-b3d0-cfaa3ca93bdd | -13.24608 | -54.27089 | 2026-08-05 05:25:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 7efca856-cf5f-31f8-8972-37197eaee71a | -10.82088 | -65.0908 | 2026-08-05 05:25:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1cf3bed6-d002-3628-956c-52a9943a8fad | -14.23301 | -48.51488 | 2026-08-05 05:25:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 3819fdd1-0a9c-38cd-980f-50c0569ae74c | -20.38429 | -49.30801 | 2026-08-05 05:25:00 | NPP-375D | NOVA GRANADA | SÃO PAULO | Brasil | 3533007 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| 44829fae-aac3-3194-8f05-d4724958acc3 | -12.60106 | -46.93436 | 2026-08-05 05:25:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 84180743-c518-3b03-90ee-20e2fca1c00e | -21.29715 | -49.04651 | 2026-08-05 05:25:00 | NPP-375D | ITAJOBI | SÃO PAULO | Brasil | 3521903 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 7c27bcb0-6878-39fd-abbc-76cd8873315a | -10.82314 | -65.09494 | 2026-08-05 05:25:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 08abe7b9-7127-3bc0-94d6-58d80643e165 | -12.17032 | -59.75808 | 2026-08-05 05:25:00 | NPP-375D | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 8ae59e57-aac3-3f62-9a32-8932f174b737 | -11.2526 | -54.82923 | 2026-08-05 05:25:00 | NPP-375D | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d57c154a-4eb8-3a43-a7fb-d464eb280ac2 | -11.71546 | -56.8851 | 2026-08-05 05:25:00 | NPP-375D | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 8a76d640-c4bd-3523-aab5-4aa4ba271adf | -9.95457 | -67.19923 | 2026-08-05 05:25:00 | NPP-375D | SENADOR GUIOMARD | ACRE | Brasil | 1200450 | 12 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b56a44cb-0b3f-301c-baab-4e5e0fadd643 | -12.87812 | -52.83181 | 2026-08-05 05:25:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| db402e05-ec21-335b-abbf-336762675612 | -12.47991 | -50.38246 | 2026-08-05 05:25:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 65afa676-de76-3b35-a845-d172d22ce45b | -10.81428 | -65.09322 | 2026-08-05 05:25:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 14124d20-31d2-3145-8d22-3857a5e15410 | -12.31784 | -53.17993 | 2026-08-05 05:25:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| e5214be1-0f38-371c-8b3e-07d1e2d8b720 | -12.59407 | -46.93872 | 2026-08-05 05:25:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 385bd21c-beb9-384b-83a8-55b79fa04f17 | -12.4922 | -45.54148 | 2026-08-05 05:25:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 271c8190-f5e3-3209-ae82-42f9073d5857 | -13.25079 | -54.26624 | 2026-08-05 05:25:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| f3aee793-668b-3bca-970f-7df8b6b2a936 | -11.34291 | -62.21486 | 2026-08-05 05:25:00 | NPP-375D | ALVORADA D'OESTE | RONDÔNIA | Brasil | 1100346 | 11 | 33 | nan | nan | nan | Amazônia | 3.7 |
| db001958-d089-340b-9297-357513c02969 | -18.84569 | -47.92277 | 2026-08-05 05:25:00 | NPP-375D | INDIANÓPOLIS | MINAS GERAIS | Brasil | 3130705 | 31 | 33 | nan | nan | nan | Cerrado | 2.8 |
| fc18b621-c730-3f86-b11e-3b5f39294d5a | -12.59473 | -46.93292 | 2026-08-05 05:25:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 51d01d35-70c5-3bcd-a536-8f338dd36d33 | -12.58588 | -46.95353 | 2026-08-05 05:25:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 11.0 |
| 6bf27e97-75f5-364a-a8d3-01fb0078eb5e | -12.14493 | -48.26682 | 2026-08-05 05:25:00 | NPP-375D | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b507a22a-e3b9-3846-98c1-93e7372ade32 | -10.81509 | -65.08883 | 2026-08-05 05:25:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 8d253461-c12f-3f1f-8999-2ad469216253 | -18.84577 | -47.91651 | 2026-08-05 05:25:00 | NPP-375D | INDIANÓPOLIS | MINAS GERAIS | Brasil | 3130705 | 31 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 9669d61f-40f4-3349-914c-2c4f69d6dfcf | -12.45472 | -50.37597 | 2026-08-05 05:25:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| caf7c7df-2ca5-34f7-9bac-3961379d6fa9 | -12.43743 | -50.51477 | 2026-08-05 05:25:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| decc7de3-d693-3b94-84b4-9fd230ef505a | -12.44923 | -50.37833 | 2026-08-05 05:25:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 291bc38e-7db1-3fbb-a32a-b8387b0cae09 | -9.96891 | -64.94022 | 2026-08-05 05:25:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ebe55f5e-b461-35a6-9e4c-55d390546524 | -11.92007 | -55.90901 | 2026-08-05 05:25:00 | NPP-375D | IPIRANGA DO NORTE | MATO GROSSO | Brasil | 5104526 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| ebadc3d3-dc45-3464-af50-c8e155e2a436 | -12.20636 | -52.87116 | 2026-08-05 05:25:00 | NPP-375D | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 77edb571-823a-32d0-9291-2e61ca600f03 | -10.81952 | -65.08968 | 2026-08-05 05:25:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| bd750f2e-0e38-3e6d-b5cf-94e918fd69f8 | -11.25194 | -54.83381 | 2026-08-05 05:25:00 | NPP-375D | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5ef42135-1172-393f-b055-ab10fe1dd5fa | -12.5947 | -46.9301 | 2026-08-05 05:30:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 59.7 |
| 5cb6f931-cf53-3dd3-a56e-aed1d65b2156 | -12.5942 | -46.9527 | 2026-08-05 05:30:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 78.9 |
| b3e1b9be-af94-3a54-a288-909b5c51ce91 | -11.1642 | -54.9007 | 2026-08-05 05:30:00 | GOES-19 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 50.1 |
| 83a0b482-55a9-35c6-9fdc-f34c625ff172 | -11.183 | -54.8991 | 2026-08-05 05:30:00 | GOES-19 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 69.9 |
| 9c42b749-497f-3973-acfa-4a0183e3bf56 | -11.1828 | -54.9194 | 2026-08-05 05:30:00 | GOES-19 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 59.1 |
| ad8988fb-150f-3401-9c23-fb139698c429 | 4.42017 | -60.54312 | 2026-08-05 05:38:00 | NOAA-20 | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |
| bdf834a1-9ccf-3b7e-a1fd-cf0b4023d1d9 | -11.1642 | -54.9007 | 2026-08-05 05:40:00 | GOES-19 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 48.2 |
| b06671a1-0c80-3aec-a975-a3bf49b3d1dd | -12.5942 | -46.9527 | 2026-08-05 05:40:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 57.4 |
| 316a4131-7a51-3aa4-bf04-8a7e3fd028cb | -11.1828 | -54.9194 | 2026-08-05 05:40:00 | GOES-19 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 62.7 |
| 507a2dcf-01c6-344b-ad57-cfa9bb977c08 | -11.183 | -54.8991 | 2026-08-05 05:40:00 | GOES-19 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 67.2 |
| e3744eb0-da5a-3f1a-a409-cf43f3c3f070 | -6.5513 | -55.16693 | 2026-08-05 05:40:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |


[Clique aqui para ver as próximas entradas](README25.md)
