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
| 24b337e2-4043-3100-831f-a002e5da2322 | -10.03775 | -59.09665 | 2025-07-24 05:04:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 97fc3846-8480-3139-a73a-a85fdc934a71 | -7.25666 | -60.18556 | 2025-07-24 05:04:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 574e59e1-519c-3189-beda-dca24a4d263d | -9.53127 | -63.63055 | 2025-07-24 05:04:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 433b8dff-272e-3af3-8da5-6ba0ff3e02c2 | -10.03878 | -59.35802 | 2025-07-24 05:04:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 912fa090-cb05-3998-8a80-6c81b36ee77b | -8.49027 | -47.23689 | 2025-07-24 05:04:00 | NOAA-20 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 20.6 |
| 0a04d0a5-9250-3d04-a95e-8cf7eb527cba | -10.05921 | -59.09623 | 2025-07-24 05:04:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6b34a97d-f4a3-3801-a7a2-916b4dcb7120 | -9.24927 | -58.74855 | 2025-07-24 05:04:00 | NOAA-20 | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| c190ae40-e40e-3ec1-a04f-bd44ef7931bf | -7.25446 | -43.07458 | 2025-07-24 05:04:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 17.1 |
| cd60ae35-2949-3512-bd3d-b3143ad8bf06 | -7.46532 | -49.40338 | 2025-07-24 05:04:00 | NOAA-20 | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| df3e5233-d7ca-3c1c-ae56-f49317ed67d7 | -8.4779 | -49.55083 | 2025-07-24 05:04:00 | NOAA-20 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ec833f49-34b9-315a-bcf1-5e68e56678c7 | -10.29632 | -60.54019 | 2025-07-24 05:04:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 3d1b7631-e6f7-3bf3-97f2-8bffe69e5890 | -9.3555 | -58.84357 | 2025-07-24 05:04:00 | NOAA-20 | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 360c1bb6-4ccf-3101-a142-c627592c7758 | -10.70804 | -48.8578 | 2025-07-24 05:04:00 | NOAA-20 | OLIVEIRA DE FÁTIMA | TOCANTINS | Brasil | 1715507 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 57cf934c-eac0-32ff-9c6d-0807e965fa97 | -10.17647 | -50.22346 | 2025-07-24 05:04:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 7404a2c1-7e39-3ba4-9b63-1cd09e1b78fc | -7.24763 | -43.07364 | 2025-07-24 05:04:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 17.1 |
| 9d19abc1-9e6b-39ac-a442-9e2161ae1fe0 | -5.88889 | -45.19324 | 2025-07-24 05:04:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 2b5b87a2-8eeb-3650-83bb-0c22f6efcea0 | -8.96188 | -62.21667 | 2025-07-24 05:04:00 | NOAA-20 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 0.5 |
| d18809a8-13fd-3ac8-934d-cb201397a26b | -8.49604 | -47.23435 | 2025-07-24 05:04:00 | NOAA-20 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| c31c9e30-f79c-347e-a2d2-6d53d43ee80c | -9.62344 | -67.25373 | 2025-07-24 05:04:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 7e084313-c2ce-3e7a-8e0f-98ef0bac22cd | -11.73324 | -48.18336 | 2025-07-24 05:04:00 | NOAA-20 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 93dbf804-2197-302c-9ef9-dc16d08dcf9c | -6.26321 | -45.27377 | 2025-07-24 05:04:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 1820049a-5543-387f-9f91-57754a9b3f39 | -10.0447 | -59.09779 | 2025-07-24 05:04:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| c134c8d3-d222-3d64-a143-a1b1f7239fba | -12.25487 | -44.78423 | 2025-07-24 05:04:00 | NOAA-20 | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 1c43fb30-912c-3384-bfe3-9e1ebf427d74 | -7.2476 | -43.08524 | 2025-07-24 05:04:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 10.5 |
| 8000165e-3e30-3be5-babe-ec779d9c8b3a | -8.49215 | -47.23713 | 2025-07-24 05:04:00 | NOAA-20 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 11.8 |
| 69cbd3cc-2cc6-3fee-b91f-b819ff26c9a2 | -10.12709 | -57.76978 | 2025-07-24 05:04:00 | NOAA-20 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 5fcb498f-732f-3ced-afbd-1fda728e7f59 | -9.16621 | -60.83315 | 2025-07-24 05:04:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b490dc06-16d5-3b20-b2c7-9229070c222d | -8.72529 | -51.13638 | 2025-07-24 05:04:00 | NOAA-20 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e88f69c6-f86a-3079-bc79-dbf0f9cfce29 | -9.26549 | -57.80225 | 2025-07-24 05:04:00 | NOAA-20 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 8593ed22-0548-311d-b084-bd01e20b5512 | -9.3175 | -44.8519 | 2025-07-24 05:04:00 | NOAA-20 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 2385a19b-fd7e-3466-97a7-aa19f71cb383 | -6.93896 | -50.31504 | 2025-07-24 05:04:00 | NOAA-20 | ÁGUA AZUL DO NORTE | PARÁ | Brasil | 1500347 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ccce39e0-f8f6-3ca2-8e51-2fd0e5bab74c | -12.41947 | -45.38359 | 2025-07-24 05:04:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 2c9c683f-a881-3f60-bc9c-32436bdc2605 | -12.42879 | -45.38724 | 2025-07-24 05:04:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 7c7785aa-c6b3-3e9f-98d2-b903f16028b1 | -9.20685 | -59.67663 | 2025-07-24 05:04:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 868209b2-e548-3f84-bf36-1e0eefddd391 | -8.30795 | -55.1077 | 2025-07-24 05:04:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 3ac95d9a-b231-3a16-adca-248d47986acc | -7.46016 | -49.40726 | 2025-07-24 05:04:00 | NOAA-20 | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 6349f199-837a-3392-87e3-04ad776dca58 | -8.48244 | -49.55152 | 2025-07-24 05:04:00 | NOAA-20 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 8.8 |
| d79cae9f-94ef-3eec-b478-6413a1c4b50b | -10.00469 | -48.12239 | 2025-07-24 05:04:00 | NOAA-20 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 83a527b8-8358-3e8e-ba23-f172f79daf3a | -7.17238 | -44.3778 | 2025-07-24 05:04:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 2e136d6a-6ee8-3fc3-8687-d725f4f4de23 | -7.44899 | -57.665 | 2025-07-24 05:04:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e890afb9-a480-39cb-96e1-f3b51bddbb27 | -9.32738 | -49.1143 | 2025-07-24 05:04:00 | NOAA-20 | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| edecde59-30ea-338e-b443-727cfe831f74 | -10.23194 | -56.76781 | 2025-07-24 05:04:00 | NOAA-20 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 0.3 |
| 7a7d7bc5-c707-3bf9-84ab-f5e4df3d2c13 | -7.25602 | -43.07381 | 2025-07-24 05:04:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 17.6 |
| 2db7630e-44ce-3b60-bbb3-b2673ab6cf56 | -5.91025 | -43.46119 | 2025-07-24 05:04:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 09a2e242-9b02-3063-b404-faa23d4fbf66 | -11.46412 | -48.15987 | 2025-07-24 05:04:00 | NOAA-20 | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 44430c4c-394f-3a5c-bedd-0321511e4f01 | -11.77561 | -47.39785 | 2025-07-24 05:04:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 0cc2f6f6-94b5-3c9f-bc68-2b64490d3832 | -8.931 | -47.34156 | 2025-07-24 05:04:00 | NOAA-20 | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 75f1fe25-d48c-3faa-a8b2-f97f58148398 | -8.92523 | -47.34415 | 2025-07-24 05:04:00 | NOAA-20 | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 0d32391c-fd2e-37af-9dd1-a877145af1b9 | -10.04122 | -59.09721 | 2025-07-24 05:04:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 86d333ce-9ac7-358d-9a0a-773b73ec7f74 | -10.11985 | -57.77225 | 2025-07-24 05:04:00 | NOAA-20 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 3e2a9e60-5282-3c07-887a-4e5c18a5c23c | -6.63187 | -56.28843 | 2025-07-24 05:04:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 5cb5db4c-9c5c-33e2-919b-84d5986fed66 | -11.77474 | -47.40513 | 2025-07-24 05:04:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| acfbc1c7-d8b2-3c7b-ae29-d789d9fe770d | -5.22667 | -56.01935 | 2025-07-24 05:04:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 33510e36-ebc9-3e8c-8df4-fe5e43b5971b | -7.24157 | -43.0781 | 2025-07-24 05:04:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 11.7 |
| 7e535636-e7e2-3756-9f8d-f987f488c512 | -11.4632 | -48.16191 | 2025-07-24 05:04:00 | NOAA-20 | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 9151ac78-f6bc-360f-917f-9b198f80652b | -10.12042 | -57.76869 | 2025-07-24 05:04:00 | NOAA-20 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 4b9d5508-ebe4-3d02-b3b7-df043e210c7d | -9.20617 | -59.6808 | 2025-07-24 05:04:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 1c000aaa-ddef-34e0-b2c2-f053466462c5 | -8.4926 | -47.23384 | 2025-07-24 05:04:00 | NOAA-20 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 10.9 |
| fe5704ac-081d-3621-9715-241011068ab1 | -7.27408 | -60.17422 | 2025-07-24 05:04:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| fd77d2b5-c228-3d2b-aa97-319e6b585f58 | -10.62371 | -45.23344 | 2025-07-24 05:04:00 | NOAA-20 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 5a6aba43-c037-35f0-bdc1-0fbae0c07c10 | -5.18781 | -62.57005 | 2025-07-24 05:04:00 | NOAA-20 | TAPAUÁ | AMAZONAS | Brasil | 1304104 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 03825b2f-f9b2-31de-a0bf-ba8657e17950 | -7.2536 | -43.08088 | 2025-07-24 05:04:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 5.8 |
| c735e543-9e92-3305-9080-db0b9b70c60d | -11.87401 | -55.45137 | 2025-07-24 05:04:00 | NOAA-20 | SINOP | MATO GROSSO | Brasil | 5107909 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 52202c7b-9818-374d-bd17-86ab3bf031d2 | -9.3238 | -44.85272 | 2025-07-24 05:04:00 | NOAA-20 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 27927ceb-926c-3493-8469-d3e1f4e6876d | -7.89318 | -45.54974 | 2025-07-24 05:04:00 | NOAA-20 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 6bef7b51-4388-32ae-8a68-e5e7a2cf6be5 | -6.53739 | -49.83719 | 2025-07-24 05:04:00 | NOAA-20 | CANAÃ DOS CARAJÁS | PARÁ | Brasil | 1502152 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 4e3f7167-c7b6-31aa-9aea-028145b49cde | -9.52757 | -63.62495 | 2025-07-24 05:04:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 38f7447b-f2d8-349b-8149-17e0cdea83a6 | -8.48682 | -47.23636 | 2025-07-24 05:04:00 | NOAA-20 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 11.8 |
| 3528e8a2-f7e9-3de5-8a4a-d30dc2031163 | -10.71297 | -48.85847 | 2025-07-24 05:04:00 | NOAA-20 | OLIVEIRA DE FÁTIMA | TOCANTINS | Brasil | 1715507 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 73be0949-ba5b-34a6-af55-24a4825ec2d8 | -7.25441 | -43.08632 | 2025-07-24 05:04:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 3.1 |
| 884d82b2-57c1-3faa-b564-f78a5209f0af | -6.44371 | -43.82409 | 2025-07-24 05:04:00 | NOAA-20 | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 26ae37b7-bf36-308d-879e-e03998429f87 | -9.1983 | -59.68373 | 2025-07-24 05:04:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 82c2d976-700f-35a3-99d5-8d3c66d9cce7 | -6.44304 | -43.82909 | 2025-07-24 05:04:00 | NOAA-20 | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 2bee7385-c5e0-350b-ae52-b3138f48fb4b | -7.45911 | -57.6667 | 2025-07-24 05:04:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 9ca92f8a-0329-3994-94c3-3ff4ef79fd2d | -11.46278 | -48.16512 | 2025-07-24 05:04:00 | NOAA-20 | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 25f88a4e-35e3-33ae-b8a4-4e1150453214 | -7.60415 | -49.94595 | 2025-07-24 05:04:00 | NOAA-20 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 73b1b7f3-ca34-3ee9-8ce7-be0c83330d9f | -7.45237 | -57.66555 | 2025-07-24 05:04:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 718880ab-0804-3c9b-8cf1-0ee25d90477e | -12.42307 | -45.3813 | 2025-07-24 05:04:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 132ab0cf-38cc-3771-9f2d-277c5c32622f | -6.57999 | -49.50782 | 2025-07-24 05:04:00 | NOAA-20 | XINGUARA | PARÁ | Brasil | 1508407 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 0cda7723-5982-35a3-abc3-f8fb1c8aeb05 | -8.299 | -55.09898 | 2025-07-24 05:04:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 1b94fb4d-1a18-3ec0-ba2e-9e668e1a3ad5 | -6.96977 | -44.82627 | 2025-07-24 05:04:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 81167c0c-0ca7-3f8a-b3e0-912c01520267 | -11.13002 | -48.63684 | 2025-07-24 05:04:00 | NOAA-20 | BREJINHO DE NAZARÉ | TOCANTINS | Brasil | 1703701 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b5ebba10-4b61-3f27-8380-b81bf763a991 | -9.16701 | -60.8285 | 2025-07-24 05:04:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 32363cf5-9189-3d0a-ba54-058a699be087 | -9.62343 | -67.25551 | 2025-07-24 05:04:00 | NOAA-20 | SENADOR GUIOMARD | ACRE | Brasil | 1200450 | 12 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 3429edfa-9fca-3c23-8ec0-9502f966e24b | -9.53212 | -63.62581 | 2025-07-24 05:04:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 5127319d-fd9f-3cf9-ac04-5276e0419dcd | -8.29361 | -44.97189 | 2025-07-24 05:04:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 5baddce8-5536-3d30-844a-4077ef872c86 | -8.03831 | -47.65814 | 2025-07-24 05:04:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 2eecd5e5-4225-3b1d-87f1-8caa709f9597 | -10.18093 | -50.22406 | 2025-07-24 05:04:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| c36f3e42-aeda-3b6b-81f1-e863cdd09404 | -9.62263 | -67.25793 | 2025-07-24 05:04:00 | NOAA-20 | SENADOR GUIOMARD | ACRE | Brasil | 1200450 | 12 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2cf91644-7dff-3463-91e2-6a4a216739bf | -6.57555 | -49.50721 | 2025-07-24 05:04:00 | NOAA-20 | XINGUARA | PARÁ | Brasil | 1508407 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 178db3f6-29de-3b10-b06e-c009a7d224b2 | -7.30784 | -49.57428 | 2025-07-24 05:04:00 | NOAA-20 | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 38a5b110-b1c2-3eeb-8e7c-49de58cfd919 | -10.71642 | -49.48472 | 2025-07-24 05:04:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| d9dcc707-60a4-3cff-aa5f-aebc676f11fa | -11.46372 | -48.16314 | 2025-07-24 05:04:00 | NOAA-20 | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| ed09751e-1d35-3706-aaec-bd7afed37c9a | -7.3058 | -49.57643 | 2025-07-24 05:04:00 | NOAA-20 | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5fa58aa4-2384-3322-a900-d6a3b6d05da5 | -10.08984 | -63.32248 | 2025-07-24 05:04:00 | NOAA-20 | MONTE NEGRO | RONDÔNIA | Brasil | 1101401 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| db0190f5-4a29-38ef-a4ff-0d5f884ede1f | -10.8475 | -61.96809 | 2025-07-24 05:04:00 | NOAA-20 | JI-PARANÁ | RONDÔNIA | Brasil | 1100122 | 11 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 87d3694a-3cf5-322d-84fe-342d4836ddc8 | -8.95836 | -62.21204 | 2025-07-24 05:04:00 | NOAA-20 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| fbbeb1db-9fb1-3414-a061-58ced40bfbb8 | -8.03873 | -47.65506 | 2025-07-24 05:04:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 94f6d36c-a3b0-303c-af8b-342d47f5b653 | -8.03914 | -47.652 | 2025-07-24 05:04:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 4aeb5df8-e505-3cb1-ae60-3d0dafefcd7c | -6.45018 | -43.82495 | 2025-07-24 05:04:00 | NOAA-20 | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |


[Clique aqui para ver as próximas entradas](README23.md)
