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

## Dados Diários - Página 12

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| f0fa0fcd-1fe2-3a1f-98d7-397e66650ce2 | -9.58303 | -43.84595 | 2025-08-02 03:55:00 | NOAA-20 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 693f0fab-1768-3d3d-b1ff-252814061d65 | -12.65356 | -44.51157 | 2025-08-02 03:55:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 10.2 |
| 35d644de-7301-3a82-b92c-e264246510e9 | -12.67096 | -44.50685 | 2025-08-02 03:55:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 075b79f4-8b56-35c6-8695-7f22aabe2da9 | -13.2156 | -42.24854 | 2025-08-02 03:55:00 | NOAA-20 | CATURAMA | BAHIA | Brasil | 2907558 | 29 | 33 | nan | nan | nan | Caatinga | 4.9 |
| cd2441ad-01c0-32c1-b658-75084698058b | -12.65614 | -44.4965 | 2025-08-02 03:55:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 7.1 |
| b7bb0e25-aafc-3916-a025-291eb2f41097 | -12.53997 | -44.72255 | 2025-08-02 03:55:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| fc59be3a-e721-38ba-a20c-b8f429384d15 | -14.79417 | -42.72283 | 2025-08-02 03:55:00 | NOAA-20 | URANDI | BAHIA | Brasil | 2932606 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| cf56a80f-fae3-35b9-a401-2cc2bff8405f | -10.58539 | -45.2688 | 2025-08-02 03:55:00 | NOAA-20 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| b4dafc25-d1a5-30d8-9547-6a3874e89223 | -9.04674 | -45.07743 | 2025-08-02 03:55:00 | NOAA-20 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| c073334f-988c-3d97-90f1-8b9895b57002 | -12.65786 | -44.48648 | 2025-08-02 03:55:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 93e85ec9-4de5-32cf-8a72-8fdbd81c823f | -10.59031 | -45.26561 | 2025-08-02 03:55:00 | NOAA-20 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| bb5b4b8b-e240-364e-a65b-ec460181a774 | -12.67519 | -44.52834 | 2025-08-02 03:55:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 0c79adf8-bef9-37ce-8f4f-9130190f97c1 | -10.25492 | -50.25424 | 2025-08-02 03:55:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 13.0 |
| a9d17572-60e6-3672-90d1-7d536cbf019a | -10.59453 | -45.26634 | 2025-08-02 03:55:00 | NOAA-20 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| e756c0fd-0e67-3531-bc36-0b9a13549c6a | -9.06732 | -45.06014 | 2025-08-02 03:55:00 | NOAA-20 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 8e179a3a-7bb4-35f4-ab5a-0168bcc734d4 | -10.07819 | -46.78309 | 2025-08-02 03:55:00 | NOAA-20 | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 713d15b0-34c0-3f40-b9b9-6ba64486b7c5 | -11.77238 | -45.01729 | 2025-08-02 03:55:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 56bc3082-94c9-32df-b1ea-fd4c267acf84 | -12.66003 | -44.49722 | 2025-08-02 03:55:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 129ca8eb-65da-37e4-9ed2-c354237395af | -12.44998 | -47.03884 | 2025-08-02 03:55:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e46b3ca8-7d39-3f7a-adfc-e270c49aa0e4 | -12.65872 | -44.53055 | 2025-08-02 03:55:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 2faaaadb-0b09-3ee3-8b79-a56c03ede953 | -12.03343 | -44.02337 | 2025-08-02 03:55:00 | NOAA-20 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 90118170-e5aa-37e3-bbcd-adf194575de2 | -10.03985 | -44.71466 | 2025-08-02 03:55:00 | NOAA-20 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 10.0 |
| 23ec70b9-e6d1-3d34-a51b-260582698a2b | -12.66477 | -44.49293 | 2025-08-02 03:55:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 9db6c589-61c8-3f6a-88f0-f863393a159c | -12.67307 | -44.51758 | 2025-08-02 03:55:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 0ab19a17-131b-30c1-8ffb-e654443958b7 | -12.66319 | -44.50541 | 2025-08-02 03:55:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 13.2 |
| 2e5520e4-a986-3e3f-9857-69237bc01a06 | -12.26221 | -45.06096 | 2025-08-02 03:55:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 87a5afe4-a4e5-398c-a72f-b65aee707898 | -12.66174 | -44.4872 | 2025-08-02 03:55:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 0e613970-63fe-3217-bd50-8bf357fd7bb7 | -13.02834 | -47.4318 | 2025-08-02 03:55:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| d8ddcc47-d39d-36ea-8862-a7bf8bb3f151 | -16.26953 | -42.37582 | 2025-08-02 03:55:00 | NOAA-20 | FRUTA DE LEITE | MINAS GERAIS | Brasil | 3127073 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 61450351-73bc-3151-a8ac-f9208ee9782e | -15.75818 | -49.94654 | 2025-08-02 03:55:00 | NOAA-20 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 37.2 |
| e4b96ac1-6a11-3869-a305-5888d5c60920 | -12.47025 | -47.05793 | 2025-08-02 03:55:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 6539bfd6-0c81-3fec-9929-29ee14a97134 | -13.21444 | -47.24775 | 2025-08-02 03:55:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 3e353e65-85a5-34c0-86e9-5333d387f15a | -13.05074 | -47.44141 | 2025-08-02 03:55:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 9ba4bf36-0308-3d98-a659-2708b84615e6 | -12.66305 | -44.50297 | 2025-08-02 03:55:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 17.2 |
| fa7f2bd3-ed0d-31ef-b8d1-cb8106a8b4f8 | -12.6602 | -44.49968 | 2025-08-02 03:55:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 17.4 |
| 841d5f9c-ac3c-30a9-911d-93913e030efb | -10.58045 | -45.27204 | 2025-08-02 03:55:00 | NOAA-20 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 31bbdd13-d75e-3857-81f6-8e70ee5b2b41 | -10.02754 | -44.71244 | 2025-08-02 03:55:00 | NOAA-20 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 7f167551-480c-3be2-ba69-6ce08373e84c | -12.67574 | -44.50256 | 2025-08-02 03:55:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 61b812bb-c885-3abb-9c12-18be45bb0993 | -13.69115 | -51.95429 | 2025-08-02 03:55:00 | NOAA-20 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| bac3866e-99a7-3c8e-84b6-da8b0e2d55b1 | -12.66918 | -44.51687 | 2025-08-02 03:55:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 4dfece72-97dc-3906-afd5-0f90679079f8 | -11.56705 | -44.8526 | 2025-08-02 03:55:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| d2531793-5daf-397d-af12-6752d465344d | -15.76177 | -49.95364 | 2025-08-02 03:55:00 | NOAA-20 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 13.5 |
| f388b48a-a7a6-36ce-b8f6-0ffc79447ab9 | -10.03165 | -44.71316 | 2025-08-02 03:55:00 | NOAA-20 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 6.7 |
| bc7a97e6-5a71-39aa-bf8b-3d63a266622f | -10.03576 | -44.71389 | 2025-08-02 03:55:00 | NOAA-20 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 23079473-4fdb-37a4-9844-5bbda79f70f2 | -12.6623 | -44.51042 | 2025-08-02 03:55:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 10.2 |
| 5488f1ea-12b0-3fef-b5f0-8164a32c6752 | -12.66475 | -48.08749 | 2025-08-02 03:55:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a6f6e802-445b-325a-b501-72db63955a91 | -12.03425 | -44.01863 | 2025-08-02 03:55:00 | NOAA-20 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 4988d8ae-6449-323d-b08a-213dd4746a39 | -12.67129 | -44.52763 | 2025-08-02 03:55:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 2ead2b6e-9794-3cfc-8136-bc4cddf2247a | -12.65631 | -44.49896 | 2025-08-02 03:55:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 17.4 |
| 7a400d98-2335-3c70-9fcb-3c9a50845a86 | -9.5873 | -44.43383 | 2025-08-02 03:55:00 | NOAA-20 | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 2c03878a-0371-3078-be01-225a373626a7 | -9.39489 | -45.49527 | 2025-08-02 03:55:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 9b31713f-b42b-3767-a817-cc4d52470b28 | -10.07534 | -46.77973 | 2025-08-02 03:55:00 | NOAA-20 | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 1c6f25f9-cff5-3736-aacf-a831dee5354c | -13.05447 | -47.44741 | 2025-08-02 03:55:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 6430f4d3-f089-3eb8-97c9-f5bf1a26ce0e | -12.44908 | -47.04366 | 2025-08-02 03:55:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 86586c92-8ca3-38a5-9e59-1631f6d4ca66 | -12.65243 | -44.49824 | 2025-08-02 03:55:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 4.2 |
| c07fdc6a-c733-360f-a373-56b93b9b8324 | -20.4358 | -46.42914 | 2025-08-02 03:57:00 | NOAA-20 | VARGEM BONITA | MINAS GERAIS | Brasil | 3170602 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| a58aaf43-183b-366a-92c7-2cd3044fbd44 | -21.34484 | -45.84073 | 2025-08-02 03:57:00 | NOAA-20 | ALFENAS | MINAS GERAIS | Brasil | 3101607 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| e04aa36e-f46d-3b3f-9c08-5b401eac2330 | -22.5662 | -45.23899 | 2025-08-02 03:57:00 | NOAA-20 | DELFIM MOREIRA | MINAS GERAIS | Brasil | 3121100 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 88f0b7f5-0d0f-38d6-8c53-2e66e33cf356 | -20.0729 | -45.81376 | 2025-08-02 03:57:00 | NOAA-20 | IGUATAMA | MINAS GERAIS | Brasil | 3130309 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c7eea30e-d9c7-3e81-b2ce-5597c2c07ab7 | -19.819 | -42.16178 | 2025-08-02 03:57:00 | NOAA-20 | CARATINGA | MINAS GERAIS | Brasil | 3113404 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 42b19c75-d428-343f-9c7c-3e396df24493 | -19.76291 | -46.04153 | 2025-08-02 03:57:00 | NOAA-20 | CÓRREGO DANTA | MINAS GERAIS | Brasil | 3119807 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| fe742a72-3769-3244-bd7a-42eed9c1d9f2 | -20.3263 | -46.62707 | 2025-08-02 03:57:00 | NOAA-20 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 447725d2-e8ea-3169-adb0-6740b2db937e | -17.1696 | -42.83591 | 2025-08-02 03:57:00 | NOAA-20 | TURMALINA | MINAS GERAIS | Brasil | 3169703 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 663570f3-bc28-3ccb-807a-5db6c24d97f6 | -21.03915 | -40.84805 | 2025-08-02 03:57:00 | NOAA-20 | ITAPEMIRIM | ESPÍRITO SANTO | Brasil | 3202801 | 32 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 2df1dbe8-cc92-3cfb-b297-2a6e8d873d94 | -18.92898 | -52.48511 | 2025-08-02 03:57:00 | NOAA-20 | CASSILÂNDIA | MATO GROSSO DO SUL | Brasil | 5002902 | 50 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 0883e60b-a277-3f99-ae59-2577f0bbe770 | -17.57236 | -47.50573 | 2025-08-02 03:57:00 | NOAA-20 | CATALÃO | GOIÁS | Brasil | 5205109 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c0ff8cdf-b0cd-3691-8c22-c890ddf7539c | -20.00307 | -45.39494 | 2025-08-02 03:57:00 | NOAA-20 | SANTO ANTÔNIO DO MONTE | MINAS GERAIS | Brasil | 3160405 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 2c83aa42-7608-3120-bd88-de678aa5fc75 | -18.92226 | -52.48805 | 2025-08-02 03:57:00 | NOAA-20 | CHAPADÃO DO SUL | MATO GROSSO DO SUL | Brasil | 5002951 | 50 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a7a8b041-0590-30c1-a1d6-61481291a241 | -20.79299 | -41.12871 | 2025-08-02 03:57:00 | NOAA-20 | CACHOEIRO DE ITAPEMIRIM | ESPÍRITO SANTO | Brasil | 3201209 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 31264075-9d6b-3fd5-97ce-497ea98844fe | -17.9193 | -42.74014 | 2025-08-02 03:57:00 | NOAA-20 | ITAMARANDIBA | MINAS GERAIS | Brasil | 3132503 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 13021e18-79ac-3357-8bb6-6cc44664e9ad | -20.32296 | -46.62449 | 2025-08-02 03:57:00 | NOAA-20 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 9e9d60b9-ac7e-3e65-bc2b-4f9eb63482c7 | -19.75536 | -46.03955 | 2025-08-02 03:57:00 | NOAA-20 | CÓRREGO DANTA | MINAS GERAIS | Brasil | 3119807 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c26c321e-bef9-3c2b-934d-6a519265f98c | -16.59094 | -49.37092 | 2025-08-02 03:57:00 | NOAA-20 | GOIÂNIA | GOIÁS | Brasil | 5208707 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| b2e2cb63-8108-312a-bfe4-2be38be92257 | -18.24193 | -45.16856 | 2025-08-02 03:57:00 | NOAA-20 | TRÊS MARIAS | MINAS GERAIS | Brasil | 3169356 | 31 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 36f119f7-5828-30e4-8b60-85aaa975d1f0 | -22.87965 | -43.27018 | 2025-08-02 03:57:00 | NOAA-20 | RIO DE JANEIRO | RIO DE JANEIRO | Brasil | 3304557 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| c852735f-87a9-3a6d-9865-ccec45c7ddd8 | -18.92221 | -52.48866 | 2025-08-02 03:57:00 | NOAA-20 | CHAPADÃO DO SUL | MATO GROSSO DO SUL | Brasil | 5002951 | 50 | 33 | nan | nan | nan | Cerrado | 1.6 |
| b10fac61-346f-334c-bb88-cf603714b7d9 | -22.40318 | -46.78905 | 2025-08-02 03:57:00 | NOAA-20 | ITAPIRA | SÃO PAULO | Brasil | 3522604 | 35 | 33 | nan | nan | nan | Cerrado | 8.2 |
| 82c175b0-14f2-3759-a809-a0523d0e712a | -19.30645 | -48.91052 | 2025-08-02 03:57:00 | NOAA-20 | PRATA | MINAS GERAIS | Brasil | 3152808 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 4273d8bc-ce06-3bdf-8724-f96d510ee532 | -20.22414 | -43.8048 | 2025-08-02 03:57:00 | NOAA-20 | ITABIRITO | MINAS GERAIS | Brasil | 3131901 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| 634857c6-d2ea-33e0-bf2e-0743efd08414 | -20.0494 | -42.14518 | 2025-08-02 03:57:00 | NOAA-20 | MANHUAÇU | MINAS GERAIS | Brasil | 3139409 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| f17efa1b-27d1-3bae-bded-90aea9470471 | -17.67933 | -44.43732 | 2025-08-02 03:57:00 | NOAA-20 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 0.3 |
| b9b3bd00-768e-3642-9877-630a0627b32c | -22.74163 | -47.02987 | 2025-08-02 03:57:00 | NOAA-20 | CAMPINAS | SÃO PAULO | Brasil | 3509502 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.6 |
| 9f850d01-c8bd-3485-9998-381ed584be59 | -21.1988 | -44.99337 | 2025-08-02 03:57:00 | NOAA-20 | LAVRAS | MINAS GERAIS | Brasil | 3138203 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| eee160ff-f2cc-3570-9d86-4e8779055727 | -21.54412 | -48.72372 | 2025-08-02 03:57:00 | NOAA-20 | ITÁPOLIS | SÃO PAULO | Brasil | 3522703 | 35 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 00e20c17-2386-3ef8-9f27-3b4e93634f3d | -19.91899 | -44.6843 | 2025-08-02 03:57:00 | NOAA-20 | IGARATINGA | MINAS GERAIS | Brasil | 3130200 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ee16ac99-0da5-3d43-8c49-1a71c81068b2 | -17.2307 | -42.55011 | 2025-08-02 03:57:00 | NOAA-20 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 3f88d85c-20d0-3763-965b-ba5f02b3f300 | -18.52959 | -49.50035 | 2025-08-02 03:57:00 | NOAA-20 | CACHOEIRA DOURADA | MINAS GERAIS | Brasil | 3109808 | 31 | 33 | nan | nan | nan | Mata Atlântica | 7.7 |
| 45d4cba6-6158-3371-989e-ee166d0bdc3b | -16.69991 | -49.3953 | 2025-08-02 03:57:00 | NOAA-20 | GOIÂNIA | GOIÁS | Brasil | 5208707 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 0bb74389-b965-3976-963c-a18229b4ab48 | -19.57329 | -40.78815 | 2025-08-02 03:57:00 | NOAA-20 | COLATINA | ESPÍRITO SANTO | Brasil | 3201506 | 32 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| d691dd45-31f3-3ccd-a3f0-6b8a9f3a11e1 | -20.14596 | -42.13559 | 2025-08-02 03:57:00 | NOAA-20 | MANHUAÇU | MINAS GERAIS | Brasil | 3139409 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| dfb85015-07e4-3c30-a3cf-8123f183264d | -16.24817 | -48.95672 | 2025-08-02 03:57:00 | NOAA-20 | ANÁPOLIS | GOIÁS | Brasil | 5201108 | 52 | 33 | nan | nan | nan | Cerrado | 4.3 |
| f0008255-f65b-382e-86b4-eb4f9f5d1c38 | -19.3003 | -46.20993 | 2025-08-02 03:57:00 | NOAA-20 | RIO PARANAÍBA | MINAS GERAIS | Brasil | 3155504 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| bbc28b74-f266-3678-ae24-ddf8c7892075 | -19.91645 | -44.68556 | 2025-08-02 03:57:00 | NOAA-20 | IGARATINGA | MINAS GERAIS | Brasil | 3130200 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| aa4ff0d2-8556-3f97-90d2-848136d0c9d9 | -22.40011 | -43.43528 | 2025-08-02 03:57:00 | NOAA-20 | PATY DO ALFERES | RIO DE JANEIRO | Brasil | 3303856 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 54e7dc9d-64b0-3165-8ed2-22c8c41bb18e | -18.21026 | -44.71215 | 2025-08-02 03:57:00 | NOAA-20 | CORINTO | MINAS GERAIS | Brasil | 3119104 | 31 | 33 | nan | nan | nan | Cerrado | 4.2 |
| a16ad662-a6ef-3b5e-831e-4929307b456b | -22.78614 | -46.3181 | 2025-08-02 03:57:00 | NOAA-20 | EXTREMA | MINAS GERAIS | Brasil | 3125101 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| a5f818a3-20d8-33ac-8597-9adfecc5988c | -22.80802 | -46.17521 | 2025-08-02 03:57:00 | NOAA-20 | CAMANDUCAIA | MINAS GERAIS | Brasil | 3110509 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| e21a854e-0b69-375a-a8d8-e8a0916fb750 | -19.74586 | -46.02655 | 2025-08-02 03:57:00 | NOAA-20 | CÓRREGO DANTA | MINAS GERAIS | Brasil | 3119807 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 970268de-31fc-3306-af10-2008bf905512 | -16.70561 | -47.57318 | 2025-08-02 03:57:00 | NOAA-20 | CRISTALINA | GOIÁS | Brasil | 5206206 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 2e7dfb01-5b49-3ba1-97db-2e86cef8a7c2 | -18.9168 | -44.68885 | 2025-08-02 03:57:00 | NOAA-20 | CURVELO | MINAS GERAIS | Brasil | 3120904 | 31 | 33 | nan | nan | nan | Cerrado | 0.4 |


[Clique aqui para ver as próximas entradas](README13.md)
