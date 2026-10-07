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

## Dados Diários - Página 33

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 2d96913a-a0b0-35f7-a010-37e1f436af7e | -11.62801 | -43.67056 | 2026-10-07 03:25:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| f0215407-5ff4-3f5c-ae08-870093283c54 | -14.7856 | -42.26928 | 2026-10-07 03:25:00 | NOAA-21 | JACARACI | BAHIA | Brasil | 2917409 | 29 | 33 | nan | nan | nan | Caatinga | 4.3 |
| 11a862c2-0cf5-3d16-8735-437a09a97289 | -15.41962 | -43.70429 | 2026-10-07 03:25:00 | NOAA-21 | VERDELÂNDIA | MINAS GERAIS | Brasil | 3171030 | 31 | 33 | nan | nan | nan | Caatinga | 16.0 |
| b09c9b73-d2fa-3dee-9ad0-eb4c1d181c74 | -12.19042 | -44.71759 | 2026-10-07 03:25:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 69cc3ac5-16e4-3dca-96a2-542a22bc1b04 | -16.04339 | -39.84505 | 2026-10-07 03:25:00 | NOAA-21 | ITAGIMIRIM | BAHIA | Brasil | 2915304 | 29 | 33 | nan | nan | nan | Mata Atlântica | 7.8 |
| 557fabd6-d971-3944-ad1b-439c714772a0 | -12.17495 | -44.72626 | 2026-10-07 03:25:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 4.6 |
| d3840268-73bd-3686-a523-424aa7e4eaae | -10.98188 | -45.4128 | 2026-10-07 03:25:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| e13a39a9-122c-3aee-8fa7-200271d9a00f | -10.98279 | -45.41294 | 2026-10-07 03:25:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 4.6 |
| d444c61b-d467-3a7e-9628-ef70286d6b2b | -15.16222 | -41.29492 | 2026-10-07 03:25:00 | NOAA-21 | CÂNDIDO SALES | BAHIA | Brasil | 2906709 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 71a663ab-b424-3905-8c3b-904eef0d828b | -12.41415 | -40.92538 | 2026-10-07 03:25:00 | NOAA-21 | LAJEDINHO | BAHIA | Brasil | 2919009 | 29 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 6c90f0ce-bf84-35a6-a484-ae9688324d68 | -11.67483 | -43.62114 | 2026-10-07 03:25:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 9.1 |
| 0771e3a7-27bc-3349-95c3-a27a06189e1f | -11.10735 | -45.7108 | 2026-10-07 03:25:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.3 |
| d9e8b6b9-1ee9-37e2-b726-94245cddc036 | -9.82092 | -44.78799 | 2026-10-07 03:25:00 | NOAA-21 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| d3de2029-c15a-34d6-9bf9-1e78d67edd1e | -12.41476 | -40.92214 | 2026-10-07 03:25:00 | NOAA-21 | LAJEDINHO | BAHIA | Brasil | 2919009 | 29 | 33 | nan | nan | nan | Caatinga | 0.7 |
| a3abe82b-2d89-3dd0-bf6d-4024322fb61a | -10.98828 | -45.42151 | 2026-10-07 03:25:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 4.1 |
| c03467a6-1899-3bda-b625-01095f53d6dc | -12.19116 | -44.71939 | 2026-10-07 03:25:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 5.1 |
| a95838ce-64f0-30f7-a608-f594a1dbe383 | -12.1823 | -44.72943 | 2026-10-07 03:25:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 8f1f843f-9d0e-31be-90d1-910f3baee0fa | -15.16152 | -41.29451 | 2026-10-07 03:25:00 | NOAA-21 | BELO CAMPO | BAHIA | Brasil | 2903508 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 9e5064a9-f8b8-37a4-aea1-f11dfe64de76 | -11.70146 | -40.11166 | 2026-10-07 03:25:00 | NOAA-21 | MAIRI | BAHIA | Brasil | 2920106 | 29 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 4d226a0c-dd22-3226-a053-1fd372142861 | -15.7296 | -43.92673 | 2026-10-07 03:25:00 | NOAA-21 | VARZELÂNDIA | MINAS GERAIS | Brasil | 3170909 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 93c1cc2c-fedd-319a-b2e1-607b8394392b | -15.41841 | -43.70685 | 2026-10-07 03:25:00 | NOAA-21 | VERDELÂNDIA | MINAS GERAIS | Brasil | 3171030 | 31 | 33 | nan | nan | nan | Caatinga | 26.0 |
| 593a9b0b-9ce6-3bf1-aaac-59b01622c090 | -15.42543 | -43.70556 | 2026-10-07 03:25:00 | NOAA-21 | VERDELÂNDIA | MINAS GERAIS | Brasil | 3171030 | 31 | 33 | nan | nan | nan | Caatinga | 16.0 |
| 259c63af-fe64-3608-a649-720b91c667c7 | -13.63792 | -44.42369 | 2026-10-07 03:25:00 | NOAA-21 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 8.4 |
| d26aac56-0b7d-34c3-9e51-a68e6039b829 | -14.78352 | -42.89966 | 2026-10-07 03:25:00 | NOAA-21 | ESPINOSA | MINAS GERAIS | Brasil | 3124302 | 31 | 33 | nan | nan | nan | Caatinga | 10.7 |
| ee64d0c1-4fc2-3481-974a-fcb154140c3b | -15.51836 | -39.23046 | 2026-10-07 03:25:00 | NOAA-21 | SANTA LUZIA | BAHIA | Brasil | 2928059 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 3eb3cec0-088b-33af-b8fa-fedc01df1032 | -12.19276 | -44.70647 | 2026-10-07 03:25:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| ce1ba03a-16d3-3720-a182-2ed8be284527 | -10.99867 | -45.43631 | 2026-10-07 03:25:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 4.4 |
| fec79963-9ce9-39e8-839c-787854a574e9 | -15.32166 | -43.09415 | 2026-10-07 03:25:00 | NOAA-21 | CATUTI | MINAS GERAIS | Brasil | 3115474 | 31 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 1307e2f2-0f08-3481-aba0-d0b21123583c | -15.88052 | -43.6031 | 2026-10-07 03:25:00 | NOAA-21 | CAPITÃO ENÉAS | MINAS GERAIS | Brasil | 3112703 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 0819d202-956e-3c4c-9874-b6209edd57f6 | -12.46152 | -38.35078 | 2026-10-07 03:25:00 | NOAA-21 | MATA DE SÃO JOÃO | BAHIA | Brasil | 2921005 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 8abc4c78-03cd-322a-b96f-926fd0b175d9 | -11.11202 | -45.71141 | 2026-10-07 03:25:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.7 |
| b3bf6946-50c6-357d-9449-1f3316e7a136 | -11.73959 | -43.65098 | 2026-10-07 03:25:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 5.0 |
| d2533121-080f-3611-9265-5a36b6da1cb2 | -16.03977 | -39.83955 | 2026-10-07 03:25:00 | NOAA-21 | ITAGIMIRIM | BAHIA | Brasil | 2915304 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 4537609f-bb60-3445-8ba0-8686fdd36924 | -13.63324 | -43.68969 | 2026-10-07 03:25:00 | NOAA-21 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| a1d2b3e5-6a03-35a8-9a6a-8debe473c144 | -11.11154 | -45.72603 | 2026-10-07 03:25:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 1e14cb7b-e319-3056-9835-24a2b468f741 | -16.04253 | -39.84957 | 2026-10-07 03:25:00 | NOAA-21 | ITAGIMIRIM | BAHIA | Brasil | 2915304 | 29 | 33 | nan | nan | nan | Mata Atlântica | 4.9 |
| 6487a425-d87b-3aa0-9de2-724a11f577cb | -11.73341 | -43.64972 | 2026-10-07 03:25:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 11.3 |
| 774ef3b3-d57a-3746-9c6c-e8f961cf8ca0 | -12.19694 | -44.71899 | 2026-10-07 03:25:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| f798e94a-ae19-3ac4-9d2c-322d78261e7e | -10.98734 | -45.4213 | 2026-10-07 03:25:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 99545121-45de-3375-a641-b2fc073ee950 | -9.80717 | -44.78577 | 2026-10-07 03:25:00 | NOAA-21 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| d989b972-3540-39b5-a2ce-ddf0f5d0440b | -15.23791 | -43.27248 | 2026-10-07 03:25:00 | NOAA-21 | PAI PEDRO | MINAS GERAIS | Brasil | 3146552 | 31 | 33 | nan | nan | nan | Caatinga | 20.1 |
| bc3c8627-14c4-3dcb-95f6-f3e00e46a0e6 | -11.73862 | -43.65587 | 2026-10-07 03:25:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 53b438bb-38a7-3adb-9db6-8ea70e1b3574 | -11.63914 | -43.66958 | 2026-10-07 03:25:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 880510c6-a80b-3657-9e41-efa2027b37f6 | -11.78699 | -43.53827 | 2026-10-07 03:25:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 07c0b509-f6c2-3fb4-a992-7987fb769478 | -11.11005 | -45.73331 | 2026-10-07 03:25:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 94e2af18-1438-343d-8c51-1099206ffaad | -12.95415 | -42.43135 | 2026-10-07 03:25:00 | NOAA-21 | IBIPITANGA | BAHIA | Brasil | 2912509 | 29 | 33 | nan | nan | nan | Caatinga | 2.3 |
| d8916e2a-8371-3e66-8dc3-dcf5c696220b | -11.0097 | -45.45289 | 2026-10-07 03:25:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 14435197-01a8-366d-b446-e5c99726b981 | -10.99467 | -45.42081 | 2026-10-07 03:25:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 127961f3-ba9b-38b9-8783-0d6a3bec3e3c | -9.81403 | -44.78697 | 2026-10-07 03:25:00 | NOAA-21 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| c42c7ce1-2a4d-3751-8a3d-b024b47943e2 | -14.25082 | -41.62785 | 2026-10-07 03:25:00 | NOAA-21 | BRUMADO | BAHIA | Brasil | 2904605 | 29 | 33 | nan | nan | nan | Caatinga | 18.7 |
| f3be03d8-72f7-3b5e-ac2a-ceb57e5d0761 | -11.72624 | -43.65339 | 2026-10-07 03:25:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 11.3 |
| 230f9e46-6af9-3ead-9d86-390598127bb6 | -13.39139 | -43.87329 | 2026-10-07 03:25:00 | NOAA-21 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 2a9b3f86-74d8-35cb-ab58-b7859d396cde | -18.18455 | -42.33974 | 2026-10-07 03:28:00 | NOAA-21 | SANTA MARIA DO SUAÇUÍ | MINAS GERAIS | Brasil | 3158201 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.5 |
| 00d6f93e-3489-321e-b099-23c76485ac3b | -17.43104 | -43.64826 | 2026-10-07 03:28:00 | NOAA-21 | OLHOS-D'ÁGUA | MINAS GERAIS | Brasil | 3145455 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 03bef0c5-dc37-355e-b60a-2604583fe7e6 | -17.43756 | -43.64504 | 2026-10-07 03:28:00 | NOAA-21 | OLHOS-D'ÁGUA | MINAS GERAIS | Brasil | 3145455 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ce6df9cd-debb-3767-853e-9c43f84c4ba0 | -18.18324 | -42.34618 | 2026-10-07 03:28:00 | NOAA-21 | SANTA MARIA DO SUAÇUÍ | MINAS GERAIS | Brasil | 3158201 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.0 |
| 70f6af7a-d2a2-3f6b-9855-271c703f0825 | -17.73579 | -42.37613 | 2026-10-07 03:28:00 | NOAA-21 | CAPELINHA | MINAS GERAIS | Brasil | 3112307 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| bce9fbc1-c899-3005-8ff0-909741fbd0b3 | -18.52857 | -41.92076 | 2026-10-07 03:28:00 | NOAA-21 | FREI INOCÊNCIO | MINAS GERAIS | Brasil | 3126901 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.8 |
| cb152964-a612-3735-ac7d-4b1c1c07b980 | -17.87753 | -45.99007 | 2026-10-07 03:28:00 | NOAA-21 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 3.8 |
| cadcd46b-e31d-34c3-8843-5b999429045d | -17.87945 | -45.98961 | 2026-10-07 03:28:00 | NOAA-21 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 40a6e4b6-10a4-3825-a3bd-b002179a9f89 | -17.87822 | -45.99499 | 2026-10-07 03:28:00 | NOAA-21 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 3.3 |
| a9d64097-4569-37b5-998e-cf1c187ce737 | -18.20291 | -42.32745 | 2026-10-07 03:28:00 | NOAA-21 | SANTA MARIA DO SUAÇUÍ | MINAS GERAIS | Brasil | 3158201 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 7dbb6471-d12c-3267-988b-35661f624948 | -18.2036 | -42.32407 | 2026-10-07 03:28:00 | NOAA-21 | SANTA MARIA DO SUAÇUÍ | MINAS GERAIS | Brasil | 3158201 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 3c014af6-71bb-3e29-8e73-fda71f277f8d | -17.43267 | -43.64059 | 2026-10-07 03:28:00 | NOAA-21 | OLHOS-D'ÁGUA | MINAS GERAIS | Brasil | 3145455 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 49e7532e-b420-3fb6-b2dd-5d508e2fd5aa | -17.43839 | -43.64119 | 2026-10-07 03:28:00 | NOAA-21 | OLHOS-D'ÁGUA | MINAS GERAIS | Brasil | 3145455 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 0298045f-2c58-34cd-b5ea-124556934122 | -17.43918 | -43.63743 | 2026-10-07 03:28:00 | NOAA-21 | OLHOS-D'ÁGUA | MINAS GERAIS | Brasil | 3145455 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 393fe6a6-ab3a-3b5a-a2a2-c682c71046bc | -18.18389 | -42.34299 | 2026-10-07 03:28:00 | NOAA-21 | SANTA MARIA DO SUAÇUÍ | MINAS GERAIS | Brasil | 3158201 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.5 |
| c09af6ac-823b-3191-8a5d-ef15ad1f4989 | -17.87632 | -45.99547 | 2026-10-07 03:28:00 | NOAA-21 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 92baed2d-38e9-307d-a243-2ea188c9a7fd | -17.43995 | -43.63386 | 2026-10-07 03:28:00 | NOAA-21 | OLHOS-D'ÁGUA | MINAS GERAIS | Brasil | 3145455 | 31 | 33 | nan | nan | nan | Cerrado | 3.3 |
| f77d0e03-e60c-3b76-bc1b-611cc5096f90 | -18.52978 | -41.92262 | 2026-10-07 03:28:00 | NOAA-21 | FREI INOCÊNCIO | MINAS GERAIS | Brasil | 3126901 | 31 | 33 | nan | nan | nan | Mata Atlântica | 8.3 |
| 96970c95-7b2d-384b-8a83-47a251f4311e | -17.43349 | -43.6368 | 2026-10-07 03:28:00 | NOAA-21 | OLHOS-D'ÁGUA | MINAS GERAIS | Brasil | 3145455 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 101b5c79-4499-339f-9ed9-e4a902796714 | -18.53346 | -41.92186 | 2026-10-07 03:28:00 | NOAA-21 | FREI INOCÊNCIO | MINAS GERAIS | Brasil | 3126901 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.1 |
| a57298d1-d9c8-3bf9-a72f-f8b8f6ad83ef | -17.43187 | -43.64438 | 2026-10-07 03:28:00 | NOAA-21 | OLHOS-D'ÁGUA | MINAS GERAIS | Brasil | 3145455 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 6133f8e1-bbd8-33e6-8546-c66f71345822 | -18.53097 | -41.91684 | 2026-10-07 03:28:00 | NOAA-21 | FREI INOCÊNCIO | MINAS GERAIS | Brasil | 3126901 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.1 |
| f5ffcef7-fd77-3d1e-a50d-4b3a9280a711 | -17.43428 | -43.63308 | 2026-10-07 03:28:00 | NOAA-21 | OLHOS-D'ÁGUA | MINAS GERAIS | Brasil | 3145455 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 9fdd088e-11ba-3591-912c-41411de426cf | -5.7376 | -45.1533 | 2026-10-07 03:30:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 55.8 |
| b5c7167e-64f8-39ee-92e0-4bc54598d3da | -3.8567 | -55.9769 | 2026-10-07 03:30:00 | GOES-19 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 75.7 |
| 67b5b15d-afd9-32eb-bb54-8593615e6d9c | -3.4762 | -50.0883 | 2026-10-07 03:30:00 | GOES-19 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 48.5 |
| 2c5cdc53-0708-3026-83ca-e645c1f5298d | -9.1517 | -65.9554 | 2026-10-07 03:30:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 54.9 |
| a80de3d6-4756-3206-b72d-cc8fb9886947 | -3.5127 | -54.6562 | 2026-10-07 03:30:00 | GOES-19 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 84.4 |
| 8b59cee4-e82e-389d-8943-45a7d1ab6324 | -3.0731 | -54.2473 | 2026-10-07 03:30:00 | GOES-19 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 54.0 |
| 0132ff4e-2c96-3c22-918b-494b14809404 | -5.7189 | -45.1547 | 2026-10-07 03:30:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 57.6 |
| 8aef3b99-8fbf-351d-9aa8-25b6d6a9701d | -3.0914 | -54.2669 | 2026-10-07 03:30:00 | GOES-19 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 54.4 |
| ce20ae3d-0f95-3247-90a0-d5e809854739 | -2.7796 | -54.1138 | 2026-10-07 03:30:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 170.3 |
| 167bdc73-4de8-37b9-b7d8-0d76e1a0cb78 | -3.0913 | -54.287 | 2026-10-07 03:30:00 | GOES-19 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 103.7 |
| 68d01434-a00c-31c3-bc60-02fcedf98d0a | -2.9448 | -54.1501 | 2026-10-07 03:30:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 63.8 |
| 1710120c-c3f0-309a-a115-2e326085a690 | -8.7036 | -45.2061 | 2026-10-07 03:30:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 155.2 |
| da20080e-cd93-3b58-98b8-3fefcd81787b | -5.7187 | -45.1773 | 2026-10-07 03:30:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 58.6 |
| 1e8a8f4c-e822-317a-aba1-baa508fbe8d9 | -2.7612 | -54.1142 | 2026-10-07 03:30:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 218.2 |
| c7c320e7-2edd-3470-9f9a-e3bbbae03090 | -3.0 | -54.1287 | 2026-10-07 03:30:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 80.6 |
| 89907b65-2365-3faa-8de9-d75151233ad1 | -3.1114 | -53.7839 | 2026-10-07 03:30:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 70.3 |
| 0a942d70-1e5c-343b-8bd6-122f3b861486 | -3.5311 | -54.6357 | 2026-10-07 03:30:00 | GOES-19 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 55.5 |
| 88bdd739-58f5-33c0-9330-f99feb3b313e | -3.073 | -54.2674 | 2026-10-07 03:30:00 | GOES-19 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 64.5 |
| 56c00062-2e16-3859-a1e7-54f18af87e25 | -3.0375 | -53.9066 | 2026-10-07 03:30:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 50.9 |
| d26e6d6c-9373-36fd-8701-6f9605a52528 | -3.0913 | -54.307 | 2026-10-07 03:30:00 | GOES-19 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 56.0 |
| ce25338e-65b1-321f-b036-c40c875c4b0f | -8.7228 | -45.1812 | 2026-10-07 03:30:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 56.5 |
| ff7d6ebb-d43e-33c3-8d51-b3004eae0b83 | -3.5126 | -54.6762 | 2026-10-07 03:30:00 | GOES-19 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 56.4 |
| 7b927f0c-abf6-3356-968b-92c97104749b | -3.531 | -54.6557 | 2026-10-07 03:30:00 | GOES-19 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 92.9 |
| d579ddab-3617-33a6-9238-b05467489547 | -2.7613 | -54.0941 | 2026-10-07 03:30:00 | GOES-19 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 250.0 |
| 48897afc-19a3-32a0-9866-f39a4a77b9c2 | -2.7613 | -54.074 | 2026-10-07 03:30:00 | GOES-19 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 78.5 |


[Clique aqui para ver as próximas entradas](README34.md)
