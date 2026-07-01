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

## Dados Diários - Página 10

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| e4f0242c-9cb3-3458-aeea-0aa0ec4a9275 | -4.94696 | -48.2433 | 2026-07-01 04:02:00 | NOAA-21 | ABEL FIGUEIREDO | PARÁ | Brasil | 1500131 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e4abdd96-f927-3ac4-a4eb-436ff1e03deb | -6.98177 | -39.82724 | 2026-07-01 04:02:00 | NOAA-21 | ASSARÉ | CEARÁ | Brasil | 2301604 | 23 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 7175dc3a-ef4c-3494-8212-3f5647b1f798 | -7.73829 | -45.9201 | 2026-07-01 04:02:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| f92638ba-4674-3c34-b6b9-df17231e5408 | -9.20746 | -45.32959 | 2026-07-01 04:02:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| e49b3e9c-6654-3706-9999-e2202d310ddd | -10.84361 | -45.0538 | 2026-07-01 04:02:00 | NOAA-21 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 9a99c41b-3b4d-3e25-beeb-e4db78a28ad7 | -10.38532 | -49.5873 | 2026-07-01 04:02:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 5.5 |
| e183b42f-44e8-3deb-8852-9de7f9af30da | -9.88774 | -50.39358 | 2026-07-01 04:02:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 8122b9eb-8922-3452-a9fb-0e48e93df54a | -10.66245 | -54.56142 | 2026-07-01 04:02:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d235c9ae-de8b-3be4-a323-47315081458e | -9.21143 | -45.33027 | 2026-07-01 04:02:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 10004b38-407b-39ef-a0ca-9137465907af | -5.80052 | -45.06688 | 2026-07-01 04:02:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 0257ca21-1bbe-3ec5-948e-14c8c7f17fbc | -9.74701 | -49.04252 | 2026-07-01 04:02:00 | NOAA-21 | DIVINÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1707108 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 16247429-a0fd-38f2-a29a-092cd1188d35 | -7.00693 | -42.7781 | 2026-07-01 04:02:00 | NOAA-21 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 0.4 |
| 9b8bb6f9-f617-31d5-a885-ca03fa9892d4 | -5.79642 | -45.06617 | 2026-07-01 04:02:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| b366ad1e-36ce-3c2a-a424-5f77870b286a | -10.43804 | -49.59049 | 2026-07-01 04:02:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 1cb062f8-a51f-3113-8e4d-c4227be93ccb | -5.79827 | -45.05526 | 2026-07-01 04:02:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 0ef3c7c3-a7be-3525-ad94-1c5b20bf46f4 | -5.55375 | -43.969 | 2026-07-01 04:02:00 | NOAA-21 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 0b2fc52c-f020-3db7-bb53-f7686eb35569 | -7.00917 | -42.78673 | 2026-07-01 04:02:00 | NOAA-21 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| aaffa2b5-2685-34d8-84c3-61e88e150226 | -10.43618 | -49.58143 | 2026-07-01 04:02:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| aa578b68-adcd-36a9-b08b-b33de5c04725 | -8.59637 | -48.00294 | 2026-07-01 04:02:00 | NOAA-21 | ITAPIRATINS | TOCANTINS | Brasil | 1710904 | 17 | 33 | nan | nan | nan | Cerrado | 14.1 |
| 9fbd62d5-ad64-3c1b-9cab-5900ede0f512 | -8.59543 | -48.00824 | 2026-07-01 04:02:00 | NOAA-21 | ITAPIRATINS | TOCANTINS | Brasil | 1710904 | 17 | 33 | nan | nan | nan | Cerrado | 12.0 |
| 3324781e-ed5c-3617-ac7c-482445fbbff1 | -5.80176 | -45.05957 | 2026-07-01 04:02:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 80912243-7063-36c6-80df-61900f6e9786 | -5.79307 | -43.88643 | 2026-07-01 04:02:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| f038dc03-9aea-3edf-b920-84b50386dc96 | -10.12676 | -52.09639 | 2026-07-01 04:02:00 | NOAA-21 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 990e5b0c-9179-3b35-868e-25a85226a8dd | -6.16266 | -44.64688 | 2026-07-01 04:02:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 7.3 |
| fe935341-0767-3ed9-9463-816bd8e881d4 | -11.9132 | -43.77693 | 2026-07-01 04:02:00 | NOAA-21 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 1db3d24c-fd74-3334-a6d6-18e2f8460b4f | -4.58487 | -48.02911 | 2026-07-01 04:02:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b9baf68a-10b7-37e4-aaa7-99259ba0daf7 | -9.28102 | -48.763 | 2026-07-01 04:02:00 | NOAA-21 | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a71d595d-cb90-3cfb-aebb-49d18fa570ec | -5.79409 | -45.03552 | 2026-07-01 04:02:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| d8f7d780-d02b-3bab-8a2a-f7e5d2d5cfd2 | -10.79047 | -53.54388 | 2026-07-01 04:02:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 5043eb23-b116-3612-ab7e-3be896fe103c | -10.66913 | -54.52818 | 2026-07-01 04:02:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 34.0 |
| 36c91710-ec17-355c-94a0-94f88e97f5be | -5.79951 | -43.6329 | 2026-07-01 04:02:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 3c3172cf-ccb7-3f49-97c1-fbc97ec3fdc8 | -10.7567 | -42.1065 | 2026-07-01 04:02:00 | NOAA-21 | ITAGUAÇU DA BAHIA | BAHIA | Brasil | 2915353 | 29 | 33 | nan | nan | nan | Caatinga | 1.8 |
| d7aa0570-41d3-3e60-92f0-031da3023528 | -7.74539 | -44.18725 | 2026-07-01 04:02:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 6b3c0065-a610-32ff-97b2-63983ea84662 | -5.55456 | -43.96416 | 2026-07-01 04:02:00 | NOAA-21 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 02e5eb9d-f4c1-3a57-8f82-f455ec0ecca4 | -5.35361 | -45.18807 | 2026-07-01 04:02:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 6.5 |
| ca7cd84b-3d1f-3415-bb72-32684b4f2ee2 | -7.10226 | -46.50708 | 2026-07-01 04:02:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 0b2d3b7a-2930-303a-a9c6-cbfda7d26779 | -5.78999 | -45.03483 | 2026-07-01 04:02:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 1abc07ef-f375-3fb9-a46a-7c71c230d98c | -10.77074 | -53.54038 | 2026-07-01 04:02:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 4.0 |
| d26674d2-c54d-3ec7-a1f4-3db8dfbadc32 | -5.79871 | -45.05897 | 2026-07-01 04:02:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 73fc3f48-5c6e-3fd7-a585-3578e47712ed | -10.78932 | -53.54955 | 2026-07-01 04:02:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f44b457c-241b-3548-a916-01ad3cb7a189 | -8.72942 | -47.83784 | 2026-07-01 04:02:00 | NOAA-21 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 61a4a8c5-ecea-32e3-89e5-4de4e293b064 | -4.94642 | -48.24657 | 2026-07-01 04:02:00 | NOAA-21 | ABEL FIGUEIREDO | PARÁ | Brasil | 1500131 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8886f7d3-4b83-364f-bdb7-c23774fa535f | -10.94758 | -44.23885 | 2026-07-01 04:02:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 48987c45-00a3-3a96-9641-054bff5c2318 | -8.65165 | -47.77348 | 2026-07-01 04:02:00 | NOAA-21 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 75428840-50cf-38fe-8817-844c0478d122 | -5.79704 | -45.06252 | 2026-07-01 04:02:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| af5df67e-2264-3297-a1a6-c0d77fa5aac4 | -6.18972 | -44.86728 | 2026-07-01 04:02:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 826ba9e4-3a5a-3282-80f5-d709e012ba8b | -12.43199 | -41.78498 | 2026-07-01 04:02:00 | NOAA-21 | SEABRA | BAHIA | Brasil | 2929909 | 29 | 33 | nan | nan | nan | Caatinga | 0.8 |
| ea782ada-8af1-3912-87b7-adf663608e69 | -10.94837 | -44.23829 | 2026-07-01 04:02:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| d69eb19b-1cf4-36e8-ad15-13f7e085de45 | -5.79929 | -45.05534 | 2026-07-01 04:02:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 7d53cdae-28c6-3434-8889-2050e9ea2db8 | -7.8373 | -43.07516 | 2026-07-01 04:02:00 | NOAA-21 | RIO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2209005 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 6c166685-140e-3fe5-ab35-7f85461bb258 | -10.67737 | -54.52312 | 2026-07-01 04:02:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 34.0 |
| 261b8ebb-3d48-3e86-b6a8-4bfd6f919470 | -11.84503 | -45.52172 | 2026-07-01 04:02:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 64ebcb0e-3667-3705-892a-3bf8cacf85f7 | -6.85965 | -38.34924 | 2026-07-01 04:02:00 | NOAA-21 | MARIZÓPOLIS | PARAÍBA | Brasil | 2509156 | 25 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 3d989f6a-26a4-310f-a44c-3109ff9d6271 | -10.44073 | -49.58555 | 2026-07-01 04:02:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| b2367be9-855d-3e70-98d1-7f94913918c5 | -10.76958 | -53.54611 | 2026-07-01 04:02:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 528fb4a7-eb27-3b53-b7b7-666f9feeddcd | -10.77733 | -53.54151 | 2026-07-01 04:02:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 4c2925da-1ebf-3a2d-abcc-dfc8fc7d8ab7 | -10.3859 | -49.58414 | 2026-07-01 04:02:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 4aa678b3-ffa1-31d0-903e-daa38a82a3b3 | -10.12067 | -52.09529 | 2026-07-01 04:02:00 | NOAA-21 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 8.6 |
| b0c00059-515e-39fa-8093-116c5c9d6494 | -11.01749 | -45.24176 | 2026-07-01 04:02:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 532fa94a-630d-35ab-9101-7c85adfb3ce5 | -10.38473 | -49.59048 | 2026-07-01 04:02:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 5.5 |
| f1b0a0f8-8177-3675-89ef-ec2ec75ccb60 | -10.66806 | -54.56949 | 2026-07-01 04:02:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c21624a3-77fa-314d-8c81-d6e5eb7d8721 | -7.29085 | -46.25121 | 2026-07-01 04:02:00 | NOAA-21 | NOVA COLINAS | MARANHÃO | Brasil | 2107258 | 21 | 33 | nan | nan | nan | Cerrado | 9.3 |
| e3fed7f6-a062-3ba4-babc-3c1776577286 | -10.4346 | -49.58008 | 2026-07-01 04:02:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 48a1918e-4111-31c1-956c-12047e61c76b | -8.58943 | -50.97532 | 2026-07-01 04:02:00 | NOAA-21 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 976c4de3-7141-3a05-9c1b-5ca81a1c61b0 | -10.81316 | -49.34262 | 2026-07-01 04:02:00 | NOAA-21 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e3b4b80e-61fc-3d44-a6d8-6c0e7bd94ab1 | -9.97477 | -48.24125 | 2026-07-01 04:02:00 | NOAA-21 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| f27d0b65-1c9f-3293-8567-c7fc3af3c281 | -10.44132 | -49.58241 | 2026-07-01 04:02:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| caec3d57-2cb0-3149-8ddc-db8caaecb6c6 | -6.18226 | -47.34549 | 2026-07-01 04:02:00 | NOAA-21 | CAMPESTRE DO MARANHÃO | MARANHÃO | Brasil | 2102556 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 04da600b-8d6d-3b0c-9337-4b6936497064 | -7.47434 | -44.75241 | 2026-07-01 04:02:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c88aefa4-4225-3fe2-b692-de1a8e8dd19e | -10.9225 | -43.05402 | 2026-07-01 04:02:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 54.4 |
| 974d9877-cfd0-38ed-aa50-d0f0ebf9ed7a | -8.12465 | -47.88261 | 2026-07-01 04:02:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 12416797-c1c6-3486-9d93-40a0558aa468 | -10.66112 | -54.568 | 2026-07-01 04:02:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b2b6791d-250a-38f4-964f-e5867a747c64 | -10.43975 | -49.58104 | 2026-07-01 04:02:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 2c07f05d-2e0f-3720-9d86-06df214f5eff | -11.5476 | -47.45338 | 2026-07-01 04:02:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 18.7 |
| 84664684-1c1a-358d-9293-0ab13f7531a9 | -10.92188 | -43.05338 | 2026-07-01 04:02:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 118.3 |
| a41d583e-7445-30e1-95e7-c44e64f082dd | -8.12557 | -47.87735 | 2026-07-01 04:02:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| fecdd54f-1d60-3697-b421-33154d29dc7d | -10.76483 | -53.54332 | 2026-07-01 04:02:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 4c6bf3eb-5d9d-31b8-87cf-04be19a768f4 | -9.74754 | -49.03959 | 2026-07-01 04:02:00 | NOAA-21 | DIVINÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1707108 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 15efb0df-47e5-3777-8e61-06e4263e90c2 | -5.78878 | -45.04222 | 2026-07-01 04:02:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| dec4af0e-400f-3338-adbc-07114f5220aa | -6.90671 | -48.04452 | 2026-07-01 04:02:00 | NOAA-21 | WANDERLÂNDIA | TOCANTINS | Brasil | 1722081 | 17 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 2013dbd1-d992-3c70-9832-1807a6cb471a | -10.68302 | -54.53092 | 2026-07-01 04:02:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 561b3704-c44f-331a-afc3-caf9286fdb97 | -5.79989 | -45.0517 | 2026-07-01 04:02:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 2e7c7e8f-1cda-322d-be76-6735a44d261b | -6.91321 | -42.84187 | 2026-07-01 04:02:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 3442b009-572f-3eda-b29e-5af75fd697ed | -4.94293 | -48.24553 | 2026-07-01 04:02:00 | NOAA-21 | ABEL FIGUEIREDO | PARÁ | Brasil | 1500131 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 80070aba-eae9-3a30-8e08-7738bcbe671f | -5.4974 | -43.22274 | 2026-07-01 04:02:00 | NOAA-21 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 41c85dda-435d-32e2-a404-a4561da7d29a | -11.9149 | -43.38963 | 2026-07-01 04:02:00 | NOAA-21 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 68d8114d-51d6-30d1-a88f-eb5d39b5f393 | -10.92312 | -43.05019 | 2026-07-01 04:02:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 54.4 |
| ba4f7b1f-bfa3-300a-aece-c9548d5d9e5d | -5.79752 | -45.06628 | 2026-07-01 04:02:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| c9e38509-7250-3e71-9e40-e8b8aa4f245a | -10.92813 | -43.05835 | 2026-07-01 04:02:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 31.9 |
| 52a0012f-b592-38f3-b158-9f9f97c989b9 | -7.09783 | -46.50635 | 2026-07-01 04:02:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 906555be-752d-3c1e-a598-a2e512b60ca3 | -8.5037 | -50.15238 | 2026-07-01 04:02:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c5258d04-67bb-3c5a-af7d-e35e309e9f53 | -7.73895 | -45.91624 | 2026-07-01 04:02:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| c418a040-c2aa-376f-9d7d-c7601d17c54d | -7.22421 | -43.27 | 2026-07-01 04:02:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 45fba4ab-0a2a-38eb-8baf-02c40bae6f25 | -10.78988 | -48.23209 | 2026-07-01 04:02:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 88b7df4b-9431-335c-bdf0-810e9bc65bd2 | -7.00404 | -42.77351 | 2026-07-01 04:02:00 | NOAA-21 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| b44e5efe-2cc4-3e74-8be1-6c2c00a36bbc | -11.53522 | -47.44672 | 2026-07-01 04:02:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| b91a33a7-439b-32af-a816-9c92d04a452e | -9.19234 | -45.32258 | 2026-07-01 04:02:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 40549381-d2fe-3823-b7df-0f59068b0284 | -5.55128 | -43.97105 | 2026-07-01 04:02:00 | NOAA-21 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 71ed03c4-fc10-39d7-a585-2b980c573cda | -11.54606 | -47.46203 | 2026-07-01 04:02:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 2fa8754f-55b4-3ffd-bedc-110ab7d36871 | -7.47709 | -44.7599 | 2026-07-01 04:02:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |


[Clique aqui para ver as próximas entradas](README11.md)
