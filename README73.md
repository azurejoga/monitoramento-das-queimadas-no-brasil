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
| 4ef91069-4038-3294-9cf6-fb1e4f3865f9 | -10.06287 | -44.21844 | 2024-10-14 04:44:00 | NPP-375D | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 5b8b9333-c6ad-360f-84b7-029a7e99fe00 | -10.06274 | -44.25503 | 2024-10-14 04:44:00 | NPP-375D | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 18.0 |
| f6bfbccf-309c-32f2-a376-a5b9e499dbd6 | -10.06217 | -44.2236 | 2024-10-14 04:44:00 | NPP-375D | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 09f90969-ac63-30f6-a783-6b1da0a906a4 | -10.05896 | -44.17546 | 2024-10-14 04:44:00 | NPP-375D | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 26282d9d-2887-37a7-8f82-55d85a79b920 | -10.0588 | -44.21257 | 2024-10-14 04:44:00 | NPP-375D | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 55a3d694-5e6a-3753-97b8-3d850e4b4c2d | -10.05348 | -44.1799 | 2024-10-14 04:44:00 | NPP-375D | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| b9bd5ace-21c0-3e35-8259-5e14d09ebd98 | -10.05276 | -44.1852 | 2024-10-14 04:44:00 | NPP-375D | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 3fc86eae-900a-36ac-8244-a6c52866228b | -10.05206 | -44.19038 | 2024-10-14 04:44:00 | NPP-375D | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 3ddc2e65-1a09-3e9f-a5e6-8ed7d3cbdd0f | -10.04798 | -44.18447 | 2024-10-14 04:44:00 | NPP-375D | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 3.8 |
| efb0901b-ef3c-3997-8762-b042ced4134a | -10.04727 | -44.18971 | 2024-10-14 04:44:00 | NPP-375D | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 1e7085b8-c6a4-3050-b7ce-52b2137037cf | -10.04657 | -44.19489 | 2024-10-14 04:44:00 | NPP-375D | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 4bed0098-802e-32f7-ba44-5d4bb2bc7527 | -10.04587 | -44.20008 | 2024-10-14 04:44:00 | NPP-375D | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| c2e2854c-bf01-347a-9a9a-41d18018e46d | -10.04517 | -44.20527 | 2024-10-14 04:44:00 | NPP-375D | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 67d61c6c-143a-3718-b99d-4642eaa8558a | -3.43145 | -43.07157 | 2024-10-14 04:44:00 | NPP-375D | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 8ad929f8-f08a-3e3c-9aaf-5c4bea5ac54c | -3.42677 | -43.07082 | 2024-10-14 04:44:00 | NPP-375D | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 08a42d93-1ece-3081-aa1f-831affc6afc6 | -3.314 | -44.18666 | 2024-10-14 04:44:00 | NPP-375D | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 21625314-59d3-3503-a9b3-47338bcc6bf3 | -3.93253 | -43.14572 | 2024-10-14 04:44:00 | NPP-375D | BURITI | MARANHÃO | Brasil | 2102200 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 0b8f9e48-1754-3f36-9db9-05a47ab07fb0 | -3.93181 | -43.15065 | 2024-10-14 04:44:00 | NPP-375D | BURITI | MARANHÃO | Brasil | 2102200 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 84f25f4e-5409-323d-9534-4643342ec506 | -3.93079 | -43.1489 | 2024-10-14 04:44:00 | NPP-375D | BURITI | MARANHÃO | Brasil | 2102200 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 9e6e1a0f-e3e3-3d2b-9385-7d4256290ba4 | -3.92783 | -43.14502 | 2024-10-14 04:44:00 | NPP-375D | BURITI | MARANHÃO | Brasil | 2102200 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 67a6ddec-cd7a-3685-b301-3d8e1cea3a27 | -3.92685 | -43.14327 | 2024-10-14 04:44:00 | NPP-375D | BURITI | MARANHÃO | Brasil | 2102200 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 8147e9a9-6c8f-323d-878a-a95c1cbe4a1b | -3.92313 | -43.14429 | 2024-10-14 04:44:00 | NPP-375D | BURITI | MARANHÃO | Brasil | 2102200 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 2b76bcb6-a1af-3b80-b848-a0e3dc6d3e55 | -3.92215 | -43.14256 | 2024-10-14 04:44:00 | NPP-375D | BURITI | MARANHÃO | Brasil | 2102200 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 9fc423f8-ec9d-39cb-a60f-aeb2bd099e52 | -4.04289 | -44.28619 | 2024-10-14 04:44:00 | NPP-375D | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 83cf2b57-42c5-37e4-a885-a2dafb3ffe12 | -4.03854 | -44.28558 | 2024-10-14 04:44:00 | NPP-375D | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 2d013f88-43ff-3401-b3fb-2293e28d74db | -3.94945 | -44.43911 | 2024-10-14 04:44:00 | NPP-375D | SÃO MATEUS DO MARANHÃO | MARANHÃO | Brasil | 2111508 | 21 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 6681704d-7fa6-3513-a096-ac7da012cce9 | -6.39462 | -44.83152 | 2024-10-14 04:44:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 0b8403b9-c061-387b-a432-ac140f54deaa | -6.39404 | -44.83553 | 2024-10-14 04:44:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |
| bbc2248e-c11b-3eb4-8fca-b56cf888da53 | -6.39026 | -44.83102 | 2024-10-14 04:44:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |
| eaed3c72-36d3-3b44-8b11-5d3cd991b8f0 | -6.38967 | -44.8351 | 2024-10-14 04:44:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 7e91adbd-9c33-32b0-9330-7db1988ba713 | -6.38853 | -44.84305 | 2024-10-14 04:44:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 329b8226-c2f2-32f8-a6ce-b9436ce58d4b | -6.38417 | -44.84257 | 2024-10-14 04:44:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 11.2 |
| 60679096-73c7-36b0-bd03-a5efd278ccaf | -6.3836 | -44.8466 | 2024-10-14 04:44:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| d33335da-fac0-37d7-8f4a-b8033ac25d04 | -6.37923 | -44.84617 | 2024-10-14 04:44:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 76e87533-c89a-3af4-9bd8-75d041a2cbc6 | -6.37865 | -44.85026 | 2024-10-14 04:44:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| fa2c0853-c9a8-31b0-95f6-094633dac2a5 | -6.37055 | -44.08674 | 2024-10-14 04:44:00 | NPP-375D | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| aa4b426d-6d8f-3aa9-849d-55616a523c97 | -6.37006 | -44.08846 | 2024-10-14 04:44:00 | NPP-375D | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 4.6 |
| ab9acb6b-6e67-3ad8-90ef-a1862390ab1c | -6.3698 | -44.09178 | 2024-10-14 04:44:00 | NPP-375D | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 8b6627e6-2603-3b8a-96eb-4beed8fd7641 | -6.3587 | -44.48975 | 2024-10-14 04:44:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 01e9f4e0-79b0-34ae-a259-421759d459b6 | -6.32035 | -44.26945 | 2024-10-14 04:44:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 3281015f-3ad8-328f-8768-1c5888bddbb1 | -6.26422 | -44.08094 | 2024-10-14 04:44:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 8.6 |
| 952a86d6-50a9-313c-b3b1-c17c3541768e | -6.26416 | -44.07777 | 2024-10-14 04:44:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 0fd9c798-ec73-3d91-9523-f8e5fa364e58 | -6.26348 | -44.08235 | 2024-10-14 04:44:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| a2211fd4-aeac-3d87-a32d-0efa7faccba0 | -6.26028 | -44.07579 | 2024-10-14 04:44:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 44378efa-bf8c-3855-b35b-798f297eaa43 | -6.25959 | -44.07719 | 2024-10-14 04:44:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 927e316e-3df5-3a88-ab17-6c69535fddde | -6.22057 | -44.21553 | 2024-10-14 04:44:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 18ea4b0d-d5da-3b62-a58a-47ca926a6b35 | -6.21067 | -44.09331 | 2024-10-14 04:44:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 2df8150c-3be7-3dba-bff5-4e01fc31dfa4 | -6.19864 | -44.17608 | 2024-10-14 04:44:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 40b10763-34c5-3b52-85b3-733dba5d44a9 | -6.1964 | -44.37929 | 2024-10-14 04:44:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 72448169-dd0a-3dd2-ab49-8cbf2f377811 | -6.19349 | -44.17977 | 2024-10-14 04:44:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 3ae9373f-0ea6-3cea-9a5c-3d621c21e26c | -6.17324 | -44.59637 | 2024-10-14 04:44:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| f9769d50-915b-3f77-bd8e-6d325aec884d | -6.17312 | -44.59722 | 2024-10-14 04:44:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 18ec14e1-dd04-33be-9cef-bd690b04e00a | -6.17265 | -44.60061 | 2024-10-14 04:44:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 4b8b4ca4-c134-3358-a938-cb76b5430202 | -6.17249 | -44.60144 | 2024-10-14 04:44:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 3bd2b459-3b17-3c36-a334-57c6d4cb9afe | -6.17157 | -44.10682 | 2024-10-14 04:44:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| a931ff3d-888a-3a40-9577-a5b7f1984bd3 | -6.16872 | -44.59659 | 2024-10-14 04:44:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 35824c40-3b61-301e-b7e0-cd77c3798b25 | -6.1681 | -44.60081 | 2024-10-14 04:44:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 2ffbbc8a-ec10-3a56-bffd-17b3f46b4511 | -6.14915 | -44.45352 | 2024-10-14 04:44:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 314fa90a-b4bd-3047-8dad-0fa025bf4895 | -6.08976 | -44.86086 | 2024-10-14 04:44:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| eb15c1d9-cd41-3577-b15a-0f9cc0418042 | -6.08916 | -44.86498 | 2024-10-14 04:44:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 86d70cd6-c467-39d6-871d-4d34c199f70c | -6.08042 | -44.83424 | 2024-10-14 04:44:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 8bada6b2-4d3b-38fa-bd27-414d2fbdc40d | -6.05371 | -44.80512 | 2024-10-14 04:44:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 9b8d0519-40c7-344b-8fce-044706cdfeac | -6.05313 | -44.80922 | 2024-10-14 04:44:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 5.8 |
| baf63acc-563a-3e3c-855e-4bd1b3865988 | -6.02682 | -44.30711 | 2024-10-14 04:44:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| f7ed0466-4339-3739-9ed5-3d5beec37ad8 | -5.89166 | -44.95422 | 2024-10-14 04:44:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 5bb25df4-4d95-3aee-b630-bb4899f70b48 | -7.8369 | -44.00035 | 2024-10-14 04:44:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 3.1 |
| c7272421-fbc8-30a0-b6df-d307575b3654 | -5.89108 | -44.95814 | 2024-10-14 04:44:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 980faf08-2132-346a-99e8-c8c9c15b30c5 | -5.88854 | -44.3151 | 2024-10-14 04:44:00 | NPP-375D | JATOBÁ | MARANHÃO | Brasil | 2105450 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 6afea9a3-0e1f-3b63-bb1c-05ad10e6fb55 | -5.87339 | -44.04174 | 2024-10-14 04:44:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f350a86d-5e7e-3cde-b140-c346289c7970 | -5.87273 | -44.04634 | 2024-10-14 04:44:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 6.0 |
| c04a7ae6-b05b-328c-b741-4d61eaffdf5c | -5.86819 | -44.04567 | 2024-10-14 04:44:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 9dbca762-5684-39a7-b8dd-aa66598193f2 | -5.77089 | -44.50145 | 2024-10-14 04:44:00 | NPP-375D | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 1d4d84eb-e9cf-3ccf-bd6a-d003c7344a41 | -5.75735 | -44.06816 | 2024-10-14 04:44:00 | NPP-375D | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 62cb18f7-e01b-3386-893b-90b3f0254f4b | -5.59157 | -44.89238 | 2024-10-14 04:44:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 14b7e2c4-4d8b-30b9-b158-8ba80b17d4b1 | -5.5867 | -44.8957 | 2024-10-14 04:44:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 743b6833-ceac-32d7-8945-78b70cc98b02 | -5.52277 | -44.64168 | 2024-10-14 04:44:00 | NPP-375D | SANTA FILOMENA DO MARANHÃO | MARANHÃO | Brasil | 2109759 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 4f77deb3-1170-39e5-94af-ce9e262d25a5 | -5.35376 | -44.41524 | 2024-10-14 04:44:00 | NPP-375D | PRESIDENTE DUTRA | MARANHÃO | Brasil | 2109106 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e1c40f1c-738c-3d71-a243-7f2f6156c936 | -5.32339 | -44.5281 | 2024-10-14 04:44:00 | NPP-375D | PRESIDENTE DUTRA | MARANHÃO | Brasil | 2109106 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d3468b88-7f99-3645-9490-7a1423fa3b4b | -5.3196 | -44.83418 | 2024-10-14 04:44:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 747eb46e-3e33-3b7a-8d5b-81f091dfa198 | -5.19708 | -44.75551 | 2024-10-14 04:44:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 667a6daf-12e1-3697-b3f2-4aa2bb9810a8 | -5.1965 | -44.75952 | 2024-10-14 04:44:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 272de9b2-7ad5-3dc1-bcb1-96c2c4f79a6c | -5.19592 | -44.76351 | 2024-10-14 04:44:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| d232165a-b532-3c44-b293-0b3683d9c160 | -5.19436 | -44.75954 | 2024-10-14 04:44:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 06456dd3-e5ad-329d-8aaa-81c885eda8bb | -5.19376 | -44.76353 | 2024-10-14 04:44:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 0b9a8a29-6450-3893-9dca-0dd6c61dee2c | -5.19222 | -44.75888 | 2024-10-14 04:44:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 4eddfc22-94d1-3bd4-92ff-017898570bc0 | -5.19164 | -44.76285 | 2024-10-14 04:44:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 2066a93e-a2a8-3ed5-8d09-8d0abd414960 | -5.09813 | -44.81927 | 2024-10-14 04:44:00 | NPP-375D | JOSELÂNDIA | MARANHÃO | Brasil | 2105609 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 85ef91e9-91b8-361e-881d-af823774a9ee | -5.09387 | -44.81864 | 2024-10-14 04:44:00 | NPP-375D | JOSELÂNDIA | MARANHÃO | Brasil | 2105609 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 5977675f-ee66-36be-b284-d75441ed4895 | -7.95825 | -44.49269 | 2024-10-14 04:44:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 73d7d39e-2f8a-38b5-bebe-492668d712f5 | -7.90709 | -44.51971 | 2024-10-14 04:44:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 85d08111-1351-36c1-b0c1-00ccf1604d01 | -7.86181 | -43.99374 | 2024-10-14 04:44:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 788f70a2-dd89-315a-a143-999ace4c29ab | -7.85785 | -43.98786 | 2024-10-14 04:44:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 7f52d2fe-34a1-3eb7-89db-9465b18c9502 | -7.84089 | -44.00603 | 2024-10-14 04:44:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 2d36a920-8a09-3858-945d-22031830084a | -7.83762 | -43.99525 | 2024-10-14 04:44:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 2e357f7e-b750-3706-b6d0-1ba85ace5f60 | -7.76486 | -44.54017 | 2024-10-14 04:44:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 8c85c60b-7dea-3e15-94ca-466af61f5218 | -7.76426 | -44.54437 | 2024-10-14 04:44:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 8b0a0de3-d8db-3514-91d4-8e0e36869dcc | -7.75971 | -44.54396 | 2024-10-14 04:44:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 706f459e-ea29-3145-aadc-ff8d20c37cdb | -7.65088 | -44.68016 | 2024-10-14 04:44:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 174ba239-4e4b-3012-99c9-3f733c7d67de | -7.64703 | -44.67524 | 2024-10-14 04:44:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 17f76988-2808-3f67-b6d2-478f5c906000 | -7.64641 | -44.67955 | 2024-10-14 04:44:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |


[Clique aqui para ver as próximas entradas](README74.md)
