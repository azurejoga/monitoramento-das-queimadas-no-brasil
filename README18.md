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
| 6e166531-aba6-3ff7-b9e1-18188a0d605c | -12.03633 | -63.77158 | 2025-07-20 05:31:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 3.7 |
| e3210a31-5d85-3439-82e6-fa54f4216be1 | -10.73405 | -52.52004 | 2025-07-20 05:31:00 | NOAA-21 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 4b38789c-29c4-33f1-a522-95480ba76140 | -10.05828 | -64.99437 | 2025-07-20 05:31:00 | NOAA-21 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| cbb89564-0b56-3764-9b37-f96b10579236 | -10.04547 | -64.90072 | 2025-07-20 05:31:00 | NOAA-21 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 37b3a1a4-01f2-3cb8-95cc-d034e122d58f | -12.58118 | -56.98061 | 2025-07-20 05:31:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 2a0c5fe4-db30-3ae2-b0bd-b68abf6149c1 | -10.50408 | -68.64402 | 2025-07-20 05:31:00 | NOAA-21 | XAPURI | ACRE | Brasil | 1200708 | 12 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ca7daa1c-b5fd-3eba-8370-eee463fa4d16 | -12.03267 | -63.77108 | 2025-07-20 05:31:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7674fa78-bc3e-385c-81e0-abc4b8d7532c | -12.03322 | -63.76757 | 2025-07-20 05:31:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f44ef199-3b62-322a-a60b-b2a9770742bb | -10.3812 | -62.76227 | 2025-07-20 05:31:00 | NOAA-21 | CACAULÂNDIA | RONDÔNIA | Brasil | 1100601 | 11 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 3a474899-b4c5-3a06-838a-d3776152aed6 | -14.15841 | -58.19614 | 2025-07-20 05:31:00 | NOAA-21 | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| ee5302fd-85a1-3230-9ecb-496cd7a8649a | -12.03577 | -63.77509 | 2025-07-20 05:31:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 3c77c6ee-b9ee-3eb5-bbfd-302c6ec9ba94 | -12.52353 | -57.24144 | 2025-07-20 05:31:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 6b610136-be11-3a79-ad7f-ed7db63216c1 | -12.35374 | -50.32153 | 2025-07-20 05:31:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 859fda80-174d-3126-bc41-226a482f78f3 | -12.02439 | -63.73734 | 2025-07-20 05:31:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 72f47e3a-cfe3-33b7-a790-ca4ce812fc2b | -10.67483 | -56.54565 | 2025-07-20 05:31:00 | NOAA-21 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8140a798-113d-33b9-933d-cd2888795d4e | -12.34686 | -50.32064 | 2025-07-20 05:31:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 2ab75318-34b1-3cd5-8a89-935dd427fc22 | -12.3675 | -50.32326 | 2025-07-20 05:31:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 1a68d6f6-5916-3d9c-8d1a-5101bd873625 | -10.38343 | -62.76979 | 2025-07-20 05:31:00 | NOAA-21 | CACAULÂNDIA | RONDÔNIA | Brasil | 1100601 | 11 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 87778c1b-ccad-36eb-84c6-41665551529f | -9.54437 | -62.80759 | 2025-07-20 05:31:00 | NOAA-21 | RIO CRESPO | RONDÔNIA | Brasil | 1100262 | 11 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 22ee4818-5caf-325d-8fb4-010ba8c9fd7d | -12.52411 | -57.23708 | 2025-07-20 05:31:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f02951b2-20c8-381f-94b7-37d6c83f0cc0 | -9.73527 | -63.13088 | 2025-07-20 05:31:00 | NOAA-21 | ALTO PARAÍSO | RONDÔNIA | Brasil | 1100403 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 886edef6-c20e-3439-b710-7f4279783327 | -10.87972 | -56.09529 | 2025-07-20 05:31:00 | NOAA-21 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| ce00a8a7-a322-3c67-a391-dc311907fbda | -10.29586 | -60.54346 | 2025-07-20 05:31:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| d1090199-6632-3f47-9d33-e919d9b62da8 | -12.02329 | -63.74436 | 2025-07-20 05:31:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 3d41fe98-e3b8-3ac9-8a62-0db5dcc00ba0 | -10.36269 | -57.49961 | 2025-07-20 05:31:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 63a1c789-be0a-31dc-90c1-844377e4b5e3 | -10.29938 | -60.54399 | 2025-07-20 05:31:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 0b7c058c-2a7b-329c-ae43-08a04094b813 | -10.38451 | -62.76279 | 2025-07-20 05:31:00 | NOAA-21 | CACAULÂNDIA | RONDÔNIA | Brasil | 1100601 | 11 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 2847b86d-336d-3978-94cd-c9d528b99574 | -14.15366 | -58.19959 | 2025-07-20 05:31:00 | NOAA-21 | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 3b82774e-3562-351b-9b75-4ffd3c055360 | -12.02274 | -63.74788 | 2025-07-20 05:31:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 32306659-5965-3fd9-ac88-788e9daee019 | -10.73457 | -52.51577 | 2025-07-20 05:31:00 | NOAA-21 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 36dc7a4f-566a-31af-af97-9ce60f71d44d | -10.05487 | -64.9938 | 2025-07-20 05:31:00 | NOAA-21 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 52aa7ffe-d3f7-3bc9-a8d3-126cc156ee04 | -10.81607 | -56.95782 | 2025-07-20 05:31:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| f24989c2-6c90-32a1-bef9-0f6a09a82907 | -10.64883 | -65.10188 | 2025-07-20 05:31:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 0.5 |
| fd206fc8-5add-3e69-8163-37033a41ea5f | -9.30979 | -64.44653 | 2025-07-20 05:31:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| b0f1a5a9-1f3c-3c6b-a571-3a000683d544 | -10.38066 | -62.76577 | 2025-07-20 05:31:00 | NOAA-21 | CACAULÂNDIA | RONDÔNIA | Brasil | 1100601 | 11 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 882593a8-0721-3dd7-8798-e2d2a89bbbb8 | -9.97884 | -67.57375 | 2025-07-20 05:31:00 | NOAA-21 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 10644aff-51e5-327f-b15f-81b278466532 | -10.81169 | -56.95718 | 2025-07-20 05:31:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 76c48804-5a2b-30a2-ab41-86e2d3abe1ea | -10.72816 | -52.51915 | 2025-07-20 05:31:00 | NOAA-21 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| a4a0b63b-ef10-3833-9aed-ae48fbdc2e5a | -12.03908 | -63.77562 | 2025-07-20 05:31:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 3.7 |
| de0c5d6e-d356-399e-93b0-03b6d30e35f2 | -10.38397 | -62.76629 | 2025-07-20 05:31:00 | NOAA-21 | CACAULÂNDIA | RONDÔNIA | Brasil | 1100601 | 11 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 6d648fc1-58c7-3e1d-94d7-29c398eda1f2 | -12.5794 | -56.9783 | 2025-07-20 05:31:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 863f2f1a-a319-3961-98b0-ab2e14616b6b | -12.03853 | -63.77914 | 2025-07-20 05:31:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 45b2130e-7ba0-3156-8ec7-710917c8d065 | -14.15314 | -58.20362 | 2025-07-20 05:31:00 | NOAA-21 | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 5949d3a0-a05f-33ef-b9f9-1522a14a6b80 | -12.5818 | -56.97601 | 2025-07-20 05:31:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8b8ff09b-4847-344d-97ca-69c02a8a57a8 | -23.33888 | -51.90212 | 2025-07-20 05:33:00 | NOAA-21 | MARINGÁ | PARANÁ | Brasil | 4115200 | 41 | 33 | nan | nan | nan | Mata Atlântica | 25.0 |
| 7982ba9d-3876-36a6-b24b-cd0b67d36fde | -23.33716 | -51.90266 | 2025-07-20 05:33:00 | NOAA-21 | MARINGÁ | PARANÁ | Brasil | 4115200 | 41 | 33 | nan | nan | nan | Mata Atlântica | 31.5 |
| ef038100-0474-3957-92d1-773fd075eb58 | -23.33844 | -51.90876 | 2025-07-20 05:33:00 | NOAA-21 | MARINGÁ | PARANÁ | Brasil | 4115200 | 41 | 33 | nan | nan | nan | Mata Atlântica | 19.0 |
| 79df746a-5e6d-362d-b423-bf8d62275eee | -3.11278 | -47.00566 | 2025-07-20 05:38:00 | AQUA_M-M | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 20.9 |
| 8f549611-be0c-3bf3-adba-5fb4ec6d8645 | -6.89886 | -45.39739 | 2025-07-20 05:38:00 | AQUA_M-M | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 38.2 |
| 5535224b-075f-3c31-86e3-a5c3bb1b829e | -4.07189 | -48.0336 | 2025-07-20 05:38:00 | AQUA_M-M | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 18.4 |
| 12f42574-865c-38f2-8ee2-16273ad1941c | -3.12349 | -47.00731 | 2025-07-20 05:38:00 | AQUA_M-M | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 7.4 |
| 71ecc6a7-b097-34fe-b42f-9915600c3942 | -3.13421 | -47.00887 | 2025-07-20 05:38:00 | AQUA_M-M | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 297937c4-890e-36f2-a01b-72d8b087ddd9 | -4.5823 | -43.31018 | 2025-07-20 05:38:00 | AQUA_M-M | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 9.0 |
| 5db6301f-55e2-3a4e-842e-f8f37ecda431 | -7.7052 | -47.29148 | 2025-07-20 05:38:00 | AQUA_M-M | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 18.7 |
| e59e72ae-c7e2-31dc-addb-5dd0321b8876 | -3.03788 | -47.85503 | 2025-07-20 05:38:00 | AQUA_M-M | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 23.3 |
| 20d0fdb2-e34d-3f35-b09c-32c624f4aea7 | -3.789 | -41.00242 | 2025-07-20 05:38:00 | AQUA_M-M | TIANGUÁ | CEARÁ | Brasil | 2313401 | 23 | 33 | nan | nan | nan | Caatinga | 6.0 |
| 8e48dc7c-d3e2-3a21-8621-89263f4a8c52 | -4.59109 | -43.31147 | 2025-07-20 05:38:00 | AQUA_M-M | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 13.3 |
| 709b80b5-f0ef-3094-9eae-aae377f1061a | -3.0354 | -47.87076 | 2025-07-20 05:38:00 | AQUA_M-M | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 14.4 |
| d7f6bd4d-4e29-36ea-a176-5f7cfa0eb23e | -2.91011 | -48.24072 | 2025-07-20 05:38:00 | AQUA_M-M | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 9.9 |
| c6943f66-e098-3624-99df-089de24e3c0d | -6.90946 | -45.3893 | 2025-07-20 05:38:00 | AQUA_M-M | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 8.5 |
| dbea7cf7-f6f2-35ce-b435-4711aec9e6a7 | -6.90327 | -45.36847 | 2025-07-20 05:38:00 | AQUA_M-M | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 79.8 |
| b7b23c59-e37a-3846-a212-63d44c2b85e2 | -7.69505 | -47.28997 | 2025-07-20 05:38:00 | AQUA_M-M | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 13.4 |
| 7c83a7f9-fcba-3af3-941f-0693409e1201 | -4.96399 | -43.23005 | 2025-07-20 05:38:00 | AQUA_M-M | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 5.3 |
| c22f7fb5-0a5e-30bd-8425-333d2474fef6 | -3.58815 | -47.51143 | 2025-07-20 05:38:00 | AQUA_M-M | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 9.4 |
| f622be5b-bb68-36f2-803e-4783bb9da294 | -4.66495 | -41.95113 | 2025-07-20 05:38:00 | AQUA_M-M | COCAL DE TELHA | PIAUÍ | Brasil | 2202711 | 22 | 33 | nan | nan | nan | Caatinga | 9.2 |
| 37b14053-1b85-3a5a-afe5-f1f1bdab986f | -3.02775 | -47.86255 | 2025-07-20 05:38:00 | AQUA_M-M | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 12.1 |
| 6bd37183-d213-3b64-8dbb-4aa4f4b979b2 | -8.36043 | -46.64492 | 2025-07-20 05:38:00 | AQUA_M-M | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 6.7 |
| adeb3d71-eb36-3f17-b7e8-a850ebee5e71 | -6.90801 | -45.39883 | 2025-07-20 05:38:00 | AQUA_M-M | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 28.7 |
| 3f5d5292-48a2-3f84-88ef-783854866130 | -3.10207 | -47.00401 | 2025-07-20 05:38:00 | AQUA_M-M | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 28426e50-affb-329d-8a93-55ffaf7e4e3f | -6.90655 | -45.40846 | 2025-07-20 05:38:00 | AQUA_M-M | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 20.0 |
| b4bcf6ec-2f28-3480-bdc6-3d6bbca1f260 | -3.58593 | -47.52578 | 2025-07-20 05:38:00 | AQUA_M-M | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 8.4 |
| d89c809f-ec73-361d-af3d-f78a5357179e | -2.89822 | -48.23903 | 2025-07-20 05:38:00 | AQUA_M-M | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 10.5 |
| 83858306-2a3f-363c-b4df-e9c54fb71f2a | -6.9018 | -45.37807 | 2025-07-20 05:38:00 | AQUA_M-M | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 181.9 |
| e762a1d8-7727-35c1-91ab-f1dcfe6e3a21 | -6.90035 | -45.38762 | 2025-07-20 05:38:00 | AQUA_M-M | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 173.3 |
| 29c4231a-40d2-3409-bbc3-4045773d0298 | -6.896 | -45.38 | 2025-07-20 05:40:00 | GOES-19 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 56.6 |
| bc0e3684-b26c-3484-a1ad-03997f1aceb1 | -6.9148 | -45.3784 | 2025-07-20 05:40:00 | GOES-19 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 46.3 |
| 7c81fac7-beed-3f90-a4bf-8f8816c931be | -10.66699 | -46.79045 | 2025-07-20 05:40:00 | AQUA_M-M | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 14.4 |
| 1ae941a4-f9bc-30da-bc84-4e7b7306bccf | -10.69437 | -46.77951 | 2025-07-20 05:40:00 | AQUA_M-M | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 11.5 |
| 894ca377-a0cb-3190-9a1b-b015067aed42 | -10.65598 | -46.79924 | 2025-07-20 05:40:00 | AQUA_M-M | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 8.9 |
| bbccb31e-d012-3406-b87f-a5e71fd936f6 | -10.65757 | -46.78901 | 2025-07-20 05:40:00 | AQUA_M-M | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 11.0 |
| b4af49bb-309b-3f9e-9d1b-343206c8640a | -10.96494 | -45.1034 | 2025-07-20 05:40:00 | AQUA_M-M | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 38.3 |
| e3ab9e5f-9e6f-358b-8e11-8c5847a2de99 | -10.68497 | -46.77797 | 2025-07-20 05:40:00 | AQUA_M-M | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 33.8 |
| b5e6ecce-2535-3e6b-adef-17997eeee868 | -10.68334 | -46.78818 | 2025-07-20 05:40:00 | AQUA_M-M | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 36.7 |
| d19ce95c-4cf3-3f86-a9a5-387dfe9345b5 | -10.67393 | -46.78672 | 2025-07-20 05:40:00 | AQUA_M-M | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 31.6 |
| 29993eba-4cc9-39f9-8503-ed8b2cc5e3cb | -10.97377 | -45.10474 | 2025-07-20 05:40:00 | AQUA_M-M | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 17.9 |
| 2eeb9502-e799-3b3a-9297-594a30e2367d | -23.33006 | -46.95755 | 2025-07-20 05:42:00 | AQUA_M-M | PIRAPORA DO BOM JESUS | SÃO PAULO | Brasil | 3539103 | 35 | 33 | nan | nan | nan | Mata Atlântica | 15.1 |
| 6887e176-0c16-3521-b0e8-badbc3d8ac6f | -23.32865 | -46.96709 | 2025-07-20 05:42:00 | AQUA_M-M | PIRAPORA DO BOM JESUS | SÃO PAULO | Brasil | 3539103 | 35 | 33 | nan | nan | nan | Mata Atlântica | 18.6 |
| ee0be37b-0bc0-3d4c-a142-713d1b96dbd1 | -23.33828 | -51.90341 | 2025-07-20 05:42:00 | AQUA_M-M | MARINGÁ | PARANÁ | Brasil | 4115200 | 41 | 33 | nan | nan | nan | Mata Atlântica | 43.7 |
| dd1c6818-8096-3315-a5c4-dce33fc9fa89 | -23.33412 | -51.89697 | 2025-07-20 05:42:00 | AQUA_M-M | MARINGÁ | PARANÁ | Brasil | 4115200 | 41 | 33 | nan | nan | nan | Mata Atlântica | 45.5 |
| e2eaad55-5cfe-36b9-bbbb-3e706c7ec736 | -10.688 | -46.7829 | 2025-07-20 05:50:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 53.4 |
| 2bb6d402-691e-3316-a682-9eac37f6f3cc | -10.6689 | -46.7853 | 2025-07-20 05:50:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 50.7 |
| 2a483f57-e0ca-3546-85a1-5a465d57ca4c | -7.26196 | -60.12004 | 2025-07-20 05:55:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 06bccd26-3b27-3a26-96e0-cb6a38a328ff | -7.25682 | -60.11932 | 2025-07-20 05:55:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f7c380bc-c1ee-3986-8a62-7f7795008c13 | -7.26073 | -60.12872 | 2025-07-20 05:55:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c0607c3d-813b-3a08-a9f9-19833a4b2007 | -7.26154 | -60.12297 | 2025-07-20 05:55:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| aa8e9807-1ff3-38cf-9e78-0e9360214b1a | -7.26114 | -60.12584 | 2025-07-20 05:55:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 595cc87e-e425-3009-96e6-70805427ed3b | -7.26799 | -60.11451 | 2025-07-20 05:55:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6acc82fa-bd41-3cb3-9f46-3101f8e4fd6a | -7.26754 | -60.11761 | 2025-07-20 05:55:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| eb310878-229d-30b8-9fe3-1fb02b0edb88 | -7.25641 | -60.12225 | 2025-07-20 05:55:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 56866a7b-ca7f-38e7-99a0-850120fa2df9 | -7.26949 | -60.1147 | 2025-07-20 05:55:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |


[Clique aqui para ver as próximas entradas](README19.md)
