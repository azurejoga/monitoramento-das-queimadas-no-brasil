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

## Dados Diários - Página 17

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| e14000b4-cc7a-334f-a0cb-7f5bd51db2d0 | -12.0056 | -47.7728 | 2025-09-08 02:30:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 55.1 |
| 28f89775-7298-3586-bf74-f3bbdacc690d | -9.4531 | -61.8147 | 2025-09-08 02:30:00 | GOES-19 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 72.4 |
| 425f67ad-465e-3757-a719-4fc37bd58f00 | -5.8791 | -43.9769 | 2025-09-08 02:30:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 79.5 |
| cd5193ef-9afc-3479-a225-b8f90d77939a | -7.3984 | -61.6156 | 2025-09-08 02:30:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 79.6 |
| bd215be3-1506-3824-b4e5-eabff55436ef | -12.6153 | -56.9742 | 2025-09-08 02:40:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 102.6 |
| d17358fc-d170-3e20-8bf8-eccb8ac87bfd | -9.4345 | -61.8156 | 2025-09-08 02:40:00 | GOES-19 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 54.1 |
| f9528434-a906-39ca-b757-ac6c852d2068 | -12.9477 | -54.793 | 2025-09-08 02:40:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 64.9 |
| 7d5520be-7dac-348d-a56c-9b66a97e1086 | -7.4168 | -61.6339 | 2025-09-08 02:40:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 56.1 |
| 2c0b66ec-1e8d-3935-ba49-c89cca862b3f | -9.453 | -61.8338 | 2025-09-08 02:40:00 | GOES-19 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 52.5 |
| c7fa1095-cbbe-3ce4-8fbb-413ea73fc4a4 | -9.4531 | -61.8147 | 2025-09-08 02:40:00 | GOES-19 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 66.5 |
| 9ad385e1-c67e-3879-abe5-e44f9d904a6a | -11.2007 | -54.9992 | 2025-09-08 02:40:00 | GOES-19 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 74.2 |
| b3fd2d4e-f08c-3219-a828-7abbf2c5ab4d | -3.316 | -48.7134 | 2025-09-08 02:40:00 | GOES-19 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 67.6 |
| 2424642e-eff3-3b4a-afc2-0ac94388a8e6 | -14.2575 | -58.3484 | 2025-09-08 02:40:00 | GOES-19 | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 57.4 |
| 9db7a021-2a12-3722-94c8-b16acc13d986 | -7.3984 | -61.6156 | 2025-09-08 02:40:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 64.6 |
| 6b4eed5f-a5e2-3dc6-ad6c-dc312b868344 | -12.6343 | -56.9725 | 2025-09-08 02:40:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 91.7 |
| 7c2b9b8a-34ed-3164-ab45-961860251209 | -14.5067 | -48.8085 | 2025-09-08 02:40:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 80.7 |
| fef7c171-006d-3d2c-b191-fd1d37f9666a | -7.3983 | -61.6346 | 2025-09-08 02:40:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 136.5 |
| bed53500-a6f0-3af4-bb77-f3ea368d7128 | -11.3558 | -50.3804 | 2025-09-08 02:50:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 54.3 |
| 0338ea64-8a0b-3835-8d68-7f9020939242 | -7.3984 | -61.6156 | 2025-09-08 02:50:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 55.6 |
| 0b08c7bb-33e3-33ae-a938-b58262fade11 | -11.2007 | -54.9992 | 2025-09-08 02:50:00 | GOES-19 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 71.7 |
| 4b6cea5d-addc-3c30-9fc0-e4df6c1074b2 | -12.6153 | -56.9742 | 2025-09-08 02:50:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 93.5 |
| 12d7d632-dd16-3603-bb15-4326be76a3a3 | -7.3983 | -61.6346 | 2025-09-08 02:50:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 122.9 |
| ec9f4f5c-25a1-365b-89c4-aec6f1f72a0a | -9.4345 | -61.8156 | 2025-09-08 02:50:00 | GOES-19 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 53.6 |
| dccccd3f-fe80-391e-9da4-3472f00b3648 | -12.6343 | -56.9725 | 2025-09-08 02:50:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 85.0 |
| e6531857-4e51-3601-8f5e-4d0afdbf6558 | -7.4168 | -61.6339 | 2025-09-08 02:50:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 69.1 |
| 5942326f-37b1-327e-89f1-549078453950 | -12.9477 | -54.793 | 2025-09-08 02:50:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 60.7 |
| a83a8485-ee3b-3af5-bc04-500da0fb0823 | -14.2575 | -58.3484 | 2025-09-08 02:50:00 | GOES-19 | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 41.8 |
| ab96076c-88de-3cd5-9441-4701ffa111a9 | -14.5067 | -48.8085 | 2025-09-08 02:50:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 77.2 |
| e35dc77d-99b8-3748-b256-84d2977cac8b | -12.6153 | -56.9742 | 2025-09-08 03:00:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 84.3 |
| 84be1008-db9b-372d-b350-777bbb022103 | -9.4531 | -61.8147 | 2025-09-08 03:00:00 | GOES-19 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 71.2 |
| 881bf8f1-1117-358f-baa7-f5b47743f450 | -14.2575 | -58.3484 | 2025-09-08 03:00:00 | GOES-19 | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 74.3 |
| 01d0e1cb-5471-33af-a40a-b638564d3b71 | -7.4168 | -61.6339 | 2025-09-08 03:00:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 64.7 |
| 62335a41-a4ad-34fc-b197-f218da3612f6 | -7.3983 | -61.6346 | 2025-09-08 03:00:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 128.3 |
| 5d4dfec1-e8c0-30fe-9662-aec2e6fbea1a | -14.5067 | -48.8085 | 2025-09-08 03:00:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 64.7 |
| 9efe62be-a628-3703-a90a-8960ac840118 | -12.9477 | -54.793 | 2025-09-08 03:00:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 67.0 |
| 750ab110-7a85-3416-ad27-d4289fa5203d | -14.5266 | -48.7833 | 2025-09-08 03:00:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 56.1 |
| 349a611f-c3e5-391e-a4cb-533fa1cb4173 | -11.4268 | -43.649 | 2025-09-08 03:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 66.6 |
| d87c0c30-b57c-3776-afc5-40299b70a780 | -10.1464 | -46.1973 | 2025-09-08 03:00:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 81.2 |
| 5fcc5c9a-334e-39ec-92be-9ec84e6fcb53 | -11.2827 | -46.4817 | 2025-09-08 03:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 32.8 |
| 4689a20b-6663-3f4a-b960-efb90fcfd0fd | -14.5072 | -48.7863 | 2025-09-08 03:00:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 44.8 |
| ecf21540-07a2-3b94-b731-4b8feb0e6992 | -12.6343 | -56.9725 | 2025-09-08 03:00:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 104.2 |
| 0f901863-bb4d-3b75-8bd5-1bbcca326a2c | -11.2831 | -46.4591 | 2025-09-08 03:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 51.2 |
| 7d797336-33b1-3572-b5bf-afb843cc3396 | -11.2007 | -54.9992 | 2025-09-08 03:00:00 | GOES-19 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 65.3 |
| ab9ad886-a03a-3af6-b8a9-a8cbb0724b3c | -7.3984 | -61.6156 | 2025-09-08 03:00:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 62.0 |
| 5b87133c-c91e-3746-bc58-8341044b1fa6 | -7.4168 | -61.6339 | 2025-09-08 03:10:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 67.0 |
| 77d408f3-f20f-35ca-a9c9-a01b29975268 | -7.3983 | -61.6346 | 2025-09-08 03:10:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 121.5 |
| 9bb02163-6aaf-3f0b-9438-8c484faa58b7 | -12.6153 | -56.9742 | 2025-09-08 03:10:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 86.9 |
| cbf67054-8b43-3325-bfd5-a3cef7e60dc6 | -14.5067 | -48.8085 | 2025-09-08 03:10:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 60.0 |
| 02be2140-ce5e-3e8d-98dd-44b99440710d | -11.3558 | -50.3804 | 2025-09-08 03:10:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 56.3 |
| 3801238b-aa26-3242-bb24-bdb6d8a1812c | -11.3742 | -50.4212 | 2025-09-08 03:10:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 75.5 |
| 814790d7-8a6b-3ffe-9911-1fb64a6fe235 | -11.4128 | -50.374 | 2025-09-08 03:10:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 77.6 |
| cc730f48-d499-3d97-8ecf-2cca1e3b01af | -12.6343 | -56.9725 | 2025-09-08 03:10:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 86.6 |
| fbe94b01-2b58-3f14-9acd-8fd69eb83413 | -9.4531 | -61.8147 | 2025-09-08 03:10:00 | GOES-19 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 51.5 |
| 4bea0c25-e955-3d6d-8759-d7c2fc12c71f | -7.3984 | -61.6156 | 2025-09-08 03:10:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 60.2 |
| 94a69636-09c8-38a6-8604-a1fe7e50c481 | -11.3938 | -50.3762 | 2025-09-08 03:10:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 60.2 |
| f289c305-220e-3e2c-b325-c2e79042dfb5 | -11.3932 | -50.419 | 2025-09-08 03:10:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 55.1 |
| c211971f-60ff-39ab-acec-a29bdee40286 | -12.9477 | -54.793 | 2025-09-08 03:10:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 57.3 |
| afb0e851-18cf-3c4a-bd8a-3f643b28939e | -11.2007 | -54.9992 | 2025-09-08 03:10:00 | GOES-19 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 67.3 |
| d6bb570f-2fb5-3f99-a7a1-3b9e60104d0f | -3.89758 | -38.53898 | 2025-09-08 03:10:00 | NOAA-21 | ITAITINGA | CEARÁ | Brasil | 2306256 | 23 | 33 | nan | nan | nan | Caatinga | 3.2 |
| 4f9c8542-1aab-3c6d-9fc2-41637d240d23 | -3.89512 | -38.53793 | 2025-09-08 03:10:00 | NOAA-21 | ITAITINGA | CEARÁ | Brasil | 2306256 | 23 | 33 | nan | nan | nan | Caatinga | 2.8 |
| de51530e-58bd-3c2e-bc3e-75b68a01f985 | -8.61888 | -40.20064 | 2025-09-08 03:13:00 | NOAA-21 | LAGOA GRANDE | PERNAMBUCO | Brasil | 2608750 | 26 | 33 | nan | nan | nan | Caatinga | 6.6 |
| 192e2005-49fb-34ee-915c-b5ce54cdde2d | -8.61988 | -40.19532 | 2025-09-08 03:13:00 | NOAA-21 | LAGOA GRANDE | PERNAMBUCO | Brasil | 2608750 | 26 | 33 | nan | nan | nan | Caatinga | 6.6 |
| 1b13afa7-86d0-383c-beff-f150cb749bcf | -7.31534 | -39.15392 | 2025-09-08 03:13:00 | NOAA-21 | MISSÃO VELHA | CEARÁ | Brasil | 2308401 | 23 | 33 | nan | nan | nan | Caatinga | 4.6 |
| 9807dd78-642d-3e84-9a30-ff47a48768cc | -7.55747 | -40.10487 | 2025-09-08 03:13:00 | NOAA-21 | BODOCÓ | PERNAMBUCO | Brasil | 2602001 | 26 | 33 | nan | nan | nan | Caatinga | 4.7 |
| b6a36d6b-bd71-3017-8ccd-ee0e624014b2 | -8.10196 | -39.51658 | 2025-09-08 03:13:00 | NOAA-21 | PARNAMIRIM | PERNAMBUCO | Brasil | 2610400 | 26 | 33 | nan | nan | nan | Caatinga | 1.7 |
| c49da5c3-e395-3039-925b-dea2c126d2d1 | -8.62568 | -40.20344 | 2025-09-08 03:13:00 | NOAA-21 | LAGOA GRANDE | PERNAMBUCO | Brasil | 2608750 | 26 | 33 | nan | nan | nan | Caatinga | 8.3 |
| 7e5da61c-eece-3206-b24d-88adfb8e5e8e | -7.55649 | -40.10634 | 2025-09-08 03:13:00 | NOAA-21 | BODOCÓ | PERNAMBUCO | Brasil | 2602001 | 26 | 33 | nan | nan | nan | Caatinga | 4.6 |
| 19bfeb89-8a4d-3a3e-809a-8f9d7622191e | -8.62533 | -40.20184 | 2025-09-08 03:13:00 | NOAA-21 | LAGOA GRANDE | PERNAMBUCO | Brasil | 2608750 | 26 | 33 | nan | nan | nan | Caatinga | 6.6 |
| 67010dd7-2266-3059-bd8f-257aa4e0c7e5 | -7.31429 | -39.15384 | 2025-09-08 03:13:00 | NOAA-21 | MISSÃO VELHA | CEARÁ | Brasil | 2308401 | 23 | 33 | nan | nan | nan | Caatinga | 4.7 |
| 0364c459-f7da-30b3-a8b4-7802474ff8f0 | -8.62027 | -40.19699 | 2025-09-08 03:13:00 | NOAA-21 | LAGOA GRANDE | PERNAMBUCO | Brasil | 2608750 | 26 | 33 | nan | nan | nan | Caatinga | 11.8 |
| 6b51d3a1-1c44-3fde-8c79-a4341713171f | -8.61924 | -40.20226 | 2025-09-08 03:13:00 | NOAA-21 | LAGOA GRANDE | PERNAMBUCO | Brasil | 2608750 | 26 | 33 | nan | nan | nan | Caatinga | 8.3 |
| 6f65a36e-4c40-3f11-9418-b12b7686784a | -7.76814 | -34.91554 | 2025-09-08 03:13:00 | NOAA-21 | ITAPISSUMA | PERNAMBUCO | Brasil | 2607752 | 26 | 33 | nan | nan | nan | Mata Atlântica | 2.7 |
| 1edf2c7e-cefa-3497-b1b9-f83273010c66 | -17.53557 | -43.74313 | 2025-09-08 03:15:00 | NOAA-21 | OLHOS-D'ÁGUA | MINAS GERAIS | Brasil | 3145455 | 31 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 8d0f7984-9fca-30a0-972f-357d08751457 | -17.66153 | -44.19143 | 2025-09-08 03:15:00 | NOAA-21 | JOAQUIM FELÍCIO | MINAS GERAIS | Brasil | 3136405 | 31 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 4e9fca3c-5b44-3fcc-a701-6d7672ef1371 | -15.296 | -43.383 | 2025-09-08 03:15:00 | NOAA-21 | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Caatinga | 8.3 |
| 038bfd7a-8746-3dc1-b5e8-3778881011ee | -17.66303 | -44.1852 | 2025-09-08 03:15:00 | NOAA-21 | JOAQUIM FELÍCIO | MINAS GERAIS | Brasil | 3136405 | 31 | 33 | nan | nan | nan | Cerrado | 3.0 |
| a0fe5d52-b0c9-3bb9-96a7-3b1942cd085d | -17.14813 | -44.44558 | 2025-09-08 03:15:00 | NOAA-21 | JEQUITAÍ | MINAS GERAIS | Brasil | 3135605 | 31 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 830f0ab2-5e06-3b41-af75-4b30adc54814 | -15.2975 | -43.37637 | 2025-09-08 03:15:00 | NOAA-21 | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Caatinga | 8.3 |
| f9a243a1-28da-3e59-a874-77d728f0ccc2 | -15.29449 | -43.38965 | 2025-09-08 03:15:00 | NOAA-21 | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Caatinga | 8.4 |
| 599d890d-7d98-3a5b-8c31-e5f27771a2a1 | -17.66857 | -44.19242 | 2025-09-08 03:15:00 | NOAA-21 | JOAQUIM FELÍCIO | MINAS GERAIS | Brasil | 3136405 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ea3bcfd8-6e55-31a7-96c3-8f12e330e815 | -17.6638 | -44.18523 | 2025-09-08 03:15:00 | NOAA-21 | JOAQUIM FELÍCIO | MINAS GERAIS | Brasil | 3136405 | 31 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 435f465c-9872-39fb-bd0d-8a08c87db82a | -17.58306 | -44.53017 | 2025-09-08 03:15:00 | NOAA-21 | VÁRZEA DA PALMA | MINAS GERAIS | Brasil | 3170800 | 31 | 33 | nan | nan | nan | Cerrado | 2.9 |
| b670cbee-ffac-3559-9bad-57d94ff775c2 | -17.15039 | -44.43594 | 2025-09-08 03:15:00 | NOAA-21 | JEQUITAÍ | MINAS GERAIS | Brasil | 3135605 | 31 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 29b58d2c-1608-332c-8725-c0dca6c7d369 | -17.59052 | -44.54787 | 2025-09-08 03:15:00 | NOAA-21 | VÁRZEA DA PALMA | MINAS GERAIS | Brasil | 3170800 | 31 | 33 | nan | nan | nan | Cerrado | 3.2 |
| b28edd1b-9a70-3b73-a3b4-894c4f750d2f | -15.29686 | -43.38203 | 2025-09-08 03:15:00 | NOAA-21 | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Caatinga | 8.1 |
| 08ba60f3-aaee-31b3-9c9f-dc1d321e6fab | -17.66939 | -44.19243 | 2025-09-08 03:15:00 | NOAA-21 | JOAQUIM FELÍCIO | MINAS GERAIS | Brasil | 3136405 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| b3f3b379-801d-3c30-aba3-f47dcad6cf17 | -18.14221 | -43.40271 | 2025-09-08 03:15:00 | NOAA-21 | COUTO DE MAGALHÃES DE MINAS | MINAS GERAIS | Brasil | 3120102 | 31 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 8a768eba-251c-36c2-ad02-dd2d1684c4c3 | -15.29539 | -43.3887 | 2025-09-08 03:15:00 | NOAA-21 | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Caatinga | 8.1 |
| 0b317e72-5659-3210-a7ec-016a7f64fc8b | -17.66236 | -44.19142 | 2025-09-08 03:15:00 | NOAA-21 | JOAQUIM FELÍCIO | MINAS GERAIS | Brasil | 3136405 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| a995b3cf-e2de-3f2a-b9c3-e606295298da | -17.53707 | -43.73666 | 2025-09-08 03:15:00 | NOAA-21 | OLHOS-D'ÁGUA | MINAS GERAIS | Brasil | 3145455 | 31 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 18d36b4d-c24b-387f-bde5-253a7348fb6c | -17.1639 | -44.44167 | 2025-09-08 03:15:00 | NOAA-21 | JEQUITAÍ | MINAS GERAIS | Brasil | 3135605 | 31 | 33 | nan | nan | nan | Cerrado | 5.2 |
| a4ab15d8-caea-3182-ba35-76bd0af8ce5e | -16.08142 | -43.63605 | 2025-09-08 03:15:00 | NOAA-21 | CAPITÃO ENÉAS | MINAS GERAIS | Brasil | 3112703 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 92b5b86a-226e-3e09-a866-26635447ecfc | -17.5924 | -44.54006 | 2025-09-08 03:15:00 | NOAA-21 | VÁRZEA DA PALMA | MINAS GERAIS | Brasil | 3170800 | 31 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 06c49efe-4d25-3b27-8790-d1a00dfec2bc | -15.66849 | -39.16769 | 2025-09-08 03:15:00 | NOAA-21 | CANAVIEIRAS | BAHIA | Brasil | 2906303 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| ebce2c8c-304f-365f-bd30-6eba2a5b6f2c | -15.29832 | -43.37538 | 2025-09-08 03:15:00 | NOAA-21 | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Caatinga | 3.2 |
| 1cf73059-b0c5-3d6a-9e2e-c8b4d41aba42 | -17.15723 | -44.43843 | 2025-09-08 03:15:00 | NOAA-21 | JEQUITAÍ | MINAS GERAIS | Brasil | 3135605 | 31 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 9e8fb3b0-b151-3a25-9cde-c5556fd09a97 | -15.28998 | -43.38046 | 2025-09-08 03:15:00 | NOAA-21 | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Caatinga | 3.3 |
| c4a5528f-60dc-3e0d-8efe-10f243279459 | -17.58839 | -44.53901 | 2025-09-08 03:15:00 | NOAA-21 | VÁRZEA DA PALMA | MINAS GERAIS | Brasil | 3170800 | 31 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 2f35f7b7-c1e4-3d98-b02b-6ead7bc63cbc | -21.21923 | -44.02361 | 2025-09-08 03:17:00 | NOAA-21 | PRADOS | MINAS GERAIS | Brasil | 3152709 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| 13be20c0-dcf5-355d-a965-6b17a3905284 | -21.21779 | -44.02954 | 2025-09-08 03:17:00 | NOAA-21 | PRADOS | MINAS GERAIS | Brasil | 3152709 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |


[Clique aqui para ver as próximas entradas](README18.md)
