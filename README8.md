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

## Dados Diários - Página 8

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 705e7bd3-134d-3a66-a91f-3166b1693793 | -9.4996 | -47.8068 | 2024-10-26 00:45:59 | GOES-16 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 88.9 |
| 2c42e9ab-63cf-303d-8e81-47be0cd32875 | -9.6346 | -47.5942 | 2024-10-26 00:46:00 | GOES-16 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 86.3 |
| e16046af-a7e0-3361-a37d-c49a411acec9 | -11.5037 | -45.8167 | 2024-10-26 00:46:10 | GOES-16 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 87.7 |
| 53cc231f-709b-39c7-b165-084f26916a23 | -11.5225 | -45.8369 | 2024-10-26 00:46:10 | GOES-16 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 91.4 |
| 1b75c457-5900-39ea-8b83-5a1dfa08a068 | -11.5228 | -45.814 | 2024-10-26 00:46:10 | GOES-16 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 95.4 |
| efaf43b1-0841-3e87-9679-16a7ecc779b7 | -16.9012 | -57.5108 | 2024-10-26 00:46:40 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 67.9 |
| b514f791-bbaf-3a77-9903-7dce41e84edc | -17.4214 | -39.9614 | 2024-10-26 00:46:41 | GOES-16 | MEDEIROS NETO | BAHIA | Brasil | 2921104 | 29 | 33 | nan | nan | nan | Mata Atlântica | 104.6 |
| 4f6a8813-ef2a-3b76-a642-292b7f1031b2 | -17.4222 | -39.9353 | 2024-10-26 00:46:41 | GOES-16 | TEIXEIRA DE FREITAS | BAHIA | Brasil | 2931350 | 29 | 33 | nan | nan | nan | Mata Atlântica | 145.5 |
| 93e4548a-c53f-3cea-8a3e-8a25426c88c4 | -17.4416 | -39.9559 | 2024-10-26 00:46:41 | GOES-16 | MEDEIROS NETO | BAHIA | Brasil | 2921104 | 29 | 33 | nan | nan | nan | Mata Atlântica | 80.9 |
| 23cce81c-31b9-3ecb-9929-a0bb30b16d32 | -17.4424 | -39.9298 | 2024-10-26 00:46:41 | GOES-16 | TEIXEIRA DE FREITAS | BAHIA | Brasil | 2931350 | 29 | 33 | nan | nan | nan | Mata Atlântica | 106.0 |
| 66f86696-1b8d-3d20-8cff-922617933997 | -16.94 | -57.5268 | 2024-10-26 00:46:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 52.9 |
| 4841c241-a4f4-3c0f-8d88-cfa886b6f17e | -17.0499 | -53.452 | 2024-10-26 00:46:41 | GOES-16 | ALTO GARÇAS | MATO GROSSO | Brasil | 5100409 | 51 | 33 | nan | nan | nan | Cerrado | 72.8 |
| dbafe8d6-9407-32b0-a4c6-b75f4c2dfe3e | -17.2733 | -57.5085 | 2024-10-26 00:46:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 41.8 |
| cf0b1839-c602-37f5-85c2-e45ad0ad67bb | -17.2537 | -57.5108 | 2024-10-26 00:46:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 56.0 |
| 6b64df8e-2010-34fb-a8f2-900c2e3f0cce | -17.254 | -57.4903 | 2024-10-26 00:46:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 73.7 |
| b80862ae-a6eb-31d1-997d-6e79cc551ad8 | -17.6667 | -57.4822 | 2024-10-26 00:46:45 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 87.2 |
| 9dbb1746-ed2a-35cf-9c29-149ce20fa268 | -17.6861 | -57.5004 | 2024-10-26 00:46:45 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 67.1 |
| b49ed6ba-2f1c-36ef-90d2-8427dea097ea | -17.6865 | -57.4798 | 2024-10-26 00:46:45 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 128.5 |
| 312a8171-e727-3994-b809-ca03be16d69d | -17.6868 | -57.4593 | 2024-10-26 00:46:45 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 45.8 |
| 4ce97471-112a-39cb-825e-bdac43fc219f | -17.7062 | -57.4774 | 2024-10-26 00:46:45 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 60.5 |
| fa2ea6dc-f17e-3656-80a3-2974aabafc4f | -17.7831 | -57.5914 | 2024-10-26 00:46:45 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 54.6 |
| 36fda0f9-6496-36cf-bc09-48fd1e86e72a | -18.0431 | -57.3745 | 2024-10-26 00:46:47 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 84.1 |
| 5cb811d4-e2bd-3dc6-b856-d196081e56ce | -18.0434 | -57.3539 | 2024-10-26 00:46:47 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 65.6 |
| fb0f5f00-d9cf-34dc-a26b-ea0a73aea87c | -18.0629 | -57.3721 | 2024-10-26 00:46:47 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 144.7 |
| c1784b5b-3c22-3aa5-bc9f-d644668784f7 | -18.0632 | -57.3514 | 2024-10-26 00:46:47 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 76.1 |
| 3c432ad9-4e04-3b42-a0cf-8fa864e0384f | -18.0653 | -57.2274 | 2024-10-26 00:46:47 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 75.1 |
| f95ccd91-cbf9-3a20-ba8d-368b9e5abd76 | -18.0827 | -57.3696 | 2024-10-26 00:46:47 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 145.4 |
| 52fd47df-e898-3936-89d1-85ddc9c0711c | -18.083 | -57.3489 | 2024-10-26 00:46:47 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 83.7 |
| e4a3079e-d417-3adf-9427-a39fd39302c5 | -18.1042 | -57.2638 | 2024-10-26 00:46:47 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 71.5 |
| 58f36faa-9392-3af5-97cd-3f36cc4c546e | -18.2649 | -55.9975 | 2024-10-26 00:46:48 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 55.8 |
| 9a30eb53-0af9-3a24-bb11-8a97e87c411c | -19.5264 | -56.7011 | 2024-10-26 00:46:54 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 82.0 |
| 86bf757f-5530-31ed-accf-897ae6f89cdf | -19.5465 | -56.6983 | 2024-10-26 00:46:54 | GOES-16 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 63.1 |
| f71d50e1-4406-31c7-b457-692ba0b53777 | -19.6067 | -56.6898 | 2024-10-26 00:46:55 | GOES-16 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 80.1 |
| 17d39525-aa82-3a82-9ade-05c54b724fa7 | -19.6264 | -56.7079 | 2024-10-26 00:46:55 | GOES-16 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 53.0 |
| 10b84df5-6102-38a7-8b2c-213e5e961451 | -19.6268 | -56.6869 | 2024-10-26 00:46:55 | GOES-16 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 132.8 |
| 767b15e5-d879-3815-8c3b-35cf06d50499 | -19.6272 | -56.6659 | 2024-10-26 00:46:55 | GOES-16 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 51.5 |
| d0d50da6-fbd1-3378-8220-1cf4ba3ddc96 | -19.6469 | -56.6841 | 2024-10-26 00:46:55 | GOES-16 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 64.9 |
| 95bacb95-77b1-3c95-80db-acf07b829fbc | -2.1929 | -53.7234 | 2024-10-26 00:55:18 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 75.7 |
| e6074204-8aaf-338f-8beb-cccda6bd9627 | -2.6949 | -51.7979 | 2024-10-26 00:55:21 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 42.8 |
| fd21db56-46d5-3d4e-a223-9ea24c4da4d5 | -2.8739 | -53.3252 | 2024-10-26 00:55:22 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 43.0 |
| ae9a9f0b-1e47-34df-9535-abe47be6a330 | -2.874 | -53.3049 | 2024-10-26 00:55:22 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 35.0 |
| ac825673-7459-30b9-8b1c-253d3aa792fa | -2.8923 | -53.3247 | 2024-10-26 00:55:22 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 36.4 |
| 753a4708-a5c7-3c2d-9fae-ae1037a58845 | -2.8924 | -53.3045 | 2024-10-26 00:55:22 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 20.1 |
| 09215530-b040-35c3-8959-325e7d0a5a8d | -2.9317 | -52.5713 | 2024-10-26 00:55:22 | GOES-16 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 22.4 |
| b9dfd63f-c8b9-3e2b-9eee-cc34c5d4632e | -2.9501 | -52.5708 | 2024-10-26 00:55:22 | GOES-16 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 48.2 |
| c58d641a-3b78-3b8f-b59c-40716cefd332 | -2.9578 | -50.4198 | 2024-10-26 00:55:22 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 20.2 |
| c6763d51-faf4-3cb5-8fec-282f19bd87f9 | -2.9661 | -53.2621 | 2024-10-26 00:55:22 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 17.0 |
| 0cebe7ff-26cf-3e66-ba72-0e1cc5c5bddb | -3.0932 | -53.7239 | 2024-10-26 00:55:23 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 24.3 |
| 63aefd8c-73ba-3f65-92d6-fc189f82428a | -3.1116 | -53.7234 | 2024-10-26 00:55:23 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 25.9 |
| ae27e97f-f1f6-359c-ba50-19c5f8ff457f | -3.1232 | -50.6033 | 2024-10-26 00:55:23 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 19.1 |
| 8531e004-92b3-3701-b5ad-597aa9e785d7 | -3.2368 | -45.8077 | 2024-10-26 00:55:23 | GOES-16 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 84.1 |
| 96fd1676-19d3-36e7-a5e3-4a40a086235d | -3.2553 | -45.807 | 2024-10-26 00:55:24 | GOES-16 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 62.6 |
| 36ad8e0f-fd55-31af-8445-dbffe9b4597f | -3.4729 | -43.3377 | 2024-10-26 00:55:25 | GOES-16 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 104.3 |
| 08eead7a-c47a-3c56-979d-61c2447b5177 | -3.473 | -43.3144 | 2024-10-26 00:55:25 | GOES-16 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 88.1 |
| b78c67d8-9e97-3c54-bf87-86bc1145edb7 | -3.4915 | -43.3368 | 2024-10-26 00:55:25 | GOES-16 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 64.2 |
| df8f013f-ecf5-3cfa-b697-eeb0df23a57a | -3.4917 | -43.3136 | 2024-10-26 00:55:25 | GOES-16 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 59.2 |
| 64d7c84f-f4c3-3f8d-b8b2-7697697cff23 | -3.4211 | -54.5787 | 2024-10-26 00:55:25 | GOES-16 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 19.9 |
| dbff2723-34ca-30d3-a9f2-b38fd770d4a9 | -3.5944 | -44.9606 | 2024-10-26 00:55:25 | GOES-16 | VITÓRIA DO MEARIM | MARANHÃO | Brasil | 2112902 | 21 | 33 | nan | nan | nan | Amazônia | 60.1 |
| 8a9f22a9-304c-3edc-bb63-8e8828a93c45 | -3.613 | -44.9598 | 2024-10-26 00:55:26 | GOES-16 | VITÓRIA DO MEARIM | MARANHÃO | Brasil | 2112902 | 21 | 33 | nan | nan | nan | Amazônia | 65.0 |
| 1e82f00c-7eff-3833-b4c5-61cdc772055a | -4.5613 | -48.0358 | 2024-10-26 00:55:31 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 118.2 |
| 30330515-3656-39cf-87f4-7d0bb8653f8e | -4.5614 | -48.0141 | 2024-10-26 00:55:31 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 132.0 |
| 62bf70e2-2d77-3215-8b85-2e56c9106199 | -4.5799 | -48.0349 | 2024-10-26 00:55:31 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 176.5 |
| 10ff19fd-7e13-34f2-a7d8-5f5a625c361a | -4.58 | -48.0132 | 2024-10-26 00:55:31 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 196.8 |
| 7a3fabbf-852c-3716-b4fe-037e5b86cb8d | -4.735 | -44.3999 | 2024-10-26 00:55:32 | GOES-16 | CAPINZAL DO NORTE | MARANHÃO | Brasil | 2102754 | 21 | 33 | nan | nan | nan | Cerrado | 24.0 |
| 8217a38f-dcd1-3492-8ea6-4ebf5e0656af | -7.6474 | -63.4584 | 2024-10-26 00:55:49 | GOES-16 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 53.2 |
| de738745-b37a-39cf-bd73-e5091599bb19 | -9.4996 | -47.8068 | 2024-10-26 00:55:59 | GOES-16 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 92.3 |
| 244e7ea4-5b94-3317-9457-25b3cfec4180 | -9.6343 | -47.6163 | 2024-10-26 00:56:00 | GOES-16 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 95.7 |
| 2ef7fe20-6ccc-39bb-bfd7-dd210ee27358 | -9.6346 | -47.5942 | 2024-10-26 00:56:00 | GOES-16 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 138.1 |
| 2a40c260-d2c2-365e-bce8-a0c670704801 | -11.5033 | -45.8396 | 2024-10-26 00:56:10 | GOES-16 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 73.3 |
| 432f50c9-6102-3745-bf2c-a03d9f1caabc | -11.5037 | -45.8167 | 2024-10-26 00:56:10 | GOES-16 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 114.7 |
| 80d5a10c-5477-34a8-b4f3-24a6d7d8c64a | -11.5225 | -45.8369 | 2024-10-26 00:56:10 | GOES-16 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 87.4 |
| 9b43a25a-4bde-3478-9843-1857321b2f62 | -11.5228 | -45.814 | 2024-10-26 00:56:10 | GOES-16 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 120.6 |
| 75de1ba2-d6d2-351c-a94a-74f5d707ddaf | -16.9012 | -57.5108 | 2024-10-26 00:56:40 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 75.0 |
| d3a79e68-c7a2-36ac-9a87-5513cd58568c | -16.94 | -57.5268 | 2024-10-26 00:56:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 53.0 |
| 5da10e92-0347-39c5-96eb-7adc725b1c75 | -17.0499 | -53.452 | 2024-10-26 00:56:41 | GOES-16 | ALTO GARÇAS | MATO GROSSO | Brasil | 5100409 | 51 | 33 | nan | nan | nan | Cerrado | 80.9 |
| 5fa394c2-91d7-31cb-9c09-4c1626542e4c | -17.2537 | -57.5108 | 2024-10-26 00:56:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 68.6 |
| 047a5a83-1d59-3c7f-8415-b7fba83f7669 | -17.254 | -57.4903 | 2024-10-26 00:56:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 74.7 |
| 21acf69f-9641-32bc-b730-6cfc3ae1fddc | -17.2733 | -57.5085 | 2024-10-26 00:56:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 54.3 |
| 76b255d1-0526-32f7-860c-bc633b9729da | -17.2737 | -57.488 | 2024-10-26 00:56:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 39.3 |
| 35f9a08b-b1ff-3f4d-8c9a-5f66a8da684e | -17.6667 | -57.4822 | 2024-10-26 00:56:45 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 88.3 |
| db073f08-2b19-3c76-8bf8-072eae14f2f0 | -17.7062 | -57.4774 | 2024-10-26 00:56:45 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 65.6 |
| 82ccd922-d702-3199-94f6-996eb13cd6e3 | -17.6865 | -57.4798 | 2024-10-26 00:56:45 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 139.2 |
| 25acb9af-6dea-3b3b-8ae3-6e9599f4bdcd | -18.0653 | -57.2274 | 2024-10-26 00:56:47 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 82.3 |
| 6350b32b-7e40-3414-b628-d09652216c3a | -18.2649 | -55.9975 | 2024-10-26 00:56:48 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 73.8 |
| 50d6933b-ee27-3684-bdc7-a476480a70cd | -19.6063 | -56.7108 | 2024-10-26 00:56:55 | GOES-16 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 47.2 |
| 61809106-fe83-340c-9f11-0e98495c3883 | -19.6067 | -56.6898 | 2024-10-26 00:56:55 | GOES-16 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 77.1 |
| 5ec95b81-0343-3402-8520-b1f584c2c44b | -19.6071 | -56.6688 | 2024-10-26 00:56:55 | GOES-16 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 47.5 |
| f9346107-7455-3950-a8a9-2b210f7b281d | -19.6264 | -56.7079 | 2024-10-26 00:56:55 | GOES-16 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 63.0 |
| ebe4ef55-aaf9-309f-9efb-dbbbf3c5df5a | -19.6268 | -56.6869 | 2024-10-26 00:56:55 | GOES-16 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 125.9 |
| 265e6941-a042-3932-98af-d47a11c8aaa9 | -19.6272 | -56.6659 | 2024-10-26 00:56:55 | GOES-16 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 57.5 |
| ab051fe2-7bcb-3837-8026-ccdee3b2c168 | -18.16171 | -41.27996 | 2024-10-26 01:05:00 | TERRA_M-M | ATALÉIA | MINAS GERAIS | Brasil | 3104700 | 31 | 33 | nan | nan | nan | Mata Atlântica | 21.8 |
| 6bf81d72-bfc5-3655-84f4-4b8a20034496 | -18.15599 | -41.28757 | 2024-10-26 01:05:00 | TERRA_M-M | ATALÉIA | MINAS GERAIS | Brasil | 3104700 | 31 | 33 | nan | nan | nan | Mata Atlântica | 27.2 |
| ef300908-e447-3c5f-9e75-c239036a5436 | -20.3068 | -55.37317 | 2024-10-26 01:05:00 | TERRA_M-M | DOIS IRMÃOS DO BURITI | MATO GROSSO DO SUL | Brasil | 5003488 | 50 | 33 | nan | nan | nan | Cerrado | 34.4 |
| 542b9560-f958-3e51-b95d-fa88e176114c | -19.62474 | -56.71685 | 2024-10-26 01:05:00 | TERRA_M-M | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 80.5 |
| db421883-8b2d-308f-a99b-88a4a94e0480 | -19.62214 | -56.69022 | 2024-10-26 01:05:00 | TERRA_M-M | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 119.5 |
| 66dffca1-2bc6-3354-bd67-286359e55edd | -19.6104 | -56.71837 | 2024-10-26 01:05:00 | TERRA_M-M | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 51.0 |
| bf446e02-7725-31bd-8a6f-86af5f268a77 | -19.54741 | -56.7037 | 2024-10-26 01:05:00 | TERRA_M-M | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 46.3 |
| 3d17c726-53b7-3a0d-833d-9a774957bc16 | -20.57791 | -57.76035 | 2024-10-26 01:05:00 | TERRA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 40.9 |
| 3d998e24-87c9-3bcc-a96e-6b20924f0021 | -17.78124 | -57.60771 | 2024-10-26 01:05:00 | TERRA_M-M | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 21.3 |
| 49fa6521-c3cd-353d-b26f-52719ca42d3d | -17.75992 | -57.54463 | 2024-10-26 01:05:00 | TERRA_M-M | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 24.3 |


[Clique aqui para ver as próximas entradas](README9.md)
