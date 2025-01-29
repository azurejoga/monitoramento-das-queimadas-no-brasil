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

## Dados Diários - Página 1

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 49fb4437-83f7-33de-99f7-d33df0d18aed | -9.8379 | -36.480598 | 2025-01-29 00:18:00 | METOP-C | JUNQUEIRO | ALAGOAS | Brasil | 2704005 | 27 | 33 | nan | nan | nan | Mata Atlântica | nan |
| eabd6070-da4f-3275-95e4-29e99b891e59 | -8.11 | -43.126701 | 2025-01-29 00:18:00 | METOP-C | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 3ba9af82-3a1f-375c-8b12-2b2c1ccf8910 | -6.3201 | -43.3633 | 2025-01-29 00:18:00 | METOP-C | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 6bb7869f-8952-3579-962f-a213cecec34c | -3.1015 | -41.867298 | 2025-01-29 00:18:00 | METOP-C | BURITI DOS LOPES | PIAUÍ | Brasil | 2202000 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 2c5bbd80-5320-3736-bbb3-be4d5bf936a0 | -5.9758 | -35.361599 | 2025-01-29 00:18:00 | METOP-C | MACAÍBA | RIO GRANDE DO NORTE | Brasil | 2407104 | 24 | 33 | nan | nan | nan | Caatinga | nan |
| 928d53b4-ff4c-363d-bbf3-de7c3d36f9c8 | -6.2876 | -43.129601 | 2025-01-29 00:18:00 | METOP-C | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 1674440f-bc8d-331a-b4d5-078f1c753414 | -3.5083 | -43.640499 | 2025-01-29 00:18:00 | METOP-C | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| b63388df-44e8-3460-b3b6-b48876801889 | -9.5613 | -38.291401 | 2025-01-29 00:18:00 | METOP-C | PAULO AFONSO | BAHIA | Brasil | 2924009 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| 19cf2a34-9e61-3d2d-8f8b-b7bcfdbfb8c4 | -3.8181 | -43.868999 | 2025-01-29 00:18:00 | METOP-C | VARGEM GRANDE | MARANHÃO | Brasil | 2112704 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| bd141ed7-2735-3188-80b1-725485bbefda | -3.0999 | -41.860298 | 2025-01-29 00:18:00 | METOP-C | BURITI DOS LOPES | PIAUÍ | Brasil | 2202000 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 323bbb9b-f4eb-3be3-9e49-5d6311909dc1 | -8.1132 | -43.1408 | 2025-01-29 00:18:00 | METOP-C | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 86dcb734-8a0a-3f0d-9343-4ed1e91a37bd | -6.5014 | -47.5952 | 2025-01-29 00:18:00 | METOP-C | PALMEIRAS DO TOCANTINS | TOCANTINS | Brasil | 1713809 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 34a434d0-b510-339a-96c5-0538ef41867a | -4.5108 | -38.2701 | 2025-01-29 00:18:00 | METOP-C | BEBERIBE | CEARÁ | Brasil | 2302206 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| f9070dbb-f393-3d67-a55d-7cc2e51d095d | -12.1836 | -41.368198 | 2025-01-29 00:18:00 | METOP-C | LENÇÓIS | BAHIA | Brasil | 2919306 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| 6536d3ad-e47a-3666-bdf5-f8a2101649fa | -5.9723 | -35.347198 | 2025-01-29 00:18:00 | METOP-C | MACAÍBA | RIO GRANDE DO NORTE | Brasil | 2407104 | 24 | 33 | nan | nan | nan | Caatinga | nan |
| cd5f6a26-9f57-3c25-a45d-0663e0d58d8e | -6.5088 | -47.582199 | 2025-01-29 00:18:00 | METOP-C | PALMEIRAS DO TOCANTINS | TOCANTINS | Brasil | 1713809 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 030ddd2c-2451-350c-9120-221d1cf79cd4 | -2.8817 | -48.276501 | 2025-01-29 00:18:00 | METOP-C | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ac5e3b7e-e33e-3a19-b060-c45376181061 | -19.029301 | -39.882099 | 2025-01-29 00:18:00 | METOP-C | JAGUARÉ | ESPÍRITO SANTO | Brasil | 3203056 | 32 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 49a84031-427c-391f-b149-f9f2a1c7997e | -2.8841 | -48.287201 | 2025-01-29 00:18:00 | METOP-C | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 67d46622-cb60-3422-8c21-21b38c33c10a | -6.5112 | -47.593102 | 2025-01-29 00:18:00 | METOP-C | PALMEIRAS DO TOCANTINS | TOCANTINS | Brasil | 1713809 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| df6efb77-aafd-3bf0-8618-b6ec02869e4d | -3.8197 | -43.8759 | 2025-01-29 00:18:00 | METOP-C | VARGEM GRANDE | MARANHÃO | Brasil | 2112704 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| b0288054-db09-3f88-93f6-db44faddcb6a | -3.4985 | -43.6427 | 2025-01-29 00:18:00 | METOP-C | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 421aee8b-9c63-3ddb-b8a4-79849d47917c | -9.5593 | -38.282902 | 2025-01-29 00:18:00 | METOP-C | PAULO AFONSO | BAHIA | Brasil | 2924009 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| 57e2ef12-b5c4-33c1-b429-a7d192b751bc | -3.5099 | -43.6474 | 2025-01-29 00:18:00 | METOP-C | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| bcd0cc07-e3ac-3168-87f4-76d52362fa78 | -9.8353 | -36.469898 | 2025-01-29 00:18:00 | METOP-C | JUNQUEIRO | ALAGOAS | Brasil | 2704005 | 27 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 3161283c-fa97-342a-8855-41e852f2fa50 | -8.1116 | -43.133701 | 2025-01-29 00:18:00 | METOP-C | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 8ff62ec7-4ecf-3386-b1fc-d778da935c1c | -16.30557 | -42.05126 | 2025-01-29 00:20:00 | TERRA_M-M | RUBELITA | MINAS GERAIS | Brasil | 3156502 | 31 | 33 | nan | nan | nan | Mata Atlântica | 7.5 |
| 44b7c40e-b774-377c-b8af-83fe00f433d6 | -17.35476 | -41.71223 | 2025-01-29 00:20:00 | TERRA_M-M | ITAIPÉ | MINAS GERAIS | Brasil | 3132305 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.3 |
| 2dae57a8-e5f8-309b-8f99-1a310c1039e0 | -5.97371 | -35.3519 | 2025-01-29 00:22:00 | TERRA_M-M | MACAÍBA | RIO GRANDE DO NORTE | Brasil | 2407104 | 24 | 33 | nan | nan | nan | Caatinga | 32.0 |
| ee09553d-757d-38dc-ab8b-93433daa2398 | -9.84023 | -36.48666 | 2025-01-29 00:22:00 | TERRA_M-M | JUNQUEIRO | ALAGOAS | Brasil | 2704005 | 27 | 33 | nan | nan | nan | Mata Atlântica | 45.9 |
| 5fc8606d-e05d-3cf0-af77-4703afed8840 | -6.32709 | -43.36619 | 2025-01-29 00:22:00 | TERRA_M-M | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 8.9 |
| 86112c51-b9a3-3a23-9dac-7f167f67b7aa | -9.56624 | -38.28566 | 2025-01-29 00:22:00 | TERRA_M-M | PAULO AFONSO | BAHIA | Brasil | 2924009 | 29 | 33 | nan | nan | nan | Caatinga | 10.4 |
| dc3ef189-0352-3180-b0ef-aa0898feb6a4 | -8.10898 | -43.13192 | 2025-01-29 00:22:00 | TERRA_M-M | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 11.1 |
| 0b77f9b4-7181-3284-8919-8cb7194e3417 | -9.83806 | -36.47246 | 2025-01-29 00:22:00 | TERRA_M-M | JUNQUEIRO | ALAGOAS | Brasil | 2704005 | 27 | 33 | nan | nan | nan | Mata Atlântica | 26.7 |
| 0a4e08ab-a680-3d34-9995-3bbf39f08e3f | -5.97681 | -35.37222 | 2025-01-29 00:22:00 | TERRA_M-M | MACAÍBA | RIO GRANDE DO NORTE | Brasil | 2407104 | 24 | 33 | nan | nan | nan | Caatinga | 18.4 |
| 46f59e74-6a13-3339-98ac-fe918fce0d40 | -12.48657 | -43.79019 | 2025-01-29 00:22:00 | TERRA_M-M | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 7.0 |
| c3593d83-d040-3c97-9b34-b4715d173507 | -12.1877 | -41.36633 | 2025-01-29 00:22:00 | TERRA_M-M | LENÇÓIS | BAHIA | Brasil | 2919306 | 29 | 33 | nan | nan | nan | Caatinga | 9.2 |
| d69ff554-f7e7-368a-a5bb-edce289ce9cf | -3.82558 | -43.86584 | 2025-01-29 00:24:00 | TERRA_M-M | VARGEM GRANDE | MARANHÃO | Brasil | 2112704 | 21 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 4649c0ab-4dc7-3380-9d02-ba01bedcef1c | -4.51808 | -38.27019 | 2025-01-29 00:24:00 | TERRA_M-M | BEBERIBE | CEARÁ | Brasil | 2302206 | 23 | 33 | nan | nan | nan | Caatinga | 12.2 |
| 9ef9704b-5919-3eb6-b9ca-17a634ddb0fd | -3.50912 | -43.64437 | 2025-01-29 00:24:00 | TERRA_M-M | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 14.6 |
| 38f93157-a4e0-310b-9b78-3291c4c45276 | -3.50012 | -43.64562 | 2025-01-29 00:24:00 | TERRA_M-M | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 4.6 |
| a25417bb-3493-3d73-ba36-8cec172bf42f | -3.09827 | -41.87274 | 2025-01-29 00:24:00 | TERRA_M-M | BURITI DOS LOPES | PIAUÍ | Brasil | 2202000 | 22 | 33 | nan | nan | nan | Caatinga | 5.5 |
| 6292b443-7b83-3359-92e9-f3f1bbd5ee26 | -2.88541 | -48.28894 | 2025-01-29 00:24:00 | TERRA_M-M | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 18.3 |
| e857314d-01fc-33e4-a84a-a2676fbab383 | -4.51498 | -38.2771 | 2025-01-29 00:24:00 | TERRA_M-M | BEBERIBE | CEARÁ | Brasil | 2302206 | 23 | 33 | nan | nan | nan | Caatinga | 9.6 |
| eeba61a2-aff4-33d2-8ed7-61f8e5db493b | -5.46536 | -42.92483 | 2025-01-29 00:24:00 | TERRA_M-M | NAZÁRIA | PIAUÍ | Brasil | 2206720 | 22 | 33 | nan | nan | nan | Caatinga | 6.9 |
| d596d81a-4386-34d1-b86d-0ee28c1665b0 | -3.51812 | -43.64314 | 2025-01-29 00:24:00 | TERRA_M-M | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 10.5 |
| dadfcc27-3741-3a1a-83bd-8da0da23d412 | -6.50881 | -47.60013 | 2025-01-29 00:24:00 | TERRA_M-M | PALMEIRAS DO TOCANTINS | TOCANTINS | Brasil | 1713809 | 17 | 33 | nan | nan | nan | Cerrado | 33.6 |
| afcc450a-41e7-3ccc-a592-408cf428cb7f | -6.63373 | -47.85598 | 2025-01-29 00:24:00 | TERRA_M-M | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Cerrado | 19.0 |
| 3101b103-2e95-3cf9-b03d-8cd2e2005397 | -3.09703 | -41.8639 | 2025-01-29 00:24:00 | TERRA_M-M | BURITI DOS LOPES | PIAUÍ | Brasil | 2202000 | 22 | 33 | nan | nan | nan | Caatinga | 8.6 |
| 8975da8a-74af-35bf-95ce-efbd8223fcf8 | -3.82689 | -43.87522 | 2025-01-29 00:24:00 | TERRA_M-M | VARGEM GRANDE | MARANHÃO | Brasil | 2112704 | 21 | 33 | nan | nan | nan | Cerrado | 22.6 |
| e4e439f5-58c6-39c3-99a3-61f1d9190a31 | -20.9053 | -56.527699 | 2025-01-29 00:58:00 | METOP-B | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| a0377938-1ae2-331b-aa36-159121d43a15 | -9.2608 | -60.302502 | 2025-01-29 00:58:00 | METOP-B | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| c28c7661-6747-3d32-ae01-7a62cad27b1a | -15.8025 | -58.509602 | 2025-01-29 00:58:00 | METOP-B | PORTO ESPERIDIÃO | MATO GROSSO | Brasil | 5106828 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| de87adcd-e9ef-3991-a002-7d9bfab005e6 | -15.8008 | -58.501801 | 2025-01-29 00:58:00 | METOP-B | PORTO ESPERIDIÃO | MATO GROSSO | Brasil | 5106828 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 7f3d1150-4bb6-3499-8b64-8fa3ddc5997c | -9.8695 | -36.4591 | 2025-01-29 01:00:00 | GOES-16 | JUNQUEIRO | ALAGOAS | Brasil | 2704005 | 27 | 33 | nan | nan | nan | Mata Atlântica | 94.5 |
| 2733f2cb-5424-39c8-ac03-ecd48cca25ab | -9.87 | -36.4321 | 2025-01-29 01:00:00 | GOES-16 | JUNQUEIRO | ALAGOAS | Brasil | 2704005 | 27 | 33 | nan | nan | nan | Mata Atlântica | 76.0 |
| f133fe89-ff87-372d-9a40-353b78d749f4 | -11.25543 | -60.79638 | 2025-01-29 02:00:00 | TERRA_M-M | ESPIGÃO D'OESTE | RONDÔNIA | Brasil | 1100098 | 11 | 33 | nan | nan | nan | Amazônia | 8.4 |
| d0764584-bf41-3220-9c22-31e3577685d6 | -6.9532 | -43.5384 | 2025-01-29 02:40:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 66.2 |
| 9cf6a5a9-cd67-3c9f-87f6-a38f4709f021 | -6.9532 | -43.5384 | 2025-01-29 03:00:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 68.0 |
| 65b75991-4534-3377-858d-51720a285a17 | -6.9344 | -43.5401 | 2025-01-29 03:00:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 55.5 |
| 208596e6-955e-3433-ab75-89bce5311685 | -6.9344 | -43.5401 | 2025-01-29 03:10:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 68.1 |
| de78526a-915b-3590-8106-85eaf428fca1 | -6.9532 | -43.5384 | 2025-01-29 03:10:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 71.9 |
| 3373858c-2ed1-320a-9969-51e1ecece745 | -3.09993 | -41.86656 | 2025-01-29 03:19:00 | NOAA-20 | BURITI DOS LOPES | PIAUÍ | Brasil | 2202000 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 5933143f-9832-3a75-9265-dc7523004bf2 | -2.92675 | -39.94017 | 2025-01-29 03:19:00 | NOAA-20 | ITAREMA | CEARÁ | Brasil | 2306553 | 23 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 45c11d2f-5927-323b-a48a-d69c607e39bc | -3.41532 | -43.16375 | 2025-01-29 03:19:00 | NOAA-20 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 9a86c152-9b2a-3d8d-949a-436270647c35 | -3.41418 | -43.17031 | 2025-01-29 03:19:00 | NOAA-20 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 68df4ed1-6ae6-32e1-bb88-eae374493892 | -3.09898 | -41.87206 | 2025-01-29 03:19:00 | NOAA-20 | BURITI DOS LOPES | PIAUÍ | Brasil | 2202000 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 807759ff-00f9-3b51-b963-6d61fb6d4b4d | -2.9274 | -39.93618 | 2025-01-29 03:19:00 | NOAA-20 | ITAREMA | CEARÁ | Brasil | 2306553 | 23 | 33 | nan | nan | nan | Caatinga | 3.6 |
| 34bf5037-bdf5-39ed-b666-1898b2625892 | -8.11057 | -43.13889 | 2025-01-29 03:21:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 087f1dac-a23b-3e3d-9711-7574b7ce58b2 | -8.11701 | -43.14014 | 2025-01-29 03:21:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| ae122d63-6e9e-3cca-a726-7e6b4a5edac4 | -5.29854 | -35.99037 | 2025-01-29 03:21:00 | NOAA-20 | PARAZINHO | RIO GRANDE DO NORTE | Brasil | 2408805 | 24 | 33 | nan | nan | nan | Caatinga | 1.0 |
| f3af35a9-3c87-3008-8d20-d523d9fa1995 | -9.56093 | -38.28787 | 2025-01-29 03:21:00 | NOAA-20 | PAULO AFONSO | BAHIA | Brasil | 2924009 | 29 | 33 | nan | nan | nan | Caatinga | 1.8 |
| d7e7e54d-a35a-3975-ab8c-496efce14862 | -8.11598 | -43.14558 | 2025-01-29 03:21:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 14a81a77-dea8-3ba0-ae3c-5ebc6ccb7128 | -8.1116 | -43.13348 | 2025-01-29 03:21:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 7cbecffc-1457-3d01-bd7e-95faaa1e4996 | -9.56005 | -38.29282 | 2025-01-29 03:21:00 | NOAA-20 | PAULO AFONSO | BAHIA | Brasil | 2924009 | 29 | 33 | nan | nan | nan | Caatinga | 2.4 |
| a1be587b-14fb-3381-9d18-aa4824c94394 | -16.87596 | -39.25972 | 2025-01-29 03:23:00 | NOAA-20 | PORTO SEGURO | BAHIA | Brasil | 2925303 | 29 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| e357aabd-71a7-3dd2-9fe8-18ddbe17ea9d | -13.98108 | -41.82764 | 2025-01-29 03:23:00 | NOAA-20 | BRUMADO | BAHIA | Brasil | 2904605 | 29 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 06c35075-98ca-3d42-b582-820c7f1d2bf2 | -13.4103 | -41.34047 | 2025-01-29 03:23:00 | NOAA-20 | IBICOARA | BAHIA | Brasil | 2912202 | 29 | 33 | nan | nan | nan | Caatinga | 2.7 |
| db9b3d54-861f-37bc-980d-d4526e1c3285 | -13.40958 | -41.3441 | 2025-01-29 03:23:00 | NOAA-20 | IBICOARA | BAHIA | Brasil | 2912202 | 29 | 33 | nan | nan | nan | Caatinga | 4.3 |
| a92abdb2-d891-3d75-ba02-66f086b9af2d | -6.9344 | -43.5401 | 2025-01-29 03:30:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 69.6 |
| cd98297c-f425-3f8a-9c5b-bdbd712d2e37 | -6.9532 | -43.5384 | 2025-01-29 03:30:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 77.7 |
| f74288ba-8101-3a3c-9915-a3493ce43023 | -6.9344 | -43.5401 | 2025-01-29 03:40:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 74.9 |
| 402cb928-62a0-3c04-ab5d-d8603c5027b9 | -17.9194 | -40.0833 | 2025-01-29 03:40:00 | GOES-16 | MUCURI | BAHIA | Brasil | 2922003 | 29 | 33 | nan | nan | nan | Mata Atlântica | 108.5 |
| cd37ed98-7491-3ff1-91e1-b91ca790e2c8 | -6.9532 | -43.5384 | 2025-01-29 03:40:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 74.3 |
| 4712fc71-aeef-3c89-8f5f-4175e491a51f | -6.9346 | -43.5168 | 2025-01-29 03:50:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 57.8 |
| 7f1fa6f6-6283-3aea-9582-fda739498eaa | -6.9344 | -43.5401 | 2025-01-29 03:50:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 77.2 |
| cc58b7b7-912c-3a85-890a-a2510ba7a28d | -6.9535 | -43.515 | 2025-01-29 03:50:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 58.2 |
| 8a1f3e3f-0895-36db-99b0-fcfa97f86a5b | -6.9532 | -43.5384 | 2025-01-29 03:50:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 76.0 |
| ea68c2c5-d4ac-30df-98e8-30db59241b1c | -6.9535 | -43.515 | 2025-01-29 04:00:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 60.3 |
| 51facdd8-c46f-3ff8-92cc-c7fd9423e119 | -6.9346 | -43.5168 | 2025-01-29 04:00:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 60.9 |
| 0ef03170-7e03-3697-9670-e96b35cfe9f3 | -6.9532 | -43.5384 | 2025-01-29 04:00:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 98.9 |
| 6b787b72-8692-30ba-826e-c6d5608cb2c4 | -6.9344 | -43.5401 | 2025-01-29 04:00:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 82.7 |
| 06d30681-769a-31df-9cd7-5a0e09d2a1d4 | -6.9535 | -43.515 | 2025-01-29 04:10:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 55.2 |
| d3e81962-a284-3451-b531-d089cc420145 | -6.9346 | -43.5168 | 2025-01-29 04:10:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 61.1 |
| 250a4610-eb50-367e-adae-a7a40696370b | -6.9344 | -43.5401 | 2025-01-29 04:10:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 73.9 |
| 0448b4dd-5548-30b0-b3ec-5a909006e76a | -6.9532 | -43.5384 | 2025-01-29 04:10:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 74.3 |
| 77d36a6e-4bb7-333f-af88-f5a67e659dbc | -3.6112 | -47.31137 | 2025-01-29 04:12:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 939b5457-1143-3591-8865-a360cd728099 | -3.44498 | -42.90279 | 2025-01-29 04:12:00 | NOAA-21 | MILAGRES DO MARANHÃO | MARANHÃO | Brasil | 2106672 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 3b63193a-cae6-3175-9eae-3b6d107ab0b7 | -2.93025 | -39.93441 | 2025-01-29 04:12:00 | NOAA-21 | ITAREMA | CEARÁ | Brasil | 2306553 | 23 | 33 | nan | nan | nan | Caatinga | 8.1 |
| 8ffd1848-af53-39c0-b5e3-ab99403374da | -3.45936 | -43.35331 | 2025-01-29 04:12:00 | NOAA-21 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |


[Clique aqui para ver as próximas entradas](README2.md)
