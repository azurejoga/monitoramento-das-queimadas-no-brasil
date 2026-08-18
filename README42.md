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

## Dados Diários - Página 42

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| ef271759-8afc-3df4-ad7e-77cd7aa52397 | -6.95919 | -59.03643 | 2026-08-18 04:57:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 64ce4563-8d30-3c5e-92a5-fd1a57ce72ec | -7.36104 | -55.49097 | 2026-08-18 04:57:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 7ffb58d3-7f61-3ab1-8b5f-f4e277e4cdb6 | -9.28115 | -50.31894 | 2026-08-18 04:57:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 10e37a1c-7eaf-37ac-9802-e11172dc05bf | -6.72739 | -48.65078 | 2026-08-18 04:57:00 | NOAA-20 | ARAGOMINAS | TOCANTINS | Brasil | 1701309 | 17 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ea442baf-c01e-3310-8b0d-6222eb0592a9 | -6.84225 | -59.00871 | 2026-08-18 04:57:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 5.7 |
| bad98e49-75f2-398b-9f1c-108ace145393 | -10.12682 | -54.2876 | 2026-08-18 04:57:00 | NOAA-20 | MATUPÁ | MATO GROSSO | Brasil | 5105606 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 1d178ba8-77af-3ad2-b74c-144a066a0a9e | -8.97653 | -60.50553 | 2026-08-18 04:57:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| daa4b4d2-a91b-39b4-90bf-1d2fe4c34264 | -6.11028 | -57.73194 | 2026-08-18 04:57:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2011d815-5f6e-33ab-9aef-ae012a53800a | -9.46529 | -51.66206 | 2026-08-18 04:57:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 95d1299d-b8dd-3ca8-b614-b88622c0510d | -7.5486 | -55.56446 | 2026-08-18 04:57:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| ab6cdcf9-d5b3-3dc9-85ac-a0ab0fd063d3 | -7.38835 | -46.8097 | 2026-08-18 04:57:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 1b5978fc-721a-30f5-afbc-94c718a52946 | -10.13468 | -62.39971 | 2026-08-18 04:57:00 | NOAA-20 | THEOBROMA | RONDÔNIA | Brasil | 1101609 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 772d6002-541c-3277-87d6-8cfcf40cbd1f | -8.49077 | -48.83035 | 2026-08-18 04:57:00 | NOAA-20 | ITAPORÃ DO TOCANTINS | TOCANTINS | Brasil | 1711100 | 17 | 33 | nan | nan | nan | Amazônia | 11.5 |
| 7ec4e748-d638-336d-913d-e18ab8286012 | -8.57579 | -54.72219 | 2026-08-18 04:57:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 8.9 |
| ac4d8130-dfbc-3f38-bfa9-6e4606418c80 | -9.17321 | -59.67232 | 2026-08-18 04:57:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 7b3709b1-4602-3218-8679-f7e4c425b2ce | -9.42019 | -60.44909 | 2026-08-18 04:57:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 8ac1ce27-0139-347d-a10c-8c39c699218c | -7.16981 | -43.1198 | 2026-08-18 04:57:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| ada5f1f7-bdfb-3a06-af73-b8931b45e64b | -8.62689 | -54.71584 | 2026-08-18 04:57:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 52575cda-2b34-3a64-9785-bd4c953b7553 | -8.74216 | -45.30307 | 2026-08-18 04:57:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 782b7980-91b3-35fc-ac76-a694beb71de8 | -10.28816 | -48.24174 | 2026-08-18 04:57:00 | NOAA-20 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 6f156346-feea-3415-9b37-1db4e2bbb319 | -10.04195 | -62.45936 | 2026-08-18 04:57:00 | NOAA-20 | THEOBROMA | RONDÔNIA | Brasil | 1101609 | 11 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 07f8bc40-99a2-35a9-a542-9474f9560124 | -8.57974 | -54.71913 | 2026-08-18 04:57:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 8.9 |
| 0a775c3d-b51b-32a2-8454-e3f0dc02aa68 | -7.88414 | -63.76152 | 2026-08-18 04:57:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| dd776844-5e9a-37f8-bd96-3fe8a2f523da | -8.56583 | -54.59118 | 2026-08-18 04:57:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 4828a510-88fc-3fac-8c25-2b9c96a6c49b | -11.11994 | -47.27016 | 2026-08-18 04:57:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 30.3 |
| 1da5e95d-4046-3775-b043-44e669a4b6ab | -7.07363 | -56.66072 | 2026-08-18 04:57:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 24c5d724-c42a-3074-94bb-2db46247d833 | -14.23191 | -45.41523 | 2026-08-18 04:57:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| d2866968-b4b6-3266-b45a-cb442fc0c9d6 | -6.99663 | -59.05152 | 2026-08-18 04:57:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 20d2493e-fa69-3f8a-9429-c5cfb983ea0a | -7.82518 | -44.09612 | 2026-08-18 04:57:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 703cde79-061f-38cd-b0cc-7acd1222c95c | -9.42276 | -48.2568 | 2026-08-18 04:57:00 | NOAA-20 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 1b38e247-c852-30a8-a9c7-bc57ac674047 | -9.06559 | -50.84488 | 2026-08-18 04:57:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 20.6 |
| b992b4b3-f77b-3696-9168-7c74a3daa2d0 | -7.53492 | -55.58227 | 2026-08-18 04:57:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 7a99f633-7a66-3c43-b21a-fd3a494ea5bb | -11.19163 | -54.82896 | 2026-08-18 04:57:00 | NOAA-20 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 3fd55166-9233-37e4-9617-8a404b1e5d5a | -8.58032 | -54.71553 | 2026-08-18 04:57:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 3154f22c-8b3e-3620-86ea-8039d131ac5b | -8.56186 | -54.70139 | 2026-08-18 04:57:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 71b9a277-4dbd-3f4a-a7e3-1ecde1ddf595 | -12.39774 | -54.95866 | 2026-08-18 04:57:00 | NOAA-20 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| cf560472-c689-378b-9cc1-a81280a80f85 | -12.47057 | -54.18425 | 2026-08-18 04:57:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 95c6c406-f3db-3137-a9cc-d5b3656ab63a | -8.551 | -47.38301 | 2026-08-18 04:57:00 | NOAA-20 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 124dd02d-160f-3c35-940f-1b6992d11816 | -11.11657 | -46.50067 | 2026-08-18 04:57:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 05d63d22-eb82-362c-baf3-c4a3a1fb5a9b | -8.36022 | -46.47664 | 2026-08-18 04:57:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| bf4eb120-eb05-31cb-95e6-178bc58e31d3 | -11.34415 | -55.27048 | 2026-08-18 04:57:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| ceb29120-df23-3761-803f-80158ace5025 | -6.95628 | -59.02745 | 2026-08-18 04:57:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 96fcbe91-03a1-3483-b267-0bd2174300a2 | -9.16763 | -59.67299 | 2026-08-18 04:57:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d877fceb-6435-31ac-8fa4-9abdd3f71fde | -7.90259 | -61.73578 | 2026-08-18 04:57:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 9a87d0a9-38fb-3d1c-9c41-3f0dab32d5c1 | -10.51865 | -50.79079 | 2026-08-18 04:57:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 047b1d51-a01a-370f-a5b4-6bc24672206b | -6.84504 | -58.99238 | 2026-08-18 04:57:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| d9f7c9ab-a33a-3312-bc71-74ce498ba21c | -6.84658 | -59.00941 | 2026-08-18 04:57:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 151c7402-c390-3937-80a8-87df5c855383 | -10.93554 | -57.10559 | 2026-08-18 04:57:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 8.2 |
| c749e9d8-3c75-3883-a456-3ae61add14c5 | -8.53183 | -54.90903 | 2026-08-18 04:57:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f78a0464-dbda-3243-a68a-f4f6b14741fc | -6.1011 | -57.73754 | 2026-08-18 04:57:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 9ad520b8-ec1b-318e-bf77-9cd59adb96e1 | -7.81807 | -44.60681 | 2026-08-18 04:57:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 1537d312-d55d-3a9a-aac6-5caaae18e18b | -9.42768 | -60.40677 | 2026-08-18 04:57:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 23ded234-0020-3336-80d8-698af98b116d | -6.75622 | -59.16677 | 2026-08-18 04:57:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 37607539-a99b-3885-9990-5d28f16dcb03 | -9.47097 | -51.67051 | 2026-08-18 04:57:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ac77991b-1ac0-378c-a7d1-3fbe00e26e68 | -7.632 | -45.74143 | 2026-08-18 04:57:00 | NOAA-20 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 88afac0c-9ba0-3519-ae1a-baa5e0ef7a5a | -9.16401 | -59.66797 | 2026-08-18 04:57:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| db502ec9-fc39-3cf2-a90d-6c7eb637bcb7 | -8.20307 | -55.03344 | 2026-08-18 04:57:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 38532136-66f0-3bed-bd60-132599f07cfa | -11.32067 | -55.23354 | 2026-08-18 04:57:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c2fa1a2c-f11a-348a-9ef9-3a059f90f6cd | -8.5809 | -54.71193 | 2026-08-18 04:57:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 2eaa7715-5eb1-3bfe-bbf0-044f58d150d9 | -11.19945 | -54.82293 | 2026-08-18 04:57:00 | NOAA-20 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c38876bc-b1f7-3b14-bf7a-7b6a332fbd78 | -6.6993 | -58.95057 | 2026-08-18 04:57:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| c7398bd9-9b8b-30eb-ae07-cec0782a797c | -9.42631 | -48.26104 | 2026-08-18 04:57:00 | NOAA-20 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 2cbfac1d-7fc2-33f0-8fc8-8b4693cb1766 | -10.34172 | -57.5757 | 2026-08-18 04:57:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| efcace85-53d9-3e89-957d-19adbbb0815c | -7.61427 | -55.6305 | 2026-08-18 04:57:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 0a297274-bebe-3407-82b2-52879f431ad8 | -6.76952 | -59.76376 | 2026-08-18 04:57:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 5225c3bf-9844-3490-a97b-fb1f0f4bb8b1 | -9.47042 | -51.65141 | 2026-08-18 04:57:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 6eb2c3fe-2815-3e7a-817e-e132d82f2940 | -8.49294 | -48.81571 | 2026-08-18 04:57:00 | NOAA-20 | ITAPORÃ DO TOCANTINS | TOCANTINS | Brasil | 1711100 | 17 | 33 | nan | nan | nan | Amazônia | 9.2 |
| 10ace780-f20c-34f3-b3d0-621ef8a33886 | -7.53691 | -46.61774 | 2026-08-18 04:57:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| bdbd26cd-4533-3dba-a7bf-24e4b6d6abdc | -9.42436 | -60.42554 | 2026-08-18 04:57:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| bbbdaddb-f641-3daf-8d98-defa2693a542 | -8.58658 | -54.69807 | 2026-08-18 04:57:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 4df63552-84fd-3534-bd13-d9bf96e9dc56 | -9.49211 | -51.60128 | 2026-08-18 04:57:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 95ce8276-0f7e-3820-a8b9-fb63fc2c5e6a | -7.9144 | -61.72856 | 2026-08-18 04:57:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| f4370d66-e098-3611-b847-0023f3bba82d | -10.04767 | -62.45724 | 2026-08-18 04:57:00 | NOAA-20 | THEOBROMA | RONDÔNIA | Brasil | 1101609 | 11 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 2a219ec6-ab35-3e47-a086-6b60a504c649 | -6.84155 | -59.01286 | 2026-08-18 04:57:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 8.6 |
| 021a6052-e0e1-3931-8d60-89bad18fd3c8 | -11.3527 | -46.37032 | 2026-08-18 04:57:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e59875fb-da00-34cb-bce0-f3da4e71642c | -8.20485 | -55.02235 | 2026-08-18 04:57:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 7a2cc427-d3f7-3240-80c5-9da8a0634bd4 | -12.26078 | -51.53819 | 2026-08-18 04:57:00 | NOAA-20 | BOM JESUS DO ARAGUAIA | MATO GROSSO | Brasil | 5101852 | 51 | 33 | nan | nan | nan | Cerrado | 6.9 |
| e378a1bd-bf26-3c12-8a20-c2ba1d07684d | -11.32126 | -55.22992 | 2026-08-18 04:57:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c4aa6b7b-a867-317e-b3a9-ce1ea5b36a0e | -8.19244 | -55.01259 | 2026-08-18 04:57:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| fd3732cf-1228-34e2-a38b-0a5d2e8e0cdf | -6.85587 | -59.007 | 2026-08-18 04:57:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| adeebacf-48af-37eb-83c5-c31cac1e9c15 | -8.56406 | -54.70916 | 2026-08-18 04:57:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 8f9eac05-df62-3318-b878-39f56f28de38 | -8.57359 | -54.71441 | 2026-08-18 04:57:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| e8326068-6e79-36e5-af6b-92f91278babb | -8.21286 | -55.01602 | 2026-08-18 04:57:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 65b237ab-02fc-304c-b59d-c8e7cf108966 | -6.86038 | -56.76009 | 2026-08-18 04:57:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| d856f79a-ee8e-347f-90ef-1145b239f467 | -10.28912 | -48.23497 | 2026-08-18 04:57:00 | NOAA-20 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 9cab4201-5f27-3dc6-9343-684a988d1d40 | -7.37564 | -55.48933 | 2026-08-18 04:57:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 61ca5865-c7cb-3b62-9aca-28abd233aa0c | -6.62576 | -52.02449 | 2026-08-18 04:57:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a18fec47-5d3c-3a47-a937-1f41462b4988 | -7.68417 | -55.16098 | 2026-08-18 04:57:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 2f1fe515-e681-32a4-8f30-dabb554a95b0 | -8.49538 | -48.82605 | 2026-08-18 04:57:00 | NOAA-20 | ITAPORÃ DO TOCANTINS | TOCANTINS | Brasil | 1711100 | 17 | 33 | nan | nan | nan | Amazônia | 11.5 |
| b47d1425-2d8b-3bf2-aa02-ea97fbe900ba | -6.70093 | -56.16537 | 2026-08-18 04:57:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a9a8377a-d7ce-3953-b9ed-4d3c2201a50f | -13.26265 | -51.6493 | 2026-08-18 04:57:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 7572c565-f117-3212-af90-e4d6b1d1fc64 | -7.1343 | -47.51423 | 2026-08-18 04:57:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 458d5cc1-2aba-357b-a22a-8eac1bf7f669 | -6.85226 | -59.00211 | 2026-08-18 04:57:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 3cafc874-0ddf-3a9f-b652-09fc15b0bf1a | -12.90797 | -52.82541 | 2026-08-18 04:57:00 | NOAA-20 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4d3ad3bf-18a1-327c-999b-89f56b104310 | -7.09602 | -55.45266 | 2026-08-18 04:57:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| cffb72b0-6d1d-3087-b170-8be0f648b8b4 | -11.52575 | -46.63516 | 2026-08-18 04:57:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 0f74bfb3-3cf6-3fe2-8012-0e6ee70eaf4d | -7.36803 | -55.49211 | 2026-08-18 04:57:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 74ce1184-4583-3dec-9f07-4f3d4c8ee4a2 | -7.90151 | -61.74188 | 2026-08-18 04:57:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| d5f84084-3a2c-362c-a796-17c146a4ee75 | -10.31761 | -59.14609 | 2026-08-18 04:57:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| bf2514fe-eb5a-3e6e-b73a-b9d068abfd5e | -10.51568 | -50.78618 | 2026-08-18 04:57:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 3.8 |


[Clique aqui para ver as próximas entradas](README43.md)
