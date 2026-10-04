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

## Dados Diários - Página 35

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 19429553-86f1-3063-88e9-cf1113b01692 | -2.98811 | -51.04771 | 2026-10-04 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 5e77f953-98df-3590-8061-3b2885a6b5e4 | 2.87174 | -60.54964 | 2026-10-04 04:55:00 | NPP-375D | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 8.7 |
| 8592ba90-4c0a-3a1a-81cf-96f2e9e1d0ab | -2.53745 | -58.03702 | 2026-10-04 04:55:00 | NPP-375D | SÃO SEBASTIÃO DO UATUMÃ | AMAZONAS | Brasil | 1303957 | 13 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 4c10023c-fe35-3db5-972b-7d12f843e673 | -3.07711 | -51.27502 | 2026-10-04 04:55:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ef072ab1-390b-3d85-a1ca-d2ff6e36c88a | -2.6837 | -49.14163 | 2026-10-04 04:55:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a93dfbac-ff59-3767-b27c-19a5b7cf966a | -3.12671 | -53.72945 | 2026-10-04 04:55:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 3ca17392-af1f-333b-ada9-b2c3c759d067 | -2.90743 | -54.1363 | 2026-10-04 04:55:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| a9b0c128-491c-352e-9d68-3757774347ca | -4.35899 | -47.77611 | 2026-10-04 04:55:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| cef80bab-75da-33a0-926f-a0b9c0d84161 | -1.12074 | -54.14783 | 2026-10-04 04:55:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 46bfde4b-2583-3dcb-8d70-08397cb8a3d2 | -3.35738 | -43.38179 | 2026-10-04 04:55:00 | NPP-375D | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 68b9e3b0-9b90-3921-a2f5-3747bbc5331c | -3.70086 | -54.19574 | 2026-10-04 04:55:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 55d9434b-e9ee-3d56-9381-9454d2949f82 | -3.28527 | -53.82803 | 2026-10-04 04:55:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 287a6370-2c2a-3da5-91a3-5d50ac8c5dec | -3.81383 | -50.84947 | 2026-10-04 04:55:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 667e8e10-fc52-3d9a-aac1-ea782ed42aa6 | -3.47113 | -50.09288 | 2026-10-04 04:55:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 10.9 |
| 594e98ba-3e8a-30e4-95a9-9782a9a79893 | -3.13332 | -53.72512 | 2026-10-04 04:55:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 66fcff44-b195-3064-ad08-c0f368e75169 | -3.06613 | -49.52792 | 2026-10-04 04:55:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 24e359ec-0332-3521-b1fb-3852717ce449 | -2.87896 | -51.03066 | 2026-10-04 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 5c841628-fbb4-3f67-8054-4024b881b4f8 | -3.20138 | -50.74559 | 2026-10-04 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 3eac1270-c1b5-357c-81d3-032cac3ee276 | -3.87961 | -49.69486 | 2026-10-04 04:55:00 | NPP-375D | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e5c3cf34-87b0-30a7-adda-38b63e8f7ade | 2.86831 | -60.55315 | 2026-10-04 04:55:00 | NPP-375D | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 43c1b5c2-5f7d-3a1b-8721-a09e55e8171e | -4.11545 | -49.06825 | 2026-10-04 04:55:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 666775af-4368-3842-947a-e701d1999557 | -3.07262 | -51.28157 | 2026-10-04 04:55:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 9d2a3d2f-8aac-307c-9c78-b6ece5dc6e8b | -2.79166 | -54.11066 | 2026-10-04 04:55:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| a32848f9-932a-3c6e-965d-542a9a1d656c | -4.05568 | -51.11984 | 2026-10-04 04:55:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| e0c69d08-11a1-3506-bf91-eed8fa1a7645 | -3.27924 | -53.81828 | 2026-10-04 04:55:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| d49a621f-8ce0-3d27-bd25-b622b1bcb2f0 | -3.70906 | -50.66246 | 2026-10-04 04:55:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| a494ff48-dbf6-34a7-9c53-13a879347320 | -4.27783 | -50.27332 | 2026-10-04 04:55:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 125.5 |
| fd9fb002-9288-32f6-a8ee-0d4d32f6b8ec | -2.83266 | -50.47062 | 2026-10-04 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 7e69d25b-2ed4-38a1-b4d3-ebe5acd4e7f5 | -3.18036 | -48.68832 | 2026-10-04 04:55:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b614ef1d-5c4e-3fcb-a544-12982b4c5fce | -2.82581 | -54.11617 | 2026-10-04 04:55:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 0b26e1be-9c3e-3c82-93cc-7fda8f89b0e5 | -2.8197 | -54.10574 | 2026-10-04 04:55:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 7b326547-e90d-3719-a1a9-ace44540d763 | -3.12747 | -53.73755 | 2026-10-04 04:55:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c6efa257-0694-3471-8918-984a6de0c4de | -3.20416 | -50.74959 | 2026-10-04 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| d140368a-60bd-3cec-b455-591c03b8a45a | -2.08348 | -47.8529 | 2026-10-04 04:55:00 | NPP-375D | SÃO DOMINGOS DO CAPIM | PARÁ | Brasil | 1507201 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3b7825a2-583c-3c29-90db-4e60d27868b3 | 2.87096 | -60.54454 | 2026-10-04 04:55:00 | NPP-375D | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 3.8 |
| bba61e25-44cb-3f6d-b451-596648064d7e | -2.44764 | -50.25394 | 2026-10-04 04:55:00 | NPP-375D | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 19.4 |
| 09b18008-09d4-3d0a-9db0-5b9b3a64e340 | -2.59498 | -51.84874 | 2026-10-04 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 216b2bec-6209-3be6-a581-0f7d57d787e4 | -3.11653 | -53.74566 | 2026-10-04 04:55:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| d066b902-7a2d-3232-b177-432a0e84fc82 | -2.81138 | -54.10912 | 2026-10-04 04:55:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 0b7a1ff9-9654-33b1-a4bb-0901d2e4d045 | -2.68913 | -54.64201 | 2026-10-04 04:55:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 12.9 |
| 677a34e8-7cbb-3c28-8adf-5f4fa54af42b | -3.18398 | -54.09528 | 2026-10-04 04:55:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 307ceaef-9452-321e-bac2-7069c28b73f6 | -3.13558 | -53.73441 | 2026-10-04 04:55:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a937278f-5602-33a7-b5b2-c27dfdb1f9fb | -2.58354 | -51.85442 | 2026-10-04 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 11.8 |
| 84184684-d734-3c5a-b8d5-6b56a43165e8 | -3.29597 | -49.1281 | 2026-10-04 04:55:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| cde8bf1c-ca21-32af-8626-6b93999ed57b | -3.04292 | -54.23141 | 2026-10-04 04:55:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 8.6 |
| 47e992f3-33e2-327a-bdc5-7dfa9a21d125 | -3.29941 | -53.83476 | 2026-10-04 04:55:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ced51749-f474-3c68-8e53-c177f42b2e19 | -3.47391 | -50.09686 | 2026-10-04 04:55:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 6d049f6f-4473-3459-8666-05c6c7ad01c1 | -3.47723 | -50.09739 | 2026-10-04 04:55:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| a291bfbf-86b9-3014-b284-26850bbdb0b0 | -1.10201 | -54.11478 | 2026-10-04 04:55:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 308e185e-3420-34a5-bf2f-66bd15e98932 | 1.75939 | -55.65398 | 2026-10-04 04:55:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c10896b8-73d5-3030-88c2-62a593dcb61d | -2.88761 | -54.09078 | 2026-10-04 04:55:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| dcbb4771-6a21-3b34-afc7-78b27dfa2e55 | -3.13134 | -53.74806 | 2026-10-04 04:55:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 48fa478b-5b4a-3068-813a-c9e5087b6934 | -3.0745 | -49.53995 | 2026-10-04 04:55:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 13.1 |
| 26a0c426-360b-3581-8ab3-e84989a94e5c | -2.55938 | -54.72625 | 2026-10-04 04:55:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 87c30be2-7e64-3581-b8af-7bd73e477637 | -3.12974 | -53.74685 | 2026-10-04 04:55:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d6061648-26e6-38da-95b3-ab50ad6cd2f2 | -2.81591 | -54.10514 | 2026-10-04 04:55:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| e7349e24-5ba7-3988-a003-255beee7f095 | -3.00422 | -53.8695 | 2026-10-04 04:55:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 40f63dc3-9ce4-3dbc-8972-33eb3663537c | -4.26455 | -49.97648 | 2026-10-04 04:55:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 3916662b-c59f-394e-8440-085b3ca7d1fb | -2.97305 | -54.09055 | 2026-10-04 04:55:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 7ca9c39f-bd50-3221-b0db-dd8dbc4ac13c | -2.68376 | -54.42902 | 2026-10-04 04:55:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| b4fb7056-0c24-32f6-9e39-83faa4f5a8ea | -2.81906 | -54.134 | 2026-10-04 04:55:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| ac0a256f-036f-30a3-85cb-0d3918068499 | -3.10402 | -50.29697 | 2026-10-04 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c8ff2d04-3d50-3efa-b858-10b5413277f3 | -3.07336 | -49.52548 | 2026-10-04 04:55:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| f63c674d-b4d1-3d3b-b6ea-6de399d49f4e | -2.86119 | -49.62804 | 2026-10-04 04:55:00 | NPP-375D | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 87742d2e-57c8-303b-baff-ee0b8c44f420 | -4.27073 | -50.74391 | 2026-10-04 04:55:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d32c2270-3fd2-33bf-8fd6-37b7a8034b84 | -3.08283 | -49.53054 | 2026-10-04 04:55:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 35cf2fa1-3a6e-3b50-becf-c18127c13bad | -3.01116 | -50.47367 | 2026-10-04 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 29931022-a6ea-3f85-9fc9-5bdcbfa7f56c | -3.16423 | -59.09299 | 2026-10-04 04:55:00 | NPP-375D | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c40ad021-f7cf-33d3-ab17-b1aa5c04821a | -2.97952 | -54.09388 | 2026-10-04 04:55:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 08d349d5-5399-3ff0-91e6-56ba256d65c0 | 1.03722 | -59.46505 | 2026-10-04 04:55:00 | NPP-375D | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 21c9be2e-59b2-3fd8-b48e-63b38d02e3a4 | -3.12971 | -53.7344 | 2026-10-04 04:55:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| fafcb68e-22dd-34ec-8e59-fcc87f2ecb4f | -2.55814 | -49.75091 | 2026-10-04 04:55:00 | NPP-375D | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| c365bbbb-b207-3322-b058-059b40fd8628 | -3.52641 | -54.61531 | 2026-10-04 04:55:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 234e7320-868a-329d-aa34-f676ea15f92d | -2.97196 | -54.09265 | 2026-10-04 04:55:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 060f900c-c9fe-31de-8729-8982be36bed4 | -2.852 | -51.28665 | 2026-10-04 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 72f78926-497f-3349-b588-6d6c5a410037 | 1.92813 | -55.72176 | 2026-10-04 04:55:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9235a99e-a0c3-323c-87a7-d40e73fbaacc | -2.96967 | -53.26437 | 2026-10-04 04:55:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 28ce7819-fbcc-3075-a868-ea6bfb1abaf8 | -3.89149 | -49.69657 | 2026-10-04 04:55:00 | NPP-375D | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 1140f8a5-3762-3df0-a84a-1cf5983002b2 | -3.57589 | -54.65297 | 2026-10-04 04:55:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 0bd0a120-c2aa-3028-9631-13d5afdf17e0 | -1.87215 | -50.61784 | 2026-10-04 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6f774d4c-110b-39a7-b971-b2b5ebfe91f8 | -2.44289 | -49.0254 | 2026-10-04 04:55:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 77fad4ac-2d8f-3b89-a40e-48a52fe8c6c5 | -3.00825 | -53.87256 | 2026-10-04 04:55:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 6f689326-7858-309d-bb69-f8a35a559e8a | -2.77101 | -57.7025 | 2026-10-04 04:55:00 | NPP-375D | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 24e3407a-31fd-36cd-b72f-b6c55f05c43d | -4.45989 | -49.69905 | 2026-10-04 04:55:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d7174293-26e6-381a-ae10-45e0971d6f97 | -2.90818 | -54.13169 | 2026-10-04 04:55:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| eb94362e-2b25-3c92-ba43-fb335d0f425b | -3.17201 | -48.58698 | 2026-10-04 04:55:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| babb28ae-0077-33c5-bcf1-f1108163c3c3 | -3.12963 | -53.72452 | 2026-10-04 04:55:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| aff7cc95-f62d-38e6-87f3-8ba1ad2703c1 | -2.91428 | -54.14213 | 2026-10-04 04:55:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| ce428495-ae90-3391-832b-08e7cb330adf | -4.81361 | -45.65284 | 2026-10-04 04:55:00 | NPP-375D | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 33b13838-9fb6-305e-a0df-3990a7876d04 | -3.29261 | -49.12757 | 2026-10-04 04:55:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ef5e4127-9536-3b17-bc3b-511bf26dc9ad | -4.25745 | -50.78443 | 2026-10-04 04:55:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 04de1e8a-9d34-3695-b7de-7a29d30f130f | -2.97449 | -54.08142 | 2026-10-04 04:55:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 685a0aa0-719d-3e63-bdf0-4a7202ea6057 | -3.81438 | -50.84599 | 2026-10-04 04:55:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ab9ac36a-08d7-37b5-89a8-9fd697003df5 | 3.64546 | -60.76265 | 2026-10-04 04:55:00 | NPP-375D | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 2.3 |
| e46f7282-74c6-3bf3-bcd4-d98f3ab26d1e | -3.81134 | -50.84903 | 2026-10-04 04:55:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 8fc72f32-bfed-3a86-af5d-ac69860542d0 | -4.26769 | -46.3714 | 2026-10-04 04:55:00 | NPP-375D | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 24.6 |
| 11c7946f-b8ab-3a7b-898d-2599b02a5cb6 | -2.80387 | -54.1315 | 2026-10-04 04:55:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| b8ef0c88-e396-3aad-89fe-a4221ea26bb6 | -3.29871 | -53.83914 | 2026-10-04 04:55:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a1b02f00-8ec3-3841-b358-2b4d09c8003b | 1.04298 | -59.46414 | 2026-10-04 04:55:00 | NPP-375D | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 6423425d-a2aa-3fb9-a7d2-25305915924c | -2.85019 | -54.13427 | 2026-10-04 04:55:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |


[Clique aqui para ver as próximas entradas](README36.md)
