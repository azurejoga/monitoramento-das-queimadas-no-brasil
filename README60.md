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

## Dados Diários - Página 60

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 65553788-ef60-3ad4-ba35-267f42618785 | -8.27321 | -54.92821 | 2026-09-01 05:16:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 7.4 |
| 6e3567ec-90c9-342b-9c92-6c1f14cb8192 | -4.84612 | -55.82996 | 2026-09-01 05:16:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 732759de-85b9-3400-b8bd-8a942d565217 | -5.24749 | -55.90018 | 2026-09-01 05:16:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 76362285-1672-39b6-9a44-6876b1030af4 | -5.34464 | -45.16405 | 2026-09-01 05:16:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| e4bbd739-ef8b-3b64-be8b-4d370f09e1a2 | -11.31736 | -45.20246 | 2026-09-01 05:16:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| a29a8e6c-a458-3874-a0e8-8e5425e4e0b0 | -10.43746 | -46.52701 | 2026-09-01 05:16:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| cf48489e-23e4-361d-ada6-bdf4d6341084 | -3.60753 | -59.06921 | 2026-09-01 05:16:00 | NPP-375D | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 17e4be17-f434-38f1-ad24-6edde4eb5855 | -9.42161 | -56.97556 | 2026-09-01 05:16:00 | NPP-375D | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 87519ee5-be01-344a-ad75-9b429f47a09b | -8.4944 | -44.75111 | 2026-09-01 05:16:00 | NPP-375D | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| a431d464-a5e1-3099-820c-f2e218567953 | -5.96449 | -57.67527 | 2026-09-01 05:16:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 3c9c7e01-00cf-34de-82a7-597727b78438 | -4.95874 | -55.84399 | 2026-09-01 05:16:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 49f91aa5-06ce-3c64-b17e-bc92f6ef6414 | -5.98303 | -53.61088 | 2026-09-01 05:16:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4a1cb8e3-2484-35d7-ab47-a408ce93a630 | -9.17251 | -59.63546 | 2026-09-01 05:16:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c3c0f8d2-e020-3841-97d3-c20e1cf01afa | -10.72748 | -47.95658 | 2026-09-01 05:16:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 489fba0a-bf2b-3a73-862c-235c3cca1236 | -8.156 | -55.37088 | 2026-09-01 05:16:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c25ebc7e-04f6-3674-a492-c8994689174b | -8.41928 | -44.99227 | 2026-09-01 05:16:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| f23e9f37-718a-3613-991f-83fe552b8508 | -8.27657 | -54.92884 | 2026-09-01 05:16:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 7.4 |
| 0bb68402-d8df-32e7-840a-09c696d007b4 | -8.55998 | -54.78934 | 2026-09-01 05:16:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 75befcd6-104d-35ba-b5e0-83e4db321de0 | -7.18167 | -55.48073 | 2026-09-01 05:16:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c9a3314e-3212-344c-bd21-10212363850e | -7.35575 | -60.59276 | 2026-09-01 05:16:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 2c587268-b2fc-3dee-8a2a-dda3b453bb15 | -5.96046 | -57.67841 | 2026-09-01 05:16:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 7bae8d08-fe1b-34e6-aad6-8c3aeeb2dbf5 | -10.03727 | -44.69531 | 2026-09-01 05:16:00 | NPP-375D | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 3b15c048-08e4-386e-9629-1003191ff013 | -5.85471 | -57.55547 | 2026-09-01 05:16:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 11.9 |
| 7250cf27-6d45-3951-8c96-55aada50a150 | -5.87249 | -57.77232 | 2026-09-01 05:16:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 5433fc50-61da-3807-8c7e-000e3c2425cb | -9.1719 | -59.61109 | 2026-09-01 05:16:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 9ad90203-ae21-3c1b-8ca1-8ccdf38df05f | -7.62651 | -55.29524 | 2026-09-01 05:16:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 9c04b753-a0db-3255-ac40-72b64b889b93 | -11.48242 | -45.09715 | 2026-09-01 05:16:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 619eaab9-a548-3901-aa12-e36857a0f67a | -6.78219 | -55.67529 | 2026-09-01 05:16:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d4501764-9a2d-31d5-af07-aac9ee6c1613 | -6.37921 | -51.7638 | 2026-09-01 05:16:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 338c526e-8473-3218-907f-31af56153e28 | -4.97203 | -55.8461 | 2026-09-01 05:16:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 9bd90233-e30f-3eb3-bbd8-0c05d0ce6450 | -6.12248 | -57.67432 | 2026-09-01 05:16:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 97a50490-9de7-31e9-829a-cd79fd507b78 | -8.78119 | -62.5022 | 2026-09-01 05:16:00 | NPP-375D | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 1968fe23-9fe1-3ae8-9164-a39a64bdb831 | -10.1532 | -45.68819 | 2026-09-01 05:16:00 | NPP-375D | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 4036868e-5078-344f-8774-195d217a3e85 | -8.46428 | -57.6473 | 2026-09-01 05:16:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 8535ca13-208c-39a8-a878-8b2153dccda8 | -8.41432 | -44.99499 | 2026-09-01 05:16:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 45211664-ef64-35e9-8489-709e4787a420 | -6.92746 | -55.63384 | 2026-09-01 05:16:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f8d4bf49-56e0-3eef-a0cc-4b684ab22ef1 | -6.12487 | -57.69678 | 2026-09-01 05:16:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 0c0e0a81-20cb-3968-a6fd-caab80fd574a | -8.13417 | -54.96939 | 2026-09-01 05:16:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 16e4a005-7cbd-3b06-afed-be539ed55bc2 | -9.43234 | -45.63058 | 2026-09-01 05:16:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| b0fa9d56-05f8-34f1-9cb4-cee603b22327 | -6.6008 | -58.60296 | 2026-09-01 05:16:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 3.7 |
| f4e445e0-0b59-3c2b-809a-db252f29f57a | -3.6278 | -60.56301 | 2026-09-01 05:16:00 | NPP-375D | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 7f9d3f18-3577-3b95-96bf-ca66a022feb6 | -5.88931 | -57.75565 | 2026-09-01 05:16:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 5d1bc33d-6229-3469-9b8e-c97f34393a00 | -5.48108 | -57.14393 | 2026-09-01 05:16:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 7bfbb775-cb0a-3935-bb8a-5b665b4cb7d4 | -6.64976 | -53.18888 | 2026-09-01 05:16:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 84326fcc-1033-3b56-b36a-b0a86483f2e1 | -8.93624 | -62.3648 | 2026-09-01 05:16:00 | NPP-375D | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f5a6aff5-772f-3d36-b123-256e72126ad0 | -7.27248 | -46.80484 | 2026-09-01 05:16:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| d39cab9f-5c8a-3925-bfd8-3bf1f3837ed6 | -5.59289 | -60.23144 | 2026-09-01 05:16:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 1a13bb31-2ac5-322a-b6fc-f1095ecce2f5 | -7.5829 | -60.48038 | 2026-09-01 05:16:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 52.4 |
| 99727cf0-8c28-3052-b645-1e4f7a632449 | -4.75972 | -50.66813 | 2026-09-01 05:16:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 7221c9e4-77af-32b5-bd5e-6d8b6b9adc4a | -8.59452 | -54.72332 | 2026-09-01 05:16:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c2b29875-de93-37f4-82ce-3a97f9a99d99 | -7.28407 | -49.82447 | 2026-09-01 05:16:00 | NPP-375D | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 4632ec15-5701-39f7-ae1b-2847605ad3b4 | -6.92914 | -55.6448 | 2026-09-01 05:16:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a1989f8f-8d5b-38a0-bc9b-b2c956a7d9a6 | -6.78551 | -55.67582 | 2026-09-01 05:16:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 5501e404-841f-3b2c-a9f5-f1e9e858898f | -11.32948 | -45.15528 | 2026-09-01 05:16:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 137d25c5-384e-3369-8b9a-63b8900ea915 | -3.50927 | -56.31996 | 2026-09-01 05:16:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3f91cfc2-6f2d-33b4-8029-524cc806d294 | -6.59436 | -58.59785 | 2026-09-01 05:16:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 9d1867fb-cd2e-31a7-9092-f5e07ec89c42 | -6.92524 | -55.62635 | 2026-09-01 05:16:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3079a241-e562-3273-852d-e964526ac1e5 | -7.05297 | -52.71488 | 2026-09-01 05:16:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c3cbd050-6d48-3a25-b490-a2f55d7d6b11 | -6.94963 | -55.64448 | 2026-09-01 05:16:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 534f8d07-1716-3240-a688-97b47a7f4e0e | -6.0024 | -57.82722 | 2026-09-01 05:16:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| d7e6c634-ee73-3170-b354-b09b686d9077 | -7.69062 | -55.34509 | 2026-09-01 05:16:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 90a302dc-a9ab-39a3-95cf-a943e5bc3c51 | -6.95961 | -55.64605 | 2026-09-01 05:16:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 8.7 |
| 77a6532b-d99c-3922-a508-d8019060a492 | -6.81718 | -59.44296 | 2026-09-01 05:16:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 98690997-3035-3b97-98e8-1bf1ac128dbd | -6.01742 | -57.82196 | 2026-09-01 05:16:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| aab7f07c-fcca-30c9-a4fe-eb21cd3930ce | -10.86463 | -45.35612 | 2026-09-01 05:16:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 832e285d-1338-3b26-97bb-4699ba82188f | -6.68851 | -55.58144 | 2026-09-01 05:16:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| eb644beb-6dd4-3e95-81f0-daa22feb1b13 | -10.86965 | -45.36681 | 2026-09-01 05:16:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 2d68ef25-781d-3715-97a4-e46ada8bfc12 | -6.86367 | -59.48194 | 2026-09-01 05:16:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| ffa9ee23-3866-3066-bb57-0686875acf3c | -8.13136 | -54.96529 | 2026-09-01 05:16:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| e33b61f1-ceb6-3714-8928-930a6f32982b | -3.48216 | -50.59175 | 2026-09-01 05:16:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 2b27e937-c909-347c-a63f-61e8e209bf9d | -6.92691 | -55.63732 | 2026-09-01 05:16:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 24841e9f-c033-3ac5-8d23-307b46c63b04 | -5.96148 | -57.69387 | 2026-09-01 05:16:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 85bb6d05-704c-3798-b672-fb2cf0f0fbee | -3.78449 | -52.40711 | 2026-09-01 05:16:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 96686959-9624-3143-885d-45c4d23f592b | -9.46469 | -45.61695 | 2026-09-01 05:16:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 0.6 |
| ce5c11ef-5296-3a59-a10f-956e0975b8fd | -9.15406 | -59.53953 | 2026-09-01 05:16:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 557cce0f-31ce-369e-bd7f-e5903eab08c3 | -10.20921 | -50.31516 | 2026-09-01 05:16:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 679e2d27-e0a4-38bf-95fe-d526f115df3b | -5.84736 | -57.75273 | 2026-09-01 05:16:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 0f4d2550-7d21-3e31-b120-5ef231b20a39 | -7.19312 | -60.67559 | 2026-09-01 05:16:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c1194968-6ab3-34fd-8928-d2823279d286 | -9.16097 | -60.2921 | 2026-09-01 05:16:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 8f1f9029-c03a-34ea-b2c3-b564f6aee203 | -10.0424 | -48.69093 | 2026-09-01 05:16:00 | NPP-375D | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 3a447e30-4200-3d5d-ae09-cc5dd548505f | -6.84727 | -59.42133 | 2026-09-01 05:16:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 533caa84-f3e0-3a89-8738-6e256f335ef5 | -8.7109 | -52.36249 | 2026-09-01 05:16:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 9f23fd99-76e8-3bda-a00f-6ca7cafc9e50 | -8.95327 | -60.60296 | 2026-09-01 05:16:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0b187ea2-ce4c-3151-8d8b-7adbabf17b8e | -8.27264 | -54.93187 | 2026-09-01 05:16:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 7.4 |
| c6480f8a-e1f5-3b80-8728-a089cb7f9b09 | -6.15967 | -52.63642 | 2026-09-01 05:16:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| cf8e9a23-0df5-3a45-a61e-3f7db1c23435 | -6.60628 | -58.5916 | 2026-09-01 05:16:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 70e7cb91-534a-3bc8-b14a-5f9198fd4177 | -11.25028 | -45.14865 | 2026-09-01 05:16:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 8ad168ca-a76e-31f3-8507-77912f45c478 | -9.15543 | -59.53125 | 2026-09-01 05:16:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 839aea8c-6a22-3378-a972-f1b8fad7f533 | -8.69073 | -54.68893 | 2026-09-01 05:16:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 79366207-df71-3370-8a65-9d17454b0737 | -5.48272 | -57.15532 | 2026-09-01 05:16:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 92245cfc-aa85-3422-8373-1dae6935d8e1 | -8.76894 | -46.44741 | 2026-09-01 05:16:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| eb5e2676-3411-346e-b078-2ca18869752d | -7.6254 | -55.30229 | 2026-09-01 05:16:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| fc9afb65-a9e3-3f13-a4be-40c511416e06 | -7.35268 | -60.58706 | 2026-09-01 05:16:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 14.7 |
| eac49b2b-3a21-3460-9ff3-6d156ae45624 | -6.15617 | -53.75237 | 2026-09-01 05:16:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 343c1b9b-9f4f-328c-be56-481dbe67c8f4 | -6.94518 | -55.62951 | 2026-09-01 05:16:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 06c3eb77-050c-3478-b087-302e75d0df7c | -8.03734 | -61.73592 | 2026-09-01 05:16:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9cea5850-a0d7-3d63-b6d0-c177162825dc | -4.15862 | -60.69398 | 2026-09-01 05:16:00 | NPP-375D | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 6bed62c3-539c-3808-8595-ac9238631f5e | -10.32926 | -49.94782 | 2026-09-01 05:16:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 8a13a5f0-e8e3-3d46-acda-9985d3ffad99 | -6.86952 | -59.46945 | 2026-09-01 05:16:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| aea39fe1-409d-34e7-8a20-4fe316916f83 | -5.86155 | -57.55661 | 2026-09-01 05:16:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |


[Clique aqui para ver as próximas entradas](README61.md)
