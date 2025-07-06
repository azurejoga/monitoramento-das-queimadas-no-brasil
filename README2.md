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
| 58b37bb5-8de9-3b99-a0fe-f9854475666f | -12.0266 | -57.0845 | 2025-07-06 03:00:00 | GOES-19 | ITANHANGÁ | MATO GROSSO | Brasil | 5104542 | 51 | 33 | nan | nan | nan | Amazônia | 61.1 |
| 424671cb-bc2f-3aac-9445-9f0a3639172d | -11.4588 | -45.0895 | 2025-07-06 03:00:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 50.6 |
| 577a6852-f262-314d-a02e-d022a358892b | -12.0266 | -57.0845 | 2025-07-06 03:10:00 | GOES-19 | ITANHANGÁ | MATO GROSSO | Brasil | 5104542 | 51 | 33 | nan | nan | nan | Amazônia | 59.7 |
| fd104709-eea2-35a0-b4d0-8ebd957a29f9 | -11.4584 | -45.1126 | 2025-07-06 03:10:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 63.2 |
| 01300581-45ac-3678-ab17-9157eacefa67 | -11.4588 | -45.0895 | 2025-07-06 03:10:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 81.6 |
| 76c5a056-dad2-338c-b32d-b158070be4f1 | -16.68232 | -43.88327 | 2025-07-06 03:15:00 | NOAA-21 | MONTES CLAROS | MINAS GERAIS | Brasil | 3143302 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| afa25c49-a5a1-36b2-8110-cc3b6cf7e970 | -16.42855 | -42.18267 | 2025-07-06 03:15:00 | NOAA-21 | RUBELITA | MINAS GERAIS | Brasil | 3156502 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.8 |
| f22ab2d9-afdb-308b-afa8-bd4787ed615e | -21.32487 | -44.24225 | 2025-07-06 03:17:00 | NOAA-21 | SÃO JOÃO DEL REI | MINAS GERAIS | Brasil | 3162500 | 31 | 33 | nan | nan | nan | Mata Atlântica | 15.8 |
| 07099e27-56c0-3372-b10a-20cb778cd29e | -12.0266 | -57.0845 | 2025-07-06 03:20:00 | GOES-19 | ITANHANGÁ | MATO GROSSO | Brasil | 5104542 | 51 | 33 | nan | nan | nan | Amazônia | 65.6 |
| fc74ce0c-a0f7-3e35-8a25-19f7afc5f748 | -11.4584 | -45.1126 | 2025-07-06 03:20:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 51.8 |
| f03ae10c-2c74-3eb9-bde3-4a19a9cda080 | -11.4588 | -45.0895 | 2025-07-06 03:20:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 70.9 |
| 233263c0-8253-3b11-a55a-bc4d853da2cb | -12.0266 | -57.0845 | 2025-07-06 03:30:00 | GOES-19 | ITANHANGÁ | MATO GROSSO | Brasil | 5104542 | 51 | 33 | nan | nan | nan | Amazônia | 52.7 |
| e680557d-e11e-3ce1-9ec6-3462e1547d0e | -11.4584 | -45.1126 | 2025-07-06 03:30:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 51.0 |
| 9f07ea49-6d9e-3372-a46b-149f3558e3b9 | -11.4588 | -45.0895 | 2025-07-06 03:30:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 52.8 |
| b1911b21-ed39-3bc2-b357-8d4dea8e5d13 | -3.50617 | -43.24624 | 2025-07-06 03:36:00 | NPP-375D | ANAPURUS | MARANHÃO | Brasil | 2100808 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| b6013012-6761-3f51-857d-0d4252cc0676 | -3.3033 | -42.65614 | 2025-07-06 03:36:00 | NPP-375D | SANTANA DO MARANHÃO | MARANHÃO | Brasil | 2110237 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 6bc22cf5-c5f5-3144-94ae-91b724d2b6e0 | -3.81242 | -42.5478 | 2025-07-06 03:36:00 | NPP-375D | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 4752c025-bcfa-3e17-abc3-3e9c0b37b92e | -3.30888 | -42.65714 | 2025-07-06 03:36:00 | NPP-375D | SANTANA DO MARANHÃO | MARANHÃO | Brasil | 2110237 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a94ce67c-2eca-340e-b563-bf7dab1f7680 | -3.50548 | -43.25025 | 2025-07-06 03:36:00 | NPP-375D | ANAPURUS | MARANHÃO | Brasil | 2100808 | 21 | 33 | nan | nan | nan | Cerrado | 9.6 |
| 387b36e6-6d2f-362a-abfb-a08f27533510 | -3.5004 | -43.2452 | 2025-07-06 03:36:00 | NPP-375D | ANAPURUS | MARANHÃO | Brasil | 2100808 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 1643bb54-4c21-3817-bd2e-8420428e2bc6 | -2.91911 | -41.3955 | 2025-07-06 03:36:00 | NPP-375D | CAJUEIRO DA PRAIA | PIAUÍ | Brasil | 2202083 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 4840394a-985d-3267-b399-e1468ae8bc90 | -2.87705 | -40.30053 | 2025-07-06 03:36:00 | NPP-375D | CRUZ | CEARÁ | Brasil | 2304251 | 23 | 33 | nan | nan | nan | Caatinga | 4.5 |
| 604c786a-499e-3fbc-addf-7cb83649cee0 | -3.81302 | -42.5442 | 2025-07-06 03:36:00 | NPP-375D | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 6dca8486-f15d-3ed1-861f-52327c54d46a | -7.2072 | -43.12514 | 2025-07-06 03:38:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 331f7bbd-299c-3bd2-b739-b6458419bcc5 | -6.85129 | -42.80111 | 2025-07-06 03:38:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 8e7edf5c-1f82-3a55-bc49-881a4658ccd8 | -7.20596 | -43.13205 | 2025-07-06 03:38:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 3.5 |
| cf04d465-4954-3ab0-9443-0c273a90c84a | -7.20658 | -43.12857 | 2025-07-06 03:38:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 3.5 |
| ac6281ba-e8d3-332b-993a-231907f08f2d | -5.57042 | -45.21328 | 2025-07-06 03:38:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 9.0 |
| 65af20de-9f01-3e7a-8b98-a10b235dfdb5 | -5.59901 | -45.18584 | 2025-07-06 03:38:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 16df31e0-5344-3970-a19c-75d874d3d5d8 | -9.09263 | -47.96677 | 2025-07-06 03:38:00 | NPP-375D | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 7c08ec3a-559a-3040-9e99-bc2c65038aba | -6.93657 | -42.80422 | 2025-07-06 03:38:00 | NPP-375D | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 51e4cfa5-abc0-3dd7-83c8-328838ff2c51 | -7.08681 | -44.39117 | 2025-07-06 03:38:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 5ab3a7b3-3b5c-3f30-87f0-c58d11a43a07 | -7.19516 | -43.13011 | 2025-07-06 03:38:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| bea2ecad-f89e-3cbc-a8d8-683058f4460e | -5.60669 | -45.19366 | 2025-07-06 03:38:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |
| ba20d46a-4e4d-3cca-ad78-e2e533c5dbc1 | -10.65123 | -44.49072 | 2025-07-06 03:38:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 2f9b3c41-0a66-3d94-b6f5-b985cf5b05e3 | -5.6071 | -45.17686 | 2025-07-06 03:38:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| ec34b2b7-8f26-32d0-8258-0bbb4a306c71 | -5.60443 | -45.19207 | 2025-07-06 03:38:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| e868911a-b6f5-3c2a-8ba8-46028aafc98b | -5.60409 | -45.17218 | 2025-07-06 03:38:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 41429b39-a004-3061-a4a2-a6940b33b7ec | -5.60621 | -45.18192 | 2025-07-06 03:38:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| abd2aedf-396a-3739-8749-b390e40f7a0b | -7.96707 | -47.22392 | 2025-07-06 03:38:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 776118a5-a21d-3abd-a19b-2204a403cde2 | -5.19043 | -37.69664 | 2025-07-06 03:38:00 | NPP-375D | BARAÚNA | RIO GRANDE DO NORTE | Brasil | 2401453 | 24 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 43b1f0b3-1a70-364b-b02a-5d6e553789bf | -5.57136 | -45.20818 | 2025-07-06 03:38:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 9.0 |
| a3beb671-6ffb-3b4e-a209-d13316fe98bb | -7.20119 | -43.1276 | 2025-07-06 03:38:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 3.5 |
| c3f04cff-a417-3a05-9919-1229fd3f7386 | -7.20056 | -43.13108 | 2025-07-06 03:38:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 3.5 |
| d3970006-9003-3517-87de-d1db431b33cd | -5.59593 | -45.18116 | 2025-07-06 03:38:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e0fa0d90-3edd-35e8-b2f2-701e755ca22f | -5.60317 | -45.17723 | 2025-07-06 03:38:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 6ad945ac-b6a5-3e3f-970d-e2af386dcdb5 | -7.19994 | -43.13459 | 2025-07-06 03:38:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 4.0 |
| 325c8380-4526-3e52-84d4-637ddf0f3649 | -5.60532 | -45.187 | 2025-07-06 03:38:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 705d3903-57a7-3ee2-b5c1-213a9d5cd76d | -7.20534 | -43.13555 | 2025-07-06 03:38:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 4.0 |
| 7f7c06c7-edb4-3973-857d-3433f02bd70b | -5.60854 | -45.18353 | 2025-07-06 03:38:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 9cd9462c-fd54-302f-98b5-19e154e9d8b9 | -7.19453 | -43.13363 | 2025-07-06 03:38:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 966b5c98-1db7-3c51-87fa-1ce447e9eea9 | -3.81212 | -42.54664 | 2025-07-06 03:38:00 | NPP-375D | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b5e32baf-80e9-3c06-9033-826aeb3038e4 | -5.61072 | -45.19337 | 2025-07-06 03:38:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| cccc09d0-33c0-3ae9-8024-3e3a18cd0e8b | -5.59499 | -45.18628 | 2025-07-06 03:38:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a4e9957d-4043-3679-b442-05ada3cfc08f | -5.06893 | -43.73131 | 2025-07-06 03:38:00 | NPP-375D | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 91d89597-4a39-3925-91ab-3a4889ccbf26 | -5.60131 | -45.18741 | 2025-07-06 03:38:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 4ee091ee-a08b-3449-906e-1e4ce869a6b8 | -5.60799 | -45.1718 | 2025-07-06 03:38:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a5de4305-cfb4-33d8-83fd-34dc40771e27 | -6.41723 | -41.73575 | 2025-07-06 03:38:00 | NPP-375D | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 0507df71-aef2-3140-8c76-1a55b83d6aef | -6.67733 | -43.14844 | 2025-07-06 03:38:00 | NPP-375D | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Caatinga | 0.8 |
| d4a43e42-a500-33f8-a4a5-586f0cc35e2f | -5.59991 | -45.18073 | 2025-07-06 03:38:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 40e06737-7d20-3421-84d2-dcaef4d9c81f | -10.64977 | -44.49038 | 2025-07-06 03:38:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| fc741ef9-364f-3d47-9751-735354000428 | -5.56949 | -45.21832 | 2025-07-06 03:38:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 7.6 |
| ba080353-e40a-3a64-abda-1b04547e148d | -5.57466 | -45.2128 | 2025-07-06 03:38:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 6.5 |
| bd163eaf-2170-3c39-91b2-1c93d2857e23 | -6.936 | -42.80745 | 2025-07-06 03:38:00 | NPP-375D | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 3.9 |
| 664e512a-4add-37dc-a71b-2072260eb87a | -7.08605 | -44.39534 | 2025-07-06 03:38:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 7765be04-a6a2-3770-a872-dd702d519bae | -5.61039 | -45.1734 | 2025-07-06 03:38:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 606e37c8-6609-3528-90d6-2f2bf7e9d3cd | -10.64568 | -44.48963 | 2025-07-06 03:38:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 03a0267e-43fa-3303-a0f3-aa63884538b3 | -7.2018 | -43.12417 | 2025-07-06 03:38:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 018ddefa-be8b-3c99-a9b7-617530ef7831 | -7.96584 | -47.23038 | 2025-07-06 03:38:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 0f3124e5-f2ab-3aa4-be7e-4bcd63621e74 | -5.60761 | -45.1886 | 2025-07-06 03:38:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| d2ce342b-8949-3c8a-9b6c-63adfab710d0 | -7.97262 | -47.23215 | 2025-07-06 03:38:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 454b59a6-fe46-3fa7-a5c4-af7ffa2eea11 | -9.09818 | -47.96162 | 2025-07-06 03:38:00 | NPP-375D | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 4a3341aa-da6d-3d98-b7b4-d5a0cf910478 | -7.18912 | -43.13272 | 2025-07-06 03:38:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 5973f009-1437-3406-871c-b7438d9688ac | -10.64422 | -44.48932 | 2025-07-06 03:38:00 | NPP-375D | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d54ff4ba-ec5c-38e2-843f-39a1dfd4bda9 | -5.06965 | -43.72719 | 2025-07-06 03:38:00 | NPP-375D | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| aa8372fe-4e42-36d7-9ded-176c5958d030 | -6.68818 | -43.15071 | 2025-07-06 03:38:00 | NPP-375D | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 961719e8-c1a2-3551-8f75-5673bae139c9 | -8.07399 | -34.97808 | 2025-07-06 03:38:00 | NPP-375D | RECIFE | PERNAMBUCO | Brasil | 2611606 | 26 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| cfc14ae4-c42e-39d1-b76b-8d2cd3765f4b | -5.56833 | -45.21167 | 2025-07-06 03:38:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 6.5 |
| e8a72efe-20d5-3e73-aa91-8ca79e0602c2 | -6.68276 | -43.14956 | 2025-07-06 03:38:00 | NPP-375D | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Caatinga | 1.2 |
| bf7ff79f-0108-3750-a2ca-ba96ca1cdd5b | -9.09391 | -47.96029 | 2025-07-06 03:38:00 | NPP-375D | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| dc8dfc76-c716-32b4-ae60-224a83f8c366 | -5.55046 | -37.31926 | 2025-07-06 03:38:00 | NPP-375D | UPANEMA | RIO GRANDE DO NORTE | Brasil | 2414605 | 24 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 974e7d30-bfc5-38b9-b772-b55568ee2f3c | -7.18975 | -43.12921 | 2025-07-06 03:38:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 8f85efd6-669d-3a61-94d6-7bcff6003f1b | -9.08985 | -47.96662 | 2025-07-06 03:38:00 | NPP-375D | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 8.0 |
| e8c27693-3695-3d31-8257-0419f60828ce | -9.20635 | -45.33784 | 2025-07-06 03:38:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 0.5 |
| f93b14ee-6e6b-3945-bcec-8d4e91c27625 | -5.6008 | -45.17566 | 2025-07-06 03:38:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 92ff96ac-c873-374c-9175-14104e38c4b9 | -6.41734 | -41.73452 | 2025-07-06 03:38:00 | NPP-375D | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 045398af-8d52-3efc-a499-ede86640c23a | -5.60224 | -45.1823 | 2025-07-06 03:38:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 3c44b52b-1a09-3ee1-a0f1-1beb6544eecf | -9.20035 | -45.33665 | 2025-07-06 03:38:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 5e11dc36-3af1-39a9-bdee-771a7e5fbed5 | -5.56743 | -45.21672 | 2025-07-06 03:38:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 271f3a6d-f7f9-3c03-a0a5-78e4285c91a2 | -7.47832 | -34.84244 | 2025-07-06 03:38:00 | NPP-375D | PITIMBU | PARAÍBA | Brasil | 2511905 | 25 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| c744ab3c-2e1e-30c4-a094-5067fbb4c63e | -11.4588 | -45.0895 | 2025-07-06 03:40:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 69.4 |
| 1e2b0cea-98ed-3ff9-9fb3-b2d51b316b3b | -11.4584 | -45.1126 | 2025-07-06 03:40:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 50.4 |
| 797609f4-56fb-33e9-9663-e8438248915f | -12.0266 | -57.0845 | 2025-07-06 03:40:00 | GOES-19 | ITANHANGÁ | MATO GROSSO | Brasil | 5104542 | 51 | 33 | nan | nan | nan | Amazônia | 73.0 |
| 0a473b91-ec45-3217-92e7-809e1f4d51be | -16.68073 | -43.88415 | 2025-07-06 03:40:00 | NPP-375D | MONTES CLAROS | MINAS GERAIS | Brasil | 3143302 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 3734ef73-05ca-3495-bf82-376844c9a6a8 | -11.4498 | -45.10526 | 2025-07-06 03:40:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 8.8 |
| 03d879e7-b49f-36a8-8fee-7f0d6322e4ff | -15.71782 | -43.49174 | 2025-07-06 03:40:00 | NPP-375D | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 2e444603-a6ae-3a6b-a311-f1ab0d884536 | -10.87619 | -47.18705 | 2025-07-06 03:40:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 0258dc51-74cd-3590-9bb3-1327d8f587b5 | -11.45058 | -45.10126 | 2025-07-06 03:40:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 7.3 |
| b57fda55-7117-36e2-9928-4c63edf7e65e | -10.87484 | -47.18417 | 2025-07-06 03:40:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 1e2c1f33-9b93-3a91-bf08-6f2aab2fb141 | -15.71716 | -43.4928 | 2025-07-06 03:40:00 | NPP-375D | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |


[Clique aqui para ver as próximas entradas](README3.md)
