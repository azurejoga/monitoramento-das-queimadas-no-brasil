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

## Dados Diários - Página 17

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| ffed28e5-019b-3db6-9c14-4805699d4143 | -7.73135 | -40.99318 | 2025-10-11 04:32:00 | NOAA-21 | CARIDADE DO PIAUÍ | PIAUÍ | Brasil | 2202554 | 22 | 33 | nan | nan | nan | Caatinga | 13.6 |
| b36e5444-7f45-305e-ab76-15fd698f7b9f | -5.87912 | -42.84603 | 2025-10-11 04:32:00 | NOAA-21 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 3.6 |
| f95d67fc-6b84-30e6-84df-b33d06d44d5d | -7.491 | -42.75867 | 2025-10-11 04:32:00 | NOAA-21 | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| df9077b2-cd92-306b-8632-8828a6d6aacf | -5.47895 | -48.65682 | 2025-10-11 04:32:00 | NOAA-21 | SÃO JOÃO DO ARAGUAIA | PARÁ | Brasil | 1507508 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ceaca4ec-cf1d-3605-a25f-3b770d8a1eba | -8.34731 | -48.16465 | 2025-10-11 04:32:00 | NOAA-21 | TUPIRATINS | TOCANTINS | Brasil | 1721307 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 55bf983e-2db4-33d6-b2e6-2506ea197545 | -6.43819 | -45.82462 | 2025-10-11 04:32:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 7a5b7f84-e327-3a93-97fc-1b3135d2d7a3 | -3.98354 | -46.27439 | 2025-10-11 04:32:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 0e294ed1-5c66-35ac-81af-7be7eaec1d52 | -3.42279 | -52.73271 | 2025-10-11 04:32:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ccfb5ead-af83-33b9-a838-fa661a3ac958 | -6.65292 | -45.9819 | 2025-10-11 04:32:00 | NOAA-21 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| b6b8a372-f71c-3bdf-b57e-39f85b1f93aa | -3.59884 | -48.98598 | 2025-10-11 04:32:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e4b07f77-99e6-3770-90dc-d5b444a81888 | -5.69484 | -44.81307 | 2025-10-11 04:32:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 52e1c1ad-d00a-36f2-bbc4-eccd045ebddd | -5.89185 | -42.70519 | 2025-10-11 04:32:00 | NOAA-21 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| f07b3f68-e3cd-39ec-b9cc-276a7fdf5054 | -3.55873 | -50.12635 | 2025-10-11 04:32:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 48c0b92a-ea74-318a-aff3-8ab838be90a2 | -5.91322 | -45.42591 | 2025-10-11 04:32:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 6931020d-848f-368c-ad8a-a4d999f26271 | -5.78168 | -43.41904 | 2025-10-11 04:32:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 4b12745d-8aaa-3349-a62b-c0a174cbc180 | -5.42132 | -44.94467 | 2025-10-11 04:32:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 602b9f55-defd-379d-ba72-72a2fdf84d1d | -6.22948 | -41.57522 | 2025-10-11 04:32:00 | NOAA-21 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| aa4b3459-b648-3c81-a352-8298d1dd1d8c | -7.86419 | -44.47876 | 2025-10-11 04:32:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 1bcbd597-90d4-3f23-a6c9-9e1dba7710be | -7.79748 | -42.42917 | 2025-10-11 04:32:00 | NOAA-21 | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 6ee11c12-2231-3551-8fd3-756d1c20cc06 | -7.51456 | -45.13904 | 2025-10-11 04:32:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 27227091-edc2-3b8a-bd3c-5df553b4182b | -7.38286 | -45.17059 | 2025-10-11 04:32:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| f32e31cd-3e00-3437-927b-288b67594c86 | -5.40368 | -40.97208 | 2025-10-11 04:32:00 | NOAA-21 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| c1ef47f6-9eac-3fd6-ab24-95e81c224364 | -6.01992 | -43.11343 | 2025-10-11 04:32:00 | NOAA-21 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 7.6 |
| 2b75c9a9-6457-3d7a-8611-10e94b9e7328 | -7.67673 | -42.57453 | 2025-10-11 04:32:00 | NOAA-21 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 3.6 |
| ec49304e-5f33-38db-a70b-7280a902faf0 | -5.75929 | -46.49492 | 2025-10-11 04:32:00 | NOAA-21 | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| e4ac611e-b77e-3d09-9a7a-5f762e4859e4 | -8.40677 | -45.09311 | 2025-10-11 04:32:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 199b16ad-8572-3df3-9ec4-3b5d93a613f0 | -5.59112 | -41.10398 | 2025-10-11 04:32:00 | NOAA-21 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 5.1 |
| fe1d7557-938f-3d40-82f1-928f9aea5950 | -8.15985 | -43.31828 | 2025-10-11 04:32:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 5.7 |
| 07e5d3a2-f991-3550-bf87-650c8c28af79 | -5.32889 | -41.56686 | 2025-10-11 04:32:00 | NOAA-21 | CASTELO DO PIAUÍ | PIAUÍ | Brasil | 2202604 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 93057806-87b2-3870-96e7-f983b0253f58 | -7.14726 | -44.13809 | 2025-10-11 04:32:00 | NOAA-21 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 3.4 |
| a67f1faa-8f5e-3d32-b338-b06c821df622 | -5.58864 | -42.98965 | 2025-10-11 04:32:00 | NOAA-21 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 126c17f9-95e0-3b05-b9b5-48a456f34b0c | -8.21739 | -43.35859 | 2025-10-11 04:32:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| e7fe305f-1169-333a-8bc7-2224bdb92057 | -7.77753 | -42.41824 | 2025-10-11 04:32:00 | NOAA-21 | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| f87a6fd1-80e9-336d-b5db-f5ae50e8a67c | -6.03799 | -42.47686 | 2025-10-11 04:32:00 | NOAA-21 | HUGO NAPOLEÃO | PIAUÍ | Brasil | 2204600 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 2c0a843a-a26a-332d-85e3-86b3c4456a0f | -8.82312 | -44.42897 | 2025-10-11 04:32:00 | NOAA-21 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e39c6a38-d57c-3329-87d6-913be949f0cc | -5.74892 | -43.37476 | 2025-10-11 04:32:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 665872cb-4cab-3084-87ea-90b4bb406df6 | -4.53622 | -50.20805 | 2025-10-11 04:32:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 922f8551-795b-331c-ace5-b1d08cf2127c | -6.035 | -42.46878 | 2025-10-11 04:32:00 | NOAA-21 | HUGO NAPOLEÃO | PIAUÍ | Brasil | 2204600 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| f9c2e5b7-ffca-3ff7-b95b-d455ca7723d3 | -3.9844 | -47.88188 | 2025-10-11 04:32:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 9435fac0-139a-3e74-a910-6370565e3ead | -7.75251 | -44.70547 | 2025-10-11 04:32:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| e7e24c94-8d70-375a-b162-deff0d1290a9 | -3.86237 | -50.76615 | 2025-10-11 04:32:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 42787a08-5d28-3fcb-84df-a6b2d08e16f1 | -4.42788 | -47.59592 | 2025-10-11 04:32:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 9.7 |
| 4d686c2b-51a5-3ba8-93e5-7337257a6884 | -8.20628 | -43.33573 | 2025-10-11 04:32:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 8.5 |
| 4f94379d-ebe2-3239-bf21-7c65126fd663 | -8.19778 | -47.86104 | 2025-10-11 04:32:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 41370575-0b0c-3e46-bbbe-40472899c5df | -3.39276 | -50.14191 | 2025-10-11 04:32:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c1492915-09d1-3e4d-b56f-fefc1dd33f77 | -7.65952 | -42.57583 | 2025-10-11 04:32:00 | NOAA-21 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 7.8 |
| 7dd33e72-e009-3d34-b53d-5f561adebaa2 | -5.32476 | -43.08772 | 2025-10-11 04:32:00 | NOAA-21 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 12.7 |
| 5b7ed188-1e55-3b62-b13d-034a6c0774d3 | -7.29823 | -45.56397 | 2025-10-11 04:32:00 | NOAA-21 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 5b74f042-578e-3eb5-8d6d-95b3c1e60c02 | -6.03475 | -42.4988 | 2025-10-11 04:32:00 | NOAA-21 | HUGO NAPOLEÃO | PIAUÍ | Brasil | 2204600 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| fa7a88c3-85ee-3339-9750-c10865cafbbb | -4.07546 | -48.03778 | 2025-10-11 04:32:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 75c48e1c-1b51-3d63-ac06-bd827705e842 | -7.67608 | -43.99021 | 2025-10-11 04:32:00 | NOAA-21 | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Cerrado | 10.5 |
| cb67a2ad-680e-3dee-8449-667a1e475459 | -7.53168 | -44.60473 | 2025-10-11 04:32:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 0c3a929f-2540-3a7e-b309-e1e365710abb | -7.67435 | -42.57285 | 2025-10-11 04:32:00 | NOAA-21 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 66277468-3a15-3f6e-ad2c-22ed3708b072 | -4.42235 | -43.46753 | 2025-10-11 04:32:00 | NOAA-21 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| ec9caa19-0638-33f0-97f2-ec93b21a67df | -4.40909 | -43.47293 | 2025-10-11 04:32:00 | NOAA-21 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 192e248d-3252-3f26-b38c-6ad52895f387 | -4.41724 | -43.4761 | 2025-10-11 04:32:00 | NOAA-21 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 6d62a148-9efd-3d43-8ebe-d0aa7ce4b74d | -7.40948 | -42.03297 | 2025-10-11 04:32:00 | NOAA-21 | SANTO INÁCIO DO PIAUÍ | PIAUÍ | Brasil | 2209500 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| be80012f-849c-3365-8458-c8fbd9d2c14e | -2.92262 | -41.91446 | 2025-10-11 04:32:00 | NOAA-21 | ARAIOSES | MARANHÃO | Brasil | 2100907 | 21 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 8ebb27a5-1686-34ab-8b7d-4887beb0ebae | -6.75602 | -39.677 | 2025-10-11 04:32:00 | NOAA-21 | TARRAFAS | CEARÁ | Brasil | 2313252 | 23 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 36c4db35-17e9-3da1-86b3-5f0f363819c2 | -5.32941 | -43.08335 | 2025-10-11 04:32:00 | NOAA-21 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 00738079-0eeb-389a-b919-58a3033f1944 | -5.91263 | -45.42972 | 2025-10-11 04:32:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 53761027-f25e-3c84-b999-e072f503c4d6 | -7.53901 | -44.60587 | 2025-10-11 04:32:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 8a1b0349-c7fb-3c65-ba8a-e13674982d80 | -4.89123 | -45.95244 | 2025-10-11 04:32:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b9a12f64-3cec-3c96-9110-8d4405e7c43d | -6.16849 | -42.55092 | 2025-10-11 04:32:00 | NOAA-21 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 3.1 |
| e9a9203f-7531-3898-9ab5-e5b357ee8469 | -7.75116 | -44.21362 | 2025-10-11 04:32:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| e7edaa70-d21c-3fab-8826-dbf3612054a3 | -7.11013 | -49.23122 | 2025-10-11 04:32:00 | NOAA-21 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 6daebb2e-9560-315f-acd2-5de9823c9f90 | -6.31928 | -45.79919 | 2025-10-11 04:32:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| a09222dc-ac24-310c-a6b9-3f1c796b0de2 | -1.90054 | -51.01092 | 2025-10-11 04:32:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| af799286-a08a-3312-9189-adee2de8f4e7 | -8.15535 | -43.32123 | 2025-10-11 04:32:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 18a15ca6-1ae8-3578-98a3-a0db5f7a85f2 | -7.50317 | -45.14199 | 2025-10-11 04:32:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| e30fb8a3-64b0-3975-b703-1535b2c0e521 | -3.39211 | -50.14592 | 2025-10-11 04:32:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 42af05a4-ce58-3100-b832-a81336b6dfb5 | -3.39049 | -50.13332 | 2025-10-11 04:32:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 8a61f90e-887f-3111-b7aa-cd9372b17df5 | -8.18784 | -43.3223 | 2025-10-11 04:32:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 3.5 |
| 62502e14-a170-337c-90b0-4888c1e37759 | -5.76453 | -47.90244 | 2025-10-11 04:32:00 | NOAA-21 | ARAGUATINS | TOCANTINS | Brasil | 1702208 | 17 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 21a87eed-1637-3593-a0ce-815bb9c77f4f | -5.60731 | -45.82135 | 2025-10-11 04:32:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 6a1f0779-a782-3aa2-90ec-9c745d5a2540 | -5.65578 | -42.78119 | 2025-10-11 04:32:00 | NOAA-21 | CURRALINHOS | PIAUÍ | Brasil | 2203255 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 2f04e92a-03c3-3231-9280-e5a558515b27 | -6.45846 | -44.57382 | 2025-10-11 04:32:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 2c9fd768-0491-364d-91af-7b0e2460c9da | -6.11002 | -42.5536 | 2025-10-11 04:32:00 | NOAA-21 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 30d62742-d3a2-3d98-94ac-c15f2eda92d8 | -7.71068 | -46.65478 | 2025-10-11 04:32:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| d52ed92d-bd2f-3694-b24e-a8eb5efa7c09 | -7.17949 | -46.72042 | 2025-10-11 04:32:00 | NOAA-21 | FEIRA NOVA DO MARANHÃO | MARANHÃO | Brasil | 2104073 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 6272171f-29c7-35f0-b819-3ec6070aa9d7 | -7.86919 | -44.47043 | 2025-10-11 04:32:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| c1c11f2e-f491-350a-a546-8dc2d902c7c7 | -8.10841 | -47.2273 | 2025-10-11 04:32:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| fd8563c4-3e1d-36b6-9cd2-7997cae0aa72 | -6.23943 | -41.56799 | 2025-10-11 04:32:00 | NOAA-21 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| ebb2c65e-e198-3c3c-a905-4cd92b757f4b | -3.42342 | -52.72885 | 2025-10-11 04:32:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| fc1c6a14-8086-38c9-aa02-c1a9f63f4b1e | -7.90133 | -46.62783 | 2025-10-11 04:32:00 | NOAA-21 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 57b75697-f916-3485-9532-b05995c3f388 | -7.26015 | -47.21449 | 2025-10-11 04:32:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e8b7a5fd-f3a0-310b-83cd-f95fd6180483 | -4.14445 | -47.66352 | 2025-10-11 04:32:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 31f2172d-e5fa-340e-b298-8327be2f040c | -6.65774 | -42.00003 | 2025-10-11 04:32:00 | NOAA-21 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 816d3902-02ac-34da-8a6c-4aa3cafee903 | -7.46742 | -46.73165 | 2025-10-11 04:32:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 0b77c92f-fb31-32e7-84af-2bb970214bc0 | -7.62316 | -47.83382 | 2025-10-11 04:32:00 | NOAA-21 | FILADÉLFIA | TOCANTINS | Brasil | 1707702 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 00b1c7eb-f646-32f8-a8f6-731fe913ca8c | -6.78486 | -44.51791 | 2025-10-11 04:32:00 | NOAA-21 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 0c13f011-e692-3a42-81dc-766e57908919 | -7.74283 | -44.69506 | 2025-10-11 04:32:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 658cc802-eb13-3619-a011-1203809e9c5b | -5.22273 | -45.6508 | 2025-10-11 04:32:00 | NOAA-21 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| ca76b66f-0e65-35fe-b5a8-dbbab8e425f0 | -8.16436 | -43.31532 | 2025-10-11 04:32:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 5.7 |
| 629dc84f-abc2-3367-b162-602b0adcf1b7 | -7.33806 | -43.8651 | 2025-10-11 04:32:00 | NOAA-21 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 973068c6-e1c1-386f-bf0b-1798581a1cd0 | -5.84849 | -43.4076 | 2025-10-11 04:32:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 8.2 |
| 5c43495d-251a-33af-ae0a-50c1430dbe8f | -7.80226 | -42.42592 | 2025-10-11 04:32:00 | NOAA-21 | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 85866ffe-7c11-3f7a-b45a-a9894baab5ee | -5.90917 | -45.42918 | 2025-10-11 04:32:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 6e69f7a3-fb2d-3f11-845f-a0c11c3b74f2 | -3.98687 | -46.27491 | 2025-10-11 04:32:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| b08c064a-2d74-3218-984f-782fe7bdd976 | -7.22634 | -45.32056 | 2025-10-11 04:32:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |


[Clique aqui para ver as próximas entradas](README18.md)
