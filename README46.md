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

## Dados Diários - Página 46

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 88a0376f-c55e-3328-afdb-8be2ff99d6ff | -3.23143 | -46.96155 | 2026-09-12 05:27:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 429f3d27-9045-38da-8858-40113261d4de | -3.8601 | -49.22392 | 2026-09-12 05:27:00 | NOAA-20 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| e073d10e-b7c8-3b08-8d79-47e192bc361b | -2.72062 | -57.60126 | 2026-09-12 05:27:00 | NOAA-20 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 9a9734b0-74b0-30bc-8c66-596b918c7ebe | -4.05334 | -56.33448 | 2026-09-12 05:27:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 82e1b540-f63a-3847-bdf1-0f913f552afa | -2.96984 | -50.41333 | 2026-09-12 05:27:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 37.7 |
| ad19b3d7-5a0f-37fc-87d0-26bfd5f03bf5 | -2.72858 | -57.64152 | 2026-09-12 05:27:00 | NOAA-20 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 4.6 |
| d6de7bc6-e044-3b98-a04d-847c53baae7b | -2.93894 | -50.3941 | 2026-09-12 05:27:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 30e1454a-4f97-35b8-b877-3c5994de3170 | -4.86346 | -55.99961 | 2026-09-12 05:27:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 5520a7a2-6153-3a3b-9e09-5b0195f51ec3 | -3.3839 | -50.76993 | 2026-09-12 05:27:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2c637b1b-f26b-3130-8506-19a705be1b25 | -5.36954 | -56.02078 | 2026-09-12 05:27:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| bd5fd943-fefc-3405-b3cb-eb0c7da58b09 | -2.9709 | -50.40622 | 2026-09-12 05:27:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 46.1 |
| bd23a626-9f51-3ff3-8f15-b2a94491c4fc | -2.93841 | -50.3977 | 2026-09-12 05:27:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 6768a843-46d0-3514-ba52-df0a91a91f43 | -3.36921 | -50.75736 | 2026-09-12 05:27:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 28459435-d6c4-35ce-a07e-ef432ab7588d | -3.23342 | -46.94834 | 2026-09-12 05:27:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 7.9 |
| 85d11051-ac8e-3bab-a8b3-e323479e3633 | -2.95155 | -50.3849 | 2026-09-12 05:27:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| da314040-0f71-3619-bf48-d4e2148be461 | -6.50702 | -47.60654 | 2026-09-12 05:27:00 | NOAA-20 | PALMEIRAS DO TOCANTINS | TOCANTINS | Brasil | 1713809 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 8ac051c8-c6ef-3513-82d8-e4768573fd7e | -1.72942 | -57.15546 | 2026-09-12 05:27:00 | NOAA-20 | FARO | PARÁ | Brasil | 1503002 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| bfbff208-8e81-3ca2-acea-7e71273727f8 | -2.96043 | -50.40099 | 2026-09-12 05:27:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 22.0 |
| 238cc115-1542-3506-98fb-8d36e2b04b34 | 1.23668 | -50.757 | 2026-09-12 05:27:00 | NOAA-20 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 87bd734a-8901-388c-bd17-8ff664465caa | -2.9615 | -50.3938 | 2026-09-12 05:27:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 8.7 |
| fdbfeb3e-7b6d-3cf0-a98a-1b6634dab98b | -2.95494 | -50.4001 | 2026-09-12 05:27:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 22.0 |
| 9025fe78-5a84-3e24-9358-0211a6c53678 | -3.81264 | -55.89181 | 2026-09-12 05:27:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3287d34e-81dd-37f5-b414-3238e22424c3 | -4.82629 | -55.77093 | 2026-09-12 05:27:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 881ce6e3-821b-3582-abfb-51074bcfd506 | -4.74254 | -55.89952 | 2026-09-12 05:27:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| bc281b31-0ed1-331e-a5c3-1b0978cce7fd | -3.54557 | -48.18064 | 2026-09-12 05:27:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 1a8ff791-5b37-306d-9810-f18fa03ef728 | -4.86815 | -56.02063 | 2026-09-12 05:27:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 00c65bfc-f885-3db0-9377-735e67278ec9 | -4.3033 | -49.11171 | 2026-09-12 05:27:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 2758c9e8-f78f-33f1-90d3-b8855c303d44 | -3.22503 | -46.96079 | 2026-09-12 05:27:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 7.8 |
| a4115edd-911e-34da-8907-f608fa231c5c | -3.37951 | -50.76234 | 2026-09-12 05:27:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| bb98d6c7-c6d9-30d3-b20e-5f88a22a7caf | -3.23284 | -46.9552 | 2026-09-12 05:27:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| ac31a525-2abf-37a2-b510-6df78743b015 | -4.36211 | -54.78258 | 2026-09-12 05:27:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 21af9813-864e-3086-99fa-7f99bfd74085 | -3.16185 | -48.61529 | 2026-09-12 05:27:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| aaa78c4d-a992-3513-9b4a-8a1525d6ed34 | 1.32557 | -60.71461 | 2026-09-12 05:27:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ef8bded5-e837-3990-9e54-4f99eb6441cc | -2.95049 | -50.39211 | 2026-09-12 05:27:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| d906720d-c03a-3341-9ca3-57579c766ccc | -2.73611 | -57.63878 | 2026-09-12 05:27:00 | NOAA-20 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 330ec5ba-b90e-3165-a870-03871bf41a48 | -5.78579 | -53.81369 | 2026-09-12 05:27:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d123fccd-dd98-3112-bbaa-952b14e5fa76 | -3.11169 | -61.47639 | 2026-09-12 05:27:00 | NOAA-20 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 0.5 |
| a07e9967-4c90-37b5-b976-0858768b4a45 | -2.89987 | -51.94147 | 2026-09-12 05:27:00 | NOAA-20 | VITÓRIA DO XINGU | PARÁ | Brasil | 1508357 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 83c00475-14e9-39b2-bdb3-410fe7610f85 | -2.94356 | -50.40054 | 2026-09-12 05:27:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 0cc71578-f77b-3808-87cb-12de0c751ab6 | -4.52646 | -54.95906 | 2026-09-12 05:27:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b8604bae-3f52-38dd-894f-67161355cdf7 | -2.94288 | -50.40557 | 2026-09-12 05:27:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 15.0 |
| cae8152a-e046-36a2-97c6-4aadd88c6b92 | -3.38543 | -50.75976 | 2026-09-12 05:27:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e7942133-7388-38c1-a610-bb264d6aa872 | -6.03928 | -52.21902 | 2026-09-12 05:27:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b71e7b6a-f9ee-39d1-88d9-d2a708462279 | -2.71707 | -57.62415 | 2026-09-12 05:27:00 | NOAA-20 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 6.6 |
| a7565412-9115-3e22-9561-90b3095a9751 | -5.80855 | -53.81686 | 2026-09-12 05:27:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 1a788a8f-a025-3ca6-9280-0b5736953e3a | -2.71597 | -57.60836 | 2026-09-12 05:27:00 | NOAA-20 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 424a11f4-4473-3066-aba0-388f48c13871 | -5.79877 | -53.82026 | 2026-09-12 05:27:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 785ab03e-57ca-3419-adc9-83b100efb4fb | -5.79034 | -53.81435 | 2026-09-12 05:27:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 7c524473-99f2-3d37-b73e-9b694c55aa23 | -4.86426 | -56.02018 | 2026-09-12 05:27:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 7ffd2a6a-bed7-3fb4-9ec3-45ab9038771c | -5.80534 | -53.80703 | 2026-09-12 05:27:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 851c777d-f92d-3f44-a6f3-a30423021412 | -4.51873 | -54.95438 | 2026-09-12 05:27:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 93e2e061-1c3b-3f47-84dc-37ddf4aaf4ac | -4.08154 | -56.30172 | 2026-09-12 05:27:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 1ecdcef2-86e7-3a10-9722-7c39ceceb584 | -2.89902 | -51.94014 | 2026-09-12 05:27:00 | NOAA-20 | VITÓRIA DO XINGU | PARÁ | Brasil | 1508357 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 8c973b10-c1f0-3e7f-a1d9-f44f0ece7890 | -3.36767 | -50.7676 | 2026-09-12 05:27:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 20ef62a5-1a75-3072-a94a-9fb291564f61 | -2.96258 | -50.38653 | 2026-09-12 05:27:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 16bb9c67-0188-3e24-8362-3bc1810ecc71 | -2.71478 | -57.61599 | 2026-09-12 05:27:00 | NOAA-20 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| e9a18ae8-512b-3d65-9821-cbcd5f23e69b | -3.38441 | -50.76653 | 2026-09-12 05:27:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| cf0f0123-534b-34e9-8168-aaffb85f6c41 | -3.76612 | -58.84726 | 2026-09-12 05:27:00 | NOAA-20 | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b0f701c4-203f-3b74-a6de-529a1a9403fd | -3.36869 | -50.76081 | 2026-09-12 05:27:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| bd55f750-8291-3e6d-914a-cd750798933b | -3.86299 | -49.21873 | 2026-09-12 05:27:00 | NOAA-20 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f08b8cdc-b1cf-3d64-ab4f-6afaf99f1173 | -6.50701 | -47.60619 | 2026-09-12 05:27:00 | NOAA-20 | PALMEIRAS DO TOCANTINS | TOCANTINS | Brasil | 1713809 | 17 | 33 | nan | nan | nan | Cerrado | 5.5 |
| ea7340dc-cbb0-370d-a7b2-4711ccb2e5f2 | -2.94235 | -50.40916 | 2026-09-12 05:27:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 28.3 |
| a998163d-8d10-3f45-be3a-24934d0a5592 | -2.95333 | -50.41093 | 2026-09-12 05:27:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 26.6 |
| 230b8ce6-8ee3-35e8-b76b-159d72dfb49d | -2.72917 | -57.63771 | 2026-09-12 05:27:00 | NOAA-20 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 34.6 |
| e8ebb5a3-591b-3b08-b27e-8addf8e3f53c | -2.96593 | -50.40184 | 2026-09-12 05:27:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 26.0 |
| 98f4c5cb-0cda-396a-aa15-3f63dcab8c88 | -1.77775 | -54.94489 | 2026-09-12 05:27:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 811e403e-2f1d-3077-877c-2cffecc15a27 | -4.30352 | -49.11499 | 2026-09-12 05:27:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 824cff79-c75b-3112-a7ef-a7c06df09e01 | -3.53843 | -48.18475 | 2026-09-12 05:27:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 76523b91-649e-38d2-b943-4f3e4b50f9c1 | -2.94246 | -50.40765 | 2026-09-12 05:27:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 8.5 |
| 6c0e1364-e274-3f2e-bd3c-69d23c66c3f1 | -3.16257 | -48.61052 | 2026-09-12 05:27:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| f5d53e12-7de2-3b03-a30a-70300e9ed5c3 | -2.83424 | -57.63801 | 2026-09-12 05:27:00 | NOAA-20 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 07940b8f-b94a-3cea-9729-0d8065488a88 | -2.94891 | -50.40282 | 2026-09-12 05:27:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 15.0 |
| e01d063c-4ce1-3daf-b29a-118b91a297f5 | -2.7263 | -57.63338 | 2026-09-12 05:27:00 | NOAA-20 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 4cb117d6-6f91-3b36-a381-5d3bead5c5cb | -1.77299 | -54.94935 | 2026-09-12 05:27:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| cfad51d1-b323-34d3-95d0-e2c8c4855d86 | -4.36394 | -47.78671 | 2026-09-12 05:27:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 0e86f1b3-083d-360d-a6c2-bd8ccf12a4d4 | -5.8249 | -53.80043 | 2026-09-12 05:27:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 3a90b6c3-4977-3ae3-a199-890672ef3bfc | -3.2474 | -50.81927 | 2026-09-12 05:27:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 378d75e5-43f2-33d5-81be-3fbebdca247c | -5.74031 | -53.48039 | 2026-09-12 05:27:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| eea0c06f-ac8b-372d-ba6f-91e87d082c96 | -3.38053 | -50.75558 | 2026-09-12 05:27:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| b8d489bf-ff59-3e80-b99e-c7b71dcf824b | -3.34046 | -53.27151 | 2026-09-12 05:27:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| cca46227-fba2-316c-8492-769db624a61e | -5.79944 | -53.81562 | 2026-09-12 05:27:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 73f5645b-376b-3d65-834f-03cc44eafe46 | -2.71825 | -57.61652 | 2026-09-12 05:27:00 | NOAA-20 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 5.3 |
| d69467fb-102e-3808-a682-8041731cc8f1 | -2.9419 | -50.41121 | 2026-09-12 05:27:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| a05c896d-4a49-3e12-ba61-1f3b454e58c7 | -2.73492 | -57.64639 | 2026-09-12 05:27:00 | NOAA-20 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 01408454-7b33-3825-923a-92da63df283f | -2.96327 | -50.41973 | 2026-09-12 05:27:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 7.3 |
| 0cabe506-62f5-3754-80ae-e281db97a123 | -2.9599 | -50.40457 | 2026-09-12 05:27:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 25.3 |
| e6113e36-5dc6-33d6-935e-a368a0556a84 | -4.52593 | -54.96267 | 2026-09-12 05:27:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f1ed0bd9-b0b3-37e9-996e-45ddf9e34411 | -4.35911 | -54.77418 | 2026-09-12 05:27:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 9c97bada-9aae-3e8d-b0bd-64fbd97162ad | -2.71877 | -57.63611 | 2026-09-12 05:27:00 | NOAA-20 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 41028af1-ef63-339c-8fa7-7cfda78028e2 | -4.86268 | -56.00468 | 2026-09-12 05:27:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f22ccbcc-8d96-31c9-8bbb-8b9ae24c4efb | -2.71537 | -57.61217 | 2026-09-12 05:27:00 | NOAA-20 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5c2475b9-b7a6-3dd9-8a25-28a9400721e6 | -6.50103 | -47.59856 | 2026-09-12 05:27:00 | NOAA-20 | PALMEIRAS DO TOCANTINS | TOCANTINS | Brasil | 1713809 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| bd095b04-6965-3a2a-922b-62eff3297a16 | -2.82016 | -51.34233 | 2026-09-12 05:27:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| defeb12c-febd-312b-8218-80b2ba9c2fbf | -4.45487 | -55.44059 | 2026-09-12 05:27:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f1deb414-87e4-33e9-813d-8acf9d8d5a46 | -3.40294 | -59.23402 | 2026-09-12 05:27:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 26edff3b-4a96-32ae-9b5a-cfe7fa14f918 | 1.22641 | -50.72585 | 2026-09-12 05:27:00 | NOAA-20 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 098e53f9-b75b-3201-86b6-fcd995926b84 | -2.94785 | -50.41 | 2026-09-12 05:27:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 28.3 |
| baaa57ab-abd4-3d4d-89c3-148c9d2dca5d | -2.97144 | -50.40266 | 2026-09-12 05:27:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 26.0 |
| 75a16ebc-b1b1-3d74-bd04-870d9cf14f7e | -3.22654 | -46.94751 | 2026-09-12 05:27:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 7.9 |
| 1aff8653-4fcb-3202-aec1-8857466480fd | -2.47087 | -48.03988 | 2026-09-12 05:27:00 | NOAA-20 | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |


[Clique aqui para ver as próximas entradas](README47.md)
