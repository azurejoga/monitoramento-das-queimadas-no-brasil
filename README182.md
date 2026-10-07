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

## Dados Diários - Página 182

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| dd778321-a57f-3fa9-9436-b46612f81a80 | -12.18399 | -44.78112 | 2026-10-07 16:35:00 | NPP-375 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 312.2 |
| d13824d4-f2c2-3d9f-9f42-3bee1f968f78 | -10.91147 | -43.1632 | 2026-10-07 16:35:00 | NPP-375 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 4.8 |
| 5fb421f0-6a67-335c-94af-79ca566c8e4f | -13.69394 | -40.29792 | 2026-10-07 16:35:00 | NPP-375 | LAFAIETE COUTINHO | BAHIA | Brasil | 2918704 | 29 | 33 | nan | nan | nan | Caatinga | 5.9 |
| 8c80646a-89db-302c-ba9c-54cdcc899297 | -12.18976 | -44.77246 | 2026-10-07 16:35:00 | NPP-375 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 0.0 |
| 738bbd20-f83c-3f69-9f0f-6940f8f71293 | -12.31904 | -47.94733 | 2026-10-07 16:35:00 | NPP-375 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 17.3 |
| 1649e54c-e199-3fba-a7c3-099b3a81beb2 | -12.63863 | -47.71493 | 2026-10-07 16:35:00 | NPP-375 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| c93b2605-4244-38df-965f-e6c042cc1dd5 | -12.16644 | -44.73322 | 2026-10-07 16:35:00 | NPP-375 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 57.9 |
| a982df94-b5da-3f59-a5fb-1182d833bc66 | -16.80145 | -39.18083 | 2026-10-07 16:35:00 | NPP-375 | PORTO SEGURO | BAHIA | Brasil | 2925303 | 29 | 33 | nan | nan | nan | Mata Atlântica | 3.1 |
| 18c3a55c-c0cf-38c8-ad7a-faf59ceee08f | -13.03474 | -43.12104 | 2026-10-07 16:35:00 | NPP-375 | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Caatinga | 14.6 |
| 8c91b685-e7e4-35d8-9cdc-4e697eaa629b | -12.19321 | -44.77196 | 2026-10-07 16:35:00 | NPP-375 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 10.5 |
| 85b1ece1-5669-3eb8-b1f1-3bbce623d3b9 | -11.2248 | -45.28102 | 2026-10-07 16:35:00 | NPP-375 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 19.1 |
| ff27e510-ffee-3fc0-814b-a29bbb2ccede | -14.06455 | -55.10034 | 2026-10-07 16:35:00 | NPP-375 | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 3.1 |
| eaae74cb-3dc6-3215-912f-accbbab956b7 | -11.27607 | -45.21784 | 2026-10-07 16:35:00 | NPP-375 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 24.0 |
| ca2d18a7-79e9-30a9-ad8d-fb08312814bd | -12.21763 | -44.6827 | 2026-10-07 16:35:00 | NPP-375 | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 2e2d6355-b01e-36da-8aae-85bcdc94a242 | -14.12661 | -41.36974 | 2026-10-07 16:35:00 | NPP-375 | TANHAÇU | BAHIA | Brasil | 2931004 | 29 | 33 | nan | nan | nan | Caatinga | 22.3 |
| be87405a-dbdd-3fd4-91e7-c1144c47bb14 | -12.17376 | -44.7593 | 2026-10-07 16:35:00 | NPP-375 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 21.7 |
| 98e27ec1-1f73-3e61-b8b0-0ca121e73381 | -11.76607 | -47.74142 | 2026-10-07 16:35:00 | NPP-375 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 6.2 |
| fa8364f6-87f7-3f30-87a3-fb28afcaac5b | -11.85049 | -43.56219 | 2026-10-07 16:35:00 | NPP-375 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 80.0 |
| fd9de98d-cc9c-319f-8f1f-5ea59fb5856b | -13.86184 | -39.53336 | 2026-10-07 16:35:00 | NPP-375 | GANDU | BAHIA | Brasil | 2911204 | 29 | 33 | nan | nan | nan | Mata Atlântica | 7.1 |
| 6be671ba-2859-3e5d-9b48-1423da939edb | -12.16244 | -44.72993 | 2026-10-07 16:35:00 | NPP-375 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 17.0 |
| 6a1fd1df-d60b-3440-b011-237724d33cef | -11.6382 | -43.67931 | 2026-10-07 16:35:00 | NPP-375 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 49.9 |
| 3393df90-24ec-344f-a8e9-e7343725648a | -14.51416 | -48.25935 | 2026-10-07 16:35:00 | NPP-375 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 8.7 |
| 6d05770b-e7e6-3a04-970e-34d8fe087f2d | -12.17592 | -46.88346 | 2026-10-07 16:35:00 | NPP-375 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 12.0 |
| 265a37a3-26c2-3dc2-a79b-1ba7f5f929c2 | -18.31184 | -42.23417 | 2026-10-07 16:35:00 | NPP-375 | SANTA MARIA DO SUAÇUÍ | MINAS GERAIS | Brasil | 3158201 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.0 |
| 71e6cfe1-4208-3c35-8d25-10d60309b24e | -10.4932 | -40.16982 | 2026-10-07 16:35:00 | NPP-375 | SENHOR DO BONFIM | BAHIA | Brasil | 2930105 | 29 | 33 | nan | nan | nan | Caatinga | 3.4 |
| 7104745f-3462-3db0-9cbb-bf2135bce26f | -14.40735 | -41.34182 | 2026-10-07 16:35:00 | NPP-375 | ARACATU | BAHIA | Brasil | 2902005 | 29 | 33 | nan | nan | nan | Caatinga | 17.3 |
| 1dccf8b6-ef65-3376-bee9-39c0c1e20fae | -19.2569 | -40.74026 | 2026-10-07 16:35:00 | NPP-375 | PANCAS | ESPÍRITO SANTO | Brasil | 3204005 | 32 | 33 | nan | nan | nan | Mata Atlântica | 3.4 |
| 58332e1b-64d9-30b4-8373-2f3436ec2980 | -11.64822 | -43.67781 | 2026-10-07 16:35:00 | NPP-375 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 10.5 |
| 77d54f31-5b56-3ba3-b1b3-a7f9ccd26972 | -19.54252 | -40.19406 | 2026-10-07 16:35:00 | NPP-375 | LINHARES | ESPÍRITO SANTO | Brasil | 3203205 | 32 | 33 | nan | nan | nan | Mata Atlântica | 15.8 |
| d1b9e6f0-df77-3186-9007-1f7bc8f28862 | -12.22037 | -44.70167 | 2026-10-07 16:35:00 | NPP-375 | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 18.7 |
| 8c17fc99-78b2-37f3-ba52-e96c375c4627 | -12.22201 | -44.71309 | 2026-10-07 16:35:00 | NPP-375 | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 16.2 |
| c6189e7b-f2ca-3104-9882-6f016d93dc28 | -11.22424 | -45.27715 | 2026-10-07 16:35:00 | NPP-375 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 6.0 |
| d23f5982-7154-3204-8100-488f77938b20 | -12.29797 | -45.29373 | 2026-10-07 16:35:00 | NPP-375 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 16.2 |
| 30c45a24-780c-3415-a55f-24d3391c143d | -13.78484 | -47.26725 | 2026-10-07 16:35:00 | NPP-375 | TERESINA DE GOIÁS | GOIÁS | Brasil | 5221080 | 52 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 193d1a80-e05e-3537-b213-66b72f6bb41d | -13.20223 | -40.91623 | 2026-10-07 16:35:00 | NPP-375 | ITAETÉ | BAHIA | Brasil | 2915007 | 29 | 33 | nan | nan | nan | Caatinga | 4.8 |
| e2b93fbe-3224-3555-b89e-b7f75d1b624f | -12.22604 | -44.73205 | 2026-10-07 16:35:00 | NPP-375 | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 35.3 |
| 565d1933-598f-3618-a804-c32391259f99 | -12.6638 | -38.5485 | 2026-10-07 16:35:00 | NPP-375 | CANDEIAS | BAHIA | Brasil | 2906501 | 29 | 33 | nan | nan | nan | Mata Atlântica | 6.4 |
| 89602ab3-da9b-3e3f-bd53-c4b4edf53a0e | -10.93 | -40.37083 | 2026-10-07 16:35:00 | NPP-375 | SAÚDE | BAHIA | Brasil | 2929800 | 29 | 33 | nan | nan | nan | Caatinga | 5.0 |
| 0241939b-85bb-32b3-8709-8b6f401076df | -11.84622 | -43.53373 | 2026-10-07 16:35:00 | NPP-375 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 13.1 |
| 10f04004-2657-3159-a62d-f65626d5ffab | -11.62391 | -43.62054 | 2026-10-07 16:35:00 | NPP-375 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 167.6 |
| 01c0a68d-e85a-3d1c-ba8f-8b23383ecf11 | -12.17209 | -44.74789 | 2026-10-07 16:35:00 | NPP-375 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 90.2 |
| eaa16b74-659d-3171-81b1-d4ef8106ebd2 | -13.78085 | -47.26777 | 2026-10-07 16:35:00 | NPP-375 | TERESINA DE GOIÁS | GOIÁS | Brasil | 5221080 | 52 | 33 | nan | nan | nan | Cerrado | 4.7 |
| e97c2b13-2c55-3464-baad-575d6f1ce34f | -12.99345 | -47.06 | 2026-10-07 16:35:00 | NPP-375 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 16.5 |
| 59f85fb3-0ede-3029-a887-711f32565a2c | -12.1811 | -44.78547 | 2026-10-07 16:35:00 | NPP-375 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 577601fe-a080-31da-99c0-98fb6dd5549c | -15.14838 | -47.19036 | 2026-10-07 16:35:00 | NPP-375 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| b75afbf4-be1d-3a64-ab56-f1cf3a54b492 | -16.85691 | -40.5966 | 2026-10-07 16:35:00 | NPP-375 | SANTA HELENA DE MINAS | MINAS GERAIS | Brasil | 3157658 | 31 | 33 | nan | nan | nan | Mata Atlântica | 20.3 |
| 2b25d707-e24b-35de-94ca-5088ad625fa2 | -12.49216 | -49.55617 | 2026-10-07 16:35:00 | NPP-375 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 8eed43f4-02ad-3702-bc80-019c90ac3003 | -11.78655 | -43.53653 | 2026-10-07 16:35:00 | NPP-375 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 35.9 |
| bb92e7e3-18e8-3aea-9d31-55d9cfd4be6e | -14.74686 | -47.45749 | 2026-10-07 16:35:00 | NPP-375 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| f9d5fae6-aa5d-3e6f-8d42-4e39cd4d2be5 | -12.21193 | -44.66054 | 2026-10-07 16:35:00 | NPP-375 | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 14.1 |
| 5c0f8103-9c68-3587-b0af-4ad19cccba65 | -12.83327 | -45.57036 | 2026-10-07 16:35:00 | NPP-375 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 11.9 |
| 1d0b89b2-ae5d-345b-ba40-60f887488800 | -11.22869 | -44.87056 | 2026-10-07 16:35:00 | NPP-375 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 00a87bc4-5c4c-3305-bec5-de9c3d957337 | -12.1852 | -44.76535 | 2026-10-07 16:35:00 | NPP-375 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 44.0 |
| 72c165f8-219c-3601-8d3f-8d2d8e0a8140 | -12.3372 | -47.06157 | 2026-10-07 16:35:00 | NPP-375 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 12.8 |
| 4d2f39c6-9d3c-38d3-a3bc-91cdcea38857 | -13.37337 | -43.87 | 2026-10-07 16:35:00 | NPP-375 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 49.3 |
| c43f4724-6fed-37e7-8602-3679e1309e57 | -12.19846 | -48.41986 | 2026-10-07 16:35:00 | NPP-375 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 24.9 |
| 642ae0cb-33e7-350b-9832-4fe019bd2f8d | -11.51555 | -41.71001 | 2026-10-07 16:35:00 | NPP-375 | LAPÃO | BAHIA | Brasil | 2919157 | 29 | 33 | nan | nan | nan | Caatinga | 19.8 |
| 928c44af-20c1-359d-aeaf-0764a4d37945 | -9.71597 | -35.9258 | 2026-10-07 16:35:00 | NPP-375 | MARECHAL DEODORO | ALAGOAS | Brasil | 2704708 | 27 | 33 | nan | nan | nan | Mata Atlântica | 10.2 |
| 15c58b55-04ff-3456-89d5-83e5272c16ef | -12.19088 | -44.78009 | 2026-10-07 16:35:00 | NPP-375 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 98.5 |
| 98f8d2ee-9ab9-32f0-a440-fc0986dfa824 | -14.79825 | -47.13512 | 2026-10-07 16:35:00 | NPP-375 | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 0f7fc0ef-e22f-32c4-814a-5f07d3d435d9 | -20.43827 | -41.60283 | 2026-10-07 16:35:00 | NPP-375 | IÚNA | ESPÍRITO SANTO | Brasil | 3203007 | 32 | 33 | nan | nan | nan | Mata Atlântica | 3.4 |
| 77f960d3-2f65-3579-971d-a57127e77197 | -18.9907 | -40.64003 | 2026-10-07 16:35:00 | NPP-375 | ÁGUIA BRANCA | ESPÍRITO SANTO | Brasil | 3200136 | 32 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 1807e227-6773-3edd-9fa4-dac851bdbd7e | -13.65293 | -44.78947 | 2026-10-07 16:35:00 | NPP-375 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 25.3 |
| 3261a2f1-d39b-3e02-8d68-81c306cf5415 | -18.22222 | -42.92647 | 2026-10-07 16:35:00 | NPP-375 | COLUNA | MINAS GERAIS | Brasil | 3116803 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.2 |
| c1c959d2-bc89-3954-8399-36ce55200f34 | -13.55077 | -49.15154 | 2026-10-07 16:35:00 | NPP-375 | PORANGATU | GOIÁS | Brasil | 5218003 | 52 | 33 | nan | nan | nan | Cerrado | 11.1 |
| d4bcc39e-d05e-376f-9f19-2947d9d05072 | -13.02303 | -47.19214 | 2026-10-07 16:35:00 | NPP-375 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 24.4 |
| bdea43ff-f41a-3568-aa26-358bd1695697 | -12.16699 | -44.73703 | 2026-10-07 16:35:00 | NPP-375 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 57.9 |
| 16555b06-ae49-3e8d-a196-3186bc2a216a | -18.29066 | -42.55726 | 2026-10-07 16:35:00 | NPP-375 | SÃO PEDRO DO SUAÇUÍ | MINAS GERAIS | Brasil | 3164100 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 8e8b81f3-6392-371b-955f-30a6186312ad | -11.36652 | -42.2735 | 2026-10-07 16:35:00 | NPP-375 | IBIPEBA | BAHIA | Brasil | 2912400 | 29 | 33 | nan | nan | nan | Caatinga | 7.8 |
| e1c816c1-ee78-35bf-a922-3dde780d2abc | -13.50212 | -39.95965 | 2026-10-07 16:35:00 | NPP-375 | JAGUAQUARA | BAHIA | Brasil | 2917607 | 29 | 33 | nan | nan | nan | Mata Atlântica | 7.8 |
| 079fe714-24ab-3f3d-b6b5-218022413d0c | -11.24122 | -45.24695 | 2026-10-07 16:35:00 | NPP-375 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 9f98e0ac-8c24-30be-be6a-00c8c4aaa8f0 | -20.11038 | -40.4852 | 2026-10-07 16:35:00 | NPP-375 | SANTA LEOPOLDINA | ESPÍRITO SANTO | Brasil | 3204500 | 32 | 33 | nan | nan | nan | Mata Atlântica | 10.5 |
| 698f6b2a-edd2-3243-8438-ab939081db4f | -12.17943 | -44.77401 | 2026-10-07 16:35:00 | NPP-375 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 0.0 |
| 1717f15f-1289-39e9-b9c1-e44b95f4e3fa | -13.39523 | -43.87375 | 2026-10-07 16:35:00 | NPP-375 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 21.4 |
| be674503-0255-3851-9d5d-7a76199e6be9 | -12.22765 | -44.72778 | 2026-10-07 16:35:00 | NPP-375 | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 9.2 |
| 83112e2d-0148-3492-b47e-1b8ea42e8f8b | -14.90567 | -48.76719 | 2026-10-07 16:35:00 | NPP-375 | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 196122b6-6381-3a91-867e-34c62814f16f | -20.11816 | -41.00142 | 2026-10-07 16:35:00 | NPP-375 | SANTA MARIA DE JETIBÁ | ESPÍRITO SANTO | Brasil | 3204559 | 32 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 904adbff-e390-3ac8-b9fa-9428f5d805af | -11.83337 | -47.36922 | 2026-10-07 16:35:00 | NPP-375 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 5.6 |
| e07c9c3c-79f1-3ad7-801e-9643ce5298fc | -14.21572 | -42.75794 | 2026-10-07 16:35:00 | NPP-375 | GUANAMBI | BAHIA | Brasil | 2911709 | 29 | 33 | nan | nan | nan | Caatinga | 6.4 |
| c548b112-9747-3820-aad5-4c0acbb0ac5e | -12.18687 | -44.77679 | 2026-10-07 16:35:00 | NPP-375 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 98.5 |
| b40ed40e-974b-3f42-b36b-d1fbe681a088 | -14.40678 | -41.33821 | 2026-10-07 16:35:00 | NPP-375 | ARACATU | BAHIA | Brasil | 2902005 | 29 | 33 | nan | nan | nan | Caatinga | 278.8 |
| f8ba5ad2-b2a8-3435-8869-4b2525fa98d5 | -11.60407 | -42.65138 | 2026-10-07 16:35:00 | NPP-375 | GENTIO DO OURO | BAHIA | Brasil | 2911303 | 29 | 33 | nan | nan | nan | Caatinga | 12.6 |
| 2b597146-fb42-30ef-ba85-1aceb17e5f7c | -12.40121 | -39.07866 | 2026-10-07 16:35:00 | NPP-375 | ANTÔNIO CARDOSO | BAHIA | Brasil | 2901700 | 29 | 33 | nan | nan | nan | Mata Atlântica | 5.2 |
| 510c1bc2-21a8-36fd-a2ab-3d5fccf3718f | -14.36253 | -41.27495 | 2026-10-07 16:35:00 | NPP-375 | ARACATU | BAHIA | Brasil | 2902005 | 29 | 33 | nan | nan | nan | Caatinga | 59.4 |
| 1f6e2fa1-0335-3417-9362-3983fc0c6bfc | -11.8168 | -41.71523 | 2026-10-07 16:35:00 | NPP-375 | CANARANA | BAHIA | Brasil | 2906204 | 29 | 33 | nan | nan | nan | Caatinga | 3.7 |
| 88285c0f-162e-37d0-aa1a-ce6b346aeea1 | -11.51442 | -41.70277 | 2026-10-07 16:35:00 | NPP-375 | LAPÃO | BAHIA | Brasil | 2919157 | 29 | 33 | nan | nan | nan | Caatinga | 9.8 |
| 41030f91-4867-3792-910c-bac6680b012a | -15.09401 | -48.49853 | 2026-10-07 16:35:00 | NPP-375 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 3.9 |
| d92b20f3-e89e-38db-9fb6-3559e87a0385 | -12.87835 | -47.65543 | 2026-10-07 16:35:00 | NPP-375 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 10.1 |
| a6d0bbf6-e21c-396a-9082-8e589158d3f7 | -11.61807 | -43.67232 | 2026-10-07 16:35:00 | NPP-375 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 10.0 |
| a8704f17-9f01-3557-9416-b036264ddce9 | -12.20794 | -44.65726 | 2026-10-07 16:35:00 | NPP-375 | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 22ecadaf-69cc-33b0-bf53-50e67c1e6e00 | -11.23444 | -44.86196 | 2026-10-07 16:35:00 | NPP-375 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 9.0 |
| 3d67b574-0407-3831-90cd-72a6faaef3a9 | -18.34207 | -44.51437 | 2026-10-07 16:35:00 | NPP-375 | CORINTO | MINAS GERAIS | Brasil | 3119104 | 31 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 403c76f5-5d4f-3617-9afd-443c8f9e3f91 | -12.21252 | -40.55616 | 2026-10-07 16:35:00 | NPP-375 | RUY BARBOSA | BAHIA | Brasil | 2927200 | 29 | 33 | nan | nan | nan | Caatinga | 4.7 |
| 919e1cf4-274c-33fd-b363-c3fe4c9fcc11 | -12.22773 | -44.74347 | 2026-10-07 16:35:00 | NPP-375 | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 56.4 |
| 634e7b81-568b-38b9-a6f4-d59f133070d2 | -11.84048 | -43.56378 | 2026-10-07 16:35:00 | NPP-375 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 23.0 |
| 3bd985c1-b228-399d-bf26-93b95836309c | -14.22839 | -41.21841 | 2026-10-07 16:35:00 | NPP-375 | TANHAÇU | BAHIA | Brasil | 2931004 | 29 | 33 | nan | nan | nan | Caatinga | 4.8 |
| ece7d7f9-fc59-3bae-9049-40730212b0a6 | -11.84889 | -43.55145 | 2026-10-07 16:35:00 | NPP-375 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 60.3 |
| de6bf31c-ccf9-37fb-8c68-9140e0e42e78 | -11.73014 | -43.65433 | 2026-10-07 16:35:00 | NPP-375 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 12.4 |
| ee37d031-ff54-313d-8928-c1b1e4b6084a | -11.77666 | -46.7771 | 2026-10-07 16:35:00 | NPP-375 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 27.7 |
| 68fa859f-034f-3447-a2b7-ea7a52f17ec8 | -12.21579 | -44.7103 | 2026-10-07 16:35:00 | NPP-375 | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 67.0 |


[Clique aqui para ver as próximas entradas](README183.md)
