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

## Dados Diários - Página 3

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| df683262-d5e2-3bee-a3a9-482f40fb1ae6 | -12.3515 | -44.81973 | 2025-05-14 03:32:00 | NPP-375D | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| aa4a7034-34b8-3a57-89df-44a9caa19df5 | -7.89944 | -44.47812 | 2025-05-14 03:32:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 99690f04-3e84-3b2b-a22c-5fc31eb30b9f | -6.60073 | -43.89088 | 2025-05-14 03:32:00 | NPP-375D | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 938786b6-58d0-3c08-aab6-73cd01f0fc66 | -11.78875 | -47.3702 | 2025-05-14 03:32:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 2952f370-4de8-3d19-960b-d7b626d7a25c | -11.79183 | -47.37133 | 2025-05-14 03:32:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| bb79ef26-db5e-3e30-8def-18a927eb7aa1 | -6.59902 | -43.88942 | 2025-05-14 03:32:00 | NPP-375D | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| f9ce9cde-8652-3a29-b893-91c977a9fc3e | -6.60531 | -43.89075 | 2025-05-14 03:32:00 | NPP-375D | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 52d21f30-bfae-300c-a686-00edb1104745 | -11.79333 | -47.36431 | 2025-05-14 03:32:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 610b40f6-38c4-3126-923b-4e6a88429d22 | -11.29259 | -41.86495 | 2025-05-14 03:32:00 | NPP-375D | IRECÊ | BAHIA | Brasil | 2914604 | 29 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 002e1c38-943b-30f8-b0ed-d2ffd492118e | -10.66167 | -44.49126 | 2025-05-14 03:32:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f97d2052-a908-374c-b14e-4cf0150204ac | -7.8976 | -44.48187 | 2025-05-14 03:32:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 405ae818-93bb-3ec4-ba9a-93deba8a1af1 | -6.97455 | -42.78326 | 2025-05-14 03:32:00 | NPP-375D | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| eb6666d0-8a55-34a7-a291-f43cf4089177 | -7.89842 | -44.48347 | 2025-05-14 03:32:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 84bc33a7-d142-3b7b-a0c9-9f1c6e517e1a | -12.35245 | -44.81504 | 2025-05-14 03:32:00 | NPP-375D | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 4f2d5f43-971c-3e06-8505-660596ba04b9 | -10.66103 | -44.49111 | 2025-05-14 03:32:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 136bb9fe-2e78-39f3-9923-65ba335c5eef | -9.74981 | -36.98054 | 2025-05-14 03:32:00 | NPP-375D | TRAIPU | ALAGOAS | Brasil | 2709202 | 27 | 33 | nan | nan | nan | Caatinga | 1.0 |
| c7ff64cb-1089-3b45-9dd4-899fb3c304b0 | -11.79437 | -47.37875 | 2025-05-14 03:32:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| d7d81e1f-3e0c-3b9b-a30a-63dcfcd261c2 | -14.63443 | -45.1101 | 2025-05-14 03:34:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d3902645-9716-366b-a58b-20aaa56cd29f | -14.63349 | -45.11454 | 2025-05-14 03:34:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 13586bf9-b57e-34af-9bd7-080afe0cbaa8 | -13.60779 | -47.38113 | 2025-05-14 03:34:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 65fa90bc-c7f3-3689-b03c-0648d344803e | -13.60728 | -47.38914 | 2025-05-14 03:34:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 76b322d6-3894-38db-8c20-081e4adb8ff4 | -14.62945 | -45.10435 | 2025-05-14 03:34:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 4ad67afb-46cd-3ac2-bae8-4603a6aa0ee2 | -15.2692 | -43.07821 | 2025-05-14 03:34:00 | NPP-375D | MONTE AZUL | MINAS GERAIS | Brasil | 3142908 | 31 | 33 | nan | nan | nan | Caatinga | 5.9 |
| d0f8a4eb-4d48-32e3-bd87-e666c09e9434 | -21.17893 | -43.97956 | 2025-05-14 03:34:00 | NPP-375D | BARROSO | MINAS GERAIS | Brasil | 3105905 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 26a52116-4645-36fd-852d-b03e7eb09fd8 | -14.63629 | -45.10127 | 2025-05-14 03:34:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c0a3010d-c626-3e15-bffd-d9edde6c09db | -14.87279 | -45.11967 | 2025-05-14 03:34:00 | NPP-375D | BONITO DE MINAS | MINAS GERAIS | Brasil | 3108255 | 31 | 33 | nan | nan | nan | Cerrado | 3.1 |
| da3e0a3d-0fe3-3813-a04d-990a26926b36 | -18.62579 | -40.67561 | 2025-05-14 03:34:00 | NPP-375D | VILA PAVÃO | ESPÍRITO SANTO | Brasil | 3205150 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| edf0bec8-7cba-3072-b7b8-37f1004f3e2f | -14.62851 | -45.10879 | 2025-05-14 03:34:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 643c4c34-8dd6-3679-beda-4c619aa6668b | -14.63235 | -45.10685 | 2025-05-14 03:34:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c148d2c9-ae8e-35bc-8708-b21e8933b9dd | -14.63535 | -45.10569 | 2025-05-14 03:34:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| cc5e25b0-c90a-3b98-858a-cac78fd7ed68 | -14.62735 | -45.10108 | 2025-05-14 03:34:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 43abfe39-8208-3792-952c-66f1d8c62322 | -15.26985 | -43.07497 | 2025-05-14 03:34:00 | NPP-375D | MONTE AZUL | MINAS GERAIS | Brasil | 3142908 | 31 | 33 | nan | nan | nan | Caatinga | 5.9 |
| 79235b96-5e0a-33fd-b63b-829de30affcd | -14.63145 | -45.11128 | 2025-05-14 03:34:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 9ed62b58-9ced-3248-8dce-b7eb0781e854 | -14.63941 | -45.11586 | 2025-05-14 03:34:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 4896df6e-b749-3e5b-b0c5-6567ecaffa8d | -13.60872 | -47.38239 | 2025-05-14 03:34:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 4c163e86-0baf-3fc5-b85a-53797f72b909 | -15.27433 | -43.0794 | 2025-05-14 03:34:00 | NPP-375D | MONTE AZUL | MINAS GERAIS | Brasil | 3142908 | 31 | 33 | nan | nan | nan | Caatinga | 5.9 |
| 68e993dd-2569-30c5-a08a-74bc54f5f615 | -14.63325 | -45.10242 | 2025-05-14 03:34:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 0e216c25-12bb-3324-898a-1a4e9c5b9e59 | -14.62644 | -45.1055 | 2025-05-14 03:34:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 1e9a1448-b2fd-3138-9650-b8527376d788 | -15.26854 | -43.08144 | 2025-05-14 03:34:00 | NPP-375D | MONTE AZUL | MINAS GERAIS | Brasil | 3142908 | 31 | 33 | nan | nan | nan | Caatinga | 12.5 |
| fef1e0bd-bb9e-35a8-a7d4-de1fb1293897 | -19.30669 | -44.43472 | 2025-05-14 03:34:00 | NPP-375D | CAETANÓPOLIS | MINAS GERAIS | Brasil | 3109907 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 838d8f7b-2d38-3b1e-b9bf-6c54afc31921 | -17.49965 | -45.17978 | 2025-05-14 03:34:00 | NPP-375D | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 1bd13677-24d6-3cad-8152-0eb49532484d | -13.6064 | -47.38745 | 2025-05-14 03:34:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 127c2236-8200-3383-8a61-d0a4aa26cae6 | -14.63038 | -45.09994 | 2025-05-14 03:34:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 72ef0a25-7d69-30aa-8418-1554ac6f6ca2 | -19.30696 | -44.43475 | 2025-05-14 03:34:00 | NPP-375D | CAETANÓPOLIS | MINAS GERAIS | Brasil | 3109907 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 0179a51d-1db0-3c04-96c0-85405160f4fc | -19.30627 | -44.43811 | 2025-05-14 03:34:00 | NPP-375D | CAETANÓPOLIS | MINAS GERAIS | Brasil | 3109907 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 9fe6729a-d433-3935-b037-5378aa0b36a0 | -14.63415 | -45.098 | 2025-05-14 03:34:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 112f3b36-e9d1-3add-adae-5fbf406aacfa | -22.6958 | -43.34959 | 2025-05-14 03:36:00 | NPP-375D | DUQUE DE CAXIAS | RIO DE JANEIRO | Brasil | 3301702 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| e56722c4-9fcb-327a-9594-68c75d1e6fa9 | -20.81537 | -49.79389 | 2025-05-14 03:36:00 | NPP-375D | MONTE APRAZÍVEL | SÃO PAULO | Brasil | 3531407 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 9992f46f-72ee-303e-b139-478ea5cd1466 | -23.34145 | -46.77276 | 2025-05-14 03:36:00 | NPP-375D | CAIEIRAS | SÃO PAULO | Brasil | 3509007 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| a722c111-af9d-3b4e-9338-e8be4eaa97c4 | -20.81716 | -49.78672 | 2025-05-14 03:36:00 | NPP-375D | MONTE APRAZÍVEL | SÃO PAULO | Brasil | 3531407 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 391ff2ec-96c3-3bc6-8436-b662f2f9fe31 | -23.33591 | -46.77146 | 2025-05-14 03:36:00 | NPP-375D | CAIEIRAS | SÃO PAULO | Brasil | 3509007 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 1383b9fd-b8f4-32f4-a6ed-bf777047a536 | -21.66649 | -48.81524 | 2025-05-14 03:36:00 | NPP-375D | ITÁPOLIS | SÃO PAULO | Brasil | 3522703 | 35 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 35e60cd3-8624-3d40-97b3-140a10bbb999 | -23.33727 | -46.77324 | 2025-05-14 03:36:00 | NPP-375D | CAIEIRAS | SÃO PAULO | Brasil | 3509007 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 61f52803-3621-3d3c-929f-799a72db95f2 | -4.91574 | -41.99887 | 2025-05-14 03:51:00 | NOAA-20 | JATOBÁ DO PIAUÍ | PIAUÍ | Brasil | 2205276 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| d67b6f1a-6695-336f-92b5-8fbe296d3e83 | -6.64625 | -41.99915 | 2025-05-14 03:51:00 | NOAA-20 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| f60f6d76-5cc4-3084-ad45-e8f6d5a750e1 | -6.64698 | -41.99475 | 2025-05-14 03:51:00 | NOAA-20 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 74c2d596-4942-3ba0-b425-97b94565a764 | -5.06855 | -37.71451 | 2025-05-14 03:51:00 | NOAA-20 | BARAÚNA | RIO GRANDE DO NORTE | Brasil | 2401453 | 24 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 2b38ca08-3770-3c84-b631-4ff82e4d837b | -7.23096 | -35.58686 | 2025-05-14 03:51:00 | NOAA-20 | INGÁ | PARAÍBA | Brasil | 2506806 | 25 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 87448e9a-ebab-38a6-8823-c66f04a0ca61 | -6.18875 | -48.0432 | 2025-05-14 03:51:00 | NOAA-20 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| aac4b255-f7fa-39d6-92a8-3a7bd005e6fc | -5.80434 | -43.6169 | 2025-05-14 03:51:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| c4392b7b-d2e3-386d-ba62-59576717ac35 | -6.6055 | -43.88731 | 2025-05-14 03:51:00 | NOAA-20 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| d90979e0-9c48-3ec5-958b-cebff1fc7c99 | -6.60135 | -43.88658 | 2025-05-14 03:51:00 | NOAA-20 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| ad89a321-e985-33ef-9b21-d310966db7cc | -6.33901 | -43.38245 | 2025-05-14 03:51:00 | NOAA-20 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| e99ae7e1-9fc5-3fda-ab6b-9ede85a4a017 | -6.32489 | -43.74717 | 2025-05-14 03:51:00 | NOAA-20 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 0d945c17-1f93-38b7-b18e-ae96650efec7 | -6.64771 | -41.99036 | 2025-05-14 03:51:00 | NOAA-20 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 468c4952-7243-3e29-b115-69c1b0fc6cd6 | -5.76921 | -43.49589 | 2025-05-14 03:51:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 35e3520b-815b-3ae2-b62c-8927262b9cf0 | -6.3255 | -43.74346 | 2025-05-14 03:51:00 | NOAA-20 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 289348a4-0908-3537-839b-a7df7b333dd6 | -5.78242 | -43.62078 | 2025-05-14 03:51:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| d90f0a16-56e8-3775-9bee-90af3cce5f40 | -6.34247 | -43.38663 | 2025-05-14 03:51:00 | NOAA-20 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 5d890b63-3fae-3985-ab98-058ddfd6be05 | -6.60072 | -43.89034 | 2025-05-14 03:51:00 | NOAA-20 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| f0ed20b0-cc95-375f-9f0c-c06ee4c83ca1 | -5.04566 | -37.40557 | 2025-05-14 03:51:00 | NOAA-20 | MOSSORÓ | RIO GRANDE DO NORTE | Brasil | 2408003 | 24 | 33 | nan | nan | nan | Caatinga | 0.8 |
| f3b60fb2-2b78-37c0-93ba-3fcd32316e5c | -5.80181 | -43.61924 | 2025-05-14 03:51:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 20482fa4-3bdb-3cba-bcb7-f1d3be4770f1 | -5.80373 | -43.62064 | 2025-05-14 03:51:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ed7d392c-5cf2-3637-8194-63ce51fada75 | -6.65068 | -41.99538 | 2025-05-14 03:51:00 | NOAA-20 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 3.2 |
| e23790f0-e766-36c2-a846-90d8fce6a958 | -6.19432 | -48.044 | 2025-05-14 03:51:00 | NOAA-20 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| eef61bac-4cab-3f56-a120-3104780a6616 | -5.79959 | -43.6199 | 2025-05-14 03:51:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| cb2735d8-1b73-39fc-a142-5a8b062d44a4 | -6.32288 | -43.74526 | 2025-05-14 03:51:00 | NOAA-20 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| bde8ffda-8777-3a77-95e0-bc37eada2444 | -6.65438 | -41.99602 | 2025-05-14 03:51:00 | NOAA-20 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 3.2 |
| ecc513d8-083d-3c7d-8485-4506e6713c64 | -6.97401 | -42.78051 | 2025-05-14 03:51:00 | NOAA-20 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 39049df9-8f1d-3181-8f49-cde1adf1da92 | -5.78304 | -43.61702 | 2025-05-14 03:51:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| ae14a827-1c76-3a08-8879-89bbd924374a | -6.32074 | -43.74656 | 2025-05-14 03:51:00 | NOAA-20 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 19e41060-6842-3963-81d2-4674b2412242 | -6.97322 | -42.78528 | 2025-05-14 03:51:00 | NOAA-20 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 056203ed-c83c-3239-9788-bca5bcbc66fc | -8.0721 | -34.97778 | 2025-05-14 03:51:00 | NOAA-20 | RECIFE | PERNAMBUCO | Brasil | 2611606 | 26 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| ac977151-cff8-35e2-b57e-5ca75cc95f35 | -9.46133 | -40.32009 | 2025-05-14 03:53:00 | NOAA-20 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 0.7 |
| a6d5daa7-7615-3c70-bb8e-27ca5c33bc01 | -9.46586 | -40.31343 | 2025-05-14 03:53:00 | NOAA-20 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 3830f61b-0973-3715-a068-1c59f924a230 | -9.45913 | -40.31233 | 2025-05-14 03:53:00 | NOAA-20 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 0.9 |
| f19a2aeb-e79b-301d-a36c-e0c04c191840 | -9.46191 | -40.31649 | 2025-05-14 03:53:00 | NOAA-20 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 0.7 |
| f52495ea-eff3-39fc-bf4d-8a1f12180d7e | -7.40871 | -43.45105 | 2025-05-14 03:53:00 | NOAA-20 | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 6a359794-3a28-37c7-b053-3ae06f0ce285 | -10.00793 | -47.83891 | 2025-05-14 03:53:00 | NOAA-20 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 55d8e854-a6ac-3705-b5ee-41fce4a41cb2 | -11.57166 | -47.44331 | 2025-05-14 03:53:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 31358241-b021-3494-80de-9a0bf6cb294a | -11.57064 | -47.44876 | 2025-05-14 03:53:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| cf231e4b-acbe-3a99-bc92-ce19c4dc97d7 | -12.49636 | -44.49559 | 2025-05-14 03:53:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 8a466e94-7bff-356f-b307-1c72560b903e | -12.35104 | -44.81486 | 2025-05-14 03:53:00 | NOAA-20 | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e0bf57d4-73dc-3a87-8412-03c5f0b91740 | -9.47363 | -40.32951 | 2025-05-14 03:53:00 | NOAA-20 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 1c3e79aa-e088-3d0a-bb56-1008782a59dc | -10.17884 | -48.0273 | 2025-05-14 03:53:00 | NOAA-20 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 98b4c511-001d-344c-a73a-d0007eec7c48 | -11.79964 | -44.26715 | 2025-05-14 03:53:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f3d77492-008a-376a-97b5-75279f94d2cf | -9.74963 | -36.97875 | 2025-05-14 03:53:00 | NOAA-20 | TRAIPU | ALAGOAS | Brasil | 2709202 | 27 | 33 | nan | nan | nan | Caatinga | 0.6 |
| a10111b2-7e5f-3679-84a8-072d9c887c1a | -11.80621 | -46.63534 | 2025-05-14 03:53:00 | NOAA-20 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e06ef09c-2494-391d-819f-163d67936d94 | -12.49242 | -44.49488 | 2025-05-14 03:53:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 2e342caa-012a-3e0e-846a-99d23c5efe09 | -11.16629 | -48.67716 | 2025-05-14 03:53:00 | NOAA-20 | BREJINHO DE NAZARÉ | TOCANTINS | Brasil | 1703701 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |


[Clique aqui para ver as próximas entradas](README4.md)
