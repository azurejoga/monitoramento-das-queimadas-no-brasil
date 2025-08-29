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

## Dados Diários - Página 51

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 0439afd4-5a94-35ff-a103-c3afd1225b0d | -8.29885 | -61.40227 | 2025-08-29 04:40:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 2b554ebf-8ce6-3b7c-bbed-d0d1fb709250 | -10.03189 | -48.0696 | 2025-08-29 04:40:00 | NOAA-21 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| ba8645b6-b105-3599-a179-6b79cc89284d | -7.79113 | -50.9707 | 2025-08-29 04:40:00 | NOAA-21 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 93f3a981-6ca4-3063-b349-59510d04f2e1 | -9.1566 | -59.53651 | 2025-08-29 04:40:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c8081ef0-ba0c-3a3c-96f1-daec11709269 | -7.42362 | -44.27709 | 2025-08-29 04:40:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 3.9 |
| c578ec1a-a347-3f70-a38c-db3e5077a36e | -12.91591 | -48.13685 | 2025-08-29 04:40:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| e3781139-336b-3998-94cc-5b9c9a1ecbf2 | -6.24259 | -42.40147 | 2025-08-29 04:40:00 | NOAA-21 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| bfd661f6-c845-3ac5-841e-5f942be36297 | -9.45255 | -48.26202 | 2025-08-29 04:40:00 | NOAA-21 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 645dfc01-9528-3aae-865c-6d71ee05637f | -11.31165 | -55.21856 | 2025-08-29 04:40:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 8a20f239-a581-38e8-a193-5672417b7481 | -7.22098 | -45.45166 | 2025-08-29 04:40:00 | NOAA-21 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| d7e0d299-2d88-37e3-a64c-b07faa421373 | -11.34872 | -43.54891 | 2025-08-29 04:40:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 2aa783a1-74e9-36eb-9802-fe685fe02ac9 | -12.68494 | -48.18414 | 2025-08-29 04:40:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 25aac13a-d860-3439-a365-d92724cc82c3 | -7.22833 | -45.4282 | 2025-08-29 04:40:00 | NOAA-21 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 0deea633-75c1-3927-b142-79989a65c37b | -7.04966 | -44.3588 | 2025-08-29 04:40:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 09f01f2d-90a0-34fc-a9f1-37957ea5362a | -11.90413 | -46.71458 | 2025-08-29 04:40:00 | NOAA-21 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| cd1b4ba3-587f-3dd5-9df6-e03c2c77c72e | -9.68623 | -48.31623 | 2025-08-29 04:40:00 | NOAA-21 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 0390a86e-1aab-3c02-b7de-2e7748d3c7e1 | -10.45103 | -57.95983 | 2025-08-29 04:40:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| e9e4d383-8b66-36c3-9fae-831b07a3a765 | -11.56318 | -47.61885 | 2025-08-29 04:40:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| de14c786-e83d-3a3a-8936-c23cd3b55bbb | -11.26168 | -45.49498 | 2025-08-29 04:40:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 65f65074-8d23-3e04-891e-86b73b33260e | -9.16948 | -60.78241 | 2025-08-29 04:40:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 436bb1d9-1e2d-335d-b431-6858e962b652 | -7.96899 | -46.37073 | 2025-08-29 04:40:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 93feeab8-9adf-3ead-a004-09e5267b4687 | -7.74463 | -50.27445 | 2025-08-29 04:40:00 | NOAA-21 | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 7c5919ca-95b8-3f1f-837a-67385b7d1e4b | -6.94223 | -44.07662 | 2025-08-29 04:40:00 | NOAA-21 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| d6311cdf-d094-391b-a59b-0bee7166d1a3 | -13.19806 | -45.28881 | 2025-08-29 04:40:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 583f235f-f32a-3b53-8421-4d722017e570 | -6.21865 | -43.33603 | 2025-08-29 04:40:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| bd630820-929a-3ed7-be33-98e7c96cbadc | -11.92957 | -46.69926 | 2025-08-29 04:40:00 | NOAA-21 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 87091c5a-de6d-36bc-b162-74eaf9de8af7 | -10.46014 | -57.93605 | 2025-08-29 04:40:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 7.2 |
| dc45300b-f2de-3231-bdd1-eefa2185e448 | -12.68851 | -48.15951 | 2025-08-29 04:40:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 89090b5c-1fd8-35f0-9987-f9e4c533e402 | -6.49667 | -43.53477 | 2025-08-29 04:40:00 | NOAA-21 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ecb0f1dd-fe60-3b25-a2f6-69c7fff20ae3 | -11.06512 | -44.76539 | 2025-08-29 04:40:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 616ba315-9456-35e7-b8ee-7a418d66ac6c | -6.08818 | -44.00055 | 2025-08-29 04:40:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 74500f18-eea3-3088-adf2-86feae493f16 | -7.62594 | -42.72163 | 2025-08-29 04:40:00 | NOAA-21 | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 0d726448-9d05-3488-80e6-833ebc5d8761 | -8.87419 | -50.25297 | 2025-08-29 04:40:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 16e21442-8ed3-3cb0-8919-919f32484c76 | -8.4725 | -43.63999 | 2025-08-29 04:40:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 92a07872-40d9-32cd-895e-d6002e5b37a1 | -10.85867 | -47.49689 | 2025-08-29 04:40:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| dc9679b7-410b-3f49-94ec-51e2d013ae3e | -9.31271 | -57.7025 | 2025-08-29 04:40:00 | NOAA-21 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 9d99df78-d15f-3f6d-ab7b-767e133f0469 | -12.92447 | -46.33987 | 2025-08-29 04:40:00 | NOAA-21 | LAVANDEIRA | TOCANTINS | Brasil | 1712157 | 17 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 14d2c7b0-993b-38ad-b52b-7c83eaa8ea2a | -6.69337 | -44.40665 | 2025-08-29 04:40:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| e5f99137-0744-359b-926d-80bed4f7ca72 | -11.61447 | -46.20574 | 2025-08-29 04:40:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 69db8a90-9eda-312b-acfc-bff7dc5ae679 | -12.87545 | -48.13971 | 2025-08-29 04:40:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| cf66e5ee-9429-3b9c-8745-6b084c5e3bcd | -12.32105 | -47.0473 | 2025-08-29 04:40:00 | NOAA-21 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 5bf26ac8-4a2b-3570-8507-34135f85c45c | -10.93898 | -46.86681 | 2025-08-29 04:40:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 18ad2224-648f-3d06-8b26-2701fe8203d6 | -11.88302 | -46.40023 | 2025-08-29 04:40:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 9989b628-a258-385a-9ea7-26672fdb6dc4 | -6.54135 | -43.9226 | 2025-08-29 04:40:00 | NOAA-21 | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 6.6 |
| cd6b3511-a3ca-3dd0-8f1f-25b37178d8ab | -5.55964 | -52.07034 | 2025-08-29 04:40:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e0468b4e-490e-31c5-9685-e3aeafa2ade7 | -8.17154 | -61.37357 | 2025-08-29 04:40:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 44ec3f8d-684c-3f96-8c45-f7135fe351b5 | -6.70942 | -49.45819 | 2025-08-29 04:40:00 | NOAA-21 | SAPUCAIA | PARÁ | Brasil | 1507755 | 15 | 33 | nan | nan | nan | Amazônia | 7.9 |
| 48d40fc8-1506-3683-85d6-dcfa1e30e0f4 | -6.21925 | -43.33176 | 2025-08-29 04:40:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 12121374-13f8-32ee-8ab6-f984aada10e3 | -11.33102 | -43.57663 | 2025-08-29 04:40:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a3a3fd59-70ce-3347-ac77-3b805edc7433 | -12.69619 | -48.15657 | 2025-08-29 04:40:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 13bccbc3-6ae9-3d47-9818-7e9f28bf94d0 | -9.39756 | -48.23065 | 2025-08-29 04:40:00 | NOAA-21 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 8fde2a70-971d-3a85-a73e-37d5be305698 | -7.21747 | -45.31148 | 2025-08-29 04:40:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 7f0e5523-d0e2-3084-93d3-ef3404cf0899 | -12.84047 | -48.16069 | 2025-08-29 04:40:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 25723663-d7a0-39fa-84c5-ec40fb3dfcf8 | -7.04446 | -44.36577 | 2025-08-29 04:40:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| dd6a1c6c-fd42-3995-b24d-7a0490887987 | -6.54189 | -43.91872 | 2025-08-29 04:40:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 967ef1cc-430d-3b27-95de-5619cf310a23 | -6.81315 | -44.32434 | 2025-08-29 04:40:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 0f2eb3f9-ca71-3d1d-9961-fd868149b170 | -6.85401 | -44.39092 | 2025-08-29 04:40:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| a9181926-b2e0-3e37-8206-6751cbdee1f9 | -11.35399 | -43.54465 | 2025-08-29 04:40:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 5af77ebb-e2d3-362b-aa9c-b070442ecd67 | -9.15034 | -59.57032 | 2025-08-29 04:40:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| e76f4020-12a5-35bc-950e-3bbd6960bcdf | -10.49895 | -51.6162 | 2025-08-29 04:40:00 | NOAA-21 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 262eb168-9714-3a97-93e3-1d3331a8f82c | -8.29278 | -61.40102 | 2025-08-29 04:40:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 61f16d29-c137-3e6a-b77a-322de8212138 | -6.81706 | -44.35614 | 2025-08-29 04:40:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 12a6e47e-76bb-3d93-ae2e-cc3281401d1e | -11.78607 | -51.44122 | 2025-08-29 04:40:00 | NOAA-21 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 1e8066cb-fc89-3625-b808-24fd4e4a5a20 | -9.17526 | -60.78342 | 2025-08-29 04:40:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 51adfd07-246b-3e87-b476-7b713ff69bdb | -6.60298 | -46.65454 | 2025-08-29 04:40:00 | NOAA-21 | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 468ba461-3982-3cb5-ab1d-2b456e6b8356 | -11.08724 | -44.75852 | 2025-08-29 04:40:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| baed2197-090e-3f57-95f3-f294c9d3aa86 | -12.91351 | -48.12819 | 2025-08-29 04:40:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 8370c21b-a577-3755-9f9b-a22b55c809b3 | -8.88931 | -60.74272 | 2025-08-29 04:40:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| f7126a65-56d2-3ce3-9194-c7dbae591afe | -11.56135 | -46.35278 | 2025-08-29 04:40:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 89519021-73f2-3b5d-9f27-0dd47d88df18 | -11.31237 | -43.58267 | 2025-08-29 04:40:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e9572dc9-4b0d-33f4-8f5c-9ab2cdd3896a | -6.13663 | -44.4291 | 2025-08-29 04:40:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| ea7d9463-0ca3-3aa2-afd4-12cb7a7e13c2 | -13.19383 | -45.28822 | 2025-08-29 04:40:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 6798852d-7853-37b5-8fa9-0439f664da8e | -10.9519 | -46.88264 | 2025-08-29 04:40:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 851e928f-5d83-3543-82ee-8fe40486f870 | -10.98209 | -46.90989 | 2025-08-29 04:40:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 17.3 |
| c65ec7de-4c06-34c6-a6c0-3d37de70afc4 | -11.35081 | -43.56942 | 2025-08-29 04:40:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 8.2 |
| bc10d071-087c-3a82-b0aa-d46e7802c4f0 | -6.78432 | -43.76884 | 2025-08-29 04:40:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 6ed24bfa-4c21-30f7-97bf-0724584a0c0f | -8.88852 | -60.74683 | 2025-08-29 04:40:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 93f5313d-e5c4-3bc7-9f79-d13e6e5006f4 | -11.11913 | -45.12016 | 2025-08-29 04:40:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 8f99b9d5-cfdc-3328-b44f-013fec0c025c | -11.22759 | -55.06263 | 2025-08-29 04:40:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 234f27b1-a1b7-38e5-8000-ce56b4cde0a5 | -12.81966 | -48.10367 | 2025-08-29 04:40:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| d33730bb-2985-34a1-99a2-b803e43a46c3 | -9.82502 | -44.89533 | 2025-08-29 04:40:00 | NOAA-21 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 6b45299f-0362-3510-98cd-4976c4f699c3 | -9.46485 | -60.55912 | 2025-08-29 04:40:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 5.0 |
| afabe359-7363-3e6c-a281-67c6a0d7e100 | -12.40187 | -46.50112 | 2025-08-29 04:40:00 | NOAA-21 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 5767a503-f0a9-3bb3-8b72-b5274c51c482 | -6.48972 | -44.40616 | 2025-08-29 04:40:00 | NOAA-21 | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 93e541b0-3e06-3bb6-adc6-9450adc309f8 | -6.7703 | -44.82691 | 2025-08-29 04:40:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 6ab557c0-4f2d-37e7-92dd-bead8cd05381 | -9.41266 | -60.57423 | 2025-08-29 04:40:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 845f3942-e78f-3f44-95cc-18cc6e892f85 | -10.69967 | -47.075 | 2025-08-29 04:40:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| bbec93bc-ad0b-3227-bf29-f541c97b1dbe | -9.17739 | -59.45373 | 2025-08-29 04:40:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 73c9cc89-52a4-3470-8539-57be033d7a31 | -8.70842 | -50.37548 | 2025-08-29 04:40:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 7c3137c6-a2bd-394e-8f62-d76cbb89df1a | -5.90136 | -46.48555 | 2025-08-29 04:40:00 | NOAA-21 | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| cd49f1d6-c3e4-3684-a54d-2d52a3c1f0fd | -10.48135 | -57.96499 | 2025-08-29 04:40:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 5dd8f6b6-938c-301d-a492-ff2f9c1d56c6 | -11.08407 | -44.74978 | 2025-08-29 04:40:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| eddb25b8-93c6-3cf1-a2c9-876ca57bcab8 | -9.45999 | -60.5539 | 2025-08-29 04:40:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 62be29a3-bdfd-3503-b67c-68aa832d00b0 | -11.34935 | -43.54397 | 2025-08-29 04:40:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 47b58bcb-3318-334b-be4b-40d4845f0a78 | -9.82398 | -44.90274 | 2025-08-29 04:40:00 | NOAA-21 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 60205432-f57d-3f64-be55-c85f478166af | -7.42867 | -42.06692 | 2025-08-29 04:40:00 | NOAA-21 | SANTO INÁCIO DO PIAUÍ | PIAUÍ | Brasil | 2209500 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| a2db79a8-b34c-3d2c-97ea-a006278d5286 | -13.19118 | -45.27554 | 2025-08-29 04:40:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 15c0a1ff-27aa-3838-90f6-713599aecc7f | -11.34089 | -43.57315 | 2025-08-29 04:40:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| bc31f561-296a-3bce-9d5d-7a8a3aef1877 | -6.13716 | -44.42555 | 2025-08-29 04:40:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 70eaa97b-af91-3627-b80b-fe7854fc3915 | -8.69578 | -50.39127 | 2025-08-29 04:40:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |


[Clique aqui para ver as próximas entradas](README52.md)
