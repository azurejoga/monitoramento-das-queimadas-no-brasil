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

## Dados Diários - Página 18

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 784fb7bf-de4e-3978-9854-01d5d5cefaf1 | -8.57634 | -54.72097 | 2025-08-12 04:08:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| d9f4fbcf-e2e0-3f77-bb2c-26474072a3c6 | -12.66428 | -46.97482 | 2025-08-12 04:08:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 0c8946a8-9b4c-39f0-9ce8-2e8842998006 | -12.99626 | -44.88912 | 2025-08-12 04:08:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 8a03fe43-40a8-39ff-944c-c7d173911440 | -12.773 | -45.45652 | 2025-08-12 04:08:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 97b56450-1a3a-324d-818e-50b8b4a468f4 | -10.86111 | -45.22073 | 2025-08-12 04:08:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| af7bb191-60e6-32eb-a481-f2710e4be7ad | -11.85341 | -49.0078 | 2025-08-12 04:08:00 | NOAA-20 | GURUPI | TOCANTINS | Brasil | 1709500 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 1262e430-571a-3b9d-920b-2070586a9489 | -14.64067 | -45.85304 | 2025-08-12 04:08:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 8.2 |
| 8e064130-616c-3d18-98a5-94b03a98099c | -13.34526 | -50.24341 | 2025-08-12 04:08:00 | NOAA-20 | SÃO MIGUEL DO ARAGUAIA | GOIÁS | Brasil | 5220207 | 52 | 33 | nan | nan | nan | Cerrado | 14.2 |
| 45f02c01-a778-3077-80bc-a2a8827e9b97 | -7.26039 | -45.36892 | 2025-08-12 04:08:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 988196e8-0b68-301e-8c24-d0b78dfe329b | -11.70806 | -51.60472 | 2025-08-12 04:08:00 | NOAA-20 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 16f7b34c-6158-36d5-ada5-2e14283aafaf | -13.11909 | -46.87085 | 2025-08-12 04:08:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 96bb0386-085c-388e-b745-ef112b646edb | -10.15428 | -40.52332 | 2025-08-12 04:08:00 | NOAA-20 | CAMPO FORMOSO | BAHIA | Brasil | 2906006 | 29 | 33 | nan | nan | nan | Caatinga | 0.4 |
| ca79a465-5d05-3fa7-bbd8-00974ad02957 | -7.21298 | -46.22389 | 2025-08-12 04:08:00 | NOAA-20 | NOVA COLINAS | MARANHÃO | Brasil | 2107258 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| edd7a591-b7ac-39f2-92f4-1c25b651456b | -14.1163 | -45.39944 | 2025-08-12 04:08:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 0ffd8f1b-b43f-3ca0-b9f7-7efe433e196b | -9.06472 | -45.05745 | 2025-08-12 04:08:00 | NOAA-20 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 12.3 |
| 4bf7dcd9-6139-31aa-9779-ad24830988ea | -10.31625 | -54.16065 | 2025-08-12 04:08:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| f39a486f-b87a-3d2d-9af9-d213edaef3a6 | -8.57196 | -54.70844 | 2025-08-12 04:08:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 848d615a-09a3-3367-9c51-070386606698 | -6.30136 | -51.40547 | 2025-08-12 04:08:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| c70d314d-fe51-37c9-b185-1e884d473b12 | -8.52131 | -43.32443 | 2025-08-12 04:08:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 9fe8fb43-3273-3c6d-836a-9978c5dee63b | -14.10143 | -44.84576 | 2025-08-12 04:08:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 9dccd577-9d6a-3f7d-8c5a-6bbbe268a209 | -8.56869 | -54.72528 | 2025-08-12 04:08:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| ac9cc9d2-2598-3343-8baa-9df6bf9b81b3 | -10.64773 | -45.23953 | 2025-08-12 04:08:00 | NOAA-20 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 3.4 |
| f18f98a5-2320-3767-bc46-51b4349ed5c5 | -11.68752 | -51.60109 | 2025-08-12 04:08:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d24bd841-f1f4-37da-8f76-d99e74ed0487 | -12.65736 | -44.52003 | 2025-08-12 04:08:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| e458bf20-715c-3897-a6e8-17e45d755ef2 | -16.2957 | -52.923 | 2025-08-12 04:10:00 | GOES-19 | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 70.2 |
| 2c54d876-866f-3a0f-a296-1c9d2813e768 | -8.9401 | -60.7288 | 2025-08-12 04:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 50.2 |
| 17957975-6fa3-3936-853e-8054fedff2eb | -17.6749 | -46.6715 | 2025-08-12 04:10:00 | GOES-19 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 91.3 |
| 241f846a-7ad2-3a5c-a03e-69194ba178f5 | -17.6544 | -46.699 | 2025-08-12 04:10:00 | GOES-19 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 107.3 |
| 885a6ef4-f493-3726-8d06-6d59c9ae02df | -12.5554 | -46.9809 | 2025-08-12 04:10:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 72.3 |
| a873068d-ed2c-3fae-9f73-266a4211a76a | -12.5742 | -47.0006 | 2025-08-12 04:10:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 83.3 |
| 079328e8-3b9f-3eb1-a7b0-070070642240 | -9.723 | -49.4806 | 2025-08-12 04:10:00 | GOES-19 | MARIANÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1712504 | 17 | 33 | nan | nan | nan | Cerrado | 48.0 |
| 238eb877-a0ac-3237-ac18-4d8cab0d8ead | -17.6355 | -46.6565 | 2025-08-12 04:10:00 | GOES-19 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 52.5 |
| 54be60c6-686f-3d59-8d9c-1596a9abba93 | -3.9686 | -47.8684 | 2025-08-12 04:10:00 | GOES-19 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 70.0 |
| 8f10b1bc-500a-362f-a0d4-b9570c897363 | -16.2961 | -52.9016 | 2025-08-12 04:10:00 | GOES-19 | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 85.7 |
| a984b494-1766-3b45-ab3c-fc168e8fb5e6 | -6.5856 | -44.564 | 2025-08-12 04:10:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 75.2 |
| b5718255-9a18-3880-ab9b-c1b045882d67 | -12.555 | -47.0034 | 2025-08-12 04:10:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 101.9 |
| 1e782543-76c6-3bb9-bd7c-f7c84ad9b62d | -3.9684 | -47.8901 | 2025-08-12 04:10:00 | GOES-19 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 69.5 |
| 93d94e65-f2c8-30eb-ab47-8e0415f796e2 | -13.3427 | -50.2448 | 2025-08-12 04:10:00 | GOES-19 | SÃO MIGUEL DO ARAGUAIA | GOIÁS | Brasil | 5220207 | 52 | 33 | nan | nan | nan | Cerrado | 64.8 |
| f71796cd-7ff2-3fd2-8f14-382c86b0b357 | -9.3806 | -61.5315 | 2025-08-12 04:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 40.3 |
| b5294353-3595-3a87-a5e8-3c3d67f6a7f6 | -17.6349 | -46.6799 | 2025-08-12 04:10:00 | GOES-19 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 121.7 |
| 70137af9-75a6-3292-90a7-0de06b62f883 | -17.6549 | -46.6757 | 2025-08-12 04:10:00 | GOES-19 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 357.2 |
| 044aaf1c-6410-3204-8120-8f5672fd9eb0 | -7.1483 | -60.1174 | 2025-08-12 04:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 44.6 |
| f020af12-be19-3ea0-ac28-ef7adef63c29 | -17.6555 | -46.6523 | 2025-08-12 04:10:00 | GOES-19 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 114.6 |
| 21cf02f9-c30d-3dcd-b226-acf99d30b137 | -16.3153 | -52.9201 | 2025-08-12 04:10:00 | GOES-19 | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 50.4 |
| a9303b56-2fb0-3d1c-9dd9-62272d15a657 | -7.1299 | -60.1182 | 2025-08-12 04:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 54.8 |
| 4e12db9a-3aeb-33ae-adc3-7110df23002c | -16.3157 | -52.8988 | 2025-08-12 04:10:00 | GOES-19 | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 53.1 |
| ede4314f-67e7-30d5-8610-0d505580ede1 | -17.56771 | -45.32877 | 2025-08-12 04:10:00 | NOAA-20 | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 15.0 |
| 78514f04-526d-308a-b365-5f77431f6c91 | -17.56436 | -45.32817 | 2025-08-12 04:10:00 | NOAA-20 | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| ba6c21a6-5c42-30cd-9cc5-b8d6686fd557 | -16.29251 | -52.91483 | 2025-08-12 04:10:00 | NOAA-20 | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 3.3 |
| b3612485-d1e5-3be2-8983-89ff13924e88 | -20.1369 | -44.92503 | 2025-08-12 04:10:00 | NOAA-20 | DIVINÓPOLIS | MINAS GERAIS | Brasil | 3122306 | 31 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 26b14d18-34ee-3d1d-bbef-7e89d33c56b5 | -18.63341 | -46.8358 | 2025-08-12 04:10:00 | NOAA-20 | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 0111ae8b-396b-3a41-abae-c05abb06d5e1 | -19.2993 | -48.42684 | 2025-08-12 04:10:00 | NOAA-20 | UBERLÂNDIA | MINAS GERAIS | Brasil | 3170206 | 31 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 00e2bfbb-80e6-3ac4-8e08-25f3dce0175e | -19.29764 | -48.4361 | 2025-08-12 04:10:00 | NOAA-20 | UBERLÂNDIA | MINAS GERAIS | Brasil | 3170206 | 31 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 0d892627-2260-31e9-91f4-0db95cfdc42b | -19.33693 | -44.41978 | 2025-08-12 04:10:00 | NOAA-20 | CAETANÓPOLIS | MINAS GERAIS | Brasil | 3109907 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 80f9c2be-5bb6-3393-b8c8-2302a4a890b2 | -17.85792 | -44.43245 | 2025-08-12 04:10:00 | NOAA-20 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 06e8f0e3-ecda-339b-af97-fd57e114afc6 | -21.99419 | -44.88054 | 2025-08-12 04:10:00 | NOAA-20 | BAEPENDI | MINAS GERAIS | Brasil | 3104908 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| eb877a23-89ad-3031-831f-ee2e1f1f00a5 | -17.65119 | -46.67926 | 2025-08-12 04:10:00 | NOAA-20 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 15.3 |
| f4dd61d5-6ca6-3f60-96e0-27025bac6835 | -17.67907 | -44.12393 | 2025-08-12 04:10:00 | NOAA-20 | JOAQUIM FELÍCIO | MINAS GERAIS | Brasil | 3136405 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 401308ae-5e3e-342d-81ff-9dc0a36eaafc | -21.11924 | -48.82911 | 2025-08-12 04:10:00 | NOAA-20 | PALMARES PAULISTA | SÃO PAULO | Brasil | 3535101 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| e8e84445-5363-334c-a0b9-9049592aea03 | -17.66577 | -46.6778 | 2025-08-12 04:10:00 | NOAA-20 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 18.6 |
| ccff1369-2849-3af8-bcda-40358d107e61 | -17.64703 | -46.68264 | 2025-08-12 04:10:00 | NOAA-20 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 8.8 |
| f9c2ab17-f422-348a-b0c6-e05464fe9b74 | -18.89859 | -46.96564 | 2025-08-12 04:10:00 | NOAA-20 | PATROCÍNIO | MINAS GERAIS | Brasil | 3148103 | 31 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 46770d53-a429-36b0-b937-010c771ad370 | -17.64355 | -46.682 | 2025-08-12 04:10:00 | NOAA-20 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 11.0 |
| 016fa194-a665-3dfd-ba27-6928d8a2e5ba | -16.50453 | -47.76706 | 2025-08-12 04:10:00 | NOAA-20 | LUZIÂNIA | GOIÁS | Brasil | 5212501 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| d1bcb0f9-df61-3bd3-be04-e0a65f898073 | -21.24624 | -46.71506 | 2025-08-12 04:10:00 | NOAA-20 | GUAXUPÉ | MINAS GERAIS | Brasil | 3128709 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| dcd520c3-fa6d-33ae-9ffe-4341be319be3 | -19.29479 | -48.43071 | 2025-08-12 04:10:00 | NOAA-20 | UBERLÂNDIA | MINAS GERAIS | Brasil | 3170206 | 31 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 094d3921-9495-31de-86ab-7f645bda435d | -17.56497 | -45.32449 | 2025-08-12 04:10:00 | NOAA-20 | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| da5c7717-dfc0-362e-9be9-0c8e56c0c5d2 | -17.63798 | -46.67269 | 2025-08-12 04:10:00 | NOAA-20 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 91401786-fd50-3fa6-8681-5a2c0c0c092e | -20.0009 | -45.39623 | 2025-08-12 04:10:00 | NOAA-20 | SANTO ANTÔNIO DO MONTE | MINAS GERAIS | Brasil | 3160405 | 31 | 33 | nan | nan | nan | Cerrado | 0.2 |
| 37ee311a-a490-31a6-8305-f3133eb7ac4f | -14.69017 | -53.71701 | 2025-08-12 04:10:00 | NOAA-20 | SANTO ANTÔNIO DO LESTE | MATO GROSSO | Brasil | 5107792 | 51 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 79875e82-5234-3cfa-b32a-445fd61f6027 | -17.65746 | -46.68454 | 2025-08-12 04:10:00 | NOAA-20 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 35.2 |
| da915f1a-cb85-3efb-aa67-55b8cad3a8c5 | -17.66025 | -46.6892 | 2025-08-12 04:10:00 | NOAA-20 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 13.8 |
| 89177d64-49a8-3d3f-af36-2de950b5d989 | -13.89872 | -51.83485 | 2025-08-12 04:10:00 | NOAA-20 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 6c620524-e1e8-3461-b9a7-9286056b0ecf | -17.63729 | -46.6767 | 2025-08-12 04:10:00 | NOAA-20 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 3e9050ca-1ead-301d-9856-8c7d6f0af6e6 | -17.66849 | -44.7905 | 2025-08-12 04:10:00 | NOAA-20 | VÁRZEA DA PALMA | MINAS GERAIS | Brasil | 3170800 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 2d735343-d145-34d7-8d62-7d23de97fc3b | -16.00829 | -43.27832 | 2025-08-12 04:10:00 | NOAA-20 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 7f485094-8a74-3041-a786-2dff8a152c12 | -16.55875 | -49.40219 | 2025-08-12 04:10:00 | NOAA-20 | GOIANIRA | GOIÁS | Brasil | 5208806 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 04f765ef-91e1-3ebe-b8ab-2173e049f4fc | -14.73534 | -46.30175 | 2025-08-12 04:10:00 | NOAA-20 | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 380806f4-231f-34f8-94ad-f52e743fc1d4 | -17.64145 | -46.67333 | 2025-08-12 04:10:00 | NOAA-20 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 48.6 |
| 0675fd45-88b4-3d75-9595-38e32175caab | -16.29319 | -52.91143 | 2025-08-12 04:10:00 | NOAA-20 | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 26a29a33-50c1-34cf-9f0a-c1578dc3cf82 | -14.71857 | -47.52597 | 2025-08-12 04:10:00 | NOAA-20 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| a10b5537-00d0-38ef-bb0c-8f497fff248b | -17.96074 | -44.29816 | 2025-08-12 04:10:00 | NOAA-20 | BUENÓPOLIS | MINAS GERAIS | Brasil | 3109204 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 4299fd30-cadd-3253-9ff6-9c15de9af7c6 | -15.40531 | -46.58794 | 2025-08-12 04:10:00 | NOAA-20 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 0814f704-a16a-3fc6-a27e-3fb3b63d6d7e | -19.43563 | -44.30934 | 2025-08-12 04:10:00 | NOAA-20 | SETE LAGOAS | MINAS GERAIS | Brasil | 3167202 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 784f2551-f275-3640-9eb9-6a01e97f074f | -15.67047 | -43.48726 | 2025-08-12 04:10:00 | NOAA-20 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 202fc78d-b165-37a4-a4a1-a9d63a8a1e73 | -14.68299 | -53.72376 | 2025-08-12 04:10:00 | NOAA-20 | SANTO ANTÔNIO DO LESTE | MATO GROSSO | Brasil | 5107792 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 428f5b98-aea3-33dc-a507-ddef163a6b90 | -16.00884 | -43.27474 | 2025-08-12 04:10:00 | NOAA-20 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f469f5e2-235b-3f22-aa50-88f1ddc3a15e | -19.71645 | -46.22029 | 2025-08-12 04:10:00 | NOAA-20 | CAMPOS ALTOS | MINAS GERAIS | Brasil | 3111507 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 97332aec-3c4f-3b63-bf0c-19fb1137339e | -15.35727 | -48.41474 | 2025-08-12 04:10:00 | NOAA-20 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 4165466d-b722-30da-8b26-9420f773c5c4 | -20.72984 | -49.40475 | 2025-08-12 04:10:00 | NOAA-20 | SÃO JOSÉ DO RIO PRETO | SÃO PAULO | Brasil | 3549805 | 35 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ecf6beb8-f397-317f-94c7-1ae88f9306fe | -14.6957 | -53.71828 | 2025-08-12 04:10:00 | NOAA-20 | SANTO ANTÔNIO DO LESTE | MATO GROSSO | Brasil | 5107792 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 6b74b8b1-1d76-3fe5-b1de-ca0dff88d6af | -15.4524 | -47.01371 | 2025-08-12 04:10:00 | NOAA-20 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 153af5f7-affe-3d07-9a50-9aad7008bfe5 | -16.30339 | -52.9138 | 2025-08-12 04:10:00 | NOAA-20 | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 8534d7c2-6ca2-3ac6-b18a-6a3102f37ceb | -13.06502 | -56.84213 | 2025-08-12 04:10:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ccf0e1b4-9e33-343c-a8f5-f81121dea1b3 | -18.45312 | -47.18958 | 2025-08-12 04:10:00 | NOAA-20 | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f2287ccd-1fde-3954-bdd0-c44333352a1c | -17.65814 | -46.68053 | 2025-08-12 04:10:00 | NOAA-20 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 32.9 |
| 897d755c-67cb-3a15-baf1-5c9f19896226 | -18.60924 | -43.90424 | 2025-08-12 04:10:00 | NOAA-20 | GOUVEIA | MINAS GERAIS | Brasil | 3127602 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| da1542b2-7242-3f7b-88f8-aff619a62fd5 | -17.57105 | -45.32936 | 2025-08-12 04:10:00 | NOAA-20 | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 15.0 |
| 2d27117a-0d7f-31b6-b89a-0cbc97f52404 | -16.38997 | -50.89845 | 2025-08-12 04:10:00 | NOAA-20 | ISRAELÂNDIA | GOIÁS | Brasil | 5210307 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 3fef7516-30ec-3dec-aaba-3430b4d093d8 | -14.69489 | -53.72223 | 2025-08-12 04:10:00 | NOAA-20 | SANTO ANTÔNIO DO LESTE | MATO GROSSO | Brasil | 5107792 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |


[Clique aqui para ver as próximas entradas](README19.md)
