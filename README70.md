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

## Dados Diários - Página 70

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| fe9e5512-8dbd-353a-9e38-249a2c78e368 | -6.62032 | -43.73831 | 2025-08-30 05:10:00 | NOAA-20 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| ac46a9d0-f7b1-34e0-b2a7-37c96e1902d1 | -11.88357 | -46.39264 | 2025-08-30 05:10:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 0facbbda-4095-39a5-80ac-00f5ba2b8df1 | -9.4356 | -62.36271 | 2025-08-30 05:10:00 | NOAA-20 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 3.5 |
| ab6c2325-8e91-3d13-b104-27df3e1fa1b8 | -10.44977 | -57.96577 | 2025-08-30 05:10:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 08287776-c43b-3fd9-a749-8bcd96de9b7e | -9.28054 | -60.46157 | 2025-08-30 05:10:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 36e7385e-5bfd-3dc4-a70a-418a5da893a4 | -11.85825 | -46.38781 | 2025-08-30 05:10:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| b7a521fe-1965-3d0a-ae51-ad5d037e100d | -11.0632 | -52.04993 | 2025-08-30 05:10:00 | NOAA-20 | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| aac79d44-cbd8-3a6b-addd-8460ab8dfc83 | -9.50362 | -49.09631 | 2025-08-30 05:10:00 | NOAA-20 | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 07445e53-c197-3587-9200-9a79dc393abb | -10.36304 | -59.19976 | 2025-08-30 05:10:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 58dffe15-e860-31bc-a26f-6f7751fa2ea8 | -9.10324 | -65.74064 | 2025-08-30 05:10:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 97a6309a-02c7-3576-8b0d-78f8ad8da54f | -9.44263 | -62.34434 | 2025-08-30 05:10:00 | NOAA-20 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 1635d54a-83fa-3e3a-a77a-177bbf92b85c | -10.3481 | -59.18633 | 2025-08-30 05:10:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6ca86bc9-1b5c-3755-8487-093a4e0de5e4 | -9.44949 | -60.55222 | 2025-08-30 05:10:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 4.1 |
| df668794-b5b1-321b-a52f-c912a6a0bf4c | -9.4372 | -62.35323 | 2025-08-30 05:10:00 | NOAA-20 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 99b4f28b-c52c-31b5-b93b-b1d5dcd0b30b | -10.37246 | -59.20496 | 2025-08-30 05:10:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 75d31b91-5306-3ef5-a47e-0ea63ca45ae2 | -10.32149 | -59.18533 | 2025-08-30 05:10:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ab4e75ac-2be8-372b-82e1-6855a3ef7464 | -8.93369 | -64.16224 | 2025-08-30 05:10:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| effcc182-b4c6-383d-9293-8d24506423ff | -10.34478 | -59.18576 | 2025-08-30 05:10:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e6854909-440a-3541-a417-cd2d75cf28be | -11.92118 | -46.69293 | 2025-08-30 05:10:00 | NOAA-20 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 897002c4-06a8-3d86-8101-2e8b5c89c29d | -11.06381 | -52.04535 | 2025-08-30 05:10:00 | NOAA-20 | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 9eb49022-8502-3498-a487-12336b8973e6 | -9.44601 | -60.55164 | 2025-08-30 05:10:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 9235e174-efc5-39e2-9932-218b8b91c1f6 | -10.45708 | -59.12055 | 2025-08-30 05:10:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 52c177f4-f758-39cf-b60d-27ad5258a4b9 | -7.12161 | -44.60774 | 2025-08-30 05:10:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |
| aa94a74c-423f-326b-ab17-acca65fb29be | -9.45722 | -60.55706 | 2025-08-30 05:10:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 89272633-b4ac-3533-a6ca-c0ee6b838b0a | -7.7183 | -50.27063 | 2025-08-30 05:10:00 | NOAA-20 | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 71329b50-e937-3ea4-91bf-564627aa8d9b | -10.33974 | -59.19583 | 2025-08-30 05:10:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 85cbf897-b64b-3b84-983b-c5b62ee520f4 | -8.67574 | -62.42959 | 2025-08-30 05:10:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 636a2b8a-1008-38b4-9add-a28857229188 | -10.46193 | -57.97484 | 2025-08-30 05:10:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 22f240a9-3ee1-398c-998c-57c63e631fa9 | -9.45489 | -62.34152 | 2025-08-30 05:10:00 | NOAA-20 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 97.0 |
| 8f0c3801-0417-33c1-b9ff-e77ca748523d | -8.87263 | -60.73676 | 2025-08-30 05:10:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| b6778c3e-ad32-323d-a679-c95b18b52840 | -11.77454 | -47.56277 | 2025-08-30 05:10:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 04facf80-8392-3d05-b5e4-302be5670083 | -8.65838 | -63.29592 | 2025-08-30 05:10:00 | NOAA-20 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8f7d6838-704b-32bd-b746-717341c12e52 | -8.11088 | -45.00598 | 2025-08-30 05:10:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 817b37bb-8767-3b1a-8d59-d900988374a6 | -9.44886 | -60.55613 | 2025-08-30 05:10:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 4.9 |
| f49cd381-08ce-39ad-b375-19ec50917e03 | -6.00778 | -57.85624 | 2025-08-30 05:10:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b94f2086-39ee-3cbd-959b-24b761febc5d | -9.44103 | -62.35387 | 2025-08-30 05:10:00 | NOAA-20 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 60dfe6fe-e19f-3f7e-b5ec-af50403c4e7a | -9.82282 | -63.86206 | 2025-08-30 05:10:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.8 |
| b7f140fd-37e1-3cb4-af22-3e3064e01045 | -9.57661 | -54.4893 | 2025-08-30 05:10:00 | NOAA-20 | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 462940b5-18e4-3e0e-bffe-320b17ae0022 | -9.44165 | -62.3736 | 2025-08-30 05:10:00 | NOAA-20 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f64f174d-1416-3754-b127-fb5795437a99 | -8.94967 | -65.95644 | 2025-08-30 05:10:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 70d2843f-a810-3fc2-824c-bb7ed5f5a327 | -8.5575 | -51.311 | 2025-08-30 05:10:00 | NOAA-20 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 0283b247-b2ba-3b9e-b112-e76b195ee88c | -10.99954 | -46.95668 | 2025-08-30 05:10:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 47.6 |
| 660c47e1-610f-3f28-86ed-70aa0bf1c7a6 | -10.84485 | -53.77349 | 2025-08-30 05:10:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ac16640b-3311-3b52-90f8-6d4bd058fb09 | -9.44807 | -60.5475 | 2025-08-30 05:10:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 72a72935-8427-3719-8f37-54926d1fd8a0 | -8.34919 | -62.93367 | 2025-08-30 05:10:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 9d4ce096-6ec8-3058-b04e-cd63c9216e2b | -8.71153 | -50.36111 | 2025-08-30 05:10:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| e5fdd3a9-ce75-3655-9994-0461b3795cfb | -10.98883 | -46.84821 | 2025-08-30 05:10:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 702dc108-946a-33a8-b0fb-65d3d5e6310a | -10.44591 | -57.96875 | 2025-08-30 05:10:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 63e66e2d-91a5-3f9b-ad5b-6d6ed1e7de61 | -9.82701 | -63.8627 | 2025-08-30 05:10:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 835d53da-b478-37d9-ac40-cecc27692934 | -9.08619 | -59.4851 | 2025-08-30 05:10:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 11.0 |
| 97f4a486-b5f3-3450-9d77-c17691d6883b | -10.07855 | -54.9327 | 2025-08-30 05:10:00 | NOAA-20 | MATUPÁ | MATO GROSSO | Brasil | 5105606 | 51 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 5bfc11f4-97a6-31cd-849e-1ee74464dad1 | -10.36962 | -57.80564 | 2025-08-30 05:10:00 | NOAA-20 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 69a46ae2-15be-30b9-bfe0-9f0650ab6dab | -8.55306 | -51.31016 | 2025-08-30 05:10:00 | NOAA-20 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| b92c8437-5cd8-3118-9191-6d2feae8127a | -9.70526 | -49.47274 | 2025-08-30 05:10:00 | NOAA-20 | MARIANÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1712504 | 17 | 33 | nan | nan | nan | Cerrado | 9.5 |
| 207464b6-81dd-3290-bbd1-ab75939ec57d | -8.55237 | -63.01584 | 2025-08-30 05:10:00 | NOAA-20 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 6f0082ea-d648-3afd-a18c-0e8bf9984e96 | -9.80598 | -61.20466 | 2025-08-30 05:10:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3ae24eeb-b434-3740-b178-bc916b052bc6 | -9.18105 | -65.80025 | 2025-08-30 05:10:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| dbd2bb79-82c1-34b7-a552-21d6c04872f8 | -9.57532 | -54.4981 | 2025-08-30 05:10:00 | NOAA-20 | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 21d47498-f218-3e5a-9590-8e36aefae8d3 | -8.69125 | -50.40102 | 2025-08-30 05:10:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| d8d9737d-0b77-31b8-94d7-20e63e39464c | -11.87751 | -46.39193 | 2025-08-30 05:10:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 80c36a1b-0096-30e0-890e-59f911ee18cf | -9.21795 | -60.86136 | 2025-08-30 05:10:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| fea455e4-b59d-34cc-829d-bcbb34a438b4 | -7.90012 | -61.52184 | 2025-08-30 05:10:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 9d988ce9-4d22-3561-aee8-5a58382f032a | -11.87704 | -46.39227 | 2025-08-30 05:10:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 7fde95d7-4b8f-39f6-a851-ab3442cbbeb6 | -11.86438 | -46.45062 | 2025-08-30 05:10:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 9.1 |
| 8c86a63f-c75f-3ab8-8cc5-68122948a2c4 | -9.44759 | -60.56396 | 2025-08-30 05:10:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 5.7 |
| beec6163-7ead-3d36-b111-187b27f01254 | -8.55116 | -63.02297 | 2025-08-30 05:10:00 | NOAA-20 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 5ff360c2-a2ce-3a9f-9f94-19065f4e7244 | -7.7442 | -50.26484 | 2025-08-30 05:10:00 | NOAA-20 | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 8.0 |
| 8e8c1be6-9a9b-377e-9c5d-8ac2082b59bf | -9.58161 | -54.48103 | 2025-08-30 05:10:00 | NOAA-20 | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 946ab5b6-cd03-3afe-bdfa-e76dfaeb444b | -9.16164 | -59.5757 | 2025-08-30 05:10:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 41ebfaad-c9c2-318d-9f5d-d1b35c95468c | -8.87617 | -60.73735 | 2025-08-30 05:10:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| ff89ea7f-edf2-3052-a1ed-0c31d1587d84 | -10.3464 | -59.19695 | 2025-08-30 05:10:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e18a6dab-3d78-3722-8978-5e3b3583e302 | -11.84522 | -46.43932 | 2025-08-30 05:10:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 26abe3b2-8940-36cb-8e53-bd554c5fe513 | -8.87747 | -60.72932 | 2025-08-30 05:10:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 67eef3f1-7617-3a5c-8ba9-6c9c685306ea | -9.45107 | -62.34085 | 2025-08-30 05:10:00 | NOAA-20 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 29.1 |
| 832cdc3a-43ef-38ee-bbeb-eeeda97df23e | -9.45568 | -60.5448 | 2025-08-30 05:10:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 5.4 |
| ded241ef-5967-3b97-b647-dac191f3b1df | -11.85225 | -46.38258 | 2025-08-30 05:10:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 81089768-1575-3d5c-b5da-ebfd1e3f05eb | -11.84403 | -46.39334 | 2025-08-30 05:10:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 7.8 |
| d5c978f0-114c-342a-bdf8-549059cb4a5d | -10.99452 | -46.94602 | 2025-08-30 05:10:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 9.7 |
| 5018ebb9-6c7a-39e9-b31b-9508123545ff | -9.44627 | -62.36948 | 2025-08-30 05:10:00 | NOAA-20 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 3.6 |
| c0c36b17-b13b-3b1e-9c10-c8093a5205d3 | -11.88383 | -46.45243 | 2025-08-30 05:10:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 11.3 |
| d5daadcc-ca8a-3273-b0cc-70a1b31144bf | -9.4501 | -62.37015 | 2025-08-30 05:10:00 | NOAA-20 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 93e7433e-dcac-3991-83b9-40123c63b74b | -10.44115 | -51.3527 | 2025-08-30 05:10:00 | NOAA-20 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| fb2c2436-6f9f-32dd-bf0f-5b2d17851902 | -8.90067 | -62.10315 | 2025-08-30 05:10:00 | NOAA-20 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 7.3 |
| cbe1e4b8-5ff8-3ab0-916f-d27dcd96b684 | -10.36856 | -59.20797 | 2025-08-30 05:10:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f49f65d9-34ec-3afe-bca5-21d2039a6b9a | -9.43966 | -60.54662 | 2025-08-30 05:10:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 9.1 |
| 01f25148-88c0-3c8d-b66b-7a923c0305de | -10.44574 | -51.35338 | 2025-08-30 05:10:00 | NOAA-20 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3b33ebc7-d8e2-3f62-8c53-410cf2e6c4bd | -11.82746 | -46.47918 | 2025-08-30 05:10:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 46.9 |
| 34d86c45-595d-319f-8512-c8e4ab928f51 | -8.88091 | -60.72878 | 2025-08-30 05:10:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 2a213258-0240-3d45-86a0-264a399208dd | -8.59432 | -60.57778 | 2025-08-30 05:10:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| fa674f20-8418-3694-96fa-b5a83a4940f6 | -9.12049 | -65.77806 | 2025-08-30 05:10:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 82a4e22d-59df-35ec-821d-20a254bb464c | -11.06881 | -52.04157 | 2025-08-30 05:10:00 | NOAA-20 | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| b9bbf6a0-04a0-3365-be89-12b82dfcf440 | -5.61152 | -45.01086 | 2025-08-30 05:10:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 13.5 |
| 4b4318b5-08ba-3892-9e74-fd4a3e601f63 | -8.2848 | -61.3993 | 2025-08-30 05:10:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| d0874372-9007-32f6-abe5-87a050ff372a | -8.7004 | -60.48499 | 2025-08-30 05:10:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 66742d58-2886-3314-b92b-c10f60f749b5 | -8.29293 | -61.41873 | 2025-08-30 05:10:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 5a35b36c-7433-3e6f-954c-ae561879ef18 | -10.48564 | -57.95355 | 2025-08-30 05:10:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 6.2 |
| b4ac2283-7de0-34d1-b367-2af5aae8f3a8 | -8.67021 | -62.43878 | 2025-08-30 05:10:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 7a7f8f05-1b15-3e61-8151-d2a3bec45d3a | -8.62405 | -67.2471 | 2025-08-30 05:10:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f9457ee5-5f11-36fc-948f-af36358eb576 | -6.00173 | -44.72266 | 2025-08-30 05:10:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 9.6 |
| e0e0086a-0ffe-3886-9579-008421615464 | -11.06417 | -52.04741 | 2025-08-30 05:10:00 | NOAA-20 | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |


[Clique aqui para ver as próximas entradas](README71.md)
