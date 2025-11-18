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

## Dados Diários - Página 3

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| ec13d9ae-80df-32df-8086-c4a030c91847 | -8.2213 | -48.289101 | 2025-11-18 00:11:00 | METOP-B | TUPIRATINS | TOCANTINS | Brasil | 1721307 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 8fba83c3-4504-39a1-93d6-06822deba239 | -3.4107 | -43.4436 | 2025-11-18 00:11:00 | METOP-B | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 87e4ec4b-9807-304a-85e4-17fed7742dce | -4.218 | -46.336102 | 2025-11-18 00:11:00 | METOP-B | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| ddcd21bf-9329-383c-a841-5419a4277c66 | -2.4947 | -49.344398 | 2025-11-18 00:11:00 | METOP-B | MOCAJUBA | PARÁ | Brasil | 1504604 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 78ce7b38-6ddb-3e5d-bb7b-bf737df40f36 | -4.1593 | -44.223701 | 2025-11-18 00:11:00 | METOP-B | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| bf19135f-c3df-31b5-a87d-4958b10c7d3e | -5.3294 | -43.032398 | 2025-11-18 00:11:00 | METOP-B | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 7b5cb552-f94f-3c31-bbaf-7b6168b4546a | -5.3215 | -43.737301 | 2025-11-18 00:11:00 | METOP-B | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| e4ff7979-eb4a-3e0b-935d-627b4c58bd5f | -11.5744 | -48.134102 | 2025-11-18 00:11:00 | METOP-B | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 22704ecf-9115-3526-b968-899bee82dd21 | -8.5418 | -46.0387 | 2025-11-18 00:11:00 | METOP-B | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 7e7154e3-892a-3e6d-b876-a3d76cf9f306 | -7.9461 | -46.8097 | 2025-11-18 00:11:00 | METOP-B | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 65e956a0-5510-3606-bf3a-f2d181bc29f9 | -4.1408 | -46.760799 | 2025-11-18 00:11:00 | METOP-B | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 477434fe-cb9a-3385-a220-27055a1e274c | -6.836 | -43.131802 | 2025-11-18 00:11:00 | METOP-B | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 87b56fcc-8a12-3171-8e06-9541f7ec38f7 | -6.1025 | -42.950401 | 2025-11-18 00:11:00 | METOP-B | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| da371af1-57ef-3b56-96e6-8c0ed4aef620 | -8.9378 | -49.8382 | 2025-11-18 00:11:00 | METOP-B | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ceb0f148-754d-3c5a-8a4a-d1f3bc3cdd33 | -3.1713 | -48.016499 | 2025-11-18 00:11:00 | METOP-B | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 250e5e0d-1874-3b2e-a01e-7ad2bf4c51c6 | -10.9271 | -43.801701 | 2025-11-18 00:11:00 | METOP-B | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| c83cb180-8d46-3877-9519-403cd32214dc | 0.2707 | -51.0522 | 2025-11-18 00:11:00 | METOP-B | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | nan |
| 84c0fbbe-9605-39f5-aabb-f78f3104db83 | -9.4076 | -48.4347 | 2025-11-18 00:11:00 | METOP-B | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| d0b050c2-99ad-3d84-b018-4106bb424d39 | -3.7237 | -52.0541 | 2025-11-18 00:11:00 | METOP-B | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4c45b6d5-6873-3cca-961d-e02fc1a72250 | -3.6443 | -50.829201 | 2025-11-18 00:11:00 | METOP-B | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 50339fed-5cd7-305d-a942-3ea24d6a5a9c | -2.8327 | -46.718601 | 2025-11-18 00:11:00 | METOP-B | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 575db4c5-a770-3926-9323-d7b70aef9107 | -3.8883 | -49.083199 | 2025-11-18 00:11:00 | METOP-B | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1323a9ed-ed86-31ba-a632-0e69ea19d227 | -12.008 | -49.264 | 2025-11-18 00:11:00 | METOP-B | CARIRI DO TOCANTINS | TOCANTINS | Brasil | 1703867 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 85854363-c599-3bfd-a3b9-09ab1586cf89 | -2.7139 | -45.132198 | 2025-11-18 00:11:00 | METOP-B | PINHEIRO | MARANHÃO | Brasil | 2108603 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 2a62aa48-8847-3ecc-905a-16714307a5f4 | -3.3441 | -44.3899 | 2025-11-18 00:11:00 | METOP-B | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 6ae5cf1a-73cd-3b32-b45f-0afc053eef47 | -7.4629 | -45.923599 | 2025-11-18 00:11:00 | METOP-B | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 9dabde35-1ac3-315c-bb31-dd9c2bcafb35 | -3.1786 | -50.635799 | 2025-11-18 00:11:00 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0489467b-d339-3b42-829e-a4c44d9e0f45 | -4.0112 | -47.408401 | 2025-11-18 00:11:00 | METOP-B | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1562745c-0654-3f7e-9323-30a668c7bfc1 | -8.1994 | -45.012699 | 2025-11-18 00:11:00 | METOP-B | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 767ca1c3-48c9-35a0-a07d-773d7d1642c6 | -7.0653 | -46.032299 | 2025-11-18 00:11:00 | METOP-B | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| e9d9a4f2-8421-3978-883f-57a1b2b26b5a | -12.7039 | -46.785599 | 2025-11-18 00:11:00 | METOP-B | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 595d58aa-a74a-3bea-96bf-b59922224507 | -3.4796 | -52.341301 | 2025-11-18 00:11:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0ddc732c-9c8e-30dd-a7ff-8aa7bbb07a06 | -6.3228 | -46.1213 | 2025-11-18 00:11:00 | METOP-B | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 3c316d08-c62b-3d73-a95c-028223b8fc96 | -11.2872 | -48.5093 | 2025-11-18 00:11:00 | METOP-B | BREJINHO DE NAZARÉ | TOCANTINS | Brasil | 1703701 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| d7ca92d4-e3a7-3c55-83f2-0e3178ca3491 | -3.4135 | -43.4557 | 2025-11-18 00:11:00 | METOP-B | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| a0143dae-1bf5-3544-a0a6-1143261f31c6 | -4.1395 | -43.438499 | 2025-11-18 00:11:00 | METOP-B | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 49252387-2aae-3e40-90c0-0e45f31f7a9d | -2.9128 | -47.832699 | 2025-11-18 00:11:00 | METOP-B | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f8ce7c88-a204-3e3e-ad39-84b5e9f5cac4 | -15.9027 | -43.212299 | 2025-11-18 00:11:00 | METOP-B | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Caatinga | nan |
| f0e70a62-7b24-30d2-bc5c-790e307ade99 | -4.8982 | -44.960602 | 2025-11-18 00:11:00 | METOP-B | ESPERANTINÓPOLIS | MARANHÃO | Brasil | 2104008 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| c601fb2e-e842-37ed-87a8-aa7c01a2c84b | -3.6613 | -51.775299 | 2025-11-18 00:11:00 | METOP-B | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5fc5b9fc-cb8e-3603-b594-cc1f2dd395b0 | -5.2151 | -50.169102 | 2025-11-18 00:11:00 | METOP-B | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9d89a9d8-6f23-3f5d-a492-b944b6946357 | -13.5255 | -43.001598 | 2025-11-18 00:11:00 | METOP-B | RIACHO DE SANTANA | BAHIA | Brasil | 2926400 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| 88a1f758-90fe-378b-9147-3189f284df47 | -12.7458 | -45.389099 | 2025-11-18 00:11:00 | METOP-B | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| b28afd24-5816-3705-a492-67f450149680 | -5.3661 | -44.8027 | 2025-11-18 00:11:00 | METOP-B | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| b1abaad6-2bbf-3a46-a2c3-d78eb21b9192 | -3.236 | -45.697601 | 2025-11-18 00:11:00 | METOP-B | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 9252e504-2634-3b19-a641-0acc31aab07a | -8.1 | -43.546101 | 2025-11-18 00:11:00 | METOP-B | ELISEU MARTINS | PIAUÍ | Brasil | 2203602 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 65bef473-b8b5-3b6f-80c3-e97b72d89b21 | -10.6646 | -49.370399 | 2025-11-18 00:11:00 | METOP-B | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 33b7be10-b25a-3fe6-bb38-06a329af0e74 | -4.4451 | -44.212799 | 2025-11-18 00:11:00 | METOP-B | PERITORÓ | MARANHÃO | Brasil | 2108454 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| b65e8802-fce7-3102-8923-1f886945da09 | -8.289 | -43.993301 | 2025-11-18 00:11:00 | METOP-B | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| bcdfec24-4a41-38bd-bc69-1c5dc66d98d4 | -2.3693 | -45.7342 | 2025-11-18 00:11:00 | METOP-B | PRESIDENTE MÉDICI | MARANHÃO | Brasil | 2109239 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 74ca5cb0-6be0-3603-aab8-bae453370bb0 | -9.1563 | -50.130001 | 2025-11-18 00:11:00 | METOP-B | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f5a22f57-43af-3a00-8615-7d0542659769 | -3.1247 | -45.7509 | 2025-11-18 00:11:00 | METOP-B | ARAGUANÃ | MARANHÃO | Brasil | 2100873 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 13ec6148-fba3-3c8b-a541-532258b77c1d | -11.2063 | -49.403599 | 2025-11-18 00:11:00 | METOP-B | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 1b2f35e4-91e6-3f8b-8fbf-49ecf23fcf49 | -11.6629 | -44.729099 | 2025-11-18 00:11:00 | METOP-B | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| c9770a52-e545-35a6-833a-5035a034abc6 | -6.7363 | -43.751701 | 2025-11-18 00:11:00 | METOP-B | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| bd649166-350d-3d30-be52-fe30fd90ba9b | -15.4675 | -43.1656 | 2025-11-18 00:11:00 | METOP-B | PAI PEDRO | MINAS GERAIS | Brasil | 3146552 | 31 | 33 | nan | nan | nan | Caatinga | nan |
| a57ae441-ac29-3e92-97dd-aca4f5f017c9 | -6.2087 | -46.8773 | 2025-11-18 00:11:00 | METOP-B | PORTO FRANCO | MARANHÃO | Brasil | 2109007 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| d48765e5-6700-39c0-893f-4b3a20ac00a3 | -3.0815 | -50.342899 | 2025-11-18 00:11:00 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ea1c95dd-9ded-3210-9cd4-92ef8bc6b616 | -7.5664 | -46.2812 | 2025-11-18 00:11:00 | METOP-B | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| bfedfc20-21b0-3f4e-8a88-d381bd77193a | -2.2788 | -47.223 | 2025-11-18 00:11:00 | METOP-B | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2f748930-d02f-3288-a90e-450c5fda19d1 | -3.2686 | -52.455502 | 2025-11-18 00:11:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 79a1abad-63d3-33e0-8f4d-a05737719b49 | -6.1248 | -42.957699 | 2025-11-18 00:11:00 | METOP-B | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 2e00e28d-e2de-3b72-befc-728bcc271ae4 | -6.2897 | -43.7803 | 2025-11-18 00:11:00 | METOP-B | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 33d823db-9df5-3fc5-93ff-c1500f24d066 | -3.3514 | -44.376999 | 2025-11-18 00:11:00 | METOP-B | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 87f6ef9f-0b2c-320c-b3ef-0e366536161b | -3.3465 | -44.400501 | 2025-11-18 00:11:00 | METOP-B | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| b000fd8e-bf27-3cf6-8f17-4e0bf8f71949 | -12.8635 | -46.035999 | 2025-11-18 00:11:00 | METOP-B | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 5556ab04-a819-3a8e-adbf-73d292f60d65 | -3.0913 | -51.253399 | 2025-11-18 00:11:00 | METOP-B | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d06b5de5-9c89-3383-b861-544349c4760a | -6.7917 | -39.203098 | 2025-11-18 00:11:00 | METOP-B | VÁRZEA ALEGRE | CEARÁ | Brasil | 2314003 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| 455a9d89-8de4-3d50-a360-6d6113f50d82 | -10.3423 | -49.634201 | 2025-11-18 00:11:00 | METOP-B | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 1fd81357-07b8-370e-93cb-b069141fd577 | -3.1652 | -51.490601 | 2025-11-18 00:11:00 | METOP-B | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 848c86ed-51c2-35c0-a827-4755dd2cecd2 | -8.2115 | -48.291302 | 2025-11-18 00:11:00 | METOP-B | TUPIRATINS | TOCANTINS | Brasil | 1721307 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 49a3a40a-1e8e-38eb-af8c-c60fb4d38da9 | -8.2034 | -45.029598 | 2025-11-18 00:11:00 | METOP-B | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 56deecf9-eb14-3c15-abd7-be6d3c155fe4 | -3.7133 | -45.8465 | 2025-11-18 00:11:00 | METOP-B | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| eaf8f3cc-0851-3564-a32e-01a524df80e6 | -5.8695 | -48.233501 | 2025-11-18 00:11:00 | METOP-B | ARAGUATINS | TOCANTINS | Brasil | 1702208 | 17 | 33 | nan | nan | nan | Amazônia | nan |
| 65f96435-9f6a-3092-8396-0323bbf28426 | -4.1642 | -50.2117 | 2025-11-18 00:11:00 | METOP-B | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b1b08077-09b4-3427-b2a3-8b9322675314 | -4.1886 | -44.2169 | 2025-11-18 00:11:00 | METOP-B | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| ea029b20-5db4-33b2-a442-3419094d430a | -3.2286 | -50.492599 | 2025-11-18 00:11:00 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f124ae6b-596b-37b6-9a21-21ef81153121 | -2.9854 | -51.057598 | 2025-11-18 00:11:00 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d75a9d85-faa5-3161-8a1c-9194ee1b3936 | -4.0976 | -45.593399 | 2025-11-18 00:11:00 | METOP-B | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| a5615922-d34f-3f0c-bfb8-cb9eac5e2241 | -6.207 | -46.8699 | 2025-11-18 00:11:00 | METOP-B | PORTO FRANCO | MARANHÃO | Brasil | 2109007 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| a41c4b38-b3f0-3183-b4fe-d60a90af032c | -4.0067 | -46.135101 | 2025-11-18 00:11:00 | METOP-B | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 82602e73-b92f-354d-a4b9-76cef75463fb | -2.4808 | -50.237598 | 2025-11-18 00:11:00 | METOP-B | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 07631bbe-4dc6-3cbb-92b9-bb84dccea79c | -2.9772 | -51.066898 | 2025-11-18 00:11:00 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a6bbb301-2622-3948-b5b8-435b21f58933 | -12.7279 | -45.401299 | 2025-11-18 00:11:00 | METOP-B | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 7898340b-e54c-3ba7-9c2b-6dc29643249f | -2.8309 | -46.710602 | 2025-11-18 00:11:00 | METOP-B | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| fc432e24-6b62-3a91-8363-27152e5e42c9 | -4.139 | -46.753101 | 2025-11-18 00:11:00 | METOP-B | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 89e79453-aabd-3b5c-a220-65b0b19f2c1f | -5.7381 | -49.244598 | 2025-11-18 00:11:00 | METOP-B | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1b3b3a2e-c37b-3c76-b5be-40096ec9d923 | -3.0625 | -45.3927 | 2025-11-18 00:11:00 | METOP-B | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 68de6e3d-6f4a-3af4-b608-64ca9894ecd9 | -3.0272 | -47.837399 | 2025-11-18 00:11:00 | METOP-B | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4e1cc137-7bc3-3a46-acd4-5e6f4bc25093 | -5.8281 | -47.8256 | 2025-11-18 00:11:00 | METOP-B | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| fd1213a9-0aa7-37a8-b69a-70e5521e5679 | -4.1667 | -44.2108 | 2025-11-18 00:11:00 | METOP-B | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 1ebffbec-42e5-3aaa-b544-020f93ef0818 | -3.6283 | -50.758099 | 2025-11-18 00:11:00 | METOP-B | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5eb2ac08-749a-3ecd-80ee-c1a0f53a526d | -10.7575 | -44.174099 | 2025-11-18 00:11:00 | METOP-B | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| f704e777-be8c-3821-b2d3-a41a1e4b1b15 | -4.0411 | -47.493999 | 2025-11-18 00:11:00 | METOP-B | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c023972b-df4e-38c9-9a9b-a5a0d842352f | -3.7615 | -50.9384 | 2025-11-18 00:11:00 | METOP-B | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| eab574cf-19c9-34e2-b001-cd64a2b0865d | -12.7423 | -45.3741 | 2025-11-18 00:11:00 | METOP-B | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| e2eaf318-2659-333f-b377-778241496eeb | -6.2994 | -43.778 | 2025-11-18 00:11:00 | METOP-B | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| b37fcf1c-26fc-3d3f-95c0-2866b5ff4516 | -4.1888 | -46.790501 | 2025-11-18 00:11:00 | METOP-B | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 3bc86c70-8721-326b-9662-8510d6a58645 | -3.8377 | -52.287998 | 2025-11-18 00:11:00 | METOP-B | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 492ec518-4e9e-3b9d-8aa8-4b8caf43863d | -11.1559 | -47.460201 | 2025-11-18 00:11:00 | METOP-B | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | nan |


[Clique aqui para ver as próximas entradas](README4.md)
