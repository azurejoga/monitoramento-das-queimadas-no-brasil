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

## Dados Diários - Página 30

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 6b177efa-a82e-3754-8d89-d9538b98ece7 | -3.06096 | -53.28175 | 2024-11-26 04:38:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 9.8 |
| 01be6811-9873-35c5-8456-06ed4d826898 | -4.29157 | -48.21706 | 2024-11-26 04:38:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c008e7d4-215e-3c99-9a9d-664211001d8a | -2.80274 | -53.02404 | 2024-11-26 04:38:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| dedd8d3a-1ba5-344d-b485-f4682f049cc8 | -2.40704 | -53.68354 | 2024-11-26 04:38:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| fc2ec711-344a-3138-bf45-4f1f5791a53e | -3.96444 | -48.05899 | 2024-11-26 04:38:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 7.8 |
| d8815f78-96bc-3cf4-b076-1ff05ab98ca1 | -3.26724 | -50.23458 | 2024-11-26 04:38:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| fec41156-ea71-32b5-a867-7ca0808e6d68 | -3.9867 | -48.06956 | 2024-11-26 04:38:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 18.1 |
| 61f1cd8d-6626-3552-a833-41e12799644d | -3.34191 | -50.51298 | 2024-11-26 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d7a8cec4-ec98-3da4-8252-b724b066a87c | -1.6377 | -53.29995 | 2024-11-26 04:38:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| a686dde3-e4a9-39c2-87c0-c63c6770c3fc | -3.776 | -46.68572 | 2024-11-26 04:38:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| bbc7e105-b079-3361-aac3-02c715aa4611 | -3.95052 | -46.91025 | 2024-11-26 04:38:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 244af4d7-b0c6-3e13-ba29-05d9c182e5f5 | -3.49789 | -53.81526 | 2024-11-26 04:38:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 01de896c-b09c-3d43-bcb8-7fd48fd55404 | -2.17441 | -53.80199 | 2024-11-26 04:38:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 11817dc6-2ab8-3bfd-aa55-7c121a80a417 | -3.44294 | -50.01087 | 2024-11-26 04:38:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b4bb5efb-86c9-310c-a8cc-0fb9abe9f21d | -2.79258 | -53.01233 | 2024-11-26 04:38:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| dcd533d8-646a-3dc1-b004-2bba83aa4595 | -2.72083 | -46.28563 | 2024-11-26 04:38:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 75e54f78-8e11-3324-b840-9e8d306e0221 | -6.69903 | -43.06091 | 2024-11-26 04:38:00 | NPP-375D | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 0cea65f7-3dcd-3e2a-b838-0dd11e7ed9bc | -3.97111 | -48.06004 | 2024-11-26 04:38:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 17.3 |
| a7207b43-37bc-38f1-ad90-5683c5bf1488 | -6.07249 | -48.03395 | 2024-11-26 04:38:00 | NPP-375D | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 4.6 |
| a8d48db1-ca0b-3ee4-98d4-5a8967b61bc1 | -3.96195 | -46.90444 | 2024-11-26 04:38:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c4d14790-17d3-3a4b-969c-3ccd60f28bc2 | -3.84805 | -47.05293 | 2024-11-26 04:38:00 | NPP-375D | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| da51d111-d0de-34da-9541-ccf6dcb0a222 | -1.57035 | -52.00962 | 2024-11-26 04:38:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b60c1dbd-b2eb-3383-8e1a-36cea6117c56 | -4.39943 | -50.53746 | 2024-11-26 04:38:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b88b987f-7cc5-3316-917a-cb0154ec6f54 | -3.98452 | -48.08355 | 2024-11-26 04:38:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 71.4 |
| e7bcfd40-9c06-3b6b-8711-1906ca719a2e | -2.71735 | -46.28509 | 2024-11-26 04:38:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 970d46af-a797-3cc5-8fc6-4dfe9f3bf6a3 | -3.38904 | -44.17001 | 2024-11-26 04:38:00 | NPP-375D | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 10.4 |
| 4db111c4-dd8e-3595-a7b4-f8ee27e76f2c | -4.28589 | -48.55723 | 2024-11-26 04:38:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 810e1d17-2267-389c-a618-4ce5cfae428e | -7.09386 | -45.45591 | 2024-11-26 04:38:00 | NPP-375D | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| d08d6a02-3ab8-3892-ae2d-6644f4288054 | -2.77338 | -48.5786 | 2024-11-26 04:38:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 70cb9d07-3913-397e-b27d-303efb78ac1e | -2.34147 | -50.56975 | 2024-11-26 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 2ffbfc79-a24f-3b10-bc95-31092b9a256a | -3.84366 | -49.96709 | 2024-11-26 04:38:00 | NPP-375D | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| bac29f02-7626-3949-bc59-5aafbb379f89 | -4.11306 | -47.9744 | 2024-11-26 04:38:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9a37990f-dd14-39d8-97cb-d0b4a69bcefa | -3.96336 | -48.06594 | 2024-11-26 04:38:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 29.5 |
| c3107718-047d-3764-8707-b405fe3ebf35 | -4.65521 | -47.94727 | 2024-11-26 04:38:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 1ce06023-ca22-3fd6-b1e6-9e6aa8fec301 | -3.80439 | -51.26315 | 2024-11-26 04:38:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ec55e3ba-72c1-3022-9e3a-3ecde9c8f23e | -2.38714 | -48.60276 | 2024-11-26 04:38:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 0.3 |
| 126e8dc3-77f5-3040-9db9-d50e19e08156 | -4.05075 | -48.30737 | 2024-11-26 04:38:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c25e4f72-f2c2-35d6-af37-bae6ae9a1666 | -6.19159 | -43.41542 | 2024-11-26 04:38:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 789a9bc5-afb5-3261-bcbd-508d76eea665 | -3.96002 | -48.06541 | 2024-11-26 04:38:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| bad885d3-57b5-320d-a371-99c3bc9bee93 | -1.48589 | -53.81209 | 2024-11-26 04:38:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 35ba2e29-a904-38e5-95df-5178e8d17e31 | -3.98167 | -48.05806 | 2024-11-26 04:38:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 18.0 |
| a3ba2999-815b-3c21-a43b-4617633c7d79 | -3.95392 | -49.93401 | 2024-11-26 04:38:00 | NPP-375D | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 28138a10-edc4-30c4-ae40-92faf80c6b95 | -1.78844 | -52.73582 | 2024-11-26 04:38:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 8275b500-ec4a-3243-917e-b63e3adefea7 | -2.69783 | -51.99325 | 2024-11-26 04:38:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a8aca8d9-3383-3940-977a-ddd2791be87b | -2.8795 | -51.58364 | 2024-11-26 04:38:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ffd6b3a0-5fe6-362b-8475-3f58664bbd49 | -1.68834 | -52.60841 | 2024-11-26 04:38:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| f21dad5d-0290-3995-82d0-fc3d24e6a1bb | -3.97615 | -48.07154 | 2024-11-26 04:38:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 63.3 |
| 3febf58a-e375-3782-aea2-5c76744ddb6e | -3.32736 | -50.05534 | 2024-11-26 04:38:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| d801c06c-7aae-3df0-b70f-d13585ddcdd6 | -3.96723 | -48.063 | 2024-11-26 04:38:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 29.5 |
| 20b710b6-101e-3b54-845a-c3f9c8cab970 | -3.53984 | -50.45257 | 2024-11-26 04:38:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 2020c0d8-e85d-30fe-861d-2c79003fb30f | -2.7767 | -48.57912 | 2024-11-26 04:38:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 2a2a1781-6d1b-3a0c-a17e-424e954c6d34 | -3.5994 | -50.38651 | 2024-11-26 04:38:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 85c4e95a-5d23-3eb2-b09f-3cc52fe5cda9 | -2.54713 | -46.39971 | 2024-11-26 04:38:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 02b13217-f8e3-366e-ba39-838987e1b618 | -6.12555 | -46.92129 | 2024-11-26 04:38:00 | NPP-375D | LAJEADO NOVO | MARANHÃO | Brasil | 2105989 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 47f4dd8d-6601-30e6-9b92-7ce593156a12 | -3.0411 | -48.51082 | 2024-11-26 04:38:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 248d641e-e9b9-3e15-afc2-9f26ea5683f6 | -3.7342 | -49.95383 | 2024-11-26 04:38:00 | NPP-375D | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 9d7984bf-2d41-3281-8245-3c14be8006fd | -6.3688 | -47.35711 | 2024-11-26 04:38:00 | NPP-375D | PORTO FRANCO | MARANHÃO | Brasil | 2109007 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 85954a7a-ec8f-384d-9733-d0f9ed40d9d3 | -4.11842 | -48.52424 | 2024-11-26 04:38:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c48a1ebe-4739-350a-b594-331dd31c8a75 | -2.45692 | -53.70578 | 2024-11-26 04:38:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9a7cdaa6-a9e4-3ae6-8bc8-82d51e1856df | -2.80737 | -54.02367 | 2024-11-26 04:38:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| e013d2d9-6099-3151-8eaf-b7d524602250 | -2.17857 | -53.80264 | 2024-11-26 04:38:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 60f2530c-d0e3-3946-b4f6-d9bf607f4ecd | -4.2966 | -48.22853 | 2024-11-26 04:38:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| bec3e29d-ed9d-33ae-ae57-4db6913bfb97 | -6.6946 | -43.06032 | 2024-11-26 04:38:00 | NPP-375D | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| a52785ec-c5b0-30bb-8ce6-8816a0b16f4a | -3.96785 | -48.08096 | 2024-11-26 04:38:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 12.4 |
| ad42f4bf-4a89-3b70-bcaa-c9e58be842b1 | -2.71391 | -46.26116 | 2024-11-26 04:38:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 56630ade-134a-3b6d-ab2b-84132e739d04 | -3.97779 | -48.06105 | 2024-11-26 04:38:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 18.0 |
| 2fd3c8f1-c2e0-36b6-84ac-7ea4cd54eb3f | -4.31471 | -47.50918 | 2024-11-26 04:38:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 7.5 |
| b0bb289f-2b39-34bb-9912-ec4b88acc89e | -2.40351 | -53.67923 | 2024-11-26 04:38:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 845ed674-a370-3710-9598-5851db6f5a3e | -2.60436 | -46.813 | 2024-11-26 04:38:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d9c08b42-5e0b-3459-97c3-f067477d7d3e | -2.98924 | -49.58751 | 2024-11-26 04:38:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 82220a2d-da18-3ebf-bbf6-5e1c6ea19439 | -2.53104 | -45.59752 | 2024-11-26 04:38:00 | NPP-375D | SANTA LUZIA DO PARUÁ | MARANHÃO | Brasil | 2110039 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9e05e3ab-416a-3694-b478-abeeb4546921 | -4.11455 | -48.52718 | 2024-11-26 04:38:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 62256286-ca8a-35ba-aa2b-444991ac8e3b | -3.38987 | -50.32069 | 2024-11-26 04:38:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c973852c-cbbd-3627-8f99-7568c0b03959 | -3.15841 | -45.44349 | 2024-11-26 04:38:00 | NPP-375D | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 619d0dd8-6704-3332-982d-79355ec6b5e5 | -4.36943 | -48.49935 | 2024-11-26 04:38:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 3cfe121f-1337-3012-b838-afb72a085bc3 | -2.59416 | -51.82971 | 2024-11-26 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 92db44c9-5653-3d2b-9c21-c71b8c2e2498 | -3.71192 | -47.1216 | 2024-11-26 04:38:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b4691871-a9fd-3a22-bb07-09e2565ff08d | -4.31551 | -48.60438 | 2024-11-26 04:38:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e3c29099-3c3f-3e0e-b8b0-22e64047c92f | -2.5928 | -51.83276 | 2024-11-26 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 2c77b946-8bc0-31f6-9aa6-a28b57411e34 | -3.592 | -50.38907 | 2024-11-26 04:38:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| ea56487f-f6eb-3549-a1c8-fa9a9c13ec69 | -2.79179 | -53.01725 | 2024-11-26 04:38:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e88b1223-b0b6-3c72-8b44-3eb1374b0b17 | -3.96832 | -48.05603 | 2024-11-26 04:38:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 7.8 |
| c11c6882-a0f4-3641-b45d-bb7bd76ebff2 | -3.11805 | -45.08199 | 2024-11-26 04:38:00 | NPP-375D | VIANA | MARANHÃO | Brasil | 2112803 | 21 | 33 | nan | nan | nan | Amazônia | 10.8 |
| 6659431e-b624-347d-8898-a558208057ef | -3.37857 | -50.10398 | 2024-11-26 04:38:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 80f4bf88-a9e3-311b-9ca1-312fa4189ce5 | -3.07458 | -49.19969 | 2024-11-26 04:38:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| a1cb85c8-2cf0-3060-9111-bb98cdd88d8f | -3.98227 | -48.07606 | 2024-11-26 04:38:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 19.6 |
| fcc78c12-921f-319e-8a65-278f9ae40cfe | -3.21756 | -50.91735 | 2024-11-26 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 16ba1f5d-4561-3199-ba0f-d960f3b20bf5 | -3.23017 | -50.31453 | 2024-11-26 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 9d3ed444-e911-39c9-9e00-b2c0e8de133e | -3.18272 | -48.42733 | 2024-11-26 04:38:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 55243084-a3a8-337b-ba4d-572ac95bd151 | -4.24031 | -48.67405 | 2024-11-26 04:38:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 4e0e3c4e-ff4e-3f81-bcc0-9c98f3fe8f96 | -1.21314 | -54.54025 | 2024-11-26 04:38:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| a32623e0-6643-3aef-81e6-acbe7ab497de | -3.33922 | -50.04618 | 2024-11-26 04:38:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 6e866111-e6d3-3c91-95cd-8e9e170bbb99 | -4.37499 | -48.50731 | 2024-11-26 04:38:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e2c167b5-91ff-3435-85bc-1d05c7272834 | -3.28527 | -50.27479 | 2024-11-26 04:38:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 4e9ee04b-4838-3d34-b594-f0b69d2938e2 | -4.04172 | -48.25621 | 2024-11-26 04:38:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c58c168d-05f9-35e5-825d-e4f6833082c4 | -3.06492 | -53.2824 | 2024-11-26 04:38:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| bedd4ca5-3d0b-3ef6-b8c1-329c921c38df | -3.47163 | -47.68132 | 2024-11-26 04:38:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 0ce5902a-6838-3ea3-8d98-ec18850103ab | -3.5435 | -50.18833 | 2024-11-26 04:38:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 455b6699-09d9-3678-ae2c-12c571b83628 | -8.19045 | -49.09288 | 2024-11-26 04:38:00 | NPP-375D | JUARINA | TOCANTINS | Brasil | 1711803 | 17 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 07a69d9f-86c0-347a-875f-67f6461eb1e3 | -3.97002 | -48.06701 | 2024-11-26 04:38:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 71.4 |


[Clique aqui para ver as próximas entradas](README31.md)
