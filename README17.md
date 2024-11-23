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

## Dados Diários - Página 17

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| f2c156c9-fea0-347e-8756-17b8b672de77 | -3.7538 | -50.0152 | 2024-11-23 01:40:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 84.4 |
| e5f02719-2678-322b-9b3c-235156c40cb3 | -4.6085 | -46.5002 | 2024-11-23 01:40:00 | GOES-16 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 49.5 |
| 5f23ba32-f73e-36cc-b14b-d3085df89570 | -4.5402 | -42.93 | 2024-11-23 01:40:00 | GOES-16 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 87.0 |
| 2bf7f159-23e8-33e0-97d6-7a03ceac0b4d | -1.7359 | -52.7385 | 2024-11-23 01:40:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 72.1 |
| 758a752e-a965-32ac-bd80-07e7b65bd582 | -6.5054 | -47.0414 | 2024-11-23 01:40:00 | GOES-16 | SÃO JOÃO DO PARAÍSO | MARANHÃO | Brasil | 2111052 | 21 | 33 | nan | nan | nan | Cerrado | 69.6 |
| 522cef9d-9086-3ff4-a243-46ee7991d27d | -3.7539 | -49.9941 | 2024-11-23 01:40:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 59.5 |
| f7fc94e0-e03d-311d-a0eb-4f88fb6cd3b4 | -4.5614 | -48.0141 | 2024-11-23 01:40:00 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 65.0 |
| 360364ed-8527-3d32-a64a-77a6ba615116 | -1.6075 | -52.5977 | 2024-11-23 01:40:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 76.0 |
| 661093cf-ecba-3b8d-880d-4fc07d9c1fa4 | -2.6963 | -46.2719 | 2024-11-23 01:40:00 | GOES-16 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 71.4 |
| de64f1f0-b2de-35dd-a680-760df7f72c98 | -1.7359 | -52.7181 | 2024-11-23 01:40:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 113.0 |
| eebe6b09-71c6-3513-bb1f-ece05a5423cd | -3.2623 | -54.2192 | 2024-11-23 01:43:00 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 40dca854-0bf1-3173-b61c-413f631aa177 | -3.1282 | -53.0924 | 2024-11-23 01:43:00 | METOP-C | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 479c9090-ba9f-3bf5-abbe-2f67e4c79b89 | -21.320999 | -55.944599 | 2024-11-23 01:43:00 | METOP-C | NIOAQUE | MATO GROSSO DO SUL | Brasil | 5005806 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| f0eecfaa-de1d-3f7b-9b9c-ec134c987ef6 | -1.7337 | -52.704201 | 2024-11-23 01:43:00 | METOP-C | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6748fcc8-156b-3837-903c-8a0d6884ea23 | -3.2527 | -54.2215 | 2024-11-23 01:43:00 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 07affd8e-e066-3d0d-84fa-969e32b7a546 | -3.2431 | -54.223801 | 2024-11-23 01:43:00 | METOP-C | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5998d1f0-bc0c-31fc-9ccd-4d5ef592306b | -21.31503 | -55.94738 | 2024-11-23 01:43:00 | TERRA_M-M | NIOAQUE | MATO GROSSO DO SUL | Brasil | 5005806 | 50 | 33 | nan | nan | nan | Cerrado | 10.2 |
| 8cf05ade-7843-3959-b8bb-980d2dcf2ec7 | -21.31667 | -55.95806 | 2024-11-23 01:43:00 | TERRA_M-M | NIOAQUE | MATO GROSSO DO SUL | Brasil | 5005806 | 50 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 295130db-c10a-3307-a3a3-d83fa8166f94 | -3.70583 | -51.79591 | 2024-11-23 01:47:00 | TERRA_M-M | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 67.9 |
| f37afeac-cbc2-3be2-88b4-c3798e0b259d | -3.70724 | -51.79071 | 2024-11-23 01:47:00 | TERRA_M-M | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 57.0 |
| 0e0c7261-3bcd-3a13-a1e0-f0c11d90804d | -3.12418 | -53.11208 | 2024-11-23 01:47:00 | TERRA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 47.3 |
| 47feddf3-fd01-3a05-95c4-4a8115e48ba0 | -3.10829 | -53.11431 | 2024-11-23 01:47:00 | TERRA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 20.7 |
| 3ee94357-71b3-39c7-a95c-aaeab0661bfe | -3.23005 | -54.23124 | 2024-11-23 01:47:00 | TERRA_M-M | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 23.5 |
| be465041-f4d6-3e14-84d6-8870feb7a8f8 | -3.25013 | -54.24834 | 2024-11-23 01:47:00 | TERRA_M-M | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 74.7 |
| a13b640a-0dc1-39a1-9d3d-cd6c48f146bd | -3.26279 | -53.83084 | 2024-11-23 01:47:00 | TERRA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 21.6 |
| 0e93cc98-1460-328d-b483-38714f49cbae | -3.24837 | -54.25509 | 2024-11-23 01:47:00 | TERRA_M-M | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 39.9 |
| 970015be-e10c-3bce-938c-6b33c7213d5d | -2.82127 | -54.03644 | 2024-11-23 01:47:00 | TERRA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 25.3 |
| 7503f5d9-4da0-347c-8b64-2cbcbba4e2d0 | -3.06977 | -53.28302 | 2024-11-23 01:47:00 | TERRA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 25.1 |
| 5e43edc3-45f4-3377-8b3b-9d69932487d9 | -1.72481 | -52.74133 | 2024-11-23 01:47:00 | TERRA_M-M | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 56.0 |
| 858cc281-a01b-36be-abd3-01a8c5931c89 | -3.25695 | -53.28147 | 2024-11-23 01:47:00 | TERRA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 29.5 |
| abb32579-686e-3633-b784-34b4b9a0ed9c | -3.2778 | -53.82877 | 2024-11-23 01:47:00 | TERRA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 35.5 |
| 97546325-4ba6-3146-830b-3202d07f25ff | -1.61036 | -52.61967 | 2024-11-23 01:47:00 | TERRA_M-M | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 40.7 |
| 4e1b80e7-17f0-3423-a16b-699814766a02 | -1.7367 | -52.74661 | 2024-11-23 01:47:00 | TERRA_M-M | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 38.5 |
| 37ec4dba-9706-3abe-ad38-6435321fe1fd | -3.31847 | -53.29686 | 2024-11-23 01:47:00 | TERRA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 19.6 |
| 18f2cbb9-e434-3bb9-8047-9ebbcccad0ad | -1.78478 | -53.63087 | 2024-11-23 01:47:00 | TERRA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 38.2 |
| 09460b4e-b5a3-33cf-b430-c17e10eb80eb | -1.38644 | -55.19827 | 2024-11-23 01:47:00 | TERRA_M-M | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 18.7 |
| 6c719c31-e82a-3dd4-a1b4-5970dc2d72c6 | -3.24459 | -54.22916 | 2024-11-23 01:47:00 | TERRA_M-M | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 71.6 |
| dbe35884-ab7a-397e-a394-81a8632d7b3a | -1.78942 | -53.6617 | 2024-11-23 01:47:00 | TERRA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 31.2 |
| 5bd1c18b-ecfb-369c-b302-eda3b0b2349f | -1.60832 | -52.57647 | 2024-11-23 01:47:00 | TERRA_M-M | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 27.8 |
| 98170efc-61e7-311f-afc8-8d9ee6bf5909 | -3.23557 | -54.25013 | 2024-11-23 01:47:00 | TERRA_M-M | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 30.9 |
| 1d25befc-7a60-3466-a275-7d852ec13ed2 | -2.82163 | -54.04292 | 2024-11-23 01:47:00 | TERRA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 18.1 |
| f3d44575-f19a-3012-89bd-fa1308fc33bc | -1.77446 | -53.63784 | 2024-11-23 01:47:00 | TERRA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 24.9 |
| 297be08d-45f7-3a32-8857-2d18e4a358cd | -1.39186 | -55.19102 | 2024-11-23 01:47:00 | TERRA_M-M | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 24.4 |
| 65d306f7-c9aa-3f8b-8d0a-21a55248e090 | -3.05969 | -53.29165 | 2024-11-23 01:47:00 | TERRA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 34.9 |
| 2e3b9b55-364a-368e-bcfd-f222066c6383 | -3.18178 | -54.32311 | 2024-11-23 01:47:00 | TERRA_M-M | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 26.8 |
| b073271f-236b-3bf7-ae1c-b817358b3e6c | -1.60487 | -52.58208 | 2024-11-23 01:47:00 | TERRA_M-M | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 39.6 |
| 6a99148b-600e-3246-990b-3879ccc234db | -3.25126 | -53.27554 | 2024-11-23 01:47:00 | TERRA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 34.4 |
| 921b75d8-071e-3917-beb3-6176510532f6 | -1.61404 | -52.614 | 2024-11-23 01:47:00 | TERRA_M-M | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 52.7 |
| 19e05651-4c75-3981-8622-f35d4004fd26 | -3.24615 | -54.22233 | 2024-11-23 01:47:00 | TERRA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 48.7 |
| 6065e268-33fc-39a2-80a5-576651d85325 | -3.23453 | -53.94811 | 2024-11-23 01:47:00 | TERRA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 23.3 |
| 64183c53-10af-3a2d-8362-9bd66d6f2ed9 | -3.27647 | -53.82347 | 2024-11-23 01:47:00 | TERRA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 40.1 |
| 46f8da31-a988-32bd-bed6-70172e2ba374 | -2.7149 | -46.2713 | 2024-11-23 01:50:00 | GOES-16 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 59.2 |
| 3fade03d-82d3-3e19-98ab-edcfa15f8de4 | -4.67 | -45.6722 | 2024-11-23 01:50:00 | GOES-16 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 70.4 |
| c437853c-434e-3787-a331-d5823f820dac | -3.2569 | -54.2226 | 2024-11-23 01:50:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 115.5 |
| fe804425-8f7c-364b-9ba2-52949aad3bf1 | -2.6963 | -46.2719 | 2024-11-23 01:50:00 | GOES-16 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 67.7 |
| 30b7c32e-ffd7-356d-9f83-79d730628c9a | -3.2768 | -53.8199 | 2024-11-23 01:50:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 81.7 |
| e807c778-f69c-329e-a057-a571c2ec03a7 | -4.6085 | -46.5002 | 2024-11-23 01:50:00 | GOES-16 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 120.3 |
| ad916874-cbd0-3cdd-bf77-1deb44d325f9 | -3.2569 | -54.2426 | 2024-11-23 01:50:00 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 120.0 |
| ebf2c7a8-e5e6-344f-8c8a-6fec9f780c69 | -3.7538 | -50.0152 | 2024-11-23 01:50:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 86.3 |
| e31201c8-bcdb-32dd-8219-df00da032e6b | -4.706 | -45.8493 | 2024-11-23 01:50:00 | GOES-16 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 76.6 |
| 45e28333-6bd7-3ded-9b38-8a3e1562a522 | -1.6075 | -52.5977 | 2024-11-23 01:50:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 81.4 |
| 1600bdf2-23fc-3f95-8072-b8102c600102 | -9.326 | -40.2338 | 2024-11-23 01:50:00 | GOES-16 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 114.1 |
| 65381df7-f527-3ed4-be80-3d7aaaf4d21c | -4.5402 | -42.93 | 2024-11-23 01:50:00 | GOES-16 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 64.5 |
| 755001df-9e0d-302b-afcd-b8283cd3dfff | -4.5403 | -42.9066 | 2024-11-23 01:50:00 | GOES-16 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 113.0 |
| 71cc8a96-ccc7-3759-89b5-5bd69c4ea923 | -3.4747 | -50.4245 | 2024-11-23 01:50:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 47.6 |
| 7f22a52f-39a8-3860-9fd9-2195da641078 | -1.7359 | -52.7181 | 2024-11-23 01:50:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 118.5 |
| b8c2be0d-3505-3ba0-8559-a333ef022baa | -3.5159 | -53.8132 | 2024-11-23 01:50:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 55.9 |
| fd262ead-e9a3-33eb-b070-b2959fbd3185 | -4.5216 | -42.9078 | 2024-11-23 01:50:00 | GOES-16 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 85.8 |
| d3d99a68-4545-3862-8edb-20977a36746f | -4.5382 | -45.881 | 2024-11-23 01:50:00 | GOES-16 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 68.3 |
| 9b6e8212-0ca4-36a0-8cb6-691106eb463f | -3.6306 | -45.1399 | 2024-11-23 01:50:00 | GOES-16 | IGARAPÉ DO MEIO | MARANHÃO | Brasil | 2105153 | 21 | 33 | nan | nan | nan | Amazônia | 52.7 |
| 5d478d6e-b035-3862-ba3c-12c39e979e79 | -3.2386 | -54.223 | 2024-11-23 01:50:00 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 97.1 |
| 08593a87-7d11-30b5-aa3a-98c67a01bd63 | -3.2385 | -54.2431 | 2024-11-23 01:50:00 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 104.9 |
| 0cb77dfe-b0e1-38d4-b1d3-dff1e725c421 | -1.7359 | -52.7385 | 2024-11-23 01:50:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 70.8 |
| 2e8fc4e0-7922-3e86-a7bd-78c749c46ba3 | -4.6086 | -46.478 | 2024-11-23 01:50:00 | GOES-16 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 63.7 |
| 84ce8994-6503-3501-91a0-a07e1e47525a | -4.5402 | -42.93 | 2024-11-23 02:00:00 | GOES-16 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 71.3 |
| daad81fa-ef25-333e-ac72-2d6cb0c4f74c | -4.5382 | -45.881 | 2024-11-23 02:00:00 | GOES-16 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 71.5 |
| 315724b5-76d9-3518-88b0-276487ed8a52 | -3.2386 | -54.223 | 2024-11-23 02:00:00 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 100.0 |
| 3c249bc8-7e2e-3839-8e08-35ff8b939f8d | -3.7538 | -50.0152 | 2024-11-23 02:00:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 86.9 |
| d5ccabd3-f5da-3e1f-a853-585336ea81c8 | -4.6086 | -46.478 | 2024-11-23 02:00:00 | GOES-16 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 81.3 |
| bc652bb4-db8d-36d0-bc13-37e67577a44a | -4.5216 | -42.9078 | 2024-11-23 02:00:00 | GOES-16 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 82.9 |
| e91223a4-3e84-32d2-9f38-b8d4e650224f | -4.5403 | -42.9066 | 2024-11-23 02:00:00 | GOES-16 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 121.1 |
| c3d851e3-1a4c-3944-85eb-cd8a83dbcc61 | -3.2385 | -54.2431 | 2024-11-23 02:00:00 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 107.3 |
| 1c5c1723-cac9-3335-94f6-22c64d32de4f | -3.2768 | -53.8199 | 2024-11-23 02:00:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 76.1 |
| 71eb37f8-5bd6-3376-bbb7-7182e7df7e28 | -4.5898 | -46.5012 | 2024-11-23 02:00:00 | GOES-16 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 76.0 |
| e018f492-68b1-3e02-815e-1de0642c8174 | -3.2569 | -54.2226 | 2024-11-23 02:00:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 111.8 |
| f03b61d2-9469-35a8-8e89-59cdb6d2ef8d | -2.6963 | -46.2719 | 2024-11-23 02:00:00 | GOES-16 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 63.4 |
| 87eef770-d69d-3f10-9849-031dc8b2d94a | -6.5054 | -47.0414 | 2024-11-23 02:00:00 | GOES-16 | SÃO JOÃO DO PARAÍSO | MARANHÃO | Brasil | 2111052 | 21 | 33 | nan | nan | nan | Cerrado | 58.6 |
| a68fb932-9677-3b58-9ca1-50b6d7c60d5a | -1.7359 | -52.7385 | 2024-11-23 02:00:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 70.7 |
| ea58d1e7-d319-352f-a1b4-bbf2f9cb213e | -1.7359 | -52.7181 | 2024-11-23 02:00:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 122.6 |
| 2b8e13cf-60c5-3eea-97d3-9b890f04e6a5 | -2.7149 | -46.2713 | 2024-11-23 02:00:00 | GOES-16 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 60.2 |
| 545ebdb7-1469-384f-ad36-5597ca901be4 | -4.6085 | -46.5002 | 2024-11-23 02:00:00 | GOES-16 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 156.6 |
| c485fe44-a8dc-3f6c-8713-c35f19d5f1a8 | -1.6075 | -52.5977 | 2024-11-23 02:00:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 73.7 |
| 49791d6b-632e-3b02-b289-98d2f7bacdac | -3.2569 | -54.2426 | 2024-11-23 02:00:00 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 111.9 |
| 39537cb9-eb4d-349a-a5ac-08a6638acd2b | -2.6963 | -46.2719 | 2024-11-23 02:10:00 | GOES-16 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 57.5 |
| 266d12f5-9e2e-361c-a50a-1f14341dca1f | -3.2572 | -45.426 | 2024-11-23 02:10:00 | GOES-16 | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | 56.4 |
| 1c97e86f-6994-34a5-8e56-8f1d5eecb508 | -4.5382 | -45.881 | 2024-11-23 02:10:00 | GOES-16 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 72.5 |
| 1098752c-5a2b-3251-990e-263419fcfb9f | -4.5403 | -42.9066 | 2024-11-23 02:10:00 | GOES-16 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 101.7 |
| 43f03a00-6b79-3475-a84e-6be7b3bb5f52 | -3.2768 | -53.8199 | 2024-11-23 02:10:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 72.3 |
| 68aaf72d-c836-3937-bb88-3de9d953050a | -3.2569 | -54.2426 | 2024-11-23 02:10:00 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 87.7 |
| c9a0a5d0-d55a-316b-aa8d-e4a1feaca1e4 | -1.7359 | -52.7181 | 2024-11-23 02:10:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 123.9 |


[Clique aqui para ver as próximas entradas](README18.md)
