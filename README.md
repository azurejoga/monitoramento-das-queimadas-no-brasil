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
| d759f443-d3c6-3656-a321-07ef191f4465 | -2.7588 | -54.934 | 2026-01-07 00:00:00 | GOES-19 | BELTERRA | PARÁ | Brasil | 1501451 | 15 | 33 | nan | nan | nan | Amazônia | 65.5 |
| d8d31714-fa81-32f3-9c75-022dcab0b130 | -2.7404 | -54.9344 | 2026-01-07 00:00:00 | GOES-19 | BELTERRA | PARÁ | Brasil | 1501451 | 15 | 33 | nan | nan | nan | Amazônia | 73.3 |
| 2b54adeb-22fa-30de-a388-9fd367e6712b | -9.7018 | -36.1652 | 2026-01-07 00:00:00 | GOES-19 | BOCA DA MATA | ALAGOAS | Brasil | 2701001 | 27 | 33 | nan | nan | nan | Mata Atlântica | 81.3 |
| 02e154ea-84b4-383f-a463-cf58ba1d6ba8 | -2.1605 | -51.9948 | 2026-01-07 00:00:00 | GOES-19 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 69.4 |
| 09dcd732-a097-304d-80d7-aeffc5c1dfea | -21.5837 | -48.6764 | 2026-01-07 00:10:00 | GOES-19 | ITÁPOLIS | SÃO PAULO | Brasil | 3522703 | 35 | 33 | nan | nan | nan | Cerrado | 68.1 |
| 78269bc2-3b33-3315-b531-803dde50fe56 | -2.1605 | -51.9948 | 2026-01-07 00:10:00 | GOES-19 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 77.6 |
| 64492cb9-d5ff-3055-9a27-20043de6675f | -2.7404 | -54.9344 | 2026-01-07 00:10:00 | GOES-19 | BELTERRA | PARÁ | Brasil | 1501451 | 15 | 33 | nan | nan | nan | Amazônia | 64.5 |
| 63e4079a-d46d-3267-bbde-7e7fe9eef323 | -9.7018 | -36.1652 | 2026-01-07 00:10:00 | GOES-19 | BOCA DA MATA | ALAGOAS | Brasil | 2701001 | 27 | 33 | nan | nan | nan | Mata Atlântica | 89.2 |
| 9940086d-c873-354d-a6ca-f3ced8747eb4 | -21.6045 | -48.6715 | 2026-01-07 00:10:00 | GOES-19 | ITÁPOLIS | SÃO PAULO | Brasil | 3522703 | 35 | 33 | nan | nan | nan | Cerrado | 75.6 |
| 52484b93-a58e-3da8-a8c6-bd70fd82b8f4 | -2.7404 | -54.9344 | 2026-01-07 00:20:00 | GOES-19 | BELTERRA | PARÁ | Brasil | 1501451 | 15 | 33 | nan | nan | nan | Amazônia | 52.0 |
| accb07ab-3232-34c5-ac95-823236387f38 | -9.7018 | -36.1652 | 2026-01-07 00:20:00 | GOES-19 | BOCA DA MATA | ALAGOAS | Brasil | 2701001 | 27 | 33 | nan | nan | nan | Mata Atlântica | 85.5 |
| 74bf19a0-872f-361d-af33-dd380cc2ba4b | -2.1605 | -51.9948 | 2026-01-07 00:20:00 | GOES-19 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 62.5 |
| 153db9d0-580d-35e8-a791-ecfa69c41f93 | -2.1605 | -51.9948 | 2026-01-07 01:00:00 | GOES-19 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 58.5 |
| 1317722c-35cd-313a-9fac-55e5a414a0b5 | -2.1605 | -51.9948 | 2026-01-07 01:20:00 | GOES-19 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 57.9 |
| d51600a4-5db1-3e17-8c03-7957113fff90 | -16.158899 | -59.309399 | 2026-01-07 01:21:00 | METOP-B | PORTO ESPERIDIÃO | MATO GROSSO | Brasil | 5106828 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 0f8bfd05-4cea-375a-8bab-49d730126808 | -16.161501 | -59.32 | 2026-01-07 01:21:00 | METOP-B | PORTO ESPERIDIÃO | MATO GROSSO | Brasil | 5106828 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 08639261-5e12-37d9-af09-df52908e42e1 | -16.308201 | -57.552898 | 2026-01-07 01:21:00 | METOP-B | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 0a603fb4-9570-36da-b58f-509a2e3f720c | -16.3179 | -57.550201 | 2026-01-07 01:21:00 | METOP-B | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| f1240070-1a51-3dc4-be69-9fe4ad511157 | -18.7131 | -57.262001 | 2026-01-07 01:21:00 | METOP-B | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 7eb7f85a-a86e-3a66-80cd-6ddd62a1cf96 | -16.31708 | -57.56532 | 2026-01-07 01:26:00 | TERRA_M-M | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 32.6 |
| ba6fc5a0-084a-3995-8c03-12fef2fa8925 | -16.16668 | -59.32061 | 2026-01-07 01:26:00 | TERRA_M-M | PORTO ESPERIDIÃO | MATO GROSSO | Brasil | 5106828 | 51 | 33 | nan | nan | nan | Amazônia | 8.6 |
| adc7ecf5-939c-30a3-bf45-3c2687b0d7de | -10.7 | -40.3981 | 2026-01-07 02:00:00 | GOES-19 | PINDOBAÇU | BAHIA | Brasil | 2924603 | 29 | 33 | nan | nan | nan | Caatinga | 106.9 |
| 3f623031-bc9c-33ee-8e3e-784c080689e9 | -10.7 | -40.3981 | 2026-01-07 02:10:00 | GOES-19 | PINDOBAÇU | BAHIA | Brasil | 2924603 | 29 | 33 | nan | nan | nan | Caatinga | 101.5 |
| bb7df526-cc67-3443-81f2-ccf20dc58656 | -10.6807 | -40.4012 | 2026-01-07 02:10:00 | GOES-19 | PINDOBAÇU | BAHIA | Brasil | 2924603 | 29 | 33 | nan | nan | nan | Caatinga | 121.1 |
| 9e539657-5f99-3bd3-993c-8d72956bc9a9 | -10.6807 | -40.4012 | 2026-01-07 02:20:00 | GOES-19 | PINDOBAÇU | BAHIA | Brasil | 2924603 | 29 | 33 | nan | nan | nan | Caatinga | 161.9 |
| 3cf55a18-3b4f-3ba0-ad88-ead02ec1f639 | -10.7 | -40.3981 | 2026-01-07 02:20:00 | GOES-19 | PINDOBAÇU | BAHIA | Brasil | 2924603 | 29 | 33 | nan | nan | nan | Caatinga | 208.7 |
| 2be926ec-5a5c-3f90-aa74-8f2c3892756c | -10.7 | -40.3981 | 2026-01-07 02:30:00 | GOES-19 | PINDOBAÇU | BAHIA | Brasil | 2924603 | 29 | 33 | nan | nan | nan | Caatinga | 139.1 |
| 3a8b95e9-f5b4-32bb-aaa1-70f39cd9e2ac | -10.6807 | -40.4012 | 2026-01-07 02:30:00 | GOES-19 | PINDOBAÇU | BAHIA | Brasil | 2924603 | 29 | 33 | nan | nan | nan | Caatinga | 84.6 |
| d7c530d4-b318-39da-b40f-b99163b6215f | -10.7 | -40.3981 | 2026-01-07 02:40:00 | GOES-19 | PINDOBAÇU | BAHIA | Brasil | 2924603 | 29 | 33 | nan | nan | nan | Caatinga | 120.9 |
| b0371813-ed1a-3f27-954b-2aff50032e80 | -10.7 | -40.3981 | 2026-01-07 02:50:00 | GOES-19 | PINDOBAÇU | BAHIA | Brasil | 2924603 | 29 | 33 | nan | nan | nan | Caatinga | 88.6 |
| 16a1b606-f938-39f5-93a2-4c35d8a1e94d | -7.50848 | -34.9451 | 2026-01-07 02:51:00 | NOAA-20 | CAAPORÃ | PARAÍBA | Brasil | 2503001 | 25 | 33 | nan | nan | nan | Mata Atlântica | 2.6 |
| 94d2d5d2-1812-3f45-97cd-f56972956676 | -9.6596 | -36.02395 | 2026-01-07 02:53:00 | NOAA-20 | PILAR | ALAGOAS | Brasil | 2706901 | 27 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| eea1cd04-f106-32d6-8829-7de7100526ef | -8.963 | -35.58043 | 2026-01-07 02:53:00 | NOAA-20 | JUNDIÁ | ALAGOAS | Brasil | 2703908 | 27 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 307ca7be-282b-32ca-98e7-08de073994ba | -8.96948 | -35.58157 | 2026-01-07 02:53:00 | NOAA-20 | JUNDIÁ | ALAGOAS | Brasil | 2703908 | 27 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 3c27bd6d-f575-3f11-a52c-853c698c3899 | -9.65297 | -36.023 | 2026-01-07 02:53:00 | NOAA-20 | PILAR | ALAGOAS | Brasil | 2706901 | 27 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 4ed2f737-15f5-3327-a769-0536ceddc1db | -4.43279 | -41.43873 | 2026-01-07 03:42:00 | NOAA-21 | PEDRO II | PIAUÍ | Brasil | 2207900 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| cbbdca07-0566-345d-b190-5420c0ba37de | -6.96792 | -34.93994 | 2026-01-07 03:42:00 | NOAA-21 | SANTA RITA | PARAÍBA | Brasil | 2513703 | 25 | 33 | nan | nan | nan | Mata Atlântica | 3.1 |
| 14a6d2f1-58bf-34bf-90c1-962c9a689ee9 | -3.91397 | -40.69625 | 2026-01-07 03:42:00 | NOAA-21 | CARIRÉ | CEARÁ | Brasil | 2303105 | 23 | 33 | nan | nan | nan | Caatinga | 8.4 |
| cae21fd2-ac7f-3392-894e-e5e50676c838 | -3.53153 | -39.72988 | 2026-01-07 03:42:00 | NOAA-21 | ITAPIPOCA | CEARÁ | Brasil | 2306405 | 23 | 33 | nan | nan | nan | Caatinga | 1.9 |
| cf0102f5-2a82-3638-874c-2668cc182b12 | -6.96846 | -34.93647 | 2026-01-07 03:42:00 | NOAA-21 | SANTA RITA | PARAÍBA | Brasil | 2513703 | 25 | 33 | nan | nan | nan | Mata Atlântica | 3.1 |
| cb5e062a-c63c-3fe5-abd7-2770c5a34dda | -6.974 | -34.94445 | 2026-01-07 03:42:00 | NOAA-21 | SANTA RITA | PARAÍBA | Brasil | 2513703 | 25 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| ef464c4c-e8b9-3f52-9303-58f3affb21a1 | -4.74108 | -38.72481 | 2026-01-07 03:42:00 | NOAA-21 | IBARETAMA | CEARÁ | Brasil | 2305266 | 23 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 3398a904-2a0c-3573-b577-81b195bede2d | -4.56871 | -37.9832 | 2026-01-07 03:42:00 | NOAA-21 | ARACATI | CEARÁ | Brasil | 2301109 | 23 | 33 | nan | nan | nan | Caatinga | 0.5 |
| be753257-6cf5-364c-a998-84740fda2722 | -2.91553 | -40.51814 | 2026-01-07 03:42:00 | NOAA-21 | JIJOCA DE JERICOACOARA | CEARÁ | Brasil | 2307254 | 23 | 33 | nan | nan | nan | Caatinga | 1.2 |
| d33d791c-d355-3244-bf98-c8460a3f828b | -5.5327 | -35.69684 | 2026-01-07 03:42:00 | NOAA-21 | POÇO BRANCO | RIO GRANDE DO NORTE | Brasil | 2410108 | 24 | 33 | nan | nan | nan | Caatinga | 1.0 |
| d8ac58cf-56be-3ce9-a104-9d91319b9c6a | -4.43569 | -41.4387 | 2026-01-07 03:42:00 | NOAA-21 | PEDRO II | PIAUÍ | Brasil | 2207900 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 80329ded-1837-37cd-afdd-d5e24b2b510e | -6.84758 | -35.18668 | 2026-01-07 03:42:00 | NOAA-21 | ITAPOROROCA | PARAÍBA | Brasil | 2507101 | 25 | 33 | nan | nan | nan | Mata Atlântica | 2.9 |
| c88f2788-987f-3899-87c2-1a4a2abcc72a | -3.6989 | -43.43507 | 2026-01-07 03:42:00 | NOAA-21 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 7522e921-bdfc-3a6d-ba72-1b36ac245c81 | -4.51326 | -43.6944 | 2026-01-07 03:42:00 | NOAA-21 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 87fff8af-6443-38fb-a32f-2bd52c7e9ab8 | -4.51379 | -43.69128 | 2026-01-07 03:42:00 | NOAA-21 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 6416a4ad-a760-3514-b1c8-d1e494ba35a4 | -1.91497 | -46.959 | 2026-01-07 03:42:00 | NOAA-21 | SANTA LUZIA DO PARÁ | PARÁ | Brasil | 1506559 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| d9b6a650-3a98-3b37-900e-ef6fde704f11 | -5.51932 | -40.41942 | 2026-01-07 03:42:00 | NOAA-21 | INDEPENDÊNCIA | CEARÁ | Brasil | 2305605 | 23 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 18b01b7b-a8d4-318d-aba2-b723ae417202 | -6.17197 | -35.37304 | 2026-01-07 03:42:00 | NOAA-21 | BREJINHO | RIO GRANDE DO NORTE | Brasil | 2401800 | 24 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 4584c693-d9cc-3f49-9dc1-c84b0e9a4f39 | -3.53095 | -39.73338 | 2026-01-07 03:42:00 | NOAA-21 | ITAPIPOCA | CEARÁ | Brasil | 2306405 | 23 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 19ededa8-9dbd-3ceb-8b18-5f2972e7b2d4 | -6.97123 | -34.94046 | 2026-01-07 03:42:00 | NOAA-21 | SANTA RITA | PARAÍBA | Brasil | 2513703 | 25 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 7fd84dc6-46bb-3adf-874a-45e1f5d72d32 | -4.57147 | -37.79222 | 2026-01-07 03:42:00 | NOAA-21 | ARACATI | CEARÁ | Brasil | 2301109 | 23 | 33 | nan | nan | nan | Caatinga | 2.1 |
| ab152889-c1da-353c-8068-2e6d32edff12 | -5.51993 | -40.41575 | 2026-01-07 03:42:00 | NOAA-21 | INDEPENDÊNCIA | CEARÁ | Brasil | 2305605 | 23 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 14ba8de4-264d-3acd-b3a9-3727c801d08f | -1.91174 | -46.95452 | 2026-01-07 03:42:00 | NOAA-21 | SANTA LUZIA DO PARÁ | PARÁ | Brasil | 1506559 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 309248a4-e037-31ec-b314-c071813458cc | -5.45109 | -39.13852 | 2026-01-07 03:42:00 | NOAA-21 | QUIXERAMOBIM | CEARÁ | Brasil | 2311405 | 23 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 67effff5-51a8-3ec6-8162-ca366f8e9e9a | -3.69941 | -43.43201 | 2026-01-07 03:42:00 | NOAA-21 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 74930ccd-f5bd-3a08-9b96-2d01f46b5177 | -3.53037 | -39.73688 | 2026-01-07 03:42:00 | NOAA-21 | ITAPIPOCA | CEARÁ | Brasil | 2306405 | 23 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 70f192f8-2226-3b96-9fbf-e2aed2927018 | -4.17067 | -40.82934 | 2026-01-07 03:42:00 | NOAA-21 | GUARACIABA DO NORTE | CEARÁ | Brasil | 2305001 | 23 | 33 | nan | nan | nan | Caatinga | 0.6 |
| bce10ddc-8917-3525-bb50-4ad1afe1125d | -4.51845 | -43.69531 | 2026-01-07 03:42:00 | NOAA-21 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 2ff71910-791a-3e5d-bbe0-70e628ca8962 | -4.44489 | -38.23485 | 2026-01-07 03:42:00 | NOAA-21 | BEBERIBE | CEARÁ | Brasil | 2302206 | 23 | 33 | nan | nan | nan | Caatinga | 0.9 |
| e6e05e30-5633-3402-9e34-5688d65a5f7b | -7.11393 | -35.2254 | 2026-01-07 03:44:00 | NOAA-21 | SAPÉ | PARAÍBA | Brasil | 2515302 | 25 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 9689cc20-fd71-3b20-88dd-64551e6f02ad | -10.69313 | -40.40771 | 2026-01-07 03:44:00 | NOAA-21 | PINDOBAÇU | BAHIA | Brasil | 2924603 | 29 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 102fde8e-4df7-3cca-b22f-c8e6f85d5d49 | -10.68498 | -40.40895 | 2026-01-07 03:44:00 | NOAA-21 | PINDOBAÇU | BAHIA | Brasil | 2924603 | 29 | 33 | nan | nan | nan | Caatinga | 7.0 |
| 25df78de-bd75-3582-8804-e189bc7bd390 | -7.17205 | -35.1352 | 2026-01-07 03:44:00 | NOAA-21 | CRUZ DO ESPÍRITO SANTO | PARAÍBA | Brasil | 2504900 | 25 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 018bc6db-762b-3f60-b2d6-29fe5c7733c1 | -8.29128 | -36.4986 | 2026-01-07 03:44:00 | NOAA-21 | BELO JARDIM | PERNAMBUCO | Brasil | 2601706 | 26 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 7af93d8d-dde5-3f2e-b106-fbc7cd67c3e3 | -5.97647 | -44.29049 | 2026-01-07 03:44:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| f573e10b-0575-3162-ac00-071e57a37432 | -10.36953 | -39.06836 | 2026-01-07 03:44:00 | NOAA-21 | CANUDOS | BAHIA | Brasil | 2906824 | 29 | 33 | nan | nan | nan | Caatinga | 3.5 |
| d131754d-9b2e-3301-8738-9d1a6cd00121 | -5.82535 | -44.13401 | 2026-01-07 03:44:00 | NOAA-21 | JATOBÁ | MARANHÃO | Brasil | 2105450 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 905f54ce-7808-35e6-8d3d-172be2ef2d7a | -5.81896 | -44.13956 | 2026-01-07 03:44:00 | NOAA-21 | JATOBÁ | MARANHÃO | Brasil | 2105450 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 8ed1aa75-67a8-3fed-927b-b87e08ca3c65 | -10.68879 | -40.40947 | 2026-01-07 03:44:00 | NOAA-21 | PINDOBAÇU | BAHIA | Brasil | 2924603 | 29 | 33 | nan | nan | nan | Caatinga | 7.0 |
| dd4ec652-c5ce-3cff-b5fd-422ce1c47171 | -10.69255 | -40.41024 | 2026-01-07 03:44:00 | NOAA-21 | PINDOBAÇU | BAHIA | Brasil | 2924603 | 29 | 33 | nan | nan | nan | Caatinga | 3.3 |
| 2c156b71-8f8d-344e-8ce7-f328dd8f866e | -6.99669 | -35.23542 | 2026-01-07 03:44:00 | NOAA-21 | SAPÉ | PARAÍBA | Brasil | 2515302 | 25 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 337c5278-6941-32f6-a567-e403f22db103 | -5.81954 | -44.1363 | 2026-01-07 03:44:00 | NOAA-21 | JATOBÁ | MARANHÃO | Brasil | 2105450 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 5158f590-545f-3768-8e21-c9988b53c6a6 | -5.82478 | -44.13722 | 2026-01-07 03:44:00 | NOAA-21 | JATOBÁ | MARANHÃO | Brasil | 2105450 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 8e36a1b5-b921-3ed7-b6ec-863709514fff | -10.37024 | -39.06542 | 2026-01-07 03:44:00 | NOAA-21 | CANUDOS | BAHIA | Brasil | 2906824 | 29 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 5e81fb37-180d-3264-81bf-424af60c6ad3 | -10.68939 | -40.40684 | 2026-01-07 03:44:00 | NOAA-21 | PINDOBAÇU | BAHIA | Brasil | 2924603 | 29 | 33 | nan | nan | nan | Caatinga | 6.4 |
| 264103d0-70ea-3d5c-a8ed-8a2e6548ee14 | -10.68587 | -40.4039 | 2026-01-07 03:44:00 | NOAA-21 | PINDOBAÇU | BAHIA | Brasil | 2924603 | 29 | 33 | nan | nan | nan | Caatinga | 7.0 |
| 1d6af81f-433e-3725-867f-84d32b89a4cc | -9.66299 | -36.01938 | 2026-01-07 03:44:00 | NOAA-21 | MARECHAL DEODORO | ALAGOAS | Brasil | 2704708 | 27 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| 79d4c3c6-a86b-3b79-8638-22e429f82b79 | -10.68177 | -40.40582 | 2026-01-07 03:44:00 | NOAA-21 | PINDOBAÇU | BAHIA | Brasil | 2924603 | 29 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 0ac37a1b-5693-3dc0-9fa4-c5bf2153ae9c | -9.2452 | -35.36353 | 2026-01-07 03:44:00 | NOAA-21 | SÃO MIGUEL DOS MILAGRES | ALAGOAS | Brasil | 2708709 | 27 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| b59fd80b-7f58-3e91-b3ec-df8c50c5ebb4 | -10.36958 | -39.06945 | 2026-01-07 03:44:00 | NOAA-21 | CANUDOS | BAHIA | Brasil | 2906824 | 29 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 7c3eac6d-28c6-352e-bc4e-0a13df97ff6a | -5.81904 | -44.13893 | 2026-01-07 03:44:00 | NOAA-21 | JATOBÁ | MARANHÃO | Brasil | 2105450 | 21 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 9d8c47b5-e78c-30a7-acb3-7bde0f63b247 | -10.69233 | -40.41254 | 2026-01-07 03:44:00 | NOAA-21 | PINDOBAÇU | BAHIA | Brasil | 2924603 | 29 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 4f65f663-ac0e-335a-98c0-b9a4fe2a0313 | -10.68561 | -40.40617 | 2026-01-07 03:44:00 | NOAA-21 | PINDOBAÇU | BAHIA | Brasil | 2924603 | 29 | 33 | nan | nan | nan | Caatinga | 6.4 |
| a590f730-8056-3164-b011-87e688a1fa31 | -5.97121 | -44.28941 | 2026-01-07 03:44:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| e6307b19-9082-3a42-acb0-895568100a1a | -11.02004 | -37.46228 | 2026-01-07 03:44:00 | NOAA-21 | SALGADO | SERGIPE | Brasil | 2806206 | 28 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| f274896a-be5d-3d65-a622-64353e319bc7 | -10.68475 | -40.41132 | 2026-01-07 03:44:00 | NOAA-21 | PINDOBAÇU | BAHIA | Brasil | 2924603 | 29 | 33 | nan | nan | nan | Caatinga | 6.4 |
| 454454ac-1a1f-3490-9699-7e75997a1343 | -7.51203 | -34.93977 | 2026-01-07 03:44:00 | NOAA-21 | CAAPORÃ | PARAÍBA | Brasil | 2503001 | 25 | 33 | nan | nan | nan | Mata Atlântica | 3.5 |
| ac4d04fb-0a1e-325e-80f2-127c6ca4d11a | -7.35859 | -38.6387 | 2026-01-07 03:44:00 | NOAA-21 | MAURITI | CEARÁ | Brasil | 2308104 | 23 | 33 | nan | nan | nan | Caatinga | 1.9 |
| a537d2d9-9da8-3d88-a37b-6861cae81ad1 | -10.68856 | -40.41182 | 2026-01-07 03:44:00 | NOAA-21 | PINDOBAÇU | BAHIA | Brasil | 2924603 | 29 | 33 | nan | nan | nan | Caatinga | 6.4 |
| 2da238f3-c3bf-3592-bf17-2977e4388e56 | -11.0621 | -38.4388 | 2026-01-07 03:44:00 | NOAA-21 | RIBEIRA DO AMPARO | BAHIA | Brasil | 2926509 | 29 | 33 | nan | nan | nan | Caatinga | 1.3 |
| e3074cde-85cd-35e5-829e-1da56be661e2 | -11.01671 | -37.46171 | 2026-01-07 03:44:00 | NOAA-21 | SALGADO | SERGIPE | Brasil | 2806206 | 28 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| ad0b7231-120e-3246-81a2-11b59e749b14 | -10.51062 | -40.42747 | 2026-01-07 03:44:00 | NOAA-21 | CAMPO FORMOSO | BAHIA | Brasil | 2906006 | 29 | 33 | nan | nan | nan | Caatinga | 0.8 |
| a1d874c2-496f-3867-8297-2df98140d214 | -9.2342 | -40.50726 | 2026-01-07 03:44:00 | NOAA-21 | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 1.1 |
| a3ce9ce3-500a-3feb-bb27-7af38332e73c | -8.29403 | -36.50267 | 2026-01-07 03:44:00 | NOAA-21 | BELO JARDIM | PERNAMBUCO | Brasil | 2601706 | 26 | 33 | nan | nan | nan | Caatinga | 1.3 |
| bf46edac-8388-3ebe-a3b5-735d9ed43e81 | -8.55693 | -35.52588 | 2026-01-07 03:44:00 | NOAA-21 | JOAQUIM NABUCO | PERNAMBUCO | Brasil | 2608206 | 26 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |


[Clique aqui para ver as próximas entradas](README2.md)
