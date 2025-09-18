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

## Dados Diários - Página 7

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| c1a09a76-447c-33b6-becb-2fe02ec3d243 | -18.5505 | -46.0369 | 2025-09-18 03:20:00 | GOES-19 | PATOS DE MINAS | MINAS GERAIS | Brasil | 3148004 | 31 | 33 | nan | nan | nan | Cerrado | 71.0 |
| 09e083b6-1612-3010-bc1b-ef2ba0f6be71 | -11.3871 | -50.8465 | 2025-09-18 03:20:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 97.2 |
| b3b5d967-0685-32a2-8619-748d7e6a0a93 | -3.84472 | -40.3693 | 2025-09-18 03:21:00 | NOAA-21 | SOBRAL | CEARÁ | Brasil | 2312908 | 23 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 9238320a-0b12-34e4-b37a-8c342ffa65ea | -3.35208 | -39.2789 | 2025-09-18 03:21:00 | NOAA-21 | TRAIRI | CEARÁ | Brasil | 2313500 | 23 | 33 | nan | nan | nan | Caatinga | 3.9 |
| 17ff7d1f-29c9-32b2-b274-548a4f135781 | -4.69846 | -41.97749 | 2025-09-18 03:21:00 | NOAA-21 | CAMPO MAIOR | PIAUÍ | Brasil | 2202208 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| f5f5067a-4069-3666-a444-c4e242d0cbc3 | -3.84325 | -40.37769 | 2025-09-18 03:21:00 | NOAA-21 | SOBRAL | CEARÁ | Brasil | 2312908 | 23 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 51d21ce5-2565-38ce-b096-66799df4a398 | -3.84356 | -40.37258 | 2025-09-18 03:21:00 | NOAA-21 | SOBRAL | CEARÁ | Brasil | 2312908 | 23 | 33 | nan | nan | nan | Caatinga | 3.4 |
| c0a9d45a-2d48-356f-bcf9-d01b741692e4 | -4.70027 | -41.96724 | 2025-09-18 03:21:00 | NOAA-21 | CAMPO MAIOR | PIAUÍ | Brasil | 2202208 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 0c99da50-17a1-3623-80a5-46ea6d36ba4c | -5.18727 | -35.87233 | 2025-09-18 03:21:00 | NOAA-21 | PEDRA GRANDE | RIO GRANDE DO NORTE | Brasil | 2409506 | 24 | 33 | nan | nan | nan | Caatinga | 1.0 |
| df137ced-5a32-3b1e-a595-f3f2204f01d1 | -4.5175 | -38.54758 | 2025-09-18 03:21:00 | NOAA-21 | OCARA | CEARÁ | Brasil | 2309458 | 23 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 89ad1a54-13c5-3378-addd-8a715ab5bd26 | -4.34255 | -40.73539 | 2025-09-18 03:21:00 | NOAA-21 | IPU | CEARÁ | Brasil | 2305803 | 23 | 33 | nan | nan | nan | Caatinga | 2.7 |
| c51faae5-1e2f-3d3a-b4ee-f61737569e25 | -3.84399 | -40.37349 | 2025-09-18 03:21:00 | NOAA-21 | SOBRAL | CEARÁ | Brasil | 2312908 | 23 | 33 | nan | nan | nan | Caatinga | 1.7 |
| e170db3d-d396-333b-b76b-e40eca1ee8ef | -4.70118 | -41.96208 | 2025-09-18 03:21:00 | NOAA-21 | CAMPO MAIOR | PIAUÍ | Brasil | 2202208 | 22 | 33 | nan | nan | nan | Caatinga | 3.2 |
| 35f030c6-5a37-3e23-a43e-616d95c4ea09 | -3.02055 | -41.7329 | 2025-09-18 03:21:00 | NOAA-21 | PARNAÍBA | PIAUÍ | Brasil | 2207702 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| df99fdb8-c390-3f9c-acc5-bd44976abad9 | -5.18791 | -35.8685 | 2025-09-18 03:21:00 | NOAA-21 | PEDRA GRANDE | RIO GRANDE DO NORTE | Brasil | 2409506 | 24 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 112ff03a-9f58-36e5-adfe-eda51d1b3c25 | -3.89716 | -40.82205 | 2025-09-18 03:21:00 | NOAA-21 | IBIAPINA | CEARÁ | Brasil | 2305308 | 23 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 500ea5a8-364f-3c27-bf13-abf93c960c0f | -4.69936 | -41.97237 | 2025-09-18 03:21:00 | NOAA-21 | CAMPO MAIOR | PIAUÍ | Brasil | 2202208 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 07c04d74-fbd6-3d8b-8200-ee75b9505fd2 | -5.19146 | -35.87296 | 2025-09-18 03:21:00 | NOAA-21 | PEDRA GRANDE | RIO GRANDE DO NORTE | Brasil | 2409506 | 24 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 545a3b74-f4e9-305c-9fe1-591bdb1670d0 | -4.517 | -38.55054 | 2025-09-18 03:21:00 | NOAA-21 | OCARA | CEARÁ | Brasil | 2309458 | 23 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 3a72dbae-ed43-3f88-9b8a-dcc8f6072f2f | -3.84286 | -40.3768 | 2025-09-18 03:21:00 | NOAA-21 | SOBRAL | CEARÁ | Brasil | 2312908 | 23 | 33 | nan | nan | nan | Caatinga | 2.2 |
| fe4f4865-80b4-3dd9-b6be-d3e94703895f | -5.19209 | -35.86914 | 2025-09-18 03:21:00 | NOAA-21 | PEDRA GRANDE | RIO GRANDE DO NORTE | Brasil | 2409506 | 24 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 8956eeba-db57-3d9c-8aa1-a6ba65462835 | -5.19273 | -35.86532 | 2025-09-18 03:21:00 | NOAA-21 | PEDRA GRANDE | RIO GRANDE DO NORTE | Brasil | 2409506 | 24 | 33 | nan | nan | nan | Caatinga | 1.5 |
| d00cc090-2b99-330b-b854-73b8adccb137 | -4.34377 | -40.73656 | 2025-09-18 03:21:00 | NOAA-21 | IPU | CEARÁ | Brasil | 2305803 | 23 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 72702811-d445-3e9a-81ac-6bd8fe2c5856 | -4.69577 | -41.95594 | 2025-09-18 03:21:00 | NOAA-21 | CAMPO MAIOR | PIAUÍ | Brasil | 2202208 | 22 | 33 | nan | nan | nan | Caatinga | 3.1 |
| 8f5f6770-f478-3d3b-a642-c49e29ad0ce6 | -4.3444 | -40.73283 | 2025-09-18 03:21:00 | NOAA-21 | IPU | CEARÁ | Brasil | 2305803 | 23 | 33 | nan | nan | nan | Caatinga | 0.7 |
| f7ef5a71-d0da-325c-86db-3b3144b3d491 | -5.73804 | -42.57014 | 2025-09-18 03:23:00 | NOAA-21 | BARRO DURO | PIAUÍ | Brasil | 2201408 | 22 | 33 | nan | nan | nan | Caatinga | 4.8 |
| edf9f97e-8a8b-36a6-a057-903cc23372c3 | -6.60555 | -43.57791 | 2025-09-18 03:23:00 | NOAA-21 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 5.2 |
| c79c4d24-75df-3217-b2fb-7a92e5094106 | -6.21684 | -44.29302 | 2025-09-18 03:23:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 63e5c914-7338-3cfc-89b9-f88544377ee4 | -6.63453 | -38.54898 | 2025-09-18 03:23:00 | NOAA-21 | TRIUNFO | PARAÍBA | Brasil | 2516805 | 25 | 33 | nan | nan | nan | Caatinga | 4.0 |
| 4680143e-4f97-3844-964f-648bf3502dfe | -6.55318 | -44.01839 | 2025-09-18 03:23:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 5.0 |
| d77a9ffa-03d1-3641-8d4b-5254c24b7786 | -8.26673 | -35.02689 | 2025-09-18 03:23:00 | NOAA-21 | CABO DE SANTO AGOSTINHO | PERNAMBUCO | Brasil | 2602902 | 26 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| e2a732ab-b89a-3f29-8e49-c45a047b560a | -6.72686 | -44.15131 | 2025-09-18 03:23:00 | NOAA-21 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 37.6 |
| 9b64eb88-cdab-3105-b7e7-b1f2006f0cf9 | -6.31894 | -42.40156 | 2025-09-18 03:23:00 | NOAA-21 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 3.7 |
| 5f0bddf7-969f-3e93-ab29-4fd71a98d3cc | -6.20982 | -44.29157 | 2025-09-18 03:23:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| bcd86d26-df03-3905-a44f-5bd96882afea | -5.7372 | -42.57069 | 2025-09-18 03:23:00 | NOAA-21 | BARRO DURO | PIAUÍ | Brasil | 2201408 | 22 | 33 | nan | nan | nan | Caatinga | 5.0 |
| dbded0a7-fd03-3ca6-acb8-4e68b9c1b6bd | -6.55296 | -43.5984 | 2025-09-18 03:23:00 | NOAA-21 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 8.8 |
| 9edba95c-8d77-3b6f-8b26-79b83d68f04a | -5.5399 | -42.17872 | 2025-09-18 03:23:00 | NOAA-21 | ALTO LONGÁ | PIAUÍ | Brasil | 2200301 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| e4891d78-c4a1-36af-be60-bb4a742ed561 | -4.8634 | -42.96926 | 2025-09-18 03:23:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| c5bf9316-ce75-3c7f-9736-17de11ce9e05 | -6.31615 | -42.39972 | 2025-09-18 03:23:00 | NOAA-21 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 3.4 |
| de7e4f61-2834-30bd-9f48-16a673352c26 | -7.22818 | -40.17656 | 2025-09-18 03:23:00 | NOAA-21 | ARARIPE | CEARÁ | Brasil | 2301307 | 23 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 66dfdde3-0f0e-3001-9cb6-5877290b618e | -6.60882 | -43.57343 | 2025-09-18 03:23:00 | NOAA-21 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 5.0 |
| f46508e1-e14f-379c-b167-b49a76044c8d | -6.72878 | -44.14703 | 2025-09-18 03:23:00 | NOAA-21 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 16.0 |
| 88cf4c45-3eda-32a3-b784-67ab5405c543 | -6.53222 | -43.93826 | 2025-09-18 03:23:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 11.1 |
| 493558b2-f6c7-36cf-9e81-8cc08a3065e2 | -6.56098 | -43.59283 | 2025-09-18 03:23:00 | NOAA-21 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 63c941f2-547a-3f73-a140-e9efca89e401 | -6.54623 | -43.59708 | 2025-09-18 03:23:00 | NOAA-21 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 8.8 |
| 2dc47528-25ed-3ba6-b917-30b01f113884 | -6.1251 | -43.94665 | 2025-09-18 03:23:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 89207ca9-e25e-30b7-9bc1-5401244bdb2b | -6.53338 | -43.93202 | 2025-09-18 03:23:00 | NOAA-21 | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 130518a0-dd19-3f04-869d-24243f186864 | -6.60768 | -43.57943 | 2025-09-18 03:23:00 | NOAA-21 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 5.0 |
| e0039290-65ea-393b-9bf1-dc8e63f15012 | -6.61223 | -43.57946 | 2025-09-18 03:23:00 | NOAA-21 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 1987d20d-4476-3d2c-8f86-976cfd151a5d | -7.23018 | -40.1771 | 2025-09-18 03:23:00 | NOAA-21 | ARARIPE | CEARÁ | Brasil | 2301307 | 23 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 346438a8-204d-35cb-87f7-d6b7e43a1707 | -6.54628 | -44.01703 | 2025-09-18 03:23:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 4.6 |
| bde5a445-ffbb-3355-8575-41fedb52a5ab | -6.31257 | -42.40074 | 2025-09-18 03:23:00 | NOAA-21 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 3.7 |
| 2cf9811a-d746-33b8-8bf7-3d7f7093eb7d | -4.86232 | -42.97532 | 2025-09-18 03:23:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 6d3be7e4-7b3e-3389-9a11-9b245130f00d | -7.22477 | -40.17619 | 2025-09-18 03:23:00 | NOAA-21 | ARARIPE | CEARÁ | Brasil | 2301307 | 23 | 33 | nan | nan | nan | Caatinga | 1.5 |
| fe13e0a4-cf64-3e81-b046-7a9b32a46364 | -6.3935 | -43.34166 | 2025-09-18 03:23:00 | NOAA-21 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 5.8 |
| f5dc3b04-3510-35cc-a6ed-818adaba8e0f | -6.72751 | -44.15391 | 2025-09-18 03:23:00 | NOAA-21 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 26.4 |
| dc82a2b3-176d-3ea6-a596-364e69433af6 | -6.7206 | -44.15245 | 2025-09-18 03:23:00 | NOAA-21 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 8d13d07d-e17a-3b46-ac44-313f4ee973ac | -6.12397 | -43.9529 | 2025-09-18 03:23:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 2124f3bd-83c3-356c-b6d8-9ab202891985 | -6.30979 | -42.39882 | 2025-09-18 03:23:00 | NOAA-21 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 3.4 |
| 8c40c3e7-c8e0-36c5-8a24-30959f6d905b | -6.53207 | -43.93888 | 2025-09-18 03:23:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 2f8f08c1-f252-3321-bb80-d850775fa83b | -6.5541 | -43.59232 | 2025-09-18 03:23:00 | NOAA-21 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 8.8 |
| 37e4e421-96d8-3844-838d-2163b1a279cc | -5.53359 | -42.17764 | 2025-09-18 03:23:00 | NOAA-21 | ALTO LONGÁ | PIAUÍ | Brasil | 2200301 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 65d0e91f-2c70-3bff-97b7-e46d1e462044 | -6.53351 | -43.93129 | 2025-09-18 03:23:00 | NOAA-21 | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 652bc0e6-dda3-3cc1-93b8-617e1600e2c7 | -6.39573 | -43.32958 | 2025-09-18 03:23:00 | NOAA-21 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 5.8 |
| b304921d-d3bb-3deb-9b7e-178e4b9281f1 | -11.3681 | -50.8486 | 2025-09-18 03:30:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 82.4 |
| cb9c4cef-1a41-395f-8546-ff5e40088e64 | -18.5303 | -46.0414 | 2025-09-18 03:30:00 | GOES-19 | VARJÃO DE MINAS | MINAS GERAIS | Brasil | 3170750 | 31 | 33 | nan | nan | nan | Cerrado | 86.8 |
| dbba3e11-7a09-3164-b41d-579f51b13d35 | -19.0332 | -48.2773 | 2025-09-18 03:30:00 | GOES-19 | UBERLÂNDIA | MINAS GERAIS | Brasil | 3170206 | 31 | 33 | nan | nan | nan | Cerrado | 67.4 |
| ddaa44ad-0657-3506-80b1-608b64ad3b75 | -22.9714 | -51.5902 | 2025-09-18 03:30:00 | GOES-19 | GUARACI | PARANÁ | Brasil | 4109203 | 41 | 33 | nan | nan | nan | Mata Atlântica | 63.4 |
| ab4970e2-2ecc-34de-844a-52cab6f932fb | -11.3871 | -50.8465 | 2025-09-18 03:30:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 136.7 |
| 96d72f47-4757-3cc3-b534-e0f1ebe1ce5e | -9.1712 | -46.9569 | 2025-09-18 03:30:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 66.0 |
| d3c2c30c-e8ac-350d-9ace-8de4aced1af5 | -11.3684 | -50.8273 | 2025-09-18 03:30:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 59.1 |
| 3a566052-3472-36f7-a2dc-1a03f7cee886 | -9.1523 | -46.9589 | 2025-09-18 03:30:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 150.9 |
| d86f1988-c921-3199-b91c-867672132381 | -11.3874 | -50.8252 | 2025-09-18 03:30:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 104.2 |
| 076f62c4-ffe1-3846-acc0-f7a2961d112d | -9.1526 | -46.9366 | 2025-09-18 03:30:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 39.2 |
| 81badbc0-4cee-3b9f-aac9-27da17f944ce | -11.3874 | -50.8252 | 2025-09-18 03:40:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 83.6 |
| 0216e623-387b-36ad-ab4f-2fc654bb5c58 | -22.9714 | -51.5902 | 2025-09-18 03:40:00 | GOES-19 | GUARACI | PARANÁ | Brasil | 4109203 | 41 | 33 | nan | nan | nan | Mata Atlântica | 77.0 |
| ec95b09d-693b-3f24-9e65-fd554075e000 | -11.3871 | -50.8465 | 2025-09-18 03:40:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 108.4 |
| a51d73ae-b939-3fc1-a95c-ff3a2c96146c | -11.3681 | -50.8486 | 2025-09-18 03:40:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 71.7 |
| e8163b7c-2356-3cb3-a555-4fbcb5421aa1 | -19.0332 | -48.2773 | 2025-09-18 03:40:00 | GOES-19 | UBERLÂNDIA | MINAS GERAIS | Brasil | 3170206 | 31 | 33 | nan | nan | nan | Cerrado | 82.0 |
| fd647b0e-0a53-3063-b58c-f3f6d99ad737 | -11.3874 | -50.8252 | 2025-09-18 03:50:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 72.4 |
| 59d55739-8bcc-3669-b813-3556af33f608 | -11.3871 | -50.8465 | 2025-09-18 03:50:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 78.1 |
| bebd73b2-0058-3d32-a25a-244c1611960a | -11.3684 | -50.8273 | 2025-09-18 03:50:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 68.9 |
| 241e8382-735c-32d4-a986-6c6d1924ee34 | -12.9068 | -44.658 | 2025-09-18 03:50:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 61.0 |
| 1e17054d-4f42-3b40-b4b7-3be3bbd422d1 | -19.0332 | -48.2773 | 2025-09-18 03:50:00 | GOES-19 | UBERLÂNDIA | MINAS GERAIS | Brasil | 3170206 | 31 | 33 | nan | nan | nan | Cerrado | 80.8 |
| a83cffd3-d09a-3f7b-adba-2eaaee235d7b | -22.9714 | -51.5902 | 2025-09-18 03:50:00 | GOES-19 | GUARACI | PARANÁ | Brasil | 4109203 | 41 | 33 | nan | nan | nan | Mata Atlântica | 95.0 |
| 373664f3-2028-3483-8a80-240c38067af0 | -18.5303 | -46.0414 | 2025-09-18 03:50:00 | GOES-19 | VARJÃO DE MINAS | MINAS GERAIS | Brasil | 3170750 | 31 | 33 | nan | nan | nan | Cerrado | 64.4 |
| 14618573-a0ac-3d78-a4e6-036dd06e97db | -11.3681 | -50.8486 | 2025-09-18 03:50:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 90.1 |
| 82b18068-e790-3c5c-865a-f8bde0ee485c | -11.3871 | -50.8465 | 2025-09-18 04:00:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 89.2 |
| b627d891-ee76-374d-a65d-04a0d26cfafa | -11.3874 | -50.8252 | 2025-09-18 04:00:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 92.8 |
| e69f78a0-b0e6-31d0-9e79-ff5d6f8635ad | -22.9714 | -51.5902 | 2025-09-18 04:00:00 | GOES-19 | GUARACI | PARANÁ | Brasil | 4109203 | 41 | 33 | nan | nan | nan | Mata Atlântica | 114.9 |
| fef62544-2030-3234-bc15-f706765d0eb2 | -19.0332 | -48.2773 | 2025-09-18 04:00:00 | GOES-19 | UBERLÂNDIA | MINAS GERAIS | Brasil | 3170206 | 31 | 33 | nan | nan | nan | Cerrado | 87.9 |
| e07014fc-c37a-3643-9ea0-50e5502eb5f3 | -11.3684 | -50.8273 | 2025-09-18 04:00:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 142.7 |
| ffd11de4-58a2-38db-88e5-f8ae3fef7f41 | -11.3681 | -50.8486 | 2025-09-18 04:00:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 144.2 |
| c0d1a640-2a07-3c27-bce8-cbbe2ec94f5f | -22.9504 | -51.5948 | 2025-09-18 04:00:00 | GOES-19 | GUARACI | PARANÁ | Brasil | 4109203 | 41 | 33 | nan | nan | nan | Mata Atlântica | 65.8 |
| e1e6a8f5-7682-3484-a6ec-9fa47019e295 | -22.9707 | -51.613 | 2025-09-18 04:10:00 | GOES-19 | GUARACI | PARANÁ | Brasil | 4109203 | 41 | 33 | nan | nan | nan | Mata Atlântica | 57.8 |
| 9d563a8d-e3c2-37d4-aede-4643c0e96a00 | -22.9504 | -51.5948 | 2025-09-18 04:10:00 | GOES-19 | GUARACI | PARANÁ | Brasil | 4109203 | 41 | 33 | nan | nan | nan | Mata Atlântica | 101.7 |
| e4575b70-0172-3b3a-85de-0f3433666f81 | -19.0332 | -48.2773 | 2025-09-18 04:10:00 | GOES-19 | UBERLÂNDIA | MINAS GERAIS | Brasil | 3170206 | 31 | 33 | nan | nan | nan | Cerrado | 113.1 |
| adc22932-12dc-3460-8df5-154bc2ab5c2e | -22.9714 | -51.5902 | 2025-09-18 04:10:00 | GOES-19 | GUARACI | PARANÁ | Brasil | 4109203 | 41 | 33 | nan | nan | nan | Mata Atlântica | 153.4 |
| 0927f940-efbd-3feb-99d4-ee1dd08edc3f | -5.87707 | -45.74885 | 2025-09-18 04:12:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 6881111a-48ca-38f5-8336-80dc33ef8755 | -3.45005 | -44.14296 | 2025-09-18 04:12:00 | NOAA-20 | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |


[Clique aqui para ver as próximas entradas](README8.md)
