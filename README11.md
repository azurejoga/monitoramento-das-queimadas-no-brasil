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

## Dados Diários - Página 11

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 6f23cc41-3ce2-303b-88ae-09d5feadf1fc | -7.27144 | -60.17789 | 2025-07-21 05:12:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 95baaa0a-7d78-3ca3-a64b-dccdc8892308 | -13.46012 | -48.02063 | 2025-07-21 05:12:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 5de7396a-7e65-3851-9c20-62580fc7789c | -10.68883 | -46.77083 | 2025-07-21 05:12:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 7d35714a-053e-3ddf-98d6-67f8bb8735f3 | -7.2369 | -60.1923 | 2025-07-21 05:12:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 06b35c53-7804-308a-83fa-dbd3c704bdc9 | -10.68559 | -56.55466 | 2025-07-21 05:12:00 | NOAA-21 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 3eaa06a6-caa3-3ff2-a21c-906950e479b2 | -10.14865 | -49.66051 | 2025-07-21 05:12:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| d00e37d1-d89e-3735-bdb0-d8aeb6960535 | -11.34009 | -54.63354 | 2025-07-21 05:12:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e79e5068-64ed-3437-abe0-5118ae41c4a0 | -10.1594 | -49.65881 | 2025-07-21 05:12:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 7068ae7c-af49-3ca4-9fcc-611bd9a6311d | -7.27904 | -60.17517 | 2025-07-21 05:12:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 18.6 |
| f6c36556-0b96-37ea-8983-64c6e5d64582 | -7.29012 | -60.17294 | 2025-07-21 05:12:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 63e3c919-bf1c-3cc6-bff1-919082836df1 | -11.96098 | -47.02693 | 2025-07-21 05:12:00 | NOAA-21 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| e05211bf-2b89-3c8d-b172-a78ca7cb74a7 | -7.28189 | -60.17962 | 2025-07-21 05:12:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 67000fc9-bd58-3d92-a2cf-20a0bae64a27 | -12.47966 | -45.87399 | 2025-07-21 05:12:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 0d1de127-1a80-3995-a51d-47f4b3543fec | -7.24388 | -60.19341 | 2025-07-21 05:12:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 7.7 |
| 865dc8ff-8333-3763-aead-0f90cf5145e4 | -8.91702 | -47.3653 | 2025-07-21 05:12:00 | NOAA-21 | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 653c36f7-a507-3aaa-ac3b-0f0e4bc44266 | -7.28315 | -60.17184 | 2025-07-21 05:12:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 18.6 |
| 6444221d-99bc-3bfd-8e04-d35ebd08b111 | -12.47898 | -45.88023 | 2025-07-21 05:12:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 77653030-8e9e-3e08-b182-8ec7d3d5cbe5 | -7.27841 | -60.17905 | 2025-07-21 05:12:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 423a3723-2804-3117-bad2-1f74a75cefdb | -10.05841 | -64.99582 | 2025-07-21 05:12:00 | NOAA-21 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 3a445f46-b983-3010-b8d2-06f8639f3399 | -10.8482 | -47.15995 | 2025-07-21 05:12:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 58622367-8308-31b8-b2e9-1be2f73a71f3 | -7.26796 | -60.17733 | 2025-07-21 05:12:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 8.8 |
| d2420510-4fba-39e7-9655-22fc7685dd19 | -7.28252 | -60.17573 | 2025-07-21 05:12:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 18.6 |
| b78cd397-af5c-3805-b13a-5b8b9bccbe74 | -8.99237 | -69.23418 | 2025-07-21 05:12:00 | NOAA-21 | MANOEL URBANO | ACRE | Brasil | 1200344 | 12 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 9dff5f73-5869-3a12-9cd7-e13f533b8d96 | -8.49608 | -64.03327 | 2025-07-21 05:12:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 904f5932-f532-37db-a50c-86087ba642fc | -10.14825 | -49.6636 | 2025-07-21 05:12:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| a08935db-df41-3677-b27a-31064578aae0 | -8.99428 | -69.23743 | 2025-07-21 05:12:00 | NOAA-21 | MANOEL URBANO | ACRE | Brasil | 1200344 | 12 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 24d8dfcf-cf6d-3424-ab25-31c3fa5cd028 | -9.54605 | -62.80701 | 2025-07-21 05:12:00 | NOAA-21 | RIO CRESPO | RONDÔNIA | Brasil | 1100262 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2d56d392-d460-3eea-acc8-af94cc962c58 | -9.01432 | -59.54129 | 2025-07-21 05:12:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 389c4009-d76d-32ca-98da-761ba9632d9a | -10.15899 | -49.66191 | 2025-07-21 05:12:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 78402fae-a15c-3252-bfef-75016dde012d | -13.09015 | -50.57355 | 2025-07-21 05:12:00 | NOAA-21 | SÃO MIGUEL DO ARAGUAIA | GOIÁS | Brasil | 5220207 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| eaf9b9ca-8351-3a29-bdaf-c76025d122bf | -10.65569 | -46.78175 | 2025-07-21 05:12:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| b05a3073-5f39-3239-b252-400548fb9356 | -10.66255 | -46.77755 | 2025-07-21 05:12:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 18.7 |
| 07bbbaa0-289f-3765-893f-d75e84b7c4f8 | -10.03772 | -59.09685 | 2025-07-21 05:12:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| ddd42967-0a9f-3dcc-9cc3-a5c3ad431335 | -10.68256 | -46.76999 | 2025-07-21 05:12:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 6.5 |
| f2bb9e2e-5c25-3ff6-99ac-caf1834e4f8e | -9.86605 | -60.29427 | 2025-07-21 05:12:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 860ccaa0-4aca-34bc-87ca-1901f1027dfa | -9.75358 | -53.2673 | 2025-07-21 05:12:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 3a202c48-b752-3ac3-817a-6b8ac5569c29 | -9.02105 | -59.54237 | 2025-07-21 05:12:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 93c45873-6a3b-39ea-a711-aebbaee73808 | -7.26671 | -60.18507 | 2025-07-21 05:12:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 49cc1f1f-0bad-3048-97a5-44f06cf1f70b | -7.95194 | -71.4577 | 2025-07-21 05:12:00 | NOAA-21 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 5647dc68-d5fb-3a8e-b770-6db822d455c9 | -11.50019 | -48.0757 | 2025-07-21 05:12:00 | NOAA-21 | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 97d17d24-7ace-3b7e-9958-e486f737f3fb | -7.25149 | -60.19062 | 2025-07-21 05:12:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 0da1a43c-2a7a-3744-acd3-41bba5eb648f | -7.29074 | -60.16905 | 2025-07-21 05:12:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 14.4 |
| d2f7857b-e3bb-351d-a845-1094fa3c5bca | -13.9019 | -48.7377 | 2025-07-21 05:12:00 | NOAA-21 | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| c4d4d34e-6032-30ff-9813-7e11699f3796 | -10.38275 | -62.76294 | 2025-07-21 05:12:00 | NOAA-21 | CACAULÂNDIA | RONDÔNIA | Brasil | 1100601 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 1d171489-3c42-3753-9bd6-a4babe3f4041 | -9.5966 | -48.54561 | 2025-07-21 05:12:00 | NOAA-21 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 8a225fdd-afa1-3fce-8222-03203d93bb49 | -11.31819 | -55.21313 | 2025-07-21 05:12:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| e5f7e2ca-9c42-383a-8c7b-d8eb9e4668ae | -8.92293 | -47.36611 | 2025-07-21 05:12:00 | NOAA-21 | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 8c94778a-ff85-37ec-8203-b9dc080f7117 | -7.23341 | -60.19176 | 2025-07-21 05:12:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 7.5 |
| bc025fec-f93b-3e88-99f9-a88deb87e4bf | -7.26384 | -60.18064 | 2025-07-21 05:12:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 8.8 |
| 88c995bf-b062-30c1-a15f-1e52ad9380a9 | -12.46936 | -46.92679 | 2025-07-21 05:12:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 78523591-c9c8-3597-9273-bc91a3fb99a3 | -8.0772 | -49.90777 | 2025-07-21 05:12:00 | NOAA-21 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3d99ca34-5265-35a0-96db-f96269dbe791 | -7.24452 | -60.18951 | 2025-07-21 05:12:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 7.7 |
| 3e0f7ed5-9eaf-3eff-a2da-edddbd9c7b9e | -12.37315 | -46.42363 | 2025-07-21 05:12:00 | NOAA-21 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 3a2bbd18-c73a-3405-8d2c-11518bb83120 | -7.28726 | -60.1685 | 2025-07-21 05:12:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 14.4 |
| cbed06d1-19ad-3010-8bc8-f614806965d4 | -7.29771 | -60.17017 | 2025-07-21 05:12:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 7.4 |
| f5abf271-8b58-38e3-a215-ace84a0a534c | -7.23626 | -60.19623 | 2025-07-21 05:12:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 14.4 |
| f93391a8-1fcb-3109-983f-9ddc8d509990 | -10.29673 | -60.54234 | 2025-07-21 05:12:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 8.5 |
| e0322eef-3189-3c42-a083-3d406bca42ac | -13.89605 | -48.73764 | 2025-07-21 05:12:00 | NOAA-21 | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 4.1 |
| e5ee8f40-9474-3889-8a68-edd3dc244144 | -13.49038 | -45.51035 | 2025-07-21 05:12:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 9c8d841d-7d5a-381b-8c57-6add04b8ea89 | -11.31755 | -55.21749 | 2025-07-21 05:12:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 0ab6384b-2043-3381-a80c-8be6d7dba684 | -7.26733 | -60.1812 | 2025-07-21 05:12:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 8.8 |
| c75162f0-4826-3bd2-b18a-b02aecc716c7 | -7.23975 | -60.19677 | 2025-07-21 05:12:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 9.6 |
| 4742cd7c-2c25-3cbd-a8fc-52f7188ecd0e | -13.09521 | -50.57424 | 2025-07-21 05:12:00 | NOAA-21 | SÃO MIGUEL DO ARAGUAIA | GOIÁS | Brasil | 5220207 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 1b7b044e-401a-3875-8ee1-d0fae83c378a | -10.67566 | -46.77439 | 2025-07-21 05:12:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 606a5a0d-3cc5-3812-a6e5-7206b509213d | -7.23277 | -60.19569 | 2025-07-21 05:12:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 14.4 |
| 9a72dca0-87fb-3d49-9198-5f655914d692 | -7.28377 | -60.16795 | 2025-07-21 05:12:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 7.4 |
| 8ffb18ad-c5fd-3af7-b273-1199b1de9baa | -8.08568 | -50.09708 | 2025-07-21 05:12:00 | NOAA-21 | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| ea88c344-451c-34e0-9350-3b3669ceb990 | -10.38006 | -62.7698 | 2025-07-21 05:12:00 | NOAA-21 | CACAULÂNDIA | RONDÔNIA | Brasil | 1100601 | 11 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 0e1fcdb0-828a-3929-a143-21a29baf5a83 | -7.28601 | -60.17628 | 2025-07-21 05:12:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 8645d90c-e3e4-36cb-ad7c-a0ef5e686d90 | -11.96497 | -47.02703 | 2025-07-21 05:12:00 | NOAA-21 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| c1edb213-8be2-31e5-9bdb-487c1cded968 | -10.66941 | -46.77339 | 2025-07-21 05:12:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 18.7 |
| 4ff02c8e-588c-336d-b30e-b7bb57ebedda | -7.27966 | -60.17128 | 2025-07-21 05:12:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 18.6 |
| 0ecfad1c-23ac-3f24-8678-a449177eace5 | -11.78333 | -46.45134 | 2025-07-21 05:12:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| f0efab01-ca6a-3fd4-816f-8adee47882a6 | -13.4922 | -45.50596 | 2025-07-21 05:12:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 7f80a076-c816-3b26-9651-0dfe46091ee4 | -7.24039 | -60.19285 | 2025-07-21 05:12:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 7.7 |
| 00d5f259-1ab7-3fa0-b4fd-86dfe2acb61a | -7.25997 | -60.11649 | 2025-07-21 05:12:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1a96fe9c-f87b-303f-9955-ec551beb5c42 | -9.01324 | -59.7647 | 2025-07-21 05:12:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| ddd497e0-7301-330c-aa71-e80e64af02f2 | -11.96157 | -47.02192 | 2025-07-21 05:12:00 | NOAA-21 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| eb57d398-c0b5-328c-88fe-1d877d4c8686 | -13.89704 | -48.73655 | 2025-07-21 05:12:00 | NOAA-21 | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 6.1 |
| cd990e54-daf7-369b-8123-9a12a508a48f | -10.68273 | -56.55034 | 2025-07-21 05:12:00 | NOAA-21 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| cbc97aae-cbfd-3c76-a7fc-dca878fea0ce | -7.29423 | -60.16961 | 2025-07-21 05:12:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 7.4 |
| 0545618c-3e00-39d7-9ae7-d83e29051b3e | -12.48575 | -45.88104 | 2025-07-21 05:12:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 7e2097e9-2e50-3822-934c-22d877a3a806 | -6.78764 | -58.63178 | 2025-07-21 05:12:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5e8d20d4-be53-34dc-a263-b694b6cf9f45 | -8.08492 | -50.10241 | 2025-07-21 05:12:00 | NOAA-21 | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| b5efecb3-6273-384d-9a4f-0ac7e4b85950 | -11.95869 | -47.0262 | 2025-07-21 05:12:00 | NOAA-21 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| f7765631-81de-3ded-bef8-ffa2792216ff | -9.75409 | -53.26373 | 2025-07-21 05:12:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 16bc5ae5-5805-3bc1-a942-feff6d5cf8f3 | -13.49104 | -45.50361 | 2025-07-21 05:12:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 948fe31f-bc29-3dfa-a7c3-bc584b8bbd88 | -10.15858 | -49.66502 | 2025-07-21 05:12:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| c0a861fb-e2eb-35b1-a163-5938463a5333 | -7.26322 | -60.18451 | 2025-07-21 05:12:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 5.1 |
| ffc3d811-8ddf-3519-88e5-990d8bcb669b | -12.49981 | -57.77927 | 2025-07-21 05:12:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 379fc5b4-581e-37b9-8452-2c1936b6bfdc | -10.13314 | -49.65846 | 2025-07-21 05:12:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 94948754-ed67-3ea2-b594-3da937fbac4a | -7.25973 | -60.18395 | 2025-07-21 05:12:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.5 |
| b1dc4ad9-6c53-34b4-87c9-7748a6990304 | -10.38355 | -49.92493 | 2025-07-21 05:12:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 8a77dbd6-c898-3e66-b737-1e04ec0d0d54 | -10.13831 | -49.65911 | 2025-07-21 05:12:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| fe6ecd6f-9df1-326c-bde6-a17a9dc985f8 | -8.71247 | -47.85856 | 2025-07-21 05:12:00 | NOAA-21 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 269cf047-3290-38e7-903f-7b568f51a6a8 | -7.24103 | -60.18894 | 2025-07-21 05:12:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 7.7 |
| 16f02b06-f1e6-3082-aa34-f1a91c5f0633 | -11.78671 | -47.55656 | 2025-07-21 05:12:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 32145214-fbcc-3d60-84b6-4035cc8a259e | -8.99155 | -69.23861 | 2025-07-21 05:12:00 | NOAA-21 | MANOEL URBANO | ACRE | Brasil | 1200344 | 12 | 33 | nan | nan | nan | Amazônia | 1.9 |
| bdf6406b-3b12-33f9-ba9f-b923c4d4756a | -11.95924 | -47.02118 | 2025-07-21 05:12:00 | NOAA-21 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| f567189e-796b-30f3-a53c-d6543f31bb6e | -20.19228 | -50.50312 | 2025-07-21 05:14:00 | NOAA-21 | VITÓRIA BRASIL | SÃO PAULO | Brasil | 3556958 | 35 | 33 | nan | nan | nan | Mata Atlântica | 4.7 |


[Clique aqui para ver as próximas entradas](README12.md)
