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

## Dados Diários - Página 71

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 629075b3-076e-3c37-8fa3-07bf0e63d990 | -2.95045 | -49.33445 | 2025-10-18 04:49:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 74dae7c8-5c61-32e9-af41-79177749d155 | -4.54204 | -50.23362 | 2025-10-18 04:49:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 4a576105-5267-3029-bb62-e89750e8c19e | -5.99778 | -43.11651 | 2025-10-18 04:49:00 | NOAA-20 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 5.7 |
| 5dafcf6e-a0c1-3b1e-9314-24d6c6ef0862 | -6.79002 | -46.47364 | 2025-10-18 04:49:00 | NOAA-20 | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| d8417175-1f2a-3467-a889-0bc1c134f8a4 | -3.80546 | -51.6482 | 2025-10-18 04:49:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 9b5ec7f3-8aa4-3ff1-82d2-581c36e07189 | -1.38014 | -55.35233 | 2025-10-18 04:49:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a11a8b31-5528-349b-8cbd-712372a4e721 | -3.49767 | -42.72538 | 2025-10-18 04:49:00 | NOAA-20 | MILAGRES DO MARANHÃO | MARANHÃO | Brasil | 2106672 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| d0332d7c-5cd8-3b05-bee3-b2fb2095aaf1 | -7.71332 | -47.8569 | 2025-10-18 04:49:00 | NOAA-20 | FILADÉLFIA | TOCANTINS | Brasil | 1707702 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 8740f283-2f77-3665-89de-82c421f8ee34 | -6.40661 | -47.21125 | 2025-10-18 04:49:00 | NOAA-20 | PORTO FRANCO | MARANHÃO | Brasil | 2109007 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| c82caa35-b92a-3f70-b9ba-54eeedc75f62 | -2.36966 | -48.29458 | 2025-10-18 04:49:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| d3e99d13-44cc-331b-8c93-1c7b3aa68f0e | -3.20964 | -54.75135 | 2025-10-18 04:49:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 7449bad1-2923-37fc-8639-f900e1b5d38d | -3.85996 | -52.22724 | 2025-10-18 04:49:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 45c045f5-9ca9-3eaa-a2eb-1b1129d93f8c | -5.8855 | -43.92642 | 2025-10-18 04:49:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e6faf923-7d64-3dcf-b0ac-3bf7a8fad658 | -2.74314 | -49.38522 | 2025-10-18 04:49:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2790b401-e85d-3498-8c8c-c7f89855195f | -5.01378 | -46.01909 | 2025-10-18 04:49:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 18.4 |
| e59f345d-5130-3f49-952e-162fbf3eeadb | -7.36165 | -44.24074 | 2025-10-18 04:49:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 605cbdc9-92d1-3a0d-9f48-eaaf83dc1a39 | -5.70884 | -46.45622 | 2025-10-18 04:49:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| b77d4f68-f826-385a-85d2-6a45659bf18f | -3.86261 | -51.9103 | 2025-10-18 04:49:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| e44e5673-7717-3eab-8019-ab5e6f0a7756 | -7.89738 | -55.42489 | 2025-10-18 04:49:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| f0bf19d5-5b5e-30fc-b1db-b3dc4853c615 | -9.15427 | -46.7457 | 2025-10-18 04:49:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 904aa261-7da7-3ce6-8ea4-160544f07508 | -6.21009 | -44.67948 | 2025-10-18 04:49:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 9bc840ca-8123-314a-9d9b-8a6f84bd6c25 | -3.77988 | -51.76753 | 2025-10-18 04:49:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 745f3af1-4572-371b-9c11-236aedda6810 | -8.10549 | -55.08957 | 2025-10-18 04:49:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 25cee2f8-6a98-35fc-b701-b30c4b61cffd | -3.40578 | -46.899 | 2025-10-18 04:49:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 61558fe1-befc-3963-b260-e75b0e3f6297 | -3.29406 | -50.0108 | 2025-10-18 04:49:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| bfcdb892-d391-3c22-865f-3aaf0271f8fc | -6.42071 | -47.02631 | 2025-10-18 04:49:00 | NOAA-20 | SÃO JOÃO DO PARAÍSO | MARANHÃO | Brasil | 2111052 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 341f6317-7176-3c55-a884-816663de30d1 | -4.08109 | -38.22224 | 2025-10-18 04:49:00 | NOAA-20 | CASCAVEL | CEARÁ | Brasil | 2303501 | 23 | 33 | nan | nan | nan | Caatinga | 2.0 |
| aca1292c-b3f3-360a-92f7-852413f4d64b | -3.45221 | -50.09481 | 2025-10-18 04:49:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 385808e0-07e4-3eed-b541-27df4bcca388 | -5.599 | -46.38012 | 2025-10-18 04:49:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| bea2c7e0-0988-3883-ad46-525dc56f1f4b | -5.33371 | -50.99893 | 2025-10-18 04:49:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| ed57d206-572c-3186-95fe-b7ba625128a8 | -3.14471 | -50.2505 | 2025-10-18 04:49:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 4a8b9eb8-b7fe-3806-84e4-ad1a41ccf872 | -2.70713 | -49.86209 | 2025-10-18 04:49:00 | NOAA-20 | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9c3ed6d6-7fd2-3132-b26e-7fb8042eb2f4 | -6.7421 | -44.36547 | 2025-10-18 04:49:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 8ca791cc-4a9a-36d2-988a-b17c4674c47a | -3.59269 | -53.96 | 2025-10-18 04:49:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 73cdbf89-4526-367b-a48b-156248728eea | -3.65722 | -50.26981 | 2025-10-18 04:49:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d892d707-44af-3254-8893-4dc2f255637f | -6.33719 | -46.34815 | 2025-10-18 04:49:00 | NOAA-20 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f13053ce-aa5f-3d2f-bd2b-ab79d5c92ca6 | -6.14443 | -44.28913 | 2025-10-18 04:49:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 6332dcb5-7de6-36b2-85f1-3cc38c8f2a7f | -3.05952 | -43.21729 | 2025-10-18 04:49:00 | NOAA-20 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| a2d9c812-2fea-38ec-b931-c55a1a89660a | -6.73943 | -43.81032 | 2025-10-18 04:49:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 7.4 |
| bed3aadd-8061-3b8c-bbe8-81adf2efc8c0 | -3.24533 | -45.9687 | 2025-10-18 04:49:00 | NOAA-20 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 52a448d5-c5f5-314e-9c89-e1086e2f9811 | -4.40181 | -43.43941 | 2025-10-18 04:49:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 9593d9db-d7d3-3922-8b87-27a796fec423 | -4.306 | -48.06353 | 2025-10-18 04:49:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b82ad7cd-028f-3625-b328-49b68c221ff9 | -7.74591 | -42.51267 | 2025-10-18 04:49:00 | NOAA-20 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 5f8dbe4b-81a4-36ad-b074-acfd59dfe708 | -4.48048 | -43.63494 | 2025-10-18 04:49:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 7ea23827-832c-3f05-8d3f-f5319cbde777 | -3.39651 | -52.96588 | 2025-10-18 04:49:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| a5ac4960-5f5c-3c7f-9310-57e4ca5e85fb | -3.78264 | -51.77148 | 2025-10-18 04:49:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d6e12d81-1154-351d-b78e-794982efd5a7 | -8.88946 | -50.58573 | 2025-10-18 04:49:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 85d198d5-3249-3cba-ae74-0218d4d397d2 | -5.76069 | -46.6889 | 2025-10-18 04:49:00 | NOAA-20 | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 821171fd-441e-3dfe-8e25-d1879abe8e79 | -8.37489 | -48.70624 | 2025-10-18 04:49:00 | NOAA-20 | ITAPORÃ DO TOCANTINS | TOCANTINS | Brasil | 1711100 | 17 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 84cf4bc8-d787-395e-8c10-d381b7ccc938 | -6.23223 | -44.14219 | 2025-10-18 04:49:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 0d52d892-ae21-3f47-916d-9a05ac91c4f2 | -8.39566 | -46.23327 | 2025-10-18 04:49:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 9e78b5a9-622c-330d-a453-420b86dc3c7e | -6.14195 | -44.46047 | 2025-10-18 04:49:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 825fe07b-3495-3051-8877-01edf261da14 | -4.96754 | -44.61636 | 2025-10-18 04:49:00 | NOAA-20 | SÃO JOSÉ DOS BASÍLIOS | MARANHÃO | Brasil | 2111250 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 9d7ea9f5-0a6f-392d-b789-a14c0d00e8c6 | -4.4485 | -43.22858 | 2025-10-18 04:49:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 8fbee776-a171-37bb-b9a9-cffaf72ec7ca | -5.2067 | -45.75267 | 2025-10-18 04:49:00 | NOAA-20 | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 46e0a2d5-1089-316d-9aad-7a579d657721 | -5.10037 | -56.15476 | 2025-10-18 04:49:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 9ad4dd73-5c5b-382f-8cd1-b90383125f36 | -8.22509 | -47.84379 | 2025-10-18 04:49:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 1a01f1b7-a7ea-30a2-9cec-71305ff4e3c9 | -5.93262 | -47.32047 | 2025-10-18 04:49:00 | NOAA-20 | RIBAMAR FIQUENE | MARANHÃO | Brasil | 2109551 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f8b98469-3eb4-328b-88c1-1d72bb766f7c | -8.3357 | -49.97151 | 2025-10-18 04:49:00 | NOAA-20 | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 883dc7c1-7938-333d-993d-7565dd043258 | -2.86847 | -50.73617 | 2025-10-18 04:49:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 0630e0e2-e7fc-3208-819d-0e0f45da3162 | -2.8707 | -50.74367 | 2025-10-18 04:49:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 8ae882bc-5ea9-39e3-9a15-ab3cfd4d2947 | -6.58531 | -48.77378 | 2025-10-18 04:49:00 | NOAA-20 | PIÇARRA | PARÁ | Brasil | 1505635 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e74df691-9427-3337-b52f-9cac568d5732 | -2.56755 | -49.11755 | 2025-10-18 04:49:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d9a4d4fc-fb13-3878-9b34-680b011b3170 | -6.85639 | -46.92944 | 2025-10-18 04:49:00 | NOAA-20 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 7dc82f11-33a1-326e-a1ac-0dc2beb96b88 | 4.4168 | -60.38541 | 2025-10-18 04:49:00 | NOAA-20 | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 0.5 |
| bf660133-8b88-34d1-b5a1-7be9e20c6c4b | -7.06733 | -44.7324 | 2025-10-18 04:49:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| f463b0eb-1d04-3a5e-8fae-80d86d6d0372 | -9.55548 | -47.77563 | 2025-10-18 04:49:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 1be2fc79-03c3-374a-8de9-dd5298e9276d | -7.47024 | -47.07339 | 2025-10-18 04:49:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 77f93264-8422-3b03-9231-49f5db39dae5 | -3.5934 | -48.9902 | 2025-10-18 04:49:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| c45032e2-6c56-3595-9dae-c00b23a8b677 | -5.16904 | -46.19046 | 2025-10-18 04:49:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| f15f07f9-85d6-3c61-90ab-185238e5c646 | -4.11897 | -42.91256 | 2025-10-18 04:49:00 | NOAA-20 | DUQUE BACELAR | MARANHÃO | Brasil | 2103901 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 07f0ae26-a5df-3c42-8a55-7feed501e6c5 | -5.6316 | -50.03055 | 2025-10-18 04:49:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 61c7ac31-b07e-39a6-abd1-a117615acdf3 | -5.92433 | -45.44297 | 2025-10-18 04:49:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 8762a656-7a67-3fc9-a0af-5433b0bab8e1 | -7.72831 | -47.63686 | 2025-10-18 04:49:00 | NOAA-20 | BARRA DO OURO | TOCANTINS | Brasil | 1703073 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| fb38c27c-285f-3fde-b6d1-094afeec852d | -6.74063 | -47.37013 | 2025-10-18 04:49:00 | NOAA-20 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 3b595f0b-35dc-33a9-9d3c-52d46ae8007b | -6.84485 | -42.42216 | 2025-10-18 04:49:00 | NOAA-20 | CAJAZEIRAS DO PIAUÍ | PIAUÍ | Brasil | 2202075 | 22 | 33 | nan | nan | nan | Caatinga | 3.8 |
| 7a638c2c-ff7f-3299-9f6f-fe42f0c3ab27 | -4.94036 | -49.76049 | 2025-10-18 04:49:00 | NOAA-20 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 143802b0-d7aa-3cdc-9239-549cd2ccad84 | -8.8347 | -49.66626 | 2025-10-18 04:49:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 76824a28-c681-32b4-8239-2d8e1279cc28 | -7.44552 | -44.74279 | 2025-10-18 04:49:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| c4f4d597-a8de-3b5d-ad3a-79c95561d8ca | -8.6052 | -40.19186 | 2025-10-18 04:49:00 | NOAA-20 | LAGOA GRANDE | PERNAMBUCO | Brasil | 2608750 | 26 | 33 | nan | nan | nan | Caatinga | 4.3 |
| d1f5f913-2b99-3768-a2d4-b0a69415487d | -8.48179 | -44.18474 | 2025-10-18 04:49:00 | NOAA-20 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b6495372-9ed7-3b1e-b434-66fdec5a5d67 | -4.08208 | -38.21528 | 2025-10-18 04:49:00 | NOAA-20 | CASCAVEL | CEARÁ | Brasil | 2303501 | 23 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 3497cceb-1994-3be4-8fe7-2c0c8530a7c6 | -2.1226 | -56.60739 | 2025-10-18 04:49:00 | NOAA-20 | TERRA SANTA | PARÁ | Brasil | 1507979 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 4d55de49-de75-3f25-a531-a88aff8ec212 | -3.19541 | -51.59442 | 2025-10-18 04:49:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| cca41737-e3f8-3e5d-85b7-15e114b0f525 | -5.55642 | -46.37364 | 2025-10-18 04:49:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| b42b7a43-157f-3405-b2ae-d846e2dc7671 | -6.94162 | -59.61318 | 2025-10-18 04:49:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b7c8c7cf-5a1a-34d1-a766-1b1b883dec20 | -3.90562 | -52.36921 | 2025-10-18 04:49:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ada7d49d-a068-364f-b2a3-eb72d7f5dce2 | -4.28303 | -49.98304 | 2025-10-18 04:49:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ae21fa34-43f7-3b71-b084-88a6ce8591e7 | -7.57703 | -44.98463 | 2025-10-18 04:49:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 2069addd-7bf8-3d8a-af17-b06d97da23bf | -6.15839 | -52.41128 | 2025-10-18 04:49:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d3b57f62-a668-3823-ac72-6a2873431ce9 | -4.49768 | -50.45372 | 2025-10-18 04:49:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f483f710-127b-3335-bfa6-879110839270 | -8.31392 | -43.42113 | 2025-10-18 04:49:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 288e0373-aa6e-34e7-be73-3ba6c7dfe06e | -9.71916 | -44.57322 | 2025-10-18 04:49:00 | NOAA-20 | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 07dfcbb1-fa56-3e24-b980-e1e351d4b761 | -8.38486 | -46.2452 | 2025-10-18 04:49:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 4dd6792c-3a8a-3dfc-a6ff-54e2274025de | -4.4433 | -43.22779 | 2025-10-18 04:49:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| f257304f-17c6-3170-a161-d6c8733cbbcf | -7.98728 | -44.15572 | 2025-10-18 04:49:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| be9a66ce-2328-3c98-8cf8-35e6dc532f00 | -7.65946 | -44.63891 | 2025-10-18 04:49:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 390f75e6-3973-3298-85d8-080cc48be50d | -4.21785 | -48.36335 | 2025-10-18 04:49:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 783e3021-0106-34c3-a089-d890d679bc12 | -4.42352 | -47.75293 | 2025-10-18 04:49:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 3c902660-94f3-3058-8250-bbbb54f33c70 | -5.63506 | -50.03107 | 2025-10-18 04:49:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |


[Clique aqui para ver as próximas entradas](README72.md)
