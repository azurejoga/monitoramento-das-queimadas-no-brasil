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

## Dados Diários - Página 7

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| d1592842-e365-31eb-b8ad-f399a661f74b | -5.5423 | -44.18299 | 2025-09-12 00:11:00 | TERRA_M-M | GOVERNADOR LUIZ ROCHA | MARANHÃO | Brasil | 2104628 | 21 | 33 | nan | nan | nan | Cerrado | 8.5 |
| e2676544-c3c8-398b-9bb5-ac97c9bf644b | -6.44794 | -44.06668 | 2025-09-12 00:11:00 | TERRA_M-M | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 8.9 |
| 9c486230-1d7c-343b-99be-d17de687d82d | -9.66429 | -43.52889 | 2025-09-12 00:11:00 | TERRA_M-M | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 6.6 |
| e87c1071-4565-342c-8248-d4ef0b9ad5c8 | -9.85737 | -43.13351 | 2025-09-12 00:11:00 | TERRA_M-M | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 8.5 |
| 30665118-aa28-3dbf-a0a3-82a74acd2199 | -6.26665 | -43.48714 | 2025-09-12 00:11:00 | TERRA_M-M | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 19.7 |
| ee0f96b5-1f80-3f18-91b1-4cd29f463965 | -2.47657 | -47.6532 | 2025-09-12 00:13:00 | TERRA_M-M | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 8.0 |
| 7e42e9ef-66b8-38df-b52c-383bb0fad39e | -2.84022 | -48.83146 | 2025-09-12 00:13:00 | TERRA_M-M | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 7.8 |
| 5384680d-09cc-3f65-8903-7d2255c8c811 | -2.4425 | -47.32582 | 2025-09-12 00:13:00 | TERRA_M-M | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| ffea0fd4-abe4-305f-b3a7-6939aab8b6a3 | -2.84212 | -48.84563 | 2025-09-12 00:13:00 | TERRA_M-M | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 10.9 |
| f75a5172-4c04-3655-a6b6-25b9926f479d | -4.47772 | -48.10449 | 2025-09-12 00:13:00 | TERRA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 7.6 |
| 3fc02eea-4bbe-367e-9622-6a4340f424c3 | -4.35693 | -43.8049 | 2025-09-12 00:13:00 | TERRA_M-M | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 11.6 |
| 8c4ff642-68fa-33b9-acc8-acdb0aa82f02 | -3.38579 | -44.11628 | 2025-09-12 00:13:00 | TERRA_M-M | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Amazônia | 11.8 |
| ac28bb58-611d-3cc2-a73c-cf9cfb513aef | -3.69017 | -49.09478 | 2025-09-12 00:13:00 | TERRA_M-M | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 15.6 |
| b3de00c7-4c1a-335b-b43d-1ca430128a3d | -4.36573 | -43.80367 | 2025-09-12 00:13:00 | TERRA_M-M | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 5bd3ed9a-78c9-37d9-8b88-16dc22f792b8 | -3.22129 | -47.12523 | 2025-09-12 00:13:00 | TERRA_M-M | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 48.6 |
| a1588b04-db29-3cf1-9d1c-8d00c1fd87a6 | -3.07792 | -48.81572 | 2025-09-12 00:13:00 | TERRA_M-M | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 10.0 |
| b6016b29-2f75-3308-8abb-e437233178f8 | -2.47811 | -47.66469 | 2025-09-12 00:13:00 | TERRA_M-M | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| aaddbc71-d0eb-38a3-8e65-6ecf270a63b8 | -4.47946 | -48.11766 | 2025-09-12 00:13:00 | TERRA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 42.8 |
| 2f4bd5d2-2b4b-3713-98ba-1e5c5d11b38a | -4.63538 | -47.06086 | 2025-09-12 00:13:00 | TERRA_M-M | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 6.5 |
| bfd70faa-c5a9-3910-80ea-48add3feee16 | -3.25923 | -48.45018 | 2025-09-12 00:13:00 | TERRA_M-M | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 10.3 |
| 2b07ede3-2194-3d5c-925c-5adf3d50a662 | -3.31895 | -50.07166 | 2025-09-12 00:13:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 14.0 |
| debc5355-520b-3212-b6d2-bb1684dd7e7d | -3.69218 | -49.11002 | 2025-09-12 00:13:00 | TERRA_M-M | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 29.8 |
| f6ee3694-a7ef-3d11-b9af-643f45dfeaa5 | -5.27621 | -49.30154 | 2025-09-12 00:13:00 | TERRA_M-M | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 21.7 |
| 54c77c9d-27cd-39d1-ba66-8cf9babc5381 | -2.62768 | -46.83314 | 2025-09-12 00:13:00 | TERRA_M-M | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 12.0 |
| 14fcb757-a8d7-3e61-8570-8be16c9c5096 | -2.35732 | -48.41977 | 2025-09-12 00:13:00 | TERRA_M-M | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 92827933-e5a4-3773-84ec-a4aae1c90741 | -4.49013 | -48.11617 | 2025-09-12 00:13:00 | TERRA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 47.0 |
| 5ca372fa-6b5b-37c6-8bf5-e6be3c6d836e | -3.2244 | -47.13019 | 2025-09-12 00:13:00 | TERRA_M-M | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 76.1 |
| 68cb4225-42ac-392a-9f9e-fe3ef4ae74ca | -5.6461 | -51.86372 | 2025-09-12 00:13:00 | TERRA_M-M | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 19.4 |
| 1a949592-2dfd-3894-9f96-3b576bb84204 | -2.62914 | -46.8436 | 2025-09-12 00:13:00 | TERRA_M-M | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 10.4 |
| 8334e774-a44e-3f45-93e9-eba2c0cb3978 | -3.35186 | -39.28431 | 2025-09-12 00:13:00 | TERRA_M-M | TRAIRI | CEARÁ | Brasil | 2313500 | 23 | 33 | nan | nan | nan | Caatinga | 10.1 |
| 73ed4c7d-d8dc-39bb-afa5-150b66dc263c | -4.93459 | -45.59487 | 2025-09-12 00:13:00 | TERRA_M-M | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Cerrado | 14.3 |
| 0c627388-f298-310e-b125-9f272fc78857 | -2.44398 | -47.3368 | 2025-09-12 00:13:00 | TERRA_M-M | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 2b70ae3c-fea7-3ea0-98d2-531f376387cf | -1.53365 | -47.55735 | 2025-09-12 00:13:00 | TERRA_M-M | SÃO MIGUEL DO GUAMÁ | PARÁ | Brasil | 1507607 | 15 | 33 | nan | nan | nan | Amazônia | 7.5 |
| c287075f-b7d0-34ad-a10d-cf2e71506bdb | -4.63384 | -47.04946 | 2025-09-12 00:13:00 | TERRA_M-M | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 16.4 |
| 92be5eaa-b91c-3286-a429-b3e9bdd3f094 | -3.96774 | -44.45424 | 2025-09-12 00:13:00 | TERRA_M-M | SÃO MATEUS DO MARANHÃO | MARANHÃO | Brasil | 2111508 | 21 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 06b1fb9f-fad7-3b6f-a4b8-e798355098ab | -3.54196 | -43.58897 | 2025-09-12 00:13:00 | TERRA_M-M | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 58effa6d-c615-390c-8c6d-2489a5c64f8f | -4.69809 | -46.0919 | 2025-09-12 00:13:00 | TERRA_M-M | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 3eb7edf8-d96a-309a-9458-2a8f58b193e7 | -3.26105 | -48.4637 | 2025-09-12 00:13:00 | TERRA_M-M | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 28.9 |
| ba51ec62-5ccb-3fb8-8dcd-cb56ae856b0c | -4.89793 | -45.19272 | 2025-09-12 00:13:00 | TERRA_M-M | LAGO DA PEDRA | MARANHÃO | Brasil | 2105708 | 21 | 33 | nan | nan | nan | Cerrado | 13.3 |
| 94441f7c-4991-3780-9069-f5b5b42baeaf | -1.69248 | -48.05504 | 2025-09-12 00:13:00 | TERRA_M-M | BUJARU | PARÁ | Brasil | 1501907 | 15 | 33 | nan | nan | nan | Amazônia | 7.4 |
| 555dd784-d388-3435-910a-5b5adc6ffc13 | -3.22281 | -47.13614 | 2025-09-12 00:13:00 | TERRA_M-M | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 30.2 |
| 79eaa1a1-9a9e-3f3a-9f7c-409d9ecf4276 | -3.48588 | -50.72276 | 2025-09-12 00:13:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 16.6 |
| 0da8996b-f800-3224-a9a6-fc2cb7bc961b | -3.08102 | -48.82401 | 2025-09-12 00:13:00 | TERRA_M-M | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 9.5 |
| 1c6bf242-f7ac-3ced-8a16-9ee0a675b5de | -3.99165 | -43.2348 | 2025-09-12 00:13:00 | TERRA_M-M | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 97dde8c4-9897-3e79-b24d-b8ff8aabe285 | -12.8286 | -61.9551 | 2025-09-12 00:20:00 | GOES-19 | ALTO ALEGRE DOS PARECIS | RONDÔNIA | Brasil | 1100379 | 11 | 33 | nan | nan | nan | Amazônia | 125.9 |
| c3aa2cc3-e248-3b27-82cb-c933b6ee0873 | -9.057 | -47.0355 | 2025-09-12 00:20:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 56.3 |
| 5f9e5c64-8e11-3626-a9a8-96e53cee7372 | -11.6821 | -46.5632 | 2025-09-12 00:20:00 | GOES-19 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 102.6 |
| fccd4299-5aef-3ca1-9ae4-11ce114dfb2c | -11.9717 | -51.1427 | 2025-09-12 00:20:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 76.8 |
| ece8e0b5-ac4d-3de4-bd6e-b5b616e6b8a8 | -16.6133 | -49.7939 | 2025-09-12 00:20:00 | GOES-19 | NAZÁRIO | GOIÁS | Brasil | 5214408 | 52 | 33 | nan | nan | nan | Cerrado | 95.5 |
| c5107eea-7039-3ba6-b7ae-86b81c0f22b4 | 2.5064 | -61.039 | 2025-09-12 00:20:00 | GOES-19 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 41.6 |
| af48be30-d60f-3d1b-84d1-0558bba17ebd | -11.9907 | -51.1405 | 2025-09-12 00:20:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 62.2 |
| 85b0bf48-e49e-3372-acdc-cb8aa73cb89f | -16.5936 | -49.7972 | 2025-09-12 00:20:00 | GOES-19 | NAZÁRIO | GOIÁS | Brasil | 5214408 | 52 | 33 | nan | nan | nan | Cerrado | 64.2 |
| 6677fe78-1a78-31e5-a3d8-ca6b7c452a7d | -6.309 | -42.2311 | 2025-09-12 00:20:00 | GOES-19 | ELESBÃO VELOSO | PIAUÍ | Brasil | 2203503 | 22 | 33 | nan | nan | nan | Caatinga | 113.0 |
| d4a883e0-4370-3f7a-ba4a-948aeb4522a9 | -12.9292 | -54.7538 | 2025-09-12 00:20:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 80.5 |
| 1a7f8a86-1658-34f2-a1d6-109cd405a340 | -11.6825 | -46.5406 | 2025-09-12 00:20:00 | GOES-19 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 86.0 |
| 1e7537e5-d827-3db4-b251-a56a6f036d7a | -11.5263 | -50.404 | 2025-09-12 00:20:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 71.6 |
| cff8e8f6-140f-3629-9a46-d9b6454a5b0c | -6.3092 | -42.2072 | 2025-09-12 00:20:00 | GOES-19 | ELESBÃO VELOSO | PIAUÍ | Brasil | 2203503 | 22 | 33 | nan | nan | nan | Caatinga | 73.3 |
| 1eedc834-a9f6-3666-ad84-6aa01c6fb319 | -11.7016 | -46.5379 | 2025-09-12 00:20:00 | GOES-19 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 97.4 |
| 51c2cb32-efe9-3c25-b517-5c1a23f45f12 | -13.3238 | -44.0945 | 2025-09-12 00:20:00 | GOES-19 | SANTA MARIA DA VITÓRIA | BAHIA | Brasil | 2928109 | 29 | 33 | nan | nan | nan | Cerrado | 97.6 |
| f316a0c3-982f-378d-a63a-6c7bad635061 | -12.8649 | -62.1268 | 2025-09-12 00:20:00 | GOES-19 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 104.2 |
| f7a63914-fdf5-320a-b9f8-d517c256cc72 | -9.5137 | -54.6292 | 2025-09-12 00:20:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 68.6 |
| 127c3a74-956b-3c01-af70-9a733fcd9fb5 | -7.4236 | -50.6354 | 2025-09-12 00:20:00 | GOES-19 | BANNACH | PARÁ | Brasil | 1501253 | 15 | 33 | nan | nan | nan | Amazônia | 51.5 |
| 7f5339e5-c0e3-3ce0-a357-2b4153b08c57 | -9.2287 | -59.3823 | 2025-09-12 00:20:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 44.9 |
| c07e85c5-464e-3330-a0f1-b84bb1cb1fbb | -12.8475 | -61.9539 | 2025-09-12 00:20:00 | GOES-19 | ALTO ALEGRE DOS PARECIS | RONDÔNIA | Brasil | 1100379 | 11 | 33 | nan | nan | nan | Amazônia | 50.6 |
| 616d2e18-f0c0-3c4e-a8cc-3aeab42bb26a | -15.834 | -50.5361 | 2025-09-12 00:20:00 | GOES-19 | ITAPIRAPUÃ | GOIÁS | Brasil | 5211008 | 52 | 33 | nan | nan | nan | Cerrado | 37.5 |
| 797e6481-5a6f-3fff-b1ee-3186b5b53012 | -13.3243 | -44.0708 | 2025-09-12 00:20:00 | GOES-19 | SANTA MARIA DA VITÓRIA | BAHIA | Brasil | 2928109 | 29 | 33 | nan | nan | nan | Cerrado | 66.0 |
| 6bb837cd-da3a-3c1a-a70b-9f329630ddaf | -8.9563 | -46.0849 | 2025-09-12 00:20:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 107.8 |
| f6fda70b-8008-37e9-bdd3-ab48b4756ccc | -11.1809 | -55.0821 | 2025-09-12 00:20:00 | GOES-19 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 69.8 |
| 65b5f300-4dcb-3893-879d-6d5312a8b84d | -6.48 | -43.8822 | 2025-09-12 00:20:00 | GOES-19 | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 75.1 |
| 171263c7-405f-31ea-b66c-7f1d6547d59e | -9.0376 | -47.0819 | 2025-09-12 00:20:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 61.5 |
| a1d81e87-f7d3-3bc3-be59-984b039234ae | -9.2101 | -59.3833 | 2025-09-12 00:20:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 39.7 |
| bc02b252-f3c3-3944-9c30-16e1b1abb36a | -7.4049 | -50.6367 | 2025-09-12 00:20:00 | GOES-19 | BANNACH | PARÁ | Brasil | 1501253 | 15 | 33 | nan | nan | nan | Amazônia | 68.8 |
| a3966a33-4dc7-374b-ac57-2b278baed770 | -20.0192 | -47.6459 | 2025-09-12 00:20:00 | GOES-19 | CONQUISTA | MINAS GERAIS | Brasil | 3118205 | 31 | 33 | nan | nan | nan | Cerrado | 67.0 |
| e807ce70-da85-337b-9d20-928bc51e23ef | -21.9478 | -47.534 | 2025-09-12 00:20:00 | GOES-19 | DESCALVADO | SÃO PAULO | Brasil | 3513702 | 35 | 33 | nan | nan | nan | Cerrado | 75.6 |
| d58b9156-0503-3e82-8b40-8a39c8606922 | -23.1139 | -47.5156 | 2025-09-12 00:20:00 | GOES-19 | PORTO FELIZ | SÃO PAULO | Brasil | 3540606 | 35 | 33 | nan | nan | nan | Mata Atlântica | 68.1 |
| e8a9a5a4-6bae-3522-b232-d34efb738c0a | -12.8287 | -61.9358 | 2025-09-12 00:20:00 | GOES-19 | ALTO ALEGRE DOS PARECIS | RONDÔNIA | Brasil | 1100379 | 11 | 33 | nan | nan | nan | Amazônia | 67.1 |
| 9cd6326c-a379-38b6-95a3-fa680ba4779b | -8.9087 | -49.9433 | 2025-09-12 00:20:00 | GOES-19 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 65.4 |
| 3f99dbe6-9eba-3636-baa6-d2fd2219dfb1 | -21.9686 | -47.5287 | 2025-09-12 00:20:00 | GOES-19 | PIRASSUNUNGA | SÃO PAULO | Brasil | 3539301 | 35 | 33 | nan | nan | nan | Cerrado | 137.5 |
| ee91dd5a-4acb-3b4a-98bf-3c11d0b3f988 | -8.8899 | -49.945 | 2025-09-12 00:20:00 | GOES-19 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 180.4 |
| 1c2f3761-68ee-3932-90ab-d774ef75a399 | -12.8651 | -62.1074 | 2025-09-12 00:20:00 | GOES-19 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 60.4 |
| 653aa0da-b796-32a3-a5a5-380a6e5786c7 | -8.8901 | -49.9236 | 2025-09-12 00:20:00 | GOES-19 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 128.5 |
| 3a4211c1-0564-3db6-81d9-88afeb75e481 | -21.947 | -47.5578 | 2025-09-12 00:20:00 | GOES-19 | DESCALVADO | SÃO PAULO | Brasil | 3513702 | 35 | 33 | nan | nan | nan | Cerrado | 97.4 |
| 80f3bacc-c553-3a2e-88cc-9a4b35655f98 | -11.1998 | -55.0805 | 2025-09-12 00:20:00 | GOES-19 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 70.6 |
| 4096afba-eed4-3bdc-9962-c28963c359e1 | -8.1837 | -46.0965 | 2025-09-12 00:20:00 | GOES-19 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 48.1 |
| d680aeab-c7a1-34f9-86ee-d6bfd998052c | -12.8837 | -62.1449 | 2025-09-12 00:20:00 | GOES-19 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 55.4 |
| cdd6ce13-f18b-341b-8b09-2ba80d518589 | -21.9679 | -47.5525 | 2025-09-12 00:20:00 | GOES-19 | DESCALVADO | SÃO PAULO | Brasil | 3513702 | 35 | 33 | nan | nan | nan | Cerrado | 214.9 |
| 197ae46d-3153-3bfc-96ee-86bb0cb44341 | 2.5064 | -61.0201 | 2025-09-12 00:20:00 | GOES-19 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 49.1 |
| fd8b3708-0517-3325-89ae-f88ce7560d04 | -21.6291 | -53.9923 | 2025-09-12 00:20:00 | GOES-19 | NOVA ALVORADA DO SUL | MATO GROSSO DO SUL | Brasil | 5006002 | 50 | 33 | nan | nan | nan | Cerrado | 87.9 |
| b852a4b3-1595-3772-8b17-3b274b9cdb7f | -12.846 | -62.128 | 2025-09-12 00:20:00 | GOES-19 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 63.3 |
| 925b7dd4-5fda-3be4-a82f-bbfa5cfaf0c8 | -23.1358 | -47.4859 | 2025-09-12 00:20:00 | GOES-19 | PORTO FELIZ | SÃO PAULO | Brasil | 3540606 | 35 | 33 | nan | nan | nan | Mata Atlântica | 65.7 |
| 15a74e2d-6ab7-36e4-9830-e330f19b5f4a | -12.8647 | -62.1461 | 2025-09-12 00:20:00 | GOES-19 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 70.2 |
| 4de2c685-e95d-37ff-beb0-903777310f29 | -11.7012 | -46.5605 | 2025-09-12 00:20:00 | GOES-19 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 58.8 |
| 413c5715-6fb1-39a4-8859-16b0c86c5efb | -23.1146 | -47.4915 | 2025-09-12 00:20:00 | GOES-19 | PORTO FELIZ | SÃO PAULO | Brasil | 3540606 | 35 | 33 | nan | nan | nan | Mata Atlântica | 132.6 |
| ade9338b-a5b9-3aac-893d-c1e7123026d9 | -12.8839 | -62.1256 | 2025-09-12 00:20:00 | GOES-19 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 55.9 |
| b22ed855-861e-3bf6-a5e2-3e204a2e5cb4 | -21.6496 | -53.9886 | 2025-09-12 00:20:00 | GOES-19 | NOVA ALVORADA DO SUL | MATO GROSSO DO SUL | Brasil | 5006002 | 50 | 33 | nan | nan | nan | Cerrado | 85.6 |
| b0aa300e-00c1-3235-9ad0-0aa372a5045a | -16.6128 | -49.8161 | 2025-09-12 00:20:00 | GOES-19 | NAZÁRIO | GOIÁS | Brasil | 5214408 | 52 | 33 | nan | nan | nan | Cerrado | 55.6 |
| 3c204ba1-140d-329f-b0ea-bf1769b598b9 | -11.6828 | -46.5179 | 2025-09-12 00:20:00 | GOES-19 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 35.0 |
| 7877beae-4d01-3a5d-8025-8027a420e3e1 | -11.702 | -46.5153 | 2025-09-12 00:20:00 | GOES-19 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 60.4 |
| 53571109-315a-39a0-8285-532c74575555 | -22.6404 | -53.0946 | 2025-09-12 00:20:00 | GOES-19 | MARILENA | PARANÁ | Brasil | 4115002 | 41 | 33 | nan | nan | nan | Mata Atlântica | 60.2 |
| b75dd64b-acf7-3563-b112-97dad65c245f | -12.8649 | -62.1268 | 2025-09-12 00:30:00 | GOES-19 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 81.6 |


[Clique aqui para ver as próximas entradas](README8.md)
