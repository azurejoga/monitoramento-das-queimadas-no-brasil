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

## Dados Diários - Página 20

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 82ed0eb6-dedf-3105-ac5a-d9eae00d7479 | -2.65725 | -53.36399 | 2024-10-11 00:58:00 | TERRA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 10.0 |
| e81993be-53e4-31d2-8571-7707b3ecabbc | -2.65544 | -53.35073 | 2024-10-11 00:58:00 | TERRA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 161.1 |
| 08f8013a-25d6-3a61-a746-abb55d9a7851 | -1.59457 | -53.34604 | 2024-10-11 00:58:00 | TERRA_M-M | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 43.3 |
| ced55848-54ec-3fff-b16e-356a79d8d074 | -1.1791 | -53.38867 | 2024-10-11 00:58:00 | TERRA_M-M | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 8.4 |
| e384b924-2e38-3da2-afd1-44103674ea8c | -1.17036 | -53.40277 | 2024-10-11 00:58:00 | TERRA_M-M | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 18.7 |
| a6e9e671-6477-3b75-8e9e-c13e30e96c61 | -1.15987 | -53.40419 | 2024-10-11 00:58:00 | TERRA_M-M | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 30.8 |
| 22a33371-7e4c-391c-b247-a0dcfb2118b1 | -1.1436 | -54.21773 | 2024-10-11 00:58:00 | TERRA_M-M | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 16.2 |
| 8e4d995e-c5a9-36d2-b055-5bab552599e6 | -1.02136 | -53.73736 | 2024-10-11 00:58:00 | TERRA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 11.5 |
| 9809e6d9-429a-3e05-ba92-3ae8a91cbb40 | -1.01954 | -53.724 | 2024-10-11 00:58:00 | TERRA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 8.0 |
| d5a3af81-c28e-3b65-8633-18be4b71924c | -1.01594 | -53.7304 | 2024-10-11 00:58:00 | TERRA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 8.3 |
| b9384099-e098-35df-ad36-a184978760a7 | -2.80302 | -54.09227 | 2024-10-11 00:58:00 | TERRA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 9.5 |
| a7a42cec-764f-3886-bd7b-ecb140f8f789 | -2.80152 | -54.08627 | 2024-10-11 00:58:00 | TERRA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 18.1 |
| b35ae801-7452-371b-b68a-988c2d0d3690 | -2.80091 | -54.07721 | 2024-10-11 00:58:00 | TERRA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 14.3 |
| 875a8b6b-dacc-3e68-8656-4e93e73fce79 | -1.52553 | -55.42458 | 2024-10-11 00:58:00 | TERRA_M-M | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 23.2 |
| c57df133-8c3d-3098-ad2a-acfd79a5bd96 | -1.52067 | -55.41306 | 2024-10-11 00:58:00 | TERRA_M-M | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 16.8 |
| e8a81079-71d2-3cbd-8d8d-67b191579f9f | -12.76 | -44.89 | 2024-10-11 01:04:12 | MSG-03 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| bb90cacf-255d-3a56-a677-08a7a7909ac4 | -12.76 | -44.84 | 2024-10-11 01:04:12 | MSG-03 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 823a3342-3298-3047-97ff-b4bf690a5af0 | -12.79 | -44.9 | 2024-10-11 01:04:12 | MSG-03 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 303715bd-ec49-3d59-b00e-f5b93f9b23be | -10.11 | -36.18 | 2024-10-11 01:04:25 | MSG-03 | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 87919e3a-4954-341a-9f84-d91a1b5c0e72 | -2.96 | -52.89 | 2024-10-11 01:05:10 | MSG-03 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1d32d5ae-65e7-3925-b782-4ab57c6e9603 | -2.6533 | -53.3506 | 2024-10-11 01:05:21 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 152.3 |
| b5e5be12-ea53-3297-af2c-1887f090e7f3 | -2.6716 | -53.3502 | 2024-10-11 01:05:21 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 104.2 |
| 37d2d153-89b3-369b-8c2f-7b03a9a4c4f7 | -2.7847 | -52.4933 | 2024-10-11 01:05:22 | GOES-16 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 199.6 |
| c1905a28-f37d-31db-a90a-7a1ab04dbf7c | -2.7848 | -52.4728 | 2024-10-11 01:05:22 | GOES-16 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 169.3 |
| 37895069-e666-3802-b7db-b84c570e694d | -2.8081 | -51.0084 | 2024-10-11 01:05:22 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 66.1 |
| 71ada49b-c15b-359e-8617-ec9ea4f6aaa5 | -2.9673 | -52.9169 | 2024-10-11 01:05:23 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 103.8 |
| a32ae6a5-9d72-31c3-b174-2dc84568345f | -2.9673 | -52.8966 | 2024-10-11 01:05:23 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 136.3 |
| 6bfdd3d7-9657-3ac5-968b-e079b0b952c3 | -2.9857 | -52.9164 | 2024-10-11 01:05:23 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 149.0 |
| a62017ee-f599-3bb5-831d-1449c55f3591 | -2.9857 | -52.8961 | 2024-10-11 01:05:23 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 157.4 |
| e7b5320d-bdf2-34a1-a61d-29c91a8644a0 | -3.0343 | -61.6918 | 2024-10-11 01:05:24 | GOES-16 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 44.3 |
| f9fc8c98-dcab-385b-bf28-8413c65d32b4 | -3.0343 | -61.673 | 2024-10-11 01:05:24 | GOES-16 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 58.9 |
| 79ccd85a-3cc0-3fda-a258-7b43a02d3f82 | -3.0525 | -61.6916 | 2024-10-11 01:05:24 | GOES-16 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 36.1 |
| 06d57b08-a5f9-32be-8a21-1ebb1e54f79f | -3.0525 | -61.6727 | 2024-10-11 01:05:24 | GOES-16 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 44.3 |
| 39be5454-3175-37f4-9f49-a29cb89cdc66 | -3.1423 | -50.4352 | 2024-10-11 01:05:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 86.4 |
| 0d942671-5d8b-308d-9fb7-9e0e8a09332b | -3.1607 | -50.4556 | 2024-10-11 01:05:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 93.0 |
| 5d0354dd-a2c6-3243-be8b-f47aea1fe286 | -3.1608 | -50.4347 | 2024-10-11 01:05:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 175.4 |
| 6523f23e-2c87-341a-90aa-518a047546a3 | -3.3097 | -46.0946 | 2024-10-11 01:05:25 | GOES-16 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 56.2 |
| ce7c63df-a123-380e-8b8f-ea0abcf93ca5 | -3.3098 | -46.0724 | 2024-10-11 01:05:25 | GOES-16 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 91.1 |
| ae915eae-6ce3-3613-99a5-b1dc9965217a | -3.614 | -44.7783 | 2024-10-11 01:05:27 | GOES-16 | ARARI | MARANHÃO | Brasil | 2101004 | 21 | 33 | nan | nan | nan | Amazônia | 56.7 |
| c6473a73-a0c6-38b6-90c4-8a247f56df06 | -3.9207 | -46.468 | 2024-10-11 01:05:28 | GOES-16 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 54.0 |
| dd85f0a8-92cf-337e-9a4f-d97ffd743eef | -4.0962 | -48.2523 | 2024-10-11 01:05:29 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 152.2 |
| d905ec86-3d55-3846-8dc5-7fb05d222457 | -4.0963 | -48.2307 | 2024-10-11 01:05:29 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 67.0 |
| 45df0c94-a569-3c68-a023-529aa9cc7cfa | -4.1146 | -48.2731 | 2024-10-11 01:05:30 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 50.0 |
| eab36206-f8ce-3859-ba0b-ae1be302ded5 | -4.1148 | -48.2515 | 2024-10-11 01:05:30 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 266.6 |
| fc3d56f3-746e-32a5-aa7f-6bc24e111962 | -4.1149 | -48.2299 | 2024-10-11 01:05:30 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 116.5 |
| 682c30b1-53da-3fde-87e1-0bd519d8594e | -4.1333 | -48.2507 | 2024-10-11 01:05:30 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 60.5 |
| 5495d02f-feb1-3193-9f8a-4ff5ba9623b3 | -5.3265 | -60.1239 | 2024-10-11 01:05:37 | GOES-16 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 67.8 |
| 1e8a284d-996d-3e9d-8115-632ec34ba5c0 | -6.5589 | -60.0252 | 2024-10-11 01:05:44 | GOES-16 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 75.4 |
| 9154283e-e1c6-302d-9bf3-e6fa0e910589 | -6.747 | -59.3259 | 2024-10-11 01:05:45 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 63.5 |
| 43498014-0567-395f-b7db-a78decb9e8bb | -6.9097 | -47.7572 | 2024-10-11 01:05:45 | GOES-16 | WANDERLÂNDIA | TOCANTINS | Brasil | 1722081 | 17 | 33 | nan | nan | nan | Cerrado | 66.4 |
| 781697c1-3251-3997-9cba-d94ea7ad9775 | -6.9284 | -47.7558 | 2024-10-11 01:05:45 | GOES-16 | WANDERLÂNDIA | TOCANTINS | Brasil | 1722081 | 17 | 33 | nan | nan | nan | Cerrado | 116.3 |
| 386a8866-84b0-3197-9fe6-e9dbac8b621d | -6.9286 | -47.7339 | 2024-10-11 01:05:45 | GOES-16 | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 87.1 |
| b94d2fe1-f512-320b-8405-81ae06fd1b3f | -8.4417 | -55.4692 | 2024-10-11 01:05:54 | GOES-16 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 82.3 |
| 8003fc40-bcb0-3234-92e9-c0ef39dc23fa | -9.2896 | -46.5651 | 2024-10-11 01:05:59 | GOES-16 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 80.1 |
| 98043753-0f5d-3b72-b265-927ebf1f7c45 | -9.5303 | -42.9946 | 2024-10-11 01:06:00 | GOES-16 | CAMPO ALEGRE DE LOURDES | BAHIA | Brasil | 2905909 | 29 | 33 | nan | nan | nan | Caatinga | 99.6 |
| 3a89dd5e-e118-30c8-b4c3-26dc5a0214bf | -10.1058 | -36.1748 | 2024-10-11 01:06:02 | GOES-16 | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | 108.9 |
| 0bc68e8d-17ba-3745-b595-db8150a750e9 | -10.1252 | -36.1713 | 2024-10-11 01:06:02 | GOES-16 | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | 74.1 |
| f0d70370-98a4-348f-9011-c6491d89306d | -9.6389 | -64.9664 | 2024-10-11 01:06:02 | GOES-16 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 76.4 |
| a2191302-7a2d-3714-919e-78d21f5f40c8 | -9.6575 | -64.9658 | 2024-10-11 01:06:02 | GOES-16 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 70.5 |
| 2752ca0d-7e17-34e4-9427-ce22cbdfcd0a | -10.3632 | -55.8554 | 2024-10-11 01:06:05 | GOES-16 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 67.4 |
| ff1d4b1a-5d1b-31e0-9c19-6e3cabda6de6 | -10.4713 | -49.9838 | 2024-10-11 01:06:06 | GOES-16 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 72.0 |
| 6c3d396e-3a3f-323a-b8c1-245e089d814d | -10.4716 | -49.9624 | 2024-10-11 01:06:06 | GOES-16 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 52.7 |
| 8c8e4304-0f14-3f60-b8bb-0f8700c0c038 | -10.5755 | -64.0438 | 2024-10-11 01:06:07 | GOES-16 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 62.4 |
| 8da70801-1908-3ea5-9d38-7fb73b9520c4 | -10.6962 | -53.0354 | 2024-10-11 01:06:07 | GOES-16 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 144.1 |
| fbed0142-d65b-3dfe-abdf-930d450575b7 | -10.6965 | -53.0147 | 2024-10-11 01:06:07 | GOES-16 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 118.1 |
| 32503674-c838-36fa-91c0-6706bc87f7dd | -10.7059 | -64.1138 | 2024-10-11 01:06:08 | GOES-16 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 63.0 |
| 2e8542a9-ffba-31ec-9d31-342a13a67511 | -11.2407 | -53.2738 | 2024-10-11 01:06:10 | GOES-16 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 79.4 |
| 6d88a5a3-479d-33f8-819c-25d9d3139298 | -11.2716 | -50.9654 | 2024-10-11 01:06:10 | GOES-16 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 54.1 |
| 5f335146-86c1-37af-ab7f-ab051da32a33 | -11.2597 | -53.272 | 2024-10-11 01:06:10 | GOES-16 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 77.1 |
| 269adbda-a272-34c8-9ee3-c7d3927c0f71 | -11.2909 | -50.9421 | 2024-10-11 01:06:10 | GOES-16 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 62.2 |
| 1ab29daa-1865-35f3-8fd9-2516167285a7 | -11.2912 | -50.9208 | 2024-10-11 01:06:10 | GOES-16 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 64.5 |
| 9dfc6d96-bfc4-38b8-b873-14ec30c46903 | -12.5717 | -53.0753 | 2024-10-11 01:06:17 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 64.7 |
| 0e2c6f18-1f1c-380f-9c66-5939477c8a98 | -12.9658 | -53.511 | 2024-10-11 01:06:20 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 62.3 |
| 0dc867b4-5fbf-3a34-804f-739f1b61f305 | -12.9661 | -53.4902 | 2024-10-11 01:06:20 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 72.1 |
| 23190cd9-9c7d-3f94-adad-bfbef5979f02 | -12.9852 | -53.4881 | 2024-10-11 01:06:20 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 89.3 |
| 69023508-bc61-343b-b1c3-a725fa65b3c1 | -12.9855 | -53.4673 | 2024-10-11 01:06:20 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 98.8 |
| 35ed7ee4-fc6f-36cd-833e-e7d834b1294c | -2.6533 | -53.3506 | 2024-10-11 01:15:21 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 119.0 |
| 34cd8fcd-8b08-342b-86cd-4b8e41e8a995 | -2.6716 | -53.3502 | 2024-10-11 01:15:21 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 128.0 |
| d4d816f2-c394-3e8b-8fc6-92ca0779d6cc | -2.7663 | -52.4937 | 2024-10-11 01:15:22 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 63.5 |
| a3d12c3d-196a-34f7-af34-682d6302aad1 | -2.7664 | -52.4733 | 2024-10-11 01:15:22 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 66.0 |
| ef0aaa0b-b5d7-383a-b2d6-473de9f3864f | -2.7847 | -52.4933 | 2024-10-11 01:15:22 | GOES-16 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 124.4 |
| 9ca50c19-adbe-3cd6-a981-4c7745580bc1 | -2.7848 | -52.4728 | 2024-10-11 01:15:22 | GOES-16 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 121.7 |
| 3de998eb-487d-3449-939e-ced1348ac39e | -2.9674 | -47.9931 | 2024-10-11 01:15:23 | GOES-16 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 46.0 |
| f72b8f3a-0257-34f9-ae6c-9620014b4646 | -2.9673 | -52.9169 | 2024-10-11 01:15:23 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 127.3 |
| 0b0f5f01-aed0-3068-a282-7198915abfa9 | -2.9673 | -52.8966 | 2024-10-11 01:15:23 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 125.8 |
| e2009d0d-c096-30ce-a03a-fec1577e48bd | -2.9857 | -52.9164 | 2024-10-11 01:15:23 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 151.6 |
| 04ff5103-21ff-3049-bd83-e2a3e5792a67 | -2.9857 | -52.8961 | 2024-10-11 01:15:23 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 133.6 |
| 2415422c-0a3b-36a0-a49b-3b32487ea080 | -3.0343 | -61.6918 | 2024-10-11 01:15:24 | GOES-16 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 35.1 |
| 9309106f-942f-3fc3-b0ef-143cc1f624b5 | -3.0343 | -61.673 | 2024-10-11 01:15:24 | GOES-16 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 36.3 |
| 418cd48e-d4b4-3129-8050-cd2bb76b4343 | -3.0525 | -61.6916 | 2024-10-11 01:15:24 | GOES-16 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 40.1 |
| 8ac01062-aeb7-392c-b3dd-724b4f987985 | -3.0525 | -61.6727 | 2024-10-11 01:15:24 | GOES-16 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 44.0 |
| 6df75ad2-a69d-3e68-8298-0d30475442ac | -3.1422 | -50.4562 | 2024-10-11 01:15:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 63.1 |
| 6240833f-fbbb-3b95-8c60-e4be888a9d78 | -3.1423 | -50.4352 | 2024-10-11 01:15:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 111.3 |
| 285e0f48-0a43-3d35-8434-5832050fdb84 | -3.1607 | -50.4556 | 2024-10-11 01:15:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 76.6 |
| 52cd2ef1-7fd0-385d-82ad-aa9b7ff34239 | -3.1608 | -50.4347 | 2024-10-11 01:15:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 137.8 |
| 0fcb46d0-4e74-3acd-b78c-e337dbb5a90a | -3.2912 | -46.0731 | 2024-10-11 01:15:25 | GOES-16 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 53.9 |
| 503a4b34-9260-33fc-a90a-c2015c0d2e2c | -3.3096 | -50.1781 | 2024-10-11 01:15:25 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 57.1 |
| 2f7f9ce7-f847-3165-b2be-80f27a35b9a6 | -3.9393 | -46.4672 | 2024-10-11 01:15:28 | GOES-16 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 58.4 |
| 6995dfeb-e3cc-370e-96ec-2880d917b0dd | -4.0962 | -48.2523 | 2024-10-11 01:15:29 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 37.8 |
| ab7bab0d-6204-3ee5-8228-bd74cf883b7d | -4.1146 | -48.2731 | 2024-10-11 01:15:30 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 33.7 |


[Clique aqui para ver as próximas entradas](README21.md)
