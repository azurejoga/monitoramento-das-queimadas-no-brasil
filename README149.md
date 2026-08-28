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

## Dados Diários - Página 149

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| ec8dc8b2-1616-3fb1-b438-c5f6f3871dc9 | -3.91041 | -60.9476 | 2026-08-28 17:47:00 | NOAA-20 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 22.6 |
| 3447ecc0-2092-38e0-aa18-0b2b789a61ee | -7.34899 | -55.16795 | 2026-08-28 17:47:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 14.7 |
| 93011eeb-ca43-3b62-b59c-8ad454c6b83f | -8.3368 | -70.814 | 2026-08-28 17:47:00 | NOAA-20 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 9.2 |
| 2a4827e3-9cb5-3b5e-8f07-2c9549ecc80c | -9.01657 | -71.60258 | 2026-08-28 17:47:00 | NOAA-20 | JORDÃO | ACRE | Brasil | 1200328 | 12 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 737dbcc4-3508-3d2d-91eb-a37a4bd919b4 | -3.35821 | -59.57824 | 2026-08-28 17:47:00 | NOAA-20 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 36.1 |
| 38e65e4d-a249-31f4-b820-26a5d8f96998 | -7.22845 | -73.10836 | 2026-08-28 17:47:00 | NOAA-20 | GUAJARÁ | AMAZONAS | Brasil | 1301654 | 13 | 33 | nan | nan | nan | Amazônia | 24.9 |
| 3f622102-4ceb-30a2-be0d-7542685bfbf9 | -7.95055 | -72.38184 | 2026-08-28 17:47:00 | NOAA-20 | CRUZEIRO DO SUL | ACRE | Brasil | 1200203 | 12 | 33 | nan | nan | nan | Amazônia | 18.4 |
| 9046582d-1303-35d2-a9b5-9edd1e40130d | -7.74542 | -61.06319 | 2026-08-28 17:47:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 8.0 |
| 0f211ac8-c30b-3b7d-9aa7-9763c6392d6a | -8.89936 | -72.71227 | 2026-08-28 17:47:00 | NOAA-20 | MARECHAL THAUMATURGO | ACRE | Brasil | 1200351 | 12 | 33 | nan | nan | nan | Amazônia | 10.6 |
| 76a21a4d-d2ab-3837-91f5-b9af403c485f | -8.8751 | -71.47238 | 2026-08-28 17:47:00 | NOAA-20 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 20.8 |
| 42da719f-b06a-3d27-b78e-72b13d69119a | -8.68072 | -62.82017 | 2026-08-28 17:47:00 | NOAA-20 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 3.3 |
| ed68221c-66b8-3eaa-847f-ebe8424f4a63 | -6.03667 | -57.79502 | 2026-08-28 17:47:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 7.8 |
| 3d218602-a5fc-34e4-9a1f-06fdd963b251 | -7.07536 | -59.7117 | 2026-08-28 17:47:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 7.9 |
| 4bd79023-bb63-38ad-9cc3-5b9ebcce1dad | -8.49737 | -70.31219 | 2026-08-28 17:47:00 | NOAA-20 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 22.5 |
| 0a6ff067-494f-32f0-88b9-318c94d18865 | -6.47021 | -55.94781 | 2026-08-28 17:47:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 3864e5c8-8db2-3fb4-bf6b-ce5eb81a2727 | -6.94133 | -58.94426 | 2026-08-28 17:47:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.7 |
| ec903bd5-5694-3084-9129-4c87a008a48f | -4.31153 | -59.46585 | 2026-08-28 17:47:00 | NOAA-20 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 8.0 |
| c78205ed-9066-3cc1-a6e0-703b3758ec4f | -4.30528 | -59.47675 | 2026-08-28 17:47:00 | NOAA-20 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 49.7 |
| 156aba4e-d39a-3eed-b174-770f32c4c274 | -6.02277 | -57.7894 | 2026-08-28 17:47:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| a432a14a-a3a0-3c8f-af00-565821929e78 | -6.80717 | -58.74269 | 2026-08-28 17:47:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 9.9 |
| 85a51074-008d-3b2a-bff2-b3997ff74130 | -8.36004 | -71.05931 | 2026-08-28 17:47:00 | NOAA-20 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 74.9 |
| 2b540a58-9318-3bdf-9e29-a053f13a1118 | -6.1467 | -53.70101 | 2026-08-28 17:47:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 34188113-bf83-3ea6-baef-daf26e8da7cb | -8.11764 | -71.30468 | 2026-08-28 17:47:00 | NOAA-20 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 11.7 |
| aa880fbb-d78b-3677-91c9-1c823d723080 | -7.36139 | -58.08655 | 2026-08-28 17:47:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 83a82656-81ec-357d-b52d-9fa339d76540 | -8.86531 | -70.90765 | 2026-08-28 17:47:00 | NOAA-20 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 25.1 |
| 599dff59-c5cc-37d1-a026-18492a2a24e1 | -7.91535 | -61.3637 | 2026-08-28 17:47:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 10.8 |
| d879a872-332b-3a86-9fb0-9f752d986d66 | -8.0025 | -71.16925 | 2026-08-28 17:47:00 | NOAA-20 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 7.9 |
| ebb5bb49-6794-3ef1-afec-b3016e12a709 | -5.9716 | -57.71701 | 2026-08-28 17:47:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 17.0 |
| a3a7f36e-c2bd-3cd1-b80e-a5fb353ef7fb | -7.36265 | -55.18854 | 2026-08-28 17:47:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 10.2 |
| f36a3ffe-d0df-36d4-8862-de994dfb5df0 | -9.06757 | -69.90806 | 2026-08-28 17:47:00 | NOAA-20 | SANTA ROSA DO PURUS | ACRE | Brasil | 1200435 | 12 | 33 | nan | nan | nan | Amazônia | 7.0 |
| e98ac71a-605c-32a1-8444-16b481528bd5 | -6.8306 | -55.61428 | 2026-08-28 17:47:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 12.3 |
| 674e221b-e920-327e-8b79-40bb5c613f96 | -3.90552 | -60.93993 | 2026-08-28 17:47:00 | NOAA-20 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 11.2 |
| 0e417e42-5014-3fd8-b057-9757ee6e8882 | -6.99064 | -60.66536 | 2026-08-28 17:47:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 41025a7a-7e41-3d1c-bfe4-f4f85c420176 | -6.94904 | -58.94298 | 2026-08-28 17:47:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 18.4 |
| 63cfa490-bc1d-3289-998a-0399d46c732e | -4.15858 | -60.69844 | 2026-08-28 17:47:00 | NOAA-20 | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 13.1 |
| 3afee52c-7690-3e33-bd25-493fb43a0be9 | -7.49192 | -55.28242 | 2026-08-28 17:47:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 11.6 |
| 420178f8-f1ab-3a64-b211-d21ad53bab1a | -8.02851 | -69.89874 | 2026-08-28 17:47:00 | NOAA-20 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 24e4838e-8e98-39f2-96f2-75b40a0d190e | -7.37371 | -55.51336 | 2026-08-28 17:47:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 35be75d6-ce26-36e2-b505-550c7febf83f | -6.4461 | -63.20926 | 2026-08-28 17:47:00 | NOAA-20 | TAPAUÁ | AMAZONAS | Brasil | 1304104 | 13 | 33 | nan | nan | nan | Amazônia | 9.3 |
| ce702d77-7c0d-3211-b181-3e913bec3daa | -7.57667 | -61.30424 | 2026-08-28 17:47:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 5.8 |
| c014fb71-f28a-3813-b7f7-b037a18016de | -4.33124 | -54.89955 | 2026-08-28 17:47:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 19.5 |
| 4180cab5-52fb-3ac2-83d2-f32c1adc9bf6 | -8.67251 | -62.81077 | 2026-08-28 17:47:00 | NOAA-20 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 9.1 |
| 3a3b1d06-2a0e-389d-b17e-d652f6e6b5e5 | -8.02741 | -69.88654 | 2026-08-28 17:47:00 | NOAA-20 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 26.9 |
| 8a8a31da-bd1a-35e6-b1f5-6c5723139fca | -8.21706 | -70.50674 | 2026-08-28 17:47:00 | NOAA-20 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 7.8 |
| abae34b7-2684-349f-8a98-b93e314ea2f0 | -6.7713 | -59.46944 | 2026-08-28 17:47:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 18.6 |
| a5c3afd6-f616-3bbc-8d90-a1b491b915d7 | -8.43799 | -70.33582 | 2026-08-28 17:47:00 | NOAA-20 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 23.1 |
| 73fe8bfe-a2c7-3bdc-b0af-45fb9fa5c679 | -4.14664 | -60.76443 | 2026-08-28 17:47:00 | NOAA-20 | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 158.6 |
| f4314569-6727-395f-94be-9af8f78143c8 | -8.32651 | -70.73856 | 2026-08-28 17:47:00 | NOAA-20 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 12.9 |
| 3075a6a5-b5e2-31cb-88d6-b3d34029c78a | -6.96003 | -59.48373 | 2026-08-28 17:47:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 17.6 |
| 5b6857de-9bd1-35b9-87de-e275280dc516 | -7.58008 | -61.30372 | 2026-08-28 17:47:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 1bf855b5-cf20-3b03-8856-95926d75b02c | -7.92628 | -70.66553 | 2026-08-28 17:47:00 | NOAA-20 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 36.0 |
| 76ca7d5d-fb24-386a-8b7f-7f9e248c20fe | -9.21105 | -65.78528 | 2026-08-28 17:47:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 3.9 |
| c0c6dace-9fa8-3e13-b14a-e3c2b04bb16d | -4.8922 | -56.26585 | 2026-08-28 17:47:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 15.1 |
| 735d1b52-d161-3b0d-9c7c-160b118814d4 | -8.63792 | -66.54491 | 2026-08-28 17:47:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 23.1 |
| 5977504a-cf89-385f-9852-3bf17148fec8 | -8.64403 | -66.53501 | 2026-08-28 17:47:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 2f7fb4b3-db2d-3d7e-b5b4-1a69f2692347 | -7.59786 | -61.35019 | 2026-08-28 17:47:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 117.5 |
| b53c116f-c8ef-3765-ac72-2201842bb161 | -8.67098 | -63.87448 | 2026-08-28 17:47:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.3 |
| a0b7175a-44fc-37d6-a444-d4b167c689e4 | -6.64542 | -58.49608 | 2026-08-28 17:47:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 12.6 |
| 06ed539d-8dd6-3ee2-9909-d5138d15f0e5 | -6.0547 | -53.88605 | 2026-08-28 17:47:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 0b202d88-ea62-3679-a0e2-f6b77753d773 | -9.01563 | -71.60459 | 2026-08-28 17:47:00 | NOAA-20 | JORDÃO | ACRE | Brasil | 1200328 | 12 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 628918e2-9255-32c9-b534-a69a10495f42 | -6.12324 | -57.68883 | 2026-08-28 17:47:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 13.1 |
| 0f722fd3-e462-3d8c-8d66-dcc7738181ec | -6.80395 | -59.60207 | 2026-08-28 17:47:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 9c8f466e-8ee3-3c93-8dcf-d58ac987a454 | -4.9318 | -55.77107 | 2026-08-28 17:47:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 14.3 |
| b6b08d0a-31d3-3406-947d-b09f0ec7a873 | -6.15307 | -57.94633 | 2026-08-28 17:47:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 7f4767dc-e4cc-3c66-b7c7-b485b2fc163b | -7.37279 | -55.50803 | 2026-08-28 17:47:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| c06f7ca8-d1f3-3913-8964-0567b87de29a | -6.37698 | -54.95367 | 2026-08-28 17:47:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 8e2f07c5-d61c-3c5b-b147-33568f785979 | -4.31304 | -59.47557 | 2026-08-28 17:47:00 | NOAA-20 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 11.8 |
| a6802090-9068-3fb8-ac49-dbd22e007e0c | -5.85217 | -57.75344 | 2026-08-28 17:47:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 43e6d75a-0db5-3d12-9301-d4368dd65e0e | -8.14378 | -64.00005 | 2026-08-28 17:47:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 177fac14-4c47-3e52-9fc3-e6aaa36d5829 | -6.66569 | -59.43898 | 2026-08-28 17:47:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 12.9 |
| 8897102e-f307-3de0-96fe-251cc3f5d94f | -7.46068 | -61.3913 | 2026-08-28 17:47:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 11.7 |
| 32d64b15-4a9a-36d4-9279-25a00dd6a7af | -9.66591 | -68.97269 | 2026-08-28 17:47:00 | NOAA-20 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 2.3 |
| f5a53c26-5c62-3ac7-9f65-eace87e486ac | -4.1496 | -60.75972 | 2026-08-28 17:47:00 | NOAA-20 | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 35.6 |
| f5d9e73e-bcf2-332c-a90c-a18c495c821b | -6.94213 | -58.94904 | 2026-08-28 17:47:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 23.1 |
| b4c269ca-6472-37ba-84f9-b04d1bf77198 | -8.59926 | -70.20354 | 2026-08-28 17:47:00 | NOAA-20 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 8.1 |
| 75f8b671-f923-336e-b78f-49b4181096de | -6.8445 | -59.46405 | 2026-08-28 17:47:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 48.0 |
| 36c21b9d-4ec3-353e-b515-67e0ec07bbe6 | -8.91232 | -70.87043 | 2026-08-28 17:47:00 | NOAA-20 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 17.8 |
| 856af9ea-a87b-3968-b886-3b2f9abd36fc | -6.52588 | -55.2537 | 2026-08-28 17:47:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 7.5 |
| b20e25bf-82de-3538-864f-f35380ec6a79 | -6.7996 | -59.40131 | 2026-08-28 17:47:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 14.2 |
| 8692d87d-e660-3d96-b1ff-3c5caea7d31e | -7.49081 | -61.40546 | 2026-08-28 17:47:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 32.2 |
| f920039e-c55c-3955-ab52-d15ebdb55f0f | -5.78832 | -57.60371 | 2026-08-28 17:47:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 13.9 |
| 97d3d2b4-f56f-3f05-ba80-bd07d76bfc1a | -3.94115 | -59.33027 | 2026-08-28 17:47:00 | NOAA-20 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 25.4 |
| c3b7b051-3b52-3fb0-babc-189d5ea79a9b | -6.77815 | -55.67965 | 2026-08-28 17:47:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 18.3 |
| f0a03782-93e9-3589-87a4-d54bf0c02b5d | -5.98284 | -61.46512 | 2026-08-28 17:47:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 25.4 |
| dd6a7faa-7e46-32f1-a2c7-904b2c27e2a3 | -4.31379 | -59.4804 | 2026-08-28 17:47:00 | NOAA-20 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 11.8 |
| 7e692d9a-9cb2-358b-a7f7-73855e7c5d74 | -7.58699 | -61.32541 | 2026-08-28 17:47:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 3.9 |
| c5b38de9-7dd4-3324-97a0-9d52ed93578f | -9.17189 | -65.78196 | 2026-08-28 17:47:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 23.5 |
| 90c4bed6-c94a-3cbf-bba5-e57b38e69aeb | -9.21282 | -65.79765 | 2026-08-28 17:47:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 7.2 |
| a190b557-d76b-3743-abf2-f72e77a72dd4 | -7.37031 | -72.65563 | 2026-08-28 17:47:00 | NOAA-20 | GUAJARÁ | AMAZONAS | Brasil | 1301654 | 13 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 9b17ec2b-11ac-3ea6-8427-4f464e88a2b4 | -4.6065 | -54.86897 | 2026-08-28 17:47:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 4cc6e8ba-60a0-3106-8457-e3bf25d3c5c0 | -7.58583 | -61.31802 | 2026-08-28 17:47:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 5ef93566-7a8b-3e56-a748-aeb8b0acf857 | -9.13609 | -67.85773 | 2026-08-28 17:47:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 3.9 |
| cf13ab66-fb6a-3064-9bd6-c927c79e37cd | -8.74823 | -70.57524 | 2026-08-28 17:47:00 | NOAA-20 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 20.0 |
| dc530190-b7b1-32cc-91a6-b0673f6107ae | -6.9533 | -59.48949 | 2026-08-28 17:47:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 30.6 |
| 9e2c2fa8-1b5e-39b3-8f84-ee9719b556d6 | -3.62871 | -60.54133 | 2026-08-28 17:47:00 | NOAA-20 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 10.3 |
| 754ebaf8-7520-3df6-ae6f-ec45d230dfba | -9.54089 | -66.77514 | 2026-08-28 17:47:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 3.5 |
| d11e0fd4-51d1-34f6-87ef-8b7066fabaca | -8.25585 | -73.31538 | 2026-08-28 17:47:00 | NOAA-20 | CRUZEIRO DO SUL | ACRE | Brasil | 1200203 | 12 | 33 | nan | nan | nan | Amazônia | 9.5 |
| 598482c4-804a-3c85-9507-a9b7e3abde74 | -4.30064 | -59.47251 | 2026-08-28 17:47:00 | NOAA-20 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 25.2 |
| 212cb10c-f794-3510-adc3-f79823222923 | -8.95713 | -71.40402 | 2026-08-28 17:47:00 | NOAA-20 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 7d7768f4-c8bd-38d2-aba6-e7416d8a8864 | -6.94756 | -58.95795 | 2026-08-28 17:47:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 7.6 |


[Clique aqui para ver as próximas entradas](README150.md)
