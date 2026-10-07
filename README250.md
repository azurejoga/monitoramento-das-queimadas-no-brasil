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

## Dados Diários - Página 250

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| b0572f19-00f0-3d97-9139-93d054ac57d9 | -7.2721 | -72.7177 | 2026-10-07 18:30:00 | GOES-19 | GUAJARÁ | AMAZONAS | Brasil | 1301654 | 13 | 33 | nan | nan | nan | Amazônia | 91.9 |
| 57d6d07d-7609-34f7-be7a-f81dcb898d84 | -8.6293 | -66.9926 | 2026-10-07 18:30:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 100.7 |
| beca8708-7fa6-3116-ad75-17d972856e4d | -5.9838 | -40.9123 | 2026-10-07 18:30:00 | GOES-19 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 111.1 |
| 18fb30ae-9e43-3874-b118-57b0c8e98faf | -1.9535 | -54.0493 | 2026-10-07 18:30:00 | GOES-19 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 70.6 |
| 0c20c24b-1b19-34c0-9420-efb62110055f | -9.806 | -65.0167 | 2026-10-07 18:30:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 75.1 |
| e848ca35-c37e-308c-b887-db54ac545f05 | -3.1697 | -58.6437 | 2026-10-07 18:30:00 | GOES-19 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 181.5 |
| 021688d2-54f7-3048-9c40-6ba667a4972f | -9.0407 | -65.9215 | 2026-10-07 18:30:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 137.2 |
| fc5c32ac-3e12-3c66-acaa-31f60c071267 | -1.801 | -57.1161 | 2026-10-07 18:30:00 | GOES-19 | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | 213.7 |
| 5df208b3-6de7-3ab0-a024-f2557354bc06 | -6.5852 | -53.0331 | 2026-10-07 18:30:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 168.0 |
| 318fcd9f-f4cc-36ee-bc82-52979d51450a | -11.6374 | -43.664 | 2026-10-07 18:30:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 124.9 |
| 71b8efea-1006-3272-9a06-c0c12cb97d0b | -3.3637 | -50.4701 | 2026-10-07 18:30:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 116.1 |
| 75090459-cc15-3d5f-a1d5-b0e7df87d477 | -7.6802 | -70.0677 | 2026-10-07 18:30:00 | GOES-19 | ENVIRA | AMAZONAS | Brasil | 1301506 | 13 | 33 | nan | nan | nan | Amazônia | 88.1 |
| 26c79a86-9ab6-3922-9363-e9d3ec592418 | -3.5684 | -54.4946 | 2026-10-07 18:30:00 | GOES-19 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 66.9 |
| de9a8d73-f645-3f0a-bcff-a1e6469f235b | -5.7305 | -53.4446 | 2026-10-07 18:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 107.0 |
| 18264bc1-0ce8-3bc7-99a8-bd12a5bd6753 | -3.1697 | -58.6244 | 2026-10-07 18:30:00 | GOES-19 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 128.7 |
| 3b80dc3c-8def-3b76-a54d-42c9811bea7f | -5.5685 | -41.0448 | 2026-10-07 18:30:00 | GOES-19 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 128.0 |
| 4e1fc9fa-c1d9-3f2b-b4f1-e4ec2c5ecd99 | -9.8431 | -65.0341 | 2026-10-07 18:30:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 64.6 |
| da41f0a3-918f-3e2f-a384-cb219690acad | -3.6603 | -54.512 | 2026-10-07 18:30:00 | GOES-19 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 119.6 |
| edce48e7-4fff-37a6-a0d0-9ed6b932aea5 | -3.2137 | -42.953 | 2026-10-07 18:30:00 | GOES-19 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 116.7 |
| ad7ecd33-6d42-3d41-af92-cd2d32b18876 | -9.0592 | -65.9209 | 2026-10-07 18:30:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 104.6 |
| da71b612-eb69-3f83-bd48-2323b97c1ff7 | -6.0447 | -53.49 | 2026-10-07 18:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 82.4 |
| 34f5dd14-ab96-3393-aa86-2e8fe56494e6 | -7.6767 | -72.296 | 2026-10-07 18:30:00 | GOES-19 | CRUZEIRO DO SUL | ACRE | Brasil | 1200203 | 12 | 33 | nan | nan | nan | Amazônia | 95.7 |
| 09affe91-4495-3041-a863-df6acfd13d03 | -11.7335 | -43.649 | 2026-10-07 18:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 114.1 |
| 746aecec-286b-35fc-840d-bebe5e71dc47 | -3.1299 | -53.7431 | 2026-10-07 18:40:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 71.8 |
| 293c9a46-02fa-3dfa-b61f-0e9497650d58 | -2.9271 | -53.9496 | 2026-10-07 18:40:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 88.1 |
| 0db46f3f-8cff-3195-ab08-75e6187c0fb5 | -1.4771 | -53.6134 | 2026-10-07 18:40:00 | GOES-19 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 65.0 |
| 9f30ae07-962a-3d0d-8d00-582668e64cc0 | -5.496 | -42.8178 | 2026-10-07 18:40:00 | GOES-19 | NAZÁRIA | PIAUÍ | Brasil | 2206720 | 22 | 33 | nan | nan | nan | Caatinga | 103.6 |
| 715140f5-475c-3464-b71b-d6d2662ae950 | -7.6802 | -70.086 | 2026-10-07 18:40:00 | GOES-19 | ENVIRA | AMAZONAS | Brasil | 1301506 | 13 | 33 | nan | nan | nan | Amazônia | 96.7 |
| 6ea9668e-df83-3a4e-9e29-f34b4ce0a07c | -3.093 | -53.7844 | 2026-10-07 18:40:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 65.1 |
| 4eb0437e-12b2-3cc8-85b1-aab25c823d34 | -7.2011 | -52.6272 | 2026-10-07 18:40:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 63.1 |
| 0e8e74c0-336a-3b7a-a0f6-133edd68c270 | -3.2957 | -49.1202 | 2026-10-07 18:40:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 89.7 |
| 7ceb69ed-5fc3-30f6-aafa-a283a4c88201 | -5.0325 | -49.7687 | 2026-10-07 18:40:00 | GOES-19 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 121.8 |
| 23faa7ae-c139-379b-b012-73255b2338bd | -2.1361 | -54.4671 | 2026-10-07 18:40:00 | GOES-19 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 73.0 |
| b7a327c0-ffbe-392d-846b-22746517e922 | -7.3085 | -73.0269 | 2026-10-07 18:40:00 | GOES-19 | GUAJARÁ | AMAZONAS | Brasil | 1301654 | 13 | 33 | nan | nan | nan | Amazônia | 104.1 |
| 412625ce-b5e6-35cd-a4ed-92a7b0b6e674 | -2.951 | -58.3201 | 2026-10-07 18:40:00 | GOES-19 | SILVES | AMAZONAS | Brasil | 1304005 | 13 | 33 | nan | nan | nan | Amazônia | 90.1 |
| 2a52e44b-f6b6-3559-8eb7-85409617fba1 | -6.8764 | -43.685 | 2026-10-07 18:40:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 147.3 |
| 7a015a3c-77c7-325c-a331-d38554b471c5 | -3.1973 | -50.5382 | 2026-10-07 18:40:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 215.3 |
| cc6eb2c8-b51d-32a5-b039-922916bc58ee | -6.5853 | -53.0127 | 2026-10-07 18:40:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 181.5 |
| c88a5e42-00ac-3e9e-81e7-4085fab23fe2 | -6.895 | -43.7066 | 2026-10-07 18:40:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 208.1 |
| 01a867ab-a64a-3613-b1d2-dadc2d670ab9 | -5.5148 | -42.8164 | 2026-10-07 18:40:00 | GOES-19 | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Caatinga | 99.0 |
| bc78b4fb-ccc1-3668-8070-063ccc86fa12 | -5.7189 | -45.1547 | 2026-10-07 18:40:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 173.0 |
| 46823475-93d6-38b2-a461-1e24bb085118 | -5.7315 | -41.7069 | 2026-10-07 18:40:00 | GOES-19 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 88.3 |
| adf51d17-a3f6-34f6-885f-9ac89b2671bd | -6.0074 | -53.5325 | 2026-10-07 18:40:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 43.7 |
| 458c96b0-f1e4-3174-bbfc-88676ccbe6b5 | -17.1213 | -41.3421 | 2026-10-07 18:40:00 | GOES-19 | CARAÍ | MINAS GERAIS | Brasil | 3113008 | 31 | 33 | nan | nan | nan | Mata Atlântica | 90.9 |
| fe64a95b-5ed5-33c9-a4e5-8f973b20af59 | -1.801 | -57.1161 | 2026-10-07 18:40:00 | GOES-19 | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | 218.1 |
| 6074efdc-187c-3532-b9a8-509d10af666c | -3.2136 | -42.9764 | 2026-10-07 18:40:00 | GOES-19 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 114.2 |
| c5f0f655-b5bf-3666-ab86-8b26a3607814 | -3.2215 | -53.8616 | 2026-10-07 18:40:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 52.6 |
| 6cc35378-7b8e-348b-afa1-ed6072d1dd13 | -8.2181 | -46.362 | 2026-10-07 18:40:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 109.9 |
| 1fed48c4-f3e0-3189-b188-d7cbf8ec3aae | 1.7855 | -55.5461 | 2026-10-07 18:40:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 61.1 |
| d66556f3-16d5-33c9-ba42-b322757494c7 | -5.7927 | -45.2626 | 2026-10-07 18:40:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 234.8 |
| 9cbf57e0-49dc-3d50-98b9-5862e9d2f885 | -8.8573 | -71.4625 | 2026-10-07 18:40:00 | GOES-19 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 104.6 |
| 1f80efae-2aee-3944-922e-53f85698675b | -7.1827 | -52.6078 | 2026-10-07 18:40:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 111.7 |
| 759af0e4-0c18-3968-8daa-7963591eb7d4 | -9.1174 | -65.359 | 2026-10-07 18:40:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 101.2 |
| 7d507fa9-c9f1-3aab-b649-b2d74c453376 | -6.8952 | -43.6833 | 2026-10-07 18:40:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 479.2 |
| c1d62932-b801-3ddd-ab4e-26d141c3c5c5 | -6.2529 | -52.847 | 2026-10-07 18:40:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 66.1 |
| 1f643e86-7068-3340-9dca-8ded5c3b6c6b | -6.6039 | -53.0116 | 2026-10-07 18:40:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 148.3 |
| 7480abb9-9625-389f-95a0-712c7d2369be | -9.96 | -43.481 | 2026-10-07 18:40:00 | GOES-19 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 121.4 |
| 2f5994b8-70b5-3a34-ae2a-559e7de67f11 | 1.7121 | -55.6063 | 2026-10-07 18:40:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 74.9 |
| 772df99d-ec3d-3abe-ba26-44f8fc59ae30 | -9.0407 | -65.9215 | 2026-10-07 18:40:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 128.2 |
| 34318367-fac5-3209-9398-ae367f34e4c8 | -10.3731 | -45.0306 | 2026-10-07 18:40:00 | GOES-19 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 98.0 |
| c7f8cb2b-7fec-3396-bfa1-69aab4999e80 | -3.1116 | -53.7436 | 2026-10-07 18:40:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 67.7 |
| 4578bbfd-7433-3dcf-a3ed-6c8080c36cfb | -5.9772 | -43.5057 | 2026-10-07 18:40:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 291.9 |
| 0f820a43-c5dd-3f3e-86a7-f5caa1f727dc | -9.9596 | -43.5045 | 2026-10-07 18:40:00 | GOES-19 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 106.0 |
| d9d7eebe-54b1-34e1-a605-dbe08f399528 | -6.1502 | -39.4158 | 2026-10-07 18:40:00 | GOES-19 | ACOPIARA | CEARÁ | Brasil | 2300309 | 23 | 33 | nan | nan | nan | Caatinga | 120.7 |
| eecc419c-9e17-3eb2-9c7f-e0bae9a2b8b4 | -6.217 | -52.6851 | 2026-10-07 18:40:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 50.8 |
| dbda59f7-ff1e-32b2-a718-932b68430a19 | -6.6753 | -44.9674 | 2026-10-07 18:40:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 145.7 |
| fc51577a-2aba-3075-a9ba-6083cb00c6c5 | -8.6108 | -66.993 | 2026-10-07 18:40:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 92.6 |
| 0ea6f96e-a915-3033-ba29-8aad87e53e8f | -9.1711 | -65.7682 | 2026-10-07 18:40:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 111.2 |
| 889f7ab3-64e3-3693-b4ca-34197b25d3b5 | -7.6802 | -70.0677 | 2026-10-07 18:40:00 | GOES-19 | ENVIRA | AMAZONAS | Brasil | 1301506 | 13 | 33 | nan | nan | nan | Amazônia | 141.9 |
| f34b0db1-f8e9-3f89-b47a-ba975f720624 | -3.1697 | -58.6244 | 2026-10-07 18:40:00 | GOES-19 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 94.9 |
| afa45cac-6f46-3409-adf4-41d01b683c77 | -3.4762 | -50.0883 | 2026-10-07 18:40:00 | GOES-19 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 171.4 |
| f82f9af0-e2fd-3f3b-9a1b-8f1dac280700 | -9.4751 | -64.3336 | 2026-10-07 18:40:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 71.3 |
| 8b44c937-ae92-3b43-84c6-7711b2e85eea | -12.0457 | -43.3864 | 2026-10-07 18:40:00 | GOES-19 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 120.3 |
| 75776633-62db-3624-b6b3-814464c17493 | -6.5794 | -41.5841 | 2026-10-07 18:40:00 | GOES-19 | INHUMA | PIAUÍ | Brasil | 2204709 | 22 | 33 | nan | nan | nan | Caatinga | 166.7 |
| 234e7ab0-8653-3479-a2ab-c5325f7d186d | -8.0207 | -47.1808 | 2026-10-07 18:40:00 | GOES-19 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 84.8 |
| b603a055-60a7-3674-9f4c-3c42b58ee1e9 | -13.885 | -44.1365 | 2026-10-07 18:40:00 | GOES-19 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 150.9 |
| 768a9845-4900-3a79-a907-310eabf0c80b | -9.3566 | -65.7436 | 2026-10-07 18:40:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 108.3 |
| fd66815e-1dcc-3050-a31d-839cbe10bf6e | -4.2744 | -46.3846 | 2026-10-07 18:40:00 | GOES-19 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 238.0 |
| 132b8441-7195-31f4-89d9-6fcc9623158f | -3.1787 | -50.5597 | 2026-10-07 18:40:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 193.3 |
| 788c0590-0fdc-34e2-8730-34200a8763cd | -5.839 | -53.8246 | 2026-10-07 18:40:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 65.3 |
| 5883ea37-bda5-3e15-b17b-d4916764af19 | -11.8503 | -43.5598 | 2026-10-07 18:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 134.8 |
| 8e3ae832-2246-3d3e-9e35-995b98a87a58 | -8.2184 | -46.3396 | 2026-10-07 18:40:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 119.9 |
| f36e7401-8d23-3877-8c90-25a9c5020210 | -5.2288 | -50.9158 | 2026-10-07 18:40:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 56.3 |
| 150c6ccb-47b5-33b9-ab75-d1ab055dd3fd | -6.1974 | -52.8295 | 2026-10-07 18:40:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 60.5 |
| dc3dec22-72d4-39d3-8f32-78e25ab9df21 | -2.0447 | -54.3085 | 2026-10-07 18:40:00 | GOES-19 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 117.3 |
| 0b039901-3ed6-38cd-9404-0a16977080ab | -3.1697 | -58.6437 | 2026-10-07 18:40:00 | GOES-19 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 150.3 |
| 4868f815-a951-30c2-97c3-66c2c256841f | -5.9835 | -40.9367 | 2026-10-07 18:40:00 | GOES-19 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 168.9 |
| b8d97227-029c-309e-b8e3-b54808f61cb0 | -8.5183 | -67.0139 | 2026-10-07 18:40:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 144.6 |
| 5be29519-35da-3592-a168-ffa5d217c488 | -9.006 | -65.4 | 2026-10-07 18:40:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 79.6 |
| 74cf9ad4-57ae-310f-ab24-5f015fa63452 | -5.8205 | -53.8255 | 2026-10-07 18:40:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 110.1 |
| 1a6a70e6-e8a1-3562-b9e2-0c1063c77efe | -3.13 | -53.7229 | 2026-10-07 18:40:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 77.4 |
| a1b9c124-2185-3391-9d78-e1674e7c3ae0 | -2.5307 | -58.0956 | 2026-10-07 18:40:00 | GOES-19 | SÃO SEBASTIÃO DO UATUMÃ | AMAZONAS | Brasil | 1303957 | 13 | 33 | nan | nan | nan | Amazônia | 68.2 |
| 0ed0525b-2088-353c-ba88-344945c17fc6 | -8.537 | -66.9764 | 2026-10-07 18:40:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 86.3 |
| 46392abe-fa65-366c-8a59-7e0eaa4c7b95 | -6.2714 | -52.846 | 2026-10-07 18:40:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 105.9 |
| 4f89fbac-7eec-325b-9a1b-ad35be3d7ec7 | -3.1788 | -50.5388 | 2026-10-07 18:40:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 96.7 |
| f973db6f-be52-3d09-a37f-f2865a418812 | -9.5425 | -65.6815 | 2026-10-07 18:40:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 72.8 |
| 1f45507a-8202-33b8-8618-d3708dfffc45 | -9.8844 | -64.2802 | 2026-10-07 18:40:00 | GOES-19 | BURITIS | RONDÔNIA | Brasil | 1100452 | 11 | 33 | nan | nan | nan | Amazônia | 69.9 |
| 59e6bc02-0003-31ce-b01e-1aa4c185a40e | -8.9082 | -49.986 | 2026-10-07 18:40:00 | GOES-19 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 81.8 |
| bcbd1d80-5481-36b3-a0fa-32a856f47c58 | -5.8388 | -53.8448 | 2026-10-07 18:40:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 56.9 |
| 58e22306-bcf1-3ec7-9e9d-60cbc1d60949 | -3.1484 | -53.7225 | 2026-10-07 18:40:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 108.4 |


[Clique aqui para ver as próximas entradas](README251.md)
