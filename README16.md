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

## Dados Diários - Página 16

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 3d2ba3ce-eeec-35d9-9af5-ef2d336dc89f | -4.91155 | -43.19762 | 2025-09-02 03:49:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 63c35c9c-e179-3244-85ec-ad5adbf44a69 | -6.27266 | -43.29591 | 2025-09-02 03:49:00 | NPP-375D | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 56b09c0e-0987-31b0-9313-d7f3f14eada4 | -7.62335 | -42.65084 | 2025-09-02 03:49:00 | NPP-375D | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| d56e5034-276d-31b4-9010-be203706acaf | -6.19945 | -45.3885 | 2025-09-02 03:49:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 7174b4b8-993a-33e9-b47e-8b5359bf7f65 | -6.92069 | -45.5645 | 2025-09-02 03:49:00 | NPP-375D | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ceb693e6-89af-371c-94dc-b95f5150cf2c | -6.86284 | -45.55797 | 2025-09-02 03:49:00 | NPP-375D | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 9f260a30-ac3c-3def-99eb-ce135e9b616e | -4.47997 | -48.1142 | 2025-09-02 03:49:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 58842bfd-e965-36b7-8bfd-f0fd1a9d4b17 | -6.72213 | -42.25913 | 2025-09-02 03:49:00 | NPP-375D | TANQUE DO PIAUÍ | PIAUÍ | Brasil | 2210979 | 22 | 33 | nan | nan | nan | Caatinga | 5.5 |
| 82dcca8b-f90c-32c9-ab30-1033742c666b | -6.42415 | -43.89139 | 2025-09-02 03:49:00 | NPP-375D | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 7.4 |
| d364fb0c-f5db-3d1c-bc58-ab4537c2797e | -6.22266 | -41.8147 | 2025-09-02 03:49:00 | NPP-375D | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 78c83405-d67d-3d4d-95d0-12a9749c3576 | -6.97743 | -44.34271 | 2025-09-02 03:49:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| dcc6f2d4-a5ea-3003-8d16-365a5d7468d3 | -4.22681 | -47.20958 | 2025-09-02 03:49:00 | NPP-375D | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 51d1221e-58c2-347b-aad0-f5a9f42684e4 | -6.25733 | -42.60823 | 2025-09-02 03:49:00 | NPP-375D | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 18a510e7-afad-360b-b7f8-9a609a64a7b4 | -3.23079 | -47.12464 | 2025-09-02 03:49:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 11.0 |
| 9fb54393-9750-3e45-9261-1da3d6719967 | -6.88442 | -43.83528 | 2025-09-02 03:49:00 | NPP-375D | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 32c55e5c-9c29-33fa-a0f1-ef5691a0fbc2 | -7.12238 | -44.57217 | 2025-09-02 03:49:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 29f77064-d5fb-3fe0-8c29-742f41154e89 | -6.86343 | -45.55473 | 2025-09-02 03:49:00 | NPP-375D | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 5feb1f37-8b19-391c-b77b-d7f10f90acf8 | -4.22603 | -47.21402 | 2025-09-02 03:49:00 | NPP-375D | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 3f3e3a9f-98b4-3e7b-8524-86c632da7c2b | -7.68997 | -40.44765 | 2025-09-02 03:49:00 | NPP-375D | ARARIPINA | PERNAMBUCO | Brasil | 2601102 | 26 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 6bedd769-cf21-3d6e-9896-745f9d2984d9 | -6.87506 | -45.8544 | 2025-09-02 03:49:00 | NPP-375D | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 53.7 |
| 2538e0d9-c2c1-3950-9f78-5f9e5631a053 | -6.95288 | -45.56431 | 2025-09-02 03:49:00 | NPP-375D | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| aeb12bcc-37e6-31b7-9294-b8cce930e028 | -6.73401 | -38.4475 | 2025-09-02 03:49:00 | NPP-375D | SÃO JOÃO DO RIO DO PEIXE | PARAÍBA | Brasil | 2500700 | 25 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 97136097-52af-3783-8842-c0417adccbcf | -6.96189 | -44.34968 | 2025-09-02 03:49:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 743532cc-42fa-3a33-a0ab-9f32f2a76a22 | -7.31239 | -44.27634 | 2025-09-02 03:49:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| eb61187c-e628-337d-88a9-a017cc8237ac | -6.88793 | -45.84344 | 2025-09-02 03:49:00 | NPP-375D | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 13.2 |
| 3928a767-9825-341e-8e05-d5b899882e1f | -6.33752 | -43.52609 | 2025-09-02 03:49:00 | NPP-375D | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 1073bd8d-5079-3f09-a0fa-40ac63ca395c | -6.62795 | -43.96004 | 2025-09-02 03:49:00 | NPP-375D | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 24b09b1b-d450-3824-a891-e8fca802d431 | -7.59776 | -37.80663 | 2025-09-02 03:49:00 | NPP-375D | JURU | PARAÍBA | Brasil | 2508000 | 25 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 66b2c07c-7596-34ca-8060-e5dfa2343021 | -6.88567 | -45.8563 | 2025-09-02 03:49:00 | NPP-375D | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 3794668f-ab3c-3c8a-b266-2e049a1d3462 | -6.97454 | -44.30415 | 2025-09-02 03:49:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 87d13a24-5785-3655-ab0a-a4ab8af74933 | -5.73194 | -45.54229 | 2025-09-02 03:49:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 43a38dbc-20ef-397e-a39f-7841352ce387 | -6.98276 | -44.31256 | 2025-09-02 03:49:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| aacfa0b3-9e4a-3a23-8437-e5ef56c49603 | -6.29926 | -43.55732 | 2025-09-02 03:49:00 | NPP-375D | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| d3b14f99-3b79-3135-88d4-b16fe770f8d5 | -6.33008 | -43.56505 | 2025-09-02 03:49:00 | NPP-375D | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a7ba4d65-56b3-34c8-b5bc-fb7da903256a | -6.88905 | -43.83607 | 2025-09-02 03:49:00 | NPP-375D | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| b6f03b93-502e-358c-9aa6-825db54d65b1 | -6.95541 | -44.3588 | 2025-09-02 03:49:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 3598060f-ad51-312d-8ea5-f5d27a0c6b86 | -6.89862 | -44.23249 | 2025-09-02 03:49:00 | NPP-375D | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| f91ea0cb-bbe6-3a41-a377-34f299013c0f | -6.98306 | -44.3387 | 2025-09-02 03:49:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 0ac2427d-c0a5-389c-a927-50bb10caac0d | -6.23269 | -41.80508 | 2025-09-02 03:49:00 | NPP-375D | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| b339ad49-cf3a-31c6-bc1b-281c817d43f2 | -3.81694 | -41.06221 | 2025-09-02 03:49:00 | NPP-375D | TIANGUÁ | CEARÁ | Brasil | 2313401 | 23 | 33 | nan | nan | nan | Caatinga | 1.4 |
| cdf084cb-2b20-30a2-bcf2-e34512c265d2 | -4.48463 | -48.11967 | 2025-09-02 03:49:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 2157115c-cbf8-3dc1-bcdb-ca2e3149b78b | -6.49673 | -45.40868 | 2025-09-02 03:49:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| c6e5eb85-0929-33df-bb86-61eed27c0747 | -6.86866 | -45.55549 | 2025-09-02 03:49:00 | NPP-375D | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| a9efaf9c-b33e-3072-ad6f-414d85eba76d | -6.54094 | -43.92184 | 2025-09-02 03:49:00 | NPP-375D | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 788ff55c-ce3d-3aa2-b64b-b13a210b7e6f | -7.40523 | -42.05494 | 2025-09-02 03:49:00 | NPP-375D | SANTO INÁCIO DO PIAUÍ | PIAUÍ | Brasil | 2209500 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| df5f5c78-6245-342e-a6b5-4e8fb6c9430f | -6.88093 | -45.85216 | 2025-09-02 03:49:00 | NPP-375D | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |
| ff3e97d2-e957-3f18-bf20-9882a5fe11f6 | -4.91612 | -43.19843 | 2025-09-02 03:49:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 54504639-30e9-3c98-9548-a63e1278eac4 | -6.33828 | -42.5581 | 2025-09-02 03:49:00 | NPP-375D | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 3.1 |
| a37f2997-1787-3eec-bf69-aa625f64164d | -6.39782 | -43.50029 | 2025-09-02 03:49:00 | NPP-375D | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 5527890f-4fac-3412-96eb-e4cf70316d19 | -4.92069 | -43.19924 | 2025-09-02 03:49:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 73c70d59-199e-3bcb-b1f5-2440796b97bc | -6.86749 | -45.56197 | 2025-09-02 03:49:00 | NPP-375D | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| c935e4e3-dd45-3a36-969c-fb63b5aeb58e | -6.21912 | -43.36531 | 2025-09-02 03:49:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 8ecbce9b-299c-36d4-ad4a-474ab5acda47 | -6.30465 | -43.55337 | 2025-09-02 03:49:00 | NPP-375D | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 557c5a06-c292-35cc-9398-34d415dfc888 | -4.22575 | -47.21232 | 2025-09-02 03:49:00 | NPP-375D | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| bb63b70b-5881-33be-a330-601fe3cc2a2a | -6.96103 | -44.35474 | 2025-09-02 03:49:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| dde109b2-8199-34ff-a96b-14dacf5e6af6 | -6.33047 | -43.56806 | 2025-09-02 03:49:00 | NPP-375D | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 1e35024a-4ee0-3cbf-a6e3-0584ab665365 | -5.16346 | -37.98245 | 2025-09-02 03:49:00 | NPP-375D | LIMOEIRO DO NORTE | CEARÁ | Brasil | 2307601 | 23 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 7212d72b-6f9c-3db7-896b-868f3cf4b63e | -6.27825 | -43.29931 | 2025-09-02 03:49:00 | NPP-375D | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| f8f9f246-db7d-32b0-bc92-30c839d148ff | -6.87562 | -45.85121 | 2025-09-02 03:49:00 | NPP-375D | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 49.9 |
| bfc8d9fd-ab8b-37f6-804b-a65125919370 | -6.88036 | -45.85537 | 2025-09-02 03:49:00 | NPP-375D | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| ff17e32b-4d83-3a18-8d33-67ce81fe73f6 | -6.98185 | -44.31771 | 2025-09-02 03:49:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 1813a279-5ebf-358f-8917-1381e44d08d8 | -6.92641 | -45.56243 | 2025-09-02 03:49:00 | NPP-375D | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 4f597dcf-181b-3be0-98d5-cd8b50eb99d7 | -6.70598 | -42.25321 | 2025-09-02 03:49:00 | NPP-375D | TANQUE DO PIAUÍ | PIAUÍ | Brasil | 2210979 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| ba797f17-cb7e-35b8-8fee-9995759e2844 | -5.37406 | -42.62182 | 2025-09-02 03:49:00 | NPP-375D | DEMERVAL LOBÃO | PIAUÍ | Brasil | 2203305 | 22 | 33 | nan | nan | nan | Caatinga | 3.3 |
| 79e6dacb-54c8-3581-af71-f70a8bce701f | -6.25165 | -42.61571 | 2025-09-02 03:49:00 | NPP-375D | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 3.3 |
| 1b6030b9-b38d-3b98-8601-93b7badcd740 | -6.8798 | -45.85855 | 2025-09-02 03:49:00 | NPP-375D | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 5d98e344-3f7d-36d5-bc81-ac7b221f4b3e | -6.18578 | -44.19252 | 2025-09-02 03:49:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 01d1bce4-1009-3d13-a63e-853d2ba8c21f | -4.8218 | -37.80608 | 2025-09-02 03:49:00 | NPP-375D | JAGUARUANA | CEARÁ | Brasil | 2307007 | 23 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 062c01c1-ba1d-39d3-914b-c796e6d408e7 | -6.97934 | -44.30482 | 2025-09-02 03:49:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 24cf8e45-b741-383d-8814-1645bc823e8c | -6.96022 | -44.35631 | 2025-09-02 03:49:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| b43000c4-1894-3fc9-9458-03f9576872aa | -6.4973 | -45.40543 | 2025-09-02 03:49:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 678a96ea-71d9-3833-970c-6e341680ff04 | -4.2265 | -47.20787 | 2025-09-02 03:49:00 | NPP-375D | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 07bd340c-9f7b-3854-ad02-c2d47f882f82 | -7.11223 | -44.75983 | 2025-09-02 03:49:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| d49b3846-7ced-33a3-a9af-7a0aa0d9b024 | -6.26231 | -42.60489 | 2025-09-02 03:49:00 | NPP-375D | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 3.5 |
| ab16d876-2f8d-3e32-a43f-49cecaca05e3 | -7.10871 | -44.76058 | 2025-09-02 03:49:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 6ead03e2-6f48-3ab1-a274-56a39fa4c170 | -6.87924 | -45.86176 | 2025-09-02 03:49:00 | NPP-375D | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 4d7d94b9-b3af-3111-8c8a-6d72ea2cfa7d | -6.19346 | -43.35184 | 2025-09-02 03:49:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| c3d6fd43-060c-38d5-a93a-8c786098b13a | -6.33674 | -43.53075 | 2025-09-02 03:49:00 | NPP-375D | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 9ca3896c-5532-327d-975d-efd93e870123 | -7.06109 | -46.24511 | 2025-09-02 03:49:00 | NPP-375D | NOVA COLINAS | MARANHÃO | Brasil | 2107258 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 39ae917e-6ba8-358a-973a-eb7856fdfaf9 | -6.7173 | -42.26231 | 2025-09-02 03:49:00 | NPP-375D | TANQUE DO PIAUÍ | PIAUÍ | Brasil | 2210979 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 771f52f2-c957-3ce9-8eec-18b07556d41b | -6.25457 | -42.6247 | 2025-09-02 03:49:00 | NPP-375D | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 19ce6dc3-8e7f-3a25-9458-4fcd2ab6529c | -5.85934 | -48.16029 | 2025-09-02 03:49:00 | NPP-375D | ARAGUATINS | TOCANTINS | Brasil | 1702208 | 17 | 33 | nan | nan | nan | Amazônia | 1.9 |
| a39604b4-c58c-3cfb-b4e8-b4c13bca030a | -6.27453 | -43.29404 | 2025-09-02 03:49:00 | NPP-375D | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 4ee85e2a-22a2-3897-bbfe-bf1e07fdc0d9 | -6.98825 | -43.2327 | 2025-09-02 03:49:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 6.6 |
| 3a77bade-6940-3db9-8c0e-0c18da97ab3d | -5.86215 | -48.15967 | 2025-09-02 03:49:00 | NPP-375D | ARAGUATINS | TOCANTINS | Brasil | 1702208 | 17 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 50090155-1e8b-36c2-9b28-ce5c19bfc168 | -3.78755 | -47.57303 | 2025-09-02 03:49:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| edc5f61b-9c06-3567-a8c3-74ec052da1ae | -4.30324 | -48.09572 | 2025-09-02 03:49:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 96a1264a-0b2e-32f9-94d3-867ddcbb16fb | -6.87033 | -45.85023 | 2025-09-02 03:49:00 | NPP-375D | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 49.9 |
| fe81b05c-faf4-30cd-993e-900b8b78e7b5 | -6.86291 | -45.55795 | 2025-09-02 03:49:00 | NPP-375D | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| ce2ce7be-caca-3f0a-acb7-eec228a47c8e | -6.01174 | -43.83707 | 2025-09-02 03:49:00 | NPP-375D | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 7.4 |
| b2b48045-1fcd-349b-942b-fa23ac9fa1f7 | -5.50589 | -42.63755 | 2025-09-02 03:49:00 | NPP-375D | LAGOA DO PIAUÍ | PIAUÍ | Brasil | 2205581 | 22 | 33 | nan | nan | nan | Caatinga | 5.0 |
| f29ef530-4990-3bd0-ba8b-45bd4df842ff | -6.98394 | -44.33375 | 2025-09-02 03:49:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| fd2c2a05-69e5-3b67-9cad-3c481e34d800 | -6.17434 | -44.1161 | 2025-09-02 03:49:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 5d367068-89d5-39ca-9100-0333db9bdb99 | -7.00253 | -43.53198 | 2025-09-02 03:49:00 | NPP-375D | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 8cfd5a56-deee-33ae-aed9-7bb41d4071bd | -7.74957 | -40.26797 | 2025-09-02 03:49:00 | NPP-375D | TRINDADE | PERNAMBUCO | Brasil | 2615607 | 26 | 33 | nan | nan | nan | Caatinga | 1.3 |
| b70760f5-4cd4-3f9a-ac50-4fe252a2c5fb | -5.85587 | -48.15865 | 2025-09-02 03:49:00 | NPP-375D | ARAGUATINS | TOCANTINS | Brasil | 1702208 | 17 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 725d343b-5e74-37dd-b6d3-7a476f655f82 | -3.23 | -47.12929 | 2025-09-02 03:49:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 11.0 |
| a3b9aeac-c6d9-3fbd-8ea1-ca69448d9831 | -4.47826 | -48.11857 | 2025-09-02 03:49:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 9647ebda-7aec-3744-ba61-78e47522657e | -6.97818 | -43.10679 | 2025-09-02 03:49:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| a4617896-d7a4-30ab-a159-550af6c8645e | -4.22501 | -47.21676 | 2025-09-02 03:49:00 | NPP-375D | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |


[Clique aqui para ver as próximas entradas](README17.md)
