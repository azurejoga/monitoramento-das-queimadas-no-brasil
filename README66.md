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

## Dados Diários - Página 66

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 86d21ef8-3dd4-3c13-b635-451cb2195d00 | -2.709 | -43.97382 | 2024-12-03 12:38:00 | TERRA_M-T | ICATU | MARANHÃO | Brasil | 2105104 | 21 | 33 | nan | nan | nan | Amazônia | 5.0 |
| db0ffca5-f3ca-312c-81ee-027547b47137 | -3.05999 | -42.35924 | 2024-12-03 12:38:00 | TERRA_M-T | TUTÓIA | MARANHÃO | Brasil | 2112506 | 21 | 33 | nan | nan | nan | Cerrado | 70.8 |
| 07e90278-415a-3b13-a904-646786b58a10 | -3.36891 | -41.98166 | 2024-12-03 12:38:00 | TERRA_M-T | MURICI DOS PORTELAS | PIAUÍ | Brasil | 2206696 | 22 | 33 | nan | nan | nan | Caatinga | 130.8 |
| 959bf837-c7da-3de3-8f20-7ae341eb0a9f | -3.32671 | -42.06113 | 2024-12-03 12:38:00 | TERRA_M-T | MURICI DOS PORTELAS | PIAUÍ | Brasil | 2206696 | 22 | 33 | nan | nan | nan | Cerrado | 18.3 |
| aa5e7c6a-fe7f-37ad-9266-5d6ca63334cd | -2.66681 | -46.125 | 2024-12-03 12:38:00 | TERRA_M-T | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 6146566e-e80d-32c2-b4cc-762924ae7cff | -3.34585 | -42.21927 | 2024-12-03 12:38:00 | TERRA_M-T | MAGALHÃES DE ALMEIDA | MARANHÃO | Brasil | 2106300 | 21 | 33 | nan | nan | nan | Cerrado | 12.8 |
| ab5543b2-169a-344d-aabb-091015636bb1 | -2.8458 | -41.99448 | 2024-12-03 12:38:00 | TERRA_M-T | ARAIOSES | MARANHÃO | Brasil | 2100907 | 21 | 33 | nan | nan | nan | Cerrado | 61.1 |
| 7c74db01-bdcc-3bb4-be23-a7528abc3938 | -7.37165 | -39.00731 | 2024-12-03 12:38:00 | TERRA_M-T | ABAIARA | CEARÁ | Brasil | 2300101 | 23 | 33 | nan | nan | nan | Caatinga | 14.5 |
| 7316e098-c59e-3156-b9fc-272dc2b5a499 | -7.11546 | -45.87073 | 2024-12-03 12:38:00 | TERRA_M-T | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 1f463a8f-e934-3cf0-bf20-d450e73136a1 | -4.04345 | -46.99976 | 2024-12-03 12:38:00 | TERRA_M-T | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 31.6 |
| 934c82a8-20a6-3b9c-b2ee-8f7feebd73b0 | -3.40329 | -42.46523 | 2024-12-03 12:38:00 | TERRA_M-T | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Caatinga | 9.5 |
| 1631f110-329f-3cd8-b731-f703c3ba9f74 | -4.91347 | -47.86051 | 2024-12-03 12:38:00 | TERRA_M-T | CIDELÂNDIA | MARANHÃO | Brasil | 2103257 | 21 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 7edfae7c-c738-354e-9f33-a8673a10f402 | -2.92207 | -42.1771 | 2024-12-03 12:38:00 | TERRA_M-T | ÁGUA DOCE DO MARANHÃO | MARANHÃO | Brasil | 2100154 | 21 | 33 | nan | nan | nan | Cerrado | 36.6 |
| 92161b53-d8a2-3488-86c7-3a9cb778e7a0 | -2.92685 | -41.92676 | 2024-12-03 12:38:00 | TERRA_M-T | ARAIOSES | MARANHÃO | Brasil | 2100907 | 21 | 33 | nan | nan | nan | Caatinga | 82.8 |
| 89f9bcc6-b653-304e-8946-c4a8bc9758a6 | -4.43823 | -42.89412 | 2024-12-03 12:38:00 | TERRA_M-T | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 13.5 |
| 95ee2f4b-6df9-3301-a092-2b812cbada1f | -3.69017 | -45.433 | 2024-12-03 12:38:00 | TERRA_M-T | PINDARÉ-MIRIM | MARANHÃO | Brasil | 2108504 | 21 | 33 | nan | nan | nan | Amazônia | 10.1 |
| cb5a1116-2555-341f-a2e5-19c9934b9ff6 | -3.46469 | -41.60336 | 2024-12-03 12:38:00 | TERRA_M-T | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 156.1 |
| f20aa911-2c91-3af7-8232-bf867ed70912 | -4.05527 | -41.98167 | 2024-12-03 12:38:00 | TERRA_M-T | BATALHA | PIAUÍ | Brasil | 2201507 | 22 | 33 | nan | nan | nan | Caatinga | 21.5 |
| a1f27ab0-3d4b-3cc1-a22c-31fcb87ea1fe | -3.70361 | -47.11318 | 2024-12-03 12:38:00 | TERRA_M-T | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 16.9 |
| db117376-d2fb-3cd8-b26c-780349932541 | -7.56757 | -45.73169 | 2024-12-03 12:38:00 | TERRA_M-T | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 67.2 |
| a9c1df5e-9233-3749-b022-e92136475526 | -3.14745 | -42.32009 | 2024-12-03 12:38:00 | TERRA_M-T | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Cerrado | 28.9 |
| c1754f72-6e68-309b-8e0b-5c4f8b673495 | -1.5984 | -47.11874 | 2024-12-03 12:38:00 | TERRA_M-T | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 8.6 |
| 4abfed4e-2219-39aa-bc3a-11bf9fbe09c7 | -3.34235 | -46.04678 | 2024-12-03 12:38:00 | TERRA_M-T | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 18.0 |
| 32169101-3de4-3320-92f9-fb12e58cad23 | -5.56689 | -44.88692 | 2024-12-03 12:38:00 | TERRA_M-T | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 78c93717-34c1-3097-a63b-026dd6cf41aa | -3.19383 | -42.28002 | 2024-12-03 12:38:00 | TERRA_M-T | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Cerrado | 30.1 |
| f665f88b-2091-342e-95d0-00f5bebca7e8 | -3.37061 | -41.96953 | 2024-12-03 12:38:00 | TERRA_M-T | MURICI DOS PORTELAS | PIAUÍ | Brasil | 2206696 | 22 | 33 | nan | nan | nan | Caatinga | 10.5 |
| 15cb22f1-f1ea-30f1-a319-28fa42c1679c | -3.35426 | -42.23223 | 2024-12-03 12:38:00 | TERRA_M-T | MAGALHÃES DE ALMEIDA | MARANHÃO | Brasil | 2106300 | 21 | 33 | nan | nan | nan | Cerrado | 249.5 |
| f33743d5-1642-3ed8-a851-701b1f498c85 | -3.35593 | -44.35036 | 2024-12-03 12:38:00 | TERRA_M-T | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 14.8 |
| 496c4b6b-f70c-39c3-99be-7fc1a7f08623 | -3.34374 | -42.08757 | 2024-12-03 12:38:00 | TERRA_M-T | MURICI DOS PORTELAS | PIAUÍ | Brasil | 2206696 | 22 | 33 | nan | nan | nan | Caatinga | 39.6 |
| 5d178e8b-067d-3ed3-a8bd-514e7a042042 | -3.39603 | -44.64811 | 2024-12-03 12:38:00 | TERRA_M-T | ANAJATUBA | MARANHÃO | Brasil | 2100709 | 21 | 33 | nan | nan | nan | Amazônia | 11.7 |
| 83bcc338-c825-3a8b-ac98-6279c8e656d8 | -3.3559 | -42.22062 | 2024-12-03 12:38:00 | TERRA_M-T | MAGALHÃES DE ALMEIDA | MARANHÃO | Brasil | 2106300 | 21 | 33 | nan | nan | nan | Cerrado | 28.3 |
| 83afcf0a-8d96-3dd0-8c35-2b14b496d017 | -3.31347 | -44.39093 | 2024-12-03 12:38:00 | TERRA_M-T | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 7.9 |
| d60671a0-61a7-31f9-9df9-c91ac5cc02be | -2.84749 | -41.98269 | 2024-12-03 12:38:00 | TERRA_M-T | ARAIOSES | MARANHÃO | Brasil | 2100907 | 21 | 33 | nan | nan | nan | Caatinga | 7.6 |
| f6d11af9-51b2-3b39-a8f2-b7f23e5f73d0 | -3.71976 | -39.6272 | 2024-12-03 12:38:00 | TERRA_M-T | ITAPAJÉ | CEARÁ | Brasil | 2306306 | 23 | 33 | nan | nan | nan | Caatinga | 43.4 |
| 6161dd1f-0db1-3fdd-9fe8-d2094d693777 | -3.4021 | -42.25624 | 2024-12-03 12:38:00 | TERRA_M-T | MAGALHÃES DE ALMEIDA | MARANHÃO | Brasil | 2106300 | 21 | 33 | nan | nan | nan | Cerrado | 9.3 |
| 518a3103-3db2-3003-965a-311dea8b4987 | -3.67093 | -42.38215 | 2024-12-03 12:38:00 | TERRA_M-T | LUZILÂNDIA | PIAUÍ | Brasil | 2205805 | 22 | 33 | nan | nan | nan | Caatinga | 20.3 |
| 8d9f773d-9437-3ed0-8918-256bf7c24a24 | -4.41116 | -46.62603 | 2024-12-03 12:38:00 | TERRA_M-T | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 8.1 |
| c5700c53-d3f3-338d-ac44-3479f57e23c0 | -7.07659 | -45.62293 | 2024-12-03 12:38:00 | TERRA_M-T | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 8.7 |
| a26a31bd-5e30-33a5-916e-6e2a37fb5cdd | -2.84412 | -42.00623 | 2024-12-03 12:38:00 | TERRA_M-T | ARAIOSES | MARANHÃO | Brasil | 2100907 | 21 | 33 | nan | nan | nan | Cerrado | 28.0 |
| c32bebbd-a440-3fd7-854c-7f8fa1a15b4e | -3.00252 | -41.39006 | 2024-12-03 12:38:00 | TERRA_M-T | CAJUEIRO DA PRAIA | PIAUÍ | Brasil | 2202083 | 22 | 33 | nan | nan | nan | Caatinga | 32.2 |
| 3262c790-e93e-3476-950e-9d5d52a6c43e | -7.23896 | -46.73014 | 2024-12-03 12:38:00 | TERRA_M-T | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 8.0 |
| c5d6cab3-c310-35bf-a52a-d5fac2da6088 | -4.05381 | -46.99186 | 2024-12-03 12:38:00 | TERRA_M-T | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 9.0 |
| 4cad8ad0-defc-3bb5-905b-9404a5eff93c | -3.28528 | -44.91435 | 2024-12-03 12:38:00 | TERRA_M-T | VIANA | MARANHÃO | Brasil | 2112803 | 21 | 33 | nan | nan | nan | Amazônia | 8.3 |
| 5a07d282-887d-3210-85f3-f0e99d2a1808 | -3.19358 | -42.28594 | 2024-12-03 12:38:00 | TERRA_M-T | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Cerrado | 29.5 |
| 75a5f53a-fd23-35e0-a199-9b2317864e0c | -9.16082 | -43.11197 | 2024-12-03 12:38:00 | TERRA_M-T | JUREMA | PIAUÍ | Brasil | 2205532 | 22 | 33 | nan | nan | nan | Caatinga | 25.5 |
| 84711580-cd5e-350e-a6b9-13b0d3647c8e | -3.15066 | -42.29734 | 2024-12-03 12:38:00 | TERRA_M-T | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Cerrado | 61.9 |
| 43f9a75c-3c25-3600-88f9-500eeb3ed755 | -3.55609 | -44.69189 | 2024-12-03 12:38:00 | TERRA_M-T | ARARI | MARANHÃO | Brasil | 2101004 | 21 | 33 | nan | nan | nan | Amazônia | 10.5 |
| f93b7bba-ceb1-36f2-8bc3-d0c5eb844cf3 | -3.85344 | -46.52803 | 2024-12-03 12:38:00 | TERRA_M-T | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 7.3 |
| 2d5cd134-128b-3341-9bd3-2de79a1f3598 | -1.83637 | -47.07577 | 2024-12-03 12:38:00 | TERRA_M-T | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 28.1 |
| 0d0c9be9-ca21-33a8-96bb-c2d4dd48fe17 | -1.70204 | -47.04103 | 2024-12-03 12:38:00 | TERRA_M-T | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 13.7 |
| 8a794153-3f73-354e-9395-4e355146ac72 | -1.59057 | -46.73204 | 2024-12-03 12:38:00 | TERRA_M-T | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 8.8 |
| 146e71cf-c7a2-3f0f-b117-de8e8f42e58c | -2.49938 | -47.26847 | 2024-12-03 12:38:00 | TERRA_M-T | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| b77ff9fb-51bc-3133-867c-34179b0a25ef | -4.04424 | -46.86882 | 2024-12-03 12:38:00 | TERRA_M-T | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 7.9 |
| b49eae97-1382-38cc-979d-94fe125cbce8 | -3.09407 | -42.04678 | 2024-12-03 12:38:00 | TERRA_M-T | ARAIOSES | MARANHÃO | Brasil | 2100907 | 21 | 33 | nan | nan | nan | Cerrado | 12.9 |
| 79dc9e03-4266-36d1-ae79-1662de9ac4ff | -5.84386 | -44.757 | 2024-12-03 12:38:00 | TERRA_M-T | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 7.4 |
| e79048a2-c9a3-3ef2-9858-f80e12780b2a | -4.57296 | -47.29255 | 2024-12-03 12:38:00 | TERRA_M-T | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 20.7 |
| 55d3f831-1a7f-3e31-a5a2-487252461fdf | -9.56086 | -46.31128 | 2024-12-03 12:38:00 | TERRA_M-T | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 10.2 |
| 16dbb33b-1397-3aac-af3a-b75d4c8176fa | -3.46652 | -41.59055 | 2024-12-03 12:38:00 | TERRA_M-T | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 46.5 |
| 4bdc465a-6877-3533-85a0-ab110b2af315 | -4.1001 | -47.80824 | 2024-12-03 12:38:00 | TERRA_M-T | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 9.1 |
| e2c8a718-1ed8-3aa6-8928-271e7130b535 | -2.92854 | -41.91476 | 2024-12-03 12:38:00 | TERRA_M-T | ARAIOSES | MARANHÃO | Brasil | 2100907 | 21 | 33 | nan | nan | nan | Caatinga | 12.1 |
| c6861309-8c94-3e67-a399-289e41e02035 | -4.54559 | -42.92659 | 2024-12-03 12:38:00 | TERRA_M-T | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 17.2 |
| 580f62b4-aec0-3436-8f4d-6b64af1fe8a9 | -7.5677 | -45.7273 | 2024-12-03 12:40:00 | GOES-16 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 93.6 |
| d92cc6b4-4b1d-3038-bbbf-1e866f99cdd8 | -15.89681 | -46.59844 | 2024-12-03 12:40:00 | TERRA_M-T | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 10.4 |
| e50cc39f-57ff-3da4-be2d-6b4eb02ae346 | -11.08284 | -44.46185 | 2024-12-03 12:40:00 | TERRA_M-T | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 10.1 |
| df3ff021-a309-33b3-868d-2ee83463a35b | -12.49606 | -43.36925 | 2024-12-03 12:40:00 | TERRA_M-T | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 9.4 |
| 5d5410dc-c591-370b-b1e4-a48370e12982 | -10.45195 | -44.88959 | 2024-12-03 12:40:00 | TERRA_M-T | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 8.9 |
| c626dca8-492e-3f73-a91d-dc6f256348ec | -11.1616 | -44.73348 | 2024-12-03 12:40:00 | TERRA_M-T | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 13.8 |
| 9bb098c9-601d-3c41-843f-8e05aff09039 | -13.18717 | -45.22145 | 2024-12-03 12:40:00 | TERRA_M-T | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 13.4 |
| 9a4e4428-dae0-341a-bec5-7398d056edcb | -12.25346 | -45.57299 | 2024-12-03 12:40:00 | TERRA_M-T | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 21ab13ac-967d-3043-8c91-3a69179f715c | -12.05913 | -46.69669 | 2024-12-03 12:40:00 | TERRA_M-T | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 6.4 |
| c2df531b-4660-3285-a912-8885107542b8 | -10.46215 | -45.07035 | 2024-12-03 12:40:00 | TERRA_M-T | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 9.6 |
| eff50eb0-05d3-3ad6-b7d2-1bddb7fd69e3 | -32.33366 | -53.62532 | 2024-12-03 12:44:00 | TERRA_M-T | JAGUARÃO | RIO GRANDE DO SUL | Brasil | 4311007 | 43 | 33 | nan | nan | nan | Pampa | 26.0 |
| c799140c-68c4-3e16-bf2d-24c86cbfef5c | -32.33196 | -53.63622 | 2024-12-03 12:44:00 | TERRA_M-T | JAGUARÃO | RIO GRANDE DO SUL | Brasil | 4311007 | 43 | 33 | nan | nan | nan | Pampa | 5.5 |
| 6053aae7-19a0-39d4-9fec-f096819a4621 | -30.62351 | -51.73547 | 2024-12-03 12:44:00 | TERRA_M-T | CERRO GRANDE DO SUL | RIO GRANDE DO SUL | Brasil | 4305173 | 43 | 33 | nan | nan | nan | Pampa | 4.3 |
| 408db76f-6522-32d7-a587-8c0d03589fd8 | -28.2972 | -49.93109 | 2024-12-03 12:44:00 | TERRA_M-T | SÃO JOAQUIM | SANTA CATARINA | Brasil | 4216503 | 42 | 33 | nan | nan | nan | Mata Atlântica | 5.6 |
| c21fb18f-0705-30f8-a70f-e62b6d6de318 | -1.3466 | -54.9763 | 2024-12-03 12:50:00 | GOES-16 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 70.9 |
| a24e02e0-21b7-322a-aa6d-af25796875f4 | -4.0673 | -46.8145 | 2024-12-03 13:00:00 | GOES-16 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 85.4 |
| 36a62b98-fd96-30c6-af0e-ffeef89d886b | -3.34 | -42.22 | 2024-12-03 13:00:00 | MSG-03 | MAGALHÃES DE ALMEIDA | MARANHÃO | Brasil | 2106300 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 57557ab9-b435-30d1-ae2d-dc56d47b9224 | -3.37 | -42.22 | 2024-12-03 13:00:00 | MSG-03 | MAGALHÃES DE ALMEIDA | MARANHÃO | Brasil | 2106300 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 636d9e55-d41f-34c5-844c-09e9c8f1ca12 | -3.785 | -47.5065 | 2024-12-03 13:10:00 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 148.9 |
| 96e7d2da-44c7-3ea4-a626-2e561e2775b7 | -4.6753 | -42.3799 | 2024-12-03 13:20:00 | GOES-16 | JOSÉ DE FREITAS | PIAUÍ | Brasil | 2205508 | 22 | 33 | nan | nan | nan | Caatinga | 79.4 |
| a89e85e6-d8d1-378e-80bf-2c460287f4dc | -3.785 | -47.5065 | 2024-12-03 13:20:00 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 91.9 |
| ab04571e-8b58-3aba-9c12-77dbfe64c24d | -4.5403 | -42.9066 | 2024-12-03 13:30:00 | GOES-16 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 122.0 |
| 4d31638a-4716-3c62-8e56-1767f3e48846 | -4.5591 | -42.9054 | 2024-12-03 13:30:00 | GOES-16 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 154.8 |
| 206613f7-897f-3f22-840c-3c5d72f3072e | -3.785 | -47.5065 | 2024-12-03 13:40:00 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 78.4 |
| 6a72e452-fd01-33ca-89a8-565c27d57b52 | -2.8828 | -41.9291 | 2024-12-03 13:40:00 | GOES-16 | ARAIOSES | MARANHÃO | Brasil | 2100907 | 21 | 33 | nan | nan | nan | Caatinga | 187.0 |
| ae9f6e4e-6048-36f1-b7b2-92d1da74cd2b | -4.5403 | -42.9066 | 2024-12-03 14:10:00 | GOES-16 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 131.4 |


