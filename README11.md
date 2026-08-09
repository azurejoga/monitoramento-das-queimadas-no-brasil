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

## Dados Diários - Página 11

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| de3c217f-4a57-3793-b7c8-ee20dec24e12 | -8.1499 | -55.40743 | 2026-08-09 04:25:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6ec47084-3773-3728-9e93-34abbca2c66d | -6.83421 | -56.43325 | 2026-08-09 04:25:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| b4cde862-b03a-37b1-a307-ac67fe582a22 | -8.14566 | -55.39859 | 2026-08-09 04:25:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ee838435-0043-37ab-bd2f-7d68efce3343 | -5.73252 | -49.13747 | 2026-08-09 04:25:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| b59f5346-7c23-3ef8-92ba-27642e098ac7 | -7.58288 | -45.2149 | 2026-08-09 04:25:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 0bc0dd83-e1b9-3d38-968a-161620ac221a | -6.15239 | -47.1186 | 2026-08-09 04:25:00 | NOAA-20 | CAMPESTRE DO MARANHÃO | MARANHÃO | Brasil | 2102556 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| f5785c5c-dae7-3aea-b549-be5d28dbe3fd | -6.86716 | -44.43417 | 2026-08-09 04:25:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 5.6 |
| ba9180ce-d251-3936-859c-b22a66a864f6 | -8.15405 | -55.39907 | 2026-08-09 04:25:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| b998b2e7-c52b-35f8-8e55-72e3628a55fa | -6.83152 | -56.41319 | 2026-08-09 04:25:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 3b461f52-6de9-30cb-b77b-ed7b4d0ec337 | -6.84731 | -56.39631 | 2026-08-09 04:25:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| a30a02d3-1e1a-3925-b278-fb6464919ea1 | -6.82101 | -56.43585 | 2026-08-09 04:25:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 4a985179-2632-3ab2-8e02-66c6a4e11eeb | -4.8025 | -56.13397 | 2026-08-09 04:25:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 57e026ea-e579-3686-a26e-435f1cd5dd8f | -6.30552 | -43.61973 | 2026-08-09 04:25:00 | NOAA-20 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ddd4d77c-74cb-3713-9f14-857395cad82b | -11.62412 | -51.09423 | 2026-08-09 04:25:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 8.9 |
| 2dbb30ae-b25b-3f94-b88f-c615d27d58f6 | -11.04929 | -44.27716 | 2026-08-09 04:25:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| bb41812d-6f2f-39ea-ad3e-c0f513eeb504 | -10.25277 | -45.81884 | 2026-08-09 04:25:00 | NOAA-20 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 7c7a2760-9349-3fa1-9ae3-4ef5ddf56cbf | -6.8377 | -56.41415 | 2026-08-09 04:25:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 7.4 |
| 0e10df32-2911-3065-81e2-cb8f350857ab | -6.98083 | -42.9029 | 2026-08-09 04:25:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| f8c7bb2e-eda1-3125-be6e-c14d0637e033 | -7.08719 | -42.26844 | 2026-08-09 04:25:00 | NOAA-20 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 1409b094-2bc3-3cb7-8f2a-27891781bb23 | -5.66237 | -43.56332 | 2026-08-09 04:25:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 0.3 |
| a55e8007-bf21-3ecf-8163-8cd0e4493817 | -7.31457 | -55.11752 | 2026-08-09 04:25:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4fb84e85-680e-3ad8-817c-f0e1782a4eff | -6.70452 | -58.95228 | 2026-08-09 04:25:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 5526ca5c-12bb-39e5-9cf9-e79c6042b631 | -6.82276 | -56.42634 | 2026-08-09 04:25:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 1dff4024-8313-3564-a2c6-fc159f9cdf52 | -11.0459 | -44.27663 | 2026-08-09 04:25:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 9be688a3-c55b-3161-9631-fbe531ce8be9 | -7.58728 | -45.20849 | 2026-08-09 04:25:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 20.1 |
| 5a6b41f3-6567-3e4c-a4e2-559858a7acce | -10.87799 | -50.37059 | 2026-08-09 04:25:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a6259699-77c0-33b0-b31b-90a2551900bf | -6.85258 | -56.40221 | 2026-08-09 04:25:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 33a1dac5-5bcb-3561-86c9-54cd40cc642d | -5.88043 | -46.50363 | 2026-08-09 04:25:00 | NOAA-20 | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| e2940cd0-ac29-3437-9314-b2e234f1c9e9 | -6.85084 | -56.41179 | 2026-08-09 04:25:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 123c5562-cefc-3215-b02d-56524259866e | -11.27091 | -44.86576 | 2026-08-09 04:25:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 541994c6-7636-3802-b730-fccab6f4509c | -7.08424 | -42.26395 | 2026-08-09 04:25:00 | NOAA-20 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 0ed506f7-ea45-3aab-bfdc-59e45c05a219 | -10.22852 | -45.80061 | 2026-08-09 04:25:00 | NOAA-20 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 7426e001-a404-3b45-bc56-f7642023faf1 | -9.47005 | -40.32236 | 2026-08-09 04:25:00 | NOAA-20 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 120.2 |
| 6c2440f8-75c1-391a-afb5-5b80f83d3e8e | -6.83599 | -56.42355 | 2026-08-09 04:25:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 9e996407-14b2-304c-abb8-f3faff638a78 | -6.83941 | -56.40483 | 2026-08-09 04:25:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| c9dfce82-401c-3f05-86c4-65ef25728eac | -6.64568 | -56.43055 | 2026-08-09 04:25:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 034b3cd7-1683-3c30-a270-087f089d4cf6 | -6.64476 | -56.43565 | 2026-08-09 04:25:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 85d1323c-e36c-384f-bf95-f816b699b682 | -8.31556 | -46.39365 | 2026-08-09 04:25:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 46d42f7b-0c9e-3bc4-b6e5-ae94549128e4 | -9.81197 | -45.25448 | 2026-08-09 04:25:00 | NOAA-20 | MONTE ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2206605 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 64dd725b-7494-304c-a677-7a5765566df0 | -7.42782 | -45.67758 | 2026-08-09 04:25:00 | NOAA-20 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 8d986165-8238-3a43-bfb4-2d34239c7aab | -11.0425 | -44.2761 | 2026-08-09 04:25:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| f6cef7f0-ab3e-37c1-8944-403025e7789f | -6.41372 | -55.79139 | 2026-08-09 04:25:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 6bb6c23b-52de-3ef8-8a01-e12e7dadc1da | -10.716 | -49.34311 | 2026-08-09 04:25:00 | NOAA-20 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f56ef18c-c9b5-3be5-8d85-36f109204a94 | -10.87712 | -50.36872 | 2026-08-09 04:25:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 3f4a731e-036a-3c0b-8138-ba7d703bc378 | -6.82452 | -56.41676 | 2026-08-09 04:25:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 1652e51d-8c09-3834-895f-3918517f6093 | -11.26756 | -44.86523 | 2026-08-09 04:25:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| edffc6b9-8f6c-3f59-a821-1f2c41f64d04 | -8.64929 | -45.88154 | 2026-08-09 04:25:00 | NOAA-20 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 07f785a4-e816-3576-84fa-9485c356a180 | -10.93365 | -50.27978 | 2026-08-09 04:25:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 9ab65fc8-463d-3617-a832-f809385d79f5 | -7.60749 | -49.69024 | 2026-08-09 04:25:00 | NOAA-20 | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| b6c58584-0908-3e95-b23a-9f54692ebe82 | -8.1477 | -55.40179 | 2026-08-09 04:25:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8e6ebfca-1b15-34c9-bac4-72971b567b77 | -6.65021 | -56.4337 | 2026-08-09 04:25:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 753b27e2-f062-3f9d-8427-30d4ab4481e7 | -6.97504 | -41.49565 | 2026-08-09 04:25:00 | NOAA-20 | SANTANA DO PIAUÍ | PIAUÍ | Brasil | 2209351 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 3d564f73-3ce4-3558-8263-a68f9b7ae0f6 | -6.82718 | -56.43691 | 2026-08-09 04:25:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 7888956c-cdbb-3c8b-8508-0183bc32861d | -12.26677 | -43.51089 | 2026-08-09 04:25:00 | NOAA-20 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 6bd40a85-00f6-3f04-b7a1-30302f3b774f | -6.88773 | -58.93729 | 2026-08-09 04:25:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 99b46f14-b405-3b2a-b8c3-73229021ed55 | -4.51965 | -48.05726 | 2026-08-09 04:25:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 76f982a4-530e-3f77-a700-962c8c66187c | -10.22907 | -45.79712 | 2026-08-09 04:25:00 | NOAA-20 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 83b6475e-3540-3cfa-9bbb-2db2a77f5ff4 | -6.85172 | -56.40691 | 2026-08-09 04:25:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 9b84104c-4b07-3691-948f-590a8c58b2b4 | -8.33178 | -46.37809 | 2026-08-09 04:25:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| c019c4f0-56be-321c-a409-35a959e51a3c | -7.00788 | -42.02591 | 2026-08-09 04:25:00 | NOAA-20 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 93515251-b268-3550-b7e6-e7fd3cc00b2f | -7.57076 | -44.38715 | 2026-08-09 04:25:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| ca107361-2c13-3e26-be4c-8910286fa402 | -10.23182 | -45.80114 | 2026-08-09 04:25:00 | NOAA-20 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| b732ccd7-ccbd-3805-a5c8-7c6b6c7b1b8f | -8.15197 | -55.39592 | 2026-08-09 04:25:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e8944b26-c6e6-319b-a86a-2bf773b59b6c | -6.81578 | -56.42969 | 2026-08-09 04:25:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 8ea734c1-755e-33b2-992a-3eb7210ce00d | -10.52971 | -46.61532 | 2026-08-09 04:25:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| d01f327d-fd9e-399d-a372-66210aa2bbdc | -9.63443 | -45.51879 | 2026-08-09 04:25:00 | NOAA-20 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 2cc50e4d-8208-31b6-a63a-d7697723f387 | -6.98026 | -42.90666 | 2026-08-09 04:25:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| f3d3f98e-7d63-33f4-9d52-a3896478bb06 | -11.62205 | -51.09715 | 2026-08-09 04:25:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 5.2 |
| fbe79b4f-a56c-3bfd-bc84-34565ddd0acd | -8.33121 | -46.38161 | 2026-08-09 04:25:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 829fa2b0-5666-3936-a753-ba671022faeb | -12.10142 | -47.21849 | 2026-08-09 04:25:00 | NOAA-20 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 8e9a2fd8-6818-3c98-84c3-30809f9b322a | -6.82632 | -56.4416 | 2026-08-09 04:25:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| c6244e00-53a1-3118-a9f5-6aff85ee74d5 | -6.8324 | -56.40841 | 2026-08-09 04:25:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 8c0ac14f-08bc-3df6-8d6a-5fb6bd2dda89 | -5.88383 | -46.50417 | 2026-08-09 04:25:00 | NOAA-20 | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 32f4cb32-2fb8-3d35-b729-13b134007c32 | -10.93449 | -50.27493 | 2026-08-09 04:25:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 603ea395-7f34-339c-b6e2-a6fcdae6ac23 | -8.58144 | -45.38902 | 2026-08-09 04:25:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 841748c9-14ea-3944-93ab-d4cca0697762 | -6.92531 | -42.42762 | 2026-08-09 04:25:00 | NOAA-20 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 7057b207-1c9d-3e2b-b28e-818d5cdf214e | -11.27425 | -44.86629 | 2026-08-09 04:25:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| e3ce8631-232e-3867-aa33-0a9aff6709cc | -9.46702 | -40.31441 | 2026-08-09 04:25:00 | NOAA-20 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 3.3 |
| ffd72a83-ba8c-3643-9ae3-d4016db436f2 | -10.71235 | -49.34243 | 2026-08-09 04:25:00 | NOAA-20 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 8320c424-1395-3a71-b844-aa6cda8ae093 | -6.84647 | -56.40092 | 2026-08-09 04:25:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 752bb462-f3c3-3e5e-8c55-eeded6fe0dde | -12.11085 | -47.22376 | 2026-08-09 04:25:00 | NOAA-20 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 69109e5b-7915-3491-b180-cbb6eb87ecd3 | -7.58343 | -45.21143 | 2026-08-09 04:25:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 23.2 |
| 6f985cc8-d993-35a7-9c67-c043083e5001 | -8.64875 | -45.8636 | 2026-08-09 04:25:00 | NOAA-20 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 1082675b-d7ae-3187-bad8-94de969cecd7 | -10.50798 | -46.6266 | 2026-08-09 04:25:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 5c809216-c69b-3ca7-8bef-d107243e8f74 | -8.04577 | -46.90904 | 2026-08-09 04:25:00 | NOAA-20 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| d761e6a4-9a3c-3630-b780-147a983aa983 | -6.88066 | -58.93572 | 2026-08-09 04:25:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.0 |
| d59bb4ef-9a29-3feb-8eb2-4dc94b5b19cb | -10.25332 | -45.81535 | 2026-08-09 04:25:00 | NOAA-20 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 21a35990-3e61-33e3-a13f-87751893a08a | -7.17968 | -42.35116 | 2026-08-09 04:25:00 | NOAA-20 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 992470e9-dccf-3973-a507-9220065d2679 | -6.87927 | -58.94297 | 2026-08-09 04:25:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 20356f4a-c6e0-34a8-a10e-3d9c33f18d84 | -8.33512 | -46.37863 | 2026-08-09 04:25:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 8f85b5f6-a967-304f-803d-4709be432078 | -8.15128 | -55.39972 | 2026-08-09 04:25:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7ab6259a-2cda-38f6-881b-cae10a83ea45 | -7.45173 | -46.87394 | 2026-08-09 04:25:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 4c4346b6-2ada-35f9-bbaa-6560506d407a | -6.87458 | -44.92508 | 2026-08-09 04:25:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| eb7f9629-a81f-3aa8-9287-829153ba28b2 | -6.8534 | -56.3977 | 2026-08-09 04:25:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 9714bd21-ed27-322e-aa42-240f834ee5cd | -8.0138 | -44.48585 | 2026-08-09 04:25:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 2b99c720-0109-3b59-8d4b-26513601f9eb | -12.11419 | -47.22432 | 2026-08-09 04:25:00 | NOAA-20 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 90e95054-0392-386e-8478-8e7808a659db | -8.04518 | -46.9127 | 2026-08-09 04:25:00 | NOAA-20 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 195af1d7-89f6-39e3-8e61-75b784d3788a | -4.52037 | -48.05277 | 2026-08-09 04:25:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 8e3e5edc-b670-3e8c-86fc-d455ce5b3cb5 | -6.60614 | -56.36789 | 2026-08-09 04:25:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| fc1fceb6-fee6-3cec-b313-644c911fd0f5 | -9.47361 | -40.32661 | 2026-08-09 04:25:00 | NOAA-20 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 68.0 |


[Clique aqui para ver as próximas entradas](README12.md)
