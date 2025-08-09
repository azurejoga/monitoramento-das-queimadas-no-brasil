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

## Dados Diários - Página 25

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 76c69890-9132-38e1-a517-e848bb29b92e | -7.39998 | -47.13538 | 2025-08-09 05:04:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| f4c4d357-b4c4-367e-a660-96e896686712 | -8.92206 | -60.73067 | 2025-08-09 05:04:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 90954d5e-bc53-341c-9015-ed2b93e9b30d | -12.56582 | -47.11089 | 2025-08-09 05:04:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 5d64a795-ba47-3859-b327-3d2912564f13 | -9.92304 | -60.48781 | 2025-08-09 05:04:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| de968b8e-368e-394f-a987-6cb83a15ed4a | -7.06309 | -59.17737 | 2025-08-09 05:04:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 45.4 |
| 67075f75-147c-30ee-a171-647d9347dcd6 | -6.1229 | -42.95476 | 2025-08-09 05:04:00 | NOAA-20 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| b927d388-5480-3d9a-9f01-44125d71207a | -9.0571 | -45.08261 | 2025-08-09 05:04:00 | NOAA-20 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 20.7 |
| b5eec575-7424-36c8-b539-8c95322efdbb | -7.06986 | -59.20409 | 2025-08-09 05:04:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.8 |
| c0992382-e823-3284-ada7-2ea6290050ba | -10.60528 | -48.36245 | 2025-08-09 05:04:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 7.9 |
| daf341e0-e7a7-3f0f-b368-d772c33f2516 | -7.96216 | -49.3993 | 2025-08-09 05:04:00 | NOAA-20 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| f4cdb2b1-9788-3a5a-8ff1-4e2671f003c5 | -7.05655 | -59.1721 | 2025-08-09 05:04:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 18.6 |
| fd750949-34d4-3d44-998c-a24ee9c67812 | -7.09095 | -59.1973 | 2025-08-09 05:04:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 14e777a7-371c-37a9-971b-305b5c1979b0 | -12.61391 | -48.10777 | 2025-08-09 05:04:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 942477f8-a9d1-3c9f-b42d-5ddf9e5a066e | -13.07247 | -43.83262 | 2025-08-09 05:04:00 | NOAA-20 | SANTANA | BAHIA | Brasil | 2928208 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 0c71582c-2d26-351b-80c3-dc3eaba9a988 | -9.93933 | -60.50462 | 2025-08-09 05:04:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| edde2eb1-c95a-34d1-83b6-20c4fc06881f | -7.05545 | -59.20167 | 2025-08-09 05:04:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 8.6 |
| ed9614d0-553d-3b60-b23e-47089a9e4651 | -7.07951 | -59.16724 | 2025-08-09 05:04:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 82.0 |
| cb85df07-b59e-3cd4-9309-e8a26b4703c4 | -9.94315 | -60.48216 | 2025-08-09 05:04:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c2fd2b29-6c30-36d1-b099-5b31e8b0c936 | -7.08943 | -59.18421 | 2025-08-09 05:04:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 427ac19b-2c4a-3c38-a362-6883e4c1499b | -7.06109 | -59.18969 | 2025-08-09 05:04:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 61.9 |
| ed1b4288-f53d-33cd-89e2-8dfc8bd95672 | -11.37943 | -54.35113 | 2025-08-09 05:04:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 17b53200-9e07-3dd3-9554-bbc463caee35 | -11.93958 | -44.54291 | 2025-08-09 05:04:00 | NOAA-20 | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| c89b279c-211a-39b3-9027-ad8da7d72174 | -7.08155 | -59.18713 | 2025-08-09 05:04:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 107.7 |
| 42d047de-2b8a-339c-a8ee-8ca7fd9633ce | -8.7481 | -55.02152 | 2025-08-09 05:04:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 97f43ee7-7a29-371a-ac90-2065e6ddc8ba | -7.05027 | -59.18795 | 2025-08-09 05:04:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 6493f9bf-0fc3-356d-bf8e-38b5062ae791 | -11.32899 | -55.22241 | 2025-08-09 05:04:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| f8ce19f1-88d0-3be1-887c-2d39d24b1920 | -7.07298 | -59.16195 | 2025-08-09 05:04:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 9.0 |
| 6df43439-58e5-3a03-86ea-59d56943f8eb | -6.13378 | -42.96195 | 2025-08-09 05:04:00 | NOAA-20 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 15.0 |
| b2f35013-16dd-34cd-81f8-37f89de82b00 | -6.13977 | -42.96854 | 2025-08-09 05:04:00 | NOAA-20 | AMARANTE | PIAUÍ | Brasil | 2200509 | 22 | 33 | nan | nan | nan | Caatinga | 15.0 |
| 04411c9d-20d9-3bef-a92e-c06d4724889b | -6.62428 | -47.29 | 2025-08-09 05:04:00 | NOAA-20 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 93ce9bb8-fc9f-3d07-b5a3-302be9909eea | -7.05613 | -59.19746 | 2025-08-09 05:04:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 8.6 |
| c25180d6-ea35-3fe6-a87a-fbe9702b3923 | -7.25296 | -44.32421 | 2025-08-09 05:04:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 60bf2d3f-c7e7-39b0-bd23-f7f8f2cd39b3 | -7.06761 | -59.19508 | 2025-08-09 05:04:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 8.0 |
| c3543bc0-9d51-30e2-9315-4ec508b7dfbe | -7.07054 | -59.19989 | 2025-08-09 05:04:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.8 |
| b4bd0ead-c363-31ee-8f86-1066957d06cc | -9.51926 | -45.4312 | 2025-08-09 05:04:00 | NOAA-20 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| a421c7a6-a154-3fff-9deb-37d267ff3695 | -7.09372 | -59.18063 | 2025-08-09 05:04:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 6.5 |
| feca2263-3099-3e96-961c-3b25677b2c00 | -11.37883 | -54.35514 | 2025-08-09 05:04:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4d4fbf52-b4b5-3bb5-8e0e-ecac3e5dad82 | -7.07365 | -59.19009 | 2025-08-09 05:04:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 23620e58-01c3-36fa-a532-7c3902e8c6fc | -8.9309 | -46.73467 | 2025-08-09 05:04:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 9ee6a3c6-5b11-39a2-a6b7-75ae753798e6 | -7.40375 | -59.99625 | 2025-08-09 05:04:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 3b1b322b-2d51-3692-8420-77b06255ebf1 | -8.93103 | -46.7364 | 2025-08-09 05:04:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 76566107-90d6-3290-96fd-57f2f67d50bd | -5.32422 | -55.94335 | 2025-08-09 05:04:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 89914d36-af5e-317c-a188-77383ab6b974 | -9.99893 | -48.1319 | 2025-08-09 05:04:00 | NOAA-20 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 9da40d23-a72a-3167-86ee-c64fa15a8a03 | -12.68698 | -48.20599 | 2025-08-09 05:04:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 53c9bd3f-a50f-3214-ae61-8372d7b40402 | -7.06895 | -59.18679 | 2025-08-09 05:04:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 42.2 |
| d9b6a11c-eb1c-3fb5-b2e9-de397493a36a | -7.09013 | -59.18003 | 2025-08-09 05:04:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 73ad279b-3a56-3178-83d8-6136bbc9057e | -7.07908 | -59.19279 | 2025-08-09 05:04:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 4eb5abb9-b343-3267-96e4-cb3bef5ec2e4 | -7.08501 | -59.16639 | 2025-08-09 05:04:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 26.2 |
| bd1b96cc-3366-33ab-9532-ec53fe432c0c | -7.08177 | -59.17613 | 2025-08-09 05:04:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 75.1 |
| 14afe747-4fad-3e21-85f7-96922b50fc11 | -8.92565 | -60.75594 | 2025-08-09 05:04:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 5825f381-8375-33f4-bb66-74c73404e02e | -7.63034 | -49.84387 | 2025-08-09 05:04:00 | NOAA-20 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 61ea00dc-10d4-3bc4-b6d9-ccb3359188f0 | -6.13413 | -42.97422 | 2025-08-09 05:04:00 | NOAA-20 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 21.1 |
| 3a19dfd3-9c28-3af3-ba94-60f8c84b0967 | -13.06365 | -43.83975 | 2025-08-09 05:04:00 | NOAA-20 | SANTANA | BAHIA | Brasil | 2928208 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 7cf99b50-1c28-3aa1-bcd7-59c61115eec0 | -7.06694 | -59.19926 | 2025-08-09 05:04:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 7d2dab7e-7773-3ff9-9f40-8d5ea2785bdd | -11.73005 | -47.48734 | 2025-08-09 05:04:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| dd195ed5-d100-3ada-b07c-d3ae14db4538 | -5.88377 | -57.74767 | 2025-08-09 05:04:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 65cc719e-2c20-36e6-ae7f-851d9ff53848 | -8.91532 | -60.54359 | 2025-08-09 05:04:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 30350949-f65b-32f2-a9d6-31f76c89b54e | -7.09442 | -59.17646 | 2025-08-09 05:04:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 6.5 |
| d753dca6-2cd9-35e2-853b-9d7be892d059 | -7.08141 | -59.1658 | 2025-08-09 05:04:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 42.4 |
| b7100b30-44d9-32d4-a448-0f3b8e2584f3 | -7.0496 | -59.19211 | 2025-08-09 05:04:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 5.0 |
| ad5c06b7-59bd-37c8-a991-f5eaf4e0abd1 | -12.609 | -48.10359 | 2025-08-09 05:04:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 51b4dda3-f4bb-305a-8cee-1ee433eb1f21 | -9.86457 | -44.70061 | 2025-08-09 05:04:00 | NOAA-20 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 5d59ec22-598d-3ab7-89dd-8ec13d36a418 | -7.10746 | -46.10789 | 2025-08-09 05:04:00 | NOAA-20 | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 1ab2760c-10ff-32a6-b0fb-3d211ea616b5 | -11.0912 | -50.50398 | 2025-08-09 05:04:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| cefe730b-a404-38f7-b127-ec261492369b | -7.06669 | -59.17793 | 2025-08-09 05:04:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 45.4 |
| 7719369b-50bb-39f7-b4c2-d036296a2beb | -7.08109 | -59.18029 | 2025-08-09 05:04:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 75.1 |
| ae0ef2b9-c6a7-3b13-aaa3-281c99598036 | -9.92393 | -60.46023 | 2025-08-09 05:04:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 9f1245a6-910d-39ee-88cf-573a5b7285c0 | -6.63421 | -60.00047 | 2025-08-09 05:04:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 460004f6-f298-38cd-bf05-4c4be0d32dde | -6.13491 | -42.96834 | 2025-08-09 05:04:00 | NOAA-20 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 21.1 |
| 6f967eeb-8063-3beb-a357-d5210c735dbb | -11.93362 | -44.55163 | 2025-08-09 05:04:00 | NOAA-20 | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 7f8f0699-3495-370c-9adc-56e897f7e92b | -12.61432 | -48.10429 | 2025-08-09 05:04:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 77d786f5-e038-3bbb-bb8f-269810fd08f1 | -7.06828 | -59.19094 | 2025-08-09 05:04:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 8.0 |
| 92765366-e8ab-3219-a5bc-895d1b4b3763 | -12.48955 | -47.50856 | 2025-08-09 05:04:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 62977511-1ce4-337d-a7a6-ac54ed4baf71 | -6.127 | -42.96108 | 2025-08-09 05:04:00 | NOAA-20 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 42850512-ed6b-3597-be0a-405092395fbb | -6.59639 | -43.39252 | 2025-08-09 05:04:00 | NOAA-20 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Caatinga | 3.4 |
| c17ac0f3-ebf9-3c46-b776-703f977f19e2 | -9.99933 | -48.12889 | 2025-08-09 05:04:00 | NOAA-20 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 5e401205-fca5-3738-bbae-1bec5e085b5e | -7.25156 | -59.99837 | 2025-08-09 05:04:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| bfb3abe1-2e5d-3fbb-a8a8-1e52205490bd | -11.72962 | -47.49094 | 2025-08-09 05:04:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| db399b84-f814-3a51-a5b6-e6fa7ba79072 | -8.93596 | -46.73919 | 2025-08-09 05:04:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 3d6733c9-65f1-3fa8-a0de-f27c3b461137 | -7.07817 | -59.17554 | 2025-08-09 05:04:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 75.1 |
| e58d54d9-d62d-30b9-abbe-f34271b21af5 | -12.56449 | -47.12194 | 2025-08-09 05:04:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 5e51228d-b489-3af3-b3cb-72abc387b846 | -7.07481 | -59.19634 | 2025-08-09 05:04:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 403aef26-a6d1-33b8-9926-f5fc43cac6fc | -9.0137 | -51.11501 | 2025-08-09 05:04:00 | NOAA-20 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 52ebb414-fac8-3fda-ae31-40b4f8fe3e32 | -9.51373 | -45.42585 | 2025-08-09 05:04:00 | NOAA-20 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| b475286a-3a08-35bb-8246-4dbcf2eb959f | -9.01423 | -51.11128 | 2025-08-09 05:04:00 | NOAA-20 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e819e535-d41c-3aab-960e-84d5337a62c1 | -10.44822 | -44.34694 | 2025-08-09 05:04:00 | NOAA-20 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 8c607e61-ab7d-36e7-85a0-6e8c6af2d374 | -12.59246 | -47.17567 | 2025-08-09 05:04:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 066c0cfe-6690-39b6-b066-dea74d740d9a | -9.55103 | -62.7198 | 2025-08-09 05:04:00 | NOAA-20 | RIO CRESPO | RONDÔNIA | Brasil | 1100262 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| dad5724f-de20-35cc-82f1-c7034f86d92b | -12.55554 | -47.10043 | 2025-08-09 05:04:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| b8cffce3-36c4-3053-9514-79bd4f07965d | -6.5986 | -43.37637 | 2025-08-09 05:04:00 | NOAA-20 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Caatinga | 2.2 |
| d9ea3b3c-af66-35d5-a3c5-0e93f529d368 | -8.91881 | -60.74982 | 2025-08-09 05:04:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| f218213f-df14-36bb-9e01-24dfc10eb3dd | -13.04933 | -43.85061 | 2025-08-09 05:04:00 | NOAA-20 | SANTANA | BAHIA | Brasil | 2928208 | 29 | 33 | nan | nan | nan | Cerrado | 10.6 |
| 0fe7941b-4f0a-3756-a636-2e076ea10194 | -12.56357 | -47.12956 | 2025-08-09 05:04:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 730be9e0-77cd-3646-989b-e96009c6e018 | -7.07884 | -59.17138 | 2025-08-09 05:04:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 82.0 |
| 19280673-3e09-39ae-91b0-2d9d4be70ed2 | -7.08003 | -59.17409 | 2025-08-09 05:04:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 52.0 |
| c799ae69-6e70-301d-a2e7-d86e2681e073 | -7.05184 | -59.20108 | 2025-08-09 05:04:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 8.6 |
| 0ee121e1-3af0-349c-bfbd-7efb0ba5b2c1 | -7.4082 | -60.01565 | 2025-08-09 05:04:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 0dc0a581-c834-3927-b63d-3fead6f086ac | -6.20088 | -55.61858 | 2025-08-09 05:04:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 9b96f7df-a865-3ca0-9f58-4d3aeb38b4c7 | -7.07976 | -59.1886 | 2025-08-09 05:04:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 97.3 |
| 6307b0c8-f37b-39c0-86f2-dc75f7e0fb12 | -6.13297 | -42.96784 | 2025-08-09 05:04:00 | NOAA-20 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 15.0 |


[Clique aqui para ver as próximas entradas](README26.md)
