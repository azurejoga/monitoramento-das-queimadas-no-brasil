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

## Dados Diários - Página 42

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| c0e35905-b67f-3162-81bd-67ed0f9b4962 | 1.712 | -55.6459 | 2026-10-07 04:10:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 44.4 |
| 37af560e-4b63-3401-9c30-0750e7d3c8e4 | -15.2517 | -43.2501 | 2026-10-07 04:10:00 | GOES-19 | MONTE AZUL | MINAS GERAIS | Brasil | 3142908 | 31 | 33 | nan | nan | nan | Caatinga | 126.9 |
| b32694c6-2566-3a2c-8387-2d9b22a2772e | -2.7613 | -54.0941 | 2026-10-07 04:10:00 | GOES-19 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 226.0 |
| b3563765-d511-3c44-a655-432223251d04 | -3.0914 | -54.2669 | 2026-10-07 04:10:00 | GOES-19 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 58.3 |
| 8d7db644-1bae-3306-839b-6373d9a47fbb | -2.7796 | -54.0937 | 2026-10-07 04:10:00 | GOES-19 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 215.5 |
| 60c0936b-fab9-3e31-b25a-d802f6a3e876 | -3.5311 | -54.6357 | 2026-10-07 04:10:00 | GOES-19 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 62.7 |
| 01e58331-cf14-3908-b792-8cac1fd47189 | -2.7612 | -54.1142 | 2026-10-07 04:10:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 160.2 |
| d4cd5d53-e6d9-3e5d-9d14-e7f45817a681 | -3.1114 | -53.7839 | 2026-10-07 04:10:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 51.5 |
| 3ba0e960-0309-3258-8aaf-ef45a0a22c01 | -3.8566 | -55.9967 | 2026-10-07 04:10:00 | GOES-19 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 69.1 |
| a08aa946-0a54-3e0a-ba35-9683e8798f2c | -3.1787 | -50.5597 | 2026-10-07 04:10:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 60.6 |
| 3c3762cc-94f7-3681-80e3-9e27545defcd | -3.4762 | -50.0883 | 2026-10-07 04:10:00 | GOES-19 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 46.6 |
| 663edd68-ffa4-331d-87e8-5fc53d15c3e0 | -3.1115 | -53.7637 | 2026-10-07 04:10:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 52.5 |
| 1750ea91-61db-3464-8faa-b12af7cba3b5 | 1.7121 | -55.6261 | 2026-10-07 04:10:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 64.2 |
| 9b962c53-f408-30cf-a3de-fbbb2b9da684 | -3.073 | -54.2674 | 2026-10-07 04:10:00 | GOES-19 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 55.3 |
| 6b22d1f6-ebd0-37a2-9203-f73698f47428 | -8.7039 | -45.1832 | 2026-10-07 04:10:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 62.4 |
| e96313d0-cfdf-328a-a1ef-c2b9195ff747 | -2.7797 | -54.0736 | 2026-10-07 04:10:00 | GOES-19 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 67.6 |
| 25636623-ef3c-3b44-81f4-bee8cd8c91df | -2.7613 | -54.074 | 2026-10-07 04:10:00 | GOES-19 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 78.1 |
| bcf1df59-3466-3a64-bdfd-0c849cd213e9 | -9.1517 | -65.9554 | 2026-10-07 04:10:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 63.1 |
| e0531645-d123-3c42-aaa9-c9b15a7e770c | -3.0731 | -54.2473 | 2026-10-07 04:10:00 | GOES-19 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 55.0 |
| 468b5fc4-9318-3012-be34-9a624a7769eb | -8.7036 | -45.2061 | 2026-10-07 04:10:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 110.8 |
| 8cdcf0da-c10d-33d1-8c1a-d9c4b9a6729b | -3.0375 | -53.9066 | 2026-10-07 04:10:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 62.9 |
| d6cfc0ad-4814-388c-a303-8fba8380b9f3 | -9.1518 | -65.9367 | 2026-10-07 04:10:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 51.2 |
| 847e10c6-6c10-338a-b00f-c710fc5f4a88 | -5.7189 | -45.1547 | 2026-10-07 04:10:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 67.7 |
| 877b5304-ec4a-349d-87ac-42b9c6acffcb | -5.7376 | -45.1533 | 2026-10-07 04:10:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 67.2 |
| 686ade37-b870-398a-abc2-3e20401b39e8 | -3.5127 | -54.6562 | 2026-10-07 04:10:00 | GOES-19 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 78.2 |
| 34ed8831-cbf8-37bf-9feb-dcb8e31377f0 | -3.8567 | -55.9769 | 2026-10-07 04:10:00 | GOES-19 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 97.3 |
| a57c0c50-1dd4-3774-b3a1-43de60ff6517 | -2.76 | -54.08 | 2026-10-07 04:15:00 | MSG-03 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| beaf2554-06a1-38ec-a6d8-8eb13b18f167 | 3.52781 | -51.27639 | 2026-10-07 04:17:00 | NOAA-20 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 1.6 |
| adca7555-64a3-34ef-acc6-425d9fcd8493 | 2.4358 | -50.85032 | 2026-10-07 04:17:00 | NOAA-20 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 96fe8167-aec9-3039-af03-5131cea304ea | 2.44131 | -50.84951 | 2026-10-07 04:17:00 | NOAA-20 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 1.9 |
| fc95f141-2de5-36bd-b59b-bea711436928 | 0.72811 | -51.37212 | 2026-10-07 04:17:00 | NOAA-20 | PORTO GRANDE | AMAPÁ | Brasil | 1600535 | 16 | 33 | nan | nan | nan | Amazônia | 0.7 |
| f88d6d15-fe34-3ce7-852e-9ae0a3a8601d | 3.51516 | -51.27016 | 2026-10-07 04:17:00 | NOAA-20 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 5f486d69-29f8-3172-a3b9-c4df4c1d26f3 | 3.52148 | -51.27329 | 2026-10-07 04:17:00 | NOAA-20 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 146ebc23-4277-3b07-ae46-f421c73b4b0b | 2.59723 | -50.8739 | 2026-10-07 04:17:00 | NOAA-20 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 2.8 |
| a90e5d43-20f8-3ab6-833b-5d40a56c07de | 2.45455 | -50.82547 | 2026-10-07 04:17:00 | NOAA-20 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 754c8943-12c1-3636-a63a-6065e3e0d824 | 2.12292 | -50.8339 | 2026-10-07 04:17:00 | NOAA-20 | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 80ed6c2e-a80e-38fc-a92a-44cca66ef6a4 | 3.53308 | -51.27949 | 2026-10-07 04:17:00 | NOAA-20 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f8024a0c-2730-32df-a251-6e6dfe4ae9f9 | 2.60276 | -50.87305 | 2026-10-07 04:17:00 | NOAA-20 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 2.2 |
| ad25c32e-f275-3ca3-ba13-6d0a43f7b601 | 3.52672 | -51.27636 | 2026-10-07 04:17:00 | NOAA-20 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 9ec5d008-59c3-3703-a62d-f8e15e472bc5 | 2.43634 | -50.85389 | 2026-10-07 04:17:00 | NOAA-20 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 1.9 |
| b3151e63-711f-372c-ac4f-d24ea1271353 | 2.44239 | -50.85663 | 2026-10-07 04:17:00 | NOAA-20 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 66ac022f-2fe7-304d-904a-4d85103e24d5 | 3.52839 | -51.2804 | 2026-10-07 04:17:00 | NOAA-20 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 1688049a-2947-3c4a-8a0f-a9972e517545 | 2.1284 | -50.8331 | 2026-10-07 04:17:00 | NOAA-20 | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 25544698-e367-3022-bb25-546e683c599c | 3.52733 | -51.28036 | 2026-10-07 04:17:00 | NOAA-20 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7a6ff16a-f063-3e3a-b16f-84d90256f67d | 0.94142 | -50.203 | 2026-10-07 04:17:00 | NOAA-20 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e8116ab7-357a-30eb-90bf-ef05531594b8 | 0.72869 | -51.37578 | 2026-10-07 04:17:00 | NOAA-20 | PORTO GRANDE | AMAPÁ | Brasil | 1600535 | 16 | 33 | nan | nan | nan | Amazônia | 0.7 |
| b77612c6-bf18-36da-8ef4-5c8e72e8ce35 | 2.59669 | -50.87173 | 2026-10-07 04:17:00 | NOAA-20 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 566655f1-434b-305c-91da-85f9f29459ba | -2.60153 | -48.25922 | 2026-10-07 04:19:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 9f58e0b7-f7fc-39e8-8fde-e0bc16aceedf | -5.16357 | -46.06024 | 2026-10-07 04:19:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| bab0b17b-e624-3c86-8dc3-1a42936fd038 | -3.73846 | -51.22051 | 2026-10-07 04:19:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 24f25b65-a6e3-3ff3-ad42-2365ed91cd5d | -3.28667 | -54.07913 | 2026-10-07 04:19:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 8.3 |
| 35fe308d-371b-3beb-b3b8-542f276d9947 | -4.26447 | -46.38145 | 2026-10-07 04:19:00 | NOAA-20 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| bff7a5f6-67eb-377a-9e0b-ef6b4c119bcd | -3.11947 | -53.76615 | 2026-10-07 04:19:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 9150ff3f-8ad9-3321-a867-36ab4c26a851 | -2.98822 | -54.04973 | 2026-10-07 04:19:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 1bb60c29-27b0-3359-ba19-24ad76795534 | -3.06539 | -54.1478 | 2026-10-07 04:19:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f825550a-cd4c-3ce3-968c-d00110513d88 | -3.73898 | -51.21745 | 2026-10-07 04:19:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 2b75c294-ff7b-33be-8888-01a2e9d34954 | -3.81101 | -47.48982 | 2026-10-07 04:19:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| a96f33d0-21dc-3892-bb3a-e184b19b36bf | -3.35784 | -43.39349 | 2026-10-07 04:19:00 | NOAA-20 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 42fc9295-d02c-3e93-91f7-481e31a25cd0 | -7.46133 | -47.59861 | 2026-10-07 04:19:00 | NOAA-20 | BARRA DO OURO | TOCANTINS | Brasil | 1703073 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 566c1025-f58c-3076-b2f2-8fa6f73de049 | -8.58202 | -45.67159 | 2026-10-07 04:19:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 3ca3dd61-5f7d-315a-912f-2cbbb64c6aa5 | -3.05324 | -54.21725 | 2026-10-07 04:19:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 05f2d151-d1b3-376a-b85d-c31be34408ad | -3.07587 | -54.27349 | 2026-10-07 04:19:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 762d41eb-ba86-3c30-9d63-e4712f4a96da | -7.46384 | -42.99521 | 2026-10-07 04:19:00 | NOAA-20 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 5275340e-b2ba-3ecc-9c1e-bc2e27b98752 | -3.04707 | -54.15655 | 2026-10-07 04:19:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 84395452-f77b-3be8-97a2-cdea2cbf8cb8 | -5.72419 | -45.16813 | 2026-10-07 04:19:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 16.6 |
| dbc3fe1a-1fbf-3a07-99fa-926d70b5ca3f | -2.86722 | -54.20613 | 2026-10-07 04:19:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| ffc5995a-51e8-39f9-935d-858dc722dbc8 | -3.08118 | -54.24275 | 2026-10-07 04:19:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| d1111a43-c2aa-368a-92c7-486d2694a34c | -5.73541 | -41.71848 | 2026-10-07 04:19:00 | NOAA-20 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 97dc51ef-6333-3e55-a8d8-0b41c340251b | -3.80862 | -51.54061 | 2026-10-07 04:19:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 4ed803f6-8be9-3342-bc4f-ede930d79869 | -2.99027 | -51.05735 | 2026-10-07 04:19:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 3528767e-97f9-3604-b855-8129b826a258 | -3.21844 | -48.81886 | 2026-10-07 04:19:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| c0e31d93-d0d6-3b79-824f-24c849c6ef69 | -3.21353 | -53.87912 | 2026-10-07 04:19:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 75e4529e-5103-3461-a742-11e508c779a6 | -2.76056 | -54.09158 | 2026-10-07 04:19:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 20.3 |
| c95ecabb-6063-3a62-9a6c-6e1571e97ff4 | -6.03188 | -42.27279 | 2026-10-07 04:19:00 | NOAA-20 | ELESBÃO VELOSO | PIAUÍ | Brasil | 2203503 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 785e8d7c-7876-3c7b-bfc1-05c3f2ff8de7 | -3.53155 | -54.6428 | 2026-10-07 04:19:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 02570801-fef8-3a0b-83c3-ec004150fc01 | -3.06734 | -54.17355 | 2026-10-07 04:19:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ee3c2546-80dd-3d4f-b1b9-fff020931d98 | -3.06125 | -54.14889 | 2026-10-07 04:19:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a925c8ff-bc99-38ca-b64a-4e8d89748d8e | -7.87162 | -44.21717 | 2026-10-07 04:19:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 45.4 |
| 247107b1-d019-3027-a6e1-0b185bad640b | -3.09765 | -51.3798 | 2026-10-07 04:19:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 45081566-4bc8-36e4-8738-10d9caf5b197 | -4.83839 | -48.21455 | 2026-10-07 04:19:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ed317c92-2a3a-32dd-8f51-4312e9f65a11 | -4.15857 | -55.14708 | 2026-10-07 04:19:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 484b5990-cabd-3921-91bc-adefe4d3158d | -3.05959 | -54.15877 | 2026-10-07 04:19:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| b9c68449-a212-3229-9953-b8d6d2a01d58 | -5.37723 | -44.15639 | 2026-10-07 04:19:00 | NOAA-20 | GOVERNADOR EUGÊNIO BARROS | MARANHÃO | Brasil | 2104602 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 72437bf5-0e6e-3a93-a730-afde6cb786bb | -3.74358 | -51.22137 | 2026-10-07 04:19:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 42ee817d-2b82-34b0-b548-22a953c2785f | -8.33399 | -44.74271 | 2026-10-07 04:19:00 | NOAA-20 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 409dd541-804f-318d-9cc1-cfa4519cbb6e | -3.05411 | -54.21225 | 2026-10-07 04:19:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 7eac950c-75c5-3f8f-91d3-140786304fd2 | -7.4043 | -44.45863 | 2026-10-07 04:19:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 6dd282a5-2bc0-3b0b-b784-d1100fe6a1a2 | -3.62911 | -55.28469 | 2026-10-07 04:19:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e6699d85-faf4-3dd8-abda-5ac44d4ebcc9 | -3.16008 | -50.44555 | 2026-10-07 04:19:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 6abaca92-05db-3b9e-9afa-1593f4444b35 | -3.07044 | -54.24852 | 2026-10-07 04:19:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| b03d67c4-0c36-355a-b90a-f8dc9e19a501 | -3.48961 | -50.09538 | 2026-10-07 04:19:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3e5915ab-2386-3cb5-b38b-b0ffe69e9dbb | -3.0628 | -54.16259 | 2026-10-07 04:19:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 52cd4221-4cc5-30b2-a24c-97ddd812fc67 | -7.60973 | -42.3695 | 2026-10-07 04:19:00 | NOAA-20 | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 5b4b7da5-f181-3c8a-b629-df7b8aa0e69c | -3.35607 | -50.47483 | 2026-10-07 04:19:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 13fcf33b-20cb-388e-af6d-53620fa0f878 | -3.28056 | -50.14226 | 2026-10-07 04:19:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 25.6 |
| d0c07f04-b56b-3ce7-998f-941f9575f3cb | -3.09138 | -54.29658 | 2026-10-07 04:19:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 12.3 |
| cc5c865e-4db1-3bfa-90d5-1166d7e90134 | -1.26355 | -49.05824 | 2026-10-07 04:19:00 | NOAA-20 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6334349a-c09a-3767-8c0a-83d63d878fdf | -6.00822 | -47.40191 | 2026-10-07 04:19:00 | NOAA-20 | RIBAMAR FIQUENE | MARANHÃO | Brasil | 2109551 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| fded3acb-75b2-3bf4-a997-7cee8edcc99d | -4.09724 | -42.50216 | 2026-10-07 04:19:00 | NOAA-20 | BARRAS | PIAUÍ | Brasil | 2201200 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 7b6166e3-1493-3d98-9435-19181c2da06c | -3.50374 | -51.68516 | 2026-10-07 04:19:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |


[Clique aqui para ver as próximas entradas](README43.md)
