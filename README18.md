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

## Dados Diários - Página 18

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| e9f88be8-98fa-3d6c-bb68-4bcfdb0f18f5 | -6.43022 | -35.25055 | 2024-11-19 03:53:00 | NOAA-20 | PEDRO VELHO | RIO GRANDE DO NORTE | Brasil | 2409803 | 24 | 33 | nan | nan | nan | Mata Atlântica | 2.9 |
| d3e4f1d6-ded9-3738-b67d-61ff182fa85a | -5.58261 | -44.87976 | 2024-11-19 03:53:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 7.2 |
| fe3ccd97-8e73-36e7-83eb-992386ebef16 | -5.96403 | -46.3091 | 2024-11-19 03:53:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 7779226d-c227-33b2-b189-b8675297738e | -4.11393 | -43.58754 | 2024-11-19 03:53:00 | NOAA-20 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 14.0 |
| d3fb5e00-e866-36e4-97be-d7277e22bbf8 | -4.10904 | -43.59084 | 2024-11-19 03:53:00 | NOAA-20 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 14.0 |
| 9dcc0119-dd58-30c3-9660-4be03cc9866d | -2.68382 | -46.07601 | 2024-11-19 03:53:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b3ca9d05-8ce8-3eb5-897e-555879446510 | -2.49338 | -49.02929 | 2024-11-19 03:53:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 7.7 |
| 2afed294-0da9-3a03-893b-8cd1dc12eb98 | -11.02219 | -41.73489 | 2024-11-19 03:53:00 | NOAA-20 | SÃO GABRIEL | BAHIA | Brasil | 2929255 | 29 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 2120a9bf-8332-3deb-8163-dd57909709b3 | -1.99718 | -45.34886 | 2024-11-19 03:53:00 | NOAA-20 | TURIAÇU | MARANHÃO | Brasil | 2112407 | 21 | 33 | nan | nan | nan | Amazônia | 7.4 |
| d714f44b-ef5a-3525-a053-eeaa6b83a183 | -3.9734 | -49.91967 | 2024-11-19 03:53:00 | NOAA-20 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 57ededb5-ef51-37ab-bfba-c6a6f0a6e963 | -7.87533 | -34.83834 | 2024-11-19 03:53:00 | NOAA-20 | PAULISTA | PERNAMBUCO | Brasil | 2610707 | 26 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 3c58e02f-7d78-359a-8cd3-f6173b1b08f2 | -4.55941 | -48.01928 | 2024-11-19 03:53:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 37c9df95-2169-3b59-a34c-b52283109f24 | -6.93282 | -42.81285 | 2024-11-19 03:53:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 3.3 |
| 71261872-107e-342b-8492-bae7f82436bb | -6.93246 | -45.08799 | 2024-11-19 03:53:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 5e1626c5-23aa-3025-9944-f8e6e82b10c5 | -4.18475 | -48.56538 | 2024-11-19 03:53:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| faccd44c-aaf8-35ed-8dde-37d5c6c3e681 | -4.94677 | -47.80754 | 2024-11-19 03:53:00 | NOAA-20 | CIDELÂNDIA | MARANHÃO | Brasil | 2103257 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 328482ef-819d-3da4-9fc3-e3bc52870029 | -11.24169 | -44.65328 | 2024-11-19 03:53:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| ec5ba704-2846-3026-a864-ec13462dec93 | -3.75137 | -44.57099 | 2024-11-19 03:53:00 | NOAA-20 | MATÕES DO NORTE | MARANHÃO | Brasil | 2106631 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 6c90bf9d-b89e-3b5f-971a-3a5e7c90c1b4 | -3.33214 | -50.49859 | 2024-11-19 03:53:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 8252729a-00cb-319a-bc2b-663bcc73ee6e | -5.53267 | -39.17323 | 2024-11-19 03:53:00 | NOAA-20 | MILHÃ | CEARÁ | Brasil | 2308351 | 23 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 1a9b5330-485f-38e2-905c-fd31a1dd7069 | -13.47556 | -44.07146 | 2024-11-19 03:53:00 | NOAA-20 | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 60583789-0d48-3d2f-81e0-1b41e5fb0655 | -6.28813 | -46.13038 | 2024-11-19 03:53:00 | NOAA-20 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| c0df4bf5-a2ca-35da-8eff-3c9dc5d8e7b9 | -10.72551 | -44.49645 | 2024-11-19 03:53:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 8b136e1d-a742-3801-886c-a4b6555dc27b | -10.40132 | -44.48492 | 2024-11-19 03:53:00 | NOAA-20 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a4cd183b-0e84-3a21-9ad0-05c886a82e0a | -10.40261 | -44.47762 | 2024-11-19 03:53:00 | NOAA-20 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| f3e89727-6c58-3596-9036-bd2c77c2451d | -4.81897 | -47.32197 | 2024-11-19 03:53:00 | NOAA-20 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 3204a74b-3801-34cc-ad87-4dbf7b6731cf | -13.77822 | -41.8801 | 2024-11-19 03:53:00 | NOAA-20 | LIVRAMENTO DE NOSSA SENHORA | BAHIA | Brasil | 2919504 | 29 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 6e035202-4041-35cb-a69e-97be0f27f28d | -6.19991 | -46.32013 | 2024-11-19 03:53:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| af18de5f-12b6-32d3-bc80-65c87a83958c | -2.49065 | -49.03203 | 2024-11-19 03:53:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 13.3 |
| bc046552-d6fe-3556-b043-83225c5e199c | -11.53032 | -45.00669 | 2024-11-19 03:53:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 19f16bb2-5727-3a20-9e50-306f70616de8 | -7.40297 | -42.76386 | 2024-11-19 03:53:00 | NOAA-20 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 5.8 |
| 3c7d520a-a9e3-3f1f-955c-a97d7e695259 | -4.55873 | -48.02331 | 2024-11-19 03:53:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| cef8f7fc-3237-31b9-91d4-b2708d8ddbf7 | -3.48133 | -48.25464 | 2024-11-19 03:53:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| a80ae6ef-f0bf-3968-afc7-efbaac7609e9 | -7.39533 | -42.76258 | 2024-11-19 03:53:00 | NOAA-20 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 9c07a3a0-2dda-3d72-b910-455785f28e68 | -7.83728 | -34.91518 | 2024-11-19 03:53:00 | NOAA-20 | IGARASSU | PERNAMBUCO | Brasil | 2606804 | 26 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| c357a7c1-54f9-3da7-9435-69ba27548a76 | -3.41616 | -42.3878 | 2024-11-19 03:53:00 | NOAA-20 | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 9966f16a-2ad1-34c5-aab9-0e472b285247 | -5.97608 | -45.36261 | 2024-11-19 03:53:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 20.5 |
| ff7789ab-432d-3801-ac4d-1ea2a294fd18 | -12.63605 | -48.81567 | 2024-11-19 03:53:00 | NOAA-20 | TALISMÃ | TOCANTINS | Brasil | 1720978 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| b9c978b8-0fe7-3718-8160-59b89b761d92 | -5.97526 | -45.36745 | 2024-11-19 03:53:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 20.5 |
| f7e4fc00-0d68-3e96-8737-153f0917f0fb | -6.92974 | -45.09102 | 2024-11-19 03:53:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 0c03d99f-cd62-312a-82f5-d69b6bab1589 | -3.70325 | -43.47504 | 2024-11-19 03:53:00 | NOAA-20 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| cdc3ebdb-582f-345c-af29-c4b2e993cba1 | -3.66132 | -50.44415 | 2024-11-19 03:53:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| cd8d7316-7173-34b1-8c3b-85105ff08798 | -12.6504 | -48.8252 | 2024-11-19 03:53:00 | NOAA-20 | TALISMÃ | TOCANTINS | Brasil | 1720978 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| f78c181a-ec5c-3028-b312-104295a89f9e | -2.70951 | -46.08035 | 2024-11-19 03:53:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 7370ab71-ba98-3459-9a2a-fa54e93fc2c3 | -2.39477 | -45.80691 | 2024-11-19 03:53:00 | NOAA-20 | PRESIDENTE MÉDICI | MARANHÃO | Brasil | 2109239 | 21 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 8f337895-a105-34ce-b32f-066634e8d082 | -7.3961 | -42.75789 | 2024-11-19 03:53:00 | NOAA-20 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 921b11a9-9b5c-3ed1-b888-f8e5edef5410 | -5.60061 | -44.88322 | 2024-11-19 03:53:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 97ef6054-6873-3c6a-87bf-8c4a5e3813ef | -10.97287 | -44.44516 | 2024-11-19 03:53:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 2fe62a2a-a7a8-3c7c-8ccf-f35cfa9b2f3f | -3.5685 | -51.45274 | 2024-11-19 03:53:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 505e449d-7cd3-3e72-a120-09dcb953da72 | -10.90149 | -44.56581 | 2024-11-19 03:53:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 097ad74e-03be-35c3-a8ef-0cf3d27a1c9a | -10.50801 | -44.88276 | 2024-11-19 03:53:00 | NOAA-20 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| fc416fb3-a04a-3a55-9498-01ed87d7a659 | -3.33764 | -45.36097 | 2024-11-19 03:53:00 | NOAA-20 | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | 3.2 |
| e26d53a3-f552-3f64-a387-3f078bb46302 | -4.10568 | -51.06657 | 2024-11-19 03:53:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| e996682a-6267-3912-866c-5a0245c8a95b | -4.09803 | -48.48253 | 2024-11-19 03:53:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 50fbe7f5-f5c5-3bc3-b095-b7c538a3fce8 | -4.22628 | -47.18337 | 2024-11-19 03:53:00 | NOAA-20 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 80445671-eba8-3ab9-8b71-55b6b826966a | -3.33783 | -50.50583 | 2024-11-19 03:53:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 0854299e-35bc-39f6-a06b-c817afc120c8 | -2.47619 | -49.11671 | 2024-11-19 03:53:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| e5f4adb9-a0cc-3ef4-b55c-6c2d6df1c2bc | -9.89663 | -44.43024 | 2024-11-19 03:53:00 | NOAA-20 | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 7b4837f1-442c-358b-8d3a-b92cb82728cb | -4.10809 | -51.05292 | 2024-11-19 03:53:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 10.6 |
| b3606492-91fc-309a-bec4-f99db96a8ff8 | -1.93736 | -46.51635 | 2024-11-19 03:53:00 | NOAA-20 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| eea0bc14-f1e7-3b30-9337-8333a9fea405 | -9.98457 | -44.72073 | 2024-11-19 03:53:00 | NOAA-20 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| d6fafcb3-4e4f-38f2-948e-8b32cc0a70f1 | -5.2275 | -37.72958 | 2024-11-19 03:53:00 | NOAA-20 | BARAÚNA | RIO GRANDE DO NORTE | Brasil | 2401453 | 24 | 33 | nan | nan | nan | Caatinga | 2.0 |
| f5cfe045-24bf-3e5a-9928-6ccaa341a01d | -5.94981 | -39.67325 | 2024-11-19 03:53:00 | NOAA-20 | MOMBAÇA | CEARÁ | Brasil | 2308500 | 23 | 33 | nan | nan | nan | Caatinga | 0.7 |
| acb26e3c-735b-349b-ae4d-23a761f14812 | -3.03646 | -49.47443 | 2024-11-19 03:53:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 0d8c71d3-ac13-38ee-ab02-5aa0378f2796 | -4.98906 | -44.33309 | 2024-11-19 03:53:00 | NOAA-20 | DOM PEDRO | MARANHÃO | Brasil | 2103802 | 21 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 033ef69a-6107-31d4-9877-6aa602e64b8f | -6.6998 | -43.95014 | 2024-11-19 03:53:00 | NOAA-20 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| a8973fe9-4da0-3162-91a2-3fbe89856cd4 | -4.54674 | -48.02504 | 2024-11-19 03:53:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 33d1817d-a0ee-3138-a203-10449a5fcdef | -2.95209 | -51.46001 | 2024-11-19 03:53:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 531f85aa-b926-3881-a100-c5dc22858d91 | -6.93328 | -45.08327 | 2024-11-19 03:53:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 7dbc1aa3-76bf-3db6-bef9-5d3c98b6be01 | -5.53154 | -39.18026 | 2024-11-19 03:53:00 | NOAA-20 | MILHÃ | CEARÁ | Brasil | 2308351 | 23 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 34b94999-4e11-3a56-a646-d9290e30587a | -1.99629 | -45.35443 | 2024-11-19 03:53:00 | NOAA-20 | TURIAÇU | MARANHÃO | Brasil | 2112407 | 21 | 33 | nan | nan | nan | Amazônia | 7.4 |
| f647fda3-37d7-3e15-95dc-e15eb1da38ab | -4.99345 | -44.33387 | 2024-11-19 03:53:00 | NOAA-20 | DOM PEDRO | MARANHÃO | Brasil | 2103802 | 21 | 33 | nan | nan | nan | Cerrado | 7.5 |
| f97ce90a-c46d-30bd-a28a-1bc0e4693754 | -4.38577 | -47.77632 | 2024-11-19 03:53:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 7b09b156-1cd4-318a-b141-5118e2d23d45 | -5.39091 | -40.65962 | 2024-11-19 03:53:00 | NOAA-20 | CRATEÚS | CEARÁ | Brasil | 2304103 | 23 | 33 | nan | nan | nan | Caatinga | 4.5 |
| 35313803-a372-365c-b8bf-1d1c6efc8200 | -12.96142 | -42.44191 | 2024-11-19 03:53:00 | NOAA-20 | MACAÚBAS | BAHIA | Brasil | 2919801 | 29 | 33 | nan | nan | nan | Caatinga | 0.8 |
| ef018d94-db84-3931-85c1-46ec9a6758bd | -5.7163 | -44.81173 | 2024-11-19 03:53:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 7.4 |
| e6e00692-01ec-319e-b773-4ad00b7e398d | -3.88449 | -43.15423 | 2024-11-19 03:53:00 | NOAA-20 | BURITI | MARANHÃO | Brasil | 2102200 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| a7b0cce0-cf6a-3b58-a796-cf9a23d46b86 | -4.22431 | -46.53313 | 2024-11-19 03:53:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 845547f0-05e7-326b-bf87-8f5793a97ec8 | -7.39992 | -42.75852 | 2024-11-19 03:53:00 | NOAA-20 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 5.8 |
| e96b1f60-2548-3929-ac0f-40eeeb32ccea | -4.55576 | -48.00644 | 2024-11-19 03:53:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a9dafe67-45a0-33eb-9c20-1fdcb3171139 | -2.67415 | -46.23045 | 2024-11-19 03:53:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 498954af-d675-32d6-8748-e674c129a49d | -12.4045 | -44.91408 | 2024-11-19 03:53:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 1c330baf-afbf-3a89-b2fd-2b13dba4e5e9 | -4.22583 | -38.52294 | 2024-11-19 03:53:00 | NOAA-20 | PACAJUS | CEARÁ | Brasil | 2309607 | 23 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 9cc9143e-0daa-30ee-a273-cd3460d9da09 | -2.68402 | -46.23537 | 2024-11-19 03:53:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| a90099b0-8ce3-3131-9159-2740cf881f3a | -2.98496 | -45.33432 | 2024-11-19 03:53:00 | NOAA-20 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| c298b919-27a7-3577-b64e-6f211b5f1281 | -7.42998 | -42.55257 | 2024-11-19 03:53:00 | NOAA-20 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| c01abd12-3bf4-3cc4-979d-17cb063ecb1f | -3.32961 | -50.49915 | 2024-11-19 03:53:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 43296eb7-92d7-3a0f-8bea-0471162d24df | -3.5505 | -51.53485 | 2024-11-19 03:53:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 399e72bc-887f-3489-bffc-9440a12fd030 | -2.49257 | -49.03426 | 2024-11-19 03:53:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| c30fa0b9-a8eb-340e-84f8-6383c9fecda9 | -3.01683 | -41.13047 | 2024-11-19 03:53:00 | NOAA-20 | BARROQUINHA | CEARÁ | Brasil | 2302057 | 23 | 33 | nan | nan | nan | Caatinga | 1.1 |
| b869c204-34f8-329e-a7cd-98bf2a588e9f | -3.46901 | -48.25605 | 2024-11-19 03:53:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9bfcac3c-1474-3f56-9ba8-c7ce8a575351 | -5.97991 | -45.36816 | 2024-11-19 03:53:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 12.7 |
| 7006320a-3d74-3b9f-aa69-5ef39b9a3ccd | -8.50959 | -35.44449 | 2024-11-19 03:53:00 | NOAA-20 | RIBEIRÃO | PERNAMBUCO | Brasil | 2611804 | 26 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 27996839-fe01-3863-af66-cc5a1ee6fbcd | -4.1139 | -51.06021 | 2024-11-19 03:53:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 7bfeaba9-4e41-3057-9908-0eb2a860c014 | -4.11512 | -51.05332 | 2024-11-19 03:53:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e46b9142-0ea2-3a00-94ff-79f754246105 | -4.38512 | -47.78016 | 2024-11-19 03:53:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 3d1384c4-a85d-3891-88b1-4fbb3826ba30 | -9.68917 | -47.86957 | 2024-11-19 03:53:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 06b3e88a-8533-3bff-bcbe-d4cab8227cdd | -4.55173 | -48.03005 | 2024-11-19 03:53:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| febb3a29-105b-3e75-b633-b48b46993ad7 | -5.38804 | -40.65514 | 2024-11-19 03:53:00 | NOAA-20 | CRATEÚS | CEARÁ | Brasil | 2304103 | 23 | 33 | nan | nan | nan | Caatinga | 4.3 |
| 01a9c3bd-228b-3866-8b62-e24b4fa72283 | -7.46513 | -40.37581 | 2024-11-19 03:53:00 | NOAA-20 | ARARIPINA | PERNAMBUCO | Brasil | 2601102 | 26 | 33 | nan | nan | nan | Caatinga | 0.8 |


[Clique aqui para ver as próximas entradas](README19.md)
