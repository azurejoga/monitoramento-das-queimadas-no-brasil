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
| ee2e084f-2665-3978-8231-09eb33848d1b | -10.8826 | -45.3075 | 2026-09-03 00:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 110.6 |
| d82292f9-c3d2-365a-aff8-7b9e4f1e857f | -18.8407 | -46.4417 | 2026-09-03 00:00:00 | GOES-19 | LAGOA FORMOSA | MINAS GERAIS | Brasil | 3137502 | 31 | 33 | nan | nan | nan | Cerrado | 125.0 |
| eb62f943-834a-3bce-ba99-3d0fbe413078 | -10.2028 | -50.2895 | 2026-09-03 00:00:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 89.8 |
| ad9bba67-70c9-3d6b-85ca-dd4a7db403dd | -6.8412 | -58.9746 | 2026-09-03 00:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 54.2 |
| 31e851e6-97e3-363c-a1f5-883db66b5df6 | -7.0428 | -59.2173 | 2026-09-03 00:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 46.8 |
| 1196666d-35d8-3470-beec-b97b3ee25eb9 | -6.6357 | -59.4459 | 2026-09-03 00:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 52.7 |
| 87047773-cda7-3bb2-8665-c108ee7d51c3 | -18.15 | -51.8156 | 2026-09-03 00:00:00 | GOES-19 | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 65.5 |
| 0016a7a0-48e3-3a76-bb47-5fb80454beae | -8.7599 | -62.8332 | 2026-09-03 00:00:00 | GOES-19 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 47.3 |
| 780c4b5d-0682-33d0-a7a4-629e010a08fd | -6.6765 | -58.7492 | 2026-09-03 00:00:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 70.7 |
| 60888d3c-384b-3f5a-ad49-fd97ce9481ea | -9.0415 | -65.7349 | 2026-09-03 00:00:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 93.7 |
| 54e2dd4d-dcb2-3bfd-94b4-de3222488e24 | -6.6063 | -55.2341 | 2026-09-03 00:00:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 73.7 |
| 2f461120-3959-35ed-83f5-e9a53b12846a | -6.6882 | -59.9628 | 2026-09-03 00:00:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 94.6 |
| 2f420cf3-5164-3771-9177-63a98e005d91 | -18.1699 | -51.8122 | 2026-09-03 00:00:00 | GOES-19 | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 87.9 |
| 7baa5324-e214-338d-b0b2-5314143b5d17 | -6.6725 | -43.4239 | 2026-09-03 00:00:00 | GOES-19 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 117.2 |
| b4223089-e063-33b6-8b19-633afbcce9c2 | -8.4675 | -54.6631 | 2026-09-03 00:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 67.2 |
| 3864d961-9e4a-39a5-9480-1f78e6370e10 | -10.9017 | -45.3049 | 2026-09-03 00:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 61.2 |
| 5f9a08a7-57f4-3120-b3fc-6f5134a56094 | -8.4296 | -54.7262 | 2026-09-03 00:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 87.7 |
| 50f06f74-7f20-3c4f-8d23-99c37d88704c | -11.7532 | -50.4851 | 2026-09-03 00:00:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 139.5 |
| 52d68f6e-c241-31e6-bb33-cc74afcd3ee6 | -8.0924 | -50.9642 | 2026-09-03 00:00:00 | GOES-19 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 105.4 |
| 5432ce68-08cb-3e4e-ab5e-69a6f8d2dc0e | -12.4033 | -44.8089 | 2026-09-03 00:00:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 203.1 |
| 59eaed7b-df3a-3225-862c-d5f96688dad6 | -13.4162 | -42.4755 | 2026-09-03 00:00:00 | GOES-19 | BOTUPORÃ | BAHIA | Brasil | 2904209 | 29 | 33 | nan | nan | nan | Caatinga | 105.7 |
| 18964a62-b304-35ae-aaef-c7b83481e394 | -6.6697 | -59.9635 | 2026-09-03 00:00:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 52.0 |
| b73012da-b380-3afb-b63e-6086e61a552c | -11.7725 | -50.4614 | 2026-09-03 00:00:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 94.1 |
| d3d5149b-7ff3-3f76-b508-5cce84231269 | -18.776 | -48.9226 | 2026-09-03 00:00:00 | GOES-19 | MONTE ALEGRE DE MINAS | MINAS GERAIS | Brasil | 3142809 | 31 | 33 | nan | nan | nan | Cerrado | 89.7 |
| 1d2ed925-f1a4-3609-8cb5-97ecc9c69197 | -18.7565 | -48.9039 | 2026-09-03 00:00:00 | GOES-19 | MONTE ALEGRE DE MINAS | MINAS GERAIS | Brasil | 3142809 | 31 | 33 | nan | nan | nan | Cerrado | 81.6 |
| 0174d3d0-3abe-3189-9940-ecd4370c8c9f | -6.6883 | -59.9436 | 2026-09-03 00:00:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 171.1 |
| a688628d-ad98-313a-823b-d0f397a99696 | -6.6727 | -43.4006 | 2026-09-03 00:00:00 | GOES-19 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 96.4 |
| d0edbe10-dc01-3ec4-b8dd-6b293c059174 | -18.1704 | -51.7904 | 2026-09-03 00:00:00 | GOES-19 | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 83.5 |
| 01c1021e-83e7-370d-94ae-e6206b62d4c9 | -18.7559 | -48.9267 | 2026-09-03 00:00:00 | GOES-19 | MONTE ALEGRE DE MINAS | MINAS GERAIS | Brasil | 3142809 | 31 | 33 | nan | nan | nan | Cerrado | 131.4 |
| 59c00965-211e-381b-9041-772932574d82 | -6.6698 | -59.9443 | 2026-09-03 00:00:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 74.5 |
| 4f40bd9a-93cb-305a-9fa0-08b459213e1a | -12.4225 | -44.8059 | 2026-09-03 00:00:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 79.2 |
| f9323f93-a3b5-3dc7-b0d7-53cd0c2eeaab | -8.9111 | -62.353 | 2026-09-03 00:00:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 50.6 |
| 2abee198-afde-3953-b4e1-3d607aab4f5c | -10.8822 | -45.3305 | 2026-09-03 00:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 65.8 |
| 893fb1d3-c0c6-38e4-aba1-69339694441f | -8.6133 | -62.555 | 2026-09-03 00:00:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 58.7 |
| fb480a55-2a2a-3503-8704-eac7113cf7c1 | -6.6006 | -59.1196 | 2026-09-03 00:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 46.2 |
| f7d60f85-d765-360d-a282-7b0f8833b621 | -18.7766 | -48.8999 | 2026-09-03 00:00:00 | GOES-19 | MONTE ALEGRE DE MINAS | MINAS GERAIS | Brasil | 3142809 | 31 | 33 | nan | nan | nan | Cerrado | 63.0 |
| 05694977-a963-35d0-82ce-c3d50a90f397 | -6.212 | -42.5243 | 2026-09-03 00:00:00 | GOES-19 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 57.4 |
| b51d2a3e-9575-3fa9-9005-7d2a70e82508 | -8.6853 | -62.9307 | 2026-09-03 00:00:00 | GOES-19 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 47.3 |
| 52c7d260-62e0-3be9-a5e5-ec4f7a4a7926 | -8.4298 | -54.706 | 2026-09-03 00:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 74.9 |
| dce2866f-a2dd-39a2-82a0-5971e3e98fcd | -9.0231 | -65.7169 | 2026-09-03 00:00:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 64.1 |
| 99e15412-4518-3867-ac04-150e7364f184 | -11.7722 | -50.4829 | 2026-09-03 00:00:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 111.1 |
| 2acf00e6-27e9-3080-9622-fcc53790869d | -6.6248 | -55.2331 | 2026-09-03 00:00:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 183.0 |
| 8af0f8c3-bc6d-3058-95d5-453365458d1a | -11.7535 | -50.4636 | 2026-09-03 00:00:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 102.1 |
| 812f80fe-663e-3215-8eca-90cd9fa28b91 | -8.6317 | -62.5732 | 2026-09-03 00:00:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 51.7 |
| d924ad90-edcf-3cf8-bce5-e95731495ef8 | -6.6247 | -55.2531 | 2026-09-03 00:00:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 116.2 |
| b7d710ca-8c66-393d-9cd3-7d4eaff0d61c | -9.0414 | -65.7536 | 2026-09-03 00:00:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 70.8 |
| e4e0f82a-6949-337b-a4fd-29aa4ec31922 | -8.4295 | -54.7464 | 2026-09-03 00:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 88.3 |
| 462ce8ab-38f2-351a-a37f-65a544f57356 | -19.0948 | -57.3641 | 2026-09-03 00:00:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 65.9 |
| 8c3052a3-9e92-3ffa-a4b0-e414e9d6614b | -8.911 | -62.372 | 2026-09-03 00:00:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 46.0 |
| c1b3cd41-a39f-38ff-ae1e-222eb6e66ec4 | -10.9013 | -45.3279 | 2026-09-03 00:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 51.1 |
| d1cb5a2e-10d7-380b-a8fa-38ac7bb94e03 | -8.0737 | -50.9656 | 2026-09-03 00:00:00 | GOES-19 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 67.9 |
| 6ba4d284-35a0-3a67-b14c-fb2608a3819a | -8.8925 | -62.3538 | 2026-09-03 00:00:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 58.6 |
| f7db4da2-4101-3adc-a138-01f1f0dfc874 | -8.6132 | -62.5739 | 2026-09-03 00:00:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 71.5 |
| 8ee11da7-bef8-3871-8950-3cfad2902a00 | -6.6764 | -58.7686 | 2026-09-03 00:00:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 92.5 |
| acfa4af9-533a-36f8-88fd-f0469b1c7dfb | -13.4157 | -42.4999 | 2026-09-03 00:00:00 | GOES-19 | BOTUPORÃ | BAHIA | Brasil | 2904209 | 29 | 33 | nan | nan | nan | Caatinga | 101.3 |
| 9e84bdd5-35e9-32e2-a3dd-3534ed8c265a | -6.6541 | -59.4452 | 2026-09-03 00:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 47.3 |
| da39f044-9140-39e3-8c61-afa7235bfca6 | -19.36106 | -47.09568 | 2026-09-03 00:03:00 | TERRA_M-M | PERDIZES | MINAS GERAIS | Brasil | 3149804 | 31 | 33 | nan | nan | nan | Cerrado | 11.5 |
| 5238f101-6db2-3bd2-92ad-0287641e9366 | -19.46894 | -46.1085 | 2026-09-03 00:03:00 | TERRA_M-M | CAMPOS ALTOS | MINAS GERAIS | Brasil | 3111507 | 31 | 33 | nan | nan | nan | Cerrado | 7.2 |
| be710da5-2a1f-3908-9a14-688a5d3c4539 | -22.43615 | -49.77102 | 2026-09-03 00:03:00 | TERRA_M-M | ALVINLÂNDIA | SÃO PAULO | Brasil | 3501509 | 35 | 33 | nan | nan | nan | Mata Atlântica | 12.4 |
| a2b46343-fbd0-37a6-8326-44981902db89 | -19.35222 | -47.0971 | 2026-09-03 00:03:00 | TERRA_M-M | PERDIZES | MINAS GERAIS | Brasil | 3149804 | 31 | 33 | nan | nan | nan | Cerrado | 8.6 |
| f4b6a0ed-f8d0-3411-a615-6682a38e4d48 | -9.15752 | -47.5856 | 2026-09-03 00:05:00 | TERRA_M-M | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 13.7 |
| 7de2a5e6-57cb-3a46-8deb-6d28a105306f | -8.3984 | -45.70762 | 2026-09-03 00:05:00 | TERRA_M-M | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 8.8 |
| 49f6698d-c3fe-35e2-9994-ea7f8b88ce01 | -18.14813 | -51.8097 | 2026-09-03 00:05:00 | TERRA_M-M | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 30.1 |
| 885e9656-3ba6-3101-90db-ec4085afebd6 | -16.7689 | -49.62892 | 2026-09-03 00:05:00 | TERRA_M-M | TRINDADE | GOIÁS | Brasil | 5221403 | 52 | 33 | nan | nan | nan | Cerrado | 55.8 |
| 1b3dafdc-2a6c-3651-a544-7416b904be27 | -10.47774 | -51.32835 | 2026-09-03 00:05:00 | TERRA_M-M | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 2118420c-c676-31f8-a7a3-b36339c84068 | -14.60436 | -41.04856 | 2026-09-03 00:05:00 | TERRA_M-M | ANAGÉ | BAHIA | Brasil | 2901205 | 29 | 33 | nan | nan | nan | Caatinga | 51.7 |
| 2b1199ca-cefd-36e0-9a64-a5eb33a85953 | -9.6111 | -48.56852 | 2026-09-03 00:05:00 | TERRA_M-M | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 19.8 |
| 99bc5863-1b1a-36ca-92cc-310076199a15 | -14.21567 | -42.05373 | 2026-09-03 00:05:00 | TERRA_M-M | RIO DO ANTÔNIO | BAHIA | Brasil | 2926806 | 29 | 33 | nan | nan | nan | Caatinga | 35.9 |
| 3d73ac1e-e2b8-35c7-aa0e-42995919ea1d | -18.77128 | -48.90956 | 2026-09-03 00:05:00 | TERRA_M-M | MONTE ALEGRE DE MINAS | MINAS GERAIS | Brasil | 3142809 | 31 | 33 | nan | nan | nan | Cerrado | 22.7 |
| c2fbc4f5-a079-36bb-90e1-63b6b6587206 | -11.31516 | -45.12278 | 2026-09-03 00:05:00 | TERRA_M-M | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 12.1 |
| 11e3a0df-0ee6-324a-ad34-51184126f854 | -16.7779 | -49.62763 | 2026-09-03 00:05:00 | TERRA_M-M | CAMPESTRE DE GOIÁS | GOIÁS | Brasil | 5204607 | 52 | 33 | nan | nan | nan | Cerrado | 12.2 |
| 258d3728-5e93-34a1-9367-27bb75878fc4 | -10.56216 | -47.7326 | 2026-09-03 00:05:00 | TERRA_M-M | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 9.0 |
| ec7b4b6a-57f3-3994-adee-943793ac93e8 | -12.17049 | -47.06431 | 2026-09-03 00:05:00 | TERRA_M-M | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 4.7 |
| e13233a5-4444-3727-b602-962897b410aa | -15.07508 | -45.31954 | 2026-09-03 00:05:00 | TERRA_M-M | JANUÁRIA | MINAS GERAIS | Brasil | 3135209 | 31 | 33 | nan | nan | nan | Cerrado | 9.5 |
| a1fd5684-f928-3ff9-a3e6-0ca079d9c743 | -14.08347 | -41.1853 | 2026-09-03 00:05:00 | TERRA_M-M | TANHAÇU | BAHIA | Brasil | 2931004 | 29 | 33 | nan | nan | nan | Caatinga | 28.0 |
| 621d5465-e1c7-333b-9608-7525bb87b8f3 | -11.75586 | -50.48434 | 2026-09-03 00:05:00 | TERRA_M-M | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 27.8 |
| a2710eed-7210-32af-af1d-ca5e164cb13f | -17.85965 | -42.61221 | 2026-09-03 00:05:00 | TERRA_M-M | ARICANDUVA | MINAS GERAIS | Brasil | 3104452 | 31 | 33 | nan | nan | nan | Mata Atlântica | 46.7 |
| 3fc4aa4a-4a94-3841-93d2-01616013c1e5 | -19.10334 | -57.38467 | 2026-09-03 00:05:00 | TERRA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 75.7 |
| 6823907a-a914-368e-8f3a-cb37a92787ba | -13.406 | -42.4927 | 2026-09-03 00:05:00 | TERRA_M-M | BOTUPORÃ | BAHIA | Brasil | 2904209 | 29 | 33 | nan | nan | nan | Caatinga | 98.0 |
| c6894708-8aea-3935-99f9-c56a850d8b93 | -10.2765 | -50.04432 | 2026-09-03 00:05:00 | TERRA_M-M | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 22f2bc8b-b6a2-3bc4-9a42-a95caee43bc8 | -10.3487 | -49.96457 | 2026-09-03 00:05:00 | TERRA_M-M | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 102b6990-4c86-39a7-b710-14b5e810f781 | -11.77127 | -50.46334 | 2026-09-03 00:05:00 | TERRA_M-M | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 75f3dc63-46c7-37fd-af91-5f99555d1f9b | -8.71151 | -47.55704 | 2026-09-03 00:05:00 | TERRA_M-M | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 5.9 |
| f1a35161-ce5e-3142-bc7e-7286376708af | -18.17023 | -51.81968 | 2026-09-03 00:05:00 | TERRA_M-M | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 13.5 |
| 4cd9e6df-4614-33b5-96a5-e38c04ee8667 | -14.61329 | -41.05255 | 2026-09-03 00:05:00 | TERRA_M-M | ANAGÉ | BAHIA | Brasil | 2901205 | 29 | 33 | nan | nan | nan | Caatinga | 55.9 |
| c842132b-3a34-3601-a941-296891c9b8b9 | -16.77014 | -49.63846 | 2026-09-03 00:05:00 | TERRA_M-M | TRINDADE | GOIÁS | Brasil | 5221403 | 52 | 33 | nan | nan | nan | Cerrado | 8.7 |
| b3e9b246-3f70-3dbd-a035-632ac0ee811e | -11.52619 | -49.2093 | 2026-09-03 00:05:00 | TERRA_M-M | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 8edf98e8-b3a4-3777-875f-711dc70cbdbc | -13.4009 | -51.36718 | 2026-09-03 00:05:00 | TERRA_M-M | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 5.2 |
| f90a1ec7-0621-3989-9718-82ab0f69b2a0 | -13.51295 | -43.46911 | 2026-09-03 00:05:00 | TERRA_M-M | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 11.4 |
| 2f618cd4-b17d-327d-bd22-c3a78cc39e02 | -8.38981 | -44.96872 | 2026-09-03 00:05:00 | TERRA_M-M | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 41.4 |
| 3c60eb52-9e88-358e-9376-f3bdbf82f4c6 | -10.24002 | -50.30477 | 2026-09-03 00:05:00 | TERRA_M-M | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 14.8 |
| 9c81bc3d-c696-317e-b4fa-2d70538b2da2 | -11.30645 | -45.13787 | 2026-09-03 00:05:00 | TERRA_M-M | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 18.4 |
| bb616853-d882-3b7f-854d-f988c82fa89b | -10.52758 | -49.99042 | 2026-09-03 00:05:00 | TERRA_M-M | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 3a1baecb-ddf0-390e-9463-2f92508f1ffd | -14.05257 | -48.41037 | 2026-09-03 00:05:00 | TERRA_M-M | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 13.4 |
| 6231633f-0d96-3518-bc8d-4fefe3b19a4a | -18.75594 | -48.93128 | 2026-09-03 00:05:00 | TERRA_M-M | MONTE ALEGRE DE MINAS | MINAS GERAIS | Brasil | 3142809 | 31 | 33 | nan | nan | nan | Cerrado | 12.9 |
| 929d69ea-4439-36b0-8d6b-b2b7f77caffb | -8.46308 | -44.68962 | 2026-09-03 00:05:00 | TERRA_M-M | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 9.4 |
| a3309c23-62f3-3c7a-b04e-d207e9e13bf8 | -18.85359 | -47.14994 | 2026-09-03 00:05:00 | TERRA_M-M | PATROCÍNIO | MINAS GERAIS | Brasil | 3148103 | 31 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 61250a53-0d0e-3cb0-8474-c58d54349c5e | -11.76356 | -50.47384 | 2026-09-03 00:05:00 | TERRA_M-M | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 163.9 |
| 50a27c19-66da-367a-a379-8509b31db920 | -14.1056 | -45.48666 | 2026-09-03 00:05:00 | TERRA_M-M | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 8.6 |
| f202e10b-f349-3607-83a0-339479a76a5b | -12.09682 | -47.06133 | 2026-09-03 00:05:00 | TERRA_M-M | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 6.6 |


[Clique aqui para ver as próximas entradas](README2.md)
