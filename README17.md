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
| 27c5ca40-cd5c-3f73-8e5e-dcb3f09daf9b | -12.55537 | -58.35003 | 2024-12-11 04:36:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 4.6 |
| bf7f792a-d309-3607-84a7-e16640c382a5 | -12.55302 | -58.36223 | 2024-12-11 04:36:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 3fee75b7-a5da-357b-8eec-c58089854beb | -14.97171 | -44.40896 | 2024-12-11 04:36:00 | NOAA-21 | JANUÁRIA | MINAS GERAIS | Brasil | 3135209 | 31 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 6be48c3d-1b53-3fc9-ae73-7966c73f0c45 | -14.97587 | -44.40956 | 2024-12-11 04:36:00 | NOAA-21 | JANUÁRIA | MINAS GERAIS | Brasil | 3135209 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 94e9a0ad-3e1d-31ba-ab52-908d7cb39fbd | -12.19645 | -46.71693 | 2024-12-11 04:36:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 7505a113-9456-3d28-93a7-a13d39a6f32d | -11.12051 | -54.6449 | 2024-12-11 04:36:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 752ebe50-3215-3542-b6b6-c286d5671e27 | -12.55204 | -58.33966 | 2024-12-11 04:36:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| c3f18e8f-396a-35ea-a75d-43339287c57a | -12.5512 | -58.37173 | 2024-12-11 04:36:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 5675d7c5-5c5c-34c5-8a68-c2bd2b0a863b | -11.87304 | -43.72358 | 2024-12-11 04:36:00 | NOAA-21 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 04867874-2ecc-3fc6-b660-45227086b49e | -11.83331 | -43.84366 | 2024-12-11 04:36:00 | NOAA-21 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 91bf667e-1dda-3037-9c9c-0aa3ca590fcc | -12.53577 | -58.36883 | 2024-12-11 04:36:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 3.8 |
| a7bcae50-5ba9-388f-b922-74db798f757b | -12.53427 | -58.34907 | 2024-12-11 04:36:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 0bb53c52-8c92-3227-a304-38c23a352330 | -12.54455 | -58.35092 | 2024-12-11 04:36:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 3f67867d-6f3d-396c-b38f-689f5d7ff064 | -11.0464 | -44.56778 | 2024-12-11 04:36:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| af31415e-25d7-3499-8709-12300965c8e4 | -12.54092 | -58.36976 | 2024-12-11 04:36:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 39098ef6-ae7e-3a88-9952-4d2db31e0c0a | -12.54214 | -58.36342 | 2024-12-11 04:36:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 3f64e74e-6459-380d-b6e6-5e16a350f7fa | -14.97119 | -44.41285 | 2024-12-11 04:36:00 | NOAA-21 | ITACARAMBI | MINAS GERAIS | Brasil | 3132107 | 31 | 33 | nan | nan | nan | Cerrado | 5.4 |
| ee71d9fa-4ad6-3841-b09a-23ac7a07cc37 | -15.54183 | -43.14695 | 2024-12-11 04:36:00 | NOAA-21 | PAI PEDRO | MINAS GERAIS | Brasil | 3146552 | 31 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 911eb7ad-3533-31ad-95df-ec2fbb2dd77a | -14.1921 | -40.54575 | 2024-12-11 04:36:00 | NOAA-21 | MIRANTE | BAHIA | Brasil | 2921450 | 29 | 33 | nan | nan | nan | Caatinga | 0.3 |
| 299b13bc-2a96-3e22-95eb-70f8ab4468dc | -12.54001 | -58.34687 | 2024-12-11 04:36:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 7.5 |
| e92d3e85-b534-31c5-a73e-9cfa6ac19fe1 | -12.54122 | -58.34061 | 2024-12-11 04:36:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 944dd729-dafc-3b4a-be85-8b9c4b9d0974 | -12.55693 | -58.36959 | 2024-12-11 04:36:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 0f583b46-a0a9-3144-9d13-815e859b0d64 | -12.55873 | -58.36024 | 2024-12-11 04:36:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 5ca28d40-47c5-3f3a-ac2f-de6ce7a9304a | -11.88468 | -54.67706 | 2024-12-11 04:36:00 | NOAA-21 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 2ec7f3bc-2222-397c-b207-3c21ff4d42ab | -10.02682 | -53.75311 | 2024-12-11 04:36:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 88d58070-a7f6-32e1-a9dd-982c2df2e82b | -12.67264 | -45.67197 | 2024-12-11 04:36:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 19.7 |
| 7d3b03b5-418c-317d-877e-bdcc03e46b5e | -12.86496 | -44.61599 | 2024-12-11 04:36:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 6bd97158-dd95-3665-8b4a-e47c50a72e0b | -11.82971 | -43.83927 | 2024-12-11 04:36:00 | NOAA-21 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 41d3593e-82e8-3824-873b-24402f0ce1ff | -12.54396 | -58.35402 | 2024-12-11 04:36:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 533697bc-a1d8-3210-b721-c6f448718e83 | -11.0943 | -54.62477 | 2024-12-11 04:36:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 477e8ed7-3b06-3b5e-b16c-aeeace1ef12f | -11.46695 | -44.95775 | 2024-12-11 04:36:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 24ac98ee-67cc-365e-b624-eb432e61ac43 | -12.5376 | -58.35934 | 2024-12-11 04:36:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 49d45163-16dc-3c32-8f86-c32ced12d5f6 | -11.78036 | -55.13097 | 2024-12-11 04:36:00 | NOAA-21 | SINOP | MATO GROSSO | Brasil | 5107909 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4b581d5c-69f5-35d2-bdf1-40c2597e3eb2 | -11.48934 | -48.20003 | 2024-12-11 04:36:00 | NOAA-21 | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 7e16a111-575e-38bc-9600-00b01f85acbf | -12.53821 | -58.35619 | 2024-12-11 04:36:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 8c36fc09-5f6a-3da7-bce3-24d41d88466d | -13.37351 | -54.24597 | 2024-12-11 04:36:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 9f7b1d8b-6c10-3b25-80dd-810c5088d784 | -11.49323 | -48.19697 | 2024-12-11 04:36:00 | NOAA-21 | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 7762fbba-c25e-3c73-9195-6e631b31260f | -12.55754 | -58.36644 | 2024-12-11 04:36:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 6.1 |
| eef49548-cbc3-3398-ad20-3feb6fb247e5 | -12.53642 | -57.73916 | 2024-12-11 04:36:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 1ed9e4ec-bf11-3678-97c8-40a90bfe805c | -12.05635 | -46.88749 | 2024-12-11 04:36:00 | NOAA-21 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 43ffbe97-5c46-3539-a92f-e3f9b58a6bf9 | -12.54062 | -58.34374 | 2024-12-11 04:36:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 4.5 |
| e500898b-7719-3f4c-b603-7cb2a0a454ff | -14.97223 | -44.40507 | 2024-12-11 04:36:00 | NOAA-21 | ITACARAMBI | MINAS GERAIS | Brasil | 3132107 | 31 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 2df4e912-a23d-3c9e-96b5-33d6de4314cd | -13.79279 | -44.417 | 2024-12-11 04:36:00 | NOAA-21 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 2ca89258-dff1-32b6-bce6-21e7492e64a8 | -10.96379 | -54.09669 | 2024-12-11 04:36:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 0536f1eb-4c5d-3933-b206-5f3662d250e9 | -12.54335 | -58.35714 | 2024-12-11 04:36:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 6.7 |
| afffe580-d961-3839-abb6-ece37ed0af04 | -12.88739 | -43.64788 | 2024-12-11 04:36:00 | NOAA-21 | SERRA DOURADA | BAHIA | Brasil | 2930303 | 29 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 63916bae-df3c-3507-860e-edbe1563167f | -13.37394 | -54.24923 | 2024-12-11 04:36:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| fbd37ac5-455b-36ef-bf32-612fdd16129e | -11.87773 | -43.72032 | 2024-12-11 04:36:00 | NOAA-21 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 29ee0076-5d3e-3d42-b5ac-57797e0fa869 | -12.53245 | -58.35843 | 2024-12-11 04:36:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 5b2cbb65-2b22-3409-a6a7-286d3dba6d1f | -13.37265 | -54.25099 | 2024-12-11 04:36:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 9f3c95be-bb63-3fa2-8203-49183c919163 | -12.53699 | -58.3625 | 2024-12-11 04:36:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 41235daf-19dc-3531-a5be-223ca7bd101a | -12.71495 | -54.97686 | 2024-12-11 04:36:00 | NOAA-21 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 847b24a6-b23e-307c-a433-c3be22eb4e89 | -12.56443 | -58.35827 | 2024-12-11 04:36:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 2a285a9f-8ebe-328f-9c09-60efa6306dcc | -12.41508 | -43.79657 | 2024-12-11 04:36:00 | NOAA-21 | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |
| bc33c817-6b54-3384-8d68-fd80baaf01b4 | -12.5599 | -58.35415 | 2024-12-11 04:36:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 0dfe0509-f19e-3e4e-ac47-012bfe4de7db | -13.25933 | -41.33969 | 2024-12-11 04:36:00 | NOAA-21 | MUCUGÊ | BAHIA | Brasil | 2921906 | 29 | 33 | nan | nan | nan | Caatinga | 5.9 |
| 87df24ac-17d2-3f4e-aaae-dc4e5e13941f | -14.57529 | -56.71497 | 2024-12-11 04:36:00 | NOAA-21 | NORTELÂNDIA | MATO GROSSO | Brasil | 5106000 | 51 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 0287ac57-9f52-3e3d-87d4-05e34f770994 | -12.53949 | -57.72978 | 2024-12-11 04:36:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| dd2bcc5b-43f4-38b6-84f7-5ea1d0b06406 | -15.15838 | -56.47567 | 2024-12-11 04:36:00 | NOAA-21 | JANGADA | MATO GROSSO | Brasil | 5104906 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| baefe0b3-b6ed-318f-ba58-eb52154e53d3 | -12.54668 | -58.36754 | 2024-12-11 04:36:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 61faa546-3cca-3ac2-912e-c067b5578b2f | -14.81751 | -46.9575 | 2024-12-11 04:36:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 37b23090-5632-3676-b660-fe46577d26e8 | -12.56266 | -58.36751 | 2024-12-11 04:36:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d78c348f-ee97-3620-a267-27d9c20079e2 | -11.10882 | -54.63887 | 2024-12-11 04:36:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| dd0da15b-357f-3548-80f5-715283395bf9 | -11.75387 | -41.13863 | 2024-12-11 04:36:00 | NOAA-21 | MORRO DO CHAPÉU | BAHIA | Brasil | 2921708 | 29 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 283c322f-11d6-3011-a235-64ae4827a777 | -11.87356 | -43.71972 | 2024-12-11 04:36:00 | NOAA-21 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 44428bff-f45b-3cf9-9a38-6ddaeafb2d71 | -12.05984 | -46.888 | 2024-12-11 04:36:00 | NOAA-21 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 9a9c7030-9a40-306e-ba18-ed7a437deeb8 | -12.55596 | -58.34696 | 2024-12-11 04:36:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 2f5d461c-31a9-35ae-842a-6f5438791b93 | -11.11228 | -54.64341 | 2024-12-11 04:36:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 9.9 |
| 44ceaa46-482e-3195-be53-e37f45614421 | -14.26683 | -45.78893 | 2024-12-11 04:36:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 7a4b57d9-263b-33fb-bcd9-39c8def31114 | -13.25431 | -41.33916 | 2024-12-11 04:36:00 | NOAA-21 | MUCUGÊ | BAHIA | Brasil | 2921906 | 29 | 33 | nan | nan | nan | Caatinga | 5.1 |
| b95c5c07-8760-359d-b4b1-5832299a1026 | -11.11293 | -54.63962 | 2024-12-11 04:36:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 68654a0b-db14-3a2f-aa8f-6ba7767e0991 | -12.53734 | -57.74102 | 2024-12-11 04:36:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 5.2 |
| f358c0ca-8812-3b7e-a357-b82f1b55c765 | -12.53306 | -58.35529 | 2024-12-11 04:36:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 7.1 |
| c95709c4-68dd-3b62-abbc-89fe760c3118 | -12.55181 | -58.36855 | 2024-12-11 04:36:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 3c444cbc-6d59-3619-bcbf-9e68bab9f6ac | -11.49268 | -48.20056 | 2024-12-11 04:36:00 | NOAA-21 | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 4f213339-7617-3a6f-864f-1a305980fd7f | -11.0052 | -44.34419 | 2024-12-11 04:36:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 3f9d45dd-5656-314b-8e58-d51a1e2ad3b9 | -11.11704 | -54.64037 | 2024-12-11 04:36:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 6.3 |
| fff07efd-09f8-335e-95c0-034a02c916f7 | -11.36141 | -57.80589 | 2024-12-11 04:36:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| fd0d7113-9dc3-334f-a19e-7fc57f4eb604 | -12.56206 | -58.37065 | 2024-12-11 04:36:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 763ab346-bee5-3cbd-b9fa-a4a817210aa5 | -12.54908 | -58.35506 | 2024-12-11 04:36:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 06bae921-f223-3641-b264-290d46a9573c | -11.95423 | -47.84182 | 2024-12-11 04:36:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 5c5e0693-de91-3d21-9604-6bc9c85234d7 | -11.69006 | -48.0843 | 2024-12-11 04:36:00 | NOAA-21 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 546b0cb5-5506-3e47-8ec5-b6b0b9adad11 | -11.04179 | -44.57222 | 2024-12-11 04:36:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 6c652042-3a67-3055-bc29-b0645f5f2c58 | -11.88443 | -54.67668 | 2024-12-11 04:36:00 | NOAA-21 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| a7a2ec12-58e3-3a4a-a431-1f0eca82bb45 | -12.54967 | -58.35199 | 2024-12-11 04:36:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 48fc5de0-64a8-357e-bf26-50a9d03542c5 | -12.41456 | -43.80046 | 2024-12-11 04:36:00 | NOAA-21 | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 30092b9c-a45e-3c0f-bbfd-b55a2c60103b | -12.55931 | -58.3572 | 2024-12-11 04:36:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 5.0 |
| bc3dcd72-f3f1-3391-9f94-71eb10595508 | -11.83195 | -43.84205 | 2024-12-11 04:36:00 | NOAA-21 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 0ea98201-a90e-3409-a268-5d0021d27044 | -12.55242 | -58.36538 | 2024-12-11 04:36:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 2319651c-2d1c-3540-a633-5549679263c6 | -12.53941 | -58.34997 | 2024-12-11 04:36:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 000b419e-d117-3618-9635-dd4e77659163 | -11.10383 | -54.61867 | 2024-12-11 04:36:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1de0b7a4-3310-3daf-b8c1-570e10d0dc18 | -12.53882 | -58.35307 | 2024-12-11 04:36:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 0b581828-a1a4-39cb-8543-36129f65181d | -12.70416 | -54.97154 | 2024-12-11 04:36:00 | NOAA-21 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 59dfc26c-5241-39f2-8669-6ed0f8aeba22 | -12.53609 | -58.33964 | 2024-12-11 04:36:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 4.5 |
| bc30c51e-2342-33d5-a48d-128c7936bd8e | -12.70742 | -54.97171 | 2024-12-11 04:36:00 | NOAA-21 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 86d81301-4f51-3cdb-94fc-986419384c46 | -12.56048 | -58.3511 | 2024-12-11 04:36:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 481dd7f3-29bb-3a52-a6f6-58c355e0d88c | -11.10536 | -54.63435 | 2024-12-11 04:36:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| b201ae2a-3a76-3675-a20c-cafa092ee7cf | -11.11012 | -54.63135 | 2024-12-11 04:36:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| ae1c16bd-36c1-31a3-890d-2ffc1e8fb2a7 | -15.02356 | -57.61681 | 2024-12-11 04:36:00 | NOAA-21 | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 5d1e1ba3-5ca9-33cd-8ede-42976ae08262 | -14.83607 | -43.14801 | 2024-12-11 04:36:00 | NOAA-21 | ESPINOSA | MINAS GERAIS | Brasil | 3124302 | 31 | 33 | nan | nan | nan | Caatinga | 1.3 |


[Clique aqui para ver as próximas entradas](README18.md)
