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

## Dados Diários - Página 6

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 0e34e107-90a0-3528-b14d-b42d20faf456 | -19.84004 | -54.21687 | 2025-05-08 05:27:00 | NPP-375D | BANDEIRANTES | MATO GROSSO DO SUL | Brasil | 5001508 | 50 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 85a447a2-f436-3977-891d-551576c3410f | -5.16565 | -45.106 | 2025-05-08 05:46:00 | AQUA_M-M | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 16.7 |
| a260158e-2e31-3328-a9c3-d50ea616c477 | -5.16725 | -45.09503 | 2025-05-08 05:46:00 | AQUA_M-M | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 174107be-10b7-309d-b99f-ecfc90f2d577 | -8.07727 | -43.12556 | 2025-05-08 05:48:00 | AQUA_M-M | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 58.5 |
| 075983fd-a75a-305e-9434-cd0614fef1aa | -8.0706 | -43.11938 | 2025-05-08 05:48:00 | AQUA_M-M | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 68.2 |
| 05e0e4f1-1b2f-3e28-bfd6-879a8637ee21 | -8.07953 | -43.10854 | 2025-05-08 05:48:00 | AQUA_M-M | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 29.8 |
| 523083f0-0fb0-36a7-bc6d-349a9c55a8a2 | -13.04487 | -53.72829 | 2025-05-08 05:50:00 | AQUA_M-M | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 8.4 |
| fc9b0336-f498-33ea-a0fa-45f5fd160553 | -14.63461 | -45.12419 | 2025-05-08 05:50:00 | AQUA_M-M | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 47.6 |
| 9eb3877b-5222-39e8-a0b7-f05f240cafa7 | -13.04703 | -53.71549 | 2025-05-08 05:50:00 | AQUA_M-M | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 13.0 |
| e859edd3-8fa8-3ace-bff6-c085c855c015 | -15.822 | -46.57002 | 2025-05-08 05:50:00 | AQUA_M-M | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 10.4 |
| 951ddec0-44ae-306d-bcbe-7286fdd485cd | -13.36879 | -54.26229 | 2025-05-08 05:50:00 | AQUA_M-M | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 12.9 |
| 0eebb262-2753-3604-a593-a676e5e6f0c5 | -11.38777 | -52.9406 | 2025-05-08 05:50:00 | AQUA_M-M | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 23.3 |
| 4e83e2fb-9851-30bc-aee9-f42693a4cbf7 | -13.4926 | -52.95502 | 2025-05-08 05:50:00 | AQUA_M-M | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 10.5 |
| b70d0926-24f4-32c3-b43b-d3fce150651e | -13.50057 | -52.96802 | 2025-05-08 05:50:00 | AQUA_M-M | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 33.6 |
| 8022fe63-2451-3685-b84f-4ed33aa004d4 | -13.49075 | -52.96645 | 2025-05-08 05:50:00 | AQUA_M-M | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 15.6 |
| 68356e25-0fdd-3560-9aa2-27f1bfb3f73d | -14.64392 | -45.14104 | 2025-05-08 05:50:00 | AQUA_M-M | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 14.3 |
| eb276559-d40e-3bc3-8e1b-8837a89b9b53 | -18.41728 | -54.70181 | 2025-05-08 05:53:00 | AQUA_M-M | COXIM | MATO GROSSO DO SUL | Brasil | 5003306 | 50 | 33 | nan | nan | nan | Cerrado | 9.1 |
| ef8ce8ba-fe77-359c-9e9a-30bb33da1319 | -19.0562 | -53.44901 | 2025-05-08 05:53:00 | AQUA_M-M | CAMAPUÃ | MATO GROSSO DO SUL | Brasil | 5002605 | 50 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 19de1787-db2e-35ad-8bc9-6eb8630dfb9c | -6.9613 | -42.8108 | 2025-05-08 11:40:00 | GOES-19 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 80.7 |
| c68352ee-31e0-3fed-9d7d-8ee0c67dcf58 | -6.6211 | -44.7668 | 2025-05-08 11:50:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 82.6 |
| c6cb738e-86b6-37fe-9133-d1d74e5f82d8 | -6.9613 | -42.8108 | 2025-05-08 11:50:00 | GOES-19 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 103.2 |
| 186af707-da16-3811-adbc-cfb7c0a9dc8e | -6.6211 | -44.7668 | 2025-05-08 12:00:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 96.6 |
| b12432d2-e9d0-3738-8221-01ae3fa7f8b0 | -6.9801 | -42.809 | 2025-05-08 12:00:00 | GOES-19 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 93.9 |
| e6684421-927a-3245-8460-9ce87ca181e4 | -6.6208 | -44.7896 | 2025-05-08 12:00:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 88.1 |
| 86a7ad1a-43f8-34c6-bb0b-0065f8e1fa78 | -6.6208 | -44.7896 | 2025-05-08 12:10:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 91.1 |
| 5e8d8f61-5aa1-3c8c-8b81-ba0e1b602e22 | -6.9613 | -42.8108 | 2025-05-08 12:10:00 | GOES-19 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 81.1 |
| 75c68bef-fe87-35d6-9167-b8dbc30134db | -6.6211 | -44.7668 | 2025-05-08 12:10:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 110.9 |
| 4cb6afe8-887d-31d3-8822-97f8e4421618 | -6.6211 | -44.7668 | 2025-05-08 12:20:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 97.8 |
| dd809ffc-eb10-3958-b329-fd737998b37a | -6.9613 | -42.8108 | 2025-05-08 12:20:00 | GOES-19 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 89.2 |
| 450351d2-229d-3067-a7b8-325850f2d0db | -6.9801 | -42.809 | 2025-05-08 12:20:00 | GOES-19 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 99.8 |
| 9b217dcd-dd48-3483-ae2c-6e7009ba2cc4 | -6.6208 | -44.7896 | 2025-05-08 12:20:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 100.3 |
| 88f8c5a4-a65b-3b80-b41b-e8bd0eae1cfd | -6.6211 | -44.7668 | 2025-05-08 12:30:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 113.7 |
| d9c9dbc7-0e58-3070-ac46-2dd805371296 | -6.9613 | -42.8108 | 2025-05-08 12:30:00 | GOES-19 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 87.9 |
| 047aae43-e83f-3cf4-9f01-ad9b33d1dd8a | -6.9801 | -42.809 | 2025-05-08 12:30:00 | GOES-19 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 116.7 |
| 12c1b341-fa0b-3269-93c8-8822ce1b1f17 | -6.6208 | -44.7896 | 2025-05-08 12:30:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 90.9 |
| 83621dc2-24ff-33bc-a447-aa116f5e0ac0 | -3.99822 | -43.2473 | 2025-05-08 12:36:00 | TERRA_M-T | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 19.9 |
| 230d2ddb-5ca0-3669-9a6f-60f94bc3d0c3 | -6.88754 | -43.75446 | 2025-05-08 12:36:00 | TERRA_M-T | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 45.6 |
| 022fc275-d456-32f6-a148-98e04236426e | -6.90168 | -43.73932 | 2025-05-08 12:36:00 | TERRA_M-T | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 21.1 |
| 11b51ab0-808c-37ee-a9cb-86635d244514 | -5.595 | -43.23215 | 2025-05-08 12:36:00 | TERRA_M-T | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 16.5 |
| 316ff21e-63e7-3e14-b477-602c8bd0c734 | -5.02146 | -43.58332 | 2025-05-08 12:36:00 | TERRA_M-T | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 14.4 |
| b50f2c63-a1a4-3d20-bfcf-298ec7b9bd14 | -6.62722 | -44.7741 | 2025-05-08 12:36:00 | TERRA_M-T | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 159.0 |
| 8c656fd9-6d97-32e1-b5c2-19892fa299fa | -3.38792 | -41.64968 | 2025-05-08 12:36:00 | TERRA_M-T | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 16.1 |
| e6b431e9-4477-3ebf-aac2-c5b1dc54006f | -5.01922 | -43.59961 | 2025-05-08 12:36:00 | TERRA_M-T | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 16.1 |
| 6aaeda45-7ae6-3497-bcbb-57e30c82c9f7 | -4.93332 | -43.72828 | 2025-05-08 12:36:00 | TERRA_M-T | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 16.7 |
| 0775ae93-e4c8-35f1-a11b-d1c984c292e7 | -5.50332 | -43.23217 | 2025-05-08 12:36:00 | TERRA_M-T | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 21.2 |
| 3595e449-3cb2-3ffd-89a5-c86a4decf3ee | -5.33234 | -43.90654 | 2025-05-08 12:36:00 | TERRA_M-T | GOVERNADOR EUGÊNIO BARROS | MARANHÃO | Brasil | 2104602 | 21 | 33 | nan | nan | nan | Cerrado | 16.4 |
| 96eb2d34-de2f-3a16-b1e1-ad04942037c3 | -5.21145 | -43.17473 | 2025-05-08 12:36:00 | TERRA_M-T | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 23.8 |
| 5f5c1afc-48da-3539-ad41-7f8446f7726f | -5.69753 | -43.65512 | 2025-05-08 12:36:00 | TERRA_M-T | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 16.2 |
| 9595f6bf-efa4-3d46-8509-3233445426cd | -6.97334 | -42.79188 | 2025-05-08 12:36:00 | TERRA_M-T | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 62.2 |
| b5648264-db91-36b4-a33f-905b9b870a59 | -6.61626 | -44.77279 | 2025-05-08 12:36:00 | TERRA_M-T | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 14.4 |
| 80df11bb-a735-3fde-ac25-7e473ab04f15 | -7.08167 | -44.3683 | 2025-05-08 12:36:00 | TERRA_M-T | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 20.6 |
| 4393bbf2-b861-334a-b723-290617321656 | -6.62534 | -44.7682 | 2025-05-08 12:36:00 | TERRA_M-T | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 67.9 |
| 22fe04a5-ed8d-3329-b89c-8bf4868cbee0 | -3.39248 | -41.64498 | 2025-05-08 12:36:00 | TERRA_M-T | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 28.9 |
| f140eb39-45d6-3aa3-a2ca-46e3c6f74b4a | -6.97078 | -42.81224 | 2025-05-08 12:36:00 | TERRA_M-T | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 183.4 |
| 47077765-296c-3306-bf6e-aff7f6162d8a | -7.07962 | -44.38381 | 2025-05-08 12:36:00 | TERRA_M-T | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 11.7 |
| c4b017bf-e866-3b50-9342-e2304670ff6a | -5.44337 | -43.31231 | 2025-05-08 12:36:00 | TERRA_M-T | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 18.0 |
| d29fefda-a98c-3fdf-9f7e-33fc0573c0d4 | -6.62343 | -44.78196 | 2025-05-08 12:36:00 | TERRA_M-T | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 188.3 |
| e0e4ae95-d063-364e-b3d1-a512e79a35d7 | -4.82745 | -43.65922 | 2025-05-08 12:36:00 | TERRA_M-T | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 19.4 |
| 0dd9be79-70b1-3fd1-b573-9575e884a963 | -6.97216 | -42.80571 | 2025-05-08 12:36:00 | TERRA_M-T | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 257.2 |
| 35bc4121-a5e9-309b-8a88-d03b634ccbc8 | -6.45588 | -48.3847 | 2025-05-08 12:36:00 | TERRA_M-T | XAMBIOÁ | TOCANTINS | Brasil | 1722107 | 17 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 6384c871-5219-32cc-aa95-3d901d15d988 | -6.62541 | -44.78787 | 2025-05-08 12:36:00 | TERRA_M-T | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 68.0 |
| 1010dea0-b77a-3fbb-9e5a-03ed57175d14 | -12.17704 | -47.02536 | 2025-05-08 12:38:00 | TERRA_M-T | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 18.6 |
| 1a7cb964-3d70-3fc8-b9de-8e6e93b4404d | -10.58919 | -46.29747 | 2025-05-08 12:38:00 | TERRA_M-T | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 10.9 |
| 989d3768-a6ad-3a00-aea9-423b28725a0f | -12.75576 | -47.97303 | 2025-05-08 12:38:00 | TERRA_M-T | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 8.6 |
| bcad56b7-ae60-3d0d-9998-c0aef4324929 | -11.39596 | -52.9337 | 2025-05-08 12:38:00 | TERRA_M-T | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 6.9 |
| e2b4bc0b-ad4d-3858-b42c-809593e0cdbb | -12.83189 | -47.39849 | 2025-05-08 12:38:00 | TERRA_M-T | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 21.6 |
| cba68ec5-bc69-39a1-b0ed-e8c4918fbe8c | -10.98554 | -44.43494 | 2025-05-08 12:38:00 | TERRA_M-T | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 22.1 |
| c9e81823-0080-3830-bb7f-425431b78c6f | -8.8124 | -50.34123 | 2025-05-08 12:38:00 | TERRA_M-T | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| e9c7c528-bcfe-3973-81e7-6bf3d2ffd94a | -10.66212 | -44.39001 | 2025-05-08 12:38:00 | TERRA_M-T | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 24.8 |
| 552ffa48-0be0-37cc-bcac-b0b6987f5b69 | -10.67418 | -44.39148 | 2025-05-08 12:38:00 | TERRA_M-T | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 50.7 |
| e6c3f6db-e75d-3c80-b550-4e634f8008f1 | -12.17853 | -47.01415 | 2025-05-08 12:38:00 | TERRA_M-T | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 9f74375a-bb5d-34d1-8a5c-72cb3485e30a | -8.07946 | -43.12901 | 2025-05-08 12:38:00 | TERRA_M-T | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 56.9 |
| 44d40f90-4583-3cc9-beae-93cdda4cc843 | -11.83288 | -43.78539 | 2025-05-08 12:38:00 | TERRA_M-T | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 34.3 |
| 138b1ebd-5a12-38fd-a655-f962e915ff1b | -10.59957 | -46.29881 | 2025-05-08 12:38:00 | TERRA_M-T | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 15.5 |
| ea9cda12-110d-32d3-b9c6-20519f317af2 | -11.35257 | -48.0785 | 2025-05-08 12:38:00 | TERRA_M-T | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | 9.7 |
| 14554173-1779-301e-83ac-481d368f24c8 | -10.98097 | -44.42775 | 2025-05-08 12:38:00 | TERRA_M-T | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 23.0 |
| 1f984585-52ae-3265-bcb3-fa6bca3d74f8 | -12.69686 | -44.94044 | 2025-05-08 12:38:00 | TERRA_M-T | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 28.3 |
| 2df6f09b-c6d6-39c1-bffa-4ad65c684ecc | -7.30219 | -47.94186 | 2025-05-08 12:38:00 | TERRA_M-T | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 8.2 |
| a6b5a7f1-c256-35ae-898b-9ee6f8e2a5fe | -9.67725 | -49.71387 | 2025-05-08 12:38:00 | TERRA_M-T | MARIANÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1712504 | 17 | 33 | nan | nan | nan | Cerrado | 7.4 |
| b0b6e7d0-fa3f-3d09-9dae-b0306904d635 | -12.6006 | -46.75844 | 2025-05-08 12:38:00 | TERRA_M-T | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 9.4 |
| 199747a4-9dcc-389e-b178-eec48c54e629 | -11.83044 | -43.80558 | 2025-05-08 12:38:00 | TERRA_M-T | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 21.7 |
| a7244ca2-76a1-3b4c-8385-6877e82e087d | -11.15505 | -48.64501 | 2025-05-08 12:38:00 | TERRA_M-T | BREJINHO DE NAZARÉ | TOCANTINS | Brasil | 1703701 | 17 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 80228b2b-1204-3918-bc91-649a2bc57d61 | -8.08202 | -43.10903 | 2025-05-08 12:38:00 | TERRA_M-T | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 32.8 |
| ee831b3e-b93e-3e5f-ac5e-8f02d5172791 | -10.60125 | -46.28607 | 2025-05-08 12:38:00 | TERRA_M-T | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 31.8 |
| be76a09a-0834-34f4-b55e-9abb35489794 | -11.5099 | -48.20479 | 2025-05-08 12:38:00 | TERRA_M-T | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 8abb82db-cef7-3713-b2c2-2118e357e3f9 | -10.97346 | -44.43349 | 2025-05-08 12:38:00 | TERRA_M-T | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 27.4 |
| cdea5abe-efb6-300e-a568-a1fc0e3e7b4e | -7.30351 | -47.93241 | 2025-05-08 12:38:00 | TERRA_M-T | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 20.1 |
| fc4efb3c-834b-347c-9731-9594971aa516 | -9.67597 | -49.72278 | 2025-05-08 12:38:00 | TERRA_M-T | MARIANÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1712504 | 17 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 26795d27-bf21-3b0e-85a3-1c8f6950d85f | -9.24701 | -48.52764 | 2025-05-08 12:38:00 | TERRA_M-T | RIO DOS BOIS | TOCANTINS | Brasil | 1718709 | 17 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 620ed8e2-053a-3fd9-8ddc-e01dea2aa280 | -12.83037 | -47.41003 | 2025-05-08 12:38:00 | TERRA_M-T | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 76.1 |
| 2b64bb3f-0828-3109-a64c-3f7d3b847a47 | -10.67641 | -44.37385 | 2025-05-08 12:38:00 | TERRA_M-T | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 39.8 |
| e2c84d22-0897-396d-b517-6af949eb8072 | -9.28612 | -48.17861 | 2025-05-08 12:38:00 | TERRA_M-T | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 7.9 |
| b83509d0-cbcd-39e0-b86d-a852da3a1187 | -10.97871 | -44.44523 | 2025-05-08 12:38:00 | TERRA_M-T | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 40.5 |
| 276aed63-a9e5-3e0a-985a-7e6dd2de4424 | -13.03392 | -45.07553 | 2025-05-08 12:38:00 | TERRA_M-T | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 37.8 |
| 890ecc01-f27c-3e72-8dfe-85b9ee90638e | -10.59086 | -46.28474 | 2025-05-08 12:38:00 | TERRA_M-T | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 23.8 |
| 68eabfde-1e5a-3efc-89cb-c50a346c3e7f | -11.56558 | -47.61648 | 2025-05-08 12:38:00 | TERRA_M-T | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 7.9 |
| b9660e6e-fea8-3a6d-866f-170d831867c6 | -11.39431 | -52.94444 | 2025-05-08 12:38:00 | TERRA_M-T | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 30.0 |
| 03dd4f43-c5f4-30ab-ad1e-b6751e1aa600 | -6.6211 | -44.7668 | 2025-05-08 12:40:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 85.9 |
| d125fa0d-7540-3af5-a2a5-9d584fe50383 | -6.9801 | -42.809 | 2025-05-08 12:40:00 | GOES-19 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 121.5 |
| 07fc022e-76d7-3372-8c6b-6da816fe2fc1 | -6.9613 | -42.8108 | 2025-05-08 12:40:00 | GOES-19 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 110.7 |


[Clique aqui para ver as próximas entradas](README7.md)
