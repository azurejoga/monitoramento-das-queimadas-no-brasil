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

## Dados Diários - Página 29

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 49305ca9-3e45-340a-b3bd-0820f35a8a5e | -8.42994 | -61.54816 | 2024-09-27 01:24:00 | TERRA_M-M | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 13.4 |
| 25523cf8-7c0b-336a-a76e-11ee2492387f | -9.10889 | -61.35035 | 2024-09-27 01:24:00 | TERRA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 69.7 |
| eea5715e-f176-3dca-9e60-f66466dc8b64 | -9.12459 | -61.36965 | 2024-09-27 01:24:00 | TERRA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 77.3 |
| 655f2740-af1b-3448-ab68-974d6938aee5 | -7.29949 | -61.08115 | 2024-09-27 01:24:00 | TERRA_M-M | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 112.4 |
| a2225e05-089a-3325-8cfb-32e636366016 | -7.30148 | -61.07541 | 2024-09-27 01:24:00 | TERRA_M-M | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 40.6 |
| cc0ba83e-572b-320f-bdf0-49710e4c4ba7 | -7.30191 | -61.09969 | 2024-09-27 01:24:00 | TERRA_M-M | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 116.8 |
| f7c25ac3-f637-3780-90c2-cba2594b04af | -7.30377 | -61.09399 | 2024-09-27 01:24:00 | TERRA_M-M | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 194.3 |
| cb49b60b-9663-39b6-a87f-80b67be70df5 | -7.53296 | -61.36954 | 2024-09-27 01:24:00 | TERRA_M-M | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 23.8 |
| 285366a6-bb52-3c62-b3ad-f140d33c62e2 | -7.53495 | -61.38402 | 2024-09-27 01:24:00 | TERRA_M-M | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 57.4 |
| 15a44d11-96c3-3f8b-a29d-4c8c259fb885 | -7.53554 | -61.38926 | 2024-09-27 01:24:00 | TERRA_M-M | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 43.5 |
| 1ab8dd20-3877-3ee0-a301-533084b6dcb3 | -7.77004 | -61.18287 | 2024-09-27 01:24:00 | TERRA_M-M | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 49.2 |
| 19d6e4fc-d381-34b4-ab38-931126c369de | -7.77254 | -61.20211 | 2024-09-27 01:24:00 | TERRA_M-M | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 66.1 |
| 230c6f76-a4a6-3e29-9821-2216edfbb0d0 | -10.52771 | -51.12717 | 2024-09-27 01:24:00 | TERRA_M-M | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 150ed060-61f1-31aa-bd9d-d1b12f00c0dd | -10.5113 | -51.15382 | 2024-09-27 01:24:00 | TERRA_M-M | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 9.4 |
| b3254344-98e7-36f0-862b-836ee04ad5ac | -10.50127 | -51.15484 | 2024-09-27 01:24:00 | TERRA_M-M | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 9.1 |
| b7d306e5-994d-38a9-b94a-ad4c0a68a642 | -10.49355 | -51.23822 | 2024-09-27 01:24:00 | TERRA_M-M | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 6.7 |
| d225e76d-2ca5-3d82-bc12-2dc527312007 | -10.49304 | -51.16779 | 2024-09-27 01:24:00 | TERRA_M-M | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 10.1 |
| 0afecf17-d4f6-3dd5-9046-bd0597a7bb11 | -10.49188 | -51.22718 | 2024-09-27 01:24:00 | TERRA_M-M | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 17.6 |
| 823bda10-3f60-37a4-81c4-93f3fbb15acb | -10.49131 | -51.15633 | 2024-09-27 01:24:00 | TERRA_M-M | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 6.6 |
| ef7c508a-50b8-32cb-967b-c9f5839caffa | -10.48845 | -51.2046 | 2024-09-27 01:24:00 | TERRA_M-M | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 7.2 |
| f6ada771-4afa-3ece-8168-ab3243a69e8f | -10.47279 | -50.75887 | 2024-09-27 01:24:00 | TERRA_M-M | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 49.3 |
| 79363270-9403-37f5-8990-dbcf4e185eb8 | -10.47167 | -50.82106 | 2024-09-27 01:24:00 | TERRA_M-M | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 5222a219-b475-3c6a-8aed-4bc2236fc5ef | -10.47092 | -50.74635 | 2024-09-27 01:24:00 | TERRA_M-M | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 18.9 |
| 90289157-126b-393c-88bd-177e429277cf | -10.46439 | -50.77261 | 2024-09-27 01:24:00 | TERRA_M-M | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 11.4 |
| 5c091625-1082-3baa-9cff-aefb449860fa | -11.1306 | -50.84455 | 2024-09-27 01:24:00 | TERRA_M-M | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 7.6 |
| b968d40c-3cef-3888-81aa-805921090063 | -11.12883 | -50.83273 | 2024-09-27 01:24:00 | TERRA_M-M | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 117.3 |
| 30980eef-a01e-3874-87f1-96aec5ead6e4 | -11.05277 | -51.42702 | 2024-09-27 01:24:00 | TERRA_M-M | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Cerrado | 20.9 |
| 6789b78a-98fd-3205-8b30-22d1522c8342 | -11.04306 | -51.42854 | 2024-09-27 01:24:00 | TERRA_M-M | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Cerrado | 58.7 |
| 8f4b554e-471c-3b5e-b360-00cd26aa60ef | -11.04145 | -51.41759 | 2024-09-27 01:24:00 | TERRA_M-M | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Cerrado | 13.5 |
| 00a9c82b-7367-3f3a-8e30-1d97e8d9982e | -13.22303 | -51.2769 | 2024-09-27 01:24:00 | TERRA_M-M | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 29.1 |
| 79d412b3-0229-388c-8473-8a93333f3dc5 | -13.22146 | -51.26632 | 2024-09-27 01:24:00 | TERRA_M-M | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 204.9 |
| a1404c26-fb2b-3ef6-af31-84aaa7e59c2e | -13.21193 | -51.26785 | 2024-09-27 01:24:00 | TERRA_M-M | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 6.9 |
| c9c18acd-f9a0-352e-a7ff-f86ed4bd4f7c | -13.16902 | -51.24215 | 2024-09-27 01:24:00 | TERRA_M-M | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 061d3ba8-1bf1-36f9-8adf-520089d0691c | -12.87086 | -51.16543 | 2024-09-27 01:24:00 | TERRA_M-M | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 7.8 |
| d0e6ad7d-babd-3855-9817-e40e05b3d490 | -3.22164 | -51.83935 | 2024-09-27 01:24:00 | TERRA_M-M | VITÓRIA DO XINGU | PARÁ | Brasil | 1508357 | 15 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 23a4ba87-08cc-3389-8fdd-06a5ef09742d | -3.20272 | -51.15936 | 2024-09-27 01:24:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 16.3 |
| 1e8768f4-ec04-315b-b930-d22c69c72da2 | -3.20056 | -51.14476 | 2024-09-27 01:24:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 11.1 |
| a65e772f-6931-33b2-a276-44224047e495 | -3.19197 | -51.16669 | 2024-09-27 01:24:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 7.5 |
| f974889b-67ce-3892-be9f-1a42bf2fcda3 | -3.19153 | -51.16113 | 2024-09-27 01:24:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 15.8 |
| b0d2e30b-515f-34e7-a4f5-e97ca80b98de | -3.1899 | -51.15203 | 2024-09-27 01:24:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 20.2 |
| 8635b661-b8ea-3c3c-baea-d55861aa6178 | -3.18935 | -51.14645 | 2024-09-27 01:24:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 8.7 |
| 38b1c192-c798-315a-ac3e-c500ce552e25 | -3.09494 | -51.29158 | 2024-09-27 01:24:00 | TERRA_M-M | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 8.6 |
| 76eefb97-563d-35b8-9ceb-eef6c8689232 | -3.01605 | -51.0631 | 2024-09-27 01:24:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 124.6 |
| c30653bd-1fd8-3964-959b-1f6cbff5be3c | -3.01385 | -51.04809 | 2024-09-27 01:24:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 13.4 |
| 52a53031-ce36-342a-a33d-63f9273e81bf | -2.87498 | -51.68394 | 2024-09-27 01:24:00 | TERRA_M-M | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 22.1 |
| 7aa6c4ae-c340-309c-9657-65fe5abfe5af | -2.87306 | -51.67038 | 2024-09-27 01:24:00 | TERRA_M-M | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 96.1 |
| 670e0ee0-4a06-366c-8428-e6b111374f06 | -2.86223 | -51.67194 | 2024-09-27 01:24:00 | TERRA_M-M | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 62.2 |
| 6ee2c00d-052b-3a28-a26f-355f7c4a36cb | -4.61081 | -50.96255 | 2024-09-27 01:24:00 | TERRA_M-M | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 8.7 |
| b3abc82e-830c-3acb-b942-7edb64de3a13 | -3.96044 | -52.20001 | 2024-09-27 01:24:00 | TERRA_M-M | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 7.0 |
| fc5e7f64-6a1a-343a-a2c1-0cee68378dab | -3.87058 | -51.16527 | 2024-09-27 01:24:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 9.1 |
| 6395c80d-d1ec-3553-a914-c28d6d0f5bdd | -7.80024 | -52.41015 | 2024-09-27 01:24:00 | TERRA_M-M | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 194b61f8-eca3-3426-b11c-f90e7071ec0d | -8.98832 | -52.13975 | 2024-09-27 01:24:00 | TERRA_M-M | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 15.5 |
| 242d2ed0-b2b5-3dc6-8fcc-dd04ea5257b2 | -8.97874 | -52.14107 | 2024-09-27 01:24:00 | TERRA_M-M | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 9.5 |
| cfd91c5f-b758-3e6a-bef5-3fc4dde5c15a | -8.94254 | -52.83058 | 2024-09-27 01:24:00 | TERRA_M-M | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 0877c98a-6b7c-321f-af96-775c7aef7c3f | -8.94115 | -52.8209 | 2024-09-27 01:24:00 | TERRA_M-M | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 88b6f207-44a5-3452-bbe7-43c2d4641aaa | -8.91562 | -52.77471 | 2024-09-27 01:24:00 | TERRA_M-M | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 12.2 |
| a91e296d-7b5a-3789-b709-16eab056c3a2 | -8.91419 | -52.76477 | 2024-09-27 01:24:00 | TERRA_M-M | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 49715d9a-a68e-3800-b0e1-d8f3496c15b6 | -8.90635 | -52.77599 | 2024-09-27 01:24:00 | TERRA_M-M | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 65078a95-52b3-3685-99a8-05ee2523fd0c | -8.90492 | -52.76614 | 2024-09-27 01:24:00 | TERRA_M-M | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| af96c137-b27e-3094-b259-840268fb5d5a | -8.89698 | -53.03521 | 2024-09-27 01:24:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 04477b2e-ce70-3707-87cc-be2fdacaab5a | -8.8956 | -53.02571 | 2024-09-27 01:24:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| a7997c5f-0e5c-39b3-8a86-dc022414e0e3 | -8.88726 | -53.02366 | 2024-09-27 01:24:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 15.9 |
| 6429c0f1-8fb2-3250-a335-f875a34c2397 | -8.80402 | -52.00605 | 2024-09-27 01:24:00 | TERRA_M-M | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 552cb4b5-2908-3f3b-953e-769f12d7445d | -8.66408 | -53.0789 | 2024-09-27 01:24:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 173abb24-1147-39fb-8ddc-6cd879dd3449 | -8.6623 | -53.19585 | 2024-09-27 01:24:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 41c85d26-865a-3a9b-bd4b-9e615aec0b4a | -8.6596 | -53.17712 | 2024-09-27 01:24:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 14.5 |
| 0b5e1d17-907b-343c-a5d4-3d53a166e128 | -8.65319 | -53.19724 | 2024-09-27 01:24:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 59ac9fb6-84a2-3b57-bfaa-249793366d1a | -8.65184 | -53.18792 | 2024-09-27 01:24:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 15.5 |
| 27842646-4bda-3987-9a15-2deb020789c1 | -8.65128 | -53.11971 | 2024-09-27 01:24:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 10.7 |
| b3cab505-349f-3106-b9ce-92c5f05f505e | -8.64991 | -53.11022 | 2024-09-27 01:24:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 0978681d-4e87-384c-abb8-634aefadf561 | -8.62726 | -53.13883 | 2024-09-27 01:24:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| b8672b2e-47a4-312a-88b6-0ae55dd6e365 | -8.5593 | -51.79962 | 2024-09-27 01:24:00 | TERRA_M-M | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 9aa5bd74-1aba-3fee-a266-9543c4b2587a | -8.47305 | -53.22661 | 2024-09-27 01:24:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 37fea0bf-c2a3-3227-88d9-8cae2284aedc | -8.37318 | -52.47781 | 2024-09-27 01:24:00 | TERRA_M-M | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| e27ba469-f336-3782-b8e8-795bfcb66142 | -9.12106 | -53.30825 | 2024-09-27 01:24:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 14140453-8beb-3cce-9ea7-1c9970a5a289 | -9.11041 | -53.29704 | 2024-09-27 01:24:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 2ee56a69-1300-3b31-926d-096139933c25 | -8.88862 | -53.0332 | 2024-09-27 01:24:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 9.8 |
| 4692dc07-0efa-3fb1-9c46-9a434b954bbd | -8.67143 | -53.19457 | 2024-09-27 01:24:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 12.7 |
| 5754ea10-aab8-3046-aa48-6a51ff5f8f06 | -8.67008 | -53.18519 | 2024-09-27 01:24:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 14.5 |
| 6745b52c-f5fe-3e53-befc-47aa4c950198 | -8.66271 | -53.06937 | 2024-09-27 01:24:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 6d13c951-ff34-3545-b3ea-b9cce8525251 | -8.66097 | -53.18659 | 2024-09-27 01:24:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 9.4 |
| 63fc6fb7-02c5-3c49-89ff-3c48a4d4e40b | -8.63576 | -53.14145 | 2024-09-27 01:24:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 285999d2-62d9-3985-923e-20cd5c4708ee | -8.46393 | -53.22797 | 2024-09-27 01:24:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 13.1 |
| e0bb0698-3b64-3831-8deb-31f03cfc6310 | -23.576799 | -47.352299 | 2024-09-27 01:24:35 | METOP-C | VOTORANTIM | SÃO PAULO | Brasil | 3557006 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 4654a5b0-bb7f-3974-afc4-1a4455f9c764 | -23.582399 | -47.334202 | 2024-09-27 01:24:35 | METOP-C | VOTORANTIM | SÃO PAULO | Brasil | 3557006 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| af2393ab-c499-3d32-9665-9a7e2006df7b | -23.568701 | -47.322201 | 2024-09-27 01:24:35 | METOP-C | VOTORANTIM | SÃO PAULO | Brasil | 3557006 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 15feb2da-659b-3737-a3bd-38c299ac5825 | -23.5728 | -47.337299 | 2024-09-27 01:24:35 | METOP-C | VOTORANTIM | SÃO PAULO | Brasil | 3557006 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 7b2c3f23-f420-3f3f-bdec-3bc9fa3869f4 | -23.4377 | -46.994598 | 2024-09-27 01:24:36 | METOP-C | SANTANA DE PARNAÍBA | SÃO PAULO | Brasil | 3547304 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 80975fc1-12c1-3ac1-9918-f34b7e530084 | -22.737499 | -44.770699 | 2024-09-27 01:24:37 | METOP-C | SILVEIRAS | SÃO PAULO | Brasil | 3552007 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 68e94224-bb57-3163-9185-2256a0e44b10 | -22.743999 | -44.792999 | 2024-09-27 01:24:37 | METOP-C | SILVEIRAS | SÃO PAULO | Brasil | 3552007 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 802fd881-2e33-3c2c-998c-c376dc331ab5 | -22.728001 | -44.773899 | 2024-09-27 01:24:37 | METOP-C | SILVEIRAS | SÃO PAULO | Brasil | 3552007 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| f3a8e3ab-3e75-338d-9c8c-0b72ff0ddcd0 | -22.734501 | -44.7962 | 2024-09-27 01:24:37 | METOP-C | SILVEIRAS | SÃO PAULO | Brasil | 3552007 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 2ce1dcba-2fcb-31c0-9639-3925f1c4c6c3 | -22.954399 | -45.931 | 2024-09-27 01:24:39 | METOP-C | SÃO JOSÉ DOS CAMPOS | SÃO PAULO | Brasil | 3549904 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 0c08ebcb-e3c8-3de3-95da-5cd622e9a76a | -22.9597 | -45.949799 | 2024-09-27 01:24:39 | METOP-C | SÃO JOSÉ DOS CAMPOS | SÃO PAULO | Brasil | 3549904 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 2d1cc413-851a-3840-9a9d-9b384d68f711 | -21.4144 | -42.957901 | 2024-09-27 01:24:50 | METOP-C | DESCOBERTO | MINAS GERAIS | Brasil | 3121308 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| a7c132c9-80f1-3806-a525-232f6b8c1d06 | -21.4049 | -42.961201 | 2024-09-27 01:24:50 | METOP-C | DESCOBERTO | MINAS GERAIS | Brasil | 3121308 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| c6e04e60-66ba-3ac4-a10e-d0ff7c9bf4b5 | -21.4142 | -42.991798 | 2024-09-27 01:24:50 | METOP-C | DESCOBERTO | MINAS GERAIS | Brasil | 3121308 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 450a4d8a-faa7-30a7-956a-cd5ffbc5042d | -21.3955 | -42.964401 | 2024-09-27 01:24:50 | METOP-C | GUARANI | MINAS GERAIS | Brasil | 3128402 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| c5375df6-3ece-379e-8be2-b39203d78ddd | -21.954201 | -45.793499 | 2024-09-27 01:24:54 | METOP-C | TURVOLÂNDIA | MINAS GERAIS | Brasil | 3169802 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 71317154-45ce-3476-b45e-a994a53c547a | -21.959801 | -45.8134 | 2024-09-27 01:24:54 | METOP-C | TURVOLÂNDIA | MINAS GERAIS | Brasil | 3169802 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |


[Clique aqui para ver as próximas entradas](README30.md)
