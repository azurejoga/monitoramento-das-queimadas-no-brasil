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
| f28481f0-b0ae-3747-a531-3d683ad58a4a | -5.26302 | -49.29283 | 2025-11-06 00:13:00 | TERRA_M-M | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 9.3 |
| b3cee960-48ab-3970-bb6e-2c200754b49f | -6.98245 | -39.07865 | 2025-11-06 00:13:00 | TERRA_M-M | AURORA | CEARÁ | Brasil | 2301703 | 23 | 33 | nan | nan | nan | Caatinga | 13.4 |
| 19ed3fd4-d6fc-3e0f-9d9d-7c489f6503dc | -5.15967 | -41.26549 | 2025-11-06 00:13:00 | TERRA_M-M | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 15.5 |
| 5ec3346e-cfc6-3c47-9358-9aa36d6c9d8f | -4.60032 | -46.0092 | 2025-11-06 00:13:00 | TERRA_M-M | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 8.8 |
| a49e61df-6cca-3bbe-a06f-fa1b2c46d9d3 | -6.20028 | -43.28083 | 2025-11-06 00:13:00 | TERRA_M-M | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 3e2915cf-0509-3e35-ae31-c90db1736fab | -10.07683 | -42.74207 | 2025-11-06 00:13:00 | TERRA_M-M | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 7.3 |
| e5eafa65-db12-3a14-9d8a-ed9de12a0f2d | -7.38714 | -46.5913 | 2025-11-06 00:13:00 | TERRA_M-M | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 8.0 |
| b389dedd-ac31-34b9-a667-6e0fe53d8d10 | -6.54397 | -43.10633 | 2025-11-06 00:13:00 | TERRA_M-M | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 55328bab-3ac9-3e00-a0d2-2c731259c796 | -7.17164 | -38.35151 | 2025-11-06 00:13:00 | TERRA_M-M | SERRA GRANDE | PARAÍBA | Brasil | 2515708 | 25 | 33 | nan | nan | nan | Caatinga | 23.4 |
| 96f8461e-2a83-3479-a91d-7caf88875803 | -7.46724 | -44.54873 | 2025-11-06 00:13:00 | TERRA_M-M | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 70e4985b-3f35-3db3-ada4-1f168dbc0023 | -7.08448 | -45.51666 | 2025-11-06 00:13:00 | TERRA_M-M | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 11.8 |
| 81969539-593c-3ab7-94b6-7d62cb5441ad | -5.20416 | -46.1725 | 2025-11-06 00:13:00 | TERRA_M-M | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 10.6 |
| 6f228397-c703-3478-858d-85491e178f1a | -6.45024 | -39.12252 | 2025-11-06 00:13:00 | TERRA_M-M | ICÓ | CEARÁ | Brasil | 2305407 | 23 | 33 | nan | nan | nan | Caatinga | 19.6 |
| 8433d8e0-3d52-31c7-86a9-79b1fb78c5b5 | -5.46238 | -47.72993 | 2025-11-06 00:13:00 | TERRA_M-M | PRAIA NORTE | TOCANTINS | Brasil | 1718303 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 8fccdbb2-92bd-3358-92a0-16ce18376c9c | -4.75928 | -45.95681 | 2025-11-06 00:13:00 | TERRA_M-M | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 5.4 |
| ba9d521e-2f8d-3dc8-a7b7-afc78e48992d | -4.96997 | -47.77511 | 2025-11-06 00:13:00 | TERRA_M-M | CIDELÂNDIA | MARANHÃO | Brasil | 2103257 | 21 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 74ecc23e-807a-32cb-bea2-77b1f0e680ae | -4.71455 | -46.43327 | 2025-11-06 00:13:00 | TERRA_M-M | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 11.5 |
| eec05ff8-0c42-3f8e-ba2a-dbd407672520 | -7.90734 | -44.33717 | 2025-11-06 00:13:00 | TERRA_M-M | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 15.8 |
| 6baf6aec-3da9-3c7b-a9ab-f8a1fc6ec687 | -4.54838 | -45.22876 | 2025-11-06 00:13:00 | TERRA_M-M | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Amazônia | 7.6 |
| 90aee348-aba4-3709-b8c7-90e20183a5e7 | -4.68317 | -44.80822 | 2025-11-06 00:13:00 | TERRA_M-M | IGARAPÉ GRANDE | MARANHÃO | Brasil | 2105203 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 4359da39-be76-3c1c-894d-f116824d4379 | -5.3995 | -43.93496 | 2025-11-06 00:13:00 | TERRA_M-M | GOVERNADOR EUGÊNIO BARROS | MARANHÃO | Brasil | 2104602 | 21 | 33 | nan | nan | nan | Cerrado | 14.8 |
| d5291574-6c98-3fa5-9b80-63e7d8f4cac7 | -7.47485 | -44.53859 | 2025-11-06 00:13:00 | TERRA_M-M | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 236.0 |
| ba243970-b5c2-349b-b917-c7a9b7da824e | -5.15094 | -41.28018 | 2025-11-06 00:13:00 | TERRA_M-M | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 48.6 |
| 62f2bbed-6a1f-37c4-81a0-6c6c84523cda | -5.25139 | -45.779 | 2025-11-06 00:13:00 | TERRA_M-M | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | 16.8 |
| 19844e2c-2c8b-34ff-86fa-fa04f150f693 | -5.4152 | -45.76171 | 2025-11-06 00:13:00 | TERRA_M-M | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | 11.7 |
| c1172adf-6775-37bb-b52f-62754c5af579 | -7.44293 | -37.89442 | 2025-11-06 00:13:00 | TERRA_M-M | SANTANA DOS GARROTES | PARAÍBA | Brasil | 2513604 | 25 | 33 | nan | nan | nan | Caatinga | 54.3 |
| a556e6b7-3735-363b-bf67-e05938638259 | -5.27058 | -44.59039 | 2025-11-06 00:13:00 | TERRA_M-M | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 0aa8197a-7edf-3d51-ac72-e695de3249ec | -4.87614 | -47.54935 | 2025-11-06 00:13:00 | TERRA_M-M | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 36.7 |
| c60572c8-e5dd-348b-989a-398a7164b618 | -4.57925 | -43.34332 | 2025-11-06 00:13:00 | TERRA_M-M | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 17.8 |
| 07c0da2c-6ddf-3d41-b342-345454b9c261 | -7.48246 | -44.52843 | 2025-11-06 00:13:00 | TERRA_M-M | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 8.2 |
| 73409e46-6c52-3859-92c6-d435921f3d81 | -5.13954 | -41.2339 | 2025-11-06 00:13:00 | TERRA_M-M | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 17.4 |
| 508d9ff4-c759-3ccc-add2-bfdb68e6dc1f | -4.718 | -46.52504 | 2025-11-06 00:13:00 | TERRA_M-M | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 32e2567a-4e08-3cb0-8f80-8e18c4b07a8c | -5.14299 | -41.22691 | 2025-11-06 00:13:00 | TERRA_M-M | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 12.8 |
| 1cca786a-0ec7-3c76-9f90-ef57cd88cabf | -4.64595 | -45.67315 | 2025-11-06 00:13:00 | TERRA_M-M | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 25.8 |
| 341caa32-70cd-37f1-bf9a-b19a09a22fa9 | -9.42725 | -43.61704 | 2025-11-06 00:13:00 | TERRA_M-M | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 4.6 |
| c90f588f-8614-3f36-958e-d0345a4f40d8 | -4.74707 | -46.60402 | 2025-11-06 00:13:00 | TERRA_M-M | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 16.0 |
| 36a793db-bfa7-31d1-8912-1d8bc2593b27 | -7.90187 | -45.56584 | 2025-11-06 00:13:00 | TERRA_M-M | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 9a3854df-6bee-3db7-980a-9e66ad2e9c83 | -7.5014 | -44.53477 | 2025-11-06 00:13:00 | TERRA_M-M | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 99.7 |
| 7a8d335c-e0d4-3a64-8e6e-ae45bf3dc31b | -5.75927 | -40.81368 | 2025-11-06 00:13:00 | TERRA_M-M | QUITERIANÓPOLIS | CEARÁ | Brasil | 2311264 | 23 | 33 | nan | nan | nan | Caatinga | 56.0 |
| c2ea085b-3373-34b3-aaed-345a8165b1dc | -4.59943 | -43.3506 | 2025-11-06 00:13:00 | TERRA_M-M | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 10.1 |
| 99b8edd1-2bd6-3308-98aa-008711b562ca | -6.28613 | -44.73369 | 2025-11-06 00:13:00 | TERRA_M-M | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 15.7 |
| eae15496-e427-3b8d-87d6-8d6c25e8b601 | -6.0688 | -43.2524 | 2025-11-06 00:13:00 | TERRA_M-M | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 5.7 |
| 54d4e55d-2448-31ef-b02e-f3fbbdf8c81d | -7.2365 | -46.02144 | 2025-11-06 00:13:00 | TERRA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 8a7f52bb-180e-3dfb-b43d-eb64eeac19f0 | -5.69544 | -46.00029 | 2025-11-06 00:13:00 | TERRA_M-M | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 6d527033-5081-3ab8-a822-5f5ee3b06af0 | -5.46003 | -44.36718 | 2025-11-06 00:13:00 | TERRA_M-M | GRAÇA ARANHA | MARANHÃO | Brasil | 2104701 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| fe777c11-a24b-394d-be13-5e0e31564a20 | -5.31938 | -44.34728 | 2025-11-06 00:13:00 | TERRA_M-M | GRAÇA ARANHA | MARANHÃO | Brasil | 2104701 | 21 | 33 | nan | nan | nan | Cerrado | 13.1 |
| 5e88dfd9-33f2-3d5b-9ffb-6d35647d2f00 | -4.72031 | -41.33409 | 2025-11-06 00:13:00 | TERRA_M-M | MILTON BRANDÃO | PIAUÍ | Brasil | 2206357 | 22 | 33 | nan | nan | nan | Caatinga | 12.5 |
| e33a30e1-6ac5-32e8-ab4c-4815265bd430 | -5.2427 | -44.39186 | 2025-11-06 00:13:00 | TERRA_M-M | PRESIDENTE DUTRA | MARANHÃO | Brasil | 2109106 | 21 | 33 | nan | nan | nan | Cerrado | 14.2 |
| 3b140c06-7572-3a5a-a096-aa63544a5de1 | -7.47857 | -44.56524 | 2025-11-06 00:13:00 | TERRA_M-M | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 6.1 |
| c7e113ca-661c-3c4d-abdd-0cb0bb822c5d | -4.5991 | -46.00036 | 2025-11-06 00:13:00 | TERRA_M-M | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 23.8 |
| 8f022a5f-e312-34b3-bfeb-2ac38667c079 | -7.46848 | -44.55761 | 2025-11-06 00:13:00 | TERRA_M-M | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 9.2 |
| d9e4e2af-680d-39b0-92d9-431f1f24b72e | -5.14698 | -41.25365 | 2025-11-06 00:13:00 | TERRA_M-M | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 97.7 |
| 7f002172-1c1e-3b48-b05f-1ada3eae5fd3 | -5.42657 | -40.66155 | 2025-11-06 00:13:00 | TERRA_M-M | CRATEÚS | CEARÁ | Brasil | 2304103 | 23 | 33 | nan | nan | nan | Caatinga | 21.2 |
| f4f86c98-1af9-3c1b-88a3-fd8e79623029 | -5.14521 | -41.2738 | 2025-11-06 00:13:00 | TERRA_M-M | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 45.6 |
| 8e362e93-ca58-3c62-a3ab-5fb6d78c20b1 | -4.59804 | -43.34061 | 2025-11-06 00:13:00 | TERRA_M-M | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 926.1 |
| 7a54fb53-0d45-3a8f-8fb2-5c35cdc11540 | -8.01995 | -45.01831 | 2025-11-06 00:13:00 | TERRA_M-M | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 12.8 |
| 2b5a3890-8786-318e-b95a-9ab2c3fb97d6 | -7.09334 | -45.5154 | 2025-11-06 00:13:00 | TERRA_M-M | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 10.6 |
| a9961211-e145-3dcc-af2b-743dea515cfb | -4.60276 | -46.55601 | 2025-11-06 00:13:00 | TERRA_M-M | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 10.3 |
| 6942517e-21cf-3b23-8566-b26c713fc941 | -6.26543 | -43.67284 | 2025-11-06 00:13:00 | TERRA_M-M | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 11.3 |
| cc303c36-7b71-3bf8-8a0e-49f6737d051d | -6.20814 | -43.26966 | 2025-11-06 00:13:00 | TERRA_M-M | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 9e97b5b1-63da-3183-b406-b4d6ca376a55 | -6.46258 | -39.12019 | 2025-11-06 00:13:00 | TERRA_M-M | ICÓ | CEARÁ | Brasil | 2305407 | 23 | 33 | nan | nan | nan | Caatinga | 13.5 |
| 13f64292-88d1-3c67-9dc5-cb56d8342ef2 | -7.49131 | -44.52716 | 2025-11-06 00:13:00 | TERRA_M-M | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 8.3 |
| b2f5eeb7-9fa8-30e1-803e-681bb46a5110 | -5.53509 | -41.09076 | 2025-11-06 00:13:00 | TERRA_M-M | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 8.3 |
| 5ffbd5d9-43ef-347b-8f10-4a4372ef5b1e | -4.45234 | -43.23388 | 2025-11-06 00:13:00 | TERRA_M-M | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 8b1f0528-db38-3da8-b449-3668d561a7d3 | -7.83286 | -40.84563 | 2025-11-06 00:13:00 | TERRA_M-M | CURRAL NOVO DO PIAUÍ | PIAUÍ | Brasil | 2203271 | 22 | 33 | nan | nan | nan | Caatinga | 8.4 |
| f6546a53-bf47-391f-b1db-52e9f939627a | -7.50263 | -44.54365 | 2025-11-06 00:13:00 | TERRA_M-M | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 36c882af-ae78-3407-a868-16f1e43ac7a2 | -4.85833 | -40.63301 | 2025-11-06 00:13:00 | TERRA_M-M | IPAPORANGA | CEARÁ | Brasil | 2305654 | 23 | 33 | nan | nan | nan | Caatinga | 11.9 |
| cbe21105-883b-3555-a1ee-009fe5713feb | -4.7038 | -46.55466 | 2025-11-06 00:13:00 | TERRA_M-M | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 6.0 |
| c2f372bd-74f6-344a-ab8c-39509de54ad4 | -4.64209 | -46.31183 | 2025-11-06 00:13:00 | TERRA_M-M | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 14f63d80-ee3b-3620-a8c8-678a08bfda2d | -6.55327 | -43.10494 | 2025-11-06 00:13:00 | TERRA_M-M | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 8.9 |
| e17aa8e8-8cf4-3951-ace8-846608dec218 | -4.45969 | -44.8521 | 2025-11-06 00:13:00 | TERRA_M-M | LAGO DO JUNCO | MARANHÃO | Brasil | 2105807 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 347501d5-9b11-3acd-8a59-0023340e89e1 | -7.93142 | -44.3155 | 2025-11-06 00:13:00 | TERRA_M-M | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 5.2 |
| d25a6ff8-4505-3c25-8e3c-8b2f9199115c | -4.71028 | -46.53526 | 2025-11-06 00:13:00 | TERRA_M-M | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 39.7 |
| f50dbd7c-3e8f-392c-8ed3-bdba40b44e13 | -6.23599 | -44.31192 | 2025-11-06 00:13:00 | TERRA_M-M | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 12.5 |
| 864e0de0-d488-340a-863f-350db924f54d | -5.93459 | -41.37876 | 2025-11-06 00:13:00 | TERRA_M-M | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 10.8 |
| ca379c4b-b05c-3718-b0da-55440733cd4b | -5.13632 | -41.25544 | 2025-11-06 00:13:00 | TERRA_M-M | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 11.0 |
| 8ab76737-5371-3bf4-9c6c-1ba280b25b99 | -5.92267 | -44.11544 | 2025-11-06 00:13:00 | TERRA_M-M | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 8.9 |
| 5c57dbfb-6d4b-3d51-b2e3-56646e438ef9 | -6.02224 | -39.06087 | 2025-11-06 00:13:00 | TERRA_M-M | ACOPIARA | CEARÁ | Brasil | 2300309 | 23 | 33 | nan | nan | nan | Caatinga | 14.0 |
| 21cb87d8-4e55-32db-ba6a-5d974e9eb571 | -5.25261 | -45.78786 | 2025-11-06 00:13:00 | TERRA_M-M | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| c906914c-f419-3d5b-bf56-941c3f6f931a | -4.97132 | -47.78517 | 2025-11-06 00:13:00 | TERRA_M-M | CIDELÂNDIA | MARANHÃO | Brasil | 2103257 | 21 | 33 | nan | nan | nan | Amazônia | 5.0 |
| f5dcc33b-d617-3ea7-beb6-0a0cfd72bc67 | -8.2511 | -44.49628 | 2025-11-06 00:13:00 | TERRA_M-M | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 6.1 |
| e0ad58bb-d39a-3f45-88b6-1a6bb23d5e29 | -4.73686 | -46.5962 | 2025-11-06 00:13:00 | TERRA_M-M | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 14.5 |
| c9b87a71-8454-3b04-b699-30c692c885bf | -5.19646 | -45.12118 | 2025-11-06 00:13:00 | TERRA_M-M | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 9308597d-ba07-3b22-95b0-41c9499acd5e | -4.4618 | -43.23252 | 2025-11-06 00:13:00 | TERRA_M-M | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 221.4 |
| f8ba8f51-538b-3de1-8f9b-b78838b7c630 | -5.27315 | -44.81509 | 2025-11-06 00:13:00 | TERRA_M-M | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 7.8 |
| cf45b9f1-e47a-31aa-ba42-7c2c3eb280a9 | -5.13441 | -41.24272 | 2025-11-06 00:13:00 | TERRA_M-M | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 11.2 |
| 048efc5d-7664-3428-b476-ecf779e42ffd | -4.45843 | -44.84317 | 2025-11-06 00:13:00 | TERRA_M-M | IGARAPÉ GRANDE | MARANHÃO | Brasil | 2105203 | 21 | 33 | nan | nan | nan | Cerrado | 5.6 |
| d0fbacc3-b3c2-3117-b221-a85b72836c3d | -6.47923 | -43.55226 | 2025-11-06 00:13:00 | TERRA_M-M | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 14.8 |
| 7d8b7bdc-a72c-33a9-a418-db825455001b | -4.47125 | -43.23114 | 2025-11-06 00:13:00 | TERRA_M-M | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 13.4 |
| 99833f8d-4e54-3d36-a6c2-08aaf97d7a25 | -6.26678 | -43.68239 | 2025-11-06 00:13:00 | TERRA_M-M | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 107.4 |
| 2805db00-3478-3984-9bf3-fa2d002c01c3 | -4.6609 | -44.51781 | 2025-11-06 00:13:00 | TERRA_M-M | PEDREIRAS | MARANHÃO | Brasil | 2108207 | 21 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 4fe0c95f-dae9-3ff0-a870-3efb8fb56e20 | -4.81812 | -43.52892 | 2025-11-06 00:13:00 | TERRA_M-M | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 9.7 |
| 50f5bcd1-7812-3379-9aa8-6039d0831da9 | -4.79316 | -45.13062 | 2025-11-06 00:13:00 | TERRA_M-M | POÇÃO DE PEDRAS | MARANHÃO | Brasil | 2108900 | 21 | 33 | nan | nan | nan | Cerrado | 36.3 |
| 1ec17dea-4c50-33dd-aff1-c2028e9444e2 | -4.59663 | -43.33057 | 2025-11-06 00:13:00 | TERRA_M-M | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 552.0 |
| 5db9dd21-7deb-3a25-98b7-a18bc9df69c6 | -7.90609 | -44.32825 | 2025-11-06 00:13:00 | TERRA_M-M | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 7.5 |
| c8458314-e450-3331-ba3f-b6f20c47b492 | -4.78431 | -45.13187 | 2025-11-06 00:13:00 | TERRA_M-M | POÇÃO DE PEDRAS | MARANHÃO | Brasil | 2108900 | 21 | 33 | nan | nan | nan | Cerrado | 77.2 |
| 06a6e38c-2652-3fd3-8739-42aca7291907 | -6.13273 | -41.61658 | 2025-11-06 00:13:00 | TERRA_M-M | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 6.6 |
| e47217ee-2121-3a0a-88c2-9f310623746c | -5.30835 | -41.02621 | 2025-11-06 00:13:00 | TERRA_M-M | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 7.7 |
| cb4118e5-af99-32b1-b0e0-ed412afb737e | -7.28766 | -45.45759 | 2025-11-06 00:13:00 | TERRA_M-M | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 14.3 |
| 96d418cb-b6de-3307-9725-569d72e75777 | -6.20588 | -43.70683 | 2025-11-06 00:13:00 | TERRA_M-M | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 7.2 |


[Clique aqui para ver as próximas entradas](README4.md)
