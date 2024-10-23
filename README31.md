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

## Dados Diários - Página 31

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| cb69d6e8-886b-35b7-8a43-f866e061d2a2 | 0.97657 | -51.1553 | 2024-10-23 04:49:00 | NOAA-21 | FERREIRA GOMES | AMAPÁ | Brasil | 1600238 | 16 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 8a215343-98cc-332c-b0ba-bf62bdae6a9d | 0.97603 | -51.15187 | 2024-10-23 04:49:00 | NOAA-21 | FERREIRA GOMES | AMAPÁ | Brasil | 1600238 | 16 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 3ceaa4a1-dd9e-36a5-abe8-6b987b128c2d | 0.97327 | -51.15581 | 2024-10-23 04:49:00 | NOAA-21 | FERREIRA GOMES | AMAPÁ | Brasil | 1600238 | 16 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 656ab25f-487a-3ac9-bc99-6713eea45984 | 0.97273 | -51.15238 | 2024-10-23 04:49:00 | NOAA-21 | FERREIRA GOMES | AMAPÁ | Brasil | 1600238 | 16 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 6c013d4e-a879-3f5b-bd32-0bb814a692d8 | 0.97051 | -51.15974 | 2024-10-23 04:49:00 | NOAA-21 | FERREIRA GOMES | AMAPÁ | Brasil | 1600238 | 16 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 683ab665-711f-35a6-a695-824c8073d0b3 | 0.96997 | -51.15632 | 2024-10-23 04:49:00 | NOAA-21 | FERREIRA GOMES | AMAPÁ | Brasil | 1600238 | 16 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 930063e7-bea2-30a7-a8b1-0ee11f8a4f64 | 0.96721 | -51.16025 | 2024-10-23 04:49:00 | NOAA-21 | FERREIRA GOMES | AMAPÁ | Brasil | 1600238 | 16 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d69bdf35-f5d9-3385-8068-636bf1578ccf | 0.3469 | -50.9847 | 2024-10-23 04:49:00 | NOAA-21 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a95d8464-4129-3d66-8e77-ece7b2eaedf5 | -1.8492 | -50.65218 | 2024-10-23 04:49:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| d171043b-47f6-36fe-a651-dff031f6edd5 | -1.84588 | -50.65166 | 2024-10-23 04:49:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 3bf5dbc9-dfc0-36bd-a1a3-375144240f65 | -1.67466 | -50.42066 | 2024-10-23 04:49:00 | NOAA-21 | BREVES | PARÁ | Brasil | 1501808 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 806fa5f6-7f5b-3a09-a59c-998575eacebf | -1.32361 | -50.64107 | 2024-10-23 04:49:00 | NOAA-21 | BREVES | PARÁ | Brasil | 1501808 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 30395c7c-74f7-398b-a181-f910e3ccafe0 | -0.73952 | -51.11051 | 2024-10-23 04:49:00 | NOAA-21 | BREVES | PARÁ | Brasil | 1501808 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 0235d86c-124e-3e23-88d9-3eb5bf9b3e57 | 3.52465 | -51.45436 | 2024-10-23 04:49:00 | NOAA-21 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 0.4 |
| de33a01c-d33b-3b7f-9a10-e08a96df8044 | 3.4853 | -51.267 | 2024-10-23 04:49:00 | NOAA-21 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 71d83627-63d5-36af-b05e-5303351f9a8a | 3.48198 | -51.26751 | 2024-10-23 04:49:00 | NOAA-21 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9669f3ed-2f60-30ce-8189-7bde125ae8ad | 1.00974 | -52.21648 | 2024-10-23 04:49:00 | NOAA-21 | PEDRA BRANCA DO AMAPARI | AMAPÁ | Brasil | 1600154 | 16 | 33 | nan | nan | nan | Amazônia | 1.4 |
| cbd2ca9b-80bd-32ea-adc3-d67ed85ddaff | 0.50356 | -51.6768 | 2024-10-23 04:49:00 | NOAA-21 | PORTO GRANDE | AMAPÁ | Brasil | 1600535 | 16 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d93b0d35-e780-36d9-81e9-fc484bd62192 | -0.12452 | -51.6451 | 2024-10-23 04:49:00 | NOAA-21 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e231b80c-87ae-3ccf-81b7-e89c3b1818e4 | -0.12398 | -51.64853 | 2024-10-23 04:49:00 | NOAA-21 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 40304683-296a-3784-b081-fb643cab16fe | -0.12176 | -51.64115 | 2024-10-23 04:49:00 | NOAA-21 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 1a5955cc-2f11-3f60-9bed-f1e6f838cf55 | -0.12122 | -51.64459 | 2024-10-23 04:49:00 | NOAA-21 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 219df83e-deb4-37ff-b18a-9bd4394de766 | -0.11846 | -51.64064 | 2024-10-23 04:49:00 | NOAA-21 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 3b8a5e53-8f0e-3058-affa-0e4ba92d73a9 | -0.11792 | -51.64408 | 2024-10-23 04:49:00 | NOAA-21 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 39e1bae1-a240-3e9f-b45b-0b5266937ca6 | -1.55834 | -52.26691 | 2024-10-23 04:49:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8000ecba-7a3b-3643-b4a1-fe2f76943c90 | -1.55502 | -52.2664 | 2024-10-23 04:49:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| c75bcedc-ffa6-33b4-a5e9-b3f0b75b391b | -1.55435 | -52.20598 | 2024-10-23 04:49:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 0.3 |
| 1960c2ea-e26e-3876-82bc-399efe326652 | -1.55158 | -52.20201 | 2024-10-23 04:49:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 5e797728-bbb0-37a8-85b0-695ada235a89 | -1.53779 | -51.94144 | 2024-10-23 04:49:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| d9c6c9c9-93b4-3b0f-a30d-7a5a18e7cb75 | -1.53752 | -52.02951 | 2024-10-23 04:49:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 5209bbe4-7947-3ede-915b-b229402e5b82 | -1.53064 | -51.94386 | 2024-10-23 04:49:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2c044fdc-b2a2-3b6c-a679-02db49565c0c | -1.43603 | -52.2438 | 2024-10-23 04:49:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8b7cc615-3d06-32f0-920d-4eff09dc1ca1 | -1.39877 | -52.00434 | 2024-10-23 04:49:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| f4526ae0-2317-358a-871e-edab8cd1ef2c | -1.396 | -52.00039 | 2024-10-23 04:49:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| d00202ef-ed3f-3c29-983f-4185db508b37 | -1.39324 | -51.99643 | 2024-10-23 04:49:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 12.6 |
| 0e4ab2bd-17c1-395b-a112-c6a968859eaf | -1.3927 | -51.99988 | 2024-10-23 04:49:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 12.6 |
| 1dab8704-a66f-3bbd-84b6-9773329fd923 | -1.39047 | -51.99248 | 2024-10-23 04:49:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 868b9c9c-0911-34f2-af78-5ed6cf95320f | -1.38993 | -51.99592 | 2024-10-23 04:49:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 12.6 |
| 3c350093-a4ea-39a7-a67d-30087efb10ec | -1.3896 | -52.27909 | 2024-10-23 04:49:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 070a65ed-fb2b-34ad-bb70-8cd33162b6cf | -1.38717 | -51.99197 | 2024-10-23 04:49:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| fdb697fc-bada-36ad-acf9-cd97b5f1e172 | -1.38663 | -51.99541 | 2024-10-23 04:49:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 12.2 |
| 3e5e996e-f631-3812-aeb1-294cfe668ab9 | -1.38386 | -51.99146 | 2024-10-23 04:49:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 2dd3459b-c85b-33ef-8c72-ad90aa2e00db | -0.95028 | -52.08602 | 2024-10-23 04:49:00 | NOAA-21 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 32b21e25-c230-3621-b3de-3f479bf2dbf5 | -0.8556 | -52.34183 | 2024-10-23 04:49:00 | NOAA-21 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 09a51c5f-35b6-3042-80dd-1a0b923d1793 | -1.46611 | -52.80894 | 2024-10-23 04:49:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 409c2a11-6140-3e04-938f-ceb163f18852 | -1.4167 | -52.67027 | 2024-10-23 04:49:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 75f3965a-93bc-3ec6-80d0-a1986200d737 | -1.28367 | -53.05523 | 2024-10-23 04:49:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 218c4062-5f26-3f5d-87d5-3faaf16a49b6 | -1.25717 | -53.37589 | 2024-10-23 04:49:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 4b8f6263-7509-3238-ad6c-73c828a3219b | -1.22925 | -54.14758 | 2024-10-23 04:49:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 606be9ce-096c-3159-8607-e63f22913b1d | -1.21521 | -53.37353 | 2024-10-23 04:49:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 52a01320-cc8d-3d32-ba6e-784ec2b80956 | -1.21236 | -53.36941 | 2024-10-23 04:49:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 8d5ba41d-6849-3efa-9199-4b95e146d309 | -1.21179 | -53.37305 | 2024-10-23 04:49:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 72c68875-e5b7-3a64-b689-4f166039b45f | -1.20084 | -53.64218 | 2024-10-23 04:49:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ab8c0e8a-2c52-3246-8587-2e3885011077 | -1.20026 | -53.64587 | 2024-10-23 04:49:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a94db737-7e89-3d0a-b604-6d4c1fee2ce4 | -1.17716 | -53.65765 | 2024-10-23 04:49:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 8e75f6d1-3cd6-3fe2-8a47-85480d3d14ff | -1.17656 | -53.6614 | 2024-10-23 04:49:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c14884c5-14a4-3f37-bc86-467b1dfc64de | -1.1101 | -54.21182 | 2024-10-23 04:49:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 66cc4054-1a23-329b-8bf2-63d515462ec2 | -1.08792 | -54.16826 | 2024-10-23 04:49:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 02c2acd9-d8b1-3025-bbf9-3b9528a4051f | -1.08476 | -54.11893 | 2024-10-23 04:49:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 705b007f-6b16-3e7d-951f-2a1b954a243d | -1.08439 | -54.16768 | 2024-10-23 04:49:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 1ec2fd40-5c97-32dd-8903-de6769d4aa9b | -0.40122 | -55.64291 | 2024-10-23 04:49:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| ef3ae1fa-7892-358c-a39f-038ee5aaa570 | -6.73442 | -40.48852 | 2024-10-23 04:51:00 | NOAA-21 | PIO IX | PIAUÍ | Brasil | 2208205 | 22 | 33 | nan | nan | nan | Caatinga | 3.4 |
| b0d0c49d-7806-3021-9914-3f019022f2a1 | -9.1477 | -40.6533 | 2024-10-23 04:51:00 | NOAA-21 | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 2.9 |
| ae3c0975-c8da-336a-bedb-3d33af8d62cc | -9.09737 | -40.3676 | 2024-10-23 04:51:00 | NOAA-21 | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 4.0 |
| 3af506a7-d888-337d-89ee-8ddad79f7848 | -10.65803 | -40.8169 | 2024-10-23 04:51:00 | NOAA-21 | MIRANGABA | BAHIA | Brasil | 2921401 | 29 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 6dc79fd7-85b3-3fd1-bbfe-5648a5a412fd | -5.32985 | -41.53029 | 2024-10-23 04:51:00 | NOAA-21 | CASTELO DO PIAUÍ | PIAUÍ | Brasil | 2202604 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 6ccee944-4946-3f3a-8429-b6410bd8bd11 | -5.26998 | -41.19368 | 2024-10-23 04:51:00 | NOAA-21 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| bbaa4e07-dc77-38dc-84fe-e8730bce2b55 | -5.2639 | -41.19283 | 2024-10-23 04:51:00 | NOAA-21 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| c7ae2de6-14be-3dd9-a588-2460e8cf48ac | -3.71736 | -41.6845 | 2024-10-23 04:51:00 | NOAA-21 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 6.4 |
| b1f6e4ab-3558-3231-a2f8-c4a8f57d3ad5 | -3.71678 | -41.68852 | 2024-10-23 04:51:00 | NOAA-21 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 6.4 |
| e4a6b9de-7a2d-353a-959e-5da80c0e102a | -3.80561 | -42.54673 | 2024-10-23 04:51:00 | NOAA-21 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 3a1e2c49-99df-3c35-a7d7-44dafe7359e1 | -3.80509 | -42.55026 | 2024-10-23 04:51:00 | NOAA-21 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 41eb8b34-785b-38cc-bfbc-4b067b462ed1 | -5.77205 | -42.6387 | 2024-10-23 04:51:00 | NOAA-21 | AGRICOLÂNDIA | PIAUÍ | Brasil | 2200103 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 12fcb0c2-e16b-344a-9d2a-5b6bffd00df9 | -5.77156 | -42.64208 | 2024-10-23 04:51:00 | NOAA-21 | AGRICOLÂNDIA | PIAUÍ | Brasil | 2200103 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 70a5538b-c12b-3dc0-999d-8e860c8e40a4 | -5.77097 | -42.64 | 2024-10-23 04:51:00 | NOAA-21 | AGRICOLÂNDIA | PIAUÍ | Brasil | 2200103 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 7728996b-8c25-31b4-87bc-03b403c2da88 | -5.70522 | -42.50465 | 2024-10-23 04:51:00 | NOAA-21 | PASSAGEM FRANCA DO PIAUÍ | PIAUÍ | Brasil | 2207751 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| f02b920a-2091-369f-ac38-711581fe328b | -5.69959 | -42.50391 | 2024-10-23 04:51:00 | NOAA-21 | PASSAGEM FRANCA DO PIAUÍ | PIAUÍ | Brasil | 2207751 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| e4a9dedb-4ad5-3c1c-ae13-0cfe99ce8bd5 | -5.69451 | -42.49907 | 2024-10-23 04:51:00 | NOAA-21 | PASSAGEM FRANCA DO PIAUÍ | PIAUÍ | Brasil | 2207751 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| f8c566c2-c465-3a7c-9d5f-c9d2df09248b | -5.53721 | -42.21535 | 2024-10-23 04:51:00 | NOAA-21 | ALTO LONGÁ | PIAUÍ | Brasil | 2200301 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 23dd2af5-efb7-3d74-adb3-b6d0da29c2cc | -5.53665 | -42.21943 | 2024-10-23 04:51:00 | NOAA-21 | ALTO LONGÁ | PIAUÍ | Brasil | 2200301 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| db8c4b96-f5c0-34bc-ad4b-86f16be99b24 | -5.07801 | -42.5627 | 2024-10-23 04:51:00 | NOAA-21 | ALTOS | PIAUÍ | Brasil | 2200400 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| ed945dfd-1fa1-32ab-80b7-3e1cf54799df | -5.71316 | -43.26222 | 2024-10-23 04:51:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 32d280ca-fc27-3da2-8351-bf8ede8cf8c5 | -5.70826 | -43.25827 | 2024-10-23 04:51:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| e9d79ecf-f36f-3516-a4d0-a754b96ded12 | -5.70782 | -43.26147 | 2024-10-23 04:51:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 7e170f9c-216f-3e32-985d-f5fc5af9c88a | -5.65344 | -43.23368 | 2024-10-23 04:51:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 7d60c971-4ee9-3f44-9405-6816158de4ab | -5.64809 | -43.23298 | 2024-10-23 04:51:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 11aaa890-d6b7-345c-a72c-df66453f1e05 | -5.62388 | -43.28846 | 2024-10-23 04:51:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 824ac686-aad5-324f-8537-2bc584316c48 | -5.62342 | -43.29176 | 2024-10-23 04:51:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| fc2a1502-5f31-3393-8172-acfe6c0a0d33 | -5.61855 | -43.28771 | 2024-10-23 04:51:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| a0e309ac-d6f9-3b8d-beb6-42396a33a47e | -5.61809 | -43.29101 | 2024-10-23 04:51:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 0879edb5-2dff-375b-ae99-dfc3033320f7 | -5.57923 | -43.25752 | 2024-10-23 04:51:00 | NOAA-21 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 18.8 |
| 74e859fa-8b1f-3875-91ca-53104de4bf24 | -5.57875 | -43.26097 | 2024-10-23 04:51:00 | NOAA-21 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 18.8 |
| 1e726d79-5a62-3590-979d-5df97f295ee5 | -5.57635 | -43.25248 | 2024-10-23 04:51:00 | NOAA-21 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 7.5 |
| f1f81ced-c698-315a-a78b-9e0ccafd18d1 | -5.57585 | -43.25592 | 2024-10-23 04:51:00 | NOAA-21 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 35.9 |
| 750b1ed3-b9f7-3415-b46f-cbf335bbd143 | -5.57536 | -43.25933 | 2024-10-23 04:51:00 | NOAA-21 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 35.9 |
| ede756fe-45a5-387c-ae16-7de35a79aa37 | -5.57486 | -43.26273 | 2024-10-23 04:51:00 | NOAA-21 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 16.1 |
| a1b20ac1-7c7e-3477-8772-7e67e3823a6a | -5.57437 | -43.25323 | 2024-10-23 04:51:00 | NOAA-21 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 18.9 |
| c4b0e570-5bb0-3883-b86a-af56b2eee57c | -5.5739 | -43.25665 | 2024-10-23 04:51:00 | NOAA-21 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 18.8 |
| dc1a58f6-ef81-3eaf-b299-9d21446a936b | -5.57344 | -43.26004 | 2024-10-23 04:51:00 | NOAA-21 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 18.8 |
| dbb768bf-2d9b-3682-9c44-87bb1f6318a1 | -5.57052 | -43.25511 | 2024-10-23 04:51:00 | NOAA-21 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |


[Clique aqui para ver as próximas entradas](README32.md)
