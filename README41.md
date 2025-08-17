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

## Dados Diários - Página 41

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 95cc47d9-1000-3f22-b129-72fe4f91a288 | -12.82453 | -45.98399 | 2025-08-17 11:55:00 | TERRA_M-M | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 39.6 |
| 0bc418b3-6ec8-3776-ad1a-bcb5dcce116f | -11.91743 | -46.74492 | 2025-08-17 11:55:00 | TERRA_M-M | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 10.2 |
| 0130b19e-4bae-3d57-9b87-2b952cab3ab8 | -11.75913 | -46.44163 | 2025-08-17 11:55:00 | TERRA_M-M | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 10.0 |
| 9574f650-9cf9-360e-a4b1-2d6a735b72dc | -11.89772 | -43.42844 | 2025-08-17 11:55:00 | TERRA_M-M | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 16.5 |
| bb34162e-1dfd-3d77-a882-9a9112531d81 | -9.77043 | -41.90572 | 2025-08-17 11:55:00 | TERRA_M-M | SENTO SÉ | BAHIA | Brasil | 2930204 | 29 | 33 | nan | nan | nan | Caatinga | 6.3 |
| 91340b48-417b-34e6-adee-3ca89f034c8e | -12.19282 | -47.23559 | 2025-08-17 11:55:00 | TERRA_M-M | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 13.1 |
| 335e7cc5-dcf3-3d1a-aff5-eeaaf5629bbe | -14.19064 | -45.31796 | 2025-08-17 11:57:00 | TERRA_M-M | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 18.4 |
| 7c76964d-d4e0-378c-bfb9-d9f741e60796 | -18.25402 | -44.98423 | 2025-08-17 11:57:00 | TERRA_M-M | TRÊS MARIAS | MINAS GERAIS | Brasil | 3169356 | 31 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 02ce27b3-a10e-3bd3-a159-fa2fb19bef60 | -21.35108 | -41.03486 | 2025-08-17 11:57:00 | TERRA_M-M | SÃO FRANCISCO DE ITABAPOANA | RIO DE JANEIRO | Brasil | 3304755 | 33 | 33 | nan | nan | nan | Mata Atlântica | 9.4 |
| f9efdd3b-18c3-34f9-a840-1a42e3596229 | -14.78928 | -47.03722 | 2025-08-17 11:57:00 | TERRA_M-M | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 36.4 |
| e9616bb8-03fe-3cbd-a2e9-c1ea0bf2a44a | -15.7748 | -43.18637 | 2025-08-17 11:57:00 | TERRA_M-M | PORTEIRINHA | MINAS GERAIS | Brasil | 3152204 | 31 | 33 | nan | nan | nan | Caatinga | 5.6 |
| 5de4c229-8796-3c63-9980-a90c8c5a20f7 | -17.90519 | -44.4205 | 2025-08-17 11:57:00 | TERRA_M-M | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 7348d7e0-de29-3837-83d2-e21daf4acdf0 | -20.03486 | -45.41299 | 2025-08-17 11:57:00 | TERRA_M-M | LAGOA DA PRATA | MINAS GERAIS | Brasil | 3137205 | 31 | 33 | nan | nan | nan | Cerrado | 8.9 |
| 1e68d40e-f73c-385b-817d-c604f2207c98 | -13.87676 | -45.54954 | 2025-08-17 11:57:00 | TERRA_M-M | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 70.0 |
| 3a7662a3-c270-3a09-a61d-6c91d7a97b5a | -13.57424 | -46.98757 | 2025-08-17 11:57:00 | TERRA_M-M | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 40.0 |
| bde0798c-167e-3244-9a06-bdb23e24cbe1 | -14.18681 | -45.34204 | 2025-08-17 11:57:00 | TERRA_M-M | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 73.8 |
| 53ec5f88-eedb-35ac-9560-5c4054a5c587 | -20.22166 | -47.01095 | 2025-08-17 11:57:00 | TERRA_M-M | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 7fda6fbb-d8ec-3165-b033-50463c118c76 | -14.38908 | -40.8959 | 2025-08-17 11:57:00 | TERRA_M-M | CAETANOS | BAHIA | Brasil | 2905156 | 29 | 33 | nan | nan | nan | Caatinga | 7.4 |
| 7fa5a04a-e79c-3f01-98bf-19a90f7f557d | -13.87875 | -45.53711 | 2025-08-17 11:57:00 | TERRA_M-M | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 68.7 |
| fc887b75-3a05-3bd2-a88b-3e0bc7dea61b | -19.17339 | -46.57388 | 2025-08-17 11:57:00 | TERRA_M-M | SERRA DO SALITRE | MINAS GERAIS | Brasil | 3166808 | 31 | 33 | nan | nan | nan | Cerrado | 16.2 |
| 48fcef16-4d02-3894-b765-ed0930338592 | -18.22373 | -45.45828 | 2025-08-17 11:57:00 | TERRA_M-M | SÃO GONÇALO DO ABAETÉ | MINAS GERAIS | Brasil | 3161700 | 31 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 21c0bcd9-ed63-317c-aa1c-b087b1d65e19 | -13.88903 | -45.53874 | 2025-08-17 11:57:00 | TERRA_M-M | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 27.1 |
| 10a33dee-f779-309a-b452-d10082e21ec7 | -17.91434 | -44.42199 | 2025-08-17 11:57:00 | TERRA_M-M | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 18623196-21c8-383d-a272-2c378ffcd0b8 | -20.01353 | -47.70607 | 2025-08-17 11:57:00 | TERRA_M-M | IGARAPAVA | SÃO PAULO | Brasil | 3520103 | 35 | 33 | nan | nan | nan | Cerrado | 16.2 |
| e0ea8b7e-ae8b-32ef-84b8-aeeff039a357 | -12.93235 | -46.11504 | 2025-08-17 11:57:00 | TERRA_M-M | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 11.2 |
| 70ca9769-58c0-3a2d-9711-e6f5cca9af4b | -14.78677 | -47.05268 | 2025-08-17 11:57:00 | TERRA_M-M | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 21.0 |
| cafc9995-09af-32d3-a922-d6ef3b621473 | -14.17864 | -45.32837 | 2025-08-17 11:57:00 | TERRA_M-M | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 9.3 |
| 046dacb1-e9ed-3c4e-a6dc-ef929fdd39f3 | -17.90368 | -44.43035 | 2025-08-17 11:57:00 | TERRA_M-M | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 10.7 |
| d5029fe8-98bc-3c38-903b-de78643de704 | -14.67622 | -42.81236 | 2025-08-17 11:57:00 | TERRA_M-M | URANDI | BAHIA | Brasil | 2932606 | 29 | 33 | nan | nan | nan | Caatinga | 11.7 |
| ee19384a-cdc3-3c09-8525-84dcce8fe07c | -14.77797 | -47.03529 | 2025-08-17 11:57:00 | TERRA_M-M | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 12.9 |
| 8e35ba52-2ce9-3bb5-b5d4-17630d3dc12a | -21.34968 | -41.04572 | 2025-08-17 11:57:00 | TERRA_M-M | SÃO FRANCISCO DE ITABAPOANA | RIO DE JANEIRO | Brasil | 3304755 | 33 | 33 | nan | nan | nan | Mata Atlântica | 16.0 |
| 4d497bb4-f17d-3075-831c-07debdce375c | -14.78737 | -47.04372 | 2025-08-17 11:57:00 | TERRA_M-M | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 48.0 |
| 73c8ea28-7bd3-302c-bfde-97c5fed20689 | -19.62921 | -45.27544 | 2025-08-17 11:57:00 | TERRA_M-M | BOM DESPACHO | MINAS GERAIS | Brasil | 3107406 | 31 | 33 | nan | nan | nan | Cerrado | 34.6 |
| 2a9fdd9c-8e94-3cd6-a0bd-ec76ab2fae65 | -19.63087 | -45.26486 | 2025-08-17 11:57:00 | TERRA_M-M | BOM DESPACHO | MINAS GERAIS | Brasil | 3107406 | 31 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 75a63f69-a70f-311c-a0e8-d53ed448a162 | -14.18873 | -45.32995 | 2025-08-17 11:57:00 | TERRA_M-M | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 116.5 |
| 3bc45212-18ab-3f12-923d-dff05ada32cc | -17.91281 | -44.43195 | 2025-08-17 11:57:00 | TERRA_M-M | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 14.0 |
| 9509f8bb-d9eb-38a9-ad6b-be03b5b197ad | -14.18056 | -45.3163 | 2025-08-17 11:57:00 | TERRA_M-M | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 28.0 |
| 5c479b83-7ffb-3983-8df4-c1a37d115781 | -12.87851 | -46.08486 | 2025-08-17 11:57:00 | TERRA_M-M | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 31.0 |
| 743aea63-a110-3180-8952-d60e58c1eb8f | -13.88704 | -45.55128 | 2025-08-17 11:57:00 | TERRA_M-M | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 32.9 |
| 23212365-b073-3ac8-991d-3ce7b3fa524f | -14.74307 | -44.20856 | 2025-08-17 11:57:00 | TERRA_M-M | MANGA | MINAS GERAIS | Brasil | 3139300 | 31 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 4f2fa11d-1419-33f0-a1b0-9c04eca1ea05 | -15.86985 | -50.19457 | 2025-08-17 11:57:00 | TERRA_M-M | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 29.1 |
| 053322f9-4f95-3585-9c4f-87330bc06be8 | -15.8602 | -50.204 | 2025-08-17 12:00:00 | GOES-19 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 104.4 |
| 425c74de-aa37-3221-8c8a-f5bea80d01fa | -5.6784 | -43.3892 | 2025-08-17 12:00:00 | GOES-19 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 82.1 |
| 81c0d428-a0a1-392c-8092-4f9b5aba7e79 | -14.1897 | -45.3241 | 2025-08-17 12:00:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 120.1 |
| cb6f537b-5aa6-3083-9923-91b6be34c7d5 | -21.67404 | -46.15412 | 2025-08-17 12:00:00 | TERRA_M-T | CAMPESTRE | MINAS GERAIS | Brasil | 3111002 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.3 |
| 6fbd0ca4-dbdc-35d3-b038-8326bcaa7c3d | -21.23634 | -45.75459 | 2025-08-17 12:00:00 | TERRA_M-T | CAMPOS GERAIS | MINAS GERAIS | Brasil | 3111606 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.5 |
| d35011ab-5038-3510-88d5-3a373bda99c7 | -14.1897 | -45.3241 | 2025-08-17 12:10:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 103.2 |
| 68b2a47c-190f-3a78-972b-790615732039 | -5.6784 | -43.3892 | 2025-08-17 12:10:00 | GOES-19 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 94.4 |
| 96ef7a74-20fd-32c1-9ba4-a8a9c37d060e | -12.8791 | -46.0936 | 2025-08-17 12:20:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 76.3 |
| d4bd2bc0-edac-3745-b942-a0a730a043e9 | -14.1897 | -45.3241 | 2025-08-17 12:20:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 103.1 |
| 65723b82-4c39-35a9-b130-d412c7c7ef3d | -5.6784 | -43.3892 | 2025-08-17 12:30:00 | GOES-19 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 89.0 |
| c88b2ba7-54b0-3bdc-86fd-931d0b1b42b8 | -14.1897 | -45.3241 | 2025-08-17 12:30:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 96.9 |
| 678845cf-3a1c-3f26-aaa9-041a45f1a3bf | -12.8791 | -46.0936 | 2025-08-17 12:30:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 78.6 |
| fe1cfa8a-de3b-34a1-b0ed-7ca32465bc8d | -13.8748 | -45.5411 | 2025-08-17 12:40:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 94.3 |
| 29d6e161-92b9-32d7-9b80-cb5a34c9e67b | -5.6784 | -43.3892 | 2025-08-17 12:40:00 | GOES-19 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 74.9 |
| 68637981-d096-31b1-b3c1-e5aa82dc162d | -14.1897 | -45.3241 | 2025-08-17 12:40:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 135.0 |
| b29ab009-e4f9-3b2f-a16c-6de4024488ac | -6.4831 | -45.4591 | 2025-08-17 12:50:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 70.6 |
| 023729f1-09e3-3692-940b-c76066229a5e | -3.982 | -42.516 | 2025-08-17 12:50:00 | GOES-19 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 82.5 |
| 6884e052-f1f5-3af8-bb58-0b2d19f7aeaf | -3.9819 | -42.5396 | 2025-08-17 12:50:00 | GOES-19 | NOSSA SENHORA DOS REMÉDIOS | PIAUÍ | Brasil | 2206803 | 22 | 33 | nan | nan | nan | Caatinga | 78.1 |
| 38a363b8-c7ff-30ef-953c-3d156f0ed12e | -14.1897 | -45.3241 | 2025-08-17 12:50:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 166.9 |
| 5d379581-941e-3a58-ae4c-1213512d0eec | -15.8602 | -50.204 | 2025-08-17 12:50:00 | GOES-19 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 85.6 |
| ca853ab5-8bce-30bd-b363-3a5f2d9b3ad4 | -5.6784 | -43.3892 | 2025-08-17 12:50:00 | GOES-19 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 106.0 |
| aa88f500-da3e-322c-a098-3d8dfa150b77 | -13.8748 | -45.5411 | 2025-08-17 12:50:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 141.0 |
| 2c50672b-f181-3538-b6f7-e702ea211769 | -12.6143 | -46.9047 | 2025-08-17 12:50:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 69.9 |
| ce4c8a09-3f09-3d18-9f56-d23d81e17d64 | -14.1702 | -45.3276 | 2025-08-17 13:00:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 84.5 |
| c2ce23c2-8601-3bbc-90d4-d0178a6ac6d2 | -7.1479 | -44.6295 | 2025-08-17 13:00:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 75.2 |
| 5a25bf33-e762-3b3c-b673-9bfe84cece2e | -6.4831 | -45.4591 | 2025-08-17 13:00:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 299.5 |
| e3b8c819-742c-3db1-ae01-817860a512d9 | -14.1897 | -45.3241 | 2025-08-17 13:00:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 175.7 |
| 47b800f5-d313-367b-bdf2-783db7869272 | -13.8748 | -45.5411 | 2025-08-17 13:00:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 114.9 |
| cfa3a41b-cd75-3758-a90e-e8370ec4e831 | -6.4833 | -45.4365 | 2025-08-17 13:00:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 87.3 |
| 2ac769b5-572a-3bc8-916a-24305c58b28d | -6.5018 | -45.4576 | 2025-08-17 13:00:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 143.8 |
| 056b9516-2d37-3145-8f50-b1295479b54d | -15.8602 | -50.204 | 2025-08-17 13:00:00 | GOES-19 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 66.8 |
| 8b6d0a67-ba85-3014-9b69-1f25976968c7 | -5.6784 | -43.3892 | 2025-08-17 13:00:00 | GOES-19 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 109.0 |
| d099c760-cac9-3018-9142-917c13fdc9d4 | -12.6335 | -46.9019 | 2025-08-17 13:00:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 77.8 |
| 132e6d6f-90a3-3bb3-84f5-f10bd9c1f6df | -14.1902 | -45.3008 | 2025-08-17 13:10:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 80.2 |
| 4df8152e-32ab-3ff5-a512-9e5a8ca96695 | -15.8602 | -50.204 | 2025-08-17 13:10:00 | GOES-19 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 59.9 |
| 5fbd7ca6-ac7f-32f4-8749-32793ff108c0 | -12.6335 | -46.9019 | 2025-08-17 13:10:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 62.0 |
| 390d7bc8-66a0-3489-b229-04f630b70455 | -5.6784 | -43.3892 | 2025-08-17 13:10:00 | GOES-19 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 210.1 |
| 66ba89e3-8f1c-3b48-a384-bc736f3eafe3 | -13.8748 | -45.5411 | 2025-08-17 13:10:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 111.7 |
| 5bc8a96b-02f9-367b-83fb-426a4ab33dfa | -14.2046 | -42.0293 | 2025-08-17 13:10:00 | GOES-19 | RIO DO ANTÔNIO | BAHIA | Brasil | 2926806 | 29 | 33 | nan | nan | nan | Caatinga | 104.5 |
| 2769c734-5ede-30ae-b1b1-6c8feeec5cd5 | -3.9819 | -42.5396 | 2025-08-17 13:10:00 | GOES-19 | NOSSA SENHORA DOS REMÉDIOS | PIAUÍ | Brasil | 2206803 | 22 | 33 | nan | nan | nan | Caatinga | 87.4 |
| db707516-1eab-31ec-9e41-79589e58aacd | -6.5018 | -45.4576 | 2025-08-17 13:10:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 90.1 |
| a7f4f03c-2ebc-3329-9462-cbf7c4319a75 | -14.1897 | -45.3241 | 2025-08-17 13:10:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 211.6 |
| 14f9977f-5a23-31e8-b4a3-3b98a219b8f5 | -7.1479 | -44.6295 | 2025-08-17 13:10:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 98.0 |
| dc6f5b8a-95fe-3a43-87bb-39d73b8addb6 | -6.4831 | -45.4591 | 2025-08-17 13:10:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 177.1 |
| 03aa40f8-3c37-3f90-be3b-bfe69a1b8ba3 | -7.1477 | -44.6524 | 2025-08-17 13:10:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 73.4 |
| 8c4a39e7-648c-3ee0-b28d-6112cb40c26f | -14.1702 | -45.3276 | 2025-08-17 13:10:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 75.9 |
| 8308deb9-d364-344f-8524-afde5ef6ca2d | -14.1702 | -45.3276 | 2025-08-17 13:20:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 98.5 |
| c25b66c9-0d1d-31d8-913c-16789d8c9fec | -6.4831 | -45.4591 | 2025-08-17 13:20:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 133.0 |
| 69b1786c-9a15-3dc7-ae6d-a2a1f94e7d7c | -3.9632 | -42.5406 | 2025-08-17 13:20:00 | GOES-19 | NOSSA SENHORA DOS REMÉDIOS | PIAUÍ | Brasil | 2206803 | 22 | 33 | nan | nan | nan | Caatinga | 77.7 |
| 8ab70ce9-f735-360f-accb-6b3a06188850 | -8.2493 | -61.4677 | 2025-08-17 13:20:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 163.4 |
| 7c8ad440-47fd-3169-8d92-c5b5148ce04f | -14.1897 | -45.3241 | 2025-08-17 13:20:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 224.0 |
| 2bf6ebc6-22c7-3a51-8730-575e061807c6 | -12.6335 | -46.9019 | 2025-08-17 13:20:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 250.4 |
| c4f97f5c-beeb-3f63-a9c0-c2a780932dd4 | -5.6784 | -43.3892 | 2025-08-17 13:20:00 | GOES-19 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 271.2 |
| f407f416-e5f0-3723-8ed1-20153570c587 | -3.9819 | -42.5396 | 2025-08-17 13:20:00 | GOES-19 | NOSSA SENHORA DOS REMÉDIOS | PIAUÍ | Brasil | 2206803 | 22 | 33 | nan | nan | nan | Caatinga | 110.9 |
| cca962f7-a0b9-3a6c-adf0-5d2bc4dda49d | -6.0791 | -44.6276 | 2025-08-17 13:20:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 78.0 |
| 3e0f07d4-cec1-3e7f-8040-b3c13fe42ad8 | -15.1903 | -53.832 | 2025-08-17 13:20:00 | GOES-19 | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 60.6 |
| 50c9085d-0ec6-33f9-a16c-b16016d1c6fd | -13.8748 | -45.5411 | 2025-08-17 13:20:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 90.0 |
| eaea78f4-68f3-38de-b01d-abaed0015b77 | -3.982 | -42.516 | 2025-08-17 13:20:00 | GOES-19 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 115.4 |
| 4edae586-2f6c-342a-b9b0-6af51b739f1c | -14.2046 | -42.0293 | 2025-08-17 13:20:00 | GOES-19 | RIO DO ANTÔNIO | BAHIA | Brasil | 2926806 | 29 | 33 | nan | nan | nan | Caatinga | 117.1 |


[Clique aqui para ver as próximas entradas](README42.md)
