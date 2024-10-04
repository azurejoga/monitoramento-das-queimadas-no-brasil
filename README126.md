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

## Dados Diários - Página 126

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| daca30ee-3a54-371e-8a4b-7fd69247c261 | -16.62209 | -55.91213 | 2024-10-04 04:34:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.6 |
| 25b61b51-bff0-319f-9bf0-ebe7d8964971 | -16.62037 | -56.01513 | 2024-10-04 04:34:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.6 |
| f0dcd85c-2991-34ee-a753-ec889bf1ce1c | -16.61543 | -56.01828 | 2024-10-04 04:34:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.6 |
| efd3774b-7c6f-3d89-b6d7-ff2db72850aa | -16.61468 | -56.0223 | 2024-10-04 04:34:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.7 |
| 3de3f3b3-15a9-3331-8f6a-7b5919cc3cbf | -16.61048 | -56.02144 | 2024-10-04 04:34:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.5 |
| a323135f-2762-3616-8bd6-8de2daeec02d | -16.60553 | -56.02461 | 2024-10-04 04:34:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.5 |
| 38afb561-9654-382d-87a8-9cc237715c77 | -16.60133 | -56.02376 | 2024-10-04 04:34:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.9 |
| b49642b1-bd54-316b-b23e-42e68519f0a8 | -16.59891 | -55.99001 | 2024-10-04 04:34:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.1 |
| 59beb70b-3305-3e14-8701-7c6f3264416c | -16.59816 | -55.994 | 2024-10-04 04:34:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.3 |
| d5f1f21f-1f6d-30aa-b296-34b1f5e704ab | -17.07994 | -56.08695 | 2024-10-04 04:34:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.1 |
| ca02d710-850d-3b6e-ba48-ad6ea3ae9f07 | -17.06803 | -56.08048 | 2024-10-04 04:34:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.9 |
| 13f781c1-9370-39de-93cc-3c7c35365f21 | -17.06458 | -56.07563 | 2024-10-04 04:34:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.9 |
| c9bc4a9c-b5dd-3d70-92b7-a48d9f26828f | -17.06385 | -56.07962 | 2024-10-04 04:34:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.9 |
| 4affc94a-2413-3274-8cdf-f3f9823223e2 | -17.0604 | -56.07478 | 2024-10-04 04:34:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.7 |
| 80d050c4-b2a0-3b2f-8a3a-351eb9c8a522 | -17.05953 | -56.68834 | 2024-10-04 04:34:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.5 |
| ca47416c-d710-3c27-85d2-3b31d369ec92 | -17.05893 | -56.08276 | 2024-10-04 04:34:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.9 |
| e7281c92-9023-3afa-b41e-070428f0b240 | -17.05872 | -56.69268 | 2024-10-04 04:34:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.5 |
| 2350bd27-1dd7-36ca-bf64-c323a36b8ca4 | -17.05791 | -56.69703 | 2024-10-04 04:34:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.5 |
| 778d842d-3b61-3559-aa97-735051d579a9 | -17.05548 | -56.0779 | 2024-10-04 04:34:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.7 |
| edf75de0-547e-3a3f-b106-d6c5d1721753 | -17.05474 | -56.08189 | 2024-10-04 04:34:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.9 |
| 0a9e1edf-0154-32e3-b2e8-c6088ecc9748 | -17.05437 | -56.69177 | 2024-10-04 04:34:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |
| 50534ec7-d377-3bf1-875f-15748e198b97 | -17.05129 | -56.07705 | 2024-10-04 04:34:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.6 |
| 182b3f4d-bb79-3965-8a04-e898936bba27 | -17.0492 | -56.69522 | 2024-10-04 04:34:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.6 |
| 49c19636-b678-323e-8fa1-cbfad19cef3b | -17.04838 | -56.69957 | 2024-10-04 04:34:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.6 |
| 09476fce-3f8f-34d7-b343-4aa6be0cb1b8 | -17.04403 | -56.69867 | 2024-10-04 04:34:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.8 |
| 95e0040d-37ff-346c-b7af-c2e4e5e19d3c | -17.04321 | -56.70302 | 2024-10-04 04:34:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.1 |
| 98d472f3-36f8-37a5-a5ad-63ac55389f1c | -17.03968 | -56.69775 | 2024-10-04 04:34:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.8 |
| 0740c6f6-75c1-3d94-85aa-b14bdedd29ce | -17.03886 | -56.7021 | 2024-10-04 04:34:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.1 |
| 5989d21a-3e7d-3083-ac8f-d0e313e859cf | -17.03533 | -56.69684 | 2024-10-04 04:34:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 5.5 |
| 1b36cd63-99c6-3c12-8d17-ac80b3eb565a | -17.03451 | -56.70118 | 2024-10-04 04:34:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.3 |
| cfd3b67f-2bbc-3c04-a2db-ae692dc697cb | -16.93078 | -55.8417 | 2024-10-04 04:34:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |
| a07edffe-e195-3804-bbd2-2690b1fa0e1a | -16.9286 | -55.85336 | 2024-10-04 04:34:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.3 |
| 358d5cd0-28c4-3264-a0e5-c029b173d38e | -16.92811 | -55.8331 | 2024-10-04 04:34:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 5.4 |
| e63c08fc-cabb-343f-9e6e-777825d8d0c8 | -16.92787 | -55.85723 | 2024-10-04 04:34:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.3 |
| b39333cb-ec92-34d2-b0ca-dc6dc9eb8ac5 | -16.92738 | -55.83698 | 2024-10-04 04:34:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 6.6 |
| fa1cd400-097b-3c40-abe7-e430b51258d4 | -16.92665 | -55.84088 | 2024-10-04 04:34:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 6.6 |
| 4042b27b-30bd-3cd9-8d4e-ca6263e1aae0 | -16.92592 | -55.84477 | 2024-10-04 04:34:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.9 |
| b6fff063-693a-3a0f-82e7-0a9bc7f8a61f | -16.92519 | -55.84864 | 2024-10-04 04:34:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.9 |
| e3eaea25-3dce-3bcb-b144-3b0c0fa65f29 | -16.92397 | -55.83228 | 2024-10-04 04:34:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 5.4 |
| 3203c500-a860-34db-baf9-7472302a73fc | -16.92373 | -55.85639 | 2024-10-04 04:34:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 3.2 |
| d5e849d5-c983-3f26-9a58-30c8bc24c915 | -16.92324 | -55.83617 | 2024-10-04 04:34:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 6.6 |
| 25731ffd-4027-3189-bfea-d1b07232bad7 | -16.92301 | -55.86028 | 2024-10-04 04:34:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.9 |
| 22c8b7e9-cb44-3f58-93c0-d60c58d37507 | -16.92251 | -55.84006 | 2024-10-04 04:34:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 6.6 |
| bd22d14e-c152-34ce-a7d1-1250f9327f1f | -16.91985 | -55.83144 | 2024-10-04 04:34:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 6.7 |
| 721bd40c-8f59-30ed-b31f-479204b7b09d | -16.91911 | -55.83535 | 2024-10-04 04:34:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.6 |
| 23cc58e8-86c5-3f79-a0ab-6837c73c0fd1 | -16.91717 | -55.8229 | 2024-10-04 04:34:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 10.7 |
| d27beb67-a446-3f48-a899-fc4bc06aa457 | -16.91644 | -55.82676 | 2024-10-04 04:34:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 6.7 |
| d43113d2-9b4b-3e4e-9673-756881ad8e1f | -16.91571 | -55.83064 | 2024-10-04 04:34:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 6.7 |
| 767eb270-8546-36d7-aaaa-0f57e404333b | -16.91551 | -55.82322 | 2024-10-04 04:34:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 11.3 |
| 6c2c75ee-d86e-347c-8055-87cc8a67c3c9 | -16.91481 | -55.8271 | 2024-10-04 04:34:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 5.7 |
| 48b2ca8a-f26c-365e-900a-966c9ca43d67 | -16.9141 | -55.83098 | 2024-10-04 04:34:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 5.7 |
| 4b4e5027-8055-35ed-8209-0e6d8a4bbd11 | -16.914 | -55.86249 | 2024-10-04 04:34:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.9 |
| 4b33302c-fcc0-31f5-8db4-8abae71cfd91 | -16.91304 | -55.82208 | 2024-10-04 04:34:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.7 |
| c4a8db76-4ee7-3a9a-a80c-583cd5e1727d | -16.91279 | -55.8461 | 2024-10-04 04:34:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.9 |
| f93250ff-7263-3fe0-bf84-f85305fad18a | -16.9123 | -55.82596 | 2024-10-04 04:34:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.5 |
| 6b224776-dcb5-3f61-9c09-65d54b5e6a2a | -16.91129 | -55.84647 | 2024-10-04 04:34:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.3 |
| 2a2346bc-9c10-3389-8559-28820c76f004 | -16.90986 | -55.86165 | 2024-10-04 04:34:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.9 |
| 5ba71c4e-446d-31c7-9b38-f33c977ace02 | -16.90913 | -55.86554 | 2024-10-04 04:34:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 6.2 |
| 872e4c7e-4e2a-3bd3-8b75-bf361f7d1694 | -16.90846 | -55.86208 | 2024-10-04 04:34:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.2 |
| 288ccf70-4409-3782-828d-22044204dc36 | -16.90793 | -55.84914 | 2024-10-04 04:34:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.5 |
| fed9c8f9-9a6f-31f1-b70e-ca40aea6bb4b | -16.90775 | -55.86598 | 2024-10-04 04:34:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 4.6 |
| 0abc506c-18f9-3029-ae59-fdc307219894 | -16.90645 | -55.84952 | 2024-10-04 04:34:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.2 |
| 2b09a265-03c3-39c9-9e75-5a6c021e90d2 | -16.90572 | -55.86082 | 2024-10-04 04:34:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.1 |
| 2f562dd6-08fd-34ca-bb25-7edb9cd1eb22 | -16.90499 | -55.86471 | 2024-10-04 04:34:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.4 |
| 6098d408-5da9-3020-99a2-4b6c07d8ea65 | -16.90453 | -55.84443 | 2024-10-04 04:34:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.9 |
| de332e29-f781-3abf-9d69-49a7c73cf7f2 | -16.90432 | -55.86123 | 2024-10-04 04:34:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.2 |
| 006226e1-629b-3c35-85b6-f0675366657b | -16.90302 | -55.84479 | 2024-10-04 04:34:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.7 |
| e114549d-baf6-360c-bc7c-099747b564e9 | -16.90158 | -55.85997 | 2024-10-04 04:34:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.1 |
| c7ac846f-5280-3d08-bdcb-3b4bbbdfbe92 | -16.90089 | -55.85648 | 2024-10-04 04:34:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.4 |
| f650f85d-4338-3a87-8397-f6d348488812 | -16.90018 | -55.86039 | 2024-10-04 04:34:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.4 |
| 96ba4dd1-9c0a-3122-9e0e-693022b68731 | -16.89604 | -55.85954 | 2024-10-04 04:34:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.4 |
| ce7b5f4d-aefa-365d-9fa6-03a0c6f90537 | -16.89546 | -55.83923 | 2024-10-04 04:34:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.2 |
| db5fe812-d57b-332a-b4d8-947c73596311 | -16.8919 | -55.8587 | 2024-10-04 04:34:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.3 |
| 678fe9e5-a10f-3b20-865e-7b6e02101938 | -16.88919 | -55.85006 | 2024-10-04 04:34:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.9 |
| e6097f98-8fdf-376e-a630-226e58d40d27 | -16.88848 | -55.85396 | 2024-10-04 04:34:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.3 |
| b453c215-ecdc-36ec-8791-509a5ca5a25f | -16.88505 | -55.84922 | 2024-10-04 04:34:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.1 |
| 0dfd49ac-bc2e-3850-bb19-b0f7d4db1454 | -16.8802 | -55.85228 | 2024-10-04 04:34:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.3 |
| d6099aea-4423-3ce4-a82b-1e9a60e0733d | -17.15477 | -56.15207 | 2024-10-04 04:34:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.4 |
| 9eb5016d-a7fe-3fcf-99a4-0f92b8a4abce | -17.15253 | -56.16415 | 2024-10-04 04:34:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.3 |
| abcefe48-62b6-3a95-ac04-b128958fac1e | -17.15179 | -56.16819 | 2024-10-04 04:34:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 3.1 |
| a3a4997a-8566-3cd9-a32d-d4f71a4db383 | -17.15057 | -56.15121 | 2024-10-04 04:34:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.4 |
| f96e3231-2c2b-3c6a-9d65-ad7ea1fec08e | -17.14908 | -56.15927 | 2024-10-04 04:34:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.3 |
| 3dbb1d23-bb0f-389f-bf42-4ca3b54fea6e | -17.14833 | -56.1633 | 2024-10-04 04:34:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.3 |
| b8d90d70-770c-3282-a7de-235122b46884 | -11.92829 | -56.95345 | 2024-10-04 04:34:00 | NPP-375D | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 37868166-f3aa-330a-a83c-ec2050578220 | -11.92595 | -56.95161 | 2024-10-04 04:34:00 | NPP-375D | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 362dcd2b-d8b0-3df4-990c-ff6c074a12c8 | -11.92345 | -56.95245 | 2024-10-04 04:34:00 | NPP-375D | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a0192706-367b-3db9-8370-a6d3abef3d8b | -11.9211 | -56.9506 | 2024-10-04 04:34:00 | NPP-375D | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 43db7f9e-5df6-3913-a0f3-c4f46a8ec87d | -11.91726 | -56.94415 | 2024-10-04 04:34:00 | NPP-375D | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 851c38d0-aade-34ee-8f9d-2f6748cf87a6 | -11.91626 | -56.94957 | 2024-10-04 04:34:00 | NPP-375D | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 4c4f87ab-f681-3563-a412-65ea191453e4 | -11.91142 | -56.94855 | 2024-10-04 04:34:00 | NPP-375D | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 81076a4d-1a08-3bde-a23f-1cef876cf06f | -11.91042 | -56.95395 | 2024-10-04 04:34:00 | NPP-375D | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 4f8de7ad-ad5f-3df9-ab9b-12c11c99fbce | -11.90171 | -56.94662 | 2024-10-04 04:34:00 | NPP-375D | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 474d6d46-09b5-38b8-aa10-b560d23c60f0 | -11.90072 | -56.95198 | 2024-10-04 04:34:00 | NPP-375D | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 510aab37-d63a-34ef-b9a6-0672c4e80d9f | -11.88759 | -56.20093 | 2024-10-04 04:34:00 | NPP-375D | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ef8fd23c-e5e5-3167-a04f-161525cc2e10 | -12.61028 | -56.48798 | 2024-10-04 04:34:00 | NPP-375D | TAPURAH | MATO GROSSO | Brasil | 5108006 | 51 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 4dbeeec0-648a-39e1-9282-957d461673c7 | -13.0673 | -57.25789 | 2024-10-04 04:34:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3242ee92-17b0-33ca-9790-a931c84299e9 | -13.0654 | -57.25271 | 2024-10-04 04:34:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 920489f4-767b-3476-bd6b-fa9e0289bcad | -14.98659 | -56.44309 | 2024-10-04 04:34:00 | NPP-375D | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| cc47e834-6a10-34f7-b9c8-2cd1021ce40e | -14.98574 | -56.4476 | 2024-10-04 04:34:00 | NPP-375D | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 3.3 |
| c67546f9-a913-3caf-9a62-21fa08bec892 | -16.46572 | -57.43715 | 2024-10-04 04:34:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.7 |


[Clique aqui para ver as próximas entradas](README127.md)
