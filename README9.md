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

## Dados Diários - Página 9

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 448dec27-3b51-3714-8788-22e64b734420 | -2.9108 | -48.254 | 2025-07-19 03:50:00 | GOES-19 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 84.9 |
| 6324ce20-a98b-3989-99c6-17579ae1de41 | -3.1384 | -47.0068 | 2025-07-19 03:50:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 48.7 |
| 9043cebf-b14d-3658-b5b8-cda16a0fcd39 | -2.9109 | -48.2325 | 2025-07-19 03:50:00 | GOES-19 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 62.3 |
| 3c3132f4-846c-382d-9261-dd35e11b1744 | -11.7317 | -48.1849 | 2025-07-19 03:50:00 | GOES-19 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 149.4 |
| 6f29ae50-54f6-3737-98f4-5d286a2925b0 | -11.7313 | -48.207 | 2025-07-19 03:50:00 | GOES-19 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 53.7 |
| 7e1fe189-ecb7-3191-95b3-38d23bd9342b | -15.8955 | -43.4523 | 2025-07-19 03:50:00 | GOES-19 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 85.3 |
| 36ee414c-766d-36bc-b458-7de1d725685c | -5.6567 | -43.7161 | 2025-07-19 04:00:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 55.3 |
| b98edf95-5f50-3ddf-a2cf-59e00a56b516 | -5.6379 | -43.7175 | 2025-07-19 04:00:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 40.5 |
| b8ff8707-9bc1-377a-a6d3-6a76bb8d499e | -2.9109 | -48.2325 | 2025-07-19 04:00:00 | GOES-19 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 54.5 |
| 34996575-2e76-30b5-9621-6456f79c7aa6 | -15.8955 | -43.4523 | 2025-07-19 04:00:00 | GOES-19 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 61.7 |
| c35f00e7-70ef-36e3-8ee3-5009e885926f | -11.7313 | -48.207 | 2025-07-19 04:00:00 | GOES-19 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 52.8 |
| d00d4b35-3e72-359e-9f96-f810bc3cc62c | -6.1606 | -48.0507 | 2025-07-19 04:00:00 | GOES-19 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 51.2 |
| 8ab959b6-0230-3941-97d1-d432b9db98aa | -2.9108 | -48.254 | 2025-07-19 04:00:00 | GOES-19 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 57.0 |
| 70ba7816-6502-35be-8d69-63ca9611d862 | -11.7317 | -48.1849 | 2025-07-19 04:00:00 | GOES-19 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 113.8 |
| 536cd50f-68ae-33d6-a967-af86e3c3140d | -2.72134 | -47.69608 | 2025-07-19 04:06:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 24fe88d0-2dde-3658-8ac5-f4523f165791 | -3.16369 | -41.83681 | 2025-07-19 04:06:00 | NOAA-21 | BURITI DOS LOPES | PIAUÍ | Brasil | 2202000 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| d4911424-3e09-3b44-9f8b-81524bc21ce3 | -2.44154 | -47.3266 | 2025-07-19 04:06:00 | NOAA-21 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 43817644-3537-37db-b165-fe239e10ddbc | -2.81064 | -42.30968 | 2025-07-19 04:06:00 | NOAA-21 | TUTÓIA | MARANHÃO | Brasil | 2112506 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| bab3edea-2bb0-36b7-abed-fba0ab157d1c | -3.29517 | -42.53615 | 2025-07-19 04:06:00 | NOAA-21 | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| cc18da21-688f-3a30-ae21-c0a2af7ab8f7 | -2.44976 | -47.33241 | 2025-07-19 04:06:00 | NOAA-21 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 95e1b63b-790f-3448-b9b9-461a62476a7d | -3.38852 | -43.36764 | 2025-07-19 04:06:00 | NOAA-21 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 9accd820-9544-36e7-bc52-8abaf6d45e46 | -3.06607 | -40.04694 | 2025-07-19 04:06:00 | NOAA-21 | ACARAÚ | CEARÁ | Brasil | 2300200 | 23 | 33 | nan | nan | nan | Caatinga | 0.4 |
| a09cea89-791d-3fd3-a0f6-06f43c1581f5 | -3.06274 | -40.04643 | 2025-07-19 04:06:00 | NOAA-21 | ACARAÚ | CEARÁ | Brasil | 2300200 | 23 | 33 | nan | nan | nan | Caatinga | 5.4 |
| a877777c-d97f-3384-ad5a-003076ad6a7c | -2.446 | -47.32728 | 2025-07-19 04:06:00 | NOAA-21 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 912f8fd0-f83e-352b-a3d5-d6e69f23a960 | -3.40304 | -43.36595 | 2025-07-19 04:06:00 | NOAA-21 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b0d24384-bb35-32ea-9049-ef9397c93586 | -2.44083 | -47.33102 | 2025-07-19 04:06:00 | NOAA-21 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e681ee38-be06-30fe-a0f7-5ae977075aee | -3.06328 | -40.04294 | 2025-07-19 04:06:00 | NOAA-21 | ACARAÚ | CEARÁ | Brasil | 2300200 | 23 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 0a2aa0be-d529-3ec7-8678-890332db9672 | -3.29179 | -42.53562 | 2025-07-19 04:06:00 | NOAA-21 | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| aee4cb81-c201-3d4d-a1e2-a0823518bb49 | -2.4453 | -47.3317 | 2025-07-19 04:06:00 | NOAA-21 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d39d9e47-aae6-3bef-a520-de0c9b909ce3 | -5.27927 | -45.12834 | 2025-07-19 04:08:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 1e6afa0c-8e7f-37ff-828e-5ceefdee2208 | -10.63674 | -44.76532 | 2025-07-19 04:08:00 | NOAA-21 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 9.4 |
| da800204-bfc5-3de0-9ee6-b871e94f3af4 | -6.16432 | -48.05547 | 2025-07-19 04:08:00 | NOAA-21 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 19.9 |
| 484c2944-2a97-30d5-b37b-d315b86f38df | -5.10849 | -43.15079 | 2025-07-19 04:08:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 5f08d486-ca51-324e-9607-9bc56e6d6f61 | -7.4702 | -44.70158 | 2025-07-19 04:08:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 8097c7a3-3cc7-3ff9-b27e-3bbc91093a0e | -8.4265 | -46.88203 | 2025-07-19 04:08:00 | NOAA-21 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 83aa01df-516a-3c73-afc2-9bef03a5caa3 | -4.6691 | -41.95648 | 2025-07-19 04:08:00 | NOAA-21 | COCAL DE TELHA | PIAUÍ | Brasil | 2202711 | 22 | 33 | nan | nan | nan | Caatinga | 3.1 |
| b208c7c2-c52e-30f1-ae59-924294c4cf2b | -6.75408 | -45.51712 | 2025-07-19 04:08:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 3321d582-793a-34ac-aae9-d8d81c6d0fbb | -10.01977 | -47.69325 | 2025-07-19 04:08:00 | NOAA-21 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 3836c3f7-90fb-3d03-b548-ffc7525362c7 | -4.25233 | -48.54567 | 2025-07-19 04:08:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| bbed8457-6de7-3df3-b831-8eac4739030b | -10.62236 | -44.76686 | 2025-07-19 04:08:00 | NOAA-21 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 11.0 |
| f4003b5d-abe0-3441-9f5b-59f15dbe7c90 | -7.08951 | -49.17527 | 2025-07-19 04:08:00 | NOAA-21 | SANTA FÉ DO ARAGUAIA | TOCANTINS | Brasil | 1718865 | 17 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e12bc52a-fd7e-34e3-9677-52ce5a248e29 | -6.41584 | -43.56 | 2025-07-19 04:08:00 | NOAA-21 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 521eed91-f5df-36ff-ae0f-64783e02a83e | -6.33006 | -43.74466 | 2025-07-19 04:08:00 | NOAA-21 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 0578903e-47b4-3b68-995c-1a8720d98331 | -9.76939 | -48.74761 | 2025-07-19 04:08:00 | NOAA-21 | BARROLÂNDIA | TOCANTINS | Brasil | 1703107 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 43919c04-ad72-3df1-aa94-8cd50728301d | -8.30466 | -55.10745 | 2025-07-19 04:08:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 794c9733-76f4-3f29-abf1-afd0e0444b8b | -10.09085 | -47.24047 | 2025-07-19 04:08:00 | NOAA-21 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 5.2 |
| de3e353e-b645-3238-9fdd-25cbff2ea208 | -11.41187 | -42.07203 | 2025-07-19 04:08:00 | NOAA-21 | UIBAÍ | BAHIA | Brasil | 2932408 | 29 | 33 | nan | nan | nan | Caatinga | 1.6 |
| ad778d4a-553a-390d-861a-8fc7c2f6a4b4 | -6.19242 | -44.09836 | 2025-07-19 04:08:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| a0d4a492-35fd-32e9-b78f-763269c08e5b | -8.38386 | -44.03535 | 2025-07-19 04:08:00 | NOAA-21 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d7410583-79d8-3c94-8150-9ad23fc224fb | -9.80723 | -48.55669 | 2025-07-19 04:08:00 | NOAA-21 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 9.2 |
| d1d8715d-d877-3285-a60c-0ffaa4864e9e | -9.51721 | -45.42915 | 2025-07-19 04:08:00 | NOAA-21 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| a3459a90-d7fd-3bb5-94ca-00e108dbd8a8 | -7.62938 | -44.29616 | 2025-07-19 04:08:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e486563e-c1ea-3c6d-90ac-3caddbdf3e5b | -8.39189 | -44.029 | 2025-07-19 04:08:00 | NOAA-21 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 44ac9dde-8431-3429-8941-8f030ae84677 | -9.81215 | -47.7312 | 2025-07-19 04:08:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 00d7a561-df3d-3fd2-baf7-606197d295a6 | -9.81497 | -47.73909 | 2025-07-19 04:08:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 19.5 |
| 11f5f80a-d514-39a3-8812-403f7902be26 | -9.9261 | -46.29792 | 2025-07-19 04:08:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 8ced39db-c744-3443-906b-8a7d47e84e1a | -8.26071 | -46.06946 | 2025-07-19 04:08:00 | NOAA-21 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 54107923-1d64-33b7-940a-e8bfbe257f6f | -10.63136 | -45.23434 | 2025-07-19 04:08:00 | NOAA-21 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| e335be03-9349-3895-b0c1-9ba8b1da192c | -8.54699 | -47.84665 | 2025-07-19 04:08:00 | NOAA-21 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 13c31f93-690c-3c78-b74d-d5d93bb74d4b | -9.80579 | -48.56491 | 2025-07-19 04:08:00 | NOAA-21 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 9.5 |
| 3ccfbeb7-8a98-3910-8029-974667764259 | -9.43522 | -48.84663 | 2025-07-19 04:08:00 | NOAA-21 | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| c658edf8-4352-3c18-96af-3635099a620e | -7.42425 | -44.85183 | 2025-07-19 04:08:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| de6395aa-b6dc-3b71-8c16-7bc0187c0154 | -6.68913 | -43.03706 | 2025-07-19 04:08:00 | NOAA-21 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 37ab2f67-29fc-3edd-bdce-b3450f02fa5a | -4.03062 | -48.06818 | 2025-07-19 04:08:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 9368b77b-1611-3ca1-9664-0fe3178c9d06 | -5.75055 | -46.19093 | 2025-07-19 04:08:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 2ab75b8f-ec24-35b8-986c-f84b965bee06 | -3.03919 | -49.42907 | 2025-07-19 04:08:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 3cdf3513-aa23-329a-b939-a63c935df30d | -8.53863 | -47.84519 | 2025-07-19 04:08:00 | NOAA-21 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| a007eb29-0885-3b89-a3e7-15afb6233675 | -4.67187 | -41.96046 | 2025-07-19 04:08:00 | NOAA-21 | COCAL DE TELHA | PIAUÍ | Brasil | 2202711 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 1a36790d-c023-3cdb-998c-865b98f96cad | -10.63535 | -45.23819 | 2025-07-19 04:08:00 | NOAA-21 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| ce6966db-920f-3477-b87b-4178b22856f0 | -2.91464 | -48.24422 | 2025-07-19 04:08:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 12.0 |
| 360ede2f-ddf9-38b6-8ca3-af479a4d28eb | -10.2303 | -48.24808 | 2025-07-19 04:08:00 | NOAA-21 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 522f260c-a112-324a-b15e-441c7498c22a | -4.31238 | -48.10312 | 2025-07-19 04:08:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 19.7 |
| 7663820c-eceb-3fc6-b818-aeae2c7dda6f | -3.78783 | -41.91362 | 2025-07-19 04:08:00 | NOAA-21 | SÃO JOSÉ DO DIVINO | PIAUÍ | Brasil | 2210052 | 22 | 33 | nan | nan | nan | Caatinga | 0.4 |
| 7ec9d168-3fbe-3e92-8cbd-60c8e4273558 | -5.65575 | -43.72098 | 2025-07-19 04:08:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 9.0 |
| 4df16a8d-7283-3762-bae7-bb67f598e57d | -6.83859 | -42.73808 | 2025-07-19 04:08:00 | NOAA-21 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| a1ef7599-b6f3-35cd-b7c2-7eef052cc231 | -8.14723 | -43.4316 | 2025-07-19 04:08:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| d8e89965-7a6d-37b8-971e-44fc612235c5 | -8.52958 | -47.84772 | 2025-07-19 04:08:00 | NOAA-21 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 07ce152e-435e-3cc8-b6a0-da0e6f729fca | -3.61457 | -43.54068 | 2025-07-19 04:08:00 | NOAA-21 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 8.3 |
| aa20b0ae-4985-35c6-951b-79f9fea643bd | -6.95306 | -50.45956 | 2025-07-19 04:08:00 | NOAA-21 | ÁGUA AZUL DO NORTE | PARÁ | Brasil | 1500347 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 9768f61f-10be-3421-9df2-745171e4e995 | -7.95405 | -43.95579 | 2025-07-19 04:08:00 | NOAA-21 | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 4ee67060-07c0-3c22-aee5-8e8486993f6a | -7.48474 | -47.49918 | 2025-07-19 04:08:00 | NOAA-21 | BARRA DO OURO | TOCANTINS | Brasil | 1703073 | 17 | 33 | nan | nan | nan | Cerrado | 6.2 |
| f888e77e-ea47-3c73-afc0-e747fbc3c9d8 | -7.48675 | -43.93461 | 2025-07-19 04:08:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 8be3ac29-ba16-3b16-a701-7e08ed1c3bf0 | -4.10703 | -48.2045 | 2025-07-19 04:08:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 45a648f3-0f19-37e7-b8a4-72b619457edb | -9.4842 | -40.38258 | 2025-07-19 04:08:00 | NOAA-21 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 11.8 |
| 42ee72f9-4837-3279-822e-c7f6097c3e07 | -7.70856 | -47.28694 | 2025-07-19 04:08:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 3f545ba7-25f5-3325-978e-10e02626ef86 | -3.67341 | -45.40408 | 2025-07-19 04:08:00 | NOAA-21 | SANTA INÊS | MARANHÃO | Brasil | 2109908 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| af063b83-eefa-346d-ae50-718b46a33bb7 | -9.51467 | -43.24336 | 2025-07-19 04:08:00 | NOAA-21 | CAMPO ALEGRE DE LOURDES | BAHIA | Brasil | 2905909 | 29 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 54f97e38-2568-33d7-adc5-b2a25e527137 | -8.53444 | -47.84451 | 2025-07-19 04:08:00 | NOAA-21 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| ffd2ab7c-ea78-30b6-bade-b7e101ab45f6 | -7.95586 | -43.94456 | 2025-07-19 04:08:00 | NOAA-21 | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 8267af0a-9916-3c83-a212-60ada699860f | -6.76295 | -45.50948 | 2025-07-19 04:08:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 7b745aad-b9db-36fe-aa60-40df220557f7 | -6.44645 | -51.89001 | 2025-07-19 04:08:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 2aa7b538-3b50-395b-b8f0-226e991b59fd | -7.17593 | -44.09851 | 2025-07-19 04:08:00 | NOAA-21 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| f8f7bc38-687f-3c3b-9ec3-bdfdbfb44673 | -3.39626 | -47.47958 | 2025-07-19 04:08:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| b64ea314-41ad-3d4e-a78e-2bc75e9089fa | -5.65197 | -43.7281 | 2025-07-19 04:08:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 2395fac1-3da9-32ec-b6d0-2a673293391e | -8.31021 | -55.11457 | 2025-07-19 04:08:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 090cce8a-faa6-36c1-819e-5cb671d30e6d | -7.63079 | -44.29985 | 2025-07-19 04:08:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 59cf7c6f-e6c2-362b-9e42-0c91053e63a6 | -5.66043 | -43.71396 | 2025-07-19 04:08:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 438a6c69-a376-3bfb-a757-2db960a0a765 | -6.87469 | -42.74737 | 2025-07-19 04:08:00 | NOAA-21 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 1c00cfe5-1732-35c0-ba82-51e1e3292d3b | -7.17939 | -44.09904 | 2025-07-19 04:08:00 | NOAA-21 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 6bf406d8-465d-35c8-ab9a-768b2b367b15 | -8.07261 | -50.11161 | 2025-07-19 04:08:00 | NOAA-21 | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |


[Clique aqui para ver as próximas entradas](README10.md)
