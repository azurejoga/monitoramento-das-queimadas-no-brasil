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

## Dados Diários - Página 70

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| e477215c-02bf-3d95-9789-b6b7972760f7 | -10.6473 | -61.7549 | 2026-09-03 16:10:00 | GOES-19 | JI-PARANÁ | RONDÔNIA | Brasil | 1100122 | 11 | 33 | nan | nan | nan | Amazônia | 90.7 |
| 62978107-1a36-3b23-8468-32450524f8fe | -20.8174 | -57.6709 | 2026-09-03 16:10:00 | GOES-19 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Pantanal | 218.6 |
| b7248dd5-d2f3-38cd-9250-98ddcb2f6d87 | -20.8377 | -57.6681 | 2026-09-03 16:10:00 | GOES-19 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Pantanal | 129.9 |
| ae131214-2a3e-32cf-b45c-8c41990c5300 | -3.1462 | -60.6506 | 2026-09-03 16:10:00 | GOES-19 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 66.4 |
| 1dd9deee-03f9-3ee4-bf2b-a164c48f1d00 | -6.7507 | -58.6687 | 2026-09-03 16:10:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 41.5 |
| e0fea407-7d5a-3bbd-8be2-28d167eadeef | -3.2181 | -61.1418 | 2026-09-03 16:10:00 | GOES-19 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 52.8 |
| 74fa3b05-15c2-3a2f-9688-28eb2137ad3f | -8.5541 | -63.2003 | 2026-09-03 16:10:00 | GOES-19 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 61.9 |
| d65f784b-09de-380a-a58b-943b6aecafc5 | -14.4846 | -52.1299 | 2026-09-03 16:10:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 67.0 |
| 4b8c10ab-126a-3535-b526-2c65bd12bc17 | -11.2298 | -51.2456 | 2026-09-03 16:10:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 60.2 |
| bc5131c0-55dc-32fe-8578-d3826c8a32e7 | -10.6472 | -61.7741 | 2026-09-03 16:10:00 | GOES-19 | JI-PARANÁ | RONDÔNIA | Brasil | 1100122 | 11 | 33 | nan | nan | nan | Amazônia | 123.1 |
| 005edc6e-e17a-341f-a600-c242691e7b49 | -6.6542 | -59.426 | 2026-09-03 16:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 128.0 |
| 8a0285c6-8599-3a38-92df-35c50718e914 | -3.6215 | -60.585 | 2026-09-03 16:10:00 | GOES-19 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 81.6 |
| ebf19d6f-64d0-3656-9862-42072cf39bb5 | -8.6667 | -62.9314 | 2026-09-03 16:10:00 | GOES-19 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 39.3 |
| d5530674-2bf7-36c1-a89c-66d3706a04e3 | -12.0101 | -60.515 | 2026-09-03 16:10:00 | GOES-19 | PIMENTA BUENO | RONDÔNIA | Brasil | 1100189 | 11 | 33 | nan | nan | nan | Amazônia | 52.3 |
| 26c91d15-bad5-323e-9366-3e2681ec71c5 | -10.1087 | -50.2776 | 2026-09-03 16:10:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 78.9 |
| 66a77623-4d91-3109-9615-06be21f81d96 | -3.1998 | -61.1421 | 2026-09-03 16:10:00 | GOES-19 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 60.8 |
| cb4427dc-bb65-3e8b-89e9-752fbf1aabe8 | -6.6925 | -62.8493 | 2026-09-03 16:10:00 | GOES-19 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 46.2 |
| 46351ad9-4124-36e1-9549-4a0fb71bfb06 | -8.5727 | -63.1996 | 2026-09-03 16:10:00 | GOES-19 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 57.4 |
| 44f2bbc9-d5d9-3c06-a52e-3d87c75e44c7 | -6.7123 | -58.9412 | 2026-09-03 16:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 73.9 |
| 464c11fe-d789-3d08-9b08-c2bee046ed72 | -6.6358 | -59.4267 | 2026-09-03 16:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 74.6 |
| f451b49b-7cfa-396c-be28-af0c4c1dae14 | -3.0164 | -61.4848 | 2026-09-03 16:10:00 | GOES-19 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 156.5 |
| 3bd68457-bf51-3b00-869f-b540e117635c | -9.4814 | -60.4324 | 2026-09-03 16:10:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 70.4 |
| 7f3dd739-ed86-3340-9fdc-72eeb888e838 | -7.2933 | -60.5905 | 2026-09-03 16:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 44.2 |
| 2d3ae345-cd34-3a1c-8b05-bad8e4e62d90 | -14.2755 | -51.9447 | 2026-09-03 16:10:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 64.4 |
| 90a1b937-67f4-3e41-98dc-1e9bf928c5cc | -5.9635 | -57.6899 | 2026-09-03 16:10:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 76.7 |
| 33a54b49-c2fa-388e-a37a-7c2b5d457bd9 | -10.547 | -49.9758 | 2026-09-03 16:10:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 67.3 |
| 16b78416-4b68-3091-843f-dc08ce570442 | -9.22 | -43.28 | 2026-09-03 16:15:00 | MSG-03 | CARACOL | PIAUÍ | Brasil | 2202505 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 2df11755-2af8-3bb3-ab44-eea8f167fdd3 | -3.7533 | -59.3231 | 2026-09-03 16:20:00 | GOES-19 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 76.7 |
| a14cca7c-8699-3bc3-a4eb-06fe2834194f | -17.0878 | -56.8534 | 2026-09-03 16:20:00 | GOES-19 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 149.4 |
| 073facc8-1779-3d71-a8b7-3573b57e0d91 | -8.8371 | -62.3181 | 2026-09-03 16:20:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 39.2 |
| c7fd412e-d550-32ce-bdd2-72441e2e1be8 | -7.5326 | -60.7147 | 2026-09-03 16:20:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 69.9 |
| f078ef75-c786-36e5-823a-1009a621f018 | -3.1449 | -61.1997 | 2026-09-03 16:20:00 | GOES-19 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 53.5 |
| e4641ee4-06a3-375d-a1de-d46983337368 | -6.6013 | -59.0037 | 2026-09-03 16:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 58.1 |
| a6bba62e-bd60-3a9f-acf0-0ab53d6ac027 | -6.9872 | -59.2582 | 2026-09-03 16:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 62.1 |
| da162daf-317b-36bc-9504-19a994243555 | -11.2298 | -51.2456 | 2026-09-03 16:20:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 38.5 |
| e187619b-c3b2-372b-8f72-879f3744f107 | -3.7828 | -61.7545 | 2026-09-03 16:20:00 | GOES-19 | ANORI | AMAZONAS | Brasil | 1300102 | 13 | 33 | nan | nan | nan | Amazônia | 49.7 |
| 93532274-43ad-3984-b830-81970901abb4 | -8.6854 | -62.9118 | 2026-09-03 16:20:00 | GOES-19 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 61.5 |
| bb35c512-6682-3666-94cd-8545d95fd367 | -3.7645 | -61.7548 | 2026-09-03 16:20:00 | GOES-19 | ANORI | AMAZONAS | Brasil | 1300102 | 13 | 33 | nan | nan | nan | Amazônia | 62.2 |
| c0fb6554-56e7-394e-aa12-45973c35c683 | -3.0347 | -61.4657 | 2026-09-03 16:20:00 | GOES-19 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 49.7 |
| a857950b-c371-3fc4-ae92-8851299a3345 | -1.4394 | -54.2169 | 2026-09-03 16:20:00 | GOES-19 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 80.5 |
| d023b6aa-7fc5-3e6a-b423-4ba2b0334fa0 | -7.3118 | -60.5897 | 2026-09-03 16:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 66.8 |
| 125d7692-030c-3aee-a7e9-04631e3bf0c6 | -3.1449 | -61.1808 | 2026-09-03 16:20:00 | GOES-19 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 61.2 |
| 5639a73e-3636-3f94-a3bb-ab666dbc107f | -3.4003 | -61.3087 | 2026-09-03 16:20:00 | GOES-19 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 69.1 |
| aafd44a5-aaea-3f46-bea6-20cecac16890 | -8.5542 | -63.1814 | 2026-09-03 16:20:00 | GOES-19 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 53.9 |
| 8fec3968-8144-3f6a-98ee-62b6015042de | -19.1547 | -57.3562 | 2026-09-03 16:20:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 87.9 |
| 4f613816-0db7-36a1-8430-9fbf91d9a9cc | -9.4813 | -60.4516 | 2026-09-03 16:20:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 90.1 |
| be7181aa-b519-33e0-90c6-9774e9898b7c | -10.1324 | -45.8598 | 2026-09-03 16:20:00 | GOES-19 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 59.8 |
| a5e0871e-2947-3520-919a-06a2bbd36d05 | -3.1998 | -61.161 | 2026-09-03 16:20:00 | GOES-19 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 83.3 |
| ac99f6c7-d54f-3380-a57d-344237a3593f | -19.0948 | -57.3641 | 2026-09-03 16:20:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 70.9 |
| bffebd96-ddbc-3b5d-ad26-1c51fc901742 | -5.9635 | -57.6899 | 2026-09-03 16:20:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 80.9 |
| a82142cd-2b8e-3e10-bcc1-ff748fc395b7 | -13.4519 | -57.039 | 2026-09-03 16:20:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Cerrado | 62.7 |
| ea641ed4-4025-3c75-8bd4-49edfc592673 | -6.7123 | -58.9412 | 2026-09-03 16:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 78.8 |
| c5f82121-149e-3e11-9820-0f7785b46c9e | -5.9451 | -57.6906 | 2026-09-03 16:20:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 54.9 |
| 8e9779a6-8a16-3fb9-bd27-9539b13181d7 | -3.1462 | -60.6506 | 2026-09-03 16:20:00 | GOES-19 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 64.7 |
| bb810898-ccb1-3090-8ca3-8d0bf16a8d10 | -20.8573 | -57.7072 | 2026-09-03 16:20:00 | GOES-19 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Pantanal | 78.7 |
| 0c12403f-680b-3309-9d28-2c8a8b8ecd6a | -6.6929 | -59.0966 | 2026-09-03 16:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 56.2 |
| 34c8c605-4433-38d6-8462-f62e444a03ab | -11.2295 | -51.2667 | 2026-09-03 16:20:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 72.3 |
| 04e19c62-ebf5-3761-8b35-8fbe60f6a925 | -14.4835 | -52.1938 | 2026-09-03 16:20:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 61.2 |
| 5899d562-969f-3cb1-bde1-8ad10605742f | -10.7274 | -50.6192 | 2026-09-03 16:20:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 54.8 |
| 27a40093-7663-3fec-96ff-32ce81f488ee | -3.2181 | -61.1418 | 2026-09-03 16:20:00 | GOES-19 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 110.0 |
| 1e024915-07f3-37e5-831e-aada11ef54dd | -3.1084 | -61.1814 | 2026-09-03 16:20:00 | GOES-19 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 48.0 |
| 07f8f5b5-5e8a-35fc-9c6a-ec497c694b5f | -9.12 | -61.6011 | 2026-09-03 16:20:00 | GOES-19 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 48.0 |
| bdd3a5ad-c35c-32cb-a861-76995f928934 | -7.272 | -61.1067 | 2026-09-03 16:20:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 52.9 |
| 15780a56-bede-3e40-8f3d-9e290ad81518 | -3.1267 | -61.1811 | 2026-09-03 16:20:00 | GOES-19 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 75.9 |
| 9a8554cc-9387-3081-9d53-53d5e0a9f406 | -3.3321 | -59.4469 | 2026-09-03 16:20:00 | GOES-19 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 87.8 |
| 4bdc7933-a7e5-3d52-a6e1-686a16898029 | -15.2866 | -53.8617 | 2026-09-03 16:20:00 | GOES-19 | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 115.5 |
| a9515dc2-c58f-3bdc-89ae-8fc105f96d7f | -19.1347 | -57.3589 | 2026-09-03 16:20:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 96.7 |
| 8a6d3665-681b-31de-8bb6-404fcaf05eaa | -10.6472 | -61.7741 | 2026-09-03 16:20:00 | GOES-19 | JI-PARANÁ | RONDÔNIA | Brasil | 1100122 | 11 | 33 | nan | nan | nan | Amazônia | 131.7 |
| 278709e3-8a29-36ff-a9ad-d748bc19ee13 | -6.7453 | -59.6341 | 2026-09-03 16:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 60.9 |
| 746dcfb3-4379-3415-a5bb-6df5d6a4ebe6 | -12.0705 | -64.7721 | 2026-09-03 16:20:00 | GOES-19 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 36.8 |
| 3aacef2b-717d-3207-880d-b951bdf18cfb | -8.5541 | -63.2003 | 2026-09-03 16:20:00 | GOES-19 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 54.1 |
| 21bfbdc5-90d0-3868-af88-f5b41d56a366 | -8.6852 | -62.9496 | 2026-09-03 16:20:00 | GOES-19 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 42.1 |
| 28e4368b-5d4e-363d-92c1-66ff62965a9e | -3.0164 | -61.4848 | 2026-09-03 16:20:00 | GOES-19 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 148.6 |
| 2a5a3ec8-72a0-3d2d-aef6-0a0eda977542 | -9.4814 | -60.4324 | 2026-09-03 16:20:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 68.6 |
| 10b128f0-42bb-3b2e-b450-173b5c0a4f06 | -3.3872 | -59.3692 | 2026-09-03 16:20:00 | GOES-19 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 73.2 |
| edf11d9e-919f-36b5-ab73-34ff2791c9f5 | -3.6215 | -60.585 | 2026-09-03 16:20:00 | GOES-19 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 82.1 |
| f77367d3-3cbb-3ea2-b00f-eb3e10ca7228 | -19.1147 | -57.3615 | 2026-09-03 16:20:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 157.0 |
| e502e9d9-8bd0-3c48-9c45-d22293e9b592 | -20.8174 | -57.6709 | 2026-09-03 16:20:00 | GOES-19 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Pantanal | 97.9 |
| 8340aa78-d4db-36ed-95f7-120cc1dec1f6 | -14.2369 | -51.9498 | 2026-09-03 16:20:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 62.6 |
| 6a291541-b7ff-36f0-9b9f-ce337c720f93 | -9.4812 | -60.4709 | 2026-09-03 16:20:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 48.3 |
| cbc44f98-b8d1-39c7-8465-87a3a10abe62 | -7.2933 | -60.5905 | 2026-09-03 16:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 43.4 |
| 9971f95c-a1e1-3189-94f5-075c548aebf7 | -3.4002 | -61.3276 | 2026-09-03 16:20:00 | GOES-19 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 80.0 |
| bdf5e46b-7c9f-33f2-ae50-32a76cde477b | -10.547 | -49.9758 | 2026-09-03 16:20:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 68.9 |
| 3f8435b7-93c1-3148-8006-5caccc1d8f33 | -6.6925 | -62.8493 | 2026-09-03 16:20:00 | GOES-19 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 55.4 |
| 07501f72-37d9-3261-8494-93f179e1b9f5 | -15.287 | -53.8407 | 2026-09-03 16:20:00 | GOES-19 | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 93.6 |
| 7d9f651f-79cc-3614-9d63-c337ded87e3a | -10.6473 | -61.7549 | 2026-09-03 16:20:00 | GOES-19 | JI-PARANÁ | RONDÔNIA | Brasil | 1100122 | 11 | 33 | nan | nan | nan | Amazônia | 98.9 |
| 6a3ae67f-6605-3f69-a09b-6776e1a1e9a5 | -10.5793 | -50.3789 | 2026-09-03 16:20:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 56.0 |
| 52341173-bbcf-3670-9beb-e48be9f64f19 | -19.1144 | -57.3823 | 2026-09-03 16:20:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 121.5 |
| 8ece3d72-5c66-3082-bd5b-fad52f709558 | -2.4836 | -54.8997 | 2026-09-03 16:20:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 58.8 |
| f06f1538-04ce-3b1e-97f6-722d1359fe78 | -20.8377 | -57.6681 | 2026-09-03 16:20:00 | GOES-19 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Pantanal | 95.5 |
| 374aadba-e61b-3fec-861a-2d64a877b06a | -6.7123 | -58.9412 | 2026-09-03 16:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 79.1 |
| fa1b1444-185c-37c7-98a2-a14713635206 | -7.5326 | -60.7147 | 2026-09-03 16:30:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 59.5 |
| 7bec13f1-54c1-364a-ab1b-e66a63e0d2fa | -13.4137 | -57.0426 | 2026-09-03 16:30:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Cerrado | 60.7 |
| 517966b8-5dac-3978-8120-fc82bbd704e0 | -5.9451 | -57.6906 | 2026-09-03 16:30:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 59.5 |
| 31fe7212-34f5-3871-966e-9ea6a99f7507 | -6.6226 | -58.4995 | 2026-09-03 16:30:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 43.4 |
| 43610eb8-c224-39a9-921a-33c05cde04dd | -6.6727 | -59.4252 | 2026-09-03 16:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 50.0 |
| db48447a-0a16-3441-ab0d-403ff4be4d3b | -3.6216 | -60.547 | 2026-09-03 16:30:00 | GOES-19 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 75.4 |
| c15b462b-eef4-3621-a75e-ff106c6038dc | -15.2672 | -53.8642 | 2026-09-03 16:30:00 | GOES-19 | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 67.3 |
| 3d93ebb2-0137-349c-b43d-80188909efe1 | -12.1711 | -50.5432 | 2026-09-03 16:30:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 56.2 |
| e90345cb-0e8b-3a6a-8f29-ce19f90de479 | -19.1347 | -57.3589 | 2026-09-03 16:30:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 97.8 |


[Clique aqui para ver as próximas entradas](README71.md)
