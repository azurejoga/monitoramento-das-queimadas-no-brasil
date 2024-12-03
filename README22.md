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

## Dados Diários - Página 22

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 6f64618b-738a-345f-be01-bbaa87dedbca | -4.56585 | -45.47436 | 2024-12-03 03:44:00 | NOAA-21 | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| fa3809e9-027e-3865-9d08-ca5fc34b99d0 | -5.12128 | -43.20854 | 2024-12-03 03:44:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 24.3 |
| b8e944dc-274a-3e3f-89da-44a2ad77e592 | -5.99894 | -45.41155 | 2024-12-03 03:44:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| d135800e-4ab4-3d9d-a6c3-2e540bfa707b | -9.81676 | -44.70705 | 2024-12-03 03:44:00 | NOAA-21 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b8713eda-6374-38e5-b251-0b41e0785e9e | -4.56007 | -45.47328 | 2024-12-03 03:44:00 | NOAA-21 | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 0c55cc3b-7cad-39ce-9811-cb967095653d | -3.26553 | -46.93073 | 2024-12-03 03:44:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| eb8f5c3a-6990-3f89-a1d9-591f0fdbb461 | -9.7002 | -42.88915 | 2024-12-03 03:44:00 | NOAA-21 | CAMPO ALEGRE DE LOURDES | BAHIA | Brasil | 2905909 | 29 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 3acf13b8-9c5d-3d7e-b4dd-d2f95f0711a0 | -3.34321 | -46.05667 | 2024-12-03 03:44:00 | NOAA-21 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 21.1 |
| a10c3211-2a2d-3050-baa1-dec4a9efdbf0 | -7.56456 | -45.73212 | 2024-12-03 03:44:00 | NOAA-21 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 77880b28-e4e6-355a-8426-638f157c167d | -5.81196 | -46.48911 | 2024-12-03 03:44:00 | NOAA-21 | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 73bde48b-2b64-31ae-9b7f-31367fb1e559 | -2.67133 | -46.61958 | 2024-12-03 03:44:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 34f82372-a12f-3f41-9a82-a634d93a0ce2 | -4.1641 | -48.59552 | 2024-12-03 03:44:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 7.8 |
| 208ced76-cba7-3380-9bce-7fab87ce5ccb | -4.01345 | -47.00757 | 2024-12-03 03:44:00 | NOAA-21 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 2.9 |
| e352fb62-1983-3774-9323-25f68dfa1dbd | -5.11038 | -43.21271 | 2024-12-03 03:44:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 109af31c-2778-3d50-8beb-0b2bd2de15e0 | -6.98148 | -43.51543 | 2024-12-03 03:44:00 | NOAA-21 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 38.5 |
| 160a9fa5-45de-3eca-ac7e-6787e19210ab | -4.47063 | -45.72147 | 2024-12-03 03:44:00 | NOAA-21 | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d6269a7c-3bfb-397c-b74f-8d068843de6f | -5.79515 | -46.5071 | 2024-12-03 03:44:00 | NOAA-21 | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 4d6af647-2379-3fb9-95fc-3849ce0493ad | -3.46528 | -42.00762 | 2024-12-03 03:44:00 | NOAA-21 | MURICI DOS PORTELAS | PIAUÍ | Brasil | 2206696 | 22 | 33 | nan | nan | nan | Caatinga | 12.1 |
| 82649585-3424-3a3f-9b16-1e1b8441ee7c | -2.85189 | -45.83059 | 2024-12-03 03:44:00 | NOAA-21 | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | 2.5 |
| aeb4dc5d-3a81-3ae0-a3ac-cc3c1cbfaccd | -3.89792 | -45.01131 | 2024-12-03 03:44:00 | NOAA-21 | PIO XII | MARANHÃO | Brasil | 2108702 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ef612c62-2f9d-3e32-bb79-abab0a401e25 | -5.80613 | -46.48028 | 2024-12-03 03:44:00 | NOAA-21 | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 37.5 |
| 9a381758-2d05-370d-aa04-8d3937bab34c | -6.11936 | -43.96375 | 2024-12-03 03:44:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 22.1 |
| 7844dee7-09f2-3ea6-ab0d-fb29b8fde5b2 | -4.15746 | -43.06205 | 2024-12-03 03:44:00 | NOAA-21 | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c2870fe6-4cac-3736-ae4b-3436e9b45511 | -5.81109 | -46.49385 | 2024-12-03 03:44:00 | NOAA-21 | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 380113cc-0ca8-3091-8bb7-47407dabfba3 | -4.16476 | -48.19748 | 2024-12-03 03:44:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 8.9 |
| 28e5befc-f1c3-3aa4-bede-7108a31c9726 | -10.4991 | -36.71604 | 2024-12-03 03:44:00 | NOAA-21 | PACATUBA | SERGIPE | Brasil | 2804904 | 28 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| ee88eb16-7de5-3928-bdc4-a41081c740ea | -8.52824 | -35.50829 | 2024-12-03 03:44:00 | NOAA-21 | JOAQUIM NABUCO | PERNAMBUCO | Brasil | 2608206 | 26 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| b0863e2d-4886-31ce-975d-924067477585 | -2.85799 | -45.83162 | 2024-12-03 03:44:00 | NOAA-21 | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | 9.3 |
| 04a61a95-cce8-36fb-8d43-d433469f95ac | -4.82565 | -43.43298 | 2024-12-03 03:44:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 3120351b-0a73-3556-8de6-09f2e3ca60a3 | -5.81909 | -46.47766 | 2024-12-03 03:44:00 | NOAA-21 | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 18.2 |
| 2cae98e6-98dc-3a1e-abd4-280985d9fb5c | -4.54502 | -42.92962 | 2024-12-03 03:44:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 8.5 |
| 2e70fa31-349a-3e22-b1b4-8817ecb56a16 | -9.8154 | -44.70797 | 2024-12-03 03:44:00 | NOAA-21 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 234950d9-a823-3e14-ac01-38d775e5fb5e | -3.60148 | -45.58982 | 2024-12-03 03:44:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 83cafd00-c76d-3ced-9280-434e0129b968 | -6.99225 | -43.52704 | 2024-12-03 03:44:00 | NOAA-21 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 23.0 |
| ba630ec6-f611-37e5-9847-dcc29b069d98 | -6.02463 | -46.25042 | 2024-12-03 03:44:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 44f506af-8b3b-3f16-b45a-c4851537a815 | -4.93617 | -43.77808 | 2024-12-03 03:44:00 | NOAA-21 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 7.5 |
| ac108bf9-23e6-3076-a34e-58445824fd90 | -6.98932 | -43.5281 | 2024-12-03 03:44:00 | NOAA-21 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 12.3 |
| c2d0c63e-ba95-356f-abac-e17b63c35067 | -6.03575 | -42.52258 | 2024-12-03 03:44:00 | NOAA-21 | HUGO NAPOLEÃO | PIAUÍ | Brasil | 2204600 | 22 | 33 | nan | nan | nan | Caatinga | 13.4 |
| 81a6b590-9ccf-3f32-bed4-f4627abbfcfa | -3.80748 | -42.55324 | 2024-12-03 03:44:00 | NOAA-21 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 1816101a-5b84-3dae-baa5-c404e4c8fed2 | -4.9413 | -43.77908 | 2024-12-03 03:44:00 | NOAA-21 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 949392fc-bf20-3fd8-a6e0-b0af2953762e | -3.34247 | -46.06113 | 2024-12-03 03:44:00 | NOAA-21 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 13.4 |
| 35806664-8c65-360b-93ed-fa22c7a687c2 | -4.16534 | -48.58871 | 2024-12-03 03:44:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 45e11d21-7b3a-3697-8dde-063bdb56b17e | -4.34623 | -43.75198 | 2024-12-03 03:44:00 | NOAA-21 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 329b3c63-dbec-3667-aec0-84549498ec8c | -4.54594 | -42.92419 | 2024-12-03 03:44:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 6.2 |
| ed9c9236-a3e6-3b2e-acb0-6c256fab39ad | -3.33671 | -46.05687 | 2024-12-03 03:44:00 | NOAA-21 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 3.0 |
| c3851b02-115e-38b9-9a3f-717ea232db37 | -2.88616 | -45.44857 | 2024-12-03 03:44:00 | NOAA-21 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 71e9455e-22c8-3f1b-9d8c-98a5e72a1a13 | -5.8199 | -46.47301 | 2024-12-03 03:44:00 | NOAA-21 | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 18.2 |
| c5ca972e-d1b7-3e22-bc63-75e8345ced04 | -6.68332 | -46.38092 | 2024-12-03 03:44:00 | NOAA-21 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| bfee3194-ca54-3bb6-b5ba-c542f0f042cf | -10.65099 | -44.49224 | 2024-12-03 03:44:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 7.7 |
| b23e9f01-ebc8-3556-a247-707ca594c228 | -4.16195 | -43.06574 | 2024-12-03 03:44:00 | NOAA-21 | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 16234080-a7ce-3607-b84a-dfb704e454d0 | -5.81823 | -46.48254 | 2024-12-03 03:44:00 | NOAA-21 | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 10.9 |
| 9cc60b53-9c6a-38de-82cc-f9dbc6c0de16 | -5.57355 | -44.88772 | 2024-12-03 03:44:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| ec279505-df26-3300-be53-eecd4f8cbf40 | -3.85075 | -46.51688 | 2024-12-03 03:44:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 3.0 |
| f857622c-cc99-33dd-88ed-0ff9579dd620 | -3.6059 | -45.59953 | 2024-12-03 03:44:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| bccbf89a-6d31-37f0-a232-722c77931be8 | -6.98432 | -43.51434 | 2024-12-03 03:44:00 | NOAA-21 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 43.0 |
| f969d711-9eae-38e9-aa1e-b419eb1eb7a4 | -6.98539 | -43.52179 | 2024-12-03 03:44:00 | NOAA-21 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 38.5 |
| 6f4a4f6f-a874-37f3-a71e-144c3113b653 | -3.46436 | -41.9986 | 2024-12-03 03:44:00 | NOAA-21 | MURICI DOS PORTELAS | PIAUÍ | Brasil | 2206696 | 22 | 33 | nan | nan | nan | Caatinga | 13.4 |
| 0da06922-cc6f-3823-8a91-20aed5d69497 | -5.81046 | -46.49119 | 2024-12-03 03:44:00 | NOAA-21 | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 32569193-0d56-3f49-8dec-5766902fb3aa | -5.79392 | -46.47858 | 2024-12-03 03:44:00 | NOAA-21 | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| a29c6875-2a0e-327d-898d-fc261d943039 | -4.2097 | -44.37151 | 2024-12-03 03:44:00 | NOAA-21 | ALTO ALEGRE DO MARANHÃO | MARANHÃO | Brasil | 2100436 | 21 | 33 | nan | nan | nan | Cerrado | 8.9 |
| 2b553328-9cce-3ad7-91f4-9a80847d9ce3 | -5.80964 | -46.4959 | 2024-12-03 03:44:00 | NOAA-21 | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 9dfc4231-3c00-3b8c-b105-a7e7396c641c | -5.41038 | -42.93109 | 2024-12-03 03:44:00 | NOAA-21 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Caatinga | 6.7 |
| 0b70c2cf-046b-3ccb-9afd-1370fb167cb1 | -3.35497 | -44.36425 | 2024-12-03 03:44:00 | NOAA-21 | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 3b795162-67af-3a5d-b2db-110ffb118830 | -2.88603 | -46.80444 | 2024-12-03 03:44:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| a6e758cc-5878-3e16-8c97-137a7c28c201 | -5.82072 | -46.46833 | 2024-12-03 03:44:00 | NOAA-21 | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 14.4 |
| c9821d47-41b8-3b27-b766-f29b2b3b70a9 | -6.24486 | -35.14882 | 2024-12-03 03:44:00 | NOAA-21 | TIBAU DO SUL | RIO GRANDE DO NORTE | Brasil | 2414209 | 24 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 6ff2957c-c327-35e3-9190-e3e4d0a46de4 | -6.98735 | -43.52617 | 2024-12-03 03:44:00 | NOAA-21 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 37.1 |
| 0f947d79-e915-32fa-91f3-0a68fe42fa9c | -3.37216 | -45.84331 | 2024-12-03 03:44:00 | NOAA-21 | GOVERNADOR NEWTON BELLO | MARANHÃO | Brasil | 2104651 | 21 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 91ef2101-2fcb-32da-aef6-12b909228f85 | -6.03772 | -44.03728 | 2024-12-03 03:44:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 470273fd-fb1a-334c-ac76-977f50ca11e8 | -3.46144 | -42.0019 | 2024-12-03 03:44:00 | NOAA-21 | MURICI DOS PORTELAS | PIAUÍ | Brasil | 2206696 | 22 | 33 | nan | nan | nan | Caatinga | 11.3 |
| d839c1cf-77d3-3c9e-ac96-0f0bcf204db1 | -5.7959 | -46.5028 | 2024-12-03 03:44:00 | NOAA-21 | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| cc10a54e-d54f-3019-90a6-81eef7808034 | -6.9785 | -43.5189 | 2024-12-03 03:44:00 | NOAA-21 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 78f3de26-7611-3b69-92ae-7eb6f761c2b8 | -2.85111 | -45.8352 | 2024-12-03 03:44:00 | NOAA-21 | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 72fcabd2-b09f-39e6-8366-18211df4cd6f | -5.11934 | -43.21981 | 2024-12-03 03:44:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 21.0 |
| 47ed107e-86f3-3c32-a7ad-4e444811978d | -5.79308 | -46.48336 | 2024-12-03 03:44:00 | NOAA-21 | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| f80f2995-5d34-36d5-a490-3010735b8886 | -5.13036 | -44.56379 | 2024-12-03 03:44:00 | NOAA-21 | SÃO JOSÉ DOS BASÍLIOS | MARANHÃO | Brasil | 2111250 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 5516a6c5-8b39-38d3-a4bb-ce42c220efcc | -3.60742 | -45.59082 | 2024-12-03 03:44:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 4.0 |
| ffcc88f9-8186-3294-88da-1238c1433c38 | -4.24658 | -41.92839 | 2024-12-03 03:44:00 | NOAA-21 | PIRIPIRI | PIAUÍ | Brasil | 2208403 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 0e3b05c5-cb23-32fc-b2ad-91d7afc1e2c8 | -5.80004 | -46.47937 | 2024-12-03 03:44:00 | NOAA-21 | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 37.5 |
| e0586bdc-a8b9-3de9-ac8a-050d2e53a95d | -6.00396 | -45.41618 | 2024-12-03 03:44:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| c2ad9672-e02d-3657-8cf5-9f69d84a7570 | -5.39046 | -42.96035 | 2024-12-03 03:44:00 | NOAA-21 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Caatinga | 3.6 |
| 063ea3d2-807e-33b4-8e47-07e8b9737793 | -5.27529 | -45.45247 | 2024-12-03 03:44:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 2064f5de-de77-336b-bae5-06dd32356649 | -4.74043 | -45.70931 | 2024-12-03 03:44:00 | NOAA-21 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 3.0 |
| e36f94a0-65e6-3e68-b37b-40caad51da19 | -5.54253 | -43.89844 | 2024-12-03 03:44:00 | NOAA-21 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 4b15c636-346c-3528-8f4e-9da64106a6c8 | -4.73969 | -45.7136 | 2024-12-03 03:44:00 | NOAA-21 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 3ac1f33d-e6b0-362a-b8c0-ad476332dddb | -6.97944 | -43.51343 | 2024-12-03 03:44:00 | NOAA-21 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 12.1 |
| 69903c38-dc7b-3e25-9250-64885447be98 | -3.33745 | -46.05256 | 2024-12-03 03:44:00 | NOAA-21 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 2d81eeb9-1be2-319e-b9fd-ec9387a5a656 | -5.45404 | -43.58208 | 2024-12-03 03:44:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| c7ba8aef-4268-3b7b-8600-cbce627f292a | -7.56795 | -45.73224 | 2024-12-03 03:44:00 | NOAA-21 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 7b8a1c89-40d2-387e-9a64-88f7abf7f832 | -9.6477 | -42.16665 | 2024-12-03 03:44:00 | NOAA-21 | REMANSO | BAHIA | Brasil | 2926004 | 29 | 33 | nan | nan | nan | Caatinga | 3.2 |
| 869bb648-31a2-3ae9-812d-1c574fe62805 | -3.95091 | -41.49138 | 2024-12-03 03:44:00 | NOAA-21 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 8178037d-5050-3491-87c9-b178a97cd9f9 | -5.29981 | -35.47318 | 2024-12-03 03:44:00 | NOAA-21 | TOUROS | RIO GRANDE DO NORTE | Brasil | 2414407 | 24 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| d6146136-e64d-3189-8efc-f1e868f07a08 | -5.79668 | -46.49841 | 2024-12-03 03:44:00 | NOAA-21 | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 0e3b74b7-7932-32ea-b2bf-5f17c7270500 | -3.85695 | -46.51833 | 2024-12-03 03:44:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 54659377-f09e-30cd-aef0-41707587863d | -8.11598 | -41.18529 | 2024-12-03 03:44:00 | NOAA-21 | PAULISTANA | PIAUÍ | Brasil | 2207801 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| dcedc8dc-9dde-3751-b488-42d834840ce4 | -5.80681 | -46.48306 | 2024-12-03 03:44:00 | NOAA-21 | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 19.0 |
| f8a2683d-246c-38c0-9e67-bfbd90cbe079 | -6.99029 | -43.52264 | 2024-12-03 03:44:00 | NOAA-21 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 25.7 |
| 83bc4287-b5b0-3b45-8e42-d900ce9f268d | -3.97121 | -46.62774 | 2024-12-03 03:44:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 5256e20a-7ee6-313a-a1d1-d42a7859eb4a | -6.98051 | -43.52088 | 2024-12-03 03:44:00 | NOAA-21 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 38.5 |
| 4add734d-e576-30ac-86b7-aa8d20897ced | -5.79748 | -46.49385 | 2024-12-03 03:44:00 | NOAA-21 | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 6.6 |


[Clique aqui para ver as próximas entradas](README23.md)
