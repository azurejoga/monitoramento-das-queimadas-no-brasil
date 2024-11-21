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

## Dados Diários - Página 10

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| d5441ef0-92da-3d89-9ea7-2db1cb248c17 | -3.295 | -53.8597 | 2024-11-21 03:10:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 61.8 |
| abc5b0f1-baac-33d8-ae06-a2fa7f9b7c37 | -4.5799 | -48.0349 | 2024-11-21 03:10:00 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 91.7 |
| 390bcbac-dd1f-3e14-bb33-c419c261b0e9 | -4.2388 | -46.1197 | 2024-11-21 03:10:00 | GOES-16 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 190.2 |
| e4523928-f23b-3b12-b24b-893a24db45c1 | -6.8258 | -46.7737 | 2024-11-21 03:10:00 | GOES-16 | SÃO PEDRO DOS CRENTES | MARANHÃO | Brasil | 2111573 | 21 | 33 | nan | nan | nan | Cerrado | 72.8 |
| 9171c28b-7323-34a7-98c6-37344d467f7e | -8.2115 | -41.0205 | 2024-11-21 03:10:00 | GOES-16 | ACAUÃ | PIAUÍ | Brasil | 2200053 | 22 | 33 | nan | nan | nan | Caatinga | 76.2 |
| 5d61b0c9-c701-3621-9df5-394794a73482 | -4.7717 | -44.4891 | 2024-11-21 03:10:00 | GOES-16 | SANTO ANTÔNIO DOS LOPES | MARANHÃO | Brasil | 2110302 | 21 | 33 | nan | nan | nan | Cerrado | 152.2 |
| 3e5b10a8-dd8c-37ed-9c7e-fd5311ef7c6a | -4.7715 | -44.512 | 2024-11-21 03:10:00 | GOES-16 | SANTO ANTÔNIO DOS LOPES | MARANHÃO | Brasil | 2110302 | 21 | 33 | nan | nan | nan | Cerrado | 74.7 |
| 91d07247-11e8-3e2f-9567-456094cf0903 | -4.58 | -48.0132 | 2024-11-21 03:10:00 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 134.4 |
| 77ea89dc-cfde-34ba-8940-9e4d754a38bf | -3.2951 | -53.8395 | 2024-11-21 03:10:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 79.4 |
| c85ba199-b896-3572-a2f0-f60efd0225a4 | -3.7611 | -52.4037 | 2024-11-21 03:10:00 | GOES-16 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 35.4 |
| 3cdb7c92-9b0f-3a3b-89dc-bdcc4e241530 | -2.0259 | -54.5289 | 2024-11-21 03:10:00 | GOES-16 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 113.3 |
| 517c0081-1206-3199-8016-3c4ea1d9d89f | -4.15247 | -42.02889 | 2024-11-21 03:14:00 | NOAA-20 | BATALHA | PIAUÍ | Brasil | 2201507 | 22 | 33 | nan | nan | nan | Caatinga | 11.3 |
| e2c3dacc-a20d-31e3-b09e-dc8e853c2d70 | -3.79316 | -40.99771 | 2024-11-21 03:14:00 | NOAA-20 | TIANGUÁ | CEARÁ | Brasil | 2313401 | 23 | 33 | nan | nan | nan | Caatinga | 2.1 |
| f92b1e72-9295-3788-9cdb-05fce8eb1018 | -6.7987 | -35.17503 | 2024-11-21 03:14:00 | NOAA-20 | MAMANGUAPE | PARAÍBA | Brasil | 2508901 | 25 | 33 | nan | nan | nan | Mata Atlântica | 3.5 |
| dfffd026-ecbf-3f1b-89cc-221eb15b23fb | -6.9207 | -34.91653 | 2024-11-21 03:14:00 | NOAA-20 | LUCENA | PARAÍBA | Brasil | 2508604 | 25 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 7605d98e-a155-38ba-a15b-7d5eeaae15eb | -6.79798 | -35.1792 | 2024-11-21 03:14:00 | NOAA-20 | MAMANGUAPE | PARAÍBA | Brasil | 2508901 | 25 | 33 | nan | nan | nan | Mata Atlântica | 3.5 |
| 710a7725-ae2a-3d4c-a465-7efe157f43c7 | -4.15055 | -42.02098 | 2024-11-21 03:14:00 | NOAA-20 | BATALHA | PIAUÍ | Brasil | 2201507 | 22 | 33 | nan | nan | nan | Caatinga | 9.2 |
| a15de779-2931-3211-be69-c43d270e5a14 | -6.90792 | -34.89899 | 2024-11-21 03:14:00 | NOAA-20 | LUCENA | PARAÍBA | Brasil | 2508604 | 25 | 33 | nan | nan | nan | Mata Atlântica | 3.3 |
| 09f85441-2734-3811-94b0-f1a2374f1f6e | -6.79434 | -35.17426 | 2024-11-21 03:14:00 | NOAA-20 | MAMANGUAPE | PARAÍBA | Brasil | 2508901 | 25 | 33 | nan | nan | nan | Mata Atlântica | 3.5 |
| 100f4459-eeef-3787-b1e9-13f9bfc15648 | -6.91808 | -34.91742 | 2024-11-21 03:14:00 | NOAA-20 | LUCENA | PARAÍBA | Brasil | 2508604 | 25 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 89d3530d-5afd-365e-bfa9-d6568afcefc4 | -4.15372 | -42.02179 | 2024-11-21 03:14:00 | NOAA-20 | BATALHA | PIAUÍ | Brasil | 2201507 | 22 | 33 | nan | nan | nan | Caatinga | 11.3 |
| cb8be5fc-4978-3406-8d62-c625f8cbe444 | -4.15761 | -42.02235 | 2024-11-21 03:14:00 | NOAA-20 | BATALHA | PIAUÍ | Brasil | 2201507 | 22 | 33 | nan | nan | nan | Caatinga | 9.2 |
| ec40798b-ba24-39fc-9584-75e098b683ec | -3.79211 | -41.00377 | 2024-11-21 03:14:00 | NOAA-20 | TIANGUÁ | CEARÁ | Brasil | 2313401 | 23 | 33 | nan | nan | nan | Caatinga | 2.4 |
| a0ebd3b1-fcab-3a95-90fc-a76c06c2051b | -4.15632 | -42.02939 | 2024-11-21 03:14:00 | NOAA-20 | BATALHA | PIAUÍ | Brasil | 2201507 | 22 | 33 | nan | nan | nan | Caatinga | 13.8 |
| dd121e32-5a8a-3aa4-b4dd-732a1ddb85b3 | -8.845 | -35.70185 | 2024-11-21 03:17:00 | NOAA-20 | MARAIAL | PERNAMBUCO | Brasil | 2609204 | 26 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 5f3e1b22-40c2-3993-a693-eb7fedf3393e | -8.21702 | -41.01364 | 2024-11-21 03:17:00 | NOAA-20 | ACAUÃ | PIAUÍ | Brasil | 2200053 | 22 | 33 | nan | nan | nan | Caatinga | 6.5 |
| 4900d44b-446b-3830-a732-07fea21a3094 | -10.45166 | -40.38382 | 2024-11-21 03:17:00 | NOAA-20 | CAMPO FORMOSO | BAHIA | Brasil | 2906006 | 29 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 8335c832-e410-3e96-84cb-ff80b0745eb3 | -8.84427 | -35.70609 | 2024-11-21 03:17:00 | NOAA-20 | MARAIAL | PERNAMBUCO | Brasil | 2609204 | 26 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| bfc46f39-cb72-3d42-8f65-837696256f68 | -8.2197 | -41.01555 | 2024-11-21 03:17:00 | NOAA-20 | ACAUÃ | PIAUÍ | Brasil | 2200053 | 22 | 33 | nan | nan | nan | Caatinga | 13.8 |
| 7005eabf-16f9-3b19-b930-2a4a41c440ae | -8.86509 | -35.71742 | 2024-11-21 03:17:00 | NOAA-20 | MARAIAL | PERNAMBUCO | Brasil | 2609204 | 26 | 33 | nan | nan | nan | Mata Atlântica | 5.3 |
| 0a0c62f6-143e-38b2-8fb1-8908f3da4c57 | -8.22321 | -41.01521 | 2024-11-21 03:17:00 | NOAA-20 | ACAUÃ | PIAUÍ | Brasil | 2200053 | 22 | 33 | nan | nan | nan | Caatinga | 6.5 |
| 0143817f-9a8d-38c6-b281-351134c38772 | -7.15971 | -35.20202 | 2024-11-21 03:17:00 | NOAA-20 | SAPÉ | PARAÍBA | Brasil | 2515302 | 25 | 33 | nan | nan | nan | Mata Atlântica | 9.3 |
| d11429a1-4626-3e7a-877e-d6fbd81a1311 | -10.45738 | -40.38538 | 2024-11-21 03:17:00 | NOAA-20 | CAMPO FORMOSO | BAHIA | Brasil | 2906006 | 29 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 61586218-3bb4-3e83-87f8-cdd0fe7ecb42 | -17.58791 | -43.29042 | 2024-11-21 03:17:00 | NOAA-20 | DIAMANTINA | MINAS GERAIS | Brasil | 3121605 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| eb73f4c7-657d-30b2-b1b6-10fcfa771abe | -8.22593 | -41.01696 | 2024-11-21 03:17:00 | NOAA-20 | ACAUÃ | PIAUÍ | Brasil | 2200053 | 22 | 33 | nan | nan | nan | Caatinga | 3.5 |
| 0702a587-97bd-3391-801d-0d739c7b59c5 | -6.64315 | -41.99824 | 2024-11-21 03:17:00 | NOAA-20 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 57c44d7f-df5e-36c3-a0f8-1fb789bdf7b0 | -17.58183 | -43.28902 | 2024-11-21 03:17:00 | NOAA-20 | DIAMANTINA | MINAS GERAIS | Brasil | 3121605 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 46cd7c76-91b2-346b-84bc-69634aa8df0d | -6.66005 | -39.24313 | 2024-11-21 03:17:00 | NOAA-20 | VÁRZEA ALEGRE | CEARÁ | Brasil | 2314003 | 23 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 0a6c9395-8a22-38cf-a0a4-6226ce8a7435 | -8.8447 | -35.70507 | 2024-11-21 03:17:00 | NOAA-20 | MARAIAL | PERNAMBUCO | Brasil | 2609204 | 26 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 7023509f-c3d7-33fc-a36a-854bd87f228f | -10.76031 | -37.1244 | 2024-11-21 03:17:00 | NOAA-20 | MARUIM | SERGIPE | Brasil | 2804003 | 28 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| dc45c573-0e3d-33e8-9bf8-780e6731f97f | -7.16043 | -35.19777 | 2024-11-21 03:17:00 | NOAA-20 | SAPÉ | PARAÍBA | Brasil | 2515302 | 25 | 33 | nan | nan | nan | Mata Atlântica | 9.3 |
| 6aa932b6-bbfd-3d9c-b2a6-b190c35bdfd3 | -18.42603 | -40.55497 | 2024-11-21 03:17:00 | NOAA-20 | NOVA VENÉCIA | ESPÍRITO SANTO | Brasil | 3203908 | 32 | 33 | nan | nan | nan | Mata Atlântica | 3.6 |
| ac2d2bce-3498-3cf6-8390-a932d0fcb4b2 | -7.36121 | -35.10956 | 2024-11-21 03:17:00 | NOAA-20 | PEDRAS DE FOGO | PARAÍBA | Brasil | 2511202 | 25 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 5ecb9bb4-eeec-33a4-80d6-673e012ea2de | -8.22223 | -41.02032 | 2024-11-21 03:17:00 | NOAA-20 | ACAUÃ | PIAUÍ | Brasil | 2200053 | 22 | 33 | nan | nan | nan | Caatinga | 6.5 |
| cfa1f6e4-1041-3a11-8aae-a225e0ffbe0e | -7.37001 | -35.21417 | 2024-11-21 03:17:00 | NOAA-20 | JURIPIRANGA | PARAÍBA | Brasil | 2507903 | 25 | 33 | nan | nan | nan | Mata Atlântica | 6.1 |
| 770b5d54-1b6c-302c-a8fb-7ad7090b8ab6 | -8.074 | -34.97915 | 2024-11-21 03:17:00 | NOAA-20 | RECIFE | PERNAMBUCO | Brasil | 2611606 | 26 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| 50aa1f81-cf0b-35f2-8fa7-0ac0eae25d8f | -18.42667 | -40.55185 | 2024-11-21 03:17:00 | NOAA-20 | NOVA VENÉCIA | ESPÍRITO SANTO | Brasil | 3203908 | 32 | 33 | nan | nan | nan | Mata Atlântica | 3.3 |
| b380ad82-3d16-3c90-9481-65e6b9e1ef74 | -18.42731 | -40.54874 | 2024-11-21 03:17:00 | NOAA-20 | NOVA VENÉCIA | ESPÍRITO SANTO | Brasil | 3203908 | 32 | 33 | nan | nan | nan | Mata Atlântica | 3.3 |
| 882b48e1-4a4e-30cf-a551-53b03f2607f7 | -7.11105 | -35.2501 | 2024-11-21 03:17:00 | NOAA-20 | SAPÉ | PARAÍBA | Brasil | 2515302 | 25 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 76f0414e-aa82-3a88-938e-c7f0a41895c3 | -7.16477 | -35.19862 | 2024-11-21 03:17:00 | NOAA-20 | SAPÉ | PARAÍBA | Brasil | 2515302 | 25 | 33 | nan | nan | nan | Mata Atlântica | 9.3 |
| 57b5bd7f-cf46-3893-ab53-22011387ebb0 | -18.43173 | -40.55302 | 2024-11-21 03:17:00 | NOAA-20 | NOVA VENÉCIA | ESPÍRITO SANTO | Brasil | 3203908 | 32 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 4e4f3e75-03a8-392b-82a1-f62ed23e3432 | -7.16405 | -35.20286 | 2024-11-21 03:17:00 | NOAA-20 | SAPÉ | PARAÍBA | Brasil | 2515302 | 25 | 33 | nan | nan | nan | Mata Atlântica | 9.3 |
| 3a9bc6b7-93d1-36ab-a756-623e7949e412 | -9.10502 | -35.44895 | 2024-11-21 03:17:00 | NOAA-20 | PORTO DE PEDRAS | ALAGOAS | Brasil | 2707404 | 27 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| b4461fad-58d9-3dae-9bfc-d0ade2975ee4 | -7.10668 | -35.24932 | 2024-11-21 03:17:00 | NOAA-20 | SAPÉ | PARAÍBA | Brasil | 2515302 | 25 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 24b114b3-4324-3c08-a983-7ea532f06ba0 | -9.10072 | -35.44827 | 2024-11-21 03:17:00 | NOAA-20 | PORTO DE PEDRAS | ALAGOAS | Brasil | 2707404 | 27 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| ff8121da-0676-35d0-9cb9-4b8019d335ea | -21.01059 | -41.84277 | 2024-11-21 03:19:00 | NOAA-20 | NATIVIDADE | RIO DE JANEIRO | Brasil | 3303104 | 33 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 9d7e6e17-e6e3-335a-991f-860dee0f23a7 | -4.58 | -48.0132 | 2024-11-21 03:20:00 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 139.7 |
| f4514c51-da6c-3381-ae3c-c949e4a0c223 | -4.2388 | -46.1197 | 2024-11-21 03:20:00 | GOES-16 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 127.9 |
| df191e96-7f8b-3f33-91d5-c060d7701bbe | -4.7717 | -44.4891 | 2024-11-21 03:20:00 | GOES-16 | SANTO ANTÔNIO DOS LOPES | MARANHÃO | Brasil | 2110302 | 21 | 33 | nan | nan | nan | Cerrado | 100.5 |
| d729c92f-1fd2-3818-9416-5fe99a125c51 | -3.2767 | -53.84 | 2024-11-21 03:20:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 87.4 |
| 5decb1ab-259c-33f3-b022-52dfd53ef693 | -6.8258 | -46.7737 | 2024-11-21 03:20:00 | GOES-16 | SÃO PEDRO DOS CRENTES | MARANHÃO | Brasil | 2111573 | 21 | 33 | nan | nan | nan | Cerrado | 71.3 |
| 09e167d1-a0c6-34bf-ac6c-8772fd6a8f0e | -4.2575 | -46.1188 | 2024-11-21 03:20:00 | GOES-16 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 148.1 |
| f7cb6348-7bd5-3c7f-bef8-0959524ac773 | -2.0075 | -54.5292 | 2024-11-21 03:20:00 | GOES-16 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 68.4 |
| ba470e03-e87a-3242-81a1-21ef0282771a | -4.2576 | -46.0965 | 2024-11-21 03:20:00 | GOES-16 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 68.3 |
| 23685a86-1326-359b-b1d7-94293d07c935 | -3.7611 | -52.4037 | 2024-11-21 03:20:00 | GOES-16 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 34.2 |
| 91e7fb0c-fa99-335e-bbf8-07e63a4cbcb1 | -2.5325 | -45.4517 | 2024-11-21 03:20:00 | GOES-16 | PRESIDENTE SARNEY | MARANHÃO | Brasil | 2109270 | 21 | 33 | nan | nan | nan | Amazônia | 49.0 |
| 0c81f54e-f43d-365a-afc4-909fa93f773b | -2.7676 | -52.1045 | 2024-11-21 03:20:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 52.1 |
| ab69091b-658c-3276-b817-c725543b7312 | -2.5326 | -45.4292 | 2024-11-21 03:20:00 | GOES-16 | PRESIDENTE SARNEY | MARANHÃO | Brasil | 2109270 | 21 | 33 | nan | nan | nan | Amazônia | 48.8 |
| a3728c70-e361-38cf-be79-2928d5717e66 | -2.0259 | -54.5289 | 2024-11-21 03:20:00 | GOES-16 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 95.1 |
| d1ba6a00-fd5e-37c2-8382-a326f8705afe | -4.239 | -46.0975 | 2024-11-21 03:20:00 | GOES-16 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 64.0 |
| f64f5d29-b490-3677-9646-f7a18ccdba27 | -3.295 | -53.8597 | 2024-11-21 03:20:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 66.7 |
| 09fed560-8c99-3d19-b581-9e471ce247e6 | -4.5799 | -48.0349 | 2024-11-21 03:20:00 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 91.5 |
| 2fc3f155-a2e6-3e8f-bc5c-1a77e5e93aa0 | -3.2768 | -53.8199 | 2024-11-21 03:20:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 51.3 |
| fcee9884-4d44-38b1-81d7-35f8ff7a3e43 | -2.262 | -48.7017 | 2024-11-21 03:20:00 | GOES-16 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 47.0 |
| 44ab0cf0-bdf3-3426-b086-0b62567ed00d | -3.2951 | -53.8395 | 2024-11-21 03:20:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 86.6 |
| 02747eb7-e613-367b-9d90-6cc4df2765dc | -4.58 | -48.0132 | 2024-11-21 03:30:00 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 69.9 |
| 2aa9f750-0867-35e5-a066-85c068751071 | -2.0075 | -54.5292 | 2024-11-21 03:30:00 | GOES-16 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 70.2 |
| 1059d090-f93e-320c-8e00-9d347b9749f4 | -6.1182 | -42.5086 | 2024-11-21 03:30:00 | GOES-16 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 52.5 |
| d74e057d-ba20-3bb6-a8c0-b876eafa76b5 | -3.2767 | -53.84 | 2024-11-21 03:30:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 84.2 |
| 5d8a6a3f-e3b0-392d-a17f-12bf7cc30d51 | -3.2952 | -53.8194 | 2024-11-21 03:30:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 36.7 |
| 609ddb57-e02a-3530-a480-c71e2bdf7e41 | -4.2575 | -46.1188 | 2024-11-21 03:30:00 | GOES-16 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 141.1 |
| 9a887d14-583f-36fc-86cf-88be13a4c68c | -4.2388 | -46.1197 | 2024-11-21 03:30:00 | GOES-16 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 132.9 |
| 907fd0d5-90de-3e25-8f40-89e2d404aa18 | -2.9423 | -45.1904 | 2024-11-21 03:30:00 | GOES-16 | SÃO VICENTE FERRER | MARANHÃO | Brasil | 2111706 | 21 | 33 | nan | nan | nan | Amazônia | 67.5 |
| 8793ae30-ddcb-3229-95bd-f58e45e98734 | -3.2768 | -53.8199 | 2024-11-21 03:30:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 46.6 |
| 9f525a17-4a84-32e9-a356-cc4c04a6fc55 | -3.2951 | -53.8395 | 2024-11-21 03:30:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 76.2 |
| 016ce1d2-3759-3ee6-a32a-898bda860b71 | -2.0259 | -54.5289 | 2024-11-21 03:30:00 | GOES-16 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 72.2 |
| 84a1190b-2598-3ee2-a1a9-080cacb18a49 | -3.295 | -53.8597 | 2024-11-21 03:30:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 50.3 |
| 0f7e1fd3-3bbc-301c-8bb5-8a19ba383225 | -3.2951 | -53.8395 | 2024-11-21 03:40:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 87.9 |
| e2422782-5ea1-336b-a471-02eeca6be09a | -2.0259 | -54.5289 | 2024-11-21 03:40:00 | GOES-16 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 72.0 |
| 0e453663-5ec3-39e9-bcd3-258423d28ea6 | -3.2767 | -53.84 | 2024-11-21 03:40:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 75.3 |
| d6b453fd-f962-31c3-96d9-c4d620d320ce | -3.2768 | -53.8199 | 2024-11-21 03:40:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 47.8 |
| 7711ab23-0da5-3049-8714-03351bd3e40e | -2.0075 | -54.5292 | 2024-11-21 03:40:00 | GOES-16 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 66.6 |
| 175d868f-d726-3a17-af32-ab50aab16ef7 | -4.58 | -48.0132 | 2024-11-21 03:40:00 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 37.4 |
| 57de7b57-4b89-3a4f-b463-3d69f84ac9c0 | -4.2575 | -46.1188 | 2024-11-21 03:40:00 | GOES-16 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 137.1 |
| 1b655492-e92e-3c64-8041-bb0858322b05 | -3.295 | -53.8597 | 2024-11-21 03:40:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 59.2 |
| 89f4d5a1-102a-3dcd-901a-e0e436344bde | -4.2388 | -46.1197 | 2024-11-21 03:40:00 | GOES-16 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 76.9 |
| 83efeb6e-c594-3f14-873a-57ead7c3fa59 | -3.2952 | -53.8194 | 2024-11-21 03:40:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 41.0 |
| 8062498f-1ff6-3e07-9675-84a0811e0a26 | -3.295 | -53.8597 | 2024-11-21 03:50:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 45.1 |
| f8131039-622f-3122-9e2f-64a30008cb32 | -4.58 | -48.0132 | 2024-11-21 03:50:00 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 41.0 |
| 60d36b85-93e2-3798-aabf-63b0bdc90fc3 | -3.2767 | -53.84 | 2024-11-21 03:50:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 75.0 |


[Clique aqui para ver as próximas entradas](README11.md)
