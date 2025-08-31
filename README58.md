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

## Dados Diários - Página 58

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 0fd8cc42-927a-3d7b-acc0-8db96e52922a | -10.51801 | -51.93703 | 2025-08-31 04:51:00 | NOAA-20 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 4e7fdaae-e3c3-30bb-93f7-3fb0e76c00ca | -11.72667 | -51.76121 | 2025-08-31 04:51:00 | NOAA-20 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| f4a578b4-6689-3389-a01f-9498dc2e9999 | -11.35452 | -43.61784 | 2025-08-31 04:51:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| da66ff8f-3b16-3937-a496-106eaad44338 | -11.08346 | -52.0381 | 2025-08-31 04:51:00 | NOAA-20 | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 83b668a5-e1ce-32f7-99e9-3464a35e0217 | -12.39924 | -46.47577 | 2025-08-31 04:51:00 | NOAA-20 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 3d2656e1-9af3-3d90-b571-3742551caa78 | -11.02099 | -46.88258 | 2025-08-31 04:51:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 7c73dfc7-fb39-3928-ba46-1cc714b19b6c | -7.70933 | -50.28012 | 2025-08-31 04:51:00 | NOAA-20 | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| ab17840b-e68b-3afc-8aa0-2215b1f9843b | -14.33204 | -51.86807 | 2025-08-31 04:51:00 | NOAA-20 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b691f3d0-5a7d-3f1d-b673-5911c86b6ee5 | -10.74927 | -59.82 | 2025-08-31 04:51:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 8ae0c714-f7af-3ab8-9977-7eb4356b44a1 | -11.89124 | -46.37411 | 2025-08-31 04:51:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| b3b4abfd-ad74-3849-87ec-ef1954ffceff | -10.31635 | -59.20057 | 2025-08-31 04:51:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 53cd1622-3c64-33d4-b901-92de0b8f641e | -10.03543 | -48.08477 | 2025-08-31 04:51:00 | NOAA-20 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 622b5824-d450-300d-84ae-c6d9a189ce11 | -15.67862 | -43.23134 | 2025-08-31 04:51:00 | NOAA-20 | PORTEIRINHA | MINAS GERAIS | Brasil | 3152204 | 31 | 33 | nan | nan | nan | Caatinga | 3.1 |
| edcef884-3250-3869-9668-7f194ab065d7 | -9.30481 | -59.22364 | 2025-08-31 04:51:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 07fc3d39-f171-3840-b54f-086b560078d5 | -9.45143 | -62.35155 | 2025-08-31 04:51:00 | NOAA-20 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 7.7 |
| a4818a03-f200-36ae-abd9-c8922ea261c7 | -12.09771 | -44.72447 | 2025-08-31 04:51:00 | NOAA-20 | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 12.4 |
| fadb6588-aef0-3abe-89ae-11568336c693 | -13.35233 | -51.75591 | 2025-08-31 04:51:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 63695a1d-4d07-37c2-9234-2b1b9789211f | -11.058 | -52.04542 | 2025-08-31 04:51:00 | NOAA-20 | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 8e689fab-6462-3a78-b819-13878b96931f | -11.24483 | -44.67661 | 2025-08-31 04:51:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f65466c1-25ac-3496-86fc-f63a651a32ba | -13.35265 | -46.9521 | 2025-08-31 04:51:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 0cb10e04-5b69-3ef1-9c30-6b3d5d4027f1 | -14.41209 | -53.44424 | 2025-08-31 04:51:00 | NOAA-20 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 62927355-4580-3e13-a1e0-7aaa64f6154d | -10.47642 | -51.63363 | 2025-08-31 04:51:00 | NOAA-20 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 17.5 |
| c3557c0a-8faf-3949-8219-ecdaffbd5662 | -7.71636 | -50.30559 | 2025-08-31 04:51:00 | NOAA-20 | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| c37069e7-2ed6-3a2c-a791-e78b5ebb9ae1 | -13.0273 | -56.906 | 2025-08-31 04:51:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 3832ab8e-1481-3164-9a0b-fd0723f7858f | -9.68225 | -47.04957 | 2025-08-31 04:51:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 5115e25b-f1d3-31da-ba0d-cf76ef26f116 | -14.03843 | -44.57357 | 2025-08-31 04:51:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c4c7b993-7362-34f9-92b1-ac2aeb8e0e1b | -10.10353 | -49.28351 | 2025-08-31 04:51:00 | NOAA-20 | CHAPADA DE AREIA | TOCANTINS | Brasil | 1704600 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| da9e4947-e197-319f-a6d3-1de5b34a572e | -9.42711 | -62.33697 | 2025-08-31 04:51:00 | NOAA-20 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 2295b15b-846b-3825-958b-596134e5c355 | -11.40966 | -63.23721 | 2025-08-31 04:51:00 | NOAA-20 | SÃO MIGUEL DO GUAPORÉ | RONDÔNIA | Brasil | 1100320 | 11 | 33 | nan | nan | nan | Amazônia | 2.5 |
| c7fdd02d-d39e-346c-88f8-ebf931d535a5 | -9.58833 | -54.47341 | 2025-08-31 04:51:00 | NOAA-20 | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3c8a3dd6-aa48-3b21-8f3d-26859084e0fb | -8.55535 | -63.02076 | 2025-08-31 04:51:00 | NOAA-20 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 2879bea2-9706-3e72-9065-cecf39dd256b | -9.43338 | -62.3615 | 2025-08-31 04:51:00 | NOAA-20 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 2.2 |
| b830ff2d-8943-3f79-84ad-b1033adbbfaf | -9.4601 | -62.3632 | 2025-08-31 04:51:00 | NOAA-20 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a1e0b1a6-d712-341d-84dc-235dd433c6cb | -7.90962 | -63.01397 | 2025-08-31 04:51:00 | NOAA-20 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a3b65e79-f403-3be6-a494-a1a2d2df1205 | -9.06564 | -65.43653 | 2025-08-31 04:51:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 1fa7f958-bcbc-3449-b667-df8ad372c99c | -9.45025 | -62.35799 | 2025-08-31 04:51:00 | NOAA-20 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 097315c5-e95a-341a-9595-d752def2d7eb | -7.94727 | -46.41083 | 2025-08-31 04:51:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 80d85805-c58d-3409-992f-f6c2fe9ef353 | -10.31566 | -59.20447 | 2025-08-31 04:51:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 81ec05da-2455-31e3-a6f9-640a741c0595 | -14.52599 | -53.01171 | 2025-08-31 04:51:00 | NOAA-20 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 008e3fe4-98d6-3e5f-a4a4-c34edb130979 | -9.59548 | -54.4929 | 2025-08-31 04:51:00 | NOAA-20 | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 44f70b18-4b3d-3ce8-8a97-6433762e009c | -10.9473 | -50.85126 | 2025-08-31 04:51:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 12.9 |
| 6600375d-503f-3e56-ac39-df584c27b727 | -8.49645 | -44.74877 | 2025-08-31 04:51:00 | NOAA-20 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 9db1876e-9123-3306-83c0-6c36b90366c5 | -12.63832 | -48.21145 | 2025-08-31 04:51:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| c90e87f6-baee-3e5f-87a6-4893eaf1ac68 | -8.29365 | -46.31447 | 2025-08-31 04:51:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 5308f347-d107-343c-8cdc-1f27869c7f01 | -11.41369 | -63.24508 | 2025-08-31 04:51:00 | NOAA-20 | SÃO MIGUEL DO GUAPORÉ | RONDÔNIA | Brasil | 1100320 | 11 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 6e9e8411-fad4-3ee3-93a1-a72a0db724f3 | -12.51655 | -53.83229 | 2025-08-31 04:51:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 97d0305a-21ad-3626-ad1a-dce1e8afdcd1 | -9.43945 | -60.5709 | 2025-08-31 04:51:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 9d439420-5bec-393c-8904-2ce982951f02 | -12.56184 | -44.79745 | 2025-08-31 04:51:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 39599164-e2e5-3eea-a9d1-4d162be2b8c6 | -11.89418 | -46.42514 | 2025-08-31 04:51:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 11231185-cb8d-3b6b-bd17-ff60a201058f | -12.83319 | -48.13819 | 2025-08-31 04:51:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 97dbd064-9290-37e2-96b5-fb8e9ced3516 | -14.98905 | -46.70359 | 2025-08-31 04:51:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 5.4 |
| a4d4a671-7291-30d4-8d8d-cbcef75d356a | -12.84929 | -48.08365 | 2025-08-31 04:51:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| b0aaa84c-2f7a-3aa7-84d6-b811b3cad85a | -14.03292 | -44.57277 | 2025-08-31 04:51:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| a4e721e1-86be-304b-a6db-95815a6bf332 | -14.99914 | -46.70195 | 2025-08-31 04:51:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| b5bd0f80-0b23-3951-9721-231c39928669 | -8.72792 | -50.37876 | 2025-08-31 04:51:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| c3492630-3b21-34fb-97cb-5dee4c7f603f | -11.08182 | -44.60872 | 2025-08-31 04:51:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 3b65b993-78da-330d-add0-df5d71865620 | -11.81081 | -46.43591 | 2025-08-31 04:51:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 9.4 |
| 746ae397-ac40-364b-81b2-5928a466b254 | -7.97702 | -46.413 | 2025-08-31 04:51:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b694810e-3a65-3696-8ade-3d008aedbf3d | -8.88736 | -62.39212 | 2025-08-31 04:51:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 1008bfac-38fe-3d14-9a13-ddc26c3335b4 | -8.6639 | -62.83355 | 2025-08-31 04:51:00 | NOAA-20 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 2.2 |
| ec712c74-8d41-31a8-8f56-7ccee8c5d8b1 | -11.30165 | -43.67386 | 2025-08-31 04:51:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 19dc1359-3e46-3f62-9864-a914ccbf987f | -14.0393 | -44.56623 | 2025-08-31 04:51:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 3c746eba-e6a2-3327-a308-850fb8930976 | -11.88205 | -46.72972 | 2025-08-31 04:51:00 | NOAA-20 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| a8979ced-b47f-3b3b-9031-0286246d518e | -11.81358 | -46.452 | 2025-08-31 04:51:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 10.3 |
| 7f726cca-c4c2-371e-a7cb-e62bb06123c1 | -10.99507 | -46.93941 | 2025-08-31 04:51:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 1b399fd9-b1af-3105-99d1-3adf52792ecb | -7.71464 | -50.26863 | 2025-08-31 04:51:00 | NOAA-20 | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 49568121-2315-33f9-94f5-ea5d00d861e5 | -13.36713 | -46.95033 | 2025-08-31 04:51:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| a0ff9d6f-4a72-346b-9ff6-ccc548d115bb | -10.94435 | -50.84665 | 2025-08-31 04:51:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 7.2 |
| caabbc0f-c3c8-3953-8346-ca1da211ba94 | -8.65249 | -62.83195 | 2025-08-31 04:51:00 | NOAA-20 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ae3bba14-0cc1-3bb7-b45c-0d51dab8247e | -12.3176 | -45.72036 | 2025-08-31 04:51:00 | NOAA-20 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 6c9f4cad-3719-30a7-93ae-01b59b334a51 | -12.63625 | -48.19505 | 2025-08-31 04:51:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 2bfb93e2-2796-3ec5-a638-2886395c561c | -10.61449 | -54.91671 | 2025-08-31 04:51:00 | NOAA-20 | TERRA NOVA DO NORTE | MATO GROSSO | Brasil | 5108055 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 52ca8f0e-6cd7-3779-beda-f93648cf29c5 | -14.04061 | -44.55511 | 2025-08-31 04:51:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| dbbcf078-44a0-323a-812a-7fd560f4793a | -13.32966 | -51.78183 | 2025-08-31 04:51:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c3fbc95d-346e-3bbf-aa6a-d7de1ee3411b | -10.03435 | -48.09243 | 2025-08-31 04:51:00 | NOAA-20 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 5aca5063-1dc1-348a-816d-39588f50d272 | -9.44561 | -62.35382 | 2025-08-31 04:51:00 | NOAA-20 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ac42175b-b50d-36cf-aa69-a94fbca2150a | -7.91522 | -63.015 | 2025-08-31 04:51:00 | NOAA-20 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 4244e878-abc2-3456-993a-e6b44194e31e | -8.67834 | -62.41349 | 2025-08-31 04:51:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 14a1adc8-99d8-38ee-a768-b59eeab68907 | -14.99266 | -46.70149 | 2025-08-31 04:51:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 5c4af115-bce1-30bb-8bd1-ce86db995050 | -13.68713 | -46.88502 | 2025-08-31 04:51:00 | NOAA-20 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 3.7 |
| f26a3aea-e612-3bc1-a657-d46e8fe93109 | -14.04018 | -44.55882 | 2025-08-31 04:51:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 93545906-6c10-3d66-bfae-908888d93814 | -13.50473 | -46.97379 | 2025-08-31 04:51:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 79b901ee-6fcb-3589-9dbd-9a44b21591d0 | -9.43978 | -62.35612 | 2025-08-31 04:51:00 | NOAA-20 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 2.1 |
| adfea0de-b03e-3585-b1cc-c3ccdfc5793b | -11.9027 | -46.70387 | 2025-08-31 04:51:00 | NOAA-20 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| c732f1e1-856d-39e4-9a9e-ccb481b821c8 | -12.62912 | -57.00715 | 2025-08-31 04:51:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| bde0b92c-f15c-3d27-9b4a-4bcf988914b7 | -7.71582 | -50.28498 | 2025-08-31 04:51:00 | NOAA-20 | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 0a205752-abd0-3bf5-94c8-2dc287abca5c | -13.47109 | -46.97673 | 2025-08-31 04:51:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 12.0 |
| 080cdb0e-5b0b-346e-bfae-b0301c65a3c5 | -13.02663 | -56.91002 | 2025-08-31 04:51:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c57cccfa-25c0-346a-b7eb-088657b21718 | -14.35294 | -53.27861 | 2025-08-31 04:51:00 | NOAA-20 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 7c2c91f0-36f8-3806-ac87-fbd9f31df1ef | -11.82943 | -51.49993 | 2025-08-31 04:51:00 | NOAA-20 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 78afea05-13ce-36c6-8f86-77d9b6655ea8 | -11.32496 | -63.25991 | 2025-08-31 04:51:00 | NOAA-20 | SÃO MIGUEL DO GUAPORÉ | RONDÔNIA | Brasil | 1100320 | 11 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 251bbb6d-3803-353e-be09-e64a8ffc17c8 | -15.94874 | -41.4082 | 2025-08-31 04:51:00 | NOAA-20 | CACHOEIRA DE PAJEÚ | MINAS GERAIS | Brasil | 3102704 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| f0d16d2b-5705-34f6-8cfb-a05d8fa9f5d4 | -9.081 | -59.48072 | 2025-08-31 04:51:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f7aa61e8-2346-33cf-88e3-e9e36014ee9f | -13.35176 | -51.75982 | 2025-08-31 04:51:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 31aceeac-8351-39d1-b62d-8290a158a64b | -11.28494 | -43.64573 | 2025-08-31 04:51:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| e7415ef2-e4bb-3541-8622-ca3d6166d30c | -9.05927 | -65.43523 | 2025-08-31 04:51:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 8ac70db6-f82e-3077-a421-19fc68fb5ccf | -8.17494 | -45.04537 | 2025-08-31 04:51:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| bc5d467c-88fd-3578-bc01-21e31b01ec15 | -9.30552 | -59.21948 | 2025-08-31 04:51:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 910383c5-53d5-3bda-8469-60ccdf8298a2 | -9.06337 | -65.41418 | 2025-08-31 04:51:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 7774322e-4ce7-32fa-9788-065e02eb8dc2 | -8.54535 | -51.30724 | 2025-08-31 04:51:00 | NOAA-20 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |


[Clique aqui para ver as próximas entradas](README59.md)
