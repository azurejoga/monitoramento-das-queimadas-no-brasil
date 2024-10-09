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

## Dados Diários - Página 2

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 37cbcfba-1416-3389-9968-5c32782e0857 | -12.9756 | -62.4673 | 2024-10-09 00:06:20 | GOES-16 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 108.9 |
| 7c207bcf-2140-390a-a9b4-f63114a26eb5 | -12.9757 | -62.448 | 2024-10-09 00:06:20 | GOES-16 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 45.8 |
| ac3f9cf1-22b7-3faf-9058-67e7d3dc2bd3 | -12.9945 | -62.4662 | 2024-10-09 00:06:20 | GOES-16 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 70.0 |
| c7757484-21d8-3491-a588-7630da74a2d8 | -13.1475 | -62.3215 | 2024-10-09 00:06:21 | GOES-16 | ALTO ALEGRE DOS PARECIS | RONDÔNIA | Brasil | 1100379 | 11 | 33 | nan | nan | nan | Amazônia | 47.0 |
| d7eb5618-a5c6-35f2-994e-d47ab8543882 | -13.3065 | -53.7227 | 2024-10-09 00:06:21 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 74.1 |
| f904cec0-ded7-3220-852a-f32a30de21e9 | -13.3978 | -61.9376 | 2024-10-09 00:06:23 | GOES-16 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 128.0 |
| 910d757d-696a-3247-a669-00ef05065c73 | -13.398 | -61.9182 | 2024-10-09 00:06:23 | GOES-16 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 138.2 |
| 3cd6d659-152a-3f98-a19c-be980e789be2 | -13.417 | -61.9169 | 2024-10-09 00:06:23 | GOES-16 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 114.8 |
| ff17e1c8-838e-35cd-bbac-c6c812a1c26f | -13.9014 | -44.2752 | 2024-10-09 00:06:24 | GOES-16 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 81.0 |
| 6fe79f88-ff11-34b1-acc3-41865b678dd4 | -13.9153 | -44.5317 | 2024-10-09 00:06:24 | GOES-16 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 86.0 |
| 4f713295-ad40-3f5c-a1ba-ccd8a9e9ffc3 | -13.9343 | -44.5518 | 2024-10-09 00:06:24 | GOES-16 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 81.4 |
| b18a579e-a7a9-3da6-a049-886040ab9247 | -13.9348 | -44.5282 | 2024-10-09 00:06:24 | GOES-16 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 89.0 |
| 5121ca90-c2a6-3843-a22a-07693acccbd2 | -14.079 | -44.1483 | 2024-10-09 00:06:25 | GOES-16 | FEIRA DA MATA | BAHIA | Brasil | 2910776 | 29 | 33 | nan | nan | nan | Cerrado | 92.5 |
| c573d5b9-0a69-30a7-a933-c5e93d06e2c2 | -14.1862 | -45.4872 | 2024-10-09 00:06:25 | GOES-16 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 73.0 |
| be84c25f-462f-3a74-bfec-15eebf5c6346 | -15.6795 | -52.4993 | 2024-10-09 00:06:34 | GOES-16 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 80.7 |
| 953cfecd-76ed-31dd-a635-9efe3c9aeeed | -15.6683 | -59.4163 | 2024-10-09 00:06:35 | GOES-16 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 74.3 |
| 7bfad1f5-7f76-3c0d-9d14-e6e0ee7f667f | -15.688 | -59.3945 | 2024-10-09 00:06:35 | GOES-16 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 99.6 |
| 076b33b4-52ae-3958-92ee-2bf3be2f3da0 | -15.6882 | -59.3745 | 2024-10-09 00:06:35 | GOES-16 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 79.3 |
| 6fdaceb3-b6d4-3ca6-b2af-cdb4300c6a69 | -15.7073 | -59.3926 | 2024-10-09 00:06:35 | GOES-16 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 114.5 |
| 4fe6f322-3c59-338f-a9e4-0d49eb053ad4 | -15.7076 | -59.3726 | 2024-10-09 00:06:35 | GOES-16 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 140.6 |
| 2f945d10-551b-398a-aff5-d0bd1db25d2b | -16.3988 | -55.9479 | 2024-10-09 00:06:39 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 60.4 |
| d3ea3e02-cd83-3904-bb64-81f550096a4f | -16.4184 | -55.9455 | 2024-10-09 00:06:39 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 170.9 |
| b89de30a-8189-32f1-b4ae-63a1d5b5253f | -16.4187 | -55.9248 | 2024-10-09 00:06:39 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 148.9 |
| 8f9b438d-2639-390b-9985-752dbd6b1962 | -16.4379 | -55.9431 | 2024-10-09 00:06:39 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 69.5 |
| 131b7c32-c00d-33f7-9a3b-7eda85079798 | -16.4383 | -55.9224 | 2024-10-09 00:06:39 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 69.6 |
| d69fd05a-eeb1-3de2-a64a-fd406cdfe906 | -16.6143 | -57.1145 | 2024-10-09 00:06:40 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 68.1 |
| 54e66636-5da4-3cd9-a96a-b332e9810585 | -16.6338 | -57.1123 | 2024-10-09 00:06:40 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 47.8 |
| cc14a49c-552f-3fdb-bb4e-c4695df580c5 | -16.7575 | -56.7081 | 2024-10-09 00:06:41 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 94.6 |
| f527da15-c219-3906-9137-6b06a411e9ac | -16.8048 | -57.4197 | 2024-10-09 00:06:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 63.4 |
| 3e790749-a986-358c-95e4-01d6ee219ef8 | -16.8244 | -57.4175 | 2024-10-09 00:06:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 74.3 |
| 8a618bb0-4d87-35be-aa4f-7974ac53f71e | -16.8743 | -56.7352 | 2024-10-09 00:06:41 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 111.1 |
| 13ed91fb-d03d-39cb-a70d-6b18f56fab07 | -16.8747 | -56.7146 | 2024-10-09 00:06:41 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 109.7 |
| 75ebe02c-a7ea-332d-9bf4-b10aa1788435 | -16.8898 | -55.8039 | 2024-10-09 00:06:41 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 122.3 |
| 798698c7-1a84-327c-b4f2-c8ca286fe14f | -16.8901 | -55.7831 | 2024-10-09 00:06:41 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 114.8 |
| d8a38b38-f3f2-3afa-918a-d3e5c8575f24 | -16.9091 | -55.8222 | 2024-10-09 00:06:41 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 66.9 |
| 6a8fbaa5-696a-3400-a8d9-237f100ba888 | -16.9094 | -55.8014 | 2024-10-09 00:06:41 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 185.1 |
| 7d92b074-7617-3954-b3b9-a234cb18f8a9 | -16.9098 | -55.7806 | 2024-10-09 00:06:41 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 129.7 |
| 471e448c-c008-3fe4-9d39-d4fc1d5fb87d | -16.929 | -55.7989 | 2024-10-09 00:06:41 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 50.1 |
| 92346a30-9b2d-3668-90d7-0b942750cbc3 | -16.9518 | -56.7875 | 2024-10-09 00:06:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 116.1 |
| 2a3c1db7-2150-3943-8c0e-1920922012e7 | -16.9521 | -56.7669 | 2024-10-09 00:06:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 95.3 |
| ef57481c-bd31-3a0a-8084-5fb5610720ee | -17.0875 | -56.874 | 2024-10-09 00:06:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 81.1 |
| 07976200-d0ef-3750-bef1-f28913dd5235 | -17.0878 | -56.8534 | 2024-10-09 00:06:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 134.5 |
| d35a5f00-a685-354f-8464-1243e43e632f | -17.1074 | -56.851 | 2024-10-09 00:06:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 113.8 |
| 201ce8cb-964e-3ca8-8f43-04ae9423a539 | -17.1271 | -56.8486 | 2024-10-09 00:06:43 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 99.1 |
| 384456be-279b-3e35-941b-dbc66c7a1b6a | -17.1467 | -56.8463 | 2024-10-09 00:06:43 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 94.4 |
| baff769f-8602-33c1-9469-904e6f71f7e8 | -17.649 | -53.0419 | 2024-10-09 00:06:45 | GOES-16 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 97.6 |
| 185f66b5-9bc7-3700-a8ef-80158ef46bfa | -17.6494 | -53.0204 | 2024-10-09 00:06:45 | GOES-16 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 107.2 |
| a9e464c8-76ed-381e-b0b1-158b5041febd | -17.7526 | -53.7948 | 2024-10-09 00:06:46 | GOES-16 | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | 157.8 |
| dbe59c6e-a6e4-3794-b946-a31977f02295 | -17.753 | -53.7735 | 2024-10-09 00:06:46 | GOES-16 | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | 153.7 |
| a93c08ee-cd59-31da-9922-5eda146706a2 | -18.5993 | -57.2629 | 2024-10-09 00:06:50 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 102.2 |
| 4fcca2b2-aecd-357f-a63a-3caabf11968b | -18.5996 | -57.2422 | 2024-10-09 00:06:50 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 103.0 |
| 33a7ad96-b63b-31d9-af72-705d9cc60b35 | -19.831 | -42.3796 | 2024-10-09 00:06:55 | GOES-16 | CÓRREGO NOVO | MINAS GERAIS | Brasil | 3120003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 93.6 |
| 4d663c3f-adfc-3d45-9672-a2baf81c5faf | -19.9916 | -42.46 | 2024-10-09 00:06:56 | GOES-16 | RAUL SOARES | MINAS GERAIS | Brasil | 3154002 | 31 | 33 | nan | nan | nan | Mata Atlântica | 121.4 |
| e00c4886-441b-38d7-97e6-f655c095b4ec | -19.9924 | -42.4346 | 2024-10-09 00:06:56 | GOES-16 | RAUL SOARES | MINAS GERAIS | Brasil | 3154002 | 31 | 33 | nan | nan | nan | Mata Atlântica | 214.9 |
| 01191f27-a4b7-378b-9f69-38bae31d449c | -20.0122 | -42.4541 | 2024-10-09 00:06:56 | GOES-16 | RAUL SOARES | MINAS GERAIS | Brasil | 3154002 | 31 | 33 | nan | nan | nan | Mata Atlântica | 109.3 |
| cb1b5a94-9a2e-3126-bf50-db560e791c7c | -20.013 | -42.4287 | 2024-10-09 00:06:56 | GOES-16 | RAUL SOARES | MINAS GERAIS | Brasil | 3154002 | 31 | 33 | nan | nan | nan | Mata Atlântica | 155.9 |
| ffce4f0f-6dbf-3331-9b3b-4ebebeac2b26 | -20.1081 | -48.8491 | 2024-10-09 00:06:57 | GOES-16 | FRUTAL | MINAS GERAIS | Brasil | 3127107 | 31 | 33 | nan | nan | nan | Cerrado | 112.3 |
| 2b9c6c78-dfe8-304b-83c3-4dd2a80dd905 | -20.1087 | -48.8261 | 2024-10-09 00:06:57 | GOES-16 | FRUTAL | MINAS GERAIS | Brasil | 3127107 | 31 | 33 | nan | nan | nan | Cerrado | 234.9 |
| 1e2a3fdf-6181-35e6-9a35-2c489994a6de | -20.1093 | -48.8031 | 2024-10-09 00:06:57 | GOES-16 | FRUTAL | MINAS GERAIS | Brasil | 3127107 | 31 | 33 | nan | nan | nan | Cerrado | 142.6 |
| 162f19ff-b49e-3442-b354-bbacfe3f46aa | -20.1291 | -48.8217 | 2024-10-09 00:06:58 | GOES-16 | FRUTAL | MINAS GERAIS | Brasil | 3127107 | 31 | 33 | nan | nan | nan | Cerrado | 116.7 |
| b21cfef3-5119-3b18-bfe8-6c22c1526d80 | -20.2915 | -43.9444 | 2024-10-09 00:06:58 | GOES-16 | ITABIRITO | MINAS GERAIS | Brasil | 3131901 | 31 | 33 | nan | nan | nan | Mata Atlântica | 105.1 |
| 83969f34-9f29-3240-b6e1-6cbd6f452724 | -20.4351 | -43.9299 | 2024-10-09 00:06:58 | GOES-16 | BELO VALE | MINAS GERAIS | Brasil | 3106408 | 31 | 33 | nan | nan | nan | Mata Atlântica | 116.8 |
| 2754efbb-6c5a-326a-8c67-84b1f3d01b9e | -20.7839 | -47.2559 | 2024-10-09 00:07:01 | GOES-16 | PATROCÍNIO PAULISTA | SÃO PAULO | Brasil | 3536307 | 35 | 33 | nan | nan | nan | Cerrado | 114.5 |
| c9a24902-e4af-31af-aa89-b41accd91b89 | -20.7846 | -47.2323 | 2024-10-09 00:07:01 | GOES-16 | PATROCÍNIO PAULISTA | SÃO PAULO | Brasil | 3536307 | 35 | 33 | nan | nan | nan | Cerrado | 146.9 |
| 09ca43f9-74c2-3cf0-ba9f-22cfba0a5e6c | -20.7853 | -47.2086 | 2024-10-09 00:07:01 | GOES-16 | SÃO TOMÁS DE AQUINO | MINAS GERAIS | Brasil | 3165107 | 31 | 33 | nan | nan | nan | Cerrado | 118.1 |
| 62931960-4ee4-344d-a581-feeb98bb77e7 | -20.8052 | -47.2273 | 2024-10-09 00:07:01 | GOES-16 | PATROCÍNIO PAULISTA | SÃO PAULO | Brasil | 3536307 | 35 | 33 | nan | nan | nan | Cerrado | 125.5 |
| 400f379b-33fa-33e1-a1ac-1a7887c96862 | -21.552 | -46.9712 | 2024-10-09 00:07:05 | GOES-16 | MOCOCA | SÃO PAULO | Brasil | 3530508 | 35 | 33 | nan | nan | nan | Cerrado | 91.5 |
| 0ba733dd-304c-3f66-b3db-9562371055e3 | -21.572 | -46.9898 | 2024-10-09 00:07:05 | GOES-16 | MOCOCA | SÃO PAULO | Brasil | 3530508 | 35 | 33 | nan | nan | nan | Cerrado | 115.2 |
| c2963f04-5ea4-3c23-832b-a617216f8dab | -21.5727 | -46.9659 | 2024-10-09 00:07:05 | GOES-16 | MOCOCA | SÃO PAULO | Brasil | 3530508 | 35 | 33 | nan | nan | nan | Cerrado | 152.6 |
| 3243defe-831e-3579-92f5-9e5fed21e11f | -21.5656 | -47.8878 | 2024-10-09 00:07:05 | GOES-16 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 115.6 |
| f298356e-97be-357d-b783-7ed33e30bae4 | -21.5935 | -46.9606 | 2024-10-09 00:07:05 | GOES-16 | SÃO JOSÉ DO RIO PARDO | SÃO PAULO | Brasil | 3549706 | 35 | 33 | nan | nan | nan | Cerrado | 71.9 |
| 020d093b-56ae-3042-ba46-e54b6a9f45b5 | -21.5857 | -47.9063 | 2024-10-09 00:07:05 | GOES-16 | RINCÃO | SÃO PAULO | Brasil | 3543709 | 35 | 33 | nan | nan | nan | Cerrado | 142.5 |
| 8e4273fc-c374-3c62-905a-0e46671b196b | -21.5864 | -47.8827 | 2024-10-09 00:07:05 | GOES-16 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 180.6 |
| e243501b-6a22-35f0-8c3c-29a1304f34cd | -21.4357 | -57.2441 | 2024-10-09 00:07:05 | GOES-16 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 49.0 |
| 90e005b6-8cd2-3445-b0cd-8b612ef5cf8c | -21.8165 | -49.1774 | 2024-10-09 00:07:06 | GOES-16 | REGINÓPOLIS | SÃO PAULO | Brasil | 3542503 | 35 | 33 | nan | nan | nan | Mata Atlântica | 76.7 |
| 2ba3cac1-3bde-3e8e-8b8e-14e5b8d8f463 | -21.8172 | -49.1541 | 2024-10-09 00:07:06 | GOES-16 | REGINÓPOLIS | SÃO PAULO | Brasil | 3542503 | 35 | 33 | nan | nan | nan | Mata Atlântica | 94.1 |
| b90311a3-8696-32a0-a219-303588f210e5 | -21.8373 | -49.1726 | 2024-10-09 00:07:06 | GOES-16 | REGINÓPOLIS | SÃO PAULO | Brasil | 3542503 | 35 | 33 | nan | nan | nan | Mata Atlântica | 106.5 |
| 357b4a4a-f1e7-36af-8327-0b9ca22eadf5 | -21.838 | -49.1493 | 2024-10-09 00:07:06 | GOES-16 | IACANGA | SÃO PAULO | Brasil | 3519105 | 35 | 33 | nan | nan | nan | Mata Atlântica | 129.4 |
| d6315e53-cfeb-3520-bf27-99af018e4307 | -22.813 | -48.4462 | 2024-10-09 00:07:11 | GOES-16 | BOTUCATU | SÃO PAULO | Brasil | 3507506 | 35 | 33 | nan | nan | nan | Cerrado | 90.1 |
| 0fe010ca-5efd-3df1-94ae-a6f20c597b7a | -22.8137 | -48.4225 | 2024-10-09 00:07:11 | GOES-16 | BOTUCATU | SÃO PAULO | Brasil | 3507506 | 35 | 33 | nan | nan | nan | Cerrado | 121.7 |
| 6e677c67-b994-3b5f-a8b1-d3cedb356590 | -22.8347 | -48.4171 | 2024-10-09 00:07:11 | GOES-16 | BOTUCATU | SÃO PAULO | Brasil | 3507506 | 35 | 33 | nan | nan | nan | Cerrado | 85.2 |
| c1ddb1ff-75eb-3c36-b78b-cce8aaa14a97 | -23.3478 | -53.907 | 2024-10-09 00:07:15 | GOES-16 | ITAQUIRAÍ | MATO GROSSO DO SUL | Brasil | 5004601 | 50 | 33 | nan | nan | nan | Mata Atlântica | 75.5 |
| 0ba5cb08-72b0-3745-bac5-92d106b955d7 | -1.11 | -53.6173 | 2024-10-09 00:15:12 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 123.6 |
| eeaa2bd4-37dc-36fa-87bc-0ac9a4571452 | -1.1284 | -53.6171 | 2024-10-09 00:15:12 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 52.5 |
| 8428de86-8442-3e6a-89db-6d0b5bffddeb | -1.9609 | -50.8404 | 2024-10-09 00:15:17 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 24.2 |
| 561bdb3b-da3f-3a84-89d4-c06d3acfd128 | -2.9829 | -53.7267 | 2024-10-09 00:15:23 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 61.8 |
| f0d3c8f9-7808-3b6b-b351-3425e77b3106 | -3.8007 | -41.6229 | 2024-10-09 00:15:27 | GOES-16 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 60.8 |
| b6680fd8-08f8-3db6-af0d-6392f10baaa2 | -3.8008 | -41.5989 | 2024-10-09 00:15:27 | GOES-16 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 85.3 |
| a446edff-5931-38d9-a69a-89843ac2d205 | -3.8119 | -49.4841 | 2024-10-09 00:15:28 | GOES-16 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 48.0 |
| 024c7b6d-5a7b-3c09-b3d2-dea9f6778d05 | -3.9021 | -46.4689 | 2024-10-09 00:15:28 | GOES-16 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 94.5 |
| ce763bb8-6bef-3df8-b9f2-cebb3cf89018 | -3.9023 | -46.4467 | 2024-10-09 00:15:28 | GOES-16 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 135.0 |
| a7623194-c94a-3a00-8ecb-599d41afe53a | -3.9207 | -46.468 | 2024-10-09 00:15:28 | GOES-16 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 56.3 |
| 8750fc16-2387-3c87-b402-e1d608cfa5dc | -3.9208 | -46.4459 | 2024-10-09 00:15:28 | GOES-16 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 90.5 |
| ce61b3e9-9b0d-377d-b62a-541d6f3335c8 | -3.9394 | -46.445 | 2024-10-09 00:15:28 | GOES-16 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 80.9 |
| 63c8a55f-eb69-3b13-b743-1a2ed6109274 | -5.2253 | -43.8164 | 2024-10-09 00:15:36 | GOES-16 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 123.9 |
| fe15ff3e-fc05-3dd7-b1b8-ed9e5d582b59 | -5.2441 | -43.8151 | 2024-10-09 00:15:36 | GOES-16 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 72.0 |
| f5e9158a-c5bc-34a5-bc58-07cb0112331b | -5.4419 | -49.5772 | 2024-10-09 00:15:37 | GOES-16 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 60.0 |
| d941148b-79eb-31d6-be9b-1cdbc6150fae | -5.4421 | -49.5559 | 2024-10-09 00:15:37 | GOES-16 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 87.4 |
| 244af463-ca7e-3ce4-bada-907d56444ef7 | -5.8216 | -44.1196 | 2024-10-09 00:15:39 | GOES-16 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 61.1 |
| 8c2643ff-a4a7-3fd7-b8e2-24dd2d055d6d | -6.1599 | -44.001 | 2024-10-09 00:15:41 | GOES-16 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 153.3 |


[Clique aqui para ver as próximas entradas](README3.md)
