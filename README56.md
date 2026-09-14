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

## Dados Diários - Página 56

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| cc041d08-8860-3a04-9196-a87e3e602d3a | -6.32349 | -59.98161 | 2026-09-14 05:36:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 5316d79e-4acc-38d6-9e59-cdaead000ac0 | -2.92307 | -50.40203 | 2026-09-14 05:36:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 6caf3fec-31f2-3413-9fd6-24187694ca8a | -3.36476 | -61.28488 | 2026-09-14 05:36:00 | NOAA-21 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 85090581-ed44-3a7c-9e12-37eb116e26d2 | -3.20709 | -61.1246 | 2026-09-14 05:36:00 | NOAA-21 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 82499485-e8f5-39fd-b1b6-e0f94bf7a600 | -3.71826 | -59.29991 | 2026-09-14 05:36:00 | NOAA-21 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| aaf96872-41c0-3089-9136-7a3bc7b6c483 | -6.84886 | -55.56572 | 2026-09-14 05:36:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| b429267a-55c1-306b-9e9b-963507f54238 | -2.90727 | -50.36901 | 2026-09-14 05:36:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 13996448-f7f3-37ab-9ed4-8313c4bf6020 | -3.09365 | -61.19921 | 2026-09-14 05:36:00 | NOAA-21 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 3.1 |
| ba70f2f1-5fb8-300a-84b9-94149c522ac6 | -6.57893 | -58.83782 | 2026-09-14 05:36:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| eb0c48a6-ad50-3dc0-b8c6-7d227881240b | -6.59692 | -58.86163 | 2026-09-14 05:36:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| f99be793-1c3c-3428-8bdf-99411eeead82 | -3.35551 | -59.82984 | 2026-09-14 05:36:00 | NOAA-21 | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 525b6500-3102-3c11-a2c7-d26a01af5dbb | -2.70901 | -57.61774 | 2026-09-14 05:36:00 | NOAA-21 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 3.3 |
| ca9c9a0e-a17c-3908-acd6-b9c3154ff936 | -6.59792 | -58.85455 | 2026-09-14 05:36:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 4c783bf3-dc42-3ee9-af8b-0d77df1727e0 | -5.59291 | -60.18237 | 2026-09-14 05:36:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 05094af7-0b3f-335d-ade7-9d6f46fa2b7a | -3.35617 | -59.3859 | 2026-09-14 05:36:00 | NOAA-21 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 608d7518-7e60-340b-b69e-00b075217fe3 | -2.89351 | -50.44031 | 2026-09-14 05:36:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 9.0 |
| 4ef26a64-62c0-3df3-990b-dfbc0a15bb4c | -6.29015 | -55.28635 | 2026-09-14 05:36:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 21f0dc77-2192-3e44-9fe0-a156693a7cb0 | -5.08304 | -56.25534 | 2026-09-14 05:36:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| bf02b28d-6d53-348a-99b7-572291279bc5 | -4.66929 | -56.00142 | 2026-09-14 05:36:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 3aba5b10-ff34-3958-889e-4f1f0c906075 | -6.11156 | -57.66241 | 2026-09-14 05:36:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 524c40eb-b9a3-31de-bdfb-1cb4b8b287e5 | -4.98286 | -56.13623 | 2026-09-14 05:36:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 3941b4b3-6e2a-3085-b260-685b922c6079 | -6.59351 | -58.85086 | 2026-09-14 05:36:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 9206c7cf-1703-3efe-9f8c-154e40bc1ef8 | -6.59246 | -58.85794 | 2026-09-14 05:36:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 2e0e9f4b-de0c-391a-85dc-aa5d54363306 | -3.37614 | -61.32442 | 2026-09-14 05:36:00 | NOAA-21 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 26f10b93-4f73-3241-8d33-a5bf71250b37 | -6.29195 | -55.27329 | 2026-09-14 05:36:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 3db394ec-9b19-36bb-90cc-20dacc4757d7 | -3.18422 | -61.11346 | 2026-09-14 05:36:00 | NOAA-21 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 64f15b80-4fb7-3533-89d6-bf05f3470e76 | -3.35012 | -58.14384 | 2026-09-14 05:36:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 531c1dd1-3717-3512-ab5a-61ed64389a3f | -3.75841 | -51.14733 | 2026-09-14 05:36:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 10.1 |
| e21f55a5-90b8-3362-aefa-6e5cbb78f9b2 | -2.89567 | -50.38034 | 2026-09-14 05:36:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| d040005c-f7b1-3dae-8168-e4308e7153d4 | -2.88961 | -50.39666 | 2026-09-14 05:36:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 64fa07cc-1342-3e78-abee-86029c5f8163 | -6.29584 | -59.93563 | 2026-09-14 05:36:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| d76ad1be-808e-3313-a545-178580646986 | -2.69948 | -57.5393 | 2026-09-14 05:36:00 | NOAA-21 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 417d2817-7511-3f68-a05e-8afafb1000c2 | -6.74838 | -59.43039 | 2026-09-14 05:36:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| b31e12ab-96bf-3483-b776-6ec65b5e8081 | -6.11467 | -57.67146 | 2026-09-14 05:36:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 775565ce-a350-374b-991e-2cb40e6ae147 | -6.87298 | -55.29433 | 2026-09-14 05:36:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d780416d-2a62-3916-926f-9dca99e17d62 | -3.63127 | -58.63918 | 2026-09-14 05:36:00 | NOAA-21 | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 3718b8b4-90a8-3463-b5a3-a9ef6819e1d0 | -6.28389 | -59.93843 | 2026-09-14 05:36:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ede31b47-b53d-3ff4-bfff-243a72135e51 | -6.58595 | -58.84614 | 2026-09-14 05:36:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| a5ae991e-8ca9-36d6-81d1-8b3677dc0d0c | -4.13166 | -54.0166 | 2026-09-14 05:36:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 8004d72d-872e-3c21-8131-f478de183262 | -6.57788 | -58.84491 | 2026-09-14 05:36:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 95e22a55-49eb-3881-b345-a3312ee81269 | -8.12419 | -54.80672 | 2026-09-14 05:36:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 4857c8ae-de3b-3926-9f10-6b7b1a7631b8 | -2.69028 | -57.57265 | 2026-09-14 05:36:00 | NOAA-21 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e9b3d541-7807-3ffd-a303-d7be23be77ca | -3.09596 | -61.18438 | 2026-09-14 05:36:00 | NOAA-21 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b57a063e-e161-3fed-81be-8d38c52b1c87 | -3.86665 | -51.97658 | 2026-09-14 05:36:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 654e8199-5733-338c-9426-7568348666b7 | -2.50693 | -59.52523 | 2026-09-14 05:36:00 | NOAA-21 | RIO PRETO DA EVA | AMAZONAS | Brasil | 1303569 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a9c688b4-e78f-3cab-b9e8-fd63a855566e | -3.89496 | -60.59272 | 2026-09-14 05:36:00 | NOAA-21 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 316342e6-d5ef-3fbd-bcba-3a5e318bc942 | -6.85013 | -55.56742 | 2026-09-14 05:36:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 41e43b95-a321-392d-bb81-72b0720cb726 | -6.30048 | -55.28733 | 2026-09-14 05:36:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b33c6a55-d265-36a2-ac18-697bb04de243 | -2.88545 | -50.40283 | 2026-09-14 05:36:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 0ab66881-bc10-3eb0-b5c3-80c638606fe3 | -3.53258 | -59.06495 | 2026-09-14 05:36:00 | NOAA-21 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 680a6e97-a0f7-309e-a4c2-cf4a325f7e11 | -4.34789 | -54.78302 | 2026-09-14 05:36:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 8613b7fa-f943-313f-9df0-aed6a1ada591 | -7.87165 | -54.72217 | 2026-09-14 05:36:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 976ca1d7-e721-348b-a715-2a699ae63427 | -3.19512 | -60.50086 | 2026-09-14 05:36:00 | NOAA-21 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a2fd79af-125e-3568-adb1-4a58abf4c944 | -3.13111 | -61.23075 | 2026-09-14 05:36:00 | NOAA-21 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| dccbbc48-9496-31f1-8393-f30aeedcb6fd | -6.29108 | -55.27961 | 2026-09-14 05:36:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b57ab453-7add-367d-9674-992105e6274c | -7.51869 | -55.27885 | 2026-09-14 05:36:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| df03f49a-57b2-389b-8b4c-4e1d7f68362a | -6.58842 | -58.85734 | 2026-09-14 05:36:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 68a9b229-928b-3e42-9a00-018f2772781e | -2.87963 | -50.39594 | 2026-09-14 05:36:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 59ce8596-7d7c-3736-be88-ee056b825a14 | -3.71688 | -57.17836 | 2026-09-14 05:36:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1c255352-aa9e-33bf-9047-6cbf4f1ed815 | -2.67453 | -57.55189 | 2026-09-14 05:36:00 | NOAA-21 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 9d88b7ef-dda4-3c42-93a6-6cf1533dcae5 | -4.39341 | -55.20782 | 2026-09-14 05:36:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| fda66c79-0518-3abb-b51e-0e9c11ea9215 | -5.80694 | -52.11823 | 2026-09-14 05:36:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 9ff07f0c-87b1-3f57-99a2-b74bf1849a6c | -6.15929 | -59.9445 | 2026-09-14 05:36:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 359b36b7-3914-37de-a44e-03792ef0be23 | -3.40289 | -61.30963 | 2026-09-14 05:36:00 | NOAA-21 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 84de0007-84d9-35e2-a4c0-560e7ad37e20 | -6.30136 | -55.28101 | 2026-09-14 05:36:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| fd657f39-9af4-36ce-a30c-59fa0fc3409f | -2.90215 | -50.40466 | 2026-09-14 05:36:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 234b9360-e9b7-3145-9b0c-2749aa8cf24a | -2.88808 | -50.3852 | 2026-09-14 05:36:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 6cbb2e93-6bd0-3ded-9ee9-dbe376fc882c | -2.92549 | -50.43246 | 2026-09-14 05:36:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 50.3 |
| 16772841-2c8d-3d3b-8eef-43ddb4e79f16 | -3.38633 | -50.38863 | 2026-09-14 05:36:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 75bdd64d-8511-35c9-b903-ce97766aa2f8 | -5.1209 | -55.95753 | 2026-09-14 05:36:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 744f1f7d-29aa-3762-b9d4-f45b37433f42 | -6.32621 | -60.01426 | 2026-09-14 05:36:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 3.8 |
| a94b4fea-90c8-33d0-a301-af56f1f38e9c | -6.10481 | -55.6644 | 2026-09-14 05:36:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 502f47a9-ce17-33d2-8b6d-8fe43fc2d23a | -5.84892 | -52.09264 | 2026-09-14 05:36:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 31ccbb1f-619d-39e2-8420-a7a1fa3731e7 | -2.89708 | -50.44001 | 2026-09-14 05:36:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| e61b84d5-0478-3388-89eb-0584fdbc48e7 | -2.9055 | -50.40605 | 2026-09-14 05:36:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 9a9f20e9-3621-3b60-8dfe-c44a87e3675e | -2.92292 | -50.45012 | 2026-09-14 05:36:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 733627ba-a46f-360b-9043-0ec6617ad78d | -2.67783 | -57.57076 | 2026-09-14 05:36:00 | NOAA-21 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 695b4076-a425-39f0-9431-5708213d0874 | -6.10909 | -57.67921 | 2026-09-14 05:36:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 0bdb3eb5-d6c7-3029-96c9-3977395433a7 | -6.29238 | -55.27023 | 2026-09-14 05:36:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| a5232fd6-bdae-330c-aa0b-81e32d37491f | -5.80134 | -52.11251 | 2026-09-14 05:36:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| c7c87c70-47c7-35e4-9ddb-96549504fa4d | -5.84815 | -52.09812 | 2026-09-14 05:36:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| cc215020-3506-379d-ae6a-76ad9296910a | -2.67853 | -57.4983 | 2026-09-14 05:36:00 | NOAA-21 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 3ba6c115-4639-3d8b-841c-da265820ef47 | -2.91045 | -50.44196 | 2026-09-14 05:36:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 22.0 |
| 5f10c55c-212d-3e35-91ce-e433d315e39e | -2.67645 | -57.55124 | 2026-09-14 05:36:00 | NOAA-21 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| eb01268d-ea45-3024-9fd7-21e4c0357dbf | -2.92478 | -50.39019 | 2026-09-14 05:36:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 8ec87f33-6d4a-3f52-933a-4a9557f2275f | -6.32593 | -55.18023 | 2026-09-14 05:36:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 89c32e44-bb21-3060-a4f8-8e09c5592c99 | -6.31431 | -59.96621 | 2026-09-14 05:36:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| bfc540cd-e399-3210-b1b3-94b57a5de842 | -4.13656 | -54.02098 | 2026-09-14 05:36:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| d79dbf9c-e003-31c1-aa0d-6feec62e79f3 | -2.90907 | -50.38238 | 2026-09-14 05:36:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 3561357f-fdd9-3440-b75e-f066bd091f32 | -2.65953 | -57.51093 | 2026-09-14 05:36:00 | NOAA-21 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| a357292f-8a8f-3012-9590-12f0227f8b94 | -6.13514 | -57.69383 | 2026-09-14 05:36:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 9c7ef827-0560-352a-9df6-fc45fbc2f567 | -3.41541 | -58.21067 | 2026-09-14 05:36:00 | NOAA-21 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 4.7 |
| f050fdad-6112-3cf8-9517-45e357013d4f | -2.92067 | -50.3712 | 2026-09-14 05:36:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 04d7c999-b139-3c9c-9b43-fd4338f971b9 | -3.16473 | -58.64697 | 2026-09-14 05:36:00 | NOAA-21 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 7.4 |
| 47a3bfd5-9a6f-3bfa-82b4-2337a212d18f | -3.37572 | -50.39526 | 2026-09-14 05:36:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| a6eaa208-7b1d-3fa9-97d7-6fc1bbd7f27d | -6.09218 | -57.90505 | 2026-09-14 05:36:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f4ebbe70-2f4b-3857-9cb1-bd9fb8ddcc9b | -6.28764 | -59.93901 | 2026-09-14 05:36:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 6.1 |
| baab9b95-8e71-367c-b7b5-2c82488b0ab0 | -6.74448 | -59.42982 | 2026-09-14 05:36:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 2d0e0f27-b344-3e7d-83af-1ee31b11e909 | -2.90386 | -50.3928 | 2026-09-14 05:36:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| e1ab2f11-29b4-38eb-9083-61e5b6137939 | -4.37172 | -55.03649 | 2026-09-14 05:36:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |


[Clique aqui para ver as próximas entradas](README57.md)
