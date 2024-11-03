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

## Dados Diários - Página 63

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 937b5277-b29b-3c27-b64a-3c3e103387bc | -4.39662 | -43.45824 | 2024-11-03 04:50:00 | AQUA_M-M | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 31.3 |
| 585abb44-7168-3b11-bf4a-0f2211e8ed9e | -19.50749 | -56.58709 | 2024-11-03 04:50:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.4 |
| 70db3dda-49a7-3c4d-aa8b-5f20eb1129c2 | -17.62157 | -57.47139 | 2024-11-03 04:50:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.6 |
| 324261a8-3b95-3b1c-8f62-d8ece40fb754 | -17.28458 | -57.50383 | 2024-11-03 04:50:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.5 |
| 6aa3e330-e73d-31ef-a202-6daf8cc86913 | -17.28375 | -57.50848 | 2024-11-03 04:50:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.3 |
| 52a2a42e-4dd1-318e-9028-b4ca0ec3b183 | -16.41702 | -58.28294 | 2024-11-03 04:50:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.1 |
| 11579b5d-a2bc-3f9e-b3c1-d9599433207a | -15.64809 | -58.66058 | 2024-11-03 04:50:00 | NOAA-21 | FIGUEIRÓPOLIS D'OESTE | MATO GROSSO | Brasil | 5103809 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| d58d8ba1-bcda-3e1c-a93d-90b12da03032 | -15.31042 | -59.39815 | 2024-11-03 04:50:00 | NOAA-21 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 40501503-6f9c-3cc0-a8c3-2c4a6d807f43 | -6.89013 | -38.55751 | 2024-11-03 04:53:00 | AQUA_M-M | CAJAZEIRAS | PARAÍBA | Brasil | 2503704 | 25 | 33 | nan | nan | nan | Caatinga | 5.5 |
| 2040d0c1-4615-3705-92d0-cdfbe32668f9 | -6.8503 | -38.46126 | 2024-11-03 04:53:00 | AQUA_M-M | CAJAZEIRAS | PARAÍBA | Brasil | 2503704 | 25 | 33 | nan | nan | nan | Caatinga | 4.9 |
| 9c1b1b40-0119-3da8-ae73-fe17d9e7369c | -6.80027 | -34.97125 | 2024-11-03 04:53:00 | AQUA_M-M | RIO TINTO | PARAÍBA | Brasil | 2512903 | 25 | 33 | nan | nan | nan | Mata Atlântica | 9.4 |
| 94cdf07d-384b-3177-b4f1-2910a13633c2 | -6.79178 | -34.97569 | 2024-11-03 04:53:00 | AQUA_M-M | MARCAÇÃO | PARAÍBA | Brasil | 2509057 | 25 | 33 | nan | nan | nan | Mata Atlântica | 11.9 |
| e55c1b7f-4561-3ad2-9af2-2ae7c8df015d | -6.51999 | -41.47321 | 2024-11-03 04:53:00 | AQUA_M-M | LAGOA DO SÍTIO | PIAUÍ | Brasil | 2205599 | 22 | 33 | nan | nan | nan | Caatinga | 8.6 |
| a263dd49-875b-3ffb-8aae-1c94918785f7 | -6.51826 | -41.48439 | 2024-11-03 04:53:00 | AQUA_M-M | LAGOA DO SÍTIO | PIAUÍ | Brasil | 2205599 | 22 | 33 | nan | nan | nan | Caatinga | 113.1 |
| f7150329-90f0-337d-8703-f9b9645344db | -6.51653 | -41.4955 | 2024-11-03 04:53:00 | AQUA_M-M | LAGOA DO SÍTIO | PIAUÍ | Brasil | 2205599 | 22 | 33 | nan | nan | nan | Caatinga | 17.9 |
| d93b4141-a3ca-367f-8f20-5680c521dbcf | -6.50841 | -41.48293 | 2024-11-03 04:53:00 | AQUA_M-M | LAGOA DO SÍTIO | PIAUÍ | Brasil | 2205599 | 22 | 33 | nan | nan | nan | Caatinga | 54.4 |
| 092f865f-1668-3520-acd1-f7030617dc94 | -6.50667 | -41.49409 | 2024-11-03 04:53:00 | AQUA_M-M | LAGOA DO SÍTIO | PIAUÍ | Brasil | 2205599 | 22 | 33 | nan | nan | nan | Caatinga | 10.5 |
| d5fff52c-f43c-3786-aaa7-e99256988f08 | -5.28985 | -43.06849 | 2024-11-03 04:53:00 | AQUA_M-M | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 38106aaf-3db6-31d6-a6de-bec5a907f2a6 | -5.28948 | -43.07432 | 2024-11-03 04:53:00 | AQUA_M-M | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 18e119aa-969c-3a88-97e1-80b637d7753c | -10.57319 | -41.47464 | 2024-11-03 04:53:00 | AQUA_M-M | SENTO SÉ | BAHIA | Brasil | 2930204 | 29 | 33 | nan | nan | nan | Caatinga | 8.4 |
| 6997335a-616f-3b03-9d7a-f54a238e1c7d | -10.5716 | -41.48482 | 2024-11-03 04:53:00 | AQUA_M-M | SENTO SÉ | BAHIA | Brasil | 2930204 | 29 | 33 | nan | nan | nan | Caatinga | 6.9 |
| cd9b5121-4c12-352d-934a-fbb329589e2d | -8.70352 | -48.01146 | 2024-11-03 04:53:00 | AQUA_M-M | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 30.4 |
| 5a52577b-ba9c-38a8-acc8-f509c36e0d7b | -8.69907 | -48.01553 | 2024-11-03 04:53:00 | AQUA_M-M | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 22.9 |
| c8c814bd-c721-3097-bb02-3d4419c20047 | -15.22745 | -43.32435 | 2024-11-03 04:55:00 | AQUA_M-M | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Caatinga | 8.2 |
| 0a98eb75-2f99-3b57-a8fa-d759f9a45f90 | -15.22354 | -43.32946 | 2024-11-03 04:55:00 | AQUA_M-M | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Caatinga | 6.2 |
| 74ab3386-3513-3408-9f38-f2e6ec8eaa17 | -15.20333 | -43.26873 | 2024-11-03 04:55:00 | AQUA_M-M | PAI PEDRO | MINAS GERAIS | Brasil | 3146552 | 31 | 33 | nan | nan | nan | Caatinga | 56.8 |
| 102ec5e7-fc6b-3916-94f6-7d43cfb1e5c4 | -15.20154 | -43.2798 | 2024-11-03 04:55:00 | AQUA_M-M | PAI PEDRO | MINAS GERAIS | Brasil | 3146552 | 31 | 33 | nan | nan | nan | Caatinga | 20.7 |
| 4ab860e2-aa1f-3e81-94f0-f7d95efcd88b | -1.2756 | -53.3734 | 2024-11-03 04:55:13 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 49.4 |
| 6f6e65f4-6821-3b40-bb19-72b5b851faf2 | -1.2755 | -53.3936 | 2024-11-03 04:55:13 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 80.7 |
| 2bde2c4f-63b8-3cbd-a59c-a8769fd7807d | -1.2755 | -53.4138 | 2024-11-03 04:55:13 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 57.6 |
| d0fa2453-c87a-376d-b78b-48f670b78c55 | -2.5797 | -53.3724 | 2024-11-03 04:55:21 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 53.9 |
| 0ec9be65-6ac2-309c-897f-f1ddb7cb95f6 | -2.5796 | -53.3927 | 2024-11-03 04:55:21 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 47.4 |
| b5fb3cac-3a79-352e-b59b-6626fdb0af7a | -2.8061 | -51.6095 | 2024-11-03 04:55:22 | GOES-16 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 32.7 |
| bdb8789e-85f4-3d61-9ad7-8dcafe6afd11 | -2.7876 | -51.6099 | 2024-11-03 04:55:22 | GOES-16 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 32.9 |
| f98d3006-4cb1-3e9f-bc30-4b087727acea | -2.7603 | -54.4149 | 2024-11-03 04:55:22 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 63.3 |
| ebbca1db-d3cc-313d-bcf1-dd249d0f19bc | -2.7602 | -54.4349 | 2024-11-03 04:55:22 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 61.1 |
| 55bb9b40-0477-3f9b-b096-e94985325270 | -3.0734 | -54.167 | 2024-11-03 04:55:24 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 39.5 |
| 5da7aeab-ad27-3d67-8b2e-022f88170db8 | -3.0734 | -54.147 | 2024-11-03 04:55:24 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 56.8 |
| a878d738-f33b-3846-a5a2-5f70f061873d | -3.1059 | -50.3105 | 2024-11-03 04:55:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 63.0 |
| 79eea3c6-3787-3103-ab4f-ed959c4a3a72 | -3.106 | -50.2896 | 2024-11-03 04:55:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 164.5 |
| 4112f855-343f-37fc-a7ab-d1e397e3cddd | -3.1061 | -50.2686 | 2024-11-03 04:55:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 94.2 |
| ca62c714-0826-3d72-be69-b8a7613e1c15 | -3.1245 | -50.289 | 2024-11-03 04:55:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 67.1 |
| ec9bd2e3-bcd5-3622-81fa-fb7adff6160b | -3.1501 | -48.5689 | 2024-11-03 04:55:24 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 63.8 |
| 1f13d579-6abf-3ee4-98e8-931963c0d678 | -3.2415 | -53.3967 | 2024-11-03 04:55:25 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 30.0 |
| ee032ce9-9b3a-38c9-b89a-411ca83b412e | -3.4749 | -50.3826 | 2024-11-03 04:55:26 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 34.8 |
| 4bcf3490-e51c-3781-a3bc-017b5f5c934c | -6.5241 | -41.4688 | 2024-11-03 04:55:43 | GOES-16 | LAGOA DO SÍTIO | PIAUÍ | Brasil | 2205599 | 22 | 33 | nan | nan | nan | Caatinga | 74.1 |
| b834a765-10e2-3e63-be77-9e95a534797c | -6.5239 | -41.4929 | 2024-11-03 04:55:43 | GOES-16 | LAGOA DO SÍTIO | PIAUÍ | Brasil | 2205599 | 22 | 33 | nan | nan | nan | Caatinga | 90.3 |
| e186e207-2430-398e-aa6f-3aff5cefaf9a | -15.2117 | -43.2825 | 2024-11-03 04:56:31 | GOES-16 | PAI PEDRO | MINAS GERAIS | Brasil | 3146552 | 31 | 33 | nan | nan | nan | Caatinga | 66.1 |
| 8bdaadae-7779-3b1c-a4c6-d78ca29d04bd | 3.71798 | -51.39041 | 2024-11-03 05:05:00 | NPP-375D | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 78be5084-7ac0-3527-aa7e-08a9fe77e29d | 3.70627 | -51.24696 | 2024-11-03 05:05:00 | NPP-375D | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 720eaf14-94d8-3929-abbb-b9af820779c7 | 3.68843 | -51.23153 | 2024-11-03 05:05:00 | NPP-375D | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 7a6080f3-4b23-360c-bb16-3df9d831a21d | 3.68771 | -51.22706 | 2024-11-03 05:05:00 | NPP-375D | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 4.6 |
| e04e43ab-0959-3306-aff4-c4f3071b5b85 | 3.68541 | -51.23656 | 2024-11-03 05:05:00 | NPP-375D | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 4cc62b01-042c-3776-825a-234bb03eaba3 | 3.68469 | -51.23212 | 2024-11-03 05:05:00 | NPP-375D | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 3.2 |
| f760ee98-9732-3dc2-84f6-47ff3a1ff982 | -1.2756 | -53.3734 | 2024-11-03 05:05:13 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 57.1 |
| 5cac3129-5be0-3072-9b74-d6e1227c6373 | -1.2755 | -53.3936 | 2024-11-03 05:05:13 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 90.2 |
| f0fce161-cfaf-3ae9-b2eb-4f0bc3982986 | -1.2755 | -53.4138 | 2024-11-03 05:05:13 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 59.8 |
| 8f0903b1-9840-3532-9630-e748a7455e05 | -2.5797 | -53.3724 | 2024-11-03 05:05:21 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 48.0 |
| b38f6e9e-9429-3a07-bcef-b12bccf048ea | -2.5796 | -53.3927 | 2024-11-03 05:05:21 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 44.9 |
| eeebd454-21eb-3c80-a1f5-049e89de1c2c | -2.7876 | -51.6099 | 2024-11-03 05:05:22 | GOES-16 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 38.1 |
| 4f9b3c71-aa52-3789-8968-984bb6a1778b | -2.7602 | -54.4349 | 2024-11-03 05:05:22 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 43.8 |
| e586b035-0ef4-37d8-8142-90a23e3cf5d9 | -2.7419 | -54.4153 | 2024-11-03 05:05:22 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 46.0 |
| 4cad92c9-16aa-3111-866d-fd7709b15a58 | -2.7419 | -54.4353 | 2024-11-03 05:05:22 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 60.1 |
| 076e70dd-21bc-341c-accd-9ace76e9b335 | -3.055 | -54.1474 | 2024-11-03 05:05:24 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 38.8 |
| eda106ae-d31a-37d0-8100-f947a606d0c9 | -3.1501 | -48.5689 | 2024-11-03 05:05:24 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 83.5 |
| f1fd93a6-31dd-3a20-ac00-014b428cddb4 | -3.1245 | -50.289 | 2024-11-03 05:05:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 60.7 |
| e3f9f0c2-b432-3cdf-8800-40bb582f3e2b | -3.1061 | -50.2686 | 2024-11-03 05:05:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 89.6 |
| cde753c5-e4d7-309a-a492-97cb2031abf1 | -3.106 | -50.2896 | 2024-11-03 05:05:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 166.3 |
| 53267b5c-9b62-31a1-9ff1-da689b4f9e28 | -3.0734 | -54.147 | 2024-11-03 05:05:24 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 64.1 |
| 8643ca9b-99ab-3182-9da0-3b6af685ada7 | -3.0734 | -54.167 | 2024-11-03 05:05:24 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 50.5 |
| 6da7163e-bd51-33a1-b762-8415224d2e72 | -3.1059 | -50.3105 | 2024-11-03 05:05:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 65.4 |
| c0bca861-d55e-3dcd-93eb-3f75c5ed09f7 | -4.7658 | -48.0037 | 2024-11-03 05:05:33 | GOES-16 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 58.3 |
| e7ae5fd6-748e-3243-8b35-107727350b7a | -6.5241 | -41.4688 | 2024-11-03 05:05:43 | GOES-16 | LAGOA DO SÍTIO | PIAUÍ | Brasil | 2205599 | 22 | 33 | nan | nan | nan | Caatinga | 70.6 |
| 9c103abf-4179-3a27-be98-0e8820bfa902 | -6.5239 | -41.4929 | 2024-11-03 05:05:43 | GOES-16 | LAGOA DO SÍTIO | PIAUÍ | Brasil | 2205599 | 22 | 33 | nan | nan | nan | Caatinga | 96.3 |
| 50a0ad85-8d6d-3a4e-bc08-3767ab7a2c0d | -1.40023 | -52.10376 | 2024-11-03 05:08:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 6cad07ec-1238-3e67-8f05-f013d51e3f93 | -1.40019 | -52.01089 | 2024-11-03 05:08:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 82f7e9a4-b70a-3781-950f-e4eb221d6db7 | -1.39953 | -52.10839 | 2024-11-03 05:08:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 67994ae9-63b2-3387-affd-f44dd6155e00 | -1.39928 | -52.11562 | 2024-11-03 05:08:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| bded5a4a-933d-3591-b4f9-05c1b0342808 | -1.39637 | -52.01028 | 2024-11-03 05:08:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| acc226f9-5ad3-3c41-acc7-42af6f5176d8 | -1.39327 | -52.005 | 2024-11-03 05:08:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 3155d8d8-5e9d-3cbb-9e56-d58dae5a4711 | -1.39098 | -52.24112 | 2024-11-03 05:08:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 95017d2b-e5a8-3ebc-8c7e-7fc038f11650 | -1.39063 | -52.24336 | 2024-11-03 05:08:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c233b86f-1667-3e58-b8c8-e0ce487693b3 | -1.39026 | -52.24566 | 2024-11-03 05:08:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f3df600b-7f91-3167-9811-1f84fc642609 | -1.38974 | -52.05236 | 2024-11-03 05:08:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| c5915b94-3f44-3d49-8115-d1a86d17f1b9 | -1.38944 | -52.0044 | 2024-11-03 05:08:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| cf856d61-8e37-3077-ab32-c10bb5fc4d62 | -1.38666 | -52.04712 | 2024-11-03 05:08:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 8ab45d65-792c-3a17-875f-d083bb06bc9b | -1.36244 | -51.97618 | 2024-11-03 05:08:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| bccdc1cb-12cf-34f5-9cc0-9d7842e6adc4 | -1.36006 | -51.96616 | 2024-11-03 05:08:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| bc2a57f2-971f-3959-820a-851647bff19e | -1.35934 | -51.97087 | 2024-11-03 05:08:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 0c6f7bba-503d-3b2e-935f-37f3492acbd4 | -1.35623 | -51.96556 | 2024-11-03 05:08:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 245e62ce-ebb7-3afb-912a-9d0d14d4f248 | -1.35032 | -52.07965 | 2024-11-03 05:08:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| a27435d7-444b-377b-8b90-1e2807950ef1 | -1.3465 | -52.07907 | 2024-11-03 05:08:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 9.8 |
| e36fd5e3-9c06-3bc2-a26a-6233bf1fb2cb | -1.33745 | -52.08715 | 2024-11-03 05:08:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 40c0372b-59d9-3b30-a3e8-a285092e3237 | -1.33222 | -52.39349 | 2024-11-03 05:08:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d3c3282a-47ac-307d-91df-110da86d8505 | -1.31665 | -51.98164 | 2024-11-03 05:08:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| a10c5718-5294-3d48-bc3d-0f2b248a4aba | -1.30954 | -52.56186 | 2024-11-03 05:08:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 19306cd5-2bf3-3a9b-ba0f-09864798bcef | -1.30778 | -52.47618 | 2024-11-03 05:08:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 51f2e1cb-c189-3618-ace6-c74cd5d8f9a7 | -1.2356 | -52.14958 | 2024-11-03 05:08:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 9ea2d28f-d0b0-39f2-a10a-eba4dd780057 | -1.23489 | -52.15416 | 2024-11-03 05:08:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 6db53cfa-2d23-33d8-874c-0291ac7ea8bb | -1.2311 | -52.15357 | 2024-11-03 05:08:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |


[Clique aqui para ver as próximas entradas](README64.md)
