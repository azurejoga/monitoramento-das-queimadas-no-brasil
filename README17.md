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

## Dados Diários - Página 17

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 6d13f0ef-373a-3a15-9c53-3a601aad1e72 | -17.62383 | -49.33955 | 2025-11-08 04:10:00 | NOAA-21 | MORRINHOS | GOIÁS | Brasil | 5213806 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 55754774-3ed7-3bd5-b85e-d7d7236ee126 | -18.48039 | -53.41028 | 2025-11-08 04:10:00 | NOAA-21 | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 8713ab6d-4a8b-31f4-ad6a-1633d24526ce | -15.79878 | -50.10735 | 2025-11-08 04:10:00 | NOAA-21 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| add042a9-6563-39ed-b574-f77ab16a1fa5 | -14.49036 | -52.14152 | 2025-11-08 04:10:00 | NOAA-21 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 6bee798e-84d3-3060-a220-790a41fe5687 | -14.48973 | -52.14468 | 2025-11-08 04:10:00 | NOAA-21 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 3d153d15-7601-34d9-9ab3-c88823b171a2 | -18.51179 | -53.49249 | 2025-11-08 04:10:00 | NOAA-21 | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 139a3d90-1a02-3227-88d6-09a5144f99fa | -16.09003 | -49.38826 | 2025-11-08 04:10:00 | NOAA-21 | PETROLINA DE GOIÁS | GOIÁS | Brasil | 5216809 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| a877ffd5-0409-3b23-97de-c4d8d315e67e | -18.33594 | -54.27655 | 2025-11-08 04:10:00 | NOAA-21 | COXIM | MATO GROSSO DO SUL | Brasil | 5003306 | 50 | 33 | nan | nan | nan | Cerrado | 0.7 |
| c1e5cea9-04a6-37c7-a6e1-574bb845d132 | -17.62472 | -49.33593 | 2025-11-08 04:10:00 | NOAA-21 | MORRINHOS | GOIÁS | Brasil | 5213806 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 259b7f4f-19e5-3eff-88f1-75b641bdcf25 | -15.76742 | -52.44577 | 2025-11-08 04:10:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 33738a10-8566-3cf0-9f1f-35580138dbeb | -15.14863 | -47.18545 | 2025-11-08 04:10:00 | NOAA-21 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 6c37cc0e-32b6-35f2-99d9-c73611a3dda4 | -18.33436 | -54.28396 | 2025-11-08 04:10:00 | NOAA-21 | COXIM | MATO GROSSO DO SUL | Brasil | 5003306 | 50 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 4e8d0c98-210d-301e-b7ec-332b6ca08baf | -14.67391 | -51.89704 | 2025-11-08 04:10:00 | NOAA-21 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| e1e52984-027f-3db0-9afb-e11117dbb48d | -16.75349 | -51.36532 | 2025-11-08 04:10:00 | NOAA-21 | PALESTINA DE GOIÁS | GOIÁS | Brasil | 5215652 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 81005447-efb7-3a8a-a001-217bd412e530 | -18.33357 | -54.28769 | 2025-11-08 04:10:00 | NOAA-21 | COXIM | MATO GROSSO DO SUL | Brasil | 5003306 | 50 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c54bb5eb-d76e-3a29-acea-83c45b0f4408 | -17.28234 | -47.13702 | 2025-11-08 04:10:00 | NOAA-21 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e9925162-6bc8-3ff7-84e5-cb98f74a5e61 | -15.18769 | -49.51947 | 2025-11-08 04:10:00 | NOAA-21 | RIALMA | GOIÁS | Brasil | 5218607 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 00ec34d5-b969-3f65-8109-9dd465fe9b81 | -15.18457 | -49.52003 | 2025-11-08 04:10:00 | NOAA-21 | RIALMA | GOIÁS | Brasil | 5218607 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 490cd7d1-80e7-3c4b-8ca4-26ec7423668a | -17.62448 | -49.33593 | 2025-11-08 04:10:00 | NOAA-21 | MORRINHOS | GOIÁS | Brasil | 5213806 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 16635451-8e5f-3006-9d48-d324aef7788d | -17.28593 | -47.13773 | 2025-11-08 04:10:00 | NOAA-21 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 26e2f87a-1ca6-314f-8b76-d61e2838c2c2 | -18.33515 | -54.28024 | 2025-11-08 04:10:00 | NOAA-21 | COXIM | MATO GROSSO DO SUL | Brasil | 5003306 | 50 | 33 | nan | nan | nan | Cerrado | 0.7 |
| b8222911-f6d7-33a4-bc8c-eb5e3be55c0b | -19.48078 | -53.9435 | 2025-11-08 04:10:00 | NOAA-21 | CAMAPUÃ | MATO GROSSO DO SUL | Brasil | 5002605 | 50 | 33 | nan | nan | nan | Cerrado | 2.0 |
| bc0a8441-307b-3057-9bc6-9eeb449e6b99 | -3.639 | -43.6544 | 2025-11-08 04:20:00 | GOES-19 | VARGEM GRANDE | MARANHÃO | Brasil | 2112704 | 21 | 33 | nan | nan | nan | Cerrado | 67.8 |
| b55e6563-ee62-3108-a98a-36f4393a6516 | -0.92026 | -47.75115 | 2025-11-08 04:33:00 | NPP-375D | MARAPANIM | PARÁ | Brasil | 1504406 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 76dd50a7-c008-373e-ba90-8017231e7683 | 0.59803 | -51.57653 | 2025-11-08 04:33:00 | NPP-375D | PORTO GRANDE | AMAPÁ | Brasil | 1600535 | 16 | 33 | nan | nan | nan | Amazônia | 0.6 |
| e5512aee-cdf6-31f1-bbe8-4e744138f934 | 3.69692 | -51.292 | 2025-11-08 04:33:00 | NPP-375D | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0e22ca32-501d-3efa-8c2c-2e076b0f5e7d | 3.53152 | -51.77998 | 2025-11-08 04:33:00 | NPP-375D | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 2.4 |
| b9969c3c-3578-318d-8ae1-42b965686b4b | -1.55687 | -45.77779 | 2025-11-08 04:33:00 | NPP-375D | GODOFREDO VIANA | MARANHÃO | Brasil | 2104305 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 264c8129-0681-364a-b351-2552df24ef93 | -1.17615 | -49.27757 | 2025-11-08 04:33:00 | NPP-375D | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 03e76c5c-278c-3e65-b58c-681114351577 | 1.33974 | -50.71258 | 2025-11-08 04:33:00 | NPP-375D | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a6f13b7a-6ce8-3127-ae9b-1a40ae932955 | -0.92362 | -47.75168 | 2025-11-08 04:33:00 | NPP-375D | MARAPANIM | PARÁ | Brasil | 1504406 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 55eea82b-6c49-320d-8071-060161bb57f6 | 0.59391 | -51.57717 | 2025-11-08 04:33:00 | NPP-375D | PORTO GRANDE | AMAPÁ | Brasil | 1600535 | 16 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 232b30f4-b724-3574-91d6-d5a54bb0aad3 | -2.1939 | -48.2256 | 2025-11-08 04:33:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| faadb8c8-393b-303b-97b6-75fe817e8213 | -2.22623 | -48.37007 | 2025-11-08 04:33:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a2bac6bb-09e3-3e32-ae03-d18a55634766 | -1.09916 | -47.51994 | 2025-11-08 04:33:00 | NPP-375D | IGARAPÉ-AÇU | PARÁ | Brasil | 1503200 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7641ee2e-2bcc-391c-b43c-27d081237036 | -1.06804 | -48.09831 | 2025-11-08 04:33:00 | NPP-375D | SANTO ANTÔNIO DO TAUÁ | PARÁ | Brasil | 1507003 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b3dc91bd-5d76-338b-a481-0b6049d3c206 | 0.61539 | -51.56314 | 2025-11-08 04:33:00 | NPP-375D | PORTO GRANDE | AMAPÁ | Brasil | 1600535 | 16 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d20f5adc-751f-3e70-8c19-972e77ecab68 | 3.36903 | -51.28692 | 2025-11-08 04:33:00 | NPP-375D | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 0.6 |
| fe285931-97ec-35a9-b0ac-db81afd981e9 | 0.90206 | -50.75032 | 2025-11-08 04:33:00 | NPP-375D | CUTIAS | AMAPÁ | Brasil | 1600212 | 16 | 33 | nan | nan | nan | Amazônia | 1.1 |
| bba97aab-6623-3c0b-9c7c-fa1950d75c9a | 0.65892 | -51.54488 | 2025-11-08 04:33:00 | NPP-375D | PORTO GRANDE | AMAPÁ | Brasil | 1600535 | 16 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 2abe92b9-4309-36b9-a2a1-621afdf7e246 | -2.26046 | -47.87385 | 2025-11-08 04:33:00 | NPP-375D | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 3c94f12f-bcf0-358d-8dd8-0625e3e675ed | 0.69196 | -51.46163 | 2025-11-08 04:33:00 | NPP-375D | PORTO GRANDE | AMAPÁ | Brasil | 1600535 | 16 | 33 | nan | nan | nan | Amazônia | 0.7 |
| b097b78d-b3f5-3eff-9856-a8a58dd5fb8e | 1.34367 | -50.71197 | 2025-11-08 04:33:00 | NPP-375D | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 82e8f2ec-6597-3e20-9536-dbb7c2cd2561 | 0.90161 | -50.74841 | 2025-11-08 04:33:00 | NPP-375D | CUTIAS | AMAPÁ | Brasil | 1600212 | 16 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 84d6f6e8-cbd9-3a67-9a12-aacc794190a6 | -1.66963 | -47.40232 | 2025-11-08 04:33:00 | NPP-375D | IRITUIA | PARÁ | Brasil | 1503507 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 30381a95-59e5-3fb4-9afd-1cac4f06cc4e | -3.06443 | -40.08237 | 2025-11-08 04:33:00 | NPP-375D | ACARAÚ | CEARÁ | Brasil | 2300200 | 23 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 51fdbbf2-08bb-3c2d-a02a-815319f5c7cc | 0.65949 | -51.54855 | 2025-11-08 04:33:00 | NPP-375D | PORTO GRANDE | AMAPÁ | Brasil | 1600535 | 16 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 0341f017-8891-3779-91c0-5eab3c91fa9f | -2.00828 | -46.2844 | 2025-11-08 04:33:00 | NPP-375D | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 4ef4617b-2e59-3a48-a83c-3f38bd0a5ccd | 1.13139 | -52.38562 | 2025-11-08 04:33:00 | NPP-375D | PEDRA BRANCA DO AMAPARI | AMAPÁ | Brasil | 1600154 | 16 | 33 | nan | nan | nan | Amazônia | 0.7 |
| ed50727a-63d4-370c-8137-762ed20ec453 | -2.09826 | -48.05042 | 2025-11-08 04:33:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| be705a8f-0076-33f1-b887-5d033604916b | -1.1182 | -47.29113 | 2025-11-08 04:33:00 | NPP-375D | PEIXE-BOI | PARÁ | Brasil | 1505601 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 8c71e3c5-6286-3375-8c47-7e4e11a197b3 | -2.09882 | -48.04688 | 2025-11-08 04:33:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| b52817e2-5be6-36db-9182-72fbebded517 | -3.24549 | -41.76252 | 2025-11-08 04:33:00 | NPP-375D | BURITI DOS LOPES | PIAUÍ | Brasil | 2202000 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 771de08d-4dfe-360e-878f-457da702ee15 | -1.19992 | -49.0626 | 2025-11-08 04:33:00 | NPP-375D | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| dc018a0f-7904-3d86-a8de-f904e1c95442 | -2.2599 | -47.87736 | 2025-11-08 04:33:00 | NPP-375D | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b645d5db-15fd-3fde-82de-4eb0cdfcd296 | -2.22566 | -48.37366 | 2025-11-08 04:33:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| bdb62eed-c919-390b-928c-88a9b7635280 | -1.67296 | -47.40284 | 2025-11-08 04:33:00 | NPP-375D | IRITUIA | PARÁ | Brasil | 1503507 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| af323cba-a188-3d0b-bcb9-625f573b6de9 | -1.24303 | -54.14753 | 2025-11-08 04:33:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 952ac5e6-53f4-320a-84ea-ca7b4b06b3cd | 3.36943 | -51.28776 | 2025-11-08 04:33:00 | NPP-375D | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 1a80ba7f-3802-32ed-afbb-0fdc4de6269e | -1.18989 | -49.05416 | 2025-11-08 04:33:00 | NPP-375D | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| cb2eec68-7131-3f23-bb7d-936f2d3da073 | -2.14746 | -48.82106 | 2025-11-08 04:33:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| b005930c-1f9c-3b99-bb7b-277e142d7fac | -0.91971 | -47.75468 | 2025-11-08 04:33:00 | NPP-375D | MARAPANIM | PARÁ | Brasil | 1504406 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 56bdea6d-c53d-3c77-aa25-642edd443a70 | 1.19628 | -50.78959 | 2025-11-08 04:33:00 | NPP-375D | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 89588084-80c1-3194-bb2a-045e7c22a730 | -1.17678 | -49.27365 | 2025-11-08 04:33:00 | NPP-375D | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 9a935ed4-c00d-3b73-81cb-8fd4b70b27fd | -1.50508 | -47.15321 | 2025-11-08 04:33:00 | NPP-375D | OURÉM | PARÁ | Brasil | 1505403 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 360f0ba9-ceef-35b4-acd7-c332afd931f7 | -1.25686 | -47.8936 | 2025-11-08 04:33:00 | NPP-375D | CASTANHAL | PARÁ | Brasil | 1502400 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| bf0e4635-bd65-3d32-a828-bfcda43c1a3c | 1.34073 | -50.71445 | 2025-11-08 04:33:00 | NPP-375D | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c461d47d-db23-3f87-a912-4fa50187256e | -3.64162 | -44.23409 | 2025-11-08 04:36:00 | NPP-375D | CANTANHEDE | MARANHÃO | Brasil | 2102705 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 724310a0-994d-3ad1-9ea1-140ab832d9b3 | -7.3191 | -47.3854 | 2025-11-08 04:36:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ce9c6cf0-deea-307d-8990-03d22bd8c1c1 | -5.90985 | -44.52893 | 2025-11-08 04:36:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| a2da323f-4700-3276-b9bd-65ff65780c8b | -4.64439 | -47.95296 | 2025-11-08 04:36:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 13.3 |
| 447ebb07-80a2-371f-91e5-7013f5538615 | -4.40783 | -42.3264 | 2025-11-08 04:36:00 | NPP-375D | CABECEIRAS DO PIAUÍ | PIAUÍ | Brasil | 2202059 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 2edb1f4a-c9b8-3159-b904-5004abfe66ba | -3.84758 | -49.81192 | 2025-11-08 04:36:00 | NPP-375D | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 9fde2fb4-f356-3d50-96c2-62658144f036 | -3.25033 | -50.13887 | 2025-11-08 04:36:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 825906dc-b90e-3153-986c-abd69db0493d | -3.1335 | -49.10261 | 2025-11-08 04:36:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| c5e9c188-25ca-35ac-83a8-2f41d1264350 | -2.7886 | -50.31721 | 2025-11-08 04:36:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c47246f8-0b23-3d22-8958-842319c57c01 | -2.46354 | -49.37501 | 2025-11-08 04:36:00 | NPP-375D | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 5a295ed5-901f-3926-959d-97c34863e8be | -6.36822 | -41.74021 | 2025-11-08 04:36:00 | NPP-375D | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 9e2117e8-3385-3034-a5fb-4deb66f2a95d | -5.35447 | -45.80637 | 2025-11-08 04:36:00 | NPP-375D | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 5722634b-870a-3c16-9a1a-d994b95c392d | -3.44428 | -46.18899 | 2025-11-08 04:36:00 | NPP-375D | GOVERNADOR NEWTON BELLO | MARANHÃO | Brasil | 2104651 | 21 | 33 | nan | nan | nan | Amazônia | 2.3 |
| e90a510c-e3fd-3969-988d-e30116237c17 | -1.69975 | -54.66899 | 2025-11-08 04:36:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| f096def8-60d8-37e8-a7df-af1542c841ac | -3.34013 | -50.20751 | 2025-11-08 04:36:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 35a1d127-0499-346f-90a6-8b8755abe5d1 | -3.44506 | -43.15703 | 2025-11-08 04:36:00 | NPP-375D | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 74829b56-bdc5-3626-b7a8-60570f0e8675 | -4.35809 | -50.67364 | 2025-11-08 04:36:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 22f3b424-29e5-3c6b-a66c-b61cdefc87c0 | -3.34798 | -50.20455 | 2025-11-08 04:36:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 7db94412-12f4-3d08-9e98-55b3006ede63 | -3.42393 | -50.04012 | 2025-11-08 04:36:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 98e61047-4732-32a7-9a4e-66e090fb775b | -3.83642 | -49.81413 | 2025-11-08 04:36:00 | NPP-375D | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| e2826fed-fa46-3fa4-85b9-89b8bbe65d00 | -3.76656 | -44.28951 | 2025-11-08 04:36:00 | NPP-375D | MATÕES DO NORTE | MARANHÃO | Brasil | 2106631 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 637b765b-7b50-35a2-8b01-6667433e79e0 | -3.67434 | -50.49489 | 2025-11-08 04:36:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ee784db6-0244-324c-9f9b-418abcca8e2f | -3.09083 | -50.31863 | 2025-11-08 04:36:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| ec93ba6c-3587-3322-b76e-b38b538acd56 | -6.33437 | -41.69654 | 2025-11-08 04:36:00 | NPP-375D | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| b0d91014-0f00-3445-9645-fef71cebf487 | -7.08898 | -48.31236 | 2025-11-08 04:36:00 | NPP-375D | CARMOLÂNDIA | TOCANTINS | Brasil | 1703883 | 17 | 33 | nan | nan | nan | Amazônia | 1.8 |
| eb937291-4212-3ace-81cd-987262bae9a1 | -2.86873 | -50.73127 | 2025-11-08 04:36:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 05e0911f-8694-35cc-8a46-623133c6e739 | -4.2773 | -46.40099 | 2025-11-08 04:36:00 | NPP-375D | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 7379e087-4d4b-3bf0-868d-b1c4ca1f5b8c | -5.60274 | -37.35656 | 2025-11-08 04:36:00 | NPP-375D | UPANEMA | RIO GRANDE DO NORTE | Brasil | 2414605 | 24 | 33 | nan | nan | nan | Caatinga | 0.9 |
| d900b6db-173d-3f2c-9845-a4b7e372225c | -2.45655 | -49.37391 | 2025-11-08 04:36:00 | NPP-375D | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 12.9 |
| a5b4a5ab-1d0a-3fa2-a428-dcd8e9b6298e | -2.97929 | -48.70897 | 2025-11-08 04:36:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| d2b742ae-36e6-3b6a-b5c3-508b94758309 | -4.27894 | -48.33842 | 2025-11-08 04:36:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| d1296bc8-6fd4-3528-8fdc-1f609b2edb7f | -3.10898 | -49.46606 | 2025-11-08 04:36:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 16b56aa9-5ac4-3b96-8035-dc420e7cd9ad | -3.43914 | -43.17039 | 2025-11-08 04:36:00 | NPP-375D | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |


[Clique aqui para ver as próximas entradas](README18.md)
