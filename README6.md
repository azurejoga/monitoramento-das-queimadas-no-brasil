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

## Dados Diários - Página 6

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 82ed58f1-0e2a-345f-9313-0f1c974d3543 | -13.1378 | -54.930302 | 2025-08-20 01:06:00 | METOP-B | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 364cb548-0ab4-37f0-b3e2-89aec842c583 | -8.8809 | -62.403599 | 2025-08-20 01:06:00 | METOP-B | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| e1ab3cd8-9d79-3ffb-9dac-da715ed2629f | -8.648 | -62.143002 | 2025-08-20 01:06:00 | METOP-B | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 701e9764-fc34-3498-8e34-176aedf7ca4f | -8.759 | -64.190903 | 2025-08-20 01:06:00 | METOP-B | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| ec6b583f-5c35-31df-823a-b5b7a5a4863b | -8.9667 | -60.490299 | 2025-08-20 01:06:00 | METOP-B | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| dd217068-8b1d-307c-ad65-09d98412219e | -13.1446 | -54.915901 | 2025-08-20 01:06:00 | METOP-B | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 4938a66b-f578-326a-a925-29d80acb5b30 | -8.034 | -47.6639 | 2025-08-20 01:10:00 | GOES-19 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 78.9 |
| 64e57902-5998-3c12-b57a-76558814775e | -15.0002 | -54.8135 | 2025-08-20 01:10:00 | GOES-19 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 49.1 |
| 7d714ec9-c8d8-36d7-803c-fd2ccdb031b5 | -20.339 | -51.7062 | 2025-08-20 01:10:00 | GOES-19 | SELVÍRIA | MATO GROSSO DO SUL | Brasil | 5007802 | 50 | 33 | nan | nan | nan | Cerrado | 116.6 |
| e680641c-5838-3780-9eae-e280473a24d9 | -3.232 | -46.8056 | 2025-08-20 01:10:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 39.3 |
| 61bf07bb-f8d6-36dd-972b-b86da8b8e84d | -13.1555 | -54.9357 | 2025-08-20 01:10:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 112.2 |
| aedf7a47-52f0-34fc-bfee-2f6a3dd3aded | -3.982 | -42.516 | 2025-08-20 01:10:00 | GOES-19 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 36.0 |
| ca1e489e-6b80-36da-84ee-2429a78fa5bd | -12.9778 | -56.8614 | 2025-08-20 01:10:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 46.1 |
| 05ada826-1541-37bf-b87c-bddb89d28b12 | -13.1558 | -54.9151 | 2025-08-20 01:10:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 87.8 |
| 4f7f0ed6-8848-33ae-abab-89c7bdcc8e49 | -4.4331 | -47.76 | 2025-08-20 01:10:00 | GOES-19 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 43.7 |
| 119aa5e8-1fc6-35be-a175-75449723c0bb | -4.912 | -43.2337 | 2025-08-20 01:10:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 87.0 |
| 3dc37abd-608a-3823-b26a-d05d6945a5c8 | -13.1367 | -54.9171 | 2025-08-20 01:10:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 57.6 |
| 9ada3c56-0e26-3006-830b-0a669139edf6 | -6.1476 | -57.7215 | 2025-08-20 01:10:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 45.0 |
| a4d77c9e-6a00-3e11-802a-2fdcebf303da | -13.1364 | -54.9376 | 2025-08-20 01:10:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 82.8 |
| 2095bfd3-7bc6-3e6a-b190-96ccf3508f5d | -8.0152 | -47.6656 | 2025-08-20 01:10:00 | GOES-19 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 61.6 |
| 68e98d9d-7ad6-3783-b29d-f948cf9774cf | -20.339 | -51.7062 | 2025-08-20 01:20:00 | GOES-19 | SELVÍRIA | MATO GROSSO DO SUL | Brasil | 5007802 | 50 | 33 | nan | nan | nan | Cerrado | 111.7 |
| 2f0f1bc9-5f60-37ce-819d-b7f32a05e64a | -15.5506 | -42.285 | 2025-08-20 01:20:00 | GOES-19 | INDAIABIRA | MINAS GERAIS | Brasil | 3130655 | 31 | 33 | nan | nan | nan | Cerrado | 51.9 |
| 8306f9dc-935d-397f-9652-9903d8ceda7f | -4.4331 | -47.76 | 2025-08-20 01:20:00 | GOES-19 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 34.2 |
| c75afebe-3ee7-3403-a549-d55ec3004d3e | -13.1558 | -54.9151 | 2025-08-20 01:20:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 97.4 |
| de8d043c-5913-3df1-95e2-2b9d161f7502 | -6.9605 | -42.8816 | 2025-08-20 01:20:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 34.0 |
| fe7731c4-2c9e-348a-bc68-987e2bbdc177 | -4.912 | -43.2337 | 2025-08-20 01:20:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 89.8 |
| 5b84eced-8d1f-322c-afaa-0135608e857a | -8.034 | -47.6639 | 2025-08-20 01:20:00 | GOES-19 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 99.5 |
| 7be856d5-670a-33f5-bcd9-82b0a04f8990 | -20.3385 | -51.7284 | 2025-08-20 01:20:00 | GOES-19 | SELVÍRIA | MATO GROSSO DO SUL | Brasil | 5007802 | 50 | 33 | nan | nan | nan | Cerrado | 63.1 |
| 140f72fd-d8fc-3131-a3c7-f05cbfac4376 | -12.9357 | -46.1534 | 2025-08-20 01:20:00 | GOES-19 | LAVANDEIRA | TOCANTINS | Brasil | 1712157 | 17 | 33 | nan | nan | nan | Cerrado | 95.1 |
| 3cca7ec2-67a1-3b02-a703-448764dda360 | -13.1367 | -54.9171 | 2025-08-20 01:20:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 53.0 |
| 67caf2d7-4d88-3a46-9111-f4ad6e159c1b | -12.9778 | -56.8614 | 2025-08-20 01:20:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 49.3 |
| 368a0018-178b-380e-a359-0172fb95b5a2 | -3.232 | -46.8056 | 2025-08-20 01:20:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 31.3 |
| a36f9d9d-6cd1-380a-b4b6-fb4728855eb7 | -13.1364 | -54.9376 | 2025-08-20 01:20:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 68.5 |
| 6bfb313c-1527-3086-857d-83cd0a68d6a1 | -3.982 | -42.516 | 2025-08-20 01:20:00 | GOES-19 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 39.2 |
| 38e5a2f4-1dc4-3db9-858a-d7ac11d2983f | -13.1555 | -54.9357 | 2025-08-20 01:20:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 130.6 |
| 73c743a4-2aa6-3d83-b743-457c7a6c6283 | -12.9353 | -46.1762 | 2025-08-20 01:20:00 | GOES-19 | LAVANDEIRA | TOCANTINS | Brasil | 1712157 | 17 | 33 | nan | nan | nan | Cerrado | 55.7 |
| 6093a67f-ca2c-3804-914e-a73f0fb4a09f | -15.0002 | -54.8135 | 2025-08-20 01:20:00 | GOES-19 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 53.8 |
| 8ebaa3a6-b655-37e9-acb8-6aa56d2dbccd | -20.4542 | -53.7014 | 2025-08-20 01:20:00 | GOES-19 | RIBAS DO RIO PARDO | MATO GROSSO DO SUL | Brasil | 5007109 | 50 | 33 | nan | nan | nan | Cerrado | 61.4 |
| 76b0f210-48d4-30e9-99c0-c1b8f1e53d5d | -20.4537 | -53.7231 | 2025-08-20 01:20:00 | GOES-19 | RIBAS DO RIO PARDO | MATO GROSSO DO SUL | Brasil | 5007109 | 50 | 33 | nan | nan | nan | Cerrado | 70.8 |
| 079f5bdf-d7ad-3bfd-b9cf-af477d260be7 | -20.44646 | -53.71379 | 2025-08-20 01:24:00 | TERRA_M-M | RIBAS DO RIO PARDO | MATO GROSSO DO SUL | Brasil | 5007109 | 50 | 33 | nan | nan | nan | Cerrado | 74.6 |
| 994a9626-84de-3918-b384-5890785c72d6 | -20.34344 | -51.7169 | 2025-08-20 01:24:00 | TERRA_M-M | SELVÍRIA | MATO GROSSO DO SUL | Brasil | 5007802 | 50 | 33 | nan | nan | nan | Cerrado | 106.0 |
| b51dba2d-c1db-3882-8656-4149b6d400d3 | -20.33002 | -51.71993 | 2025-08-20 01:24:00 | TERRA_M-M | SELVÍRIA | MATO GROSSO DO SUL | Brasil | 5007802 | 50 | 33 | nan | nan | nan | Cerrado | 20.1 |
| 6f1d6a23-2a1b-3b85-9ed0-63503c3da0b3 | -20.33919 | -51.69331 | 2025-08-20 01:24:00 | TERRA_M-M | SELVÍRIA | MATO GROSSO DO SUL | Brasil | 5007802 | 50 | 33 | nan | nan | nan | Cerrado | 26.1 |
| 90558d76-c0ee-32dd-9eb0-28cdec03104d | -20.34145 | -51.73496 | 2025-08-20 01:24:00 | TERRA_M-M | SELVÍRIA | MATO GROSSO DO SUL | Brasil | 5007802 | 50 | 33 | nan | nan | nan | Cerrado | 22.5 |
| 0426d50d-4c25-3a3c-a61a-585f6a061d27 | -20.33708 | -51.71165 | 2025-08-20 01:24:00 | TERRA_M-M | SELVÍRIA | MATO GROSSO DO SUL | Brasil | 5007802 | 50 | 33 | nan | nan | nan | Cerrado | 119.1 |
| b72a18c5-b9aa-3046-9a9e-99a0fbbc9c24 | -20.35048 | -51.70857 | 2025-08-20 01:24:00 | TERRA_M-M | SELVÍRIA | MATO GROSSO DO SUL | Brasil | 5007802 | 50 | 33 | nan | nan | nan | Cerrado | 18.7 |
| d033c985-1b25-3928-9f93-9e06e389c254 | -20.44936 | -53.73061 | 2025-08-20 01:24:00 | TERRA_M-M | RIBAS DO RIO PARDO | MATO GROSSO DO SUL | Brasil | 5007109 | 50 | 33 | nan | nan | nan | Cerrado | 21.6 |
| 195b920a-2ca1-3236-8e2a-2edb306a79dd | -21.44704 | -51.63776 | 2025-08-20 01:24:00 | TERRA_M-M | DRACENA | SÃO PAULO | Brasil | 3514403 | 35 | 33 | nan | nan | nan | Mata Atlântica | 14.7 |
| e4ea6b1f-3b41-3db7-8513-c0d486fc8ba9 | -13.14472 | -54.9208 | 2025-08-20 01:26:00 | TERRA_M-M | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 105.3 |
| b286735f-c97e-321b-80e6-24b4a92258b0 | -14.32996 | -51.99369 | 2025-08-20 01:26:00 | TERRA_M-M | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 27.8 |
| be779769-d2c5-36f4-983e-12d142241657 | -11.67441 | -60.18855 | 2025-08-20 01:26:00 | TERRA_M-M | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 18.5 |
| 29817417-2734-330c-a5a7-60fe807504f2 | -14.65695 | -54.89259 | 2025-08-20 01:26:00 | TERRA_M-M | PLANALTO DA SERRA | MATO GROSSO | Brasil | 5106455 | 51 | 33 | nan | nan | nan | Cerrado | 10.8 |
| b51262fd-c4c2-30c2-8002-a8174e581603 | -13.13904 | -54.93373 | 2025-08-20 01:26:00 | TERRA_M-M | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 32.7 |
| 807e5682-8a77-3eca-902d-948b84cb0781 | -13.35068 | -54.39502 | 2025-08-20 01:26:00 | TERRA_M-M | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 22.5 |
| 15e67883-36be-39c6-9a32-66e8f49651a1 | -13.34138 | -54.41694 | 2025-08-20 01:26:00 | TERRA_M-M | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 23.3 |
| 168427ca-5784-3b11-9b7e-d0f59d96715e | -13.14758 | -54.93874 | 2025-08-20 01:26:00 | TERRA_M-M | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 129.8 |
| aba52a3e-4a0c-3115-8d55-93de27dbba2c | -11.66546 | -60.18989 | 2025-08-20 01:26:00 | TERRA_M-M | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 4.9 |
| d9b10234-1b6d-3364-b21d-f90a0141470b | -13.32852 | -54.42453 | 2025-08-20 01:26:00 | TERRA_M-M | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 27.7 |
| fc121b2e-a26c-38d6-9219-2aa5a9e35a80 | -15.00244 | -54.82434 | 2025-08-20 01:26:00 | TERRA_M-M | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 35.9 |
| 35152385-1c78-3f68-9172-bd4addee2c15 | -15.0528 | -54.835 | 2025-08-20 01:26:00 | TERRA_M-M | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 12.5 |
| 85f3edb7-77cf-372e-8418-a1b5f34a3b80 | -10.92105 | -57.50797 | 2025-08-20 01:26:00 | TERRA_M-M | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 8.6 |
| 14f3cc97-a045-3d24-bada-971be623d5b4 | -12.98156 | -56.86774 | 2025-08-20 01:26:00 | TERRA_M-M | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 22.5 |
| 009f0aaa-9ac1-30af-a2e5-23060d1988f4 | -13.03404 | -56.85876 | 2025-08-20 01:26:00 | TERRA_M-M | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 17.1 |
| 9849c394-c970-36fe-8758-294375b6fe6f | -13.10793 | -51.91419 | 2025-08-20 01:26:00 | TERRA_M-M | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Amazônia | 28.6 |
| 39b5e145-1b22-3efb-ad6c-c7ff77916217 | -12.98362 | -56.88073 | 2025-08-20 01:26:00 | TERRA_M-M | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 19.9 |
| c43eac6e-9bf7-3956-b20b-b82fda852580 | -12.97471 | -56.86143 | 2025-08-20 01:26:00 | TERRA_M-M | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 33.9 |
| 85238afd-97ae-319d-9f27-6482660aab48 | -10.91065 | -57.50956 | 2025-08-20 01:26:00 | TERRA_M-M | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 14.2 |
| e1c23e6f-6ce1-3d5e-b9fb-971673663ac3 | -13.03201 | -56.84569 | 2025-08-20 01:26:00 | TERRA_M-M | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 12.3 |
| aa4498cf-1c6a-3954-966f-5b2ec89f02e6 | -12.97868 | -56.88749 | 2025-08-20 01:26:00 | TERRA_M-M | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 17.1 |
| 33f1bf8b-e82c-32d5-92d1-babaf5da5c3d | -11.67309 | -60.17929 | 2025-08-20 01:26:00 | TERRA_M-M | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 632bdb9f-bead-3b4b-b09c-a8df75f9bdad | -13.32875 | -54.41904 | 2025-08-20 01:26:00 | TERRA_M-M | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 28.2 |
| 216a9b67-08a7-3d6c-ad55-7b33f8f2b55f | -10.90872 | -57.49691 | 2025-08-20 01:26:00 | TERRA_M-M | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 6.5 |
| bbe8f783-c2d9-37dc-a47e-c8c73d342e8f | -12.97669 | -56.87448 | 2025-08-20 01:26:00 | TERRA_M-M | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 32.5 |
| eda4d29c-15be-38f0-b85e-1075a3f8b766 | -13.14823 | -54.9138 | 2025-08-20 01:26:00 | TERRA_M-M | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 28.5 |
| ca46e4c5-a7de-311a-9e1f-e05cda40b598 | -13.15418 | -54.94955 | 2025-08-20 01:26:00 | TERRA_M-M | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 42.0 |
| 9fc8c952-6b76-3904-86c0-4b8e1817406b | -13.44123 | -57.10694 | 2025-08-20 01:26:00 | TERRA_M-M | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 9ff3b242-0e21-315c-a46c-225f5925f1d6 | -13.14147 | -57.1615 | 2025-08-20 01:26:00 | TERRA_M-M | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 9.0 |
| 3d260c1a-19c5-340c-8517-9dc81529cab8 | -14.99059 | -54.82628 | 2025-08-20 01:26:00 | TERRA_M-M | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 30.8 |
| ebe26eff-c674-3b59-bec8-5d8536585691 | -14.99962 | -54.80733 | 2025-08-20 01:26:00 | TERRA_M-M | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 23.4 |
| da0aef49-325c-3c66-96ae-d5a82b237396 | -13.1512 | -54.93166 | 2025-08-20 01:26:00 | TERRA_M-M | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 221.1 |
| 781d131c-bb12-38ed-a68a-a12392d74817 | -8.88634 | -62.3979 | 2025-08-20 01:28:00 | TERRA_M-M | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 4.5 |
| faa00aed-e3d4-382d-bbbe-72ce1796eef1 | -9.07175 | -60.42188 | 2025-08-20 01:28:00 | TERRA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 53db7b83-2f3d-3e41-be9e-bb71d520aa24 | -8.7624 | -64.19222 | 2025-08-20 01:28:00 | TERRA_M-M | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 8.7 |
| b136390e-4606-36e0-bc9d-3d1dfc270cf7 | -9.22457 | -60.32977 | 2025-08-20 01:28:00 | TERRA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 17.0 |
| b40d2b45-efb6-390e-a294-59de70567d38 | -9.52067 | -60.53336 | 2025-08-20 01:28:00 | TERRA_M-M | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 7.3 |
| 8a88d442-a866-3d9c-9b78-7ac18163007d | -8.87623 | -62.39017 | 2025-08-20 01:28:00 | TERRA_M-M | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 4523e841-d8b1-3e73-8266-f1f19bd506d3 | -7.01942 | -59.6632 | 2025-08-20 01:28:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.9 |
| f5efba12-372d-3d58-8c0c-c8bbfead2f5b | -8.87746 | -62.39916 | 2025-08-20 01:28:00 | TERRA_M-M | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 10.3 |
| 8d76e597-d411-34af-8caf-e1b838640b88 | -8.97087 | -60.49073 | 2025-08-20 01:28:00 | TERRA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.0 |
| d8dca673-910f-301a-83a9-00dd056acde8 | -7.05043 | -59.23653 | 2025-08-20 01:28:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 18fc35dc-64fc-34ba-a8e6-f51629092e0a | -6.15164 | -57.71737 | 2025-08-20 01:28:00 | TERRA_M-M | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 39.7 |
| 930c407c-9b2e-3bb5-83e6-15f1e1e2bf92 | -6.13838 | -57.70454 | 2025-08-20 01:28:00 | TERRA_M-M | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 12.1 |
| 8fd4e045-1d0f-3350-bfe5-85ae67b596ee | -6.93548 | -62.88049 | 2025-08-20 01:28:00 | TERRA_M-M | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 14.4 |
| 97c53c52-7264-3668-8329-f18cda738352 | -8.96185 | -60.49204 | 2025-08-20 01:28:00 | TERRA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 47cb2cf5-32c7-3544-96a6-0a70f8b784f6 | -8.43279 | -63.86501 | 2025-08-20 01:28:00 | TERRA_M-M | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 36.6 |
| 48de9eba-eff3-330e-adec-ff91de1b62a4 | -9.2259 | -60.33914 | 2025-08-20 01:28:00 | TERRA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 48.1 |
| 8f28e4c0-46e7-3551-a393-e56d97d89aee | -7.02897 | -59.66184 | 2025-08-20 01:28:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 242323b7-154d-33aa-8a9b-d31274a1b37b | -10.46366 | -64.46519 | 2025-08-20 01:28:00 | TERRA_M-M | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 5.3 |
| dad2fb95-088b-3418-9c46-3ab8bd1fdf65 | -5.4471 | -60.13143 | 2025-08-20 01:28:00 | TERRA_M-M | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 4.1 |
| a7945f4d-e932-35e4-8c7e-15309c9b824c | -11.61443 | -65.07951 | 2025-08-20 01:28:00 | TERRA_M-M | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 8.2 |


[Clique aqui para ver as próximas entradas](README7.md)
