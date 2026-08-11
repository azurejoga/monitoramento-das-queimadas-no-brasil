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
| 2b60dc26-8d10-3b08-bc00-0e5fb133c39c | -2.96184 | -49.26715 | 2026-08-11 04:32:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 16.1 |
| a85e9655-f5e0-39c8-bb6e-1f4e30408e91 | -4.26061 | -48.19267 | 2026-08-11 04:32:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 462d73d6-9de0-33af-a679-eecda8667523 | -4.3127 | -46.41846 | 2026-08-11 04:32:00 | NOAA-21 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2c707bbe-b874-38df-856e-f8ae875baf72 | -0.86971 | -47.9284 | 2026-08-11 04:32:00 | NOAA-21 | SÃO JOÃO DA PONTA | PARÁ | Brasil | 1507466 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| bcfae157-1cf4-31ee-ac2a-c0dc5dae7551 | -3.4902 | -50.05145 | 2026-08-11 04:32:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| b1a2566f-ee0d-32d7-b2d8-651747d5d066 | -5.34689 | -45.16677 | 2026-08-11 04:32:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 0d59139b-dc47-3fa9-a72f-55602de4d070 | -4.45685 | -47.91804 | 2026-08-11 04:32:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| a412fb41-e296-3302-8183-be8560c5c5d8 | -4.26834 | -48.18675 | 2026-08-11 04:32:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 45.1 |
| e80065ab-ccc0-3e9e-a911-dd1b82c40ccd | -2.50762 | -51.81352 | 2026-08-11 04:32:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| e2b4f452-ce22-3798-aaaa-da9e4a9892ef | -0.86915 | -47.93194 | 2026-08-11 04:32:00 | NOAA-21 | SÃO JOÃO DA PONTA | PARÁ | Brasil | 1507466 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 294a2d23-61d5-3250-b6df-aea0cef0d11b | -4.39708 | -50.96961 | 2026-08-11 04:32:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8083ea39-44eb-3dce-82bb-c066b96419a8 | -4.40004 | -50.9745 | 2026-08-11 04:32:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e091787e-4ca4-3d20-ab77-e02d57043c57 | -4.27166 | -48.18726 | 2026-08-11 04:32:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 45.1 |
| d59cbc57-06fa-3f04-ab3c-5a26c981f793 | -2.95958 | -49.25912 | 2026-08-11 04:32:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 9f6c3b23-6956-3bee-a5fe-9f6e16c809e6 | -5.80492 | -43.63799 | 2026-08-11 04:32:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| ff0d3c5d-ec0c-3aa6-996a-29cdaf012aee | -2.80949 | -48.59097 | 2026-08-11 04:32:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 50cd5854-04d3-3afe-adc1-d2f9d6eea064 | -2.7066 | -49.50512 | 2026-08-11 04:32:00 | NOAA-21 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b187634c-604c-3376-a039-4aa90f047baa | -4.62497 | -48.03692 | 2026-08-11 04:32:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| dc59f196-387c-33a2-9130-3668065c7a45 | -6.31539 | -44.82148 | 2026-08-11 04:32:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| d095a945-3f77-333a-a2bd-189b3d74e1e2 | -2.50909 | -51.82938 | 2026-08-11 04:32:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8687dd39-176a-31e2-95a2-1209fdad13ed | -2.96302 | -49.25966 | 2026-08-11 04:32:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 11.9 |
| b281360d-c94a-3067-8dd0-e464538619c9 | -7.14595 | -37.78204 | 2026-08-11 04:32:00 | NOAA-21 | OLHO D'ÁGUA | PARAÍBA | Brasil | 2510402 | 25 | 33 | nan | nan | nan | Caatinga | 1.7 |
| ded73dfb-14c7-3ed3-9cf7-2df54d20b15d | -1.18103 | -47.61388 | 2026-08-11 04:32:00 | NOAA-21 | IGARAPÉ-AÇU | PARÁ | Brasil | 1503200 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| ac7664fa-77a4-3266-9351-ee65c0d6745f | -2.51049 | -51.82755 | 2026-08-11 04:32:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 78e49440-f59d-363f-b122-2855381ef66c | -2.96243 | -49.2634 | 2026-08-11 04:32:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 16.1 |
| 6840c98a-c159-3918-97e0-f664b1b6f218 | -4.30936 | -46.41795 | 2026-08-11 04:32:00 | NOAA-21 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d8b1f6ad-d033-32c9-887d-4d6a89355924 | -3.66452 | -48.9749 | 2026-08-11 04:32:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| cd675a2b-5965-3f4f-82c7-1e498c2fe634 | -2.69002 | -48.20811 | 2026-08-11 04:32:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 3163726d-a10e-3083-a472-309fbfec45f4 | -4.4599 | -55.43981 | 2026-08-11 04:32:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 17e9a3e4-d075-3143-a59f-1cee690e89fa | -4.40144 | -50.96593 | 2026-08-11 04:32:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 552aaaac-cae6-3c7b-b923-265d7e818202 | -4.40074 | -50.9702 | 2026-08-11 04:32:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 98b32e5a-d392-332a-8ede-c5e5948a9734 | -5.10472 | -46.94567 | 2026-08-11 04:32:00 | NOAA-21 | JOÃO LISBOA | MARANHÃO | Brasil | 2105500 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| c0e5d3b0-6ff7-367c-84dd-9802d0dbfcc3 | -6.12718 | -42.95264 | 2026-08-11 04:32:00 | NOAA-21 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 87644869-101a-318d-9b09-783b846b6b7d | -3.4825 | -47.68697 | 2026-08-11 04:32:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 5f46bf2c-9f90-3b09-95c2-18308f97d525 | -5.13235 | -48.33774 | 2026-08-11 04:32:00 | NOAA-21 | SÃO PEDRO DA ÁGUA BRANCA | MARANHÃO | Brasil | 2111532 | 21 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 765ab9f3-c4bc-3d93-9b91-85b2381d9f04 | -4.39777 | -50.96534 | 2026-08-11 04:32:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6f10512a-b84a-3fbf-8257-8c3f664fdb1e | -13.57406 | -46.2702 | 2026-08-11 04:34:00 | NOAA-21 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 14.3 |
| 08ffb347-e2ab-3a34-b075-fb16bf0b863b | -8.89775 | -60.58185 | 2026-08-11 04:34:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 7.2 |
| efbfe58e-00e0-3b02-befb-6d66bf8dd402 | -6.84255 | -56.41171 | 2026-08-11 04:34:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 191b8b78-ab4d-3793-9c3a-c82619807793 | -13.56374 | -46.29045 | 2026-08-11 04:34:00 | NOAA-21 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 15.5 |
| 3c43e6dd-0455-3126-8718-e30adc5a06e5 | -10.49664 | -46.61388 | 2026-08-11 04:34:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 60b0c56e-8747-344b-8032-d4c253013c4e | -10.24414 | -45.85778 | 2026-08-11 04:34:00 | NOAA-21 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 4.4 |
| dc9f38b8-d6f3-35ce-b812-7ea75ac16d67 | -10.42176 | -46.64188 | 2026-08-11 04:34:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 12.9 |
| 75555b33-88f7-3e23-ac5e-03a938a0b5eb | -13.55828 | -46.30271 | 2026-08-11 04:34:00 | NOAA-21 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 31237e97-4629-32de-a035-f6bb4fb7ebe9 | -8.89875 | -60.57669 | 2026-08-11 04:34:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 85c25e1e-e1e5-30eb-a6b4-16666662bed0 | -6.84795 | -59.10046 | 2026-08-11 04:34:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 2f652fc3-827f-3211-a4d9-91c101f93978 | -7.66042 | -44.38644 | 2026-08-11 04:34:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.1 |
| c7bcf570-dd7a-34c9-9211-d022b88cbe2c | -7.62688 | -42.76362 | 2026-08-11 04:34:00 | NOAA-21 | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 3b2da614-c372-3b6d-8e42-ab10320b0b26 | -11.64539 | -51.64927 | 2026-08-11 04:34:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 3ffca785-0593-348b-8189-a915913d949f | -11.96536 | -46.34655 | 2026-08-11 04:34:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 25ea29ab-9d4b-3eeb-9a9d-25f8ec8abdba | -10.49173 | -50.29807 | 2026-08-11 04:34:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 696643f2-2eba-35c0-9ceb-f09f0ab13573 | -7.72388 | -46.22486 | 2026-08-11 04:34:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 3bf95b82-bdb9-3e60-8789-faea5ddcc1ba | -10.72621 | -47.91772 | 2026-08-11 04:34:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 852147c5-4b49-3ba2-97de-a92e713eadc5 | -12.47723 | -45.31834 | 2026-08-11 04:34:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 1de1d29c-d7db-3afe-b1bd-df5a2163fda2 | -12.48673 | -45.30549 | 2026-08-11 04:34:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 14.4 |
| abd29d51-8d72-3099-a349-3a038fd07010 | -10.73008 | -47.91475 | 2026-08-11 04:34:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 6ff3e661-7700-3d95-bf1b-3b7e4b3f40a1 | -11.22266 | -54.85137 | 2026-08-11 04:34:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 149ddff9-5d6e-310e-93b2-7bd24f2c1140 | -10.10379 | -46.19451 | 2026-08-11 04:34:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| e3950bd3-e016-3dc2-9310-49ae191659da | -7.39144 | -42.87097 | 2026-08-11 04:34:00 | NOAA-21 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 49473c0d-1770-3f0b-aec3-63171ac5da2f | -12.12784 | -47.18113 | 2026-08-11 04:34:00 | NOAA-21 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 1bdfe631-4262-39da-83bf-88b9bf7e3caf | -11.31886 | -45.22537 | 2026-08-11 04:34:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 7eb40474-c8a9-3a0a-9c3c-d6b7cb2505bf | -12.47788 | -45.31369 | 2026-08-11 04:34:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| cfd4397c-be10-3c79-aed4-b30b9bde002f | -11.47262 | -44.5707 | 2026-08-11 04:34:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 40003250-79fd-39a2-846c-78ab81db560c | -11.24463 | -54.87531 | 2026-08-11 04:34:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 9924ac06-ec15-3156-92cd-d8912912ba60 | -11.47108 | -46.65665 | 2026-08-11 04:34:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 1f7a1b5c-356e-3bfd-8dc7-2555c0708e2a | -7.62013 | -42.78156 | 2026-08-11 04:34:00 | NOAA-21 | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 9a01ec8d-f9d5-3747-b895-b2d50e04b03e | -13.60555 | -46.23751 | 2026-08-11 04:34:00 | NOAA-21 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| dce15996-70e4-39a0-a53d-62a3817103c4 | -9.39065 | -47.4549 | 2026-08-11 04:34:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 2f1c247a-f5f7-3268-b8b8-91feda6bdf40 | -11.0196 | -45.64257 | 2026-08-11 04:34:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| d7f45ef1-9b91-39fe-a993-7f28e66c1ede | -11.46818 | -46.65223 | 2026-08-11 04:34:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| b8293918-b51f-376c-a06e-8089c654a6c0 | -12.49003 | -45.28204 | 2026-08-11 04:34:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 29f3c64a-f22c-3693-8137-63b5026c7abe | -10.41617 | -46.67955 | 2026-08-11 04:34:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 92ea67e0-953d-360d-acfc-2a791dda734c | -8.93916 | -60.50349 | 2026-08-11 04:34:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 12.6 |
| 88fabff5-a4bb-3ba2-ad83-78a5d8348a5b | -7.72044 | -46.2244 | 2026-08-11 04:34:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 1ee41b12-eb30-3dc5-acc5-c3da371deefb | -13.51936 | -44.14168 | 2026-08-11 04:34:00 | NOAA-21 | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 99583d40-dae5-313d-a038-6c7feba1e868 | -13.51527 | -44.14092 | 2026-08-11 04:34:00 | NOAA-21 | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 2aaf6081-66d8-395c-880e-b32fe4220f39 | -11.28843 | -44.87179 | 2026-08-11 04:34:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| b16683df-cf59-3b59-b261-e204d658cbb5 | -8.8954 | -60.56005 | 2026-08-11 04:34:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 8b5201a5-05a5-37a9-99dd-cad05971d2a6 | -6.77712 | -42.97668 | 2026-08-11 04:34:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| c9bd97e8-e26b-3a56-b965-ed1b802e8352 | -8.94785 | -60.52647 | 2026-08-11 04:34:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 8.8 |
| 2feaec75-d935-35cc-8485-c346d2ed64ba | -9.3873 | -47.45438 | 2026-08-11 04:34:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ae261b01-e40e-39dd-a889-d80d9494116d | -9.47882 | -60.52793 | 2026-08-11 04:34:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 16625b23-a267-316c-a3b1-5081ceb8d00e | -8.90143 | -60.58612 | 2026-08-11 04:34:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 5a3adb55-504a-3cc0-9c88-dc66abd1bfaa | -12.23885 | -47.30605 | 2026-08-11 04:34:00 | NOAA-21 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| fb277142-0952-3683-a038-d3e4240b2459 | -13.59648 | -46.24935 | 2026-08-11 04:34:00 | NOAA-21 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 0a13995d-66f9-35eb-ad84-2108771897e0 | -11.9643 | -47.31525 | 2026-08-11 04:34:00 | NOAA-21 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| eab3595b-918b-3f26-8716-a55434879b2d | -11.46878 | -46.62431 | 2026-08-11 04:34:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d2a56591-bbf6-358d-9e06-b255a6bbb137 | -10.7145 | -47.90492 | 2026-08-11 04:34:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 9a1018f3-5eb9-388b-afb6-b1e578c0c2f6 | -7.5964 | -42.77031 | 2026-08-11 04:34:00 | NOAA-21 | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 2db406eb-130a-39b8-b246-4e9608189a6b | -11.27756 | -46.58011 | 2026-08-11 04:34:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 665b46f6-a695-3457-90f5-e40d04f9ca92 | -12.32329 | -54.12162 | 2026-08-11 04:34:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6b8ab7b3-aa63-30c2-a3b9-df989d6cccec | -8.23983 | -46.24319 | 2026-08-11 04:34:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| db3388dd-7bc3-3ed1-a8ec-b49632bf1176 | -13.55705 | -46.31123 | 2026-08-11 04:34:00 | NOAA-21 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 28.5 |
| aea657ae-cd09-3c30-a45d-ac6b5a477019 | -13.26305 | -43.54194 | 2026-08-11 04:34:00 | NOAA-21 | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| f2416f54-a536-3c39-b839-2189bb302b89 | -13.56729 | -46.31708 | 2026-08-11 04:34:00 | NOAA-21 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 2893c4f8-b4d7-3e80-b0b0-2996d1fb2dd4 | -8.36795 | -46.39249 | 2026-08-11 04:34:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 7406ec6a-83e2-3b84-9cc2-d25542b692b0 | -13.57521 | -46.28786 | 2026-08-11 04:34:00 | NOAA-21 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 7c74359e-0342-3385-96bd-f9cdc0a96370 | -10.41721 | -46.64872 | 2026-08-11 04:34:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 14.1 |
| 60337d7e-6e21-35e2-a533-bc8264d18fb8 | -6.00948 | -47.40313 | 2026-08-11 04:34:00 | NOAA-21 | RIBAMAR FIQUENE | MARANHÃO | Brasil | 2109551 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 201489f1-8330-397e-9941-57f8b69ce78a | -11.26159 | -44.89645 | 2026-08-11 04:34:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |


[Clique aqui para ver as próximas entradas](README12.md)
