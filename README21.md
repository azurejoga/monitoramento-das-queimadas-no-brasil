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

## Dados Diários - Página 21

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| d3d3ab55-bec4-3cf9-83b2-336bf142d632 | -6.9323 | -43.7264 | 2026-07-03 13:10:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 98.8 |
| 966d1fed-8a6c-3d7a-90b2-5b12326b4aaa | -12.5138 | -48.2581 | 2026-07-03 13:10:00 | GOES-19 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 200.5 |
| 1245e83d-230a-3a36-b556-0534117582f0 | -12.4947 | -48.2607 | 2026-07-03 13:10:00 | GOES-19 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 76.5 |
| f6c226e9-6622-3163-b61b-aa875367a59e | -12.7553 | -44.5194 | 2026-07-03 13:20:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 93.2 |
| a779adb3-6b51-3f03-8c85-11428de53125 | -6.9323 | -43.7264 | 2026-07-03 13:20:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 98.9 |
| c42477c2-94dc-3baf-bff7-aad15d6f3e1c | -8.6919 | -54.5873 | 2026-07-03 13:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 74.8 |
| 899dc13a-1b3a-3b0d-9441-fec7aa51e485 | -5.7945 | -45.0586 | 2026-07-03 13:20:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 181.4 |
| f4fc520c-e117-3d24-9b2e-37b4ca025c40 | -5.8132 | -45.0573 | 2026-07-03 13:20:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 103.0 |
| 77b7649a-9334-3f03-b789-ee5b25ac3cc1 | -11.4345 | -46.5291 | 2026-07-03 13:20:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 71.4 |
| a7552c65-d6ce-36f2-9b77-3bf8ebf00d85 | -6.9326 | -43.7032 | 2026-07-03 13:20:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 88.7 |
| 51765718-e610-31bd-a85f-10e5c192cbdb | -12.5138 | -48.2581 | 2026-07-03 13:20:00 | GOES-19 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 224.0 |
| 1c643e64-6e39-3e5a-a319-9cb6746e5f0c | -5.7943 | -45.0813 | 2026-07-03 13:20:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 82.6 |
| 1f3e3d29-884a-3da4-a631-f8ac9cd16880 | -12.5135 | -48.2802 | 2026-07-03 13:20:00 | GOES-19 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 67.6 |
| 411b63f3-c1d2-36d9-80c0-ea5997419825 | -6.9323 | -43.7264 | 2026-07-03 13:30:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 114.4 |
| 828a3129-4ba7-3099-b28f-4cae97a0bd39 | -12.5138 | -48.2581 | 2026-07-03 13:30:00 | GOES-19 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 242.9 |
| 6b540ba3-c6ed-3978-8694-d564d4e1782f | -12.7553 | -44.5194 | 2026-07-03 13:30:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 121.7 |
| d7eff38e-6de0-3a80-8cfe-1c89611c1de6 | -5.8132 | -45.0573 | 2026-07-03 13:30:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 109.1 |
| 40bc95ae-42fa-378f-aa0b-dd2dabfb424d | -5.7945 | -45.0586 | 2026-07-03 13:30:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 194.8 |
| 6e98c610-2122-34a5-837a-995bc2042da6 | -6.9326 | -43.7032 | 2026-07-03 13:30:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 86.5 |
| 2fe1ccb7-6980-3b27-a210-4e8cff76ff54 | -3.8671 | -42.9685 | 2026-07-03 13:30:00 | GOES-19 | BURITI | MARANHÃO | Brasil | 2102200 | 21 | 33 | nan | nan | nan | Cerrado | 76.9 |
| ba64e301-cf64-30eb-b3f0-706ec8f0bb81 | -8.6919 | -54.5873 | 2026-07-03 13:40:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 66.8 |
| eb6e141d-5356-317e-a907-a34de96ad52a | -6.9138 | -43.7049 | 2026-07-03 13:40:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 92.6 |
| c58f0f8d-1435-3cf2-80ca-8ccdaea4ddc5 | -6.9326 | -43.7032 | 2026-07-03 13:40:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 88.3 |
| bfae280c-9d1a-3ac4-a69d-f3cc898a889e | -3.8857 | -42.9675 | 2026-07-03 13:40:00 | GOES-19 | BURITI | MARANHÃO | Brasil | 2102200 | 21 | 33 | nan | nan | nan | Cerrado | 75.9 |
| 08fbdf34-77fe-3e89-8a6c-a8abbb929ca7 | -5.7945 | -45.0586 | 2026-07-03 13:40:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 207.8 |
| 23b13b32-0dea-3ebf-a934-faf04d1c5072 | -5.8132 | -45.0573 | 2026-07-03 13:40:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 95.5 |
| 07c589a7-6770-3624-b894-cf1cbfc0d34e | -6.9135 | -43.7281 | 2026-07-03 13:40:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 115.2 |
| 82554811-3289-3491-9bdb-e559bc4956f3 | -6.9323 | -43.7264 | 2026-07-03 13:40:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 124.2 |
| ccad962f-9cc9-346e-afc6-d602bb26dd38 | -12.7553 | -44.5194 | 2026-07-03 13:40:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 169.9 |
| 91651ea7-d996-3421-8b03-26a1b4d7b5d4 | -12.5138 | -48.2581 | 2026-07-03 13:40:00 | GOES-19 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 184.7 |
| 064758e1-d669-38bd-9183-ffd5d49b36b0 | -12.4947 | -48.2607 | 2026-07-03 13:40:00 | GOES-19 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 86.0 |
| adbbceed-99e9-37de-9183-0d26d9bd424e | -11.9305 | -43.3812 | 2026-07-03 13:40:00 | GOES-19 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 99.9 |
| 6e4ae474-2e30-3232-9f86-3a954521d107 | -3.4259 | -41.714 | 2026-07-03 13:40:00 | GOES-19 | BURITI DOS LOPES | PIAUÍ | Brasil | 2202000 | 22 | 33 | nan | nan | nan | Caatinga | 84.5 |
| 1ddabc44-92d7-3e74-9ec5-7b797cd37d35 | -5.7945 | -45.0586 | 2026-07-03 13:50:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 172.6 |
| 8524241c-8c90-3fa5-ae8d-c8f18a5d8073 | -12.7553 | -44.5194 | 2026-07-03 13:50:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 189.3 |
| 2cbe7448-1fe9-36a6-9b5c-0f887b313e4c | -3.4259 | -41.714 | 2026-07-03 13:50:00 | GOES-19 | BURITI DOS LOPES | PIAUÍ | Brasil | 2202000 | 22 | 33 | nan | nan | nan | Caatinga | 93.2 |
| def96baf-40d0-3289-bda6-e02a77d971f2 | -5.7943 | -45.0813 | 2026-07-03 13:50:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 85.5 |
| d17814be-8f24-3a58-a01a-562ef24f6129 | -6.9135 | -43.7281 | 2026-07-03 13:50:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 106.9 |
| 8b4593b6-24df-3d48-985c-5b265d7b2a2e | -12.5138 | -48.2581 | 2026-07-03 13:50:00 | GOES-19 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 178.8 |
| cec810c3-170a-32ed-8e69-d3e93f341cf1 | -6.9326 | -43.7032 | 2026-07-03 13:50:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 102.1 |
| de790b55-866e-3ac6-9f4b-b46f16dd4f81 | -6.9323 | -43.7264 | 2026-07-03 13:50:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 136.0 |
| ebe65fdf-d282-3567-b95d-a2f86bb63acc | -3.8857 | -42.9675 | 2026-07-03 13:50:00 | GOES-19 | BURITI | MARANHÃO | Brasil | 2102200 | 21 | 33 | nan | nan | nan | Cerrado | 75.4 |
| 1a3fd5d3-d7a8-362c-a02e-647276b23f5a | -12.4947 | -48.2607 | 2026-07-03 13:50:00 | GOES-19 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 72.6 |
| cf76c193-201e-3e48-a1af-9cb88134837e | -6.9138 | -43.7049 | 2026-07-03 13:50:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 102.1 |
| c336999a-8b15-3e59-b982-b4ca79666091 | -11.4341 | -46.5517 | 2026-07-03 13:50:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 68.7 |
| 26198d81-7af5-3eb1-bec1-96cc29075ecb | -3.8671 | -42.9685 | 2026-07-03 13:50:00 | GOES-19 | BURITI | MARANHÃO | Brasil | 2102200 | 21 | 33 | nan | nan | nan | Cerrado | 75.9 |
| 911525d1-3ec8-3f02-b016-6995c1e32c79 | -3.8857 | -42.9675 | 2026-07-03 14:00:00 | GOES-19 | BURITI | MARANHÃO | Brasil | 2102200 | 21 | 33 | nan | nan | nan | Cerrado | 85.1 |
| d00f59b8-0090-3d28-9821-626409cd8f8a | -5.7945 | -45.0586 | 2026-07-03 14:00:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 187.9 |
| f29e897c-2b14-354c-b8c2-3ff782e169c0 | -6.9135 | -43.7281 | 2026-07-03 14:00:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 108.5 |
| 6e039f29-14e8-3177-be14-7948181535bd | -3.4259 | -41.714 | 2026-07-03 14:00:00 | GOES-19 | BURITI DOS LOPES | PIAUÍ | Brasil | 2202000 | 22 | 33 | nan | nan | nan | Caatinga | 138.9 |
| d3d1d4c3-a402-370f-9efc-12ee8cd66097 | -6.9326 | -43.7032 | 2026-07-03 14:00:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 87.0 |
| 3422762f-164b-33f2-b39f-758c67254303 | -12.7553 | -44.5194 | 2026-07-03 14:00:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 188.0 |
| c47f1f8e-a1e9-3d02-b2ab-c3e87858a07b | -6.9138 | -43.7049 | 2026-07-03 14:00:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 91.4 |
| 4fe786f3-add0-389b-ac78-81077d49a2d3 | -11.6984 | -51.6391 | 2026-07-03 14:00:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 74.6 |
| 1145cfd9-5d81-30ba-8bdc-bb2bbc23241c | -5.944 | -45.0704 | 2026-07-03 14:00:00 | GOES-19 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 80.5 |
| 522d0b20-d57a-3a1a-9ccb-4d0b7bdd77f3 | -6.9323 | -43.7264 | 2026-07-03 14:00:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 112.8 |
| 687b886f-b360-38aa-b0f2-facf4a8e4782 | -12.4947 | -48.2607 | 2026-07-03 14:00:00 | GOES-19 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 86.7 |
| 820c0376-bfb6-34d0-9b63-02803a4b9a24 | -11.4341 | -46.5517 | 2026-07-03 14:00:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 82.3 |
| 14c61cea-2e6d-325e-aa3d-c42f8170ec2a | -12.5138 | -48.2581 | 2026-07-03 14:00:00 | GOES-19 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 184.3 |
| c5d0aa15-b2c3-3882-bbee-32b7120fe403 | -12.4947 | -48.2607 | 2026-07-03 14:10:00 | GOES-19 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 63.6 |
| a435a207-4b9d-3684-a611-923ff5ec30de | -12.7553 | -44.5194 | 2026-07-03 14:10:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 243.3 |
| 56c815ae-4007-3f3e-8ca5-6b4da1daae38 | -5.7945 | -45.0586 | 2026-07-03 14:10:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 153.9 |
| 9730a16d-c81c-3075-b17c-0f6f1a9f7810 | -6.9323 | -43.7264 | 2026-07-03 14:10:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 148.2 |
| d4f747d3-ecaa-3f1b-bd3c-e0efe86f2135 | -3.4259 | -41.714 | 2026-07-03 14:10:00 | GOES-19 | BURITI DOS LOPES | PIAUÍ | Brasil | 2202000 | 22 | 33 | nan | nan | nan | Caatinga | 141.4 |
| de6480f2-5e0e-3f08-8d7a-8b5833769313 | -19.6467 | -48.6967 | 2026-07-03 14:10:00 | GOES-19 | CAMPO FLORIDO | MINAS GERAIS | Brasil | 3111408 | 31 | 33 | nan | nan | nan | Cerrado | 99.5 |
| b8ca9c93-24d9-32af-8bb3-5d6305018462 | -6.9326 | -43.7032 | 2026-07-03 14:10:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 101.2 |
| 3b7c51fb-a8cb-36d6-87ad-07515c64722f | -11.4341 | -46.5517 | 2026-07-03 14:10:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 82.3 |
| b8980e89-d421-332b-95d8-d7611e66a88e | -11.6984 | -51.6391 | 2026-07-03 14:10:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 91.9 |
| 356f9a0b-8ccf-3d4e-b916-dadcf8687368 | -12.5138 | -48.2581 | 2026-07-03 14:10:00 | GOES-19 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 167.8 |
| 674bdb3d-1127-309e-b434-5f66fb6f2e03 | -6.9135 | -43.7281 | 2026-07-03 14:10:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 105.4 |
| 05c11feb-320d-395a-9d0b-c7fc95fe2245 | -6.9138 | -43.7049 | 2026-07-03 14:10:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 87.3 |
| e05f9a5c-c757-35ed-9c99-37cff18cbb13 | -7.7958 | -47.1569 | 2026-07-03 14:10:00 | GOES-19 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 87.6 |
| 721edecb-5963-3b83-8c9f-6a8669b01cfe | -12.7548 | -44.5428 | 2026-07-03 14:20:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 100.1 |
| 34218d95-a69b-3795-a1f8-a5877a541f11 | -6.9135 | -43.7281 | 2026-07-03 14:20:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 99.5 |
| c5bc36c0-e4bc-3b6a-a7b3-cfd13a0b879b | -12.4947 | -48.2607 | 2026-07-03 14:20:00 | GOES-19 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 79.1 |
| b79d4931-285a-3f97-9611-607db3d0f143 | -6.9323 | -43.7264 | 2026-07-03 14:20:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 137.6 |
| 57a5bbce-e6b1-3fef-a6e6-2677f35a9520 | -3.4259 | -41.714 | 2026-07-03 14:20:00 | GOES-19 | BURITI DOS LOPES | PIAUÍ | Brasil | 2202000 | 22 | 33 | nan | nan | nan | Caatinga | 157.1 |
| baaf198e-a692-3b47-91a8-051d20ca7574 | -5.7945 | -45.0586 | 2026-07-03 14:20:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 159.9 |
| 5859f4b4-6487-3878-8515-37d4d639185a | -19.5078 | -52.7365 | 2026-07-03 14:20:00 | GOES-19 | PARAÍSO DAS ÁGUAS | MATO GROSSO DO SUL | Brasil | 5006275 | 50 | 33 | nan | nan | nan | Cerrado | 103.7 |
| f5c1450d-2e8c-3293-a923-1a440ea9bd94 | -12.7553 | -44.5194 | 2026-07-03 14:20:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 250.8 |
| 3294c98f-5c60-31a9-a954-f7e261dddd09 | -3.8671 | -42.9685 | 2026-07-03 14:20:00 | GOES-19 | BURITI | MARANHÃO | Brasil | 2102200 | 21 | 33 | nan | nan | nan | Cerrado | 72.4 |
| 0ebedc67-360b-378a-add6-571f9cad7ba1 | -12.5138 | -48.2581 | 2026-07-03 14:20:00 | GOES-19 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 185.7 |
| 2702a268-9d1e-323f-aa92-783a0e4db918 | -11.9305 | -43.3812 | 2026-07-03 14:20:00 | GOES-19 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 86.1 |
| aa6c7cc6-244e-3be0-9e3b-8152dada438b | -6.9326 | -43.7032 | 2026-07-03 14:20:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 102.6 |
| df4e5d27-8b7b-3759-9f23-93bc714588ac | -11.4341 | -46.5517 | 2026-07-03 14:20:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 67.5 |
| ae0878a5-c48c-3ea3-b796-e72b28f1a50b | -5.9068 | -45.0504 | 2026-07-03 14:20:00 | GOES-19 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 74.2 |
| 083f4227-9b33-3a25-baf1-4187941f7c5a | -11.6984 | -51.6391 | 2026-07-03 14:20:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 138.0 |
| 12871de4-4b5a-37ba-a971-d84b5c6b5132 | -6.9138 | -43.7049 | 2026-07-03 14:20:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 85.2 |
| 9e474edc-0f8f-324a-9f52-84e90eddc855 | -5.9255 | -45.049 | 2026-07-03 14:30:00 | GOES-19 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 77.1 |
| bf80d51c-92ea-3cca-8573-4903f6b4037c | -8.6919 | -54.5873 | 2026-07-03 14:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 78.4 |
| c39cfd26-fbd6-376e-8f78-40c10c2c0b20 | -12.7548 | -44.5428 | 2026-07-03 14:30:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 109.0 |
| 06601e91-836b-3019-ac51-195ac08dbdc7 | -11.4341 | -46.5517 | 2026-07-03 14:30:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 106.4 |
| da9ead11-5c3f-37b1-91df-e629a9a46a88 | -3.4259 | -41.714 | 2026-07-03 14:30:00 | GOES-19 | BURITI DOS LOPES | PIAUÍ | Brasil | 2202000 | 22 | 33 | nan | nan | nan | Caatinga | 163.4 |
| e33d5915-645b-34dc-be46-e02bd3019591 | -8.6921 | -54.567 | 2026-07-03 14:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 57.3 |
| 041a3be0-a627-34c8-8fc2-75e158cc32dd | -6.9326 | -43.7032 | 2026-07-03 14:30:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 96.7 |
| ea74e0bd-b7a2-3731-ae4b-192cc8b009a9 | -12.7553 | -44.5194 | 2026-07-03 14:30:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 253.3 |
| d373ced8-9d91-34f1-8a36-d7895ccd9f51 | -6.9323 | -43.7264 | 2026-07-03 14:30:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 142.3 |
| 0813c5be-edc0-3e08-ad7a-2c3d534356c5 | -12.5138 | -48.2581 | 2026-07-03 14:30:00 | GOES-19 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 194.6 |
| 0d35190d-f758-3374-b219-4a5dcf66a901 | -5.9068 | -45.0504 | 2026-07-03 14:30:00 | GOES-19 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 77.0 |
| 9f750a76-938f-33db-a54c-9d06cf0a0611 | -11.6984 | -51.6391 | 2026-07-03 14:30:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 110.1 |


[Clique aqui para ver as próximas entradas](README22.md)
