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

## Dados Diários - Página 33

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 8e575750-3c68-3895-9888-59e247be9a38 | -2.67805 | -46.60966 | 2024-12-02 04:23:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| d80960d3-c471-399d-932d-47dbfc26e754 | -1.69349 | -52.63641 | 2024-12-02 04:23:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6833a54f-847a-3700-84bc-ab361fb816f8 | -3.13153 | -45.98722 | 2024-12-02 04:23:00 | NPP-375D | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 3.0 |
| f1155e37-9714-3eb5-9f0e-4404ef1883a3 | -2.5688 | -46.57083 | 2024-12-02 04:23:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 128f41fb-fdfd-3ee2-a2b0-6ff86c330f3c | -2.80474 | -45.93647 | 2024-12-02 04:23:00 | NPP-375D | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 3d06dc53-bdb5-3c50-b15f-cf4873d486e0 | -1.23313 | -53.3641 | 2024-12-02 04:23:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 86c6c1d7-3907-3683-a090-6541fcb4bd83 | -3.29777 | -45.65943 | 2024-12-02 04:23:00 | NPP-375D | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 6bb3bc8c-1e95-3b70-993c-50dbba9737f4 | -2.20096 | -48.32899 | 2024-12-02 04:23:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| ed21d489-802d-3cdf-aa0e-3b89889cee61 | -1.07957 | -46.80229 | 2024-12-02 04:23:00 | NPP-375D | BRAGANÇA | PARÁ | Brasil | 1501709 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 3754d6ec-c8be-3a0c-b272-3165285bf6eb | 1.11177 | -56.01489 | 2024-12-02 04:23:00 | NPP-375D | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 3b7e3dbd-be61-3189-858d-d714c517e620 | -3.00026 | -46.9159 | 2024-12-02 04:23:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| f016e22b-e033-3780-9878-8f2fe46a544d | -1.37779 | -52.38111 | 2024-12-02 04:23:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 67494487-2791-3033-a143-541f691d5b8c | -2.67693 | -46.61678 | 2024-12-02 04:23:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 17c497c9-2330-3a9b-8c2a-e96b847f2a0e | -2.6517 | -46.58006 | 2024-12-02 04:23:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 248495a3-c41c-3ccc-a0b1-329fac44f499 | -3.61692 | -42.74091 | 2024-12-02 04:23:00 | NPP-375D | BREJO | MARANHÃO | Brasil | 2102101 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| dbcd721d-4f56-3cff-8732-53ff842d5da6 | -2.55927 | -46.56569 | 2024-12-02 04:23:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 74438613-7ade-3b35-8513-c611b585d425 | -2.75515 | -46.09953 | 2024-12-02 04:23:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| db95ad15-fafc-35a6-845b-fbc0ed9ba452 | -2.56207 | -46.56977 | 2024-12-02 04:23:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 3510a5ec-08ca-3e33-acc1-733005dc76b0 | -2.46787 | -46.56933 | 2024-12-02 04:23:00 | NPP-375D | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| e15d1295-3e46-38fc-8faa-8fd12dc92490 | -2.48751 | -46.57609 | 2024-12-02 04:23:00 | NPP-375D | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 00e50b25-08e3-3e63-b8fe-3e03d8b250fe | -1.91084 | -52.86742 | 2024-12-02 04:23:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7e99f493-6579-36d1-85ab-ceecb683c406 | -1.73252 | -52.78265 | 2024-12-02 04:23:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7121213d-b2fa-375e-84dd-da96358951e6 | -2.7281 | -46.22757 | 2024-12-02 04:23:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 5e9e06cb-2bfa-3a53-82e3-212d9e344083 | -3.16091 | -46.63008 | 2024-12-02 04:23:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 88b7586c-eb4c-3e0e-bc25-c8512bc42778 | -3.12433 | -45.98965 | 2024-12-02 04:23:00 | NPP-375D | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 414c6625-a1e5-39cf-8630-0875ee170cc5 | -0.60553 | -51.68882 | 2024-12-02 04:23:00 | NPP-375D | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 69fff424-38b7-383e-9618-85516757c43b | -1.25932 | -51.58712 | 2024-12-02 04:23:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| d7c85cb5-bc7b-31fb-b210-7ab3cad2acb3 | -1.28174 | -54.55695 | 2024-12-02 04:23:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| be61d3e5-8e2b-3fc8-b70e-6b470928bc52 | -1.94658 | -53.34806 | 2024-12-02 04:23:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 522c97ec-c4d3-30f8-b4a1-6da9a6c4be2e | -3.48779 | -46.08577 | 2024-12-02 04:23:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 4.1 |
| b3079787-70ce-3c8b-b7f8-b8a4c91edf29 | -2.56433 | -46.40342 | 2024-12-02 04:23:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 37066594-3023-3664-961d-6a7ae2d182bd | -2.55931 | -46.34852 | 2024-12-02 04:23:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 6cf7b8ce-ea60-3b88-a865-457727af3b9f | -2.01636 | -54.31091 | 2024-12-02 04:23:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 3517b31e-d180-37d4-ba5b-81e6409012b1 | -2.197 | -53.77472 | 2024-12-02 04:23:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| b6c03954-5676-35b7-9076-f756aa7e5236 | -1.29433 | -51.37409 | 2024-12-02 04:23:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c12d76d2-8954-30ff-b36b-316c18b0ddea | -3.16323 | -46.55077 | 2024-12-02 04:23:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 9975fd5b-0558-3e73-b02e-c53c00de78c1 | -3.12875 | -45.98324 | 2024-12-02 04:23:00 | NPP-375D | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 119ae331-28d8-397c-96dd-d242dc81e2df | -2.47011 | -46.55513 | 2024-12-02 04:23:00 | NPP-375D | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 5ef667be-fd3c-3b6d-95b7-7f6a13711040 | -1.23516 | -51.61191 | 2024-12-02 04:23:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 93d8daee-cf27-387d-8d27-6c8d53159cf9 | -2.58899 | -46.57402 | 2024-12-02 04:23:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d891f5ea-3d08-3401-9641-aab17a26cf34 | -2.66323 | -46.12445 | 2024-12-02 04:23:00 | NPP-375D | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8848cc3b-4c08-3f3d-a42a-e07cccfd74b4 | -3.26503 | -45.37534 | 2024-12-02 04:23:00 | NPP-375D | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| e35f1f2d-7063-3079-8039-9fd0b39367e5 | -2.63227 | -46.87752 | 2024-12-02 04:23:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f97ec4ae-f641-3cfa-b3d2-57d317599d4f | -2.72028 | -46.21202 | 2024-12-02 04:23:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ee9b98d3-17d8-3b5d-88c8-61ea02268c45 | -2.92777 | -48.01674 | 2024-12-02 04:23:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| fa1b272a-9678-32b5-b2d8-5ad8e85445d6 | -1.72277 | -52.48482 | 2024-12-02 04:23:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b397653c-8a7b-3fa1-9df1-0cba4408652f | 0.88753 | -50.9579 | 2024-12-02 04:23:00 | NPP-375D | FERREIRA GOMES | AMAPÁ | Brasil | 1600238 | 16 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 0e6c0792-208b-3d52-b131-fedae868c671 | -2.26561 | -53.61421 | 2024-12-02 04:23:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| cd65b2f9-7012-3262-8c15-97b8c3e15f86 | -2.80102 | -46.00341 | 2024-12-02 04:23:00 | NPP-375D | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f85b2602-8701-3f74-a084-abace0ca2255 | -2.77993 | -48.58322 | 2024-12-02 04:23:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 5271dac7-8481-36d7-a878-aa495be5bbfb | -3.26483 | -46.45126 | 2024-12-02 04:23:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 2.6 |
| c1bafe24-fb61-326c-80b3-aa8a300e6647 | -2.54694 | -46.5565 | 2024-12-02 04:23:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 1f21a275-3c7b-3a5e-aa3f-349117943035 | -2.65155 | -46.77746 | 2024-12-02 04:23:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 822d44d7-664a-30cc-9ea6-02b1ba3c7a91 | -2.57266 | -46.19969 | 2024-12-02 04:23:00 | NPP-375D | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 548abec1-6334-3a71-b9c8-68a9b36f08e9 | -2.47292 | -46.55921 | 2024-12-02 04:23:00 | NPP-375D | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 40e22cf8-c7ae-3f4a-8882-154671098002 | -2.14336 | -46.39185 | 2024-12-02 04:23:00 | NPP-375D | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 5ce4229c-e06f-3705-84ee-9462afa189f2 | -3.19901 | -46.36908 | 2024-12-02 04:23:00 | NPP-375D | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 96a17794-06d6-3cff-84e8-27fe7ee4a2fd | -1.09618 | -53.64763 | 2024-12-02 04:23:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 3a0a6f9b-e4b1-326b-82eb-2935c2dbce16 | -0.92791 | -47.61799 | 2024-12-02 04:23:00 | NPP-375D | MARAPANIM | PARÁ | Brasil | 1504406 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| b098a2bf-46d1-34e4-8907-15fbde6f0250 | -2.80365 | -45.94341 | 2024-12-02 04:23:00 | NPP-375D | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 76711336-aea0-3cfc-96bc-9d82c8354fde | -0.92459 | -47.6178 | 2024-12-02 04:23:00 | NPP-375D | MARAPANIM | PARÁ | Brasil | 1504406 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| dbea66e7-3d58-3e18-aafb-4707c7e2b3db | -1.94936 | -51.21135 | 2024-12-02 04:23:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a8fcb30c-2156-34ee-a4a0-ceb6f65d5105 | -2.68142 | -46.61019 | 2024-12-02 04:23:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 7c984e8f-15c7-393d-a564-7f5a6e75676b | -2.72445 | -45.07127 | 2024-12-02 04:23:00 | NPP-375D | PALMEIRÂNDIA | MARANHÃO | Brasil | 2107605 | 21 | 33 | nan | nan | nan | Amazônia | 4.8 |
| ed378e69-711c-3cf4-844a-1dd2eb61d36e | -2.67749 | -46.61322 | 2024-12-02 04:23:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 9ff2f9f6-a0ca-3503-84ad-d303d1d97f67 | 1.12671 | -55.9877 | 2024-12-02 04:23:00 | NPP-375D | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 8fbf1e99-fc6a-3b1e-ae0f-1d4b8dcde430 | -1.93126 | -53.44449 | 2024-12-02 04:23:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d32f3be5-b5a4-3201-b84a-8b7314ae9aff | -2.48078 | -46.57503 | 2024-12-02 04:23:00 | NPP-375D | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 6bc7a098-45a9-385a-8a6d-a7ff02076e05 | -1.07254 | -53.45183 | 2024-12-02 04:23:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| a14bb3e1-b2c2-36fc-8581-fcc599de571f | -2.63487 | -46.57743 | 2024-12-02 04:23:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 82abc0c9-3365-3e69-94e2-994a787047b4 | -1.62852 | -45.81951 | 2024-12-02 04:23:00 | NPP-375D | CÂNDIDO MENDES | MARANHÃO | Brasil | 2102606 | 21 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 428c0975-6264-3b21-8e88-7687c4a333a4 | -3.17085 | -46.31834 | 2024-12-02 04:23:00 | NPP-375D | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ea83b356-a822-3b5f-a6d4-82ba39b8454b | -2.60551 | -46.2084 | 2024-12-02 04:23:00 | NPP-375D | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| fdd4bcfe-cf96-3035-af4d-804d965f9410 | -2.66652 | -46.10356 | 2024-12-02 04:23:00 | NPP-375D | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 9a7443b9-df3e-3bf6-804f-dc2c17ca09f3 | -2.72867 | -46.24559 | 2024-12-02 04:23:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d7c9dac1-6de0-3c85-b48f-92a7f9707d57 | -2.68198 | -46.60664 | 2024-12-02 04:23:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| f35cabee-421e-3469-8224-f112fe3e7df4 | -1.99189 | -46.44782 | 2024-12-02 04:23:00 | NPP-375D | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| bce14812-a7b9-394a-891c-c1dff09d7e1c | -2.48358 | -46.57911 | 2024-12-02 04:23:00 | NPP-375D | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| efd4341e-fd2f-3bd1-b96c-23d9e207528c | -1.07503 | -53.45311 | 2024-12-02 04:23:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 71f52f79-2768-3ac6-92e8-9b24f78051d5 | -2.58863 | -46.01297 | 2024-12-02 04:23:00 | NPP-375D | MARANHÃOZINHO | MARANHÃO | Brasil | 2106375 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 24916393-4d19-337c-bc23-661acaab95d1 | -2.46451 | -46.5688 | 2024-12-02 04:23:00 | NPP-375D | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 2a44a4c0-553d-3427-9c5a-8eef61bfeb25 | -1.1476 | -53.66214 | 2024-12-02 04:23:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ab14ae35-2548-3002-ba8f-d1dcfb3f8635 | -2.9313 | -48.0173 | 2024-12-02 04:23:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0530e5b6-fab6-3461-9b30-ad39d998d874 | -1.82866 | -45.57778 | 2024-12-02 04:23:00 | NPP-375D | TURIAÇU | MARANHÃO | Brasil | 2112407 | 21 | 33 | nan | nan | nan | Amazônia | 0.3 |
| 1841389a-6b58-329b-8753-620d4e083fd3 | -1.82225 | -53.73164 | 2024-12-02 04:23:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 4f669127-23f5-303d-8d95-46eae9915785 | -2.58675 | -46.56638 | 2024-12-02 04:23:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 7971234c-033d-34f4-9049-329acb86b13e | -2.49651 | -47.27282 | 2024-12-02 04:23:00 | NPP-375D | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f71d2954-71f1-3ec6-8236-e310419321c5 | -1.47677 | -47.34072 | 2024-12-02 04:23:00 | NPP-375D | BONITO | PARÁ | Brasil | 1501600 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c580d9ea-0bf3-3b3c-807f-96605ae926fa | -2.92213 | -48.00896 | 2024-12-02 04:23:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 753e89a7-882c-36b5-acdf-d321ccd645f5 | -2.20328 | -48.33777 | 2024-12-02 04:23:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 77a73df9-79f1-3eb2-8680-95ad0e73497f | 1.09926 | -56.01686 | 2024-12-02 04:23:00 | NPP-375D | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 39af64c4-c5d0-3d26-983c-1964475a4716 | -1.35036 | -55.20119 | 2024-12-02 04:23:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| a0c2a745-cd2f-3eef-abcf-c935379ad42f | -1.59909 | -47.3629 | 2024-12-02 04:23:00 | NPP-375D | SÃO MIGUEL DO GUAMÁ | PARÁ | Brasil | 1507607 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| a67d5f53-aabd-3206-9e0d-dc2125fff508 | -2.49816 | -49.01685 | 2024-12-02 04:23:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| aa5d6693-8907-3b84-9cae-05f4ef5d9ddf | -2.72699 | -46.23457 | 2024-12-02 04:23:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 07c64d18-c8c1-3ec1-a4d2-045b70722a61 | -2.48134 | -46.57147 | 2024-12-02 04:23:00 | NPP-375D | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| a89b14c0-7136-39d0-8574-6c1465d623f1 | -1.73338 | -52.7774 | 2024-12-02 04:23:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e04ba95b-3b9d-3a78-ba72-5df6cede68d3 | -3.1391 | -45.2316 | 2024-12-02 04:23:00 | NPP-375D | VIANA | MARANHÃO | Brasil | 2112803 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 9b83bc20-6632-3cd0-8d35-475dff31ac3a | -2.5475 | -46.55296 | 2024-12-02 04:23:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 40de86cd-1aff-3a64-92be-d4ebbc347fec | -2.72757 | -46.25259 | 2024-12-02 04:23:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |


[Clique aqui para ver as próximas entradas](README34.md)
