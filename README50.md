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

## Dados Diários - Página 50

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 2933780e-b8ca-3430-a421-d7a3acc3e233 | -0.5379 | -58.0762 | 2025-11-17 05:29:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| ba50b469-8b80-37c9-a076-fe72a9f43351 | -3.29856 | -50.07301 | 2025-11-17 05:29:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c68d3814-0f70-30af-80f7-f12117e08a59 | 0.2408 | -51.01433 | 2025-11-17 05:29:00 | NOAA-20 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7e43137d-59eb-3213-b9d9-6d2d44d28922 | -3.18115 | -50.6509 | 2025-11-17 05:29:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| b995a3f1-4185-36a0-8e57-796dc6b6af56 | -1.53143 | -55.52175 | 2025-11-17 05:29:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 43fcda0e-39ff-3fc7-a2bd-34a236ec4c80 | -3.23592 | -50.49157 | 2025-11-17 05:29:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 4f8f82e8-4b76-3be9-b118-128ac97281ee | -3.2338 | -50.50542 | 2025-11-17 05:29:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 301929c3-4d37-32b6-a909-64257d0065ed | -9.44367 | -59.20569 | 2025-11-17 05:29:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| c3695737-ac29-3a79-b3ab-477ae654ca39 | -9.10674 | -62.50396 | 2025-11-17 05:29:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e1487287-81d4-3532-bd0b-c520226dbdf9 | -3.18975 | -50.65472 | 2025-11-17 05:29:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 7d6fb6dc-9942-3683-911d-7c30c8cc1b3a | -10.38999 | -59.18612 | 2025-11-17 05:29:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 85a757fd-5d31-3e2f-88d0-e04d48a85af9 | -10.65692 | -49.37988 | 2025-11-17 05:29:00 | NOAA-20 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 6.4 |
| cfc3880b-d14c-3851-b0ee-63a97bac3ba4 | 1.01006 | -59.51639 | 2025-11-17 05:29:00 | NOAA-20 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 35d07ac3-495e-3675-93d4-549db45a0eb9 | -2.58504 | -51.82976 | 2025-11-17 05:29:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6ef3a598-a53f-36aa-95a1-5cd24a9a02b6 | -3.60471 | -55.53746 | 2025-11-17 05:29:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a413d267-2e66-3b09-80b9-e86a25a4b878 | -3.50914 | -54.37528 | 2025-11-17 05:29:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 840aa8cf-6b13-360a-b08e-ca08ca60c953 | -5.12445 | -55.97463 | 2025-11-17 05:29:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| d3501e30-774e-3e4d-b88b-b9b95c4fbfb3 | -3.41005 | -50.12651 | 2025-11-17 05:29:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| cfdedde8-4621-336b-b28f-0a1c2afe6abc | -3.18378 | -50.6539 | 2025-11-17 05:29:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 114eb22c-7a13-3349-bb65-10e7523b0234 | -3.30475 | -50.07393 | 2025-11-17 05:29:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| b86df1f1-3cfd-3825-a670-1c495d8d450c | -4.10055 | -48.03055 | 2025-11-17 05:29:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| df88161c-ce8c-3d7f-82cd-abf1d6de3329 | -11.44119 | -54.33737 | 2025-11-17 05:29:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 48041470-e531-3da2-bd32-bb53980b0348 | -3.38333 | -50.13688 | 2025-11-17 05:29:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 9ed591a7-0252-3d60-bf20-70ebf1a267e1 | -3.23742 | -50.49426 | 2025-11-17 05:29:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 044da54c-3fbb-317a-a549-1ec5406f09c5 | -2.75775 | -48.43066 | 2025-11-17 05:29:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 03376e4b-4657-3601-b26e-e96ccf0c4cc5 | -3.59747 | -50.7218 | 2025-11-17 05:29:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8e62462f-50f9-38c7-ba04-4084e6a268ba | -3.23206 | -50.48881 | 2025-11-17 05:29:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 5045b558-ab0e-3aa8-9c2e-9bdc004948d7 | -10.51266 | -58.57867 | 2025-11-17 05:29:00 | NOAA-20 | JURUENA | MATO GROSSO | Brasil | 5105176 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 6c338cf5-962a-3539-918f-3cde439c37d1 | -3.83294 | -49.8096 | 2025-11-17 05:29:00 | NOAA-20 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 11.2 |
| f6b545f8-e3a6-3d5d-95e4-e3b6029c7ecc | -3.80961 | -48.92313 | 2025-11-17 05:29:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 055fc350-c661-3909-9fa2-01912bf79824 | -3.83614 | -49.80775 | 2025-11-17 05:29:00 | NOAA-20 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 8.5 |
| 123b0869-ac8f-3559-ba80-c18d4fc9cefe | -1.53202 | -55.51795 | 2025-11-17 05:29:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a0608b7e-1809-360a-9909-ad16cc9234d0 | -2.24803 | -53.62651 | 2025-11-17 05:29:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 7f185245-1cef-3391-9950-b17235521cec | -3.59216 | -50.71659 | 2025-11-17 05:29:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2b846ebe-371f-3f12-822a-8af8328ef2dc | -3.4923 | -54.04306 | 2025-11-17 05:29:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| a9483063-6c47-38f1-ada7-2c64864295be | 0.24137 | -51.01792 | 2025-11-17 05:29:00 | NOAA-20 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b0a0b8ec-1de8-39e1-a787-90442b01ea69 | -3.29718 | -50.08254 | 2025-11-17 05:29:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ef71312b-d50c-308d-8d46-1ae285f70755 | -3.57957 | -50.71928 | 2025-11-17 05:29:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 06d42970-3a49-302b-b843-351bf38c4d3e | -3.59152 | -50.72087 | 2025-11-17 05:29:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2c2469b7-7cc3-35b0-8d5e-18ae7576c5aa | -3.77767 | -50.14098 | 2025-11-17 05:29:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| a30bacab-a760-3808-a633-3ee0e58bfc53 | -2.93978 | -51.76106 | 2025-11-17 05:29:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3f17f217-81a9-3b30-bb10-f387d873d4a1 | -3.24143 | -50.50898 | 2025-11-17 05:29:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 321f4f3d-0547-358b-8ac9-f62314266655 | -9.5798 | -49.11511 | 2025-11-17 05:29:00 | NOAA-20 | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 239b17a0-d949-380f-9c45-ba6256ba90d2 | -3.30061 | -53.85218 | 2025-11-17 05:29:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| f0e087c7-7b7e-34dd-87c9-d4dd2ada2979 | -3.2344 | -50.4952 | 2025-11-17 05:30:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 51.2 |
| 65594c65-3d28-32d8-b43b-ff8d963a9390 | -8.86763 | -50.19398 | 2025-11-17 05:31:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| cba0a1dc-e286-3b65-a2dc-433576e18e7c | -6.80136 | -59.14042 | 2025-11-17 05:31:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 39ac077c-3244-3176-bac9-86188bd4cc72 | -7.97282 | -50.00386 | 2025-11-17 05:31:00 | NOAA-20 | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| d753588d-9f44-388f-b92f-c36b3739a5bd | -7.9662 | -50.00304 | 2025-11-17 05:31:00 | NOAA-20 | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| c8a46f34-8b25-34da-95ae-77f3525deb6b | -7.96842 | -50.0023 | 2025-11-17 05:31:00 | NOAA-20 | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| bfa7f242-35f0-3487-b0ba-0e23998456c5 | -6.91883 | -59.72503 | 2025-11-17 05:31:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ce5f53cb-746f-3965-808c-78c3c1945d42 | -7.43382 | -48.93754 | 2025-11-17 05:31:00 | NOAA-20 | ARAGUAÍNA | TOCANTINS | Brasil | 1702109 | 17 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 3adbfc90-6faf-3be6-84ba-dbd92c7e422b | -13.50494 | -61.53755 | 2025-11-17 05:31:00 | NOAA-20 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 6c12f1a0-c575-32c7-8fa5-60074792aa7d | -6.91995 | -59.72466 | 2025-11-17 05:31:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 02f7c131-1399-31fc-925c-56f8a5e6b365 | -6.89991 | -59.00142 | 2025-11-17 05:31:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 327cd149-77c6-39fc-aada-ef3480947d21 | -7.96548 | -50.00877 | 2025-11-17 05:31:00 | NOAA-20 | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| dfa53f9e-4d40-36a7-a9ae-0715f31f387c | -7.97211 | -50.00955 | 2025-11-17 05:31:00 | NOAA-20 | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 07935909-3794-3b3c-927e-d78185768ba2 | -7.96766 | -50.00802 | 2025-11-17 05:31:00 | NOAA-20 | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 8.0 |
| a2640044-645c-3fb9-afb1-2fafb08e0b8f | -8.86836 | -50.18826 | 2025-11-17 05:31:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b9ac87e9-d4ce-35bc-a4c7-218c1f9018b1 | -3.2344 | -50.4952 | 2025-11-17 05:40:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 46.5 |
| 04e741d2-ca52-31f2-8af6-a8cb6e3e00b5 | -3.2344 | -50.4952 | 2025-11-17 05:50:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 49.9 |
| ae05cb08-cb9f-3f0a-bea2-b95857fa693b | -3.8733 | -45.0156 | 2025-11-17 05:50:00 | GOES-19 | PIO XII | MARANHÃO | Brasil | 2108702 | 21 | 33 | nan | nan | nan | Amazônia | 59.6 |
| cfd193a3-04a1-39dd-9ad0-c5c315d77bb0 | -10.9443 | -48.6764 | 2025-11-17 05:50:00 | GOES-19 | BREJINHO DE NAZARÉ | TOCANTINS | Brasil | 1703701 | 17 | 33 | nan | nan | nan | Cerrado | 78.6 |
| f5eb3651-122c-3a29-9206-0e533a83d2cc | -3.8735 | -44.9929 | 2025-11-17 05:50:00 | GOES-19 | PIO XII | MARANHÃO | Brasil | 2108702 | 21 | 33 | nan | nan | nan | Amazônia | 84.1 |
| d9b1faa7-f208-377b-beb8-0b2ae0350a56 | -10.9633 | -48.6742 | 2025-11-17 05:50:00 | GOES-19 | BREJINHO DE NAZARÉ | TOCANTINS | Brasil | 1703701 | 17 | 33 | nan | nan | nan | Cerrado | 101.0 |
| 210f18e8-6e39-3c53-a5d9-d1352d8fb4a5 | -11.3992 | -43.33646 | 2025-11-17 05:59:00 | AQUA_M-M | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 23298c70-9b94-3b41-ac60-dba5ea8d8e51 | -3.65412 | -44.72717 | 2025-11-17 05:59:00 | AQUA_M-M | ARARI | MARANHÃO | Brasil | 2101004 | 21 | 33 | nan | nan | nan | Amazônia | 4.1 |
| aebe1bff-33d6-3cef-bb02-7d7142b8c300 | -7.08231 | -42.73424 | 2025-11-17 05:59:00 | AQUA_M-M | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 6.5 |
| 8c122791-d572-30ed-af5e-cbf84b1719ed | -4.65439 | -46.74063 | 2025-11-17 05:59:00 | AQUA_M-M | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 26.5 |
| 076d2d70-9d94-33c6-a977-064b4a69a123 | -11.78634 | -44.64101 | 2025-11-17 05:59:00 | AQUA_M-M | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 11.5 |
| 62493f14-0db5-337f-b8e5-12a38c7e6793 | -3.29631 | -50.06752 | 2025-11-17 05:59:00 | AQUA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 9.2 |
| 04dd283a-2bf1-3525-8434-1de42a0a3219 | -11.15101 | -44.03275 | 2025-11-17 05:59:00 | AQUA_M-M | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 7.7 |
| f135e309-fd97-370a-85da-b92e2a179fe8 | -11.83512 | -49.2121 | 2025-11-17 05:59:00 | AQUA_M-M | CARIRI DO TOCANTINS | TOCANTINS | Brasil | 1703867 | 17 | 33 | nan | nan | nan | Cerrado | 30.2 |
| 32ec1b1c-1ec1-3320-a2de-b38edeac7b33 | -12.86356 | -46.43399 | 2025-11-17 05:59:00 | AQUA_M-M | COMBINADO | TOCANTINS | Brasil | 1705557 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 746f7d08-9103-3dc1-acb6-9742a1ece6b1 | -4.99579 | -44.35122 | 2025-11-17 05:59:00 | AQUA_M-M | DOM PEDRO | MARANHÃO | Brasil | 2103802 | 21 | 33 | nan | nan | nan | Cerrado | 17.1 |
| 80e5c968-a380-31f6-9c75-f668531dc348 | -10.94576 | -48.68338 | 2025-11-17 05:59:00 | AQUA_M-M | BREJINHO DE NAZARÉ | TOCANTINS | Brasil | 1703701 | 17 | 33 | nan | nan | nan | Cerrado | 13.4 |
| d961f5c4-883b-3c4d-bc46-c5d48b87af83 | -3.86551 | -44.9905 | 2025-11-17 05:59:00 | AQUA_M-M | PIO XII | MARANHÃO | Brasil | 2108702 | 21 | 33 | nan | nan | nan | Amazônia | 25.3 |
| 6ccab763-ac08-386d-bf95-052379439392 | -11.82073 | -47.57875 | 2025-11-17 05:59:00 | AQUA_M-M | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 9.8 |
| 2e68f083-8868-3c0f-aced-1de5066a093c | -9.58218 | -49.11273 | 2025-11-17 05:59:00 | AQUA_M-M | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 7.4 |
| cf21f633-3d70-3d7f-b8c6-bf611aabd172 | -10.92725 | -48.68029 | 2025-11-17 05:59:00 | AQUA_M-M | BREJINHO DE NAZARÉ | TOCANTINS | Brasil | 1703701 | 17 | 33 | nan | nan | nan | Cerrado | 21.9 |
| 71934961-8a1e-3fc5-b49d-4e26a5196acf | -10.91326 | -49.40872 | 2025-11-17 05:59:00 | AQUA_M-M | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 7.9 |
| bec6993e-5ada-35ff-a551-d35797670c50 | -4.45184 | -43.97653 | 2025-11-17 05:59:00 | AQUA_M-M | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 5.9 |
| ab595a13-a920-3250-bf64-0a231ac151fb | -4.71858 | -46.3835 | 2025-11-17 05:59:00 | AQUA_M-M | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 329d839f-72ce-3260-ac37-f9b3a73b8d3d | -2.51376 | -47.8108 | 2025-11-17 05:59:00 | AQUA_M-M | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 41.0 |
| 9e35cf5e-9972-3bf6-8799-992b49694982 | -3.47387 | -49.6833 | 2025-11-17 05:59:00 | AQUA_M-M | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 8.0 |
| 69e48226-80b2-3df0-bf36-fc8ef06d15f2 | -3.8642 | -44.99922 | 2025-11-17 05:59:00 | AQUA_M-M | PIO XII | MARANHÃO | Brasil | 2108702 | 21 | 33 | nan | nan | nan | Amazônia | 63.2 |
| b0d87423-17a3-32a9-8ade-5a836535f88e | -3.87297 | -45.00051 | 2025-11-17 05:59:00 | AQUA_M-M | PIO XII | MARANHÃO | Brasil | 2108702 | 21 | 33 | nan | nan | nan | Amazônia | 34.6 |
| 49aa7be1-15f5-3a3d-88f3-fc2972c37cd4 | -10.90892 | -44.83969 | 2025-11-17 05:59:00 | AQUA_M-M | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 8a01c1eb-de0d-3577-8755-97ef48d7ad5c | -5.04199 | -43.60695 | 2025-11-17 05:59:00 | AQUA_M-M | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 5.6 |
| ca56304a-e949-3a17-a258-1c4db447ba61 | -3.39705 | -44.17619 | 2025-11-17 05:59:00 | AQUA_M-M | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 6.5 |
| c48213c1-c5fd-3531-81ea-7329628c9683 | -7.03351 | -47.61796 | 2025-11-17 05:59:00 | AQUA_M-M | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 208ac910-280b-34fb-b0c4-e2e775119135 | -4.71998 | -46.37441 | 2025-11-17 05:59:00 | AQUA_M-M | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 10.1 |
| 3293accc-cbbe-3b3c-af39-fb112e90cb8f | -6.30778 | -43.78959 | 2025-11-17 05:59:00 | AQUA_M-M | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 10.0 |
| a678f9ca-67c8-37c7-9a0a-26792acb0ccd | -8.5371 | -46.06735 | 2025-11-17 05:59:00 | AQUA_M-M | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 14.6 |
| 8cce6df8-8d00-3b9c-b5eb-2f9087007adc | -11.84455 | -49.2136 | 2025-11-17 05:59:00 | AQUA_M-M | CARIRI DO TOCANTINS | TOCANTINS | Brasil | 1703867 | 17 | 33 | nan | nan | nan | Cerrado | 6.5 |
| a6cb8ef3-674b-3a80-8bf6-df26a2edce32 | -10.6376 | -44.60398 | 2025-11-17 05:59:00 | AQUA_M-M | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 4.8 |
| f3e078a7-005d-3128-a74a-62ed098632db | -4.05877 | -47.49957 | 2025-11-17 05:59:00 | AQUA_M-M | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 7.8 |
| 453fbeee-f815-3e29-a953-4a32e0fdb11c | -6.68228 | -42.0332 | 2025-11-17 05:59:00 | AQUA_M-M | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 42.6 |
| ea3c6ff8-3dbb-332c-b6f4-dc6e5f047b43 | -10.94731 | -48.6736 | 2025-11-17 05:59:00 | AQUA_M-M | BREJINHO DE NAZARÉ | TOCANTINS | Brasil | 1703701 | 17 | 33 | nan | nan | nan | Cerrado | 135.9 |
| b38e57ab-e41b-32b0-8c8f-76cbfabe844b | -8.52832 | -46.06604 | 2025-11-17 05:59:00 | AQUA_M-M | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 10.2 |


[Clique aqui para ver as próximas entradas](README51.md)
