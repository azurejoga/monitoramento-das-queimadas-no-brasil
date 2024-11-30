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

## Dados Diários - Página 20

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| a1b9ceed-2da7-37ba-baaa-9064d9bf4f2a | -1.68342 | -46.77851 | 2024-11-30 03:46:00 | NOAA-20 | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 5ccd4b38-b6ea-3678-8c3f-665a1798f6e9 | -3.59757 | -49.99227 | 2024-11-30 03:46:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 12.0 |
| 1316b755-fd1e-3f9b-9ce0-c441f3f42cf8 | -6.0601 | -44.43931 | 2024-11-30 03:46:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| fb0c0529-c623-397f-ba14-871c19ea2130 | -6.938 | -39.64742 | 2024-11-30 03:46:00 | NOAA-20 | ASSARÉ | CEARÁ | Brasil | 2301604 | 23 | 33 | nan | nan | nan | Caatinga | 1.5 |
| c4e8d189-4067-3e15-b86e-cd460716e18d | -3.01601 | -45.10139 | 2024-11-30 03:46:00 | NOAA-20 | MATINHA | MARANHÃO | Brasil | 2106508 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 48e7f8a6-39ef-3b40-a062-659f9fedb8ed | -3.98995 | -41.51974 | 2024-11-30 03:46:00 | NOAA-20 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 1198f39b-6b9f-33ad-a720-23d6f2ebd936 | -2.27244 | -46.4367 | 2024-11-30 03:46:00 | NOAA-20 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4002c802-2977-3541-abab-2b59e56cedaf | -3.99599 | -43.25583 | 2024-11-30 03:46:00 | NOAA-20 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 5675df8a-5b1a-3013-b157-8e7e74c02714 | -4.8763 | -41.3036 | 2024-11-30 03:46:00 | NOAA-20 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 3.2 |
| bbbb8a69-641c-356c-b2e4-6e8109efd0de | -3.79349 | -45.85595 | 2024-11-30 03:46:00 | NOAA-20 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 7734c46c-d369-3ce7-9a34-ce37543e7036 | -5.72552 | -43.77545 | 2024-11-30 03:46:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 05aabcde-4580-3ff2-8c1a-c0cf644e04c2 | -4.10678 | -46.11429 | 2024-11-30 03:46:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| fff5ea8d-d32e-35aa-a765-f3708f19959d | -6.90448 | -43.56084 | 2024-11-30 03:46:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 4.2 |
| b3908a02-4a03-37dd-873e-253d17ff8ddc | -4.85253 | -41.27316 | 2024-11-30 03:46:00 | NOAA-20 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 9d57b37e-6146-30f2-8fa7-cadc6a9e35a1 | -6.03436 | -39.36452 | 2024-11-30 03:46:00 | NOAA-20 | ACOPIARA | CEARÁ | Brasil | 2300309 | 23 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 1b3f3b56-3394-393a-9c6c-ceffcb91696a | -4.87006 | -41.2915 | 2024-11-30 03:46:00 | NOAA-20 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 1ddaf4ad-01d6-3ce8-ae5e-e816f5d278de | -2.37861 | -47.88712 | 2024-11-30 03:46:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 5a9b6353-3ed3-3ec8-a576-c9eb9c227de8 | -5.74199 | -46.18198 | 2024-11-30 03:46:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| afd5b365-eefe-3db9-a8ef-acfe38ca2b10 | -4.69601 | -42.39022 | 2024-11-30 03:46:00 | NOAA-20 | JOSÉ DE FREITAS | PIAUÍ | Brasil | 2205508 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 25e78145-4d1d-3b83-86fa-2502c57d4773 | -4.03842 | -41.91218 | 2024-11-30 03:46:00 | NOAA-20 | BRASILEIRA | PIAUÍ | Brasil | 2201960 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| 464a3a62-107a-3b0b-81ef-addb5e4bf6f9 | -2.70911 | -46.12843 | 2024-11-30 03:46:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 925250c2-9835-3f7e-8dee-56ba4e6466d8 | -11.77123 | -44.63299 | 2024-11-30 03:46:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 745c9174-4730-3e64-a3ca-fcc465260057 | -3.01066 | -45.10051 | 2024-11-30 03:46:00 | NOAA-20 | MATINHA | MARANHÃO | Brasil | 2106508 | 21 | 33 | nan | nan | nan | Amazônia | 25.0 |
| 28566bea-fdcc-387a-85e7-055efb3b8867 | -4.65439 | -43.92715 | 2024-11-30 03:46:00 | NOAA-20 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| de6a242d-a148-3a06-bdc0-2a264b4d3d97 | -2.31937 | -44.82861 | 2024-11-30 03:46:00 | NOAA-20 | BEQUIMÃO | MARANHÃO | Brasil | 2101905 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 441c981c-d463-3d82-95ed-8e5ea5347680 | -6.92918 | -45.20725 | 2024-11-30 03:46:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c94d1cc0-6b9e-3d11-8a00-708b47b31250 | -2.99506 | -45.5241 | 2024-11-30 03:46:00 | NOAA-20 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2e3e0a07-c85a-3474-8d7b-b6f5f79cbf03 | -3.99613 | -46.94936 | 2024-11-30 03:46:00 | NOAA-20 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 01355864-817e-3ac1-b581-6b32af75baff | -2.77184 | -45.9245 | 2024-11-30 03:46:00 | NOAA-20 | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a211d5b4-b0a8-34f7-b87f-5712e1ff42c2 | -3.01008 | -45.1039 | 2024-11-30 03:46:00 | NOAA-20 | MATINHA | MARANHÃO | Brasil | 2106508 | 21 | 33 | nan | nan | nan | Amazônia | 15.2 |
| 7c474582-0d4b-3375-924a-89781b7331ec | -4.85475 | -41.30924 | 2024-11-30 03:46:00 | NOAA-20 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| bc51f649-db33-3239-87b1-cf045bca8b75 | -2.51397 | -48.46949 | 2024-11-30 03:46:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 1e6a1aac-8874-31bd-84fd-f7accce0d97b | -4.11038 | -39.99085 | 2024-11-30 03:46:00 | NOAA-20 | SANTA QUITÉRIA | CEARÁ | Brasil | 2312205 | 23 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 312921f1-c630-3a3e-84d2-8caa50c85096 | -5.53748 | -39.16653 | 2024-11-30 03:46:00 | NOAA-20 | MILHÃ | CEARÁ | Brasil | 2308351 | 23 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 6a3b508d-4d48-3088-92ae-c77417d6a8ad | -4.87517 | -41.28551 | 2024-11-30 03:46:00 | NOAA-20 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 12.0 |
| 57af5389-01e3-3f46-a03d-5bac84e42cfe | -4.08697 | -47.02645 | 2024-11-30 03:46:00 | NOAA-20 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 79f7f10d-2055-3d49-8552-43a296241f46 | -4.44305 | -48.56715 | 2024-11-30 03:46:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 8.4 |
| 98762c3b-b7bc-3470-bf24-a36cd2c91421 | -8.31555 | -44.95055 | 2024-11-30 03:46:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 3975712e-2398-36e0-9bb2-39518603f6c3 | -3.69722 | -45.69008 | 2024-11-30 03:46:00 | NOAA-20 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 77493d76-938c-3f8a-8dcb-92f4f1346c1c | -1.92229 | -47.90896 | 2024-11-30 03:46:00 | NOAA-20 | CONCÓRDIA DO PARÁ | PARÁ | Brasil | 1502756 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a41aa0eb-e7e7-398c-82d1-8b209f57051a | -3.01203 | -45.10774 | 2024-11-30 03:46:00 | NOAA-20 | MATINHA | MARANHÃO | Brasil | 2106508 | 21 | 33 | nan | nan | nan | Amazônia | 20.0 |
| 69607b49-ee0f-32c9-bb94-2104a73e67cf | -2.94619 | -47.99979 | 2024-11-30 03:46:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d7ce5322-d958-3d8c-9ce4-3e5b7674df1c | -4.60899 | -47.00578 | 2024-11-30 03:46:00 | NOAA-20 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 3.2 |
| fd33902d-b07c-3088-adda-ba4199894e3d | -3.00058 | -45.52499 | 2024-11-30 03:46:00 | NOAA-20 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| feab2870-322c-3d09-905e-89297ec1ba77 | -6.91135 | -43.54782 | 2024-11-30 03:46:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 75.2 |
| fbd6b5af-3c41-3e6a-872c-cdfd2bc70f00 | -14.33585 | -43.52394 | 2024-11-30 03:46:00 | NOAA-20 | IUIU | BAHIA | Brasil | 2917334 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 7c9b391a-3491-3a05-9b84-0c45da4e5c1e | -7.88279 | -37.3462 | 2024-11-30 03:46:00 | NOAA-20 | IGUARACY | PERNAMBUCO | Brasil | 2606903 | 26 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 36618f24-6144-3dfc-b6d0-ca82c01cfcd0 | -6.83067 | -35.32026 | 2024-11-30 03:46:00 | NOAA-20 | ARAÇAGI | PARAÍBA | Brasil | 2500809 | 25 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 2fd5a6a4-d65a-3f35-8831-a9904ef0896d | -2.35135 | -49.01609 | 2024-11-30 03:46:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 9.6 |
| facae6a3-ce56-3332-aa5b-fe0bb836e61c | -3.12714 | -46.05345 | 2024-11-30 03:46:00 | NOAA-20 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 11d3be78-1257-330b-9cc9-35e45e875ec0 | -3.62476 | -42.73981 | 2024-11-30 03:46:00 | NOAA-20 | BREJO | MARANHÃO | Brasil | 2102101 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 39a5b29d-173c-39d3-b090-32964f8eb00b | -2.27312 | -46.4325 | 2024-11-30 03:46:00 | NOAA-20 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 833f361b-47ea-356a-a11f-4a2725d1ee01 | -2.3795 | -47.88184 | 2024-11-30 03:46:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| bb4b7cb6-26ca-3ff5-bcb2-dc12fcee36d1 | -3.97571 | -41.52903 | 2024-11-30 03:46:00 | NOAA-20 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 3.7 |
| 151554c5-4c27-3ebc-9327-23cf283de0da | -3.26283 | -45.37547 | 2024-11-30 03:46:00 | NOAA-20 | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 7b45fceb-81ac-355a-afa6-c03b2819c6bb | -1.68191 | -46.78799 | 2024-11-30 03:46:00 | NOAA-20 | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 74658223-5a75-3bd6-9ca0-d4dd4926c9e7 | -4.67489 | -40.69343 | 2024-11-30 03:46:00 | NOAA-20 | IPUEIRAS | CEARÁ | Brasil | 2305902 | 23 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 3ead9bf3-ead4-3c49-b8f8-d766ede933e2 | -5.03882 | -45.24724 | 2024-11-30 03:46:00 | NOAA-20 | SÃO RAIMUNDO DO DOCA BEZERRA | MARANHÃO | Brasil | 2111631 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 9cdfd4b7-4bc7-3022-a9b0-02aaacc18212 | -3.9722 | -41.52462 | 2024-11-30 03:46:00 | NOAA-20 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 4.0 |
| dead5e07-352a-3abb-ae03-b4912bdb6d6e | -14.10693 | -44.08421 | 2024-11-30 03:46:00 | NOAA-20 | FEIRA DA MATA | BAHIA | Brasil | 2910776 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 9685da07-ef93-3015-bb5a-bcec0e861aa0 | -4.67207 | -46.37531 | 2024-11-30 03:46:00 | NOAA-20 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 7ca471d2-ad55-3715-9073-c1b11bb099cc | -6.7009 | -47.26646 | 2024-11-30 03:46:00 | NOAA-20 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 92b5e9e3-6cdc-39aa-a47e-454196f8d65c | -4.61169 | -47.00373 | 2024-11-30 03:46:00 | NOAA-20 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 01c4d278-5810-32ca-aa52-f371871063c8 | -2.51497 | -48.46355 | 2024-11-30 03:46:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| bc723f94-08cb-3388-a689-2073b0d07896 | -6.94531 | -42.83833 | 2024-11-30 03:46:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 2fa58334-ed43-3c19-b906-3df7a223f3e9 | -2.40175 | -48.23283 | 2024-11-30 03:46:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 02ae3966-4260-3af1-a604-30e3c89e425a | -3.98352 | -41.50724 | 2024-11-30 03:46:00 | NOAA-20 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 4.2 |
| e0d1b61b-e163-328a-858f-2ae40bc15450 | -3.55594 | -41.8173 | 2024-11-30 03:46:00 | NOAA-20 | CARAÚBAS DO PIAUÍ | PIAUÍ | Brasil | 2202539 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| fb5c1509-79a3-3270-9480-18240e8f3c96 | -7.36583 | -41.73759 | 2024-11-30 03:46:00 | NOAA-20 | SANTA CRUZ DO PIAUÍ | PIAUÍ | Brasil | 2209104 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| c66d5f1f-d7d8-326a-bc09-6e523350689e | -6.06954 | -48.04336 | 2024-11-30 03:46:00 | NOAA-20 | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 7.9 |
| d17ead07-48f9-3186-bcd2-0c0f26dbe70b | -6.90684 | -43.54706 | 2024-11-30 03:46:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 75.2 |
| 5fdfee8a-fa84-3fbd-86b2-4e7c6b7500f3 | -5.89126 | -39.06374 | 2024-11-30 03:46:00 | NOAA-20 | SOLONÓPOLE | CEARÁ | Brasil | 2313005 | 23 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 9151111a-a878-3aa4-9508-cd8fe6ed6b7e | -2.65751 | -48.79707 | 2024-11-30 03:46:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| c5d4d552-2562-3ab9-a369-8dbef3acb6a6 | -3.96868 | -41.52021 | 2024-11-30 03:46:00 | NOAA-20 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 4.6 |
| 1bffa506-4dd1-3470-84fb-be1a8f5c8d5c | -3.67109 | -47.12927 | 2024-11-30 03:46:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 19.7 |
| 5647ad0c-a83c-38bc-bfd0-beaaf7fa0256 | -4.87121 | -41.28455 | 2024-11-30 03:46:00 | NOAA-20 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 97a0b426-d86f-369e-8622-b58c308f16f0 | -4.0739 | -50.03352 | 2024-11-30 03:46:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| c4424907-5e1f-3ce4-9268-bdf67a22c1eb | -1.82946 | -46.30374 | 2024-11-30 03:46:00 | NOAA-20 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 33d604b0-d89f-36b5-9f85-464180001d0a | -5.46628 | -43.26836 | 2024-11-30 03:46:00 | NOAA-20 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| e6771d11-3578-3d6f-a5c5-d9c73376c02f | -4.15459 | -44.26781 | 2024-11-30 03:46:00 | NOAA-20 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 4d516f90-e806-3032-9956-8c9938174b99 | -15.44502 | -43.64948 | 2024-11-30 03:46:00 | NOAA-20 | VERDELÂNDIA | MINAS GERAIS | Brasil | 3171030 | 31 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 4e487584-c97c-331d-ad8c-490bdb629a6b | -4.70102 | -42.38683 | 2024-11-30 03:46:00 | NOAA-20 | JOSÉ DE FREITAS | PIAUÍ | Brasil | 2205508 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| b3df02d7-78ad-3db3-a7d2-f0bb71c7deb1 | -2.85198 | -46.69096 | 2024-11-30 03:46:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 7750e688-acc1-3340-a1be-e6443215e3f3 | -2.2672 | -46.43154 | 2024-11-30 03:46:00 | NOAA-20 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 39ce99d7-43ae-36ff-ade5-dbccce5c2645 | -1.68041 | -45.79068 | 2024-11-30 03:46:00 | NOAA-20 | CÂNDIDO MENDES | MARANHÃO | Brasil | 2102606 | 21 | 33 | nan | nan | nan | Amazônia | 5.6 |
| b29c7bff-54d5-3777-aa29-b5d091810b5d | -6.41156 | -39.73776 | 2024-11-30 03:46:00 | NOAA-20 | JUCÁS | CEARÁ | Brasil | 2307403 | 23 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 23cb896a-7e94-30a4-9177-fc46e57dab77 | -5.0726 | -44.99498 | 2024-11-30 03:46:00 | NOAA-20 | SÃO ROBERTO | MARANHÃO | Brasil | 2111672 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a7a0bae7-0ad7-3b98-9bc5-6261361d8e8a | -4.68581 | -42.37148 | 2024-11-30 03:46:00 | NOAA-20 | JOSÉ DE FREITAS | PIAUÍ | Brasil | 2205508 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 2049e4c4-b4b4-30e4-b5e0-f18538130da0 | -5.93264 | -43.78839 | 2024-11-30 03:46:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 9.2 |
| 68b31b40-ad4d-3015-83bd-986c3ef50f02 | -5.46551 | -43.27302 | 2024-11-30 03:46:00 | NOAA-20 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 814a4bab-9ea0-3655-96e5-5899dd0086ea | -5.42151 | -44.85281 | 2024-11-30 03:46:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 4dede275-40ed-32b3-aa19-cb809efe9cba | -2.30594 | -47.08449 | 2024-11-30 03:46:00 | NOAA-20 | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 6b5b3782-1816-33d9-b74a-255bd4cb7e16 | -3.2516 | -48.89392 | 2024-11-30 03:46:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 18723718-5be9-353a-94ec-dfd1741f4e62 | -10.22153 | -36.65785 | 2024-11-30 03:46:00 | NOAA-20 | IGREJA NOVA | ALAGOAS | Brasil | 2703205 | 27 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| fe2f56d8-81a5-3c6c-845b-52ff3dbe91c5 | -3.70429 | -47.15346 | 2024-11-30 03:46:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 37739ac1-f0a2-369d-88e9-42e2e25c70ab | -4.58795 | -44.70758 | 2024-11-30 03:46:00 | NOAA-20 | TRIZIDELA DO VALE | MARANHÃO | Brasil | 2112233 | 21 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 15eae8b0-d5ec-376a-b602-e6d100fb28f3 | -6.89702 | -43.55009 | 2024-11-30 03:46:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 6daf5544-16d6-399e-8bb3-ba8bb17c2bf4 | -3.97343 | -41.51713 | 2024-11-30 03:46:00 | NOAA-20 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 4.6 |
| 64cbca30-0969-3469-8a26-c55018564539 | -4.6967 | -42.38608 | 2024-11-30 03:46:00 | NOAA-20 | JOSÉ DE FREITAS | PIAUÍ | Brasil | 2205508 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| bc156cb6-9004-3cd0-b9fb-59357b43fbed | -2.58468 | -48.20967 | 2024-11-30 03:46:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |


[Clique aqui para ver as próximas entradas](README21.md)
