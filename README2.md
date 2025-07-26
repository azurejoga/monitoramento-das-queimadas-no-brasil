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

## Dados Diários - Página 2

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| aaca3f60-1daa-37f2-b69a-40406f681310 | -6.5441 | -56.2508 | 2025-07-26 01:10:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 63.7 |
| 2895729f-55d0-347f-bac6-035704875206 | -7.2405 | -43.0899 | 2025-07-26 01:10:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 75.7 |
| c81a4d85-7183-3e38-9d97-ccb76e71140d | -3.3957 | -47.5003 | 2025-07-26 01:10:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 81.9 |
| def4548b-4dd2-38aa-9fb0-2470847aa5cd | -6.1549 | -42.6001 | 2025-07-26 01:10:00 | GOES-19 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 174.9 |
| f5a0fc7e-d986-3a31-8ac5-7793a7adbe60 | -3.3958 | -47.4785 | 2025-07-26 01:10:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 70.4 |
| 695dbdd7-048f-37cc-9e35-bd8f19d37a81 | -7.2597 | -43.0645 | 2025-07-26 01:20:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 66.1 |
| 87e34ce2-72e8-37ab-be04-95d5975390d2 | -6.1551 | -42.5764 | 2025-07-26 01:20:00 | GOES-19 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 64.6 |
| 122bdb5f-3815-34b0-995f-0395ff20ef80 | -7.2408 | -43.0664 | 2025-07-26 01:20:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 134.3 |
| 0cec73e9-2b29-38d5-94a2-f18490b85857 | -6.1737 | -42.5985 | 2025-07-26 01:20:00 | GOES-19 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 67.0 |
| 3b99e726-eb21-3551-841a-9dbef99b87e2 | -3.3957 | -47.5003 | 2025-07-26 01:20:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 92.6 |
| 4d31f364-486f-3c39-9c0b-8c239f669693 | -6.5441 | -56.2508 | 2025-07-26 01:20:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 56.8 |
| 9bdff21b-d670-3d57-90b6-f53c4c563dc8 | -6.1549 | -42.6001 | 2025-07-26 01:20:00 | GOES-19 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 167.8 |
| 5a884584-7ba5-3e5f-948d-0e6341edddd5 | -19.01466 | -55.77839 | 2025-07-26 01:22:00 | TERRA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 7.1 |
| 6386ae4a-b184-3ab3-ba97-bfa58dda1243 | -20.6221 | -54.84345 | 2025-07-26 01:22:00 | TERRA_M-M | TERENOS | MATO GROSSO DO SUL | Brasil | 5008008 | 50 | 33 | nan | nan | nan | Cerrado | 8.9 |
| ca8eb836-55bb-33f2-9bbe-1a1a4c073eaa | -21.10624 | -50.61987 | 2025-07-26 01:22:00 | TERRA_M-M | GUARARAPES | SÃO PAULO | Brasil | 3518206 | 35 | 33 | nan | nan | nan | Mata Atlântica | 116.6 |
| 8abeb25d-e74e-3a90-84fa-908991d51f95 | -20.0426 | -57.87146 | 2025-07-26 01:22:00 | TERRA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.8 |
| 8f460b8e-5674-3e17-a0ec-dab6d98820c3 | -21.99369 | -57.61065 | 2025-07-26 01:22:00 | TERRA_M-M | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 41.8 |
| db19f548-9025-3c23-896b-7e6d58e4f4d0 | -22.00331 | -55.53389 | 2025-07-26 01:22:00 | TERRA_M-M | PONTA PORÃ | MATO GROSSO DO SUL | Brasil | 5006606 | 50 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 68079019-3e7a-302c-bb9b-1e2a41e427ce | -21.99501 | -57.62017 | 2025-07-26 01:22:00 | TERRA_M-M | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 18.1 |
| 206df61c-764a-33ab-8d42-a31d2135e46f | -9.64221 | -63.15533 | 2025-07-26 01:24:00 | TERRA_M-M | ALTO PARAÍSO | RONDÔNIA | Brasil | 1100403 | 11 | 33 | nan | nan | nan | Amazônia | 29.4 |
| 40da29f1-977f-3d79-a0be-37452401d13d | -9.97434 | -64.96251 | 2025-07-26 01:24:00 | TERRA_M-M | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 12.3 |
| 89b7b3e4-55fd-36e3-b609-17f121cdd781 | -10.04674 | -64.99091 | 2025-07-26 01:24:00 | TERRA_M-M | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 10.3 |
| 934f04e0-3bdf-39e3-aecd-bb6e861a3922 | -16.30365 | -52.93176 | 2025-07-26 01:24:00 | TERRA_M-M | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 11.8 |
| a8c929e5-f3eb-3afd-ae04-32d506dd2c33 | -16.30711 | -52.92556 | 2025-07-26 01:24:00 | TERRA_M-M | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 13.4 |
| 561d2d10-2ebd-3867-a310-cde24ed0473a | -18.22686 | -54.54721 | 2025-07-26 01:24:00 | TERRA_M-M | COXIM | MATO GROSSO DO SUL | Brasil | 5003306 | 50 | 33 | nan | nan | nan | Cerrado | 16.8 |
| 6804958e-7637-3367-8f6b-259a70f85197 | -9.45993 | -57.85123 | 2025-07-26 01:24:00 | TERRA_M-M | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 7.4 |
| f8d0a9bf-f826-317e-bee9-3fe992b94242 | -13.2411 | -51.15346 | 2025-07-26 01:24:00 | TERRA_M-M | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 32.8 |
| 494c7c47-65f4-3933-9545-c1598f6f1338 | -9.64362 | -63.16619 | 2025-07-26 01:24:00 | TERRA_M-M | ALTO PARAÍSO | RONDÔNIA | Brasil | 1100403 | 11 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 80f9d81e-a40d-33ac-817c-26ac6515f7ed | -10.29302 | -57.05332 | 2025-07-26 01:24:00 | TERRA_M-M | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 10.1 |
| e9f01af5-a9c8-3628-86a1-8e369b7feec1 | -6.6935 | -58.83989 | 2025-07-26 01:26:00 | TERRA_M-M | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 7.4 |
| 63bb1ac9-ef76-3d3a-abd8-2ec13a1255da | -6.63083 | -58.84529 | 2025-07-26 01:26:00 | TERRA_M-M | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 528.9 |
| 995ffced-8087-3e29-b70a-4c78e3d67308 | -6.54633 | -56.24336 | 2025-07-26 01:26:00 | TERRA_M-M | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 24.6 |
| 10605225-085c-3b07-a699-18ded0c9cbd6 | -6.67473 | -58.84264 | 2025-07-26 01:26:00 | TERRA_M-M | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 721.9 |
| 0464ac96-ae24-3a08-895c-fef16e05fbca | -6.68411 | -58.84128 | 2025-07-26 01:26:00 | TERRA_M-M | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 86.2 |
| e7025479-1b31-31c4-8ed9-f81ac4f00fd9 | -7.56073 | -61.40852 | 2025-07-26 01:26:00 | TERRA_M-M | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 24.6 |
| 3b9e0ecf-f4de-37b1-8004-38d857ccbf33 | -6.62285 | -58.85662 | 2025-07-26 01:26:00 | TERRA_M-M | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 6.2 |
| cd147f4a-c8c9-3e65-968d-c52bde92be2a | -6.62001 | -58.83659 | 2025-07-26 01:26:00 | TERRA_M-M | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 490.5 |
| 0360c3aa-0790-3c52-9066-48be67923663 | -7.49325 | -63.8223 | 2025-07-26 01:26:00 | TERRA_M-M | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 9.6 |
| 4bde756f-a54c-3233-84c2-468ba2ca7824 | -6.65741 | -58.85541 | 2025-07-26 01:26:00 | TERRA_M-M | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 88.0 |
| a97a5469-768a-3eaf-b6f7-b8793bd2cfbd | -6.68554 | -58.85128 | 2025-07-26 01:26:00 | TERRA_M-M | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 102.7 |
| 0c2f529c-f835-386e-84f6-d0f6b6cfa443 | -6.77999 | -61.96514 | 2025-07-26 01:26:00 | TERRA_M-M | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 1ece1350-9715-39b4-bd07-e9236742a359 | -6.6372 | -58.84818 | 2025-07-26 01:26:00 | TERRA_M-M | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 294.9 |
| 2b5a82d5-5e67-386a-bf4b-d58a066067bb | -6.65305 | -58.82528 | 2025-07-26 01:26:00 | TERRA_M-M | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 191.7 |
| 3df2e4c5-789e-393f-a9c1-4c06afa070ed | -6.53738 | -56.25998 | 2025-07-26 01:26:00 | TERRA_M-M | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 62.5 |
| 922abd1c-668a-3b0d-8cef-f2393bd08ee8 | -6.64365 | -58.82663 | 2025-07-26 01:26:00 | TERRA_M-M | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 150.4 |
| b1582542-3ad0-32cb-a636-f3e0a04c0677 | -6.62941 | -58.83521 | 2025-07-26 01:26:00 | TERRA_M-M | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 439.5 |
| 6579e747-b8a2-3278-9aa1-31252263bf1a | -7.29695 | -60.17261 | 2025-07-26 01:26:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 859e0e3e-e78c-3c94-bafb-977384ca571f | -5.91626 | -61.30669 | 2025-07-26 01:26:00 | TERRA_M-M | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 13.1 |
| 4a108c05-816c-3a0f-b06a-b52d091b50dd | -6.65596 | -58.8454 | 2025-07-26 01:26:00 | TERRA_M-M | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 699.1 |
| a9decfd7-e9bb-348c-955c-5e56b9c3686e | -6.66535 | -58.84402 | 2025-07-26 01:26:00 | TERRA_M-M | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1141.3 |
| e8f8a460-264f-30fb-b08a-860760fc0ecd | -6.62144 | -58.84662 | 2025-07-26 01:26:00 | TERRA_M-M | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 158.8 |
| c4f3831e-8eeb-3d69-b7c9-4b7e38fb9ba6 | -7.28932 | -60.18287 | 2025-07-26 01:26:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 29ed736d-4083-386f-a04a-791d83086895 | -7.56839 | -61.39832 | 2025-07-26 01:26:00 | TERRA_M-M | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 9.5 |
| 5bd89b84-8821-3fb1-be90-ec2001d9f068 | -6.55756 | -56.24162 | 2025-07-26 01:26:00 | TERRA_M-M | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 27.7 |
| 7294da8d-f137-3cdd-a26f-d585c3eb933c | -6.54859 | -56.25821 | 2025-07-26 01:26:00 | TERRA_M-M | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 23.8 |
| 8e0f6c26-f87a-3a85-8deb-c57d50854d93 | -6.68268 | -58.83125 | 2025-07-26 01:26:00 | TERRA_M-M | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 102.3 |
| e1069634-8921-353d-a10d-04ac14da6eb3 | -7.18501 | -59.44983 | 2025-07-26 01:26:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 4ce80d9b-2d86-36cd-ade6-a19bdff74668 | -7.56962 | -61.40727 | 2025-07-26 01:26:00 | TERRA_M-M | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 24.3 |
| f6ff917f-ae69-304a-b289-961824e55079 | -7.18366 | -59.44044 | 2025-07-26 01:26:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 2abf6ac6-769a-3e9f-a211-4deb41b897d8 | -8.07098 | -63.86189 | 2025-07-26 01:26:00 | TERRA_M-M | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 14e56862-195d-36e0-b536-97329da25e9d | -6.66245 | -58.82392 | 2025-07-26 01:26:00 | TERRA_M-M | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 256.8 |
| 0ae3a0cd-484e-34a8-a335-e7fe7849a1b8 | -6.53809 | -56.26569 | 2025-07-26 01:26:00 | TERRA_M-M | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 43.9 |
| aab9530f-fc4b-3ae0-b5d3-b1213222fe27 | -6.68123 | -58.82112 | 2025-07-26 01:26:00 | TERRA_M-M | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 26.2 |
| 7dd21435-2178-3825-855e-4b6e38f8cc65 | -6.63224 | -58.85525 | 2025-07-26 01:26:00 | TERRA_M-M | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 100.3 |
| 4e803de7-2bab-30b9-93d0-b5d4e34fb4e1 | -6.6639 | -58.83398 | 2025-07-26 01:26:00 | TERRA_M-M | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 216.9 |
| 40054b95-a9e2-3a18-b8b1-3208fb9e4d5d | -6.41437 | -53.34397 | 2025-07-26 01:26:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 20.9 |
| 235828a0-a40e-35e7-b984-eb55a6858b6a | -6.66679 | -58.85405 | 2025-07-26 01:26:00 | TERRA_M-M | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 314.9 |
| aa381948-bc49-356f-9258-b473dc30235d | -6.62798 | -58.8251 | 2025-07-26 01:26:00 | TERRA_M-M | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 9.8 |
| c3a14991-3f3f-36ce-a92f-b3c7898a69bf | -6.63574 | -58.83816 | 2025-07-26 01:26:00 | TERRA_M-M | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 464.6 |
| d74d4372-965f-3964-88e5-054d6bf898ed | -6.67329 | -58.83263 | 2025-07-26 01:26:00 | TERRA_M-M | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 133.0 |
| f2952a5b-c5e0-348a-8d61-38abcd1b02de | -6.67616 | -58.85265 | 2025-07-26 01:26:00 | TERRA_M-M | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 626.8 |
| 447410d2-df5a-33de-aa28-ba7db599107b | -7.94171 | -61.56883 | 2025-07-26 01:26:00 | TERRA_M-M | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 6.9 |
| b666538e-5856-35a2-b40d-6709985fb6bd | -6.64512 | -58.8367 | 2025-07-26 01:26:00 | TERRA_M-M | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 372.4 |
| 4c012853-a804-397c-8780-754ac5d83afd | -7.90424 | -63.53494 | 2025-07-26 01:26:00 | TERRA_M-M | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 9.5 |
| 796a487b-df3e-3152-beda-69ed3eb7a907 | -6.69492 | -58.84988 | 2025-07-26 01:26:00 | TERRA_M-M | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 10.3 |
| 26e308fa-b212-3d16-bc84-4c7aaa8c55b4 | -6.64658 | -58.84676 | 2025-07-26 01:26:00 | TERRA_M-M | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1157.2 |
| 8ef05659-341a-3f0d-99bd-92f9a2bbd9ae | -8.50229 | -64.03977 | 2025-07-26 01:26:00 | TERRA_M-M | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 10.8 |
| 976b0f2a-3b32-3611-8ab1-e48a0e0b43fe | -6.53593 | -56.2508 | 2025-07-26 01:26:00 | TERRA_M-M | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 28.9 |
| a9f07d22-2b7c-3eed-acbf-79bd89635087 | -6.63426 | -58.82804 | 2025-07-26 01:26:00 | TERRA_M-M | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 233.5 |
| 9dfd7135-1c3e-38a6-bc1a-d1e962205f62 | -6.64803 | -58.85678 | 2025-07-26 01:26:00 | TERRA_M-M | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 67.1 |
| cacf43e0-e211-30a8-8e1c-dd594af38eb3 | -6.61859 | -58.82652 | 2025-07-26 01:26:00 | TERRA_M-M | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 19.8 |
| 1f19901d-245f-32d4-832f-bc8ac76dfc8c | -3.45867 | -59.86626 | 2025-07-26 01:26:00 | TERRA_M-M | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 78950a90-aca9-3b88-9470-924b5c8561d8 | -6.67184 | -58.82254 | 2025-07-26 01:26:00 | TERRA_M-M | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 68.7 |
| 54c886e4-12c0-36fe-bb84-0a1bb852f95e | -6.5598 | -56.25642 | 2025-07-26 01:26:00 | TERRA_M-M | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 21.2 |
| 541f4aef-5b29-3289-96ad-2fbf578e9157 | -6.65451 | -58.83534 | 2025-07-26 01:26:00 | TERRA_M-M | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 206.5 |
| 4127ca4e-6ab3-3b37-bcc0-5209396c82de | -6.1551 | -42.5764 | 2025-07-26 01:30:00 | GOES-19 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 73.3 |
| 872ee310-6ff6-39ae-9aba-0a7b5525a50f | -6.5441 | -56.2508 | 2025-07-26 01:30:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 54.9 |
| f73c4122-12f6-3afc-9edf-4a9f5ac6d2b3 | -6.1549 | -42.6001 | 2025-07-26 01:30:00 | GOES-19 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 139.8 |
| ee4bc727-622e-31ea-b2cc-a5f0f354339b | -7.2597 | -43.0645 | 2025-07-26 01:30:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 60.5 |
| fe129f1c-a369-366e-ad63-182c6f67dbf2 | -3.3957 | -47.5003 | 2025-07-26 01:30:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 82.6 |
| 72b7a25b-f966-3253-a4c2-b5daffdfcb5b | -7.2408 | -43.0664 | 2025-07-26 01:30:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 125.0 |
| f7760a88-1fdf-33fa-8ace-4090ef07c37c | -6.5441 | -56.2508 | 2025-07-26 01:40:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 53.3 |
| abd051d6-e7a1-3202-9bf4-885878441e0b | -6.1551 | -42.5764 | 2025-07-26 01:40:00 | GOES-19 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 69.6 |
| 1d1c7bf6-ab35-35b0-84b2-4e789f3c253e | -7.2408 | -43.0664 | 2025-07-26 01:40:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 107.7 |
| ce6cd4d9-82e4-3add-bc13-ef90377ec975 | -16.2761 | -49.9608 | 2025-07-26 01:40:00 | GOES-19 | ANICUNS | GOIÁS | Brasil | 5201306 | 52 | 33 | nan | nan | nan | Cerrado | 126.2 |
| 63d145b6-a8dd-36fd-81e4-a4820aa57332 | -3.3958 | -47.4785 | 2025-07-26 01:40:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 76.3 |
| 1aacdd7a-2a28-3da5-b4bb-bdfaa217d1e2 | -16.2569 | -49.9419 | 2025-07-26 01:40:00 | GOES-19 | ANICUNS | GOIÁS | Brasil | 5201306 | 52 | 33 | nan | nan | nan | Cerrado | 109.3 |
| 0846a5da-3be4-3282-b571-69b298d0e25d | -3.3957 | -47.5003 | 2025-07-26 01:40:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 88.5 |
| 093b75c6-d0af-366a-9ed1-ee7a87521a6b | -6.1549 | -42.6001 | 2025-07-26 01:40:00 | GOES-19 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 156.4 |
| c943af4a-5907-377e-a7f0-849c9fcddc0c | -7.2597 | -43.0645 | 2025-07-26 01:40:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 56.9 |


[Clique aqui para ver as próximas entradas](README3.md)
