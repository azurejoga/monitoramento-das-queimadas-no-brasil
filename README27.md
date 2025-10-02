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

## Dados Diários - Página 27

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| faf44b50-7bdb-390e-b74e-60fddd5538d4 | -11.4442 | -43.88651 | 2025-10-02 04:02:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 3c932408-4e35-3137-ae3e-9e68a2a766a2 | -11.80986 | -45.00488 | 2025-10-02 04:02:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 3.1 |
| f2caa5f3-d8f7-32a7-89d7-2a0877f9affa | -10.14361 | -42.1351 | 2025-10-02 04:02:00 | NOAA-21 | SENTO SÉ | BAHIA | Brasil | 2930204 | 29 | 33 | nan | nan | nan | Caatinga | 2.2 |
| f6104dab-9873-39b8-b39c-95ca1f64da92 | -11.48134 | -44.98995 | 2025-10-02 04:02:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 56381f4b-457d-313c-94ca-6c79dd284b44 | -12.93293 | -45.10299 | 2025-10-02 04:02:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 36647d64-aa04-3914-9f1f-28af710d5187 | -11.0941 | -47.82211 | 2025-10-02 04:02:00 | NOAA-21 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| c820370d-59d0-3dc1-994b-eaf17ea905ea | -11.17469 | -47.26116 | 2025-10-02 04:02:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 9.1 |
| 03b42528-3206-3c85-974e-01ccd96923b0 | -6.70112 | -48.70894 | 2025-10-02 04:02:00 | NOAA-21 | ARAGOMINAS | TOCANTINS | Brasil | 1701309 | 17 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 4903eba7-d91d-3e59-a734-c65bd2ef2aed | -11.03901 | -47.82032 | 2025-10-02 04:02:00 | NOAA-21 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 41b123e1-fc84-3301-a16b-da4119ece535 | -10.26939 | -50.3222 | 2025-10-02 04:02:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 7.9 |
| a4b7dbb1-a768-3a1c-96ab-30a07e66e1f1 | -11.16923 | -47.19159 | 2025-10-02 04:02:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| a25cba86-196a-329a-9638-dec8ef390c96 | -10.82346 | -46.63243 | 2025-10-02 04:02:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 10.1 |
| f91658be-4131-3582-9f03-6cc921aa8034 | -11.06012 | -47.80558 | 2025-10-02 04:02:00 | NOAA-21 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 2ca64037-49f4-37f2-856c-21cced3aafb3 | -11.82077 | -45.03006 | 2025-10-02 04:02:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 65427f88-bb83-3e62-a72b-5b4b52ede83f | -11.09684 | -47.82188 | 2025-10-02 04:02:00 | NOAA-21 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| b0f73b12-daa1-3b1f-942b-8a398655a72d | -12.22312 | -43.76513 | 2025-10-02 04:02:00 | NOAA-21 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |
| c9e581ac-1490-3de8-a5eb-d5646622866e | -9.9463 | -43.72046 | 2025-10-02 04:02:00 | NOAA-21 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 3.6 |
| ab59e0c3-21d3-380a-a1a1-b843a206f5b9 | -10.85158 | -46.59363 | 2025-10-02 04:02:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| faf82af6-3a34-3456-bfda-69bcf4fb37a5 | -11.78745 | -47.56395 | 2025-10-02 04:02:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| ae9d941d-5760-330b-a018-161d944f206e | -9.94692 | -43.58333 | 2025-10-02 04:02:00 | NOAA-21 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 1e7bcabd-ad20-3a89-b045-823f88385fcb | -11.00759 | -46.58189 | 2025-10-02 04:02:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 0239900d-97b2-397b-ba0a-fb0bf7d628bd | -6.72862 | -44.14317 | 2025-10-02 04:02:00 | NOAA-21 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| eb4a91a1-c4b5-39e2-b333-03c31e30e12d | -9.90508 | -43.70512 | 2025-10-02 04:02:00 | NOAA-21 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 127144ad-d0b2-3b51-aec7-fc59e7cdd850 | -10.1906 | -50.28232 | 2025-10-02 04:02:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| ce0b2e25-65cc-3362-8ad1-e83a78a3992d | -7.723 | -46.21834 | 2025-10-02 04:02:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| fa0676e4-3a10-36cf-9bce-9f3f758f6bb7 | -11.51314 | -43.56437 | 2025-10-02 04:02:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| b481b576-e570-3997-97d8-ef3da921872b | -10.26874 | -50.32565 | 2025-10-02 04:02:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 7.9 |
| c526f8ff-9073-37c2-a2c2-0ef1449c7c61 | -12.10927 | -43.42859 | 2025-10-02 04:02:00 | NOAA-21 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 04b7d6a8-96a4-3ab7-a90c-7961e0127c92 | -6.72406 | -44.14716 | 2025-10-02 04:02:00 | NOAA-21 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 13.6 |
| abde0014-bfe4-3c7f-b256-fc4fdb9348c2 | -12.80563 | -46.86554 | 2025-10-02 04:02:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 5112f74b-bda2-39a5-b227-e54d6b6b3630 | -11.86598 | -45.03343 | 2025-10-02 04:02:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| db8ad3cd-5e0e-3479-8bc6-c060683f387f | -7.55515 | -42.40516 | 2025-10-02 04:02:00 | NOAA-21 | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 3.1 |
| 86f8ae77-6f23-3d4f-869a-cd1e9fa2d34c | -12.20171 | -47.81097 | 2025-10-02 04:02:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 681f5034-4138-3255-8168-6efa6d87b727 | -11.58775 | -47.64401 | 2025-10-02 04:02:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 9a5368bc-e636-3493-ad94-4adaf09be1a9 | -11.60934 | -45.05809 | 2025-10-02 04:02:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 87baa7e7-8fd6-3f60-b193-7c0e3744936f | -12.75255 | -46.90638 | 2025-10-02 04:02:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 1e947124-6abe-3e18-a090-157cd306e1d0 | -6.95527 | -45.3205 | 2025-10-02 04:02:00 | NOAA-21 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 11.2 |
| da08fc77-0360-3ad3-97b9-6585852c05ca | -11.91809 | -46.74503 | 2025-10-02 04:02:00 | NOAA-21 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| b9265294-1613-3e98-b55e-b31d848ce977 | -6.48766 | -44.28744 | 2025-10-02 04:02:00 | NOAA-21 | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 64bc09b6-7da5-35f1-b4a3-333e6281440a | -12.89859 | -46.91137 | 2025-10-02 04:02:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| ef42adc1-324f-3bb8-a1b7-4b19a3f7ae84 | -7.46342 | -46.4632 | 2025-10-02 04:02:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 3c617f40-490b-3212-99d4-2201d2985c62 | -6.27589 | -44.05904 | 2025-10-02 04:02:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| c2664d3a-4281-3794-a69d-69582a8efab1 | -8.57681 | -49.60646 | 2025-10-02 04:02:00 | NOAA-21 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 1d346836-a912-38c6-81e6-1493cba2b9c1 | -6.27211 | -44.05839 | 2025-10-02 04:02:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| d3227c21-6b08-3f44-8d0f-3c7421d8c07b | -12.41818 | -44.08527 | 2025-10-02 04:02:00 | NOAA-21 | TABOCAS DO BREJO VELHO | BAHIA | Brasil | 2930907 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| b4535ee3-c98b-3088-b25c-4cf462ffbda4 | -11.84429 | -44.95979 | 2025-10-02 04:02:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| b1385982-210b-3467-b664-0ba05f81d0da | -9.42313 | -47.35714 | 2025-10-02 04:02:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| cf3183fe-0717-3617-8c1e-97288da2a9fd | -10.86181 | -46.58379 | 2025-10-02 04:02:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 70d0477f-7211-3a13-8f21-0e633c8bf755 | -11.8757 | -45.02107 | 2025-10-02 04:02:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 399ff547-535a-398b-86c4-76522baa9cf3 | -12.85234 | -46.93459 | 2025-10-02 04:02:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 20dbf995-f79a-332e-8d84-46ec7054c66c | -11.34996 | -44.97561 | 2025-10-02 04:02:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 53c67971-bd6d-3d1b-a82a-729dd8829fd7 | -12.25839 | -47.82294 | 2025-10-02 04:02:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| be00fc16-6d17-369d-9aea-fe2f61734fcc | -9.94831 | -43.70819 | 2025-10-02 04:02:00 | NOAA-21 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 218e487d-9fb4-3750-8caf-b3d6b45d1466 | -11.48272 | -45.00407 | 2025-10-02 04:02:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 2a55e091-b60b-3980-821c-8bcbbd0a994d | -9.08875 | -46.72446 | 2025-10-02 04:02:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 3ec9f421-c992-387c-8e56-01fdb2f9d1a1 | -7.02835 | -38.82619 | 2025-10-02 04:02:00 | NOAA-21 | BARRO | CEARÁ | Brasil | 2302008 | 23 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 99838396-b9c9-3784-a37f-0f85b2c548cd | -9.93896 | -43.76549 | 2025-10-02 04:02:00 | NOAA-21 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 5.7 |
| 054269df-b1dd-397f-9373-03ef9cbdd54f | -11.85418 | -48.04905 | 2025-10-02 04:02:00 | NOAA-21 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| cefc7593-363f-3fd6-80c7-4ac0fcfd0994 | -11.56922 | -47.02165 | 2025-10-02 04:02:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 5.9 |
| d553b0d6-9b10-39ff-9d99-ddab86d73e8b | -8.87298 | -46.58675 | 2025-10-02 04:02:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 560c16b4-fc53-3a77-aaf0-c263382940cb | -12.9552 | -46.37245 | 2025-10-02 04:02:00 | NOAA-21 | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 104b186f-c55d-3272-b8da-1fa351489dbf | -10.8008 | -44.23915 | 2025-10-02 04:02:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 52b410a9-d023-30e8-b9f4-92cc14d96016 | -12.88282 | -46.90519 | 2025-10-02 04:02:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 2dcb1b4b-0754-3b8c-8681-ee6e65d96a7a | -6.81801 | -45.99253 | 2025-10-02 04:02:00 | NOAA-21 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 01e480b4-1175-3bda-af62-1a796928cc1d | -12.66059 | -46.88225 | 2025-10-02 04:02:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| ab72723a-4c2b-3d02-8023-5220450f28d7 | -11.76808 | -46.8341 | 2025-10-02 04:02:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| acf0d066-36c5-34a7-9d0a-a2d6571ab241 | -6.96721 | -38.55184 | 2025-10-02 04:02:00 | NOAA-21 | CAJAZEIRAS | PARAÍBA | Brasil | 2503704 | 25 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 93d72f09-1a10-3539-857f-0ef36f4c7ec1 | -10.77798 | -46.5994 | 2025-10-02 04:02:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 44c8c01b-8e89-3685-ba64-6d15b3d42450 | -12.82353 | -47.02531 | 2025-10-02 04:02:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| cda57064-c277-3184-a709-866689cc31a5 | -6.72822 | -44.14467 | 2025-10-02 04:02:00 | NOAA-21 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| ec11c8f2-3767-3224-9c38-99c9509668b6 | -10.2546 | -50.31226 | 2025-10-02 04:02:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 23bb5ae6-63c6-31bc-a901-06c103928639 | -11.81945 | -45.01559 | 2025-10-02 04:02:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| d9a7ae02-3012-3272-8d86-4eb755596f0d | -11.14039 | -43.37551 | 2025-10-02 04:02:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 5e4d9095-b6d0-35aa-b101-1b9c11686335 | -9.33543 | -45.91861 | 2025-10-02 04:02:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 5f0bc023-3ee1-3a3a-9e30-2503001dec3d | -6.27664 | -44.05441 | 2025-10-02 04:02:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 4.6 |
| b83fe15b-7b3d-3f0f-bc6f-9209e2975d03 | -6.26527 | -43.88781 | 2025-10-02 04:02:00 | NOAA-21 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 7db04cfe-7200-3fb4-869e-087e7c8d76f9 | -10.65947 | -48.49996 | 2025-10-02 04:02:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| c58e8c74-d906-3b2a-a534-b92aa412861f | -6.96336 | -45.32202 | 2025-10-02 04:02:00 | NOAA-21 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 87e7dccd-7f77-3240-9662-87f3721b942e | -10.81514 | -46.63103 | 2025-10-02 04:02:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 7.4 |
| ed46ce19-11a1-3ab9-bf15-5a070654244c | -6.85885 | -48.65374 | 2025-10-02 04:02:00 | NOAA-21 | ARAGOMINAS | TOCANTINS | Brasil | 1701309 | 17 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 08926f8d-7020-3e66-8b9a-dfc1307cb8f1 | -11.35442 | -44.97189 | 2025-10-02 04:02:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| f68f796f-9f9d-34f7-ac11-8381da34e5a9 | -10.99311 | -46.60207 | 2025-10-02 04:02:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 16.4 |
| 13e627d9-25ee-35e4-844d-45a5e4118296 | -12.87554 | -47.01951 | 2025-10-02 04:02:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 1c5ccd4c-23c0-3237-931d-1a1b4b3d07e0 | -6.72747 | -44.14933 | 2025-10-02 04:02:00 | NOAA-21 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| d75290c3-c069-312e-b60e-06e594650e75 | -11.83769 | -44.95396 | 2025-10-02 04:02:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| ec60398f-cd0f-3717-8107-816cc3c9e3fc | -11.81651 | -45.01054 | 2025-10-02 04:02:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| a12b0eaf-1181-3a68-9e15-485206b50c03 | -6.69032 | -42.82227 | 2025-10-02 04:02:00 | NOAA-21 | FRANCISCO AYRES | PIAUÍ | Brasil | 2204105 | 22 | 33 | nan | nan | nan | Caatinga | 7.3 |
| e5a2ec0b-5256-36d0-b3ee-5219fd9eb099 | -11.43975 | -43.50019 | 2025-10-02 04:02:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 2280100f-9f2a-3053-93a3-a4a47360c102 | -6.50145 | -44.29229 | 2025-10-02 04:02:00 | NOAA-21 | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| c94d400f-c77b-33d9-9713-3b1c3c6514e6 | -10.2076 | -50.26793 | 2025-10-02 04:02:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 12.6 |
| c90f3c7e-81b9-37bf-b31e-4e582b3aa7aa | -11.07941 | -47.80084 | 2025-10-02 04:02:00 | NOAA-21 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 5.1 |
| d85f9322-d4dd-35d9-81a2-0824fd37e902 | -9.33817 | -45.70825 | 2025-10-02 04:02:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| e14c9b2c-6b4a-3a09-92ad-d8192b39aa65 | -10.23252 | -50.3117 | 2025-10-02 04:02:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| d3d2c2fd-f108-38b1-8c0b-fb9ff2033be3 | -9.77128 | -47.74491 | 2025-10-02 04:02:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 85e71982-2dc1-3c36-898d-d04f61f9fb0a | -11.17852 | -47.18902 | 2025-10-02 04:02:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 40a4f538-e8e6-3466-8539-21b5fec65434 | -11.81876 | -47.59652 | 2025-10-02 04:02:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| bc4f8b21-7aeb-35f4-aab5-0522d5a378f8 | -5.89439 | -43.24034 | 2025-10-02 04:02:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 67c3a946-9295-3907-a101-3dcb502bb20e | -6.96441 | -45.3185 | 2025-10-02 04:02:00 | NOAA-21 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 23f6c354-3dff-31ad-8e73-1d43dba4673b | -10.81794 | -47.96996 | 2025-10-02 04:02:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| be9391d3-f465-39dc-97a4-41a20436053c | -9.95175 | -43.57591 | 2025-10-02 04:02:00 | NOAA-21 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |


[Clique aqui para ver as próximas entradas](README28.md)
