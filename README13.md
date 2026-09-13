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

## Dados Diários - Página 13

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 9c3437ee-a5a5-30ab-9c2c-a4d4fe173d9f | -7.0122 | -44.6143 | 2026-09-13 01:05:00 | METOP-C | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| a2d15c8b-26e2-3077-983b-d4a8fd904be5 | -6.9516 | -59.750301 | 2026-09-13 01:05:00 | METOP-C | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| d8d560bd-e401-338c-a7ca-fde359ef9137 | -3.2262 | -50.586601 | 2026-09-13 01:05:00 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5d3e79f8-bec3-3dbf-88c9-bf695b7f38b9 | -6.7912 | -48.6637 | 2026-09-13 01:05:00 | METOP-C | ARAGOMINAS | TOCANTINS | Brasil | 1701309 | 17 | 33 | nan | nan | nan | Amazônia | nan |
| 7299379f-895b-315d-ae6a-4fd7dc03c3c7 | -6.6712 | -58.710899 | 2026-09-13 01:05:00 | METOP-C | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 557b4991-de1a-32c7-a068-327f549bddb5 | -6.1077 | -57.659599 | 2026-09-13 01:05:00 | METOP-C | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 372705e2-d374-38d0-8036-b8c2b93d009f | -15.0169 | -48.490898 | 2026-09-13 01:05:00 | METOP-C | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 485caebb-6855-3e68-bfb4-e7680d4035b2 | -10.5438 | -51.377499 | 2026-09-13 01:05:00 | METOP-C | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| c74b5fc1-dc9f-3d26-a799-209fe73e5e28 | -6.2136 | -55.2621 | 2026-09-13 01:05:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9fe92c1b-c39f-34ee-83d5-18d2d8d25f5e | -3.3547 | -58.188301 | 2026-09-13 01:05:00 | METOP-C | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 9bd444ac-957a-3230-b28e-c4e9bae779de | -3.4103 | -48.892899 | 2026-09-13 01:05:00 | METOP-C | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3b559097-90d0-3a34-a7ae-dd3b6a299e71 | -10.534 | -51.379799 | 2026-09-13 01:05:00 | METOP-C | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 77d0bce7-19d9-3e03-a4f1-7d8b584352e3 | -8.0603 | -54.859501 | 2026-09-13 01:05:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| bac1d4ed-558d-37d4-9d63-51e170b0c7c0 | -1.4662 | -52.971199 | 2026-09-13 01:05:00 | METOP-C | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6db59ec1-49bc-3725-8956-d7769b1f7047 | -9.3999 | -50.097099 | 2026-09-13 01:05:00 | METOP-C | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ad592e4b-0ac4-3b8a-8ad7-ca24fe708b2d | -15.5802 | -53.7948 | 2026-09-13 01:05:00 | METOP-C | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 33c985b2-e16e-3dd2-a179-33e4af73fd11 | -10.904 | -47.810501 | 2026-09-13 01:05:00 | METOP-C | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 3a3da8db-924c-3a8f-b3ae-435e9115940c | -6.8546 | -55.585999 | 2026-09-13 01:05:00 | METOP-C | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 20da5890-6143-35f9-8ccc-a830a414f680 | -1.6566 | -55.181499 | 2026-09-13 01:05:00 | METOP-C | CURUÁ | PARÁ | Brasil | 1502855 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 539896b5-5c73-312c-bc67-a318d63eaa13 | -6.2321 | -51.7033 | 2026-09-13 01:05:00 | METOP-C | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 77427f37-dcf8-3c7d-b446-145a0cb30b0c | -10.9399 | -47.9128 | 2026-09-13 01:05:00 | METOP-C | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| cedca8e2-bd7a-350b-8919-2313e4d7a1ca | -3.8305 | -59.200001 | 2026-09-13 01:05:00 | METOP-C | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 1488d918-d578-325d-a0b7-913067897b9c | -6.8514 | -55.572201 | 2026-09-13 01:05:00 | METOP-C | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ee65c061-9eb4-3c7f-8cfb-be4f87c84af6 | -6.7918 | -58.791801 | 2026-09-13 01:05:00 | METOP-C | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| fcc1fe1d-abd7-31fb-bfb4-108db49d1c63 | -6.3404 | -57.871601 | 2026-09-13 01:05:00 | METOP-C | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 61a91050-f89a-3100-8f07-59cf206af6fe | -10.9448 | -57.1759 | 2026-09-13 01:05:00 | METOP-C | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| f4264018-3319-3a7b-8493-40d67ce79060 | -10.7315 | -54.002499 | 2026-09-13 01:05:00 | METOP-C | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| e6012ea9-b392-3ea6-918b-ddb11d28ac3d | -6.385 | -55.245098 | 2026-09-13 01:05:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e69c2246-f1b2-3a7c-98c2-693db211423b | -3.9089 | -55.7365 | 2026-09-13 01:05:00 | METOP-C | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| fd0ba8e1-ed35-37f5-af65-b70307ad6f11 | -10.6848 | -54.1595 | 2026-09-13 01:05:00 | METOP-C | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 69dcd54b-a477-3661-877e-12ce178a13f9 | -2.9794 | -57.218102 | 2026-09-13 01:05:00 | METOP-C | BARREIRINHA | AMAZONAS | Brasil | 1300508 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| c3c01438-0980-3cdb-ac9c-6c3be94fe9a5 | -5.7868 | -53.812801 | 2026-09-13 01:05:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c2671961-8667-3e35-941e-5e5b8479fd14 | -15.0293 | -48.498901 | 2026-09-13 01:05:00 | METOP-C | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| aa1a235b-fc1f-314d-92ab-8be148e4996c | -6.5997 | -58.851601 | 2026-09-13 01:05:00 | METOP-C | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 4a6228f6-c14d-3729-9004-7c1dc1a11cdc | -2.669 | -57.529499 | 2026-09-13 01:05:00 | METOP-C | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 086c6055-7247-30bc-9e03-9f29cf06cc4a | -15.6397 | -43.3307 | 2026-09-13 01:05:00 | METOP-C | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Caatinga | nan |
| 8fbf62b2-1459-31d7-aaf2-e692623ec9c3 | -10.6895 | -54.180302 | 2026-09-13 01:05:00 | METOP-C | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| c83f0ec0-5c51-3b47-b7f1-b0e401eec20e | -10.5672 | -51.3456 | 2026-09-13 01:05:00 | METOP-C | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| c61cff66-5172-3037-b24d-894da8fbab96 | -6.1933 | -57.719898 | 2026-09-13 01:05:00 | METOP-C | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a619bbfc-4075-3110-a5cc-6603cae79ebe | -6.131 | -57.717701 | 2026-09-13 01:05:00 | METOP-C | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| fa3cf256-e0ad-3c97-a79a-fdbe2e69fadc | -10.9465 | -57.183899 | 2026-09-13 01:05:00 | METOP-C | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 4aad92af-d9e0-3310-b5e1-b6c3c4b2124a | -7.8656 | -54.73 | 2026-09-13 01:05:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7131f613-362c-3d24-90c7-162e5aa289ee | -12.6673 | -54.7253 | 2026-09-13 01:05:00 | METOP-C | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 5ead1e91-8ddc-3af5-a426-610e72be2862 | -6.1111 | -57.674599 | 2026-09-13 01:05:00 | METOP-C | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e4f5ad48-ac3a-3cab-9e47-f3d39d173022 | -5.4868 | -57.233601 | 2026-09-13 01:05:00 | METOP-C | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 007e4fac-2977-3726-8a60-da17c5427d38 | -11.3323 | -48.533298 | 2026-09-13 01:05:00 | METOP-C | BREJINHO DE NAZARÉ | TOCANTINS | Brasil | 1703701 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 75bfd1d2-0bce-390e-8348-665146b01d35 | -9.6693 | -47.995701 | 2026-09-13 01:05:00 | METOP-C | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 8114708d-a30f-347b-a767-95c8e6c168c9 | -10.9073 | -47.8237 | 2026-09-13 01:05:00 | METOP-C | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| aaa2e20a-3520-3512-8f3d-fc101dd15aef | -6.134 | -57.685299 | 2026-09-13 01:05:00 | METOP-C | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e10d7d08-0c0f-3f7e-ae58-1cd4e491e435 | -1.1919 | -55.717701 | 2026-09-13 01:05:00 | METOP-C | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0841ccde-d829-3918-970f-82f014440534 | -10.6434 | -46.0919 | 2026-09-13 01:05:00 | METOP-C | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 5366b25a-77c2-3d5f-9aa5-5a14c37ee6b5 | -14.829 | -48.152 | 2026-09-13 01:05:00 | METOP-C | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| e7da098a-d3c8-3b2a-8480-289230ee56d2 | -10.6381 | -46.111801 | 2026-09-13 01:05:00 | METOP-C | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 127e6da4-16e0-375c-b928-f6942c74f753 | -7.0283 | -44.637001 | 2026-09-13 01:05:00 | METOP-C | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 0c89e310-629b-3af8-b795-e9d744ac11f1 | -7.8625 | -54.716202 | 2026-09-13 01:05:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b05eee9c-593a-39bf-8c6a-ea15d2d8fece | -6.2398 | -51.692101 | 2026-09-13 01:05:00 | METOP-C | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c9426099-7d4d-3f71-a6e4-af070c846370 | -7.6364 | -45.976601 | 2026-09-13 01:05:00 | METOP-C | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 979a0a05-2d67-343c-8c45-17cf1abf9b94 | -10.5418 | -51.369202 | 2026-09-13 01:05:00 | METOP-C | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| ea357cde-84b3-3ffe-b8cc-304304ca5e2c | -7.4729 | -46.143398 | 2026-09-13 01:05:00 | METOP-C | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 8fe927cc-34bf-3b28-b0e6-560f619b8179 | -2.6706 | -57.536598 | 2026-09-13 01:05:00 | METOP-C | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| b928cfe0-6c43-30f3-bd36-6d985f262632 | -5.1153 | -55.9613 | 2026-09-13 01:05:00 | METOP-C | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| fd009f74-b462-39d8-a7c0-b03d59f68020 | -8.5395 | -54.700199 | 2026-09-13 01:05:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2aee196c-11fe-3a40-ae28-8cae339fbd78 | -9.5573 | -51.356998 | 2026-09-13 01:05:00 | METOP-C | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 54a808f6-2e1d-38a6-b7d4-26880b44c52e | -6.9494 | -59.740501 | 2026-09-13 01:05:00 | METOP-C | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 5af5f269-216b-3f97-aff9-3116c23d659e | -6.7432 | -55.639801 | 2026-09-13 01:05:00 | METOP-C | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ad224e96-9012-3b82-bb94-f18b462bead4 | -6.1916 | -57.712299 | 2026-09-13 01:05:00 | METOP-C | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| aaacd64e-e745-3355-8081-9bd0145c7ba4 | -6.853 | -55.579102 | 2026-09-13 01:05:00 | METOP-C | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f52fa384-fd3a-3bcc-90e1-a3c7416ee33e | -7.8691 | -54.7001 | 2026-09-13 01:05:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a88a066a-b50a-39cc-9e94-449e88880d3c | -8.5426 | -54.713902 | 2026-09-13 01:05:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 65ecab19-8ac5-3677-9f3a-22f12e4dd4d4 | -6.6582 | -58.883999 | 2026-09-13 01:05:00 | METOP-C | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| d08cb8fd-71a5-3d20-9747-f7dbdc8c1c4b | -15.5704 | -53.7971 | 2026-09-13 01:05:00 | METOP-C | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| fc7d913b-0bfc-3741-8c7d-08c8ab161665 | -6.1293 | -57.710201 | 2026-09-13 01:05:00 | METOP-C | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 46961f8d-e090-38a2-a470-c5ba7949d4e7 | -15.554 | -53.815899 | 2026-09-13 01:05:00 | METOP-C | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| dc28b7c0-4222-3d9d-9955-a4b7ac03b6da | -7.1893 | -45.874901 | 2026-09-13 01:05:00 | METOP-C | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 8281e662-3a40-36ff-a4b6-ad7b1e79d11b | -5.3203 | -57.135101 | 2026-09-13 01:05:00 | METOP-C | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d6a28c01-15fc-354f-8c7b-772f97f66d1d | -3.5765 | -53.003601 | 2026-09-13 01:05:00 | METOP-C | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 26f01569-52cf-3902-8aec-d88b817be258 | -1.1935 | -55.724602 | 2026-09-13 01:05:00 | METOP-C | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b2260a13-70ba-3f91-98c4-21ead70d6456 | -2.9544 | -50.3937 | 2026-09-13 01:05:00 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 75fd3426-4288-3406-a9d3-b44a2c5bccf0 | -3.7269 | -61.7603 | 2026-09-13 01:05:00 | METOP-C | ANORI | AMAZONAS | Brasil | 1300102 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 845da4ad-4af2-3f17-a450-d69effd36bfb | -6.721 | -50.462101 | 2026-09-13 01:05:00 | METOP-C | ÁGUA AZUL DO NORTE | PARÁ | Brasil | 1500347 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 23221985-48be-3d38-b4c6-bf8740b98d1f | -9.7083 | -54.353901 | 2026-09-13 01:05:00 | METOP-C | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 4737232a-d0aa-35b9-8714-c9d7d7160a46 | -11.2506 | -54.153702 | 2026-09-13 01:05:00 | METOP-C | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| ade0f653-aaec-3db8-bd2e-baad4f472e71 | -15.0467 | -48.5275 | 2026-09-13 01:05:00 | METOP-C | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 5cf443f3-41ac-304b-a954-6a7e3b15182c | -8.5379 | -54.693298 | 2026-09-13 01:05:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 43f33ead-399b-3f04-b05a-127a13ff240d | -5.9758 | -57.7598 | 2026-09-13 01:05:00 | METOP-C | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ed9e36bb-be69-3375-917c-2805698e1e18 | -12.4939 | -48.047501 | 2026-09-13 01:05:00 | METOP-C | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| fb647c5a-5488-3692-b95b-542bf4a4e0d6 | -5.9694 | -57.7771 | 2026-09-13 01:05:00 | METOP-C | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2f1f5c60-29d3-39d1-bb32-4457e23c22f7 | -4.9296 | -45.8209 | 2026-09-13 01:05:00 | METOP-C | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 2d759066-62ac-3193-9300-923da4cdc043 | -3.3908 | -50.760201 | 2026-09-13 01:05:00 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 121e588f-c240-36b0-9787-d80053782714 | -10.9483 | -57.191898 | 2026-09-13 01:05:00 | METOP-C | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 9111f56b-2903-35f5-80d1-c97207b4c768 | -9.679 | -47.993198 | 2026-09-13 01:05:00 | METOP-C | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 59a6997f-eae9-3966-a103-59d2b1a8e804 | -3.5956 | -59.070801 | 2026-09-13 01:05:00 | METOP-C | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 2ac2ca00-ccc7-3872-870d-d39732c256df | -7.8577 | -54.695499 | 2026-09-13 01:05:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c2e85cf4-6308-3f72-bec7-de2c471b95c6 | -10.6478 | -46.109299 | 2026-09-13 01:05:00 | METOP-C | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| e32c3ba7-793b-3018-8345-f339bc50245b | -6.7416 | -55.6329 | 2026-09-13 01:05:00 | METOP-C | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8bfbfddb-2460-3259-ab0d-cf814037d5b0 | -12.8643 | -44.3969 | 2026-09-13 01:05:00 | METOP-C | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 6cc55618-3581-3b1e-83ba-64943ad459b8 | -8.1179 | -54.795799 | 2026-09-13 01:05:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a2522694-ece8-3a44-a982-9d90193312b2 | -10.2922 | -55.065399 | 2026-09-13 01:05:00 | METOP-C | TERRA NOVA DO NORTE | MATO GROSSO | Brasil | 5108055 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 70b94f3c-5a33-3c20-8b89-ca40952544a0 | -6.8499 | -55.565399 | 2026-09-13 01:05:00 | METOP-C | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2d853fea-faf9-3b04-8c3c-a446d6d972d6 | -11.2475 | -54.139801 | 2026-09-13 01:05:00 | METOP-C | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |


[Clique aqui para ver as próximas entradas](README14.md)
