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

## Dados Diários - Página 35

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 5d291c24-2b20-3998-836b-7ce006a33724 | -6.31396 | -43.76506 | 2025-08-24 04:32:00 | NOAA-21 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 49be6588-f25c-3b15-bfcc-a140d0434da9 | -2.91699 | -48.30836 | 2025-08-24 04:32:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 69b78f6f-aa3d-3267-a75d-b9513fb3b6fc | -1.66493 | -50.46144 | 2025-08-24 04:32:00 | NOAA-21 | BREVES | PARÁ | Brasil | 1501808 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f92f7ca3-71ce-36f6-9a75-1e318694da3c | -5.58207 | -45.80362 | 2025-08-24 04:32:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| c2fcf5a2-8698-3bbf-b910-f727eb8da39a | -2.25735 | -47.85091 | 2025-08-24 04:32:00 | NOAA-21 | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 8e0d8df1-b27d-3c90-ab03-9d5a9f734ac1 | -4.58224 | -48.03609 | 2025-08-24 04:32:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d46321f3-ba7f-3768-8e3e-d1a748877d9a | -4.09603 | -48.7466 | 2025-08-24 04:32:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 89901b59-5909-378f-b1bb-2dda1217ff5f | -6.21949 | -44.11561 | 2025-08-24 04:32:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 0c27cb65-0c88-34f9-afb9-a46f486226e1 | -5.80704 | -45.40427 | 2025-08-24 04:32:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a474a55e-e19e-3220-9c53-f41741ec479d | -6.77027 | -44.31577 | 2025-08-24 04:32:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 1b7a9036-21c2-35a4-a9d7-a8324b8b23a8 | -9.25122 | -48.19436 | 2025-08-24 04:34:00 | NOAA-21 | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 4.7 |
| e20ade5a-b670-3731-9070-91f3e9c770bb | -7.61535 | -45.2447 | 2025-08-24 04:34:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 655997fe-68b8-3dc3-ad90-9e99a69dbe5c | -10.58014 | -47.14851 | 2025-08-24 04:34:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 0e887e2d-cf86-3af0-9d5d-f63c8bc4f95e | -12.72948 | -48.1171 | 2025-08-24 04:34:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.9 |
| b02a454d-25a2-35e8-bc61-3c1081ad0c2f | -9.24889 | -59.63696 | 2025-08-24 04:34:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 83b62a65-2c21-3060-89db-ef389d6fbc35 | -8.71601 | -51.13987 | 2025-08-24 04:34:00 | NOAA-21 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 0a283700-c241-3e58-8224-00f35af9fc94 | -11.33358 | -47.84561 | 2025-08-24 04:34:00 | NOAA-21 | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| cbc2d340-f3b6-3d79-a1ed-51f0f5990e57 | -11.32857 | -47.85594 | 2025-08-24 04:34:00 | NOAA-21 | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 64404ed4-dfd2-35b4-bed7-e337231dd742 | -13.05237 | -45.22345 | 2025-08-24 04:34:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 8489ebaf-6b4d-3128-8a7a-1840a52eac82 | -13.16386 | -46.93196 | 2025-08-24 04:34:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 95ca7784-941b-3010-a6ec-9e0ef683d7e3 | -6.58002 | -59.87263 | 2025-08-24 04:34:00 | NOAA-21 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| cb37eefc-af64-37a0-9751-5199e0ad11a1 | -6.11811 | -53.78298 | 2025-08-24 04:34:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 586c073c-4d13-38ce-8353-c8cf7a1ad689 | -8.55054 | -48.87053 | 2025-08-24 04:34:00 | NOAA-21 | ITAPORÃ DO TOCANTINS | TOCANTINS | Brasil | 1711100 | 17 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 3686da8e-8ebd-3f04-8df3-53279b3efaff | -7.65393 | -46.28789 | 2025-08-24 04:34:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 26ab5060-39ea-3311-bc04-97533e7ca556 | -13.44086 | -47.03706 | 2025-08-24 04:34:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| fcb09cdc-093c-3f3e-ba48-b4d163a261ff | -11.53295 | -51.91374 | 2025-08-24 04:34:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 96eae0eb-635e-3710-9729-55a39f8dcb49 | -8.91175 | -62.44159 | 2025-08-24 04:34:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 3.1 |
| a27e3a78-0bc7-328d-886e-0505c27cdca8 | -12.72779 | -48.10559 | 2025-08-24 04:34:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 30c84b11-842e-397d-8ce9-d45f9ec7b06b | -11.18212 | -55.02834 | 2025-08-24 04:34:00 | NOAA-21 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 2bb44555-8e15-320b-a330-1db4db49cb44 | -5.74355 | -57.58076 | 2025-08-24 04:34:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 1eea28ea-4560-3776-a76f-3a25ad3af50d | -9.17181 | -59.59078 | 2025-08-24 04:34:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| e6c5be87-878f-3992-b948-cb80edcb5338 | -7.60438 | -46.26888 | 2025-08-24 04:34:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 50ac5b79-a1d8-3a8b-a4d6-528fa9caa367 | -9.15817 | -59.5031 | 2025-08-24 04:34:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| d5442315-a8c3-393d-b87f-33f5e4b79fb8 | -11.18704 | -55.02509 | 2025-08-24 04:34:00 | NOAA-21 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e0a4764a-e336-3053-81b9-134401d129d0 | -9.73653 | -47.93689 | 2025-08-24 04:34:00 | NOAA-21 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 9ac2c991-b41a-33af-a312-fe010533bcfa | -6.43218 | -53.3831 | 2025-08-24 04:34:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| f4440b9e-1584-31bb-93a3-2e37a17d2775 | -11.54837 | -51.90808 | 2025-08-24 04:34:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 59526842-8e18-3432-abc3-62b7e6fa8940 | -13.38612 | -47.52532 | 2025-08-24 04:34:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 77ac9e8a-1c9f-364c-9892-0ba9e5c7842b | -9.95524 | -60.19706 | 2025-08-24 04:34:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| d03107f4-3b5d-37d7-b8e2-3027a260b3cc | -13.04607 | -45.21264 | 2025-08-24 04:34:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| f4476a48-38e2-38e0-a61c-6b3eca24e0e0 | -10.80708 | -46.40513 | 2025-08-24 04:34:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 98809873-c51b-3061-bdc2-6b58d3df44b0 | -6.42807 | -53.38243 | 2025-08-24 04:34:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 9bcf37e9-79ea-3e3a-b258-a5aebc0d0412 | -11.93801 | -46.73233 | 2025-08-24 04:34:00 | NOAA-21 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 54739483-f2fc-3b6c-a42c-34bfa0da6457 | -8.92247 | -62.43668 | 2025-08-24 04:34:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 82f8daf0-2dc4-3d6d-a744-e10e102f8fa2 | -7.0208 | -44.64118 | 2025-08-24 04:34:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 039f33f9-ef86-3a2e-9375-75ce147707ca | -9.5228 | -60.55944 | 2025-08-24 04:34:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| d73b730b-4ce0-38dd-a44a-9c10ff4f5e2b | -6.87309 | -59.82005 | 2025-08-24 04:34:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 65b796b0-963d-358d-a8eb-03f78d384875 | -11.15827 | -44.70856 | 2025-08-24 04:34:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 1982f45c-f6b8-3690-adff-e10e3eea6811 | -11.54098 | -51.86562 | 2025-08-24 04:34:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 2143bd70-238f-36cf-b665-3d84a5fdeecf | -7.65219 | -46.27624 | 2025-08-24 04:34:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 83fe3d4a-fc8c-3c15-bd70-8c61f96ecc45 | -11.60581 | -46.23735 | 2025-08-24 04:34:00 | NOAA-21 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 8ca9dcd7-d220-3309-8e7c-5102313bed00 | -11.31182 | -47.85307 | 2025-08-24 04:34:00 | NOAA-21 | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| f8ce20b1-95d9-344d-8203-a45c5477ba1f | -9.16767 | -59.59231 | 2025-08-24 04:34:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 57b8fb22-6988-364b-a3d6-32c047467a03 | -5.74947 | -57.57962 | 2025-08-24 04:34:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| b71ac9a9-6a20-3a60-9f09-1ea7b017597c | -12.49432 | -53.82633 | 2025-08-24 04:34:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| d71fdcb6-bb1a-36a4-97f8-dd9c22c3e7f9 | -11.90565 | -47.11797 | 2025-08-24 04:34:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 97bf2db2-454c-3090-b922-5e5c2d24612a | -11.05547 | -44.61536 | 2025-08-24 04:34:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 72c5dede-2ecd-3160-8010-001bcf0a543c | -9.18491 | -59.45917 | 2025-08-24 04:34:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 1a9b72af-b72c-33d4-9a26-c921c2a2417a | -5.45786 | -60.18746 | 2025-08-24 04:34:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 4.9 |
| d3606fd6-965b-3c7f-8a62-e2410b06e54e | -11.3275 | -47.86295 | 2025-08-24 04:34:00 | NOAA-21 | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | 6.7 |
| a31d1f0e-87b0-3cdd-8d2e-d9843c3f156a | -5.6112 | -60.22644 | 2025-08-24 04:34:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 7cd26bf3-f767-3efd-bc3b-be1875ee8012 | -6.88901 | -45.69274 | 2025-08-24 04:34:00 | NOAA-21 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| f8d7c1c3-202e-3eb7-af45-45f30442cf3c | -8.22284 | -45.11396 | 2025-08-24 04:34:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 7fab966b-c6d8-33a4-bb45-c2346413f2f1 | -5.45687 | -60.19297 | 2025-08-24 04:34:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 4.9 |
| b9489672-6564-3fcd-8442-e452da16a0b6 | -7.75321 | -47.35236 | 2025-08-24 04:34:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 8f5dd808-8eec-3f75-9f65-a2161cb4ba7c | -9.81733 | -46.44215 | 2025-08-24 04:34:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 7ed8cbe4-e5dd-3b40-9acc-e6466f85e500 | -5.86141 | -52.08324 | 2025-08-24 04:34:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 33c3e4e8-4de1-30e6-8134-c596bc9514d6 | -6.89656 | -45.68999 | 2025-08-24 04:34:00 | NOAA-21 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 7194e230-c9af-329c-a7f6-d459ac8cf64e | -8.90435 | -62.45475 | 2025-08-24 04:34:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 72be7d9e-7f7f-3945-960b-60fdda590261 | -8.90187 | -62.41842 | 2025-08-24 04:34:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 6.0 |
| c7a89ff2-16e9-3cdd-a362-e1c0a1c75f6f | -7.75654 | -47.35288 | 2025-08-24 04:34:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 95c4204e-951a-3c71-b9d9-8fbb0ab25d94 | -13.03814 | -45.24111 | 2025-08-24 04:34:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| fe853d43-33f2-3046-b317-844f439435f1 | -7.02512 | -44.63737 | 2025-08-24 04:34:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 13.3 |
| af46fe5d-34f2-3503-be9a-aa1f6b7fc3e1 | -9.2497 | -59.6326 | 2025-08-24 04:34:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 44c5b98d-b807-301e-926c-8295ce510e7e | -7.439 | -60.63033 | 2025-08-24 04:34:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 96d0e468-c52b-35d2-a1a7-799fb8f94416 | -8.86242 | -52.04579 | 2025-08-24 04:34:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| c018a063-650f-3786-8177-c4a9b1edae66 | -8.5329 | -48.87487 | 2025-08-24 04:34:00 | NOAA-21 | ITAPORÃ DO TOCANTINS | TOCANTINS | Brasil | 1711100 | 17 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 15faacd7-e822-3a9b-bae0-8025b35bf8ca | -7.17361 | -47.58171 | 2025-08-24 04:34:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ee93f669-caae-3af7-a519-eaca5c174700 | -9.40001 | -47.35533 | 2025-08-24 04:34:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| e828e208-24a7-364e-b8c1-9a3bb92b4178 | -10.59489 | -50.17783 | 2025-08-24 04:34:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 0eef36d5-c869-3fa0-95dc-de601d50dcea | -8.12425 | -47.14454 | 2025-08-24 04:34:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| eae81cfa-14ab-3db3-8072-2cb366fc448a | -5.43378 | -60.17191 | 2025-08-24 04:34:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 8.2 |
| b4e19524-92d0-3a2f-bf5a-6a99cb93ffd6 | -5.7427 | -57.58601 | 2025-08-24 04:34:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 0bc3a485-8700-36e2-9b14-b45e38eee1cb | -8.76798 | -49.97006 | 2025-08-24 04:34:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 61fa3436-2729-3d95-8579-a3395427fee3 | -8.15107 | -47.30572 | 2025-08-24 04:34:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| cd171fdd-adfe-3953-9d39-b130dfdeae3c | -5.75251 | -57.59501 | 2025-08-24 04:34:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d103453b-1153-371a-b396-35fa848d1875 | -6.87548 | -59.81852 | 2025-08-24 04:34:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.2 |
| ee1cea9e-bdc7-3a24-8583-bd6c48b1c168 | -13.4133 | -51.81207 | 2025-08-24 04:34:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 105a6ee3-43bf-3a4e-9f78-54807d06b979 | -10.54211 | -47.1463 | 2025-08-24 04:34:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 757127d6-21c1-3bdd-9168-dec17aedab6f | -6.87625 | -45.68276 | 2025-08-24 04:34:00 | NOAA-21 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b2bf0918-45be-3284-8409-dec4da25bc0a | -11.53227 | -51.91777 | 2025-08-24 04:34:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 8e182700-85d1-34c4-8aaa-aa7c70c72f1d | -7.13732 | -44.16409 | 2025-08-24 04:34:00 | NOAA-21 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| c169a213-9065-332e-9dfa-cf88d412168a | -13.49976 | -47.0331 | 2025-08-24 04:34:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 3b69131c-160e-3583-804f-b8db32182ff1 | -11.10495 | -44.78001 | 2025-08-24 04:34:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 3e69c7f1-4851-374b-be07-838605159a85 | -7.78361 | -61.57432 | 2025-08-24 04:34:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| bb51566f-feb1-3f51-bced-61ae55331ab7 | -11.69696 | -60.18613 | 2025-08-24 04:34:00 | NOAA-21 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 2.5 |
| ffcb65d4-28d3-3200-aa64-a26e23b3d186 | -10.82762 | -46.41189 | 2025-08-24 04:34:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 2c63f019-6b0b-3fa4-8681-65a8d2bc4b9f | -11.31517 | -47.85367 | 2025-08-24 04:34:00 | NOAA-21 | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 20383ad3-5876-38c3-bede-f183675eb966 | -11.31626 | -47.84642 | 2025-08-24 04:34:00 | NOAA-21 | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 4a194437-f369-310c-88e3-37918c793d73 | -13.41548 | -51.82032 | 2025-08-24 04:34:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |


[Clique aqui para ver as próximas entradas](README36.md)
