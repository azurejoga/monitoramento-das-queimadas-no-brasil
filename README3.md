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
| 5f9c5a5d-1ba8-3fa9-a6e1-e80477e24bca | -23.68588 | -51.67652 | 2025-07-21 03:36:00 | NOAA-21 | JANDAIA DO SUL | PARANÁ | Brasil | 4112108 | 41 | 33 | nan | nan | nan | Mata Atlântica | 6.1 |
| eb7faed5-677f-308f-9fb6-20058d90aeab | -23.68801 | -51.68066 | 2025-07-21 03:36:00 | NOAA-21 | JANDAIA DO SUL | PARANÁ | Brasil | 4112108 | 41 | 33 | nan | nan | nan | Mata Atlântica | 9.0 |
| 630f10bd-d296-3ee7-9178-1a819799aea0 | -23.68381 | -51.68448 | 2025-07-21 03:36:00 | NOAA-21 | JANDAIA DO SUL | PARANÁ | Brasil | 4112108 | 41 | 33 | nan | nan | nan | Mata Atlântica | 6.1 |
| 2ef8e634-84c9-3dd7-8057-e15c93334cd9 | -28.91 | -49.96494 | 2025-07-21 03:36:00 | NOAA-21 | CAMBARÁ DO SUL | RIO GRANDE DO SUL | Brasil | 4303608 | 43 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| 5b8e8099-d8ad-3fce-80bd-66a67e961d42 | -24.54992 | -50.7977 | 2025-07-21 03:36:00 | NOAA-21 | RESERVA | PARANÁ | Brasil | 4121703 | 41 | 33 | nan | nan | nan | Mata Atlântica | 4.4 |
| 20aff183-a474-39f4-9625-9f6c067d5806 | -7.2587 | -60.1897 | 2025-07-21 03:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 49.9 |
| e375ebb1-772f-3caa-afe6-7dca21a2f893 | -7.2957 | -60.169 | 2025-07-21 03:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 69.7 |
| 5ae4aeae-d350-3eaa-969f-facda71d1a96 | -7.2771 | -60.1889 | 2025-07-21 03:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 55.5 |
| 014154c1-ffa3-3477-a952-f2890b4c75b2 | -7.2772 | -60.1698 | 2025-07-21 03:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 123.9 |
| 0ff661dd-d1b3-30ed-a5fa-b142dfa6570b | -7.2402 | -60.1904 | 2025-07-21 03:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 65.4 |
| 226ea371-2e37-308b-968d-2d4e96c9f30d | -7.2957 | -60.169 | 2025-07-21 03:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 67.6 |
| 218ffce9-d6fe-32bb-991c-0f33ce718cd1 | -7.2402 | -60.1904 | 2025-07-21 03:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 75.6 |
| 3d759ac6-4f16-3f19-a817-41032d949a50 | -7.2771 | -60.1889 | 2025-07-21 03:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 45.9 |
| 3dbe8e2f-839e-3429-8d8d-d1bb536cb7cd | -7.2772 | -60.1698 | 2025-07-21 03:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 97.6 |
| 89708ffa-41f8-3f29-a65d-1eaae4d0b7dd | -6.7592 | -44.13232 | 2025-07-21 03:55:00 | NPP-375D | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 9757483d-8b55-38df-bbf4-05392be8dbf6 | -7.76036 | -42.15987 | 2025-07-21 03:55:00 | NPP-375D | SIMPLÍCIO MENDES | PIAUÍ | Brasil | 2210805 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 38298c31-b724-380c-bcbb-ac237e8a746e | -7.92646 | -43.95091 | 2025-07-21 03:55:00 | NPP-375D | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 901075b7-21d3-3117-bd42-5e4f11dd9a31 | -7.94604 | -43.97635 | 2025-07-21 03:55:00 | NPP-375D | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 7170d40e-0a04-3a7f-9bf1-118fd05e5c6d | -6.89022 | -45.39222 | 2025-07-21 03:55:00 | NPP-375D | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 15.5 |
| cf55ebe1-9be8-3919-8453-f16bbb371f1f | -5.27688 | -44.94947 | 2025-07-21 03:55:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| b37209db-74d9-34f1-9cc3-ffc074aa396f | -6.88675 | -42.7636 | 2025-07-21 03:55:00 | NPP-375D | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 88a59427-e8b8-34ae-a770-f1fd72a75aea | -5.8777 | -45.20036 | 2025-07-21 03:55:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 77c1ed62-1552-3591-a363-826ed1411e6f | -6.80251 | -42.98048 | 2025-07-21 03:55:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 4.6 |
| 568e078f-98d1-3ec5-941c-e35c749fbfc5 | -3.11683 | -47.01237 | 2025-07-21 03:55:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 6db5473d-5dd5-3735-b64c-794953c2fe64 | -7.75151 | -42.16743 | 2025-07-21 03:55:00 | NPP-375D | PAES LANDIM | PIAUÍ | Brasil | 2207306 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 483f791c-eda9-327f-8247-9e5b8e4d1ada | -6.57267 | -43.39456 | 2025-07-21 03:55:00 | NPP-375D | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Caatinga | 0.9 |
| bad85d8b-ffa2-365c-a105-008a6e3254b8 | -3.12908 | -47.0107 | 2025-07-21 03:55:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 5e0b6dbc-afdb-34fc-b666-eb5be147763a | -3.14002 | -47.01247 | 2025-07-21 03:55:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 0d98f96e-56fc-3919-9256-4724946e2b28 | -7.27098 | -44.27559 | 2025-07-21 03:55:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| a1dc2145-2c11-3525-b3ef-93178c0bde27 | -6.20716 | -44.30647 | 2025-07-21 03:55:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| e8a7e549-8bbe-36d6-9bdd-7a9171702dde | -8.51873 | -41.19665 | 2025-07-21 03:55:00 | NPP-375D | QUEIMADA NOVA | PIAUÍ | Brasil | 2208650 | 22 | 33 | nan | nan | nan | Caatinga | 6.9 |
| 83f5128e-df51-3074-b37b-c9ad976f6d7b | -3.12849 | -47.01418 | 2025-07-21 03:55:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 38d3e801-c566-36e2-a1e1-bd81d7ae5393 | -6.89835 | -45.48343 | 2025-07-21 03:55:00 | NPP-375D | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 64015cf9-305e-3a28-8bec-6e1765001ed3 | -7.75225 | -42.16301 | 2025-07-21 03:55:00 | NPP-375D | SIMPLÍCIO MENDES | PIAUÍ | Brasil | 2210805 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| d272480d-bd71-3767-85ae-cad773f5ad5c | -3.1121 | -47.01139 | 2025-07-21 03:55:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 09ac6cd4-6d0b-39a3-8f27-20660dde7e73 | -7.95905 | -43.97447 | 2025-07-21 03:55:00 | NPP-375D | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| ab090226-de03-37f6-ac58-c95644f6d484 | -7.27958 | -44.50865 | 2025-07-21 03:55:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| c7f9ee3b-9582-3b5a-9960-7b887282c646 | -6.49839 | -44.812 | 2025-07-21 03:55:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 01389ce0-c38d-34f2-a845-3e07352747cb | -7.13467 | -43.1946 | 2025-07-21 03:55:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 3.3 |
| 455908e1-4334-38f0-8b65-2154c083b25a | -6.20187 | -44.39061 | 2025-07-21 03:55:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 775c418b-603d-335a-a70d-53f4ea699780 | -5.87308 | -45.19963 | 2025-07-21 03:55:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| b41bea2e-485d-3745-af34-ece9b0329bd3 | -5.86223 | -45.20763 | 2025-07-21 03:55:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 5afaa054-d1e6-3dfc-946e-4e70d6d67e20 | -2.57226 | -42.7547 | 2025-07-21 03:55:00 | NPP-375D | BARREIRINHAS | MARANHÃO | Brasil | 2101707 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| e7fa227b-37dc-31ba-8353-d626589f28fe | -6.46831 | -43.49525 | 2025-07-21 03:55:00 | NPP-375D | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 109e4628-c250-3181-96ce-aa194a4a707f | -5.07077 | -37.71737 | 2025-07-21 03:55:00 | NPP-375D | BARAÚNA | RIO GRANDE DO NORTE | Brasil | 2401453 | 24 | 33 | nan | nan | nan | Caatinga | 0.7 |
| f18ad6a8-692f-34ad-920b-41071a970368 | -7.43913 | -44.27938 | 2025-07-21 03:55:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 30d8ff1e-d169-39f6-8e70-e81ed3c35999 | -5.23066 | -40.87778 | 2025-07-21 03:55:00 | NPP-375D | CRATEÚS | CEARÁ | Brasil | 2304103 | 23 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 33a213e6-aa6b-37d6-ae99-0b41a22f9949 | -5.86845 | -45.19891 | 2025-07-21 03:55:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 9c0b03f6-df00-30cf-b8dc-3e6eda798ed8 | -3.58836 | -47.52436 | 2025-07-21 03:55:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 1714d1cb-c2a3-39c3-8cfe-6a66407fb369 | -8.51937 | -41.19276 | 2025-07-21 03:55:00 | NPP-375D | QUEIMADA NOVA | PIAUÍ | Brasil | 2208650 | 22 | 33 | nan | nan | nan | Caatinga | 6.9 |
| 2c227b9b-c93e-3bb9-baba-52ff0636e8e2 | -3.03832 | -47.85717 | 2025-07-21 03:55:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| fdb80a12-1a23-3dbc-80b3-0a14c9d5349a | -6.57669 | -43.39533 | 2025-07-21 03:55:00 | NPP-375D | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 8beab553-c475-3769-b68e-3e5480351f16 | -7.56619 | -43.98952 | 2025-07-21 03:55:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 664a7f88-62d9-3def-bfb5-a173cf713698 | -3.1108 | -47.01492 | 2025-07-21 03:55:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 86193391-449a-3a98-9718-2e03f4d52131 | -6.89511 | -42.78497 | 2025-07-21 03:55:00 | NPP-375D | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 6e7fc5d3-a725-39d0-9f13-318649e066a4 | -3.58901 | -47.52056 | 2025-07-21 03:55:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 861d237c-6385-3719-9fd2-b8a0a2cfbd60 | -7.75594 | -42.16365 | 2025-07-21 03:55:00 | NPP-375D | SIMPLÍCIO MENDES | PIAUÍ | Brasil | 2210805 | 22 | 33 | nan | nan | nan | Caatinga | 6.0 |
| 1f7605da-8074-3d7e-a8a8-4376d2b0ca93 | -6.89898 | -42.78562 | 2025-07-21 03:55:00 | NPP-375D | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 3a8550ca-e3b0-3938-ac6c-523a34e02728 | -6.49969 | -44.81433 | 2025-07-21 03:55:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 74164844-0f6d-38ab-9146-e3e243155036 | -6.7816 | -47.1624 | 2025-07-21 03:55:00 | NPP-375D | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 002b23e3-0fc4-3f7c-bb86-d32a86a13e33 | -5.28254 | -44.94854 | 2025-07-21 03:55:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 45ed02a0-74ea-39c8-9ad3-27900bd49299 | -6.50548 | -43.51991 | 2025-07-21 03:55:00 | NPP-375D | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 74784f85-5369-3b4e-9750-e795532d8a65 | -7.96444 | -43.96774 | 2025-07-21 03:55:00 | NPP-375D | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c546ecca-a162-336e-a52b-d92e38735690 | -3.11137 | -47.01142 | 2025-07-21 03:55:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 101170e1-4d97-31f7-a289-d9cc96e71fd2 | -7.27166 | -44.27164 | 2025-07-21 03:55:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c159ef1b-517c-3801-a1d0-bbb905b71ad2 | -3.13455 | -47.01159 | 2025-07-21 03:55:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 9ca8b56b-6a03-3687-b173-6a2c12c3b20c | -5.26292 | -44.8688 | 2025-07-21 03:55:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 6b7d99c6-969d-315e-9dc6-a1f31d9a909d | -4.6656 | -41.9654 | 2025-07-21 03:55:00 | NPP-375D | COCAL DE TELHA | PIAUÍ | Brasil | 2202711 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| de496bdb-e0e4-3448-8d21-9bd468a8b836 | -3.04275 | -47.86625 | 2025-07-21 03:55:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 9790a93e-e737-3d13-8d73-b11b6d5c3934 | -7.43946 | -44.93862 | 2025-07-21 03:55:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 5776cdf3-729a-38d5-9633-cc05cd56dfaf | -5.8872 | -45.2182 | 2025-07-21 03:55:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 8.5 |
| bb58a644-4f91-3c6c-bb04-56d3722680fc | -5.88456 | -45.21616 | 2025-07-21 03:55:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 028d1bd3-8884-3d10-8868-95809d9aefde | -5.27797 | -44.94768 | 2025-07-21 03:55:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 46f9b13a-3abd-353a-881a-fd08fb153020 | -8.00797 | -43.69068 | 2025-07-21 03:55:00 | NPP-375D | ELISEU MARTINS | PIAUÍ | Brasil | 2203602 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 0441483d-f5a7-3702-8a0b-59b930001ea6 | -7.95969 | -43.97078 | 2025-07-21 03:55:00 | NPP-375D | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 5152fa0b-7586-31e1-832f-22565820db5b | -6.77056 | -43.80719 | 2025-07-21 03:55:00 | NPP-375D | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f5eca350-0fa9-3e94-9282-87d203dd335e | -3.04345 | -47.86209 | 2025-07-21 03:55:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| ebafdcb7-348d-3b16-8683-f835d7c35002 | -7.93888 | -43.94469 | 2025-07-21 03:55:00 | NPP-375D | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ef2adeca-bcf1-3b3c-be02-aa43e808f706 | -6.80254 | -42.97731 | 2025-07-21 03:55:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 4.9 |
| 55aba8ae-0770-341d-b4ae-ce1bc8e257d7 | -5.28146 | -44.95028 | 2025-07-21 03:55:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 03cc0694-eb3e-3804-9384-4b4937be032a | -5.28228 | -44.94552 | 2025-07-21 03:55:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 43492751-c454-3c70-ab0c-f1052f3b8e82 | -7.96381 | -43.97141 | 2025-07-21 03:55:00 | NPP-375D | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 11a7dd0f-9a06-33dd-8320-03586a2654ae | -3.11151 | -47.01488 | 2025-07-21 03:55:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f3eb7d76-d39a-3d8e-9ca5-29645d72b7bf | -3.13395 | -47.0151 | 2025-07-21 03:55:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| da08e7ed-8be2-33b8-9cf6-895ead5079b8 | -8.00333 | -43.69356 | 2025-07-21 03:55:00 | NPP-375D | ELISEU MARTINS | PIAUÍ | Brasil | 2203602 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 76682374-8953-3ef3-a21c-a5c75147cb39 | -3.1223 | -47.01331 | 2025-07-21 03:55:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 48b45e34-283c-3ff3-9b9d-11a7fbe01457 | -7.93121 | -43.94773 | 2025-07-21 03:55:00 | NPP-375D | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 844fc7e5-4008-37e4-a542-54aa2d1c2250 | -6.21152 | -44.30696 | 2025-07-21 03:55:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| a5113660-5121-340f-a0bc-d30418bd2784 | -7.57033 | -43.99024 | 2025-07-21 03:55:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 2e9ec9d1-d1a7-3358-95d1-a703d3beeca1 | -5.88257 | -45.21747 | 2025-07-21 03:55:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| e60f15f3-4d88-3bf1-b917-7a2949fa649c | -6.50198 | -43.5197 | 2025-07-21 03:55:00 | NPP-375D | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 970a646c-d82b-3473-b7ea-6575640f9430 | -3.03696 | -47.86533 | 2025-07-21 03:55:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| f6ebdbe4-bab6-3894-86f9-473bf515a667 | -7.25197 | -44.28466 | 2025-07-21 03:55:00 | NPP-375D | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 12b17b98-ac0f-3d7a-ad93-40ea8ff008e1 | -3.12303 | -47.01325 | 2025-07-21 03:55:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 120c0b6b-3f1b-3fec-8928-4cb46ce5f893 | -7.2591 | -44.29393 | 2025-07-21 03:55:00 | NPP-375D | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 5fcd1c8f-7499-3db3-b467-9b86fa72d586 | -5.2675 | -44.86943 | 2025-07-21 03:55:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 7a7d87ee-727d-3076-b710-ca92aa854950 | -7.06026 | -43.51154 | 2025-07-21 03:55:00 | NPP-375D | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 0a728d4c-25c8-3748-a142-c345602af059 | -5.86767 | -45.20355 | 2025-07-21 03:55:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| bc61b116-0f2a-3f29-910b-7ea7e8af363e | -7.07353 | -43.83062 | 2025-07-21 03:55:00 | NPP-375D | MARCOS PARENTE | PIAUÍ | Brasil | 2206001 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| dbc4f505-d881-30fc-97d1-dfece82be80e | -7.28027 | -44.50456 | 2025-07-21 03:55:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |


[Clique aqui para ver as próximas entradas](README4.md)
