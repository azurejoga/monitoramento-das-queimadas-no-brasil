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

## Dados Diários - Página 23

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| ff4a86d3-a5b1-3cfa-8dae-5dac02ac1027 | -5.15086 | -38.05555 | 2025-08-26 03:04:00 | NOAA-20 | LIMOEIRO DO NORTE | CEARÁ | Brasil | 2307601 | 23 | 33 | nan | nan | nan | Caatinga | 4.0 |
| 848ee8fb-25e2-3e57-b274-742a20d1d4bb | -6.56951 | -35.22232 | 2025-08-26 03:04:00 | NOAA-20 | JACARAÚ | PARAÍBA | Brasil | 2507309 | 25 | 33 | nan | nan | nan | Mata Atlântica | 2.6 |
| 6f1daa97-ca89-3538-b867-8eafc5fe3858 | -4.87877 | -37.48549 | 2025-08-26 03:04:00 | NOAA-20 | ARACATI | CEARÁ | Brasil | 2301109 | 23 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 2dd8c10b-63c6-392e-bc16-20f695d6e442 | -9.16516 | -40.60614 | 2025-08-26 03:04:00 | NOAA-20 | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 5.9 |
| f3027880-f0d2-3840-8545-5ed33587bc6e | -6.56888 | -35.22582 | 2025-08-26 03:04:00 | NOAA-20 | JACARAÚ | PARAÍBA | Brasil | 2507309 | 25 | 33 | nan | nan | nan | Mata Atlântica | 2.7 |
| 23bd5198-884c-32e1-b16b-8c7f3655d015 | -5.50935 | -36.67559 | 2025-08-26 03:04:00 | NOAA-20 | AFONSO BEZERRA | RIO GRANDE DO NORTE | Brasil | 2400307 | 24 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 9f646162-7dcd-3708-b1d0-82edfc9b5bd9 | -9.16664 | -40.59874 | 2025-08-26 03:04:00 | NOAA-20 | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 5.9 |
| 36ced523-6184-344d-a7bf-9a80ebfce2fa | -9.16701 | -40.60801 | 2025-08-26 03:04:00 | NOAA-20 | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 8.6 |
| 1bbef52a-8209-3dc7-baf4-9ca2a561b764 | -9.16856 | -40.60049 | 2025-08-26 03:04:00 | NOAA-20 | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 7.2 |
| a89949d8-bddf-3188-a00e-ffcdb5d10e27 | -22.259 | -42.51038 | 2025-08-26 03:08:00 | NOAA-20 | NOVA FRIBURGO | RIO DE JANEIRO | Brasil | 3303401 | 33 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| 2e601b05-ba9b-3764-9b36-b87f7bff141b | -22.25776 | -42.50881 | 2025-08-26 03:08:00 | NOAA-20 | NOVA FRIBURGO | RIO DE JANEIRO | Brasil | 3303401 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| e7d17f02-ebdf-3e4d-9fbb-005a3a3e862b | -20.45344 | -43.88047 | 2025-08-26 03:08:00 | NOAA-20 | CONGONHAS | MINAS GERAIS | Brasil | 3118007 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| b1ca64c7-467f-39c0-8ca3-4b29b924c236 | -22.25637 | -42.51462 | 2025-08-26 03:08:00 | NOAA-20 | NOVA FRIBURGO | RIO DE JANEIRO | Brasil | 3303401 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 0cd8fc8b-b96f-3412-abf3-17576cd49b73 | -20.72592 | -40.66266 | 2025-08-26 03:08:00 | NOAA-20 | ANCHIETA | ESPÍRITO SANTO | Brasil | 3200409 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 6467fbef-af41-3fbb-8c61-b1be081622d3 | -20.45511 | -43.87378 | 2025-08-26 03:08:00 | NOAA-20 | CONGONHAS | MINAS GERAIS | Brasil | 3118007 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 3267b3da-9449-3a63-a26e-31230b79b7f4 | -7.3854 | -64.3475 | 2025-08-26 03:10:00 | GOES-19 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 80.9 |
| f02c6e31-974c-3ff7-bf3d-5ee0ec1d9e66 | -4.9605 | -55.8226 | 2025-08-26 03:10:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 64.5 |
| 2302921c-9940-3c3e-ab5f-3ecb163d67a9 | -6.8228 | -58.9753 | 2025-08-26 03:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 154.9 |
| 40d20546-8f2b-3549-aaf6-09f972e89157 | -6.2275 | -60.018 | 2025-08-26 03:10:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 54.6 |
| 1c7b6c53-f2f4-33f1-8066-72f9836addb6 | -8.9873 | -65.4379 | 2025-08-26 03:10:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 39.2 |
| a3333f05-e34f-3857-bf6c-6d2f26bff2a5 | -11.5587 | -52.138 | 2025-08-26 03:10:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 55.9 |
| 8424c65c-b381-30c9-abca-c87defed3901 | -11.3126 | -55.1112 | 2025-08-26 03:10:00 | GOES-19 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 50.0 |
| 1c9fd48e-c921-301d-9bb0-b4fb558122b3 | -6.8229 | -58.956 | 2025-08-26 03:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 129.2 |
| 32cf31ce-93da-3193-9ede-306c2dadc768 | -8.8548 | -62.4503 | 2025-08-26 03:10:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 265.8 |
| 5353fb61-de35-33ee-a610-559b155c95f9 | -8.8734 | -62.4495 | 2025-08-26 03:10:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 83.8 |
| eb646768-f794-354d-9dfe-f783134f053c | -4.9606 | -55.8028 | 2025-08-26 03:10:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 50.1 |
| 974fd025-cdce-320c-a491-9098cc732988 | -14.2876 | -49.1291 | 2025-08-26 03:10:00 | GOES-19 | CAMPINORTE | GOIÁS | Brasil | 5204706 | 52 | 33 | nan | nan | nan | Cerrado | 60.9 |
| 8579f2b5-cbbf-3970-a82f-af34435a22b0 | -11.54 | -52.119 | 2025-08-26 03:10:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 75.5 |
| 2bbd900c-b9ea-33e0-8a13-0b6f9db390ad | -7.3854 | -64.3662 | 2025-08-26 03:10:00 | GOES-19 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 49.7 |
| fb00b78f-6cd5-3089-81a3-fbaa384767d1 | -8.9874 | -65.4192 | 2025-08-26 03:10:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 39.3 |
| ca82ec17-f2c9-3b41-a7bc-f05940428aa9 | -6.7819 | -59.6711 | 2025-08-26 03:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 41.7 |
| 1d7d26f2-5aba-3bcd-bae7-618c881c7629 | -11.5397 | -52.14 | 2025-08-26 03:10:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 59.8 |
| 6c4a64cc-4ff2-3b5d-86d8-c4f431fc462b | -9.006 | -65.4 | 2025-08-26 03:10:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 28.0 |
| fca5a2d2-ca20-3e7a-8e39-0299072a7035 | -11.5779 | -52.115 | 2025-08-26 03:10:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 64.9 |
| f77c17e6-5792-34f8-bc5b-66d9423ca34a | -6.2459 | -60.0174 | 2025-08-26 03:10:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 88.6 |
| 72f51da3-62f2-372c-abce-187886892e47 | -6.8413 | -58.9552 | 2025-08-26 03:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 50.3 |
| 1dbb848f-396c-3ab6-91f8-7c6d6ad7836a | -9.1722 | -59.4629 | 2025-08-26 03:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 80.5 |
| e672f10a-14e5-3f48-9cee-ca846bb49738 | -8.855 | -62.4313 | 2025-08-26 03:10:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 130.6 |
| 3ec14595-77e6-35a5-b19c-10f6b2040438 | -20.9577 | -49.0515 | 2025-08-26 03:10:00 | GOES-19 | TABAPUÃ | SÃO PAULO | Brasil | 3552601 | 35 | 33 | nan | nan | nan | Mata Atlântica | 85.6 |
| 60e448ec-0bd6-3a6e-8a5e-bb2feef30bb4 | -9.1909 | -59.4619 | 2025-08-26 03:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 52.2 |
| de39d00b-af8c-3db3-8c00-704c6480add1 | -9.1724 | -59.4436 | 2025-08-26 03:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 54.3 |
| c5a75bf1-1be8-39b1-9297-742c1477477a | -6.8412 | -58.9746 | 2025-08-26 03:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 44.1 |
| 7e990b15-7fc7-3bd9-aa8f-30ba18fb206f | -11.559 | -52.117 | 2025-08-26 03:10:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 93.0 |
| 68cf77d8-e702-3626-a70d-693c3cf5bedc | -8.8364 | -62.4321 | 2025-08-26 03:10:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 96.6 |
| 15796924-fcaa-34e7-b8c5-fa4835d90c9f | -6.7635 | -59.6718 | 2025-08-26 03:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 65.7 |
| 6d0d9208-f02e-34db-a642-7d607d284830 | -6.8043 | -58.9761 | 2025-08-26 03:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 68.5 |
| f0346697-3bf2-36fe-9bcb-2b237470cdfd | -8.8363 | -62.451 | 2025-08-26 03:10:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 182.6 |
| e0fa7cd4-feb6-385f-af1c-602af6b8cb3b | -6.8044 | -58.9568 | 2025-08-26 03:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 53.2 |
| 659d760b-e920-3c5a-8ca1-dde0792731c4 | -14.2682 | -49.132 | 2025-08-26 03:10:00 | GOES-19 | CAMPINORTE | GOIÁS | Brasil | 5204706 | 52 | 33 | nan | nan | nan | Cerrado | 77.5 |
| b8f4b879-9d17-3f52-afe1-92087bfdb6c6 | -8.8548 | -62.4503 | 2025-08-26 03:20:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 286.3 |
| cdcc7a77-0ebb-34b7-912c-06666c880a21 | -8.855 | -62.4313 | 2025-08-26 03:20:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 183.2 |
| 22744837-c062-3328-8f74-37026e98702c | -11.5397 | -52.14 | 2025-08-26 03:20:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 52.5 |
| 0f92f32f-34dd-3519-bed5-fb6f0bec732e | -14.8508 | -47.161 | 2025-08-26 03:20:00 | GOES-19 | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 95.6 |
| 484730f2-860d-3fb6-ac11-147d9c235b3e | -7.3854 | -64.3662 | 2025-08-26 03:20:00 | GOES-19 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 45.5 |
| 114f4f7e-8367-3d6e-9418-f1101d425bac | -6.246 | -59.9982 | 2025-08-26 03:20:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 41.0 |
| d249b233-008e-3d3c-a196-ecd182fec698 | -9.191 | -59.4425 | 2025-08-26 03:20:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 51.1 |
| ee8542c4-c704-3e35-9a3a-354ce36ef33a | -11.559 | -52.117 | 2025-08-26 03:20:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 91.5 |
| dc766787-a449-3f84-83c7-d991df1e664a | -6.7635 | -59.6718 | 2025-08-26 03:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 75.0 |
| b37c9790-257d-3f6b-b4e0-737fd0f31009 | -6.2275 | -60.018 | 2025-08-26 03:20:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 52.9 |
| b3e4df02-2657-3959-86f6-28ef02ca9314 | -6.6961 | -58.5546 | 2025-08-26 03:20:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 32.0 |
| 6963bb39-4bc7-38c0-858a-e6682057286e | -11.5207 | -52.142 | 2025-08-26 03:20:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 43.5 |
| 4f982e4a-c62e-33ff-9e3e-33235547b111 | -6.7144 | -58.5732 | 2025-08-26 03:20:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 23.4 |
| de4a5d72-4824-3c55-abf6-d9f3cd815400 | -6.8044 | -58.9568 | 2025-08-26 03:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 39.9 |
| 2df1babc-5ebe-32ce-8371-77ba40ea67e6 | -9.1715 | -59.5599 | 2025-08-26 03:20:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 60.3 |
| 63773a36-eb33-3abd-a3be-3412245e8a31 | -6.8043 | -58.9761 | 2025-08-26 03:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 36.6 |
| 442f9d39-1c81-3ddd-b8ea-c45621418b16 | -8.8364 | -62.4321 | 2025-08-26 03:20:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 104.0 |
| c26ba314-8732-3ac9-bb16-c16e2566bd1a | -6.8229 | -58.956 | 2025-08-26 03:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 134.6 |
| d60c70ee-e254-3d01-9c68-266d1a78361a | -9.1718 | -59.5211 | 2025-08-26 03:20:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 78.5 |
| f7e093e0-732b-3cb9-aacc-89e8f880d9dc | -14.8317 | -47.1415 | 2025-08-26 03:20:00 | GOES-19 | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 58.6 |
| eac7f440-d8b7-3f3c-a053-0cc3b6e4a7aa | -6.2459 | -60.0174 | 2025-08-26 03:20:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 81.8 |
| 55f59177-1624-385f-b757-f11730778cb3 | -6.8413 | -58.9552 | 2025-08-26 03:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 47.1 |
| 13c6e74b-f14c-3878-9aa1-be9d76566e46 | -8.8363 | -62.451 | 2025-08-26 03:20:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 153.4 |
| 78096fe1-850e-3966-95d0-16a5462c57d7 | -9.1909 | -59.4619 | 2025-08-26 03:20:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 58.5 |
| 05a5e8f6-33f8-3d83-8602-9de7d5d4908e | -8.9874 | -65.4192 | 2025-08-26 03:20:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 36.7 |
| 58b2bb73-253a-3277-ae9a-76870ed8df3e | -6.7145 | -58.5539 | 2025-08-26 03:20:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 21.7 |
| 8d87050a-0be9-3da4-9356-40f0bf5514ef | -6.8228 | -58.9753 | 2025-08-26 03:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 136.5 |
| dcb4a5f2-5c13-31ef-978b-8fb640635306 | -9.153 | -59.5415 | 2025-08-26 03:20:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 54.1 |
| d9957df1-c013-301c-9d21-50408b29ac4b | -9.1903 | -59.5395 | 2025-08-26 03:20:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 58.5 |
| 1cc1edb4-3a37-3e7d-99a0-f7cd906222db | -6.7819 | -59.6711 | 2025-08-26 03:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 53.6 |
| 0119fbb1-69e9-3c08-9962-e1a39ee50305 | -9.1717 | -59.5405 | 2025-08-26 03:20:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 114.4 |
| 7e23272f-7654-327a-9919-1381356c3d44 | -9.1722 | -59.4629 | 2025-08-26 03:20:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 66.7 |
| bdc404b3-0466-3a94-be4a-a3d10f2029f6 | -7.3854 | -64.3475 | 2025-08-26 03:20:00 | GOES-19 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 69.6 |
| 12f35bed-3798-368d-b6f1-6c068a75317d | -4.9605 | -55.8226 | 2025-08-26 03:20:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 72.5 |
| a9bfbdac-8fde-3386-a6e2-5049e27fb35d | -20.9577 | -49.0515 | 2025-08-26 03:20:00 | GOES-19 | TABAPUÃ | SÃO PAULO | Brasil | 3552601 | 35 | 33 | nan | nan | nan | Mata Atlântica | 87.1 |
| 0b186078-8b8d-3339-8321-d3182b498c59 | -19.1824 | -48.7259 | 2025-08-26 03:20:00 | GOES-19 | PRATA | MINAS GERAIS | Brasil | 3152808 | 31 | 33 | nan | nan | nan | Cerrado | 81.1 |
| 4e7d2ffe-3b42-33e3-aabf-e647fd89b0ba | -8.9873 | -65.4379 | 2025-08-26 03:20:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 31.3 |
| a3c2744d-4365-3f5f-b7df-553f6192fbd6 | -9.1904 | -59.5201 | 2025-08-26 03:20:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 60.8 |
| 94a46743-853d-3cdb-b3b4-b30b767e28c0 | -9.006 | -65.4 | 2025-08-26 03:20:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 28.8 |
| b703383e-c634-306c-ab97-bbfbb0eff296 | -14.8512 | -47.1382 | 2025-08-26 03:20:00 | GOES-19 | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 124.4 |
| ba621c2c-d301-3876-9e77-8b38c0265928 | -8.8734 | -62.4495 | 2025-08-26 03:20:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 81.2 |
| e2615300-ad5d-3f86-a895-e3dbb433bc93 | -11.54 | -52.119 | 2025-08-26 03:20:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 74.2 |
| 45905440-024b-3742-ab6c-36002210bbcf | -6.2275 | -60.018 | 2025-08-26 03:30:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 57.0 |
| 43d166bd-cb80-387a-ab5d-c7207563fa67 | -6.8229 | -58.956 | 2025-08-26 03:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 149.5 |
| 0acae3ea-0e9a-3411-a770-74572b7c26c2 | -9.006 | -65.4 | 2025-08-26 03:30:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 28.9 |
| 59510c7c-21d0-3576-b6a0-b19dd804d081 | -6.8228 | -58.9753 | 2025-08-26 03:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 153.8 |
| 2d56a710-bcdd-3019-a271-bc8c442b6a4b | -6.2276 | -59.9989 | 2025-08-26 03:30:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 41.4 |
| 570b2705-279e-3d60-bb9b-7cb83f72f4d8 | -6.8043 | -58.9761 | 2025-08-26 03:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 62.1 |
| b29b9c13-8554-3c18-b6f3-4854dfaba45b | -11.559 | -52.117 | 2025-08-26 03:30:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 73.5 |
| e937a7fc-3989-3df2-a899-05a5a3698181 | -4.9605 | -55.8226 | 2025-08-26 03:30:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 70.9 |
| 11153d6c-eb13-3491-93a7-fb8f474f98eb | -6.7635 | -59.6718 | 2025-08-26 03:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 86.3 |


[Clique aqui para ver as próximas entradas](README24.md)
