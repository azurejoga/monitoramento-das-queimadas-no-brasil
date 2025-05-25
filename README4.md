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

## Dados Diários - Página 4

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 1ccd5657-d184-3775-aab4-05857a642f29 | -11.02208 | -45.14708 | 2025-05-25 03:47:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f14065c9-7830-326f-913f-520624fb57eb | -5.5808 | -43.45663 | 2025-05-25 03:47:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 0fc87205-b692-3fbb-8b9c-12026f324d11 | -7.20166 | -43.12378 | 2025-05-25 03:47:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 97122fc8-6620-391e-88f2-8f66e5f3faab | -10.74164 | -49.28745 | 2025-05-25 03:47:00 | NOAA-20 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 1374bcb7-bc5b-3646-9401-00d238102dfe | -7.27949 | -43.24954 | 2025-05-25 03:47:00 | NOAA-20 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| bde570c5-3a92-3824-9309-7eb340312374 | -10.37115 | -47.98208 | 2025-05-25 03:47:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 8d96c2fa-19fe-3c58-90a2-73d5393c472f | -7.47425 | -43.37708 | 2025-05-25 03:47:00 | NOAA-20 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 4d52be6d-e6a6-3a4c-80be-c3b142edd346 | -11.75491 | -47.25813 | 2025-05-25 03:47:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 07aa72f2-fb2d-39aa-a05f-b26479528387 | -12.37507 | -49.9847 | 2025-05-25 03:47:00 | NOAA-20 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 86661b25-125f-3567-93be-0b0b7d699885 | -12.27292 | -44.59612 | 2025-05-25 03:47:00 | NOAA-20 | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 0356e123-a99a-3862-9a6b-486e29678cc0 | -7.48381 | -43.37428 | 2025-05-25 03:47:00 | NOAA-20 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 6745a26f-1bbe-3e8d-aebd-d60ccc82750e | -6.55616 | -44.49427 | 2025-05-25 03:47:00 | NOAA-20 | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 8.3 |
| e03745bc-28f8-384a-940f-5761ee720560 | -12.37402 | -49.98974 | 2025-05-25 03:47:00 | NOAA-20 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| cef4d836-967d-3105-a565-2859323b7c25 | -12.37044 | -49.98737 | 2025-05-25 03:47:00 | NOAA-20 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 5cc90155-eb5e-396b-ac2d-84821dc0fc34 | -7.23061 | -43.11144 | 2025-05-25 03:47:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 3.1 |
| dc86d415-22c1-3139-a27e-8a9c873cb52f | -7.21542 | -43.12183 | 2025-05-25 03:47:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| be1c975d-910f-3728-a7ec-5609050a518b | -14.13487 | -41.69162 | 2025-05-25 03:47:00 | NOAA-20 | BRUMADO | BAHIA | Brasil | 2904605 | 29 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 3ee2a333-0085-3d17-98e2-874ec189e3ed | -6.95696 | -42.06327 | 2025-05-25 03:47:00 | NOAA-20 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| c6181668-ab8b-30a4-982a-c361656b5d89 | -12.27651 | -44.60146 | 2025-05-25 03:47:00 | NOAA-20 | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| db622657-38ab-3380-95e0-d6861b7a3070 | -7.21471 | -43.12601 | 2025-05-25 03:47:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| f55927bf-9d2a-3ea7-ab10-e0d3f6e6f859 | -4.28758 | -48.27262 | 2025-05-25 03:47:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| e838d474-24d9-3fca-95ba-eac82e6a1bb1 | -12.82963 | -47.38676 | 2025-05-25 03:47:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 35233711-7f10-39b8-a3fa-7599ec01b7ec | -12.83027 | -47.38348 | 2025-05-25 03:47:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 2baedda0-f2aa-3589-999a-7f06e86e391f | -11.14506 | -48.11177 | 2025-05-25 03:47:00 | NOAA-20 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 41c04776-2d00-3372-beee-baf8ccd90781 | -5.50435 | -35.59723 | 2025-05-25 03:47:00 | NOAA-20 | TAIPU | RIO GRANDE DO NORTE | Brasil | 2413904 | 24 | 33 | nan | nan | nan | Caatinga | 3.8 |
| c4ec346c-f1a9-3319-9bbe-8f78ae5d0af6 | -7.51678 | -43.36699 | 2025-05-25 03:47:00 | NOAA-20 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 8d5fc769-6ca5-332e-a0a6-9b1bbd49c40e | -5.58173 | -45.19762 | 2025-05-25 03:47:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| c586c0f7-fe2c-34dd-a1e0-1c258aa630aa | -6.8366 | -44.63327 | 2025-05-25 03:47:00 | NOAA-20 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 6e436581-4b39-3127-a994-aa93c2b2c440 | -7.21035 | -43.12527 | 2025-05-25 03:47:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 4.6 |
| de444793-2dfc-31e3-9a88-5c6a474b2b80 | -5.58122 | -43.45404 | 2025-05-25 03:47:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| b5466153-88fe-3102-b3ee-bd4d7553df51 | -6.66485 | -38.3244 | 2025-05-25 03:47:00 | NOAA-20 | SOUSA | PARAÍBA | Brasil | 2516201 | 25 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 375fa844-28e5-39f4-8a23-c9ea999e220f | -12.36782 | -49.98841 | 2025-05-25 03:47:00 | NOAA-20 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 32e74304-dd48-3168-80ce-7ff8c3d7559a | -5.68086 | -44.12411 | 2025-05-25 03:47:00 | NOAA-20 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 4d4cc7b0-6b00-3805-9839-cf4583cd2772 | -6.95236 | -42.8092 | 2025-05-25 03:47:00 | NOAA-20 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| ca1a3b95-0dc3-3951-bb14-bc666ca275eb | -11.86415 | -52.25739 | 2025-05-25 03:47:00 | NOAA-20 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 0f96ffab-a9fa-34a0-b566-903738775782 | -12.37666 | -49.98862 | 2025-05-25 03:47:00 | NOAA-20 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 038ed938-994f-31cd-9dae-052f3610e616 | -10.37684 | -47.98321 | 2025-05-25 03:47:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 959090a9-b4ad-3810-895c-f2c7159ef312 | -11.61758 | -47.99566 | 2025-05-25 03:47:00 | NOAA-20 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 9f313956-6f2e-3f32-a7fa-94cbe3fbcb34 | -7.22412 | -43.12329 | 2025-05-25 03:47:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| e92e8f54-fd88-3b11-b280-9eb39cb6262c | -7.22484 | -43.1191 | 2025-05-25 03:47:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| 5557c5fb-f4d7-3ad8-a41d-8218fb682572 | -7.20528 | -43.12872 | 2025-05-25 03:47:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 4.6 |
| 72675440-8a4b-38b2-ad54-c1ad903d4e50 | -8.06801 | -43.1314 | 2025-05-25 03:49:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 5.1 |
| 72f8e162-4599-3df2-a1cd-ba03da564027 | -8.05373 | -43.1373 | 2025-05-25 03:49:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| ace23c64-3bad-33c0-83de-4d4d54896bca | -15.37072 | -45.67965 | 2025-05-25 03:49:00 | NOAA-20 | CHAPADA GAÚCHA | MINAS GERAIS | Brasil | 3116159 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| b8499be4-767f-383b-8225-a99f9abd61ca | -17.0441 | -49.06371 | 2025-05-25 03:49:00 | NOAA-20 | BELA VISTA DE GOIÁS | GOIÁS | Brasil | 5203302 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 143e83ea-c84f-3674-9566-4130a3a0fea3 | -14.85609 | -39.34999 | 2025-05-25 03:49:00 | NOAA-20 | ITABUNA | BAHIA | Brasil | 2914802 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| 01fb45df-b0b9-336c-b405-5bf03350bb52 | -8.72854 | -47.99458 | 2025-05-25 03:49:00 | NOAA-20 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 45a3253f-df39-36bb-a153-e6c2f0aa28c5 | -19.37257 | -53.20987 | 2025-05-25 03:49:00 | NOAA-20 | PARAÍSO DAS ÁGUAS | MATO GROSSO DO SUL | Brasil | 5006275 | 50 | 33 | nan | nan | nan | Cerrado | 2.5 |
| f91b6911-578b-33e1-ae81-8ad77458184c | -19.9482 | -49.1035 | 2025-05-25 03:49:00 | NOAA-20 | FRUTAL | MINAS GERAIS | Brasil | 3127107 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 2b5928ee-4058-3a11-8d48-5a29e05a95b8 | -7.65706 | -46.1009 | 2025-05-25 03:49:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 25078d32-4a6d-3b69-a562-275eba67735a | -8.05873 | -43.13398 | 2025-05-25 03:49:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 6b75d859-9249-31cd-b8a2-fd983109d8c6 | -17.59367 | -43.19741 | 2025-05-25 03:49:00 | NOAA-20 | CARBONITA | MINAS GERAIS | Brasil | 3113503 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 703fdea4-ab31-3dc1-9051-7120998c068a | -7.64647 | -46.09915 | 2025-05-25 03:49:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| bd3983fe-4280-3d6a-9ceb-0a44cc2ca076 | -8.05445 | -43.1332 | 2025-05-25 03:49:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| dc49b7e5-e4bd-36e4-a0b1-24745f545912 | -14.85891 | -39.35059 | 2025-05-25 03:49:00 | NOAA-20 | ITABUNA | BAHIA | Brasil | 2914802 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 3f55ffb8-bafc-3dc2-b890-389c1307c04a | -8.05801 | -43.13809 | 2025-05-25 03:49:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 721d1003-9435-3718-a091-2657b7c1311c | -9.75819 | -41.8846 | 2025-05-25 03:49:00 | NOAA-20 | SENTO SÉ | BAHIA | Brasil | 2930204 | 29 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 8bcfd632-be96-310d-94f4-acb4a94271e6 | -7.65646 | -46.10423 | 2025-05-25 03:49:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 628d4068-7add-341b-a0de-e80cdd9d5975 | -8.06373 | -43.13063 | 2025-05-25 03:49:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 5.1 |
| 62321af9-7ec2-38e2-bdc2-4970b80d0605 | -8.89591 | -44.78289 | 2025-05-25 03:49:00 | NOAA-20 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 37d77e90-0e2f-3b94-b5c1-0223684f5758 | -16.47537 | -43.41903 | 2025-05-25 03:49:00 | NOAA-20 | FRANCISCO SÁ | MINAS GERAIS | Brasil | 3126703 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 3cbe45ad-2d25-3f01-a74a-e9aed6b00ed4 | -14.67285 | -52.68784 | 2025-05-25 03:49:00 | NOAA-20 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 86f5c47d-68e0-3758-9b29-94c49acd168e | -17.77998 | -42.80721 | 2025-05-25 03:49:00 | NOAA-20 | ITAMARANDIBA | MINAS GERAIS | Brasil | 3132503 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 4360bece-0c4a-3b1b-bfe3-c890bb8bfc24 | -9.76005 | -41.88196 | 2025-05-25 03:49:00 | NOAA-20 | SENTO SÉ | BAHIA | Brasil | 2930204 | 29 | 33 | nan | nan | nan | Caatinga | 2.3 |
| cd3210b8-3eaa-3b0b-85c5-6aa019c33e4c | -7.65056 | -46.10669 | 2025-05-25 03:49:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f5928549-2670-3fe4-a23e-822dd6e68dd2 | -14.67773 | -52.69081 | 2025-05-25 03:49:00 | NOAA-20 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| bc9c399b-dd9e-3db5-8eb2-3e4daa73c225 | -7.94979 | -44.87122 | 2025-05-25 03:49:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.9 |
| d49e8629-1596-3b70-a62e-fc5514a329bf | -8.0673 | -43.13553 | 2025-05-25 03:49:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 7.8 |
| c69095ed-6698-3bd0-b40d-95ae0128cb43 | -19.95261 | -49.10791 | 2025-05-25 03:49:00 | NOAA-20 | FRUTAL | MINAS GERAIS | Brasil | 3127107 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| f7b5e8d0-e247-34b2-889a-c7628c0cb2f7 | -7.65117 | -46.1033 | 2025-05-25 03:49:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 995243e1-4c8b-34ce-81b6-b7353d46c954 | -19.60208 | -45.01771 | 2025-05-25 03:49:00 | NOAA-20 | LEANDRO FERREIRA | MINAS GERAIS | Brasil | 3138302 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 696d3520-1a24-3238-96a3-3a7bcd505e93 | -7.65584 | -46.10766 | 2025-05-25 03:49:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| d86694a4-99c8-356d-8cd4-f5dda96bfc94 | -14.29128 | -43.77072 | 2025-05-25 03:49:00 | NOAA-20 | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| e1dc089a-3fda-31bf-864a-9a4d4ec708d8 | -14.68126 | -52.68279 | 2025-05-25 03:49:00 | NOAA-20 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 79ed5b55-574b-3b5d-90c0-8361356de388 | -8.0573 | -43.14222 | 2025-05-25 03:49:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 14.4 |
| 46633485-8208-3cc9-a8f0-a19a2b9fac86 | -15.37519 | -45.68058 | 2025-05-25 03:49:00 | NOAA-20 | CHAPADA GAÚCHA | MINAS GERAIS | Brasil | 3116159 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 30b0d10e-8582-3c75-9660-012115485d95 | -19.95191 | -49.11121 | 2025-05-25 03:49:00 | NOAA-20 | FRUTAL | MINAS GERAIS | Brasil | 3127107 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| fb7e968d-f7d4-30f6-841f-73aaaaaafd25 | -16.68146 | -43.88506 | 2025-05-25 03:49:00 | NOAA-20 | MONTES CLAROS | MINAS GERAIS | Brasil | 3143302 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 21aa61b2-9054-39e4-b9b4-40ad183d17d8 | -15.54004 | -47.16539 | 2025-05-25 03:49:00 | NOAA-20 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 1f5a4dea-520d-3aed-8138-7e247d74625b | -14.87769 | -47.83712 | 2025-05-25 03:49:00 | NOAA-20 | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| fc6bd464-60c9-3126-b2c5-8b02faa4d936 | -17.38545 | -42.65756 | 2025-05-25 03:49:00 | NOAA-20 | TURMALINA | MINAS GERAIS | Brasil | 3169703 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 9a973334-40aa-35f6-91d8-81d76116392d | -21.12183 | -42.95817 | 2025-05-25 03:49:00 | NOAA-20 | UBÁ | MINAS GERAIS | Brasil | 3169901 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| 5252b32f-4e95-3b9b-9b90-631cb0887b96 | -8.73016 | -47.9859 | 2025-05-25 03:49:00 | NOAA-20 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 9ae1bda5-2014-3934-9b1d-3bd056f39cfc | -20.5429 | -47.4591 | 2025-05-25 03:49:00 | NOAA-20 | FRANCA | SÃO PAULO | Brasil | 3516200 | 35 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d5022796-fe2a-391c-84f8-61721fb9135d | -9.97347 | -42.13634 | 2025-05-25 03:49:00 | NOAA-20 | SENTO SÉ | BAHIA | Brasil | 2930204 | 29 | 33 | nan | nan | nan | Caatinga | 0.4 |
| f82d7482-8adb-3374-8f8d-0925c46f3acf | -8.0794 | -43.1166 | 2025-05-25 03:49:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| af0e7cd9-720d-35fc-9511-711caa888145 | -16.14894 | -45.94552 | 2025-05-25 03:49:00 | NOAA-20 | RIACHINHO | MINAS GERAIS | Brasil | 3154457 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b4fab74f-d0ac-38c0-8575-80ec3928be66 | -8.05302 | -43.14141 | 2025-05-25 03:49:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 14.4 |
| 618752f9-fade-3f50-8f87-9f0bd2d783d0 | -15.53909 | -47.1641 | 2025-05-25 03:49:00 | NOAA-20 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 3a00f9d7-021f-3890-a502-bc647489d6b0 | -9.759 | -41.87969 | 2025-05-25 03:49:00 | NOAA-20 | SENTO SÉ | BAHIA | Brasil | 2930204 | 29 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 6b7b8a43-ff08-32b9-bb8a-17c8410705fd | -16.37466 | -46.87569 | 2025-05-25 03:49:00 | NOAA-20 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 7fcb8557-e619-3f72-879f-33cb20d499a3 | -8.72935 | -47.99025 | 2025-05-25 03:49:00 | NOAA-20 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| ad627620-32d3-3fa7-9efd-be51cc1d6eb1 | -14.67925 | -52.68414 | 2025-05-25 03:49:00 | NOAA-20 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 22062bcb-978b-3591-a3ea-ebbefecf2b1f | -14.67979 | -52.68944 | 2025-05-25 03:49:00 | NOAA-20 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 86ed3c81-cfa0-3294-83e3-a83a43db51b5 | -7.64588 | -46.10241 | 2025-05-25 03:49:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| a6a05c63-392a-357f-afa7-6737ae9903d1 | -8.07014 | -43.11913 | 2025-05-25 03:49:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 7.4 |
| b7651109-f086-3f4f-80bc-e95468b96299 | -19.9475 | -49.10676 | 2025-05-25 03:49:00 | NOAA-20 | FRUTAL | MINAS GERAIS | Brasil | 3127107 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 728c4d02-8ca4-3dc2-9efd-09f32a5fb3df | -7.66112 | -46.10863 | 2025-05-25 03:49:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| e5a9fa4d-c6bb-3ca4-92ca-deb5f07c6935 | -7.66174 | -46.10517 | 2025-05-25 03:49:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 402e30f7-8130-3954-b9bc-7efc59606394 | -8.06943 | -43.12321 | 2025-05-25 03:49:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 7.4 |


[Clique aqui para ver as próximas entradas](README5.md)
