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

## Dados Diários - Página 17

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 96180876-03ff-35a3-b3de-5f8fc83ccb66 | -7.11167 | -35.02128 | 2024-11-09 03:17:00 | NPP-375D | SANTA RITA | PARAÍBA | Brasil | 2513703 | 25 | 33 | nan | nan | nan | Mata Atlântica | 5.0 |
| 0fd9e0f1-830a-3bf5-802b-1b2c380f7c73 | -6.49695 | -39.55323 | 2024-11-09 03:17:00 | NPP-375D | JUCÁS | CEARÁ | Brasil | 2307403 | 23 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 3a066e5a-31f7-388a-bf4f-2e6cf53286d3 | -6.32546 | -39.5208 | 2024-11-09 03:17:00 | NPP-375D | ACOPIARA | CEARÁ | Brasil | 2300309 | 23 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 709561e9-91aa-3dd7-9b72-003d38fce123 | -5.11506 | -37.5655 | 2024-11-09 03:17:00 | NPP-375D | BARAÚNA | RIO GRANDE DO NORTE | Brasil | 2401453 | 24 | 33 | nan | nan | nan | Caatinga | 2.6 |
| f7b5e105-5961-3461-afbc-24773eb4637b | -9.12808 | -43.17439 | 2024-11-09 03:17:00 | NPP-375D | JUREMA | PIAUÍ | Brasil | 2205532 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| feae81e7-e6be-314f-a0ee-e30e949bafed | -7.76862 | -35.39412 | 2024-11-09 03:17:00 | NPP-375D | CARPINA | PERNAMBUCO | Brasil | 2604007 | 26 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 95f9cd76-93ab-35b7-9541-8788b0dc8125 | -6.39249 | -39.7127 | 2024-11-09 03:17:00 | NPP-375D | JUCÁS | CEARÁ | Brasil | 2307403 | 23 | 33 | nan | nan | nan | Caatinga | 0.9 |
| a4f0e7b2-d047-3f99-8182-5aa4b7824d6e | -5.5946 | -37.86674 | 2024-11-09 03:17:00 | NPP-375D | APODI | RIO GRANDE DO NORTE | Brasil | 2401008 | 24 | 33 | nan | nan | nan | Caatinga | 4.7 |
| 2ba7df3a-a752-38c4-badc-e243e2c56606 | -7.10803 | -35.01635 | 2024-11-09 03:17:00 | NPP-375D | SANTA RITA | PARAÍBA | Brasil | 2513703 | 25 | 33 | nan | nan | nan | Mata Atlântica | 9.9 |
| 29710f97-232a-3853-92c7-53e21c0d5904 | -6.12668 | -42.56296 | 2024-11-09 03:17:00 | NPP-375D | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 3.5 |
| 9f7151a0-ac13-3c0c-b1fb-c1a13e45cd9d | -6.32622 | -39.51649 | 2024-11-09 03:17:00 | NPP-375D | ACOPIARA | CEARÁ | Brasil | 2300309 | 23 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 78bc7c98-94eb-32da-9f22-684f50e4bcb1 | -6.1294 | -42.56103 | 2024-11-09 03:17:00 | NPP-375D | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 5.0 |
| ae1e7e75-7758-3726-a823-8ecf730a37cf | -6.24328 | -39.70412 | 2024-11-09 03:17:00 | NPP-375D | ACOPIARA | CEARÁ | Brasil | 2300309 | 23 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 890e9a30-8485-363a-ba1a-9f47eb1f4443 | -6.39855 | -39.71352 | 2024-11-09 03:17:00 | NPP-375D | JUCÁS | CEARÁ | Brasil | 2307403 | 23 | 33 | nan | nan | nan | Caatinga | 0.4 |
| 28ebf752-c9ce-3443-ac0f-8245e2426c0d | -4.55993 | -38.00654 | 2024-11-09 03:17:00 | NPP-375D | BEBERIBE | CEARÁ | Brasil | 2302206 | 23 | 33 | nan | nan | nan | Caatinga | 1.5 |
| e4ad89ad-ad80-3cb7-89df-4d9b18aa360a | -7.24128 | -38.92708 | 2024-11-09 03:17:00 | NPP-375D | MILAGRES | CEARÁ | Brasil | 2308302 | 23 | 33 | nan | nan | nan | Caatinga | 1.8 |
| c0465fc5-62b9-35d4-9440-cddc5d7bd514 | -6.76409 | -34.97849 | 2024-11-09 03:17:00 | NPP-375D | MARCAÇÃO | PARAÍBA | Brasil | 2509057 | 25 | 33 | nan | nan | nan | Mata Atlântica | 3.7 |
| 926ef554-6b33-3d02-8f54-ca5d5848f089 | -9.81146 | -36.15076 | 2024-11-09 03:17:00 | NPP-375D | SÃO MIGUEL DOS CAMPOS | ALAGOAS | Brasil | 2708600 | 27 | 33 | nan | nan | nan | Mata Atlântica | 12.0 |
| 34deb69b-3066-3680-b877-492b96aaaaca | -11.08999 | -43.34681 | 2024-11-09 03:19:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 65.7 |
| 2c356b58-ad26-345e-b66e-18704702f93a | -11.07851 | -43.33911 | 2024-11-09 03:19:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 30.0 |
| 4a4ca655-443b-393d-aed9-a52a6b4e8c82 | -11.09954 | -43.33541 | 2024-11-09 03:19:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 15.8 |
| e30fd58a-a2b4-3010-8752-108e77daf89e | -11.08443 | -43.33897 | 2024-11-09 03:19:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 42.7 |
| 1a387710-36f3-38be-b6d8-fda5b4c3e101 | -11.08308 | -43.34546 | 2024-11-09 03:19:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 65.7 |
| a0183066-ed53-3617-992b-b4142fecd068 | -11.08671 | -43.33409 | 2024-11-09 03:19:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 22.3 |
| dd36d39f-e5d1-3a92-952a-54fd1895c726 | -10.51585 | -42.39548 | 2024-11-09 03:19:00 | NPP-375D | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 69550d3e-c739-3a4d-a0d6-d7ec195be214 | -11.09133 | -43.34037 | 2024-11-09 03:19:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 42.7 |
| 1c0a201f-ad63-308c-bd94-8206a5509692 | -11.07753 | -43.33755 | 2024-11-09 03:19:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 98a5c05f-d2fb-389f-835f-757f0c98b31c | -11.0772 | -43.34562 | 2024-11-09 03:19:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 30.0 |
| a069d2b1-296b-3d14-952b-6d39bffad42a | -11.09265 | -43.33397 | 2024-11-09 03:19:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 42.7 |
| d5e79382-9b04-366d-9390-bc2d55f19865 | -11.0841 | -43.34702 | 2024-11-09 03:19:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 30.0 |
| f81404ca-4eff-3edf-b2c4-a4880544ba97 | -11.08541 | -43.34054 | 2024-11-09 03:19:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 30.0 |
| 97d25dd1-a353-317e-8e01-ee545ca55ece | -11.09822 | -43.3418 | 2024-11-09 03:19:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 15.8 |
| 04cd11ed-96df-3a10-b760-ddcb21d23d11 | -10.50926 | -42.39412 | 2024-11-09 03:19:00 | NPP-375D | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 1.5 |
| abf05562-4dc6-3d6d-9a2d-29fd37d81100 | -4.2484 | -47.5947 | 2024-11-09 03:20:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 53.4 |
| f0e38ebe-0dbc-34c4-9c93-60239d603714 | -3.6003 | -47.3614 | 2024-11-09 03:20:00 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 165.9 |
| 6485ba64-4720-3f75-b0b8-71ccb68c40d2 | -3.6004 | -47.3395 | 2024-11-09 03:20:00 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 249.9 |
| 7be7b4cf-1da9-3fef-af69-766a89d39fcc | -3.9483 | -48.1724 | 2024-11-09 03:20:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 53.3 |
| 48d31fe9-15f2-3853-a9a7-fea82cde78cf | -3.1511 | -52.9731 | 2024-11-09 03:20:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 96.4 |
| 0278e696-caa1-3344-b127-0a8dcb58f940 | -4.2058 | -48.5491 | 2024-11-09 03:20:00 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 36.8 |
| c3c74c51-5e5b-38f8-bbf3-b90e299cf0f9 | -2.2295 | -53.7832 | 2024-11-09 03:20:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 57.1 |
| 47e5ab54-1ca7-3a47-aa45-ba767c061115 | -3.735 | -54.2292 | 2024-11-09 03:20:00 | GOES-16 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 55.5 |
| 461da0a1-8324-30c3-9cb7-d5510d1a2f02 | -4.2033 | -45.8538 | 2024-11-09 03:20:00 | GOES-16 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 61.5 |
| bb481809-afd5-3bdc-b1fe-0555f2090274 | -1.5164 | -52.1696 | 2024-11-09 03:20:00 | GOES-16 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 52.7 |
| fbde196e-d863-361e-a4a1-5d103789a7d7 | -3.5462 | -43.5663 | 2024-11-09 03:20:00 | GOES-16 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 58.0 |
| 29662afe-1a46-3d4e-a694-66d94fdcd236 | -3.1327 | -52.9736 | 2024-11-09 03:20:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 82.5 |
| 3d1a6e76-2e84-30ba-a93f-328f9ef1df8c | -3.9854 | -48.1708 | 2024-11-09 03:20:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 77.0 |
| ae5b476d-3572-3084-8d7f-b978f157496c | -4.2486 | -47.5729 | 2024-11-09 03:20:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 141.9 |
| 392ededc-c344-377e-a6ee-65245564b199 | -3.5819 | -47.3403 | 2024-11-09 03:20:00 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 165.2 |
| c1e7e106-c35a-3707-950c-9eaa0d3371bb | -3.9853 | -48.1924 | 2024-11-09 03:20:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 62.6 |
| b4377a88-a479-351b-99d0-dbf4c75ae9c0 | -2.2295 | -53.7631 | 2024-11-09 03:20:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 57.1 |
| 74109ce9-2924-36c6-8d16-250a6985189d | -1.5163 | -52.1901 | 2024-11-09 03:20:00 | GOES-16 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 56.0 |
| 5d2c3101-7ab1-354b-b7e2-95f46e54ac4b | -3.9669 | -48.1716 | 2024-11-09 03:20:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 265.8 |
| 20b4ebb8-c8b9-3514-8377-b19cf61a28d1 | -3.9668 | -48.1932 | 2024-11-09 03:20:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 181.2 |
| 00bf8719-c956-35a2-8e63-1c8d66abdb69 | -3.5818 | -47.3621 | 2024-11-09 03:20:00 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 110.0 |
| c14c45d5-3a2a-3ec8-b9e5-737a391b9c0d | -4.2671 | -47.572 | 2024-11-09 03:20:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 52.8 |
| e7937459-7a55-3fce-a51b-abd095f3dcec | -3.0865 | -50.5625 | 2024-11-09 03:20:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 96.3 |
| 5b6cff79-a0d0-3ad1-b4ee-be1ebf833ec9 | -3.9668 | -48.1932 | 2024-11-09 03:30:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 182.5 |
| 4fb60ab6-af3f-3308-bf46-cd022bf3aede | -11.0689 | -43.3248 | 2024-11-09 03:30:00 | GOES-16 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 64.9 |
| f04ef423-09cf-3d03-b6b2-fe052f7277d2 | -1.5164 | -52.1696 | 2024-11-09 03:30:00 | GOES-16 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 57.1 |
| b7261a6e-d153-310e-9cfd-281d67552ca5 | -4.2033 | -45.8538 | 2024-11-09 03:30:00 | GOES-16 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 57.9 |
| 2a328717-63cd-3201-80c2-08aabd029ead | -3.1511 | -52.9731 | 2024-11-09 03:30:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 119.3 |
| d8a9dd5b-be84-3f22-9184-4bbf6f3068a2 | -11.0877 | -43.3456 | 2024-11-09 03:30:00 | GOES-16 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 257.5 |
| 175649fd-fb88-3c50-b228-3c3dc2ddc3bc | -3.9483 | -48.1724 | 2024-11-09 03:30:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 50.3 |
| 4c086a09-d7ff-37bd-b65c-feef0129ae64 | -3.6004 | -47.3395 | 2024-11-09 03:30:00 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 193.4 |
| 65116a88-94db-3d5c-b22f-5f54f0926a42 | -3.6003 | -47.3614 | 2024-11-09 03:30:00 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 157.6 |
| 86d065c4-00fb-3842-ab94-1c367a31f003 | -2.2295 | -53.7832 | 2024-11-09 03:30:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 72.0 |
| 7c7267a4-55a1-3376-b3da-90ab02fd5503 | -2.2295 | -53.7631 | 2024-11-09 03:30:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 68.4 |
| ed3a65e7-a3a4-3a66-afc1-07d36203622b | -1.5163 | -52.1901 | 2024-11-09 03:30:00 | GOES-16 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 55.1 |
| e769ef6b-0487-336f-891b-de62f9dc77b8 | -3.9853 | -48.1924 | 2024-11-09 03:30:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 98.5 |
| 71c601e8-9880-388e-8428-b880794ff908 | -3.0865 | -50.5625 | 2024-11-09 03:30:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 85.9 |
| a707f1fd-a69d-3d82-9c1c-d2250f708f2d | -4.2671 | -47.572 | 2024-11-09 03:30:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 78.5 |
| 9635b423-c9a1-3c06-90e8-2340c2e381f0 | -4.2058 | -48.5491 | 2024-11-09 03:30:00 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 56.8 |
| 960f1583-0d44-3203-a7d8-3aafecd4e0ee | -2.6764 | -51.8189 | 2024-11-09 03:30:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 59.1 |
| d82c3169-cd7e-3ca0-8aeb-195c4ab8352e | -11.0685 | -43.3485 | 2024-11-09 03:30:00 | GOES-16 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 78.0 |
| a978f2f4-0585-3ff7-adeb-3c985e644a6d | -3.5818 | -47.3621 | 2024-11-09 03:30:00 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 126.4 |
| 41a29168-32e2-330b-b649-eeb8906039b6 | -3.9854 | -48.1708 | 2024-11-09 03:30:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 85.4 |
| fe675c04-94ae-3542-92a6-039c224c5739 | -3.9669 | -48.1716 | 2024-11-09 03:30:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 228.3 |
| 7b105cca-30aa-33e3-912f-e88e70c24dd8 | -2.2318 | -46.5508 | 2024-11-09 03:30:00 | GOES-16 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 43.8 |
| c540f7d7-cc72-348a-a079-6a198d835823 | -3.5819 | -47.3403 | 2024-11-09 03:30:00 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 147.5 |
| 132e2a9f-11c8-3cab-878c-ffe09aac6e76 | -11.1073 | -43.319 | 2024-11-09 03:30:00 | GOES-16 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 94.7 |
| d680140b-6e5c-3954-b221-95c08c79c375 | -4.2486 | -47.5729 | 2024-11-09 03:30:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 131.6 |
| 97f4b505-ff86-376c-832a-364d8d58bb25 | -11.0881 | -43.3219 | 2024-11-09 03:30:00 | GOES-16 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 181.0 |
| 32608dfe-d55b-3d73-a159-8100baa4d9ce | -11.1068 | -43.3428 | 2024-11-09 03:30:00 | GOES-16 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 149.9 |
| b51a3d4e-86e6-3609-bf9a-281b21b7c650 | -4.2033 | -45.8538 | 2024-11-09 03:40:00 | GOES-16 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 55.8 |
| f27cc1cd-3534-3e1e-8a51-3e9cdb7e1224 | -4.2671 | -47.572 | 2024-11-09 03:40:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 60.3 |
| d77a72e3-82e7-3e82-82ea-b9a16f69f9d2 | -3.5818 | -47.3621 | 2024-11-09 03:40:00 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 97.0 |
| bf9d23ab-c2f2-35bc-8aca-38ac60abf20c | -11.0881 | -43.3219 | 2024-11-09 03:40:00 | GOES-16 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 139.7 |
| ab40123d-1f15-32dc-a322-e331996b1c73 | -2.6764 | -51.8189 | 2024-11-09 03:40:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 69.2 |
| 51e4a2df-a1d6-3bfd-b9dc-1a6b3d74d00d | -3.9483 | -48.1724 | 2024-11-09 03:40:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 61.0 |
| c4cf134d-a597-3726-a23b-edd4b9b3515f | -3.9668 | -48.1932 | 2024-11-09 03:40:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 144.8 |
| 54a7c585-ce03-38fc-93f1-d4d42dabba0d | -3.9669 | -48.1716 | 2024-11-09 03:40:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 201.9 |
| 5978e45e-dfe6-3fcf-a853-0ab537941948 | -11.1068 | -43.3428 | 2024-11-09 03:40:00 | GOES-16 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 136.8 |
| ba229456-ef02-325c-b9b0-45a50c4b17c6 | -4.2486 | -47.5729 | 2024-11-09 03:40:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 195.2 |
| fd4bfc71-b356-355f-878d-d3355bf5837c | -12.0122 | -44.1466 | 2024-11-09 03:40:00 | GOES-16 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 52.1 |
| 1fa9482e-e317-36e3-ad54-90fbbdffc169 | -3.0865 | -50.5625 | 2024-11-09 03:40:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 70.7 |
| 41d80e0f-bd24-3be6-9ec6-74c67de90c24 | -3.1511 | -52.9731 | 2024-11-09 03:40:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 93.9 |
| 8c0ffcb4-6c0c-39b8-9c85-3931d024e0c1 | -3.6004 | -47.3395 | 2024-11-09 03:40:00 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 236.3 |
| 39e8e5f0-39a4-3753-8d28-b24f16926e0d | -3.9853 | -48.1924 | 2024-11-09 03:40:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 116.9 |
| 6508afa8-a43c-31e0-9c26-e8de6d2a3425 | -11.1073 | -43.319 | 2024-11-09 03:40:00 | GOES-16 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 82.1 |
| 1359ad1a-a060-3671-9356-358aebfa3109 | -3.068 | -50.5631 | 2024-11-09 03:40:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 59.0 |


[Clique aqui para ver as próximas entradas](README18.md)
