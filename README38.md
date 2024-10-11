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

## Dados Diários - Página 38

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| b2e0a54d-d7c2-369d-a872-f20c9baedafa | -5.8673 | -46.42489 | 2024-10-11 04:00:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 3a2992cb-02b2-3a65-9588-4993388d5a29 | -5.61002 | -46.36681 | 2024-10-11 04:00:00 | NPP-375D | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 7a5d21b3-91de-364a-ba9f-fc3cca3da7ac | -5.60547 | -46.3661 | 2024-10-11 04:00:00 | NPP-375D | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| dc8b0062-d567-3042-bdb3-5b7d57d728ff | -5.60468 | -46.37075 | 2024-10-11 04:00:00 | NPP-375D | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 8a83fb21-5c40-38d2-96ba-db9b1a071d18 | -5.57193 | -45.41561 | 2024-10-11 04:00:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 58624518-a910-338f-8316-2dca911c07bf | -5.5713 | -45.41943 | 2024-10-11 04:00:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 7922c4f2-ae48-37ec-8d12-16a5c1d255a7 | -5.34586 | -45.42434 | 2024-10-11 04:00:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 1a69ca4a-f888-3eda-b5b9-de0fe5feca10 | -5.25857 | -46.22772 | 2024-10-11 04:00:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 57a8283e-401c-3868-ae0a-412769d0c6c0 | -5.25325 | -46.23154 | 2024-10-11 04:00:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 2.3 |
| e108bf57-8c52-344b-bf9a-4e6967f61082 | -5.25308 | -46.22948 | 2024-10-11 04:00:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 173bd2bf-19e3-39c8-97a0-8f7c98bb319b | -5.19531 | -45.95199 | 2024-10-11 04:00:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 2.8 |
| ed13d5a6-d877-320d-8ac5-b2288c1655a5 | -5.19459 | -45.95638 | 2024-10-11 04:00:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 41377918-8bf1-38e4-a492-4e3e664cc311 | -5.19406 | -45.94996 | 2024-10-11 04:00:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 43ac9c9d-ae94-31af-a162-2f39d817e1b5 | -5.19335 | -45.95412 | 2024-10-11 04:00:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 4a547083-908f-3cf8-92c2-dd52f2050685 | -5.19086 | -45.95121 | 2024-10-11 04:00:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 6.3 |
| b33a93fc-833b-376d-9aba-3fa8e8b6ea14 | -5.13707 | -45.32889 | 2024-10-11 04:00:00 | NPP-375D | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| e80e2597-235f-3125-871a-0b0ba60b7074 | -5.13119 | -45.3116 | 2024-10-11 04:00:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 23b62297-5a49-3bfc-8f94-81ba6f43119f | -5.11449 | -46.10627 | 2024-10-11 04:00:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| ec778725-613c-3be7-ac5c-c6428891cb87 | -5.11001 | -46.10544 | 2024-10-11 04:00:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| bb02f148-6352-35fa-a04e-fee27f5dbbf1 | -7.8196 | -46.4859 | 2024-10-11 04:00:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| aa45dfbb-fe2e-350f-b826-e57c362d2d87 | -7.81697 | -46.48322 | 2024-10-11 04:00:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| b7014564-67c0-3dd6-bf74-9abdacd8f123 | -7.81623 | -46.48761 | 2024-10-11 04:00:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| e4b4084a-07e5-3aa9-a237-b1aeddc1278a | -7.81519 | -46.48512 | 2024-10-11 04:00:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 383b9bae-a617-372e-81b4-8307d5ec78eb | -7.33027 | -45.51782 | 2024-10-11 04:00:00 | NPP-375D | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| ed0a6bf9-5761-3a4a-99a4-fb0d846c5c5a | -7.27362 | -45.37195 | 2024-10-11 04:00:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| f4cac5c7-b310-33d9-95ee-bab85d3a8835 | -7.26949 | -45.37123 | 2024-10-11 04:00:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 0c222d04-82b8-30c1-83c5-ed020ab6d9e5 | -7.25865 | -45.38482 | 2024-10-11 04:00:00 | NPP-375D | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 7dcc7031-1043-3318-a2f9-49c57174ec5b | -7.258 | -45.38857 | 2024-10-11 04:00:00 | NPP-375D | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 9981dbf8-6c9f-3af8-831e-b8734c577ae7 | -7.23395 | -45.52848 | 2024-10-11 04:00:00 | NPP-375D | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| d039f991-66b2-3d72-b3c2-e302f72c554c | -7.22976 | -45.52785 | 2024-10-11 04:00:00 | NPP-375D | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 7cd1bcda-0a5d-37a3-950d-b70bc99976cb | -7.1039 | -45.32439 | 2024-10-11 04:00:00 | NPP-375D | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 6556502d-abf1-30ba-a110-7ec7dd39a7a9 | -7.10327 | -45.32816 | 2024-10-11 04:00:00 | NPP-375D | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| ef0c98ce-c72d-3734-8c30-c1417f361019 | -7.09261 | -45.44266 | 2024-10-11 04:00:00 | NPP-375D | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 7e82666a-e545-3765-860c-05a299c78d7c | -6.99974 | -45.2492 | 2024-10-11 04:00:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c6f97286-9c57-3458-a39e-29e13d7b83a9 | -6.99911 | -45.253 | 2024-10-11 04:00:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| d4983522-564c-3f01-8743-243f148472f1 | -6.99268 | -45.70009 | 2024-10-11 04:00:00 | NPP-375D | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 07b3c830-d5af-31bb-b4d5-08473c8a738a | -6.992 | -45.70402 | 2024-10-11 04:00:00 | NPP-375D | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 7232962d-a7ba-34ab-8223-b27c859ae9a4 | -6.98774 | -45.70339 | 2024-10-11 04:00:00 | NPP-375D | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 668ac57b-2c89-3fb2-b13c-9b4a2bf2f6a0 | -6.97516 | -45.7256 | 2024-10-11 04:00:00 | NPP-375D | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 4037822f-8292-3512-b6ec-fd9b50623340 | -6.95868 | -45.29115 | 2024-10-11 04:00:00 | NPP-375D | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 44846743-0b67-37ad-9b2f-08f18643056d | -6.95803 | -45.29495 | 2024-10-11 04:00:00 | NPP-375D | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 7056696f-6d57-3ae9-8a61-4e64d75faa70 | -6.95396 | -45.29389 | 2024-10-11 04:00:00 | NPP-375D | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 78238555-2af1-3966-99b2-2c38ba0aad0f | -6.94953 | -45.22068 | 2024-10-11 04:00:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 36183555-f77a-3b12-a86c-fda5a8ffb7df | -6.94889 | -45.2244 | 2024-10-11 04:00:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 004d64f0-88f4-3c1a-aee6-3208b3ff2763 | -6.93954 | -46.32513 | 2024-10-11 04:00:00 | NPP-375D | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f6b53540-b5f8-3c68-b73a-c27160492f0c | -6.93512 | -46.32432 | 2024-10-11 04:00:00 | NPP-375D | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 09e1ed9b-7f38-3437-95a8-eeb4ab84e44c | -6.82974 | -46.17449 | 2024-10-11 04:00:00 | NPP-375D | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| a3c098ab-3c22-3d3e-83a1-dd30964991f1 | -6.80118 | -46.47619 | 2024-10-11 04:00:00 | NPP-375D | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 600fa9ee-e30e-3ed2-b579-d62fa7cf0e23 | -6.79019 | -45.64599 | 2024-10-11 04:00:00 | NPP-375D | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b01b24fc-3aee-3613-81fa-a36e52852ed9 | -6.7866 | -45.64144 | 2024-10-11 04:00:00 | NPP-375D | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 17ffd40d-ba44-3ccc-9177-6626a5d42a67 | -6.78593 | -45.64532 | 2024-10-11 04:00:00 | NPP-375D | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 5b1ce855-993c-3b9e-9293-8d47d98ecf3c | -6.78527 | -45.64918 | 2024-10-11 04:00:00 | NPP-375D | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 2edba380-f4d4-39e0-bfb0-64b4b1e5a986 | -6.71655 | -46.23329 | 2024-10-11 04:00:00 | NPP-375D | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| c424bc6d-3f18-3e70-b000-0cb8851a214a | -6.49805 | -46.16731 | 2024-10-11 04:00:00 | NPP-375D | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 131f63c1-afa7-35de-93ba-cc5c4ac88174 | -3.30209 | -46.07765 | 2024-10-11 04:00:00 | NPP-375D | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 12.8 |
| 2091a51a-311c-3695-8139-4ce363edac56 | -3.58924 | -46.41087 | 2024-10-11 04:00:00 | NPP-375D | SÃO JOÃO DO CARÚ | MARANHÃO | Brasil | 2111029 | 21 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 92ec3f48-77e6-3ccb-88e8-69d66fcd8562 | -3.58665 | -46.45644 | 2024-10-11 04:00:00 | NPP-375D | SÃO JOÃO DO CARÚ | MARANHÃO | Brasil | 2111029 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f2c483db-f526-3edf-90da-368966538cb1 | -3.36093 | -46.49237 | 2024-10-11 04:00:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 922ab52e-71fe-309a-8abe-1c08612fb5e5 | -4.91461 | -47.65292 | 2024-10-11 04:00:00 | NPP-375D | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 5.2 |
| fb4815a9-f28d-3ff0-838b-2c33e21f5b60 | -4.91379 | -47.65381 | 2024-10-11 04:00:00 | NPP-375D | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 8f43842f-098c-3e3b-885a-2968865db387 | -4.31654 | -47.70874 | 2024-10-11 04:00:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 3f71d66f-2f5a-3d9e-8f6f-2b09ce4488d3 | -3.81064 | -47.49082 | 2024-10-11 04:00:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d678d01c-3bef-3be7-b890-e8953608dfb4 | -3.81016 | -47.49371 | 2024-10-11 04:00:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 13caf614-a417-3c19-a271-d78559b968f4 | -3.70164 | -47.59645 | 2024-10-11 04:00:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 7ae43145-a345-39dc-ab28-d2dbc6c65fac | -4.99482 | -47.36216 | 2024-10-11 04:00:00 | NPP-375D | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 31aa5c24-fd22-3146-bdb0-e1c8776fcb5a | -4.9508 | -47.4042 | 2024-10-11 04:00:00 | NPP-375D | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| a7cd2261-8b3f-3ab1-9a17-d483797f5704 | -4.94688 | -47.40492 | 2024-10-11 04:00:00 | NPP-375D | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 2.9 |
| d1a3a338-f388-34f2-90d0-ca1da3f4f5d7 | -4.94585 | -47.40346 | 2024-10-11 04:00:00 | NPP-375D | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| efe54cec-1352-3cdf-be88-8ce13d8aa67c | -4.91107 | -46.70399 | 2024-10-11 04:00:00 | NPP-375D | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| cdb1a501-5b9d-3a30-bf90-0939d156b6c3 | -4.9102 | -46.70912 | 2024-10-11 04:00:00 | NPP-375D | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 98ee3678-86bf-362e-940f-e9aeedd1df7e | -4.9046 | -46.71363 | 2024-10-11 04:00:00 | NPP-375D | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 1ab61abb-9535-3412-a8ff-f535ae2571dc | -4.67884 | -46.43553 | 2024-10-11 04:00:00 | NPP-375D | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| dc9a89cd-7599-3d15-aa0e-828223c95594 | -4.67801 | -46.44036 | 2024-10-11 04:00:00 | NPP-375D | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 42bccb08-c625-3c32-a727-ef0aa1a2bde3 | -4.67543 | -46.43776 | 2024-10-11 04:00:00 | NPP-375D | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 5.6 |
| f86117fd-03f8-31b5-98c8-d1e7f76ed23b | -4.66692 | -46.43162 | 2024-10-11 04:00:00 | NPP-375D | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 6b3aa05d-5439-3a8e-b668-faea539f0603 | -4.6643 | -46.80348 | 2024-10-11 04:00:00 | NPP-375D | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 91ac5ffa-7a2c-3ae4-a099-a8cfafd9cfaf | -4.65954 | -46.80275 | 2024-10-11 04:00:00 | NPP-375D | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3175320c-3130-3270-9517-0f18a43d6944 | -4.65866 | -46.80793 | 2024-10-11 04:00:00 | NPP-375D | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 315f0698-2392-3b15-a81a-ccb6192c03eb | -4.21346 | -46.89487 | 2024-10-11 04:00:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 5e06bfe6-c4a0-35b2-b9c3-63064e44264e | -4.20866 | -46.89397 | 2024-10-11 04:00:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 46a88a07-32e1-3272-820e-8708dabf0251 | -4.12587 | -46.68763 | 2024-10-11 04:00:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 11564eba-cef9-348a-b889-32b12f173592 | -3.94725 | -46.44123 | 2024-10-11 04:00:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 2b478af7-7351-3e96-b6ff-618804db6597 | -3.94635 | -46.43957 | 2024-10-11 04:00:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 81cd5b14-74bb-3016-b0ab-62eb9ee58eb0 | -3.93696 | -46.43798 | 2024-10-11 04:00:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f3384873-9059-3537-87ac-3cd52f3f3d7d | -3.93354 | -46.46516 | 2024-10-11 04:00:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.6 |
| b892bfcf-4463-3dcc-8baa-3da5148ec068 | -3.93318 | -46.43887 | 2024-10-11 04:00:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 85914658-f0e5-362b-9e68-f9184e4eb7dc | -3.93226 | -46.43724 | 2024-10-11 04:00:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 12739622-4fd2-39be-abf5-ebacdce675a1 | -3.93146 | -46.44213 | 2024-10-11 04:00:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.5 |
| acbff067-132f-3397-abd6-cf6ecc35c8a3 | -3.92979 | -46.45878 | 2024-10-11 04:00:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.6 |
| ddc0628f-ccbe-341a-a976-98d0a1e1b538 | -3.92889 | -46.46402 | 2024-10-11 04:00:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 0faf859c-da25-3fdd-9fce-5392322be88e | -3.9282 | -46.46226 | 2024-10-11 04:00:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 11.8 |
| b59ca3ef-1d9d-3d4f-ad0c-1d4efcb950f5 | -3.92598 | -46.45277 | 2024-10-11 04:00:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e1674307-d320-3e89-9b04-77bbe8d00e7b | -3.92512 | -46.45782 | 2024-10-11 04:00:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 2ec3f3ad-f297-3f2b-ac03-9ed83461b4c6 | -3.92425 | -46.46293 | 2024-10-11 04:00:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 4.3 |
| a05131a3-8ca2-3d37-8e09-f7fa0dc32d5e | -3.92354 | -46.4612 | 2024-10-11 04:00:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 8700891d-077a-39b4-8f61-278bd67f4d20 | -3.92265 | -46.46667 | 2024-10-11 04:00:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| b198e565-c2b4-3804-9e09-32b9d27ca45a | -3.90481 | -46.42819 | 2024-10-11 04:00:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| dc5c1d7a-a68e-3531-86bc-817820eb7be9 | -3.84882 | -46.47429 | 2024-10-11 04:00:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| b23d2472-c373-3c20-aee9-da7ea8663e2b | -3.80608 | -47.48701 | 2024-10-11 04:00:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 42cc1450-d4e0-36f3-b7b0-10bc273fe6aa | -3.8056 | -47.48988 | 2024-10-11 04:00:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |


[Clique aqui para ver as próximas entradas](README39.md)
