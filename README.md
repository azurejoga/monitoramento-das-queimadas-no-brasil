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

## Dados Diários - Página 1

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 6b8ea003-099f-3f34-a506-8e1f5f62d3b3 | -0.8539 | -52.8501 | 2024-11-06 00:00:00 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 48.8 |
| 3d782e24-0acb-3ff6-af65-f3ea9b3f4450 | -5.6561 | -45.9468 | 2024-11-06 00:00:00 | GOES-16 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 111.5 |
| 8a77bb10-2e9c-3cb7-a255-e8367473310c | -3.6603 | -50.2291 | 2024-11-06 00:00:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 38.1 |
| 66a7e030-5188-3f40-ac13-a5c8a2798da8 | -4.4715 | -50.6583 | 2024-11-06 00:00:00 | GOES-16 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 58.7 |
| 0d9c85cf-a330-34b7-9d3a-17377311370e | -2.8662 | -45.5977 | 2024-11-06 00:00:00 | GOES-16 | SANTA HELENA | MARANHÃO | Brasil | 2109809 | 21 | 33 | nan | nan | nan | Amazônia | 55.0 |
| 9dd1ee7b-2ace-3888-8916-387658da4d4f | -4.1246 | -43.5833 | 2024-11-06 00:00:00 | GOES-16 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 98.2 |
| 15dc9718-720e-307a-aae3-a461ff6ca5b6 | -3.0849 | -50.9591 | 2024-11-06 00:00:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 38.9 |
| a0d1dfc4-23de-34e1-8667-7e78ab1adf3a | -6.1041 | -43.9593 | 2024-11-06 00:00:00 | GOES-16 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 103.7 |
| 85e250f6-4f67-3102-8d9f-1a7e36ff757b | -2.8608 | -51.7524 | 2024-11-06 00:00:00 | GOES-16 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 42.9 |
| 8efd652a-c799-335c-8081-40d3fe5938ee | -6.4827 | -47.4827 | 2024-11-06 00:00:00 | GOES-16 | AGUIARNÓPOLIS | TOCANTINS | Brasil | 1700301 | 17 | 33 | nan | nan | nan | Cerrado | 188.5 |
| 63999ff0-3c62-3dfd-b40c-11dc73145147 | -2.6948 | -51.8185 | 2024-11-06 00:00:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 41.5 |
| 01cbbc0a-93b8-3517-8f44-878131ba1d44 | -3.7066 | -41.6997 | 2024-11-06 00:00:00 | GOES-16 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 103.8 |
| f0787b3b-430d-34ee-a21d-d40628fce26a | -4.5614 | -48.0141 | 2024-11-06 00:00:00 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 92.4 |
| 2797dac0-3081-3afc-86e1-32d96d04a232 | -2.764 | -53.2062 | 2024-11-06 00:00:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 39.0 |
| a9d42acd-9d1c-34f6-b845-d6d4f6092b6b | -3.0207 | -53.4227 | 2024-11-06 00:00:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 119.0 |
| ec457a42-39d6-3f64-bc81-f2c538b4b549 | -4.0667 | -46.9246 | 2024-11-06 00:00:00 | GOES-16 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 46.5 |
| cfd0266d-234e-367b-bf48-756f0621e2fb | -3.0396 | -53.2805 | 2024-11-06 00:00:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 132.0 |
| 62446d8c-8e2b-35f5-82cf-047d6bc47b11 | -2.658 | -51.8194 | 2024-11-06 00:00:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 49.7 |
| 283fa348-41a8-3d24-b6d1-8f3880375601 | -3.2348 | -50.3904 | 2024-11-06 00:00:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 35.5 |
| 554b7dee-3ba3-33ed-9de8-45a4b9a1b842 | -2.8423 | -51.7735 | 2024-11-06 00:00:00 | GOES-16 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 102.6 |
| 9b3d3d21-3cc7-33de-a695-12ea7057c48d | -2.2505 | -46.484 | 2024-11-06 00:00:00 | GOES-16 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 55.7 |
| f3cc9fff-549b-3532-a1bd-d9e3f744e72f | -3.0207 | -53.443 | 2024-11-06 00:00:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 115.2 |
| e3f2100a-eb78-3384-8052-9096d9430a6b | -6.1226 | -43.9809 | 2024-11-06 00:00:00 | GOES-16 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 237.0 |
| f9aa5f65-8c4d-3b7e-b311-b25dea3842e9 | -3.0397 | -53.2603 | 2024-11-06 00:00:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 155.5 |
| 5ddc850f-a974-3a0e-8a62-b891470ce05d | -3.526 | -47.3862 | 2024-11-06 00:00:00 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 44.0 |
| c7101478-0921-3cf7-8928-a87fb3b67d51 | -5.5632 | -43.6998 | 2024-11-06 00:00:00 | GOES-16 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 99.6 |
| 1bcec127-899a-368a-9f2a-c826a553e3fb | -3.967 | -48.15 | 2024-11-06 00:00:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 69.1 |
| 07374ad5-e890-3ef8-a472-96243c0ef180 | -3.9669 | -48.1716 | 2024-11-06 00:00:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 54.8 |
| 3092b7c2-5633-3ab3-abd9-23a5afca5146 | -2.2691 | -46.4835 | 2024-11-06 00:00:00 | GOES-16 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 40.5 |
| d63dd7a1-2d27-38f5-bf42-990a55144801 | -23.9517 | -54.0521 | 2024-11-06 00:00:00 | GOES-16 | ALTÔNIA | PARANÁ | Brasil | 4100509 | 41 | 33 | nan | nan | nan | Mata Atlântica | 95.3 |
| a245657a-97d0-30cd-a152-7e12462d99fe | -3.2053 | -53.2356 | 2024-11-06 00:00:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 53.7 |
| 65d0d71c-e83a-3a00-8543-06250b5256e0 | -5.5445 | -43.7012 | 2024-11-06 00:00:00 | GOES-16 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 78.8 |
| f394c784-62e8-31a5-8338-0524dcae44f8 | -3.1617 | -50.2038 | 2024-11-06 00:00:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 63.9 |
| bf466bf5-36b6-351f-b329-d7fc461890bc | -2.8661 | -45.6201 | 2024-11-06 00:00:00 | GOES-16 | SANTA HELENA | MARANHÃO | Brasil | 2109809 | 21 | 33 | nan | nan | nan | Amazônia | 106.3 |
| a405856c-d6cb-3ed3-a036-a5d5f97bda07 | -2.1746 | -53.7036 | 2024-11-06 00:00:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 80.0 |
| 6a961f00-db24-3250-b036-3fd8b38e949c | -2.7881 | -51.4859 | 2024-11-06 00:00:00 | GOES-16 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 32.1 |
| e5ef0d10-a4ec-36c9-823c-30bd127f6dcf | -2.8423 | -51.7942 | 2024-11-06 00:00:00 | GOES-16 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 59.8 |
| 9b37cd21-6cdb-309a-9a8a-23700dc3f88d | -1.3696 | -51.9458 | 2024-11-06 00:00:00 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 31.4 |
| 244a29d3-09b3-3b7f-b2fd-a7a2499b25fd | -5.6748 | -45.9456 | 2024-11-06 00:00:00 | GOES-16 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 88.8 |
| a6e00f35-1731-3b30-a04b-277a55cbd7b9 | -5.6563 | -45.9244 | 2024-11-06 00:00:00 | GOES-16 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 92.1 |
| 0ea45467-c7b4-3788-8a85-4729debaca9a | -2.7639 | -53.2265 | 2024-11-06 00:00:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 38.4 |
| abab96a1-4b5b-3f0f-9be8-efc0c0528bee | -6.5012 | -47.5033 | 2024-11-06 00:00:00 | GOES-16 | AGUIARNÓPOLIS | TOCANTINS | Brasil | 1700301 | 17 | 33 | nan | nan | nan | Cerrado | 268.9 |
| ccbfe517-2c5e-3bc6-b1ef-3774f24f6be6 | -0.8539 | -52.8298 | 2024-11-06 00:00:00 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 59.8 |
| 72a0e394-753b-368c-a99a-94cd33663458 | -2.1746 | -53.6834 | 2024-11-06 00:00:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 51.2 |
| f066b12c-5389-3f16-af3c-f4fa8220eeed | -2.7243 | -54.1552 | 2024-11-06 00:00:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 126.8 |
| a2e80f3b-2db3-32f2-93d4-26bdfa1e85dd | -3.0607 | -52.5066 | 2024-11-06 00:00:00 | GOES-16 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 55.8 |
| 2fadc590-2ce4-33bc-8afd-c8af117e1446 | -6.1229 | -43.9578 | 2024-11-06 00:00:00 | GOES-16 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 163.3 |
| 094217fe-632c-3702-99d2-382e840f7d31 | -4.0859 | -53.9365 | 2024-11-06 00:00:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 59.5 |
| ca41ef9d-b665-3a6d-8024-d894a3887032 | -6.1039 | -43.9824 | 2024-11-06 00:00:00 | GOES-16 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 90.7 |
| c9151ef0-1e2c-368c-aeb6-cdc1131f4271 | -3.7068 | -41.6758 | 2024-11-06 00:00:00 | GOES-16 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 89.0 |
| 0cfcc705-e9c2-32b9-913d-c291a13c49d0 | -2.8506 | -49.4744 | 2024-11-06 00:00:00 | GOES-16 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 47.1 |
| 8eea5c5a-b959-310a-934d-792c9c9f9ee8 | -2.8065 | -51.4855 | 2024-11-06 00:00:00 | GOES-16 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 47.8 |
| 65fc0d83-20e7-33a7-8f1e-3e416b413fc0 | -3.2054 | -53.2153 | 2024-11-06 00:00:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 48.5 |
| 83e450c5-e106-3937-b17c-b9b5a7f71acd | -23.9512 | -54.0744 | 2024-11-06 00:00:00 | GOES-16 | ALTÔNIA | PARANÁ | Brasil | 4100509 | 41 | 33 | nan | nan | nan | Mata Atlântica | 92.1 |
| a749edd3-3541-3e85-96ea-37505bf1e55f | -23.9306 | -54.0564 | 2024-11-06 00:00:00 | GOES-16 | ALTÔNIA | PARANÁ | Brasil | 4100509 | 41 | 33 | nan | nan | nan | Mata Atlântica | 109.4 |
| e17f2cf5-a60e-34eb-999f-65e0246bcee2 | -2.8608 | -51.7731 | 2024-11-06 00:00:00 | GOES-16 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 194.4 |
| 68fb77e2-9482-3099-ae8b-079e51fe69f5 | -23.93 | -54.0787 | 2024-11-06 00:00:00 | GOES-16 | ALTÔNIA | PARANÁ | Brasil | 4100509 | 41 | 33 | nan | nan | nan | Mata Atlântica | 110.4 |
| dcb9d857-a616-3051-8e1c-87e97925a40d | -3.6788 | -50.2284 | 2024-11-06 00:00:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 49.5 |
| bb5e091f-a40f-37be-b86e-584063d895b0 | -6.1416 | -43.9563 | 2024-11-06 00:00:00 | GOES-16 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 100.2 |
| 47400df4-1d88-3236-ad86-78263ef21550 | -3.1786 | -50.6016 | 2024-11-06 00:00:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 43.4 |
| bc645b9c-5509-3699-a0c1-28186f5a8190 | -2.6764 | -51.8395 | 2024-11-06 00:00:00 | GOES-16 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 57.3 |
| ab2a79d7-bc1f-3ffc-95bf-d5b4de1c04e5 | -3.0213 | -53.2607 | 2024-11-06 00:00:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 112.3 |
| 7546b5f9-f1e7-38c4-bbfb-fdfc98add0bd | -3.5447 | -47.3636 | 2024-11-06 00:00:00 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 55.6 |
| 3a2f87f3-a81e-385b-9669-b0fb31ae7e1a | -3.2415 | -53.3967 | 2024-11-06 00:00:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 73.3 |
| d51b0c61-0967-3acf-915e-9fe50241bf2b | -3.0023 | -53.4232 | 2024-11-06 00:00:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 95.8 |
| 1ef75276-439b-34a1-8799-27f105cde02a | -4.1432 | -43.5822 | 2024-11-06 00:00:00 | GOES-16 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 73.9 |
| 28889b5d-aa0c-36e8-8cc7-9a0094ca5946 | -2.8607 | -51.7937 | 2024-11-06 00:00:00 | GOES-16 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 96.0 |
| 81d8d194-0a79-3a39-a194-7f901379a888 | -6.1414 | -43.9794 | 2024-11-06 00:00:00 | GOES-16 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 136.9 |
| c218cc8a-68b4-332b-893c-85613c773a6d | -0.8355 | -52.8299 | 2024-11-06 00:00:00 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 35.0 |
| 7a202a7d-6d57-36a0-972c-4dcb6a17b0d7 | -2.2691 | -46.4614 | 2024-11-06 00:00:00 | GOES-16 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 43.9 |
| c1977cec-e22b-3b4e-a692-d4c632c6e76d | -6.5096 | -44.6618 | 2024-11-06 00:00:00 | GOES-16 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 96.0 |
| 7e3a2c0d-0072-34b5-b10f-2da473357817 | -2.2506 | -46.4619 | 2024-11-06 00:00:00 | GOES-16 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 39.1 |
| e756190a-ece4-3cc9-84da-7ca0e71d5cb5 | -3.1213 | -51.1036 | 2024-11-06 00:00:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 45.2 |
| 2636ddc3-adeb-3be6-9e1b-6963545c6e4c | -6.5094 | -44.6847 | 2024-11-06 00:00:00 | GOES-16 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 185.3 |
| 16ded1b0-badf-3044-bdd7-76a47fc88eab | -3.3285 | -50.0723 | 2024-11-06 00:00:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 37.0 |
| b071e182-10e5-3ff1-991c-834adddddb79 | -3.5446 | -47.3855 | 2024-11-06 00:00:00 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 169.7 |
| dd84ecbb-a0ee-349d-96ca-a016963acfb9 | -6.5014 | -47.4813 | 2024-11-06 00:00:00 | GOES-16 | AGUIARNÓPOLIS | TOCANTINS | Brasil | 1700301 | 17 | 33 | nan | nan | nan | Cerrado | 449.2 |
| 37a51c49-1dbd-311a-9d31-e64165a5864a | -2.7244 | -54.1351 | 2024-11-06 00:00:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 74.5 |
| ff05298a-b6bd-3895-8851-b1093878dfb1 | -3.2231 | -53.3972 | 2024-11-06 00:00:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 58.8 |
| 1c913535-2cc6-3de8-90c0-246433cb3920 | -6.4906 | -44.6862 | 2024-11-06 00:00:00 | GOES-16 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 137.4 |
| 1e895f6a-adf4-35a8-9988-2650ce8e8cdc | -2.6131 | -54.5381 | 2024-11-06 00:00:00 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 50.6 |
| dc583831-f0bc-3ec7-bda4-174715d46468 | -3.1787 | -50.5807 | 2024-11-06 00:00:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 35.7 |
| 65f62239-39c8-33f2-b236-2787f8478ffe | -3.7255 | -41.6748 | 2024-11-06 00:00:00 | GOES-16 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 115.2 |
| 955c7fbb-efea-3fb8-ab3c-903af6b44b09 | -2.6764 | -51.8189 | 2024-11-06 00:00:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 98.1 |
| b6273f3a-adc7-3892-8842-28ca67fb4df5 | -3.0023 | -53.4434 | 2024-11-06 00:00:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 89.6 |
| aeda4deb-2f33-3f21-9e9c-269808c1d024 | -3.5444 | -47.4073 | 2024-11-06 00:00:00 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 41.8 |
| a7c40b4b-30f8-39b2-b4df-f736dc144b29 | -5.675 | -45.9232 | 2024-11-06 00:00:00 | GOES-16 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 73.2 |
| 53ad1b5f-0766-3a04-81ed-2f4222d1c2f0 | -3.0212 | -53.281 | 2024-11-06 00:00:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 72.0 |
| 345f60d0-c85d-3756-b90d-a206dd6e72e4 | -6.5016 | -47.4594 | 2024-11-06 00:00:00 | GOES-16 | AGUIARNÓPOLIS | TOCANTINS | Brasil | 1700301 | 17 | 33 | nan | nan | nan | Cerrado | 93.3 |
| c2c665d5-52cd-34bc-a797-d4827cd7931b | -6.4825 | -47.5046 | 2024-11-06 00:00:00 | GOES-16 | AGUIARNÓPOLIS | TOCANTINS | Brasil | 1700301 | 17 | 33 | nan | nan | nan | Cerrado | 127.5 |
| 0ba8ec2a-01f8-3556-8566-4e94d55373ee | -0.8355 | -52.8503 | 2024-11-06 00:00:00 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 30.8 |
| b521cd92-c002-31e3-9474-10f80308ea87 | -4.5616 | -47.9925 | 2024-11-06 00:00:00 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 68.6 |
| 19d3da3a-625b-3658-99f6-afa68471a553 | -3.7254 | -41.6987 | 2024-11-06 00:00:00 | GOES-16 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 123.4 |
| 593cc2c4-2d7e-3b1f-a6ab-df92ff33612f | -1.3512 | -51.946 | 2024-11-06 00:00:00 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 29.7 |
| d0f7d300-6f5d-34ef-82e6-712f047d0b17 | -3.2349 | -50.3695 | 2024-11-06 00:00:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 37.2 |
| 40b85ec1-6148-3ce4-8d87-964c788694d8 | -6.4909 | -44.6633 | 2024-11-06 00:00:00 | GOES-16 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 75.3 |
| dc26d0a4-da65-3c9a-abb7-2baf87b3d147 | -5.5474 | -35.5741 | 2024-11-06 00:00:00 | GOES-16 | TAIPU | RIO GRANDE DO NORTE | Brasil | 2413904 | 24 | 33 | nan | nan | nan | Caatinga | 54.3 |
| 4251bb53-0708-39d6-8877-87be510d27f1 | -2.84 | -52.88 | 2024-11-06 00:00:00 | MSG-03 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a27b6afb-1f27-3714-8527-33cf9350ac31 | -2.81 | -53.0 | 2024-11-06 00:00:00 | MSG-03 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8a484051-092e-3ae8-93f2-da9c82876374 | -6.12 | -43.99 | 2024-11-06 00:00:00 | MSG-03 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | nan |


[Clique aqui para ver as próximas entradas](README2.md)
