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
| 8ae45fc1-498d-3496-8566-34222fd39775 | -2.99286 | -53.44531 | 2024-11-24 04:53:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| ff2a69c6-1c7f-3de1-9323-0f69deb8a249 | -2.19591 | -50.68269 | 2024-11-24 04:53:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 9b840a14-dda8-3763-b65e-75a214d64661 | -3.54947 | -51.53643 | 2024-11-24 04:53:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 47d945d9-f1bd-32fb-b668-709ad5df267e | -1.82238 | -46.38496 | 2024-11-24 04:53:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d932adf7-03fa-3291-b7dd-c8bde92b5c71 | -3.48872 | -49.92038 | 2024-11-24 04:53:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 731b5cb3-b72a-395a-ae7f-8026eb88ad56 | -2.24019 | -49.31574 | 2024-11-24 04:53:00 | NOAA-21 | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 710307f9-dee5-321d-a154-291df2abfccb | -1.29112 | -51.73046 | 2024-11-24 04:53:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 2e54f3b6-c796-386b-a39d-9da75b8e1b5d | -3.88402 | -51.94232 | 2024-11-24 04:53:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| a26326f6-1fa4-3fb0-bef7-c8eca1378006 | -3.07413 | -54.55516 | 2024-11-24 04:53:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 529560cf-7085-3306-a3fd-69a8f40c887b | -4.62812 | -49.66724 | 2024-11-24 04:53:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 5592c3ee-d6d9-3d25-9e86-1e3b6d01ea8d | -3.05226 | -52.76094 | 2024-11-24 04:53:00 | NOAA-21 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| e0ee57af-a652-3ccc-9876-ec5f440e4101 | -3.24701 | -53.27744 | 2024-11-24 04:53:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 15d50d2c-6b2d-3219-932f-6ae086bc62a2 | -3.2525 | -49.78743 | 2024-11-24 04:53:00 | NOAA-21 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| dfdb09a1-58cf-3614-85e2-a32df9999b33 | -3.12666 | -54.18195 | 2024-11-24 04:53:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a501a0a6-b0bc-3536-bbe6-00d41f752daf | -2.84803 | -53.96861 | 2024-11-24 04:53:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9f0ce8fc-7b14-32ec-9d65-1de1a70ace0c | -2.37394 | -50.392 | 2024-11-24 04:53:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| f971919d-7380-3ea1-8600-81819adf79e6 | -4.08748 | -50.36201 | 2024-11-24 04:53:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 099d5fad-b3c8-3170-9d73-a138fe26c2b0 | -1.86821 | -48.16324 | 2024-11-24 04:53:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 5dd7269b-4ad8-382b-b7e7-f4ef312d3502 | -2.2397 | -53.61994 | 2024-11-24 04:53:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 8494ec41-6134-3df3-bcfa-8ae15d2bdc89 | -0.986 | -51.76677 | 2024-11-24 04:53:00 | NOAA-21 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 086dd20a-711a-3cdc-91c3-cd177dd50a68 | -1.3797 | -52.42751 | 2024-11-24 04:53:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| cc14b07d-1a4e-3e56-8224-b8ee611cf2fc | -2.35489 | -49.04432 | 2024-11-24 04:53:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 03507b1d-f6d4-320d-88e9-0a536ced7ace | -0.19919 | -51.64344 | 2024-11-24 04:53:00 | NOAA-21 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 344c2af9-ccd9-3404-ab7f-cad30ec18461 | -3.60297 | -47.50905 | 2024-11-24 04:53:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 20cbdf73-7302-391f-bb21-7fed10bafaaa | -1.31922 | -49.39001 | 2024-11-24 04:53:00 | NOAA-21 | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| e13f3482-679f-3d28-8da4-409d57b9795d | -2.61692 | -51.80447 | 2024-11-24 04:53:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| d3609a9f-e75f-3118-a078-269f47539c17 | -3.14944 | -50.60225 | 2024-11-24 04:53:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| e4ad8998-2498-3c99-9c06-065dad3fff5a | -3.1099 | -54.28689 | 2024-11-24 04:53:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 7362abb9-279c-3a09-9d5a-f6759ee4fae3 | -2.78453 | -53.99252 | 2024-11-24 04:53:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 70f30923-5c7e-3bf6-af2a-d824f0f76f43 | -3.27068 | -53.82313 | 2024-11-24 04:53:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| b88dd9a9-03ce-3659-bfe9-75a175211c33 | -1.29442 | -51.73096 | 2024-11-24 04:53:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 24.1 |
| 2c580eff-d6e0-3dc9-a478-a80938c88f50 | -2.45406 | -49.08283 | 2024-11-24 04:53:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| fa58d605-288c-351c-8088-f20356492874 | -2.64515 | -46.85879 | 2024-11-24 04:53:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 62004127-9d79-3d94-bd1e-06cfa7152041 | -1.59919 | -52.5901 | 2024-11-24 04:53:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 12.4 |
| 229e745f-2d00-3349-a9a4-616dc3530237 | -1.58691 | -53.81738 | 2024-11-24 04:53:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c04a8756-a8d9-3520-9797-286f93e84724 | -1.48236 | -51.11584 | 2024-11-24 04:53:00 | NOAA-21 | MELGAÇO | PARÁ | Brasil | 1504505 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| f52aa81b-c01e-3622-aeef-dccb2b182d33 | -3.98933 | -49.93148 | 2024-11-24 04:53:00 | NOAA-21 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2b82b7b0-2e9b-37cc-99a1-de2a25b1398c | -1.46905 | -46.04076 | 2024-11-24 04:53:00 | NOAA-21 | CARUTAPERA | MARANHÃO | Brasil | 2102903 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 477d39e4-ce69-3f0c-83a5-1dfba2e47544 | -3.76378 | -52.40957 | 2024-11-24 04:53:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2b98f4d0-ba39-371e-bb92-997f17a4ad61 | -3.04263 | -53.42732 | 2024-11-24 04:53:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 8d3edc7d-bdad-323d-b248-981f01adbab2 | -3.22316 | -53.83815 | 2024-11-24 04:53:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 1cbc2174-5d15-3f3c-bc67-0b4950c5ed0c | -3.17933 | -54.31733 | 2024-11-24 04:53:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| f199b11b-9366-31e3-abc0-96876ba6b680 | -3.61481 | -47.5109 | 2024-11-24 04:53:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d0728bbe-ffc1-38d8-92c0-57cad7cd5621 | -1.22848 | -51.74189 | 2024-11-24 04:53:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| e18550af-3750-36eb-8630-6e209f7cda16 | -1.61508 | -55.13756 | 2024-11-24 04:53:00 | NOAA-21 | CURUÁ | PARÁ | Brasil | 1502855 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 1f8efa67-e224-3c14-a09b-b9b335fdd103 | -1.61687 | -53.30846 | 2024-11-24 04:53:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| a5d82e10-6c36-34cf-8d11-fa1d014d4d86 | -2.89749 | -54.01033 | 2024-11-24 04:53:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ad1a3a07-613f-344e-854a-8166d1fdbc55 | -3.24847 | -50.11556 | 2024-11-24 04:53:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 97b5703e-ce7f-3d83-99dc-f26d66785d7e | -3.03656 | -54.01986 | 2024-11-24 04:53:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 883dca26-0a5d-3059-9102-5168726916f2 | -1.12822 | -51.68712 | 2024-11-24 04:53:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1e414336-a370-3c9b-b65a-79b2a88ce0fe | -2.82895 | -54.02254 | 2024-11-24 04:53:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| a8c4c2e2-a8da-34bd-8a9b-710fa250eaa6 | -2.28323 | -53.63042 | 2024-11-24 04:53:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 15ca76b9-0bb0-3706-85d7-6dddc796a8a6 | -3.31815 | -46.67223 | 2024-11-24 04:53:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 76eea218-f7ca-38f1-8957-5231ec7d4cbe | -3.95968 | -49.96224 | 2024-11-24 04:53:00 | NOAA-21 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 19c0820c-80be-3dd9-8d9f-cd9930464e44 | -3.27464 | -53.82001 | 2024-11-24 04:53:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| ac2159c0-a79b-3b72-b33f-2b8d17e84712 | -3.98535 | -49.91118 | 2024-11-24 04:53:00 | NOAA-21 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| fb8789ab-9612-37cf-81c2-252691e21fcf | 0.08211 | -49.82619 | 2024-11-24 04:53:00 | NOAA-21 | CHAVES | PARÁ | Brasil | 1502509 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| a9ee728f-62ea-3e1c-af05-bf582f489768 | -5.1049 | -43.14344 | 2024-11-24 04:53:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 26633246-48e8-3edf-80ce-009d23d9f550 | -3.12441 | -53.10371 | 2024-11-24 04:53:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2c0abf8f-0ac8-3b13-bff2-bbfc689e30ea | -2.40672 | -49.05905 | 2024-11-24 04:53:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| d51373db-6ce9-3e5a-b72d-5b5f54bcc5b1 | -2.31476 | -50.59546 | 2024-11-24 04:53:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 132387f3-b912-347e-b9fa-1046b3a10ff6 | -3.51755 | -49.94038 | 2024-11-24 04:53:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5104838a-a42a-3147-95e0-9bbc9b870d13 | -5.19627 | -49.15178 | 2024-11-24 04:53:00 | NOAA-21 | NOVA IPIXUNA | PARÁ | Brasil | 1504976 | 15 | 33 | nan | nan | nan | Amazônia | 9.4 |
| 28706d1d-e810-3b90-bf4a-72efd727f92d | -2.7487 | -49.12046 | 2024-11-24 04:53:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 1025b884-1256-34c0-a36e-69381b4c3953 | -2.46126 | -49.15373 | 2024-11-24 04:53:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 24297dcc-7dcb-3d0a-87ca-bc5f85d2cbf0 | -3.10689 | -45.78317 | 2024-11-24 04:53:00 | NOAA-21 | ARAGUANÃ | MARANHÃO | Brasil | 2100873 | 21 | 33 | nan | nan | nan | Amazônia | 9.4 |
| 71bd4a4d-d4ac-32f4-8c5c-e0448100b9a2 | -2.57166 | -54.0519 | 2024-11-24 04:53:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| b844e83d-dee4-3476-9e34-0122c55e95d0 | -3.84617 | -54.75999 | 2024-11-24 04:53:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 045ab6cb-2992-3527-b5bf-5a477b50ed12 | -3.51154 | -53.81594 | 2024-11-24 04:53:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 9.3 |
| a75bf465-c6cf-3cf9-ab4f-152110b9e47d | -3.88348 | -51.94576 | 2024-11-24 04:53:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 219eb406-69ad-3a2d-89c6-aba78bc5a98d | -2.58577 | -54.22685 | 2024-11-24 04:53:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 8.4 |
| 7efa5637-7808-327d-b81e-9cd56f2fcbc7 | -3.26654 | -52.63137 | 2024-11-24 04:53:00 | NOAA-21 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 2a0ff119-db9d-312c-b2e5-08cc83dbb486 | -3.80027 | -51.05983 | 2024-11-24 04:53:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c208ed6a-5804-3ad5-8e3b-e77455fbb8b0 | -2.11693 | -50.13064 | 2024-11-24 04:53:00 | NOAA-21 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b619e6aa-7e5c-3429-829f-bf394b6f309a | -2.16744 | -50.32045 | 2024-11-24 04:53:00 | NOAA-21 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 689a1cd3-6733-3346-8c84-742fd553ea61 | -2.2105 | -53.66718 | 2024-11-24 04:53:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8f2e7d8d-209e-33a4-b774-d3abeba128fc | -2.16056 | -50.62285 | 2024-11-24 04:53:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d5fbf32b-c2d7-365b-a37b-2643c6cd9ce4 | -9.82502 | -48.17303 | 2024-11-24 04:53:00 | NOAA-21 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 0ced3ace-62f5-3c5e-b2f4-5d68e957489d | -3.19732 | -48.58609 | 2024-11-24 04:53:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 500d6ce9-1afe-3bef-be74-57eed50b3155 | -3.2903 | -53.83774 | 2024-11-24 04:53:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| e5ba898e-db8d-3847-aa62-81d32e8a6832 | -2.08487 | -49.61232 | 2024-11-24 04:53:00 | NOAA-21 | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 10e37ab4-ff0c-3abd-a76c-21015899990c | -3.23822 | -53.63296 | 2024-11-24 04:53:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 6b13bfb0-a676-3b94-b349-493921964ff4 | -2.6217 | -54.9364 | 2024-11-24 04:53:00 | NOAA-21 | BELTERRA | PARÁ | Brasil | 1501451 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 63402089-b01f-3a96-8116-452713120727 | -1.01835 | -48.07174 | 2024-11-24 04:53:00 | NOAA-21 | VIGIA | PARÁ | Brasil | 1508209 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b2e71995-e6d7-396c-ac42-a375c0155ed6 | 0.9486 | -50.75774 | 2024-11-24 04:53:00 | NOAA-21 | CUTIAS | AMAPÁ | Brasil | 1600212 | 16 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ab5ff43d-80a0-303b-8b3b-bae979079ad7 | -3.95148 | -51.22338 | 2024-11-24 04:53:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| ae7df853-4bf5-36f2-bd25-cdefcbe8f0d1 | -4.40895 | -49.65604 | 2024-11-24 04:53:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 686b20e8-18ed-36a7-a5ee-b98c4418bc94 | -1.44908 | -53.39751 | 2024-11-24 04:53:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 9498983b-3e6f-3c15-a511-cfbb7d170370 | -1.6141 | -52.58171 | 2024-11-24 04:53:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 222233a0-bf30-3447-927e-b8d2a3953a64 | -0.93245 | -51.71992 | 2024-11-24 04:53:00 | NOAA-21 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d6901240-d939-3bc8-8d4c-9dcbc14d8f3f | -3.76353 | -52.34619 | 2024-11-24 04:53:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 25611c64-cc4a-3039-8b6a-7ad45187349f | -2.82836 | -54.02625 | 2024-11-24 04:53:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| fc1463d3-e3b0-3b5d-b489-1887fc2107c2 | -2.78052 | -53.99573 | 2024-11-24 04:53:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| a4e248ce-5e2f-3095-a462-a302198d6e67 | -1.608 | -52.57722 | 2024-11-24 04:53:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 93a48363-a134-30de-a5ba-7cda4f23156b | -1.73499 | -52.04914 | 2024-11-24 04:53:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 6f3bd188-45c2-351a-bd39-2399ef3f914c | -2.71915 | -46.27621 | 2024-11-24 04:53:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 97234440-d970-38a5-baba-39a2929e7a77 | -3.23142 | -54.22921 | 2024-11-24 04:53:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| e3101b27-8d02-3356-96e8-859ed6cc39a7 | -3.24518 | -54.23132 | 2024-11-24 04:53:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 9017e9c6-8933-33da-b093-29b33433d5ab | 0.40227 | -50.85375 | 2024-11-24 04:53:00 | NOAA-21 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 8.4 |
| a840ca92-1dc6-3611-b8cd-969785c73f38 | -2.74575 | -49.11589 | 2024-11-24 04:53:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |


[Clique aqui para ver as próximas entradas](README64.md)
