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
| f8398ae9-3ea9-3254-8837-fadbb9fc8672 | -4.35056 | -45.79035 | 2024-11-25 04:33:00 | NOAA-21 | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 5a71c4c6-0117-3553-b3d4-18292ecb2fe7 | -4.49803 | -49.63607 | 2024-11-25 04:33:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 24a7dc61-2f43-3755-b68f-93c869995d3d | -4.30528 | -46.57043 | 2024-11-25 04:33:00 | NOAA-21 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 7e0c1b64-6113-36da-bde4-d748c0175e68 | -3.52442 | -53.5109 | 2024-11-25 04:33:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9bce1b86-41fe-3dab-a7f1-383ecfd7c3c8 | -3.9772 | -49.93507 | 2024-11-25 04:33:00 | NOAA-21 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 2a79db82-6841-3472-9b62-92e431abe5e8 | -3.54719 | -51.53507 | 2024-11-25 04:33:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| e9178229-227f-33a3-bd39-c59fa058e8c6 | -3.55099 | -51.53561 | 2024-11-25 04:33:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 014e0c0d-72e9-37e4-8fcc-a148b2967918 | -2.80756 | -53.01492 | 2024-11-25 04:33:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| a3a5fb92-5707-37db-a429-07c0ef7c8c25 | -5.9016 | -43.40961 | 2024-11-25 04:33:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 2d72da0c-7a8a-3c6b-a9da-ed0e95825c29 | -3.27895 | -50.42936 | 2024-11-25 04:33:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 99636c0c-3a26-34f7-893f-ac913cd2ce10 | -2.66045 | -46.56541 | 2024-11-25 04:33:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 72a0f88c-92a4-3186-960b-172dad482604 | -4.03217 | -48.08534 | 2024-11-25 04:33:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| b024fb54-3522-3a70-9333-d551fa24bb71 | -3.89597 | -46.66837 | 2024-11-25 04:33:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 2c3191b3-655c-3a0b-86ec-9b2ba89f0c84 | -2.54853 | -46.54121 | 2024-11-25 04:33:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 04634a36-4994-301f-82ae-7b64d9da68d0 | -4.2608 | -48.68907 | 2024-11-25 04:33:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| fa9c294a-9059-37a1-af0b-2f5e694e2058 | -2.80225 | -54.11084 | 2024-11-25 04:33:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| d4e7a55d-5194-374e-b937-8e7b7548745b | -3.34644 | -46.61556 | 2024-11-25 04:33:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 4ba627a8-0f81-3f14-b188-f3431cf85c0c | -2.73619 | -46.01448 | 2024-11-25 04:33:00 | NOAA-21 | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3b29c568-69b2-3c7c-a044-a0de856677d4 | -2.58587 | -46.56459 | 2024-11-25 04:33:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 1a549729-0815-39a3-b86a-7d60495d5c00 | -3.7885 | -49.855 | 2024-11-25 04:33:00 | NOAA-21 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 76288832-523c-342a-8a93-deff948a4663 | -1.60199 | -52.58487 | 2024-11-25 04:33:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0f106747-286f-3176-9e8b-f059ada28c9e | -4.62175 | -45.55362 | 2024-11-25 04:33:00 | NOAA-21 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 88d64407-fa6c-3e56-ac8f-d763057a8455 | -2.54028 | -46.39777 | 2024-11-25 04:33:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 74291051-5883-3fd3-bdad-0478ecfdb542 | -1.48056 | -51.9608 | 2024-11-25 04:33:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 0c5a2e1c-a94a-33c5-9b76-1e7c44b37a44 | -1.97268 | -56.14042 | 2024-11-25 04:33:00 | NOAA-21 | TERRA SANTA | PARÁ | Brasil | 1507979 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 23cfe3a6-8aeb-312b-9266-cb1ef9375f54 | -2.67299 | -46.15656 | 2024-11-25 04:33:00 | NOAA-21 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e5ad157f-b569-311c-972d-8a65e4f652cd | -3.61935 | -52.2061 | 2024-11-25 04:33:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| fe4406ce-10bf-3a7b-bb4b-ee068d7ed782 | -1.78084 | -52.73513 | 2024-11-25 04:33:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 7.8 |
| e4d57641-af2c-363e-8c18-e89c3ec65e59 | -3.10225 | -51.50111 | 2024-11-25 04:33:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 4a15a96f-3460-3f95-8558-14a61e82ef69 | -2.70338 | -46.2905 | 2024-11-25 04:33:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 42226070-c114-34a7-9f4a-511cf2eaa90b | -3.82427 | -52.23631 | 2024-11-25 04:33:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 385edfd7-2ab3-321f-8604-1cf0a6000f5c | -4.07309 | -46.09138 | 2024-11-25 04:33:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| fe7b3a4b-05fb-3869-9f63-ba5281080b12 | -2.64285 | -46.13029 | 2024-11-25 04:33:00 | NOAA-21 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 087820f5-ad94-3a65-8dda-7d0fa51d5649 | -1.60165 | -52.57755 | 2024-11-25 04:33:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 795d23a3-3362-31cb-af85-c68e49b438f3 | -1.19185 | -53.88438 | 2024-11-25 04:33:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 086076e4-2696-3d31-9fd3-4789ca0f0bbf | -4.17973 | -46.83364 | 2024-11-25 04:33:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| df31381e-4585-3ab0-9dc7-9d6b8f0fd92b | -4.13509 | -46.70543 | 2024-11-25 04:33:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 302ebc9e-1024-38c1-aabf-68ee0364bea7 | -1.17638 | -54.12694 | 2024-11-25 04:33:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 4206e87e-824b-38f8-a244-b7456b85e01d | -2.60939 | -53.96589 | 2024-11-25 04:33:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| f2db1ba8-f01e-33c7-889b-7c3a928114c4 | -2.64742 | -51.7731 | 2024-11-25 04:33:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 2c13cb6b-0cda-3ab9-a317-ab2d6fa54693 | -3.41888 | -53.28667 | 2024-11-25 04:33:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 8c88a07b-fafd-32db-b06f-fe204d3af1c0 | -3.96849 | -46.72652 | 2024-11-25 04:33:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| b12f208b-4102-3ab3-b9f3-21699564af50 | -3.19466 | -46.36665 | 2024-11-25 04:33:00 | NOAA-21 | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d7f78b85-7507-3d5e-9f93-2d1da4baca8f | -7.87717 | -46.69516 | 2024-11-25 04:33:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| f9f18782-6c71-3f36-8725-7b0a0a0ffff7 | -4.24298 | -48.67188 | 2024-11-25 04:33:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 18097354-3ed0-3efa-a97e-ac37d09f31fb | -3.19197 | -46.5593 | 2024-11-25 04:33:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 79b3d287-2ba4-3a3e-8969-f16ac1c70bea | -3.46164 | -50.83257 | 2024-11-25 04:33:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 10.5 |
| f3713dd6-d65a-3f8b-9a5d-3f6948335dfe | -2.7156 | -46.27496 | 2024-11-25 04:33:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 26506740-1d64-39c6-9af9-34af0be9c9a2 | -2.68612 | -46.26992 | 2024-11-25 04:33:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| a579bb1f-866d-37ab-8166-34f222093a1e | -3.38399 | -50.73066 | 2024-11-25 04:33:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 8f577adb-8c40-3dfa-a4bc-247090027851 | -5.58758 | -45.20462 | 2024-11-25 04:33:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 386a79f3-9cc6-3109-826a-280e9597110c | -7.26361 | -49.51299 | 2024-11-25 04:33:00 | NOAA-21 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 26da7a8d-e114-3bc5-ad6f-99c128560906 | -4.54589 | -46.66486 | 2024-11-25 04:33:00 | NOAA-21 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| ef5a00fa-ef5e-377c-9ce4-9c6c3d974c2e | -3.04701 | -54.0239 | 2024-11-25 04:33:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ffafa616-719b-3710-94f8-2757f23eda6a | -3.25445 | -54.22288 | 2024-11-25 04:33:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| bf93a3d7-50e7-3bae-864d-0bb0ee131961 | -2.81969 | -54.11835 | 2024-11-25 04:33:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| d60e41bb-07a7-39a4-928d-4f4bd3999572 | -3.80904 | -51.37962 | 2024-11-25 04:33:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 413f9192-aa27-36d2-9a57-03ef100b29a2 | -3.94759 | -46.5114 | 2024-11-25 04:33:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 32b676c3-436a-3589-ba10-a1c2044d587f | -3.24079 | -54.22072 | 2024-11-25 04:33:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 73a68a75-b1ae-39e3-96da-0a75640b4f2c | -3.69029 | -49.78854 | 2024-11-25 04:33:00 | NOAA-21 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 31b7ae85-7778-38cb-928a-b9c1f87d6c78 | -4.0397 | -46.66247 | 2024-11-25 04:33:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 37d8c2dc-074c-3d6e-99ca-a10c265fd432 | -4.13726 | -48.76041 | 2024-11-25 04:33:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 61f63a43-ef10-3ba6-ae15-a6ae5ad0e331 | -2.92462 | -51.77196 | 2024-11-25 04:33:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 72d4b58f-5c2c-3115-b535-97172f7f4060 | -2.80149 | -54.11544 | 2024-11-25 04:33:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 8e62f948-6f8b-361b-8f15-62d50542ef87 | -3.99692 | -46.49782 | 2024-11-25 04:33:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c3e71b12-95cc-35f5-9d20-683a665ada45 | -8.79712 | -47.5993 | 2024-11-25 04:33:00 | NOAA-21 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 818a629f-6dd9-314e-a98e-3717114bcbea | -3.7786 | -51.87507 | 2024-11-25 04:33:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| c72fa769-29a0-3323-aa02-12e19b4eeb5d | -4.9525 | -49.99813 | 2024-11-25 04:33:00 | NOAA-21 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 2bbe8f13-750d-3cf8-9d36-0ca8be0ef829 | -4.2391 | -48.69652 | 2024-11-25 04:33:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 4eb950b8-22e0-3c39-bfe5-e32ce06c331d | -4.91404 | -48.60151 | 2024-11-25 04:33:00 | NOAA-21 | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 38cf1fac-c0bc-3f6a-8fc4-4ba90ddbb6e7 | -5.18802 | -46.13795 | 2024-11-25 04:33:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7596c0ac-0f3e-3200-94cd-ac4680818263 | -3.51841 | -53.81891 | 2024-11-25 04:33:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 8cc8e22b-2dfc-3895-bbf0-54fc6ad32e82 | -3.25639 | -53.26976 | 2024-11-25 04:33:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a349ce45-0943-3d07-aadd-b274dc510471 | -3.2613 | -53.26649 | 2024-11-25 04:33:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 446fc6ee-4916-331e-ad1c-af887d9f6348 | -2.82973 | -51.28883 | 2024-11-25 04:33:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 86a25563-202d-3dcf-8dbb-b7fd9cc386f9 | -4.28464 | -45.91937 | 2024-11-25 04:33:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 2.3 |
| fc2cf54f-096e-374a-bc00-96319d63a8be | -3.52153 | -52.75068 | 2024-11-25 04:33:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ac2eef08-40fe-37d5-93e8-05b5ca9a02e7 | -4.3296 | -46.83226 | 2024-11-25 04:33:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7fb90161-19dd-318e-a5af-763e3da56eae | -2.89359 | -45.31937 | 2024-11-25 04:33:00 | NOAA-21 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 8b7d6d47-92f1-30ff-804d-09391aa304ab | -3.97875 | -49.97073 | 2024-11-25 04:33:00 | NOAA-21 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| f43cce6f-cb86-3121-9580-10b040a81ce0 | -3.30077 | -45.68144 | 2024-11-25 04:33:00 | NOAA-21 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 8.0 |
| 6f6bffe1-bc9f-30f3-90c7-b90783967aef | -1.41756 | -52.41036 | 2024-11-25 04:33:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 223ff12d-cb1a-3260-b640-40114d3a3e66 | -3.97128 | -46.7305 | 2024-11-25 04:33:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 22156202-30bb-38b5-a866-a48b94fdba45 | -4.19734 | -50.67049 | 2024-11-25 04:33:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 786d60d1-7438-31ae-b571-0fb3ce8d804e | -1.45467 | -53.40685 | 2024-11-25 04:33:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| f6aa63fc-d525-3e07-b80d-67d685652fc1 | -4.51347 | -44.59758 | 2024-11-25 04:33:00 | NOAA-21 | PEDREIRAS | MARANHÃO | Brasil | 2108207 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e94ede39-cdb8-35d8-9b1d-7b293d84b3ae | -2.59917 | -46.2604 | 2024-11-25 04:33:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f8ca771d-467c-34d7-9599-64d48dc7d697 | -3.0559 | -53.22279 | 2024-11-25 04:33:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 0dafc16c-fb09-336e-ba4d-c4ad3d6e1d88 | -3.34976 | -46.61607 | 2024-11-25 04:33:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9ca4e313-ad95-3a66-876b-ad541819dd59 | -3.39531 | -44.73952 | 2024-11-25 04:33:00 | NOAA-21 | ARARI | MARANHÃO | Brasil | 2101004 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f7193c4d-33ab-3a8f-8eda-14faa2999873 | -2.69922 | -46.18578 | 2024-11-25 04:33:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e962bdfe-0aa1-3ce7-8493-96729db29cfa | -4.24855 | -47.98534 | 2024-11-25 04:33:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 662cd999-0e34-3bc0-a893-3495b4829395 | -4.03603 | -48.08238 | 2024-11-25 04:33:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| c5d0dec3-cf30-3fce-a9a2-d8eea2138a80 | -2.56628 | -54.05839 | 2024-11-25 04:33:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 6ef200c8-dbf3-308f-80f2-6ec7205a8ce6 | -2.66772 | -51.7211 | 2024-11-25 04:33:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c7f60bca-7026-30b9-b7f0-0b8330f8227e | -3.70893 | -52.42057 | 2024-11-25 04:33:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| a7763139-4152-33db-9c3d-6477a5fb5c8a | -3.83803 | -46.53785 | 2024-11-25 04:33:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 1a763dad-aee1-3a4c-b6f4-c709d15bac5a | -2.80695 | -53.01874 | 2024-11-25 04:33:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| cb824264-bedb-3b0d-ad5a-d054bb292056 | -7.57969 | -49.40692 | 2024-11-25 04:33:00 | NOAA-21 | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 83978f7f-25fa-3556-9a4f-c13bc4384afc | -4.62771 | -50.5481 | 2024-11-25 04:33:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |


[Clique aqui para ver as próximas entradas](README25.md)
