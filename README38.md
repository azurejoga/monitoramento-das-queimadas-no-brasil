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

## Dados Diários - Página 38

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| b43eb63b-b5a1-3816-837b-1c8e5e0aa664 | -17.60263 | -46.69553 | 2025-10-15 04:10:00 | NOAA-20 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| b3a2554d-df55-348a-bb73-15c57eb555cc | -18.79894 | -44.81062 | 2025-10-15 04:10:00 | NOAA-20 | FELIXLÂNDIA | MINAS GERAIS | Brasil | 3125705 | 31 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 661596bb-03aa-34af-8cd6-e4cf4dbe2731 | -21.17021 | -48.41245 | 2025-10-15 04:10:00 | NOAA-20 | TAIÚVA | SÃO PAULO | Brasil | 3553203 | 35 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 306c306a-6b77-3fe4-9691-5dc8d8a075b1 | -19.84541 | -50.63363 | 2025-10-15 04:10:00 | NOAA-20 | CARNEIRINHO | MINAS GERAIS | Brasil | 3114550 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 83e6423f-efd8-3600-80c7-19e67072d6bf | -17.47026 | -45.47288 | 2025-10-15 04:10:00 | NOAA-20 | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 0c334054-9c63-387b-b56f-192ff836f214 | -17.60333 | -46.69138 | 2025-10-15 04:10:00 | NOAA-20 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 7423de2c-8053-34ee-a8f7-b0e3be13c787 | -20.5592 | -54.65932 | 2025-10-15 04:10:00 | NOAA-20 | CAMPO GRANDE | MATO GROSSO DO SUL | Brasil | 5002704 | 50 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 21b99692-da83-3c80-b893-65a7a16dd41b | -24.4367 | -49.49086 | 2025-10-15 04:10:00 | NOAA-20 | JAGUARIAÍVA | PARANÁ | Brasil | 4112009 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 5e0d8a9f-25d6-31d3-ade3-7082781d670f | -20.91746 | -49.26159 | 2025-10-15 04:10:00 | NOAA-20 | CEDRAL | SÃO PAULO | Brasil | 3511300 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| fca350d5-ed6d-320e-a05a-ab3aff658a94 | -23.42381 | -47.54716 | 2025-10-15 04:10:00 | NOAA-20 | IPERÓ | SÃO PAULO | Brasil | 3521002 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| 8b7beca7-6955-3bbb-a270-4b4a6bb09f7b | -21.42955 | -54.14419 | 2025-10-15 04:10:00 | NOAA-20 | NOVA ALVORADA DO SUL | MATO GROSSO DO SUL | Brasil | 5006002 | 50 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 755e88f5-0818-3d78-81f0-040fcf90bfa7 | -20.55726 | -54.6584 | 2025-10-15 04:10:00 | NOAA-20 | CAMPO GRANDE | MATO GROSSO DO SUL | Brasil | 5002704 | 50 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 70cfb472-f412-32df-9c02-8b21b8dad009 | -17.85864 | -45.56776 | 2025-10-15 04:10:00 | NOAA-20 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 871398e3-bd04-3af2-8ad6-515be796d4b2 | -20.30464 | -44.67835 | 2025-10-15 04:10:00 | NOAA-20 | CARMO DO CAJURU | MINAS GERAIS | Brasil | 3114204 | 31 | 33 | nan | nan | nan | Cerrado | 0.4 |
| d912b238-f72a-352d-944f-b6befec5aaf9 | -23.72048 | -47.45653 | 2025-10-15 04:10:00 | NOAA-20 | PIEDADE | SÃO PAULO | Brasil | 3537800 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 6f18dd8b-791b-31a2-9af1-c35927f5f630 | -18.90806 | -47.00124 | 2025-10-15 04:10:00 | NOAA-20 | PATROCÍNIO | MINAS GERAIS | Brasil | 3148103 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 4e9a41aa-cae1-3036-a3d1-3b807d3f9e23 | -18.21574 | -50.94371 | 2025-10-15 04:10:00 | NOAA-20 | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 4331dc96-17dc-3cdb-b597-80738ebf92d8 | -20.43048 | -50.13422 | 2025-10-15 04:10:00 | NOAA-20 | VALENTIM GENTIL | SÃO PAULO | Brasil | 3556107 | 35 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 0a12a9d3-a4dc-3c8d-8826-94a1557da822 | -19.84621 | -50.62957 | 2025-10-15 04:10:00 | NOAA-20 | CARNEIRINHO | MINAS GERAIS | Brasil | 3114550 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 459ff3e0-8310-32f3-8d3f-f9b531b22353 | -18.19553 | -50.74144 | 2025-10-15 04:10:00 | NOAA-20 | QUIRINÓPOLIS | GOIÁS | Brasil | 5218508 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| f9514354-e9bd-3e67-90c1-78a6b8c0d997 | -21.43026 | -54.14084 | 2025-10-15 04:10:00 | NOAA-20 | NOVA ALVORADA DO SUL | MATO GROSSO DO SUL | Brasil | 5006002 | 50 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 1aab62e1-27ed-3370-8463-e52fce4787f9 | -18.20434 | -50.74306 | 2025-10-15 04:10:00 | NOAA-20 | QUIRINÓPOLIS | GOIÁS | Brasil | 5218508 | 52 | 33 | nan | nan | nan | Cerrado | 5.5 |
| cd929ded-e065-3256-a5a3-586c6ffa5af1 | -17.27003 | -50.86059 | 2025-10-15 04:10:00 | NOAA-20 | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 4756c65a-c90e-3920-877b-04b48264ebf9 | -20.7088 | -47.28167 | 2025-10-15 04:10:00 | NOAA-20 | PATROCÍNIO PAULISTA | SÃO PAULO | Brasil | 3536307 | 35 | 33 | nan | nan | nan | Cerrado | 0.9 |
| f8ef2f85-d7f0-3e38-83ed-bd565cb5f97c | -19.84653 | -50.63159 | 2025-10-15 04:10:00 | NOAA-20 | CARNEIRINHO | MINAS GERAIS | Brasil | 3114550 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| c67679b9-9a33-3f49-862c-9a783c47b778 | -22.29694 | -43.49482 | 2025-10-15 04:10:00 | NOAA-20 | VASSOURAS | RIO DE JANEIRO | Brasil | 3306206 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 71414dcb-2776-33bd-bebc-6752c1af75d2 | -18.4475 | -44.90279 | 2025-10-15 04:10:00 | NOAA-20 | TRÊS MARIAS | MINAS GERAIS | Brasil | 3169356 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b58a860c-f44f-3da9-a922-f5d52cc2c559 | -17.71935 | -44.35793 | 2025-10-15 04:10:00 | NOAA-20 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 0b81c6e7-9f5c-3751-86d2-717681c37b4c | -19.94518 | -44.71661 | 2025-10-15 04:10:00 | NOAA-20 | IGARATINGA | MINAS GERAIS | Brasil | 3130200 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| add90e6f-2a34-3467-850c-8c15bb33946b | -20.78394 | -50.19625 | 2025-10-15 04:10:00 | NOAA-20 | GASTÃO VIDIGAL | SÃO PAULO | Brasil | 3516804 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| ca14d0de-1719-3424-aae5-686d7ca22b40 | -19.49496 | -44.27866 | 2025-10-15 04:10:00 | NOAA-20 | SETE LAGOAS | MINAS GERAIS | Brasil | 3167202 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 271c68c4-d978-344b-96a9-fe879ffcc756 | -19.72294 | -49.59409 | 2025-10-15 04:10:00 | NOAA-20 | ITAPAGIPE | MINAS GERAIS | Brasil | 3133402 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.8 |
| 1eb84781-70c2-335e-933e-ef030351a406 | -18.19993 | -50.74228 | 2025-10-15 04:10:00 | NOAA-20 | QUIRINÓPOLIS | GOIÁS | Brasil | 5218508 | 52 | 33 | nan | nan | nan | Cerrado | 5.5 |
| daa036f6-10e6-3559-8004-7ebc637cddea | -24.88265 | -48.54404 | 2025-10-15 04:12:00 | NOAA-20 | BARRA DO TURVO | SÃO PAULO | Brasil | 3505401 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 3e52dfca-7f6f-3304-9ed1-0f3e6cbc9979 | -29.71656 | -51.1046 | 2025-10-15 04:12:00 | NOAA-20 | NOVO HAMBURGO | RIO GRANDE DO SUL | Brasil | 4313409 | 43 | 33 | nan | nan | nan | Pampa | 0.6 |
| 13e06afc-4897-345f-a28a-a6c1ddb82672 | -27.68714 | -48.75044 | 2025-10-15 04:12:00 | NOAA-20 | SANTO AMARO DA IMPERATRIZ | SANTA CATARINA | Brasil | 4215703 | 42 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| df61faee-79fc-3027-be80-b418fa6def4a | -26.41079 | -48.79151 | 2025-10-15 04:12:00 | NOAA-20 | ARAQUARI | SANTA CATARINA | Brasil | 4201307 | 42 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| d74deecd-917a-3dae-921a-995673b76e4a | -28.01735 | -50.22851 | 2025-10-15 04:12:00 | NOAA-20 | LAGES | SANTA CATARINA | Brasil | 4209300 | 42 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| ba903a09-731d-32df-9af5-d4ce5ee6e365 | -28.24814 | -48.78382 | 2025-10-15 04:12:00 | NOAA-20 | IMARUÍ | SANTA CATARINA | Brasil | 4207205 | 42 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 3ee3b0e5-3732-3048-81b5-c9d282578b95 | -26.40986 | -48.79311 | 2025-10-15 04:12:00 | NOAA-20 | ARAQUARI | SANTA CATARINA | Brasil | 4201307 | 42 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 0044f331-dc48-3ec5-b2f2-5b8919392981 | -5.4278 | -44.2172 | 2025-10-15 04:20:00 | GOES-19 | GOVERNADOR EUGÊNIO BARROS | MARANHÃO | Brasil | 2104602 | 21 | 33 | nan | nan | nan | Cerrado | 124.0 |
| 09c0a797-bd46-3f9f-9253-e16d25eade1c | -4.6509 | -43.1337 | 2025-10-15 04:20:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 74.2 |
| a26511d4-b29e-3eda-bb00-b3de32b9f480 | -4.8915 | -43.4678 | 2025-10-15 04:20:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 129.4 |
| 3bcef13e-b739-30a7-ac32-14968b0b9498 | -8.2371 | -43.3382 | 2025-10-15 04:20:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 85.8 |
| b525269c-d8b4-3ff6-8ada-f9c0506b9358 | -4.9102 | -43.4666 | 2025-10-15 04:20:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 164.7 |
| 22e4d0d4-3717-39e5-b9c2-92957b2c3235 | -4.6511 | -43.1104 | 2025-10-15 04:20:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 66.3 |
| d9db39bc-8654-3c33-a962-e7956c7d4391 | -5.4276 | -44.2402 | 2025-10-15 04:20:00 | GOES-19 | GRAÇA ARANHA | MARANHÃO | Brasil | 2104701 | 21 | 33 | nan | nan | nan | Cerrado | 62.8 |
| e351946c-f8c2-35bc-b31b-922f73b41a1e | -7.9439 | -44.1381 | 2025-10-15 04:20:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 47.5 |
| e532e7dd-4bd6-3cdd-8be9-0c05c4063bc1 | -4.9104 | -43.4434 | 2025-10-15 04:20:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 104.8 |
| 2178983b-3b08-32ef-a161-8dbf9b419d95 | -4.8916 | -43.4446 | 2025-10-15 04:20:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 93.0 |
| 7003c318-b459-3fbb-a16e-4ffa2a0155c6 | -5.4465 | -44.2159 | 2025-10-15 04:20:00 | GOES-19 | GOVERNADOR EUGÊNIO BARROS | MARANHÃO | Brasil | 2104602 | 21 | 33 | nan | nan | nan | Cerrado | 78.8 |
| b61bd072-f76b-3c45-b67e-3887c91b39ed | -8.2561 | -43.3361 | 2025-10-15 04:20:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 74.3 |
| 31137d94-6139-3a7b-8f7c-12d27314494b | -4.6509 | -43.1337 | 2025-10-15 04:30:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 67.3 |
| 9b5ca3f6-9429-3cae-a3b0-655bdefdf8ed | -5.4278 | -44.2172 | 2025-10-15 04:30:00 | GOES-19 | GOVERNADOR EUGÊNIO BARROS | MARANHÃO | Brasil | 2104602 | 21 | 33 | nan | nan | nan | Cerrado | 105.0 |
| a44b88a7-a0eb-3167-b3a6-ab16ec6fcb59 | -5.4465 | -44.2159 | 2025-10-15 04:30:00 | GOES-19 | GOVERNADOR EUGÊNIO BARROS | MARANHÃO | Brasil | 2104602 | 21 | 33 | nan | nan | nan | Cerrado | 71.2 |
| 949a374a-af0c-3666-b402-56f7952677d5 | -4.6511 | -43.1104 | 2025-10-15 04:30:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 75.1 |
| 6ab4b8a1-d8de-3fd9-885a-3a0fe02295a1 | -4.9102 | -43.4666 | 2025-10-15 04:30:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 209.2 |
| 19e0b1fb-d023-3183-a68b-5d4904d6e48a | -2.8147 | -49.1993 | 2025-10-15 04:30:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 32.3 |
| 4931aa88-40fa-3b1f-97dc-6c22160d3253 | -4.8915 | -43.4678 | 2025-10-15 04:30:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 125.8 |
| 25f16bda-1447-3877-a556-5249bd3aabb1 | -4.9104 | -43.4434 | 2025-10-15 04:30:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 154.5 |
| a268a4fb-1e53-3542-a61b-2d99320023cc | -3.564 | -51.1104 | 2025-10-15 04:30:00 | GOES-19 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 51.1 |
| bef05041-f7de-31a0-92cc-d29d6ac7a7c6 | -4.8916 | -43.4446 | 2025-10-15 04:30:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 103.0 |
| fb4d4aa8-f0ee-3845-99d3-679abadac7d2 | -4.9102 | -43.4666 | 2025-10-15 04:40:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 253.4 |
| e1317a0e-7e27-3c04-a842-88940d3a346a | -5.4465 | -44.2159 | 2025-10-15 04:40:00 | GOES-19 | GOVERNADOR EUGÊNIO BARROS | MARANHÃO | Brasil | 2104602 | 21 | 33 | nan | nan | nan | Cerrado | 78.4 |
| 48784d34-b1a3-3cbc-b146-c0f5419d1d37 | -4.6509 | -43.1337 | 2025-10-15 04:40:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 61.1 |
| 186f5fde-cb4b-3996-ba13-00fd0dfafb42 | -4.8916 | -43.4446 | 2025-10-15 04:40:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 130.5 |
| b77f9644-54eb-36d6-9337-480451a2dfe0 | -4.9104 | -43.4434 | 2025-10-15 04:40:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 194.9 |
| 11cc44c5-e244-33ef-a546-b02a821f05d0 | -3.564 | -51.1104 | 2025-10-15 04:40:00 | GOES-19 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 60.5 |
| e4522158-5771-3f6e-814b-d7e35ae91bb8 | -13.3138 | -45.5425 | 2025-10-15 04:40:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 97.0 |
| aa035247-fd45-3076-863c-45b4224e2dea | -5.4278 | -44.2172 | 2025-10-15 04:40:00 | GOES-19 | GOVERNADOR EUGÊNIO BARROS | MARANHÃO | Brasil | 2104602 | 21 | 33 | nan | nan | nan | Cerrado | 113.6 |
| 3102de32-3d45-3331-aaf0-627549fbe23a | -4.6511 | -43.1104 | 2025-10-15 04:40:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 95.4 |
| 8a5ece77-6998-3ace-a5d4-1501f1ff5684 | -0.8967 | -47.5384 | 2025-10-15 04:40:00 | GOES-19 | MARACANÃ | PARÁ | Brasil | 1504307 | 15 | 33 | nan | nan | nan | Amazônia | 48.9 |
| be17d2c5-f94b-3ff5-9fa2-d8fb73373ad9 | -4.8915 | -43.4678 | 2025-10-15 04:40:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 149.8 |
| 51ada805-9260-3cc9-b67f-52cef06746fc | -13.2944 | -45.5457 | 2025-10-15 04:40:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 71.9 |
| 69b74ec2-9480-3101-a0bc-48f6f3a8a640 | -12.2877 | -50.4004 | 2025-10-15 04:50:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 63.0 |
| ed2b5317-991a-3fe7-9a15-f0c34844f41a | -12.2683 | -50.4242 | 2025-10-15 04:50:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 57.7 |
| 78fb94eb-1bf3-33e2-bc24-87f1d004e48b | -5.4278 | -44.2172 | 2025-10-15 04:50:00 | GOES-19 | GOVERNADOR EUGÊNIO BARROS | MARANHÃO | Brasil | 2104602 | 21 | 33 | nan | nan | nan | Cerrado | 108.2 |
| 93fc287a-2b10-3894-bdb2-b0129010767f | -12.2686 | -50.4027 | 2025-10-15 04:50:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 202.5 |
| d3a6f0b1-0d2c-39cb-b97d-913fb36dc628 | -5.4465 | -44.2159 | 2025-10-15 04:50:00 | GOES-19 | GOVERNADOR EUGÊNIO BARROS | MARANHÃO | Brasil | 2104602 | 21 | 33 | nan | nan | nan | Cerrado | 71.0 |
| 67859622-3179-3d71-bea3-3655476e7fe5 | -4.9102 | -43.4666 | 2025-10-15 04:50:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 556.8 |
| 70ad812d-2889-389d-8821-47d1f344ce5c | -4.8916 | -43.4446 | 2025-10-15 04:50:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 208.2 |
| b85fce5c-a6d4-3500-8be3-2a7ef9cea42f | -4.9104 | -43.4434 | 2025-10-15 04:50:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 334.5 |
| ea4c8af9-7b07-3297-8cd9-1bb8f83ae248 | -4.8915 | -43.4678 | 2025-10-15 04:50:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 297.9 |
| 44d011a5-f344-3927-b386-746d73fb3af4 | -3.564 | -51.1104 | 2025-10-15 04:50:00 | GOES-19 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 68.4 |
| c42c6280-b0f2-3092-a782-5cf8f2c82ec8 | -5.01402 | -44.49632 | 2025-10-15 04:55:00 | NOAA-21 | SÃO JOSÉ DOS BASÍLIOS | MARANHÃO | Brasil | 2111250 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 6d370879-ff49-3a4e-9c5a-07bf1048c95a | -3.15738 | -49.17465 | 2025-10-15 04:55:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 52a79e30-4f94-35d7-adb3-9167f67b7af7 | -4.82593 | -45.44561 | 2025-10-15 04:55:00 | NOAA-21 | LAGOA GRANDE DO MARANHÃO | MARANHÃO | Brasil | 2105963 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 0c567f2c-1e09-3269-b912-8fdf8d06ce69 | -3.05225 | -44.47602 | 2025-10-15 04:55:00 | NOAA-21 | SANTA RITA | MARANHÃO | Brasil | 2110203 | 21 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 7de1cfec-e5dc-3dad-8c55-c9100b0587a4 | -3.51985 | -49.71645 | 2025-10-15 04:55:00 | NOAA-21 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 55905daa-3a25-3dd8-8861-db3e4dfd92c0 | 1.86199 | -55.69941 | 2025-10-15 04:55:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 5027cc2b-0015-3018-9f81-8ecb36f49733 | -2.7963 | -48.94101 | 2025-10-15 04:55:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 5cbd520a-b5f7-38f3-b4c0-fa2f3a31062b | -4.11447 | -48.72677 | 2025-10-15 04:55:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 4a8029e8-9224-38c4-a7db-59e7fa9e2439 | -3.52884 | -50.31219 | 2025-10-15 04:55:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 10ab1311-df00-3ff3-9438-fd6b3ba19e6a | -4.11401 | -48.0219 | 2025-10-15 04:55:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 22c15852-77d8-3eed-9dce-a74c415d8c4c | -3.05703 | -44.48008 | 2025-10-15 04:55:00 | NOAA-21 | SANTA RITA | MARANHÃO | Brasil | 2110203 | 21 | 33 | nan | nan | nan | Amazônia | 4.1 |
| f9709cc8-a812-3490-82b7-5fd17eb41831 | -3.43939 | -51.03964 | 2025-10-15 04:55:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| c60523fd-591d-3926-a2f0-36eaff73bf70 | -2.87584 | -50.73891 | 2025-10-15 04:55:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| e15cc230-cc54-39eb-85bf-a72a2cf83d27 | -4.87872 | -45.94031 | 2025-10-15 04:55:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f7f9ba61-e4ec-3062-91cd-d7fe978a5e5b | -3.73402 | -44.13944 | 2025-10-15 04:55:00 | NOAA-21 | PIRAPEMAS | MARANHÃO | Brasil | 2108801 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| c4f72fef-80c1-3ed9-8c3e-54c212550259 | -3.13728 | -50.2093 | 2025-10-15 04:55:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |


[Clique aqui para ver as próximas entradas](README39.md)
