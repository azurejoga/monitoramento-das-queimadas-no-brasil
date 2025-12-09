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

## Dados Diários - Página 8

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| bfd7b236-f3d7-3502-83b2-4978e13964fb | 2.0181 | -55.66861 | 2025-12-09 04:53:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7ba24cf5-9a08-32ba-8c02-e8e6cdcfb29b | -3.43209 | -41.66433 | 2025-12-09 04:53:00 | NPP-375D | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 7.5 |
| ddfdb53b-aee0-3496-add5-803d0b1d285f | 0.41416 | -53.70391 | 2025-12-09 04:53:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| c83508b7-2578-38c2-aef6-b5ebb775dd06 | -3.42654 | -41.65911 | 2025-12-09 04:53:00 | NPP-375D | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 7.1 |
| e54539a3-55fd-3c8c-b7a8-509e4fb8ceb7 | -3.43878 | -41.65678 | 2025-12-09 04:53:00 | NPP-375D | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 5.6 |
| 6ad7d7a2-f6f0-36ae-ad03-afd96b0f1030 | 2.01916 | -55.67549 | 2025-12-09 04:53:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 83bceb25-f3a0-3255-91b2-16c52eb8cf03 | 0.06977 | -51.08273 | 2025-12-09 04:53:00 | NPP-375D | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 15f56c98-fe58-3a50-9404-f0b36968878c | -1.10144 | -52.26062 | 2025-12-09 04:53:00 | NPP-375D | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 97b968b4-2b87-3508-9d21-75d8e7c4bbfc | -2.05898 | -46.50028 | 2025-12-09 04:53:00 | NPP-375D | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 29aa6008-0c6e-3be2-aa58-0b3ecd2cdf4e | 2.05724 | -60.87338 | 2025-12-09 04:53:00 | NPP-375D | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 63c37e27-df31-3825-842f-e93517f34177 | 1.56979 | -55.99091 | 2025-12-09 04:53:00 | NPP-375D | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 4ef4dcf6-34b7-3f73-824b-17f3e8bd0ed2 | -3.20086 | -43.16953 | 2025-12-09 04:53:00 | NPP-375D | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 64f1dd61-3f7b-383f-9441-e44faa5abaad | -0.85188 | -51.95798 | 2025-12-09 04:53:00 | NPP-375D | LARANJAL DO JARI | AMAPÁ | Brasil | 1600279 | 16 | 33 | nan | nan | nan | Amazônia | 1.2 |
| dfac1877-bb44-3e93-aff5-8c52e00c2f7c | 1.57553 | -56.00097 | 2025-12-09 04:53:00 | NPP-375D | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| dbc02f5e-d997-3eff-9e47-fd2341a85f33 | -1.76849 | -46.19901 | 2025-12-09 04:53:00 | NPP-375D | BOA VISTA DO GURUPI | MARANHÃO | Brasil | 2101970 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 85699ed2-fff7-36fa-ac54-06e06c780c91 | -3.1956 | -43.16883 | 2025-12-09 04:53:00 | NPP-375D | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| c214e191-910a-36f4-a7de-6774a9b6470c | -0.99721 | -52.32303 | 2025-12-09 04:53:00 | NPP-375D | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 798c1e00-f2c3-3084-88a5-573eba4eb035 | -2.25871 | -46.06379 | 2025-12-09 04:53:00 | NPP-375D | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9e3cba3c-96c0-3d2e-af58-320b16537287 | -3.42107 | -41.65852 | 2025-12-09 04:53:00 | NPP-375D | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| e01c9caa-bb8d-34fd-8d3f-6250c92b6307 | -3.43818 | -41.66085 | 2025-12-09 04:53:00 | NPP-375D | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 4.9 |
| e7a7a997-d95e-31c0-b190-35466904c288 | -3.43996 | -41.64868 | 2025-12-09 04:53:00 | NPP-375D | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 5.3 |
| f211df6c-b1c3-375c-9f9b-cda4e8dd6c16 | -2.10587 | -45.35934 | 2025-12-09 04:53:00 | NPP-375D | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| dfa16ed7-9457-3372-bc22-aa8dfe2caad1 | -2.08918 | -45.79301 | 2025-12-09 04:53:00 | NPP-375D | GOVERNADOR NUNES FREIRE | MARANHÃO | Brasil | 2104677 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 373ef344-7f9c-35ed-8a35-cffc2eb82007 | -2.2591 | -46.46309 | 2025-12-09 04:53:00 | NPP-375D | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 85051ce3-4b5a-3e93-8df6-73b9c0c511f2 | -1.01631 | -47.98553 | 2025-12-09 04:53:00 | NPP-375D | SÃO CAETANO DE ODIVELAS | PARÁ | Brasil | 1507102 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 65438608-116f-332e-9f68-15eabeb2b868 | -3.43759 | -41.66492 | 2025-12-09 04:53:00 | NPP-375D | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 4.9 |
| 57896483-dea0-3151-a7e4-629e5adfde61 | 1.12965 | -60.52522 | 2025-12-09 04:53:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 18b4f84a-d766-30ae-b307-ce69ada11611 | -2.09285 | -45.79773 | 2025-12-09 04:53:00 | NPP-375D | GOVERNADOR NUNES FREIRE | MARANHÃO | Brasil | 2104677 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 1e39c8b2-04d8-390d-ac1a-f7a0ca2e78b8 | -2.05489 | -46.49961 | 2025-12-09 04:53:00 | NPP-375D | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| ea56270d-eb67-31cc-9117-28ee43b349bc | -1.10475 | -52.23973 | 2025-12-09 04:53:00 | NPP-375D | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 391c308e-75e5-3afe-a7c0-2bdc30ad467b | -2.10965 | -45.36434 | 2025-12-09 04:53:00 | NPP-375D | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 73dad0f0-92f3-380f-a319-d1f56e94b6f5 | 2.05663 | -60.86928 | 2025-12-09 04:53:00 | NPP-375D | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 0.7 |
| f73faaf6-a53c-3f23-b74e-427c1d943e9b | -0.99666 | -52.32651 | 2025-12-09 04:53:00 | NPP-375D | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 54569182-df7b-3d13-851d-cfc7905dac5c | 1.6769 | -50.71408 | 2025-12-09 04:53:00 | NPP-375D | PRACUÚBA | AMAPÁ | Brasil | 1600550 | 16 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 8e97669e-f3fe-3745-8543-4a583059e442 | -3.43937 | -41.65273 | 2025-12-09 04:53:00 | NPP-375D | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 5.6 |
| e034e5c6-e999-350c-8408-3c5e81cd5945 | -2.03418 | -45.82309 | 2025-12-09 04:53:00 | NPP-375D | GOVERNADOR NUNES FREIRE | MARANHÃO | Brasil | 2104677 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 5553b838-062e-3802-805d-cae11ee533bb | -1.10141 | -52.2392 | 2025-12-09 04:53:00 | NPP-375D | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 48189580-d1ac-3bd3-93a2-34c33f7784fa | -0.80425 | -47.86331 | 2025-12-09 04:53:00 | NPP-375D | CURUÇÁ | PARÁ | Brasil | 1502905 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 2e175611-2261-36ba-a09e-c0ecfe046f77 | 1.57497 | -55.99741 | 2025-12-09 04:53:00 | NPP-375D | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 8e9cf36f-a096-346d-b88e-a89b9e48f947 | 1.12904 | -60.52656 | 2025-12-09 04:53:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 67a7c9e1-56ab-35a0-a32d-f0edf8e30f2a | -3.33734 | -42.83679 | 2025-12-09 04:53:00 | NPP-375D | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c52bcd1a-244c-3b64-8c02-e6772797b093 | -3.42689 | -41.6594 | 2025-12-09 04:53:00 | NPP-375D | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 7.5 |
| 7c06c2f7-4e1a-3feb-a35f-b562447859ca | -3.43458 | -41.64806 | 2025-12-09 04:53:00 | NPP-375D | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 3.4 |
| 43d8e28f-2336-3034-93bb-8fab23b201b2 | -3.43414 | -41.64776 | 2025-12-09 04:53:00 | NPP-375D | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 454b1631-aa97-3d39-87d3-efc5c4ed72df | -2.10705 | -45.36164 | 2025-12-09 04:53:00 | NPP-375D | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 2.3 |
| fb6e4387-572d-34cd-a803-b7271df5db44 | 2.01514 | -55.67611 | 2025-12-09 04:53:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| eae4a5cc-07cc-3d25-91a0-c3e95d731c0b | -0.60369 | -51.81302 | 2025-12-09 04:53:00 | NPP-375D | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 0.7 |
| b7fede55-ada3-3bd5-b83f-0829e7364cf6 | -3.16218 | -44.1909 | 2025-12-09 04:55:00 | NPP-375D | ROSÁRIO | MARANHÃO | Brasil | 2109601 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 29f80fb3-6a6b-3ece-8008-40cc7079b026 | -1.87922 | -54.68518 | 2025-12-09 04:55:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| efbae0b8-c50c-3128-a63f-292d37086ced | -4.40327 | -44.31856 | 2025-12-09 04:55:00 | NPP-375D | PERITORÓ | MARANHÃO | Brasil | 2108454 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 238ca28e-effd-3de8-8093-57e95d28ca26 | -4.18438 | -43.8266 | 2025-12-09 04:55:00 | NPP-375D | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ea59a02c-f6e0-35ce-9b4c-f3fa239d2032 | -3.95587 | -41.52356 | 2025-12-09 04:55:00 | NPP-375D | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 6de6843a-4da6-32fd-b9df-29172f5a776c | -6.68016 | -43.76833 | 2025-12-09 04:55:00 | NPP-375D | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| ad1da484-685c-3189-ac9c-37bb809d54d0 | -5.70632 | -42.07357 | 2025-12-09 04:55:00 | NPP-375D | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| 62143477-e595-39a1-b117-95322d41902d | -5.71208 | -42.06793 | 2025-12-09 04:55:00 | NPP-375D | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 03bfb5ed-b511-3425-9798-f21621afa5f2 | -5.03956 | -43.59894 | 2025-12-09 04:55:00 | NPP-375D | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 9ad75db0-7a75-33c1-8b2d-616513712425 | -6.68548 | -43.76893 | 2025-12-09 04:55:00 | NPP-375D | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 9b459b28-0eef-30ac-b967-39f8c2b51170 | -5.70752 | -42.06533 | 2025-12-09 04:55:00 | NPP-375D | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 867d6884-7309-30fb-8131-2248c35007af | 3.40301 | -51.24969 | 2025-12-09 04:55:00 | NPP-375D | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 07d1e2d0-7b4e-3aab-be26-976eb0165bea | -5.03416 | -47.76264 | 2025-12-09 04:55:00 | NPP-375D | CIDELÂNDIA | MARANHÃO | Brasil | 2103257 | 21 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 4d77dc72-5df6-3170-914b-aa83ad8aab08 | -3.17662 | -45.22537 | 2025-12-09 04:55:00 | NPP-375D | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| a6aba855-7f9c-3398-ae01-3e26f137d39e | 3.39967 | -51.25021 | 2025-12-09 04:55:00 | NPP-375D | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 1f11ca4f-ecd8-32ff-8551-8a7f5f36f2e7 | -2.77441 | -54.52562 | 2025-12-09 04:55:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 6a06e5a4-b996-3cd4-96f2-bc21429cf025 | -3.95649 | -41.51939 | 2025-12-09 04:55:00 | NPP-375D | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 700de52c-a6e0-3cea-a1ec-5382a9f4eca1 | -4.18481 | -43.82364 | 2025-12-09 04:55:00 | NPP-375D | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| fea7ddae-8ea8-3fe6-b1a3-f037fe14fcea | -3.95954 | -41.51966 | 2025-12-09 04:55:00 | NPP-375D | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 66684725-8200-38bf-90de-47ab7509eb97 | -5.70692 | -42.06944 | 2025-12-09 04:55:00 | NPP-375D | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| fec2d81e-f259-3f55-ab16-5c7952a62941 | -3.62556 | -42.36898 | 2025-12-09 04:55:00 | NPP-375D | LUZILÂNDIA | PIAUÍ | Brasil | 2205805 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 654689a0-450e-3e30-b39b-c2cc72ce3f22 | -3.87431 | -42.51494 | 2025-12-09 04:55:00 | NPP-375D | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 0.4 |
| a3f8bab5-6f59-30a1-8ab7-099a5e14732b | -5.70624 | -42.06699 | 2025-12-09 04:55:00 | NPP-375D | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 543b2225-ad00-31c4-90e7-72fbeb7a47f6 | -3.6261 | -42.36519 | 2025-12-09 04:55:00 | NPP-375D | LUZILÂNDIA | PIAUÍ | Brasil | 2205805 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 3a20e304-46e3-3e40-908d-dce98fbc9274 | -5.7068 | -42.06287 | 2025-12-09 04:55:00 | NPP-375D | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| d24496ff-94a5-37f6-8e61-41d85bf18552 | -3.95363 | -41.51864 | 2025-12-09 04:55:00 | NPP-375D | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| d7faaf52-f5aa-3619-9d29-f94755840ae6 | -3.17732 | -45.2208 | 2025-12-09 04:55:00 | NPP-375D | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| aec76f49-8520-314a-ae6b-c445d252dba5 | -3.73869 | -44.55052 | 2025-12-09 04:55:00 | NPP-375D | MATÕES DO NORTE | MARANHÃO | Brasil | 2106631 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 0a46df48-7170-311a-a545-411eef3e99cb | -4.40266 | -44.3178 | 2025-12-09 04:55:00 | NPP-375D | PERITORÓ | MARANHÃO | Brasil | 2108454 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 30e075cf-9276-31dd-805f-7db75542a6e5 | -3.16707 | -44.19163 | 2025-12-09 04:55:00 | NPP-375D | ROSÁRIO | MARANHÃO | Brasil | 2109601 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| aa966e43-e0a7-3798-95da-3c7fbeecb1d0 | -4.40406 | -44.31301 | 2025-12-09 04:55:00 | NPP-375D | PERITORÓ | MARANHÃO | Brasil | 2108454 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 1b8cd4b0-4b5f-3401-9205-5ab16f6362e8 | -1.87562 | -54.6846 | 2025-12-09 04:55:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 0e175c52-f65a-36c9-8081-98db28192702 | -5.7051 | -42.07526 | 2025-12-09 04:55:00 | NPP-375D | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 696f1b35-4309-3382-b5d3-1668c97f5484 | -3.73724 | -44.55143 | 2025-12-09 04:55:00 | NPP-375D | MATÕES DO NORTE | MARANHÃO | Brasil | 2106631 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 38f7e320-22fa-340a-b404-17c9bfd420e9 | -5.70567 | -42.07112 | 2025-12-09 04:55:00 | NPP-375D | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 4c74cd1e-af48-37df-a4bd-3b5aa9c162f4 | -3.62784 | -42.36691 | 2025-12-09 04:55:00 | NPP-375D | LUZILÂNDIA | PIAUÍ | Brasil | 2205805 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 5131638e-8a88-3ca2-afd0-ce64a7026e0f | -2.77794 | -54.52623 | 2025-12-09 04:55:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| febba502-7a05-3a98-a1d6-e48b364f61c5 | -5.71322 | -42.05968 | 2025-12-09 04:55:00 | NPP-375D | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 364aa0c6-8c89-3d8a-809a-785a7bd3cb95 | -5.03908 | -43.60215 | 2025-12-09 04:55:00 | NPP-375D | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| cca3f55b-f3aa-38fe-9f14-afea353325b5 | -3.87985 | -42.51577 | 2025-12-09 04:55:00 | NPP-375D | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| cb682668-9022-3090-b839-5144ef029af4 | 3.3657 | -59.82343 | 2025-12-09 05:14:00 | NOAA-20 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 930d235c-2fb4-34a9-9ad6-27f74c6de56d | 3.39607 | -51.24956 | 2025-12-09 05:14:00 | NOAA-20 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 7.3 |
| cb193175-3f04-3735-b02d-951b56d11f49 | 3.39252 | -51.25406 | 2025-12-09 05:14:00 | NOAA-20 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 99a16c94-cb30-3eae-bfdb-9b2194c6d04b | 3.40443 | -51.24821 | 2025-12-09 05:14:00 | NOAA-20 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 46a22a41-cd40-3fa4-9ad2-38cf5043c3a7 | 3.40506 | -51.25203 | 2025-12-09 05:14:00 | NOAA-20 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 7ea603f3-333f-3a14-825b-756494026094 | 3.40025 | -51.24888 | 2025-12-09 05:14:00 | NOAA-20 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 7.3 |
| b7eb271f-e764-3d4d-b42b-77b4906a7026 | 3.3967 | -51.25339 | 2025-12-09 05:14:00 | NOAA-20 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 2.7 |
| e8714307-d098-3a59-bb04-6dbaf58334fe | -2.18909 | -48.1358 | 2025-12-09 05:16:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 30e90f62-066b-31be-a6fc-950d81437556 | -2.18343 | -48.13501 | 2025-12-09 05:16:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 69e12cf7-c281-3972-9812-66c2fa1ed156 | 1.96946 | -55.69144 | 2025-12-09 05:16:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| cd524f51-c44a-3ebe-a963-9f1b776bd19c | 2.01154 | -55.66373 | 2025-12-09 05:16:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 8376a346-e989-312f-9679-007dace97f8d | -2.18401 | -48.13121 | 2025-12-09 05:16:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| cc01d175-e62c-34e5-a6dd-ce0b0a16cea3 | -0.80357 | -47.86581 | 2025-12-09 05:16:00 | NOAA-20 | CURUÇÁ | PARÁ | Brasil | 1502905 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |


[Clique aqui para ver as próximas entradas](README9.md)
