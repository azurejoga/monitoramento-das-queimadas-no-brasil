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

## Dados Diários - Página 40

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 56491aad-a8dc-35f9-aa15-920c8d72c467 | -6.67826 | -59.94735 | 2026-09-03 04:57:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 16.9 |
| 00267786-d449-3375-b894-9ec2c6b266e8 | -5.46456 | -60.05869 | 2026-09-03 04:57:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| afeffd62-ccc4-3734-9059-3ea3d2373b65 | -7.26186 | -47.52634 | 2026-09-03 04:57:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| b46f9a0b-f53d-3324-ba08-acc8f853c5e9 | -6.26359 | -55.42949 | 2026-09-03 04:57:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| cf287705-8bcc-3d9e-9262-428afead7a4f | -11.31255 | -45.119 | 2026-09-03 04:57:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 9.0 |
| bdce28e7-e3b2-3ced-a3b8-4d5906fefc31 | -9.21724 | -59.75798 | 2026-09-03 04:57:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e3a25c7a-3bbb-3201-9128-4aa11e0153cb | -7.67365 | -62.54725 | 2026-09-03 04:57:00 | NOAA-20 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 828e937d-b3c2-39df-bcc1-019c0daff614 | -8.46807 | -54.67361 | 2026-09-03 04:57:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| e05c5814-2843-33b9-a6f0-69772f0a8e7e | -8.07339 | -50.96515 | 2026-09-03 04:57:00 | NOAA-20 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 1a052b21-9d21-3069-9738-9d1c7749645f | -3.61585 | -60.56139 | 2026-09-03 04:57:00 | NOAA-20 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 7191e8b0-7831-38f2-a2d8-9ede0f7da26d | -6.62333 | -55.24226 | 2026-09-03 04:57:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d4c39621-7d39-3153-88b3-f8be1f71f176 | -5.25333 | -55.88752 | 2026-09-03 04:57:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d1dcd7c5-96af-34d8-9e32-6b4095fd0e9c | -5.80505 | -52.30058 | 2026-09-03 04:57:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 38b58d27-2d4c-3053-adcb-b2dce491e7ee | -5.58873 | -61.47845 | 2026-09-03 04:57:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 21a1667f-2346-370a-8bee-032eccf148d4 | -8.46307 | -54.66171 | 2026-09-03 04:57:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e657e36b-4531-3fed-b074-7bf6ca706192 | -4.54377 | -54.91071 | 2026-09-03 04:57:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| eb2fbe1a-0038-3f21-85cc-2fa92484dfaf | -8.46202 | -54.64678 | 2026-09-03 04:57:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 18.7 |
| 007529c6-f4bd-3e49-9584-2143a83f68bd | -6.39085 | -55.22514 | 2026-09-03 04:57:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c657a47b-612b-3251-8f82-5bf021b873b8 | -6.7462 | -59.44289 | 2026-09-03 04:57:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 7458c821-9fde-33fd-9e6f-783a3cc33ba5 | -5.21357 | -60.03306 | 2026-09-03 04:57:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 9adb6e0a-43ba-3318-adec-05522b61b3da | -8.4368 | -54.73904 | 2026-09-03 04:57:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9927c31b-486c-3376-8d78-1afb612c4051 | -5.25099 | -60.18888 | 2026-09-03 04:57:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| a8c784f8-6a93-370e-a527-c31f607c0356 | -9.88157 | -60.29971 | 2026-09-03 04:57:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6b4c0556-30e6-3578-b30f-2ab9eb8b8eaf | -8.43227 | -54.7457 | 2026-09-03 04:57:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 88052f0b-d5ee-3838-8887-4215c1c9e704 | -8.07589 | -50.95843 | 2026-09-03 04:57:00 | NOAA-20 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 0.3 |
| 645de5b5-6d84-3496-8e65-e83ff30d1776 | -8.08147 | -50.95857 | 2026-09-03 04:57:00 | NOAA-20 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 7cd7e9bc-563f-3ba0-8044-45a771c0d870 | -8.45508 | -54.68996 | 2026-09-03 04:57:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 4fa4214c-e7b1-3f04-a8fb-df1893dee5ac | -6.95549 | -59.78955 | 2026-09-03 04:57:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 6382d536-70db-305a-9bc4-2f62c33ccfd0 | -7.11856 | -42.23172 | 2026-09-03 04:57:00 | NOAA-20 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 32e11d55-cb21-3ded-9a98-eb05a9f2984b | -8.70434 | -52.36946 | 2026-09-03 04:57:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 0ef60ba0-a21c-32ee-b167-79f0ba544d9b | -8.4546 | -54.67144 | 2026-09-03 04:57:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| dd7ad0a6-3689-3bda-8c83-b28eda26d74d | -3.1388 | -60.64433 | 2026-09-03 04:57:00 | NOAA-20 | IRANDUBA | AMAZONAS | Brasil | 1301852 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| d3332910-9fbc-3ae2-bab5-80625f2d2845 | -9.62342 | -54.30932 | 2026-09-03 04:57:00 | NOAA-20 | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 34480e6c-6c79-3008-bade-1c75d6e3e632 | -6.64891 | -59.43237 | 2026-09-03 04:57:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.2 |
| a43b2d9f-eb85-332e-babe-b86a60063aae | -9.08458 | -47.82242 | 2026-09-03 04:57:00 | NOAA-20 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| d0c34b8c-15b2-302b-be1e-1529c9f86063 | -8.43985 | -54.69864 | 2026-09-03 04:57:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| cc30aafc-1f27-3f75-b9e8-75b2a31c0f0d | -8.43285 | -54.74209 | 2026-09-03 04:57:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 5e30a5c4-a1af-3716-af82-5e19c7a90bf6 | -6.67909 | -59.94252 | 2026-09-03 04:57:00 | NOAA-20 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 12.3 |
| 8cdaf07f-072e-314d-8b52-bb88c16ed3fa | -10.56967 | -47.71269 | 2026-09-03 04:57:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c7f2e5b1-b87a-317e-81e7-5a4275fa23fc | -7.35532 | -60.61293 | 2026-09-03 04:57:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 67bd106c-250c-341c-8b86-07b43300978d | -7.35632 | -60.60738 | 2026-09-03 04:57:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 82886164-8e59-3495-a38b-68bf2f01d92a | -7.07566 | -44.36024 | 2026-09-03 04:57:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e648d8f9-783f-3dc1-925d-204bc0a74a76 | -5.84483 | -52.06869 | 2026-09-03 04:57:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 413ee36f-6ed4-3b6d-99d9-e8fd4f0421d0 | -10.56674 | -47.7336 | 2026-09-03 04:57:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 2465af99-4d5b-3fed-af19-858a8ea0b956 | -6.05486 | -53.80684 | 2026-09-03 04:57:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 2151861e-481b-3e4c-99f2-677ab9c5a424 | -9.08827 | -65.37613 | 2026-09-03 04:57:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 8f083cc5-6808-335a-9cbf-03aa27fa26ac | -5.80555 | -43.64703 | 2026-09-03 04:57:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 3ec83abf-5663-355e-a4ff-ba96bb2f291f | -5.30128 | -49.16489 | 2026-09-03 04:57:00 | NOAA-20 | NOVA IPIXUNA | PARÁ | Brasil | 1504976 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 94f7a2ec-ac60-3f2d-ab61-636d04bd2ed4 | -10.75688 | -48.97694 | 2026-09-03 04:57:00 | NOAA-20 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 3cbb8464-b436-313b-ade2-c3c5bcf1651b | -3.634 | -60.54633 | 2026-09-03 04:57:00 | NOAA-20 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| af8a3b93-2342-3270-a777-b2226837e5e2 | -11.32973 | -50.5354 | 2026-09-03 04:57:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 79e65657-6b2a-3dfe-9222-e592841616e1 | -6.83335 | -59.43395 | 2026-09-03 04:57:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f139c856-3462-3be6-9f8e-cbde20f733d9 | -8.43122 | -54.73071 | 2026-09-03 04:57:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 78326375-58c7-3d6d-932e-8ab11e02af66 | -5.58895 | -61.47382 | 2026-09-03 04:57:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7d72a1ab-5721-3dff-8f27-c40132480ad2 | -9.09577 | -65.50597 | 2026-09-03 04:57:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1cece915-1a00-3497-86ec-d39dcb779649 | -10.34992 | -49.96622 | 2026-09-03 04:57:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 334468f6-523b-3a56-a85d-3346065cde04 | -5.8007 | -43.65034 | 2026-09-03 04:57:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| e28fc55f-0723-3f0f-94c4-4201721bfc9f | -12.0932 | -47.06903 | 2026-09-03 04:57:00 | NOAA-20 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 0ac5cfe2-e392-3783-be45-2349ae6ea113 | -10.92807 | -45.34776 | 2026-09-03 04:57:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| caab6286-8d65-3ce6-980e-ea41b9234db1 | -9.61532 | -57.88399 | 2026-09-03 04:57:00 | NOAA-20 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e45fdd6b-5737-3b5b-8af6-80ffd6701f7b | -9.04289 | -65.74371 | 2026-09-03 04:57:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 3.3 |
| c88eab2f-f976-394b-a2a3-71f64cf464a4 | -8.43253 | -54.70115 | 2026-09-03 04:57:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| a56df065-5eb3-3d25-b544-eba5392361ee | -8.08436 | -50.96292 | 2026-09-03 04:57:00 | NOAA-20 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 9123967f-01de-3788-85f4-a9400071f322 | -10.56479 | -47.71615 | 2026-09-03 04:57:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 59c091fb-9118-3e54-b7ac-c900eb6820c0 | -9.83047 | -59.476 | 2026-09-03 04:57:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 24b79643-720f-350d-86dd-4e9697a05cfd | -9.0375 | -65.73705 | 2026-09-03 04:57:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 65dcbdd5-b4cf-3057-83ab-b23412b043d7 | -6.75705 | -56.33693 | 2026-09-03 04:57:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 226eadb3-23ae-3d0a-b22a-c4a6943668e2 | -4.96851 | -55.84103 | 2026-09-03 04:57:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 6e0117ab-ff46-3668-aa57-8fe83f7aa94a | -10.88075 | -45.31378 | 2026-09-03 04:57:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| b3f99ba3-1179-32f2-853a-23bcc976d4c4 | -6.65524 | -46.14077 | 2026-09-03 04:57:00 | NOAA-20 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 26551540-3349-386e-b1e1-e6f3fc913776 | -6.31033 | -56.04665 | 2026-09-03 04:57:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 15.9 |
| 78caaf46-ce74-3de3-b6a3-e26157b0cadf | -9.03644 | -65.74251 | 2026-09-03 04:57:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 6b159b13-92c4-3668-9c21-2e0ff1ecc4bb | -8.07628 | -50.96951 | 2026-09-03 04:57:00 | NOAA-20 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| d33cc5b3-355d-32ed-9d5f-a154f6e0a5e2 | -11.32306 | -50.52996 | 2026-09-03 04:57:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 20.0 |
| 0c6d7709-1da6-38b9-8efd-b9c9b7bd612d | -11.7433 | -50.46047 | 2026-09-03 04:57:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 8a4c6041-d1cc-3730-b225-4ebd6b113f11 | -8.07125 | -50.96553 | 2026-09-03 04:57:00 | NOAA-20 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| d5246a0d-91b4-3816-8042-80626ebac2e2 | -8.43622 | -54.74265 | 2026-09-03 04:57:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 3f502f21-94c2-3c44-8df3-02d1c7661beb | -4.97146 | -55.8459 | 2026-09-03 04:57:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 8221afc5-76ba-3710-835a-2aeaacb518c3 | -10.24404 | -47.76183 | 2026-09-03 04:57:00 | NOAA-20 | SANTA TEREZA DO TOCANTINS | TOCANTINS | Brasil | 1719004 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 4e3ad80d-c478-342a-84a4-cf3851b3c811 | -6.61985 | -55.24168 | 2026-09-03 04:57:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 50b7c00a-7851-3c2a-a52e-a8615142739f | -6.64814 | -59.43688 | 2026-09-03 04:57:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 61f8c1e2-3160-39d4-a6ca-45e768abd8a7 | -4.97372 | -55.855 | 2026-09-03 04:57:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 09a35123-296a-3377-8b35-7700d17deda7 | -8.43091 | -54.68976 | 2026-09-03 04:57:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 337e0f9a-8a53-39c4-b18d-94064a7a5d65 | -5.23393 | -49.59848 | 2026-09-03 04:57:00 | NOAA-20 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 1136f771-fe08-32c7-a65f-c9ba0b0c4d93 | -4.6927 | -56.06053 | 2026-09-03 04:57:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 8bdb7884-3306-3021-bd7f-46d3aca4e6dd | -6.64579 | -59.45066 | 2026-09-03 04:57:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 9.4 |
| 8db22d56-1af6-357f-9003-15fc5a1154f4 | -6.8393 | -59.42596 | 2026-09-03 04:57:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 5285f0a5-1a76-3217-91af-6e575db24e1d | -8.44043 | -54.69501 | 2026-09-03 04:57:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 21fb4c43-82f4-3329-b26a-bc9f9364a536 | -11.31209 | -45.12259 | 2026-09-03 04:57:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 20cb5c55-6437-3f86-9536-05cf26373be6 | -6.80337 | -58.98 | 2026-09-03 04:57:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 72a860ab-6c88-3032-8762-409f9987c269 | -3.61991 | -60.56815 | 2026-09-03 04:57:00 | NOAA-20 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| fcb4a625-805a-3a3d-bc31-161938c4c883 | -8.45391 | -54.69724 | 2026-09-03 04:57:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| edefb6da-0327-3465-adf5-adba1c7a6e07 | -8.08666 | -50.9711 | 2026-09-03 04:57:00 | NOAA-20 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 238190ed-725c-3af5-b167-e7420381e36a | -6.75584 | -59.44014 | 2026-09-03 04:57:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0cd311f2-78b8-3dc8-b701-d7a61daf96de | -4.96574 | -55.85803 | 2026-09-03 04:57:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 91fbdfb0-b563-3068-9b06-9584698e60a3 | -3.76006 | -59.3199 | 2026-09-03 04:57:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| a110bbda-34b2-35c6-a83d-52bbe16f5856 | -3.20132 | -61.2284 | 2026-09-03 04:57:00 | NOAA-20 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 7480ecd8-3cc5-39ac-8f9e-a07cf2bd6338 | -10.52189 | -49.98331 | 2026-09-03 04:57:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ce227676-6097-32cb-97d1-dd99126110aa | -10.24835 | -47.76219 | 2026-09-03 04:57:00 | NOAA-20 | SANTA TEREZA DO TOCANTINS | TOCANTINS | Brasil | 1719004 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| c8d5c5b0-eda3-32d5-bb25-ed573dbca850 | -7.29332 | -60.71464 | 2026-09-03 04:57:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 3.2 |


[Clique aqui para ver as próximas entradas](README41.md)
