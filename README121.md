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

## Dados Diários - Página 121

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| fb5ca7d6-f759-3ea9-9686-375f496b130c | -6.47143 | -55.94802 | 2026-08-28 17:28:00 | NPP-375 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 9.3 |
| f947de42-6dd9-3361-8433-aa894f40bb46 | -5.9336 | -55.67489 | 2026-08-28 17:28:00 | NPP-375 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 36.2 |
| 08487765-fb2e-3008-a3e0-f1e91be146b3 | -8.59062 | -54.79037 | 2026-08-28 17:28:00 | NPP-375 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 43.2 |
| e43d6808-a554-3283-904b-aed49d24ead8 | -6.51153 | -55.24003 | 2026-08-28 17:28:00 | NPP-375 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| cbb64ed6-b16b-3c53-a770-160faca679e8 | -4.14864 | -60.75994 | 2026-08-28 17:28:00 | NPP-375 | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 87.1 |
| 46039f49-169f-336e-851a-e50c65402ae6 | -5.21475 | -49.18018 | 2026-08-28 17:28:00 | NPP-375 | NOVA IPIXUNA | PARÁ | Brasil | 1504976 | 15 | 33 | nan | nan | nan | Amazônia | 21.9 |
| fdf84d50-9ae4-35ff-89a5-1cb01e3efc45 | -7.28542 | -49.95872 | 2026-08-28 17:28:00 | NPP-375 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 7.5 |
| caed4d6f-e555-32fa-bb79-059187f6c20f | -4.0572 | -60.64382 | 2026-08-28 17:28:00 | NPP-375 | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 3d0e3c9d-7305-33e3-94d1-73b0a6e5f594 | -6.50821 | -53.60271 | 2026-08-28 17:28:00 | NPP-375 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 34.0 |
| 14ff408d-ba55-36bb-99ed-37ceb34b258a | -10.58218 | -57.48241 | 2026-08-28 17:28:00 | NPP-375 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 10.0 |
| 15796626-d0c7-3091-85a5-71bc260552c3 | -5.7983 | -57.6353 | 2026-08-28 17:28:00 | NPP-375 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 45979b8e-86b0-3702-afd4-df7800670936 | -6.40159 | -56.06121 | 2026-08-28 17:28:00 | NPP-375 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 4299ab3e-606a-3445-a9f5-f03866bb07d9 | -10.75846 | -54.04425 | 2026-08-28 17:28:00 | NPP-375 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 21.1 |
| 35bae1c4-f4d0-3592-884b-65fa8e5a069c | -6.33147 | -57.74569 | 2026-08-28 17:28:00 | NPP-375 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 16.7 |
| 2b3dedc8-01b7-3bf7-9f8f-198fd51b0f5e | -7.49165 | -55.28586 | 2026-08-28 17:28:00 | NPP-375 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 3f7aa747-aaf2-386a-994f-a5fbafec7d35 | -7.447 | -65.42322 | 2026-08-28 17:28:00 | NPP-375 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 16.0 |
| 2e6c7b8d-1a7b-3994-acd1-f53876d4397f | -9.40339 | -51.63351 | 2026-08-28 17:28:00 | NPP-375 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 13.1 |
| bd362d86-0e05-3552-8875-6208deb450e2 | -6.24031 | -55.40304 | 2026-08-28 17:28:00 | NPP-375 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| a1979c27-8c3d-3ee6-b586-5430b685bef9 | -8.99518 | -65.45536 | 2026-08-28 17:28:00 | NPP-375 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 412b94d8-e2d5-30ce-9ee5-0ccfa0016f4c | -9.62891 | -48.26775 | 2026-08-28 17:28:00 | NPP-375 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 11.9 |
| 65620a3d-5235-37ca-959e-ffe4ad7f4e3d | -7.13359 | -48.06941 | 2026-08-28 17:28:00 | NPP-375 | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| d680241e-8543-3428-bca1-3c638fec782d | -4.45175 | -55.38811 | 2026-08-28 17:28:00 | NPP-375 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 7.4 |
| 6e2fcc70-f1a6-3126-9437-991f303e8cf2 | -6.1156 | -56.1109 | 2026-08-28 17:28:00 | NPP-375 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| c1673265-0c3d-35ee-8494-0a00ae344e42 | -6.83959 | -59.94158 | 2026-08-28 17:28:00 | NPP-375 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 16.4 |
| d7234afa-4ed7-38a4-a055-75b4bdc297c1 | -8.9536 | -69.4674 | 2026-08-28 17:28:00 | NPP-375 | MANOEL URBANO | ACRE | Brasil | 1200344 | 12 | 33 | nan | nan | nan | Amazônia | 7.4 |
| 77a62307-9b84-3430-8254-28003b9e3ce0 | -2.19453 | -48.80804 | 2026-08-28 17:28:00 | NPP-375 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| cd87ecac-67cd-30fb-b456-649b51f9f39e | -6.54627 | -55.2416 | 2026-08-28 17:28:00 | NPP-375 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 113.7 |
| 1c9bcdc7-6c9b-340b-a621-2e97e9a07b36 | -8.83325 | -49.60721 | 2026-08-28 17:28:00 | NPP-375 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 6.8 |
| de8ff55a-8699-33b2-a2df-29c794013109 | -6.17533 | -53.50274 | 2026-08-28 17:28:00 | NPP-375 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 7.6 |
| 3ea5fc61-cdd2-3fbe-87cc-4fecb00c6106 | -8.80744 | -50.04366 | 2026-08-28 17:28:00 | NPP-375 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 10.4 |
| 2c03519c-f64f-358e-9586-57fc36834941 | -4.14927 | -60.76418 | 2026-08-28 17:28:00 | NPP-375 | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 87.1 |
| b5584545-da2a-3e33-9868-4bb61e2cd036 | -6.05447 | -53.88757 | 2026-08-28 17:28:00 | NPP-375 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| b73c35c4-b387-37dd-9e58-c6206db8f9b9 | -2.90621 | -43.76633 | 2026-08-28 17:28:00 | NPP-375 | MORROS | MARANHÃO | Brasil | 2107100 | 21 | 33 | nan | nan | nan | Cerrado | 11.0 |
| e3582064-99cd-3297-8953-f40154ff7f73 | -6.27949 | -53.1452 | 2026-08-28 17:28:00 | NPP-375 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 20.3 |
| 9466b2fc-1e8e-319e-a7ab-9911bc523b65 | -6.83219 | -59.74104 | 2026-08-28 17:28:00 | NPP-375 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 18bd27d3-a184-32c7-98f2-e66cfefb82cb | -6.9321 | -42.71954 | 2026-08-28 17:28:00 | NPP-375 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 15.0 |
| 29fe6af6-a5de-3d1c-9628-e447ff196ac5 | -7.91895 | -61.31591 | 2026-08-28 17:28:00 | NPP-375 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 12.4 |
| 49d69dca-2b75-3472-b72f-07ee79975cd2 | -6.9475 | -58.94341 | 2026-08-28 17:28:00 | NPP-375 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 15.2 |
| 7b33dd6b-3a0a-31a7-9e84-b75d81bf4fae | -7.49448 | -55.28172 | 2026-08-28 17:28:00 | NPP-375 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 1a7180c7-90df-3691-8ea5-58c2b11f582b | -6.745 | -59.17661 | 2026-08-28 17:28:00 | NPP-375 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 12.9 |
| e43883c2-1a17-3303-8a94-5ce640fac27b | -8.5782 | -54.82266 | 2026-08-28 17:28:00 | NPP-375 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 11.0 |
| c584bb61-129f-3b7b-ab0e-826b3d84d99f | -4.34766 | -55.43507 | 2026-08-28 17:28:00 | NPP-375 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 9.3 |
| ca6a4587-958b-3ab7-8ede-b592cde42f9b | -7.59033 | -61.32882 | 2026-08-28 17:28:00 | NPP-375 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 7.0 |
| a62e065a-89bb-3238-a662-ef44854fcc29 | -6.99066 | -60.6637 | 2026-08-28 17:28:00 | NPP-375 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 16.0 |
| 0250ca27-bb06-35ad-8830-3138f822cf79 | -6.69085 | -56.35739 | 2026-08-28 17:28:00 | NPP-375 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 34e860ec-f1ac-3460-bffb-1a9f42ae3d93 | -3.54354 | -54.48607 | 2026-08-28 17:28:00 | NPP-375 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 10.5 |
| f06d1e31-58ae-3c09-9916-be3026827c3c | -8.63343 | -66.54704 | 2026-08-28 17:28:00 | NPP-375 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 7.4 |
| 637cadec-f660-33e6-b35d-e4f7f92761f7 | -8.38238 | -46.60434 | 2026-08-28 17:28:00 | NPP-375 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 4.9 |
| c247baef-3ef0-35d9-8b5a-cc3821c92656 | -8.24871 | -54.99249 | 2026-08-28 17:28:00 | NPP-375 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| b2876708-da93-3dc9-9995-d0bb8fb1c253 | -8.97231 | -54.39984 | 2026-08-28 17:28:00 | NPP-375 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| e46e25d0-1e5b-3f0c-826b-2a9c195944d7 | -4.43618 | -55.62664 | 2026-08-28 17:28:00 | NPP-375 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| bfe232f5-d3e6-3415-ae25-c7a6d3a08f6c | -9.21694 | -51.54571 | 2026-08-28 17:28:00 | NPP-375 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 9.4 |
| 25aec6b6-f367-33a6-8d65-44b0563ad372 | -7.0965 | -55.48235 | 2026-08-28 17:28:00 | NPP-375 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 28.1 |
| 496e9a3e-c89d-396e-b490-c6f98f81299b | -8.14892 | -64.00359 | 2026-08-28 17:28:00 | NPP-375 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 12.9 |
| 39a75e2d-5b38-3bc4-af74-8372d2e41eaa | -4.91516 | -43.46861 | 2026-08-28 17:28:00 | NPP-375 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 4.6 |
| dd655624-ad94-3fa4-965d-b7b6981a307b | -4.31156 | -59.46332 | 2026-08-28 17:28:00 | NPP-375 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 6.7 |
| f1585e91-4b7b-3272-a0df-6af6c4825a65 | -6.69365 | -59.43459 | 2026-08-28 17:28:00 | NPP-375 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 12.3 |
| 1a35fc2f-98f6-3219-8b9e-0788ed98ac58 | -6.75626 | -55.69117 | 2026-08-28 17:28:00 | NPP-375 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 21.4 |
| 9e3cd2fb-34f1-3737-b6f7-7bdee22c396f | -6.93229 | -42.68064 | 2026-08-28 17:28:00 | NPP-375 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 6.1 |
| 13c341c5-d6c8-39c1-bc2c-98dc05fdee3f | -6.57967 | -56.53888 | 2026-08-28 17:28:00 | NPP-375 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 7.7 |
| 299e0d73-315f-3712-acd5-888c4f893b24 | -8.0164 | -48.01913 | 2026-08-28 17:28:00 | NPP-375 | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 1d568555-5f66-3929-8a1c-7d73e3363c35 | -6.00015 | -57.67548 | 2026-08-28 17:28:00 | NPP-375 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 707f5c7a-ad45-307a-b305-592c08465a30 | -9.22027 | -59.67146 | 2026-08-28 17:28:00 | NPP-375 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 394b85f2-65f3-3dba-a66c-45f53a818711 | -10.17869 | -54.22035 | 2026-08-28 17:28:00 | NPP-375 | MATUPÁ | MATO GROSSO | Brasil | 5105606 | 51 | 33 | nan | nan | nan | Amazônia | 10.7 |
| 3d6b0e80-7536-3579-851f-3a761fa018eb | -8.60255 | -54.77714 | 2026-08-28 17:28:00 | NPP-375 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 68.6 |
| 1cdea9ad-8a8d-38c8-b6ed-3337b2aa06de | -6.32866 | -57.74971 | 2026-08-28 17:28:00 | NPP-375 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 05cba1f1-9c78-3fab-ad44-daacc0d78494 | -6.81133 | -59.3811 | 2026-08-28 17:28:00 | NPP-375 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 5.8 |
| f2b631b6-c6d9-3fa9-952e-e9ba04a7147d | -9.41343 | -50.43283 | 2026-08-28 17:28:00 | NPP-375 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 89.9 |
| 119f48ea-6114-3fa6-b261-115fd834172b | -8.66174 | -62.84462 | 2026-08-28 17:28:00 | NPP-375 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 2e2bd40b-a3f0-3560-8868-4785c5056dd1 | -4.31213 | -59.46707 | 2026-08-28 17:28:00 | NPP-375 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 6.7 |
| a44cae98-5a95-3966-9bce-8a499b6dcb03 | -2.99526 | -48.95348 | 2026-08-28 17:28:00 | NPP-375 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 11.7 |
| 52f9cc84-9bcb-3e39-ba07-aea5307e0316 | -8.99174 | -65.42878 | 2026-08-28 17:28:00 | NPP-375 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 14.8 |
| bd5dfeab-6512-3972-af6f-f05ef5866627 | -8.65671 | -62.84091 | 2026-08-28 17:28:00 | NPP-375 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 7.3 |
| 228254ef-549a-367c-b161-ee62c5fa049d | -5.29059 | -50.93576 | 2026-08-28 17:28:00 | NPP-375 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 10.2 |
| 8f205e5c-1640-35b9-bf75-ba44822174bb | -6.34477 | -56.00477 | 2026-08-28 17:28:00 | NPP-375 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 6.8 |
| ec8c722a-36f1-3519-af21-ea5b3bca58a7 | -6.85652 | -59.44309 | 2026-08-28 17:28:00 | NPP-375 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 35.5 |
| 58e34ac6-8ccc-3644-8be7-76750960adc1 | -9.39266 | -60.55172 | 2026-08-28 17:28:00 | NPP-375 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 13.0 |
| 39a05594-c71b-3eda-a6ee-002c4018b77f | -2.90666 | -43.76271 | 2026-08-28 17:28:00 | NPP-375 | MORROS | MARANHÃO | Brasil | 2107100 | 21 | 33 | nan | nan | nan | Cerrado | 11.2 |
| a16f90e1-a2c4-3205-a684-aee86bd58dd8 | -7.62708 | -61.35967 | 2026-08-28 17:28:00 | NPP-375 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 166.5 |
| 060fa980-eec0-39b8-a604-63875df5752f | -10.75922 | -53.98193 | 2026-08-28 17:28:00 | NPP-375 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 20.0 |
| be3eeed3-0125-32e9-aab1-4cb0327b85f7 | -3.93885 | -59.32865 | 2026-08-28 17:28:00 | NPP-375 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 123.6 |
| 4243b1cd-0100-3132-abbf-f663bea05bef | -6.97326 | -59.06815 | 2026-08-28 17:28:00 | NPP-375 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 694dd27e-b3e6-3a47-8c1e-a07c930ace03 | -9.76274 | -64.97232 | 2026-08-28 17:28:00 | NPP-375 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 19.2 |
| 347f1a43-4594-38c1-b723-219ba3ab8c7e | -9.03626 | -69.57619 | 2026-08-28 17:28:00 | NPP-375 | MANOEL URBANO | ACRE | Brasil | 1200344 | 12 | 33 | nan | nan | nan | Amazônia | 5.0 |
| eef86f48-63d1-35f0-8a7f-d616859377c4 | -6.16123 | -57.78592 | 2026-08-28 17:28:00 | NPP-375 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 59.8 |
| 9cb3f6ce-ab4f-3f01-907e-5cc729feec71 | -6.48987 | -56.83487 | 2026-08-28 17:28:00 | NPP-375 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 39eeb77b-6004-39c1-ae5f-28c0a4fa2a2b | -7.28848 | -49.94935 | 2026-08-28 17:28:00 | NPP-375 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 521bcf07-0b3d-36c5-a0ff-498e55109f84 | -6.97303 | -55.62745 | 2026-08-28 17:28:00 | NPP-375 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| deba6499-a3f3-3a4a-a227-f604e13ec381 | -8.0251 | -51.80871 | 2026-08-28 17:28:00 | NPP-375 | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 8d621f87-2b4a-348b-8966-b26fae555afe | -6.03216 | -57.79604 | 2026-08-28 17:28:00 | NPP-375 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| fc64460c-c34d-3b13-b4ad-0ba1d9d13be7 | -9.69642 | -65.07972 | 2026-08-28 17:28:00 | NPP-375 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 6b8b0623-b151-35fa-9f07-b5935b57bd7b | -8.21464 | -54.95341 | 2026-08-28 17:28:00 | NPP-375 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| bb0006c0-43f7-3d53-8071-512cd68c67d4 | -6.41913 | -61.38887 | 2026-08-28 17:28:00 | NPP-375 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 4.0 |
| e975ad7b-c6d4-38af-8e6b-32c77482a1b7 | -8.67723 | -49.54673 | 2026-08-28 17:28:00 | NPP-375 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| b5cfcc6b-87fa-37c0-96e2-e19ed6d63cda | -6.80016 | -59.40278 | 2026-08-28 17:28:00 | NPP-375 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 9.4 |
| 26ff7abf-b201-3d8b-a907-51fe48f1483c | -7.58607 | -57.69416 | 2026-08-28 17:28:00 | NPP-375 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 182f2c8b-c55c-3c6b-b1e6-15a8a8cfabf4 | -8.50593 | -55.34056 | 2026-08-28 17:28:00 | NPP-375 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 8bbf71ab-a24c-3d52-b097-5629a5a45408 | -8.31921 | -47.6316 | 2026-08-28 17:28:00 | NPP-375 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 9937c310-2d3f-39e6-9d46-8442d27f3ad7 | -8.04818 | -45.85744 | 2026-08-28 17:28:00 | NPP-375 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 14.5 |
| 4cd0499e-ff90-358d-8bc0-bf50cdbdc601 | -6.00054 | -57.85831 | 2026-08-28 17:28:00 | NPP-375 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 7.6 |


[Clique aqui para ver as próximas entradas](README122.md)
