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

## Dados Diários - Página 75

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| ba0384b5-1b95-3af1-9a63-89c3df2b19ce | -8.40912 | -62.6926 | 2026-08-21 05:42:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 81e8e5eb-b491-3358-a52b-885b7f8dd455 | -8.56802 | -54.66727 | 2026-08-21 05:42:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 6b7258b2-3797-3de4-b74d-2efd53146400 | -6.43089 | -52.7417 | 2026-08-21 05:42:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| e0a62435-cd0d-3b8b-ac40-60cd6dcb737b | -11.16934 | -54.01229 | 2026-08-21 05:42:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 03474637-e1c3-364e-979d-c753a5bc183c | -9.2145 | -59.7821 | 2026-08-21 05:42:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 3eb27df3-54db-3074-878b-31689ed5b5aa | -8.59577 | -54.7123 | 2026-08-21 05:42:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| b76cd77d-6be7-30b4-bf7b-2b5ae16d934b | -4.78805 | -62.91911 | 2026-08-21 05:42:00 | NOAA-20 | TAPAUÁ | AMAZONAS | Brasil | 1304104 | 13 | 33 | nan | nan | nan | Amazônia | 3.2 |
| e03ad860-0d46-35a5-b98d-595c7a64d773 | -6.57614 | -58.97358 | 2026-08-21 05:42:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| b61d5ad2-74be-3cd6-907c-0ffb2b0fa73e | -5.82562 | -57.63853 | 2026-08-21 05:42:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f4a762e7-267f-31a5-8d83-4f321e7e9f21 | -6.0027 | -57.86706 | 2026-08-21 05:42:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2385c91a-d34c-36a3-8814-f26ea704ed8a | -6.58173 | -58.9637 | 2026-08-21 05:42:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 52612a43-1b4d-32dd-a0e1-3993ea63872f | -10.38527 | -61.20898 | 2026-08-21 05:42:00 | NOAA-20 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| dfe92013-c87b-3a61-95cd-75b08d0b72be | -5.49268 | -60.13158 | 2026-08-21 05:42:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 417c340a-313c-3c81-8b36-c94dcbc2093f | -6.64474 | -56.41605 | 2026-08-21 05:42:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| c9301b1a-d908-3e58-93fb-48a0fc4d0ff4 | -6.88636 | -59.44286 | 2026-08-21 05:42:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 13bc2b68-4b63-3e92-9602-8b0103540f21 | -7.37178 | -59.95174 | 2026-08-21 05:42:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 178e7e35-7875-3388-b6e4-fcef713c2c52 | -6.21356 | -55.47827 | 2026-08-21 05:42:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 623aaa4d-de55-3aa5-aedb-8c919b5f24a0 | -7.86594 | -63.75631 | 2026-08-21 05:42:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 2f5ec7df-5a14-33cc-8b8b-0ea57c9d3a27 | -7.60443 | -60.94729 | 2026-08-21 05:42:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b305c141-e0b9-3f29-89b9-3b1ebd712334 | -6.88579 | -56.43793 | 2026-08-21 05:42:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 5c789d92-ff19-3582-a97c-a99974c05490 | -6.437 | -52.74249 | 2026-08-21 05:42:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 2543841a-50bf-33f7-ae8b-9e590429482a | -6.88072 | -59.42667 | 2026-08-21 05:42:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 99d8efcd-3b9c-3846-83d1-da04a240d56e | -6.85626 | -59.02128 | 2026-08-21 05:42:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 42bf69dc-e15a-332a-9bfb-3bc2eb180255 | -9.41166 | -60.42078 | 2026-08-21 05:42:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 6c6bb0a7-7c02-38f7-b46d-65b01acfcb48 | -9.41866 | -60.43407 | 2026-08-21 05:42:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c4e5de24-7982-38f5-a4f2-9fa0b93863d8 | -6.42656 | -54.92633 | 2026-08-21 05:42:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 48c1fe0e-933d-34f2-8f1e-a31cb1db59a3 | -6.01628 | -57.82271 | 2026-08-21 05:42:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 97cf6a98-5eba-3320-a4ad-58c19df15d32 | -6.57666 | -58.97008 | 2026-08-21 05:42:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 100ad314-7e13-3229-a956-ea936baaecde | -9.21274 | -59.76613 | 2026-08-21 05:42:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.9 |
| d6350a6a-72ec-3554-a8da-f63a34351ada | -8.65703 | -54.63134 | 2026-08-21 05:42:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 1474a0e2-0948-345c-a9e9-de3d01f09007 | -9.07064 | -60.43324 | 2026-08-21 05:42:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b1bc38fb-4b97-349a-807f-c25d0047d1ba | -6.17123 | -55.44791 | 2026-08-21 05:42:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 9ee28d21-f1ee-3103-941b-a43ad7ae9c9c | -8.58654 | -54.78223 | 2026-08-21 05:42:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 4dbbc649-0565-3bd5-9eb5-2e353406f4a8 | -9.21523 | -59.77699 | 2026-08-21 05:42:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| a90f68ef-16b5-334b-9a55-46d984da2653 | -11.16721 | -54.02995 | 2026-08-21 05:42:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 896b3191-9ac8-3d1e-857a-12c4c2e7bfe9 | -7.77566 | -61.16816 | 2026-08-21 05:42:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 6.3 |
| f782a9b8-820e-34e6-af82-6bd5028a4e9e | -6.01309 | -57.82724 | 2026-08-21 05:42:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 1e2b63a7-4661-3a09-8b22-228cbae17886 | -6.84495 | -59.42403 | 2026-08-21 05:42:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 1f895999-ab26-341b-a100-869b90923623 | -6.6646 | -56.34669 | 2026-08-21 05:42:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 5e707f9c-cc4d-3e0b-8318-ac4161ae9dc4 | -9.41862 | -60.42666 | 2026-08-21 05:42:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 2d9de22c-59cf-3170-8753-df7e2a6552ac | -6.86605 | -59.44493 | 2026-08-21 05:42:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 7fa38fa9-f836-3354-949e-df4ddeda5319 | -11.16774 | -54.02559 | 2026-08-21 05:42:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 97db6a3a-9379-31b1-b0fb-8bf7963e5a54 | -6.90176 | -58.99191 | 2026-08-21 05:42:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e07f5a44-9859-3dfb-baf1-974afd21aabd | -6.38494 | -54.95369 | 2026-08-21 05:42:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 83d7c188-8bdc-3f1e-956a-fd4e04f2977b | -6.22294 | -55.62287 | 2026-08-21 05:42:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 18.8 |
| 1fb886b2-8c19-3981-9dd6-488607246f50 | -6.96707 | -59.30567 | 2026-08-21 05:42:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 568b7fcf-73d1-38c5-8c23-5aec6d88093f | -6.43215 | -52.73228 | 2026-08-21 05:42:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 791e191c-18c6-3d36-a5be-7dd73dfcc5ea | -6.43362 | -52.76343 | 2026-08-21 05:42:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d60b4279-ad8b-39d5-a9e1-d8db50877251 | -8.50141 | -54.87247 | 2026-08-21 05:42:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f93a1883-b980-3dde-9f99-8afe354a9eef | -9.40897 | -60.43966 | 2026-08-21 05:42:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 9014ee11-7b92-3ed5-ad48-0341619aa3e4 | -6.92078 | -59.34546 | 2026-08-21 05:42:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| f00e7ada-dd67-376e-9765-f3eb2d2a16a5 | -8.54774 | -54.77639 | 2026-08-21 05:42:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d534e9ca-763c-39eb-86b8-cc2564ddaaef | -9.41456 | -60.40931 | 2026-08-21 05:42:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 15.7 |
| 7453bccd-8f9d-3e8f-b621-aaaa2bcce438 | -10.24708 | -54.3649 | 2026-08-21 05:42:00 | NOAA-20 | MATUPÁ | MATO GROSSO | Brasil | 5105606 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 5a3d459a-2322-33e1-98cb-1fe8265bdd91 | -7.05603 | -59.83995 | 2026-08-21 05:42:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 390cc809-4106-39bb-af38-0fea564e3dcb | -6.41987 | -54.93536 | 2026-08-21 05:42:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 53dc01ec-7584-341c-8439-83165e4c7ea3 | -8.59675 | -54.7468 | 2026-08-21 05:42:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 4aa33087-5e67-321d-bb2f-d39b123926b9 | -6.38678 | -54.94071 | 2026-08-21 05:42:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 309d6515-a8bc-3fcc-8f5c-edf6ac5e5406 | -6.58522 | -58.9678 | 2026-08-21 05:42:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| c72cc838-ccc5-3077-a3dd-a41059121815 | -11.19922 | -55.057 | 2026-08-21 05:42:00 | NOAA-20 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 48cb4e55-e721-394c-843b-08ca7f2672a9 | -9.39736 | -60.54816 | 2026-08-21 05:42:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 41e63623-d9e3-3e3b-827e-e4ef736b22fc | -6.87287 | -59.42556 | 2026-08-21 05:42:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.4 |
| dee524a3-1e75-36a8-8061-50e2db129ec5 | -6.22362 | -55.62207 | 2026-08-21 05:42:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 29.4 |
| ba2be2a9-636a-34c1-afd8-6bfcc5e8fb2c | -9.41615 | -60.41661 | 2026-08-21 05:42:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 33.1 |
| 393502ab-4211-3d4e-bc98-c4d97ddbef42 | -8.40515 | -62.69575 | 2026-08-21 05:42:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 40a2dabf-41bc-326a-a9b6-1d2dd1fd6ad6 | -8.58561 | -54.78942 | 2026-08-21 05:42:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| eb1723bb-c17d-3fd9-be20-287985f228c7 | -8.37687 | -62.69883 | 2026-08-21 05:42:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 20.6 |
| 3c1fc001-5968-3a76-94a0-ae60f0d50aca | -9.15919 | -59.55584 | 2026-08-21 05:42:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c34ee18b-3ce3-3b68-a3b7-29f3e501aec0 | -11.21303 | -54.00365 | 2026-08-21 05:42:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| fd9075d2-36a9-33bc-ac13-4d6ec6340f84 | -10.3883 | -61.21394 | 2026-08-21 05:42:00 | NOAA-20 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b044d6d8-5b52-3913-97a3-ebd9278e3191 | -6.80688 | -59.01406 | 2026-08-21 05:42:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| eb58f7b5-3bbe-30c4-8605-2e94d79cc48f | -7.87148 | -63.76433 | 2026-08-21 05:42:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 599d8ab9-7c9c-3bc5-aef5-a25c120025ef | -9.41103 | -60.43293 | 2026-08-21 05:42:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 3.9 |
| b38a29b0-11d5-322b-ab6f-eb04388bb061 | -9.41174 | -60.42822 | 2026-08-21 05:42:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| ef68cd43-8bc6-32c9-ae59-5caace4f4685 | -6.76254 | -59.46745 | 2026-08-21 05:42:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 4a1f4397-b430-3e61-98d3-d2bbf27e4e64 | -9.4175 | -60.40712 | 2026-08-21 05:42:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 33.0 |
| fceba69b-cc6d-364a-8333-97091666b0c3 | -8.52068 | -55.32947 | 2026-08-21 05:42:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 4580d86e-c8d2-3364-8a95-fb6f2f17bfff | -8.5198 | -55.33616 | 2026-08-21 05:42:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 07098ef0-4597-3eab-9d04-c0758b749c97 | -9.21596 | -59.77187 | 2026-08-21 05:42:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 69b74a6e-53ec-386f-ae6c-b59bfb51df84 | -7.06385 | -59.97063 | 2026-08-21 05:42:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c7a6eba4-881a-39e7-9c22-90aa9f7b9152 | -7.60346 | -60.94863 | 2026-08-21 05:42:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a8a05748-e389-3f44-8329-154fc84f101a | -6.20131 | -55.49144 | 2026-08-21 05:42:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ef3af8b3-cd22-3179-9c53-95afb4c38ce7 | -9.41144 | -60.40401 | 2026-08-21 05:42:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 39.7 |
| 021565ec-75e7-3f0f-a902-a5d10f9d5b43 | -6.6932 | -58.94069 | 2026-08-21 05:42:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 6.8 |
| f1e9c1ec-8566-378d-aa15-9c74f0502541 | -6.89884 | -55.72061 | 2026-08-21 05:42:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| eb74e843-0818-3317-9984-991ce9546ed2 | -5.86717 | -57.6679 | 2026-08-21 05:42:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 8a8a4af9-0435-3437-97cc-fdf5b28c0201 | -9.39215 | -60.55935 | 2026-08-21 05:42:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 09d12ea3-063a-37dc-a384-23e55d00c38e | -8.58577 | -54.78532 | 2026-08-21 05:42:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 1230c14f-b48f-3a52-bde2-37d5b97c2c29 | -6.12883 | -59.91179 | 2026-08-21 05:42:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 860f2317-192f-3bf9-9e39-3e9ef478b62a | -7.60858 | -60.96938 | 2026-08-21 05:42:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 694aea9d-dddb-3cb6-b386-877c24746f96 | -10.38963 | -61.2051 | 2026-08-21 05:42:00 | NOAA-20 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| dbe3bd2c-de1f-39f2-997d-1673a441e3c1 | -9.39663 | -60.55527 | 2026-08-21 05:42:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 97115716-e031-3eaf-b68e-4fe35f4cc63a | -6.43026 | -52.74638 | 2026-08-21 05:42:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| bbdd3e90-6366-39ca-b7da-d5c7c25be7ee | -6.00269 | -57.83791 | 2026-08-21 05:42:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 454f2cd1-327c-3da7-80bf-7e39d0621ba5 | -6.22445 | -55.61642 | 2026-08-21 05:42:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 41.8 |
| 209588b4-45b0-301e-babe-7b1dc7b60ca3 | -6.85503 | -59.43817 | 2026-08-21 05:42:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 986105c8-1156-3299-93d4-9e87f3f375e1 | -6.58505 | -58.99624 | 2026-08-21 05:42:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 5e076875-d165-3fa5-9d5c-951fd0833406 | -9.44923 | -51.6142 | 2026-08-21 05:42:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| d5b8eb86-8721-3a39-8cbb-de57e97cab75 | -6.82908 | -59.39626 | 2026-08-21 05:42:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 15.9 |
| 9ad7b2b0-3e56-3ed0-aa52-8016faa6f4c4 | -6.81266 | -59.39879 | 2026-08-21 05:42:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 5.6 |


[Clique aqui para ver as próximas entradas](README76.md)
