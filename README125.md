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

## Dados Diários - Página 125

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 19f0a5f7-cfe7-32d2-b4c6-86538379efa1 | -12.81115 | -54.02489 | 2024-09-26 04:59:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a82d0069-6828-3885-83d0-d44c5ecad3d9 | -12.8106 | -54.02859 | 2024-09-26 04:59:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0f1b747c-65e5-344e-9319-09dd54a67e7c | -12.81038 | -54.02083 | 2024-09-26 04:59:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| c4cb8ce8-5be3-39fe-9624-6936b056c2e4 | -12.81005 | -54.03228 | 2024-09-26 04:59:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a0bb6867-0904-3671-a2b7-70e59614b097 | -12.80982 | -54.02452 | 2024-09-26 04:59:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8c29d99f-e1bd-304e-a130-3ca76e026244 | -12.80926 | -54.02821 | 2024-09-26 04:59:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9d969915-5a2d-3144-a325-bd225946e523 | -12.80895 | -54.03966 | 2024-09-26 04:59:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3e356438-0575-3fa8-b12d-32e8ae9b9027 | -12.8087 | -54.0319 | 2024-09-26 04:59:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d6d55b5a-6a64-3c22-9205-d9cd233fed99 | -12.8084 | -54.04336 | 2024-09-26 04:59:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d63d7509-50fc-3b75-8a1e-95d730a5b9c7 | -12.80814 | -54.03559 | 2024-09-26 04:59:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 88ff3f78-ca70-38c2-9d6e-8bdaa4442c91 | -12.80758 | -54.03928 | 2024-09-26 04:59:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ee6e6daf-dc52-3cd1-9833-10b22617cbcc | -12.80737 | -54.07338 | 2024-09-26 04:59:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 79763e42-75a6-307d-8b6c-2dc2617b6c4e | -12.8073 | -54.05074 | 2024-09-26 04:59:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 6b00ccf7-1e2c-35ef-bc98-8f6b604b09e7 | -12.80702 | -54.04296 | 2024-09-26 04:59:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d73b6969-5cb4-3ad7-aa0b-b3fe02f38480 | -12.80675 | -54.05442 | 2024-09-26 04:59:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 01146f4a-c2af-3364-80ba-4bfa4201e3b4 | -12.80645 | -54.04665 | 2024-09-26 04:59:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 585171ad-11d6-3fbf-929d-c2fcddcc29b5 | -12.80645 | -54.02399 | 2024-09-26 04:59:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4b69d778-60db-3a85-8886-d734d1bd7d06 | -12.80589 | -54.05034 | 2024-09-26 04:59:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b5aa6485-349d-33b1-9709-860d2d2163e8 | -12.80588 | -54.02768 | 2024-09-26 04:59:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| fc19ba8a-8b5e-3c17-a56a-cc024bf55980 | -12.80533 | -54.05402 | 2024-09-26 04:59:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 8135a058-f37a-3bc5-b458-900daa4ba3f0 | -12.80532 | -54.03137 | 2024-09-26 04:59:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b5837bd3-3a26-3ab2-8765-40389502e11f | -12.80477 | -54.0577 | 2024-09-26 04:59:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b0b7976b-cea1-33e8-867d-866711587816 | -12.80476 | -54.03506 | 2024-09-26 04:59:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ec220888-ae7e-3601-b6ab-11dbc435406b | -12.8042 | -54.03874 | 2024-09-26 04:59:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e7a8e960-d214-301e-9e37-2fd26a8e74e2 | -12.804 | -54.07285 | 2024-09-26 04:59:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 65da42b2-a90b-32d0-b1b7-e6f06bc0978c | -12.80364 | -54.04243 | 2024-09-26 04:59:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a9059e63-5a3d-3673-ae74-7fbd6d9a4c0a | -12.80363 | -54.01976 | 2024-09-26 04:59:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 1bb78786-c41e-34e3-ad06-6e3f14d03171 | -12.80308 | -54.04612 | 2024-09-26 04:59:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b7e37d9e-a0c1-36c2-a33c-ee9f7932dd72 | -12.80307 | -54.02346 | 2024-09-26 04:59:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 1cb20ab1-0d88-32dc-bf1c-6f80e95ddbfb | -12.80253 | -54.07242 | 2024-09-26 04:59:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 066e5801-f462-3f37-bd6a-b92f4a082aeb | -12.80252 | -54.0498 | 2024-09-26 04:59:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e48875cd-d187-3b80-8cdf-83b0a1616b9b | -12.80251 | -54.02715 | 2024-09-26 04:59:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| f871d543-24d0-32cb-9b84-b9f4a7b8588b | -12.80196 | -54.05349 | 2024-09-26 04:59:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6a6b975f-2814-3b43-b9b0-473fceff7a6e | -12.80195 | -54.03084 | 2024-09-26 04:59:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| aca38fd1-a3ab-30e4-b9ba-027b26d4ddb0 | -12.80139 | -54.03452 | 2024-09-26 04:59:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 97586713-fb53-37dd-9b2e-697907191bc0 | -12.80085 | -54.08346 | 2024-09-26 04:59:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3b73fa87-9aa9-3a00-83bd-026afccf6d22 | -12.80083 | -54.03821 | 2024-09-26 04:59:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| cf3e47ba-924e-3cc5-a6bf-0b72fc422479 | -12.80026 | -54.04189 | 2024-09-26 04:59:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 7b9a48f8-c1b4-339c-bc51-c55b33c255e1 | -12.79972 | -54.06822 | 2024-09-26 04:59:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c95cc350-4ec1-354f-990c-ba68fcf90950 | -12.79971 | -54.04557 | 2024-09-26 04:59:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 5dcda76d-1f21-3551-abbc-755bbac5bda9 | -12.79969 | -54.02293 | 2024-09-26 04:59:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 817b3349-fa49-365d-86b6-046e6debd7ba | -12.79916 | -54.0719 | 2024-09-26 04:59:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 114fc75d-3639-316e-9c4a-1b48b9031318 | -12.79914 | -54.04926 | 2024-09-26 04:59:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 6aab777b-c139-3ae8-813a-6518a6d2966f | -12.79913 | -54.02662 | 2024-09-26 04:59:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 6ee9001b-6467-3cbf-92b7-91bf7ab8aafe | -12.79859 | -54.07558 | 2024-09-26 04:59:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 4.3 |
| b73f2bec-0d39-3829-a861-7e05bb3fdfb2 | -12.79858 | -54.05295 | 2024-09-26 04:59:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| af3e5aa6-0a65-33ef-9049-e140b144e1f3 | -12.79857 | -54.03031 | 2024-09-26 04:59:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| a8a089f9-3041-3251-a316-227fec6805f4 | -12.79801 | -54.03399 | 2024-09-26 04:59:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 5bbb2396-b9f4-37fd-9b1e-b6d8c5ec4cf4 | -12.79747 | -54.08294 | 2024-09-26 04:59:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8df829f9-20a3-3ae1-9240-573132364a90 | -12.79745 | -54.03767 | 2024-09-26 04:59:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 39966636-4528-3369-996a-e255b7063515 | -12.79689 | -54.04136 | 2024-09-26 04:59:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 725045b8-2a85-3dcc-b777-a5cb9953fc6a | -12.79633 | -54.04504 | 2024-09-26 04:59:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 377117d7-c64e-3da8-802a-6fed715bcf18 | -12.79577 | -54.04873 | 2024-09-26 04:59:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| cd63d2a0-3e6d-3c50-b957-decf9cf4abf9 | -12.79521 | -54.05241 | 2024-09-26 04:59:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ff36a6de-f214-3543-8b3b-ac0adc0a2c29 | -12.79463 | -54.03346 | 2024-09-26 04:59:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| cb7857ce-d7be-3acd-92ec-728321d1c1fa | -12.79407 | -54.03714 | 2024-09-26 04:59:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 7722f158-a925-3686-800c-e21ff1b727f8 | -12.79351 | -54.04082 | 2024-09-26 04:59:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| cbc3299d-d379-3a9c-a636-cd1bb4a6db22 | -12.79296 | -54.0445 | 2024-09-26 04:59:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| a8de54f6-b7a9-3758-8a9c-a70c37dd35f6 | -12.7924 | -54.04818 | 2024-09-26 04:59:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 5ed058b9-8db0-37a7-beda-64ea7323a481 | -12.7907 | -54.03661 | 2024-09-26 04:59:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| aec41bac-b417-31b6-830b-4f7bad0282ee | -12.79014 | -54.04029 | 2024-09-26 04:59:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| a30bb027-27fe-3e2d-aa3e-cd4cbb1fa2a4 | -12.78958 | -54.04396 | 2024-09-26 04:59:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 629b393b-42d6-38ab-b6f9-9fe714f41d18 | -12.78732 | -54.03608 | 2024-09-26 04:59:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 1c2a1276-8099-34bc-9f7c-a26bc6a178fe | -12.78676 | -54.03976 | 2024-09-26 04:59:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2056eb9f-a954-3753-9f0f-9662d41fe42b | -12.7862 | -54.04343 | 2024-09-26 04:59:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 104cacca-467d-3487-9461-1590198b1881 | -12.65508 | -53.21036 | 2024-09-26 04:59:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 5551db70-a276-39f7-8016-5b87b5288d0c | -12.65161 | -53.20984 | 2024-09-26 04:59:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 7bc6f45b-82d1-3ca5-b089-b2d98497773c | -12.64756 | -53.2132 | 2024-09-26 04:59:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 19893a35-8783-31ff-b4ec-c3a084bacc22 | -12.63657 | -53.21553 | 2024-09-26 04:59:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 58891420-bc60-3499-b2ed-1a78572c39aa | -12.6302 | -53.21058 | 2024-09-26 04:59:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ba77597e-21f4-35c4-9c9f-243a5edce27a | -12.6273 | -53.20614 | 2024-09-26 04:59:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a1433138-8fd6-3d30-8cae-dd8d4f01b869 | -12.62383 | -53.2056 | 2024-09-26 04:59:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| bd7315d6-fead-3447-8d64-b536960a9f5a | -12.62036 | -53.20506 | 2024-09-26 04:59:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 167fd8a3-aad2-3389-8c5e-6ea0f80e1f58 | -12.61415 | -53.27182 | 2024-09-26 04:59:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8985d9a6-b873-33e2-9118-de2814f163d2 | -12.61012 | -53.2752 | 2024-09-26 04:59:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| dbca869d-bd52-36bf-9f24-3a0a57e630c9 | -12.60948 | -53.19197 | 2024-09-26 04:59:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f5d94e6f-6dc5-3a36-9d26-a69f9dab801b | -12.60762 | -53.1951 | 2024-09-26 04:59:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 353589c2-794f-3bee-97b5-a4ce4cb3e521 | -12.6043 | -53.17917 | 2024-09-26 04:59:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 275d8880-daff-3f0b-ae46-2ebfde344adc | -12.60312 | -53.187 | 2024-09-26 04:59:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 28b7f05c-1242-33ee-bebd-7e72c66a1484 | -12.60258 | -53.16689 | 2024-09-26 04:59:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 3f222a1a-bcc4-395a-aff2-4bdb07cab596 | -12.60199 | -53.1708 | 2024-09-26 04:59:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 672210a0-d660-3a4c-812d-0f6c1fe35630 | -12.60141 | -53.17471 | 2024-09-26 04:59:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| b0c8cdd5-b92b-3d4c-bf2c-7885623fda24 | -12.60082 | -53.17863 | 2024-09-26 04:59:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| a6b5c056-e967-36d7-a68d-d700d046ea6f | -12.5991 | -53.16635 | 2024-09-26 04:59:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 845cb0f9-6edd-3fe8-a609-e2d49b7ce3bb | -12.59852 | -53.17026 | 2024-09-26 04:59:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 90a66640-cf44-3f62-add7-32e62f08962e | -12.59794 | -53.17417 | 2024-09-26 04:59:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 22c1d4c8-5b29-3960-b4c4-5e82082e9d0a | -12.59563 | -53.16581 | 2024-09-26 04:59:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 49b4b9e1-4306-3d85-9468-04d53a596d46 | -12.59215 | -53.16528 | 2024-09-26 04:59:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| c76a65df-765c-37aa-802f-90f21e70e52a | -12.58868 | -53.16475 | 2024-09-26 04:59:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| c0ac67b1-cc70-3736-bd64-eb28f8abd38c | -12.5881 | -53.16865 | 2024-09-26 04:59:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| f5c6711e-97be-3620-be4f-8b505c399ec7 | -12.58521 | -53.16422 | 2024-09-26 04:59:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| e08c6d5c-3904-35ca-a073-c87cd9e9b07c | -12.58462 | -53.16812 | 2024-09-26 04:59:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 39dc2322-aa7c-3771-a5b6-4e3d30b75f8c | -12.58173 | -53.16368 | 2024-09-26 04:59:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 69b5c7ed-905e-385a-919c-74e4131b9a54 | -12.58115 | -53.16759 | 2024-09-26 04:59:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 1d28bc8b-e250-3433-9e70-696a2410923c | -12.57826 | -53.16315 | 2024-09-26 04:59:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 069aadda-0971-3ad9-8025-f17f5ef942c6 | -12.57767 | -53.16706 | 2024-09-26 04:59:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 7523e0d0-63e6-3220-8aed-f24d0dc3be41 | -12.5742 | -53.16652 | 2024-09-26 04:59:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 670104ae-308c-3b46-9e66-03593f91072b | -12.57073 | -53.16599 | 2024-09-26 04:59:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| b3670921-c7dc-3246-b297-d61c13b40e4e | -12.56667 | -53.16937 | 2024-09-26 04:59:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 2d6318a1-afb3-3bc6-adab-c6b1bac191cc | -12.5632 | -53.16883 | 2024-09-26 04:59:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |


[Clique aqui para ver as próximas entradas](README126.md)
