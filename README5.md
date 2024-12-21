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

## Dados Diários - Página 5

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| ff2d7349-e323-3500-b583-47b943d957af | -1.99403 | -44.54108 | 2024-12-21 03:53:00 | NOAA-20 | CEDRAL | MARANHÃO | Brasil | 2103109 | 21 | 33 | nan | nan | nan | Amazônia | 2.3 |
| e3c22db8-8196-3acf-baef-9027e24c33c8 | -3.15244 | -44.2693 | 2024-12-21 03:53:00 | NOAA-20 | SANTA RITA | MARANHÃO | Brasil | 2110203 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 97daf84a-846f-3733-803c-e46ce0752289 | -3.31409 | -42.2671 | 2024-12-21 03:53:00 | NOAA-20 | MAGALHÃES DE ALMEIDA | MARANHÃO | Brasil | 2106300 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 94c582f6-0f65-3704-8813-06dc6ac04a00 | -9.50901 | -35.9356 | 2024-12-21 03:53:00 | NOAA-20 | RIO LARGO | ALAGOAS | Brasil | 2707701 | 27 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 7bb0733b-26d5-3f52-ae7d-7ef83f980c7a | -3.31274 | -42.26925 | 2024-12-21 03:53:00 | NOAA-20 | MAGALHÃES DE ALMEIDA | MARANHÃO | Brasil | 2106300 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 2f2905ab-6d6e-3c1b-8e93-a339aee713b8 | -1.88452 | -45.55527 | 2024-12-21 03:53:00 | NOAA-20 | TURIAÇU | MARANHÃO | Brasil | 2112407 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 49489f41-5350-32dd-b7cd-edb16824890b | -1.29808 | -47.7575 | 2024-12-21 03:53:00 | NOAA-20 | SÃO FRANCISCO DO PARÁ | PARÁ | Brasil | 1507409 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| bd687e9f-3e4e-3bfc-8ddb-1ab66ee08114 | -1.88357 | -45.5612 | 2024-12-21 03:53:00 | NOAA-20 | TURIAÇU | MARANHÃO | Brasil | 2112407 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 21389d6b-726c-3918-acbf-08179ea00bc2 | -5.17722 | -37.58379 | 2024-12-21 03:53:00 | NOAA-20 | BARAÚNA | RIO GRANDE DO NORTE | Brasil | 2401453 | 24 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 5645bf7f-b402-39d7-97ce-ddbe54fd1d3a | -7.15283 | -40.26287 | 2024-12-21 03:53:00 | NOAA-20 | ARARIPE | CEARÁ | Brasil | 2301307 | 23 | 33 | nan | nan | nan | Caatinga | 3.2 |
| 093475e7-82ec-301b-a634-fcb9478b80ca | -5.47153 | -39.30961 | 2024-12-21 03:53:00 | NOAA-20 | QUIXERAMOBIM | CEARÁ | Brasil | 2311405 | 23 | 33 | nan | nan | nan | Caatinga | 1.5 |
| e7180e34-252f-37a6-80cc-a351eec61837 | -3.75693 | -47.19298 | 2024-12-21 03:53:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 6ffd7b81-f52b-3469-b4f1-da190407790a | -3.90382 | -47.15972 | 2024-12-21 03:53:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 1418b17a-e8b4-3eaf-9113-c356228e5d52 | -5.11494 | -43.32446 | 2024-12-21 03:53:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 937426d1-8286-3bc2-bcb4-5c7cf56f64d7 | -2.6723 | -46.91419 | 2024-12-21 03:53:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 57ad391e-4901-3ede-b92a-004ccfacad0e | -2.67473 | -46.93316 | 2024-12-21 03:53:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 96aa5063-4b49-3b87-99dd-692d0d0175ea | -3.42242 | -44.68833 | 2024-12-21 03:53:00 | NOAA-20 | ARARI | MARANHÃO | Brasil | 2101004 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 1358b92f-3e3f-3a92-abc5-133ce205f6db | -2.50823 | -48.06427 | 2024-12-21 03:53:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 098eeaf0-c246-3669-90ec-6a22e72cd0af | -7.44534 | -40.36213 | 2024-12-21 03:53:00 | NOAA-20 | ARARIPINA | PERNAMBUCO | Brasil | 2601102 | 26 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 977daf1e-1fe9-361c-a60c-e2a7c4e0fed8 | -1.87345 | -45.55957 | 2024-12-21 03:53:00 | NOAA-20 | TURIAÇU | MARANHÃO | Brasil | 2112407 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 7128b769-d9db-3baa-9b07-0557036f7261 | -7.31969 | -39.9883 | 2024-12-21 03:53:00 | NOAA-20 | ARARIPE | CEARÁ | Brasil | 2301307 | 23 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 1f7f9320-ef7e-3161-9808-24a60a24b646 | -2.62598 | -48.03788 | 2024-12-21 03:53:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| dfe38851-e5e9-3292-a22c-81b4940a2eed | -7.32202 | -39.97379 | 2024-12-21 03:53:00 | NOAA-20 | ARARIPE | CEARÁ | Brasil | 2301307 | 23 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 4b0959fc-3b72-326c-b829-33d55039ec28 | -7.89852 | -35.24398 | 2024-12-21 03:53:00 | NOAA-20 | PAUDALHO | PERNAMBUCO | Brasil | 2610608 | 26 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 8f3faf2d-fcdf-3ac7-a7a2-ddc86ad0f392 | -10.17654 | -36.37355 | 2024-12-21 03:55:00 | NOAA-20 | PENEDO | ALAGOAS | Brasil | 2706703 | 27 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| fd4138bd-a1f1-34b2-a1e2-a74e42245371 | -16.34913 | -43.69651 | 2024-12-21 03:55:00 | NOAA-20 | CAPITÃO ENÉAS | MINAS GERAIS | Brasil | 3112703 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 32965d0f-c8ca-31d8-bbff-5887ffdcc915 | -10.87735 | -41.23658 | 2024-12-21 03:55:00 | NOAA-20 | OUROLÂNDIA | BAHIA | Brasil | 2923357 | 29 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 185e4fb6-e84d-39c9-a045-dcda693c37ce | -9.72714 | -43.49646 | 2024-12-21 03:55:00 | NOAA-20 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 1fce5a87-4568-37d6-b9a4-892ed02c93ba | -15.96535 | -38.95456 | 2024-12-21 03:55:00 | NOAA-20 | BELMONTE | BAHIA | Brasil | 2903409 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 7060eb35-10f6-3fbf-ab53-5381c28ec8dd | -8.93747 | -44.24599 | 2024-12-21 03:55:00 | NOAA-20 | SANTA LUZ | PIAUÍ | Brasil | 2209302 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| e5cfb459-3f89-3d5e-91a8-ac1c04125b0e | -10.87673 | -41.24035 | 2024-12-21 03:55:00 | NOAA-20 | OUROLÂNDIA | BAHIA | Brasil | 2923357 | 29 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 2c8cfa2e-c295-3852-8a90-efc14f4c6ba5 | -10.94915 | -39.27527 | 2024-12-21 03:55:00 | NOAA-20 | CANSANÇÃO | BAHIA | Brasil | 2906808 | 29 | 33 | nan | nan | nan | Caatinga | 0.9 |
| fc82315f-9608-37c9-aeac-373cfc4a1e26 | -17.75386 | -39.59553 | 2024-12-21 03:55:00 | NOAA-20 | CARAVELAS | BAHIA | Brasil | 2906907 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| fe351de6-9d69-3876-aa65-b5e4a045137c | -12.00038 | -38.16805 | 2024-12-21 03:55:00 | NOAA-20 | ENTRE RIOS | BAHIA | Brasil | 2910503 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 1a86c672-e464-3c31-a9a3-cc22b01ab6dd | -17.75443 | -39.59181 | 2024-12-21 03:55:00 | NOAA-20 | CARAVELAS | BAHIA | Brasil | 2906907 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 4e564ce3-9a9e-312f-bad7-999825171194 | -17.51571 | -39.55345 | 2024-12-21 03:55:00 | NOAA-20 | ALCOBAÇA | BAHIA | Brasil | 2900801 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 7192ace1-2b40-3885-ace1-58f050a8a412 | -29.8735 | -51.15896 | 2024-12-21 03:59:00 | NOAA-20 | CANOAS | RIO GRANDE DO SUL | Brasil | 4304606 | 43 | 33 | nan | nan | nan | Pampa | 1.4 |
| bbab194c-3749-34e6-bce0-60335ce379b8 | -29.7773 | -51.18014 | 2024-12-21 03:59:00 | NOAA-20 | SÃO LEOPOLDO | RIO GRANDE DO SUL | Brasil | 4318705 | 43 | 33 | nan | nan | nan | Pampa | 1.0 |
| 5ddba3ca-d4e4-3038-b4d2-38a29e98d026 | -29.77834 | -51.17531 | 2024-12-21 03:59:00 | NOAA-20 | SÃO LEOPOLDO | RIO GRANDE DO SUL | Brasil | 4318705 | 43 | 33 | nan | nan | nan | Pampa | 1.0 |
| e25289cf-83b9-3599-946f-d43d1b1ade74 | -1.36563 | -46.02674 | 2024-12-21 04:44:00 | NOAA-21 | CARUTAPERA | MARANHÃO | Brasil | 2102903 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 367dbcd8-223c-32da-bbfd-b6e50648c753 | -0.37294 | -50.08786 | 2024-12-21 04:44:00 | NOAA-21 | CHAVES | PARÁ | Brasil | 1502509 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 5551232d-b683-33a2-b9ba-e16cd4147ae1 | -0.35959 | -50.08221 | 2024-12-21 04:44:00 | NOAA-21 | CHAVES | PARÁ | Brasil | 1502509 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 21c1e05a-542a-30d8-8dd4-a844143845a7 | -0.99995 | -48.87778 | 2024-12-21 04:44:00 | NOAA-21 | CACHOEIRA DO ARARI | PARÁ | Brasil | 1502004 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 7dda34f1-556a-3b20-b950-eb4bf86d6401 | -1.61916 | -45.83958 | 2024-12-21 04:44:00 | NOAA-21 | AMAPÁ DO MARANHÃO | MARANHÃO | Brasil | 2100550 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 5693b5d5-6cff-3472-af02-21a551b5d639 | -0.33447 | -48.43382 | 2024-12-21 04:44:00 | NOAA-21 | SOURE | PARÁ | Brasil | 1507904 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b10d2082-369f-322d-a2bf-bd555b408266 | -0.33784 | -48.43434 | 2024-12-21 04:44:00 | NOAA-21 | SOURE | PARÁ | Brasil | 1507904 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4a8e965b-9fc1-373d-91b6-3654bc983fb4 | -0.99941 | -48.88131 | 2024-12-21 04:44:00 | NOAA-21 | CACHOEIRA DO ARARI | PARÁ | Brasil | 1502004 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4103a983-5cfb-37c7-9b3d-29fe29cc4cc9 | -1.08789 | -48.21209 | 2024-12-21 04:44:00 | NOAA-21 | SANTO ANTÔNIO DO TAUÁ | PARÁ | Brasil | 1507003 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f4290d88-2278-34c8-9fa1-03f781286ed5 | -0.85898 | -47.13052 | 2024-12-21 04:44:00 | NOAA-21 | SÃO JOÃO DE PIRABAS | PARÁ | Brasil | 1507474 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| b6dbfd27-2342-3bba-b7ad-8bfa59ff0c28 | 0.6573 | -51.57056 | 2024-12-21 04:44:00 | NOAA-21 | PORTO GRANDE | AMAPÁ | Brasil | 1600535 | 16 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 9482d3dd-7da6-3639-ade4-4857b3ed4914 | -0.3412 | -48.43486 | 2024-12-21 04:44:00 | NOAA-21 | SOURE | PARÁ | Brasil | 1507904 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 04c97f71-b533-3257-93c0-13f35cc6d8cd | -0.25698 | -51.49687 | 2024-12-21 04:44:00 | NOAA-21 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 719ab912-c1dc-3a01-9163-ac9915b27c1e | -0.00434 | -51.67116 | 2024-12-21 04:44:00 | NOAA-21 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 0.7 |
| dcee478a-5743-37f4-809a-51057da887da | 4.45665 | -61.02608 | 2024-12-21 04:44:00 | NOAA-21 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 10.8 |
| 353f96a7-96c9-3103-ae08-9cc3917e3951 | 0.69639 | -51.44051 | 2024-12-21 04:44:00 | NOAA-21 | PORTO GRANDE | AMAPÁ | Brasil | 1600535 | 16 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 341ce65a-7e66-3934-8a36-be553d88584f | -1.01579 | -48.0691 | 2024-12-21 04:44:00 | NOAA-21 | SÃO CAETANO DE ODIVELAS | PARÁ | Brasil | 1507102 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 32268dfa-4320-38d6-b2fb-909fe84842b5 | -1.30326 | -47.75132 | 2024-12-21 04:44:00 | NOAA-21 | SÃO FRANCISCO DO PARÁ | PARÁ | Brasil | 1507409 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| a060300f-020a-3e99-ac3a-8ef3e49e2bca | -1.29979 | -47.75079 | 2024-12-21 04:44:00 | NOAA-21 | SÃO FRANCISCO DO PARÁ | PARÁ | Brasil | 1507409 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 8483b8ea-13a6-3585-b43e-e31431815dfc | -1.52607 | -46.06849 | 2024-12-21 04:44:00 | NOAA-21 | CARUTAPERA | MARANHÃO | Brasil | 2102903 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 1e8fd067-e875-37f7-820c-cfd3876fb074 | 4.45731 | -61.03079 | 2024-12-21 04:44:00 | NOAA-21 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 10.8 |
| 0dee0aa2-3892-33d7-a5ba-a1e2cbfaf036 | -0.24753 | -48.64587 | 2024-12-21 04:44:00 | NOAA-21 | SOURE | PARÁ | Brasil | 1507904 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| aa3e227b-e926-366d-8769-a023ea1615d5 | -0.35628 | -50.0817 | 2024-12-21 04:44:00 | NOAA-21 | CHAVES | PARÁ | Brasil | 1502509 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| c6b9ec9d-6eb9-3548-9741-541ef829b09e | -0.33728 | -48.43792 | 2024-12-21 04:44:00 | NOAA-21 | SOURE | PARÁ | Brasil | 1507904 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| b835d421-a523-3469-a43c-e939cf70aaa3 | -0.06213 | -51.33005 | 2024-12-21 04:44:00 | NOAA-21 | SANTANA | AMAPÁ | Brasil | 1600600 | 16 | 33 | nan | nan | nan | Amazônia | 0.6 |
| f4a03ada-b2c4-3aea-9b20-0eb01de4b3b5 | -0.25641 | -51.50049 | 2024-12-21 04:44:00 | NOAA-21 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 1.2 |
| fdb17272-aabe-36ed-9c2d-0e688ea71638 | -1.08562 | -47.93522 | 2024-12-21 04:44:00 | NOAA-21 | CASTANHAL | PARÁ | Brasil | 1502400 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 97d9866a-7e49-3b0f-9998-11f6acf5a58f | 0.46664 | -51.34163 | 2024-12-21 04:44:00 | NOAA-21 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 8981b276-2587-3636-a59d-163a63d4702d | -0.36964 | -50.08736 | 2024-12-21 04:44:00 | NOAA-21 | CHAVES | PARÁ | Brasil | 1502509 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 12d6702d-2f18-3e93-89fa-cf30128b2aa2 | -0.85836 | -47.13453 | 2024-12-21 04:44:00 | NOAA-21 | SÃO JOÃO DE PIRABAS | PARÁ | Brasil | 1507474 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 528da370-ac80-3b5e-9b9c-58c920aa5b0b | -0.35298 | -50.08119 | 2024-12-21 04:44:00 | NOAA-21 | CHAVES | PARÁ | Brasil | 1502509 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 80116744-b875-309d-bd91-170d6bc6bd08 | -0.48344 | -48.53007 | 2024-12-21 04:44:00 | NOAA-21 | SOURE | PARÁ | Brasil | 1507904 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 8641a411-d571-3afa-8ac7-9fa6fc82beff | 4.45094 | -61.0328 | 2024-12-21 04:44:00 | NOAA-21 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 10.8 |
| ef17dfa6-f4de-3ad8-8be4-2df8f9b43490 | -4.06754 | -47.08936 | 2024-12-21 04:46:00 | NOAA-21 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 1527e0fb-e379-3b36-ba29-12ddb09a3c6c | -2.44584 | -48.57482 | 2024-12-21 04:46:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 368c2e86-cac8-3b09-af94-bf82c95f819b | -4.02042 | -47.05086 | 2024-12-21 04:46:00 | NOAA-21 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c1b746c0-8dea-32eb-9898-933c089cdd95 | -2.85218 | -46.73114 | 2024-12-21 04:46:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 5620c008-2086-3780-84cc-3a1d2c1d84e2 | -2.62852 | -48.03335 | 2024-12-21 04:46:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 7d451f65-ded2-3b86-876a-fd8ab3dfad6d | -4.0017 | -46.55563 | 2024-12-21 04:46:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 471c64cc-4bf8-3cc6-8aba-07d6c633f9e1 | -3.31476 | -42.26739 | 2024-12-21 04:46:00 | NOAA-21 | MAGALHÃES DE ALMEIDA | MARANHÃO | Brasil | 2106300 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 53af1370-a0e0-3628-bbae-0ea780b6bf23 | -3.24576 | -46.02604 | 2024-12-21 04:46:00 | NOAA-21 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 22fbe48c-f054-3992-ac16-94bcfded4427 | -1.61953 | -53.26403 | 2024-12-21 04:46:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 03420125-84c2-38a6-b563-03c66c2a587a | -3.91428 | -46.67204 | 2024-12-21 04:46:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 5eda76b2-8903-3334-8559-aee84c39d00d | -1.29194 | -53.09574 | 2024-12-21 04:46:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 656f5027-e067-3840-bf24-8ed57f3b64cb | -3.91974 | -46.89761 | 2024-12-21 04:46:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 68a66926-bd33-3093-b57e-38b971597c73 | -9.72908 | -43.496 | 2024-12-21 04:46:00 | NOAA-21 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| ae52327c-4138-30da-8827-c02113a20131 | -3.91329 | -46.65322 | 2024-12-21 04:46:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 7cced8ee-2ca8-3627-a9f9-dfc19295b4b3 | -2.54892 | -46.88206 | 2024-12-21 04:46:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 253f0b8b-4a89-324f-8439-203f7f05ced2 | -4.1015 | -46.81699 | 2024-12-21 04:46:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 34323f59-9ffe-37b4-a4e3-eb1ea912f428 | -3.80124 | -46.85147 | 2024-12-21 04:46:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 3.4 |
| f11a1e87-d95d-393b-8cea-e8b47da726d5 | -3.08991 | -46.56649 | 2024-12-21 04:46:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 143d3fe8-dcdb-3c30-b1ed-8557c5b0b5c2 | -2.50878 | -48.05864 | 2024-12-21 04:46:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 38ec1cb8-978f-38e0-aea3-f5ea576e1ea4 | -5.11434 | -43.32559 | 2024-12-21 04:46:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| c08b8816-3197-3617-93e3-fb6edec99b1e | -4.07077 | -46.91851 | 2024-12-21 04:46:00 | NOAA-21 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 3.9 |
| c3560190-e462-3b5d-ba71-e06b24ebe345 | -1.22026 | -53.67948 | 2024-12-21 04:46:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 910e7acb-f1b8-3e7e-8746-beadda9d0e77 | -3.87456 | -46.52395 | 2024-12-21 04:46:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 65f0da91-0b89-3534-b4b9-ccb4254c0f88 | -3.99789 | -46.55508 | 2024-12-21 04:46:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 2b518f5e-7675-3176-9587-bd025ee51a13 | -3.08683 | -46.56134 | 2024-12-21 04:46:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 74826574-d3e6-389a-b711-975f943435d6 | -3.80702 | -46.71442 | 2024-12-21 04:46:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b89d64c3-7927-3634-a554-fc6978cfdfac | -2.70608 | -46.13552 | 2024-12-21 04:46:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| dbf24f5f-4a59-3703-af1f-ee7f883a02df | -4.06385 | -47.08879 | 2024-12-21 04:46:00 | NOAA-21 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |


[Clique aqui para ver as próximas entradas](README6.md)
