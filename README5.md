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
| 01afe65c-1723-3685-9434-783853104bb7 | -12.769 | -62.2678 | 2024-10-09 00:26:19 | GOES-16 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 96.7 |
| 662680ba-ada6-3b05-bcd2-0fe666acb5bd | -12.8589 | -62.8211 | 2024-10-09 00:26:20 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 91.9 |
| eee645af-5f38-3928-b182-3fdb213d0faf | -12.8591 | -62.8018 | 2024-10-09 00:26:20 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 244.7 |
| 56716f57-4c00-3861-9236-75e37cb738d6 | -12.8593 | -62.7826 | 2024-10-09 00:26:20 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 66.2 |
| ba1d0be5-a337-3097-8370-d579fdb35e66 | -12.8779 | -62.82 | 2024-10-09 00:26:20 | GOES-16 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 163.5 |
| f971542a-849b-3c5e-8c42-fab8b925badb | -12.878 | -62.8007 | 2024-10-09 00:26:20 | GOES-16 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 476.6 |
| 685c5d7c-1773-35db-920b-be87cb6dc3f1 | -12.8782 | -62.7815 | 2024-10-09 00:26:20 | GOES-16 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 90.4 |
| 72da53df-e20f-3d61-bf3e-8ac1417609ee | -12.9166 | -62.7214 | 2024-10-09 00:26:20 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 62.4 |
| f7f08daa-657b-3479-8a5b-a79f70c4f022 | -13.1475 | -62.3215 | 2024-10-09 00:26:21 | GOES-16 | ALTO ALEGRE DOS PARECIS | RONDÔNIA | Brasil | 1100379 | 11 | 33 | nan | nan | nan | Amazônia | 33.4 |
| 3a495727-38e5-3aed-9fe8-3cd28c03ac7e | -13.3065 | -53.7227 | 2024-10-09 00:26:21 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 77.5 |
| 552169d5-5bd2-376c-90a0-551e4edc744d | -13.8188 | -43.6026 | 2024-10-09 00:26:23 | GOES-16 | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 75.2 |
| 5cdf5ef4-5363-3694-99b2-b9c672b71ef4 | -13.8958 | -44.5351 | 2024-10-09 00:26:24 | GOES-16 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 50.7 |
| f4f4f7fa-9742-34b5-ad84-5ab04f47475d | -14.079 | -44.1483 | 2024-10-09 00:26:25 | GOES-16 | FEIRA DA MATA | BAHIA | Brasil | 2910776 | 29 | 33 | nan | nan | nan | Cerrado | 77.4 |
| 2080b178-d43c-32e7-ae85-714662dcd5ae | -15.6795 | -52.4993 | 2024-10-09 00:26:34 | GOES-16 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 63.0 |
| 2d42af83-49f4-38eb-91a7-6f9d622f470f | -15.688 | -59.3945 | 2024-10-09 00:26:35 | GOES-16 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 95.8 |
| bdd38d28-8b7d-32c8-874d-98ffdadcb136 | -15.6882 | -59.3745 | 2024-10-09 00:26:35 | GOES-16 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 85.4 |
| 13713467-e32f-398f-b3d6-c782b28285b7 | -15.7073 | -59.3926 | 2024-10-09 00:26:35 | GOES-16 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 96.6 |
| 002a814f-022c-37ca-97ad-ee6a9cc5ff19 | -15.7076 | -59.3726 | 2024-10-09 00:26:35 | GOES-16 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 145.7 |
| 6c451eee-dbe7-3700-91bd-39e66bf39b2a | -16.4187 | -55.9248 | 2024-10-09 00:26:39 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 117.9 |
| 7664ef94-e0b2-35bf-bffc-56ee10c3d69d | -16.4379 | -55.9431 | 2024-10-09 00:26:39 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 61.8 |
| 3b3eb951-9dd3-3c05-96cd-f16c855e5d3d | -16.4383 | -55.9224 | 2024-10-09 00:26:39 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 59.0 |
| 4027f5d1-3312-3dbb-b326-d98eb2a8fbfc | -16.3988 | -55.9479 | 2024-10-09 00:26:39 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 56.3 |
| 8e87303e-d243-38cb-95f5-8cac79fb41eb | -16.4184 | -55.9455 | 2024-10-09 00:26:39 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 149.3 |
| a0547c69-172a-3eba-9c25-96a5795fbad9 | -16.6723 | -57.1488 | 2024-10-09 00:26:40 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 66.0 |
| 0f96efc2-f24f-32f5-a5cd-f2cff2f31d7d | -16.7575 | -56.7081 | 2024-10-09 00:26:41 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 89.2 |
| db613286-0c6e-34a7-8189-ad423a972182 | -16.777 | -56.7057 | 2024-10-09 00:26:41 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 87.2 |
| a56c2af4-0176-3c33-af44-75c315652f12 | -16.8743 | -56.7352 | 2024-10-09 00:26:41 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 101.2 |
| a6d87b72-b6e8-30c1-b1bb-ae24acd776f1 | -16.8747 | -56.7146 | 2024-10-09 00:26:41 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 95.8 |
| 9117e3e4-d709-38f2-9e21-97db33d7c9d1 | -16.9094 | -55.8014 | 2024-10-09 00:26:41 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 55.8 |
| 8fd82875-7380-3ac9-b4dc-da0876204dcf | -16.9518 | -56.7875 | 2024-10-09 00:26:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 97.6 |
| 7845dd87-a6c4-3ae5-9c90-e4d5f2d56944 | -16.9603 | -57.4836 | 2024-10-09 00:26:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 126.5 |
| bd318939-7ee8-35f0-ae30-80158b506cfa | -16.9606 | -57.4631 | 2024-10-09 00:26:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 100.2 |
| f8b9292d-6765-36c3-987d-b2e28886ef38 | -16.9799 | -57.4813 | 2024-10-09 00:26:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 94.2 |
| df6549be-2486-3795-9d0f-cab6d917855e | -16.9802 | -57.4609 | 2024-10-09 00:26:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 63.1 |
| 3c5dde6e-dc72-3be1-819a-9a0b78549ebb | -17.0878 | -56.8534 | 2024-10-09 00:26:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 115.8 |
| 1bd8dfff-c932-33d1-ae6c-4d2f2ea6f459 | -17.1074 | -56.851 | 2024-10-09 00:26:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 101.8 |
| 9a492007-8b32-3fb5-88be-64d9c6f86996 | -17.1271 | -56.8486 | 2024-10-09 00:26:43 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 94.3 |
| 47e49ec7-8419-3c4b-838d-1fa9db811fec | -17.1467 | -56.8463 | 2024-10-09 00:26:43 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 97.0 |
| 0a337eaf-bb60-3ed4-8cb9-8790391538d3 | -17.1588 | -56.1222 | 2024-10-09 00:26:43 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 68.5 |
| 0bcd6b98-c56c-3c7f-8ba6-c1d98095f702 | -17.1977 | -57.333 | 2024-10-09 00:26:43 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 72.2 |
| c83f4901-ba5a-3aa9-a76c-c3695d02fb33 | -17.198 | -57.3125 | 2024-10-09 00:26:43 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 66.1 |
| 80900fdf-6888-3976-9741-fbbb23b40e49 | -17.2173 | -57.3307 | 2024-10-09 00:26:43 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 93.8 |
| bd53eca9-e32f-3c8e-ad9d-ef0674c36e43 | -17.3149 | -55.0603 | 2024-10-09 00:26:43 | GOES-16 | ITIQUIRA | MATO GROSSO | Brasil | 5104609 | 51 | 33 | nan | nan | nan | Pantanal | 52.2 |
| 0d5d44f3-d357-3593-aaa7-e705fa7c47db | -17.3353 | -55.0156 | 2024-10-09 00:26:43 | GOES-16 | ITIQUIRA | MATO GROSSO | Brasil | 5104609 | 51 | 33 | nan | nan | nan | Pantanal | 57.8 |
| bceeaa17-7897-3e12-8021-e6e45b6442ba | -18.5993 | -57.2629 | 2024-10-09 00:26:50 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 96.2 |
| 53a2fdea-51c4-34b1-bc11-ccbfd7fac554 | -18.5996 | -57.2422 | 2024-10-09 00:26:50 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 94.8 |
| 0d90653d-f0dd-359d-8bda-d35d7f79d3b5 | -19.831 | -42.3796 | 2024-10-09 00:26:55 | GOES-16 | CÓRREGO NOVO | MINAS GERAIS | Brasil | 3120003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 100.2 |
| caa6773c-1027-39ca-afb0-d1a45a253af2 | -19.9924 | -42.4346 | 2024-10-09 00:26:56 | GOES-16 | RAUL SOARES | MINAS GERAIS | Brasil | 3154002 | 31 | 33 | nan | nan | nan | Mata Atlântica | 137.8 |
| 7ef37c11-b95f-3ea2-aa44-13af26ac3ace | -20.013 | -42.4287 | 2024-10-09 00:26:56 | GOES-16 | RAUL SOARES | MINAS GERAIS | Brasil | 3154002 | 31 | 33 | nan | nan | nan | Mata Atlântica | 116.0 |
| 34489ca6-5bda-3ddd-86c4-0fc3ff6dcf92 | -20.1087 | -48.8261 | 2024-10-09 00:26:57 | GOES-16 | FRUTAL | MINAS GERAIS | Brasil | 3127107 | 31 | 33 | nan | nan | nan | Cerrado | 157.7 |
| 39a7f0fd-8ded-38c0-8034-63ba05fa48e6 | -20.1093 | -48.8031 | 2024-10-09 00:26:57 | GOES-16 | FRUTAL | MINAS GERAIS | Brasil | 3127107 | 31 | 33 | nan | nan | nan | Cerrado | 103.1 |
| 5a55cdad-b829-34fe-8718-2550cb9b37a8 | -20.3346 | -48.7307 | 2024-10-09 00:26:59 | GOES-16 | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 318.7 |
| db67c577-6f85-3979-9d00-09c066df4b37 | -20.3352 | -48.7076 | 2024-10-09 00:26:59 | GOES-16 | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 297.6 |
| 88b3b0d0-7067-3e2c-89de-6d108084dcc3 | -20.3551 | -48.7262 | 2024-10-09 00:26:59 | GOES-16 | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 724.6 |
| 25e7ae02-2985-3b4f-92ba-bf6afb50cc88 | -20.3557 | -48.7031 | 2024-10-09 00:26:59 | GOES-16 | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 469.7 |
| 38fc8a61-9136-37e7-bf8c-071686c3a89b | -20.3755 | -48.7217 | 2024-10-09 00:26:59 | GOES-16 | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Cerrado | 212.6 |
| 9ce31cd7-a3e2-3dab-8b65-88476da92359 | -20.3761 | -48.6986 | 2024-10-09 00:26:59 | GOES-16 | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Cerrado | 130.2 |
| 90ce7fdf-7625-3f67-b968-bbfc8a45e817 | -20.5559 | -43.3515 | 2024-10-09 00:26:59 | GOES-16 | PIRANGA | MINAS GERAIS | Brasil | 3150802 | 31 | 33 | nan | nan | nan | Mata Atlântica | 132.0 |
| 33028790-f86a-3097-9df5-d8720fd1012c | -20.5766 | -43.3457 | 2024-10-09 00:26:59 | GOES-16 | PIRANGA | MINAS GERAIS | Brasil | 3150802 | 31 | 33 | nan | nan | nan | Mata Atlântica | 134.7 |
| f805c0b6-da25-388a-8f61-4f65b11be651 | -20.7839 | -47.2559 | 2024-10-09 00:27:01 | GOES-16 | PATROCÍNIO PAULISTA | SÃO PAULO | Brasil | 3536307 | 35 | 33 | nan | nan | nan | Cerrado | 203.8 |
| a7e63e45-b693-3c5a-b022-3ef10633b1f9 | -20.7846 | -47.2323 | 2024-10-09 00:27:01 | GOES-16 | PATROCÍNIO PAULISTA | SÃO PAULO | Brasil | 3536307 | 35 | 33 | nan | nan | nan | Cerrado | 235.7 |
| 0e40d883-aac8-3e39-908f-7fb8186da318 | -20.8045 | -47.251 | 2024-10-09 00:27:01 | GOES-16 | PATROCÍNIO PAULISTA | SÃO PAULO | Brasil | 3536307 | 35 | 33 | nan | nan | nan | Cerrado | 125.4 |
| 6692369c-8c63-32ee-94c2-143b52156b14 | -20.8052 | -47.2273 | 2024-10-09 00:27:01 | GOES-16 | PATROCÍNIO PAULISTA | SÃO PAULO | Brasil | 3536307 | 35 | 33 | nan | nan | nan | Cerrado | 150.1 |
| e3068910-40a6-3a76-8312-0f64af05259a | -21.5512 | -46.9951 | 2024-10-09 00:27:05 | GOES-16 | MOCOCA | SÃO PAULO | Brasil | 3530508 | 35 | 33 | nan | nan | nan | Cerrado | 68.1 |
| 4ab5dcab-28a9-3f5b-98a9-10629c345de0 | -21.552 | -46.9712 | 2024-10-09 00:27:05 | GOES-16 | MOCOCA | SÃO PAULO | Brasil | 3530508 | 35 | 33 | nan | nan | nan | Cerrado | 90.1 |
| afb1d6c3-8bd2-38ed-bb56-c23ebb8ddd6c | -21.572 | -46.9898 | 2024-10-09 00:27:05 | GOES-16 | MOCOCA | SÃO PAULO | Brasil | 3530508 | 35 | 33 | nan | nan | nan | Cerrado | 112.6 |
| 257085ea-0802-3aff-b81e-cfdc958ce4d1 | -21.5727 | -46.9659 | 2024-10-09 00:27:05 | GOES-16 | MOCOCA | SÃO PAULO | Brasil | 3530508 | 35 | 33 | nan | nan | nan | Cerrado | 153.5 |
| e5055aa6-2083-329f-b6b8-7d836d239bb2 | -21.5649 | -47.9114 | 2024-10-09 00:27:05 | GOES-16 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 113.1 |
| 6dd75457-5cab-3a0b-b554-f1acc3bfa916 | -21.5656 | -47.8878 | 2024-10-09 00:27:05 | GOES-16 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 116.1 |
| 8778276b-f401-31e1-bedd-4144f8c42caa | -21.5857 | -47.9063 | 2024-10-09 00:27:05 | GOES-16 | RINCÃO | SÃO PAULO | Brasil | 3543709 | 35 | 33 | nan | nan | nan | Cerrado | 143.9 |
| 5ad00be7-668d-3edd-96b0-f39ae307f547 | -21.5864 | -47.8827 | 2024-10-09 00:27:05 | GOES-16 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 174.2 |
| 89e18754-86f6-386c-913e-4eccab20561e | -21.5871 | -47.8591 | 2024-10-09 00:27:05 | GOES-16 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 76.9 |
| e34002b7-f884-318e-a464-0fc54ad2ae74 | -21.8165 | -49.1774 | 2024-10-09 00:27:06 | GOES-16 | REGINÓPOLIS | SÃO PAULO | Brasil | 3542503 | 35 | 33 | nan | nan | nan | Mata Atlântica | 96.1 |
| c7ff311d-aaed-312c-9b08-0f35e4cee11a | -21.8172 | -49.1541 | 2024-10-09 00:27:06 | GOES-16 | REGINÓPOLIS | SÃO PAULO | Brasil | 3542503 | 35 | 33 | nan | nan | nan | Mata Atlântica | 102.5 |
| 974d9392-243c-37ff-b860-7a1be8b767b2 | -21.8373 | -49.1726 | 2024-10-09 00:27:06 | GOES-16 | REGINÓPOLIS | SÃO PAULO | Brasil | 3542503 | 35 | 33 | nan | nan | nan | Mata Atlântica | 129.0 |
| 1db13ff5-0ad4-3418-bddf-7e4de8007140 | -21.838 | -49.1493 | 2024-10-09 00:27:06 | GOES-16 | IACANGA | SÃO PAULO | Brasil | 3519105 | 35 | 33 | nan | nan | nan | Mata Atlântica | 138.3 |
| 7f478441-cb1d-3489-8201-2bc5c88a753b | -22.813 | -48.4462 | 2024-10-09 00:27:11 | GOES-16 | BOTUCATU | SÃO PAULO | Brasil | 3507506 | 35 | 33 | nan | nan | nan | Cerrado | 74.8 |
| 4a3082f8-e627-3008-b705-f58a1a60c8b3 | -22.8137 | -48.4225 | 2024-10-09 00:27:11 | GOES-16 | BOTUCATU | SÃO PAULO | Brasil | 3507506 | 35 | 33 | nan | nan | nan | Cerrado | 98.6 |
| e0010e43-7f55-3b55-8fef-0dc5a6420166 | -22.8347 | -48.4171 | 2024-10-09 00:27:11 | GOES-16 | BOTUCATU | SÃO PAULO | Brasil | 3507506 | 35 | 33 | nan | nan | nan | Cerrado | 70.2 |
| 55c2fc05-eb2f-36fc-bd31-278ccce44343 | -1.11 | -53.6173 | 2024-10-09 00:35:12 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 118.1 |
| 201fc168-870c-3c3c-a813-8afb8a7e1aaa | -1.1284 | -53.6171 | 2024-10-09 00:35:12 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 50.9 |
| 10d2a0dd-0c86-3ba4-b913-8863920708d4 | -1.9609 | -50.8404 | 2024-10-09 00:35:17 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 22.2 |
| 159a1528-6920-370b-b6b2-5779d31f87ef | -3.8007 | -41.6229 | 2024-10-09 00:35:27 | GOES-16 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 55.3 |
| 77e5d963-67fa-367f-abc7-40f4461a7733 | -3.8008 | -41.5989 | 2024-10-09 00:35:27 | GOES-16 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 68.1 |
| d28f28d0-4512-3516-a162-79724a8b8772 | -3.8196 | -41.5979 | 2024-10-09 00:35:28 | GOES-16 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 68.5 |
| b733158d-7bae-33f9-b01b-5eb7f1868a79 | -3.9021 | -46.4689 | 2024-10-09 00:35:28 | GOES-16 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 93.5 |
| a4343e2b-702b-3670-84ca-49ae06b76776 | -3.9023 | -46.4467 | 2024-10-09 00:35:28 | GOES-16 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 106.1 |
| cadbe61c-4a4c-3d1a-a324-01e3dc22e98e | -3.9207 | -46.468 | 2024-10-09 00:35:28 | GOES-16 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 59.0 |
| 067d554c-d546-3f7e-b6dd-51b53299d4fc | -3.9208 | -46.4459 | 2024-10-09 00:35:28 | GOES-16 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 102.8 |
| 277f7215-c864-355b-b8f2-d9aee0486ac6 | -3.9393 | -46.4672 | 2024-10-09 00:35:28 | GOES-16 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 54.2 |
| 86ce1e8a-4396-3d4f-ad74-4c0809ab9667 | -3.9394 | -46.445 | 2024-10-09 00:35:28 | GOES-16 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 99.8 |
| 8cb83218-e45b-3b83-b016-88267b04b73c | -5.2253 | -43.8164 | 2024-10-09 00:35:36 | GOES-16 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 64.0 |
| c3a30c94-5096-3bfe-9505-0ac69b188e20 | -5.4421 | -49.5559 | 2024-10-09 00:35:37 | GOES-16 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 70.5 |
| 5bb1366b-5d72-3b5c-89d8-770ea68225b8 | -5.8216 | -44.1196 | 2024-10-09 00:35:39 | GOES-16 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 58.9 |
| 495b1b48-f2f3-3bfb-8d4e-bdd96f7d5a3a | -6.7613 | -60.0751 | 2024-10-09 00:35:45 | GOES-16 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 28.5 |
| 65d08b33-0780-35e1-aa84-ca970a0a8454 | -6.7614 | -60.0559 | 2024-10-09 00:35:45 | GOES-16 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 144.8 |
| ac23b2c5-34ff-37fe-a1e9-30737ef698ce | -6.7615 | -60.0367 | 2024-10-09 00:35:45 | GOES-16 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 65.5 |
| 1ed874c7-d681-34eb-a1ec-d5e831ca79e0 | -6.7797 | -60.0744 | 2024-10-09 00:35:45 | GOES-16 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 31.6 |
| e5f43238-d5ef-3de5-b706-9ed9a69d63cc | -6.7798 | -60.0552 | 2024-10-09 00:35:45 | GOES-16 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 198.3 |
| 8c06a466-4fd2-3229-8e1b-aeb2ce4751f1 | -6.7799 | -60.036 | 2024-10-09 00:35:45 | GOES-16 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 96.9 |


[Clique aqui para ver as próximas entradas](README6.md)
