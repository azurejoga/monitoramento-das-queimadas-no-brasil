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

## Dados Diários - Página 34

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 5c470a9f-a82f-37a6-9cf4-6ed2c75b0071 | -5.83418 | -43.00294 | 2025-09-04 04:25:00 | NOAA-21 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 3.8 |
| 7aaf28c6-3d73-3813-968b-f84ccd69fc43 | -4.78463 | -43.81889 | 2025-09-04 04:25:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 3ad38b6b-62b8-3c42-b840-856a907e192a | -5.77119 | -44.86773 | 2025-09-04 04:25:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 776b813f-5917-3825-9b81-0954989f8b06 | -5.83481 | -42.99873 | 2025-09-04 04:25:00 | NOAA-21 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 3.1 |
| 9388e299-5c7d-3900-9997-a149326825c9 | -6.50035 | -44.08648 | 2025-09-04 04:25:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 96801f4f-cc6a-33db-b511-bc8d9763acb7 | -6.35249 | -43.76741 | 2025-09-04 04:25:00 | NOAA-21 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 27a6c57c-2363-32ab-bfb0-a32f49f62cce | -5.74557 | -45.53972 | 2025-09-04 04:25:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 44dd737d-c0c5-3db8-a12a-5af7c14ed656 | -5.48223 | -45.21935 | 2025-09-04 04:25:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| faf9ea97-9aff-39d5-a66f-fefa5784ffc7 | -3.41516 | -51.56684 | 2025-09-04 04:25:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 4f57dd42-9e38-34bf-8bdb-3b92e935dd4b | -5.78268 | -45.25513 | 2025-09-04 04:25:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 895f4d9c-c4be-3317-bb03-9e24e7009baf | -5.30183 | -55.97322 | 2025-09-04 04:25:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| c7fd299c-5248-3f39-828e-26884b22577e | -8.0312 | -44.06333 | 2025-09-04 04:25:00 | NOAA-21 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| dcfe62dc-09fd-3417-9c6b-3a9a16167ed7 | -6.26487 | -42.64405 | 2025-09-04 04:25:00 | NOAA-21 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 2b243412-2648-34d3-9561-71039aa7be73 | -6.28521 | -43.85005 | 2025-09-04 04:25:00 | NOAA-21 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 75a423cd-234a-34c7-bab6-0bb4e3616856 | -6.13867 | -42.97002 | 2025-09-04 04:25:00 | NOAA-21 | AMARANTE | PIAUÍ | Brasil | 2200509 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 5744ed9d-06b6-39ed-88a7-e10d77dbac00 | -6.23346 | -43.38116 | 2025-09-04 04:25:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 28afc50a-be4a-3db2-ae82-210ec99b97f3 | -6.6235 | -43.96623 | 2025-09-04 04:25:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 2ef783e9-9d8f-340e-a020-5f6ae0700390 | -8.00876 | -44.77768 | 2025-09-04 04:25:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 3eacfac5-481e-3df8-9641-a983b04d796b | -6.7674 | -44.47864 | 2025-09-04 04:25:00 | NOAA-21 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| db2a5ba7-9f9f-3ba2-af05-bd2cbb43aadc | -5.48781 | -45.22741 | 2025-09-04 04:25:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 6bc98157-cf65-3252-99d2-61ccc873290e | -6.98295 | -43.28019 | 2025-09-04 04:25:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| c868a76c-0422-3c14-9b73-7d75397d0620 | -5.99239 | -44.77628 | 2025-09-04 04:25:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 04a236f4-cf5c-33a2-8b2e-098fb82a8d57 | -6.09784 | -43.26907 | 2025-09-04 04:25:00 | NOAA-21 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 0a451f04-8dfa-3910-a574-449c771cbb54 | -8.02825 | -44.05887 | 2025-09-04 04:25:00 | NOAA-21 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 15da41be-88ee-3651-b1c6-96e8d18647dc | -5.60679 | -45.02879 | 2025-09-04 04:25:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 9.3 |
| becf0be3-a1bc-35c4-9924-6552ea6b65ce | -6.49687 | -44.08602 | 2025-09-04 04:25:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 9c40fbd5-6c1a-3a5a-a534-f66739c250a9 | -6.84338 | -46.39661 | 2025-09-04 04:25:00 | NOAA-21 | SÃO PEDRO DOS CRENTES | MARANHÃO | Brasil | 2111573 | 21 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 6b9630b4-0cb8-3c36-8cfc-4e25b93c932d | -5.70305 | -45.39688 | 2025-09-04 04:25:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| baac8a31-1c68-3f72-9652-aea50792a973 | -7.67103 | -42.71484 | 2025-09-04 04:25:00 | NOAA-21 | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 071886dc-449f-352a-b85e-bc0528dd47c0 | -5.92761 | -44.16585 | 2025-09-04 04:25:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 33e3a59e-70ef-39d0-8a34-afc7da8befa5 | -5.68544 | -45.59763 | 2025-09-04 04:25:00 | NOAA-21 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| dc451fd5-f3bb-3686-be2f-6909cb309a9e | -6.2671 | -42.64214 | 2025-09-04 04:25:00 | NOAA-21 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 3.2 |
| 4b447f29-f721-3993-aa83-83747074e760 | -6.25848 | -43.31306 | 2025-09-04 04:25:00 | NOAA-21 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| cec3258c-a4b3-3bf2-af6f-38fed270ca9e | -5.85872 | -45.64281 | 2025-09-04 04:25:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| dccf2673-afbc-3ad7-bb6d-932c485659e7 | -6.76089 | -45.92303 | 2025-09-04 04:25:00 | NOAA-21 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| aea8e062-53e1-3ded-87be-7266c76ae265 | -4.3293 | -48.39154 | 2025-09-04 04:25:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 38c2d71d-7df8-3067-81c2-897dd2965187 | -5.48061 | -45.22986 | 2025-09-04 04:25:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 5bb5a569-8bbb-381c-9109-b4942dea8a42 | -6.12388 | -43.91355 | 2025-09-04 04:25:00 | NOAA-21 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 2f11a7a9-942d-3766-af9e-2e5180801567 | -1.98292 | -47.97634 | 2025-09-04 04:25:00 | NOAA-21 | CONCÓRDIA DO PARÁ | PARÁ | Brasil | 1502756 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 48040a9b-a9bd-3c75-bd61-b2ef1ee28359 | -6.87904 | -45.55476 | 2025-09-04 04:25:00 | NOAA-21 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| d8208919-e199-3a76-8c56-8c3618bd93b6 | -5.1801 | -43.04481 | 2025-09-04 04:25:00 | NOAA-21 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f1eeabf5-3dc6-32cb-b8f8-2fed68fdc78f | -7.60637 | -46.21608 | 2025-09-04 04:25:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| ac9333ae-17d8-3a64-a165-232bd082497b | -5.62729 | -51.13846 | 2025-09-04 04:25:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| d82b9883-fd00-3f0b-add2-de203738d410 | -6.25077 | -43.55299 | 2025-09-04 04:25:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 0c7cad47-143c-333f-8d75-3df2967b7476 | -5.18073 | -43.04063 | 2025-09-04 04:25:00 | NOAA-21 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b03fd61a-f141-31ba-a78e-6e2e7d65c84d | -8.61036 | -40.30753 | 2025-09-04 04:25:00 | NOAA-21 | LAGOA GRANDE | PERNAMBUCO | Brasil | 2608750 | 26 | 33 | nan | nan | nan | Caatinga | 7.4 |
| 1a3688e4-62cb-3fb0-add8-62eaa3f09b68 | -3.22434 | -47.12435 | 2025-09-04 04:25:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 2db40fb7-3caa-359d-90df-18b001833f6a | -6.69433 | -48.40682 | 2025-09-04 04:25:00 | NOAA-21 | XAMBIOÁ | TOCANTINS | Brasil | 1722107 | 17 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 607b9fce-3c8f-3ed3-a734-657f8e0a0e5e | -6.26871 | -43.50562 | 2025-09-04 04:25:00 | NOAA-21 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 42e312ad-6935-3fd1-a81d-5db2d8da19c9 | -6.69032 | -48.40995 | 2025-09-04 04:25:00 | NOAA-21 | XAMBIOÁ | TOCANTINS | Brasil | 1722107 | 17 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 760ef24c-4f6a-30f5-be98-472a75d3300d | -6.22226 | -44.74092 | 2025-09-04 04:25:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 8efb5fda-7f7c-3dd7-b133-d4e95038e76c | -3.40556 | -46.9053 | 2025-09-04 04:25:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 44993d6c-9ab9-31ce-8e7d-694db7b0a238 | -5.71004 | -45.32985 | 2025-09-04 04:25:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| ff2ae691-918c-3424-9214-dba13cb001ae | -4.62126 | -47.41627 | 2025-09-04 04:25:00 | NOAA-21 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| daa041fe-9fdd-302c-a1b2-da519300c6db | -5.27622 | -55.95974 | 2025-09-04 04:25:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e19de3e5-8501-326d-8dad-55ace92a1001 | -6.2698 | -43.32576 | 2025-09-04 04:25:00 | NOAA-21 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| ca08502a-d0eb-3dbf-b7de-c289018b3997 | -6.7971 | -44.10242 | 2025-09-04 04:25:00 | NOAA-21 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| afb7e6bf-c4cf-33b3-865d-04827b3adcb3 | -7.55024 | -45.71999 | 2025-09-04 04:25:00 | NOAA-21 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| ab8de2c2-0f03-3c1b-bc11-b46b0bd570a9 | -6.13153 | -44.14264 | 2025-09-04 04:25:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| e1af67ef-4f92-3d55-8858-d6cf5149eeb7 | -6.1275 | -44.14585 | 2025-09-04 04:25:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| e75bcf88-2955-36e4-a93b-6c7116367ad7 | -5.88519 | -43.23949 | 2025-09-04 04:25:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 5901da83-dd22-3a67-b9a8-8eb0cb918891 | -6.03767 | -46.0009 | 2025-09-04 04:25:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 31e40760-84d5-3907-94a0-c8153aeb4096 | -5.90746 | -44.16294 | 2025-09-04 04:25:00 | NOAA-21 | JATOBÁ | MARANHÃO | Brasil | 2105450 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| cf16bebc-36d5-3511-8352-d877ec818519 | -6.25529 | -42.64474 | 2025-09-04 04:25:00 | NOAA-21 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 8908d79e-ee93-389e-960d-2b9625a80752 | -6.68072 | -48.40444 | 2025-09-04 04:25:00 | NOAA-21 | XAMBIOÁ | TOCANTINS | Brasil | 1722107 | 17 | 33 | nan | nan | nan | Amazônia | 10.4 |
| f2e29441-6212-39af-b76d-8548fd7e6441 | -5.67255 | -43.66865 | 2025-09-04 04:25:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 1fcecc8f-b473-36b7-87d5-561393a03d06 | -7.13139 | -44.45953 | 2025-09-04 04:25:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 0880b9ef-fd17-33df-8f3a-3d893b9327bb | -3.16331 | -48.6071 | 2025-09-04 04:25:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f0f53f67-ca96-3ce5-be38-3cf6019aa558 | -5.70117 | -45.16641 | 2025-09-04 04:25:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| d1490822-bf53-39f0-8865-ca3c2b62bf47 | -7.41443 | -42.04109 | 2025-09-04 04:25:00 | NOAA-21 | SANTO INÁCIO DO PIAUÍ | PIAUÍ | Brasil | 2209500 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 30af3d29-4e17-3b69-8d82-cfced1689538 | -4.39384 | -47.2815 | 2025-09-04 04:25:00 | NOAA-21 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 0.5 |
| d2ce38e4-5556-3590-8d3b-03664a37e7fd | -6.26321 | -45.09343 | 2025-09-04 04:25:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| cd312ace-3760-35ea-bfea-a84e619a85a6 | -6.36425 | -45.62928 | 2025-09-04 04:25:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 33d74403-48df-3cab-94f6-459a3e28e211 | -6.82291 | -45.67548 | 2025-09-04 04:25:00 | NOAA-21 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| a742f0ea-fc21-3b6e-a8cf-42c1d92ddbea | -7.04872 | -43.26752 | 2025-09-04 04:25:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| 152d674a-e98c-354b-9170-a673cd8b2d52 | -6.50758 | -43.07881 | 2025-09-04 04:25:00 | NOAA-21 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 946e23b5-1386-3eb3-be2f-49bd761c10c8 | -7.55079 | -45.71646 | 2025-09-04 04:25:00 | NOAA-21 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| c97ea1c4-ee21-3c39-9329-6930fcd9f4ea | -5.69034 | -45.93918 | 2025-09-04 04:25:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| f8d8e0e9-b053-3964-b06d-498a2ad7e9ae | -6.63051 | -43.96714 | 2025-09-04 04:25:00 | NOAA-21 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 29e0d497-7744-3350-a97e-ccdb0f1c9e0d | -6.51109 | -42.18022 | 2025-09-04 04:25:00 | NOAA-21 | VÁRZEA GRANDE | PIAUÍ | Brasil | 2211407 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| d6cff195-8f25-3fa5-a6c1-e85b69d2bdf0 | -8.03001 | -44.07138 | 2025-09-04 04:25:00 | NOAA-21 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 286d27c3-c9d2-3cd9-a819-fe90d21d9cbb | -6.02996 | -46.66011 | 2025-09-04 04:25:00 | NOAA-21 | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 8b00b591-7218-3712-8026-0b1be73f5d9e | -5.91701 | -43.41565 | 2025-09-04 04:25:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| a3f6b0f7-68ed-3fd7-a4c3-d5cecee0aa54 | -6.75427 | -45.92199 | 2025-09-04 04:25:00 | NOAA-21 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ae065386-58c9-3af0-9486-4f3de11e351f | -5.68927 | -45.94608 | 2025-09-04 04:25:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| ebd640ff-80c9-3b76-952e-11a9289e8fa9 | -5.6029 | -45.03181 | 2025-09-04 04:25:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 3bc6d9be-47c2-349b-9201-446be2d2417e | -6.84008 | -46.3961 | 2025-09-04 04:25:00 | NOAA-21 | SÃO PEDRO DOS CRENTES | MARANHÃO | Brasil | 2111573 | 21 | 33 | nan | nan | nan | Cerrado | 4.8 |
| c02e3620-26de-30e8-a000-3cbdd0494296 | -6.36682 | -44.43827 | 2025-09-04 04:25:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| f587dc78-494c-33b2-86c0-b54e0ce5e294 | -5.67102 | -43.6728 | 2025-09-04 04:25:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| fa3d7473-54ec-33d9-b1fb-e41e567b4174 | -6.90089 | -43.80402 | 2025-09-04 04:25:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 125fec12-47ad-35ce-83cd-82fe2445be59 | -6.84998 | -44.25903 | 2025-09-04 04:25:00 | NOAA-21 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e9f7028d-c9e5-3844-a61a-826d5dc5053a | -6.71008 | -44.1841 | 2025-09-04 04:25:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| b06f10ac-a6a0-3208-a128-92674f550a3a | -6.17705 | -43.31766 | 2025-09-04 04:25:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| b0a60024-9618-35f3-be08-b84e8ba99a79 | -6.77083 | -44.47918 | 2025-09-04 04:25:00 | NOAA-21 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 5f2e0b79-c67a-3c6a-8924-9d56575a27c2 | -6.45949 | -42.39701 | 2025-09-04 04:25:00 | NOAA-21 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 29771c14-6d39-3776-8ef3-5b0d7668f666 | -5.50807 | -42.6559 | 2025-09-04 04:25:00 | NOAA-21 | LAGOA DO PIAUÍ | PIAUÍ | Brasil | 2205581 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| fde56804-be18-3b69-a1fc-e8a09ffb2bff | -7.60968 | -46.21661 | 2025-09-04 04:25:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 58a44796-bc3f-3c07-9e91-be53088ed88e | -5.98675 | -44.14803 | 2025-09-04 04:25:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 28f89eda-e2cb-3d00-bb5f-97f319ae8e08 | -6.75704 | -45.92596 | 2025-09-04 04:25:00 | NOAA-21 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| bdda824d-ddbd-3bb0-8dff-71bfa95dbf93 | -6.73323 | -42.27574 | 2025-09-04 04:25:00 | NOAA-21 | TANQUE DO PIAUÍ | PIAUÍ | Brasil | 2210979 | 22 | 33 | nan | nan | nan | Caatinga | 6.3 |


[Clique aqui para ver as próximas entradas](README35.md)
