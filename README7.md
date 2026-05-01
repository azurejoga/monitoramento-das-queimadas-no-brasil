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

## Dados Diários - Página 7

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 733e5f7e-dabd-3b97-ae6a-b48116e630d1 | -10.9811 | -45.1104 | 2026-05-01 06:50:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 57.1 |
| 194919b2-ce34-313f-9fcc-c1a4f8f83168 | -11.001 | -45.0617 | 2026-05-01 06:50:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 48.5 |
| e6a962a0-14fd-36ad-8737-23022d9707d5 | -10.9819 | -45.0643 | 2026-05-01 06:50:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 107.1 |
| 074aa990-57ec-379d-b34e-867c2cdbb0f0 | -11.0006 | -45.0847 | 2026-05-01 06:50:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 79.7 |
| 80eb777c-f6ed-3dfd-a7eb-7df3d83a8c18 | -10.9819 | -45.0643 | 2026-05-01 07:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 100.0 |
| 702e1b7e-2ece-319b-bcbc-14363e9e4f50 | -10.9624 | -45.09 | 2026-05-01 07:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 89.0 |
| 92407742-661e-378f-9b09-be3ca54e634d | -10.9815 | -45.0874 | 2026-05-01 07:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 240.6 |
| be6bcf03-a276-3896-a529-0b4070acf78d | -11.001 | -45.0617 | 2026-05-01 07:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 45.4 |
| 8321158f-00a1-388b-9ca2-cf3c6b21b444 | -10.9811 | -45.1104 | 2026-05-01 07:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 68.9 |
| a9c2bb3b-fb9c-3e6a-be4c-6fe8a454b9c2 | -11.0006 | -45.0847 | 2026-05-01 07:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 74.4 |
| b4595c72-56a0-3aa1-8571-65cd83dd7de9 | -10.9624 | -45.09 | 2026-05-01 07:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 100.0 |
| 31c34365-ceba-3abd-aa39-121c5012aa69 | -10.9815 | -45.0874 | 2026-05-01 07:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 245.1 |
| 661631c8-d2ef-3265-97df-27d67ed07507 | -11.001 | -45.0617 | 2026-05-01 07:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 42.3 |
| fa8c6932-74a9-3d6e-8776-013ecb0da231 | -10.9819 | -45.0643 | 2026-05-01 07:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 92.1 |
| 8de5338e-acdd-390f-b3a2-c3af1e9eccac | -11.0006 | -45.0847 | 2026-05-01 07:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 84.9 |
| b3434e00-1a25-3be1-8ce4-e3cab50b5394 | -10.9811 | -45.1104 | 2026-05-01 07:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 51.9 |
| 7cf755c9-88b9-324e-9a79-cc3e5370fd32 | -10.9815 | -45.0874 | 2026-05-01 07:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 237.5 |
| 1f3333ca-efcf-399b-b283-afe45b90365f | -10.9624 | -45.09 | 2026-05-01 07:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 104.1 |
| a299f94a-907d-3b08-a1a6-e856942e21fc | -10.9819 | -45.0643 | 2026-05-01 07:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 89.0 |
| eaf4ef72-683b-3abd-9b50-ffa388d3b7b3 | -10.9811 | -45.1104 | 2026-05-01 07:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 49.5 |
| fe1469c8-c370-3bc9-b248-54400b113d70 | -11.0006 | -45.0847 | 2026-05-01 07:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 77.4 |
| 43ab27b4-20bb-3438-bef6-8caf1538045c | -10.9819 | -45.0643 | 2026-05-01 07:50:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 83.9 |
| 34104a6b-d91c-3968-909d-cd406f3eec1f | -11.0006 | -45.0847 | 2026-05-01 07:50:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 66.8 |
| c6cb2f0a-fd79-3af6-bb4a-5bac7cdf8f30 | -10.9815 | -45.0874 | 2026-05-01 07:50:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 241.4 |
| ed5f1000-f994-38bd-9b62-4ccbcd9bd265 | -10.962 | -45.113 | 2026-05-01 07:50:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 40.0 |
| 66f75728-d99c-3cea-84b9-fcf8b32a43ed | -10.9624 | -45.09 | 2026-05-01 07:50:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 108.2 |
| fb01e708-096e-3a65-b0cf-64423fceadf5 | -10.9811 | -45.1104 | 2026-05-01 07:50:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 45.4 |
| c946ace7-2338-322f-a0e6-fe486faa1483 | -10.9819 | -45.0643 | 2026-05-01 08:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 83.3 |
| 8cbee310-6de8-38af-9bac-538b20e10bdd | -10.9811 | -45.1104 | 2026-05-01 08:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 56.8 |
| 76d0a49a-58d4-3403-9fba-c5dc4eb135b4 | -11.0006 | -45.0847 | 2026-05-01 08:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 70.6 |
| 0eb48037-610a-34a0-9d5e-6c4265dc4eaf | -10.9624 | -45.09 | 2026-05-01 08:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 95.5 |
| da1275c5-d9db-3943-b39c-1d8a1d5faa39 | -10.9815 | -45.0874 | 2026-05-01 08:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 217.9 |
| b702b340-18e8-31b4-aab3-713d325b960d | -10.9624 | -45.09 | 2026-05-01 08:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 77.7 |
| 9d2ac791-4fd6-3ec5-a936-dbd938595300 | -10.9815 | -45.0874 | 2026-05-01 08:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 247.4 |
| 413cf19e-7362-3eaa-9d93-b7507c1085b0 | -10.9811 | -45.1104 | 2026-05-01 08:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 56.5 |
| f3bf85f4-75de-34f1-bc9a-3a3a8a9f0663 | -10.9819 | -45.0643 | 2026-05-01 08:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 87.5 |
| 5885e132-803c-37ae-8597-79ffb0c07fd0 | -11.001 | -45.0617 | 2026-05-01 08:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 39.5 |
| f981ebe1-28b3-3ed3-b4f6-90e4393aec69 | -11.0006 | -45.0847 | 2026-05-01 08:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 76.5 |
| 8a36de0d-ae33-37cc-a108-13c263c06bae | -10.9624 | -45.09 | 2026-05-01 08:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 56.5 |
| a74d8583-6739-3beb-a6a6-898916e76477 | -10.9819 | -45.0643 | 2026-05-01 08:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 83.9 |
| a68706c5-4c2f-322b-a2c5-18d0437deae7 | -10.9815 | -45.0874 | 2026-05-01 08:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 216.8 |
| 90f4aefe-2273-3e66-a15f-faa8afb2f1ae | -10.9811 | -45.1104 | 2026-05-01 08:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 40.8 |
| d9816c3d-d117-3a57-870d-7d5743ee9597 | -11.0006 | -45.0847 | 2026-05-01 08:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 57.1 |
| c4ef350e-0841-36da-957d-4f61601dded7 | -10.9815 | -45.0874 | 2026-05-01 09:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 222.6 |
| 1640225e-d133-35ff-aff2-d7ef356bd19a | -10.9815 | -45.0874 | 2026-05-01 09:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 250.8 |
| eca70abf-3d4d-39da-ad2f-71e6e3b8c38f | -10.9815 | -45.0874 | 2026-05-01 09:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 189.8 |
| 5104af39-70e7-384c-9a7b-8d61d3955a10 | -10.9815 | -45.0874 | 2026-05-01 09:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 173.0 |
| 672b879f-f5c2-3712-8bcb-7a529c36cff0 | -10.9815 | -45.0874 | 2026-05-01 09:50:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 201.9 |
| f24eec0a-ae2e-3a07-afbc-b78cf75b31a6 | -10.9815 | -45.0874 | 2026-05-01 10:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 200.1 |
| 573df6d0-30c5-33ff-94fb-f2d07684325d | -10.9815 | -45.0874 | 2026-05-01 10:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 200.5 |
| e911cb84-dcfb-37d0-af72-bdb5f087af09 | -10.9815 | -45.0874 | 2026-05-01 10:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 231.8 |
| 84c903de-83eb-3b9c-84cf-f4d03fd05eb6 | -10.9815 | -45.0874 | 2026-05-01 10:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 204.5 |


