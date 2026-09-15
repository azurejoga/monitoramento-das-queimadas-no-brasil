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

## Dados Diários - Página 20

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| bc88336f-9abf-3c27-a363-ea8ba9763e93 | -10.75832 | -44.81803 | 2026-09-15 03:38:00 | NOAA-21 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 6.9 |
| f6987637-6927-3290-93f4-4f19d6e377d9 | -7.21484 | -46.1381 | 2026-09-15 03:38:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 9968363b-8a7b-319b-b07b-be10381a7cff | -12.7854 | -47.56165 | 2026-09-15 03:38:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| b2507227-0cf2-3038-9aac-d938f8e66a9a | -11.23602 | -43.46559 | 2026-09-15 03:38:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 8ad86135-b088-3b7e-acec-1b8f42b3ed0c | -13.63485 | -47.88457 | 2026-09-15 03:38:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| fcb7a71c-bf33-38c6-8f3f-ea19a0bfea78 | -11.24559 | -43.47049 | 2026-09-15 03:38:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 5cb5ecfd-16fc-3dff-ba93-4cbb26f6c383 | -11.19314 | -42.82436 | 2026-09-15 03:38:00 | NOAA-21 | GENTIO DO OURO | BAHIA | Brasil | 2911303 | 29 | 33 | nan | nan | nan | Caatinga | 3.0 |
| 46f6760e-96e3-36ec-89d6-6c88b17837fd | -9.45501 | -40.39397 | 2026-09-15 03:38:00 | NOAA-21 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 15.3 |
| cfc024d5-2ae2-3dc8-a2c3-777454832efb | -7.22817 | -46.17292 | 2026-09-15 03:38:00 | NOAA-21 | NOVA COLINAS | MARANHÃO | Brasil | 2107258 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 6d044152-1523-3e68-b8f5-2c45ca6a3671 | -7.22223 | -46.13416 | 2026-09-15 03:38:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 3186a4f5-6060-3bb2-9b7a-87ee650eaaa5 | -12.47435 | -41.40683 | 2026-09-15 03:38:00 | NOAA-21 | LENÇÓIS | BAHIA | Brasil | 2919306 | 29 | 33 | nan | nan | nan | Caatinga | 2.1 |
| b835ae80-c9d2-3e15-bd7e-4a5dd57959eb | -10.85694 | -46.30558 | 2026-09-15 03:38:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 70da56b7-6639-3982-90ee-d81d09907319 | -7.22656 | -46.17667 | 2026-09-15 03:38:00 | NOAA-21 | NOVA COLINAS | MARANHÃO | Brasil | 2107258 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| ecb1ded4-1efc-34d9-b3de-abfa8d84eda7 | -10.5852 | -47.74725 | 2026-09-15 03:38:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| de264aa4-34b3-39c7-8436-c86cf46e1487 | -11.5068 | -45.78887 | 2026-09-15 03:38:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| fe111666-ba66-3104-8c8c-54a753fc8750 | -11.23658 | -43.46258 | 2026-09-15 03:38:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| ef7fbe37-45d6-35c0-9e60-ebcf8a6bf41d | -14.19815 | -47.43517 | 2026-09-15 03:38:00 | NOAA-21 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 14.6 |
| a61a18e2-d231-3a00-a04b-33bfca51640e | -8.99616 | -39.98417 | 2026-09-15 03:38:00 | NOAA-21 | SANTA MARIA DA BOA VISTA | PERNAMBUCO | Brasil | 2612604 | 26 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 57e90110-4a9b-38dc-b1fe-59d7a27c5ca9 | -14.19926 | -47.42993 | 2026-09-15 03:38:00 | NOAA-21 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 22.1 |
| 88f1d99a-8411-3c75-9640-8da810e020ba | -10.57981 | -47.73964 | 2026-09-15 03:38:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 067118f4-140a-3e89-8194-cbef39e6e183 | -8.47119 | -46.87041 | 2026-09-15 03:38:00 | NOAA-21 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 7.6 |
| dffaa960-0ef8-3a93-86b5-21b6af5d093c | -12.21291 | -38.98042 | 2026-09-15 03:38:00 | NOAA-21 | FEIRA DE SANTANA | BAHIA | Brasil | 2910800 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 41bd4f65-274f-306f-8e2a-e69578a765db | -11.8913 | -43.82256 | 2026-09-15 03:38:00 | NOAA-21 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 15004133-ff11-3a45-815b-005a5cbd4059 | -14.84563 | -42.40763 | 2026-09-15 03:38:00 | NOAA-21 | JACARACI | BAHIA | Brasil | 2917409 | 29 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 90810837-d40f-3b16-aa7e-446f151a9b0f | -7.24035 | -46.17398 | 2026-09-15 03:38:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 9.7 |
| 00531453-d996-34a5-867a-646ed0fd7edd | -10.95451 | -39.26891 | 2026-09-15 03:38:00 | NOAA-21 | CANSANÇÃO | BAHIA | Brasil | 2906808 | 29 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 49243915-f185-3261-b8c6-f2862fcd195a | -14.22043 | -47.42103 | 2026-09-15 03:38:00 | NOAA-21 | ALTO PARAÍSO DE GOIÁS | GOIÁS | Brasil | 5200605 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| a7e83513-0042-36b4-a645-11b426406aec | -9.45992 | -40.39563 | 2026-09-15 03:38:00 | NOAA-21 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 32.5 |
| 955dad98-cfc7-366c-91fe-0abdc6b6a01a | -14.16101 | -47.40343 | 2026-09-15 03:38:00 | NOAA-21 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d5224335-c7c8-3bab-858a-218c1946203b | -9.88444 | -47.77168 | 2026-09-15 03:38:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 8fc35040-b07e-3cd1-8bbf-b893dfb7f2f6 | -11.88424 | -43.82015 | 2026-09-15 03:38:00 | NOAA-21 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 11.6 |
| 45037855-f59b-33dc-a812-1ed19bf7d586 | -7.21948 | -46.14273 | 2026-09-15 03:38:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 932dd3b9-ba1f-3829-9719-ca9f873bed3b | -11.23995 | -43.44456 | 2026-09-15 03:38:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 00345b17-3de5-314c-9a03-db27fc0ed353 | -8.4713 | -46.86127 | 2026-09-15 03:38:00 | NOAA-21 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 6.7 |
| fb9b9d4a-621b-3387-861d-41dd61e45f4c | -12.49021 | -41.41787 | 2026-09-15 03:38:00 | NOAA-21 | LENÇÓIS | BAHIA | Brasil | 2919306 | 29 | 33 | nan | nan | nan | Caatinga | 1.9 |
| d84f79db-5205-3c76-9687-a28358795e90 | -11.97908 | -44.929 | 2026-09-15 03:38:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 2ef66009-a04e-327b-b911-fefb9cefd24e | -7.23656 | -46.16372 | 2026-09-15 03:38:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 13e9d844-4540-30d5-9d9b-1709aa4dc5a3 | -14.04375 | -43.29359 | 2026-09-15 03:38:00 | NOAA-21 | PALMAS DE MONTE ALTO | BAHIA | Brasil | 2923407 | 29 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 0263dded-5b97-3f14-be6c-7754040ac7a1 | -11.17383 | -42.7925 | 2026-09-15 03:38:00 | NOAA-21 | GENTIO DO OURO | BAHIA | Brasil | 2911303 | 29 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 04b88579-b787-33da-8eec-3f344c2ea9b8 | -7.10638 | -47.48316 | 2026-09-15 03:38:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 5.4 |
| b6479bd1-33d4-31a4-9859-660c0e74e7d1 | -10.86296 | -46.30716 | 2026-09-15 03:38:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b955abea-f3ef-3b91-88e3-6b278970e545 | -7.10019 | -47.48407 | 2026-09-15 03:38:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 21bfebbc-76da-36cf-85a6-cbbd284288f8 | -14.04371 | -43.29531 | 2026-09-15 03:38:00 | NOAA-21 | PALMAS DE MONTE ALTO | BAHIA | Brasil | 2923407 | 29 | 33 | nan | nan | nan | Caatinga | 2.6 |
| b9886959-ffbc-3be9-a96d-4618f90b300a | -7.24935 | -46.16642 | 2026-09-15 03:38:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 12.4 |
| 5193c45d-ac68-3e55-8696-e2c566a8a110 | -7.61271 | -47.29603 | 2026-09-15 03:38:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 622e8423-e1ed-3b4e-b6c9-09e7ed70d6d1 | -14.67908 | -42.84949 | 2026-09-15 03:38:00 | NOAA-21 | SEBASTIÃO LARANJEIRAS | BAHIA | Brasil | 2930006 | 29 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 6c1fd9c1-7dd5-3acc-abcc-3dc255d588c3 | -14.03896 | -43.29436 | 2026-09-15 03:38:00 | NOAA-21 | PALMAS DE MONTE ALTO | BAHIA | Brasil | 2923407 | 29 | 33 | nan | nan | nan | Caatinga | 2.6 |
| f6996248-b6bc-30e0-a47d-119f1160ef96 | -12.85651 | -44.38987 | 2026-09-15 03:38:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 86d8918e-6a8d-3731-8c78-a0fd984248fb | -14.20974 | -47.38483 | 2026-09-15 03:38:00 | NOAA-21 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 2d57577e-72f9-3950-9cb7-b9cc75b0f0f6 | -11.17285 | -42.79794 | 2026-09-15 03:38:00 | NOAA-21 | GENTIO DO OURO | BAHIA | Brasil | 2911303 | 29 | 33 | nan | nan | nan | Caatinga | 3.0 |
| 981b11f3-dd12-3fdc-8b25-c2dc8462a04b | -13.51756 | -44.16774 | 2026-09-15 03:38:00 | NOAA-21 | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 6b548aa8-8046-3d00-a182-4bbc8663e4de | -7.21309 | -46.14138 | 2026-09-15 03:38:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| e9e5302b-0984-321f-a4ba-73b38e1c3c80 | -7.10703 | -47.48598 | 2026-09-15 03:38:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 8.3 |
| cb519dfd-b6df-34c6-98f6-6dfafd48d663 | -12.85193 | -44.38558 | 2026-09-15 03:38:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 9.9 |
| 9a29d670-edfb-3773-b281-73e051a238f9 | -14.21455 | -47.3882 | 2026-09-15 03:38:00 | NOAA-21 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 6017808f-fd06-3035-9890-4a8c94e4a771 | -12.32071 | -41.78011 | 2026-09-15 03:38:00 | NOAA-21 | SEABRA | BAHIA | Brasil | 2929909 | 29 | 33 | nan | nan | nan | Caatinga | 1.2 |
| c3ab8b9a-0b13-3c8d-8927-a550c7e7876b | -11.24671 | -43.4645 | 2026-09-15 03:38:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 218fce1f-08ce-3d2e-80f7-2af0aa040107 | -10.8567 | -46.30584 | 2026-09-15 03:38:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 84da6890-89f1-3973-a234-402e1c4155b6 | -7.23456 | -46.17434 | 2026-09-15 03:38:00 | NOAA-21 | NOVA COLINAS | MARANHÃO | Brasil | 2107258 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 07e4b299-d722-38fe-a924-1cd041c990d2 | -8.46991 | -46.8683 | 2026-09-15 03:38:00 | NOAA-21 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 1ab73fef-714e-3dde-8c7a-55996b7a2efa | -7.76246 | -45.18332 | 2026-09-15 03:38:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 45ab0ea7-42d2-3456-adf7-d14ac02ed827 | -11.24615 | -43.46749 | 2026-09-15 03:38:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 1fe35135-5c3f-348a-91fb-a7b229c29840 | -8.47255 | -46.86322 | 2026-09-15 03:38:00 | NOAA-21 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 8c33b819-72c7-35a4-99fe-1ba1f1483c4a | -8.79211 | -45.90705 | 2026-09-15 03:38:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 95c8333b-61af-31e1-8dcd-3c4266085796 | -9.45572 | -40.38993 | 2026-09-15 03:38:00 | NOAA-21 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 15.3 |
| fd2ba16a-b52e-3e31-bc36-2ad31c220c4c | -12.47799 | -41.41142 | 2026-09-15 03:38:00 | NOAA-21 | LENÇÓIS | BAHIA | Brasil | 2919306 | 29 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 1af3824a-eb9a-3360-97d0-8baae2eaac51 | -10.752 | -44.82085 | 2026-09-15 03:38:00 | NOAA-21 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 9ea9be4d-bc13-3ab2-8a99-2a57364142ea | -15.25963 | -40.99945 | 2026-09-15 03:38:00 | NOAA-21 | VITÓRIA DA CONQUISTA | BAHIA | Brasil | 2933307 | 29 | 33 | nan | nan | nan | Mata Atlântica | 10.1 |
| 2f6a2dc3-72d4-30bb-9b93-dc3bc0db8994 | -7.23557 | -46.16896 | 2026-09-15 03:38:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 3309a418-cd85-3f6b-9134-992c5f61af77 | -11.23714 | -43.45959 | 2026-09-15 03:38:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 4444d244-e14c-38c5-bf41-33ac11e6d440 | -12.39167 | -41.43529 | 2026-09-15 03:38:00 | NOAA-21 | IRAQUARA | BAHIA | Brasil | 2914406 | 29 | 33 | nan | nan | nan | Caatinga | 0.9 |
| dc3cdbc9-8d90-3094-a2e9-1a761f9f806c | -8.09537 | -43.78137 | 2026-09-15 03:38:00 | NOAA-21 | COLÔNIA DO GURGUÉIA | PIAUÍ | Brasil | 2202752 | 22 | 33 | nan | nan | nan | Caatinga | 3.4 |
| a488248c-768c-34d4-981f-38101f1a37fe | -8.99683 | -39.98034 | 2026-09-15 03:38:00 | NOAA-21 | SANTA MARIA DA BOA VISTA | PERNAMBUCO | Brasil | 2612604 | 26 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 2fc960ac-4073-3579-b40a-8512c1ecffe6 | -10.86273 | -46.30747 | 2026-09-15 03:38:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| b0cd50c6-254f-321e-b0e0-4dd1404189f9 | -7.24962 | -46.15948 | 2026-09-15 03:38:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 13.4 |
| 8927296f-73bf-3698-a76b-4c11dfc076c3 | -12.1251 | -44.21484 | 2026-09-15 03:38:00 | NOAA-21 | CRISTÓPOLIS | BAHIA | Brasil | 2909703 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 35737fca-69b1-3b81-a4ba-7c89f3a11f9b | -10.75274 | -44.81702 | 2026-09-15 03:38:00 | NOAA-21 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 82a38f48-ad71-3e2b-8bb6-8e392d8b7318 | -8.48966 | -44.5852 | 2026-09-15 03:38:00 | NOAA-21 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 677c39f0-f481-3218-a000-f2b42b5ffef3 | -14.17148 | -47.41485 | 2026-09-15 03:38:00 | NOAA-21 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| a7df8f48-247a-3a04-aaff-34df21542380 | -9.89001 | -47.77906 | 2026-09-15 03:38:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 31649137-83fa-33af-a390-ec316a60a6d1 | -8.8049 | -46.90786 | 2026-09-15 03:38:00 | NOAA-21 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 35adba9a-f9c6-3fd6-bfe2-cfbf9ed6ae40 | -14.76466 | -42.94934 | 2026-09-15 03:38:00 | NOAA-21 | ESPINOSA | MINAS GERAIS | Brasil | 3124302 | 31 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 7e975bc4-3451-3ed0-90e8-d5f10b3215e1 | -9.45567 | -40.39488 | 2026-09-15 03:38:00 | NOAA-21 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 32.5 |
| 1a667b62-2d51-37db-a8c3-1bda6379749c | -11.49693 | -45.75274 | 2026-09-15 03:38:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 30.3 |
| e5ac7632-9ff4-3388-b622-a4a9b8d2ee0f | -8.48407 | -44.58344 | 2026-09-15 03:38:00 | NOAA-21 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 69ab1f68-3954-3365-8e52-d0df4eaabe18 | -13.55567 | -43.52729 | 2026-09-15 03:38:00 | NOAA-21 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| dec0eda3-ed9a-370a-bad3-268c48d46cac | -7.23046 | -46.1553 | 2026-09-15 03:38:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 32a10d55-93b3-3be6-8e1f-eb0d93e5fd44 | -11.49695 | -45.7841 | 2026-09-15 03:38:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ea292f4d-124a-3235-a541-6c45ae744f73 | -8.29136 | -41.35804 | 2026-09-15 03:38:00 | NOAA-21 | PAULISTANA | PIAUÍ | Brasil | 2207801 | 22 | 33 | nan | nan | nan | Caatinga | 4.5 |
| 4a20a74c-8b68-3a0d-87c4-a3ad5bbf8e04 | -12.49093 | -41.41384 | 2026-09-15 03:38:00 | NOAA-21 | LENÇÓIS | BAHIA | Brasil | 2919306 | 29 | 33 | nan | nan | nan | Caatinga | 2.8 |
| f0452e6a-9f64-3c6f-a76d-67f4c46ba7d5 | -14.76929 | -42.94741 | 2026-09-15 03:38:00 | NOAA-21 | ESPINOSA | MINAS GERAIS | Brasil | 3124302 | 31 | 33 | nan | nan | nan | Caatinga | 4.7 |
| 5b558686-3fa4-33a1-a99d-ec0dad7324be | -13.57281 | -47.8939 | 2026-09-15 03:38:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 4.7 |
| a8908e40-a620-348c-8fc2-cd859a0b7302 | -7.24324 | -46.15802 | 2026-09-15 03:38:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 13.4 |
| 0c325203-019f-3123-9133-ceb1eba828cb | -8.39691 | -42.21721 | 2026-09-15 03:38:00 | NOAA-21 | SÃO JOÃO DO PIAUÍ | PIAUÍ | Brasil | 2210003 | 22 | 33 | nan | nan | nan | Caatinga | 3.5 |
| 48c1e1b8-c259-3bc8-864e-294048126709 | -7.21387 | -46.14319 | 2026-09-15 03:38:00 | NOAA-21 | NOVA COLINAS | MARANHÃO | Brasil | 2107258 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 7ef8f8ed-b1f8-3301-838e-e0232e8c760e | -11.19027 | -42.81247 | 2026-09-15 03:38:00 | NOAA-21 | GENTIO DO OURO | BAHIA | Brasil | 2911303 | 29 | 33 | nan | nan | nan | Caatinga | 3.2 |
| 5be7061b-5982-3b04-92e5-978ec09c8371 | -14.20087 | -47.42804 | 2026-09-15 03:38:00 | NOAA-21 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 16.2 |
| c9a25b31-3573-3aa7-8092-107d2c2cacc7 | -13.43851 | -43.82223 | 2026-09-15 03:38:00 | NOAA-21 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c768bfce-2226-312d-8643-d3fe7af8635c | -11.245 | -43.44552 | 2026-09-15 03:38:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 7de2a012-3502-386c-a009-b18f03065acc | -8.48563 | -44.5832 | 2026-09-15 03:38:00 | NOAA-21 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 3.3 |


[Clique aqui para ver as próximas entradas](README21.md)
