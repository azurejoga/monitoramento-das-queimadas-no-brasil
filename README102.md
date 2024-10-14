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

## Dados Diários - Página 102

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| e16436f8-c50d-3893-a63d-a632f376539e | -18.26283 | -56.52848 | 2024-10-14 04:49:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 19.7 |
| 1816d6b0-106b-3f16-9b7d-d0c9ea1a3037 | -18.26212 | -56.53268 | 2024-10-14 04:49:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 19.7 |
| a97664e9-b7ac-33a0-bd8e-cf8116949955 | -18.2614 | -56.53688 | 2024-10-14 04:49:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.4 |
| e3eebe52-aadc-38b9-8a5b-6a8228f24975 | -18.25928 | -56.52781 | 2024-10-14 04:49:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 8.5 |
| fac9cb34-03fe-3b25-992c-8dcf82753d65 | -18.25856 | -56.53201 | 2024-10-14 04:49:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 8.5 |
| d9c15780-9867-33ea-8d04-7e850790a4a8 | -18.25573 | -56.52713 | 2024-10-14 04:49:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 8.5 |
| 6e848357-e82d-3b66-9ee8-7540e0350b03 | -18.23556 | -56.62339 | 2024-10-14 04:49:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.8 |
| 8e7c5275-8e68-30ca-a946-ac4b398e9089 | -18.2349 | -56.60579 | 2024-10-14 04:49:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.8 |
| d9c4b64d-5223-3e29-a496-8b0a2a9d1d1f | -18.23483 | -56.62763 | 2024-10-14 04:49:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.0 |
| 190455e2-0271-3e04-80e8-d4001791c9eb | -18.23424 | -56.58822 | 2024-10-14 04:49:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.4 |
| 0286e807-f63b-3199-8d3b-398610a5e57a | -18.23417 | -56.61002 | 2024-10-14 04:49:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.9 |
| b7649542-51ae-3c59-8492-7f5a3a3eeae3 | -18.23352 | -56.59244 | 2024-10-14 04:49:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.8 |
| bebc0ef7-7350-37cc-a7b4-a3e520954bdd | -18.23345 | -56.61425 | 2024-10-14 04:49:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.9 |
| 37dd9560-ac4b-374e-8bd5-f0003c1c9873 | -18.23272 | -56.61848 | 2024-10-14 04:49:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.8 |
| d49678f4-6fcd-38d9-a904-58a02830350a | -18.23207 | -56.60089 | 2024-10-14 04:49:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.0 |
| e97ce186-6085-38b7-baa7-00abe45402b2 | -18.23199 | -56.62271 | 2024-10-14 04:49:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.8 |
| 9a65b4f2-d3d5-3f0b-86b9-5d4e90e8b09c | -18.23134 | -56.60511 | 2024-10-14 04:49:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.0 |
| e9f9c2c6-04c6-3782-8bff-272bec095f56 | -18.23126 | -56.62695 | 2024-10-14 04:49:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.0 |
| a10af6a6-585b-3ea2-a83f-f5fdbae0b078 | -18.23068 | -56.58755 | 2024-10-14 04:49:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.4 |
| c1936e1c-1a76-3a24-9c94-701b736f8923 | -18.23061 | -56.60934 | 2024-10-14 04:49:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 20.2 |
| 1b74f0a6-6af8-397d-8bd6-e18f0b0c2ef9 | -18.22989 | -56.61356 | 2024-10-14 04:49:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 20.2 |
| 85b0284d-d93c-34aa-b49d-074b4dd91b13 | -18.22915 | -56.6178 | 2024-10-14 04:49:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.6 |
| 75f25aab-4143-36be-9236-f7afdc61e68c | -18.2285 | -56.60021 | 2024-10-14 04:49:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.0 |
| dccce48d-1c06-301c-b43a-a2669957e81e | -18.22843 | -56.62203 | 2024-10-14 04:49:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.6 |
| edc1115b-bc6b-3efb-bdda-f814a54131b7 | -18.22785 | -56.58265 | 2024-10-14 04:49:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.9 |
| 7a33cca4-1605-3645-8c27-4a9f19a74a69 | -18.22777 | -56.60443 | 2024-10-14 04:49:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.0 |
| 0b618f49-caca-3a5c-b6e6-95fab7052f87 | -18.22705 | -56.60865 | 2024-10-14 04:49:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 20.2 |
| 0435505a-8ff8-3634-8395-ba54a27a74f7 | -18.22639 | -56.59108 | 2024-10-14 04:49:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.8 |
| b925d8f2-98c3-36da-98e9-29e8395ff494 | -18.22632 | -56.61289 | 2024-10-14 04:49:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 20.2 |
| b5843132-eb13-3ace-962b-7aa7201be7d7 | -18.22567 | -56.59531 | 2024-10-14 04:49:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.8 |
| 6db5811c-a2ae-3ec5-be1b-e44abe3f90c6 | -18.22559 | -56.61712 | 2024-10-14 04:49:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.6 |
| 19b172ee-90db-343a-a8ca-a9bbd56bf71f | -18.22494 | -56.59953 | 2024-10-14 04:49:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.0 |
| be9c6ab4-4894-3d96-954a-65817a635977 | -18.22429 | -56.58197 | 2024-10-14 04:49:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.9 |
| 0e47cfda-934a-3c98-9cdb-ea39f2ec2e83 | -18.22421 | -56.60375 | 2024-10-14 04:49:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.0 |
| e9aed3f4-b871-3267-90ab-f1ea1e8a7f8a | -18.22348 | -56.60798 | 2024-10-14 04:49:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 9.5 |
| 2a87aef4-d7bf-391c-a5aa-b63aa0b266f0 | -18.22283 | -56.5904 | 2024-10-14 04:49:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.8 |
| 093c1b8e-254b-3514-81f6-f82f7aa3bc9d | -18.22276 | -56.61221 | 2024-10-14 04:49:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 9.5 |
| 62c1685f-7388-35bc-9b06-e92166cffad4 | -18.22211 | -56.59462 | 2024-10-14 04:49:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.8 |
| ea26d3d0-5e35-34a0-9170-c386a61fe9ff | -18.22138 | -56.59885 | 2024-10-14 04:49:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.0 |
| ec898556-63a9-3fd1-ad23-239d8d41191c | -18.22065 | -56.60308 | 2024-10-14 04:49:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.0 |
| 78411cf9-8b18-36a9-9987-836b5ea6b6cb | -18.21992 | -56.6073 | 2024-10-14 04:49:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 9.5 |
| 1a1b3881-c514-3b15-bff7-52b1ddb6bb3d | -18.21919 | -56.61152 | 2024-10-14 04:49:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 9.5 |
| 4f70bf07-0b17-35c2-8a92-a595a082d5e1 | -18.21854 | -56.59395 | 2024-10-14 04:49:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.0 |
| 5d6fef8e-4467-39b6-b8f8-0f4399b38350 | -18.21781 | -56.59818 | 2024-10-14 04:49:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 5.7 |
| b9bd04b3-3411-340b-8a95-ecd5bbd528d7 | -18.21708 | -56.6024 | 2024-10-14 04:49:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 5.7 |
| ee730a90-26c0-30e3-9810-884ce0c3c419 | -18.21635 | -56.60662 | 2024-10-14 04:49:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.9 |
| 846d1926-44fd-3433-bf70-d64d53cdea4c | -18.21498 | -56.59327 | 2024-10-14 04:49:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.0 |
| 927185ff-4452-3bf8-8179-282ffa70fa12 | -18.21425 | -56.5975 | 2024-10-14 04:49:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 5.7 |
| 29d39e36-f3d1-3c49-91b4-46bd583c0864 | -19.58871 | -56.5326 | 2024-10-14 04:49:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 1.3 |
| 90437396-5ddf-39bd-9cfc-c1a9073cd76e | -28.58764 | -49.4427 | 2024-10-14 04:51:00 | NPP-375D | SIDERÓPOLIS | SANTA CATARINA | Brasil | 4217600 | 42 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 394d0795-1db5-35a0-97c2-6a278be25b94 | -28.58328 | -49.44213 | 2024-10-14 04:51:00 | NPP-375D | SIDERÓPOLIS | SANTA CATARINA | Brasil | 4217600 | 42 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 91cb49c7-b183-33b7-8fdd-703eee41758a | -24.24379 | -50.74146 | 2024-10-14 04:51:00 | NPP-375D | ORTIGUEIRA | PARANÁ | Brasil | 4117305 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 2a5560b4-6f0e-3cef-9cc7-4c92838a1038 | -24.24164 | -50.73945 | 2024-10-14 04:51:00 | NPP-375D | ORTIGUEIRA | PARANÁ | Brasil | 4117305 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| b9e0b5aa-e7af-3df1-895c-0ed3ce9c40ab | -29.4462 | -56.35642 | 2024-10-14 04:51:00 | NPP-375D | ALEGRETE | RIO GRANDE DO SUL | Brasil | 4300406 | 43 | 33 | nan | nan | nan | Pampa | 1.0 |
| 31dfdc88-de80-32a7-8832-ba69b8134933 | -31.58093 | -53.73078 | 2024-10-14 04:53:00 | NPP-375D | CANDIOTA | RIO GRANDE DO SUL | Brasil | 4304358 | 43 | 33 | nan | nan | nan | Pampa | 0.7 |
| 5f9cb699-3b14-3ad8-93c3-19f35f1b63bd | -2.4344 | -46.9195 | 2024-10-14 04:55:18 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 42.8 |
| 750ff57c-5686-3f47-bcc4-63acd41fbd61 | -3.289 | -42.8327 | 2024-10-14 04:55:23 | GOES-16 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 94.2 |
| c79858aa-7705-3cb6-be06-a779b071f6d9 | -3.9103 | -48.3466 | 2024-10-14 04:55:27 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 56.6 |
| 0e84cdca-84e3-3fdd-af0d-e3396cf096cf | -4.1149 | -48.2299 | 2024-10-14 04:55:28 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 71.4 |
| bf3c3270-e930-3aa4-a61f-3462ab6def5a | -17.87 | -57.26 | 2024-10-14 05:03:45 | MSG-03 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 92c99c2c-2851-322b-a4e1-376c4ce55a1c | -17.9 | -57.36 | 2024-10-14 05:03:45 | MSG-03 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 2c291785-b2b4-31a8-a531-5ae5d6636521 | -17.9 | -57.28 | 2024-10-14 05:03:45 | MSG-03 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 52f5cfcb-c211-3714-98e5-04898bbf6eaa | -17.9 | -57.21 | 2024-10-14 05:03:45 | MSG-03 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| d441959b-4d54-3245-aa76-37884647d6c3 | -17.93 | -57.38 | 2024-10-14 05:03:45 | MSG-03 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 547db030-1e37-38a6-8f9a-05f4c72c3776 | -17.93 | -57.3 | 2024-10-14 05:03:45 | MSG-03 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| fb1bc0dc-9495-3080-a949-59ded2ce95d9 | -17.93 | -57.23 | 2024-10-14 05:03:45 | MSG-03 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| c3255ff8-6bfc-360f-9638-c77331ef8005 | -17.97 | -57.4 | 2024-10-14 05:03:45 | MSG-03 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| bb1a05b6-cd28-3fc2-97a3-fa6a965852b8 | -18.0 | -57.35 | 2024-10-14 05:03:45 | MSG-03 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 43a6a095-c99f-363d-8ac6-fc6c4ed6add2 | -17.96 | -57.25 | 2024-10-14 05:03:45 | MSG-03 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 92f48262-79ba-3ea0-bc5a-9e1c7f411d44 | -17.96 | -57.33 | 2024-10-14 05:03:45 | MSG-03 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 10f4d92b-f822-3b09-83b2-2cc6c40e4643 | -17.84 | -57.31 | 2024-10-14 05:03:45 | MSG-03 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| e6e453e4-ccf5-303a-82ba-11d8d13f862d | -17.83 | -57.24 | 2024-10-14 05:03:45 | MSG-03 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| b8ed3c3e-452a-303b-8b42-6ef7b045f0a2 | -17.87 | -57.34 | 2024-10-14 05:03:45 | MSG-03 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| bf16311b-f6d1-36b1-9f18-eee42612a68e | -2.4344 | -46.9195 | 2024-10-14 05:05:19 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 46.1 |
| 732886d3-3b52-3a61-ae81-c30be2c635c7 | -2.6118 | -49.0985 | 2024-10-14 05:05:20 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 23.1 |
| 8b1595df-279b-3d1c-b549-f9a3924c98dd | -2.6119 | -49.0772 | 2024-10-14 05:05:20 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 19.9 |
| 98b30f82-ee8a-3869-995d-a3a530c82c4d | -3.9103 | -48.3466 | 2024-10-14 05:05:28 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 51.3 |
| 4a724241-b142-35ef-abb1-fdb851ac32b9 | -4.1148 | -48.2515 | 2024-10-14 05:05:29 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 42.5 |
| 6d14d5d4-5797-3c5f-b890-64b5cbcb5af6 | -4.1149 | -48.2299 | 2024-10-14 05:05:29 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 60.4 |
| 90ff2f32-3b7e-3473-8b8a-d4803a91107c | -7.9419 | -63.6177 | 2024-10-14 05:05:51 | GOES-16 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 48.9 |
| e11b12b9-e90e-34de-bc42-b2563ca3cf1b | -7.9418 | -63.6365 | 2024-10-14 05:05:51 | GOES-16 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 44.9 |
| ceb18f2f-4344-368f-8a44-bf1de3b86ca8 | 2.5272 | -60.63435 | 2024-10-14 05:06:00 | NOAA-20 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e413c3df-ba7d-321e-be88-8b5ac44d165a | 2.43815 | -50.94114 | 2024-10-14 05:06:00 | NOAA-20 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 79b9aead-e766-376d-84d0-5bcab6927331 | 2.43738 | -50.93629 | 2024-10-14 05:06:00 | NOAA-20 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 3.2 |
| f93add9a-0205-3438-84ae-15e2282400ee | 0.95375 | -50.20616 | 2024-10-14 05:06:00 | NOAA-20 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0ef9b0bf-f2cd-34f2-8aec-4b821790879c | 0.9496 | -50.20682 | 2024-10-14 05:06:00 | NOAA-20 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e763816a-8c04-3c6a-8890-dad04c57fadf | 3.72928 | -51.63515 | 2024-10-14 05:06:00 | NOAA-20 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 7b67a221-1f50-37d1-96b3-db0b7f899afa | 3.37104 | -51.3409 | 2024-10-14 05:06:00 | NOAA-20 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 62946b32-7135-3ad3-9fb2-f17e4809549b | 3.36731 | -51.3415 | 2024-10-14 05:06:00 | NOAA-20 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 394c2aaa-7611-3a86-b2c2-248c210e98ca | 3.35103 | -51.31187 | 2024-10-14 05:06:00 | NOAA-20 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 2ece341a-57f1-3db6-875f-cc2a21405689 | 3.3503 | -51.30738 | 2024-10-14 05:06:00 | NOAA-20 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 56047c4e-5ee0-324d-84ad-1abb7c0f5a90 | 2.90855 | -51.49888 | 2024-10-14 05:06:00 | NOAA-20 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3d7a611e-935b-3435-a4b0-e500d4a2997c | 1.3447 | -51.25994 | 2024-10-14 05:06:00 | NOAA-20 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 1432ebe6-fcc5-33cd-bc31-748015183999 | 0.97925 | -51.90754 | 2024-10-14 05:06:00 | NOAA-20 | SERRA DO NAVIO | AMAPÁ | Brasil | 1600055 | 16 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 009c5222-4f6f-37a0-91a2-6aaeebb04f21 | 0.92517 | -51.97518 | 2024-10-14 05:06:00 | NOAA-20 | SERRA DO NAVIO | AMAPÁ | Brasil | 1600055 | 16 | 33 | nan | nan | nan | Amazônia | 0.6 |
| c39144d8-5343-3cc0-8780-0902b6a0c351 | 0.92225 | -52.04145 | 2024-10-14 05:06:00 | NOAA-20 | SERRA DO NAVIO | AMAPÁ | Brasil | 1600055 | 16 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 77482343-e738-34e6-a550-84bd7500f143 | 0.50328 | -51.64016 | 2024-10-14 05:06:00 | NOAA-20 | PORTO GRANDE | AMAPÁ | Brasil | 1600535 | 16 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 8ae6cb61-68d9-32a1-97d2-deb68a040722 | -1.84284 | -55.04956 | 2024-10-14 05:08:00 | NOAA-20 | CURUÁ | PARÁ | Brasil | 1502855 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 17323ca3-0cc9-3e08-9d35-5f14f127e33c | -1.82257 | -55.37 | 2024-10-14 05:08:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 303dbb13-ba57-383a-9bf6-25a8bdffc33a | -1.81924 | -55.36948 | 2024-10-14 05:08:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |


[Clique aqui para ver as próximas entradas](README103.md)
