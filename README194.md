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

## Dados Diários - Página 194

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 27253dbb-6903-34e1-b6ce-a049137309df | -16.65007 | -55.89234 | 2024-10-09 05:06:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 3.4 |
| 50c0bf85-9fe5-3169-9e9a-68f1d9079c51 | -16.6495 | -55.89627 | 2024-10-09 05:06:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.7 |
| 3ec3bb2f-7abe-3060-9fe0-897aa38a98f1 | -16.64662 | -55.8918 | 2024-10-09 05:06:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.8 |
| 5b16910a-5023-3ca1-a0f1-7694be52f68d | -16.64604 | -55.89573 | 2024-10-09 05:06:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.9 |
| 8dd6a9e0-e8d5-3cd6-8593-8f02377cb3cb | -16.63914 | -55.89464 | 2024-10-09 05:06:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 0.7 |
| 7f18b315-72c1-3727-af8c-8f7b2c1f7336 | -16.63856 | -55.89856 | 2024-10-09 05:06:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 0.7 |
| acdfdbb9-0af7-338c-b312-be7201a49cd4 | -16.63569 | -55.89409 | 2024-10-09 05:06:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 0.7 |
| 0ae5df98-142a-3fd7-862a-5a4f9b54dfaf | -16.63511 | -55.89801 | 2024-10-09 05:06:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 0.7 |
| 8178d0fc-7fa0-35b4-8f57-2ca271329955 | -16.91438 | -55.79819 | 2024-10-09 05:06:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 16.2 |
| 4f3281d3-2ebe-3db9-a296-162a261f0c7f | -16.91307 | -55.79459 | 2024-10-09 05:06:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 15.1 |
| ff5c39d1-3e3a-3ce9-ad97-96ed2d92676f | -16.91248 | -55.79858 | 2024-10-09 05:06:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 12.1 |
| 6cbb0c33-4f6b-3182-bad5-927bdda8ea1f | -16.91204 | -55.78968 | 2024-10-09 05:06:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 13.3 |
| 0c6e55b0-3bc5-31ab-b061-ee164990dcec | -16.91147 | -55.79367 | 2024-10-09 05:06:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 13.3 |
| ad390bed-ed6f-3c31-a5d3-e47c3f2481ef | -16.9109 | -55.79765 | 2024-10-09 05:06:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 16.2 |
| de2adab8-711d-31ae-947b-87d485923668 | -16.91018 | -55.79007 | 2024-10-09 05:06:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 15.1 |
| a3d4d72b-afb7-30e7-84dc-a788df3c81af | -16.90959 | -55.79405 | 2024-10-09 05:06:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 15.1 |
| c01c0f9c-aeb2-35a1-8d68-2aad317202ca | -16.90901 | -55.79803 | 2024-10-09 05:06:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 12.1 |
| 3cb11d90-67cf-39ad-95f0-e5c098c45a40 | -16.90729 | -55.78555 | 2024-10-09 05:06:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 4.8 |
| 183fe6d2-3d19-31c3-b80c-09edad163ca0 | -16.90671 | -55.78953 | 2024-10-09 05:06:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 9.0 |
| 3505a844-b3d7-31a7-8fe2-1fe6af2d2535 | -16.90612 | -55.79351 | 2024-10-09 05:06:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 9.0 |
| e14b3177-c577-3bab-8888-10a7d3b53074 | -16.90553 | -55.7975 | 2024-10-09 05:06:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 10.0 |
| 646e4891-b1f8-3bde-8bc9-b15f99f425b5 | -16.9044 | -55.78102 | 2024-10-09 05:06:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 4.8 |
| 850950c8-10b5-3bd8-b277-d43a2605ca83 | -16.90382 | -55.78501 | 2024-10-09 05:06:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 4.8 |
| 35561523-9cfa-373e-b285-388802cbe828 | -16.90323 | -55.78899 | 2024-10-09 05:06:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 9.0 |
| e9e13704-bd88-34d2-a82f-0bfd0f6d9233 | -16.90265 | -55.79297 | 2024-10-09 05:06:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 9.0 |
| 7b0be4a9-b0e9-3671-8f82-cb2a05277829 | -16.90206 | -55.79695 | 2024-10-09 05:06:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 10.0 |
| aa580cef-e28d-37fd-913c-ddac8deda617 | -16.90093 | -55.78048 | 2024-10-09 05:06:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 3.6 |
| a48c2b8a-65fd-3dce-be32-26cd7bec047d | -16.90034 | -55.78446 | 2024-10-09 05:06:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 3.6 |
| da2bf63b-4b26-387f-aca3-03544e7f1a73 | -16.89976 | -55.78845 | 2024-10-09 05:06:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 6.9 |
| ba957e48-2be1-3fc8-aa10-a50c20a2a8f0 | -16.89917 | -55.79243 | 2024-10-09 05:06:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 6.9 |
| 4c7c9e9f-12d3-3d5a-844b-a320156fb241 | -16.89859 | -55.79641 | 2024-10-09 05:06:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 6.3 |
| 2d9e490b-51db-37ae-b1ea-55612b69ae29 | -16.89745 | -55.77994 | 2024-10-09 05:06:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 3.6 |
| ab53edf3-e33a-344e-b1c7-ba2951c4c16b | -16.89687 | -55.78392 | 2024-10-09 05:06:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 3.6 |
| c77a8354-ee65-3deb-82bf-776978610023 | -16.89628 | -55.78791 | 2024-10-09 05:06:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 6.9 |
| 0d85c1b4-3120-3f37-ad53-f6188f1f09e7 | -16.8957 | -55.79189 | 2024-10-09 05:06:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 6.9 |
| 4ed3dd37-0848-308a-8dce-1e472fffb47c | -16.89511 | -55.79586 | 2024-10-09 05:06:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 6.3 |
| 085e022b-ef70-3690-b70b-552f40cc8f31 | -16.89398 | -55.7794 | 2024-10-09 05:06:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 3.0 |
| 7ebf5fad-9743-3bf1-96e4-f1619944af11 | -16.89339 | -55.78338 | 2024-10-09 05:06:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 3.0 |
| cc0563c9-c387-3d3f-a886-d948ae817926 | -16.89281 | -55.78736 | 2024-10-09 05:06:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 4.7 |
| a0a0590e-838c-34fd-b8f3-6f8b7bf3357a | -16.89223 | -55.79134 | 2024-10-09 05:06:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 4.7 |
| 99325b19-00eb-30bf-8b0f-d5f616413348 | -16.89164 | -55.79531 | 2024-10-09 05:06:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.5 |
| a1a7e268-5390-3342-ba2e-b13d66ea5469 | -16.88934 | -55.78681 | 2024-10-09 05:06:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 4.7 |
| 699c6b28-774b-34d4-a11b-09b7c66ff691 | -16.88875 | -55.79079 | 2024-10-09 05:06:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 4.7 |
| c52a385f-86d6-390e-a422-566468211d1a | -16.88817 | -55.79476 | 2024-10-09 05:06:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.5 |
| 6df909a7-6cd5-39ba-a9df-4c02b41fe162 | -16.88761 | -55.77433 | 2024-10-09 05:06:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.9 |
| bb19065a-858d-3bf4-8d6c-67e9641bc46f | -16.88759 | -55.79874 | 2024-10-09 05:06:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.5 |
| 66ef7fd9-bbfe-3583-ad99-26de7e054b91 | -16.88645 | -55.78229 | 2024-10-09 05:06:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.1 |
| b27387e6-ccbd-323e-a47a-22968ede66a6 | -16.88586 | -55.78627 | 2024-10-09 05:06:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.7 |
| f68f0c9a-fc04-38c4-99f6-0ff60921f7d2 | -16.88528 | -55.79025 | 2024-10-09 05:06:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.7 |
| c4dbe0a3-32af-3e85-bdd1-4006a7b35736 | -16.88123 | -55.79368 | 2024-10-09 05:06:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.4 |
| 3f848707-9692-3d41-9ba2-709e0d81b088 | -16.88065 | -55.79765 | 2024-10-09 05:06:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.4 |
| 01608ad3-434d-3af7-a059-f449ab6e8e6d | -16.87717 | -55.79711 | 2024-10-09 05:06:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.1 |
| bdd4c394-2289-3050-b80c-1018e02bc895 | -16.8737 | -55.79656 | 2024-10-09 05:06:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.1 |
| f3c2a7e2-095e-30b3-bb8c-a6ba0a96b99f | -17.16476 | -56.12525 | 2024-10-09 05:06:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.2 |
| 5cf154a2-5b7e-38e6-a3cc-51e3826c25e7 | -17.16304 | -56.11301 | 2024-10-09 05:06:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 3.0 |
| bd49ba38-a2b7-3681-a29d-9fefc83bd5e7 | -17.16247 | -56.11691 | 2024-10-09 05:06:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 3.7 |
| 0d416f19-161d-3037-8368-11a689629f1b | -17.1619 | -56.12081 | 2024-10-09 05:06:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 3.7 |
| 9f22be76-5434-3fb7-9d7c-0813b6144299 | -17.16132 | -56.12471 | 2024-10-09 05:06:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.2 |
| 4cc2645e-a147-324e-a5bd-e4b09243757e | -17.1596 | -56.11246 | 2024-10-09 05:06:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 3.0 |
| 9548abab-99c9-3a60-8a73-efb8c5c1f2d5 | -17.15903 | -56.11637 | 2024-10-09 05:06:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 3.7 |
| 04dd3b43-c587-3fe0-a689-98523379a1c8 | -17.15845 | -56.12027 | 2024-10-09 05:06:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 3.7 |
| 80a05a63-25aa-320e-8a76-e69d40ebc4ff | -17.15788 | -56.12417 | 2024-10-09 05:06:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.2 |
| 9ed24592-9d29-31cb-9cfd-97a321348e28 | -17.1573 | -56.12807 | 2024-10-09 05:06:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.2 |
| f4b7ec85-0987-3f88-8be7-a4930a56759f | -17.15616 | -56.11192 | 2024-10-09 05:06:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 5.7 |
| c5cc1302-4f49-3a65-9a50-37bf0a06c1f5 | -17.15559 | -56.11582 | 2024-10-09 05:06:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 8.5 |
| 564e7c90-9993-3141-b282-422bc07cb890 | -17.15502 | -56.11973 | 2024-10-09 05:06:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 8.5 |
| d340594f-1f67-36c7-a167-f1a074744d41 | -17.15444 | -56.12363 | 2024-10-09 05:06:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 8.4 |
| 721cf197-dd1d-3833-adbb-7c667b9f28d2 | -17.15387 | -56.12753 | 2024-10-09 05:06:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 8.4 |
| 6077ca43-813d-39c9-a966-6e0d6ffcd0c7 | -17.15329 | -56.13142 | 2024-10-09 05:06:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.3 |
| e8f25504-53c0-3b89-8bf4-9873c076eb11 | -17.15272 | -56.13531 | 2024-10-09 05:06:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.3 |
| 8b11ad36-3ea8-3b14-8b08-54dc3fe39052 | -17.14756 | -56.14645 | 2024-10-09 05:06:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.2 |
| 1a88b4a3-32a3-3704-af79-e857e5d4f201 | -17.1447 | -56.14201 | 2024-10-09 05:06:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.6 |
| b8a7fa19-c379-31ce-8031-ddeeca9858ba | -17.14356 | -56.14979 | 2024-10-09 05:06:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.8 |
| 75f7fe39-a155-3691-8339-bbb5c1a6a848 | -17.08838 | -56.40526 | 2024-10-09 05:06:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.6 |
| 5b5185fe-56e9-366b-b5a5-a0bfa84a9e49 | -17.06043 | -56.02535 | 2024-10-09 05:06:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 43.4 |
| 16ea120b-7bf6-37c3-a102-22f59a8d30e5 | -17.05698 | -56.02481 | 2024-10-09 05:06:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 43.4 |
| 16c9baac-8680-30c9-b2dc-fe1edcb22742 | -17.0564 | -56.02873 | 2024-10-09 05:06:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 48.8 |
| b05baf02-4d31-309d-b80b-be3fb243bc7a | -17.05353 | -56.02427 | 2024-10-09 05:06:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 7.4 |
| baad1d54-f558-3b89-94d1-d6bf82d5f976 | -17.05296 | -56.02819 | 2024-10-09 05:06:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 8.0 |
| f9651c1f-1445-30ef-943a-2fa6c786ec97 | -17.05066 | -56.04383 | 2024-10-09 05:06:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.1 |
| 61ffa21b-2b62-33e9-bc91-50d15e31af4b | -17.04721 | -56.04328 | 2024-10-09 05:06:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.1 |
| db11dcf7-ea22-33b5-980c-d69023d383a8 | -17.03918 | -56.05002 | 2024-10-09 05:06:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |
| 45dcda15-c9e2-3b7c-b018-d23916b01991 | -17.0386 | -56.05393 | 2024-10-09 05:06:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |
| 75fc4428-240e-3acb-b78e-bd976541be6e | -17.03688 | -56.04166 | 2024-10-09 05:06:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.9 |
| 5a9c57b3-9503-3507-a376-9470762aacfb | -17.03573 | -56.04948 | 2024-10-09 05:06:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.0 |
| 0becbb75-f5dc-3153-b704-4e33b40a1ea4 | -16.98578 | -56.62186 | 2024-10-09 05:06:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.1 |
| 8bcb025a-3166-3a75-b64a-22b20d412067 | -16.9001 | -55.87299 | 2024-10-09 05:06:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.7 |
| 84eb4804-2a0e-30a2-b4d0-94782a4c7aad | -16.89791 | -55.87327 | 2024-10-09 05:06:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 3.2 |
| 101e5ff7-0718-302d-9d5a-369bb5d5120c | -16.89733 | -55.87722 | 2024-10-09 05:06:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.4 |
| 28819289-b99c-33b4-a083-a58ab47c33f0 | -16.89445 | -55.87273 | 2024-10-09 05:06:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.8 |
| 1c88f12f-c03c-3cb1-ad79-d6d3e19c3172 | -16.89386 | -55.87667 | 2024-10-09 05:06:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.2 |
| d76d1bc9-27df-3f67-8975-c288fedc0169 | -16.87999 | -55.89871 | 2024-10-09 05:06:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.1 |
| 0e755f4f-fa89-3f95-a1ce-606f8dd82f94 | -16.87654 | -55.89817 | 2024-10-09 05:06:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.5 |
| 42d04c80-2b50-3941-b632-1b083b181622 | -16.87595 | -55.90211 | 2024-10-09 05:06:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.5 |
| 38ad860b-f550-3e5f-9511-2d8d526f8335 | -16.87307 | -55.89763 | 2024-10-09 05:06:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.5 |
| 0dbf9a80-c217-388d-8875-fcf3dac840a9 | -16.87072 | -55.96158 | 2024-10-09 05:06:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.8 |
| fddc4aba-c7a5-3f5a-a69d-3367394ad62e | -16.86785 | -55.95712 | 2024-10-09 05:06:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.6 |
| d08bf4d0-66d8-312b-8d41-3abebb92cd48 | -16.86443 | -55.88418 | 2024-10-09 05:06:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.5 |
| d2eea71f-824d-3502-8711-5f027f8b5b4a | -16.86386 | -55.86391 | 2024-10-09 05:06:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.9 |
| b4cc10e7-bb8d-3c54-81fe-0382f39ca752 | -16.86097 | -55.88363 | 2024-10-09 05:06:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.5 |


[Clique aqui para ver as próximas entradas](README195.md)
