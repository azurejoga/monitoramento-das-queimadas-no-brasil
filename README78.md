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

## Dados Diários - Página 78

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| bd81b113-cfda-3dd2-9fe1-96df542a0789 | -4.00781 | -53.4292 | 2024-09-27 04:38:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 4457bc4d-5a98-3491-9cec-dc0181f8e9cf | -4.18975 | -53.82642 | 2024-09-27 04:38:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4ff4bb59-58c6-3b9e-a73a-da993f16a1ec | -4.18867 | -53.83314 | 2024-09-27 04:38:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| eebea2eb-e29d-36d8-a6a4-65d40b12eb5e | -4.18772 | -53.82639 | 2024-09-27 04:38:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 76cea04b-072e-3eb3-8b74-00ea21a99d6c | -3.62877 | -53.6072 | 2024-09-27 04:38:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 60078300-65e1-38f0-b247-3fdbe0aad2e6 | -3.59069 | -53.47121 | 2024-09-27 04:38:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 57654b48-30c2-3eaf-af11-01ea64fec9d0 | -3.82676 | -52.28902 | 2024-09-27 04:38:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b16d4b67-4003-3287-940f-c95a3998dd8e | -3.82312 | -52.28833 | 2024-09-27 04:38:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 8cbdb5fc-5b1b-3da4-ae74-f7760a6c94e4 | -3.78215 | -52.28631 | 2024-09-27 04:38:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 249aaf41-9327-32bb-bebf-a5b7f14d203d | -3.78204 | -52.28774 | 2024-09-27 04:38:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 552ba7cf-98d8-394a-9907-0e37e635dee3 | -3.59072 | -53.46827 | 2024-09-27 04:38:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| ef651042-d284-36e5-9701-3b0e5fb251a4 | -5.68318 | -53.74968 | 2024-09-27 04:40:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| f0bf09f3-2cc7-387a-a9ed-276e2e11f9d8 | -5.67211 | -53.91547 | 2024-09-27 04:40:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 5f575645-0a01-309d-a369-2ad5ec588e51 | -5.67127 | -53.92064 | 2024-09-27 04:40:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 77822719-93e4-3998-9693-15e946273d28 | -5.66841 | -53.74243 | 2024-09-27 04:40:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e801d4ff-8782-31a8-b374-0f0573d3b9df | -5.64734 | -53.87008 | 2024-09-27 04:40:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 1ac85326-e859-354b-a8bf-302ade9812ea | -8.04098 | -53.26273 | 2024-09-27 04:40:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 7a9a4002-51ee-38ef-9793-2430bff16dd4 | -9.17378 | -54.66526 | 2024-09-27 04:40:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| bb348d27-2bc9-324d-a5bc-1df7250e436d | -9.17294 | -54.6701 | 2024-09-27 04:40:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| aef14ce3-58a7-3aa3-ba28-55f5f3ffc9ec | -9.17206 | -54.67518 | 2024-09-27 04:40:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| c26d3a98-5e5c-3656-9bc2-19801439e5fa | -9.17194 | -54.62943 | 2024-09-27 04:40:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 9bcb7942-55ca-3891-a75b-9101299f4595 | -9.17086 | -54.63129 | 2024-09-27 04:40:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| cad4c30c-f094-384c-b249-55e35db2f792 | -9.10008 | -54.67023 | 2024-09-27 04:40:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 0e23699a-d61d-3fd6-ae6c-a1c4e932425d | -8.92937 | -54.74807 | 2024-09-27 04:40:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 3b3c2192-ded2-3ad2-a0a2-90b155742b52 | -8.92543 | -54.74743 | 2024-09-27 04:40:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 0e59ae60-a610-32a0-86a2-c6a3c9e8c2e5 | -8.92538 | -54.75067 | 2024-09-27 04:40:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 62051dff-8c9f-340f-aa7f-2d4886403dce | -8.92148 | -54.74682 | 2024-09-27 04:40:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 84c607ae-96d8-3978-9c6b-41a7a15b4a2e | -8.92144 | -54.75001 | 2024-09-27 04:40:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 6269fc9f-6efe-35f0-9d90-1796de42a318 | -8.91834 | -54.74435 | 2024-09-27 04:40:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 42166084-d9c1-3e70-a1a5-7ced1057dd80 | -8.89635 | -54.73056 | 2024-09-27 04:40:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 5db5f88f-d254-3f06-91bc-c2763434b09c | -8.79541 | -54.68435 | 2024-09-27 04:40:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 8f786240-3244-318a-ba37-e14de54fcce2 | -8.79061 | -54.68885 | 2024-09-27 04:40:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c162f422-b853-36b8-822f-e44cfd762dc5 | -8.71334 | -54.80814 | 2024-09-27 04:40:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 63729a48-bb87-3dc6-a3ad-85846d511319 | -8.70933 | -54.80765 | 2024-09-27 04:40:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 36416fda-46d0-3f82-b275-f903f51d18d0 | -8.70658 | -54.79997 | 2024-09-27 04:40:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 9c6aa4d5-2dde-30db-b626-e6f191d7ff91 | -8.70446 | -54.79582 | 2024-09-27 04:40:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| b97d6eb7-40c0-348d-9ab7-6ff13922b5cb | -8.70329 | -54.80285 | 2024-09-27 04:40:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 0dbac5fd-9026-3d0e-b244-ae3ba552ef16 | -8.70045 | -54.79539 | 2024-09-27 04:40:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| b5eb3e1a-d945-3cbc-9da7-604a42d753f2 | -8.69702 | -54.79153 | 2024-09-27 04:40:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| cdca4b15-f481-3615-952d-ae7bb497d212 | -8.69623 | -54.78909 | 2024-09-27 04:40:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 3a629477-32f9-3e90-a3a5-549d94bf50b4 | -8.69533 | -54.79426 | 2024-09-27 04:40:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 17f58bc0-7fb4-318f-a8c3-9a83c44e20b8 | -8.53877 | -54.58065 | 2024-09-27 04:40:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| e2ad8d73-5a07-3e79-9d99-0de6bd2b5079 | -8.53791 | -54.58569 | 2024-09-27 04:40:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| cd4bfc2e-06e7-32ea-b26d-1cb1c8eb3ae8 | -8.53485 | -54.58001 | 2024-09-27 04:40:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| df914e92-c4ec-3c8f-b75b-520b178d2881 | -8.53092 | -54.57936 | 2024-09-27 04:40:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| c84b152a-269e-3d2a-b670-01bb487039bd | -8.53006 | -54.58439 | 2024-09-27 04:40:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| b1f443dd-1f19-3dde-b9ab-0e737903cdbb | -8.52973 | -54.58656 | 2024-09-27 04:40:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 95c6ab40-5f67-320a-bb71-532796228040 | -8.52744 | -54.59958 | 2024-09-27 04:40:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 69ba7674-b850-3204-b23c-a30cffcfacce | -8.5117 | -54.69085 | 2024-09-27 04:40:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 5bd673f2-da97-38b7-8611-1a33907840b4 | -8.44835 | -54.66169 | 2024-09-27 04:40:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| b865059c-f42f-3b6e-abe2-4929343dcc86 | -8.4282 | -54.68449 | 2024-09-27 04:40:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 6464831e-aca3-34a6-957a-3d141a1e6793 | -8.4238 | -54.71025 | 2024-09-27 04:40:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| f555e723-fc6a-3412-afcd-cb190756cae1 | -8.42337 | -54.68895 | 2024-09-27 04:40:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 62f39bf4-1d24-3410-9c13-0777a2ca6472 | -8.42163 | -54.69915 | 2024-09-27 04:40:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 96c28a19-4923-3f32-8730-3c389e057169 | -8.42074 | -54.70433 | 2024-09-27 04:40:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| e81521e7-caea-36f4-b6f2-69cb143f8966 | -8.41767 | -54.69851 | 2024-09-27 04:40:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| d7c30e1a-cebd-3eb9-bdf1-cd0aec78bd7f | -8.2137 | -54.66558 | 2024-09-27 04:40:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| f47821ee-8979-3ddd-8465-397f01da938a | -8.62222 | -53.65233 | 2024-09-27 04:40:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| cca122fb-4ac6-36a8-ae5b-0df3521de8fa | -8.6148 | -53.65111 | 2024-09-27 04:40:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d0b9c334-2182-33de-b49c-83edf02cf911 | -8.61034 | -53.655 | 2024-09-27 04:40:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e747f9bd-4454-3458-b779-43fcaff09309 | -8.57654 | -53.34032 | 2024-09-27 04:40:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| f76d5c55-5acf-3340-9b58-cb7e4f574aa9 | -8.57583 | -53.3446 | 2024-09-27 04:40:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 7a957abe-7222-34b7-84c6-d8d200a053d9 | -8.53571 | -54.57502 | 2024-09-27 04:40:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 02c21a11-046d-3757-8c45-f4ba5ea9d64e | -8.53139 | -54.57649 | 2024-09-27 04:40:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| e0c9c645-bb18-3ed5-b1d8-7ccb570e7989 | -8.53137 | -54.60023 | 2024-09-27 04:40:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| aeab27e9-f06b-3b8a-9160-9868ba916fc0 | -8.53058 | -54.69926 | 2024-09-27 04:40:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f4eb95f8-def0-37bd-86fc-e39269880ab2 | -8.53056 | -54.58151 | 2024-09-27 04:40:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| df1c5264-a254-3272-9548-b6fdb4eff655 | -8.52722 | -54.60178 | 2024-09-27 04:40:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 67f6d37f-c72f-3453-aebb-95899f4b7082 | -8.52664 | -54.58087 | 2024-09-27 04:40:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| c0d8573f-a815-3aba-8702-0b7d7fff56b5 | -8.5121 | -54.69328 | 2024-09-27 04:40:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 26f42166-d20e-3bdb-8c21-05b7a51e819e | -8.43217 | -54.68511 | 2024-09-27 04:40:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| e40a0511-d9a5-3c81-bae4-36ab7ee8be80 | -8.42908 | -54.67939 | 2024-09-27 04:40:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 30cecaa9-e7d6-3a7b-a41d-da028e28c450 | -8.4247 | -54.705 | 2024-09-27 04:40:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| cd0746df-472d-3aac-85f1-1dddad4dfdec | -8.42424 | -54.68386 | 2024-09-27 04:40:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 0fa7a772-3f11-341c-a81f-9a8c530da0c2 | -8.41984 | -54.70958 | 2024-09-27 04:40:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 24245f5a-3270-33c2-baf6-e4fb8c41959a | -8.41678 | -54.70368 | 2024-09-27 04:40:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| d4b22a22-2155-3d9f-acf1-0bd8d5095d35 | -9.17597 | -54.67585 | 2024-09-27 04:40:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| f744b6d2-f4ee-3917-9c53-caa38db4a511 | -8.93019 | -54.74615 | 2024-09-27 04:40:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 9e74ced0-d30c-358a-bad9-8a1acee713bf | -8.92624 | -54.74551 | 2024-09-27 04:40:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 755a31bf-0ffa-3e87-a0ce-646a685e94a4 | -8.91749 | -54.74942 | 2024-09-27 04:40:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 046d87ca-e029-3e4a-a4a5-2d6fb14dd469 | -8.91438 | -54.7438 | 2024-09-27 04:40:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 875b3298-1a06-3da3-be00-3d1c26cedc2d | -8.91042 | -54.74324 | 2024-09-27 04:40:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 6dc5030c-5f9b-3b46-baa8-d8af6e7202df | -8.90337 | -54.737 | 2024-09-27 04:40:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a1e1431f-be42-369a-b144-aa755c7035c4 | -8.9003 | -54.73115 | 2024-09-27 04:40:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 192b7afb-109f-313a-8ffa-6966e965eb59 | -8.87837 | -54.71723 | 2024-09-27 04:40:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| b19f432e-e0f7-3592-9e35-797481cbbf1a | -8.86308 | -54.68833 | 2024-09-27 04:40:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 006bbbd8-a926-3fa3-a609-773d86e80991 | -8.71393 | -54.80468 | 2024-09-27 04:40:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 254575ce-2293-3627-9f6c-a2b3e8112569 | -8.70996 | -54.80406 | 2024-09-27 04:40:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 599daafa-af10-37af-953f-54999ec258e6 | -8.70598 | -54.80346 | 2024-09-27 04:40:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| a9570ada-e13c-3a76-af49-b82de13ad593 | -8.70449 | -54.74673 | 2024-09-27 04:40:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 0cefd312-fa89-39bf-80a3-0b9f5619540d | -8.70388 | -54.7993 | 2024-09-27 04:40:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| a4480859-2422-3c6c-a697-c239d44836cb | -8.70335 | -54.79507 | 2024-09-27 04:40:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| fd281bef-cc59-38f2-9b3c-458852a3cd9a | -8.70329 | -54.74852 | 2024-09-27 04:40:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 069e87cd-c8e7-3640-92e2-1aef3191ee15 | -8.7026 | -54.79943 | 2024-09-27 04:40:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| b998f951-1572-3816-8b2a-f6fd1dd59834 | -8.69987 | -54.7989 | 2024-09-27 04:40:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 15658da7-e313-3bd9-8de1-72f0504bcc8b | -8.69934 | -54.79465 | 2024-09-27 04:40:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 650ecaf3-88f3-3a7c-90c2-391f56a861d4 | -8.69644 | -54.79498 | 2024-09-27 04:40:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| c7c217d4-78a5-339d-b0cb-31167ed0c036 | -8.69373 | -54.78684 | 2024-09-27 04:40:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 21061410-5700-3fe8-aa5d-1b17293a6d24 | -8.69301 | -54.79115 | 2024-09-27 04:40:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| dfdda03e-6646-3331-9b7c-6616cbc619af | -8.68972 | -54.78645 | 2024-09-27 04:40:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |


[Clique aqui para ver as próximas entradas](README79.md)
