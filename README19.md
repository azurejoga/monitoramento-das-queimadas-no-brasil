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

## Dados Diários - Página 19

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 84e402fa-8b1d-3607-8661-5637b8ddec8f | -2.95453 | -50.40361 | 2026-09-12 04:32:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 20.8 |
| 958369c3-1b33-3a00-bd7e-cb4f6819f338 | -4.80812 | -42.88741 | 2026-09-12 04:32:00 | NOAA-21 | UNIÃO | PIAUÍ | Brasil | 2211100 | 22 | 33 | nan | nan | nan | Cerrado | 9.1 |
| b05a8926-e232-31fc-a304-38146eb1835a | -3.22572 | -46.95714 | 2026-09-12 04:32:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 5bda72b2-20c5-3b90-9696-0e9d39348af9 | -4.27415 | -46.53731 | 2026-09-12 04:32:00 | NOAA-21 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1ac165a9-c03d-3f5e-ac27-b9de49188069 | -3.23064 | -46.94732 | 2026-09-12 04:32:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 24.9 |
| d38a4452-766c-34bc-92ac-a305cae90ca9 | -2.7319 | -57.6412 | 2026-09-12 04:32:00 | NOAA-21 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 07b02f34-05af-328f-bcf2-216955b816ae | -4.96134 | -45.14838 | 2026-09-12 04:32:00 | NOAA-21 | LAGO DA PEDRA | MARANHÃO | Brasil | 2105708 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 5e283cdf-7bfb-311d-b786-ed831e98013d | -3.2334 | -46.95127 | 2026-09-12 04:32:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 7.4 |
| 1dd927b4-80da-376d-aab8-7159f9c0c2e3 | -3.87327 | -51.18195 | 2026-09-12 04:32:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 668c791f-a6ac-3424-974c-3c14074bafec | -3.23233 | -46.95816 | 2026-09-12 04:32:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| e2aa075a-e9a8-3e15-a098-9f32c3788c77 | -4.08601 | -49.49323 | 2026-09-12 04:32:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a6942544-582d-3557-b1c2-eca6be01055f | -2.96144 | -50.38349 | 2026-09-12 04:32:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 05e73449-7d6a-33ae-8cbe-0be3d89e5ef5 | -2.9496 | -50.41134 | 2026-09-12 04:32:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 46.4 |
| e38552aa-8baf-3f4c-bdf1-fc6a811aa583 | -4.36614 | -47.7807 | 2026-09-12 04:32:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 18.6 |
| df4af809-3afd-39ec-901a-b8335162df38 | -6.12843 | -43.73258 | 2026-09-12 04:32:00 | NOAA-21 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 5f514c53-1fda-3530-93c4-6abedd5b58be | 2.51522 | -50.85688 | 2026-09-12 04:32:00 | NOAA-21 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 1.9 |
| fd18fad9-2e77-3f32-8e0c-5fc322373da9 | -2.95783 | -50.38293 | 2026-09-12 04:32:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| fe18e4eb-bccc-3462-be40-b6564f9fa6b7 | -3.85811 | -49.22352 | 2026-09-12 04:32:00 | NOAA-21 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 9075c9f5-d48e-3172-b0e2-4dc4951de8f1 | -3.23617 | -46.95522 | 2026-09-12 04:32:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 7.4 |
| 5aa88e93-2ba9-3a99-a78a-659e0b736509 | -2.94571 | -50.38949 | 2026-09-12 04:32:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| b73e799f-6ce3-3c8e-ae6c-ceb1292f805e | -5.77302 | -45.0952 | 2026-09-12 04:32:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 43.8 |
| c63799b4-5cd9-3b3e-a0a8-33a107f1c412 | -2.9588 | -50.40002 | 2026-09-12 04:32:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 20.8 |
| db5ac53b-edc3-371c-a218-7de8aa712290 | -2.73396 | -49.45551 | 2026-09-12 04:32:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 740802fe-230d-3e13-940f-34f88aff8c0a | -3.38806 | -50.76498 | 2026-09-12 04:32:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 95f142fc-6329-3665-bd97-79454304d019 | -3.87173 | -51.18064 | 2026-09-12 04:32:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d9b8ae0e-99fb-3382-9e14-519480e5be98 | -5.09384 | -42.73713 | 2026-09-12 04:32:00 | NOAA-21 | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| a2505c5c-2e20-3994-b8c5-3a5f759fc562 | -5.12958 | -41.08147 | 2026-09-12 04:32:00 | NOAA-21 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 121d70c5-f2df-3b27-9f36-df3491fea962 | -4.95842 | -45.14391 | 2026-09-12 04:32:00 | NOAA-21 | LAGO DA PEDRA | MARANHÃO | Brasil | 2105708 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d370b797-ad53-36bc-bbbb-dd4da5afc99d | -3.33056 | -42.29874 | 2026-09-12 04:32:00 | NOAA-21 | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 9f7d4fca-4946-3e2e-a3cd-6a7eeb5ac3d4 | -2.72359 | -57.61982 | 2026-09-12 04:32:00 | NOAA-21 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b45b4aea-0e7f-38ab-bc7d-2df1dc7ea21c | -2.60913 | -47.74846 | 2026-09-12 04:32:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d13778aa-a5b0-3a86-9afe-9e7adefc8ae4 | -2.71845 | -57.6148 | 2026-09-12 04:32:00 | NOAA-21 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 3.4 |
| a2fd44ae-8d7b-3da5-8b50-c2eb64e9f396 | -5.76948 | -45.09464 | 2026-09-12 04:32:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 43.8 |
| b1296d02-98ec-32db-a00b-4320e9b632b5 | -2.95814 | -50.40416 | 2026-09-12 04:32:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 20.8 |
| 5c26b305-2353-31ad-8bf3-c834aa998029 | -2.94865 | -50.3942 | 2026-09-12 04:32:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| d75d2190-82d5-3748-882f-a2076d54747b | -2.96896 | -50.40584 | 2026-09-12 04:32:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 30.2 |
| 54fd2cac-d77e-3398-a763-79a2de5a8272 | -2.71725 | -57.62202 | 2026-09-12 04:32:00 | NOAA-21 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 3.0 |
| d7965c49-6eb9-3899-8721-131b294fb9a3 | -2.96043 | -50.41301 | 2026-09-12 04:32:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 138.0 |
| 28b56ee1-d716-331d-8e8f-353e4595c01d | -5.12509 | -41.08069 | 2026-09-12 04:32:00 | NOAA-21 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 267e7cb7-456b-3e4b-86fa-def3296e3e42 | -2.95225 | -50.39478 | 2026-09-12 04:32:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 8e486dda-8aa5-39a9-9755-950019406b60 | -6.29109 | -41.69818 | 2026-09-12 04:32:00 | NOAA-21 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 0e7820e8-657d-3924-a491-c75e9d59f0a0 | -2.96667 | -50.39698 | 2026-09-12 04:32:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 33.1 |
| 195dc494-4f77-35f3-b4eb-4c85060b691f | -2.71712 | -57.62297 | 2026-09-12 04:32:00 | NOAA-21 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 7cbb20c2-86a7-37e0-80c9-73cd5dd849a2 | -3.73801 | -40.42438 | 2026-09-12 04:32:00 | NOAA-21 | SOBRAL | CEARÁ | Brasil | 2312908 | 23 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 3e6baf8d-3115-33b7-a365-8d9c3597abd4 | -2.95423 | -50.38237 | 2026-09-12 04:32:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 5aff67ee-4022-3e5b-97b9-f292c92b606f | -1.72715 | -57.15368 | 2026-09-12 04:32:00 | NOAA-21 | FARO | PARÁ | Brasil | 1503002 | 15 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 1c88aab6-d437-34d9-9d8c-a1f8e2ad22f7 | -1.77259 | -54.94962 | 2026-09-12 04:32:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 1a761c71-12e0-330f-982b-4f6c52ddefb0 | -1.45275 | -45.7423 | 2026-09-12 04:32:00 | NOAA-21 | CÂNDIDO MENDES | MARANHÃO | Brasil | 2102606 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1078a07a-2464-3f65-9581-7a670de5743a | -3.158 | -48.60864 | 2026-09-12 04:32:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 7.5 |
| cce7b6c0-6d11-3f1c-b8fc-5a1b685e8062 | -5.75888 | -45.09293 | 2026-09-12 04:32:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 7e7584d5-044a-3007-84bc-65c013f8ac93 | -6.27606 | -41.95131 | 2026-09-12 04:32:00 | NOAA-21 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| e40b0f3e-b20c-3db3-bc9d-9306c30a80dc | -2.72541 | -57.64538 | 2026-09-12 04:32:00 | NOAA-21 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| d1faf95c-ad76-39ef-baa0-94a5b717900a | -3.3821 | -50.75523 | 2026-09-12 04:32:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| baad3e5c-6d96-3eb3-ac5f-9486688eebfe | -5.76888 | -45.0986 | 2026-09-12 04:32:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 25.0 |
| 1e1315f9-97d7-3830-9cd6-3198afbfaba7 | -5.77362 | -45.09123 | 2026-09-12 04:32:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 43.8 |
| 5b8317e6-1d0a-35e1-ae83-1d5c0e4d907c | -4.28191 | -46.53136 | 2026-09-12 04:32:00 | NOAA-21 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 5.1 |
| ccbebdfd-de86-3615-900c-98777f363cd0 | -5.4785 | -45.12913 | 2026-09-12 04:32:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 4.6 |
| e1f4b7a7-bddf-3a73-b8d0-1c0867ab5381 | -3.32654 | -42.29808 | 2026-09-12 04:32:00 | NOAA-21 | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 748d10fe-2a5c-3257-a639-2f7822f61380 | -3.73269 | -40.42854 | 2026-09-12 04:32:00 | NOAA-21 | SOBRAL | CEARÁ | Brasil | 2312908 | 23 | 33 | nan | nan | nan | Caatinga | 8.4 |
| c74ed308-f429-3b09-8bbe-3566846af78c | -2.96403 | -50.41358 | 2026-09-12 04:32:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 138.0 |
| f2996062-4d44-30b0-9234-f2857b9caf3a | -2.73051 | -57.6494 | 2026-09-12 04:32:00 | NOAA-21 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 06073957-21dc-3f94-a0fa-8369b6600cc7 | -3.74969 | -42.47593 | 2026-09-12 04:32:00 | NOAA-21 | LUZILÂNDIA | PIAUÍ | Brasil | 2205805 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 3a4a4635-c69c-31e7-9a16-c4a3c21b3a99 | -5.59379 | -45.81023 | 2026-09-12 04:32:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| cfb6a325-657f-38f4-9cd2-9c2765b7e498 | -2.94618 | -50.47913 | 2026-09-12 04:32:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| c2d14d8e-0f59-38f7-8f40-005430841793 | -2.94438 | -50.39777 | 2026-09-12 04:32:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| ee3365dc-e38b-3e5b-b4c6-b4d4d344e87a | -2.58359 | -54.61916 | 2026-09-12 04:32:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| bf1ab805-d272-38dd-9fb7-d83989772666 | -2.96078 | -50.38762 | 2026-09-12 04:32:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 9b74255f-b218-34c0-9de5-b5fd0c93bf5e | -3.40933 | -48.88981 | 2026-09-12 04:32:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| f7d52616-e92e-3d2a-9b04-fab9f74839d2 | -1.72543 | -57.15404 | 2026-09-12 04:32:00 | NOAA-21 | FARO | PARÁ | Brasil | 1503002 | 15 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 16baa66b-c193-30ca-b811-b0f34e5f7ea5 | -2.71779 | -57.61888 | 2026-09-12 04:32:00 | NOAA-21 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 6cb625e5-3f89-3bef-ba1d-552f2276c135 | -2.81479 | -46.71333 | 2026-09-12 04:32:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| fd588cd1-343b-3e8f-b1b5-bd45d4daf423 | -2.96012 | -50.39175 | 2026-09-12 04:32:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 12.5 |
| 9a8370e7-441a-3594-a0ab-0c933892bfee | -5.77008 | -45.09067 | 2026-09-12 04:32:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 43.8 |
| 87d5a0a7-a48b-3f06-8ea8-836aa619cad1 | -1.72648 | -57.15772 | 2026-09-12 04:32:00 | NOAA-21 | FARO | PARÁ | Brasil | 1503002 | 15 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 66523792-a2a4-3b5d-82e0-f1fe91dda335 | -2.02041 | -47.55344 | 2026-09-12 04:32:00 | NOAA-21 | MÃE DO RIO | PARÁ | Brasil | 1504059 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ced2c6d8-82dc-3f48-ae60-05eced325e64 | -5.5538 | -43.43238 | 2026-09-12 04:32:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| a34f24a1-a5e8-3129-82b0-26b9312d474f | -3.7334 | -40.42374 | 2026-09-12 04:32:00 | NOAA-21 | SOBRAL | CEARÁ | Brasil | 2312908 | 23 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 526411df-35e1-3af0-a554-aaaecaa08e3b | -2.72609 | -57.64027 | 2026-09-12 04:32:00 | NOAA-21 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 57bd0728-ec92-3a78-88ac-0b0ea11aff4e | -2.93733 | -50.46488 | 2026-09-12 04:32:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e5ba30c6-8275-394a-8a22-703345141dd1 | -2.72747 | -57.63208 | 2026-09-12 04:32:00 | NOAA-21 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 6a46b649-db7c-37ec-bab7-d2d9875dda2a | -3.23394 | -46.94782 | 2026-09-12 04:32:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 11.9 |
| b8e9d265-1295-3580-b375-55d6c007b3fe | -2.95616 | -50.4166 | 2026-09-12 04:32:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 10.8 |
| 3374959a-1e57-3cb2-adcc-6d7e475c9b8f | -3.07365 | -51.33331 | 2026-09-12 04:32:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7bf6ba52-1e96-39e4-b1a8-8bc701eb6e82 | -2.72678 | -57.63617 | 2026-09-12 04:32:00 | NOAA-21 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 6ed128e1-6960-374f-865c-ea554355b54d | -3.89174 | -55.8186 | 2026-09-12 04:32:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 129ac5ab-6e4b-331b-9dc2-ce7241c19e0f | -5.63301 | -43.54944 | 2026-09-12 04:32:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 6fbeed1b-4b65-303d-805c-70d66cd43344 | -2.94028 | -50.46963 | 2026-09-12 04:32:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 82fb9637-8ff7-31b2-9883-9988b5df1305 | -2.25921 | -47.00703 | 2026-09-12 04:32:00 | NOAA-21 | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 7ea34958-82d5-3338-affa-5f8499f2559c | -4.2747 | -46.53381 | 2026-09-12 04:32:00 | NOAA-21 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2ad6ae65-e26c-3a79-a9dd-3d02e20c4df9 | -3.36747 | -50.75298 | 2026-09-12 04:32:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5d47b7b8-4451-3e30-8d42-fe594efbb8ad | -3.09801 | -48.68337 | 2026-09-12 04:32:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f7b75f76-a91a-3257-9321-1e10e7bec3d2 | -3.08418 | -47.75539 | 2026-09-12 04:32:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 303d0898-f9df-384b-bbe1-0d8bee11a59d | -2.95682 | -50.41245 | 2026-09-12 04:32:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 36.1 |
| 70bcd3a3-76d4-311d-ab4c-89e2dde531e7 | -5.48261 | -45.12574 | 2026-09-12 04:32:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| e96e8f63-d1e2-3dae-b2d3-e650758ec03a | -4.73414 | -45.67566 | 2026-09-12 04:32:00 | NOAA-21 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c5f271f6-2813-32d2-82de-760352f6f174 | -3.86334 | -49.21732 | 2026-09-12 04:32:00 | NOAA-21 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d3c715bc-202f-3831-85f2-51fd5fbe0c10 | -4.73071 | -45.67516 | 2026-09-12 04:32:00 | NOAA-21 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d53670e3-cb5f-39b7-b663-5cd5f1519ab6 | -3.95625 | -47.6177 | 2026-09-12 04:32:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 8150d49b-0166-3c01-a101-7e62846f82a7 | -2.94144 | -50.39306 | 2026-09-12 04:32:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| d119adc6-294a-3110-8851-440b83fd36d3 | -5.47837 | -45.12635 | 2026-09-12 04:32:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |


[Clique aqui para ver as próximas entradas](README20.md)
