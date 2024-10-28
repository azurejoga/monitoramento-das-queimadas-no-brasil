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

## Dados Diários - Página 81

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 4383e207-db99-354f-8a82-e7b2cdf1eadd | -3.95851 | -52.20503 | 2024-10-28 05:23:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 85b9cca8-6f52-3dcd-8e6b-1dcda11873a7 | -3.92583 | -52.12263 | 2024-10-28 05:23:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| dbe77b29-cc4f-3377-93b2-25d34a19d20b | -3.86078 | -51.70021 | 2024-10-28 05:23:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 8df919e8-6269-351a-aaff-ac7b64186ac7 | -3.86014 | -51.70089 | 2024-10-28 05:23:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 14568bda-223d-35c8-af96-47a3224fabe0 | -3.85989 | -51.70607 | 2024-10-28 05:23:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c29136f9-f49f-37a4-ac1f-1ec9a9c5ec76 | -3.8593 | -51.70675 | 2024-10-28 05:23:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 283d7ce8-9aa0-38ce-9792-11304500eb1c | -3.85574 | -51.69956 | 2024-10-28 05:23:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 3e6b3548-39e5-3852-b071-3e47970823e4 | -3.80697 | -50.961 | 2024-10-28 05:23:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ee5d8e69-3afc-302b-86d8-e74d3b4d00e4 | -3.80172 | -50.96001 | 2024-10-28 05:23:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ee9c5114-c824-3a52-9ee8-f1b3f7011ad8 | -3.80122 | -50.96338 | 2024-10-28 05:23:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 98f36292-4a7d-372c-91f0-f07f475b5852 | -3.80072 | -50.9668 | 2024-10-28 05:23:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b7765868-7fb8-3971-8fcb-b2e6b7e37abb | -3.79645 | -50.95913 | 2024-10-28 05:23:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c9bba39e-da67-3838-be5f-4fbccf7497ec | -3.79596 | -50.96244 | 2024-10-28 05:23:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8abebe48-8ae6-3bb0-aa66-7b04aac6fbf8 | -3.79547 | -50.9658 | 2024-10-28 05:23:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 1445f138-dc31-3a61-baf6-ddd038122124 | -3.77275 | -51.94672 | 2024-10-28 05:23:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b8b9947b-9afe-3b8a-bd62-e951d94dba45 | -3.76782 | -51.94597 | 2024-10-28 05:23:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7c18b29a-5d08-37b5-a213-ba5617332a39 | -3.767 | -51.95149 | 2024-10-28 05:23:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| efc492d0-fe86-3c1c-b709-83b2ae20d60f | -3.7651 | -51.06313 | 2024-10-28 05:23:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| c2f58b97-bc2e-335a-acf8-ce725371171c | -3.76464 | -51.06625 | 2024-10-28 05:23:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 357b1590-5c0b-3a3d-9e55-3a855fa79ab5 | -3.69318 | -51.14952 | 2024-10-28 05:23:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4b877906-4389-319c-ac21-d6df97f26c9a | -6.131 | -52.16367 | 2024-10-28 05:23:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3b378cde-e713-3f93-8ac7-fe1846b6e8ce | -6.12597 | -52.16293 | 2024-10-28 05:23:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f4c5af5b-62bb-3bf6-ac9c-a03ace97498c | -6.90252 | -52.71336 | 2024-10-28 05:23:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6e6bbf5d-fb7f-36f1-a7a9-448befb3db87 | -6.90172 | -52.71898 | 2024-10-28 05:23:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 9a4c183e-1066-3c8a-9cf4-8bf2f702c664 | -3.52586 | -53.24846 | 2024-10-28 05:23:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 2e44db44-1bac-3ae9-9801-6d2a017354b0 | -3.40017 | -53.6862 | 2024-10-28 05:23:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.3 |
| 45ee83b0-28f9-3ff8-8e04-919007e37d84 | -3.39954 | -53.69032 | 2024-10-28 05:23:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| b1c3ca86-b3c9-3ab2-8835-4bdf45097a72 | -2.98502 | -53.26556 | 2024-10-28 05:23:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 28232b74-b88a-34fe-9624-dc2ba9dc2ccc | -2.98376 | -53.26448 | 2024-10-28 05:23:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 7ca4598e-98f6-353a-8eb8-413438730c8e | -2.98056 | -53.26499 | 2024-10-28 05:23:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a55b8509-93e6-3314-802b-969d38520b01 | -2.9793 | -53.2639 | 2024-10-28 05:23:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| a815c1d2-57f6-3299-be8f-773288e7f435 | -2.97867 | -53.26818 | 2024-10-28 05:23:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| c2f4b8d9-01c3-34f6-ad63-d84e0064aa9b | -2.97421 | -53.26759 | 2024-10-28 05:23:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 0a542780-7482-3311-af41-ac57f7435a48 | -2.88184 | -53.31697 | 2024-10-28 05:23:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 4ccd9d66-9099-326c-baa1-ae7d1a0a3563 | -2.87805 | -53.31201 | 2024-10-28 05:23:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 369e0925-7758-35d7-a3de-c2d679511fea | -2.86703 | -53.33421 | 2024-10-28 05:23:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 2db66996-ebce-375f-978a-d757bb3f07e1 | -2.86634 | -53.33857 | 2024-10-28 05:23:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 906ce126-5215-3a5d-912e-75d58b672bd7 | -2.86605 | -53.33194 | 2024-10-28 05:23:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| d46a7ae1-215d-38b1-992e-ae798780026c | -2.8654 | -53.33632 | 2024-10-28 05:23:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 936f0fb1-53a3-347a-b338-f6811e7ca885 | -2.86325 | -53.32939 | 2024-10-28 05:23:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| c5aaa78d-f276-32ae-a994-175234077142 | -2.86257 | -53.33376 | 2024-10-28 05:23:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| af533167-25b5-39d6-9fec-74e29bb31f08 | -2.86189 | -53.3381 | 2024-10-28 05:23:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 8f8ed633-7d7a-3883-90aa-346696fa9f65 | -2.8616 | -53.33144 | 2024-10-28 05:23:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| cbb5b390-bed8-3138-90f3-e12d8eadb686 | -2.86095 | -53.3358 | 2024-10-28 05:23:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 7ecd2bee-3f7a-3c0d-9b4c-28408d3519d7 | -2.85814 | -53.33314 | 2024-10-28 05:23:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 808ee089-a770-3e17-98fc-6a5acf2328ee | -2.8568 | -53.34176 | 2024-10-28 05:23:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| e6cac0fe-5d8c-3cde-b577-b129a267d1e3 | -10.22075 | -54.90676 | 2024-10-28 05:25:00 | NPP-375D | MATUPÁ | MATO GROSSO | Brasil | 5105606 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 2edb8047-5231-30d1-bd42-17c75c3648d1 | -10.13164 | -56.27514 | 2024-10-28 05:25:00 | NPP-375D | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6c1ff810-1e9e-32cd-a154-6a215dfc40f3 | -9.65771 | -56.96693 | 2024-10-28 05:25:00 | NPP-375D | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 2d98d441-7170-3a6b-b49a-2977a75fc2d1 | -10.53074 | -59.42708 | 2024-10-28 05:25:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4da9d919-ce11-3025-b652-4350b1d2fd42 | -10.53017 | -59.43085 | 2024-10-28 05:25:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8eeceac9-a964-3351-8f32-9635a3db927d | -11.15236 | -58.58669 | 2024-10-28 05:25:00 | NPP-375D | CASTANHEIRA | MATO GROSSO | Brasil | 5102850 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 64891a15-bd7d-3584-b670-5bebb1d19d3d | -9.91942 | -59.913 | 2024-10-28 05:25:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a5fe321e-e361-3ded-a47b-b3164c24c4fc | -9.73878 | -60.40572 | 2024-10-28 05:25:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 742092b9-056b-35b9-8397-1cf7a65ea74e | -9.39718 | -62.4584 | 2024-10-28 05:25:00 | NPP-375D | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f2e6a8ca-f0dd-3ad7-a517-e473aa41cd2c | -8.91812 | -64.04283 | 2024-10-28 05:25:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 27a7f03a-7d8a-321c-862c-ca4c430cfbff | -1.1836 | -53.4956 | 2024-10-28 05:25:12 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 51.7 |
| e2d8fe5e-ae76-3575-98f8-f568d10f4345 | -1.9763 | -52.0804 | 2024-10-28 05:25:17 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 44.7 |
| d3b67118-37ec-31e7-899d-cbf942a7e73f | -1.9947 | -52.0801 | 2024-10-28 05:25:17 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 34.3 |
| ac8f8b78-8167-3bdc-91b5-efb41c48bf0d | -2.2662 | -53.7825 | 2024-10-28 05:25:18 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 38.5 |
| 8813c2ac-d677-3fd3-a46f-65a3772ef341 | -2.2846 | -53.7822 | 2024-10-28 05:25:19 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 31.2 |
| c8afed9b-1e43-3bdb-a72f-b54f9907c1bd | -2.4104 | -48.5479 | 2024-10-28 05:25:19 | GOES-16 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 52.8 |
| 0d70c850-bcc6-356c-b015-24645c4a6cec | -2.833 | -49.2413 | 2024-10-28 05:25:22 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 57.5 |
| 8c1d2a1b-8a2a-3aae-b5ca-37ec787c25e6 | -2.8699 | -49.2615 | 2024-10-28 05:25:22 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 67.5 |
| 34f8d3f6-6324-3177-86ab-1138c23fb3b6 | -2.87 | -49.2402 | 2024-10-28 05:25:22 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 52.4 |
| 9028c4d6-e45a-318c-8976-c8bf92110165 | -2.8884 | -49.2609 | 2024-10-28 05:25:22 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 73.5 |
| d83f6912-d431-3016-bab3-1c1d59d1767e | -2.8885 | -49.2397 | 2024-10-28 05:25:22 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 48.8 |
| d99026bd-ba25-34ad-b097-4ecf5754c787 | -3.0317 | -50.4176 | 2024-10-28 05:25:23 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 73.6 |
| b7d230f6-da5d-382a-a16f-953a8cb7d5b9 | -3.0501 | -50.4171 | 2024-10-28 05:25:23 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 54.6 |
| 9ee72b98-3690-3a9e-b55e-b48fd34c1ecc | -3.497 | -45.7971 | 2024-10-28 05:25:25 | GOES-16 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 90.2 |
| 1e688167-be09-38e9-ba17-b0014b5d5780 | -3.5155 | -45.7964 | 2024-10-28 05:25:25 | GOES-16 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 96.7 |
| f73c838c-a1a4-3df6-a1f5-5f03743f956a | -4.6819 | -46.6511 | 2024-10-28 05:25:32 | GOES-16 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 59.3 |
| 43d30380-eaf3-3c4a-af08-dbf91355ea55 | -1.9763 | -52.0804 | 2024-10-28 05:35:17 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 74.8 |
| 1dbc5b4d-ce0d-37bd-9ea4-67212d57eea2 | -2.2662 | -53.7825 | 2024-10-28 05:35:18 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 56.9 |
| c979b19a-8403-3fee-9ca5-418162f39c77 | -2.8699 | -49.2615 | 2024-10-28 05:35:22 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 58.9 |
| 8f531160-b291-3813-8750-f246ab69b111 | -2.87 | -49.2402 | 2024-10-28 05:35:22 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 49.3 |
| ac5cb627-30a2-354e-a0bc-bf58a67f1469 | -2.8884 | -49.2609 | 2024-10-28 05:35:22 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 69.3 |
| ec062137-4d86-3249-b979-8fb7d053c988 | -3.0317 | -50.4176 | 2024-10-28 05:35:23 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 71.6 |
| 6ec4f917-0da6-3c3a-b50c-0ebde2655124 | -3.497 | -45.7971 | 2024-10-28 05:35:25 | GOES-16 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 51.0 |
| 9f2932e4-acc6-30aa-82bd-62e1aa3a1e36 | -3.5155 | -45.7964 | 2024-10-28 05:35:25 | GOES-16 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 65.3 |
| a670f1de-819b-3e4d-a5d0-fba748a7894c | -4.6819 | -46.6511 | 2024-10-28 05:35:32 | GOES-16 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 58.0 |
| 40d6d28d-b980-3fae-b360-697974d8e0b0 | 3.58762 | -51.28245 | 2024-10-28 05:44:00 | AQUA_M-M | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 6.6 |
| ccef7a06-1a88-3b3c-b4a4-ef79c5ad3534 | 3.58628 | -51.2734 | 2024-10-28 05:44:00 | AQUA_M-M | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 17.3 |
| 797d0f93-9471-3866-9c2f-16173789865c | 3.47292 | -51.25035 | 2024-10-28 05:44:00 | AQUA_M-M | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 9.2 |
| c2587aad-9ed4-3290-98c3-1837891724f0 | 3.47159 | -51.24133 | 2024-10-28 05:44:00 | AQUA_M-M | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 14.3 |
| e33e04e4-c9fc-3c3f-b8ca-5f306134697b | 3.46265 | -51.24263 | 2024-10-28 05:44:00 | AQUA_M-M | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 10.1 |
| 6e41c0c6-035f-3142-93aa-3b27e0a717e9 | 2.35556 | -50.76125 | 2024-10-28 05:44:00 | AQUA_M-M | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 6.3 |
| d2f25973-1b31-3c80-b16b-9386d7b3a217 | 2.35424 | -50.75247 | 2024-10-28 05:44:00 | AQUA_M-M | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 14.3 |
| 80b58989-6825-3b04-a6fe-02d72fd021ce | -4.76412 | -46.38646 | 2024-10-28 05:44:00 | AQUA_M-M | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 25.2 |
| 8056f32b-2f80-3261-8e6c-797fc5c422fc | -1.16818 | -53.49409 | 2024-10-28 05:44:00 | AQUA_M-M | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 7.8 |
| 23656e1d-9022-3a0e-b2cd-5a5602b125af | -4.68262 | -46.65971 | 2024-10-28 05:44:00 | AQUA_M-M | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 33.3 |
| 56f88314-6274-3138-9c58-814d33daa11b | -4.67907 | -46.64945 | 2024-10-28 05:44:00 | AQUA_M-M | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 45.7 |
| 4c3c9b4f-c884-33a8-beb3-110388395af3 | -4.67684 | -46.66581 | 2024-10-28 05:44:00 | AQUA_M-M | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 25.2 |
| 8c15a276-f181-3007-a886-9032eadc6dde | -4.67083 | -46.65802 | 2024-10-28 05:44:00 | AQUA_M-M | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 24.1 |
| de1f18ec-31da-3952-b827-5e7b92a8f3d7 | -4.48727 | -48.11529 | 2024-10-28 05:44:00 | AQUA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 9.1 |
| e997b443-d0c8-36aa-aaf4-48ab6776303b | -4.29531 | -48.60773 | 2024-10-28 05:44:00 | AQUA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 31.6 |
| 6227ab34-2a0c-3acf-b750-6c328db5f119 | -4.09575 | -48.23147 | 2024-10-28 05:44:00 | AQUA_M-M | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 8.1 |
| 2332ef9f-91b3-3d5c-bbbb-0fcada616421 | -4.06857 | -50.01809 | 2024-10-28 05:44:00 | AQUA_M-M | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 10.8 |
| c59e1371-8675-3375-9c73-54ba04705d18 | -4.06714 | -50.02779 | 2024-10-28 05:44:00 | AQUA_M-M | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 0fad35a5-7639-3526-89fb-956e8ab3cb76 | -4.06614 | -48.28967 | 2024-10-28 05:44:00 | AQUA_M-M | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 10.4 |


[Clique aqui para ver as próximas entradas](README82.md)
