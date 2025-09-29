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

## Dados Diários - Página 99

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 4f3ed556-3228-3a68-a5ff-402e03c22664 | -5.9185 | -45.839 | 2025-09-29 14:30:00 | GOES-19 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 71.7 |
| 366efefb-27e9-322b-a983-57797bf54d32 | -10.8238 | -45.407 | 2025-09-29 14:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 105.3 |
| cf583e6e-e992-3cbc-a91a-165502d5717f | -7.7226 | -46.9865 | 2025-09-29 14:30:00 | GOES-19 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 69.6 |
| db26f5c1-0647-3885-8768-787116b53410 | -8.5224 | -44.6305 | 2025-09-29 14:30:00 | GOES-19 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 85.1 |
| 998b8786-0a69-3681-b93a-b6e5008a1696 | -8.2476 | -45.481 | 2025-09-29 14:30:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 92.9 |
| 8b4d5e85-4b84-3226-ae52-804cfd5db956 | -7.8375 | -46.7766 | 2025-09-29 14:30:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 143.9 |
| e5a42545-8c0c-3878-bd7d-21a311ad4f51 | -15.2194 | -50.0851 | 2025-09-29 14:30:00 | GOES-19 | ARAGUAPAZ | GOIÁS | Brasil | 5202155 | 52 | 33 | nan | nan | nan | Cerrado | 67.8 |
| b14cb5a2-2631-3b42-9d7c-45ec5ce75b56 | -6.0797 | -42.6064 | 2025-09-29 14:30:00 | GOES-19 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 78.9 |
| 0cca8a83-e873-371c-8bef-ff28303fce0e | -4.1386 | -44.2965 | 2025-09-29 14:30:00 | GOES-19 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 82.0 |
| 1cb0bafe-0a58-3c72-83af-96bb2a62c639 | -8.2662 | -45.5018 | 2025-09-29 14:30:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 145.2 |
| 14400514-de89-3b9e-a9ee-fe1c92526094 | -11.6649 | -45.3361 | 2025-09-29 14:30:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 84.6 |
| 7eeae7ca-91a7-3d9c-adc6-fe70bee01c8d | -7.4414 | -46.9888 | 2025-09-29 14:30:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 80.7 |
| 2a397d85-776e-3f68-ab1e-4be304e442f6 | -6.6981 | -42.7882 | 2025-09-29 14:30:00 | GOES-19 | FRANCISCO AYRES | PIAUÍ | Brasil | 2204105 | 22 | 33 | nan | nan | nan | Caatinga | 67.2 |
| 22ef48a3-5707-3810-b64d-3ce21d229782 | -8.71 | -54.6467 | 2025-09-29 14:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 76.0 |
| 546833cc-f8a9-30ae-a7a0-e7f866c59e3b | -8.2665 | -45.4791 | 2025-09-29 14:30:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 95.0 |
| 85ac25b7-66ae-39a3-9ed6-17597f27aa3b | -9.0871 | -47.6294 | 2025-09-29 14:30:00 | GOES-19 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 78.2 |
| eecdaccc-4742-3838-a237-f9ac195db87d | -9.4009 | -54.6781 | 2025-09-29 14:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 72.9 |
| cfb88a6b-051b-3b96-a386-0482b3ae5527 | -9.5199 | -47.6946 | 2025-09-29 14:30:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 99.1 |
| 0cefac50-5d81-3544-95ef-cd7ec2e5db84 | -9.0685 | -47.6093 | 2025-09-29 14:30:00 | GOES-19 | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 145.5 |
| bf4ecf45-24dd-325a-85fb-26c0452cca9b | -13.2346 | -50.9691 | 2025-09-29 14:30:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 121.5 |
| 2ee5b6c8-5238-37ed-bed9-bc5f0cf17b60 | -9.4458 | -47.5923 | 2025-09-29 14:30:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 77.0 |
| 7474b8ee-e4ff-3317-a0a3-5acb1218ca52 | -5.7413 | -42.6576 | 2025-09-29 14:30:00 | GOES-19 | AGRICOLÂNDIA | PIAUÍ | Brasil | 2200103 | 22 | 33 | nan | nan | nan | Caatinga | 79.6 |
| f68eb9c9-c5da-3999-88f6-5e3f7e8120ff | -13.7889 | -47.9181 | 2025-09-29 14:30:00 | GOES-19 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 107.9 |
| 7f32882d-ad0c-320e-88a5-892d6fd443d3 | -8.8896 | -51.6549 | 2025-09-29 14:30:00 | GOES-19 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 83.8 |
| 178dbc9e-da3f-3c90-9e13-1dc3afc4c140 | -11.4417 | -44.9767 | 2025-09-29 14:30:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 94.0 |
| 7c891441-bdc1-3c45-8f7b-f95d1d9b2401 | -5.207 | -43.7714 | 2025-09-29 14:30:00 | GOES-19 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 74.5 |
| deb627da-95f0-3fe7-a82a-ce428062a2f5 | -8.9456 | -51.6712 | 2025-09-29 14:30:00 | GOES-19 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 89.4 |
| 0080703e-76aa-310a-ac17-4bc12f0161d8 | -20.7334 | -57.8293 | 2025-09-29 14:30:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 73.8 |
| 351ebd88-e32e-33d4-8682-0b9b72991820 | -4.1204 | -44.2287 | 2025-09-29 14:30:00 | GOES-19 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 158.0 |
| 37434ecf-b2f8-3580-a6bc-4cf1fd818efd | -9.2821 | -45.733 | 2025-09-29 14:30:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 98.8 |
| 5833cb1d-a672-3755-a084-9dd6a6dd5301 | -5.7158 | -45.5162 | 2025-09-29 14:30:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 58.3 |
| d9500fa2-eb06-36d8-be23-c25ff5154c5d | -11.9782 | -47.1296 | 2025-09-29 14:30:00 | GOES-19 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 108.6 |
| 66a60ce0-c2e1-3609-8da2-b38195aee001 | -13.5933 | -48.0593 | 2025-09-29 14:30:00 | GOES-19 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 93.9 |
| 5b99c102-7c7d-3e7f-881b-0e3b4896b139 | -7.8165 | -46.9781 | 2025-09-29 14:30:00 | GOES-19 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 108.0 |
| fa5d0d72-3c1d-33c8-bd94-13fe2672fc2e | -5.8149 | -42.8167 | 2025-09-29 14:30:00 | GOES-19 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 67.1 |
| c897406f-c1e3-30f8-9680-8fb25b07608b | -6.797 | -44.0859 | 2025-09-29 14:30:00 | GOES-19 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 61.1 |
| 7ffe126d-d4ed-38ad-9f1c-01a721ee1c32 | -5.9183 | -45.8615 | 2025-09-29 14:30:00 | GOES-19 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 76.5 |
| 2ff02018-6135-366b-903a-871f2bdb8421 | -7.0481 | -45.1856 | 2025-09-29 14:30:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 72.9 |
| 8f8841ea-7fda-3e6e-9236-de2177fb91f3 | -11.4608 | -44.9739 | 2025-09-29 14:30:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 109.4 |
| 78da53d9-f46b-3ae0-9c82-59fd972c77fb | -14.6942 | -48.1557 | 2025-09-29 14:30:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 108.8 |
| 1ea37d07-e301-3636-83f4-8669a7df7555 | -7.4676 | -46.2974 | 2025-09-29 14:30:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 98.8 |
| 2af0bb6b-21dc-39b1-840b-8cd0b5d39b4d | -7.7416 | -46.9626 | 2025-09-29 14:30:00 | GOES-19 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 85.6 |
| f0dea5f1-6f7d-339e-a288-41a15c49bfe5 | -7.8019 | -48.3173 | 2025-09-29 14:30:00 | GOES-19 | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 205.0 |
| 920d7b49-6c74-3fb3-b5fb-fc33782b0074 | -11.6249 | -52.8416 | 2025-09-29 14:30:00 | GOES-19 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 89.9 |
| f9b5770e-361d-33f6-b515-8533761aeaeb | -10.7478 | -45.3942 | 2025-09-29 14:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 113.2 |
| 1baa5b9d-6562-301e-84c9-05805db4df0e | -8.5221 | -44.6535 | 2025-09-29 14:30:00 | GOES-19 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 93.3 |
| 903de03b-1488-35a9-adc2-014abd8eb2ae | -9.4005 | -54.7186 | 2025-09-29 14:30:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 80.5 |
| 532f12cd-ca66-3a29-9274-955410233df0 | -7.6062 | -47.3498 | 2025-09-29 14:30:00 | GOES-19 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 71.7 |
| be57f658-aa26-39df-a5e5-978678b08546 | -10.1628 | -50.464 | 2025-09-29 14:30:00 | GOES-19 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 86.0 |
| c166d549-7a61-3c49-a5e6-45857da1467c | -8.8893 | -51.6758 | 2025-09-29 14:30:00 | GOES-19 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 76.5 |
| 4f54e28a-5074-3f76-9b72-d26b264b98f0 | -10.6242 | -48.5167 | 2025-09-29 14:30:00 | GOES-19 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 76.1 |
| f0fa6885-ac08-3602-931b-0abb1848ffba | -5.7411 | -42.6812 | 2025-09-29 14:30:00 | GOES-19 | AGRICOLÂNDIA | PIAUÍ | Brasil | 2200103 | 22 | 33 | nan | nan | nan | Caatinga | 69.0 |
| 106ee2e5-126a-3dd9-b7ce-77f2a945f29e | -9.4194 | -54.697 | 2025-09-29 14:30:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 139.8 |
| c9b836ba-45f3-3433-a9f3-28a2dc6a6827 | -9.7264 | -47.7827 | 2025-09-29 14:30:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 129.2 |
| e238599c-025f-324b-8165-c82117c53630 | -15.5571 | -47.8764 | 2025-09-29 14:30:00 | GOES-19 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 110.4 |
| 144dc529-8a4d-30a0-970e-7b7fc7f58da1 | -15.5169 | -47.9284 | 2025-09-29 14:30:00 | GOES-19 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 74.1 |
| e3709726-7324-3868-9900-98df1bcfc98b | -7.3001 | -42.825 | 2025-09-29 14:30:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 85.6 |
| 728127c9-7e40-3670-8140-bb13ac39be72 | -6.2968 | -43.4331 | 2025-09-29 14:30:00 | GOES-19 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 70.6 |
| 8b26cdce-71bf-3e2d-aea6-8a160b85b247 | -12.887 | -44.6846 | 2025-09-29 14:30:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 193.2 |
| 24630cba-ace8-3d91-ad4a-6ee5265d51fa | -7.9816 | -47.3168 | 2025-09-29 14:30:00 | GOES-19 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 80.5 |
| 5176c574-fd13-3239-ac20-aedf451b8753 | -9.8848 | -45.9349 | 2025-09-29 14:30:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 64.9 |
| 37947de2-6e74-3cfb-84e2-cb3b6dcee960 | -7.8163 | -47.0003 | 2025-09-29 14:30:00 | GOES-19 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 196.6 |
| 5c4e2925-f65d-35e0-863a-3b7853e8eaea | -5.7294 | -43.9651 | 2025-09-29 14:30:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 69.6 |
| e79ed1b9-eecb-3a8b-8971-f71b5419635f | -12.9543 | -45.185 | 2025-09-29 14:30:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 256.5 |
| 0f9e62b6-39ba-3b7a-81c5-6f84c9d956f8 | -9.7451 | -47.8027 | 2025-09-29 14:30:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 163.0 |
| ff7dc368-d6a7-3405-93a7-843065fe8f8a | -7.5089 | -44.297 | 2025-09-29 14:30:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 120.2 |
| 9b05ac9d-8904-3d95-9a33-5dda889685fb | -7.2605 | -42.9939 | 2025-09-29 14:30:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 84.9 |
| f0550887-c9be-3c77-a0aa-b11e80151e97 | -10.4022 | -48.1476 | 2025-09-29 14:30:00 | GOES-19 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 66.0 |
| 360d5dc8-3f1b-30e4-a3a9-102080a83616 | -5.3647 | -42.8275 | 2025-09-29 14:30:00 | GOES-19 | NAZÁRIA | PIAUÍ | Brasil | 2206720 | 22 | 33 | nan | nan | nan | Caatinga | 75.6 |
| 4b73c3ee-b369-3da8-8d2d-4faf457fc1d9 | -5.572 | -44.8472 | 2025-09-29 14:30:00 | GOES-19 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 67.7 |
| 2e83eb37-c753-38d5-9213-6bf1101e626e | -9.301 | -45.7309 | 2025-09-29 14:30:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 72.1 |
| 39c7749c-ddb1-3766-aeeb-9362f99d3589 | -6.4789 | -45.887 | 2025-09-29 14:30:00 | GOES-19 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 228.3 |
| 6c1024ca-c4c0-3f6a-8c2f-fcd432170b96 | -9.764 | -47.8006 | 2025-09-29 14:30:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 71.0 |
| 68259b65-2516-3077-88eb-4decfa3d584c | -7.6064 | -47.3278 | 2025-09-29 14:30:00 | GOES-19 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 90.9 |
| b2a4a2a0-3d4d-3f2e-be80-455421839cea | -7.9008 | -44.5805 | 2025-09-29 14:30:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 85.0 |
| 188fd99b-4fb8-3ca3-9b99-8fa919603426 | -9.7643 | -47.7786 | 2025-09-29 14:30:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 88.0 |
| bc63c8a5-91c9-3f95-aa3b-adbeeefccfca | -9.4196 | -54.6767 | 2025-09-29 14:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 80.2 |
| e6fc1647-7591-3829-a189-bb7ca99a53c1 | -6.9108 | -43.9834 | 2025-09-29 14:30:00 | GOES-19 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 80.7 |
| 8ab8fc78-abc5-32ae-b271-89518ec0dc18 | -6.0623 | -42.466 | 2025-09-29 14:30:00 | GOES-19 | HUGO NAPOLEÃO | PIAUÍ | Brasil | 2204600 | 22 | 33 | nan | nan | nan | Caatinga | 87.5 |
| 76c5b658-4bc4-3080-b71d-c11a88244101 | -7.0293 | -45.1873 | 2025-09-29 14:30:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 79.7 |
| 229d9488-c5c4-3084-8e52-05eb2aabd192 | -6.2142 | -44.2041 | 2025-09-29 14:30:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 56.3 |
| a31aa02e-5bd6-3cab-8f39-7399592aaacb | -11.3834 | -45.0312 | 2025-09-29 14:30:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 136.1 |
| b50a3e40-c269-35e7-8281-76e89e465a94 | -23.2074 | -49.2138 | 2025-09-29 14:30:00 | GOES-19 | CERQUEIRA CÉSAR | SÃO PAULO | Brasil | 3511409 | 35 | 33 | nan | nan | nan | Cerrado | 132.9 |
| 0bcdd42b-9b85-3242-84ea-202d7899f961 | -7.9628 | -47.3184 | 2025-09-29 14:30:00 | GOES-19 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 65.4 |
| a95df4e3-e0a6-3a91-9ebb-5e170e0834cf | -20.7537 | -57.8265 | 2025-09-29 14:30:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 73.3 |
| d8b0350c-8686-35cd-a138-a48488cbcd27 | -11.807 | -48.2414 | 2025-09-29 14:30:00 | GOES-19 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 94.0 |
| 0d6c53fb-f82f-344a-84fd-b2fa94ba6b64 | -13.3154 | -50.7227 | 2025-09-29 14:30:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 71.5 |
| d0a22c2e-b1ca-3d06-8e4f-a3385e46603f | -9.8852 | -45.9122 | 2025-09-29 14:30:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 76.9 |
| 3e71dc12-1cac-3576-8be9-680a6460c333 | -9.7454 | -47.7806 | 2025-09-29 14:30:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 131.2 |
| 5071d135-1c38-3148-9f17-83077912ef7f | -11.3642 | -45.0339 | 2025-09-29 14:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 134.9 |
| 1a98d1de-cf12-3754-8e1a-289178abd11a | -7.8378 | -46.7544 | 2025-09-29 14:30:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 145.9 |
| d152ad9c-f940-3eb1-8323-61ab4fac7d82 | -6.4602 | -45.8884 | 2025-09-29 14:30:00 | GOES-19 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 110.3 |
| 60b07fad-18d2-3c8d-bc26-cb28f7127206 | -9.3708 | -47.556 | 2025-09-29 14:30:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 91.8 |
| a56ff7ab-d8c1-35f9-b26f-0fe73c8b4db8 | -7.0291 | -45.21 | 2025-09-29 14:30:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 76.1 |
| 39b229a7-cf5d-3efe-b051-7828dc78d0f1 | -10.6239 | -48.5386 | 2025-09-29 14:30:00 | GOES-19 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 76.4 |
| 389ceda3-d92e-3ae5-92a6-b1632976c105 | -5.8833 | -45.5945 | 2025-09-29 14:30:00 | GOES-19 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 56.3 |
| 9b1e19db-88ca-3acb-bd1d-477415404f33 | -6.6192 | -44.9493 | 2025-09-29 14:30:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 79.2 |
| d04b1ca6-db76-3483-8b47-3c31427684b4 | -6.0809 | -42.4881 | 2025-09-29 14:30:00 | GOES-19 | HUGO NAPOLEÃO | PIAUÍ | Brasil | 2204600 | 22 | 33 | nan | nan | nan | Caatinga | 110.6 |
| fc6d745a-9fc3-36d7-ae10-a6e0c87ca1d3 | -12.7637 | -50.4921 | 2025-09-29 14:30:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 92.1 |
| f56e7f37-4948-3a12-8207-470595ae172a | -9.4455 | -47.6144 | 2025-09-29 14:40:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 125.7 |


[Clique aqui para ver as próximas entradas](README100.md)
