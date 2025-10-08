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

## Dados Diários - Página 15

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 8fadc6ff-165e-39ac-a2b7-587ad5833a70 | -6.65487 | -41.98906 | 2025-10-08 03:47:00 | NOAA-21 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 6f6559d9-202f-3fa0-87e2-c0808fb8530a | -5.4895 | -44.61836 | 2025-10-08 03:47:00 | NOAA-21 | SANTA FILOMENA DO MARANHÃO | MARANHÃO | Brasil | 2109759 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| bfa0baca-1f5c-39f7-a5a5-9a21fea01a75 | -7.79482 | -42.61753 | 2025-10-08 03:47:00 | NOAA-21 | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 3.1 |
| 72353b38-f03a-3b64-b02b-c4f742b9fd8f | -7.82541 | -44.14313 | 2025-10-08 03:47:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 93016a4d-155f-3a3d-b4b4-a9e4454c709a | -7.2827 | -41.98055 | 2025-10-08 03:47:00 | NOAA-21 | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| f5acc14a-5937-3f13-89a9-42ea89f3164a | -7.34465 | -43.86737 | 2025-10-08 03:47:00 | NOAA-21 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 10c124a5-40c8-3f33-9f3c-df14091c534b | -7.32032 | -39.25429 | 2025-10-08 03:47:00 | NOAA-21 | BARBALHA | CEARÁ | Brasil | 2301901 | 23 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 9cfb538c-fe9d-3b2a-9dd0-139461fb8249 | -7.05429 | -37.69017 | 2025-10-08 03:47:00 | NOAA-21 | EMAS | PARAÍBA | Brasil | 2505907 | 25 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 3154061e-c365-3fcf-850f-6e20febe7ea0 | -4.94717 | -45.78663 | 2025-10-08 03:47:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 59dce428-5b00-396e-8911-02506c65cc68 | -7.02412 | -42.88169 | 2025-10-08 03:47:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 39.5 |
| ec09d491-0496-3272-9b04-0d240d19b3a3 | -7.69958 | -42.39 | 2025-10-08 03:47:00 | NOAA-21 | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 13de8a4f-5b51-3147-a13a-3b70124f54a4 | -7.35455 | -43.86407 | 2025-10-08 03:47:00 | NOAA-21 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 12.5 |
| ac8b983a-b223-3fbb-8087-6c6d1ea2e802 | -7.80387 | -44.21142 | 2025-10-08 03:47:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 508326f5-a552-3094-b5a0-ae7fa9c0d3f0 | -5.31583 | -44.99949 | 2025-10-08 03:47:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 6b045154-2ace-350c-90f6-0dae541f0d8f | -4.91559 | -45.08788 | 2025-10-08 03:47:00 | NOAA-21 | POÇÃO DE PEDRAS | MARANHÃO | Brasil | 2108900 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f93d2a30-ac0f-3b76-8293-e7c6860214e7 | -7.81434 | -44.17904 | 2025-10-08 03:47:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 5e9213e5-1606-3fa3-bb3f-038e8c35d8a4 | -5.36604 | -40.99756 | 2025-10-08 03:47:00 | NOAA-21 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 4.2 |
| ed12aff0-db18-30b9-9338-d64c7a7496c3 | -5.9978 | -39.30957 | 2025-10-08 03:47:00 | NOAA-21 | DEPUTADO IRAPUAN PINHEIRO | CEARÁ | Brasil | 2304269 | 23 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 57f87824-caef-3b0b-ae8e-b32998964802 | -7.80331 | -44.21759 | 2025-10-08 03:47:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 632626ed-0a94-3390-86d6-97b3e49a4c61 | -5.31636 | -44.99642 | 2025-10-08 03:47:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 4664bea6-c696-3578-a924-47608a019e6c | -7.43688 | -43.14256 | 2025-10-08 03:47:00 | NOAA-21 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 6.4 |
| 39f2779c-4c67-3e02-a51c-93217a5ae2ee | -7.0349 | -42.89594 | 2025-10-08 03:47:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 4.1 |
| 791ece85-176f-335d-8fc5-00e2063c8112 | -5.13666 | -44.96516 | 2025-10-08 03:47:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 13.4 |
| e2cb0a28-f826-3824-ad24-db1e6287c3e3 | -7.05761 | -37.69069 | 2025-10-08 03:47:00 | NOAA-21 | EMAS | PARAÍBA | Brasil | 2505907 | 25 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 14441322-78c2-36e2-a753-6e6f6e768a21 | -5.71426 | -44.65902 | 2025-10-08 03:47:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f5907cb4-a28d-3fd9-bb19-544a208a205a | -7.45142 | -43.14819 | 2025-10-08 03:47:00 | NOAA-21 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 17b6909c-43c5-3ead-99b8-13594fdc50a3 | -5.20509 | -37.62915 | 2025-10-08 03:47:00 | NOAA-21 | BARAÚNA | RIO GRANDE DO NORTE | Brasil | 2401453 | 24 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 315b52ad-53cb-3abe-9843-140f944fb41b | -7.78412 | -42.40875 | 2025-10-08 03:47:00 | NOAA-21 | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 3b0b8f3e-32d9-3d4c-a505-00c6bbd1551c | -7.77875 | -44.19481 | 2025-10-08 03:47:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 34b73ef5-8fb4-32db-bf97-a2b2c913351e | -7.76414 | -44.19707 | 2025-10-08 03:47:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 90f0631a-6f42-3c64-965d-b885e6f2f163 | -4.84916 | -45.76055 | 2025-10-08 03:47:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 13346544-b6e9-375f-8dfe-df637f8894cb | -7.01063 | -42.8837 | 2025-10-08 03:47:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 5.7 |
| 88e86aac-bb37-38e5-b270-31f5e19e2211 | -5.01468 | -44.08434 | 2025-10-08 03:47:00 | NOAA-21 | GONÇALVES DIAS | MARANHÃO | Brasil | 2104404 | 21 | 33 | nan | nan | nan | Cerrado | 7.0 |
| c7465aa6-e59b-342f-bd61-481a463e72dd | -4.76323 | -45.72988 | 2025-10-08 03:47:00 | NOAA-21 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2c6ef0dc-a992-37a2-a762-bac87401621b | -5.40951 | -46.22841 | 2025-10-08 03:47:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f55c963c-4dff-3b48-ae8b-3b614992d3b2 | -5.17458 | -45.13012 | 2025-10-08 03:47:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 39e5d5e4-7447-38d5-9543-81054ac582dd | -5.1377 | -44.95907 | 2025-10-08 03:47:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 29.1 |
| 209ea19e-1f22-3aea-88ea-6f9efe5c33c1 | -5.71512 | -45.68843 | 2025-10-08 03:47:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 957c5fa6-fcdb-321d-ac30-8c68ea9bef6a | -5.25619 | -44.14072 | 2025-10-08 03:47:00 | NOAA-21 | GOVERNADOR EUGÊNIO BARROS | MARANHÃO | Brasil | 2104602 | 21 | 33 | nan | nan | nan | Cerrado | 24.0 |
| 85d95357-eaa3-31e9-bb61-acdf32f26bb1 | -3.57438 | -49.44114 | 2025-10-08 03:47:00 | NOAA-21 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| dd979b48-77c0-3d37-8508-84198710bea0 | -4.47879 | -49.71525 | 2025-10-08 03:47:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 8.8 |
| b0867e9f-cc74-3732-8392-3353f90f9138 | -7.80976 | -44.17945 | 2025-10-08 03:47:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 0e27ee21-318c-33cb-b5a5-3def0ed24cdb | -7.00928 | -42.89174 | 2025-10-08 03:47:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 10.8 |
| c003b6fc-db76-301e-8fa6-780616c4cd4e | -3.21848 | -49.36334 | 2025-10-08 03:47:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| f9b3d740-c988-3401-92fb-4659f0f28ed1 | -7.72568 | -42.40937 | 2025-10-08 03:47:00 | NOAA-21 | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| d1faaa7d-8cc5-35d8-93d9-4ab802dcd039 | -5.59713 | -44.42766 | 2025-10-08 03:47:00 | NOAA-21 | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| bc8cb47f-f55a-3665-adc7-5ddc1849045f | -4.49536 | -46.36934 | 2025-10-08 03:47:00 | NOAA-21 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 56dfc3ef-a6e2-396e-a413-419eb159c942 | -7.8227 | -44.18535 | 2025-10-08 03:47:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 4.7 |
| e2feaa6e-59ca-3663-9254-e72ddfb9e808 | -5.7447 | -44.51031 | 2025-10-08 03:47:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 892b9dfd-e2b8-3b94-a6dc-ef1e02ed0f49 | -7.79171 | -44.19975 | 2025-10-08 03:47:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 9c0032a9-146e-3c9d-9782-9ac24d5c12e8 | -4.92077 | -45.08852 | 2025-10-08 03:47:00 | NOAA-21 | POÇÃO DE PEDRAS | MARANHÃO | Brasil | 2108900 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 38c58416-4c0e-320c-aff4-53c190c0e51b | -6.69554 | -42.19431 | 2025-10-08 03:47:00 | NOAA-21 | TANQUE DO PIAUÍ | PIAUÍ | Brasil | 2210979 | 22 | 33 | nan | nan | nan | Caatinga | 7.0 |
| c6065715-1806-3716-b277-a049dd0707f7 | -4.76263 | -45.73337 | 2025-10-08 03:47:00 | NOAA-21 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| abcf3dee-5158-33ed-8910-45bbe00a773d | -7.44137 | -43.12951 | 2025-10-08 03:47:00 | NOAA-21 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| 20d3786f-9e9a-32d3-9706-b5eba48f3246 | -7.7824 | -42.39636 | 2025-10-08 03:47:00 | NOAA-21 | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| f49fb364-a5cb-3f2f-b1be-482220b69ef5 | -4.62456 | -47.41363 | 2025-10-08 03:47:00 | NOAA-21 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 035f704c-cdba-3a1f-a533-b727599d934b | -7.78946 | -44.21534 | 2025-10-08 03:47:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 77572bab-2d2c-3ff5-beb7-bb037d16f10c | -4.68802 | -45.84288 | 2025-10-08 03:47:00 | NOAA-21 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 3eccdb5b-b6e4-38ba-b332-534f5e69e8d7 | -7.23746 | -45.33015 | 2025-10-08 03:47:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b7ed7c2d-ffb2-328e-a5cb-6e43f88b4653 | -7.44856 | -43.13915 | 2025-10-08 03:47:00 | NOAA-21 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 5.7 |
| d119d28f-b703-3a14-8217-2426eb63ee17 | -4.08104 | -48.0491 | 2025-10-08 03:47:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| f185b152-c66e-352f-92f0-60b83ccf24a4 | -7.78349 | -42.4124 | 2025-10-08 03:47:00 | NOAA-21 | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 25b29f39-a3ce-3d7b-836d-7bfb22e4ec2c | -7.79351 | -42.62526 | 2025-10-08 03:47:00 | NOAA-21 | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 61e3822a-679c-39e1-afb4-29355699f17d | -6.65454 | -41.98558 | 2025-10-08 03:47:00 | NOAA-21 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 4a557894-4d92-33bb-b81a-0f25fddb27e5 | -4.94753 | -45.59618 | 2025-10-08 03:47:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 125a76e3-741b-3f65-bfe7-8d75b7468274 | -6.75785 | -43.76448 | 2025-10-08 03:47:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 517ee855-253a-37fb-8465-fac4fbc6775c | -7.02278 | -42.88972 | 2025-10-08 03:47:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 48.5 |
| 95046f40-2732-33e3-87f8-e73fe2f55301 | -7.44638 | -43.15165 | 2025-10-08 03:47:00 | NOAA-21 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 4.2 |
| caff5633-9e4e-3923-a47d-d32e4cdc6f06 | -5.0092 | -44.08699 | 2025-10-08 03:47:00 | NOAA-21 | GONÇALVES DIAS | MARANHÃO | Brasil | 2104404 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| a6ca83bc-10f5-3933-b75f-35d4eb469d26 | -4.68738 | -45.84652 | 2025-10-08 03:47:00 | NOAA-21 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 7.1 |
| b3804b22-86f2-35a7-8bb8-1918eeb2abe5 | -7.29643 | -41.9721 | 2025-10-08 03:47:00 | NOAA-21 | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| da75a6bf-86e8-3de4-9061-5bae74cfb576 | -4.94848 | -45.59752 | 2025-10-08 03:47:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| a0bfb3fa-9439-3a38-882b-5b575eac6e5c | -4.69267 | -45.83625 | 2025-10-08 03:47:00 | NOAA-21 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 3ac1004d-8ad3-3788-a3bf-4c97fab78f7b | -4.49342 | -46.36665 | 2025-10-08 03:47:00 | NOAA-21 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 5b56314d-a03f-3b85-8a84-396f338a7a26 | -7.00055 | -42.86555 | 2025-10-08 03:47:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 9.2 |
| f0be92c8-18dd-374a-975b-aedc2d4e86a0 | -4.50235 | -46.3622 | 2025-10-08 03:47:00 | NOAA-21 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 18e77171-01f9-31a6-ac0b-7ca4758b8026 | -7.4392 | -43.14193 | 2025-10-08 03:47:00 | NOAA-21 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 4.0 |
| f358458a-4adc-335b-8236-d81c257f8b95 | -7.80678 | -44.2218 | 2025-10-08 03:47:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 31547199-63be-3a8a-a285-c834e6aee941 | -7.02474 | -42.79977 | 2025-10-08 03:47:00 | NOAA-21 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 5.0 |
| 42ed0f50-4149-3a7c-9e27-cb1982dc91b6 | -7.78865 | -44.22012 | 2025-10-08 03:47:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 6.0 |
| cda7e037-10cf-367b-bcbf-ef43760d9854 | -7.51766 | -42.71556 | 2025-10-08 03:47:00 | NOAA-21 | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| bd64d1b1-c3ab-37aa-9cf9-be7d81c62b02 | -4.69024 | -45.85072 | 2025-10-08 03:47:00 | NOAA-21 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 39502439-868b-3daf-9e17-193b8122ce88 | -5.71821 | -44.66551 | 2025-10-08 03:47:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 2f8a5e40-d5d7-35f1-8abc-462980be71f2 | -5.24067 | -46.57455 | 2025-10-08 03:47:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 4beaa02c-c472-3bc9-92da-136bd98cc487 | -0.90669 | -47.54951 | 2025-10-08 03:47:00 | NOAA-21 | MARACANÃ | PARÁ | Brasil | 1504307 | 15 | 33 | nan | nan | nan | Amazônia | 7.3 |
| 5c3b47f5-c0e5-38c3-a9f9-1c1d1092d3d9 | -7.79417 | -42.62136 | 2025-10-08 03:47:00 | NOAA-21 | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 3.1 |
| 25324dfb-147d-3e6e-9292-9af9a02263c9 | -7.78565 | -44.20991 | 2025-10-08 03:47:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 3.2 |
| a36169aa-55b5-38cc-9ed2-50a96b044710 | -7.46845 | -46.85353 | 2025-10-08 03:47:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| a4c48658-ef0d-3c06-8884-39fd5daa9d8f | -6.4204 | -47.24466 | 2025-10-08 03:47:00 | NOAA-21 | PORTO FRANCO | MARANHÃO | Brasil | 2109007 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| accd804b-0121-313e-8337-9f3e127f565d | -5.31079 | -44.99846 | 2025-10-08 03:47:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 0254ff42-013d-37d5-bd28-c7dfd16b0694 | -6.42114 | -47.24056 | 2025-10-08 03:47:00 | NOAA-21 | PORTO FRANCO | MARANHÃO | Brasil | 2109007 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 5035b8a9-265f-3976-bb97-bf5fa58fedc3 | -6.99919 | -42.87354 | 2025-10-08 03:47:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 11.6 |
| 997e5939-031a-3289-9a4f-a75e3e92a93b | -5.1321 | -44.96133 | 2025-10-08 03:47:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 13.4 |
| 81eb6721-a594-33b3-b2ef-0717df474b6a | -8.04059 | -35.241 | 2025-10-08 03:47:00 | NOAA-21 | CHÃ DE ALEGRIA | PERNAMBUCO | Brasil | 2604403 | 26 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| d8cb9261-c7cf-30b8-825c-6f9ddbda7727 | -7.00501 | -42.89107 | 2025-10-08 03:47:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 9.8 |
| 1fc1bafe-c643-3b2f-95aa-e2fc4c712bc1 | -7.44928 | -43.135 | 2025-10-08 03:47:00 | NOAA-21 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 5.7 |
| d04120d1-bd9a-3c07-9573-bc9e5c809d31 | -5.00989 | -44.08362 | 2025-10-08 03:47:00 | NOAA-21 | GONÇALVES DIAS | MARANHÃO | Brasil | 2104404 | 21 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 18a62919-c7db-3862-90bf-0a27f4853e34 | -5.73996 | -45.26202 | 2025-10-08 03:47:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 15066f9c-9152-3428-b188-1441cb95dbb8 | -7.79122 | -44.22914 | 2025-10-08 03:47:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 495df7e8-1213-3e27-ab80-7d9f61030bc4 | -7.02345 | -42.8857 | 2025-10-08 03:47:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 39.5 |


[Clique aqui para ver as próximas entradas](README16.md)
