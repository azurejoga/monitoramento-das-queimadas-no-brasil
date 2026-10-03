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

## Dados Diários - Página 12

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| b1291078-cc9b-3361-b26e-ee440c0f6edb | -4.5706 | -46.5907 | 2026-10-03 01:10:00 | GOES-19 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 64.9 |
| dff14689-6f9b-3bd3-b57a-3046a37f110c | -6.4933 | -58.5242 | 2026-10-03 01:10:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 73.9 |
| 50d422f5-a499-39e0-b9bf-8ec8ebbe7675 | -3.1299 | -53.7431 | 2026-10-03 01:20:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 198.6 |
| 196193e2-75e6-3b17-80dc-ccfc4fec5e44 | -10.9881 | -59.1197 | 2026-10-03 01:20:00 | GOES-19 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Amazônia | 55.4 |
| ef949d9b-a31b-3034-9c2d-1270cf145ef0 | -5.9569 | -43.67 | 2026-10-03 01:20:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 70.6 |
| d48815ae-d47d-3223-9b8e-f0cac0198181 | -11.793 | -43.5452 | 2026-10-03 01:20:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 99.4 |
| 3a6698dd-b514-3abd-be6e-e434928580af | -3.13 | -53.7229 | 2026-10-03 01:20:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 96.7 |
| e7a89901-86a9-3ecf-bd0e-20d3d5973710 | 1.8037 | -55.5854 | 2026-10-03 01:20:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 42.6 |
| 5cc6aa61-561d-3ac5-93bc-a7410b46d4cd | -2.8897 | -54.1313 | 2026-10-03 01:20:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 48.1 |
| 9cfc8fcd-cd52-318d-b645-53b03018b0b5 | -2.9082 | -54.0907 | 2026-10-03 01:20:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 37.1 |
| d1cb8533-b64d-391d-91c0-fea52c8b9070 | -3.1116 | -53.7234 | 2026-10-03 01:20:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 43.4 |
| 48f79c25-a620-3fa7-a96d-328b03d2d59e | -2.9266 | -54.0903 | 2026-10-03 01:20:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 45.3 |
| 1500e4af-4a4b-39b3-9ae6-982db879a3e1 | -5.9384 | -43.6482 | 2026-10-03 01:20:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 122.6 |
| 6caad554-1d28-3bd9-bff2-ce3ea00bcf45 | -4.7434 | -43.2679 | 2026-10-03 01:20:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 58.5 |
| afc3e256-4391-3ca5-9a31-b9d86937ddce | -5.7376 | -45.1533 | 2026-10-03 01:20:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 105.8 |
| bca90e48-bc3a-3492-8be7-871b2fb15f52 | -3.1839 | -54.0839 | 2026-10-03 01:20:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 52.0 |
| 91e339f8-9a1e-3d76-9f0c-ecc0f527346f | -6.0508 | -62.5294 | 2026-10-03 01:20:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 55.4 |
| 666091e3-1955-3521-8a88-223f0f4c01a4 | -3.1299 | -53.7633 | 2026-10-03 01:20:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 65.8 |
| d9d00746-d3a6-3d43-b1da-7db2db96627f | -11.8123 | -43.5422 | 2026-10-03 01:20:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 82.6 |
| ecee61cf-8e0d-30f6-b94e-ee790bfb3a1f | -4.5706 | -46.5907 | 2026-10-03 01:20:00 | GOES-19 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 65.7 |
| 5a52a8cd-2520-3be5-ab0a-b56574920905 | -11.7935 | -43.5215 | 2026-10-03 01:20:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 109.3 |
| 14d9d903-6f51-3761-b045-1baa5f02b43e | -6.4933 | -58.5242 | 2026-10-03 01:20:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 87.3 |
| 0357cab7-0d75-3c52-a6c8-3952d638578c | -3.1483 | -53.7426 | 2026-10-03 01:20:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 55.2 |
| 15ef6257-a119-3459-8d56-8ad1b9cd7ba0 | -2.8898 | -54.1112 | 2026-10-03 01:20:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 37.3 |
| 39bace1c-86e3-3935-abae-0b067cb9efc8 | -3.1655 | -54.0844 | 2026-10-03 01:20:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 44.1 |
| 2c792c34-52d8-396f-ba07-5cafea3597e6 | -3.1838 | -54.104 | 2026-10-03 01:20:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 49.6 |
| 7f1b7801-123c-3959-95ba-c5753e22cd06 | -2.8856 | -45.395 | 2026-10-03 01:20:00 | GOES-19 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 44.5 |
| 7161ed27-d39f-3fdd-beee-174597306d0b | -5.6134 | -44.3876 | 2026-10-03 01:20:00 | GOES-19 | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 66.0 |
| d452876c-dff7-3bb4-84cf-86f504e3968f | -4.4506 | -47.9329 | 2026-10-03 01:20:00 | GOES-19 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 72.5 |
| 89f41b25-7b6c-3d5c-93c0-c713d937f447 | -5.7355 | -43.2916 | 2026-10-03 01:20:00 | GOES-19 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 54.1 |
| 13e9a15b-f964-38d3-b595-a928a7b8d1ec | -2.9265 | -54.1104 | 2026-10-03 01:20:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 37.9 |
| c1f73d02-aaf0-36b3-bb95-e06439f137c8 | -5.9571 | -43.6467 | 2026-10-03 01:20:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 121.7 |
| 17923aa1-5370-3502-98e7-d93ca2a4a6a8 | -5.9381 | -43.6714 | 2026-10-03 01:20:00 | GOES-19 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 74.2 |
| a7ab2b1a-b28b-3a1b-8846-cdc429e93dd2 | -11.7174 | -43.4861 | 2026-10-03 01:20:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 103.8 |
| a178bde7-1aaa-3649-9a58-856b7da73e56 | 1.7854 | -55.5856 | 2026-10-03 01:20:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 49.9 |
| 87464147-3ad7-37c6-9b72-0ed4b8b98f26 | -3.1116 | -53.7436 | 2026-10-03 01:20:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 77.0 |
| 34f53d32-638c-3e56-babb-5c8660f096f8 | -2.8855 | -45.4175 | 2026-10-03 01:20:00 | GOES-19 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 47.4 |
| 04e3f8cc-d8e4-33cc-9929-3889ef51f32f | -10.9879 | -59.1393 | 2026-10-03 01:20:00 | GOES-19 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Amazônia | 72.4 |
| 2e0d90af-caf5-35c6-b9f7-585ba003efc9 | -2.8855 | -45.4175 | 2026-10-03 01:30:00 | GOES-19 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 44.3 |
| b32ec024-49ff-3612-8c75-d408ad8796a2 | -3.2767 | -53.84 | 2026-10-03 01:30:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 58.6 |
| 22a168f9-d28d-3940-8b6d-293f91e3f3dd | -5.9571 | -43.6467 | 2026-10-03 01:30:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 114.2 |
| eece8a6a-e536-3314-9e03-ba3d170030ca | -3.1839 | -54.0839 | 2026-10-03 01:30:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 53.2 |
| 4d1572be-9bac-3ac2-be58-5241f31b1c24 | -4.4507 | -47.9112 | 2026-10-03 01:30:00 | GOES-19 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 77.4 |
| 7c590b77-6863-3984-9459-e0785d5c2433 | -5.9569 | -43.67 | 2026-10-03 01:30:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 68.1 |
| 323cdc30-9bdd-3a87-8990-d479ef45332c | -2.9082 | -54.0907 | 2026-10-03 01:30:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 41.6 |
| 28ffa36f-9560-3fdf-a556-1293ccfbf5c4 | -6.4933 | -58.5242 | 2026-10-03 01:30:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 84.6 |
| 43aa48db-99ba-311c-96fb-a018a9084578 | -2.9266 | -54.0903 | 2026-10-03 01:30:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 44.0 |
| 9ce66a20-7179-3839-b3a8-bb06d38717aa | -2.8897 | -54.1313 | 2026-10-03 01:30:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 51.5 |
| 59df92b5-7daf-3a1b-a6bb-cbee056ba525 | -5.9384 | -43.6482 | 2026-10-03 01:30:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 119.5 |
| f669385c-18c0-3816-8404-41162702093b | 1.7854 | -55.5856 | 2026-10-03 01:30:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 21.7 |
| 467052d1-b704-3686-ba4f-8f89119fc2f0 | -4.7434 | -43.2679 | 2026-10-03 01:30:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 56.6 |
| b6805a66-9a91-38a0-894d-b28b868e0e66 | -5.7376 | -45.1533 | 2026-10-03 01:30:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 105.2 |
| 799e555d-cd5b-39f0-b264-8381dbbb726c | -5.9381 | -43.6714 | 2026-10-03 01:30:00 | GOES-19 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 75.8 |
| 58960bfa-f4df-3f95-b912-c195f5f0592f | -3.1838 | -54.104 | 2026-10-03 01:30:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 48.7 |
| 2db7c79b-f0e1-365f-be87-0ebb31e0495d | -6.0508 | -62.5294 | 2026-10-03 01:30:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 46.8 |
| ac984440-e06d-38ea-bd6d-2825b2733fba | -5.6134 | -44.3876 | 2026-10-03 01:30:00 | GOES-19 | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 69.5 |
| 1bce8f3e-f07b-341b-a56f-e34dbf861b03 | -4.4506 | -47.9329 | 2026-10-03 01:30:00 | GOES-19 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 93.4 |
| afb538c9-457e-3195-aecb-5056c2963253 | -11.7174 | -43.4861 | 2026-10-03 01:30:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 93.4 |
| f6941531-521b-38ec-8b63-30384ee475c8 | -3.2951 | -53.8395 | 2026-10-03 01:30:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 62.3 |
| 3c96fba5-da80-3086-92f8-251bbb7b2942 | -10.9879 | -59.1393 | 2026-10-03 01:30:00 | GOES-19 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Amazônia | 86.0 |
| 75450f4b-8108-31de-8fde-1b2eba9f0e2a | -9.711 | -57.4548 | 2026-10-03 01:30:00 | GOES-19 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 54.6 |
| 4b9ca206-4a06-3341-a2a6-2da1110942e7 | -4.5706 | -46.5907 | 2026-10-03 01:30:00 | GOES-19 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 73.4 |
| 585e71f0-3c09-3d94-9288-a88bdd9e1783 | -8.86812 | -66.79253 | 2026-10-03 01:34:00 | TERRA_M-M | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 7.7 |
| 656e93e4-9a9a-3323-b22b-3533f24f096e | -12.14094 | -63.17658 | 2026-10-03 01:34:00 | TERRA_M-M | SERINGUEIRAS | RONDÔNIA | Brasil | 1101500 | 11 | 33 | nan | nan | nan | Amazônia | 22.2 |
| 16bd89bc-0369-3b3b-b80e-66624ab7e89e | -8.70212 | -66.74308 | 2026-10-03 01:34:00 | TERRA_M-M | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 16.8 |
| 2f697094-105e-3ccf-b2d3-275a2355dd01 | -9.016 | -65.70738 | 2026-10-03 01:34:00 | TERRA_M-M | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 15.1 |
| 03b5a769-576e-3a69-92df-3a6f3f5a592d | -9.54814 | -68.52388 | 2026-10-03 01:34:00 | TERRA_M-M | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 12.4 |
| 46da5dac-7f39-3aa8-a6d1-74a7d35e5e18 | -12.13285 | -63.18333 | 2026-10-03 01:34:00 | TERRA_M-M | SERINGUEIRAS | RONDÔNIA | Brasil | 1101500 | 11 | 33 | nan | nan | nan | Amazônia | 23.0 |
| f12c9ac9-1e8b-3bc5-9850-a32d432e740e | -9.62038 | -65.73507 | 2026-10-03 01:34:00 | TERRA_M-M | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 14.1 |
| 31174c56-3c68-39fc-a86b-de64f908fe11 | -9.0068 | -65.70223 | 2026-10-03 01:34:00 | TERRA_M-M | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 16.4 |
| b7c1d506-bce7-3e0f-a8d7-70b7d2eb7680 | -8.7008 | -66.72799 | 2026-10-03 01:34:00 | TERRA_M-M | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 19.4 |
| 8ec27ee3-08b6-3c03-99c8-818c3f93642c | -8.85529 | -66.79465 | 2026-10-03 01:34:00 | TERRA_M-M | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 44.4 |
| f597aebf-0721-3f90-81b6-ec179fe944ab | 1.8037 | -55.5854 | 2026-10-03 01:40:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 28.9 |
| 62dc9383-8de5-3781-b2ee-b51bc32b1db1 | -3.2767 | -53.84 | 2026-10-03 01:40:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 70.5 |
| 42c9408b-f20b-3597-b260-9aa6762c6d23 | -3.1299 | -53.7431 | 2026-10-03 01:40:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 119.7 |
| 418f65f6-483f-35f7-a444-1296bdda2993 | -2.8897 | -54.1313 | 2026-10-03 01:40:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 50.5 |
| ce48a119-7528-3abc-a04a-b8bf825ce783 | -5.7376 | -45.1533 | 2026-10-03 01:40:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 97.1 |
| 46114f24-5d70-35fc-bd2d-a96f8083fee5 | -6.4933 | -58.5242 | 2026-10-03 01:40:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 82.1 |
| 0946c919-8363-36b8-a385-a60f054c6a6c | -3.2952 | -53.8194 | 2026-10-03 01:40:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 54.5 |
| a186d960-7c37-371f-85da-37c551cd237a | -3.1839 | -54.0839 | 2026-10-03 01:40:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 54.7 |
| 1e1d73d8-b983-3212-9428-ce04584ab36d | -5.9571 | -43.6467 | 2026-10-03 01:40:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 103.7 |
| a36d62e8-7ca2-3fb9-9e19-6d21c91cc38c | -3.13 | -53.7229 | 2026-10-03 01:40:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 65.7 |
| ccc3bc64-a501-3bca-8ec5-323960174f47 | -3.1116 | -53.7436 | 2026-10-03 01:40:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 49.2 |
| e7324338-e9f5-3c35-a7e0-42ebaf79a742 | -5.9384 | -43.6482 | 2026-10-03 01:40:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 96.7 |
| ce656ab8-5e45-3a09-9da2-6cb7faba77a9 | -5.9381 | -43.6714 | 2026-10-03 01:40:00 | GOES-19 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 56.7 |
| 989d53b5-04d6-316c-a98f-ff9b47fa48dc | -2.9266 | -54.0903 | 2026-10-03 01:40:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 50.1 |
| 6894f669-e238-35ab-a23d-4f3d81624f08 | -3.1483 | -53.7426 | 2026-10-03 01:40:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 55.9 |
| e4c7d0e5-745c-33e7-9577-f7eedfda6f5c | 1.7854 | -55.5856 | 2026-10-03 01:40:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 31.7 |
| adac81eb-211e-3ec7-ac92-60f1dede46c7 | -3.2768 | -53.8199 | 2026-10-03 01:40:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 64.0 |
| db806106-ad8a-3b59-aa85-4f9f7250a49e | -6.4932 | -58.5436 | 2026-10-03 01:40:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 51.3 |
| db8bcdb7-f0e2-3717-83e1-59cbd1e64d99 | -5.6134 | -44.3876 | 2026-10-03 01:40:00 | GOES-19 | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 62.5 |
| 0c6c7127-e645-3afb-a9af-780927910989 | -3.1838 | -54.104 | 2026-10-03 01:40:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 53.2 |
| 84444bf6-e877-3717-bed8-e53a6e14c071 | -5.9569 | -43.67 | 2026-10-03 01:40:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 61.6 |
| ace438f7-af65-37c1-be09-6128984e4694 | -10.9879 | -59.1393 | 2026-10-03 01:40:00 | GOES-19 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Amazônia | 48.5 |
| 9c0b1a3b-0628-383e-8768-83162ab66e1c | -6.9295 | -49.6325 | 2026-10-03 01:40:00 | GOES-19 | SAPUCAIA | PARÁ | Brasil | 1507755 | 15 | 33 | nan | nan | nan | Amazônia | 51.8 |
| 51725061-453b-3732-904a-c6772928eff7 | -3.2951 | -53.8395 | 2026-10-03 01:40:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 66.6 |
| a33ca873-9448-3ae4-be63-0f9359139818 | -3.1299 | -53.7633 | 2026-10-03 01:40:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 43.6 |
| 8a376bcc-5fcd-3f7f-ae2c-01b7fd14d203 | -2.8897 | -54.1313 | 2026-10-03 01:50:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 51.6 |
| d314b805-ee02-332c-905d-9c1b0b67d609 | -2.9266 | -54.0903 | 2026-10-03 01:50:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 45.9 |
| b398aef5-6966-3df3-b173-8380b69a0f15 | -10.9879 | -59.1393 | 2026-10-03 01:50:00 | GOES-19 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Amazônia | 81.1 |


[Clique aqui para ver as próximas entradas](README13.md)
