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

## Dados Diários - Página 5

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 0344edc3-6f77-3689-b5ac-cb5e2ec89a4a | -10.8862 | -46.384998 | 2024-09-28 00:13:28 | METOP-B | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 093c6252-fbe3-3ca3-b8dd-c861f0eec6d4 | -10.8882 | -46.394402 | 2024-09-28 00:13:28 | METOP-B | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 23894ca8-2b7b-371e-ab39-5a5fb71fb1f8 | -10.8902 | -46.403801 | 2024-09-28 00:13:28 | METOP-B | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| f3b0bcad-9b2f-36e8-a646-6349a5977529 | -10.8922 | -46.4133 | 2024-09-28 00:13:28 | METOP-B | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 2f2abc42-cd24-31a8-b81d-60d5ae475a6d | -10.8942 | -46.422798 | 2024-09-28 00:13:28 | METOP-B | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 0f6e3516-af78-3f67-9774-f6533a2fc5c1 | -10.266 | -43.5476 | 2024-09-28 00:13:29 | METOP-B | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| e309e715-0506-39d4-8cd5-623988f3f328 | -10.2676 | -43.554699 | 2024-09-28 00:13:29 | METOP-B | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 162015ec-32a9-3791-871e-9f73b653e204 | -10.2692 | -43.561798 | 2024-09-28 00:13:29 | METOP-B | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 17d1ed85-7810-3e39-ac55-0d86bbd88dc8 | -10.2707 | -43.569 | 2024-09-28 00:13:29 | METOP-B | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 9c633af7-b0fa-3f97-9686-882247f2652c | -10.2723 | -43.576099 | 2024-09-28 00:13:29 | METOP-B | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 29a679cc-2a30-324e-90b5-bb7883d1904a | -10.2578 | -43.5569 | 2024-09-28 00:13:29 | METOP-B | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| a89bfb97-df62-3f1e-8953-339c5026fc16 | -10.2594 | -43.563999 | 2024-09-28 00:13:29 | METOP-B | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 61f0a47f-2ba8-3d65-8b0b-4740ab1fd53f | -10.2609 | -43.571201 | 2024-09-28 00:13:29 | METOP-B | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 8088debb-d85d-3729-a5e4-f6d42f1598c7 | -10.2625 | -43.5783 | 2024-09-28 00:13:29 | METOP-B | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| fc12e3c4-701b-3102-b131-effed888f535 | -10.8804 | -46.405899 | 2024-09-28 00:13:29 | METOP-B | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 78109a25-c732-3d70-97de-b9c3f4d66d68 | -10.8824 | -46.415401 | 2024-09-28 00:13:29 | METOP-B | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| a65aa87e-d7ed-3d9f-885b-122a203c193a | -10.8686 | -46.398602 | 2024-09-28 00:13:29 | METOP-B | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| b863f722-6342-3e5d-a927-fab51a5838e9 | -10.8706 | -46.408001 | 2024-09-28 00:13:29 | METOP-B | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 694cf1e1-966d-3a0b-9f2e-a53632766659 | -10.8726 | -46.4175 | 2024-09-28 00:13:29 | METOP-B | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| f2b9c718-7b82-3f8d-a7b6-254893ccc4bc | -10.6616 | -45.854401 | 2024-09-28 00:13:30 | METOP-B | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 82506d34-c9e3-3daf-958a-a58373df163a | -10.6653 | -45.871899 | 2024-09-28 00:13:30 | METOP-B | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| e84772ab-6e27-38ad-9f64-b02e04168917 | -10.6672 | -45.880699 | 2024-09-28 00:13:30 | METOP-B | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 380814ae-161d-35f7-a669-ee96debe74bf | -10.6691 | -45.8895 | 2024-09-28 00:13:30 | METOP-B | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| ce9d6725-6ca4-32ed-8a0c-11d5cf2064ca | -10.65 | -45.847698 | 2024-09-28 00:13:30 | METOP-B | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| be6243c9-9103-3e14-9e6a-91ce96796d63 | -10.6667 | -45.9268 | 2024-09-28 00:13:30 | METOP-B | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 20252e23-c5ab-3db4-a679-749902082586 | -10.6812 | -45.850101 | 2024-09-28 00:13:30 | METOP-B | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 51907c15-d89d-3735-a08e-6e4116d61471 | -10.6635 | -45.863098 | 2024-09-28 00:13:30 | METOP-B | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| f3a32ea7-0e43-3e92-853e-6b772e85967f | -10.6463 | -45.8302 | 2024-09-28 00:13:30 | METOP-B | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| f818518b-b74f-323d-acf1-04f416246854 | -10.6481 | -45.839001 | 2024-09-28 00:13:30 | METOP-B | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| d0a9f1da-2f81-315b-83b6-fdb31dbfdc00 | -10.6588 | -45.937698 | 2024-09-28 00:13:31 | METOP-B | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| ac667403-efb7-3742-b072-d206f1035db4 | -10.6626 | -45.955502 | 2024-09-28 00:13:31 | METOP-B | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 166aa4f5-c48a-3355-8778-aa2e0761e9d7 | -10.6551 | -45.920101 | 2024-09-28 00:13:31 | METOP-B | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 6e3198a2-45f9-3297-8448-1c26f09eeb41 | -10.6569 | -45.928902 | 2024-09-28 00:13:31 | METOP-B | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 0deb06cc-2ca2-3a4e-82eb-0db9f9ab0e67 | -10.6607 | -45.946602 | 2024-09-28 00:13:31 | METOP-B | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 6a3fffc3-0f43-350c-800d-931627855192 | -10.6645 | -45.964298 | 2024-09-28 00:13:31 | METOP-B | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| e0789c19-695f-362c-a83f-3432b8571324 | -10.6509 | -45.9487 | 2024-09-28 00:13:31 | METOP-B | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 22f6968f-0e83-3547-b882-b6bb87b0f3cc | -10.6385 | -46.035099 | 2024-09-28 00:13:31 | METOP-B | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| ca1ce855-5953-3993-a184-1018e50db0da | -10.6306 | -46.046101 | 2024-09-28 00:13:31 | METOP-B | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 5ccfefe8-9188-38f1-aa0b-55320dad056a | -10.6324 | -46.055099 | 2024-09-28 00:13:31 | METOP-B | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| a00d2316-15d7-3413-99bf-fed2528c6124 | -10.6366 | -46.026199 | 2024-09-28 00:13:31 | METOP-B | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 0c1c1f13-e50e-32d8-80cc-ed4a320f08d6 | -10.6166 | -46.077301 | 2024-09-28 00:13:32 | METOP-B | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 1c05b0ef-e84f-3967-9949-c1ed29926731 | -10.6069 | -46.079399 | 2024-09-28 00:13:32 | METOP-B | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 44660aca-20d8-3642-80f2-d7047b1563e9 | -10.5839 | -46.018799 | 2024-09-28 00:13:32 | METOP-B | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 9d9b61dc-9663-32e8-80db-0a1a94209df2 | -10.6208 | -46.048199 | 2024-09-28 00:13:32 | METOP-B | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| c7379311-4b90-3ecc-9d3b-cd11e6a27616 | -10.6226 | -46.057201 | 2024-09-28 00:13:32 | METOP-B | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 1227e5f6-2de6-391c-b1b4-e5deb041ca74 | -10.6245 | -46.0662 | 2024-09-28 00:13:32 | METOP-B | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 4183856b-00e0-3b93-8ba9-9ef613b93201 | -10.6264 | -46.075199 | 2024-09-28 00:13:32 | METOP-B | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 6e85c3bc-a260-3091-b21a-7f2e2df8eedf | -10.611 | -46.050301 | 2024-09-28 00:13:32 | METOP-B | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| cf746433-70ac-3227-809f-1f80b63ca39a | -10.6128 | -46.059299 | 2024-09-28 00:13:32 | METOP-B | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| c23981a7-e3cf-3ea1-bfe7-efb1125de4f5 | -10.6147 | -46.068298 | 2024-09-28 00:13:32 | METOP-B | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 5e966933-4f0d-3bcf-8b11-21f6acf53c79 | -10.605 | -46.0704 | 2024-09-28 00:13:32 | METOP-B | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 57bf2629-5ebd-3559-987e-ec5346bc04e1 | -10.5877 | -46.036701 | 2024-09-28 00:13:32 | METOP-B | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| fa2a4f61-bfb6-3381-9c78-6849ab00274b | -10.5896 | -46.045601 | 2024-09-28 00:13:32 | METOP-B | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| d913edc2-d4f6-3c17-9736-e7ddbeb46d8b | -10.5741 | -46.020901 | 2024-09-28 00:13:32 | METOP-B | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 698fae28-6b00-3ef4-96aa-cf54b957c3ec | -10.576 | -46.0298 | 2024-09-28 00:13:32 | METOP-B | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| d7a6f290-8359-3282-ace2-eaef3a48c5c0 | -10.5779 | -46.038799 | 2024-09-28 00:13:32 | METOP-B | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 87661ba3-b395-3d98-8cef-fa0b7e0e63cf | -10.5798 | -46.047699 | 2024-09-28 00:13:32 | METOP-B | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 5d8b8a9c-884b-3d1e-b44f-67636ac0c715 | -10.5835 | -46.065601 | 2024-09-28 00:13:32 | METOP-B | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| fd4ed251-3aaf-3046-9b97-d3e6215bd814 | -10.5854 | -46.0746 | 2024-09-28 00:13:32 | METOP-B | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| e7509022-2e16-3d0a-bee7-5b9119e18450 | -10.5643 | -46.022999 | 2024-09-28 00:13:32 | METOP-B | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| dfd60eee-9665-3af7-925a-6b4576062ac7 | -10.5662 | -46.031898 | 2024-09-28 00:13:32 | METOP-B | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| a73891a3-0e82-37bd-9229-58f3715a46aa | -10.5681 | -46.040901 | 2024-09-28 00:13:32 | METOP-B | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| b0cf1d9f-bd33-3d0d-a0d3-1b76d176520d | -10.5737 | -46.067699 | 2024-09-28 00:13:32 | METOP-B | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 52cfd6df-dcad-37d5-98b5-e1e862644c32 | -10.5775 | -46.085701 | 2024-09-28 00:13:32 | METOP-B | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 8e31e8c6-57ce-37ef-b50d-b5c1ea256b26 | -10.5794 | -46.094601 | 2024-09-28 00:13:32 | METOP-B | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 613517b0-2bbd-32a8-904d-54d3d6de44af | -10.3197 | -45.1651 | 2024-09-28 00:13:33 | METOP-B | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 37034d3e-df0f-3102-bc6b-4ac23da1744f | -10.3215 | -45.173199 | 2024-09-28 00:13:33 | METOP-B | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 31b6827f-5f31-32bd-b592-d1a8ff11c5f0 | -10.5564 | -46.034 | 2024-09-28 00:13:33 | METOP-B | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 2c3edbe5-a9d7-32e4-b620-4e05bd8430a5 | -10.5677 | -46.087799 | 2024-09-28 00:13:33 | METOP-B | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| dac7afa4-d925-3d2c-9631-1e4ac95c0d5a | -10.5696 | -46.096699 | 2024-09-28 00:13:33 | METOP-B | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| f30c0703-d0e2-3860-b5a4-434689f0b379 | -9.9493 | -44.025299 | 2024-09-28 00:13:35 | METOP-B | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 7087e5f0-3550-3ace-aa39-7efebba08898 | -10.1006 | -44.7677 | 2024-09-28 00:13:36 | METOP-B | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| a98ef7ba-7978-38c5-82ab-acbabda1b3ea | -10.9427 | -50.1012 | 2024-09-28 00:13:40 | METOP-B | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| c1f2f290-4a4e-37f2-94f9-bd40e3470193 | -10.8859 | -50.4272 | 2024-09-28 00:13:42 | METOP-B | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 554b88ac-23c7-35ca-8d88-5618da20128a | -10.4217 | -48.178101 | 2024-09-28 00:13:42 | METOP-B | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 2e43b2c8-20e6-3ecb-a889-4fecbe8cb02c | -10.4241 | -48.189999 | 2024-09-28 00:13:42 | METOP-B | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| a39b949f-a9bc-3876-97d8-89f16d21a6eb | -10.8761 | -50.429199 | 2024-09-28 00:13:42 | METOP-B | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 0de149a4-6d9a-36dd-ae66-4be379db5fd1 | -10.8796 | -50.446499 | 2024-09-28 00:13:42 | METOP-B | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 6d7721fb-cf73-36c8-9e4c-587fed03f004 | -9.4742 | -44.061901 | 2024-09-28 00:13:43 | METOP-B | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| bbcbf5aa-56e7-322d-8fe6-5fd941fe8292 | -9.4758 | -44.069099 | 2024-09-28 00:13:43 | METOP-B | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 4448e045-0bc1-38c1-922c-587bc695def2 | -9.2805 | -43.4632 | 2024-09-28 00:13:44 | METOP-B | CAMPO ALEGRE DE LOURDES | BAHIA | Brasil | 2905909 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| 8313888e-e1da-33c5-8940-5d1104354310 | -9.1277 | -43.145901 | 2024-09-28 00:13:46 | METOP-B | JUREMA | PIAUÍ | Brasil | 2205532 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 6ea7723c-60da-365a-90a1-d02764af4c02 | -9.1179 | -43.148102 | 2024-09-28 00:13:46 | METOP-B | JUREMA | PIAUÍ | Brasil | 2205532 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| bba5636c-4e7c-3bff-8d7e-1fddb20e2be0 | -9.1261 | -43.138901 | 2024-09-28 00:13:46 | METOP-B | JUREMA | PIAUÍ | Brasil | 2205532 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| d9747491-b4c2-3c4a-87fc-d5a8d600a872 | -10.6921 | -50.930401 | 2024-09-28 00:13:47 | METOP-B | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 359949db-d943-33df-b34f-fe0e2ed31b05 | -10.6957 | -50.949001 | 2024-09-28 00:13:47 | METOP-B | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 071a4231-c839-3d95-a076-8e2465590f13 | -8.3937 | -40.857399 | 2024-09-28 00:13:49 | METOP-B | DORMENTES | PERNAMBUCO | Brasil | 2605152 | 26 | 33 | nan | nan | nan | Caatinga | nan |
| ca0706d0-1130-3d55-88a7-c804911f4eb6 | -8.3954 | -40.864799 | 2024-09-28 00:13:49 | METOP-B | AFRÂNIO | PERNAMBUCO | Brasil | 2600203 | 26 | 33 | nan | nan | nan | Caatinga | nan |
| 219dcb4f-84c8-36b3-8fa1-1098295c0b7f | -10.6073 | -51.0639 | 2024-09-28 00:13:49 | METOP-B | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 865efe2b-f562-3c33-9b95-4346c3ae3b88 | -10.5975 | -51.0658 | 2024-09-28 00:13:49 | METOP-B | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 054674fa-afd2-3c9a-a077-8301e63ff544 | -10.5878 | -51.067699 | 2024-09-28 00:13:49 | METOP-B | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| fc4a74f5-bdf9-3c7c-b89e-cf1536b68a6a | -8.8251 | -44.243099 | 2024-09-28 00:13:54 | METOP-B | CRISTINO CASTRO | PIAUÍ | Brasil | 2203107 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| da703a1b-8a4b-3e34-9f67-49deadb304ca | -8.1063 | -41.132702 | 2024-09-28 00:13:55 | METOP-B | PAULISTANA | PIAUÍ | Brasil | 2207801 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| aebd089f-9e9c-3911-b800-d72ab3b4c76b | -8.108 | -41.139999 | 2024-09-28 00:13:55 | METOP-B | PAULISTANA | PIAUÍ | Brasil | 2207801 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 99650b0e-3598-33aa-bc60-d8075686fe9f | -8.833 | -45.076801 | 2024-09-28 00:13:57 | METOP-B | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 723c20be-2ee0-3e16-aafb-99993c6325d2 | -7.1244 | -38.768002 | 2024-09-28 00:14:02 | METOP-B | BARRO | CEARÁ | Brasil | 2302008 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| 9bd3ac9c-b328-3c9f-9235-892139f203ca | -8.0669 | -42.8689 | 2024-09-28 00:14:02 | METOP-B | PAJEÚ DO PIAUÍ | PIAUÍ | Brasil | 2207355 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 8dc509ff-3ffc-33e2-a83f-8c621ebb3b54 | -8.0684 | -42.875801 | 2024-09-28 00:14:02 | METOP-B | PAJEÚ DO PIAUÍ | PIAUÍ | Brasil | 2207355 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 6bb198fa-3bd8-374f-92ef-bd67370fb428 | -8.0731 | -42.8965 | 2024-09-28 00:14:02 | METOP-B | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 0d9cad8b-282f-3a93-8369-0d0cb9648108 | -8.0746 | -42.903301 | 2024-09-28 00:14:02 | METOP-B | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | nan |


[Clique aqui para ver as próximas entradas](README6.md)
