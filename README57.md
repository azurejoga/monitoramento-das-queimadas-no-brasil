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

## Dados Diários - Página 57

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 24aa1fd6-de47-3cf3-ae2c-11180e3b229c | -7.61303 | -42.5155 | 2024-10-07 04:00:00 | NOAA-20 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 5.0 |
| b011c42f-ad11-3fa6-bd08-fe4b49ee162c | -7.6124 | -42.51937 | 2024-10-07 04:00:00 | NOAA-20 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 5.0 |
| ee19d8c6-b1df-3efe-b33b-9394fa54ca1a | -7.55159 | -42.31038 | 2024-10-07 04:00:00 | NOAA-20 | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 8829ca24-8800-36e2-9f5e-5afdd3b3eeb6 | -7.14522 | -42.63061 | 2024-10-07 04:00:00 | NOAA-20 | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| a023907f-f517-30e0-95f8-017f48e52934 | -7.14459 | -42.63455 | 2024-10-07 04:00:00 | NOAA-20 | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | 3.1 |
| 0c8e9519-be29-3874-83bd-0c96141e8ce8 | -7.14363 | -42.61819 | 2024-10-07 04:00:00 | NOAA-20 | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | 3.3 |
| 88f7aee8-4932-34d4-a46a-e24f6345a9cd | -7.14299 | -42.62213 | 2024-10-07 04:00:00 | NOAA-20 | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | 3.3 |
| 81883a87-04e2-3b63-864f-de04e403bdb7 | -7.14108 | -42.63397 | 2024-10-07 04:00:00 | NOAA-20 | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 34aaf5c5-afca-3ab0-8cc7-1506490b603c | -7.14076 | -42.61369 | 2024-10-07 04:00:00 | NOAA-20 | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | 11.8 |
| a0343181-41dc-3444-a6e4-680041d30d12 | -7.14044 | -42.63791 | 2024-10-07 04:00:00 | NOAA-20 | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 741defa0-3c21-3293-abbe-72c08c1793bd | -7.14013 | -42.61762 | 2024-10-07 04:00:00 | NOAA-20 | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | 3.3 |
| b7e85996-772b-344a-b1ec-dbf3dd4ca4c7 | -7.13789 | -42.60919 | 2024-10-07 04:00:00 | NOAA-20 | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 9d6b09a9-1be0-3e69-b1cd-2030bb229974 | -7.13726 | -42.61311 | 2024-10-07 04:00:00 | NOAA-20 | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| a7a93bee-9a2e-36b4-a9c4-eed48eafb524 | -7.13693 | -42.63733 | 2024-10-07 04:00:00 | NOAA-20 | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 605638fc-e044-313a-8879-064706ecc57a | -7.13439 | -42.60862 | 2024-10-07 04:00:00 | NOAA-20 | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 6d05cc9d-0f6b-3a8a-a321-06ea5fa5c225 | -7.13406 | -42.63282 | 2024-10-07 04:00:00 | NOAA-20 | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| fc9c663a-7901-369d-95e6-d12741ef339d | -7.13342 | -42.63676 | 2024-10-07 04:00:00 | NOAA-20 | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 5eab2d28-50ee-32ad-92e8-7db078c79e74 | -7.1299 | -42.63621 | 2024-10-07 04:00:00 | NOAA-20 | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 985d40b0-8055-323d-b20d-192e2893a037 | -7.12639 | -42.63562 | 2024-10-07 04:00:00 | NOAA-20 | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| b714a8a0-aee7-357d-a154-09db304af1ea | -7.12575 | -42.63957 | 2024-10-07 04:00:00 | NOAA-20 | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| b551aee3-9fee-3335-84ba-af4b192a6e90 | -7.1245 | -42.60302 | 2024-10-07 04:00:00 | NOAA-20 | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 96673032-1afd-3728-96bb-1ffba27d2d65 | -7.12224 | -42.63898 | 2024-10-07 04:00:00 | NOAA-20 | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| fbfa1bdf-5129-346e-8a34-0751ef18adc7 | -7.12099 | -42.60247 | 2024-10-07 04:00:00 | NOAA-20 | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 8d8e6ae0-78c8-3d28-a6a4-520522281552 | -7.11874 | -42.63839 | 2024-10-07 04:00:00 | NOAA-20 | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 6071bcc9-967c-3076-89d2-621dfa6c9735 | -7.11809 | -42.64234 | 2024-10-07 04:00:00 | NOAA-20 | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 4967b4bc-e8ff-3067-b080-052b3bdacb20 | -7.11684 | -42.60585 | 2024-10-07 04:00:00 | NOAA-20 | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 2977a284-fbd8-3983-a50e-d5f8d261e787 | -7.11458 | -42.64174 | 2024-10-07 04:00:00 | NOAA-20 | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 25c80475-0e32-3d73-aff5-4f6b178fc039 | -7.11107 | -42.64115 | 2024-10-07 04:00:00 | NOAA-20 | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| a9d49a90-3203-36fc-a7ce-ad6f06a823be | -7.10756 | -42.64058 | 2024-10-07 04:00:00 | NOAA-20 | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 41177a96-9076-3b5c-b8c3-422725f68c69 | -7.10727 | -42.62032 | 2024-10-07 04:00:00 | NOAA-20 | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 97659cbb-f8e0-3f6c-a86b-7a7446f8cfd7 | -7.10663 | -42.62424 | 2024-10-07 04:00:00 | NOAA-20 | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| f43d384b-1938-38b3-95fd-c1504e80318d | -7.10599 | -42.62817 | 2024-10-07 04:00:00 | NOAA-20 | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 8285a8ca-38db-3d1a-8264-54281da4257a | -7.10534 | -42.63211 | 2024-10-07 04:00:00 | NOAA-20 | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 18dca24c-45d7-3ed0-974b-d760b4e3bab1 | -6.82712 | -42.80677 | 2024-10-07 04:00:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| a484831e-140e-3369-ae32-3b53cc8061fa | -6.82663 | -42.80556 | 2024-10-07 04:00:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 63f0b61f-32b0-3563-a418-92688cdf3c17 | -6.46869 | -43.22133 | 2024-10-07 04:00:00 | NOAA-20 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 5.8 |
| a476b660-03cc-39f6-a27e-42f409b09d83 | -6.46505 | -43.22075 | 2024-10-07 04:00:00 | NOAA-20 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 631d5950-8e59-3242-ace3-f4f4b0eb03a1 | -7.30404 | -42.25532 | 2024-10-07 04:00:00 | NOAA-20 | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 4.3 |
| 1766577a-25e9-3690-8b2b-fc4e00cb52ae | -7.3006 | -42.25474 | 2024-10-07 04:00:00 | NOAA-20 | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 4.3 |
| 3b3c12b8-49e8-36ba-9284-4da5150a3e0d | -7.29937 | -42.26233 | 2024-10-07 04:00:00 | NOAA-20 | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 3.6 |
| 80395ab7-8a75-3abb-a9c3-b88a2fe9e14a | -7.29898 | -42.24285 | 2024-10-07 04:00:00 | NOAA-20 | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 59058ba2-9579-3f96-a527-f8dacfa335cb | -6.64397 | -42.12743 | 2024-10-07 04:00:00 | NOAA-20 | BARRA D'ALCÂNTARA | PIAUÍ | Brasil | 2201176 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| c9a76015-a198-3638-ba73-41c3d3df1ab9 | -6.6399 | -42.13068 | 2024-10-07 04:00:00 | NOAA-20 | BARRA D'ALCÂNTARA | PIAUÍ | Brasil | 2201176 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| accf1da0-3bbf-3b9f-a181-523d5bd25d32 | -6.63928 | -42.13453 | 2024-10-07 04:00:00 | NOAA-20 | BARRA D'ALCÂNTARA | PIAUÍ | Brasil | 2201176 | 22 | 33 | nan | nan | nan | Caatinga | 4.9 |
| 530ec272-3364-3e6f-ac42-849f35ffe612 | -6.63582 | -42.13395 | 2024-10-07 04:00:00 | NOAA-20 | BARRA D'ALCÂNTARA | PIAUÍ | Brasil | 2201176 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| d31d4020-fc2e-31ce-a49f-3f5f1cd4e5a6 | -6.6352 | -42.1378 | 2024-10-07 04:00:00 | NOAA-20 | BARRA D'ALCÂNTARA | PIAUÍ | Brasil | 2201176 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 1a13d207-6646-3a7e-bb18-8c4112f609f2 | -9.24636 | -43.52189 | 2024-10-07 04:00:00 | NOAA-20 | CARACOL | PIAUÍ | Brasil | 2202505 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 3071e732-735a-3189-8cfa-80d81aa4d68f | -9.24567 | -43.52603 | 2024-10-07 04:00:00 | NOAA-20 | CARACOL | PIAUÍ | Brasil | 2202505 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| efd14805-4663-3c1e-9138-32c961c62e49 | -9.24497 | -43.5302 | 2024-10-07 04:00:00 | NOAA-20 | CARACOL | PIAUÍ | Brasil | 2202505 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 0f21d547-8b96-32db-82d5-d87e61ff5d13 | -9.24426 | -43.53446 | 2024-10-07 04:00:00 | NOAA-20 | CARACOL | PIAUÍ | Brasil | 2202505 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| eba0d11d-373b-3fc9-a559-742cd8cddbf2 | -9.24277 | -43.52138 | 2024-10-07 04:00:00 | NOAA-20 | CARACOL | PIAUÍ | Brasil | 2202505 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| a6ba7a76-4714-3051-8005-21cd28c4b9c6 | -8.20001 | -43.72561 | 2024-10-07 04:00:00 | NOAA-20 | COLÔNIA DO GURGUÉIA | PIAUÍ | Brasil | 2202752 | 22 | 33 | nan | nan | nan | Caatinga | 28.3 |
| 4b14df5d-ba1e-3513-9a7b-5159b4c980e5 | -8.19997 | -43.72381 | 2024-10-07 04:00:00 | NOAA-20 | COLÔNIA DO GURGUÉIA | PIAUÍ | Brasil | 2202752 | 22 | 33 | nan | nan | nan | Caatinga | 48.8 |
| f334b18c-bfaa-310d-ac2e-1ee868d6fcc9 | -8.19992 | -43.70187 | 2024-10-07 04:00:00 | NOAA-20 | COLÔNIA DO GURGUÉIA | PIAUÍ | Brasil | 2202752 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 01dd2289-3979-319f-a615-5a4af3b4fd13 | -8.19983 | -43.70361 | 2024-10-07 04:00:00 | NOAA-20 | COLÔNIA DO GURGUÉIA | PIAUÍ | Brasil | 2202752 | 22 | 33 | nan | nan | nan | Caatinga | 4.0 |
| d1b0d355-4d3b-35e3-972a-55fef59f1e57 | -8.19931 | -43.72993 | 2024-10-07 04:00:00 | NOAA-20 | COLÔNIA DO GURGUÉIA | PIAUÍ | Brasil | 2202752 | 22 | 33 | nan | nan | nan | Caatinga | 28.3 |
| 376b7cab-e462-3be7-a376-b02fc03955e7 | -8.19925 | -43.72811 | 2024-10-07 04:00:00 | NOAA-20 | COLÔNIA DO GURGUÉIA | PIAUÍ | Brasil | 2202752 | 22 | 33 | nan | nan | nan | Caatinga | 48.8 |
| 9f5a3e94-2645-3d1d-900c-083cb812d0cc | -8.19914 | -43.70786 | 2024-10-07 04:00:00 | NOAA-20 | COLÔNIA DO GURGUÉIA | PIAUÍ | Brasil | 2202752 | 22 | 33 | nan | nan | nan | Caatinga | 3.6 |
| 0ac8b53b-5a0b-3b3d-b014-18fa113ab5bf | -8.19848 | -43.71036 | 2024-10-07 04:00:00 | NOAA-20 | COLÔNIA DO GURGUÉIA | PIAUÍ | Brasil | 2202752 | 22 | 33 | nan | nan | nan | Caatinga | 3.9 |
| a244928d-c381-37ec-95e5-db3b5da39a7b | -8.19636 | -43.72496 | 2024-10-07 04:00:00 | NOAA-20 | COLÔNIA DO GURGUÉIA | PIAUÍ | Brasil | 2202752 | 22 | 33 | nan | nan | nan | Caatinga | 44.0 |
| 0cd7625c-9e8e-399f-92fe-ccd32bfec30a | -8.1956 | -43.72747 | 2024-10-07 04:00:00 | NOAA-20 | COLÔNIA DO GURGUÉIA | PIAUÍ | Brasil | 2202752 | 22 | 33 | nan | nan | nan | Caatinga | 48.8 |
| abd5f480-264c-37ff-9ca2-57eb04692d7f | -8.19341 | -43.72001 | 2024-10-07 04:00:00 | NOAA-20 | COLÔNIA DO GURGUÉIA | PIAUÍ | Brasil | 2202752 | 22 | 33 | nan | nan | nan | Caatinga | 6.6 |
| 506cc143-3461-33c2-9eac-53d6a19d86bf | -8.1927 | -43.72433 | 2024-10-07 04:00:00 | NOAA-20 | COLÔNIA DO GURGUÉIA | PIAUÍ | Brasil | 2202752 | 22 | 33 | nan | nan | nan | Caatinga | 44.0 |
| 8133300f-5b17-3569-bc66-2b86df4d8166 | -8.20353 | -43.68045 | 2024-10-07 04:00:00 | NOAA-20 | COLÔNIA DO GURGUÉIA | PIAUÍ | Brasil | 2202752 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ec464834-de67-3f9f-9fe3-0550da6eb635 | -8.20332 | -43.68216 | 2024-10-07 04:00:00 | NOAA-20 | COLÔNIA DO GURGUÉIA | PIAUÍ | Brasil | 2202752 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 781961d4-e653-32b4-8d7c-4dd209cc6c96 | -8.19968 | -43.68149 | 2024-10-07 04:00:00 | NOAA-20 | COLÔNIA DO GURGUÉIA | PIAUÍ | Brasil | 2202752 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| aebc7f90-511e-372e-8e1d-b7e6b3681614 | -9.95523 | -44.10485 | 2024-10-07 04:00:00 | NOAA-20 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Cerrado | 3.8 |
| a9d3f087-8914-3532-b8dd-a0d65193822e | -9.95452 | -44.10917 | 2024-10-07 04:00:00 | NOAA-20 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 40449d7c-943c-30f5-8e51-7199be3c7cba | -9.9538 | -44.11351 | 2024-10-07 04:00:00 | NOAA-20 | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 2f221079-f655-3d4f-b96f-0c80f5ddec89 | -9.95159 | -44.10421 | 2024-10-07 04:00:00 | NOAA-20 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| b3979018-6641-3795-8a1e-0ee5f647ab51 | -9.95087 | -44.10854 | 2024-10-07 04:00:00 | NOAA-20 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 367ab29d-6217-3859-9091-67ed5fdd85a7 | -9.94715 | -44.08579 | 2024-10-07 04:00:00 | NOAA-20 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| eca60751-cba6-3c98-8d42-8de9a2a99f74 | -9.94644 | -44.09008 | 2024-10-07 04:00:00 | NOAA-20 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| b0298e58-c242-3de2-83cb-050c4d944b3a | -9.94357 | -44.10727 | 2024-10-07 04:00:00 | NOAA-20 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 69c2376b-f7ed-3a25-909a-99ca78e17fc0 | -9.94065 | -44.10229 | 2024-10-07 04:00:00 | NOAA-20 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 225307f0-b3e3-33d0-943f-aede896df664 | -11.75319 | -44.49947 | 2024-10-07 04:00:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 46682526-bd19-363e-adb7-c2ff6c791d2a | -11.75247 | -44.5038 | 2024-10-07 04:00:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 5.9 |
| c4f4fee3-b7da-3cf5-939d-2d6d85dcdf14 | -11.74958 | -44.52111 | 2024-10-07 04:00:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 05fd05a1-9b2c-36a9-a421-c2a56c0e41c6 | -11.74955 | -44.49884 | 2024-10-07 04:00:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 43aa7334-d8b4-3d30-8aeb-86810ea1436e | -11.74883 | -44.50316 | 2024-10-07 04:00:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 893cfb65-4d41-329a-aa4f-72d14e98aa23 | -11.74811 | -44.50749 | 2024-10-07 04:00:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 1a37cdcc-be29-320a-a243-c4fb22d2c734 | -11.74738 | -44.51182 | 2024-10-07 04:00:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 657a8927-ae12-36f9-9e78-0d876b7fd6e8 | -11.74594 | -44.52047 | 2024-10-07 04:00:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 3348310f-fb54-39d5-af08-aa2e07b25f10 | -11.74519 | -44.50252 | 2024-10-07 04:00:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 7.1 |
| f057bb5c-945a-3e74-a2c3-bfcc84ddf38f | -11.74155 | -44.50188 | 2024-10-07 04:00:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a7b1fbfe-cad0-39b0-bb1d-133f1815877f | -12.40715 | -47.03257 | 2024-10-07 04:02:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 04a776de-cf87-32b2-8ae8-dab07489d3ac | -12.40647 | -47.03646 | 2024-10-07 04:02:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 94aef641-d75c-3024-b2fb-8da48376caa0 | -12.40612 | -47.06388 | 2024-10-07 04:02:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 11.9 |
| 8e473f6b-411b-3f42-969f-2e5f0e6fa59d | -12.40581 | -47.06492 | 2024-10-07 04:02:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 9.2 |
| 9dcd04f4-52b0-37e4-973b-c519ce64aab4 | -12.40578 | -47.04038 | 2024-10-07 04:02:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| cfc35ac9-9a04-3c44-b2f3-6cdc4214044a | -12.4054 | -47.06782 | 2024-10-07 04:02:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 11.9 |
| e75ef7e2-5264-3051-8416-44fcf395a110 | -12.40512 | -47.06887 | 2024-10-07 04:02:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 9.2 |
| dbd43d3b-1ada-3d3a-9702-dd582732768c | -12.40468 | -47.07178 | 2024-10-07 04:02:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 5.7 |
| e61b5a1d-cae9-39de-9058-f5514c80a7d6 | -12.40442 | -47.07285 | 2024-10-07 04:02:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| fae9e07d-2346-35e4-b412-f1cb626cc06a | -12.4044 | -47.04825 | 2024-10-07 04:02:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 581695b8-2c7f-3742-a989-655dbb43edd7 | -12.40395 | -47.07578 | 2024-10-07 04:02:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 9575bfe6-0033-3487-96fb-e42e3d2ae20c | -12.40372 | -47.07686 | 2024-10-07 04:02:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 002d3be8-69ce-3964-b0ba-9f5e7e83cd5c | -12.40371 | -47.05219 | 2024-10-07 04:02:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 8904ad1b-7183-3e5a-9ca4-8d427fd77f86 | -12.40322 | -47.07978 | 2024-10-07 04:02:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| e18c92ff-624f-32d6-98e5-bbd7c0265976 | -12.40302 | -47.08087 | 2024-10-07 04:02:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |


[Clique aqui para ver as próximas entradas](README58.md)
