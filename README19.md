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

## Dados Diários - Página 19

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| d25fdef8-4d68-38db-b1de-18924785fcf1 | -15.61481 | -55.70845 | 2025-10-22 05:18:00 | NOAA-20 | CUIABÁ | MATO GROSSO | Brasil | 5103403 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| a41aac8d-c735-32e6-b438-4e21f819fbad | -18.11188 | -48.53058 | 2025-10-22 05:18:00 | NOAA-20 | CORUMBAÍBA | GOIÁS | Brasil | 5205901 | 52 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 2de0c4b2-2193-3e2d-80bf-3a7c8d184150 | -18.16783 | -52.97034 | 2025-10-22 05:18:00 | NOAA-20 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 0a341724-845d-3896-bdb8-151fa6c88590 | -9.79873 | -67.02769 | 2025-10-22 05:18:00 | NOAA-20 | ACRELÂNDIA | ACRE | Brasil | 1200013 | 12 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 7fad6feb-bc25-390a-8e6e-692fd32ef841 | -18.11136 | -48.5362 | 2025-10-22 05:18:00 | NOAA-20 | CORUMBAÍBA | GOIÁS | Brasil | 5205901 | 52 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 836d6cfb-a68a-3e6f-9c3d-f60124931bdd | -14.68835 | -48.78479 | 2025-10-22 05:18:00 | NOAA-20 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 825bca54-13af-3150-a9eb-ec2c3ddcfcd4 | -11.96208 | -63.12638 | 2025-10-22 05:18:00 | NOAA-20 | SERINGUEIRAS | RONDÔNIA | Brasil | 1101500 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| af61d9b1-ca19-3663-98bd-a38018005165 | -16.09982 | -55.41644 | 2025-10-22 05:18:00 | NOAA-20 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 35218575-40a3-38d0-8b11-c21cb11e9260 | -9.72118 | -67.47438 | 2025-10-22 05:18:00 | NOAA-20 | PORTO ACRE | ACRE | Brasil | 1200807 | 12 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 71886083-312f-3613-a0dd-12d0e2cafb7e | -16.77139 | -52.48898 | 2025-10-22 05:18:00 | NOAA-20 | DOVERLÂNDIA | GOIÁS | Brasil | 5207253 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| dd5a9623-eb9a-3da1-a8cb-e87d81f87fa8 | -12.51196 | -48.58484 | 2025-10-22 05:18:00 | NOAA-20 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 40f82d2a-2b40-3dac-97a8-bb02b28ad5dc | -18.14605 | -52.98276 | 2025-10-22 05:18:00 | NOAA-20 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 3200e474-96e1-3ee5-94e2-6cd1ca302217 | -16.24158 | -49.59929 | 2025-10-22 05:18:00 | NOAA-20 | INHUMAS | GOIÁS | Brasil | 5210000 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| a4492e10-a133-3e9f-bacc-1f9d4cb62740 | -15.48763 | -50.46408 | 2025-10-22 05:18:00 | NOAA-20 | FAINA | GOIÁS | Brasil | 5207535 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c7445980-3381-3a92-9043-21b6ba4ea35d | -9.79659 | -67.03206 | 2025-10-22 05:18:00 | NOAA-20 | ACRELÂNDIA | ACRE | Brasil | 1200013 | 12 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 60292491-b0c4-38ce-8812-967e35a9670d | -12.38004 | -63.87097 | 2025-10-22 05:18:00 | NOAA-20 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 2.2 |
| acdae8cc-0d1e-3451-b759-44314060d921 | -16.0425 | -54.26269 | 2025-10-22 05:18:00 | NOAA-20 | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 53eaf80f-36b3-35fe-be72-8ef5e4049c70 | -10.92649 | -68.58848 | 2025-10-22 05:18:00 | NOAA-20 | EPITACIOLÂNDIA | ACRE | Brasil | 1200252 | 12 | 33 | nan | nan | nan | Amazônia | 0.6 |
| d51dcfd4-a0d1-363d-87f4-7b6516ca65a5 | -12.27485 | -63.8726 | 2025-10-22 05:18:00 | NOAA-20 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 5cb1ece8-ddba-394c-9077-d39592ab48ae | -18.14639 | -52.97975 | 2025-10-22 05:18:00 | NOAA-20 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| a82796b3-ead7-3574-9189-03d143f15d9d | -18.16716 | -52.97623 | 2025-10-22 05:18:00 | NOAA-20 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| c035f747-0d87-361e-8c69-d70b7a189217 | -11.17062 | -62.5453 | 2025-10-22 05:18:00 | NOAA-20 | URUPÁ | RONDÔNIA | Brasil | 1101708 | 11 | 33 | nan | nan | nan | Amazônia | 0.6 |
| a6fc37a4-a554-3ee2-abda-28b8a9fe2e38 | -4.4632 | -43.2386 | 2025-10-22 05:20:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 126.5 |
| 23e8d912-92d0-3ce6-a91d-4d17c9a375fa | -4.4633 | -43.2152 | 2025-10-22 05:20:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 60.6 |
| c0810a31-f52a-334d-a0ab-07ceddd066c8 | -4.4445 | -43.2397 | 2025-10-22 05:20:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 117.9 |
| 40708312-1592-3037-a0dc-809cd8056486 | -19.09233 | -57.52191 | 2025-10-22 05:21:00 | NOAA-20 | LADÁRIO | MATO GROSSO DO SUL | Brasil | 5005202 | 50 | 33 | nan | nan | nan | Pantanal | 2.5 |
| 4c68fba1-935b-3395-8133-81332635be01 | -18.59506 | -51.72281 | 2025-10-22 05:21:00 | NOAA-20 | ITARUMÃ | GOIÁS | Brasil | 5211305 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 711d30ff-4f5b-3ccf-870d-762eadbc43d6 | -19.15947 | -49.12548 | 2025-10-22 05:21:00 | NOAA-20 | PRATA | MINAS GERAIS | Brasil | 3152808 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 498d7275-9d50-3e40-b6f2-6fd80ef9774c | -19.15862 | -49.12888 | 2025-10-22 05:21:00 | NOAA-20 | PRATA | MINAS GERAIS | Brasil | 3152808 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a7f55fa9-344e-38b7-ac74-5588aeab6785 | -19.10622 | -57.53388 | 2025-10-22 05:21:00 | NOAA-20 | LADÁRIO | MATO GROSSO DO SUL | Brasil | 5005202 | 50 | 33 | nan | nan | nan | Pantanal | 2.8 |
| 8912ef1e-3dab-365c-a425-7f09826c8ddb | -18.94523 | -55.07818 | 2025-10-22 05:21:00 | NOAA-20 | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Pantanal | 5.9 |
| 81cda0eb-39ef-31bf-9eaa-3bb5bfb3ec11 | -19.09484 | -57.53216 | 2025-10-22 05:21:00 | NOAA-20 | LADÁRIO | MATO GROSSO DO SUL | Brasil | 5005202 | 50 | 33 | nan | nan | nan | Pantanal | 3.0 |
| d68af60a-1529-3845-a082-1b2de4f72587 | -18.11565 | -54.52393 | 2025-10-22 05:21:00 | NOAA-20 | PEDRO GOMES | MATO GROSSO DO SUL | Brasil | 5006408 | 50 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 86132344-acb6-39b9-808e-6b873952edf0 | -19.05692 | -57.49665 | 2025-10-22 05:21:00 | NOAA-20 | LADÁRIO | MATO GROSSO DO SUL | Brasil | 5005202 | 50 | 33 | nan | nan | nan | Pantanal | 1.7 |
| 37edcd21-3243-3d0c-a558-f732ec505b59 | -19.08409 | -57.52561 | 2025-10-22 05:21:00 | NOAA-20 | LADÁRIO | MATO GROSSO DO SUL | Brasil | 5005202 | 50 | 33 | nan | nan | nan | Pantanal | 2.3 |
| 46ee8a07-6c6d-35c4-bfd6-dd08a72c868c | -20.41957 | -55.74304 | 2025-10-22 05:21:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 2.5 |
| 396db632-338b-3ddb-ad15-2de33850128b | -19.08854 | -57.52131 | 2025-10-22 05:21:00 | NOAA-20 | LADÁRIO | MATO GROSSO DO SUL | Brasil | 5005202 | 50 | 33 | nan | nan | nan | Pantanal | 5.9 |
| 1e119763-a582-336a-a653-afabd35a6a39 | -20.42009 | -55.73881 | 2025-10-22 05:21:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 2.5 |
| 737429dd-d68f-3ed4-9b36-4a8595d5cce1 | -19.06299 | -57.48517 | 2025-10-22 05:21:00 | NOAA-20 | LADÁRIO | MATO GROSSO DO SUL | Brasil | 5005202 | 50 | 33 | nan | nan | nan | Pantanal | 6.0 |
| 55a61a30-5274-3716-add3-f98f0b0d8aaa | -18.65065 | -49.09055 | 2025-10-22 05:21:00 | NOAA-20 | CENTRALINA | MINAS GERAIS | Brasil | 3115805 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 1d71f577-ced7-3a67-abf7-e4126835a2d5 | -19.15294 | -49.12536 | 2025-10-22 05:21:00 | NOAA-20 | PRATA | MINAS GERAIS | Brasil | 3152808 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a40d93a3-4564-3e09-810f-efa7edd18f01 | -19.05376 | -57.49118 | 2025-10-22 05:21:00 | NOAA-20 | LADÁRIO | MATO GROSSO DO SUL | Brasil | 5005202 | 50 | 33 | nan | nan | nan | Pantanal | 8.0 |
| 55ac41be-590d-3bce-886c-eda4aeac1869 | -19.48857 | -54.93207 | 2025-10-22 05:21:00 | NOAA-20 | RIO NEGRO | MATO GROSSO DO SUL | Brasil | 5007307 | 50 | 33 | nan | nan | nan | Cerrado | 0.8 |
| e6477b8f-326d-3b5f-be87-56b2c7dd271f | -18.59467 | -51.72663 | 2025-10-22 05:21:00 | NOAA-20 | ITARUMÃ | GOIÁS | Brasil | 5211305 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a89512d9-2dd4-37d5-afea-545688986222 | -18.9447 | -55.08265 | 2025-10-22 05:21:00 | NOAA-20 | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Pantanal | 4.3 |
| 82808517-2374-3083-a83c-ec27acce9e53 | -20.42389 | -55.74364 | 2025-10-22 05:21:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 2.5 |
| 64dafe2e-4418-3a19-b268-3d3c2f831b1b | -19.05312 | -57.49607 | 2025-10-22 05:21:00 | NOAA-20 | LADÁRIO | MATO GROSSO DO SUL | Brasil | 5005202 | 50 | 33 | nan | nan | nan | Pantanal | 8.0 |
| 7fb42d42-7746-31d2-abdb-85ce7aa32319 | -19.05405 | -57.49376 | 2025-10-22 05:21:00 | NOAA-20 | LADÁRIO | MATO GROSSO DO SUL | Brasil | 5005202 | 50 | 33 | nan | nan | nan | Pantanal | 18.3 |
| 05a0e9ae-2d28-3e47-af6c-c71674ae59bc | -18.94912 | -55.08323 | 2025-10-22 05:21:00 | NOAA-20 | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Pantanal | 4.3 |
| f83e4775-5e7f-3730-9a83-a1e1358a52d2 | -19.062 | -57.48744 | 2025-10-22 05:21:00 | NOAA-20 | LADÁRIO | MATO GROSSO DO SUL | Brasil | 5005202 | 50 | 33 | nan | nan | nan | Pantanal | 5.8 |
| c52caa2d-cbbb-3edc-a305-39b585b8690b | -19.15209 | -49.12882 | 2025-10-22 05:21:00 | NOAA-20 | PRATA | MINAS GERAIS | Brasil | 3152808 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 5420bbf9-daa5-33f1-826d-a4d767694122 | -17.95546 | -57.64041 | 2025-10-22 05:21:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.4 |
| 3d1bcbfb-ee6d-33b1-8309-c0ad0e3b2db6 | -18.94965 | -55.07875 | 2025-10-22 05:21:00 | NOAA-20 | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Pantanal | 5.9 |
| 690d75dd-18c0-3cf4-87e2-533c45f8f5d3 | -20.42441 | -55.73938 | 2025-10-22 05:21:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 5e4a1c17-c8f2-34ef-8a26-7dc3d303ec88 | -18.64375 | -49.09472 | 2025-10-22 05:21:00 | NOAA-20 | CENTRALINA | MINAS GERAIS | Brasil | 3115805 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ba93e4e4-30bf-37db-85c1-f6476954a15d | -7.93875 | -44.83837 | 2025-10-22 05:40:00 | AQUA_M-M | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 6.0 |
| d8380a94-f19f-3fa0-a174-6f14e8e65651 | -4.90384 | -38.92344 | 2025-10-22 05:40:00 | AQUA_M-M | QUIXADÁ | CEARÁ | Brasil | 2311306 | 23 | 33 | nan | nan | nan | Caatinga | 9.6 |
| b250c346-4dfc-3fdf-82fa-0af206523916 | -6.64168 | -43.59929 | 2025-10-22 05:40:00 | AQUA_M-M | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 8.2 |
| ddebe038-f817-335c-a678-3545b95a456a | -4.45197 | -43.22816 | 2025-10-22 05:40:00 | AQUA_M-M | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 60.9 |
| bc12e2c7-0f9c-3343-921c-0ac845793bad | -6.64018 | -43.60902 | 2025-10-22 05:40:00 | AQUA_M-M | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 9.9 |
| f9df1c38-be54-36ea-8023-5a6c1054f6ec | -3.44408 | -41.84282 | 2025-10-22 05:40:00 | AQUA_M-M | CAXINGÓ | PIAUÍ | Brasil | 2202653 | 22 | 33 | nan | nan | nan | Caatinga | 6.3 |
| f25ff2a4-53e0-3ca4-b7f9-ed575771274e | -3.99222 | -43.27828 | 2025-10-22 05:40:00 | AQUA_M-M | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 8.6 |
| 8ea4d9af-48f0-33d4-ae7e-cda379a242b4 | -4.14901 | -40.90744 | 2025-10-22 05:40:00 | AQUA_M-M | CARNAUBAL | CEARÁ | Brasil | 2303402 | 23 | 33 | nan | nan | nan | Caatinga | 16.1 |
| 5f0a8c74-28cb-36bd-9295-c097ce2c04b4 | -6.53486 | -44.35706 | 2025-10-22 05:40:00 | AQUA_M-M | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 3cbf6b9f-bcf7-3473-9e50-7f384c532183 | -4.45047 | -43.23789 | 2025-10-22 05:40:00 | AQUA_M-M | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 255.2 |
| f53b6245-dc5d-34c5-95b2-669f58029163 | -2.85712 | -41.74055 | 2025-10-22 05:40:00 | AQUA_M-M | PARNAÍBA | PIAUÍ | Brasil | 2207702 | 22 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 8c2e1432-4f1c-3590-ba35-10f76348f28e | -7.92997 | -46.00815 | 2025-10-22 05:40:00 | AQUA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 11.1 |
| d86e1910-b1af-3a37-bb1c-cb55d88cff66 | -5.15175 | -37.64354 | 2025-10-22 05:40:00 | AQUA_M-M | BARAÚNA | RIO GRANDE DO NORTE | Brasil | 2401453 | 24 | 33 | nan | nan | nan | Caatinga | 9.2 |
| afbe14c0-ce63-3109-861f-68ff67848b2f | -22.08377 | -43.27031 | 2025-10-22 05:44:00 | AQUA_M-M | PARAÍBA DO SUL | RIO DE JANEIRO | Brasil | 3303708 | 33 | 33 | nan | nan | nan | Mata Atlântica | 15.2 |
| 44fad307-c2c8-30da-9d62-409ba2b8e39d | -24.76769 | -47.60214 | 2025-10-22 05:44:00 | AQUA_M-M | ILHA COMPRIDA | SÃO PAULO | Brasil | 3520426 | 35 | 33 | nan | nan | nan | Mata Atlântica | 9.5 |
| 567846ec-3bd6-3bc4-898d-9492a7a6a717 | -9.0086 | -65.91794 | 2025-10-22 06:08:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 5f678bc2-a991-3c86-ac49-36dfcbd4c976 | -10.52419 | -68.04163 | 2025-10-22 06:08:00 | NOAA-21 | XAPURI | ACRE | Brasil | 1200708 | 12 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3ab2c5cd-8065-3587-b663-a24afe9adda1 | -9.00716 | -65.92011 | 2025-10-22 06:08:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 3823024f-84e1-36a1-aa3b-a9656fa7a82d | -9.01181 | -65.92706 | 2025-10-22 06:08:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 350df467-f282-3388-9b16-5f22895bd2d1 | -9.55987 | -66.74817 | 2025-10-22 06:08:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 7e6686f1-af8d-3271-9acc-3babaeddca3f | -9.55219 | -66.64913 | 2025-10-22 06:08:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 5c2b7ce8-f37b-3d4c-b4dc-74464a2c8bdd | -9.10881 | -65.93285 | 2025-10-22 06:08:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| b9ca8bad-336e-39de-a09d-eec27e7da5f3 | -9.09594 | -67.68988 | 2025-10-22 06:08:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 3085b0ba-39a2-3e45-b993-1ac95a2f784e | -9.93976 | -66.71394 | 2025-10-22 06:08:00 | NOAA-21 | ACRELÂNDIA | ACRE | Brasil | 1200013 | 12 | 33 | nan | nan | nan | Amazônia | 0.5 |
| e52bc9d0-d20a-3fe2-a3cf-fcb54759470b | -9.1082 | -65.93708 | 2025-10-22 06:08:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| c248558e-632b-3e2f-a966-5de83234f138 | -10.05502 | -68.74624 | 2025-10-22 06:08:00 | NOAA-21 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 1.0 |
| edac0f44-0dc9-3696-849d-c84c9d6ff0f9 | -9.00688 | -65.93063 | 2025-10-22 06:08:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 4e3db5ab-39bd-336b-9689-52cce560309f | -9.09205 | -67.6893 | 2025-10-22 06:08:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 3.5 |
| ab027fa5-53c7-3088-a3f6-a0cf4c8b4592 | -9.00746 | -65.92639 | 2025-10-22 06:08:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 10.5 |
| 8453d7fe-b1d4-3897-956d-d22db5e68a6f | -9.728 | -67.47279 | 2025-10-22 06:08:00 | NOAA-21 | PORTO ACRE | ACRE | Brasil | 1200807 | 12 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 44e409bd-2526-38d3-bafb-ef3cda6d8ff8 | -9.28827 | -67.32227 | 2025-10-22 06:08:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| f78c548d-dff1-3f0a-a3e9-372720ff17cf | -9.00424 | -65.91728 | 2025-10-22 06:08:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 101c5410-d9f5-319e-8fa7-70def6f34916 | -9.65011 | -65.25283 | 2025-10-22 06:08:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 5bf5c002-4c81-335e-aec2-b5baf0ddaf34 | -9.73598 | -68.88306 | 2025-10-22 06:08:00 | NOAA-21 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 5ba293bd-7061-35f0-93ed-71f68120c780 | -9.55272 | -66.64522 | 2025-10-22 06:08:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| b68bd0f1-8ab3-3387-b998-c854e63a7b8f | -8.93363 | -66.88972 | 2025-10-22 06:08:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f31e78bb-d85d-3df2-b983-47677c2632f4 | -9.36102 | -68.81428 | 2025-10-22 06:08:00 | NOAA-21 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 0.6 |
| c279e1a4-4a5c-3068-ae25-44b3fe4ef948 | -10.07735 | -65.1662 | 2025-10-22 06:08:00 | NOAA-21 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| df289fb4-b17f-3615-816f-af89967c709d | -10.01535 | -67.87169 | 2025-10-22 06:08:00 | NOAA-21 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f0cba03a-6688-3b1b-a2f6-b7c7c1092797 | -9.11317 | -65.93344 | 2025-10-22 06:08:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 583ae9c1-d118-3e6b-9785-e3d1bf6bf1c7 | -9.42746 | -69.00222 | 2025-10-22 06:08:00 | NOAA-21 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 0fab3cd0-0d57-3cb0-a15c-aa2c04a671c9 | -12.38153 | -63.87006 | 2025-10-22 06:08:00 | NOAA-21 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 8318b51a-e9dc-3ac5-b20b-a1f8aa63c317 | -8.93615 | -66.90125 | 2025-10-22 06:08:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| c42e4db4-d0b3-3a94-b024-b27b54887367 | -12.37668 | -63.8661 | 2025-10-22 06:08:00 | NOAA-21 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 7d823cff-70bb-32e8-8972-e6875fbde620 | -9.00803 | -65.92217 | 2025-10-22 06:08:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 10.5 |


[Clique aqui para ver as próximas entradas](README20.md)
