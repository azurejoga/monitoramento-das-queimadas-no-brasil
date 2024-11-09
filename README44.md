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

## Dados Diários - Página 44

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 29dbdb2c-498b-3ccd-967f-ea57724f2014 | -4.22599 | -50.64458 | 2024-11-09 04:33:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| eeaa6f3e-63d8-3ffe-91ef-c4aeb4cc27b0 | -3.19153 | -50.58717 | 2024-11-09 04:33:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 2c1fdfab-ff89-35be-a978-343587b705a5 | -2.81285 | -52.96409 | 2024-11-09 04:33:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 378d1c5e-3947-3188-8646-639fcf2ec287 | -3.51085 | -51.67502 | 2024-11-09 04:33:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 48802c4e-d374-3c68-94f8-6e2664d9c942 | -4.49743 | -48.49165 | 2024-11-09 04:33:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| c3e3a50f-8e80-3c46-ae04-20e9a1542903 | -3.97286 | -48.12698 | 2024-11-09 04:33:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 64d7042e-d26b-333e-8366-b759cde24874 | -3.25074 | -46.47488 | 2024-11-09 04:33:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b3a1f433-23b1-38c7-a616-0910be1e03e9 | -4.06341 | -48.3091 | 2024-11-09 04:33:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 90ac4368-7d3a-3567-868b-3ea6dcfa3093 | -4.01697 | -48.30129 | 2024-11-09 04:33:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 8da14ce4-3acc-3818-b7b4-6f5a60e9c61f | -3.58658 | -47.35722 | 2024-11-09 04:33:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 65b4c0be-26c1-3aa0-a4b1-1a17c1460b71 | -3.03065 | -50.37112 | 2024-11-09 04:33:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| c5077824-c358-3aa1-bd96-3adb247eedc5 | -3.76693 | -51.37991 | 2024-11-09 04:33:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 3b476291-efc0-3f88-bae7-b5f309791b2b | -4.72949 | -48.98094 | 2024-11-09 04:33:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 0cf8aae8-4fc8-327a-9431-303d194fa507 | -3.23894 | -50.26761 | 2024-11-09 04:33:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 8.3 |
| 6cb8cab7-964b-3198-a6a0-ef0c21c419ed | -4.6089 | -45.98391 | 2024-11-09 04:33:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 2a93265a-a972-3a0d-b966-12455aad0345 | -5.45087 | -43.28521 | 2024-11-09 04:33:00 | NOAA-21 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| c68fcaab-153a-36a2-91ec-e300e12cdd86 | -3.02273 | -47.96008 | 2024-11-09 04:33:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 49dc4414-2fbd-3d27-b59d-be914f91f780 | -3.09435 | -51.29012 | 2024-11-09 04:33:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 407be825-97a2-3e01-aafe-c23640cac0a1 | -4.51385 | -48.0175 | 2024-11-09 04:33:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 89b8728e-0520-3e56-bd59-8babd5c1d088 | -5.84005 | -46.24035 | 2024-11-09 04:33:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| ff8c7771-8855-3b50-b836-22500ed1b3fe | -6.42031 | -44.0526 | 2024-11-09 04:33:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 7ad62e0a-84f1-369c-97bd-64be6f5a4d4a | -2.96188 | -48.02176 | 2024-11-09 04:33:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6a30f3c3-4ab3-378b-9318-3bb0df83e988 | -3.821 | -46.45985 | 2024-11-09 04:33:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a9ec4bb6-0e15-3ce5-845f-6c1bd81a9e06 | -2.80861 | -49.87134 | 2024-11-09 04:33:00 | NOAA-21 | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| c9e07ee0-a9c2-3e0e-bc3d-349a15478929 | -4.05668 | -48.24326 | 2024-11-09 04:33:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 428b95cf-dcba-35b8-915e-46d022655be7 | -3.50086 | -51.02524 | 2024-11-09 04:33:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 9891b02e-5945-3921-a6c9-f2733a1b235c | -3.6365 | -50.18673 | 2024-11-09 04:33:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 37c241d2-93ba-34a1-8221-b6fe98652b0c | -2.82953 | -49.10949 | 2024-11-09 04:33:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 2eb489ee-43e2-34bc-8d01-345859de5d51 | -4.2238 | -48.61059 | 2024-11-09 04:33:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 583d3ef7-9345-38be-ae79-cc749b7856ba | -2.94315 | -49.50314 | 2024-11-09 04:33:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 11697835-4b67-305b-90d9-ae49e0c5b363 | -4.12697 | -46.85624 | 2024-11-09 04:33:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e533661b-dca6-32d7-96b3-737dff9908b4 | -2.62351 | -51.29617 | 2024-11-09 04:33:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 691bec85-1ec6-3399-88bb-2b0bbeaac76c | -5.37477 | -48.4304 | 2024-11-09 04:33:00 | NOAA-21 | ARAGUATINS | TOCANTINS | Brasil | 1702208 | 17 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 573a43c8-f088-3d66-8901-8c5b12b65ea3 | -4.58609 | -48.05709 | 2024-11-09 04:33:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4b4cd765-eec0-3e4f-b675-8b3d97a8b1be | -5.2583 | -45.45927 | 2024-11-09 04:33:00 | NOAA-21 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 3aedde94-5db3-3bef-a087-80cf688659f0 | -3.35217 | -50.26325 | 2024-11-09 04:33:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| f9eca02d-4d3e-31e3-905e-9de29e75cd2e | -2.64531 | -49.89554 | 2024-11-09 04:33:00 | NOAA-21 | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 9023c9f0-e7c1-3009-97f2-2605462e6b49 | -3.11898 | -51.11181 | 2024-11-09 04:33:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b6c7c2cf-006a-3ef0-a152-f126aee31d86 | -4.11976 | -51.06834 | 2024-11-09 04:33:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 8ac90cfe-3a77-32e4-81b4-e1a52192337c | -3.21701 | -50.38168 | 2024-11-09 04:33:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 3249b7fd-a6f0-313d-9e0e-111f9da3a104 | -5.20332 | -47.45969 | 2024-11-09 04:33:00 | NOAA-21 | IMPERATRIZ | MARANHÃO | Brasil | 2105302 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 6d46c598-5e38-338f-b45a-c354ad0e45ed | -3.45763 | -50.37552 | 2024-11-09 04:33:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 2c4c2f52-c6eb-33fa-a780-a62ad4ac1ce0 | -2.66032 | -49.86943 | 2024-11-09 04:33:00 | NOAA-21 | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 224f3db9-a157-3271-813d-30f2b5c699fb | -2.92334 | -54.19613 | 2024-11-09 04:33:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 772785b6-f04c-3e31-ab73-325bd20da7c9 | -2.91895 | -51.68329 | 2024-11-09 04:33:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 424d7611-2034-3ed0-a790-45f01b3e5226 | -3.09207 | -50.23785 | 2024-11-09 04:33:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 93a7293f-2cee-35df-8b1a-d9e310b32031 | -4.20946 | -50.62178 | 2024-11-09 04:33:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 69aceb05-4682-3021-8e70-9fc0e7a19ff5 | -4.40044 | -49.41259 | 2024-11-09 04:33:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| f41d0a3b-c188-3095-94cd-bfdf57934c37 | -3.74261 | -50.4511 | 2024-11-09 04:33:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a3c47337-ee1b-3d05-89e0-0638c432a248 | -4.11803 | -48.50391 | 2024-11-09 04:33:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 7.3 |
| 4efa8b44-d219-3239-a85b-2b3d38574748 | -2.43269 | -53.66169 | 2024-11-09 04:33:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 1d9e2d23-efa6-30e1-a2bd-a245f26ff9fb | -2.94523 | -48.55919 | 2024-11-09 04:33:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c52d2de1-59a7-331b-8c6c-68614dae4210 | -2.96411 | -48.02923 | 2024-11-09 04:33:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 694e93ac-627a-31b8-b68e-7317f83742c4 | -3.17617 | -46.6267 | 2024-11-09 04:33:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 1d7b0c70-35a4-303a-952f-1c55565e4161 | -3.17026 | -46.53357 | 2024-11-09 04:33:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9a620eea-f4f7-3bad-89ee-da4d27d7ab19 | -4.8412 | -49.33452 | 2024-11-09 04:33:00 | NOAA-21 | NOVA IPIXUNA | PARÁ | Brasil | 1504976 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 1d780795-0857-3e58-a5ca-10ddc28350e8 | -4.8381 | -45.6354 | 2024-11-09 04:33:00 | NOAA-21 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d9cc5675-64c1-3597-9861-c8348b0b6958 | -3.20572 | -49.46514 | 2024-11-09 04:33:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 30f6f121-8575-3c5c-aba5-4a060a0cec2f | -3.14389 | -48.57208 | 2024-11-09 04:33:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 020c60d8-4b18-3459-ab41-6a4ec0878057 | -3.96972 | -48.16926 | 2024-11-09 04:33:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e1f5703f-d492-3174-a210-36d05117f8fa | -5.24801 | -49.93449 | 2024-11-09 04:33:00 | NOAA-21 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 2bb72c41-830d-39e0-b27c-69ba2e42588c | -6.24701 | -39.70783 | 2024-11-09 04:33:00 | NOAA-21 | ACOPIARA | CEARÁ | Brasil | 2300309 | 23 | 33 | nan | nan | nan | Caatinga | 2.0 |
| cb726e63-561d-3120-9193-ac749360d26b | -3.96067 | -49.0005 | 2024-11-09 04:33:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c2f68c37-3569-30ef-b215-413167746c78 | -3.69812 | -54.61692 | 2024-11-09 04:33:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 3ebefe7e-5981-390f-b7d9-e3ec8dca113c | -2.23831 | -53.77797 | 2024-11-09 04:33:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 15.0 |
| 3fd27439-da65-37c2-a959-63e075fd5e5c | -6.74468 | -47.14493 | 2024-11-09 04:33:00 | NOAA-21 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| bd1085c6-857f-3fa9-af64-6db2e71322ae | -3.26256 | -51.01336 | 2024-11-09 04:33:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f909a9b1-87fb-3b66-8e7f-8bda55f089e7 | -3.02245 | -48.11314 | 2024-11-09 04:33:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 320297c9-2dfd-36b2-9355-17107b300cfb | -3.084 | -49.57119 | 2024-11-09 04:33:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c219a098-337d-3f07-aba9-58c85992c4ce | -6.13964 | -42.80231 | 2024-11-09 04:33:00 | NOAA-21 | AMARANTE | PIAUÍ | Brasil | 2200509 | 22 | 33 | nan | nan | nan | Caatinga | 3.5 |
| bed9f6a1-8077-32c0-80fd-f6de3d9acc51 | -4.70687 | -46.49209 | 2024-11-09 04:33:00 | NOAA-21 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 9f363392-b90d-374f-9556-514d39310397 | -4.2427 | -47.57635 | 2024-11-09 04:33:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| af3b913c-8dbe-34e5-8914-43078f3f4792 | -3.88711 | -52.39049 | 2024-11-09 04:33:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b56e2b32-d7e4-35b4-bd9e-3d08da9018d9 | -3.68116 | -47.49155 | 2024-11-09 04:33:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e8dc1334-14d5-33d6-a318-3cb4293fec31 | -2.87077 | -50.32206 | 2024-11-09 04:33:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 74e5aed5-7340-32bb-8493-b22fa30cd593 | -3.9243 | -50.24616 | 2024-11-09 04:33:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| addd0966-821c-391f-8181-af0625cba6e8 | -4.2741 | -47.07055 | 2024-11-09 04:33:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 841a25b0-298d-3faa-ae55-96a40a1294b6 | -2.81793 | -52.93273 | 2024-11-09 04:33:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 6405695d-df4d-3649-9e5d-d1f225a7fe09 | -4.20702 | -48.54306 | 2024-11-09 04:33:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 74f2dfdd-c466-3394-9f1d-ba608e93d216 | -2.89224 | -49.38252 | 2024-11-09 04:33:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e77262bd-2afd-3db7-83c8-a9c8a220f7b4 | -4.38116 | -48.58138 | 2024-11-09 04:33:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 94d0fd10-7b47-3951-825f-01892965d30d | -4.57256 | -43.7963 | 2024-11-09 04:33:00 | NOAA-21 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b01d9260-7551-33a7-b2f6-8dc3e0a63c15 | -3.33904 | -46.65232 | 2024-11-09 04:33:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d5349149-30c3-3466-bfd2-efe2cc927e12 | -4.24836 | -48.53853 | 2024-11-09 04:33:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 2990e79e-e305-3b8f-8c14-86ef9d8a311a | -3.89988 | -50.30816 | 2024-11-09 04:33:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 07f8b438-9f88-3bf4-957c-d8a394e0c842 | -3.53935 | -51.10691 | 2024-11-09 04:33:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| f909783f-5529-38cf-889d-5f924453e4c5 | -10.86536 | -44.91175 | 2024-11-09 04:33:00 | NOAA-21 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 08ac73bb-916c-3539-89d6-42923b613176 | -5.44917 | -43.26999 | 2024-11-09 04:33:00 | NOAA-21 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 551a267e-642d-3677-ad87-8fa7720371d7 | -2.86166 | -49.39718 | 2024-11-09 04:33:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 59539604-b8fa-3f20-aeca-cb9ca36b480b | -2.83422 | -49.45886 | 2024-11-09 04:33:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 9b8d1f47-89a6-31b9-af4e-c3d7002770b5 | -3.75705 | -45.9535 | 2024-11-09 04:33:00 | NOAA-21 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 09a81e1f-76d4-3e76-be39-d3c5e64e280d | -3.53799 | -51.25867 | 2024-11-09 04:33:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| de640670-416b-37cd-841d-087d58c2f44e | -2.81483 | -51.80549 | 2024-11-09 04:33:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 92b08b0d-5671-3749-bf05-6bc4e61eda34 | -3.74652 | -51.10016 | 2024-11-09 04:33:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 04b431de-3574-3850-bfd7-3b4cb1e27003 | -4.06287 | -48.31258 | 2024-11-09 04:33:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| cb43572c-1aa9-370d-9ccf-8685164ce55d | -2.79219 | -49.65656 | 2024-11-09 04:33:00 | NOAA-21 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 16.0 |
| b4f2b662-4f85-30cd-8ffa-7df53ce3e546 | -4.80453 | -44.78239 | 2024-11-09 04:33:00 | NOAA-21 | POÇÃO DE PEDRAS | MARANHÃO | Brasil | 2108900 | 21 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 5f8ea157-d767-3b26-8ca7-50ebc870342b | -3.95695 | -48.16362 | 2024-11-09 04:33:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 7.8 |
| 58e3a97c-d859-3872-881a-5cba69524061 | -3.8271 | -52.1654 | 2024-11-09 04:33:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 3ee6e3f5-21cf-388a-8961-915ce408af61 | -2.69454 | -51.70322 | 2024-11-09 04:33:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |


[Clique aqui para ver as próximas entradas](README45.md)
