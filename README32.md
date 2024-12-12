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

## Dados Diários - Página 32

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| e1ec36b8-4f8d-3bff-8949-be2becc81e76 | -14.75487 | -52.65962 | 2024-12-12 05:03:00 | NOAA-20 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 5.6 |
| f917a06c-4db3-338f-af33-6d68a3a5651b | -12.5393 | -57.72462 | 2024-12-12 05:03:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 8ee0e360-7f0c-3248-a452-c505622daa24 | -11.21162 | -53.83233 | 2024-12-12 05:03:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| a3670330-5624-3f90-83ad-f04b466abdda | -15.07826 | -59.62614 | 2024-12-12 05:03:00 | NOAA-20 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 57108644-673b-36d8-8536-2d1f1c740988 | -15.09069 | -59.63624 | 2024-12-12 05:03:00 | NOAA-20 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| f4d8b133-93fb-3c61-b6e1-c9dd3fd706fa | -11.43124 | -55.91779 | 2024-12-12 05:03:00 | NOAA-20 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 360b9f7b-5e9a-3f34-990e-e563d6ee2acf | -11.65166 | -58.27291 | 2024-12-12 05:03:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6b0c3330-d8f1-3926-99d0-9ceb789e66a3 | -13.26568 | -57.38625 | 2024-12-12 05:03:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 7cf9d34d-aebd-36ce-9375-e9def87bcb2b | -15.02945 | -57.61453 | 2024-12-12 05:03:00 | NOAA-20 | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 616c77e3-92c1-3469-ad76-2ea3158ee129 | -11.65106 | -58.27657 | 2024-12-12 05:03:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 77fcd05e-4738-39f5-9916-4c39030460aa | -15.08232 | -59.6229 | 2024-12-12 05:03:00 | NOAA-20 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 7a616c7c-3afa-39fa-b7c9-93077577d3f4 | -11.20035 | -53.83477 | 2024-12-12 05:03:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 5afda892-e61c-36ca-a0b4-ecb8e98a6b30 | -12.53703 | -57.73881 | 2024-12-12 05:03:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 12.0 |
| 906587ce-6811-33a9-9b01-03a5427add30 | -11.1974 | -53.83011 | 2024-12-12 05:03:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 60536399-509e-3d6d-a67a-dfcc8b7cb19d | -11.11791 | -54.64593 | 2024-12-12 05:03:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 0ee8d38f-4ba4-39c4-8ca6-c994a64310df | -16.18335 | -58.17733 | 2024-12-12 05:03:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 0.7 |
| cd43ba65-091a-3807-a13f-674bcc2718fa | -13.26899 | -57.3868 | 2024-12-12 05:03:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 84c37090-fed3-35e6-af8a-c0b3d50f5284 | -11.64829 | -58.27235 | 2024-12-12 05:03:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| dd6ca046-c4ed-3173-9eca-a15b50d20068 | -13.69133 | -54.76499 | 2024-12-12 05:03:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 6.4 |
| a5202e46-4326-35af-a3dc-a43c8c87dd3f | -11.11676 | -54.65349 | 2024-12-12 05:03:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 92c1479a-41af-3639-b433-f6929eab4b96 | -15.02283 | -57.61343 | 2024-12-12 05:03:00 | NOAA-20 | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 16deae75-93cf-3cad-a803-49f68cc8a19e | -14.7538 | -52.6558 | 2024-12-12 05:03:00 | NOAA-20 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 4.6 |
| a9b93ea4-7a41-3a1e-88d2-fbd3f05b2fc8 | -14.75845 | -52.65125 | 2024-12-12 05:03:00 | NOAA-20 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 5.3 |
| d970f339-68b7-3897-a87d-1fdad759cdc5 | -14.75308 | -52.64333 | 2024-12-12 05:03:00 | NOAA-20 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 7763bbd2-c156-3556-b985-f0768e3ab023 | -12.56355 | -57.76513 | 2024-12-12 05:03:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 3a956485-772c-3787-ad35-8a6f67eebce3 | -11.20095 | -53.83067 | 2024-12-12 05:03:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 5.7 |
| b0acc217-e16b-31a7-bd1a-25522346dc0b | -14.91317 | -52.87134 | 2024-12-12 05:03:00 | NOAA-20 | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 4c5242cb-6dca-3ed9-bc26-48fd80dc6574 | -15.02227 | -57.61699 | 2024-12-12 05:03:00 | NOAA-20 | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6654a013-b128-3a88-8f09-f277d6ab7df9 | -13.69424 | -54.76953 | 2024-12-12 05:03:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 6.4 |
| ca5562ad-ede4-36c1-a0f7-ea88a7b93408 | -13.69543 | -54.76152 | 2024-12-12 05:03:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 69fb4786-dbe7-396d-ae42-29358ee6d427 | -11.198 | -53.826 | 2024-12-12 05:03:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 41d60f25-c0de-3dc2-9703-4ef29ccd82c5 | -12.91415 | -55.04843 | 2024-12-12 05:03:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 238bf54c-616f-3191-ac5b-8c2f00ba7291 | -15.07571 | -59.64151 | 2024-12-12 05:03:00 | NOAA-20 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 5818282f-aaad-3a94-a8cc-84d8520086ba | -16.87764 | -57.51463 | 2024-12-12 05:03:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.3 |
| 0a1a82fb-3670-3dec-9ccf-80fdad25652c | -14.6054 | -57.71983 | 2024-12-12 05:03:00 | NOAA-20 | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 97a6f869-c1c2-38bb-9a92-259ed91f176d | -12.91646 | -55.05661 | 2024-12-12 05:03:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7e68e52e-38bf-3655-86cd-03a831889ab4 | -18.48639 | -54.51792 | 2024-12-12 05:03:00 | NOAA-20 | COXIM | MATO GROSSO DO SUL | Brasil | 5003306 | 50 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 2c1fed6e-1ec8-3954-9b44-a92adf512709 | -15.44379 | -57.82952 | 2024-12-12 05:03:00 | NOAA-20 | LAMBARI D'OESTE | MATO GROSSO | Brasil | 5105234 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 8ea14614-8ac8-3b44-9b0f-fd165d31bb8f | -15.07914 | -59.64211 | 2024-12-12 05:03:00 | NOAA-20 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 09a4288c-9acc-3a3b-bb8c-534844edd070 | -14.74765 | -52.65329 | 2024-12-12 05:03:00 | NOAA-20 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 393e27fd-071d-3509-a65a-f93266b4b0a8 | -14.75311 | -52.66101 | 2024-12-12 05:03:00 | NOAA-20 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 4.6 |
| e7818a51-f529-303b-bcac-1db7c2266b71 | -14.74619 | -52.66381 | 2024-12-12 05:03:00 | NOAA-20 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 80f645e1-8f72-3d2c-989f-48fbcb9d08fe | -11.20277 | -53.81836 | 2024-12-12 05:03:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 6.0 |
| e77de81d-db38-3dd6-a33f-78867e505d5b | -12.91816 | -55.04514 | 2024-12-12 05:03:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 832a1c5d-8b62-32e4-a463-4b8d85d3a12f | -12.40331 | -49.68168 | 2024-12-12 05:03:00 | NOAA-20 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c4cea8b7-f783-3313-be9f-1b658e7f069a | -10.52112 | -58.81105 | 2024-12-12 05:03:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 88946f92-c0a7-38ee-8aac-f0d7729d1a6a | -15.08448 | -59.63116 | 2024-12-12 05:03:00 | NOAA-20 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 74c05519-3a59-317a-a600-000bc5a3ccfb | -15.96585 | -57.15813 | 2024-12-12 05:03:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| f02d7f6b-b8f6-3c5e-85d1-de35b6478842 | -15.06693 | -59.65184 | 2024-12-12 05:03:00 | NOAA-20 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 7e8a4f01-b978-3ce7-99a5-f1fd8806bc47 | -15.92233 | -59.80632 | 2024-12-12 05:03:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| ec066043-614b-35af-9aa5-d2792c861ec0 | -12.91759 | -55.04897 | 2024-12-12 05:03:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 10fdd772-c446-3d87-8877-59e347341762 | -11.10988 | -54.65245 | 2024-12-12 05:03:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 3073e769-9b89-3a18-9cea-cdccc060edbf | -11.20156 | -53.82657 | 2024-12-12 05:03:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 5.7 |
| bb38c1ea-87aa-32cf-99ed-f0c4b95146b4 | -14.75519 | -52.64529 | 2024-12-12 05:03:00 | NOAA-20 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 5.3 |
| c6674f02-e7c9-36be-998e-a9814966b47e | -15.09221 | -59.6484 | 2024-12-12 05:03:00 | NOAA-20 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 22b3db3d-de91-3173-bb6c-67738c6abef0 | -15.92511 | -59.81076 | 2024-12-12 05:03:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 4009845d-a535-3161-8b9e-93dad56433cb | -15.07977 | -59.63826 | 2024-12-12 05:03:00 | NOAA-20 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 3d395d1d-738b-317c-8cd8-43a406a8b26a | -14.74659 | -52.6316 | 2024-12-12 05:03:00 | NOAA-20 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 22557bd9-a5cc-3fa9-8466-643f76a390e8 | -14.75884 | -52.66018 | 2024-12-12 05:03:00 | NOAA-20 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| e822721d-20a7-3206-88dc-a9fbf50aa5d1 | -12.57077 | -57.76268 | 2024-12-12 05:03:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 386305fe-81a4-39b4-86de-2f34a05a39ae | -12.56687 | -57.76568 | 2024-12-12 05:03:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 9d3fe227-f919-3d3d-b9d6-ecc5f9ae499a | -15.0267 | -57.61042 | 2024-12-12 05:03:00 | NOAA-20 | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 5990505d-7ae5-39ec-b13a-eed4eb42fd3c | -15.08511 | -59.62732 | 2024-12-12 05:03:00 | NOAA-20 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 6f87c55c-1401-3e5a-aabb-07ecf1ce5249 | -12.55284 | -58.35838 | 2024-12-12 05:03:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 24b0ea28-8c6f-3efe-8887-f03e7a9ffe14 | -11.11504 | -54.64162 | 2024-12-12 05:03:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 1d9f1556-3f0c-311b-8064-dadb8ac172b8 | -14.75709 | -52.66154 | 2024-12-12 05:03:00 | NOAA-20 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 24b6710e-355a-326a-9690-75a666cc02b8 | -15.24318 | -59.92163 | 2024-12-12 05:03:00 | NOAA-20 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 4b1f5553-2b3e-3973-8c60-2a13c59fd428 | -11.11733 | -54.64971 | 2024-12-12 05:03:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 08c79379-c0d3-357d-87ff-52a437758521 | -15.07379 | -59.65304 | 2024-12-12 05:03:00 | NOAA-20 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f5c727b4-d836-3112-98d4-60651195406b | -12.91823 | -55.72564 | 2024-12-12 05:03:00 | NOAA-20 | SORRISO | MATO GROSSO | Brasil | 5107925 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 740e2e2f-14a5-3bbc-9441-ac64097561c4 | -15.96197 | -57.16119 | 2024-12-12 05:03:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| bbb643d0-d80d-327d-9937-68c3d736dd51 | -12.56744 | -57.76213 | 2024-12-12 05:03:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| fdbc946d-01be-3998-8ce7-6b303c35bf0e | -11.11332 | -54.65297 | 2024-12-12 05:03:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 0b87ba93-7a44-38f1-9b5c-96b531d50dac | -12.56412 | -57.76157 | 2024-12-12 05:03:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 238cfad5-362b-35ad-a1bb-01a1872522b7 | -14.75017 | -52.66433 | 2024-12-12 05:03:00 | NOAA-20 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 7701e58b-2428-300a-8c35-50546f503433 | -11.20928 | -53.82359 | 2024-12-12 05:03:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| ca564c35-b6fa-3c1f-838d-851d19b53bae | -13.06147 | -52.04375 | 2024-12-12 05:03:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| dd9f55ce-dc3b-36fa-aeb8-8ebcd77d5b47 | -12.9216 | -55.04568 | 2024-12-12 05:03:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| a9ef5783-34c2-39cd-b4aa-c502da93b05a | -12.91712 | -55.73298 | 2024-12-12 05:03:00 | NOAA-20 | SORRISO | MATO GROSSO | Brasil | 5107925 | 51 | 33 | nan | nan | nan | Cerrado | 3.2 |
| ddceb1cb-785a-39ed-a65c-62a144d3f08e | -12.5582 | -57.71315 | 2024-12-12 05:03:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1cbb3283-6124-3053-9390-0218e63cae1c | -11.20512 | -53.82713 | 2024-12-12 05:03:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 4e397f70-f3f0-325d-bc79-45197fbcc659 | -15.47757 | -58.8036 | 2024-12-12 05:03:00 | NOAA-20 | FIGUEIRÓPOLIS D'OESTE | MATO GROSSO | Brasil | 5103809 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0eb85d0b-8fa4-3099-9352-169e9eeb4d62 | -11.65226 | -58.26925 | 2024-12-12 05:03:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 75b3fc19-7f90-3c95-a5f5-1eb7d57a91d5 | -11.11389 | -54.64919 | 2024-12-12 05:03:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 6a186216-64e2-3531-a4e5-54d1a3fe13a7 | -15.09006 | -59.64009 | 2024-12-12 05:03:00 | NOAA-20 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 7.6 |
| fc3f9bea-7274-3f73-b222-4bb6f4958b4f | -11.20217 | -53.82247 | 2024-12-12 05:03:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 6.0 |
| c7899403-3a62-3031-9219-e2a14b4429f9 | -18.53299 | -56.17048 | 2024-12-12 05:03:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.4 |
| 0b7816d3-27da-3d29-92ca-d1f522dbcc48 | -11.42791 | -55.91726 | 2024-12-12 05:03:00 | NOAA-20 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 1e766c8d-838a-309e-8721-a8c637d3e298 | -14.75235 | -52.64861 | 2024-12-12 05:03:00 | NOAA-20 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 87be4d89-802d-3782-b68d-db6e196155c4 | -14.74513 | -52.64219 | 2024-12-12 05:03:00 | NOAA-20 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 409811b9-36b0-380f-ab0b-78851699bd17 | -15.12078 | -57.68078 | 2024-12-12 05:03:00 | NOAA-20 | SALTO DO CÉU | MATO GROSSO | Brasil | 5107750 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c71d9b38-b7ec-36c1-a156-1d2f0bdf8a07 | -11.20867 | -53.82769 | 2024-12-12 05:03:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 8b7dad22-0314-3806-a4e3-860ccd44fcbb | -21.7915 | -55.98893 | 2024-12-12 05:05:00 | NOAA-20 | JARDIM | MATO GROSSO DO SUL | Brasil | 5005004 | 50 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f9bbbd3c-9b65-3ce8-8328-a1ea00fc051d | -21.7879 | -55.98834 | 2024-12-12 05:05:00 | NOAA-20 | JARDIM | MATO GROSSO DO SUL | Brasil | 5005004 | 50 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 6eba6c37-a5da-3897-aa23-18d8c29be952 | -20.72917 | -54.42305 | 2024-12-12 05:05:00 | NOAA-20 | CAMPO GRANDE | MATO GROSSO DO SUL | Brasil | 5002704 | 50 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 9d49c32f-8472-3543-bec1-124a742bd6f0 | -20.47787 | -53.67576 | 2024-12-12 05:05:00 | NOAA-20 | RIBAS DO RIO PARDO | MATO GROSSO DO SUL | Brasil | 5007109 | 50 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 59b06d6c-b04a-3de1-bbe1-c3802419b603 | -31.02798 | -50.79174 | 2024-12-12 05:08:00 | NOAA-20 | MOSTARDAS | RIO GRANDE DO SUL | Brasil | 4312500 | 43 | 33 | nan | nan | nan | Pampa | 0.5 |
| 907d9186-7731-395f-815b-49d87c25b0ff | -29.62971 | -51.96829 | 2024-12-12 05:08:00 | NOAA-20 | CRUZEIRO DO SUL | RIO GRANDE DO SUL | Brasil | 4306205 | 43 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| ef96e16a-0581-3a93-b9f1-2afca39510a6 | -31.02829 | -50.78763 | 2024-12-12 05:08:00 | NOAA-20 | MOSTARDAS | RIO GRANDE DO SUL | Brasil | 4312500 | 43 | 33 | nan | nan | nan | Pampa | 0.5 |
| 0c31cee7-8ac5-3a53-8dcd-388cf650984a | -12.5682 | -57.7579 | 2024-12-12 05:10:00 | GOES-16 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 48.4 |


[Clique aqui para ver as próximas entradas](README33.md)
