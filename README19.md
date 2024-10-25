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
| cc0fd154-26b6-3975-907b-14fb39fe2c4f | -17.0014 | -57.3561 | 2024-10-25 02:46:41 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 91.9 |
| 6643a659-91e8-3797-b246-42e922b79465 | -17.0381 | -57.5155 | 2024-10-25 02:46:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 109.3 |
| 57015db3-ce1f-35a0-93dd-b5005d011dd9 | -17.039 | -57.454 | 2024-10-25 02:46:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 91.5 |
| 337f112f-f84b-3e56-b47e-8437ec0ac801 | -17.0586 | -57.4517 | 2024-10-25 02:46:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 95.4 |
| e13889a9-a312-325e-a7cd-400463c9148b | -17.0786 | -57.429 | 2024-10-25 02:46:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 89.3 |
| fc066ff1-4076-3b55-a759-ec2fd82ea6c3 | -16.9593 | -57.545 | 2024-10-25 02:46:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 85.0 |
| 62befff3-3ed6-357f-928b-52423dc0f3de | -17.2186 | -57.2485 | 2024-10-25 02:46:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 85.3 |
| 2d93127a-a4b4-3533-8fa3-db22981fce84 | -17.219 | -57.228 | 2024-10-25 02:46:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 81.7 |
| de4a9b4f-801e-3929-83ec-60ce5d62ea98 | -17.2383 | -57.2462 | 2024-10-25 02:46:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 82.9 |
| 325b9d49-2203-3757-bbcf-5c277c149d4e | -17.2386 | -57.2256 | 2024-10-25 02:46:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 106.1 |
| d00023be-30d1-3615-a0c2-a7419e2ecb5d | -17.2537 | -57.5108 | 2024-10-25 02:46:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 107.7 |
| f40c962d-8013-39c9-bc0d-679c8911a354 | -17.7644 | -57.532 | 2024-10-25 02:46:45 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 84.6 |
| fe8ac8d2-826c-38b6-9162-fdfe2ff56d29 | -17.7671 | -57.3673 | 2024-10-25 02:46:45 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 78.7 |
| a63c06f7-6794-3694-beaa-3381c48a55a9 | -17.8038 | -57.5273 | 2024-10-25 02:46:45 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 80.5 |
| cbb124d9-24fb-34cc-b4d3-80f90196559c | -17.8042 | -57.5067 | 2024-10-25 02:46:45 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 81.2 |
| f1502956-7452-38b3-bc72-8beea56ad74d | -17.9268 | -57.2447 | 2024-10-25 02:46:46 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 89.8 |
| 0a172dce-c3fc-3816-9250-e1c0ccc68f55 | -17.9071 | -57.2472 | 2024-10-25 02:46:46 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 93.3 |
| 9522f7ff-d267-3972-93be-ab7192e96481 | -17.9272 | -57.224 | 2024-10-25 02:46:46 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 92.8 |
| c2806a37-2a05-3182-8ca4-85299bfbc4fb | -17.9275 | -57.2034 | 2024-10-25 02:46:46 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 84.0 |
| 8bf54448-7557-31dc-a8e3-0563d892f90d | -18.0431 | -57.3745 | 2024-10-25 02:46:47 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 77.3 |
| 3ebc218f-fb87-3cc8-a011-29020a686f2e | -18.0434 | -57.3539 | 2024-10-25 02:46:47 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 79.9 |
| f53a22c7-a5d3-30de-a5ff-344d0ae637a1 | -18.0441 | -57.3126 | 2024-10-25 02:46:47 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 110.6 |
| 2dc9e239-9869-393e-b759-84b9c50a0992 | -18.1223 | -57.3647 | 2024-10-25 02:46:47 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 89.5 |
| 7e6b8ebe-17db-311d-a498-cad205d01546 | -18.1226 | -57.344 | 2024-10-25 02:46:47 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 85.6 |
| 0b246ad3-76ba-3b18-b494-d0ce0c6b9506 | -18.1421 | -57.3622 | 2024-10-25 02:46:47 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 60.5 |
| 525c22a1-dfa7-3416-bd33-f8b2879aeefe | -18.3398 | -56.2377 | 2024-10-25 02:46:48 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 111.8 |
| a9862780-b6e9-33d6-975f-ebd2bdb3afe8 | -18.3401 | -56.2168 | 2024-10-25 02:46:48 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 92.6 |
| ab786fa3-f8a4-3d84-b602-a0c5d9d25b24 | -18.3199 | -56.2404 | 2024-10-25 02:46:48 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 110.2 |
| 8c63157f-b424-37e2-b148-b582a1b3abcb | -18.3203 | -56.2195 | 2024-10-25 02:46:48 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 76.6 |
| 6ba35fe9-1522-3abf-89fb-14644cfdba3c | -1.0445 | -47.6237 | 2024-10-25 02:55:11 | GOES-16 | MARAPANIM | PARÁ | Brasil | 1504406 | 15 | 33 | nan | nan | nan | Amazônia | 56.3 |
| e5ac7d3c-e2ca-3478-be3a-2970fa416836 | -1.211 | -47.5999 | 2024-10-25 02:55:12 | GOES-16 | IGARAPÉ-AÇU | PARÁ | Brasil | 1503200 | 15 | 33 | nan | nan | nan | Amazônia | 44.5 |
| fc96188f-b185-3ecf-aa3c-6bc882df4f99 | -2.8145 | -49.2418 | 2024-10-25 02:55:21 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 62.4 |
| 8e59b996-e868-3f59-b16e-7bfd39a457fa | -2.8144 | -49.2631 | 2024-10-25 02:55:21 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 64.5 |
| 09d720b9-bff7-3d40-9a0e-25b5d80dfa82 | -2.796 | -49.2424 | 2024-10-25 02:55:21 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 55.2 |
| 09f20afe-88bb-3b3a-97d1-7365573cabc7 | -3.2136 | -46.7843 | 2024-10-25 02:55:23 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 73.8 |
| 60bf02e2-d1b6-3262-b3f5-7fd5ca1705d6 | -3.2135 | -46.8063 | 2024-10-25 02:55:23 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 138.1 |
| c6fafa0c-9140-3849-9dae-5babae0bd439 | -3.1949 | -46.807 | 2024-10-25 02:55:23 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 65.8 |
| a3a47a12-44bc-3c83-a09c-4bbbc826f501 | -3.9581 | -46.422 | 2024-10-25 02:55:28 | GOES-16 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 62.8 |
| c41cbdba-10e9-38cb-ae46-46c2e21da98d | -3.958 | -46.4442 | 2024-10-25 02:55:28 | GOES-16 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 62.3 |
| 4bbc19d6-7e70-35d3-99f7-3cebaca55238 | -4.2429 | -48.5474 | 2024-10-25 02:55:29 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 81.3 |
| a06d8bde-6a58-3abf-a401-cb331a281f8f | -6.5219 | -60.0457 | 2024-10-25 02:55:43 | GOES-16 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 65.4 |
| 9feaa9a7-14b8-3030-b863-4ca45041cdec | -5.1521 | -37.74126 | 2024-10-25 02:56:00 | NPP-375D | BARAÚNA | RIO GRANDE DO NORTE | Brasil | 2401453 | 24 | 33 | nan | nan | nan | Caatinga | 10.1 |
| dcd5d581-c11b-3301-a5e5-ffd1689815f5 | -5.15079 | -37.74841 | 2024-10-25 02:56:00 | NPP-375D | BARAÚNA | RIO GRANDE DO NORTE | Brasil | 2401453 | 24 | 33 | nan | nan | nan | Caatinga | 8.9 |
| 8433a208-f18a-3ab5-be9e-1a9c85d95e7c | -5.14489 | -37.73991 | 2024-10-25 02:56:00 | NPP-375D | BARAÚNA | RIO GRANDE DO NORTE | Brasil | 2401453 | 24 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 49b11212-cede-363c-a627-1c0de1716588 | -12.0012 | -63.9013 | 2024-10-25 02:56:14 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 120.0 |
| 4d176ed3-cc72-3d5c-a6d8-b6cbf7e61054 | -12.0011 | -63.9203 | 2024-10-25 02:56:14 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 79.4 |
| 5c533aca-43a6-3ddf-9447-7353c309020a | -11.9824 | -63.9022 | 2024-10-25 02:56:14 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 64.3 |
| dde5ef52-04b8-335e-adfe-da2e35f89270 | -11.9822 | -63.9213 | 2024-10-25 02:56:14 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 48.7 |
| 050a43b8-78fc-357a-9412-589728d8cbb4 | -12.478 | -63.1693 | 2024-10-25 02:56:16 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 70.4 |
| 546ea9c1-df17-3af2-bbea-76340b581cc1 | -12.4591 | -63.1704 | 2024-10-25 02:56:16 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 74.8 |
| d6591329-77d4-3a2d-914c-c18dbe9d8cea | -12.4589 | -63.1895 | 2024-10-25 02:56:16 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 58.9 |
| ee92da99-20de-3c5a-804b-8d4679d5b880 | -12.3782 | -63.8821 | 2024-10-25 02:56:16 | GOES-16 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 64.4 |
| 02cf9f59-3ffd-3ff6-84ee-49f6ce22f7c4 | -13.4959 | -61.6203 | 2024-10-25 02:56:22 | GOES-16 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 73.6 |
| b24ed518-87c3-35f1-a1a8-2f0055acd07b | -17.0586 | -57.4517 | 2024-10-25 02:56:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 94.5 |
| 5701c4a7-5b49-35c7-a9fd-3bd0f67270f4 | -17.039 | -57.454 | 2024-10-25 02:56:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 91.1 |
| 62c78db0-98c5-3a63-9d42-d48ca2c66deb | -17.0381 | -57.5155 | 2024-10-25 02:56:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 106.0 |
| 525ad371-b83d-361b-899c-8d8d0e3f5f9d | -17.0377 | -57.536 | 2024-10-25 02:56:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 83.2 |
| ad6c8d55-4573-3244-a054-a70a323d6671 | -16.9792 | -57.5223 | 2024-10-25 02:56:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 110.8 |
| 0d69b497-4f0d-3e8d-8356-76e9ed2b5803 | -16.9596 | -57.5245 | 2024-10-25 02:56:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 129.6 |
| 29f3eb1a-0e3e-376c-918b-db0aed0a06e9 | -16.9593 | -57.545 | 2024-10-25 02:56:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 84.6 |
| 17c9a45e-4f76-3d97-a2b9-23306911761e | -16.94 | -57.5268 | 2024-10-25 02:56:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 88.8 |
| 982252c8-75ed-3d56-b404-6ef45828644f | -17.2537 | -57.5108 | 2024-10-25 02:56:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 90.3 |
| 386705aa-3bee-30a8-8731-c16a8b4c0b5f | -17.2386 | -57.2256 | 2024-10-25 02:56:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 104.2 |
| 9e4d5a14-cbe8-3c73-86d7-c0d7dbd2dd42 | -17.219 | -57.228 | 2024-10-25 02:56:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 98.2 |
| dfd69ff3-dfc8-3e48-8c5f-9285b0a99d4b | -17.2186 | -57.2485 | 2024-10-25 02:56:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 94.3 |
| 253cd422-3030-3c30-b6ad-9c1a758d27d0 | -17.7644 | -57.532 | 2024-10-25 02:56:45 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 83.1 |
| 4b5e8260-48c4-3aa1-9c91-5ddf8ae1b543 | -17.9275 | -57.2034 | 2024-10-25 02:56:46 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 87.8 |
| c57a4360-0526-3706-bc78-4ac1c51e0568 | -17.9272 | -57.224 | 2024-10-25 02:56:46 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 94.3 |
| 59769a2f-70d6-3986-843b-afb3c2f62ef0 | -17.9268 | -57.2447 | 2024-10-25 02:56:46 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 87.6 |
| a6b415f6-acd0-334d-af92-c12abacb846e | -17.9071 | -57.2472 | 2024-10-25 02:56:46 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 87.6 |
| 94eeddfe-d88a-3564-8316-13bc5ef5fef5 | -17.9023 | -57.5359 | 2024-10-25 02:56:46 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 79.0 |
| 3792155b-ffe5-3634-beeb-69f43225ac96 | -18.1424 | -57.3415 | 2024-10-25 02:56:47 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 68.7 |
| 663857e5-4849-3eec-ba9d-c37cfcb37f2a | -18.1421 | -57.3622 | 2024-10-25 02:56:47 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 53.7 |
| 777c0160-ece9-3386-936b-ef0a3025efaf | -18.1226 | -57.344 | 2024-10-25 02:56:47 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 87.7 |
| 0c3e0a43-5f21-3b09-aadc-54bb3ca6d7e4 | -18.1223 | -57.3647 | 2024-10-25 02:56:47 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 79.1 |
| 754704dc-0443-3f4a-98da-c64d3dc3f424 | -18.0441 | -57.3126 | 2024-10-25 02:56:47 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 123.8 |
| 8cb475f9-009e-34d4-8775-f52b0db87202 | -18.3401 | -56.2168 | 2024-10-25 02:56:48 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 99.1 |
| 278fb230-4197-3bc1-ba96-fa3ad44f4446 | -18.3398 | -56.2377 | 2024-10-25 02:56:48 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 103.1 |
| 8f6d1f8f-3bda-3b85-adab-d8d60804330c | -18.3203 | -56.2195 | 2024-10-25 02:56:48 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 97.6 |
| e37627a0-509d-3f48-ae5b-cf01a492fc5c | -18.3199 | -56.2404 | 2024-10-25 02:56:48 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 137.1 |
| 1a11cfa3-c866-3548-83b2-fd0846e59530 | -18.3004 | -56.2222 | 2024-10-25 02:56:48 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 86.7 |
| 72640c58-d9b3-30ee-abe7-d2400821bbdc | -9.38401 | -38.30371 | 2024-10-25 02:58:00 | NPP-375D | GLÓRIA | BAHIA | Brasil | 2911402 | 29 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 2ae5838f-7b05-30da-a09a-efcb742d9cf8 | -9.37705 | -38.30222 | 2024-10-25 02:58:00 | NPP-375D | GLÓRIA | BAHIA | Brasil | 2911402 | 29 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 2bd9de6a-e76b-39d4-81aa-183633d119fd | -10.01139 | -36.38368 | 2024-10-25 02:58:00 | NPP-375D | TEOTÔNIO VILELA | ALAGOAS | Brasil | 2709152 | 27 | 33 | nan | nan | nan | Caatinga | 8.0 |
| 9d4f1f8f-085c-3951-b073-8d4224f824c2 | -10.07864 | -36.52059 | 2024-10-25 02:58:00 | NPP-375D | IGREJA NOVA | ALAGOAS | Brasil | 2703205 | 27 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 57e21e4f-48a6-388f-baa1-d5bd109b63f0 | -10.07771 | -36.52537 | 2024-10-25 02:58:00 | NPP-375D | IGREJA NOVA | ALAGOAS | Brasil | 2703205 | 27 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 9edda90d-9c9b-313f-9190-abea8dbfaa7c | -10.01044 | -36.38857 | 2024-10-25 02:58:00 | NPP-375D | TEOTÔNIO VILELA | ALAGOAS | Brasil | 2709152 | 27 | 33 | nan | nan | nan | Mata Atlântica | 5.4 |
| 1662e7ad-3f0a-3ede-9138-ca41da1b83d2 | -12.34592 | -38.0657 | 2024-10-25 02:58:00 | NPP-375D | ITANAGRA | BAHIA | Brasil | 2915908 | 29 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| e8df1af3-6970-3510-a15b-024ae7b30864 | -2.796 | -49.2424 | 2024-10-25 03:05:21 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 54.2 |
| c9eaf29c-41c2-3d82-a74b-32c95f91baf6 | -2.8144 | -49.2631 | 2024-10-25 03:05:21 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 63.0 |
| 41ba7247-a8ad-383f-add9-2248c469bd62 | -2.8145 | -49.2418 | 2024-10-25 03:05:21 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 74.3 |
| 11815fbe-f9c9-3411-99fc-3aedc22eec50 | -3.1949 | -46.807 | 2024-10-25 03:05:23 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 90.5 |
| bb2624b1-6776-3126-ae94-4bf5e4afb471 | -3.2135 | -46.8063 | 2024-10-25 03:05:23 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 129.2 |
| 4b1cc922-3fa2-3034-84b4-742322355602 | -3.9581 | -46.422 | 2024-10-25 03:05:28 | GOES-16 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 77.9 |
| ff279eb0-c5f9-3392-8ecd-ae0c1fc8aae4 | -4.2427 | -48.5689 | 2024-10-25 03:05:29 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 53.8 |
| decff271-4aa1-3dbb-8638-96e8f0d87f2d | -4.2429 | -48.5474 | 2024-10-25 03:05:29 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 88.6 |
| d0ee9fc6-ee27-3e0b-932e-88fd2550f2cd | -4.58 | -48.0132 | 2024-10-25 03:05:31 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 79.4 |
| a4c75e16-6119-38a7-8aa7-99783c37bbcc | -5.9788 | -45.3621 | 2024-10-25 03:05:39 | GOES-16 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 48.9 |
| 5c4d65ff-98be-3e11-8f48-c75bd50df66a | -6.5219 | -60.0457 | 2024-10-25 03:05:43 | GOES-16 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 69.9 |
| cfa29035-3f3c-36c9-af77-f9043304a5de | -12.0012 | -63.9013 | 2024-10-25 03:06:14 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 67.5 |


[Clique aqui para ver as próximas entradas](README20.md)
