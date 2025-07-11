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

## Dados Diários - Página 16

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| c6f6db03-ef97-397f-8a87-cd088bf9fe66 | -10.6862 | -49.4874 | 2025-07-11 04:50:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 76.2 |
| 189cb6b8-8fde-3696-beb3-30952c860a91 | -5.5614 | -43.9082 | 2025-07-11 04:50:00 | GOES-19 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 71.8 |
| f17d2221-f3b3-39ad-b31d-e2858e20a121 | -9.9148 | -47.8282 | 2025-07-11 04:50:00 | GOES-19 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 71.5 |
| a8fc7e85-0d49-34a3-bd77-d578d3fc99b7 | -5.5427 | -43.9096 | 2025-07-11 04:50:00 | GOES-19 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 98.8 |
| b273bc79-3c95-3c40-a70a-b164249156cb | -5.5429 | -43.8864 | 2025-07-11 04:50:00 | GOES-19 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 66.5 |
| 240cb276-1f21-3203-8fd3-02f3ba87cbb9 | -2.44315 | -47.46644 | 2025-07-11 04:55:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| cce4445a-3c3e-38fc-a21e-c6c20d0ad57b | -2.66108 | -47.39664 | 2025-07-11 04:55:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 54c23911-cb7e-3126-b66a-7d82aa4e3bec | -2.44684 | -47.47114 | 2025-07-11 04:55:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| b8a21ed1-89e7-3c22-99c8-a2ececb982f1 | -2.44745 | -47.46709 | 2025-07-11 04:55:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| df4bed03-ce2a-3711-a923-ad7a2f705a71 | -7.87797 | -44.54868 | 2025-07-11 04:57:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 7d5284a7-0765-3ab9-ba69-c2c50db1a469 | -9.346 | -50.21817 | 2025-07-11 04:57:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| ad8e2203-dacf-32b9-b0c2-16057e12e29e | -7.18975 | -43.12684 | 2025-07-11 04:57:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 4.6 |
| ca526aa3-ddb3-39fa-aabe-0bfcfc931ef4 | -9.06671 | -47.89271 | 2025-07-11 04:57:00 | NOAA-21 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 3eda4281-8ddb-37d6-a435-0f222f84f7c6 | -3.74812 | -47.11695 | 2025-07-11 04:57:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| cc2bf8ee-953d-3036-abfc-5d037c998709 | -9.53938 | -46.2962 | 2025-07-11 04:57:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 5c971831-b664-3bd3-9411-36ace2770445 | -6.72419 | -44.3329 | 2025-07-11 04:57:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 4ca2361c-ba70-36e2-8ddf-90fda62abd35 | -8.25075 | -44.92514 | 2025-07-11 04:57:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 4877c4ab-3979-34d2-ba34-a2dc343e6c2a | -7.186 | -43.11403 | 2025-07-11 04:57:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 3.4 |
| d856b298-0891-33f0-827a-00f7961e7d5b | -9.35121 | -48.17604 | 2025-07-11 04:57:00 | NOAA-21 | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 69fe4fa6-81a2-363b-a164-d712885b79e5 | -4.57159 | -50.95511 | 2025-07-11 04:57:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 83c1c359-7fdf-37ff-aa90-812a399e0c16 | -3.78634 | -47.09218 | 2025-07-11 04:57:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 02c67a21-46c4-31e1-a627-afed771c1a84 | -7.19096 | -43.11731 | 2025-07-11 04:57:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 4.8 |
| 30656377-5809-3ca8-8431-e439df0b7486 | -6.15643 | -47.27262 | 2025-07-11 04:57:00 | NOAA-21 | CAMPESTRE DO MARANHÃO | MARANHÃO | Brasil | 2102556 | 21 | 33 | nan | nan | nan | Cerrado | 5.4 |
| a52cf543-0cd1-3458-8fe3-fe2205f16179 | -8.38193 | -51.07605 | 2025-07-11 04:57:00 | NOAA-21 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 680eeda5-5a1c-325d-8db8-5da5b47440c3 | -7.55567 | -45.62999 | 2025-07-11 04:57:00 | NOAA-21 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 37977dd9-c6e2-3a0d-8095-b7ef7cd9f163 | -7.20389 | -43.12143 | 2025-07-11 04:57:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 5.2 |
| 525c46fb-4426-3489-a685-88e2a3d67c24 | -5.54504 | -43.89883 | 2025-07-11 04:57:00 | NOAA-21 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f0c0fb03-bbd1-32b7-a241-c690666a7509 | -3.66515 | -48.31749 | 2025-07-11 04:57:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 75d70529-4f9f-3a2d-a9e2-325fed83b1aa | -9.79381 | -47.74606 | 2025-07-11 04:57:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 9f4eb67b-9d88-364e-affc-e9bd504ab7a3 | -6.13929 | -44.11081 | 2025-07-11 04:57:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| dae2b4a4-af65-39b9-b01d-d04c3cdc7d5e | -6.51812 | -43.33184 | 2025-07-11 04:57:00 | NOAA-21 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| d9543399-34ff-3b0e-95f0-964957b42b09 | -7.65948 | -45.34601 | 2025-07-11 04:57:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| d195a213-cf3f-309a-bbb9-18a897462766 | -8.89157 | -47.33831 | 2025-07-11 04:57:00 | NOAA-21 | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ae46a2fb-4bd8-3908-b8c8-e43007435c1e | -5.54559 | -43.89489 | 2025-07-11 04:57:00 | NOAA-21 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 57c9a14f-dedf-3122-be61-395555639c81 | -6.14424 | -45.90817 | 2025-07-11 04:57:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| a95ae6e4-4bf7-3491-9193-35ac2e4ef5ee | -8.58406 | -47.19149 | 2025-07-11 04:57:00 | NOAA-21 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| af6c1399-a0cb-3d36-a481-9bb45ef1a9d1 | -2.9229 | -48.23869 | 2025-07-11 04:57:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6f5627ad-031d-31f4-a201-26bee3b3e3f1 | -8.89085 | -47.3435 | 2025-07-11 04:57:00 | NOAA-21 | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 5db6b1c6-95d7-33b2-a2ac-c9814b18b207 | -9.91345 | -47.83171 | 2025-07-11 04:57:00 | NOAA-21 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 32.9 |
| 29676002-1dae-3963-9b70-f6863357a454 | -6.98146 | -44.45839 | 2025-07-11 04:57:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 3b929e7e-a296-3e53-846b-cd2150b1ca6e | -5.43 | -47.53903 | 2025-07-11 04:57:00 | NOAA-21 | IMPERATRIZ | MARANHÃO | Brasil | 2105302 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f36bd51f-d011-39e8-b64d-396f7ddcc31f | -8.89563 | -47.34416 | 2025-07-11 04:57:00 | NOAA-21 | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 0729eb6a-59fe-35db-913d-ecf37b4e3e09 | -4.23643 | -53.49014 | 2025-07-11 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 0f698498-f5d5-37e8-9e4b-7b2eb854b29b | -3.75397 | -47.1087 | 2025-07-11 04:57:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| d24234ed-cb3d-3572-9a2a-045d89ede679 | -6.85794 | -42.79915 | 2025-07-11 04:57:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 40682336-b2a0-3d1e-b6e2-47cdf4652127 | -9.6166 | -49.02262 | 2025-07-11 04:57:00 | NOAA-21 | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 5149d82f-648e-30c3-a3b5-5bb3b09c3458 | -3.142 | -50.16663 | 2025-07-11 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 1e508d84-82ca-3ebe-889f-716ef4e1a687 | -8.3603 | -51.07903 | 2025-07-11 04:57:00 | NOAA-21 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d595c09c-04cc-3709-9457-5456e5436e7f | -7.55611 | -45.62677 | 2025-07-11 04:57:00 | NOAA-21 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c420f9b4-b7eb-3aca-ad4f-c39acb0e1e5b | -5.55023 | -43.90374 | 2025-07-11 04:57:00 | NOAA-21 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 0d1b21fe-5f2e-3cfd-a16e-29b13a380fa6 | -7.65411 | -45.34525 | 2025-07-11 04:57:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 5dfbde45-2ac4-3312-b460-639ae7ffd947 | -6.99376 | -44.45269 | 2025-07-11 04:57:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| d473f815-69ff-3c11-9b62-729c5e60248e | -3.75027 | -47.11908 | 2025-07-11 04:57:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 1b0d2eaa-4525-39a9-aa86-96d9aca121e1 | -5.12488 | -56.11576 | 2025-07-11 04:57:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| ec17459a-23b7-363d-a3fa-06cfd002628e | -7.63765 | -46.01228 | 2025-07-11 04:57:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 522ace5d-54ba-3ce8-b862-adfd0b3e651f | -7.43086 | -43.83595 | 2025-07-11 04:57:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 7f2dc62b-cdfd-3f9f-bd56-439212c95b52 | -7.94587 | -44.85101 | 2025-07-11 04:57:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| de89d869-ea91-3932-91d0-92fae9d4e69e | -7.19219 | -43.1148 | 2025-07-11 04:57:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 3.4 |
| 4b651142-56c0-3118-b756-7db644f2da57 | -8.59227 | -47.20351 | 2025-07-11 04:57:00 | NOAA-21 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 849f20ca-7649-33bd-977b-497bc347a4e5 | -7.19034 | -43.35974 | 2025-07-11 04:57:00 | NOAA-21 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Caatinga | 4.9 |
| 334542ae-61b0-3169-9a89-9178394566e2 | -6.72648 | -44.33614 | 2025-07-11 04:57:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 13.1 |
| 1fa59d48-3fae-35b7-b021-d806902cf228 | -7.20269 | -43.12397 | 2025-07-11 04:57:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 3.1 |
| 8a0f4325-41b2-3ca8-a48f-f7c391e2bb6a | -8.21903 | -44.917 | 2025-07-11 04:57:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d2abf8e9-0980-3ff3-923d-a0b41e490d2a | -9.62149 | -49.01912 | 2025-07-11 04:57:00 | NOAA-21 | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| b900b5fe-94a6-3725-99eb-71bb1223ed4c | -8.39417 | -46.94261 | 2025-07-11 04:57:00 | NOAA-21 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| bab78027-f80d-374e-83a2-21d11df51fba | -3.7526 | -47.1177 | 2025-07-11 04:57:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 293f4da7-a295-3ca7-bdd7-94b006702b2f | -4.48925 | -50.71119 | 2025-07-11 04:57:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 81ae06dd-5cac-35bb-aa71-fc949279a610 | -7.19091 | -43.12441 | 2025-07-11 04:57:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 7.5 |
| 1bbabd87-31aa-332f-9a46-f177f271754e | -7.95098 | -49.65679 | 2025-07-11 04:57:00 | NOAA-21 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 45471dcc-f4c2-3f2f-9627-e4451cc20b26 | -9.65986 | -49.88979 | 2025-07-11 04:57:00 | NOAA-21 | CASEARA | TOCANTINS | Brasil | 1703909 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ebc75b73-1c5e-362b-8b61-0e8bc6a8931a | -9.19603 | -45.26778 | 2025-07-11 04:57:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 341280bd-43a4-3805-b064-e3862cea256a | -7.95049 | -49.66023 | 2025-07-11 04:57:00 | NOAA-21 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 90fc0d18-416f-3f62-8220-f58ab028739f | -7.87751 | -44.55232 | 2025-07-11 04:57:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| cf7de959-a7cb-385e-8bbf-6932d0616d09 | -8.28737 | -46.33632 | 2025-07-11 04:57:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 5ba29d14-af84-343c-b42b-29c2aed8520e | -9.61718 | -49.01853 | 2025-07-11 04:57:00 | NOAA-21 | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 6498df2c-2e87-369f-a9a0-fa28f09fffa5 | -6.14544 | -44.10851 | 2025-07-11 04:57:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| a1cb93b5-1c4b-38a5-beed-3f94b3ec4f9d | -8.59221 | -47.2067 | 2025-07-11 04:57:00 | NOAA-21 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 5.1 |
| f48b1c10-a974-3c6a-837c-179034b93d81 | -7.87546 | -44.55026 | 2025-07-11 04:57:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 4148a6ca-f72e-3788-9eef-ec7abfb1b9c8 | -3.12968 | -52.4488 | 2025-07-11 04:57:00 | NOAA-21 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 88e42f4b-b3c4-332c-94cb-b90580c741cc | -7.88109 | -44.55151 | 2025-07-11 04:57:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 1ff4e79f-5a32-3578-a4ce-fccb46fa554a | -4.22394 | -47.20957 | 2025-07-11 04:57:00 | NOAA-21 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 31d3b738-d54b-3685-85e7-89f75a088894 | -7.55799 | -49.91102 | 2025-07-11 04:57:00 | NOAA-21 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 51837ef0-3441-3c7e-abca-bfab52e8c173 | -8.89168 | -47.34035 | 2025-07-11 04:57:00 | NOAA-21 | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 862ac096-3fe3-3be6-a978-4f3d8da9ad68 | -7.08097 | -49.60474 | 2025-07-11 04:57:00 | NOAA-21 | XINGUARA | PARÁ | Brasil | 1508407 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 880edaa8-3ce8-3784-8e71-ed916b2f7227 | -10.62146 | -45.229 | 2025-07-11 04:57:00 | NOAA-21 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 2f5b5856-6a07-3abc-b79d-4919fdcc5e26 | -6.85164 | -42.79845 | 2025-07-11 04:57:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 3.9 |
| b80e64a3-8697-30d3-a8e3-fe0fc74b96b2 | -10.62615 | -45.23746 | 2025-07-11 04:57:00 | NOAA-21 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 613aa1c4-680d-3d8e-bc93-03c5a5d688d3 | -3.75328 | -47.1132 | 2025-07-11 04:57:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 9ba01d2c-98b8-3b8e-8f98-429ed5f3a51b | -8.57449 | -47.1932 | 2025-07-11 04:57:00 | NOAA-21 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| d74b2581-8f6b-32ab-9897-67f4a3526a9d | -7.19157 | -43.11244 | 2025-07-11 04:57:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 4.6 |
| d011cf35-e545-3404-a1fa-3fc5ec2bc12d | -10.51005 | -46.52485 | 2025-07-11 04:57:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 75ab6c2f-1f15-3ade-ab27-9190ef8a8b4d | -9.53463 | -46.29222 | 2025-07-11 04:57:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 2c809fa0-cf4f-3545-8458-aa7c878e3bca | -4.31293 | -47.75908 | 2025-07-11 04:57:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f302ce14-617e-3d75-839c-4d8f505e32dc | -7.65089 | -45.35023 | 2025-07-11 04:57:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 8.0 |
| a1f4f40c-d996-34c0-8c11-a7a9fac74d82 | -10.62713 | -45.22963 | 2025-07-11 04:57:00 | NOAA-21 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 305b5169-0591-303d-b0d6-b8bf97899765 | -2.53358 | -53.95802 | 2025-07-11 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 8a7a4f44-d190-34b0-b116-5b06e1b26cfe | -6.87614 | -45.23317 | 2025-07-11 04:57:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| cd3fa8e1-e423-3ede-a77d-fec2e0e6e2a7 | -9.0019 | -54.97278 | 2025-07-11 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 6827484c-e6dd-3acf-9957-01fe36b560d9 | -7.9403 | -44.85008 | 2025-07-11 04:57:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 01811bd0-bb50-3427-b70b-37f727575030 | -6.86687 | -42.77985 | 2025-07-11 04:57:00 | NOAA-21 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |


[Clique aqui para ver as próximas entradas](README17.md)
