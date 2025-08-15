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

## Dados Diários - Página 60

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 7d5a7c53-0565-35dc-ada4-37ba28c8e912 | -9.5131 | -63.58494 | 2025-08-15 05:44:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 2f409c16-da48-3251-8e13-d18d9ebb1a58 | -10.42874 | -67.87385 | 2025-08-15 05:44:00 | NOAA-21 | CAPIXABA | ACRE | Brasil | 1200179 | 12 | 33 | nan | nan | nan | Amazônia | 1.4 |
| fa2e253f-fca9-3939-8688-dbd35ed4c791 | -8.1026 | -61.1907 | 2025-08-15 05:44:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| a1e8ac52-e396-3b7b-8960-63cbc464ab1f | -7.59114 | -63.46217 | 2025-08-15 05:44:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 8757d9c8-0b0d-3924-a551-71a21513025a | -7.9524 | -61.75061 | 2025-08-15 05:44:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 3.9 |
| a90283c9-43b1-36b2-afa9-23ff271b67e8 | -10.32582 | -64.45042 | 2025-08-15 05:44:00 | NOAA-21 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 35c453cc-5aaa-36bb-83c5-2b7145363458 | -8.59044 | -63.87379 | 2025-08-15 05:44:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 4cfce3a6-0a21-3757-8dd6-d110f00fef95 | -9.93979 | -60.47781 | 2025-08-15 05:44:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 5fca2167-05ef-3ede-9ea7-3aef8050d020 | -9.15375 | -59.69241 | 2025-08-15 05:44:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 95e6f8db-3477-3b3f-b847-0d3c443e42da | -9.16374 | -59.6851 | 2025-08-15 05:44:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| f86e6398-660e-3b4e-ab53-3e48c6034843 | -7.58709 | -63.46547 | 2025-08-15 05:44:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| fd071dbd-fce9-360f-bd68-c5068a83eadd | -8.40232 | -70.43907 | 2025-08-15 05:44:00 | NOAA-21 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 0bc78d85-c15f-385e-aff1-48f7a28a3a51 | -9.15585 | -59.42265 | 2025-08-15 05:44:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 770e1872-abe9-31f7-8c5d-49db376e6422 | -10.32567 | -63.61891 | 2025-08-15 05:44:00 | NOAA-21 | CAMPO NOVO DE RONDÔNIA | RONDÔNIA | Brasil | 1100700 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 764a78d7-b5fd-37db-b35b-5e566a2ffcb2 | -9.17994 | -59.66538 | 2025-08-15 05:44:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 8.8 |
| c19cf97c-8d2d-3ebb-a4e4-ba38a09daf4e | -7.52914 | -61.33334 | 2025-08-15 05:44:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 30.8 |
| 60a04c3a-b013-304e-b3f2-b81439127e63 | -7.61009 | -63.52371 | 2025-08-15 05:44:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 12461c62-b458-3b5c-a154-48e67775240b | -9.18998 | -59.65799 | 2025-08-15 05:44:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| feb96d7c-732a-3a78-b946-01ad722e69bf | -7.9555 | -61.75585 | 2025-08-15 05:44:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 3.9 |
| f24c62f3-ae56-30b1-8cf0-d74caa7ca0db | -7.917 | -63.50972 | 2025-08-15 05:44:00 | NOAA-21 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 75c43a17-6b5b-3462-af42-d36767b283f1 | -9.50029 | -60.53478 | 2025-08-15 05:44:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 5.3 |
| fa72371b-256f-3d61-b123-ca273d2665c4 | -11.35329 | -55.42911 | 2025-08-15 05:44:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 0d09a819-f6a5-3d41-b3b7-a729194eabb6 | -8.60662 | -62.66316 | 2025-08-15 05:44:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.1 |
| c1c8c50e-7162-39a0-899b-62dc85ec092d | -7.62412 | -63.51775 | 2025-08-15 05:44:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5b1caf8a-4f1b-3c78-85e7-e6156c614241 | -7.82277 | -61.32802 | 2025-08-15 05:44:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 99b0a4fe-88b0-3b7b-9be0-66c0c7716868 | -7.60263 | -63.50304 | 2025-08-15 05:44:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 10.0 |
| d46efe2a-c9fa-3411-856f-63b08e81bfae | -7.53477 | -61.34909 | 2025-08-15 05:44:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 9.0 |
| 61705ae3-9680-3701-a95c-a682108e47ba | -7.94861 | -61.75004 | 2025-08-15 05:44:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 81c5a50d-cdb6-38cc-aca7-a782ee66dc55 | -8.94623 | -62.23147 | 2025-08-15 05:44:00 | NOAA-21 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 44d477f7-5160-30e9-bd73-2192051a2a94 | -7.62701 | -63.52209 | 2025-08-15 05:44:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 125a77f1-97e1-325b-bcce-f1a8ec186174 | -7.60857 | -63.52708 | 2025-08-15 05:44:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| faf5c63b-e7d4-30d6-bde7-344536baef39 | -7.27933 | -64.69842 | 2025-08-15 05:44:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 537ce7a5-fcc7-3b15-b898-16d4a225072e | -7.62355 | -63.52156 | 2025-08-15 05:44:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 28bdfd12-fb70-3c33-9651-4b44aff0bd7f | -13.12274 | -57.16426 | 2025-08-15 05:44:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ef8aa96c-8994-3e46-a773-7af4700f4675 | -9.16287 | -59.65826 | 2025-08-15 05:44:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 973f8cf0-d764-38c1-848b-d374c966170c | -9.20449 | -59.65095 | 2025-08-15 05:44:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 2c70cea0-c8d1-39ec-8233-7048013a75d6 | -7.88103 | -61.81567 | 2025-08-15 05:44:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 0ec6b9ef-ac47-3226-a9a5-8941c247fa83 | -8.11222 | -61.20761 | 2025-08-15 05:44:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 1af34f63-0a78-3cfc-bcfd-5310922a4466 | -9.39169 | -60.53989 | 2025-08-15 05:44:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| d548cc36-8b3c-378a-8b79-ae6bf4751dd6 | -8.55956 | -63.9154 | 2025-08-15 05:44:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 46bba95e-e61e-3aa9-a2ec-0ddc109fde17 | -7.96466 | -63.46548 | 2025-08-15 05:44:00 | NOAA-21 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a98bbdc0-a82c-3fb8-8393-82b850acacd0 | -10.36676 | -67.71141 | 2025-08-15 05:44:00 | NOAA-21 | CAPIXABA | ACRE | Brasil | 1200179 | 12 | 33 | nan | nan | nan | Amazônia | 0.6 |
| d62e890a-ac60-35aa-baf2-05e15d5be411 | -7.8075 | -61.34406 | 2025-08-15 05:44:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 79523604-8274-340b-abb8-a7fd852929d7 | -9.1814 | -59.6877 | 2025-08-15 05:44:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 743edce0-3c23-3574-af76-15f5f74d9c97 | -7.60205 | -63.50686 | 2025-08-15 05:44:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 10.0 |
| ea8c0287-0c17-3419-a98d-894e89f0c5c4 | -13.11207 | -57.15916 | 2025-08-15 05:44:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| fc8c1977-4142-3d1d-be63-bd35d2491b51 | -8.90197 | -60.57379 | 2025-08-15 05:44:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 86fce0cd-4ccd-39d5-9a80-714e02a495d0 | -11.83427 | -55.2112 | 2025-08-15 05:44:00 | NOAA-21 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| ff125615-6d30-382a-a321-8dca86a9bebb | -9.49868 | -60.54636 | 2025-08-15 05:44:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 83d3e473-1670-3af7-ac5a-dd93f06feda0 | -7.95309 | -61.74596 | 2025-08-15 05:44:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 3c9a7482-d6f6-3ca6-a7c0-0ace907552c7 | -8.37075 | -70.14363 | 2025-08-15 05:44:00 | NOAA-21 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.8 |
| ac7d65da-fac5-311b-b2eb-d942987df5ea | -8.09939 | -61.18507 | 2025-08-15 05:44:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| ac76c326-f107-3ebb-9e42-eb3816eb1d51 | -7.8848 | -61.81625 | 2025-08-15 05:44:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 6de712ff-90eb-3f2c-b951-e8be6361791f | -11.36043 | -55.42078 | 2025-08-15 05:44:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| af955ab2-71c2-365b-8aaa-8eadcc912cce | -9.16256 | -59.69376 | 2025-08-15 05:44:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 53edb429-f22b-3ad8-a71a-9e8c2b5b91d4 | -9.49921 | -60.54251 | 2025-08-15 05:44:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 2131195a-acec-32f1-85ba-21a2d59fc977 | -10.36116 | -64.44819 | 2025-08-15 05:44:00 | NOAA-21 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e2feb749-164f-3f3d-8be4-5be7742494cb | -8.46776 | -60.58601 | 2025-08-15 05:44:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d2f6a469-27de-342f-ada7-580c65b143e9 | -11.31738 | -55.20591 | 2025-08-15 05:44:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 610e1b3f-dd40-3720-ab47-f1c21011ad68 | -8.60562 | -62.66498 | 2025-08-15 05:44:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c5fff9f6-89af-3ed4-94f2-885ba88cdd36 | -7.56036 | -61.41688 | 2025-08-15 05:44:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| b50b7303-11a1-367c-80d1-70dfc1002708 | -7.80362 | -61.34347 | 2025-08-15 05:44:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 1eaf0082-8381-3f82-b281-65f6a8fe5ba2 | -7.80678 | -61.34898 | 2025-08-15 05:44:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| f354cb7c-2291-3aa3-9049-90c3eb1254c6 | -9.16228 | -59.66262 | 2025-08-15 05:44:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| fb4be924-dd1f-3b3d-98d4-8cc98f88ec94 | -9.21275 | -59.65651 | 2025-08-15 05:44:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 758dce78-8582-3e51-8b0f-beec08ba9a5f | -9.50244 | -60.51929 | 2025-08-15 05:44:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 7.9 |
| 53bdeadf-e5cd-3a5a-9a5f-595eca332fde | -7.61606 | -63.52432 | 2025-08-15 05:44:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| caeb676c-7aac-372b-ae66-b65bb6dea7ee | -11.93023 | -63.24448 | 2025-08-15 05:44:00 | NOAA-21 | SERINGUEIRAS | RONDÔNIA | Brasil | 1101500 | 11 | 33 | nan | nan | nan | Amazônia | 3.1 |
| a5e2f8a2-be44-348e-abd2-175ab7acf96e | -9.19322 | -59.66722 | 2025-08-15 05:44:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 29cfbae4-590a-327c-ba9e-538a667f0648 | -9.15669 | -59.67066 | 2025-08-15 05:44:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 52e4a7cf-a9a8-31cd-b9bd-4ecd4e559e7d | -8.94073 | -62.21677 | 2025-08-15 05:44:00 | NOAA-21 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 60949f8f-fa16-30eb-9afe-b9c9256021c9 | -11.34995 | -55.40538 | 2025-08-15 05:44:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 6b790f25-d579-39de-88b4-3e77ad56ee10 | -7.59859 | -63.50633 | 2025-08-15 05:44:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 14.4 |
| c867c380-c7a4-3b64-8f12-ffe986419e75 | -8.92037 | -60.73137 | 2025-08-15 05:44:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f8394396-ec8d-3743-8f94-e7d25610f336 | -11.34832 | -55.41922 | 2025-08-15 05:44:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 8b17cb33-b435-3488-b76a-43acb2e4d87f | -8.47082 | -64.06272 | 2025-08-15 05:44:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| ea9cff38-043c-31fd-b7de-a4473217c729 | -13.13381 | -57.16573 | 2025-08-15 05:44:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 817ed406-7b00-34e4-8fa2-9702748949bc | -10.32981 | -64.44719 | 2025-08-15 05:44:00 | NOAA-21 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e1c948f8-a02f-3a56-bf3f-9677222afe97 | -9.17639 | -59.6914 | 2025-08-15 05:44:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 9fb4f591-6a6c-35a6-ae76-c824cd31ceed | -10.0073 | -59.22286 | 2025-08-15 05:44:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 121692ef-cd42-3661-a5c8-740e29959d6f | -7.58884 | -63.45397 | 2025-08-15 05:44:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 5f8629ff-09fd-3bff-967d-b49e5c9fd5d0 | -7.46567 | -60.41036 | 2025-08-15 05:44:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d01efbfb-2015-3975-9bc1-944d85b2fc8c | -10.35773 | -64.44767 | 2025-08-15 05:44:00 | NOAA-21 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 4c6e785c-ee5d-315d-bb8e-8b6306cec225 | -9.20892 | -59.65155 | 2025-08-15 05:44:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 62abe0a9-60aa-3bbb-9cd1-abe90a3c65d0 | -10.31743 | -63.62587 | 2025-08-15 05:44:00 | NOAA-21 | CAMPO NOVO DE RONDÔNIA | RONDÔNIA | Brasil | 1100700 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| fa8209ac-4dbb-3d56-8bb3-14322dcffbe6 | -8.55716 | -63.86093 | 2025-08-15 05:44:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 55ea83f8-3c84-39ea-8334-36b05abacb2f | -9.50975 | -60.52819 | 2025-08-15 05:44:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 0d45ee4b-cece-3105-b38c-c2ec55a64383 | -9.18115 | -59.65654 | 2025-08-15 05:44:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 7ee2b39a-b39d-39f4-b2f2-958ce7646dc7 | -9.32682 | -67.53475 | 2025-08-15 05:44:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 8b7742ec-3853-309d-9a8b-488e1b3903e9 | -7.82205 | -61.32622 | 2025-08-15 05:44:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 804d207d-0419-3197-aa4f-90b253b1d1fd | -10.0495 | -59.12008 | 2025-08-15 05:44:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 30e40313-0d8e-3850-b168-7dc58f151e8e | -9.93814 | -60.48973 | 2025-08-15 05:44:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 72abe3c2-6010-3ba6-b24a-78d3b4396bba | -7.61203 | -63.52761 | 2025-08-15 05:44:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b9ed4838-3ae3-38e3-b8ae-eb4334954fe5 | -8.59108 | -62.66279 | 2025-08-15 05:44:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 921f188c-5136-3861-8aae-1d8cb4d64f07 | -8.55556 | -63.91864 | 2025-08-15 05:44:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a2523132-ecdc-331d-af0b-2c24d71464b3 | -7.5316 | -61.34366 | 2025-08-15 05:44:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 8292eaa0-683c-3bd4-a17c-152c0b52f0f3 | -13.1172 | -57.16353 | 2025-08-15 05:44:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 12aafd72-c7ea-3cca-a7a2-9b66c948b1cf | -7.87969 | -61.82494 | 2025-08-15 05:44:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 2fa96a01-04b4-386a-b4fd-7afa69594f84 | -9.17257 | -59.68637 | 2025-08-15 05:44:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 1b65c4f5-c33a-384d-9a04-768825da8eb4 | -10.47367 | -61.32937 | 2025-08-15 05:44:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 4.3 |


[Clique aqui para ver as próximas entradas](README61.md)
