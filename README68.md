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

## Dados Diários - Página 68

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 6f80af5f-e885-3ccd-9f32-2da05d2028fe | -10.8404 | -50.6499 | 2026-09-03 15:50:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 59.6 |
| 8006c48c-7845-3d83-9298-42a7b0ef16ae | -7.0243 | -59.2181 | 2026-09-03 15:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 45.9 |
| a7f7a07c-94a3-3faa-9fc7-9275b12409c6 | -6.8784 | -58.9343 | 2026-09-03 15:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 45.8 |
| 79a5923d-3fff-3426-ada3-763012b5acad | -17.1227 | -55.9402 | 2026-09-03 15:50:00 | GOES-19 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 66.6 |
| 52bb9672-db19-32a3-a3b9-00633479beb1 | -7.2933 | -60.5905 | 2026-09-03 15:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 42.2 |
| b82bc099-1c90-3382-80ae-5026281d99db | -3.7645 | -61.7548 | 2026-09-03 15:50:00 | GOES-19 | ANORI | AMAZONAS | Brasil | 1300102 | 13 | 33 | nan | nan | nan | Amazônia | 52.0 |
| 79015e5b-49ad-370d-a5c8-c2de83ddc5fe | -10.4334 | -49.9878 | 2026-09-03 15:50:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 67.1 |
| 806b2469-237d-3a27-99fa-727fd529ed0b | -13.4005 | -51.3756 | 2026-09-03 15:50:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 81.3 |
| f5b36831-8f1a-3c72-af50-942b462f9f66 | -10.2915 | -68.8411 | 2026-09-03 15:50:00 | GOES-19 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 81.5 |
| 842f653f-1c6b-3ce0-a30b-e9c8bccb4919 | -3.7828 | -61.7545 | 2026-09-03 15:50:00 | GOES-19 | ANORI | AMAZONAS | Brasil | 1300102 | 13 | 33 | nan | nan | nan | Amazônia | 49.3 |
| 971effa1-32c1-3999-9bd8-b3a66708e7d0 | -6.6357 | -59.4459 | 2026-09-03 15:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 205.4 |
| 1012ca7c-640e-3b74-a469-e4aa553f4004 | -8.4488 | -54.6644 | 2026-09-03 15:50:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 65.0 |
| ca7a8e36-8e1a-37cd-a065-f3a44315637d | -3.0347 | -61.4846 | 2026-09-03 15:50:00 | GOES-19 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 94.9 |
| 879c9243-7b4c-3cc8-9006-33271883b21f | -7.0428 | -59.2173 | 2026-09-03 15:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 88.6 |
| 55be6d26-73f4-3788-800c-d9204c1351c9 | -20.8377 | -57.6681 | 2026-09-03 15:50:00 | GOES-19 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Pantanal | 107.1 |
| 067eddf6-b981-308b-b857-cc843f6ef074 | -8.6853 | -62.9307 | 2026-09-03 15:50:00 | GOES-19 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 74.5 |
| 179e0c03-bcb0-3fe7-ac98-aa12548e462e | -4.1906 | -59.9443 | 2026-09-03 15:50:00 | GOES-19 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 46.9 |
| 71a5b66e-4e69-3799-9c74-95f7191ed676 | -10.3385 | -50.0191 | 2026-09-03 15:50:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 77.4 |
| 7a8c133e-9535-3f83-a3fb-07be776383c8 | -20.8633 | -57.3916 | 2026-09-03 15:50:00 | GOES-19 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 70.1 |
| 0e33bfc5-886d-33c9-9a86-3fab50b73be4 | -13.8384 | -54.0158 | 2026-09-03 15:50:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 72.4 |
| e58f6055-2276-330e-a184-7d2174a3a8d9 | -6.6013 | -59.0037 | 2026-09-03 15:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 52.4 |
| 29446f10-cd30-3784-8f9c-8bdbab7cfdcd | -6.8599 | -58.9351 | 2026-09-03 15:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 47.5 |
| 9a8695f0-277a-3834-8cad-e1e545a899f3 | -7.1123 | -42.7727 | 2026-09-03 15:50:00 | GOES-19 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 69.4 |
| 7b354045-ca67-3a07-9f67-2ec0ce1e7569 | -10.1134 | -45.8621 | 2026-09-03 15:50:00 | GOES-19 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 62.2 |
| f2f001ce-0c33-3155-a7c4-93e4038d3629 | -13.8381 | -54.0365 | 2026-09-03 15:50:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 80.1 |
| a5ebbba1-994f-3b6e-9005-256ab2db3910 | -9.4816 | -60.4131 | 2026-09-03 15:50:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 43.3 |
| 2decbbc1-e7b0-3309-bf9e-ff858a5d700d | -10.6472 | -61.7741 | 2026-09-03 15:50:00 | GOES-19 | JI-PARANÁ | RONDÔNIA | Brasil | 1100122 | 11 | 33 | nan | nan | nan | Amazônia | 107.3 |
| 13914783-f3a3-3ff4-9fa0-a3793c8ed623 | -3.6216 | -60.547 | 2026-09-03 15:50:00 | GOES-19 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 76.9 |
| d2673ee1-8a50-35e4-8dd0-3de54d74c21c | -13.4009 | -51.3542 | 2026-09-03 15:50:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 53.3 |
| 2d7ee5a3-639d-3438-ae27-a6304b884aff | -7.0058 | -59.2382 | 2026-09-03 15:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 68.4 |
| d9e30aec-3af6-3e6b-907d-6cdcf9997c97 | -1.4752 | -54.8157 | 2026-09-03 15:50:00 | GOES-19 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 72.4 |
| 68c2d096-b3cc-34c5-8e88-8e62df6a00ef | -9.4813 | -60.4516 | 2026-09-03 15:50:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 70.4 |
| 87df480a-7fac-39f3-9b3a-1661cc2eb03f | -6.8203 | -59.4001 | 2026-09-03 15:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 69.3 |
| a31afa6e-b3fc-350c-8951-79ba5c107157 | -3.1266 | -61.2 | 2026-09-03 15:50:00 | GOES-19 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 53.3 |
| d958f857-d6a2-33ef-937a-ee1a8b46db3b | -7.0242 | -59.2374 | 2026-09-03 15:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 77.6 |
| 00f432e5-e814-34e5-9bba-a581e749a12c | -6.6542 | -59.426 | 2026-09-03 15:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 78.9 |
| 6fdfa1a6-fee4-381c-810d-228ca878b974 | -9.6839 | -48.1386 | 2026-09-03 15:50:00 | GOES-19 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 66.0 |
| ebd2ea62-a880-3c61-90a6-9730f77bbcff | -3.3321 | -59.4469 | 2026-09-03 15:50:00 | GOES-19 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 70.0 |
| 2433b585-cf14-3d76-ab88-a7b2cfe328f0 | -11.2106 | -51.2688 | 2026-09-03 15:50:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 79.9 |
| 6dda2880-33f0-3438-ab23-04f4f855d426 | -8.7613 | -62.5869 | 2026-09-03 15:50:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 51.2 |
| 399c752f-b8de-3b4b-877e-0127261c1025 | -10.2403 | -50.307 | 2026-09-03 15:50:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 72.5 |
| 1248cbac-05c3-3973-ac9c-b37ec469ccef | -8.3718 | -62.697 | 2026-09-03 15:50:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 43.4 |
| ec75272d-1c33-3fc8-8005-00e23db3bed2 | -15.4429 | -52.681 | 2026-09-03 15:50:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 39.7 |
| e17ad494-96e5-3bf4-914a-93844993de1d | -10.3583 | -49.9528 | 2026-09-03 15:50:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 82.4 |
| b095bb8a-8159-32a6-a917-429b4f1e33f3 | -3.0164 | -61.4848 | 2026-09-03 15:50:00 | GOES-19 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 130.7 |
| 1bffa6cf-2f47-37d9-be72-df5a71c529ca | -7.5326 | -60.7147 | 2026-09-03 15:50:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 73.4 |
| 7b467fe2-b365-3965-a5a3-281900487882 | -9.4345 | -45.6477 | 2026-09-03 15:50:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 78.9 |
| 63d35d04-c0bb-33c3-b57a-e40b25531af8 | -5.9819 | -57.6892 | 2026-09-03 15:50:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 47.4 |
| 47742a7b-2b6c-3c83-9958-087a7b59909c | -10.7649 | -50.6366 | 2026-09-03 15:50:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 103.6 |
| ff2304ae-7139-3d0f-be1e-8b487e76761b | -3.1462 | -60.6506 | 2026-09-03 15:50:00 | GOES-19 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 53.7 |
| 006b6ca4-56fd-3153-a72e-cea8d83528a2 | -8.5728 | -63.1807 | 2026-09-03 15:50:00 | GOES-19 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 45.7 |
| 50226958-6b0b-3445-a7fc-5f9550b66462 | -19.1547 | -57.3562 | 2026-09-03 15:50:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 104.7 |
| bbce2026-e661-37de-a053-cfa77cb04744 | -10.547 | -49.9758 | 2026-09-03 15:50:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 70.7 |
| 7b9f9eae-05cd-344f-baa4-93f3fce6ce53 | -3.1815 | -61.1613 | 2026-09-03 15:50:00 | GOES-19 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 85.8 |
| b6297956-5a4e-3ae2-a17e-c8f5044ffe1d | -13.6817 | -51.7872 | 2026-09-03 15:50:00 | GOES-19 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 69.5 |
| 924bb609-eb5a-3372-a4c3-5fc5efcc62bb | -17.0878 | -56.8534 | 2026-09-03 15:50:00 | GOES-19 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 166.5 |
| 992c7f32-ef9f-3780-aea6-b5bf76f673a7 | -8.6854 | -62.9118 | 2026-09-03 15:50:00 | GOES-19 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 48.0 |
| 868a3b6e-9d9c-383d-a302-c67e9e3ffbfd | -20.8174 | -57.6709 | 2026-09-03 15:50:00 | GOES-19 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Pantanal | 118.6 |
| 4e3668d9-d5f6-37eb-a9b7-17878dfdd8b9 | -8.5542 | -63.1814 | 2026-09-03 15:50:00 | GOES-19 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 50.8 |
| 0d298d15-765f-3e18-9c03-50a540e12e8a | -7.3118 | -60.5897 | 2026-09-03 15:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 69.4 |
| 089bd79c-c863-3962-82fb-7092dc71497f | -3.6232 | -54.5931 | 2026-09-03 15:50:00 | GOES-19 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 82.6 |
| 467bc42e-890b-303a-b5fd-ec8a3b16d6f6 | -19.1347 | -57.3589 | 2026-09-03 15:50:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 101.6 |
| e589c2a5-2978-39d2-bd7e-9055c35d179b | -6.6226 | -58.4995 | 2026-09-03 15:50:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 44.3 |
| 9e20eee5-96f4-38c9-b23a-b64882b6dec1 | -6.7675 | -45.1188 | 2026-09-03 15:50:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 49.5 |
| b282de3f-1291-34c0-b832-5e90295092e8 | -14.4201 | -52.5201 | 2026-09-03 15:50:00 | GOES-19 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 63.1 |
| 88db6d1b-b83e-31f5-b3f0-2f52ed1dc326 | -6.6358 | -59.4267 | 2026-09-03 15:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 60.8 |
| d01de014-cbf9-38fe-9abd-16e08b46ad8a | -17.0875 | -56.874 | 2026-09-03 15:50:00 | GOES-19 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 69.1 |
| 3443c113-685c-30b6-a0b2-9fbd3e1ed592 | -9.4814 | -60.4324 | 2026-09-03 15:50:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 65.5 |
| 3a2d257a-ea7b-328b-8bb3-0ff458b7ad6b | -7.3117 | -60.6089 | 2026-09-03 15:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 73.5 |
| ad5b8a48-e8b0-3325-a4dd-6abbdbc7e8dd | -8.7599 | -62.8332 | 2026-09-03 15:50:00 | GOES-19 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 40.9 |
| 80a181b6-7112-3d53-961e-ecc05a1dba0f | -7.2006 | -60.6706 | 2026-09-03 15:50:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 51.5 |
| b51ade98-3d5f-39d7-b4a2-cd946a3f4bc0 | -10.5278 | -49.9993 | 2026-09-03 15:50:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 87.4 |
| 1277761b-a1cc-3ed0-9a4e-e71c0508450e | -14.4645 | -52.1751 | 2026-09-03 15:50:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 53.4 |
| 5eef1a94-a043-3337-a46e-70a756fbf500 | -3.1267 | -61.1811 | 2026-09-03 15:50:00 | GOES-19 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 64.3 |
| ed28f4be-a49d-3f6b-a5a1-b6589ec94508 | -3.4002 | -61.3276 | 2026-09-03 15:50:00 | GOES-19 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 59.0 |
| fa72e9de-28aa-3976-a154-60cc5fd89f84 | -11.2298 | -51.2456 | 2026-09-03 15:50:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 62.2 |
| 056c78de-0483-33d4-8f06-bd1c4e9c3992 | -14.2989 | -51.7072 | 2026-09-03 15:50:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 79.9 |
| bd4a1f76-6bd1-3e92-8bf9-649a13c4b51a | -10.5278 | -49.9993 | 2026-09-03 16:00:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 91.0 |
| 9ae616dc-7161-3ef1-b4d7-b4c77ffde1b2 | -17.0878 | -56.8534 | 2026-09-03 16:00:00 | GOES-19 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 237.0 |
| fde1b7ac-3a7e-3cd4-ba22-b6b77298727b | -5.9451 | -57.6906 | 2026-09-03 16:00:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 54.2 |
| e1006599-4813-34f5-99aa-533d683f5b01 | -19.1347 | -57.3589 | 2026-09-03 16:00:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 152.3 |
| 41196a36-83f3-3eaf-b583-0364452ea5bd | -11.2295 | -51.2667 | 2026-09-03 16:00:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 70.0 |
| 56deb386-3a12-31f4-9964-58c69b85a10e | -19.1547 | -57.3562 | 2026-09-03 16:00:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 126.9 |
| f9ecdc0d-c57a-31c1-8e85-0e517fa10432 | -6.7123 | -58.9412 | 2026-09-03 16:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 75.2 |
| 7908a4a8-5ee7-31f5-894d-41bf9438206e | -3.0721 | -61.0685 | 2026-09-03 16:00:00 | GOES-19 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 63.7 |
| 9648a5bc-46c8-37ff-b5e3-05408010e06c | -3.1815 | -61.1424 | 2026-09-03 16:00:00 | GOES-19 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 70.7 |
| e52f906d-5138-3474-9e20-45b79b53127d | -8.9428 | -63.2797 | 2026-09-03 16:00:00 | GOES-19 | ITAPUÃ DO OESTE | RONDÔNIA | Brasil | 1101104 | 11 | 33 | nan | nan | nan | Amazônia | 51.2 |
| 521d7e75-c4f9-3208-acbc-96d4a4a6e2d4 | -8.4488 | -54.6644 | 2026-09-03 16:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 65.1 |
| 9f3fce26-1bb1-3512-abce-0f58e4ef5095 | -8.5542 | -63.1814 | 2026-09-03 16:00:00 | GOES-19 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 48.8 |
| 2239468f-16f9-335a-b367-49f9e4596c7c | -10.1087 | -50.2776 | 2026-09-03 16:00:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 77.4 |
| 47574f48-d975-3be2-b23e-14ab1b52202d | -4.1906 | -59.9443 | 2026-09-03 16:00:00 | GOES-19 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 53.5 |
| 9b28d838-fd1f-385d-956a-a0d05b6ad8f4 | -7.0058 | -59.2382 | 2026-09-03 16:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 65.3 |
| efaab26c-7f96-305e-956f-9de70742df04 | -13.6817 | -51.7872 | 2026-09-03 16:00:00 | GOES-19 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 68.1 |
| 7cf62196-75fb-35d8-bd30-2e6ca44ed575 | -13.681 | -51.8298 | 2026-09-03 16:00:00 | GOES-19 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 58.9 |
| 9fa9d6fd-31b5-33a0-90be-2e3351aa2ea4 | -8.6667 | -62.9314 | 2026-09-03 16:00:00 | GOES-19 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 49.5 |
| a1b9995c-f4e8-32a3-8235-72764a1247b3 | -3.3872 | -59.3692 | 2026-09-03 16:00:00 | GOES-19 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 75.4 |
| 1b43e09d-fec1-3932-9e79-b1c630f2227c | -8.7613 | -62.5869 | 2026-09-03 16:00:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 55.5 |
| 068a775e-f1fa-34c5-8dfb-6b0302253d0a | -19.1147 | -57.3615 | 2026-09-03 16:00:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 79.6 |
| 2d4c802a-8c88-3e98-8924-1bcbd4f68769 | -6.6358 | -59.4267 | 2026-09-03 16:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 62.2 |
| 4a5ae619-03b8-3d74-800d-44d615a8567a | -13.4002 | -51.3969 | 2026-09-03 16:00:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 60.1 |


[Clique aqui para ver as próximas entradas](README69.md)
