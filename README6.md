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

## Dados Diários - Página 6

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 65588838-b60a-38d5-b1bd-2ca92c7bce21 | -6.7249 | -45.62 | 2026-09-29 01:20:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 68.7 |
| 771e79f9-e6fc-3c76-868a-de818d546be8 | 1.6749 | -55.9225 | 2026-09-29 01:20:00 | GOES-19 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 70.4 |
| 39b56000-9f86-30f3-964d-770115894904 | -6.2947 | -43.6427 | 2026-09-29 01:20:00 | GOES-19 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 175.4 |
| 5fd3a7de-0238-352a-b622-afdb8fae2a2a | -5.6081 | -45.0038 | 2026-09-29 01:20:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 100.2 |
| 8ec524fd-adcb-3c37-8ddc-ed95534b7e37 | -9.9595 | -50.1431 | 2026-09-29 01:20:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 68.0 |
| c9038cc7-0ea6-32d6-b85d-4cc8753376d5 | -7.7025 | -48.8667 | 2026-09-29 01:20:00 | GOES-19 | ARAPOEMA | TOCANTINS | Brasil | 1702307 | 17 | 33 | nan | nan | nan | Amazônia | 51.2 |
| 7c6b41e7-f9b0-3ada-925a-7a2cfe7baa35 | -7.8486 | -45.8138 | 2026-09-29 01:20:00 | GOES-19 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 294.3 |
| fcc96a40-d886-3b94-abd4-82ae4689bebf | -10.3894 | -61.2502 | 2026-09-29 01:20:00 | GOES-19 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 81.4 |
| 834f0761-ebf8-31a5-bfbe-6ef44d0f03e0 | -11.1775 | -44.7832 | 2026-09-29 01:20:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 61.9 |
| 2e230408-63db-3566-ba14-7874a0661a7a | 1.675 | -55.9028 | 2026-09-29 01:20:00 | GOES-19 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 83.7 |
| 54a9c794-2f8c-3a9b-9726-10478bbd8567 | -10.3892 | -61.2695 | 2026-09-29 01:20:00 | GOES-19 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 63.5 |
| 7c0451ff-197a-38d4-96f8-62c307b06c73 | -10.4081 | -61.2492 | 2026-09-29 01:20:00 | GOES-19 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 51.3 |
| d7c29c5c-fb48-3394-b5be-4805ea3fdcb1 | -9.5156 | -40.3061 | 2026-09-29 01:20:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 70.3 |
| afcc6ed1-4ea0-3a82-bbe9-fc42c02fb931 | -3.7166 | -54.2096 | 2026-09-29 01:20:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 63.9 |
| 1d5e6292-81d6-3f65-a25f-fefd08bb89e0 | -7.8483 | -45.8363 | 2026-09-29 01:20:00 | GOES-19 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 70.4 |
| c3b3f50e-3c18-3ac6-aa7a-9b6d695b7c48 | -3.7166 | -54.2297 | 2026-09-29 01:20:00 | GOES-19 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 92.3 |
| 2a5ff47c-79b9-3dbb-b698-73a3fca6b58c | -7.3825 | -72.4621 | 2026-09-29 01:20:00 | GOES-19 | GUAJARÁ | AMAZONAS | Brasil | 1301654 | 13 | 33 | nan | nan | nan | Amazônia | 73.8 |
| 66461278-e4a9-39f3-bad4-b0472484b9f3 | -9.1256 | -67.8507 | 2026-09-29 01:20:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 72.0 |
| 82527113-9f26-3ab1-a868-0c3334c07ce5 | -7.3825 | -72.4803 | 2026-09-29 01:20:00 | GOES-19 | GUAJARÁ | AMAZONAS | Brasil | 1301654 | 13 | 33 | nan | nan | nan | Amazônia | 68.3 |
| 50743758-bb5d-3529-861f-93dcfab4637b | -15.4585 | -46.1367 | 2026-09-29 01:20:00 | GOES-19 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 101.8 |
| ad4700bf-e358-3008-ab0b-a69b64b5784b | -7.8483 | -45.8363 | 2026-09-29 01:30:00 | GOES-19 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 64.2 |
| d23138ed-cb68-3fd3-8820-0d74f86b8c2b | -11.1775 | -44.7832 | 2026-09-29 01:30:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 59.8 |
| 7251b6f1-bb59-3709-9a63-4e6a7fcfa407 | -15.4585 | -46.1367 | 2026-09-29 01:30:00 | GOES-19 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 132.1 |
| 10dfc0e2-4053-3d12-aba6-51abda6c217d | -6.7249 | -45.62 | 2026-09-29 01:30:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 142.8 |
| b0aaf60d-b3f3-3d71-84d7-96f809946dcc | 1.6749 | -55.9225 | 2026-09-29 01:30:00 | GOES-19 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 67.1 |
| 8857850f-1ac6-3b9c-8627-bef5232ee019 | -11.937 | -50.9125 | 2026-09-29 01:30:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 68.5 |
| 67ff2b66-de05-3770-bc6a-1e56c942a130 | -7.3825 | -72.4803 | 2026-09-29 01:30:00 | GOES-19 | GUAJARÁ | AMAZONAS | Brasil | 1301654 | 13 | 33 | nan | nan | nan | Amazônia | 71.4 |
| 8b1691fe-6abe-370e-a744-4b3633df2dd3 | -8.2479 | -45.4583 | 2026-09-29 01:30:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 74.1 |
| 5a4ef24d-54a1-37b3-99da-07672d38c999 | -9.9593 | -50.1644 | 2026-09-29 01:30:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 61.4 |
| b273aa42-987f-3236-8dee-25d45d191698 | -7.8486 | -45.8138 | 2026-09-29 01:30:00 | GOES-19 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 254.6 |
| 3e59e45d-fbc2-32e7-be46-3552e0532804 | -5.6083 | -44.9811 | 2026-09-29 01:30:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 55.7 |
| 4abf72f1-db69-324a-9a19-19df379e5a86 | -7.3825 | -72.4621 | 2026-09-29 01:30:00 | GOES-19 | GUAJARÁ | AMAZONAS | Brasil | 1301654 | 13 | 33 | nan | nan | nan | Amazônia | 78.2 |
| 0b7fe19a-1ef6-3791-b2b1-0c15b996deca | -9.9595 | -50.1431 | 2026-09-29 01:30:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 78.2 |
| edd2c66c-3994-3d73-baf5-1a5a409f6e5f | -6.7251 | -45.5975 | 2026-09-29 01:30:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 70.9 |
| cf774d14-6074-3505-9816-41ab3d204a1d | 1.675 | -55.9028 | 2026-09-29 01:30:00 | GOES-19 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 91.4 |
| 53c16403-e236-34dd-9df6-00860fad758f | -11.9373 | -50.8912 | 2026-09-29 01:30:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 69.2 |
| b4f2a5e2-1f03-3dc2-8831-ae1e26321a93 | 1.6567 | -55.8833 | 2026-09-29 01:30:00 | GOES-19 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 78.6 |
| 11956c52-f4e1-3c3c-8bca-ce6dc72c1a2b | -3.7166 | -54.2297 | 2026-09-29 01:30:00 | GOES-19 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 53.0 |
| a54f25fe-16cd-38f6-98be-72058b658bf1 | -6.2759 | -43.6442 | 2026-09-29 01:30:00 | GOES-19 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 52.8 |
| 405d8182-ddee-376a-94d4-3e7ec5b59e74 | -7.8297 | -45.8156 | 2026-09-29 01:30:00 | GOES-19 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 191.9 |
| bc45b43e-d272-3e1b-9d0d-d7eb640f9e65 | -9.9568 | -59.2629 | 2026-09-29 01:30:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 50.0 |
| bf09d228-9e9c-317f-a775-4756cef80e9c | -8.2291 | -45.4602 | 2026-09-29 01:30:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 52.1 |
| fed56ee7-9969-3faa-9636-4e3d03829c95 | -6.2947 | -43.6427 | 2026-09-29 01:30:00 | GOES-19 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 148.4 |
| d8248c15-c081-3e75-8a45-46a9f183c5c2 | -5.6081 | -45.0038 | 2026-09-29 01:30:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 135.7 |
| 2e1fba2a-6742-3460-bacb-68c6eb2f086f | 1.6566 | -55.903 | 2026-09-29 01:30:00 | GOES-19 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 65.1 |
| 678a33ad-a563-3746-a24b-42398cc2391f | -5.6268 | -45.0025 | 2026-09-29 01:30:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 91.2 |
| e2eb0162-1e75-3662-994d-87f9efd076c2 | -21.0665 | -48.8196 | 2026-09-29 01:40:00 | GOES-19 | PALMARES PAULISTA | SÃO PAULO | Brasil | 3535101 | 35 | 33 | nan | nan | nan | Mata Atlântica | 151.6 |
| e61ec0ef-7fad-34fb-83a7-208291f6ed88 | -6.3285 | -52.6379 | 2026-09-29 01:40:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 59.9 |
| 7bd8f62a-4d3a-326e-b284-5506f148e8e0 | -7.3825 | -72.4621 | 2026-09-29 01:40:00 | GOES-19 | GUAJARÁ | AMAZONAS | Brasil | 1301654 | 13 | 33 | nan | nan | nan | Amazônia | 52.8 |
| 516fc4c2-48d1-30e6-87b9-9d67e5831c4f | -5.6081 | -45.0038 | 2026-09-29 01:40:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 250.2 |
| 456ea368-5bf8-3e0f-b202-92472c38a490 | -5.6083 | -44.9811 | 2026-09-29 01:40:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 131.8 |
| c5a14fb0-4e39-3062-bef1-3f68f8de5e6c | -8.2479 | -45.4583 | 2026-09-29 01:40:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 72.3 |
| 8dfaec2c-d57e-386a-adc1-a706950923ff | -5.6268 | -45.0025 | 2026-09-29 01:40:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 74.7 |
| 643db32d-1714-345c-a9c3-b5ddbb2e4d2d | -7.8486 | -45.8138 | 2026-09-29 01:40:00 | GOES-19 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 248.0 |
| 4b89e708-a397-3d95-9c25-feef97d54ef4 | -7.8488 | -45.7912 | 2026-09-29 01:40:00 | GOES-19 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 62.2 |
| 5720d1ca-46fd-34e8-949c-7c0dfc223d37 | -8.5738 | -67.0125 | 2026-09-29 01:40:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 51.8 |
| c0656dc7-6043-33b7-bb62-2f2faa464b56 | -7.7025 | -48.8667 | 2026-09-29 01:40:00 | GOES-19 | ARAPOEMA | TOCANTINS | Brasil | 1702307 | 17 | 33 | nan | nan | nan | Amazônia | 57.7 |
| 13deab4b-0443-3a1e-884f-9f8d0e5fc221 | -6.3287 | -52.6174 | 2026-09-29 01:40:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 65.0 |
| 97d4489c-bb59-3f96-beeb-f1f3ab039e9e | -7.8483 | -45.8363 | 2026-09-29 01:40:00 | GOES-19 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 55.9 |
| 46f4d5dc-34a3-390f-8c25-aff4c4f9ebd9 | -6.31 | -52.6389 | 2026-09-29 01:40:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 53.2 |
| 637252cc-3240-31d6-865c-04c147126f6f | -9.9595 | -50.1431 | 2026-09-29 01:40:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 62.1 |
| d1f48451-f563-3512-ac74-f445290f77c5 | -21.0871 | -48.8149 | 2026-09-29 01:40:00 | GOES-19 | PALMARES PAULISTA | SÃO PAULO | Brasil | 3535101 | 35 | 33 | nan | nan | nan | Mata Atlântica | 83.6 |
| 25e031ba-c5fa-322d-8dfb-3f29e66dddd1 | -8.5738 | -66.994 | 2026-09-29 01:40:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 54.8 |
| 9f1aacc7-ff58-31f7-9105-faf532b287ff | -6.3101 | -52.6184 | 2026-09-29 01:40:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 57.5 |
| 01e43f38-7334-3715-91bd-c1a29d1aa8eb | -6.2947 | -43.6427 | 2026-09-29 01:40:00 | GOES-19 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 143.3 |
| 27d4cf92-ebed-372b-9ee1-f45ba2fac75c | -8.2482 | -45.4356 | 2026-09-29 01:40:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 66.9 |
| de09f2eb-5e94-3982-b9ae-3c2e069de644 | -21.0658 | -48.8428 | 2026-09-29 01:40:00 | GOES-19 | PALMARES PAULISTA | SÃO PAULO | Brasil | 3535101 | 35 | 33 | nan | nan | nan | Mata Atlântica | 123.5 |
| 3d14ef1b-cd7f-32a3-bc64-e27d6d064c36 | -7.3825 | -72.4803 | 2026-09-29 01:40:00 | GOES-19 | GUAJARÁ | AMAZONAS | Brasil | 1301654 | 13 | 33 | nan | nan | nan | Amazônia | 56.0 |
| 1f197135-7d96-34f6-8ef6-576ef489ab42 | -21.0865 | -48.8381 | 2026-09-29 01:40:00 | GOES-19 | PALMARES PAULISTA | SÃO PAULO | Brasil | 3535101 | 35 | 33 | nan | nan | nan | Mata Atlântica | 69.0 |
| c7a1dfea-469c-3d9a-8add-869a1df46da3 | -7.8297 | -45.8156 | 2026-09-29 01:40:00 | GOES-19 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 151.3 |
| a332394c-b4e5-33f0-b942-7792445ec640 | -15.4585 | -46.1367 | 2026-09-29 01:40:00 | GOES-19 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 144.3 |
| 96ee5349-fc74-3574-9ffa-c389bc23d7cf | -11.1775 | -44.7832 | 2026-09-29 01:50:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 58.8 |
| 1b81227a-0f88-37ff-a5cf-b9d29c3caba9 | -6.31 | -52.6389 | 2026-09-29 01:50:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 65.7 |
| b2ce59d8-211e-374e-b06d-eaef58750ed9 | -5.6268 | -45.0025 | 2026-09-29 01:50:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 138.7 |
| 884e4faf-09c4-30a0-9bc3-db362375c4ca | -7.3825 | -72.4621 | 2026-09-29 01:50:00 | GOES-19 | GUAJARÁ | AMAZONAS | Brasil | 1301654 | 13 | 33 | nan | nan | nan | Amazônia | 56.9 |
| 2ea422ac-5fd6-3037-9447-86435428f6bd | -5.6083 | -44.9811 | 2026-09-29 01:50:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 107.2 |
| cbb49207-a7b2-35d6-bde8-dc55cce56e45 | -7.3825 | -72.4803 | 2026-09-29 01:50:00 | GOES-19 | GUAJARÁ | AMAZONAS | Brasil | 1301654 | 13 | 33 | nan | nan | nan | Amazônia | 58.4 |
| 81b7b426-8e40-3bac-a72b-f2401143962e | -11.9373 | -50.8912 | 2026-09-29 01:50:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 134.7 |
| 582daef4-ddba-3656-bc61-c33fec42936d | -7.8483 | -45.8363 | 2026-09-29 01:50:00 | GOES-19 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 63.9 |
| 2017aff8-a82c-37cb-bbdc-5f0250a4609b | -8.5738 | -66.994 | 2026-09-29 01:50:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 52.5 |
| 6344e82b-e7f7-3d59-a451-6f69b8152431 | -7.8297 | -45.8156 | 2026-09-29 01:50:00 | GOES-19 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 169.8 |
| 2ef4ef29-1cfb-3633-9c6b-6270e420b675 | -7.6838 | -48.8682 | 2026-09-29 01:50:00 | GOES-19 | ARAPOEMA | TOCANTINS | Brasil | 1702307 | 17 | 33 | nan | nan | nan | Amazônia | 58.6 |
| 48420845-b296-3b20-b7ac-e72a89d3065e | -5.6081 | -45.0038 | 2026-09-29 01:50:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 226.0 |
| 667fbf18-b668-3b23-a744-a3c91dd72611 | -15.4585 | -46.1367 | 2026-09-29 01:50:00 | GOES-19 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 137.9 |
| 74626ae6-196a-3002-9a13-5d10f7690ef1 | -7.7025 | -48.8667 | 2026-09-29 01:50:00 | GOES-19 | ARAPOEMA | TOCANTINS | Brasil | 1702307 | 17 | 33 | nan | nan | nan | Amazônia | 58.6 |
| 2b87e610-c275-371a-bca0-1fe5f3a01de7 | -7.8486 | -45.8138 | 2026-09-29 01:50:00 | GOES-19 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 207.3 |
| 59c155bf-bc41-30b6-b058-ef49d07c5d4b | -12.1202 | -57.1767 | 2026-09-29 01:50:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 52.8 |
| 9137b290-404f-3e84-8b03-6ca95574c8cd | -6.3101 | -52.6184 | 2026-09-29 01:50:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 82.3 |
| 503fc65f-3390-303d-b1bf-31edbf52aadf | -9.9595 | -50.1431 | 2026-09-29 01:50:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 72.1 |
| 07bef397-1beb-3bc7-900a-2db7b52c893d | -5.627 | -44.9797 | 2026-09-29 01:50:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 66.4 |
| 1d42367e-140e-34a3-9d8d-b663a93befda | -9.9595 | -50.1431 | 2026-09-29 02:00:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 69.6 |
| fd32a260-387a-3171-991e-c2a84bb1d5fb | -11.1775 | -44.7832 | 2026-09-29 02:00:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 59.4 |
| 3b3667be-6632-38c1-8363-5e9be51b5197 | 1.6567 | -55.8833 | 2026-09-29 02:00:00 | GOES-19 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 92.4 |
| 8bc6cd14-e7a6-39a0-8799-471e188e7175 | -11.9373 | -50.8912 | 2026-09-29 02:00:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 129.3 |
| df03f598-0003-3848-a203-6a584590fbe2 | -5.6083 | -44.9811 | 2026-09-29 02:00:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 127.7 |
| afeb2375-10a3-30fb-baac-986f68b61713 | -7.8297 | -45.8156 | 2026-09-29 02:00:00 | GOES-19 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 165.9 |
| f429a4b4-d0bd-3cbc-b349-9f6c46a25a90 | 1.675 | -55.9028 | 2026-09-29 02:00:00 | GOES-19 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 102.9 |
| 26e4780f-63ef-3cad-a8bb-48b3a4afa642 | -9.177 | -61.4073 | 2026-09-29 02:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 70.2 |
| 419473fb-ac8c-3289-8cf8-b3a112c6dbc5 | -5.6268 | -45.0025 | 2026-09-29 02:00:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 163.9 |
| ecfa4648-45f4-3a51-aedb-190d4c9238c8 | -7.6838 | -48.8682 | 2026-09-29 02:00:00 | GOES-19 | ARAPOEMA | TOCANTINS | Brasil | 1702307 | 17 | 33 | nan | nan | nan | Amazônia | 64.6 |


[Clique aqui para ver as próximas entradas](README7.md)
