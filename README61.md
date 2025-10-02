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

## Dados Diários - Página 61

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 7de2a60f-576c-3596-abd3-819118ae8e29 | -3.79095 | -48.63071 | 2025-10-02 04:27:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0a623670-d991-39aa-88ee-623deb42d4f3 | -5.93955 | -44.85624 | 2025-10-02 04:27:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c3675a8e-8a1d-352c-9d72-b8537790a743 | -3.78222 | -48.63094 | 2025-10-02 04:27:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a762dfd7-341d-381a-b5e7-6bb2e249904c | -3.35036 | -43.19294 | 2025-10-02 04:27:00 | NPP-375D | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 3be98de7-3e56-37aa-95b9-0702ade29b7e | -7.03908 | -43.34096 | 2025-10-02 04:29:00 | NPP-375D | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 240f2b1b-0c68-31d7-a424-00fb9e6a8d89 | -11.00488 | -46.58497 | 2025-10-02 04:29:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 0486be80-79e0-3009-ab78-95dd1eb2358e | -10.54473 | -43.64766 | 2025-10-02 04:29:00 | NPP-375D | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f9923411-0ec1-32ad-9cf8-2cb0cef4900a | -10.32787 | -45.25259 | 2025-10-02 04:29:00 | NPP-375D | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 1a6c3746-f52e-3627-8da8-a5b3c39802fa | -11.34823 | -44.97633 | 2025-10-02 04:29:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 8c7c5470-e37b-324e-b39b-111afa74eccc | -11.79926 | -44.99265 | 2025-10-02 04:29:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 0982f055-f954-3564-b655-02c260fa772a | -10.22687 | -50.32447 | 2025-10-02 04:29:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 15.0 |
| dc94381f-a429-39a4-a335-1b981bc2d8e5 | -11.17739 | -47.27165 | 2025-10-02 04:29:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 15.5 |
| 9fd6a490-637f-3857-bce8-a352f0ac6393 | -12.75869 | -39.73987 | 2025-10-02 04:29:00 | NPP-375D | ITATIM | BAHIA | Brasil | 2916856 | 29 | 33 | nan | nan | nan | Caatinga | 10.0 |
| 62896a2e-6784-3e3c-a69e-3cca79066552 | -10.9056 | -44.30442 | 2025-10-02 04:29:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 9e0376a2-6574-309a-aa6d-3442b7e2e537 | -7.7676 | -42.54431 | 2025-10-02 04:29:00 | NPP-375D | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 15.1 |
| cfab4247-1ec1-36d5-9556-97cf6aeb28b9 | -11.17406 | -47.27112 | 2025-10-02 04:29:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 15.5 |
| 8f0cc9b0-d3db-396a-8b37-8fd6d1a3738a | -9.33426 | -45.71226 | 2025-10-02 04:29:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 7cec2b4a-cbcb-3901-b351-a25a8290068c | -10.83238 | -46.6451 | 2025-10-02 04:29:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 61d758cf-9acc-30d0-bca2-ce6340236f4b | -8.84603 | -46.57602 | 2025-10-02 04:29:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 93f4deea-a45e-384b-a689-01aa9f6e6206 | -7.41182 | -45.19178 | 2025-10-02 04:29:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 9d6a7035-141c-3174-bfe9-96ebb3f69a36 | -6.23259 | -44.15026 | 2025-10-02 04:29:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 3b685ee5-584b-350a-b041-88a36ba9fda9 | -7.7753 | -42.53305 | 2025-10-02 04:29:00 | NPP-375D | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 6.8 |
| cc9493d6-3b3c-3bc5-a5e7-141fe9a0d2eb | -11.81593 | -45.02637 | 2025-10-02 04:29:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| fd741f39-3de2-302f-bec6-05d7379a6f5d | -9.4643 | -45.47577 | 2025-10-02 04:29:00 | NPP-375D | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| c2184993-eeff-3cd9-9421-09f1abe9b286 | -7.05075 | -43.31274 | 2025-10-02 04:29:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| 65232fe6-438e-3a85-94c6-e0969422fae2 | -11.42048 | -43.49444 | 2025-10-02 04:29:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 631d6f10-8284-3c33-9225-7d92625f45e1 | -6.36267 | -44.64543 | 2025-10-02 04:29:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 8b80ddcc-6496-3026-85b0-7e87f66492d3 | -8.70773 | -44.84133 | 2025-10-02 04:29:00 | NPP-375D | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 33179520-84ca-3ddd-a186-812920406926 | -10.2514 | -50.3114 | 2025-10-02 04:29:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 12.6 |
| 4b6e6676-7808-30fc-bb6c-b9e5361bccbd | -7.48548 | -43.0403 | 2025-10-02 04:29:00 | NPP-375D | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 3.3 |
| a66abfd4-5a07-3c12-8aad-2fa771e799e8 | -6.31871 | -43.03701 | 2025-10-02 04:29:00 | NPP-375D | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| fb743e35-de60-3c3a-b7b7-8d23891f941f | -9.4609 | -45.47525 | 2025-10-02 04:29:00 | NPP-375D | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| ef168abe-8376-3d9a-910c-66b7df24d860 | -8.88212 | -46.59944 | 2025-10-02 04:29:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| a2f334e5-7181-3d7e-8b11-2869140a4b4d | -6.54961 | -43.9338 | 2025-10-02 04:29:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 1421b4ec-cec1-3cf4-acf7-e08fdecc45e3 | -10.83459 | -46.63091 | 2025-10-02 04:29:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| b101ba9d-3855-3cc0-994f-845b2cd09481 | -8.70377 | -44.82122 | 2025-10-02 04:29:00 | NPP-375D | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 974ff27f-7217-3904-a6ca-df499f738129 | -6.54788 | -43.92171 | 2025-10-02 04:29:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 84ad74be-3ea6-3ff7-a2c1-8d3798a4be71 | -11.12802 | -43.38866 | 2025-10-02 04:29:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 46a3a61d-2ec2-394e-8d72-1d78056a2389 | -10.11799 | -45.3511 | 2025-10-02 04:29:00 | NPP-375D | SÃO GONÇALO DO GURGUÉIA | PIAUÍ | Brasil | 2209757 | 22 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 5a609efc-b2f4-3b56-9016-6e47a1cd9b3e | -9.07413 | -46.71264 | 2025-10-02 04:29:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| d5dfd6ee-124e-38dd-877b-1b661b0a07b1 | -9.93809 | -43.71035 | 2025-10-02 04:29:00 | NPP-375D | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 6780001c-7e1c-3b0f-bbeb-f578193d96ac | -11.10254 | -49.80309 | 2025-10-02 04:29:00 | NPP-375D | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| cea9eedf-ba7b-33b9-846a-48e8783e0c55 | -9.94047 | -43.71951 | 2025-10-02 04:29:00 | NPP-375D | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| a1cbbb45-020f-318a-bdf5-03d836c2f51c | -9.93662 | -43.74529 | 2025-10-02 04:29:00 | NPP-375D | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 14.0 |
| e99c68d7-aaed-3b2b-a115-3bc5bd94356e | -10.38678 | -45.12124 | 2025-10-02 04:29:00 | NPP-375D | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 5c4755f3-d5a6-3c51-8b24-9c7575a5b21a | -11.26832 | -47.81361 | 2025-10-02 04:29:00 | NPP-375D | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 2318b217-5fed-3443-8a04-3b653f875308 | -10.41715 | -51.6665 | 2025-10-02 04:29:00 | NPP-375D | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 8a0518e8-b714-38b4-bd2c-5f8c2d63d466 | -11.11021 | -51.06403 | 2025-10-02 04:29:00 | NPP-375D | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| f4503020-3275-3213-a67d-c2941f232306 | -10.24779 | -50.31079 | 2025-10-02 04:29:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 25.9 |
| 213d98b2-e454-39ed-8bae-20611f6694b5 | -11.17461 | -47.2676 | 2025-10-02 04:29:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 15.5 |
| f19e3ec3-cfc2-390a-b985-51ce77e7e599 | -8.41151 | -47.75449 | 2025-10-02 04:29:00 | NPP-375D | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| b70f4756-0e2d-31c2-aeec-19158fb1e30a | -11.00377 | -46.59209 | 2025-10-02 04:29:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 1d25e6b0-27b5-3d2e-8918-4d658adb2d8a | -7.55919 | -42.64375 | 2025-10-02 04:29:00 | NPP-375D | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 96adb334-c37e-35e8-8160-c5100031626e | -11.15353 | -47.19236 | 2025-10-02 04:29:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b37f9e93-217e-3d0a-a32e-2c1a4cafc9ee | -8.5834 | -49.60552 | 2025-10-02 04:29:00 | NPP-375D | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 078b42df-e739-3b89-ab19-ce1cf4e37a1c | -9.42231 | -47.35626 | 2025-10-02 04:29:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| dad6a899-a9b9-3ca6-a35a-4325faa43ca8 | -11.80283 | -44.96884 | 2025-10-02 04:29:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 3499a725-156a-35fa-b638-4eabfd855496 | -8.79027 | -44.79924 | 2025-10-02 04:29:00 | NPP-375D | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 9afdbf2b-3dbd-3e3a-8319-4d52dd0e0545 | -11.91576 | -46.74274 | 2025-10-02 04:29:00 | NPP-375D | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 0d125de8-cb52-3d9d-920b-7eccd3bcccc1 | -11.16519 | -47.26247 | 2025-10-02 04:29:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 6e21fe35-043f-39d5-9649-6a2c632abd43 | -10.70925 | -48.00184 | 2025-10-02 04:29:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 2d25dd87-348a-31f9-a4de-a3d5e1a16d3b | -11.47354 | -45.00635 | 2025-10-02 04:29:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 1590b47c-e1a1-3793-b37a-97e00e04a804 | -11.8061 | -44.8989 | 2025-10-02 04:29:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| ed02d38e-9d4c-312b-a474-271efec137c1 | -10.25211 | -50.30721 | 2025-10-02 04:29:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| c683606b-d028-303c-a293-3e155165e295 | -10.19459 | -44.89595 | 2025-10-02 04:29:00 | NPP-375D | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 77120a78-cf1d-3c43-82c2-80d43e14ef35 | -8.89433 | -46.60856 | 2025-10-02 04:29:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 1322e0f1-1280-3725-bfc0-b93586890cbf | -11.16017 | -47.40239 | 2025-10-02 04:29:00 | NPP-375D | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 02665b3a-880c-3a07-ac50-6c359681d242 | -10.3069 | -42.39135 | 2025-10-02 04:29:00 | NPP-375D | ITAGUAÇU DA BAHIA | BAHIA | Brasil | 2915353 | 29 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 0573594a-cbb8-3dfd-99af-7aaa878ae3a7 | -11.46487 | -44.96838 | 2025-10-02 04:29:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 582a7612-b557-3a6f-b6b6-d865f13ae212 | -7.55851 | -42.64838 | 2025-10-02 04:29:00 | NPP-375D | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 1089cb11-7f2a-373d-8c3e-7ce351fbf85d | -11.4532 | -43.50885 | 2025-10-02 04:29:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| bbdd45a3-0e42-3c26-890d-f24999b052d4 | -7.78225 | -42.53896 | 2025-10-02 04:29:00 | NPP-375D | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 3.8 |
| 86739ac3-8b3d-31d9-83a6-c28ad3de33b4 | -10.4216 | -48.30386 | 2025-10-02 04:29:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| bddfe3ae-516d-384f-bc16-5f6b048620d1 | -9.93243 | -43.64726 | 2025-10-02 04:29:00 | NPP-375D | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 4454a3ef-c1fd-3358-a97f-769e88c31bb3 | -11.47295 | -45.01025 | 2025-10-02 04:29:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| efa00398-81a1-333e-9dbe-c2738e74ed1b | -6.68984 | -42.81873 | 2025-10-02 04:29:00 | NPP-375D | FRANCISCO AYRES | PIAUÍ | Brasil | 2204105 | 22 | 33 | nan | nan | nan | Caatinga | 6.2 |
| 4eb355df-5852-3c2a-ab5e-1187993e8a12 | -10.81736 | -47.96875 | 2025-10-02 04:29:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 13e1c61f-abc5-3e59-b33a-6d1df647520e | -8.85934 | -46.57814 | 2025-10-02 04:29:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| a68acd6f-5562-30dd-9d24-302c2002f92d | -9.03638 | -46.67759 | 2025-10-02 04:29:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ad2e1e5a-d6d1-32a3-a39f-a4860a7390ac | -8.57205 | -49.60773 | 2025-10-02 04:29:00 | NPP-375D | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| e792aa7c-3e16-32fe-b616-e278e8084e7e | -12.11023 | -43.43211 | 2025-10-02 04:29:00 | NPP-375D | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| e9781660-5906-39ab-98d5-05a77d341c89 | -8.87433 | -46.58387 | 2025-10-02 04:29:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 1ac61856-6ea9-35bb-bce0-fd8d14b7516a | -11.79659 | -47.57003 | 2025-10-02 04:29:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f9e8c80b-c7d2-3ffd-b942-ad148e765069 | -9.84614 | -49.95976 | 2025-10-02 04:29:00 | NPP-375D | MARIANÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1712504 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c42ccf38-72d9-32a2-9548-ee6b505e7bd3 | -8.8416 | -46.58248 | 2025-10-02 04:29:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 156c92fb-d8bb-3d83-a1ec-193e989981d3 | -7.0053 | -44.50699 | 2025-10-02 04:29:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| bad681d7-55d1-3335-9d6d-7fd32735db5c | -10.829 | -46.62275 | 2025-10-02 04:29:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| ccf587a6-544f-3b4e-99ef-0a8a76e57443 | -11.6176 | -45.05442 | 2025-10-02 04:29:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 42d930b3-15d1-3ead-b463-e71ed0ad205e | -9.80453 | -47.84446 | 2025-10-02 04:29:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 7fbffb5b-35e6-39b9-9a1b-e070dbf1e061 | -10.81272 | -46.5841 | 2025-10-02 04:29:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.3 |
| 4f04b2d8-706e-3ba2-9f5c-29c44d4953a1 | -9.94093 | -43.74155 | 2025-10-02 04:29:00 | NPP-375D | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 8.4 |
| e3745dac-c6f0-3da9-8ee4-e8a8c1db95e2 | -9.94586 | -43.58218 | 2025-10-02 04:29:00 | NPP-375D | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 8f0f9ebd-4d64-30df-9b87-7ce2b5721307 | -11.79749 | -45.00441 | 2025-10-02 04:29:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 9daa5368-dba5-3a57-959e-341708b8ab73 | -9.94522 | -43.66259 | 2025-10-02 04:29:00 | NPP-375D | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 77b0bf98-aed5-3270-a59e-92e9782bf8f6 | -7.55959 | -42.40047 | 2025-10-02 04:29:00 | NPP-375D | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 12338f9f-7457-34a9-a229-fd53fe1c0e92 | -6.33268 | -43.04333 | 2025-10-02 04:29:00 | NPP-375D | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e1512000-2700-3368-9e1d-e08255c79f19 | -11.5799 | -47.65812 | 2025-10-02 04:29:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| c9805eae-5818-339d-9b89-98672bbd4cc0 | -9.94847 | -43.71627 | 2025-10-02 04:29:00 | NPP-375D | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 33d6aee7-b5d8-3492-891d-14c5b49d7b81 | -11.08718 | -47.71188 | 2025-10-02 04:29:00 | NPP-375D | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a6e97b37-0666-3291-9382-64b168f1e02d | -10.94492 | -44.26338 | 2025-10-02 04:29:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |


[Clique aqui para ver as próximas entradas](README62.md)
