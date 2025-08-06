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

## Dados Diários - Página 25

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| d08e7cce-334f-33a5-ad72-e7173bab1bca | -9.47442 | -57.84939 | 2025-08-06 05:12:00 | NOAA-21 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 0d69de59-adf5-3235-8905-e3a34270c490 | -8.9079 | -60.60325 | 2025-08-06 05:12:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 57.6 |
| 0d893f74-ead3-3fe2-9a1f-764f7e37fcca | -8.91239 | -60.57602 | 2025-08-06 05:12:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 18.2 |
| 6ddb85f7-78b0-318d-9016-0d770c7ac74b | -11.7367 | -47.52913 | 2025-08-06 05:12:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 1d8a074d-6531-3abc-a916-868168f26aca | -8.9843 | -45.6899 | 2025-08-06 05:12:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| d4e5ab91-7e18-3166-894b-2c790c74ba2d | -8.91936 | -60.57717 | 2025-08-06 05:12:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 9.0 |
| 00655e29-b173-3342-a043-f720660e8f05 | -8.92029 | -60.59328 | 2025-08-06 05:12:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 7b010096-d0fc-37e8-86e9-8d2597b4d188 | -8.91275 | -60.55209 | 2025-08-06 05:12:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 16.8 |
| d281faca-0d6c-3fee-a46f-93fd737cd505 | -9.18595 | -60.83313 | 2025-08-06 05:12:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| dd43b12d-3ba2-38b5-95f5-fc3221a742c5 | -9.71951 | -61.29539 | 2025-08-06 05:12:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| d20e20c1-ee41-3be4-92ba-ddb68ca8e906 | -8.90477 | -60.57877 | 2025-08-06 05:12:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 13.2 |
| 394f249b-1c19-39b1-a0c8-cc48f238a08b | -8.90514 | -60.55484 | 2025-08-06 05:12:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 61.2 |
| fd032ebc-8239-3893-9494-fd88376fd6d1 | -8.90991 | -60.54763 | 2025-08-06 05:12:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 6.2 |
| cb8d4a7f-5f8a-3183-9c0e-2776059a1130 | -9.50873 | -63.52834 | 2025-08-06 05:12:00 | NOAA-21 | ALTO PARAÍSO | RONDÔNIA | Brasil | 1100403 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3bacbd02-8bdf-3b27-b6e7-d728774d2039 | -8.62918 | -50.01443 | 2025-08-06 05:12:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| c3a587ec-12ef-3bcb-af82-b531045ca260 | -16.24982 | -39.04572 | 2025-08-06 05:12:00 | AQUA_M-M | SANTA CRUZ CABRÁLIA | BAHIA | Brasil | 2927705 | 29 | 33 | nan | nan | nan | Mata Atlântica | 7.0 |
| bbea8df1-0e41-33ab-8238-43733fe3efd3 | -8.91844 | -60.56099 | 2025-08-06 05:12:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 1a434815-32ca-3066-914e-4b0ecb479e56 | -9.71169 | -61.29829 | 2025-08-06 05:12:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 071dff27-b9a1-36e5-894a-0674f8dea3b2 | -10.62624 | -55.31194 | 2025-08-06 05:12:00 | NOAA-21 | COLÍDER | MATO GROSSO | Brasil | 5103205 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| bc23ff50-a25e-3e08-ba2c-3e7cf7875a95 | -8.91744 | -60.74214 | 2025-08-06 05:12:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 22.8 |
| 1dc3ea30-c135-3a80-9a53-b47a7620f397 | -9.07361 | -45.04969 | 2025-08-06 05:12:00 | NOAA-21 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 2.9 |
| f9296270-3356-3bb5-942c-f6ab3c2a19d7 | -8.91055 | -60.54373 | 2025-08-06 05:12:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 5c930bfe-f71c-3557-8cdb-e6ef47723398 | -8.91468 | -60.54041 | 2025-08-06 05:12:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 28.2 |
| 1c32af2e-c8bb-3bde-9b38-ec189d705ab2 | -8.9257 | -60.58219 | 2025-08-06 05:12:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| c31f5965-ec12-3e2e-993b-7e3ed00ba5a1 | -10.75699 | -60.74974 | 2025-08-06 05:12:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 12.1 |
| 488615e9-88a3-3383-80bc-745620931514 | -9.51158 | -46.73109 | 2025-08-06 05:12:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| bb24aef1-4027-3524-98b6-ca76e24ca84f | -8.91523 | -60.73363 | 2025-08-06 05:12:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d252b88b-9bda-3254-abf0-5b285621a844 | -12.53691 | -47.17193 | 2025-08-06 05:12:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 6b123e3d-fad4-3acc-960c-4859e93e821c | -11.43461 | -45.13684 | 2025-08-06 05:12:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 15.8 |
| f56bd197-52fe-3fe9-accb-753573830f0a | -11.69839 | -60.55754 | 2025-08-06 05:12:00 | NOAA-21 | PIMENTA BUENO | RONDÔNIA | Brasil | 1100189 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| d79d7bcf-8497-3115-83f2-f83715837f40 | -8.92129 | -60.56546 | 2025-08-06 05:12:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 42383ae6-50fa-3989-8a9a-2b2f27bff39e | -8.92064 | -60.56936 | 2025-08-06 05:12:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| c0f45cbc-8af8-3b0f-9d42-2b53e847c64e | -8.90826 | -60.57934 | 2025-08-06 05:12:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 18.2 |
| 61ddecd3-dc03-33f4-8518-436e732b4db6 | -10.12279 | -51.67488 | 2025-08-06 05:12:00 | NOAA-21 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 43e03b54-1f5b-3329-89ec-08d138f84e0d | -11.89792 | -44.97826 | 2025-08-06 05:12:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 3.3 |
| e72063e7-d84a-341c-8d57-b16047a68ffb | -9.18661 | -60.82917 | 2025-08-06 05:12:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 50eaa2b1-036a-31cd-8f8b-daa1fd3293e5 | -8.89586 | -60.58931 | 2025-08-06 05:12:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 23b65a35-faa1-3ebb-a3a1-9cc5668ac479 | -8.921 | -60.54543 | 2025-08-06 05:12:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 727ca193-e612-33bc-ba29-55ab3f064239 | -8.91404 | -60.54429 | 2025-08-06 05:12:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 21.3 |
| aa389f2e-44c9-3336-9660-1bef0c6571b1 | -8.91965 | -60.75066 | 2025-08-06 05:12:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 19.1 |
| c212a2c3-3e7e-3460-a433-00ded3d2cc79 | -7.59863 | -55.19627 | 2025-08-06 05:12:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 01544820-ab46-3136-81cf-5d7e84bc4238 | -6.63933 | -59.99946 | 2025-08-06 05:12:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 1c349a18-315b-3307-a2a1-d8792a88bb99 | -8.89871 | -60.59377 | 2025-08-06 05:12:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 5.9 |
| f71ef2b9-4a12-37e2-b3f7-1845aa659b4d | -8.90669 | -60.5671 | 2025-08-06 05:12:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 20.5 |
| befa19ea-2b58-34ed-ac5d-0fd17b5d9a34 | -11.90099 | -44.97782 | 2025-08-06 05:12:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 5773073d-90e7-3031-b3ba-3bbb8d1918d5 | -8.53844 | -47.48169 | 2025-08-06 05:12:00 | NOAA-21 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 5cebf870-d9d9-353d-98e0-104335187395 | -8.92442 | -60.58996 | 2025-08-06 05:12:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 6.2 |
| aaa1824d-f301-3505-b5cf-3e44238e2e57 | -11.90437 | -44.98516 | 2025-08-06 05:12:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 4.2 |
| ca0ca9ee-7a91-36f2-a86d-2c7b09321bf3 | -8.90192 | -60.57432 | 2025-08-06 05:12:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 13.2 |
| d6e163f9-ad87-3089-b3cb-fc42cd0340a2 | -11.87266 | -52.29821 | 2025-08-06 05:12:00 | NOAA-21 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d22a7b15-00d0-3d87-aaa8-7a67e3634326 | -9.85604 | -61.43044 | 2025-08-06 05:12:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| a5339dc1-60c1-3bec-9226-22e76be4f04b | -11.72939 | -47.52709 | 2025-08-06 05:12:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 2d8d3a03-ffb8-3888-9a96-9b624cc3f6f5 | -8.92285 | -60.57773 | 2025-08-06 05:12:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 02e93958-d1d6-3276-a254-26df3785770e | -8.90441 | -60.60267 | 2025-08-06 05:12:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 57.6 |
| 4eec948a-710e-33ee-97be-32f47f461cf8 | -8.92349 | -60.57383 | 2025-08-06 05:12:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 1ba7f1cf-8177-321e-8c38-4846ef6006ca | -8.90697 | -60.58712 | 2025-08-06 05:12:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 28.7 |
| 43be65f9-5535-38b6-b1b6-1bf95c04665f | -8.91268 | -60.59601 | 2025-08-06 05:12:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 23.5 |
| 3d198a34-3f05-347e-b522-7b19656e7a45 | -8.91966 | -60.59716 | 2025-08-06 05:12:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 8262faad-1604-3cf0-ba6f-3694a808674f | -11.48703 | -50.29206 | 2025-08-06 05:12:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 3d1b338d-02d6-33c8-8211-0fbc23f4bcd1 | -11.90843 | -54.78531 | 2025-08-06 05:12:00 | NOAA-21 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 1952b65b-ec7c-3f6d-b018-c0f10d9be95c | -8.87978 | -44.79189 | 2025-08-06 05:12:00 | NOAA-21 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 493fba35-0aa7-3572-a6bb-71cf3500c34f | -11.50166 | -50.29107 | 2025-08-06 05:12:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 07ffae0f-c5be-3fcc-ac4b-61836f426eda | -11.699 | -60.55382 | 2025-08-06 05:12:00 | NOAA-21 | PIMENTA BUENO | RONDÔNIA | Brasil | 1100189 | 11 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 61218ea2-1ad1-3c5a-8c2e-d83d8f76ab94 | -8.92257 | -60.55768 | 2025-08-06 05:12:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 1f4a0269-4492-369b-9048-8fa1a2c849cb | -9.70387 | -61.30119 | 2025-08-06 05:12:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| bc16eaa0-8eff-3e35-af0d-19b12f1b900f | -9.70812 | -61.29768 | 2025-08-06 05:12:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 64e01c50-8d5d-3b35-a710-7bfbebba6123 | -8.83377 | -47.6216 | 2025-08-06 05:12:00 | NOAA-21 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 563b0134-b72c-3de2-b46b-f3a2e68c32d4 | -9.69309 | -57.42383 | 2025-08-06 05:12:00 | NOAA-21 | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 63a2b888-a256-3d92-8957-9fc3ed44ca05 | -9.70702 | -51.95118 | 2025-08-06 05:12:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 97ad3a94-45a7-3cc9-8305-d638ae9c3e25 | -8.9089 | -60.57545 | 2025-08-06 05:12:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 18.2 |
| 409dc862-b036-3ae1-95ae-9ed361878b6f | -8.91752 | -60.54486 | 2025-08-06 05:12:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 21.3 |
| bcbf9d98-aa4f-32c5-bf40-b1708c81ddae | -8.834 | -47.6191 | 2025-08-06 05:12:00 | NOAA-21 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 121bb122-9e6d-3e02-b579-fe9ee07fe092 | -9.83229 | -60.75941 | 2025-08-06 05:12:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| b043a50f-cddd-304e-9243-a5829662277d | -8.92095 | -60.74274 | 2025-08-06 05:12:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 22.8 |
| d206ea5a-63de-36d5-8452-543f42d6f789 | -8.91488 | -60.60439 | 2025-08-06 05:12:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 23.6 |
| b707a315-1fcc-34e5-9ff0-eded0c0cc8e9 | -8.90862 | -60.55541 | 2025-08-06 05:12:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 61.2 |
| ff34ab7c-87db-3b47-aae1-72b1b70ac5ef | -8.92093 | -60.5894 | 2025-08-06 05:12:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 6.2 |
| e0140f53-6543-35b3-9d6d-21ec9edf9067 | -8.9045 | -60.55873 | 2025-08-06 05:12:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 84.4 |
| bbb3997c-82b2-358c-9336-c302eae0d14c | -8.51321 | -44.74588 | 2025-08-06 05:12:00 | NOAA-21 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 5a11e702-a836-320d-a5b8-70a71daa9c6e | -10.11096 | -58.2153 | 2025-08-06 05:12:00 | NOAA-21 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 21207114-cf10-3c55-abc3-efbb1c934700 | -8.84591 | -47.61932 | 2025-08-06 05:12:00 | NOAA-21 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 1b022ac5-4f73-3452-98b8-b4c487f7a1fb | -11.73124 | -47.52293 | 2025-08-06 05:12:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 6bae4149-46b8-3e5a-8ea3-5477cc6e6806 | -8.91204 | -60.59992 | 2025-08-06 05:12:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 23.6 |
| 02fbb894-70e5-3090-89c8-0f7799b1768c | -8.90541 | -60.57489 | 2025-08-06 05:12:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 13.2 |
| f8ba23b9-4b84-35b0-8433-752083e795b2 | -8.53363 | -47.46933 | 2025-08-06 05:12:00 | NOAA-21 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 8bd68f99-47e5-3d4f-8052-32dd853015ea | -8.92 | -60.57326 | 2025-08-06 05:12:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 4724cfd3-24fb-3963-9ece-2e6d45940f33 | -8.92698 | -60.57439 | 2025-08-06 05:12:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 4359f3a3-86c4-3c1a-abbe-137031b5e591 | -9.35353 | -58.8377 | 2025-08-06 05:12:00 | NOAA-21 | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| c6157159-8a71-3515-b9ef-30175bb52052 | -16.71539 | -49.4604 | 2025-08-06 05:14:00 | NOAA-21 | TRINDADE | GOIÁS | Brasil | 5221403 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| c9201aca-af32-344e-8887-47c4b649c832 | -13.07231 | -56.86245 | 2025-08-06 05:14:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 10.2 |
| 6dd97069-e176-3ade-b675-20e90911a053 | -13.07866 | -56.86737 | 2025-08-06 05:14:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 36e75bb0-1f10-3977-bb0f-fc4ab5b98d62 | -13.93594 | -54.07072 | 2025-08-06 05:14:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 8f772043-003d-3431-aa12-36f99426b7bf | -13.06621 | -56.86261 | 2025-08-06 05:14:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 7.1 |
| be2fa592-b287-3b0b-a7e1-975d20385d6e | -16.34592 | -50.35367 | 2025-08-06 05:14:00 | NOAA-21 | SÃO LUÍS DE MONTES BELOS | GOIÁS | Brasil | 5220108 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| cec8691a-7008-3b95-b2fa-6d5d750566ee | -13.0752 | -56.86685 | 2025-08-06 05:14:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 10.2 |
| 3b0ac5a7-7465-358a-82bb-0444b9fa49bb | -19.84612 | -51.19977 | 2025-08-06 05:14:00 | NOAA-21 | PARANAÍBA | MATO GROSSO DO SUL | Brasil | 5006309 | 50 | 33 | nan | nan | nan | Cerrado | 5.4 |
| af6f813c-8134-3baf-aadd-0e7adfabce35 | -13.06829 | -56.86581 | 2025-08-06 05:14:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 11.9 |
| d13f5386-75d6-3df6-84ad-bfd0b582ad0a | -13.05469 | -56.86877 | 2025-08-06 05:14:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 929f80fb-65e2-3b96-a648-89d7c092342d | -13.05757 | -56.87318 | 2025-08-06 05:14:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| fbfd0f2e-8201-370b-ad40-4cfcad63df28 | -13.0593 | -56.86155 | 2025-08-06 05:14:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 4.7 |


[Clique aqui para ver as próximas entradas](README26.md)
