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

## Dados Diários - Página 132

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 5fd55601-edd3-3153-8aef-dcb419437670 | -13.3706 | -43.89455 | 2026-10-10 05:06:00 | NOAA-20 | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 4.0 |
| e8cd1105-2874-3492-b8a4-68792b39aced | -10.49407 | -51.94236 | 2026-10-10 05:06:00 | NOAA-20 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c7998b21-9af7-3e8e-878d-cbec0c3fc757 | -11.95243 | -43.49117 | 2026-10-10 05:06:00 | NOAA-20 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 1385b84f-2a00-3a9e-9f8f-22229090c327 | -8.57742 | -53.10144 | 2026-10-10 05:06:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b49ac18d-6de9-3e13-9a46-d1f74580f158 | -10.61806 | -60.48492 | 2026-10-10 05:06:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7b2814b3-0402-33fc-a866-5d53a918bcc2 | -8.32914 | -54.67301 | 2026-10-10 05:06:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6c63e9bc-3d47-3cf0-88f5-b067a5339837 | -8.20558 | -54.70316 | 2026-10-10 05:06:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 6485eaa4-35b8-3ccb-9eb5-e16a53bdb32f | -13.19932 | -48.13879 | 2026-10-10 05:06:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 24888d5d-8b2f-3c1c-8570-f8958e62c56d | -10.7339 | -52.03664 | 2026-10-10 05:06:00 | NOAA-20 | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| f0fc5540-67a2-372a-8961-03be0c8aab8f | -13.37698 | -43.89537 | 2026-10-10 05:06:00 | NOAA-20 | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 840d02c6-e05e-3d49-a5fd-5cfdbbf6ec55 | -12.09386 | -57.15544 | 2026-10-10 05:06:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ad367dba-90a1-37cd-9452-b42c94bcd234 | -12.29546 | -63.37283 | 2026-10-10 05:06:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 9378aa43-634b-3bbd-abb0-7d0cff828abc | -10.89043 | -44.81623 | 2026-10-10 05:06:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 37d98b5c-984c-3c5b-81f9-edc275adec39 | -15.02562 | -46.2589 | 2026-10-10 05:06:00 | NOAA-20 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 056cb030-8fdd-356c-9cbe-3ea24e8e90d9 | -8.54561 | -54.70022 | 2026-10-10 05:06:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c83d5115-ab90-3c1d-8279-487c75abf3b9 | -8.64654 | -54.53481 | 2026-10-10 05:06:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 66283553-7702-3a64-a1a1-fb656fdbf38c | -13.37636 | -43.9008 | 2026-10-10 05:06:00 | NOAA-20 | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 27f4197d-7a7e-395e-bff1-2d0a10791cf1 | -9.8765 | -50.52014 | 2026-10-10 05:06:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 7fd15af3-655b-3325-a5c3-fa06c5657f2b | -8.62494 | -66.78381 | 2026-10-10 05:06:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 42e76a46-5cf2-38c6-942e-9ab5ab795e83 | -12.37888 | -46.5683 | 2026-10-10 05:06:00 | NOAA-20 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| d70294df-40c3-3400-912b-6ebcd520c9c3 | -10.04441 | -48.21292 | 2026-10-10 05:06:00 | NOAA-20 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 01a6c856-0845-3b7d-b82b-8233fc203a8e | -8.18906 | -54.72187 | 2026-10-10 05:06:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 49d84e1d-017d-3e95-ac6e-6db6cc49f1b4 | -11.77642 | -45.48849 | 2026-10-10 05:06:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 0f0d8a87-8eca-3f73-a41c-740806f76765 | -9.11871 | -45.82007 | 2026-10-10 05:06:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 5d4269df-22e8-3816-8059-3f8bdaf6e9b3 | -12.77878 | -44.8903 | 2026-10-10 05:06:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 47c16cfa-4713-309e-9fb6-67dbd728ce1c | -8.57686 | -53.10514 | 2026-10-10 05:06:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ca137f9a-bce6-3e1b-a064-bc25bf8c54b6 | -8.50192 | -54.61131 | 2026-10-10 05:06:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 596a5c52-1bf0-39a6-b3ca-a9aae530dd37 | -7.91124 | -54.71599 | 2026-10-10 05:06:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 43d54167-4880-339f-aa35-5a4074ce1555 | -11.08201 | -44.10592 | 2026-10-10 05:06:00 | NOAA-20 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 533ab2e9-aff4-3120-8267-01cffe5c789b | -8.5168 | -67.03714 | 2026-10-10 05:06:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 65eb1204-d998-3a18-894d-58a3e6e5f22f | -11.99036 | -57.61546 | 2026-10-10 05:06:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| af5afe86-c844-3739-915b-9eda2ac65503 | -11.57072 | -43.7112 | 2026-10-10 05:06:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 7b640931-708f-36c0-96d4-649cc2d863e3 | -9.51127 | -54.6725 | 2026-10-10 05:06:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 4c29370e-37f7-354d-b4ff-0ea48f9c4c5e | -13.91461 | -47.84527 | 2026-10-10 05:06:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| c10115af-edc5-3c09-be58-03460f140040 | -10.62119 | -53.8628 | 2026-10-10 05:06:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| c1707ba5-4c17-3bc4-8854-68813207a585 | -8.60092 | -55.3152 | 2026-10-10 05:06:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 12e7a1b2-baee-36f6-a146-4b53435f831c | -7.90629 | -54.72586 | 2026-10-10 05:06:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| b07f9138-3a15-3e08-8dff-e8e46e5e5be3 | -9.93723 | -44.88264 | 2026-10-10 05:06:00 | NOAA-20 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 29026f6e-e90e-3fa3-bd7f-09a24c3627f7 | -13.84139 | -49.68266 | 2026-10-10 05:06:00 | NOAA-20 | AMARALINA | GOIÁS | Brasil | 5200829 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| cc22498a-ab5a-3908-a2a5-adfaec9b17c1 | -14.32183 | -44.66611 | 2026-10-10 05:06:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 6c49f721-c345-39f6-8f73-9eb71af8d363 | -9.69517 | -58.08806 | 2026-10-10 05:06:00 | NOAA-20 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 65a48a9d-10c3-3f38-bb94-d590dd41ee99 | -13.51428 | -48.60968 | 2026-10-10 05:06:00 | NOAA-20 | TROMBAS | GOIÁS | Brasil | 5221452 | 52 | 33 | nan | nan | nan | Cerrado | 7.7 |
| f00673ff-6657-3e79-a863-ea8482d06295 | -11.9093 | -46.57238 | 2026-10-10 05:06:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 1be307ad-9b90-36da-8bc3-60209af00d2b | -9.11253 | -45.82559 | 2026-10-10 05:06:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 7463b6c3-8ab9-3978-bb9e-99513c79aa0b | -14.4589 | -43.94847 | 2026-10-10 05:06:00 | NOAA-20 | JUVENÍLIA | MINAS GERAIS | Brasil | 3136959 | 31 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 0d237030-11c9-38b0-86c6-fb33db9fefd6 | -9.28716 | -47.39525 | 2026-10-10 05:06:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 16.0 |
| a53df06b-e6d2-3482-9750-26e086e7d4eb | -11.18678 | -45.32791 | 2026-10-10 05:06:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| ecc4519f-f4ea-367f-a578-b4d34525d1de | -14.89518 | -47.22861 | 2026-10-10 05:06:00 | NOAA-20 | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 230d034f-4884-3f9c-9289-42ed661cf373 | -7.90574 | -54.72933 | 2026-10-10 05:06:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| b93764e7-2544-32a7-a7e8-ac16fd189385 | -9.76 | -53.88207 | 2026-10-10 05:06:00 | NOAA-20 | MATUPÁ | MATO GROSSO | Brasil | 5105606 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 0519ff6e-0652-3da9-b9ce-c1a51c3f261a | -14.53278 | -48.041 | 2026-10-10 05:06:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 86d0b671-50e5-33ea-b0c4-c94a1a617f8d | -12.45097 | -51.39895 | 2026-10-10 05:06:00 | NOAA-20 | BOM JESUS DO ARAGUAIA | MATO GROSSO | Brasil | 5101852 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 100fd632-ec6b-36f4-9f91-6e63ecf63eb7 | -11.56449 | -43.70969 | 2026-10-10 05:06:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 3b89f01b-bb91-3b18-921c-1f1d8365916e | -8.70848 | -62.39088 | 2026-10-10 05:06:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 877bef40-0970-3142-bdce-4f948f84e9fb | -10.24308 | -49.67254 | 2026-10-10 05:06:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| e8f34812-48ab-36f5-a6da-e4137cdb15ec | -11.96084 | -43.48288 | 2026-10-10 05:06:00 | NOAA-20 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 3.5 |
| f56d3dac-98c5-3db4-89a5-3fbc5c8b045d | -10.45565 | -47.83963 | 2026-10-10 05:06:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 567da6a8-b17d-3306-8ae4-7ff1c40e601a | -8.18354 | -54.71387 | 2026-10-10 05:06:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 94dbba8a-949f-3e92-aea3-e777daef36e4 | -11.9532 | -43.48463 | 2026-10-10 05:06:00 | NOAA-20 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a87974fc-b400-3fd2-bf0b-8b83ddbd1286 | -8.64599 | -54.5383 | 2026-10-10 05:06:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a0fda473-27fb-30d2-a781-869c12dda3c9 | -13.1479 | -54.35019 | 2026-10-10 05:06:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 65c5ae93-85f8-3ce1-892c-d4cef5596527 | -14.45646 | -43.96354 | 2026-10-10 05:06:00 | NOAA-20 | JUVENÍLIA | MINAS GERAIS | Brasil | 3136959 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 2c64f751-4585-3d26-b3ac-b041e4021434 | -10.88765 | -44.79489 | 2026-10-10 05:06:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 4313ed05-cc7b-35a6-b608-d95e99df80fd | -11.08167 | -44.10853 | 2026-10-10 05:06:00 | NOAA-20 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 556ebb97-5f6a-3eb7-809b-96d654af55b1 | -11.56502 | -43.70514 | 2026-10-10 05:06:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| d5901d96-a28d-310d-988c-40b534f91017 | -7.57063 | -61.54318 | 2026-10-10 05:06:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| dbb7572f-2611-3f8b-9e40-1bf24ec68bb3 | -11.37534 | -54.03547 | 2026-10-10 05:06:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2f84ce4f-4421-36a9-a2b2-e0aeb4896c56 | -8.69067 | -62.40881 | 2026-10-10 05:06:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 6fa839d6-5266-3001-af85-aaa421e8b0f1 | -11.76276 | -43.52888 | 2026-10-10 05:06:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| ff3abd05-aec1-325b-a80a-b7be869bf4b3 | -7.56076 | -61.54398 | 2026-10-10 05:06:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 1bf2d10f-f7f7-3e78-928d-6378085e1606 | -10.45965 | -47.84569 | 2026-10-10 05:06:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 0c2cd29f-f4b4-3092-b86d-1b66cab13152 | -13.77422 | -48.12519 | 2026-10-10 05:06:00 | NOAA-20 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 078e51d6-b5e8-300f-a164-c5096f9c5053 | -11.79379 | -46.72298 | 2026-10-10 05:06:00 | NOAA-20 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 0de9d456-1911-3d7d-9c79-b574a25a6fe7 | -11.20142 | -49.93967 | 2026-10-10 05:06:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 5674e331-b496-3701-9771-11d2971f694b | -12.37843 | -46.61581 | 2026-10-10 05:06:00 | NOAA-20 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| f0bccde3-1c4b-3998-a61d-014aedc2cd64 | -7.88809 | -54.7123 | 2026-10-10 05:06:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ee80065b-01c8-3ed5-9aec-080cd3af948b | -13.7729 | -48.13591 | 2026-10-10 05:06:00 | NOAA-20 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 17e11f7e-e075-3af8-b07f-e2daa63af500 | -9.12448 | -45.81761 | 2026-10-10 05:06:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 56411420-4302-337b-bdde-d894ae235359 | -7.88754 | -54.71577 | 2026-10-10 05:06:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 7d80c16b-135c-36ef-afde-94cf0ee2acf8 | -9.51513 | -54.66956 | 2026-10-10 05:06:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 97d86420-2ac1-389d-af31-566ad02c20c2 | -14.71856 | -48.23187 | 2026-10-10 05:06:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 916fac2b-5079-3962-b188-a5e2ba721a45 | -11.79471 | -46.72022 | 2026-10-10 05:06:00 | NOAA-20 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 96da4e69-bd6f-3c41-98bc-4ad923388524 | -11.36915 | -54.03075 | 2026-10-10 05:06:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 0c375ba9-68bd-35a7-9e6e-5f2d420132d8 | -9.95974 | -55.33784 | 2026-10-10 05:06:00 | NOAA-20 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| ccddf982-0427-3e44-a7ca-33ca91a80c40 | -9.92534 | -44.78739 | 2026-10-10 05:06:00 | NOAA-20 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 45725dd6-b1b3-35ed-9611-b98fe7fd9a3f | -13.20415 | -48.13946 | 2026-10-10 05:06:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| b34abc26-e36c-3523-b5a0-6b7a24c53c2e | -11.38613 | -47.58406 | 2026-10-10 05:06:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b375ae11-e703-3431-9844-a98f8fb8e96e | -7.92118 | -54.7389 | 2026-10-10 05:06:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 16a394ea-9fce-3212-b985-25e5bd272362 | -7.57066 | -61.54094 | 2026-10-10 05:06:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 0b6a8cc3-15ed-347c-97f5-0f0f99f694ff | -7.91014 | -54.72293 | 2026-10-10 05:06:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| f3ca1afd-d0b4-308d-800d-76b7bc302747 | -11.38455 | -55.15615 | 2026-10-10 05:06:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 05270591-fbed-3849-be31-1c7173c9b2aa | -7.9129 | -54.72692 | 2026-10-10 05:06:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| ce8f1e89-068a-32eb-85de-ecab47dd6f49 | -13.16426 | -54.31096 | 2026-10-10 05:06:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d9e96cfb-c282-30e2-ad23-0dcffd670c28 | -14.45766 | -43.95265 | 2026-10-10 05:06:00 | NOAA-20 | JUVENÍLIA | MINAS GERAIS | Brasil | 3136959 | 31 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 856bd67b-2713-39ff-ac35-c43f393169f8 | -12.47052 | -54.49983 | 2026-10-10 05:06:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 0f51aa16-3f9e-3f7c-ab0a-3f902c16cf1e | -12.012 | -43.43493 | 2026-10-10 05:06:00 | NOAA-20 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 088a2ab8-02f0-37a1-928c-5111bfba1a0e | -8.68685 | -62.40276 | 2026-10-10 05:06:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2392f7bb-5651-330f-86fc-ed5558882d43 | -12.15067 | -57.24042 | 2026-10-10 05:06:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 053db5bf-a82e-3dc6-8a89-13d02faf3517 | -7.45497 | -63.64359 | 2026-10-10 05:06:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| be236826-3804-3027-88f4-cc5a43068495 | -11.97326 | -57.6125 | 2026-10-10 05:06:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |


[Clique aqui para ver as próximas entradas](README133.md)
