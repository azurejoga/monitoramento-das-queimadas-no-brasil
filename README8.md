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

## Dados Diários - Página 8

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| e0704706-6f7c-3503-a282-f4a89fc598bc | -22.7038 | -47.267 | 2025-07-19 02:40:00 | GOES-19 | AMERICANA | SÃO PAULO | Brasil | 3501608 | 35 | 33 | nan | nan | nan | Cerrado | 50.6 |
| b1c2c476-f461-34d3-9e0c-db2510545980 | -5.6567 | -43.7161 | 2025-07-19 02:40:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 140.7 |
| d6ee0075-f327-360a-8d4d-6f2ca5da06ef | -2.9109 | -48.2325 | 2025-07-19 02:40:00 | GOES-19 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 66.1 |
| aad29884-98a6-3d71-a7d6-52bffe0f9e01 | -7.492 | -47.5134 | 2025-07-19 02:40:00 | GOES-19 | BARRA DO OURO | TOCANTINS | Brasil | 1703073 | 17 | 33 | nan | nan | nan | Cerrado | 50.1 |
| 64e7d4c2-fc13-3bab-b693-3038ef4abf97 | -11.7317 | -48.1849 | 2025-07-19 02:40:00 | GOES-19 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 194.3 |
| 41709722-24e0-3bee-b027-e2ed25249bbc | -11.7313 | -48.207 | 2025-07-19 02:40:00 | GOES-19 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 97.6 |
| b2e9fd29-f2ba-3d75-901c-c59b58f79ab9 | -2.9108 | -48.254 | 2025-07-19 02:40:00 | GOES-19 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 84.4 |
| 2b95db9d-8ea1-3ffb-9c4e-1814bc94e232 | -4.301 | -48.1133 | 2025-07-19 02:40:00 | GOES-19 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 82.9 |
| a032c345-a0e2-359d-93cf-3b8de5291268 | -3.1384 | -47.0068 | 2025-07-19 02:40:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 52.7 |
| a21eeaff-7814-3e2f-8d59-64dbc5714f81 | -3.1384 | -47.0068 | 2025-07-19 02:50:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 56.1 |
| 264ee1c8-ee40-36e4-8e89-2286f889378d | -15.8955 | -43.4523 | 2025-07-19 02:50:00 | GOES-19 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 50.4 |
| a9eda882-02af-3913-9b28-03378afe88ef | -2.9109 | -48.2325 | 2025-07-19 02:50:00 | GOES-19 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 64.5 |
| e223fe5a-15f6-3c68-8a4f-45191a5808a0 | -4.301 | -48.1133 | 2025-07-19 02:50:00 | GOES-19 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 73.9 |
| 7e871b61-cfc2-34c9-a9c6-27961a700334 | -5.6567 | -43.7161 | 2025-07-19 02:50:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 153.4 |
| 868bed1c-23fc-38ca-9d6a-a92e8c1d8a47 | -11.7313 | -48.207 | 2025-07-19 02:50:00 | GOES-19 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 77.4 |
| 450fb4c1-cd0d-3f4a-a092-62aca7f838f9 | -11.7317 | -48.1849 | 2025-07-19 02:50:00 | GOES-19 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 204.9 |
| 6b797efe-41ed-3210-abd3-cfb693d8067f | -2.9108 | -48.254 | 2025-07-19 02:50:00 | GOES-19 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 89.9 |
| dd0b0f33-e757-3747-b6d9-8663d7c1b5da | -4.3196 | -48.1125 | 2025-07-19 02:50:00 | GOES-19 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 80.9 |
| 6756a35a-33e6-3e13-b825-4bc91f84a977 | -6.1606 | -48.0507 | 2025-07-19 02:50:00 | GOES-19 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 62.6 |
| 2ec27b4c-f617-35ff-996a-d5783803294e | -11.7508 | -48.1825 | 2025-07-19 02:50:00 | GOES-19 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 54.7 |
| 012f966a-a5ce-354d-9dc1-baa814fa09dc | -6.1481 | -47.331 | 2025-07-19 03:00:00 | GOES-19 | CAMPESTRE DO MARANHÃO | MARANHÃO | Brasil | 2102556 | 21 | 33 | nan | nan | nan | Cerrado | 49.3 |
| 72aef1db-6ca7-3e8b-a548-4782e345ec19 | -6.1483 | -47.3091 | 2025-07-19 03:00:00 | GOES-19 | CAMPESTRE DO MARANHÃO | MARANHÃO | Brasil | 2102556 | 21 | 33 | nan | nan | nan | Cerrado | 55.1 |
| bbb2e909-f325-3c21-86c7-6cf567e094ea | -15.8955 | -43.4523 | 2025-07-19 03:00:00 | GOES-19 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 61.0 |
| 96c6782c-3aca-32f9-a9ae-302d7b3d6bbb | -5.6567 | -43.7161 | 2025-07-19 03:00:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 139.2 |
| a99544a9-18a2-3ceb-8d61-a2f76559f423 | -3.1384 | -47.0068 | 2025-07-19 03:00:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 47.3 |
| 95ec404c-c719-3cf6-a206-feaeba287bfe | -2.9108 | -48.254 | 2025-07-19 03:00:00 | GOES-19 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 72.0 |
| be0dea70-a32a-31f7-b5c0-77a4f13916d9 | -2.9109 | -48.2325 | 2025-07-19 03:00:00 | GOES-19 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 59.8 |
| 071c17e3-8551-3054-b429-ac9a10305c16 | -4.3196 | -48.1125 | 2025-07-19 03:00:00 | GOES-19 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 71.3 |
| 2cda3239-d216-306d-b5d7-1e798775b09b | -6.1606 | -48.0507 | 2025-07-19 03:00:00 | GOES-19 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 55.9 |
| 6f1a2039-a7ed-3bc2-b1f2-bd3f931a3161 | -4.301 | -48.1133 | 2025-07-19 03:00:00 | GOES-19 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 58.1 |
| 55b52a42-ac59-3187-aba7-c0cf1936619b | -11.7313 | -48.207 | 2025-07-19 03:00:00 | GOES-19 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 90.9 |
| 326d9921-3967-3751-8be7-e540b6960a95 | -5.6379 | -43.7175 | 2025-07-19 03:00:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 55.4 |
| 6a80eb78-ccb1-387c-9db6-b744f998fd28 | -11.7317 | -48.1849 | 2025-07-19 03:00:00 | GOES-19 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 162.6 |
| a45e08d6-aae3-31b4-b6f1-0c2d4ad91e44 | -5.6567 | -43.7161 | 2025-07-19 03:10:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 147.8 |
| ce41ea8e-4f07-3450-a125-466165c860c9 | -4.301 | -48.1133 | 2025-07-19 03:10:00 | GOES-19 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 76.3 |
| fe18f08f-3e90-3ae4-920b-224aae4b0322 | -2.9109 | -48.2325 | 2025-07-19 03:10:00 | GOES-19 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 60.8 |
| f406b797-3c41-326d-b9e4-23c4984b3595 | -19.5573 | -48.2572 | 2025-07-19 03:10:00 | GOES-19 | VERÍSSIMO | MINAS GERAIS | Brasil | 3171105 | 31 | 33 | nan | nan | nan | Cerrado | 54.1 |
| 9939d9f0-4382-3b00-a86d-602b52bd4cef | -15.8955 | -43.4523 | 2025-07-19 03:10:00 | GOES-19 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 60.9 |
| 4bdc51aa-1583-3206-8cba-495aeaac7a52 | -11.7317 | -48.1849 | 2025-07-19 03:10:00 | GOES-19 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 190.7 |
| 58145739-d231-3973-a20a-6ba3d8850553 | -11.7313 | -48.207 | 2025-07-19 03:10:00 | GOES-19 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 74.5 |
| 67e2dbdb-9185-369d-9b43-98c9f569a816 | -2.9108 | -48.254 | 2025-07-19 03:10:00 | GOES-19 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 84.5 |
| 0652b468-c995-3d7b-829d-1aaa2a26dd9b | -3.1384 | -47.0068 | 2025-07-19 03:10:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 51.3 |
| 942826a5-2ceb-33b6-a4b3-a810acbb3573 | -4.3196 | -48.1125 | 2025-07-19 03:10:00 | GOES-19 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 49.0 |
| 7ed25dac-afc7-3cdc-a907-232a23854a52 | -6.40702 | -35.33329 | 2025-07-19 03:15:00 | NOAA-20 | NOVA CRUZ | RIO GRANDE DO NORTE | Brasil | 2408300 | 24 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 1888775e-d6a8-3da9-9319-6b058774c86e | -4.91342 | -37.48598 | 2025-07-19 03:15:00 | NOAA-20 | BARAÚNA | RIO GRANDE DO NORTE | Brasil | 2401453 | 24 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 25ed8e49-cdb3-3ea6-8c53-ebf5b2bd4d60 | -9.04529 | -40.57418 | 2025-07-19 03:15:00 | NOAA-20 | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 9d41836e-017f-3434-a9a2-42085034891e | -4.91289 | -37.48915 | 2025-07-19 03:15:00 | NOAA-20 | BARAÚNA | RIO GRANDE DO NORTE | Brasil | 2401453 | 24 | 33 | nan | nan | nan | Caatinga | 1.5 |
| f80f0173-97bf-3734-9d82-10bc06ad66c0 | -4.66279 | -41.96271 | 2025-07-19 03:15:00 | NOAA-20 | COCAL DE TELHA | PIAUÍ | Brasil | 2202711 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| d4e2ecca-bf04-38ba-b82b-077a5c984f7a | -7.21572 | -35.78169 | 2025-07-19 03:15:00 | NOAA-20 | MASSARANDUBA | PARAÍBA | Brasil | 2509206 | 25 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 501edb89-9dc6-3b2d-bf3f-2f88c36f616c | -3.06269 | -40.04389 | 2025-07-19 03:15:00 | NOAA-20 | ACARAÚ | CEARÁ | Brasil | 2300200 | 23 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 13559d97-e01b-3a92-9a03-57266bf40e65 | -4.66394 | -41.95612 | 2025-07-19 03:15:00 | NOAA-20 | COCAL DE TELHA | PIAUÍ | Brasil | 2202711 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 17a2be51-7565-3826-947b-2c7f9f0b604b | -4.91363 | -37.48636 | 2025-07-19 03:15:00 | NOAA-20 | BARAÚNA | RIO GRANDE DO NORTE | Brasil | 2401453 | 24 | 33 | nan | nan | nan | Caatinga | 2.9 |
| e87b6828-139c-3315-8b6a-8406a72ef5c9 | -3.0618 | -40.04903 | 2025-07-19 03:15:00 | NOAA-20 | ACARAÚ | CEARÁ | Brasil | 2300200 | 23 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 4b46323f-73ea-391f-87ba-b714b4b28e1e | -4.66298 | -41.95789 | 2025-07-19 03:15:00 | NOAA-20 | COCAL DE TELHA | PIAUÍ | Brasil | 2202711 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 7a403835-2cc4-354d-a744-d6705aa7bf05 | -4.66992 | -41.95906 | 2025-07-19 03:15:00 | NOAA-20 | COCAL DE TELHA | PIAUÍ | Brasil | 2202711 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| dcc44b1c-d72d-3cd3-9ff3-8a348089ba9a | -11.40835 | -42.0765 | 2025-07-19 03:17:00 | NOAA-20 | UIBAÍ | BAHIA | Brasil | 2932408 | 29 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 499e6a94-c02b-3190-8fcb-3f032ec97795 | -15.89064 | -43.4592 | 2025-07-19 03:19:00 | NOAA-20 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 16.5 |
| ad9be505-a888-3018-a441-2719b3f8823f | -16.21881 | -41.79102 | 2025-07-19 03:19:00 | NOAA-20 | COMERCINHO | MINAS GERAIS | Brasil | 3117009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 97c63ae9-9594-3e27-bd10-b652c2e879fd | -15.92515 | -43.51237 | 2025-07-19 03:19:00 | NOAA-20 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 30fb5328-d11e-34c2-b337-10fe05f70cbd | -15.924 | -43.51768 | 2025-07-19 03:19:00 | NOAA-20 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 6.0 |
| bfa90ec9-2f4d-3c2f-87a6-4a606c0b3f6e | -15.89805 | -43.45534 | 2025-07-19 03:19:00 | NOAA-20 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 16.5 |
| 1ee0450b-4218-3f17-8bb5-c6cd60e1c1c6 | -15.8918 | -43.4539 | 2025-07-19 03:19:00 | NOAA-20 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 16.5 |
| c5cabfa4-6788-3a11-b51b-7d3429f649c7 | -16.22456 | -41.79168 | 2025-07-19 03:19:00 | NOAA-20 | COMERCINHO | MINAS GERAIS | Brasil | 3117009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 364db15b-5a63-3442-b7f6-57caf87bdde2 | -16.04224 | -43.72424 | 2025-07-19 03:19:00 | NOAA-20 | SÃO JOÃO DA PONTE | MINAS GERAIS | Brasil | 3162401 | 31 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 479372f4-5cd4-3361-b604-b9bb03e13d14 | -15.89689 | -43.46065 | 2025-07-19 03:19:00 | NOAA-20 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 16.5 |
| d2a978cd-82e4-3bbc-b298-b48459932f65 | -20.87429 | -43.06356 | 2025-07-19 03:19:00 | NOAA-20 | SENADOR FIRMINO | MINAS GERAIS | Brasil | 3165701 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| c16c0160-a5ea-3ee0-a996-e2d48810a5b7 | -15.88948 | -43.46451 | 2025-07-19 03:19:00 | NOAA-20 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 18.2 |
| 01537738-a21b-3663-b819-3b196e01077b | -2.9108 | -48.254 | 2025-07-19 03:20:00 | GOES-19 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 85.6 |
| 67e882d6-dac0-3388-9c55-f881753336cc | -5.6567 | -43.7161 | 2025-07-19 03:20:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 138.4 |
| f4354738-4fbe-3fdd-8c0c-0fc87c76ee50 | -2.9109 | -48.2325 | 2025-07-19 03:20:00 | GOES-19 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 55.9 |
| 8d324956-97b4-3e2b-ac4c-51130d2ce187 | -11.7313 | -48.207 | 2025-07-19 03:20:00 | GOES-19 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 73.4 |
| 2618ed4e-51a5-3df5-b998-5c8b4e55ff76 | -4.301 | -48.1133 | 2025-07-19 03:20:00 | GOES-19 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 65.7 |
| cf800129-4a83-3b1a-b746-3974d5496e90 | -15.8955 | -43.4523 | 2025-07-19 03:20:00 | GOES-19 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 53.2 |
| b95587d6-7dea-3941-8a06-6a9cba8dbc35 | -11.7317 | -48.1849 | 2025-07-19 03:20:00 | GOES-19 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 181.9 |
| 2fe582b8-28be-34f3-a370-af38569c49c4 | -3.1384 | -47.0068 | 2025-07-19 03:20:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 49.6 |
| 4914d5c8-2f86-3780-8c3e-d896ecfb2a89 | -23.47865 | -45.37232 | 2025-07-19 03:21:00 | NOAA-20 | NATIVIDADE DA SERRA | SÃO PAULO | Brasil | 3532306 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 180b36bc-138f-309c-b953-e11042f3ed9b | -22.83474 | -46.84267 | 2025-07-19 03:21:00 | NOAA-20 | PEDREIRA | SÃO PAULO | Brasil | 3537107 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| 52eb2c6e-414c-3fa8-8344-39d6f5b924fe | -22.83324 | -46.84864 | 2025-07-19 03:21:00 | NOAA-20 | PEDREIRA | SÃO PAULO | Brasil | 3537107 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| 206afae6-b9d5-3ac2-81d6-95722c7f9827 | -22.74621 | -44.75501 | 2025-07-19 03:21:00 | NOAA-20 | SILVEIRAS | SÃO PAULO | Brasil | 3552007 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 13600f81-c83c-32a8-9724-785ef9e4d172 | -25.97202 | -48.95316 | 2025-07-19 03:21:00 | NOAA-20 | GUARATUBA | PARANÁ | Brasil | 4109609 | 41 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| 2a2c77ab-c414-3bbe-9076-bbe248a64a99 | -22.70207 | -47.25418 | 2025-07-19 03:21:00 | NOAA-20 | AMERICANA | SÃO PAULO | Brasil | 3501608 | 35 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 0815104e-828a-3271-90b8-54afeed71153 | -22.69363 | -47.2589 | 2025-07-19 03:21:00 | NOAA-20 | AMERICANA | SÃO PAULO | Brasil | 3501608 | 35 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 8208ae26-d42c-3f79-8ef2-854be35c392b | -22.69527 | -47.2525 | 2025-07-19 03:21:00 | NOAA-20 | AMERICANA | SÃO PAULO | Brasil | 3501608 | 35 | 33 | nan | nan | nan | Cerrado | 2.7 |
| de23296a-47a1-3098-928a-36f3a1d4b3bd | -23.48488 | -45.37304 | 2025-07-19 03:21:00 | NOAA-20 | NATIVIDADE DA SERRA | SÃO PAULO | Brasil | 3532306 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| d78b1768-9c65-30d4-992a-513d42c27881 | -25.9703 | -48.95947 | 2025-07-19 03:21:00 | NOAA-20 | TIJUCAS DO SUL | PARANÁ | Brasil | 4127601 | 41 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| 600a8b03-12b3-33e5-ab6e-a169135a3a44 | -27.68238 | -48.75372 | 2025-07-19 03:21:00 | NOAA-20 | SANTO AMARO DA IMPERATRIZ | SANTA CATARINA | Brasil | 4215703 | 42 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 8e428b9e-4a32-3ce1-8513-59d115feb7cb | -2.9109 | -48.2325 | 2025-07-19 03:30:00 | GOES-19 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 61.0 |
| 1c11128c-ba2a-3ce9-b5b6-18d42bd7a3e9 | -11.7317 | -48.1849 | 2025-07-19 03:30:00 | GOES-19 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 152.3 |
| 48799e79-e528-333a-8af9-d62da1f18d37 | -19.5776 | -48.2528 | 2025-07-19 03:30:00 | GOES-19 | VERÍSSIMO | MINAS GERAIS | Brasil | 3171105 | 31 | 33 | nan | nan | nan | Cerrado | 47.4 |
| d08e55b8-b9c9-3daf-af4c-6d92f0c26267 | -5.6567 | -43.7161 | 2025-07-19 03:30:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 128.1 |
| c5474df2-aab7-3c6f-a377-cdb6a4b0c711 | -2.9108 | -48.254 | 2025-07-19 03:30:00 | GOES-19 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 70.3 |
| 5e4c4479-a73c-3062-9c46-096837127eea | -11.7313 | -48.207 | 2025-07-19 03:30:00 | GOES-19 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 79.6 |
| e617b193-6e31-3fd2-995a-f42c83b838eb | -15.8955 | -43.4523 | 2025-07-19 03:30:00 | GOES-19 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 52.1 |
| afa9b85c-0368-3e61-90ae-d52667652e3c | -3.1384 | -47.0068 | 2025-07-19 03:40:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 48.4 |
| b00711e0-2d6c-338a-9926-06b23539dc41 | -5.6567 | -43.7161 | 2025-07-19 03:40:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 91.4 |
| 1ab788e3-3458-33e7-b0fe-992d0a6755fa | -11.7317 | -48.1849 | 2025-07-19 03:40:00 | GOES-19 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 157.8 |
| a143357c-2591-3d2a-ab31-5bf7bbfda439 | -2.9108 | -48.254 | 2025-07-19 03:40:00 | GOES-19 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 85.3 |
| 493b27e2-9d1b-370a-a3ef-1fe432d01953 | -11.7313 | -48.207 | 2025-07-19 03:40:00 | GOES-19 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 61.7 |
| 92799cc4-d906-3452-bf7d-0e35af025e2f | -15.8955 | -43.4523 | 2025-07-19 03:40:00 | GOES-19 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 81.5 |
| 84adeee6-5670-3c10-af8c-dcb977faf738 | -2.9109 | -48.2325 | 2025-07-19 03:40:00 | GOES-19 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 61.2 |


[Clique aqui para ver as próximas entradas](README9.md)
