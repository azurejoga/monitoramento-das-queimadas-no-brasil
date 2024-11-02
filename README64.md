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

## Dados Diários - Página 64

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| d5a3c184-f58f-348a-a1b7-1643efb55302 | -2.57536 | -49.08319 | 2024-11-02 05:04:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 440c7637-a36b-3e59-8d27-d9a413ba6102 | -2.57371 | -49.12336 | 2024-11-02 05:04:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 83e313d2-5bfb-3d9e-a451-eb96bd681d37 | -2.56948 | -49.1227 | 2024-11-02 05:04:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 57adfcd6-d1de-38d7-9ee4-06733d6461af | -2.56745 | -49.07789 | 2024-11-02 05:04:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 13ea9228-4da1-3f0a-9ce3-a1c21b38a840 | -2.56668 | -48.97306 | 2024-11-02 05:04:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| e25fddea-a062-3ebb-9dac-71cf4edf6b29 | -2.56574 | -48.971 | 2024-11-02 05:04:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 20d97286-384e-3860-a0b1-f0dc2bf789a7 | -2.56515 | -48.97503 | 2024-11-02 05:04:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 8bff2cf9-5875-3254-9c6c-07434648abca | -2.56404 | -49.24585 | 2024-11-02 05:04:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 171ddcfe-7826-330e-b55d-e111e4df50bc | -2.56332 | -49.22196 | 2024-11-02 05:04:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 45f3d95c-cafe-319e-8cc4-66b4015438d3 | -2.56121 | -48.95168 | 2024-11-02 05:04:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| e6b19753-e65f-3ca1-9152-808e929a178f | -2.56042 | -49.2413 | 2024-11-02 05:04:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 7c499ee6-d015-36e4-80f4-654e21fdddcc | -2.55911 | -49.22129 | 2024-11-02 05:04:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 146d0a19-1601-31e7-a90a-1ec0eae1d0c8 | -2.55503 | -49.13247 | 2024-11-02 05:04:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 9.9 |
| c0f8e7ac-1679-3e7f-94a3-567760ab1716 | -2.5549 | -49.22061 | 2024-11-02 05:04:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2e737a9e-5e2e-39b0-ad96-e9e137baf63e | -2.52518 | -49.24126 | 2024-11-02 05:04:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| cc108b2d-e123-344e-a977-c116d908a2da | -2.5226 | -49.23536 | 2024-11-02 05:04:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 93126632-873d-37cc-96ae-e1bc509de2da | -2.52204 | -49.23922 | 2024-11-02 05:04:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 8b717fc7-14cd-3a23-b25c-c641477541aa | -2.52158 | -49.23674 | 2024-11-02 05:04:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| bddf20d6-f225-3dd9-b4e1-21c47f11bc49 | -2.52147 | -49.24308 | 2024-11-02 05:04:00 | NOAA-21 | MOCAJUBA | PARÁ | Brasil | 1504604 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 8345063f-8797-3315-85ea-66741da81b5e | -2.52098 | -49.2406 | 2024-11-02 05:04:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 8.0 |
| 7e8c43d3-fd23-3c8e-8270-1f8249f7f819 | -2.50016 | -49.03669 | 2024-11-02 05:04:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 1065f0e2-e98e-353b-a98a-aee30faebf89 | -2.49417 | -49.07644 | 2024-11-02 05:04:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 1a4518e0-77fa-351e-bc9d-12081022265c | -2.49357 | -49.0804 | 2024-11-02 05:04:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 858d117e-89af-3b62-b26f-182aa2a80776 | -2.48992 | -49.07579 | 2024-11-02 05:04:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| e439c422-1926-3995-951a-e8688fc12184 | -2.48933 | -49.07978 | 2024-11-02 05:04:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 9885599f-fc83-3ce0-8793-e0f42156ec2d | -2.44773 | -49.00817 | 2024-11-02 05:04:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 25f4e306-c01e-35ca-8a8e-280a1082ad8f | -2.12374 | -50.14399 | 2024-11-02 05:04:00 | NOAA-21 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 95ef47fe-f3c9-3892-b68b-5eead8f913e5 | -2.1198 | -50.14338 | 2024-11-02 05:04:00 | NOAA-21 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| b91668db-50b8-3edf-a687-7a5b9ddb1cab | -2.45081 | -50.40018 | 2024-11-02 05:04:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c66b8988-1ae0-3915-8527-a3ebd0844d44 | -2.44608 | -50.29595 | 2024-11-02 05:04:00 | NOAA-21 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 5f82b916-16e3-327b-b0a3-792c89c20b7d | -2.40701 | -50.4208 | 2024-11-02 05:04:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 0ad656d3-6acb-37bc-b132-37fd5dd493c5 | -2.39928 | -50.3141 | 2024-11-02 05:04:00 | NOAA-21 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 3ade2258-2a22-3087-a3e2-2f3aa4675593 | -2.39925 | -50.4196 | 2024-11-02 05:04:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 330ab1fd-c506-35f9-b4c7-de5fbe929b63 | -2.39537 | -50.3135 | 2024-11-02 05:04:00 | NOAA-21 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 0ef39016-cc82-3a2a-98dc-04d4af152cc0 | -2.213 | -50.32251 | 2024-11-02 05:04:00 | NOAA-21 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 10aaf7ee-10c5-3335-8718-5209448a39bc | -2.21225 | -50.32741 | 2024-11-02 05:04:00 | NOAA-21 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 239e0afc-bd08-3396-9093-354e13a9e9e7 | -2.20835 | -50.32682 | 2024-11-02 05:04:00 | NOAA-21 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c23abd4b-eded-3a0c-bc00-be9fb08dbe51 | -2.20446 | -50.32624 | 2024-11-02 05:04:00 | NOAA-21 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 9563af25-8547-3c5b-86c5-70881d98d86c | -2.19816 | -50.31519 | 2024-11-02 05:04:00 | NOAA-21 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| e3509578-496c-39ad-a985-96a5b6535cdc | -2.19427 | -50.3146 | 2024-11-02 05:04:00 | NOAA-21 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 2ceb7aa9-d659-32f9-b21b-2e7cda404378 | -2.07258 | -50.34866 | 2024-11-02 05:04:00 | NOAA-21 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 4d20e7a9-394a-3b22-b080-387645098902 | -2.21934 | -49.57202 | 2024-11-02 05:04:00 | NOAA-21 | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 99f3187b-4eda-36c4-ba5f-4a6bf17a5d9f | -2.15993 | -50.14441 | 2024-11-02 05:04:00 | NOAA-21 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 47217354-8e0f-3444-be8b-6c445972d668 | -2.15677 | -50.13879 | 2024-11-02 05:04:00 | NOAA-21 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 40d70678-88c1-3935-9ab6-21ca9aa16649 | -2.15599 | -50.14381 | 2024-11-02 05:04:00 | NOAA-21 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| c75ada32-f73b-3d8c-944d-8b18e5cd0047 | -2.15206 | -50.1432 | 2024-11-02 05:04:00 | NOAA-21 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 6ae0ef6e-0277-3554-a3ca-766084fbf065 | -2.15128 | -50.14822 | 2024-11-02 05:04:00 | NOAA-21 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 55090c50-02a7-36bf-9aa1-d6932620df2c | -2.91101 | -49.03654 | 2024-11-02 05:04:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| fad9c532-3a0e-3c8a-9b51-a35842445960 | -2.89414 | -49.23763 | 2024-11-02 05:04:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 1c79f619-9d21-3232-98df-2152cef060f0 | -2.88568 | -49.23634 | 2024-11-02 05:04:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| e680bbb5-ba3b-3f98-806b-526c3a3779b7 | -2.87723 | -49.23508 | 2024-11-02 05:04:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 1ab1ad3f-eb3a-32f1-b9ed-2fbd5451daea | -2.873 | -49.23442 | 2024-11-02 05:04:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| cc2db82f-25ef-33d0-b5b9-449cfc3cd545 | -2.86878 | -49.23376 | 2024-11-02 05:04:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4de6d70a-5f5d-3a4f-bf28-92e7934acd54 | -2.86455 | -49.2331 | 2024-11-02 05:04:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 7307be8d-d284-37e6-800b-048c9455744a | -2.86033 | -49.23244 | 2024-11-02 05:04:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| e3fef8e4-ffc3-3bca-98db-afc378f11959 | -2.80263 | -49.21299 | 2024-11-02 05:04:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 7f7ff481-0c4c-3b04-843c-76cb4fc98b68 | -2.79781 | -49.2163 | 2024-11-02 05:04:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| b7b84916-b1b7-3b1b-8ab8-dbef1d07ead6 | -2.75961 | -49.18222 | 2024-11-02 05:04:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 0c9335d5-26f0-3f72-b060-6007b3aed196 | -2.75538 | -49.18155 | 2024-11-02 05:04:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| f64e5c1b-1779-353d-98bd-7b30ce208163 | -2.72607 | -49.17471 | 2024-11-02 05:04:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 719d3be9-04b2-3c32-ae25-fd5abb1a5c95 | -2.72184 | -49.17406 | 2024-11-02 05:04:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 3b4d725b-1eec-317a-8ef2-4d52ed265d80 | -2.94301 | -49.34785 | 2024-11-02 05:04:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d71b8d92-a0f1-3487-8a56-aedbf414eab2 | -2.94256 | -49.34447 | 2024-11-02 05:04:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 9a0a69af-5a77-36d7-92e3-128cc86b7d20 | -2.94196 | -49.34838 | 2024-11-02 05:04:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ed0a7ae0-d681-36be-ab14-950b1e1fdc8a | -2.93938 | -49.34329 | 2024-11-02 05:04:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 345b71f6-eba4-3337-8dbe-37866e0f05f2 | -2.93881 | -49.34722 | 2024-11-02 05:04:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| fc7596ad-4025-361c-8b46-dd9eb7b57be6 | -2.93836 | -49.34387 | 2024-11-02 05:04:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 9436dcc2-f7a1-3b0a-b2d5-a1702f243979 | -2.93776 | -49.34776 | 2024-11-02 05:04:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| a4c6cc8f-625c-36bb-ade6-0d732e5f4f3f | -2.89709 | -49.36118 | 2024-11-02 05:04:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 9383d7ee-38b4-3718-81fc-b1a7ec68f902 | -2.89058 | -49.37595 | 2024-11-02 05:04:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| d9a0ab65-4dd4-3860-9194-65a97f357ca7 | -2.88525 | -49.26823 | 2024-11-02 05:04:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e5b064a9-f644-35f7-b636-53198e783bad | -2.88161 | -49.26368 | 2024-11-02 05:04:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 3a89eeb1-0248-327b-bf98-094c852590f1 | -2.88103 | -49.26758 | 2024-11-02 05:04:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 81111ca5-0fce-3a2d-9d30-9fbeb78e924e | -2.87681 | -49.26694 | 2024-11-02 05:04:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| d3b7c2d3-5c06-34d8-9352-b493a747f4c1 | -2.86319 | -49.38734 | 2024-11-02 05:04:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| e94e7f79-d37d-3135-bd47-255a4bf65104 | -2.859 | -49.38672 | 2024-11-02 05:04:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| c75cc9b8-f5c4-3a59-a72f-3dd54652e476 | -2.85766 | -49.36693 | 2024-11-02 05:04:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 85655348-d5bd-3854-ac85-4df9e58906d4 | -2.85539 | -49.38227 | 2024-11-02 05:04:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 35335b27-971b-3178-ab7f-4bb9c56e0c89 | -2.85482 | -49.3861 | 2024-11-02 05:04:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| f8762bfc-ce33-35d1-9a71-46e2516c694a | -2.85405 | -49.3624 | 2024-11-02 05:04:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 364a9efe-0f72-3a88-9c04-b442e002168b | -2.85348 | -49.36628 | 2024-11-02 05:04:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 4fda24c8-7a56-3920-ad98-00260a6ad348 | -2.85007 | -49.38925 | 2024-11-02 05:04:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 2d61e485-0756-374e-932e-2a5afcb0d53c | -2.84797 | -49.34557 | 2024-11-02 05:04:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a0d4b321-496d-374e-bd1e-1c946836b7fb | -2.84702 | -49.38097 | 2024-11-02 05:04:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| e89e5b4f-d4ff-32f8-9df6-89b8b885c7e6 | -2.84646 | -49.38477 | 2024-11-02 05:04:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| a30558e7-313a-3126-b896-277da58ddc20 | -2.8434 | -49.3765 | 2024-11-02 05:04:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 430796f4-f167-37b9-9825-ee25b388ea1a | -2.84228 | -49.38413 | 2024-11-02 05:04:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 96af332d-f064-37aa-bc62-80b1090fc466 | -2.83979 | -49.37202 | 2024-11-02 05:04:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 4c1d818e-5cce-3b6b-b154-ffdfe4f0f56c | -2.83118 | -49.34312 | 2024-11-02 05:04:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 1313f513-1332-3f7e-ad0e-98e585fa3fdf | -2.82328 | -49.2761 | 2024-11-02 05:04:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 197b30f7-95cd-3e25-bc87-6be1d3ad2bd7 | -2.82274 | -49.30777 | 2024-11-02 05:04:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| a7715495-3847-3927-8891-20bf57bd2080 | -2.81907 | -49.27546 | 2024-11-02 05:04:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e0de2538-641f-326a-a172-168979ee58cb | -2.81854 | -49.30711 | 2024-11-02 05:04:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f6be9969-4470-3085-902d-7bf45a5f85ac | -2.81618 | -49.32254 | 2024-11-02 05:04:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 6626657b-d71a-3efc-9e76-7752795d945b | -2.8156 | -49.32639 | 2024-11-02 05:04:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 3678675a-0740-345a-87ed-f06ddbe4c5f7 | -2.81434 | -49.30647 | 2024-11-02 05:04:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 827d5884-2530-3b9d-8974-c00daae36d37 | -2.81081 | -49.32961 | 2024-11-02 05:04:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 3bbf5618-7f83-31d2-b782-ca0099f1599f | -2.80662 | -49.32898 | 2024-11-02 05:04:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 33aad30c-2d8a-331e-bcaf-57a0059904e5 | -2.80603 | -49.33281 | 2024-11-02 05:04:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 6637a49b-c260-352b-a34c-ad6324873bbd | -2.80242 | -49.32834 | 2024-11-02 05:04:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |


[Clique aqui para ver as próximas entradas](README65.md)
