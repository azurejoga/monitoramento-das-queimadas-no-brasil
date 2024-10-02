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

## Dados Diários - Página 28

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| d6b82ae4-3649-351c-8b3a-26ec57a8fc2e | -16.511299 | -57.311298 | 2024-10-02 01:24:03 | METOP-C | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 25c6ea87-b740-335d-9c0a-07b24fc86a09 | -16.498301 | -57.298599 | 2024-10-02 01:24:04 | METOP-C | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 86bcdc2b-2124-3d07-996e-896abf77f10b | -16.499901 | -57.306 | 2024-10-02 01:24:04 | METOP-C | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| ed865472-4300-3817-9bf6-4c5ec2ed7429 | -16.501499 | -57.313499 | 2024-10-02 01:24:04 | METOP-C | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 22fb624e-a5ea-3a2e-b705-190996b241d9 | -16.503099 | -57.3209 | 2024-10-02 01:24:04 | METOP-C | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| d61bedc8-5ab5-3768-b0ea-0f118c0432ee | -16.5047 | -57.3284 | 2024-10-02 01:24:04 | METOP-C | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| db775711-cce5-3c4f-b41b-6464fba51a45 | -16.483801 | -57.278599 | 2024-10-02 01:24:04 | METOP-C | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 0b27a032-f760-3de8-9b14-1e8cc01dd242 | -16.485399 | -57.285999 | 2024-10-02 01:24:04 | METOP-C | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| dfe2d8dd-d432-35ee-aac9-ba43fe50cda8 | -16.487 | -57.2934 | 2024-10-02 01:24:04 | METOP-C | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 2a5744fb-5d54-3298-a449-68b38ea1d800 | -16.4886 | -57.3009 | 2024-10-02 01:24:04 | METOP-C | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| e0f95423-a465-3d00-9fad-0a04b5d9011f | -16.4902 | -57.3083 | 2024-10-02 01:24:04 | METOP-C | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| a98a5915-1586-3737-a944-b83607b3bddb | -16.4918 | -57.3158 | 2024-10-02 01:24:04 | METOP-C | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 082dfac4-358f-3dbd-8941-d105cbf076dc | -16.493401 | -57.3232 | 2024-10-02 01:24:04 | METOP-C | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 853221da-4aac-3ac7-ac2f-db116e5ab6ec | -16.495001 | -57.3307 | 2024-10-02 01:24:04 | METOP-C | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 74b6cb15-6cc2-353d-a7cd-7f63ffd75f29 | -16.474001 | -57.2808 | 2024-10-02 01:24:04 | METOP-C | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 6a5ce4c4-c98a-3360-9677-77c3c1435170 | -16.475599 | -57.2882 | 2024-10-02 01:24:04 | METOP-C | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 12c550d9-e0ed-388f-9740-4c1f2e625cf7 | -16.4772 | -57.295601 | 2024-10-02 01:24:04 | METOP-C | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 75a44797-fab2-3979-9984-55d0ef4a4a1b | -16.4788 | -57.303101 | 2024-10-02 01:24:04 | METOP-C | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 48972acb-8f58-3324-a736-a49ea51bddec | -16.4804 | -57.310501 | 2024-10-02 01:24:04 | METOP-C | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 46915a19-1de1-333e-815c-eeac9d8f6394 | -16.482 | -57.318001 | 2024-10-02 01:24:04 | METOP-C | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 5fe8ed71-00dc-3a74-9646-46fdbba66fa8 | -16.483601 | -57.325401 | 2024-10-02 01:24:04 | METOP-C | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 7694a98e-fe4b-3270-bdd4-5b83c0cb67ed | -16.464199 | -57.2831 | 2024-10-02 01:24:04 | METOP-C | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 8ab296db-7c13-30ed-a9b6-b79d7800808c | -16.465799 | -57.290501 | 2024-10-02 01:24:04 | METOP-C | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 81a674eb-24b2-30c4-8928-4f0063413ecd | -16.4674 | -57.297901 | 2024-10-02 01:24:04 | METOP-C | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| fc58423e-9171-3ec7-83ee-a5aae7877ad8 | -16.469 | -57.305401 | 2024-10-02 01:24:04 | METOP-C | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| e2415a72-4c4b-36b2-8335-36317cf6b49b | -16.4706 | -57.312801 | 2024-10-02 01:24:04 | METOP-C | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 32fce1a5-5bf2-3e90-9a1d-a0fd5c018c46 | -16.4722 | -57.320301 | 2024-10-02 01:24:04 | METOP-C | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 4a71ea77-a947-3dee-b04c-cd5fd94dfe41 | -16.4592 | -57.307598 | 2024-10-02 01:24:04 | METOP-C | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| be7dc1e3-fc7a-30ca-bb67-ca9581527db9 | -16.4608 | -57.314999 | 2024-10-02 01:24:04 | METOP-C | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 9c1427c5-87e6-3e05-ba4d-484852113bae | -16.4624 | -57.322498 | 2024-10-02 01:24:04 | METOP-C | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| e3df0f34-34d1-32cc-af4f-4bec20092298 | -16.464001 | -57.329899 | 2024-10-02 01:24:04 | METOP-C | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| e5eb6b57-e4f4-30a0-845a-8cbb993aa4cf | -16.467199 | -57.344799 | 2024-10-02 01:24:04 | METOP-C | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 68fa6677-1905-3fab-a4e0-9897fd7eb8f4 | -16.468901 | -57.352299 | 2024-10-02 01:24:04 | METOP-C | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| cb9ef923-52eb-3501-9785-3d269aba1b06 | -16.470501 | -57.359798 | 2024-10-02 01:24:04 | METOP-C | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 8209cfe0-532d-30d7-aaa5-c925fea36dd7 | -16.451 | -57.3172 | 2024-10-02 01:24:04 | METOP-C | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 98c92bd8-c38c-327d-b571-f99ac72edf3c | -16.4526 | -57.324699 | 2024-10-02 01:24:04 | METOP-C | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 766e7e49-cced-3e4f-9823-c5da731facf1 | -16.454201 | -57.3321 | 2024-10-02 01:24:04 | METOP-C | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 76250ab3-689b-3890-9257-9391f3324a9a | -16.455799 | -57.3396 | 2024-10-02 01:24:04 | METOP-C | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 758baa04-bd08-388c-9756-34858d816113 | -16.457399 | -57.347 | 2024-10-02 01:24:04 | METOP-C | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 913d70b3-1a7f-3368-a569-2656f03cef18 | -16.459101 | -57.3545 | 2024-10-02 01:24:04 | METOP-C | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| f9b96df0-fa5d-38d3-b2b4-71dda1d366d2 | -16.460699 | -57.362 | 2024-10-02 01:24:04 | METOP-C | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| ac68760e-f555-3e57-907b-2c34e060fb7f | -16.462299 | -57.3694 | 2024-10-02 01:24:04 | METOP-C | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 08c46d88-8f2f-3ecc-835e-ada9e8132467 | -16.4655 | -57.384399 | 2024-10-02 01:24:04 | METOP-C | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| aaaa30e4-7743-3dc8-aff2-6b40a6bb39c1 | -16.4671 | -57.391899 | 2024-10-02 01:24:04 | METOP-C | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| c8d9d2c3-1c28-3779-b50d-9b9c325a8162 | -16.4769 | -57.436798 | 2024-10-02 01:24:04 | METOP-C | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 885b3bdb-c9cb-3e29-b8ad-f3bab8181e20 | -16.4785 | -57.444302 | 2024-10-02 01:24:04 | METOP-C | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 31323014-c9a8-3711-9702-296b19860129 | -16.4622 | -57.416599 | 2024-10-02 01:24:05 | METOP-C | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 3e66b01d-f166-3523-a181-38bbca5234d2 | -16.4638 | -57.424099 | 2024-10-02 01:24:05 | METOP-C | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| c958e269-dcb5-3099-9194-cf7f2a7ad64b | -16.465401 | -57.431599 | 2024-10-02 01:24:05 | METOP-C | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| d788344b-1204-3c8d-a120-c2b797121086 | -16.4459 | -57.388802 | 2024-10-02 01:24:05 | METOP-C | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 5454505f-3966-3edc-9f23-a75ddcae97cd | -16.4475 | -57.396301 | 2024-10-02 01:24:05 | METOP-C | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 35132150-7cf0-31b2-8cd2-87d527170b54 | -16.4492 | -57.403801 | 2024-10-02 01:24:05 | METOP-C | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 062aa8cf-436a-341b-a8b8-34821bf83efb | -16.4524 | -57.4188 | 2024-10-02 01:24:05 | METOP-C | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 7d53409b-33d3-37bb-a245-5de079483a50 | -16.454 | -57.4263 | 2024-10-02 01:24:05 | METOP-C | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| d9a3e590-faca-3c54-868c-860c447d762a | -16.455601 | -57.4338 | 2024-10-02 01:24:05 | METOP-C | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 27384949-cb61-352d-8155-fdb43dce2d05 | -16.4377 | -57.398602 | 2024-10-02 01:24:05 | METOP-C | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| b7e3ad44-7da6-3817-bb6b-33083e1468e5 | -16.4426 | -57.421001 | 2024-10-02 01:24:05 | METOP-C | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 2c3ed73f-7e0d-3f72-ae24-f941bb86536f | -16.444201 | -57.428501 | 2024-10-02 01:24:05 | METOP-C | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| f102d828-30d9-3119-bc51-c0fab1325a19 | -16.445801 | -57.436001 | 2024-10-02 01:24:05 | METOP-C | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 232f41b4-18b8-3477-8945-7d8921c74543 | -16.6108 | -58.207401 | 2024-10-02 01:24:05 | METOP-C | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| ddc8557b-b830-3812-8fc4-f2b769b3133d | -16.612499 | -58.215401 | 2024-10-02 01:24:05 | METOP-C | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| c0be3d54-0484-319b-be19-8f81c0c00d90 | -16.6141 | -58.223301 | 2024-10-02 01:24:05 | METOP-C | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| a4d110ef-889a-3d8f-9206-c5ea499e292a | -16.4345 | -57.430801 | 2024-10-02 01:24:05 | METOP-C | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 55054ca4-3242-3c0d-8de5-612e5697504f | -16.4361 | -57.438301 | 2024-10-02 01:24:05 | METOP-C | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 9eb82282-3b0a-3dee-822b-f9cc168cbbe5 | -16.5993 | -58.201599 | 2024-10-02 01:24:05 | METOP-C | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| a76e0cb4-08c5-3adf-937a-4e02f46c9274 | -16.601 | -58.209599 | 2024-10-02 01:24:05 | METOP-C | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| e6a799f4-6009-30dd-9e8a-bbd0f22a24ff | -16.602699 | -58.217602 | 2024-10-02 01:24:05 | METOP-C | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 1ef43906-e708-370a-b713-9437891ebe32 | -16.6043 | -58.225498 | 2024-10-02 01:24:05 | METOP-C | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 5e12dd8a-8243-3a85-9e7b-a8ced149f3d7 | -16.606001 | -58.233501 | 2024-10-02 01:24:05 | METOP-C | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 6f11fe42-48ba-3547-8739-b41dfb116efb | -16.5895 | -58.2038 | 2024-10-02 01:24:05 | METOP-C | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 0229c3f8-3ba6-3f01-a73e-a83ce67d47ed | -16.5912 | -58.2118 | 2024-10-02 01:24:05 | METOP-C | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 3a6b97a7-f306-3a3d-b403-00cc78390017 | -16.592899 | -58.219799 | 2024-10-02 01:24:05 | METOP-C | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 847e3b05-b026-3980-8f31-71ebe1f0603e | -16.5945 | -58.227699 | 2024-10-02 01:24:05 | METOP-C | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 384fb7ed-8c0c-3ef6-93e3-cfbf953b10b2 | -16.596201 | -58.235699 | 2024-10-02 01:24:05 | METOP-C | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| bbd70120-44c0-3dac-bdaf-829b2c56d246 | -16.5798 | -58.206001 | 2024-10-02 01:24:05 | METOP-C | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 42c5ffc3-6589-329a-a066-4dcae59c0ef1 | -16.581499 | -58.214001 | 2024-10-02 01:24:05 | METOP-C | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 5d4af888-b36c-36ac-9942-20a0c132194c | -16.5832 | -58.222 | 2024-10-02 01:24:05 | METOP-C | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| d2fdc22c-4074-30fe-95f4-97301cdb40a6 | -16.584801 | -58.2299 | 2024-10-02 01:24:05 | METOP-C | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| e5e3f070-eb72-3b55-b4b3-43f93ffc80a9 | -16.5865 | -58.2379 | 2024-10-02 01:24:05 | METOP-C | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 55aad661-5b3f-31e3-a581-b31af88b53fb | -16.5882 | -58.245899 | 2024-10-02 01:24:05 | METOP-C | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 52f58450-057b-3b8d-9181-3e4da58170db | -16.571699 | -58.216202 | 2024-10-02 01:24:06 | METOP-C | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 69bd1d61-6528-3787-a50c-d28cefa556ec | -16.5734 | -58.224201 | 2024-10-02 01:24:06 | METOP-C | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 2f5cea78-8e26-300a-9e1a-c72719383c20 | -16.575001 | -58.232101 | 2024-10-02 01:24:06 | METOP-C | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| eb6da4f1-cc4f-301b-86c3-d30ef84b3a9a | -16.5767 | -58.240101 | 2024-10-02 01:24:06 | METOP-C | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 414be904-0603-389c-ab22-38f27db89e6e | -16.5784 | -58.2481 | 2024-10-02 01:24:06 | METOP-C | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| a6a24962-0a52-30dc-afc8-585a1ae1e360 | -16.565201 | -58.234299 | 2024-10-02 01:24:06 | METOP-C | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 9dc65d41-d7ad-3a64-adad-f7202984edc6 | -16.5669 | -58.242298 | 2024-10-02 01:24:06 | METOP-C | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 97673828-9824-3428-92bf-57341e601cd9 | -16.5686 | -58.250301 | 2024-10-02 01:24:06 | METOP-C | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 074f20b6-6bd2-31a9-9b3b-89d5448155dd | -15.9032 | -55.402599 | 2024-10-02 01:24:06 | METOP-C | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 1f959b61-6349-3588-bed3-b81415062a4a | -15.8919 | -55.3978 | 2024-10-02 01:24:07 | METOP-C | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| b76f1d25-90ea-340a-9ddb-387fed88197f | -16.0951 | -57.523701 | 2024-10-02 01:24:11 | METOP-C | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 9a7c1990-37d1-3b5e-be50-e983cb9aba19 | -16.096701 | -57.5312 | 2024-10-02 01:24:11 | METOP-C | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 5dee233d-4e76-361d-a931-b619a5c58cb6 | -13.7518 | -48.302898 | 2024-10-02 01:24:13 | METOP-C | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 85888756-3b2e-3bae-ac6e-34819cc4c197 | -16.186001 | -58.427799 | 2024-10-02 01:24:13 | METOP-C | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| dac3b768-45b0-3f07-8d7b-3c6d75d0b2a2 | -15.9038 | -57.163601 | 2024-10-02 01:24:13 | METOP-C | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| df3bc511-be76-3390-b29d-16b8b8e3a9b1 | -15.9054 | -57.170898 | 2024-10-02 01:24:13 | METOP-C | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 0a86f019-2294-37b7-8e2a-ef1891aa6d18 | -15.907 | -57.1782 | 2024-10-02 01:24:13 | METOP-C | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 97906b7a-3ca3-3882-9c75-a358918d7cf3 | -15.8956 | -57.1731 | 2024-10-02 01:24:13 | METOP-C | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 53747a76-c877-3c32-9795-698d525016c3 | -15.8972 | -57.180401 | 2024-10-02 01:24:13 | METOP-C | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 985f1c80-28ee-3e3e-9a08-2c0110bb06f8 | -15.8843 | -57.168098 | 2024-10-02 01:24:13 | METOP-C | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | nan |


[Clique aqui para ver as próximas entradas](README29.md)
