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

## Dados Diários - Página 10

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 8d9d101d-8248-3880-822e-92f2497208e5 | -9.7133 | -57.887299 | 2026-09-03 01:12:00 | METOP-C | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 260be85c-8c1e-3cb0-a503-1203d7a40cc7 | -9.622 | -48.557999 | 2026-09-03 01:12:00 | METOP-C | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 71805a72-540e-34a8-a17d-e03616778c4b | -6.6554 | -59.445702 | 2026-09-03 01:12:00 | METOP-C | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| f99e9d42-be83-399e-806b-c20008c18016 | -7.0564 | -59.214699 | 2026-09-03 01:12:00 | METOP-C | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 750feaf7-c637-36d2-8a7f-d76d2b287ff8 | -8.4601 | -54.746101 | 2026-09-03 01:12:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e588ea80-0f0f-35aa-aec4-9f55a556c16c | -6.3251 | -56.042599 | 2026-09-03 01:12:00 | METOP-C | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4a76ddc7-de31-3825-8940-bdf8a043574f | -4.1208 | -51.020401 | 2026-09-03 01:12:00 | METOP-C | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e06aeb23-edc9-3688-8628-27b176988011 | -6.4281 | -58.298199 | 2026-09-03 01:12:00 | METOP-C | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 7792994d-a098-3da6-981c-86ee2cde21cf | -9.0441 | -65.720497 | 2026-09-03 01:12:00 | METOP-C | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 2077736d-78e2-3cd5-ba3d-0c5c072e58f1 | -5.2765 | -60.178699 | 2026-09-03 01:12:00 | METOP-C | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| ed0a10b4-b71c-3950-9260-083ff8d2d98e | -4.9579 | -55.797798 | 2026-09-03 01:12:00 | METOP-C | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d3a50789-7f70-3156-9488-7285c95704a7 | -5.4862 | -60.058498 | 2026-09-03 01:12:00 | METOP-C | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 4cb4e030-5e24-31b7-99fd-5a4c88dc5a05 | -3.1363 | -61.227501 | 2026-09-03 01:12:00 | METOP-C | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| c841a629-26ee-3435-b684-79904a0bc452 | -10.3724 | -49.941601 | 2026-09-03 01:12:00 | METOP-C | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 0eb4604c-6821-3a79-8723-d282a32b074d | -8.4881 | -54.6451 | 2026-09-03 01:12:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 469147d3-164c-308d-9dd2-7818eb21c57e | -7.3416 | -55.129501 | 2026-09-03 01:12:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1cb06f44-f254-356c-9f87-01b14a20945c | -9.0343 | -65.722397 | 2026-09-03 01:12:00 | METOP-C | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| bafe9990-5210-3789-b949-9392d93457b5 | -6.7747 | -59.427399 | 2026-09-03 01:12:00 | METOP-C | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 79b60173-0ced-36f2-8d67-4f7641f485c6 | -5.5981 | -60.191299 | 2026-09-03 01:12:00 | METOP-C | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 27f1356e-3e8f-360b-8c6c-abb449cf18e5 | -10.918 | -45.3414 | 2026-09-03 01:12:00 | METOP-C | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 41798ebf-c72a-3086-a8bc-f6d0263c65e7 | -18.1485 | -51.817799 | 2026-09-03 01:12:00 | METOP-C | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 316bb8ae-d7de-3f37-9927-39f37aeb04d5 | -5.1748 | -60.2757 | 2026-09-03 01:12:00 | METOP-C | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 69ff1188-773a-3ad7-9e01-8e9ee3c70916 | -18.1583 | -51.8153 | 2026-09-03 01:12:00 | METOP-C | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 5f538be9-59bd-3f90-b9c1-8546c58b3e23 | -6.3381 | -56.054401 | 2026-09-03 01:12:00 | METOP-C | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e0167976-5f52-31fc-9b47-8c81dc99b132 | -6.3924 | -58.276798 | 2026-09-03 01:12:00 | METOP-C | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 81ddbc55-88d0-32f1-9562-25a521d535fd | -4.9828 | -55.8606 | 2026-09-03 01:12:00 | METOP-C | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c5760716-bbad-32c8-a3ca-db79133ca6d1 | -3.2185 | -61.227001 | 2026-09-03 01:12:00 | METOP-C | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| b4eb8361-54f7-3464-8d28-dd860d50f518 | -8.4766 | -54.6399 | 2026-09-03 01:12:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| fa2413e7-8290-36ab-a391-b5dfae8cd767 | -5.3398 | -60.139999 | 2026-09-03 01:12:00 | METOP-C | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 4dadc041-8469-35f5-8ff9-0ddc4de4faab | -8.4755 | -54.679699 | 2026-09-03 01:12:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 00e99176-a2e1-3af3-918a-db78cc95c535 | -7.633 | -57.612202 | 2026-09-03 01:12:00 | METOP-C | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5c02c9f5-7b5f-3c94-99a2-e28c6072bbbb | -10.6542 | -61.7607 | 2026-09-03 01:12:00 | METOP-C | JI-PARANÁ | RONDÔNIA | Brasil | 1100122 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 2baf8db6-3e75-3463-8c68-adef0d584c82 | -6.3826 | -58.278999 | 2026-09-03 01:12:00 | METOP-C | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| d060392d-4550-39bd-8d3f-be148a1e7c2b | -6.6537 | -59.438099 | 2026-09-03 01:12:00 | METOP-C | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| d6938c09-ed3b-3c9b-9164-ed005f766569 | -8.153 | -54.934299 | 2026-09-03 01:12:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 795ad6d3-e0a0-3b1d-bdcf-c2dfbbad17ac | -4.426 | -55.772999 | 2026-09-03 01:12:00 | METOP-C | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 22a62439-e4c9-3a1c-bbc4-a42c733ae57f | -18.1759 | -51.8022 | 2026-09-03 01:12:00 | METOP-C | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| c1860bfb-99f8-3f8e-93d1-69e63833dd99 | -4.9926 | -55.858398 | 2026-09-03 01:12:00 | METOP-C | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 37dd6e57-a946-3232-9dc1-6c2538a8b629 | -5.7796 | -53.3992 | 2026-09-03 01:12:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4a9bf181-cd92-3551-a895-faaf1a783b8d | -22.444401 | -49.7663 | 2026-09-03 01:12:00 | METOP-C | ALVINLÂNDIA | SÃO PAULO | Brasil | 3501509 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| ad340612-de37-3380-868c-e68551f10ef8 | -18.1544 | -51.799099 | 2026-09-03 01:12:00 | METOP-C | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 9223afcb-907b-3e02-8fe2-f7284a622065 | -4.991 | -55.8512 | 2026-09-03 01:12:00 | METOP-C | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 151fb696-ab62-3304-b215-e6a93b55676f | -11.0084 | -45.064701 | 2026-09-03 01:12:00 | METOP-C | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 2618f6d8-581a-3a3d-8c67-9c32d05d5d52 | -6.274 | -55.421001 | 2026-09-03 01:12:00 | METOP-C | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5fc0addd-df40-3222-8bbd-98a6ef5900ce | -6.6926 | -59.934799 | 2026-09-03 01:12:00 | METOP-C | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 6aa1a3e5-457d-3aa3-8680-564dbc61c52f | -4.1338 | -51.0317 | 2026-09-03 01:12:00 | METOP-C | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 37796de8-1c2b-38fb-9feb-3a5f7643504f | -5.5961 | -61.472801 | 2026-09-03 01:12:00 | METOP-C | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 58a12f7d-3189-3056-afbe-3fc8621005da | -6.7568 | -59.439301 | 2026-09-03 01:12:00 | METOP-C | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 7f906c40-58eb-321b-93d1-d1d623cdd1f1 | -8.4497 | -54.701401 | 2026-09-03 01:12:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f8ac6ed5-ce25-3403-b426-f535fccb7612 | -6.699 | -58.768299 | 2026-09-03 01:12:00 | METOP-C | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 40d6b14c-3e66-3911-83f6-48780b9d3609 | -11.006 | -45.0938 | 2026-09-03 01:12:00 | METOP-C | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 41717e95-1b94-3f5a-837a-3d24b54038e9 | -8.4462 | -54.686501 | 2026-09-03 01:12:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ae89e89a-5825-33e5-995f-876300acb5c5 | -6.6859 | -58.756001 | 2026-09-03 01:12:00 | METOP-C | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 5c9c15dd-11b6-359a-8dd5-c7a7309d6721 | -18.8389 | -47.584801 | 2026-09-03 01:12:00 | METOP-C | ROMARIA | MINAS GERAIS | Brasil | 3156403 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 36d9f0e3-00cb-330a-a082-88c77fc93503 | -9.7117 | -57.8801 | 2026-09-03 01:12:00 | METOP-C | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 95dd6ff0-a2c7-3710-a893-d33082a52a05 | -18.181801 | -51.783401 | 2026-09-03 01:12:00 | METOP-C | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 0094eae2-47cd-3d54-83b6-d2cefcd29882 | -3.4017 | -59.355701 | 2026-09-03 01:12:00 | METOP-C | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 63e819e5-a59d-3fc8-9056-efb0fb8a813d | -3.6329 | -60.556499 | 2026-09-03 01:12:00 | METOP-C | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| ad802652-0463-3cfb-a03c-079fcd57484d | -3.3411 | -59.451599 | 2026-09-03 01:12:00 | METOP-C | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 18a8aada-808a-3e23-ae93-046122960c2e | -3.2147 | -61.2103 | 2026-09-03 01:12:00 | METOP-C | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| cf1d3059-d2ca-3541-82e3-b0e8e96b1556 | -10.3756 | -49.954399 | 2026-09-03 01:12:00 | METOP-C | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 3849e251-b9f3-30ef-87b1-82b39c6ed0e6 | -10.1797 | -50.372601 | 2026-09-03 01:12:00 | METOP-C | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 8e506c13-ebcb-3623-879c-74c87953f758 | -8.4783 | -54.6474 | 2026-09-03 01:12:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 62e2ad85-1d82-303e-a83a-b04237930880 | -10.2103 | -50.287701 | 2026-09-03 01:12:00 | METOP-C | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 0c77928a-5f4b-3778-b579-df9cc70b4bce | -6.3728 | -58.281101 | 2026-09-03 01:12:00 | METOP-C | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| a1b60239-4e8f-335d-af71-f108f81849ef | -7.5816 | -57.703899 | 2026-09-03 01:12:00 | METOP-C | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3ff9fe02-1bda-3e0b-83a1-edb906ea89c6 | -6.6892 | -58.7705 | 2026-09-03 01:12:00 | METOP-C | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 8155c6e7-f813-35fc-8972-7ec08a8a659a | -10.217 | -50.2729 | 2026-09-03 01:12:00 | METOP-C | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 3cf20c80-f637-373b-a78c-366294ba7ed0 | -3.6347 | -60.5644 | 2026-09-03 01:12:00 | METOP-C | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 9cb1f601-cd4f-3881-a06d-8d24cc1b1b64 | -6.6404 | -55.221001 | 2026-09-03 01:12:00 | METOP-C | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ef0e5cf2-c593-30c3-9230-82e5d3ec44ac | -8.4417 | -54.711102 | 2026-09-03 01:12:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| cffc62a0-1481-36a4-ae29-de034634ed09 | -8.4836 | -54.669899 | 2026-09-03 01:12:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a1186732-6a7f-3295-a263-856048a47be5 | -9.093 | -65.366699 | 2026-09-03 01:12:00 | METOP-C | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 32f3c071-974c-3b9f-9dfc-fefeae2236a7 | -8.4503 | -54.748402 | 2026-09-03 01:12:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1d5d6653-41f8-3073-8ca5-f2750f46835d | -19.104601 | -57.360199 | 2026-09-03 01:12:00 | METOP-C | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 3bbc8cd8-b252-3c64-a15b-c4a39cbc4fcc | -6.6979 | -59.958698 | 2026-09-03 01:12:00 | METOP-C | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 5ef0ac42-84ef-3b89-a369-2f558da63017 | -14.1585 | -58.875099 | 2026-09-03 01:12:00 | METOP-C | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 852d1dc0-8b27-3d4d-b570-4804fd5da887 | -11.018 | -45.062 | 2026-09-03 01:12:00 | METOP-C | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| ac115512-8c39-3dd0-a4c1-580c1086d259 | -8.4469 | -54.733501 | 2026-09-03 01:12:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| de47b6db-5e1b-33b7-a95a-4225528801f2 | -7.598 | -57.6856 | 2026-09-03 01:12:00 | METOP-C | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 498d6a70-2a0c-3ee7-997a-93dec6502dc9 | -3.6249 | -60.566601 | 2026-09-03 01:12:00 | METOP-C | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 95575002-e668-3967-b2d4-2783d3e25ed8 | -5.2171 | -60.051998 | 2026-09-03 01:12:00 | METOP-C | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 049e1cfc-4d46-35ae-8b11-bc34098f2b2d | -6.7764 | -59.435001 | 2026-09-03 01:12:00 | METOP-C | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 2ebaa8d8-e014-3bc9-8bbe-1469d398dbc9 | -6.3267 | -56.049599 | 2026-09-03 01:12:00 | METOP-C | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| bdd2fce2-bd1d-3a44-8efc-9d930a9221b4 | -6.6438 | -55.235802 | 2026-09-03 01:12:00 | METOP-C | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| bf3ab6b9-0f37-388e-9aa1-017b21706886 | -6.4221 | -58.226101 | 2026-09-03 01:12:00 | METOP-C | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f423a6a4-1655-3c11-92b9-2d56194f7e85 | -7.3603 | -55.210098 | 2026-09-03 01:12:00 | METOP-C | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 097df574-1628-3b06-8839-90ca614849fb | -8.4543 | -54.676701 | 2026-09-03 01:12:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7bceb76e-1672-3069-972d-45ce14914588 | -7.3587 | -55.202801 | 2026-09-03 01:12:00 | METOP-C | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 72a19ed2-1c0f-3658-afe4-89a0b339a20b | -6.6962 | -59.950802 | 2026-09-03 01:12:00 | METOP-C | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| d9915f50-0b88-3824-8fbf-c989a218a883 | -3.4077 | -61.336201 | 2026-09-03 01:12:00 | METOP-C | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| f099a556-9f3f-3abb-abf0-856b3bde4f59 | -10.5403 | -49.993698 | 2026-09-03 01:12:00 | METOP-C | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| f7856202-0c84-3470-865d-9ec0cfbff533 | -3.3967 | -59.424198 | 2026-09-03 01:12:00 | METOP-C | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 1fc13f63-a79d-3485-bd68-bb26e9c6989b | -5.4746 | -60.052799 | 2026-09-03 01:12:00 | METOP-C | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| ba94ef42-3e90-3c8d-9e88-fd134f47e020 | -7.0581 | -59.222198 | 2026-09-03 01:12:00 | METOP-C | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| f5d24367-cf47-3ae1-9390-42dcbd59b733 | -10.9207 | -45.313099 | 2026-09-03 01:12:00 | METOP-C | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 3106cf7c-01ad-328b-9581-b6a3cd78dcfb | -10.5372 | -49.981098 | 2026-09-03 01:12:00 | METOP-C | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 96d05f94-3fe0-3077-bcca-5b897619ac61 | -4.6434 | -55.7313 | 2026-09-03 01:12:00 | METOP-C | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 62f7fb95-f32a-3417-b255-ee89b87e36c7 | -6.3834 | -55.225601 | 2026-09-03 01:12:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 64b0b80b-e319-3187-8eba-3ffb04f91de3 | -6.3365 | -56.047401 | 2026-09-03 01:12:00 | METOP-C | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |


[Clique aqui para ver as próximas entradas](README11.md)
