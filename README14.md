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

## Dados Diários - Página 14

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 9ba2e305-8799-3692-9451-3aaaf055af39 | -13.4618 | -51.1541 | 2025-08-26 01:10:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 144.5 |
| ebc1a0e4-69ff-3032-842d-5dea9b2be697 | -6.2275 | -60.018 | 2025-08-26 01:20:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 78.6 |
| c88cd6fa-6401-3657-8bbd-05eccf75423e | -6.9128 | -59.3578 | 2025-08-26 01:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 87.5 |
| f6726f1e-62a1-3f50-b4ac-523bc362806d | -11.1591 | -44.7395 | 2025-08-26 01:20:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 166.2 |
| d409ef04-d62f-3a1d-8dae-f61802fd21e5 | -20.8761 | -49.0468 | 2025-08-26 01:20:00 | GOES-19 | TABAPUÃ | SÃO PAULO | Brasil | 3552601 | 35 | 33 | nan | nan | nan | Mata Atlântica | 75.1 |
| 6313668f-c076-31ce-861d-478670f1833b | -7.4224 | -60.6236 | 2025-08-26 01:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 90.6 |
| dd8cf4be-1514-35be-a209-a12c35da5b75 | -11.5397 | -52.14 | 2025-08-26 01:20:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 323.1 |
| 6f125057-ee67-38eb-8759-0a4475ce8361 | -11.1396 | -44.7654 | 2025-08-26 01:20:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 110.5 |
| dcbf17a0-b5dd-3f96-93f4-ba7f3029b625 | -7.3854 | -64.3475 | 2025-08-26 01:20:00 | GOES-19 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 121.4 |
| aad66545-d19c-3309-88a5-91bafa585e73 | -9.191 | -59.4425 | 2025-08-26 01:20:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 79.0 |
| 7ff0cfec-8fcc-3f29-b956-d351223e055a | -4.9606 | -55.8028 | 2025-08-26 01:20:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 57.4 |
| 7e861c2e-0c33-3e66-8314-1726e2ef0208 | -8.9873 | -65.4379 | 2025-08-26 01:20:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 50.2 |
| 84fec897-a023-3c04-aa94-c2b521ba0aaf | -8.8734 | -62.4495 | 2025-08-26 01:20:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 77.0 |
| 7411e9c7-bc95-36f0-a094-57cf2e40d14d | -9.0415 | -65.7349 | 2025-08-26 01:20:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 39.3 |
| 8b30eaf0-fc4b-3b83-956c-2ebb3c4f06cb | -8.3396 | -50.5652 | 2025-08-26 01:20:00 | GOES-19 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 105.1 |
| a579b326-4993-341b-adc3-d57c50c638c2 | -11.559 | -52.117 | 2025-08-26 01:20:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 220.0 |
| 84a16a01-673a-361e-9ab1-4564d10fd859 | -7.367 | -64.348 | 2025-08-26 01:20:00 | GOES-19 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 72.6 |
| 7724a727-4d9a-323a-9a66-01421bd621f1 | -11.6351 | -44.8561 | 2025-08-26 01:20:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 89.9 |
| 67a1de6d-3207-3834-9ff9-ae822b54b9f1 | -7.3669 | -64.3667 | 2025-08-26 01:20:00 | GOES-19 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 45.6 |
| a6394c00-7c6a-35e4-bb9a-5bcea2c68c9f | -11.1779 | -44.76 | 2025-08-26 01:20:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 84.7 |
| 2e0caca1-7f9d-3999-bf33-7dfd11c802ee | -8.8548 | -62.4503 | 2025-08-26 01:20:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 221.4 |
| 88dcadc1-6a62-3b00-a300-10bc6a4bb6b8 | -15.0244 | -48.1689 | 2025-08-26 01:20:00 | GOES-19 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 88.2 |
| b4d257a1-26a5-3540-9775-dc4f18e27651 | -6.246 | -59.9982 | 2025-08-26 01:20:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 69.3 |
| d34c4c32-9929-3386-837c-bbae561c5ba8 | -6.7819 | -59.6711 | 2025-08-26 01:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 82.9 |
| bed6257f-dfee-38ba-a344-75ac17374455 | -14.2379 | -53.0492 | 2025-08-26 01:20:00 | GOES-19 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 42.7 |
| 197452e8-a286-31e6-aea1-e7ed4df9d912 | -6.6961 | -58.5546 | 2025-08-26 01:20:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 33.6 |
| 4259731e-c571-3c28-81aa-2c5daea75f60 | -4.9605 | -55.8226 | 2025-08-26 01:20:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 87.9 |
| 3319a51c-3322-3c12-ae91-10f5e6b2099b | -8.3394 | -50.5863 | 2025-08-26 01:20:00 | GOES-19 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 69.2 |
| 7f0ee5c3-14c4-381f-849d-3b1026e9e507 | -6.7144 | -58.5732 | 2025-08-26 01:20:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 30.1 |
| 8f2caf82-e1bb-3f24-aaf4-5ee37b75fd90 | -6.2459 | -60.0174 | 2025-08-26 01:20:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 134.1 |
| 47b51f1f-99da-3ba0-bd5e-2986eec1a9e0 | -9.1724 | -59.4436 | 2025-08-26 01:20:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 58.7 |
| 1db42930-27bd-35cc-bfa0-943c9a2a0cab | -9.1909 | -59.4619 | 2025-08-26 01:20:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 94.9 |
| 0058dd0d-b4ac-3a2d-b7d9-1ac2ca02097f | -6.2458 | -60.0365 | 2025-08-26 01:20:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 56.6 |
| b2759e79-97f8-3c6b-9d2b-f75bc66757c9 | -11.3126 | -55.1112 | 2025-08-26 01:20:00 | GOES-19 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 75.5 |
| 2e83a9d6-d09d-3439-9df8-533241e96ecb | -11.14 | -44.7422 | 2025-08-26 01:20:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 71.1 |
| 117eea0b-7b11-35e1-bc9b-08db053e4089 | -13.1644 | -45.2897 | 2025-08-26 01:20:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 52.1 |
| ae45299c-38df-3685-90c0-0871938cb83f | -8.3206 | -50.5879 | 2025-08-26 01:20:00 | GOES-19 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 63.8 |
| d96c9fd2-2c71-30d0-a04e-fb1a8ae8c4e8 | -8.855 | -62.4313 | 2025-08-26 01:20:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 86.8 |
| 41aa853e-c63f-3543-8663-487610c935ad | -8.8363 | -62.451 | 2025-08-26 01:20:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 87.6 |
| 0f789948-c3b0-3e31-8b0d-20d5a0b0399c | -6.9127 | -59.3771 | 2025-08-26 01:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 62.5 |
| a23eb763-c218-3066-b39a-56f486696608 | -11.5587 | -52.138 | 2025-08-26 01:20:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 331.8 |
| 8bfa6e16-6faf-3130-bb23-02768aaee7ee | -9.1677 | -40.6026 | 2025-08-26 01:20:00 | GOES-19 | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 64.4 |
| 2f3e30c3-f096-3d4b-bf31-86074bf1bdbd | -7.3854 | -64.3662 | 2025-08-26 01:20:00 | GOES-19 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 66.6 |
| ab5a1e8c-3ab1-3577-bb24-1b670e75659c | -8.9874 | -65.4192 | 2025-08-26 01:20:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 50.8 |
| cb783028-472d-3da6-8e14-cd7f1d1d7c5b | -6.7635 | -59.6718 | 2025-08-26 01:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 84.0 |
| d1ccb4d8-61a5-3947-8b56-50d19069f328 | -8.3209 | -50.5667 | 2025-08-26 01:20:00 | GOES-19 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 90.8 |
| d305e020-fd27-3ba6-9f99-b01109440026 | -6.766 | -62.8659 | 2025-08-26 01:20:00 | GOES-19 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 74.1 |
| 749928c8-1c05-3457-a332-2ecd03cc5c2c | -11.1587 | -44.7627 | 2025-08-26 01:20:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 334.4 |
| 6323baaf-6d69-32e8-9afe-1e76e6fc47b6 | -11.2937 | -55.1129 | 2025-08-26 01:20:00 | GOES-19 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 56.6 |
| 92945988-0639-3967-bd56-ff192861890a | -15.0439 | -48.1657 | 2025-08-26 01:20:00 | GOES-19 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 69.8 |
| 50e78d3e-5984-3fcf-a7b7-c7583283ca53 | -9.023 | -65.7355 | 2025-08-26 01:20:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 32.7 |
| cfc7bf0a-fe5e-3e5a-9fc1-232939b0a547 | -9.1722 | -59.4629 | 2025-08-26 01:20:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 79.8 |
| fd588c8d-d5ee-3fdb-b6d1-88471e7b7995 | -6.7476 | -62.8664 | 2025-08-26 01:20:00 | GOES-19 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 75.7 |
| 4260477c-bd53-311e-8388-11441c5cb429 | -20.8768 | -49.0237 | 2025-08-26 01:20:00 | GOES-19 | TABAPUÃ | SÃO PAULO | Brasil | 3552601 | 35 | 33 | nan | nan | nan | Mata Atlântica | 93.8 |
| cdf94568-1d9c-394e-9d4e-b9c4cb3329b8 | -11.1583 | -44.7859 | 2025-08-26 01:20:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 76.7 |
| 52d797f6-6f79-3360-90cb-1b3b9be061ff | -5.5281 | -60.2133 | 2025-08-26 01:20:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 43.7 |
| 89eb7341-0096-30f3-8718-70cd7a793b5b | -11.54 | -52.119 | 2025-08-26 01:20:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 224.6 |
| 51ded739-3205-30ad-a1b9-f5ba01d0ca42 | -4.9606 | -55.8028 | 2025-08-26 01:30:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 52.8 |
| 6dcafd0b-5cf8-3e4a-8716-944208b377ba | -8.3206 | -50.5879 | 2025-08-26 01:30:00 | GOES-19 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 55.6 |
| 461948cc-023d-38bf-8ba0-e348d779da66 | -9.1724 | -59.4436 | 2025-08-26 01:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 65.8 |
| 322d1ca6-b641-3186-8da2-ba824a32a161 | -13.4621 | -51.1327 | 2025-08-26 01:30:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 53.4 |
| 8b42ed8f-67de-3dc8-93bb-aab12361bce8 | -11.1583 | -44.7859 | 2025-08-26 01:30:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 76.5 |
| bcf51af5-a8d6-3e49-9709-5447d4302b79 | -6.2275 | -60.018 | 2025-08-26 01:30:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 82.8 |
| 37c034b6-8d29-3d55-891f-89c25ec5502e | -8.9873 | -65.4379 | 2025-08-26 01:30:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 50.6 |
| 3143e22f-a45d-3e36-8e33-d2aa79a9dcff | -8.8548 | -62.4503 | 2025-08-26 01:30:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 190.8 |
| 7425e3c7-37e9-3593-b0bf-579be766c474 | -9.1722 | -59.4629 | 2025-08-26 01:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 85.6 |
| b94f2b7f-c713-3049-9c5e-adb635b0c9e0 | -13.4425 | -51.1566 | 2025-08-26 01:30:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 235.9 |
| 4b497dd2-7a4c-359c-bee1-ff03b44422b0 | -6.7145 | -58.5539 | 2025-08-26 01:30:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 32.0 |
| 3dc11003-1b7d-3272-a4e1-cc5aeb736b18 | -9.0415 | -65.7349 | 2025-08-26 01:30:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 39.9 |
| c1755f11-2fc0-330b-a0fc-9a169077ca37 | -11.1587 | -44.7627 | 2025-08-26 01:30:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 282.7 |
| 779b82d7-bb2d-3d3d-8983-c5999bddd6ee | -11.1396 | -44.7654 | 2025-08-26 01:30:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 86.5 |
| 761dd753-c6da-30a8-8266-e78207bad9e2 | -4.9605 | -55.8226 | 2025-08-26 01:30:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 92.3 |
| db7870de-a1e5-3c8d-aaff-da59f7cef3b5 | -8.3396 | -50.5652 | 2025-08-26 01:30:00 | GOES-19 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 108.8 |
| 7578f2fe-eecc-3216-add8-ba25f3dfb245 | -11.54 | -52.119 | 2025-08-26 01:30:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 270.9 |
| 7693e7ce-bf54-3214-aeda-eef93d4b9c45 | -5.5281 | -60.2133 | 2025-08-26 01:30:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 47.0 |
| 3f3a2a64-047f-3225-8029-ed331c1931d7 | -6.7476 | -62.8664 | 2025-08-26 01:30:00 | GOES-19 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 85.9 |
| e349ff2c-b1dc-3a44-9b95-814c3914b0b9 | -13.4618 | -51.1541 | 2025-08-26 01:30:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 165.3 |
| 53f3e738-91a4-3657-a750-4c6e5fd3f1d5 | -8.8363 | -62.451 | 2025-08-26 01:30:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 90.7 |
| 9776c125-7b91-38c3-ad2c-4e7dfe73ca58 | -7.3854 | -64.3662 | 2025-08-26 01:30:00 | GOES-19 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 74.6 |
| 7f8df5d9-607a-39e1-b28d-5ee73f2adaf3 | -11.5587 | -52.138 | 2025-08-26 01:30:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 227.0 |
| e6383ea3-6f97-3a32-b0dc-fced23169dd3 | -6.7635 | -59.6718 | 2025-08-26 01:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 93.3 |
| d9c57c96-16ae-3937-886f-c37b9ea079d8 | -8.8734 | -62.4495 | 2025-08-26 01:30:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 72.9 |
| d9ab64e2-8142-3f1c-85f7-e44936f35a53 | -13.4614 | -51.1756 | 2025-08-26 01:30:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 57.7 |
| 49b91aee-1ee4-3b23-bffa-7f468428b054 | -13.4429 | -51.1351 | 2025-08-26 01:30:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 89.5 |
| 091df012-8f24-3b19-bc3d-6525e2627aa2 | -7.367 | -64.348 | 2025-08-26 01:30:00 | GOES-19 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 59.3 |
| f688b3a8-dcf1-3b63-8e0a-b917161789b8 | -8.855 | -62.4313 | 2025-08-26 01:30:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 88.4 |
| b443e636-e211-3837-a6fa-aabbeb6c6052 | -9.1909 | -59.4619 | 2025-08-26 01:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 84.1 |
| df2bbc38-ecf2-37c9-b64a-d27807130d7a | -8.3394 | -50.5863 | 2025-08-26 01:30:00 | GOES-19 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 63.5 |
| 848b82cb-1617-3d81-88a1-ba6078867a8e | -11.2937 | -55.1129 | 2025-08-26 01:30:00 | GOES-19 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 62.6 |
| 5830ae31-4fb7-3279-98ab-2717ddfbefe5 | -9.023 | -65.7355 | 2025-08-26 01:30:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 32.1 |
| 792de58f-2782-36f9-8ac6-e13c53b2158c | -13.4422 | -51.178 | 2025-08-26 01:30:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 63.5 |
| 1072dc35-d6ea-371c-b053-22df25b83072 | -9.191 | -59.4425 | 2025-08-26 01:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 75.6 |
| a284a2ce-5a38-35a4-a553-1dfb8632b598 | -20.8768 | -49.0237 | 2025-08-26 01:30:00 | GOES-19 | TABAPUÃ | SÃO PAULO | Brasil | 3552601 | 35 | 33 | nan | nan | nan | Mata Atlântica | 81.6 |
| 52c6023a-1b7b-3758-9731-28973ea90a21 | -11.559 | -52.117 | 2025-08-26 01:30:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 203.1 |
| 97714c13-43b8-3d06-b1e5-cf5f1d6be9af | -11.1591 | -44.7395 | 2025-08-26 01:30:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 130.1 |
| 68bd91e6-2916-3f66-a3a9-c20c67197069 | -11.5207 | -52.142 | 2025-08-26 01:30:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 46.5 |
| 9b1702ea-7df6-37d1-a770-e101cb48efb7 | -6.7819 | -59.6711 | 2025-08-26 01:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 77.5 |
| e53b995e-8edd-34d3-9439-023f04458d80 | -8.9874 | -65.4192 | 2025-08-26 01:30:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 51.8 |
| e74fe661-34b1-37c1-b37c-b64f002420fb | -7.4224 | -60.6236 | 2025-08-26 01:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 84.2 |
| bacc7767-0b6b-3d76-8d0b-72bc1db146ba | -6.766 | -62.8659 | 2025-08-26 01:30:00 | GOES-19 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 71.4 |


[Clique aqui para ver as próximas entradas](README15.md)
