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

## Dados Diários - Página 73

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 70aa2d2d-338c-3954-bb7c-612efc577eb8 | -11.6924 | -44.40327 | 2025-09-28 04:25:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 7c4490e4-53c6-38f0-b678-6d8887620ea3 | -11.60081 | -44.34 | 2025-09-28 04:25:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| f90a1b1c-d00c-3da1-8a4c-08c7f50cf1db | -9.07313 | -45.53734 | 2025-09-28 04:25:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| f8f38948-444c-3bf6-8898-431290b75697 | -6.0711 | -42.45037 | 2025-09-28 04:25:00 | NOAA-20 | HUGO NAPOLEÃO | PIAUÍ | Brasil | 2204600 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 96e8ae1b-b1a0-357d-b9b5-c44beb6d1d7b | -12.53775 | -48.29648 | 2025-09-28 04:25:00 | NOAA-20 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| f4238845-f65a-3ed8-b9ff-e36f13870134 | -10.31639 | -48.20232 | 2025-09-28 04:25:00 | NOAA-20 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 24eda579-85c6-3a7b-88d8-b523b6631189 | -6.69693 | -44.57436 | 2025-09-28 04:25:00 | NOAA-20 | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 300aae0b-3af9-36f6-a566-dfc34f001d99 | -6.48051 | -44.25088 | 2025-09-28 04:25:00 | NOAA-20 | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b4d489c4-7a04-34c3-b078-ad719c47350d | -12.78397 | -47.75249 | 2025-09-28 04:25:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| bd9ad17f-291f-3611-84f7-97c1dfc039e1 | -12.68993 | -46.87874 | 2025-09-28 04:25:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 9.3 |
| 207fce15-48b1-347e-bd0a-a328598c58a2 | -11.99883 | -47.04376 | 2025-09-28 04:25:00 | NOAA-20 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 6379b114-6f95-325d-bc2b-2c98969a3f95 | -12.90795 | -45.14752 | 2025-09-28 04:25:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 57086eef-37b7-30af-8365-60908d6baa7d | -11.44067 | -44.97927 | 2025-09-28 04:25:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 660cfcec-2656-3d45-aca2-37b5e6ba550c | -7.53283 | -46.09684 | 2025-09-28 04:25:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 6.0 |
| ea8a52c2-f664-3f56-af8d-b2ebc67b9fad | -8.82779 | -46.00005 | 2025-09-28 04:25:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| d1a04d55-35b3-3648-b75e-5534002a788d | -6.48905 | -44.24088 | 2025-09-28 04:25:00 | NOAA-20 | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 063df962-4583-3962-94ef-37732f4d2a9e | -6.47996 | -44.25452 | 2025-09-28 04:25:00 | NOAA-20 | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 3d14aeff-7f04-3a73-8dd9-f03361f84c21 | -10.91843 | -45.72781 | 2025-09-28 04:25:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 0f4d2e39-d889-348b-915f-4810c599d5d6 | -9.41336 | -54.68664 | 2025-09-28 04:25:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 49126c4e-ab57-3daf-98bd-3393cc06e750 | -7.17956 | -41.71992 | 2025-09-28 04:25:00 | NOAA-20 | PAQUETÁ | PIAUÍ | Brasil | 2207553 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 99ec4b1c-41df-3d74-8eb7-d1aa17812b4b | -8.16613 | -46.41024 | 2025-09-28 04:25:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 9.0 |
| 57e08845-ed15-30a1-a2aa-2f58d82db7c8 | -8.28386 | -45.43675 | 2025-09-28 04:25:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 88ffba67-0d4d-3a9b-896f-019fd65148b2 | -5.95563 | -43.77132 | 2025-09-28 04:25:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| f6de1c29-4beb-3af0-a846-0bc02aae8f5e | -11.98796 | -47.95128 | 2025-09-28 04:25:00 | NOAA-20 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e0270fe5-8866-3c20-a6df-c846bc6690c1 | -11.98059 | -47.8923 | 2025-09-28 04:25:00 | NOAA-20 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| eb847fa4-cc2c-3785-9f55-cc7abfb8f646 | -5.71519 | -47.90803 | 2025-09-28 04:25:00 | NOAA-20 | ARAGUATINS | TOCANTINS | Brasil | 1702208 | 17 | 33 | nan | nan | nan | Amazônia | 0.6 |
| ef01bf25-c636-3e0a-be17-3f070af61428 | -8.48021 | -47.79108 | 2025-09-28 04:25:00 | NOAA-20 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 06650d7a-84f4-3eac-a028-06b5b1b4efdf | -12.92901 | -45.12634 | 2025-09-28 04:25:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 886f03c1-f7c2-356f-9e06-c39c01ac3108 | -9.10826 | -45.87804 | 2025-09-28 04:25:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 7095119c-9e6b-3189-b68d-82910599a535 | -11.99441 | -47.05027 | 2025-09-28 04:25:00 | NOAA-20 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 5b78fd36-8474-3708-8d21-ec232b25695f | -11.99311 | -47.8978 | 2025-09-28 04:25:00 | NOAA-20 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 9802ea3f-f020-3bc7-b255-bce482d4deba | -11.94345 | -47.93327 | 2025-09-28 04:25:00 | NOAA-20 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| ad689446-9ab5-386c-88a9-61354023b8ee | -10.75576 | -45.39082 | 2025-09-28 04:25:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 0ec7d267-a901-3ec1-b9ea-35fe1bb87112 | -5.98489 | -44.12769 | 2025-09-28 04:25:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 6e34c9db-c6e9-349b-a521-f150fb240f7f | -10.99936 | -45.60548 | 2025-09-28 04:25:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 3f858b4d-e84b-3f1c-aede-28bc9efe77b1 | -10.11792 | -45.32804 | 2025-09-28 04:25:00 | NOAA-20 | SÃO GONÇALO DO GURGUÉIA | PIAUÍ | Brasil | 2209757 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 00f0bdcb-9664-3d01-a5bb-99443ac21fa0 | -11.61489 | -44.4183 | 2025-09-28 04:25:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e3750db6-428e-3056-9e4c-85010cc457f0 | -11.84477 | -48.25137 | 2025-09-28 04:25:00 | NOAA-20 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| f5778d0c-6cac-3a0f-83d8-db6467a525b4 | -10.8228 | -45.38565 | 2025-09-28 04:25:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 11d9cee3-b0bf-346f-bc6f-e9e44ed8130f | -12.67941 | -46.88064 | 2025-09-28 04:25:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 7c5cb35d-2bdd-3ebe-85dd-dfa9487947c7 | -8.28335 | -45.46225 | 2025-09-28 04:25:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 7e5b4427-3333-37da-a037-dbf6c7eb9582 | -12.01262 | -47.08592 | 2025-09-28 04:25:00 | NOAA-20 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| afd1878d-3c09-3977-9dab-06742bb7a0b0 | -11.99496 | -47.06843 | 2025-09-28 04:25:00 | NOAA-20 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 8d9c4e5e-82d0-3bbe-ab1a-3e65961c0d46 | -12.69239 | -45.47127 | 2025-09-28 04:25:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 8a36d518-2004-347b-85fb-aa616ef26bf1 | -9.35296 | -47.62354 | 2025-09-28 04:25:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a7b05239-6dee-3c44-a89c-90e1a4407468 | -10.80062 | -45.37084 | 2025-09-28 04:25:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| c33bebc2-3e9f-334d-b7c4-d77c75286c72 | -11.99592 | -47.88017 | 2025-09-28 04:25:00 | NOAA-20 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 31382fb4-dfc9-3846-92bd-f13e3caace76 | -6.43699 | -43.9397 | 2025-09-28 04:25:00 | NOAA-20 | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 70d39576-f0f5-30af-880d-d7ae74d5753b | -10.11907 | -45.66142 | 2025-09-28 04:25:00 | NOAA-20 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 1b7e9559-a774-3d17-8e97-84805ae19460 | -8.44109 | -46.86375 | 2025-09-28 04:25:00 | NOAA-20 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| cf4d5593-6555-3ce6-bf2f-85547e3290ad | -5.87728 | -43.19864 | 2025-09-28 04:25:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 3e963eb6-c925-3a78-a550-188ded95f6b4 | -7.86449 | -44.56393 | 2025-09-28 04:25:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 6e0daa81-f16b-336e-b732-afc35721b5e0 | -6.75921 | -45.52911 | 2025-09-28 04:25:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 67005b88-7af4-3434-851f-9fd82081fa51 | -6.83379 | -44.09099 | 2025-09-28 04:25:00 | NOAA-20 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| db0ad7e6-f612-34ae-a1a7-45ae2f0534a1 | -11.26246 | -48.38276 | 2025-09-28 04:25:00 | NOAA-20 | IPUEIRAS | TOCANTINS | Brasil | 1709807 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 366da895-fe3d-32de-bf8a-9302bc6397b2 | -8.64522 | -44.85997 | 2025-09-28 04:25:00 | NOAA-20 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 3.9 |
| d1c2d944-1949-35ad-8efa-ec88fabe2d1c | -10.91647 | -45.73125 | 2025-09-28 04:25:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 52a30095-2534-3c05-9916-3383f79659b0 | -6.02185 | -44.77111 | 2025-09-28 04:25:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| c2a18e20-ba70-3bcb-83ea-9e509f8395c8 | -8.48405 | -47.80996 | 2025-09-28 04:25:00 | NOAA-20 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 513d3a4c-c987-3bed-9892-e1941d96219d | -10.91591 | -45.73489 | 2025-09-28 04:25:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 454963f8-2418-3e96-8d2e-5dc35a1a83d8 | -8.28725 | -45.45922 | 2025-09-28 04:25:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 5fbd1c61-a01e-341d-a316-c972e5282c8d | -12.00491 | -47.09171 | 2025-09-28 04:25:00 | NOAA-20 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 9244a054-83ca-3e61-abf9-6a00e096f40f | -11.40325 | -46.96638 | 2025-09-28 04:25:00 | NOAA-20 | PORTO ALEGRE DO TOCANTINS | TOCANTINS | Brasil | 1718006 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 605798eb-9ee7-3e8b-9829-5a6e9f6f01fc | -7.54939 | -46.09946 | 2025-09-28 04:25:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 8be9b60c-8d4b-37cd-89e3-38c11379ceac | -6.70768 | -44.5948 | 2025-09-28 04:25:00 | NOAA-20 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 08b309a3-bc1b-372a-9357-f6c5bc98c9e9 | -7.03221 | -45.19287 | 2025-09-28 04:25:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| bdc9d3fd-c208-3246-9f50-1aba43b3ee6a | -12.00546 | -47.08819 | 2025-09-28 04:25:00 | NOAA-20 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 8158e88b-b474-39c5-9496-6f8254d4ad60 | -12.73994 | -46.81719 | 2025-09-28 04:25:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| b4decab9-7b93-3858-a42d-8f5c32d47d24 | -6.43257 | -43.51378 | 2025-09-28 04:25:00 | NOAA-20 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 4c75179a-e93d-39d5-afc8-6c2065b393dc | -8.64579 | -44.85626 | 2025-09-28 04:25:00 | NOAA-20 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 3.6 |
| ab8805d2-5f20-3634-8aa1-8fb49d0b7103 | -6.47853 | -44.51493 | 2025-09-28 04:25:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 602def28-e91c-3b7b-b53d-5554f83d2322 | -15.08319 | -48.33173 | 2025-09-28 04:27:00 | NOAA-20 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 3031f1fc-51b9-3b90-b432-e781e0567c8f | -15.58469 | -42.40627 | 2025-09-28 04:27:00 | NOAA-20 | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| fb496bbf-3432-3ab3-a383-b5fd07cb142b | -15.44053 | -48.2188 | 2025-09-28 04:27:00 | NOAA-20 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 3a74134f-13d2-3021-9d24-f2848068d525 | -15.44047 | -48.24077 | 2025-09-28 04:27:00 | NOAA-20 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 98df98bb-2234-3733-ab90-e3ff1c2c0d0e | -15.25348 | -56.81968 | 2025-09-28 04:27:00 | NOAA-20 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| cd42b50d-3199-3aa6-a901-cfacb6a22760 | -15.3275 | -47.90056 | 2025-09-28 04:27:00 | NOAA-20 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| aaedaa21-62d2-310c-b067-376908c91b88 | -19.865 | -43.80453 | 2025-09-28 04:27:00 | NOAA-20 | SABARÁ | MINAS GERAIS | Brasil | 3156700 | 31 | 33 | nan | nan | nan | Mata Atlântica | 6.3 |
| 9dd154b6-125a-3bea-b38b-fc5557162f14 | -17.7198 | -46.71253 | 2025-09-28 04:27:00 | NOAA-20 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 3.5 |
| ab3ed58f-d839-3956-9dc8-967e236a5f29 | -15.1974 | -48.4677 | 2025-09-28 04:27:00 | NOAA-20 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 7d2a0eee-4e0d-35ee-b9c1-dbd7e8ce2be6 | -13.33894 | -47.28828 | 2025-09-28 04:27:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 17e4ab12-9727-31dd-8ba8-55daf00837b0 | -18.17985 | -53.31906 | 2025-09-28 04:27:00 | NOAA-20 | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 70ea060c-2e16-3df3-9e5f-ece35502490a | -13.79908 | -47.92593 | 2025-09-28 04:27:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| b5bcd45e-34d3-3dc7-9d5b-90d5ef909dfe | -15.95528 | -50.4232 | 2025-09-28 04:27:00 | NOAA-20 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f31b6545-298d-361a-a93e-9c0e425a265e | -19.8597 | -42.59836 | 2025-09-28 04:27:00 | NOAA-20 | DIONÍSIO | MINAS GERAIS | Brasil | 3121803 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 99236956-d412-3b1e-aa2f-b1c61e24766e | -13.78204 | -47.88315 | 2025-09-28 04:27:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c4141800-368c-34ec-82eb-40a3b99d7014 | -14.53708 | -48.41228 | 2025-09-28 04:27:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 6d112e06-4ffe-34dd-b8c8-f7cae3ce30e2 | -15.29245 | -49.48332 | 2025-09-28 04:27:00 | NOAA-20 | SANTA ISABEL | GOIÁS | Brasil | 5219357 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 6164e623-1e68-3c71-b121-55435e60acf2 | -13.24966 | -48.45363 | 2025-09-28 04:27:00 | NOAA-20 | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ca30d7bb-8168-34ac-95ef-57d87089632a | -15.20015 | -48.47183 | 2025-09-28 04:27:00 | NOAA-20 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| b43e9354-3daf-32f9-98ed-4e403362dbf9 | -16.96037 | -53.69826 | 2025-09-28 04:27:00 | NOAA-20 | ALTO GARÇAS | MATO GROSSO | Brasil | 5100409 | 51 | 33 | nan | nan | nan | Cerrado | 10.5 |
| 5c2ff184-c27c-3a3c-8d6a-e8c8cd822ebf | -15.31791 | -56.80741 | 2025-09-28 04:27:00 | NOAA-20 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ed0eef7f-7970-3740-a06b-26f0ea8ec6b0 | -14.49931 | -48.56329 | 2025-09-28 04:27:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| cd04396d-6144-3af1-a0f2-4c5226514a41 | -15.20423 | -48.05956 | 2025-09-28 04:27:00 | NOAA-20 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 85658285-2ab0-3b4a-abf9-813494fbcc33 | -13.25687 | -48.45121 | 2025-09-28 04:27:00 | NOAA-20 | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f4ebab69-4d64-3df9-8336-977b57337c19 | -15.28851 | -49.48634 | 2025-09-28 04:27:00 | NOAA-20 | SANTA ISABEL | GOIÁS | Brasil | 5219357 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d4a3fc47-7193-3dfc-afd3-d07fe170afee | -19.49147 | -41.10865 | 2025-09-28 04:27:00 | NOAA-20 | AIMORÉS | MINAS GERAIS | Brasil | 3101102 | 31 | 33 | nan | nan | nan | Mata Atlântica | 10.4 |
| 74cd6590-61be-3c23-b91c-4c3748103e9f | -14.77273 | -45.65241 | 2025-09-28 04:27:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 43bb2500-f6b3-3920-ba49-76cce6142749 | -19.31827 | -43.81244 | 2025-09-28 04:27:00 | NOAA-20 | BALDIM | MINAS GERAIS | Brasil | 3105004 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 6abd57c7-c305-396c-af34-a898dfc17879 | -15.21579 | -48.07246 | 2025-09-28 04:27:00 | NOAA-20 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |


[Clique aqui para ver as próximas entradas](README74.md)
