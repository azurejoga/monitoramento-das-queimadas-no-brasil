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
| e813b041-17db-3206-afcf-20eb0992dc4e | -8.5221 | -46.1301 | 2025-10-10 03:20:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 115.4 |
| 0844bfdf-e744-306e-be98-a7dcaef6ee3a | -18.6497 | -43.9301 | 2025-10-10 03:20:00 | GOES-19 | SANTANA DE PIRAPAMA | MINAS GERAIS | Brasil | 3158508 | 31 | 33 | nan | nan | nan | Cerrado | 124.8 |
| 60b50454-a7f2-3993-83f0-424676ec1512 | -14.9372 | -46.7591 | 2025-10-10 03:20:00 | GOES-19 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 116.7 |
| 37b441eb-9df1-32fc-9d2a-dd221a8d6a19 | -12.6294 | -45.0517 | 2025-10-10 03:20:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 90.5 |
| 0d87617d-a565-30ca-bd42-79b96d6fa53a | -17.9175 | -45.0194 | 2025-10-10 03:20:00 | GOES-19 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 84.6 |
| eaf89157-c211-325b-884b-e3b4d4b20904 | -10.1707 | -44.5959 | 2025-10-10 03:20:00 | GOES-19 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 79.6 |
| 6f7a09a0-bb00-3a0e-9e10-88e1dc99bf75 | -18.6294 | -43.9351 | 2025-10-10 03:20:00 | GOES-19 | GOUVEIA | MINAS GERAIS | Brasil | 3127602 | 31 | 33 | nan | nan | nan | Cerrado | 92.1 |
| f5796c41-8aef-3981-addf-71788575b1aa | -8.5218 | -46.1526 | 2025-10-10 03:20:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 57.0 |
| d5979b76-6b57-37c0-ae3c-b72580f7096c | -17.9376 | -45.0148 | 2025-10-10 03:20:00 | GOES-19 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 181.9 |
| 44cc1283-9bdb-3efc-9abf-e715e88ebc37 | -13.8302 | -45.8255 | 2025-10-10 03:20:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 62.1 |
| ba48755b-735c-3902-9423-1cdf31829066 | -17.9029 | -57.4947 | 2025-10-10 03:20:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 49.0 |
| c0221e71-5d35-319f-9fbf-5bdf811e09a3 | -13.8491 | -45.8454 | 2025-10-10 03:20:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 117.2 |
| 3292db8a-1bc8-3cff-b2cd-0974cac62ea8 | -13.8297 | -45.8486 | 2025-10-10 03:20:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 74.5 |
| fbac1df6-4002-3ca9-9ffa-c12ede3f42c4 | -17.9026 | -57.5153 | 2025-10-10 03:20:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 57.5 |
| 04711329-6407-3bf3-bb9f-85f8ca51e3bd | -8.1996 | -43.3189 | 2025-10-10 03:20:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 42.6 |
| 7aae89b8-6e4f-372a-85c4-0a5218a31362 | -8.5029 | -46.1545 | 2025-10-10 03:20:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 57.0 |
| 53ec8b52-7cad-3d89-9107-29723adaf9e9 | -13.8496 | -45.8223 | 2025-10-10 03:20:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 84.1 |
| 74548438-d2d2-3e84-a088-c362e7ff4848 | -8.5035 | -46.1096 | 2025-10-10 03:30:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 74.6 |
| aefcccc0-f814-30f5-beaf-59020d17c8da | -18.6294 | -43.9351 | 2025-10-10 03:30:00 | GOES-19 | GOUVEIA | MINAS GERAIS | Brasil | 3127602 | 31 | 33 | nan | nan | nan | Cerrado | 110.0 |
| 39fdd6df-b425-3c0e-a7d4-6f9a19f79cb9 | -17.9376 | -45.0148 | 2025-10-10 03:30:00 | GOES-19 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 141.4 |
| f5987bf5-478e-3dc1-864f-ffe59240a17d | -8.5029 | -46.1545 | 2025-10-10 03:30:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 155.3 |
| 34a00edc-bb75-33f2-815d-eb9c9d7b08f2 | -13.8487 | -45.8685 | 2025-10-10 03:30:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 63.5 |
| def08429-daa7-373b-959e-bb47a9b7d610 | -17.9026 | -57.5153 | 2025-10-10 03:30:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 57.4 |
| 51f267d3-58e4-386b-8042-85fa7be98d99 | -8.5032 | -46.1321 | 2025-10-10 03:30:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 246.2 |
| 01a7372e-3cb5-3b6b-9603-35fe1289375a | -13.8491 | -45.8454 | 2025-10-10 03:30:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 181.3 |
| b33edd3b-7f33-31b7-b2a5-a9466289a063 | -8.5218 | -46.1526 | 2025-10-10 03:30:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 103.8 |
| c9863c88-f71c-3c83-bb8b-40450f1da91a | -13.8496 | -45.8223 | 2025-10-10 03:30:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 74.8 |
| 1e0647b8-d8c7-3972-bd67-ffa3abf2aaec | -12.629 | -45.0749 | 2025-10-10 03:30:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 101.8 |
| 0057c16b-6c65-3512-985c-bfade526d223 | -12.6294 | -45.0517 | 2025-10-10 03:30:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 121.0 |
| 2461bc79-b149-39d1-ad0f-ee0139c26088 | -12.6488 | -45.0486 | 2025-10-10 03:30:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 63.8 |
| 3f8159e1-4831-3727-8f12-f71f1306b6ad | -13.8297 | -45.8486 | 2025-10-10 03:30:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 123.0 |
| 275a3310-852d-3432-b192-27f7dfa82e21 | -8.5224 | -46.1076 | 2025-10-10 03:30:00 | GOES-19 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 69.4 |
| 0bfa8d37-594b-374a-9f44-c4a954000fd8 | -10.1517 | -44.5984 | 2025-10-10 03:30:00 | GOES-19 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 99.8 |
| 55448f66-9771-3dae-9fca-d0767e065975 | -18.6497 | -43.9301 | 2025-10-10 03:30:00 | GOES-19 | SANTANA DE PIRAPAMA | MINAS GERAIS | Brasil | 3158508 | 31 | 33 | nan | nan | nan | Cerrado | 153.6 |
| 718e0f0a-f23a-3162-a807-ce159b64f16a | -17.8828 | -57.5177 | 2025-10-10 03:30:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 51.1 |
| 1da6c45d-fdfc-3be4-abda-947ca7e355cf | -8.5221 | -46.1301 | 2025-10-10 03:30:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 189.0 |
| 8b8470f2-c5c0-346d-81e7-9af0afee1619 | -10.1707 | -44.5959 | 2025-10-10 03:30:00 | GOES-19 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 131.2 |
| 636fae4a-48bf-3eb1-bbf9-68cc471b9516 | -17.9175 | -45.0194 | 2025-10-10 03:30:00 | GOES-19 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 86.3 |
| 62ff041b-3ce8-37cc-9869-8c0e2f18743b | -4.84678 | -42.76636 | 2025-10-10 03:38:00 | NPP-375D | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 6b34f4e3-3147-3c9a-92cc-6d7ce1554b3b | -4.84661 | -42.77002 | 2025-10-10 03:38:00 | NPP-375D | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 160f1f26-de20-3bc8-aaf3-280eab1816d3 | -4.44317 | -40.77362 | 2025-10-10 03:38:00 | NPP-375D | IPUEIRAS | CEARÁ | Brasil | 2305902 | 23 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 3150932e-d5c5-3ce9-8235-3d7769557c9e | -4.95111 | -42.81649 | 2025-10-10 03:38:00 | NPP-375D | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Cerrado | 4.0 |
| b9012154-0ced-3b6f-8637-8dac232943d0 | -4.49613 | -45.87768 | 2025-10-10 03:38:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 66c705ae-f464-3d0a-bbed-5779e102db38 | -5.40036 | -40.98126 | 2025-10-10 03:38:00 | NPP-375D | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| e7a3a8b8-d844-341d-9057-e8baf1ae1f14 | -5.2036 | -44.36005 | 2025-10-10 03:38:00 | NPP-375D | PRESIDENTE DUTRA | MARANHÃO | Brasil | 2109106 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 99860861-be86-3297-9f59-816f7ce144a2 | -4.95119 | -42.81763 | 2025-10-10 03:38:00 | NPP-375D | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 5540e621-db93-3a9f-b03d-026660296828 | -6.52607 | -37.17256 | 2025-10-10 03:38:00 | NPP-375D | CAICÓ | RIO GRANDE DO NORTE | Brasil | 2402006 | 24 | 33 | nan | nan | nan | Caatinga | 1.4 |
| ee4fa68b-33b6-30cc-b079-84b9215936d1 | -5.32987 | -44.82191 | 2025-10-10 03:38:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 8387edd7-6398-3cb0-b18d-d4a98de44d9d | -5.40903 | -40.98837 | 2025-10-10 03:38:00 | NPP-375D | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 10.4 |
| e0bd1c68-ae88-3d87-b1b1-986156dc13b6 | -4.85222 | -42.76746 | 2025-10-10 03:38:00 | NPP-375D | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 0cf935fa-7524-3dc4-9222-9691666acc48 | -5.10283 | -45.21066 | 2025-10-10 03:38:00 | NPP-375D | SÃO RAIMUNDO DO DOCA BEZERRA | MARANHÃO | Brasil | 2111631 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| fed74d56-f68b-3871-81bc-e9eb99c439eb | -5.46346 | -35.66973 | 2025-10-10 03:38:00 | NPP-375D | PUREZA | RIO GRANDE DO NORTE | Brasil | 2410405 | 24 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 8de4358f-c82d-31bc-a6f2-f44c27001af0 | -5.74535 | -42.76368 | 2025-10-10 03:38:00 | NPP-375D | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 5.4 |
| 2ab33197-dd0d-310e-b833-be0c7d68d8c7 | -4.49349 | -45.87413 | 2025-10-10 03:38:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 02ed5828-53fd-3a8f-932c-d431a723d2c5 | -5.1422 | -46.09711 | 2025-10-10 03:38:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 9d15bbe0-cec5-3463-8d97-44d51bf2d853 | -4.47485 | -42.86495 | 2025-10-10 03:38:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| cf17c675-3995-32f9-8990-83ed105daee5 | -4.84616 | -42.76999 | 2025-10-10 03:38:00 | NPP-375D | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Cerrado | 5.1 |
| cb047e9c-b518-39d7-bbe4-75c9dd3c0999 | -5.8421 | -42.30462 | 2025-10-10 03:38:00 | NPP-375D | SÃO MIGUEL DA BAIXA GRANDE | PIAUÍ | Brasil | 2210383 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 2f300897-c948-3924-8e88-f1953823b73d | -5.20437 | -44.35564 | 2025-10-10 03:38:00 | NPP-375D | PRESIDENTE DUTRA | MARANHÃO | Brasil | 2109106 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 376c433f-a96e-3bf4-90d4-bba89679902a | -4.94997 | -42.82482 | 2025-10-10 03:38:00 | NPP-375D | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 835e2bb4-8114-3523-99f2-e10502324c9c | -5.75047 | -42.5264 | 2025-10-10 03:38:00 | NPP-375D | BARRO DURO | PIAUÍ | Brasil | 2201408 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| f94dbaae-d3ab-32b5-b0a5-a9431d9ffd16 | -4.85162 | -42.77105 | 2025-10-10 03:38:00 | NPP-375D | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Cerrado | 0.6 |
| a8374e3d-4155-3e14-b0a0-c67e8269884d | -4.68506 | -45.83734 | 2025-10-10 03:38:00 | NPP-375D | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f1dbbddb-dc1f-3e1e-b952-65e7440d0475 | -4.84014 | -45.41532 | 2025-10-10 03:38:00 | NPP-375D | LAGOA GRANDE DO MARANHÃO | MARANHÃO | Brasil | 2105963 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 351f50c2-bbee-35b1-a693-2dde7892d424 | -5.58847 | -35.25737 | 2025-10-10 03:38:00 | NPP-375D | CEARÁ-MIRIM | RIO GRANDE DO NORTE | Brasil | 2402600 | 24 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 24426331-a8f2-35df-9769-f61e44cc6d01 | -3.18967 | -41.48795 | 2025-10-10 03:38:00 | NPP-375D | LUÍS CORREIA | PIAUÍ | Brasil | 2205706 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 5eed8a01-90f7-3a3e-936e-fb183162caaf | -6.5053 | -35.31483 | 2025-10-10 03:38:00 | NPP-375D | MONTANHAS | RIO GRANDE DO NORTE | Brasil | 2407708 | 24 | 33 | nan | nan | nan | Caatinga | 0.4 |
| 3beaf886-947c-356c-bd91-b16cd7109d9b | -4.84725 | -42.7664 | 2025-10-10 03:38:00 | NPP-375D | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 34404d50-e5c2-31ec-b4ac-5df97b890a87 | -5.68582 | -41.72676 | 2025-10-10 03:38:00 | NPP-375D | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| a2f74171-9ec0-33d0-ac2d-3f5ae9c5a884 | -4.93294 | -38.75102 | 2025-10-10 03:38:00 | NPP-375D | QUIXADÁ | CEARÁ | Brasil | 2311306 | 23 | 33 | nan | nan | nan | Caatinga | 3.0 |
| 789bf627-1051-3471-b104-8ff1c05c8336 | -6.50189 | -35.31428 | 2025-10-10 03:38:00 | NPP-375D | MONTANHAS | RIO GRANDE DO NORTE | Brasil | 2407708 | 24 | 33 | nan | nan | nan | Caatinga | 0.4 |
| b2283b47-d35e-3657-bd10-3f95ebb48998 | -4.95058 | -42.82121 | 2025-10-10 03:38:00 | NPP-375D | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 39964aa6-0659-38c1-a25d-0d747884a587 | -5.33073 | -44.81701 | 2025-10-10 03:38:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 23d82b27-97c2-351b-924d-639393d724ef | -5.20512 | -44.3587 | 2025-10-10 03:38:00 | NPP-375D | PRESIDENTE DUTRA | MARANHÃO | Brasil | 2109106 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 9e4f6360-6d08-3ffb-bc34-22f0258e62c3 | -5.84786 | -42.30241 | 2025-10-10 03:38:00 | NPP-375D | SÃO MIGUEL DA BAIXA GRANDE | PIAUÍ | Brasil | 2210383 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 97070bb3-5ea1-3d60-873b-fe042a14470d | -4.94985 | -42.82364 | 2025-10-10 03:38:00 | NPP-375D | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Cerrado | 7.6 |
| b4df4f2f-81d2-3ba0-87d5-4439d8e85358 | -5.9012 | -38.47616 | 2025-10-10 03:38:00 | NPP-375D | PEREIRO | CEARÁ | Brasil | 2310803 | 23 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 2757a108-7e9c-3a7a-bc31-87c5b21a6d92 | -5.39555 | -40.98046 | 2025-10-10 03:38:00 | NPP-375D | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| faea52e7-4211-34e2-bb9e-d54cdbaaf212 | -4.47547 | -42.86132 | 2025-10-10 03:38:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 356cb535-0ab1-3169-9e63-8de02fa4542f | -4.49251 | -45.87975 | 2025-10-10 03:38:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 6b0401a2-01e4-3c9e-aa14-a4539e294338 | -5.28076 | -44.8825 | 2025-10-10 03:38:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 125c0cba-6222-3762-8f27-3edd37069a6f | -4.84115 | -45.4097 | 2025-10-10 03:38:00 | NPP-375D | LAGOA GRANDE DO MARANHÃO | MARANHÃO | Brasil | 2105963 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 09e50fab-d728-3fa1-9dda-755d74f0e550 | -5.10373 | -45.20568 | 2025-10-10 03:38:00 | NPP-375D | SÃO RAIMUNDO DO DOCA BEZERRA | MARANHÃO | Brasil | 2111631 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 875e72b9-63f1-3762-9bf5-4f792a998a60 | -4.93232 | -38.75477 | 2025-10-10 03:38:00 | NPP-375D | QUIXADÁ | CEARÁ | Brasil | 2311306 | 23 | 33 | nan | nan | nan | Caatinga | 4.3 |
| 2128ae07-65ae-3c7b-9925-97531c3e7a4c | -5.90157 | -38.47563 | 2025-10-10 03:38:00 | NPP-375D | PEREIRO | CEARÁ | Brasil | 2310803 | 23 | 33 | nan | nan | nan | Caatinga | 0.7 |
| d194e4ba-6e19-36e5-b57c-589b061536a9 | -4.69161 | -45.83908 | 2025-10-10 03:38:00 | NPP-375D | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 82d8e680-6572-3298-8be3-dad53b541ecf | -5.328 | -44.82368 | 2025-10-10 03:38:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ac711d2d-bd87-3345-88e4-9ddb2003fc8c | -5.74517 | -42.52541 | 2025-10-10 03:38:00 | NPP-375D | BARRO DURO | PIAUÍ | Brasil | 2201408 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 9a40d25c-a8eb-38d5-a8f1-7f82c57f4d8f | -4.95049 | -42.82005 | 2025-10-10 03:38:00 | NPP-375D | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 648a8c59-bd59-3e8a-8e4b-b86632eab2d2 | -5.32893 | -44.8186 | 2025-10-10 03:38:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| fb1841ad-b33a-3330-b59d-ef01a6c104a3 | -5.89761 | -38.47456 | 2025-10-10 03:38:00 | NPP-375D | PEREIRO | CEARÁ | Brasil | 2310803 | 23 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 2a037955-c293-3022-a46c-eccfee7fc086 | -6.5849 | -44.6327 | 2025-10-10 03:40:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 60.6 |
| 06b3cdd0-0314-33a6-b578-fbf29f69c663 | -10.1711 | -44.5727 | 2025-10-10 03:40:00 | GOES-19 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 45.0 |
| c3f84a82-718a-3c56-9f1a-1468249baa02 | -10.1517 | -44.5984 | 2025-10-10 03:40:00 | GOES-19 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 120.6 |
| d1b29a01-501f-3905-aa82-44aba957c0da | -13.8491 | -45.8454 | 2025-10-10 03:40:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 113.9 |
| f193ab04-5228-3fa3-9720-2761f25decbc | -12.6294 | -45.0517 | 2025-10-10 03:40:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 189.6 |
| aa8701e2-6c65-34ac-b241-e675749b61e0 | -4.8408 | -42.77 | 2025-10-10 03:40:00 | GOES-19 | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Cerrado | 107.1 |
| 1f9299a9-5ec6-3f7b-bc82-692fc49e98b0 | -17.9376 | -45.0148 | 2025-10-10 03:40:00 | GOES-19 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 167.4 |
| 13c2e0a7-97b3-3068-a8af-76cd0c4ddad3 | -12.629 | -45.0749 | 2025-10-10 03:40:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 122.9 |
| 2e1e3054-08d4-3630-9b1a-29e94a84f29f | -12.6488 | -45.0486 | 2025-10-10 03:40:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 77.4 |


[Clique aqui para ver as próximas entradas](README11.md)
