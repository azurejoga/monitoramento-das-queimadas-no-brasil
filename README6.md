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

## Dados Diários - Página 6

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 694d7c06-79e1-364d-938c-6d92731f79f1 | -13.76381 | -44.0971 | 2025-06-24 03:38:00 | NOAA-21 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 938a04a1-94cb-3430-b202-9455d8ae11b9 | -12.40727 | -43.80561 | 2025-06-24 03:38:00 | NOAA-21 | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 710b2e26-2925-34e3-90ba-107ad44f262b | -14.44323 | -48.91671 | 2025-06-24 03:38:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 8.5 |
| a032b307-511d-34c0-82fb-991a21dbb5d5 | -14.19258 | -42.78124 | 2025-06-24 03:38:00 | NOAA-21 | GUANAMBI | BAHIA | Brasil | 2911709 | 29 | 33 | nan | nan | nan | Caatinga | 3.6 |
| 518df8cb-254b-3ae9-8554-905da72b7e6f | -12.2479 | -46.68506 | 2025-06-24 03:38:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 1332c28e-1216-3b69-9aa8-35a1b454d65a | -13.07095 | -48.83883 | 2025-06-24 03:38:00 | NOAA-21 | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 17.7 |
| 1a5e9374-3cc6-34dd-8ae6-92a371a5fd32 | -10.25337 | -47.67453 | 2025-06-24 03:38:00 | NOAA-21 | SANTA TEREZA DO TOCANTINS | TOCANTINS | Brasil | 1719004 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| e931385a-90e7-3fcc-9b62-7ef193831185 | -13.76888 | -44.09803 | 2025-06-24 03:38:00 | NOAA-21 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| df451a00-593a-3413-b15c-2ceb6bf28cb7 | -14.79678 | -40.14774 | 2025-06-24 03:38:00 | NOAA-21 | NOVA CANAÃ | BAHIA | Brasil | 2922706 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 2e56c9ca-a7fc-3ac1-962b-fe986cdec706 | -10.24971 | -47.67847 | 2025-06-24 03:38:00 | NOAA-21 | SANTA TEREZA DO TOCANTINS | TOCANTINS | Brasil | 1719004 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| fddaa2f5-8fb6-308a-b8bf-dfcee09cc430 | -10.45451 | -46.98623 | 2025-06-24 03:38:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 5.0 |
| fb6a232d-573a-3164-97d0-eda3dcd6a84a | -11.09242 | -46.65429 | 2025-06-24 03:38:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 8ec5aaf8-3322-3d62-baa6-f320cdb4627a | -13.55666 | -44.09907 | 2025-06-24 03:38:00 | NOAA-21 | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f1b2dec8-7428-3b90-b647-26f04a5f80c3 | -14.38711 | -46.14072 | 2025-06-24 03:38:00 | NOAA-21 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d920eff4-7889-38fc-9123-9b2b459637f1 | -13.64236 | -41.35786 | 2025-06-24 03:38:00 | NOAA-21 | BARRA DA ESTIVA | BAHIA | Brasil | 2902807 | 29 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 50d27b0f-2549-36d5-b498-ae28541696a9 | -12.40279 | -43.80143 | 2025-06-24 03:38:00 | NOAA-21 | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 46d698c2-d828-361e-949a-96a4705ed2bf | -14.44134 | -48.91197 | 2025-06-24 03:38:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 10.1 |
| d0cb3e1b-8534-3ead-abc3-e42344c9a5e3 | -11.93879 | -48.4244 | 2025-06-24 03:38:00 | NOAA-21 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| b7963cc2-ec49-3110-bb76-db6e195f7741 | -10.25215 | -47.68046 | 2025-06-24 03:38:00 | NOAA-21 | SANTA TEREZA DO TOCANTINS | TOCANTINS | Brasil | 1719004 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 4141916a-4b5e-3e8b-9d45-e02da63a0b7c | -13.07236 | -48.83208 | 2025-06-24 03:38:00 | NOAA-21 | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 17.4 |
| 29ab2bff-9a8e-305d-8014-45af59f54a9d | -14.44184 | -48.92297 | 2025-06-24 03:38:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 8.5 |
| f977d67c-f1fb-3ed9-857b-64bc236bfdda | -14.38136 | -46.13987 | 2025-06-24 03:38:00 | NOAA-21 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 9b38eb98-e946-32a4-8430-c15a8008cb53 | -4.5429 | -48.0151 | 2025-06-24 03:40:00 | GOES-19 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 47.3 |
| 9b5c0aa9-0882-392c-830d-e7623a1e3ce6 | -10.0784 | -52.7393 | 2025-06-24 03:40:00 | GOES-19 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 48.9 |
| 17490e19-6dc0-3b3e-b097-d69072c73227 | -17.33729 | -42.66434 | 2025-06-24 03:40:00 | NOAA-21 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| b87e6544-c618-34c7-8330-2c4c3107e631 | -17.09551 | -43.8064 | 2025-06-24 03:40:00 | NOAA-21 | BOCAIÚVA | MINAS GERAIS | Brasil | 3107307 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 3c5b487c-37d3-3d71-acd4-301e4bbee445 | -20.89983 | -43.82124 | 2025-06-24 03:40:00 | NOAA-21 | CARANDAÍ | MINAS GERAIS | Brasil | 3113206 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 64122909-6f4d-3993-b4a1-9ea9ddbcb41a | -17.21612 | -46.86697 | 2025-06-24 03:40:00 | NOAA-21 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a778099a-a3c2-3e44-985a-3097e1c5cc3f | -18.61334 | -44.26121 | 2025-06-24 03:40:00 | NOAA-21 | INIMUTABA | MINAS GERAIS | Brasil | 3131109 | 31 | 33 | nan | nan | nan | Cerrado | 19.9 |
| 8bebde3d-bb0c-3f55-8bf9-41415c5a80d8 | -17.33814 | -42.65997 | 2025-06-24 03:40:00 | NOAA-21 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 08d4fe52-cda9-38e8-83a5-0860d0aef4db | -19.71719 | -40.3522 | 2025-06-24 03:40:00 | NOAA-21 | JOÃO NEIVA | ESPÍRITO SANTO | Brasil | 3203130 | 32 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 3fa0442c-4481-3532-abc9-9f0667253039 | -17.20264 | -46.08111 | 2025-06-24 03:40:00 | NOAA-21 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 97761c74-29ad-3934-9060-1cb861be2b41 | -22.6765 | -42.86131 | 2025-06-24 03:40:00 | NOAA-21 | ITABORAÍ | RIO DE JANEIRO | Brasil | 3301900 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 45d39fe5-40b2-34b8-bbe7-7ee83037c926 | -17.04831 | -43.77512 | 2025-06-24 03:40:00 | NOAA-21 | BOCAIÚVA | MINAS GERAIS | Brasil | 3107307 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| d5890f1f-e830-3a7e-807f-e921718bb823 | -22.69971 | -43.34844 | 2025-06-24 03:40:00 | NOAA-21 | BELFORD ROXO | RIO DE JANEIRO | Brasil | 3300456 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 92f43ded-ba79-3e9a-8e65-c986f59c6416 | -17.65564 | -46.84669 | 2025-06-24 03:40:00 | NOAA-21 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| ef46e660-8da4-3068-8708-ba4fa350123d | -17.20558 | -46.07734 | 2025-06-24 03:40:00 | NOAA-21 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 13d9e3c2-ec14-3dd5-8875-f9cf5e4e33f5 | -22.57831 | -44.73278 | 2025-06-24 03:40:00 | NOAA-21 | AREIAS | SÃO PAULO | Brasil | 3503505 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 3ec136c5-804e-3e2a-b6fb-39a3ef2f07ae | -17.20464 | -46.0818 | 2025-06-24 03:40:00 | NOAA-21 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 036c3ea2-14a5-326d-8f95-7ceefe9d03dd | -17.34075 | -42.66075 | 2025-06-24 03:40:00 | NOAA-21 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ca5628fa-b363-3197-be6d-c5319a8fa8e3 | -19.82614 | -42.13477 | 2025-06-24 03:40:00 | NOAA-21 | CARATINGA | MINAS GERAIS | Brasil | 3113404 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| 79df1602-004c-30c2-90db-9e4e67f6e55a | -17.33645 | -42.65986 | 2025-06-24 03:40:00 | NOAA-21 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d057861e-1942-3bcf-9b59-7fa720987269 | -19.40904 | -45.13786 | 2025-06-24 03:40:00 | NOAA-21 | MARTINHO CAMPOS | MINAS GERAIS | Brasil | 3140506 | 31 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 5088adba-e8a2-30bd-b221-3ae670b35bc2 | -21.67781 | -42.05653 | 2025-06-24 03:40:00 | NOAA-21 | ITAOCARA | RIO DE JANEIRO | Brasil | 3302106 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| f02688bb-7369-3768-b8c9-09f56aa539fc | -17.20351 | -46.07684 | 2025-06-24 03:40:00 | NOAA-21 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 31cd4ebe-5385-356a-be90-9fd73ab4503d | -17.34244 | -42.66087 | 2025-06-24 03:40:00 | NOAA-21 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 16afbbb2-8f9f-311e-ba81-fb4f69cc56e4 | -22.67722 | -42.8576 | 2025-06-24 03:40:00 | NOAA-21 | ITABORAÍ | RIO DE JANEIRO | Brasil | 3301900 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 9f5de731-0c63-3ae3-88c2-cf80a293e571 | -16.6796 | -43.88517 | 2025-06-24 03:40:00 | NOAA-21 | MONTES CLAROS | MINAS GERAIS | Brasil | 3143302 | 31 | 33 | nan | nan | nan | Cerrado | 2.7 |
| c1f42afd-1a37-3392-be61-90c01bc6d333 | -21.16663 | -45.21695 | 2025-06-24 03:40:00 | NOAA-21 | NEPOMUCENO | MINAS GERAIS | Brasil | 3144607 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 4ba53dad-3c07-34dd-a8d9-3f22caacdcd7 | -16.68386 | -43.884 | 2025-06-24 03:40:00 | NOAA-21 | MONTES CLAROS | MINAS GERAIS | Brasil | 3143302 | 31 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 88974c6d-234c-39c9-aa3e-dd96c0af663b | -18.61231 | -44.2664 | 2025-06-24 03:40:00 | NOAA-21 | CURVELO | MINAS GERAIS | Brasil | 3120904 | 31 | 33 | nan | nan | nan | Cerrado | 19.9 |
| 573dd494-ced9-360f-b787-b2a77787ef2e | -17.33563 | -42.66423 | 2025-06-24 03:40:00 | NOAA-21 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| e5a90bef-e3bd-3475-a706-cd441b4d7d18 | -4.5429 | -48.0151 | 2025-06-24 03:50:00 | GOES-19 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 46.7 |
| d41b8a0b-b99a-3eea-a54c-febf661b2b24 | -4.543 | -47.9934 | 2025-06-24 03:50:00 | GOES-19 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 42.8 |
| d188d9d1-5e42-36db-ba8b-d427070f976b | -10.0784 | -52.7393 | 2025-06-24 03:50:00 | GOES-19 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 47.0 |
| 00d86c74-cb43-31d8-9d5b-9a5d44a871fa | -8.5724 | -51.5552 | 2025-06-24 04:00:00 | GOES-19 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 41.0 |
| 286b0962-bdbf-3385-b2e6-f02359fa2603 | -4.5429 | -48.0151 | 2025-06-24 04:00:00 | GOES-19 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 45.9 |
| b885e613-c969-38a7-88e9-c6822635cf03 | -4.543 | -47.9934 | 2025-06-24 04:00:00 | GOES-19 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 40.9 |
| df1974de-d27f-3ac7-9a4c-eed915d5eb7f | -8.5722 | -51.5761 | 2025-06-24 04:00:00 | GOES-19 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 41.0 |
| f23a5115-61e3-3b14-b816-8ab59c27d160 | -8.5537 | -51.5567 | 2025-06-24 04:00:00 | GOES-19 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 53.2 |
| d68f44f2-7b84-3b4b-a0b1-7182c2c9f12c | -8.0703 | -43.0981 | 2025-06-24 04:00:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 40.0 |
| f2aeafcd-9f21-339c-b5e2-41c1c2e0f688 | -7.20493 | -43.10113 | 2025-06-24 04:02:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 6.6 |
| 54e56ebf-e9fc-3df0-9b07-2a287bbaa97f | -5.92313 | -43.47794 | 2025-06-24 04:02:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| fd9b1c54-cca5-3028-a2a1-71dd049aa0a6 | -5.91861 | -43.45901 | 2025-06-24 04:02:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 1de48baf-696c-3207-98b5-16cb6e67ec7e | -7.20559 | -43.09702 | 2025-06-24 04:02:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 6.6 |
| 986e624b-1eec-3316-9028-00f87b9f9bd3 | -5.98065 | -43.7615 | 2025-06-24 04:02:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f8bbfc0a-708d-3ea3-bbc3-3b85b41c7d3a | -6.95288 | -42.80433 | 2025-06-24 04:02:00 | NPP-375D | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 1f3401b0-4063-3d1f-afd3-2fbcc045cb24 | -7.36924 | -43.4904 | 2025-06-24 04:02:00 | NPP-375D | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 3f582553-d737-32c4-8c86-7adbcf5aeef9 | -6.9538 | -42.80588 | 2025-06-24 04:02:00 | NPP-375D | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 08efcb65-ff37-3b76-9377-0ab3b420516c | -5.49365 | -42.14872 | 2025-06-24 04:02:00 | NPP-375D | ALTO LONGÁ | PIAUÍ | Brasil | 2200301 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| cdcd53f9-811a-3413-8090-5e3a5ab016c6 | -6.63915 | -47.85389 | 2025-06-24 04:02:00 | NPP-375D | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| d58db782-4ebd-3c98-aa69-225e92e9e12d | -5.12548 | -45.0335 | 2025-06-24 04:02:00 | NPP-375D | SÃO RAIMUNDO DO DOCA BEZERRA | MARANHÃO | Brasil | 2111631 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 3d493cc6-95f8-38f0-9964-2980b1059c8d | -5.97613 | -43.7654 | 2025-06-24 04:02:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| effb0299-6637-36d3-b1a8-43548f492dce | -4.54499 | -48.00796 | 2025-06-24 04:02:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 13e0e415-3849-3da1-a0cb-dedab48a0bda | -3.0275 | -49.43232 | 2025-06-24 04:02:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| ef5f9f2d-d633-30db-88e9-c69ef7e2b1e0 | -4.79338 | -37.79192 | 2025-06-24 04:02:00 | NPP-375D | JAGUARUANA | CEARÁ | Brasil | 2307007 | 23 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 1aa6f415-b0a4-3bd6-b861-32c069a09a3c | -5.91498 | -43.48111 | 2025-06-24 04:02:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 10.4 |
| c48a4f97-4cd2-3c9f-ad49-228e02d58834 | -5.78483 | -43.61298 | 2025-06-24 04:02:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| ab5a26df-939a-3684-ac03-4fa4d309e2c4 | -7.13337 | -43.73801 | 2025-06-24 04:02:00 | NPP-375D | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f0a5e2ab-261f-34c6-b139-533dd1ab3313 | -4.5352 | -48.00362 | 2025-06-24 04:02:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 72573462-92f0-3735-9263-1d1a62e698b1 | -5.92015 | -43.47286 | 2025-06-24 04:02:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 04c0af0d-e332-3b4e-96a1-b52d372062c1 | -5.12959 | -45.03433 | 2025-06-24 04:02:00 | NPP-375D | SÃO RAIMUNDO DO DOCA BEZERRA | MARANHÃO | Brasil | 2111631 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| c89a4628-83c2-3cd9-98e4-17e3bfb71dc8 | -7.20201 | -43.09644 | 2025-06-24 04:02:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| cbebcc38-acd3-37e8-9955-b4ba588fcd5b | -6.00551 | -43.75154 | 2025-06-24 04:02:00 | NPP-375D | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 4e700d3b-62b0-39b1-b7fd-6b4555a06a7b | -4.83827 | -37.43516 | 2025-06-24 04:02:00 | NPP-375D | ARACATI | CEARÁ | Brasil | 2301109 | 23 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 2499a6f1-1b0b-3d00-a5b4-843134aec343 | -7.20851 | -43.10172 | 2025-06-24 04:02:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 6.6 |
| 669260fc-cf8f-3df9-ae8c-de59908e7c11 | -6.63427 | -47.85298 | 2025-06-24 04:02:00 | NPP-375D | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 8ae3689c-824b-38ec-8cdb-7edb195af011 | -3.02819 | -49.42834 | 2025-06-24 04:02:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 945b06a1-fdcd-316e-993c-c2f3e73834a3 | -5.07021 | -37.71522 | 2025-06-24 04:02:00 | NPP-375D | BARAÚNA | RIO GRANDE DO NORTE | Brasil | 2401453 | 24 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 3e35d65e-72d2-3930-afb1-8a92c810d66c | -7.30029 | -43.20487 | 2025-06-24 04:02:00 | NPP-375D | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 40221f4d-6fde-3557-b98d-9dfdb9428e79 | -7.20426 | -43.10524 | 2025-06-24 04:02:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 3.2 |
| 88b9d109-98f8-32f8-ba29-e4a5856a4b42 | -7.28745 | -43.21555 | 2025-06-24 04:02:00 | NPP-375D | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 0033de09-17c5-3339-93c4-fa407a0105a2 | -6.95445 | -42.80189 | 2025-06-24 04:02:00 | NPP-375D | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 465173fd-0b52-3494-a1e0-d612e764f79b | -6.95643 | -42.8049 | 2025-06-24 04:02:00 | NPP-375D | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 0.3 |
| 44475f3a-c58b-36ba-9693-39f63df64b3c | -4.54035 | -48.00427 | 2025-06-24 04:02:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 14bfce08-c547-39c6-bc0f-bcf6127125bc | -6.63618 | -47.855 | 2025-06-24 04:02:00 | NPP-375D | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 74ce903d-ef0a-373e-8bea-93864d547c0d | -6.64104 | -47.85598 | 2025-06-24 04:02:00 | NPP-375D | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| ba39bc8c-01cd-39d1-b1d7-a1f77228d16d | -6.25492 | -44.83907 | 2025-06-24 04:02:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| d61544dd-854a-3c45-806f-c8ea947db8a5 | -7.08892 | -44.3763 | 2025-06-24 04:02:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 78b455ae-4312-329b-bdb2-7be2074f12d3 | -3.02849 | -49.42616 | 2025-06-24 04:02:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |


[Clique aqui para ver as próximas entradas](README7.md)
