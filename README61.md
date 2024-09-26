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

## Dados Diários - Página 61

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 5853d2ee-ba39-3254-aaa0-7334a6b8a63e | -8.68633 | -44.74448 | 2024-09-26 04:06:00 | NOAA-20 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| a9de6677-4579-3430-8640-92226b41f4a5 | -8.24583 | -44.86581 | 2024-09-26 04:06:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| fc52b4db-4946-3e85-972a-d5ff934fc28c | -8.23419 | -44.84708 | 2024-09-26 04:06:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| e72258a2-61d5-3b5f-917b-87440d4564ee | -8.2335 | -44.85119 | 2024-09-26 04:06:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| bbb82232-cade-3306-9b14-6c5d33d9061f | -8.23282 | -44.8553 | 2024-09-26 04:06:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 0a12ee17-87dd-3888-8753-9b3dd66cbcbc | -8.62451 | -44.05908 | 2024-09-26 04:06:00 | NOAA-20 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| aa83d92f-73cf-34a5-83dd-29db88edbf2a | -8.55012 | -44.06663 | 2024-09-26 04:06:00 | NOAA-20 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 5.6 |
| c1f32f24-95c3-3bee-89f7-39529044ea0b | -8.37128 | -45.39587 | 2024-09-26 04:06:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| d783af5b-8420-31d8-909d-fdf93de641b2 | -8.69891 | -44.80089 | 2024-09-26 04:06:00 | NOAA-20 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ac3ae5f1-16eb-33f0-9971-bdc681bd4b82 | -10.45188 | -45.80518 | 2024-09-26 04:06:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 3c07fb89-9327-31e8-bb59-4d63512d8e48 | -10.45044 | -45.81392 | 2024-09-26 04:06:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |
| b2819e6d-3a15-387a-8b31-4d8b27b9939c | -10.44972 | -45.81829 | 2024-09-26 04:06:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 9cf4e631-91dc-3f52-a066-0aa2daa6d510 | -10.44749 | -45.8089 | 2024-09-26 04:06:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 247719fc-2b5f-39b5-a0a7-f5bd1931a284 | -10.44677 | -45.81327 | 2024-09-26 04:06:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |
| ddd99cac-a315-310f-905f-37280a6d5755 | -10.44634 | -45.81126 | 2024-09-26 04:06:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 181a6c83-8fa3-34d8-8a9f-8acdc268d114 | -10.44605 | -45.81765 | 2024-09-26 04:06:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d908f7cc-4a03-3e74-abf0-890587c0d379 | -10.44559 | -45.81563 | 2024-09-26 04:06:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 7.4 |
| ac836c50-cb07-3dcb-8ce5-401090aab900 | -10.44311 | -45.81263 | 2024-09-26 04:06:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| e5742d36-4e83-3a06-9dea-babc76ad9425 | -12.12074 | -45.04985 | 2024-09-26 04:06:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 9fcecb28-9e96-330f-9b24-7aaa8a24f92d | -12.11793 | -45.04531 | 2024-09-26 04:06:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 30b141fe-8654-37c2-b200-9b1e5ef29ccd | -12.11727 | -45.04922 | 2024-09-26 04:06:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 5592cab5-ec0d-378e-9af5-8ba74ff0eae4 | -11.86282 | -45.52936 | 2024-09-26 04:06:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 0.1 |
| 60b18910-796b-31db-bc98-35de36308e23 | -11.86215 | -45.53337 | 2024-09-26 04:06:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 0.1 |
| dc677c59-2379-3a43-825c-09a65da0ad16 | -11.78343 | -45.55135 | 2024-09-26 04:06:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ad1dda86-9d4b-3106-b073-9c119cb7d07c | -11.77985 | -45.55083 | 2024-09-26 04:06:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 041fecb1-1e5a-3abe-a691-60dd3df49033 | -11.77821 | -45.5165 | 2024-09-26 04:06:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 80072c96-2f83-311c-baa2-3292fca16f26 | -11.77752 | -45.52065 | 2024-09-26 04:06:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| dca0a5ff-55a7-33d3-8fbb-b3c09ce1e5f1 | -11.77463 | -45.51605 | 2024-09-26 04:06:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 64f269c6-3e50-3827-9300-313e6fbf64d8 | -11.77105 | -45.51558 | 2024-09-26 04:06:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f5889282-c026-30b5-a949-ffe18d397100 | -11.45575 | -45.72417 | 2024-09-26 04:06:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c36e4e0c-9955-358b-8f9d-1f309a4dd780 | -11.22897 | -45.39439 | 2024-09-26 04:06:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| edee6025-cd16-3ed2-8f89-9f5bb6b3e922 | -11.2275 | -45.49144 | 2024-09-26 04:06:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 3cd8e673-24ff-33df-82c5-3a734c2dfa87 | -11.2268 | -45.49562 | 2024-09-26 04:06:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 80675360-5bb5-3bad-a3d9-70fa6e6d4285 | -11.22611 | -45.4998 | 2024-09-26 04:06:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| eff38028-2f70-3483-8879-53b7676559ff | -11.22542 | -45.50395 | 2024-09-26 04:06:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 1fa9f2fc-df86-32f6-bbf4-7a1936319ff5 | -11.2246 | -45.48676 | 2024-09-26 04:06:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e465a329-9a1f-3b39-a351-bad1e149a8c0 | -11.22338 | -45.51624 | 2024-09-26 04:06:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 54490e9a-8808-351d-b26d-833f7854831a | -11.22312 | -45.47355 | 2024-09-26 04:06:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 51c933a1-049f-33b2-9541-54f9050170a8 | -11.22171 | -45.48204 | 2024-09-26 04:06:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| d4b4b3ee-990d-3cd7-b6b9-2e556cbd0c02 | -11.22024 | -45.46879 | 2024-09-26 04:06:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| f63a9dbb-efe1-3549-88a4-6c2095c7bb1f | -11.2198 | -45.51558 | 2024-09-26 04:06:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 00bb68c7-cae9-3326-9f2a-e7da6c9bacfb | -11.21953 | -45.47303 | 2024-09-26 04:06:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| f75a5e73-9474-3af1-a859-e0eae2776a50 | -11.21856 | -45.54515 | 2024-09-26 04:06:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 10.9 |
| d3d0722c-57d5-3919-95fb-8d7359fb59a0 | -11.21787 | -45.54933 | 2024-09-26 04:06:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 10.9 |
| 0399008a-1aa2-39bc-8369-903bd5f7612d | -11.21636 | -45.53624 | 2024-09-26 04:06:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 137cc3b3-49ef-3bd6-bc44-b72e386aac71 | -11.21567 | -45.54039 | 2024-09-26 04:06:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 5715c5a7-376f-3bae-a7f8-bcf3de4d7eaf | -11.21498 | -45.54454 | 2024-09-26 04:06:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 10.9 |
| 28ca49ee-a305-3447-8613-d8d203064c3e | -11.21482 | -45.52341 | 2024-09-26 04:06:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| cec08773-90a6-3e7a-9474-e6ffb90d55da | -11.21429 | -45.54871 | 2024-09-26 04:06:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 10.9 |
| 6a749e1c-1006-3cf6-9595-4db5fa67ad62 | -11.21359 | -45.55288 | 2024-09-26 04:06:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 8.7 |
| 13b69420-d469-32d1-8d86-c741833237de | -11.21278 | -45.53564 | 2024-09-26 04:06:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 6fe75877-f244-3d6f-bc4a-da2f94cce79d | -11.21209 | -45.53977 | 2024-09-26 04:06:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 8bd98c0b-eb93-33ff-9ea0-e08441bec9a6 | -11.2114 | -45.54393 | 2024-09-26 04:06:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 19.7 |
| 56039797-6383-371d-b65d-96c15f81adfb | -11.21122 | -45.52288 | 2024-09-26 04:06:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| a24731e7-5452-390c-9fbe-048139176d4d | -11.2107 | -45.54809 | 2024-09-26 04:06:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 19.7 |
| a77dffd0-2d3b-30d4-aa46-9eaf2d2a0ac0 | -11.21001 | -45.55227 | 2024-09-26 04:06:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| c521543a-3c33-359e-a45e-750620e6f020 | -11.20851 | -45.53915 | 2024-09-26 04:06:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 77e17174-2e78-3cdd-87f7-c18ec9b296fe | -11.20781 | -45.54331 | 2024-09-26 04:06:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 19.7 |
| e0ac6bd5-5dea-3e64-9d4c-7bb228e73168 | -11.20763 | -45.52231 | 2024-09-26 04:06:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 4339cf91-5408-3774-b969-1d093599cc64 | -11.20712 | -45.54748 | 2024-09-26 04:06:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 19.7 |
| bf5b4bb6-2b90-3f45-aa75-0ca06b94b8c8 | -11.20642 | -45.55166 | 2024-09-26 04:06:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 017ba712-607e-33aa-9b9d-ee15230071c4 | -11.2063 | -45.53028 | 2024-09-26 04:06:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 2800b50a-8cb3-3a05-8243-01574f4a9d80 | -11.20561 | -45.5344 | 2024-09-26 04:06:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 80dc86b1-8e01-33da-a2e1-6cf93ff294bf | -11.20492 | -45.53854 | 2024-09-26 04:06:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 5c2a271e-2781-3369-810d-57e65a07573b | -11.20423 | -45.5427 | 2024-09-26 04:06:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 4e7a9589-8b32-3048-bd37-99bf88ed5a99 | -11.20353 | -45.54688 | 2024-09-26 04:06:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 5277e3a6-99c9-3aed-b7e5-52d69a61d303 | -11.20338 | -45.5257 | 2024-09-26 04:06:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 96bd6e32-fab4-37dd-817b-5b88cf48d108 | -11.20272 | -45.52968 | 2024-09-26 04:06:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 04b06307-93eb-3ba9-b7b2-e786dbdf982b | -11.19606 | -45.48154 | 2024-09-26 04:06:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 360ea2c5-7cb0-39ac-8340-a72c1b24601a | -11.19316 | -45.47686 | 2024-09-26 04:06:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| fdf1cd9d-759f-3d92-9d06-f3a5dda92d9c | -11.18983 | -45.54057 | 2024-09-26 04:06:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 0855c911-16c6-3782-8e1d-f2b3099aa25f | -11.17541 | -45.53857 | 2024-09-26 04:06:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| e29bd49e-974a-38f4-94a0-4a4594b77de1 | -11.17401 | -45.54691 | 2024-09-26 04:06:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 409e3dee-9387-3f04-bee9-c39d4f3d0654 | -11.17112 | -45.54215 | 2024-09-26 04:06:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| abf0ae63-1936-396f-8714-998698571097 | -11.1667 | -45.50284 | 2024-09-26 04:06:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 9469f54e-4d82-3745-9e79-df3f87b099e8 | -10.92103 | -45.52884 | 2024-09-26 04:06:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 14.7 |
| 84b1db80-7092-3e72-9f2f-4971153b3bd0 | -10.92033 | -45.53305 | 2024-09-26 04:06:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 7.8 |
| eaaeb76a-7b42-3d0c-a0e1-3740ee662da8 | -10.91743 | -45.5282 | 2024-09-26 04:06:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 7b5f745f-2b01-361c-b9f6-cdddadd97985 | -10.91674 | -45.53241 | 2024-09-26 04:06:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 7a70abf8-26e5-3a20-aa12-469967026170 | -10.79156 | -45.81233 | 2024-09-26 04:06:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 148baac7-671b-3922-9438-a6b568993ef8 | -10.79081 | -45.81669 | 2024-09-26 04:06:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 69c15454-c0ef-3e59-ab46-004a42d80871 | -11.2511 | -46.11519 | 2024-09-26 04:06:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 1ce9b372-c607-3b0b-ad9d-2ee0d2f4cd2b | -11.24154 | -46.10425 | 2024-09-26 04:06:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 9ca15f12-26a7-33ec-b27f-ac564a007c8b | -11.24077 | -46.10888 | 2024-09-26 04:06:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| be051f6a-7c8f-390f-8b8a-bc09739cd1aa | -6.0041 | -46.55178 | 2024-09-26 04:06:00 | NOAA-20 | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 61ec8ad6-22b2-3ffc-98ff-a548ac3964d7 | -5.73957 | -46.46405 | 2024-09-26 04:06:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 8f26ffe9-10fc-3598-8740-09b1e7108b22 | -5.73188 | -46.4852 | 2024-09-26 04:06:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 50415070-e84a-3519-9d63-dce1f460c30c | -5.72779 | -46.4845 | 2024-09-26 04:06:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 8dd96851-9054-3a09-bd16-8da5c38c8892 | -6.26776 | -45.08738 | 2024-09-26 04:06:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 966b75e5-38b0-3ada-8ae2-92071c6d239f | -6.26405 | -45.08668 | 2024-09-26 04:06:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a09181f0-a07b-34a4-9367-0c281b9820be | -7.78874 | -45.90958 | 2024-09-26 04:06:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| fc54e36d-4417-300c-829f-38e007db73b7 | -7.78795 | -45.91433 | 2024-09-26 04:06:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 67fdbc15-5016-358b-96fd-eebf57c30ce1 | -7.76962 | -46.16957 | 2024-09-26 04:06:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 0565aa44-df41-3d7e-aeac-6cbb36d8c162 | -7.76573 | -46.16892 | 2024-09-26 04:06:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| a2f402c4-8457-353e-bcc3-80c6a9154e84 | -7.50957 | -46.09101 | 2024-09-26 04:06:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| d55e7f51-c42c-3fad-8f28-db9e2ce8c2a3 | -7.30316 | -46.67149 | 2024-09-26 04:06:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| bf4824d2-04d3-3c59-a58b-4c3f620fd3da | -7.28064 | -46.60875 | 2024-09-26 04:06:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 67954295-b068-3ef4-bbac-dd7cbdde9e11 | -7.28004 | -46.61223 | 2024-09-26 04:06:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| afcd21cb-e772-335c-8e7e-477a3858c38a | -7.27662 | -46.60801 | 2024-09-26 04:06:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 56e0c56d-7807-3d9a-9246-4d31543584e7 | -7.27602 | -46.61151 | 2024-09-26 04:06:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |


[Clique aqui para ver as próximas entradas](README62.md)
