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

## Dados Diários - Página 8

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 853c6899-15b7-306d-ab4a-89628688c9a6 | -8.0321 | -43.1257 | 2025-08-01 02:50:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 160.7 |
| ed1554e5-e54d-3d21-ae0e-ee14277bd45f | -8.0513 | -43.1001 | 2025-08-01 02:50:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 112.9 |
| abc28ec4-fe10-3c65-9656-b0a6ade2c823 | -6.7295 | -59.153 | 2025-08-01 02:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 111.0 |
| 2953b05f-ee64-3b96-be53-d42707fa686d | -9.5152 | -40.331 | 2025-08-01 03:00:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 97.7 |
| 2928cf7d-f003-3942-bfcf-171b45b671f8 | -6.7293 | -59.1916 | 2025-08-01 03:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 97.4 |
| 1ba4964c-72d7-353a-8555-94f5aba6319c | -6.821 | -59.2844 | 2025-08-01 03:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 96.2 |
| 4d2982eb-6f96-37d4-ac34-fbaf1f2687fe | -6.6329 | -59.9649 | 2025-08-01 03:00:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 60.4 |
| 2109337e-7153-37f1-9970-82e222542cca | -6.7478 | -59.1716 | 2025-08-01 03:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 225.8 |
| 7add4eef-361f-327b-9a06-80e3a04513d0 | -6.8397 | -59.245 | 2025-08-01 03:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 60.8 |
| 9c3f5044-c591-3cd5-9693-de1972bf6a4e | -6.6328 | -59.9841 | 2025-08-01 03:00:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 72.3 |
| 767df40c-606c-3ea6-b4ed-d4f394157db3 | -9.5147 | -40.3558 | 2025-08-01 03:00:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 97.7 |
| 9e9d5d41-5e21-31e6-a64f-d67bd2b59edb | -6.8212 | -59.2458 | 2025-08-01 03:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 134.6 |
| b50d2699-0df6-3d4a-895d-9834c9aa50fd | -6.7295 | -59.153 | 2025-08-01 03:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 101.1 |
| 7dde35ae-eaac-308e-965c-e1e42ef8789b | -6.748 | -59.1523 | 2025-08-01 03:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 112.5 |
| 09e3f904-e2c4-3fc9-8043-9d3c8d86b036 | -6.7477 | -59.1909 | 2025-08-01 03:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 66.4 |
| e7187839-34be-3061-8ddc-fe4e885f4604 | -23.5234 | -47.835 | 2025-08-01 03:00:00 | GOES-19 | ALAMBARI | SÃO PAULO | Brasil | 3500758 | 35 | 33 | nan | nan | nan | Mata Atlântica | 139.1 |
| 05fd09b1-d836-348b-95d8-b4aad407d850 | -8.0513 | -43.1001 | 2025-08-01 03:00:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 105.7 |
| da1b6366-efec-3dee-91a0-6247b5ea232b | -8.051 | -43.1237 | 2025-08-01 03:00:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 145.2 |
| 098ab701-fbc2-306a-a271-1ade146b9cd0 | -6.8026 | -59.2658 | 2025-08-01 03:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 95.8 |
| b0da0029-0ca1-34b3-b6d0-b43ec94a90ee | -6.8211 | -59.2651 | 2025-08-01 03:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 372.3 |
| f79c9d72-76a9-3a9d-8e0f-132985410de9 | -6.8395 | -59.2643 | 2025-08-01 03:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 68.4 |
| c8a2da6b-1e59-3e7f-8a76-adf621aea51d | -8.0321 | -43.1257 | 2025-08-01 03:00:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 184.0 |
| 3a87e736-84e5-3bd1-89a4-bd037f332fe8 | -23.5022 | -47.8407 | 2025-08-01 03:00:00 | GOES-19 | ITAPETININGA | SÃO PAULO | Brasil | 3522307 | 35 | 33 | nan | nan | nan | Mata Atlântica | 50.0 |
| 51096b30-9d01-310a-bd3a-326a4c07a0fc | -8.0324 | -43.1022 | 2025-08-01 03:00:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 97.9 |
| 8437284a-2693-3795-b35c-2ee9a75c2227 | -6.7294 | -59.1723 | 2025-08-01 03:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 313.4 |
| e45523e6-68cd-37fc-96c9-ea8f7f964b14 | -23.5242 | -47.8109 | 2025-08-01 03:00:00 | GOES-19 | ALAMBARI | SÃO PAULO | Brasil | 3500758 | 35 | 33 | nan | nan | nan | Mata Atlântica | 70.3 |
| 4d77b31a-8681-3e3f-a95e-e41603f328cf | -6.7478 | -59.1716 | 2025-08-01 03:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 166.6 |
| f07dbed7-902f-36c9-b5df-2020cc2cbac7 | -6.6144 | -59.9656 | 2025-08-01 03:10:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 63.6 |
| 53dbab9e-2298-3235-b51c-452143b4d96c | -23.5234 | -47.835 | 2025-08-01 03:10:00 | GOES-19 | ALAMBARI | SÃO PAULO | Brasil | 3500758 | 35 | 33 | nan | nan | nan | Mata Atlântica | 164.3 |
| 4a224b55-416a-3473-a121-256b1ca28894 | -6.7294 | -59.1723 | 2025-08-01 03:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 312.9 |
| 9e363147-2861-31bf-b0b7-7dc3806857b6 | -8.0513 | -43.1001 | 2025-08-01 03:10:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 112.2 |
| 00f2ad02-f81e-3407-aac7-384a373a797a | -8.051 | -43.1237 | 2025-08-01 03:10:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 114.4 |
| 8fc22486-0e97-3077-acf9-459165262656 | -6.7295 | -59.153 | 2025-08-01 03:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 123.5 |
| d32b9cf4-766d-36fe-adac-8b87e69d52c9 | -6.748 | -59.1523 | 2025-08-01 03:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 97.2 |
| a7bc08a7-b927-3849-a40d-9e35fe706786 | -8.0324 | -43.1022 | 2025-08-01 03:10:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 112.5 |
| bbcf4bbf-2362-34e7-ac46-3ebad3f6784b | -9.5147 | -40.3558 | 2025-08-01 03:10:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 86.0 |
| e1604502-7be1-33c6-a6dd-a9fdb5fd3239 | -9.5152 | -40.331 | 2025-08-01 03:10:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 80.4 |
| 9a10a4c5-258d-3aa4-875f-ad9002e887d9 | -23.5242 | -47.8109 | 2025-08-01 03:10:00 | GOES-19 | ALAMBARI | SÃO PAULO | Brasil | 3500758 | 35 | 33 | nan | nan | nan | Mata Atlântica | 83.2 |
| bf09d377-62fe-36b7-b564-b4a0b8ae61fd | -6.6143 | -59.9848 | 2025-08-01 03:10:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 62.5 |
| 685a1a13-9d2e-33b7-8565-8f201e806e38 | -6.7293 | -59.1916 | 2025-08-01 03:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 110.1 |
| 39d66535-6298-30ce-ab29-a63f5e713eb1 | -8.0321 | -43.1257 | 2025-08-01 03:10:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 228.6 |
| f8010b8a-fdaa-31fe-aa96-73c539d6069c | -23.5242 | -47.8109 | 2025-08-01 03:20:00 | GOES-19 | ALAMBARI | SÃO PAULO | Brasil | 3500758 | 35 | 33 | nan | nan | nan | Mata Atlântica | 53.3 |
| fbea1b0a-0841-38ca-867c-2ff6c028419f | -8.0324 | -43.1022 | 2025-08-01 03:20:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 107.2 |
| f89ad697-70ff-377e-a512-05772b2b8e0f | -8.051 | -43.1237 | 2025-08-01 03:20:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 113.9 |
| 159d788d-a362-39fc-b246-ff4f91f1ddf4 | -6.7295 | -59.153 | 2025-08-01 03:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 98.7 |
| e6367bb5-7816-3c72-bd54-3b313fb4d962 | -6.7293 | -59.1916 | 2025-08-01 03:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 100.7 |
| c884a8f0-28ba-3c31-af14-f0383304a043 | -6.7294 | -59.1723 | 2025-08-01 03:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 324.8 |
| 10e1b1a8-e34b-3fe6-a6cf-2735fae361c7 | -23.5234 | -47.835 | 2025-08-01 03:20:00 | GOES-19 | ALAMBARI | SÃO PAULO | Brasil | 3500758 | 35 | 33 | nan | nan | nan | Mata Atlântica | 152.9 |
| a46c8554-b1c6-3497-9109-edf2eeded8e5 | -8.0321 | -43.1257 | 2025-08-01 03:20:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 159.7 |
| dbea71fa-4342-3828-be63-f6149f043489 | -6.6143 | -59.9848 | 2025-08-01 03:20:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 66.2 |
| 57f9ed24-fdb8-38a4-82d7-4d7c26579806 | -6.748 | -59.1523 | 2025-08-01 03:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 92.4 |
| 24f09789-d9bf-3c1a-9197-6c8375c0fe1d | -8.0513 | -43.1001 | 2025-08-01 03:20:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 104.1 |
| 86d40e66-1f90-3c09-8d24-15536e5c3b30 | -6.7478 | -59.1716 | 2025-08-01 03:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 169.7 |
| 1a9fc226-fc35-34f2-bf49-38db7fb7a579 | -3.50312 | -43.24029 | 2025-08-01 03:21:00 | NOAA-21 | ANAPURUS | MARANHÃO | Brasil | 2100808 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 19e0a81c-548e-3b51-913c-e97a6d01a16b | -3.51004 | -43.24142 | 2025-08-01 03:21:00 | NOAA-21 | ANAPURUS | MARANHÃO | Brasil | 2100808 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 4cd09445-7afb-36e7-9286-f542d7896201 | -3.50182 | -43.2472 | 2025-08-01 03:21:00 | NOAA-21 | ANAPURUS | MARANHÃO | Brasil | 2100808 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 30a8abe2-028b-3910-a5a4-b835e9eae24e | -3.50202 | -43.24664 | 2025-08-01 03:21:00 | NOAA-21 | ANAPURUS | MARANHÃO | Brasil | 2100808 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 1131feee-bde1-39e7-92f0-383e76ff9b11 | -3.50987 | -43.24197 | 2025-08-01 03:21:00 | NOAA-21 | ANAPURUS | MARANHÃO | Brasil | 2100808 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| f95163e4-4f89-3a6f-b598-2604cf140301 | -3.50295 | -43.24086 | 2025-08-01 03:21:00 | NOAA-21 | ANAPURUS | MARANHÃO | Brasil | 2100808 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 63635e45-c2ef-3395-9c21-1e5d89a56a5c | -8.04531 | -43.10772 | 2025-08-01 03:23:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 8.0 |
| f978a2fc-3411-3f43-be05-038c8d410612 | -8.04249 | -43.11386 | 2025-08-01 03:23:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 38.4 |
| 462f3450-55a3-338e-bd39-4816889c2825 | -8.51469 | -43.31578 | 2025-08-01 03:23:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 13.5 |
| 5d644572-3ee4-3663-a012-13541adf6061 | -8.51368 | -43.32112 | 2025-08-01 03:23:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 8.1 |
| 128a12ba-c1be-3674-8d94-d8a26b6e7168 | -8.05625 | -43.11097 | 2025-08-01 03:23:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 14.1 |
| 84990d64-1110-310d-ad73-33da276aeb54 | -9.65009 | -40.58298 | 2025-08-01 03:23:00 | NOAA-21 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 3.1 |
| 113d7dca-6dca-34c2-9ba5-e3598a947a06 | -8.0415 | -43.11919 | 2025-08-01 03:23:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 38.4 |
| 57fa72d0-52a0-33ea-a317-7212ffd97e6c | -8.03412 | -43.12332 | 2025-08-01 03:23:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 59.4 |
| daa6ff9a-443b-31c7-b478-733874a4187c | -8.04226 | -43.12355 | 2025-08-01 03:23:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 68.3 |
| 1a122891-0927-31c2-b49a-e747dc4e7610 | -8.04328 | -43.11825 | 2025-08-01 03:23:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 32.8 |
| 45d60321-f206-3194-8e4c-ac52e0e8c757 | -8.05911 | -43.10476 | 2025-08-01 03:23:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 11.3 |
| 2c0befbb-b471-386c-9ad6-f7459e5b47a0 | -8.04888 | -43.11506 | 2025-08-01 03:23:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 18.8 |
| 8d539cc8-4001-39fc-9340-d30cf355e4c7 | -8.04052 | -43.12449 | 2025-08-01 03:23:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 59.4 |
| abc5899b-7b8b-3fc2-a716-497c27ba196b | -9.5208 | -40.34499 | 2025-08-01 03:23:00 | NOAA-21 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 4.6 |
| 8fb702f6-3b79-3836-92a2-7c3d2c6256ab | -6.17508 | -35.2588 | 2025-08-01 03:23:00 | NOAA-21 | ARÊS | RIO GRANDE DO NORTE | Brasil | 2401206 | 24 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 9db2db5f-df13-39ab-afe8-9e830a5ae5c2 | -8.0443 | -43.11296 | 2025-08-01 03:23:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 32.8 |
| 720cc14c-d3d0-32d3-96e7-d6a05f015c86 | -8.03688 | -43.11711 | 2025-08-01 03:23:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 32.8 |
| 030f5c27-c0b5-318d-bff3-4644f70999c7 | -8.03586 | -43.12241 | 2025-08-01 03:23:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 68.3 |
| ea9f77b2-dd70-38db-b960-b0720ce9e868 | -8.05084 | -43.1045 | 2025-08-01 03:23:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 14.1 |
| 29e463d7-232c-358c-af0d-195ab2054ea8 | -7.59116 | -44.81049 | 2025-08-01 03:23:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| b884963f-b9c0-3487-ac05-cee759db3080 | -6.17882 | -35.25714 | 2025-08-01 03:23:00 | NOAA-21 | ARÊS | RIO GRANDE DO NORTE | Brasil | 2401206 | 24 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 30e0d220-1b65-3639-8ce2-dbe73c76da1f | -6.68939 | -43.07398 | 2025-08-01 03:23:00 | NOAA-21 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| f9acda95-7b3f-36b6-80ee-fc9e7b888d7d | -6.54352 | -43.61768 | 2025-08-01 03:23:00 | NOAA-21 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 9b770294-1e6b-3ac1-b99e-c0426838eec9 | -9.52604 | -40.34595 | 2025-08-01 03:23:00 | NOAA-21 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 2b0d1efc-b0ff-3c8b-8b11-80a3a26239e3 | -8.03313 | -43.12862 | 2025-08-01 03:23:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 59.4 |
| e11e2b56-f47c-3370-bdde-5142e1926b60 | -7.58766 | -44.80911 | 2025-08-01 03:23:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 1b506ca2-83de-3419-a3cd-5a8bd84c6d55 | -8.05723 | -43.10567 | 2025-08-01 03:23:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 14.1 |
| 80fa034c-4844-3233-a02f-f66c6943b08c | -7.58409 | -44.80902 | 2025-08-01 03:23:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 701f8849-2420-3d1c-97b8-085f813a9cdd | -8.03483 | -43.12769 | 2025-08-01 03:23:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 68.3 |
| 9f61373e-6e2d-3e97-8dc9-4e453fcd2ec4 | -6.17984 | -35.25438 | 2025-08-01 03:23:00 | NOAA-21 | ARÊS | RIO GRANDE DO NORTE | Brasil | 2401206 | 24 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 6936b786-3da0-3f01-b963-1c173ba7721c | -9.52021 | -40.34824 | 2025-08-01 03:23:00 | NOAA-21 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 4.6 |
| 3b021835-5097-3606-9573-415339a24b1c | -8.5157 | -43.31046 | 2025-08-01 03:23:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 13.5 |
| 2296c2a5-8dcf-36a3-868c-71af34f28b9d | -8.05069 | -43.11414 | 2025-08-01 03:23:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 16.4 |
| 0d14b120-cff2-3f06-9760-acc2bc107897 | -8.05271 | -43.10363 | 2025-08-01 03:23:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 11.3 |
| 2318cbfb-ea6b-3d05-9df4-ed944ed6f34e | -8.03511 | -43.11802 | 2025-08-01 03:23:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 38.4 |
| a86d9ff8-9f2a-3d29-80af-7e1a2ee3b755 | -8.04986 | -43.10978 | 2025-08-01 03:23:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 14.1 |
| 57574497-f3bf-3e3c-9107-9dce394664db | -8.05171 | -43.10886 | 2025-08-01 03:23:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 11.3 |
| 6d84a992-3d46-3bce-bbcc-ac59b0eee6ef | -9.35837 | -40.31526 | 2025-08-01 03:23:00 | NOAA-21 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 2dec9e52-0008-39dd-b655-1d9269f58a34 | -8.0581 | -43.11004 | 2025-08-01 03:23:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 11.3 |
| b44040a2-a7f7-3b9d-817c-8aaf34fea012 | -14.20615 | -42.84627 | 2025-08-01 03:25:00 | NOAA-21 | GUANAMBI | BAHIA | Brasil | 2911709 | 29 | 33 | nan | nan | nan | Caatinga | 0.7 |
| b526205c-48c7-34b5-b2e5-9017bc65c653 | -14.20695 | -42.8423 | 2025-08-01 03:25:00 | NOAA-21 | GUANAMBI | BAHIA | Brasil | 2911709 | 29 | 33 | nan | nan | nan | Caatinga | 0.7 |


[Clique aqui para ver as próximas entradas](README9.md)
