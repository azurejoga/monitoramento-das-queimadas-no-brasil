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

## Dados Diários - Página 22

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 69fc6a7b-dbab-3254-9516-2a347d4b4b09 | -6.8711 | -59.030102 | 2024-10-30 01:47:29 | METOP-C | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 9ddd46d7-9392-39b6-9809-fecfe31813af | -6.8733 | -59.039501 | 2024-10-30 01:47:29 | METOP-C | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| b04932ab-8754-3480-abb0-43f2a00c3592 | -6.8756 | -59.048901 | 2024-10-30 01:47:29 | METOP-C | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 8666be0e-738d-39ee-98a9-175d897455ba | -2.7471 | -57.460098 | 2024-10-30 01:48:29 | METOP-C | BARREIRINHA | AMAZONAS | Brasil | 1300508 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 3565a95e-40b1-30e4-9104-37c30505cffd | -2.7503 | -57.473701 | 2024-10-30 01:48:29 | METOP-C | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 8e37dd3a-36f6-3b3e-ba6c-ad9320f4f17b | -2.7406 | -57.476002 | 2024-10-30 01:48:29 | METOP-C | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 81f7167c-1fa5-3cc3-87c3-62cee2dd2ebe | -1.447 | -54.189602 | 2024-10-30 01:48:38 | METOP-C | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| cdb9cde8-e086-3219-928b-93b9549a9f00 | -1.4422 | -60.2756 | 2024-10-30 01:49:01 | METOP-C | PRESIDENTE FIGUEIREDO | AMAZONAS | Brasil | 1303536 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 53265484-a8c7-38ce-967b-c30c6683b3c0 | -0.7939 | -62.867401 | 2024-10-30 01:49:21 | METOP-C | BARCELOS | AMAZONAS | Brasil | 1300409 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| fbefa37e-ce1d-3817-8d75-b8c18105d34b | -0.7955 | -62.874699 | 2024-10-30 01:49:21 | METOP-C | BARCELOS | AMAZONAS | Brasil | 1300409 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| eeda627f-3769-341b-b58d-95cd09e14701 | -0.7972 | -62.881901 | 2024-10-30 01:49:21 | METOP-C | BARCELOS | AMAZONAS | Brasil | 1300409 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| d56425f1-051f-37e6-8643-acd27e14faa5 | -0.7841 | -62.869598 | 2024-10-30 01:49:21 | METOP-C | BARCELOS | AMAZONAS | Brasil | 1300409 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 6c1f0cb0-551e-3cac-90bb-ac3b5952df33 | -0.7857 | -62.8769 | 2024-10-30 01:49:21 | METOP-C | BARCELOS | AMAZONAS | Brasil | 1300409 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| e206eaad-252e-308a-bc7c-50c950952a0e | -0.7874 | -62.884102 | 2024-10-30 01:49:21 | METOP-C | BARCELOS | AMAZONAS | Brasil | 1300409 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 099e06fc-e8b6-3d7e-ac61-fdb9c064e42c | -0.7891 | -62.8913 | 2024-10-30 01:49:21 | METOP-C | BARCELOS | AMAZONAS | Brasil | 1300409 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| e9959f7b-7f49-3645-a1e6-8330d31ee51b | -0.7776 | -62.886299 | 2024-10-30 01:49:22 | METOP-C | BARCELOS | AMAZONAS | Brasil | 1300409 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| b9fc7ae8-8215-3c4e-8e87-04382e5280be | 3.1596 | -64.199203 | 2024-10-30 01:50:30 | METOP-C | ALTO ALEGRE | RORAIMA | Brasil | 1400050 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| 1bc38e35-bca0-3005-ba90-5f7bf3cb8527 | -2.3906 | -48.9337 | 2024-10-30 01:55:19 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 48.2 |
| c4ff727d-860d-377b-b089-152c2ed7ce3a | -2.833 | -49.2413 | 2024-10-30 01:55:22 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 116.5 |
| d0cd2bd3-b293-3b1f-a8dc-3f73b39e8e52 | -2.8331 | -49.22 | 2024-10-30 01:55:22 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 57.7 |
| 6174ba9e-2170-39d4-bb20-493dd38f61e2 | -2.8515 | -49.2408 | 2024-10-30 01:55:22 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 56.3 |
| 1156c45c-c591-3a30-8cb2-16cca9c58624 | -3.1098 | -54.2665 | 2024-10-30 01:55:24 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 39.9 |
| c42ccd00-39f9-3451-823d-c3213cc88875 | -3.1281 | -54.266 | 2024-10-30 01:55:24 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 50.2 |
| 22959cc1-2ae5-37d0-8a38-6ae0b9ec2ec8 | -3.1601 | -50.6021 | 2024-10-30 01:55:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 75.9 |
| aae0344c-8bb7-3df8-8416-b0a03606e04e | -3.1602 | -50.5812 | 2024-10-30 01:55:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 67.4 |
| 68924bc1-1c67-3c86-8922-930a1d48f44c | -3.1786 | -50.6016 | 2024-10-30 01:55:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 100.8 |
| 44909535-0c7d-3fff-b1f5-5c994e39dbd5 | -3.1787 | -50.5807 | 2024-10-30 01:55:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 96.7 |
| 94c920cf-770c-341d-ab11-d545198e7e2d | -3.234 | -50.5789 | 2024-10-30 01:55:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 53.6 |
| 76fb262c-e3b2-3cc4-8031-bd6b34d4f07b | -3.2534 | -50.3689 | 2024-10-30 01:55:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 65.7 |
| bf2c4f48-1345-39da-ad40-eb3630bcf5f7 | -3.2535 | -50.3479 | 2024-10-30 01:55:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 152.7 |
| 9a51a3cb-07b8-3fd4-8415-b0726c78bdbf | -3.2719 | -50.3473 | 2024-10-30 01:55:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 96.6 |
| 65c09e3b-d36c-3164-a155-9488180e7369 | -3.5631 | -47.3847 | 2024-10-30 01:55:26 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 269.5 |
| 1c374fa8-139e-37a7-ba20-e414d40bd237 | -3.5632 | -47.3629 | 2024-10-30 01:55:26 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 133.8 |
| 149aaac3-1e77-3942-8326-df37eb6e517e | -3.5688 | -50.043 | 2024-10-30 01:55:26 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 33.8 |
| b06ea43b-4af0-3f9a-a7d5-a3b32e0bede1 | -3.5817 | -47.384 | 2024-10-30 01:55:26 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 279.1 |
| 6c05acad-a5c1-34fb-bf1e-d422f8b2afab | -3.5818 | -47.3621 | 2024-10-30 01:55:26 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 138.8 |
| 52ba7b37-0a44-303b-8f07-54b6a8ba5066 | -3.9326 | -41.4957 | 2024-10-30 01:55:28 | GOES-16 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 65.5 |
| 29bb10ea-f6f5-3562-b96e-907376c8a3d5 | -4.0681 | -50.024 | 2024-10-30 01:55:29 | GOES-16 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 45.1 |
| 011c051c-3fc2-3455-b52c-6f974bb53607 | -4.0682 | -50.0029 | 2024-10-30 01:55:29 | GOES-16 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 41.8 |
| 70b35cdd-f866-32a1-92d9-148871addb9a | -4.2496 | -50.6677 | 2024-10-30 01:55:30 | GOES-16 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 39.1 |
| 2e0e8029-4bae-357c-8765-c8844437614b | -4.2681 | -50.6669 | 2024-10-30 01:55:30 | GOES-16 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 58.3 |
| 839d571c-7dd6-3a9c-bdfe-57d1999311e0 | -4.2561 | -43.46 | 2024-10-30 01:55:30 | GOES-16 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 57.1 |
| e70a842b-01a4-30e4-af88-a051a0f3f889 | -4.2563 | -43.4368 | 2024-10-30 01:55:30 | GOES-16 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 82.1 |
| 7401590c-c14e-3ced-b1ae-fcd503c276c9 | -4.2749 | -43.4357 | 2024-10-30 01:55:30 | GOES-16 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 75.1 |
| 388c1c0d-88f5-3552-ae2b-fc2cddd30f84 | -4.4971 | -46.4618 | 2024-10-30 01:55:31 | GOES-16 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 82.4 |
| b7317333-49c1-31e1-9421-1eb2b006c6a5 | -4.6049 | -44.3161 | 2024-10-30 01:55:32 | GOES-16 | CAPINZAL DO NORTE | MARANHÃO | Brasil | 2102754 | 21 | 33 | nan | nan | nan | Cerrado | 70.4 |
| ead942f7-d573-3bfc-afb6-1c811d15b8bb | -4.6051 | -44.2932 | 2024-10-30 01:55:32 | GOES-16 | CAPINZAL DO NORTE | MARANHÃO | Brasil | 2102754 | 21 | 33 | nan | nan | nan | Cerrado | 105.8 |
| 1b1634b4-9ef2-32c2-9a2e-b1aeb7797fe7 | -5.212 | -47.9577 | 2024-10-30 01:55:35 | GOES-16 | VILA NOVA DOS MARTÍRIOS | MARANHÃO | Brasil | 2112852 | 21 | 33 | nan | nan | nan | Amazônia | 62.1 |
| 01b557fa-e773-379f-b07d-cdba02f92bfd | -5.2122 | -47.9359 | 2024-10-30 01:55:35 | GOES-16 | VILA NOVA DOS MARTÍRIOS | MARANHÃO | Brasil | 2112852 | 21 | 33 | nan | nan | nan | Amazônia | 42.8 |
| 7e8ec14b-a65d-3161-a872-e78691ec56ef | -5.2306 | -47.9566 | 2024-10-30 01:55:35 | GOES-16 | VILA NOVA DOS MARTÍRIOS | MARANHÃO | Brasil | 2112852 | 21 | 33 | nan | nan | nan | Amazônia | 92.4 |
| ed100dfe-92a5-376a-a687-014e2229c847 | -5.2308 | -47.9349 | 2024-10-30 01:55:35 | GOES-16 | VILA NOVA DOS MARTÍRIOS | MARANHÃO | Brasil | 2112852 | 21 | 33 | nan | nan | nan | Amazônia | 64.6 |
| cd2274c3-ada7-334f-9739-4b7e429172eb | -5.9788 | -45.3621 | 2024-10-30 01:55:40 | GOES-16 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 85.0 |
| 0f32bd18-7f1f-3703-93de-f8257af30d31 | -6.8408 | -59.0519 | 2024-10-30 01:55:45 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 61.5 |
| 4f7b4dc9-6ba7-36ff-a0ca-96cca2a3a532 | -6.8592 | -59.0511 | 2024-10-30 01:55:45 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 85.3 |
| 8c9d2a1a-8741-3605-ae97-1a91d73503c3 | -6.8593 | -59.0318 | 2024-10-30 01:55:45 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 46.7 |
| 6f42abe1-88cd-38b6-924e-729e1c689e98 | -10.3434 | -49.6536 | 2024-10-30 01:56:04 | GOES-16 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 146.0 |
| 5cac043c-1403-3dde-aec7-075bc5665159 | -10.3437 | -49.6321 | 2024-10-30 01:56:04 | GOES-16 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 67.6 |
| 5a01342a-56e4-3555-88ab-92a59bb6ea38 | -10.7171 | -44.9391 | 2024-10-30 01:56:06 | GOES-16 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 77.9 |
| cf3c5767-9771-3920-96b2-3ad370a85442 | -10.7175 | -44.916 | 2024-10-30 01:56:06 | GOES-16 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 152.9 |
| 81203fbe-a206-3c29-88f0-c7128b631d49 | -12.899 | -45.0549 | 2024-10-30 01:56:18 | GOES-16 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 81.9 |
| 23090603-752a-3281-aa2c-58df6cecd57f | -18.2454 | -55.9793 | 2024-10-30 01:56:48 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 82.5 |
| 153c309c-76f1-3bc3-a140-231e11f421c8 | -23.9923 | -54.1106 | 2024-10-30 01:57:18 | GOES-16 | ALTÔNIA | PARANÁ | Brasil | 4100509 | 41 | 33 | nan | nan | nan | Mata Atlântica | 83.6 |
| bfb746b0-b9bc-35d1-9e3a-22a951d5d27f | -23.98592 | -54.10586 | 2024-10-30 02:04:00 | TERRA_M-M | ALTÔNIA | PARANÁ | Brasil | 4100509 | 41 | 33 | nan | nan | nan | Mata Atlântica | 42.6 |
| f9463e05-a724-3157-b6d0-b72b19699148 | -23.98493 | -54.10073 | 2024-10-30 02:04:00 | TERRA_M-M | ALTÔNIA | PARANÁ | Brasil | 4100509 | 41 | 33 | nan | nan | nan | Mata Atlântica | 28.6 |
| 6cc4d005-6514-3d85-b6b7-926a1afaf60c | -2.3906 | -48.955 | 2024-10-30 02:05:19 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 50.8 |
| 897daa5d-b98e-3ab0-b75e-acaca9b666e6 | -2.3906 | -48.9337 | 2024-10-30 02:05:19 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 79.6 |
| 70e5f55c-51da-3bdd-b260-4a0c9aded098 | -2.833 | -49.2413 | 2024-10-30 02:05:22 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 105.7 |
| fe10c0fc-b0dc-34bc-a9cd-0f26621327ae | -2.8331 | -49.22 | 2024-10-30 02:05:22 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 47.8 |
| 8650afd7-660d-31bd-9be0-8dfd5ac086d4 | -2.8515 | -49.2408 | 2024-10-30 02:05:22 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 46.5 |
| f2e38704-8fda-3f68-a719-6a8fa363ff9b | -3.0734 | -54.167 | 2024-10-30 02:05:23 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 51.5 |
| bb178cb0-5cc9-3453-8cec-e4b1fd9a2ff1 | -3.1094 | -45.2293 | 2024-10-30 02:05:23 | GOES-16 | VIANA | MARANHÃO | Brasil | 2112803 | 21 | 33 | nan | nan | nan | Amazônia | 90.2 |
| 2c0bd1a3-2bd4-36b3-8a07-d4fa6c8b4638 | -3.0913 | -54.287 | 2024-10-30 02:05:23 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 57.7 |
| c6bf75c3-fc44-39f5-adaf-7ae0e3561fb5 | -3.0914 | -54.2669 | 2024-10-30 02:05:23 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 42.2 |
| 41377f68-d6b9-3c40-ba10-07ad8516a9c3 | -3.2534 | -50.3689 | 2024-10-30 02:05:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 63.9 |
| c86e6a77-a426-3334-8616-7fd3971547d2 | -3.2535 | -50.3479 | 2024-10-30 02:05:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 168.6 |
| 1432c7bb-a77b-3f15-8ccb-cd4726b60e45 | -3.2719 | -50.3473 | 2024-10-30 02:05:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 92.2 |
| 423a2606-faa5-3bde-b250-dda600446e60 | -3.1097 | -54.2865 | 2024-10-30 02:05:24 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 63.0 |
| 17c6e904-6ca3-371c-b108-b184b1775f5f | -3.1098 | -54.2665 | 2024-10-30 02:05:24 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 54.0 |
| a92b92f3-0cf8-3425-993d-1a8f16d786bd | -3.1601 | -50.6021 | 2024-10-30 02:05:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 71.2 |
| 3517e48d-2184-3c8a-926a-2032c42dbe86 | -3.1602 | -50.5812 | 2024-10-30 02:05:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 66.3 |
| 7ffb3910-dae7-34e0-a48d-e529834f4401 | -3.1786 | -50.6016 | 2024-10-30 02:05:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 111.9 |
| 98bd6579-678e-300f-a118-cb0f7a1d0f6e | -3.1787 | -50.5807 | 2024-10-30 02:05:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 98.6 |
| e4e7b3f4-749f-3b82-a820-63dd28f6a9fa | -3.234 | -50.5789 | 2024-10-30 02:05:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 49.1 |
| a1674f77-5fda-3a72-aedd-3a6a6f8524b0 | -3.4597 | -54.0765 | 2024-10-30 02:05:26 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 35.9 |
| d00c5214-baf3-36d8-b0c0-be18cb716f15 | -3.5631 | -47.3847 | 2024-10-30 02:05:26 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 229.5 |
| 84543dfd-2c35-3ec9-bc08-79d62fce394c | -3.5632 | -47.3629 | 2024-10-30 02:05:26 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 128.3 |
| bd104a84-2a20-31d0-bfbb-cfbab59cf6c3 | -3.5817 | -47.384 | 2024-10-30 02:05:26 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 277.5 |
| 803e900b-ffc0-39be-92d1-bb677d79c266 | -3.5818 | -47.3621 | 2024-10-30 02:05:26 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 153.0 |
| 43976fe3-4615-3e25-95fa-795c87aff71e | -3.9326 | -41.4957 | 2024-10-30 02:05:28 | GOES-16 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 60.8 |
| d62a734d-2374-3ae2-84be-1d091eb0f5d4 | -4.0681 | -50.024 | 2024-10-30 02:05:29 | GOES-16 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 43.6 |
| 2ede2909-961f-366f-b549-d42b952e073e | -4.0682 | -50.0029 | 2024-10-30 02:05:29 | GOES-16 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 39.1 |
| faaae480-d13f-3221-b3fe-ac66cc287411 | -4.2496 | -50.6677 | 2024-10-30 02:05:30 | GOES-16 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 41.0 |
| 206655b1-7cee-3237-9b07-f8708d90f622 | -4.2681 | -50.6669 | 2024-10-30 02:05:30 | GOES-16 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 61.2 |
| 634b7140-6079-320a-b9a3-98fec6bdbbab | -4.2561 | -43.46 | 2024-10-30 02:05:30 | GOES-16 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 59.9 |
| 13980bc8-5492-3151-bd9d-d4681224b29b | -4.2563 | -43.4368 | 2024-10-30 02:05:30 | GOES-16 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 75.5 |
| 4b6e975d-7db8-3ef2-badb-e5c5d87ad3b6 | -4.2748 | -43.4589 | 2024-10-30 02:05:30 | GOES-16 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 54.6 |
| 3f8de592-433a-311e-a59d-78d158f978ae | -4.2749 | -43.4357 | 2024-10-30 02:05:30 | GOES-16 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 85.2 |
| dd314cea-75a7-32eb-aca6-50a5c7299b97 | -4.4971 | -46.4618 | 2024-10-30 02:05:31 | GOES-16 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 58.8 |
| 35334539-3542-3905-b057-d05a6456be29 | -4.6051 | -44.2932 | 2024-10-30 02:05:32 | GOES-16 | CAPINZAL DO NORTE | MARANHÃO | Brasil | 2102754 | 21 | 33 | nan | nan | nan | Cerrado | 293.6 |
| 973b4c04-55f3-330e-aaf6-0842b78aa8fc | -4.5864 | -44.2943 | 2024-10-30 02:05:32 | GOES-16 | CAPINZAL DO NORTE | MARANHÃO | Brasil | 2102754 | 21 | 33 | nan | nan | nan | Cerrado | 60.8 |


[Clique aqui para ver as próximas entradas](README23.md)
