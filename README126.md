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

## Dados Diários - Página 126

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 2a1e7336-6e22-32fe-8cd8-36a88d24f0ce | -11.82642 | -42.51871 | 2024-10-25 15:33:00 | NPP-375 | IPUPIARA | BAHIA | Brasil | 2914109 | 29 | 33 | nan | nan | nan | Caatinga | 5.4 |
| 1486eb37-c6db-3efc-aa98-fce4ae2521ae | -11.6912 | -42.54089 | 2024-10-25 15:33:00 | NPP-375 | GENTIO DO OURO | BAHIA | Brasil | 2911303 | 29 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 37260141-a3ef-3f8c-b34a-6807a3a42667 | -11.51567 | -42.43562 | 2024-10-25 15:33:00 | NPP-375 | GENTIO DO OURO | BAHIA | Brasil | 2911303 | 29 | 33 | nan | nan | nan | Caatinga | 18.5 |
| fcd78c04-a148-3054-828c-80664490be81 | -11.3534 | -41.88714 | 2024-10-25 15:33:00 | NPP-375 | IRECÊ | BAHIA | Brasil | 2914604 | 29 | 33 | nan | nan | nan | Caatinga | 2.4 |
| b3c0a244-f33e-359d-95d8-00e981676c1e | -11.326 | -41.65264 | 2024-10-25 15:33:00 | NPP-375 | JOÃO DOURADO | BAHIA | Brasil | 2918357 | 29 | 33 | nan | nan | nan | Caatinga | 19.0 |
| 8d965aa8-23bb-3795-b52a-5bca5e78e0e9 | -11.32544 | -41.64786 | 2024-10-25 15:33:00 | NPP-375 | JOÃO DOURADO | BAHIA | Brasil | 2918357 | 29 | 33 | nan | nan | nan | Caatinga | 57.7 |
| 41ef8f41-c45c-347b-a082-4243d34f6b4b | -11.32488 | -41.64308 | 2024-10-25 15:33:00 | NPP-375 | JOÃO DOURADO | BAHIA | Brasil | 2918357 | 29 | 33 | nan | nan | nan | Caatinga | 57.7 |
| 8a533998-37aa-344b-8346-b0e8e211d299 | -4.91933 | -41.97737 | 2024-10-25 15:33:00 | NPP-375 | JATOBÁ DO PIAUÍ | PIAUÍ | Brasil | 2205276 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| 89cd2e98-edc4-357b-9191-9f540564f773 | -4.91877 | -41.97337 | 2024-10-25 15:33:00 | NPP-375 | JATOBÁ DO PIAUÍ | PIAUÍ | Brasil | 2205276 | 22 | 33 | nan | nan | nan | Caatinga | 5.8 |
| c0318f2b-8da1-31c8-b910-494f49d7d2c1 | -4.71204 | -41.97284 | 2024-10-25 15:33:00 | NPP-375 | CAMPO MAIOR | PIAUÍ | Brasil | 2202208 | 22 | 33 | nan | nan | nan | Caatinga | 11.1 |
| 8ea6f599-3c73-305a-91be-b811dfddfd37 | -4.71146 | -41.96876 | 2024-10-25 15:33:00 | NPP-375 | CAMPO MAIOR | PIAUÍ | Brasil | 2202208 | 22 | 33 | nan | nan | nan | Caatinga | 21.5 |
| 6f8e748d-ac88-3be5-9815-602a41849f6e | -4.50588 | -41.97678 | 2024-10-25 15:33:00 | NPP-375 | CAPITÃO DE CAMPOS | PIAUÍ | Brasil | 2202406 | 22 | 33 | nan | nan | nan | Caatinga | 7.7 |
| b8199a76-f0c0-339a-8fd5-2ba0d9e86552 | -4.85812 | -42.47369 | 2024-10-25 15:33:00 | NPP-375 | JOSÉ DE FREITAS | PIAUÍ | Brasil | 2205508 | 22 | 33 | nan | nan | nan | Caatinga | 9.7 |
| 3141fe95-1989-33d9-b6ce-4de17df9b708 | -4.77457 | -42.41478 | 2024-10-25 15:33:00 | NPP-375 | JOSÉ DE FREITAS | PIAUÍ | Brasil | 2205508 | 22 | 33 | nan | nan | nan | Caatinga | 6.9 |
| 18680466-6cba-344f-9541-5d1900d9cc35 | -4.72336 | -42.66208 | 2024-10-25 15:33:00 | NPP-375 | JOSÉ DE FREITAS | PIAUÍ | Brasil | 2205508 | 22 | 33 | nan | nan | nan | Caatinga | 6.0 |
| 57b5cad9-3952-37c8-a8a7-2974860a05de | -4.72131 | -42.66133 | 2024-10-25 15:33:00 | NPP-375 | JOSÉ DE FREITAS | PIAUÍ | Brasil | 2205508 | 22 | 33 | nan | nan | nan | Caatinga | 6.2 |
| b021490b-7e6c-3959-8480-1517c72d9bd7 | -4.7159 | -42.66656 | 2024-10-25 15:33:00 | NPP-375 | JOSÉ DE FREITAS | PIAUÍ | Brasil | 2205508 | 22 | 33 | nan | nan | nan | Caatinga | 11.1 |
| 5c2318d5-abd3-3e2a-9dd5-e5e6b36695c4 | -4.71527 | -42.66209 | 2024-10-25 15:33:00 | NPP-375 | JOSÉ DE FREITAS | PIAUÍ | Brasil | 2205508 | 22 | 33 | nan | nan | nan | Caatinga | 6.2 |
| 295ca4eb-557a-326b-af90-f90efaba173d | -4.50645 | -41.98077 | 2024-10-25 15:33:00 | NPP-375 | CAPITÃO DE CAMPOS | PIAUÍ | Brasil | 2202406 | 22 | 33 | nan | nan | nan | Caatinga | 7.7 |
| e9f8561f-a3de-3e54-a92c-88a805bd8590 | -6.58577 | -42.24414 | 2024-10-25 15:33:00 | NPP-375 | VÁRZEA GRANDE | PIAUÍ | Brasil | 2211407 | 22 | 33 | nan | nan | nan | Caatinga | 9.4 |
| 21807485-6bd4-3aac-a67a-f954ce8aea49 | -6.50582 | -42.35155 | 2024-10-25 15:33:00 | NPP-375 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 7.7 |
| 0193e6f8-a932-3d2d-a5ac-da84a3499d07 | -6.50522 | -42.34691 | 2024-10-25 15:33:00 | NPP-375 | FRANCINÓPOLIS | PIAUÍ | Brasil | 2204006 | 22 | 33 | nan | nan | nan | Caatinga | 12.9 |
| 20c77273-b19d-39b7-87d1-c7bbf8c1cbf5 | -6.50508 | -42.35061 | 2024-10-25 15:33:00 | NPP-375 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 10.5 |
| cf571a36-2668-3212-be6e-d14e72242849 | -6.50445 | -42.34599 | 2024-10-25 15:33:00 | NPP-375 | FRANCINÓPOLIS | PIAUÍ | Brasil | 2204006 | 22 | 33 | nan | nan | nan | Caatinga | 14.2 |
| 32c5aad9-fbfc-3ef9-ab96-f687832d05e7 | -6.36058 | -42.93074 | 2024-10-25 15:33:00 | NPP-375 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 8.8 |
| 082022fc-7460-3f67-9fa1-52e2ce67e6db | -6.3599 | -42.92579 | 2024-10-25 15:33:00 | NPP-375 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 6.5 |
| 9ecf48e0-ecd3-3e31-b9d1-9310cc9f9ec7 | -6.35689 | -42.92768 | 2024-10-25 15:33:00 | NPP-375 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 8.0 |
| 99a225e9-8ca2-3e39-adaa-3d041c5c115f | -6.35626 | -42.92281 | 2024-10-25 15:33:00 | NPP-375 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 8.0 |
| 9e618eff-6db9-31c2-8289-d63871af4802 | -6.35361 | -42.92646 | 2024-10-25 15:33:00 | NPP-375 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 6.5 |
| d9f1c182-0315-3acf-b433-d5adefe9b900 | -6.35295 | -42.92163 | 2024-10-25 15:33:00 | NPP-375 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 6.5 |
| 0031fe1b-1b76-3812-aafe-0e7a530a9638 | -6.27848 | -42.65215 | 2024-10-25 15:33:00 | NPP-375 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 17.2 |
| cff770b2-2e88-347f-bff9-42be71dd7b7d | -6.04522 | -42.7232 | 2024-10-25 15:33:00 | NPP-375 | SANTO ANTÔNIO DOS MILAGRES | PIAUÍ | Brasil | 2209450 | 22 | 33 | nan | nan | nan | Caatinga | 3.7 |
| 6966332c-8680-3151-bb8e-b4c8a9d10277 | -5.95331 | -43.27931 | 2024-10-25 15:33:00 | NPP-375 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 12.4 |
| 884ecbd9-9bb9-3e2e-a20d-8af2dd82655b | -5.9051 | -42.42417 | 2024-10-25 15:33:00 | NPP-375 | PASSAGEM FRANCA DO PIAUÍ | PIAUÍ | Brasil | 2207751 | 22 | 33 | nan | nan | nan | Caatinga | 3.7 |
| f75e59d2-f1fc-36fc-a779-3645cac44e95 | -5.89908 | -42.42508 | 2024-10-25 15:33:00 | NPP-375 | PASSAGEM FRANCA DO PIAUÍ | PIAUÍ | Brasil | 2207751 | 22 | 33 | nan | nan | nan | Caatinga | 4.1 |
| ab14751f-748f-3b9d-9535-d398ac345613 | -5.77746 | -42.63324 | 2024-10-25 15:33:00 | NPP-375 | AGRICOLÂNDIA | PIAUÍ | Brasil | 2200103 | 22 | 33 | nan | nan | nan | Caatinga | 4.3 |
| 20db9ecc-b1ac-3732-834f-2aae1add4aae | -5.71191 | -42.78501 | 2024-10-25 15:33:00 | NPP-375 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 4.6 |
| 840de702-05fe-3b46-8fe9-ac964320bc4c | -5.71079 | -42.78639 | 2024-10-25 15:33:00 | NPP-375 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 3.7 |
| 105c03ab-f547-326a-8464-9940c18a3b2a | -5.69531 | -42.48485 | 2024-10-25 15:33:00 | NPP-375 | PASSAGEM FRANCA DO PIAUÍ | PIAUÍ | Brasil | 2207751 | 22 | 33 | nan | nan | nan | Caatinga | 3.2 |
| 898d6e2d-a157-3bb4-90de-5279c27cd5d4 | -6.34828 | -42.8874 | 2024-10-25 15:33:00 | NPP-375 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 8.9 |
| 93b0e8f9-63fc-351d-829b-37638f52cbc4 | -6.34762 | -42.88257 | 2024-10-25 15:33:00 | NPP-375 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 8.9 |
| 3f0c05a3-f1e5-37f8-9c5c-b57563088355 | -6.34619 | -42.89418 | 2024-10-25 15:33:00 | NPP-375 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 10.5 |
| 4259dcc0-f6fe-3e7c-a57f-cfbca577fc00 | -6.34555 | -42.88929 | 2024-10-25 15:33:00 | NPP-375 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 01c3c3b8-0579-34f1-85d8-3083a23a2962 | -6.34493 | -42.88447 | 2024-10-25 15:33:00 | NPP-375 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 7.5 |
| be22be77-783c-3c18-980a-cddd3da338b5 | -6.34431 | -42.87968 | 2024-10-25 15:33:00 | NPP-375 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 12.0 |
| 42e1374b-d5bc-3cab-b4f0-cfb2bd66eb91 | -6.34336 | -42.89804 | 2024-10-25 15:33:00 | NPP-375 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 7.5 |
| df5f969a-e187-3203-b1e9-3820ac233327 | -6.34138 | -42.88349 | 2024-10-25 15:33:00 | NPP-375 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 9.8 |
| 8956363f-d9f1-3b89-b5c9-766c6b09722f | -6.19325 | -43.11055 | 2024-10-25 15:33:00 | NPP-375 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 19caeaf8-e949-351c-bebd-5a4f42271dfe | -5.59335 | -41.86251 | 2024-10-25 15:33:00 | NPP-375 | SÃO JOÃO DA SERRA | PIAUÍ | Brasil | 2209906 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 5be14d91-0615-3016-8e19-116802836335 | -5.59279 | -41.85836 | 2024-10-25 15:33:00 | NPP-375 | SÃO JOÃO DA SERRA | PIAUÍ | Brasil | 2209906 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| b104f131-9909-3747-b779-c2d8160dafe5 | -5.5881 | -41.86322 | 2024-10-25 15:33:00 | NPP-375 | SÃO JOÃO DA SERRA | PIAUÍ | Brasil | 2209906 | 22 | 33 | nan | nan | nan | Caatinga | 4.4 |
| b2842e6e-564a-3bce-8ab8-3f476155bfb9 | -5.58755 | -41.86327 | 2024-10-25 15:33:00 | NPP-375 | SÃO JOÃO DA SERRA | PIAUÍ | Brasil | 2209906 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 570ff111-cb3d-3e7b-b149-047140335c09 | -5.47919 | -41.97301 | 2024-10-25 15:33:00 | NPP-375 | SÃO JOÃO DA SERRA | PIAUÍ | Brasil | 2209906 | 22 | 33 | nan | nan | nan | Caatinga | 7.6 |
| 67e965fd-a901-33e4-a6dd-e309b270e79c | -5.47892 | -41.97348 | 2024-10-25 15:33:00 | NPP-375 | SÃO JOÃO DA SERRA | PIAUÍ | Brasil | 2209906 | 22 | 33 | nan | nan | nan | Caatinga | 5.7 |
| cde94a4d-cf82-3f6e-8ed6-fa2cba088903 | -5.4786 | -41.96884 | 2024-10-25 15:33:00 | NPP-375 | SÃO JOÃO DA SERRA | PIAUÍ | Brasil | 2209906 | 22 | 33 | nan | nan | nan | Caatinga | 14.1 |
| 6f57caf2-bda5-3074-b655-6ec324672c38 | -5.47836 | -41.96931 | 2024-10-25 15:33:00 | NPP-375 | SÃO JOÃO DA SERRA | PIAUÍ | Brasil | 2209906 | 22 | 33 | nan | nan | nan | Caatinga | 14.9 |
| fd13e072-0e6a-3326-80bb-615e3cb2c4f8 | -5.40911 | -41.89479 | 2024-10-25 15:33:00 | NPP-375 | SÃO JOÃO DA SERRA | PIAUÍ | Brasil | 2209906 | 22 | 33 | nan | nan | nan | Caatinga | 3.6 |
| 2fa68921-68e0-32ec-bf47-6650bc2d6f78 | -5.22395 | -41.79521 | 2024-10-25 15:33:00 | NPP-375 | CASTELO DO PIAUÍ | PIAUÍ | Brasil | 2202604 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| c83ebdb8-dd32-352e-8078-c165468aa329 | -5.26246 | -42.96078 | 2024-10-25 15:33:00 | NPP-375 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Caatinga | 12.5 |
| 59749c45-e7a7-3678-84cf-93327b19bad0 | -5.25695 | -42.96654 | 2024-10-25 15:33:00 | NPP-375 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Caatinga | 12.1 |
| a27489bb-f447-351e-9143-3d7997065508 | -5.2833 | -43.06577 | 2024-10-25 15:33:00 | NPP-375 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 13.7 |
| a29d7abb-bd4d-333c-accd-e4dca8e5fddb | -5.23049 | -43.19295 | 2024-10-25 15:33:00 | NPP-375 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 7fe308d6-e6af-3389-b156-13f410bbb0cc | -5.2055 | -43.17897 | 2024-10-25 15:33:00 | NPP-375 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 9.1 |
| 3aae34bb-b954-3372-881e-36eaa878fb08 | -5.0668 | -43.16911 | 2024-10-25 15:33:00 | NPP-375 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| a24baca1-de15-38e6-a20e-0fcef693e226 | -7.42925 | -42.32255 | 2024-10-25 15:33:00 | NPP-375 | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 5.6 |
| 68750496-7d46-33cf-9096-ec6cba4defa6 | -7.42882 | -42.32124 | 2024-10-25 15:33:00 | NPP-375 | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 6.9 |
| 68d14d73-eb2e-38be-85ab-01c6b0e7f069 | -7.19215 | -42.90748 | 2024-10-25 15:33:00 | NPP-375 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 3.5 |
| cbbd537a-ffc5-3bc3-8fba-6d9b82f35b68 | -7.18986 | -42.90577 | 2024-10-25 15:33:00 | NPP-375 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 3.3 |
| e8960688-7bf0-3013-a854-612659e1b7ef | -6.82405 | -43.27997 | 2024-10-25 15:33:00 | NPP-375 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 4.0 |
| f2756dc0-f11b-3444-adff-8dbef70a6e05 | -6.82365 | -43.27761 | 2024-10-25 15:33:00 | NPP-375 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 5.2 |
| a2a2d953-821e-364a-94c7-e842fdbdfaa5 | -6.5902 | -42.24708 | 2024-10-25 15:33:00 | NPP-375 | VÁRZEA GRANDE | PIAUÍ | Brasil | 2211407 | 22 | 33 | nan | nan | nan | Caatinga | 9.8 |
| f3656773-782d-3e5c-b6f4-bf3107a3cc2c | -6.55767 | -43.20848 | 2024-10-25 15:33:00 | NPP-375 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Caatinga | 11.5 |
| 62848a9d-b145-3f9b-95de-2869b9abf931 | -6.86041 | -43.50233 | 2024-10-25 15:33:00 | NPP-375 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 5ab1d4ce-5efd-341e-b1b6-a4230322492f | -6.67922 | -43.04034 | 2024-10-25 15:33:00 | NPP-375 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 5.8 |
| fc9c11d4-9ac0-3ae0-b21e-f4102aa73409 | -6.67591 | -43.04308 | 2024-10-25 15:33:00 | NPP-375 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 13.6 |
| 04b5938d-508e-3fa9-9796-a61a5bd6e158 | -6.67356 | -43.04623 | 2024-10-25 15:33:00 | NPP-375 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 56785436-50e5-30b0-ac65-b3bbe8b4c4ff | -6.67289 | -43.04123 | 2024-10-25 15:33:00 | NPP-375 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 9ae95812-65df-3f50-9d89-9de09b6745b7 | -6.65386 | -43.14133 | 2024-10-25 15:33:00 | NPP-375 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 707199fd-2659-31bc-b264-27fe2f55a5d0 | -6.65319 | -43.13625 | 2024-10-25 15:33:00 | NPP-375 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 7.2 |
| de1d0130-36e7-33cd-b8ef-f612776b0cb3 | -6.60104 | -43.48679 | 2024-10-25 15:33:00 | NPP-375 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 3723d2be-1eda-3d83-a8af-1c66a74b2f99 | -6.49944 | -43.03541 | 2024-10-25 15:33:00 | NPP-375 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| dc930cae-7470-3627-8421-9a556d8f9717 | -6.49615 | -43.03553 | 2024-10-25 15:33:00 | NPP-375 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 658f71f0-47d7-339e-80bb-933d126b5dcf | -6.4504 | -43.24798 | 2024-10-25 15:33:00 | NPP-375 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 76adfd2d-5456-3af3-b0e8-ced0b796cf6d | -6.44398 | -43.24871 | 2024-10-25 15:33:00 | NPP-375 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 38679a6a-8d20-34a5-bf3e-e2a2546eeb66 | -7.99855 | -42.35471 | 2024-10-25 15:33:00 | NPP-375 | PEDRO LAURENTINO | PIAUÍ | Brasil | 2207934 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| 9e772890-df6b-3135-a95c-2f3d914d4dcc | -7.67394 | -42.87188 | 2024-10-25 15:33:00 | NPP-375 | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 3.9 |
| 3bb1c4a0-7856-3d49-99e4-11a53b06c376 | -7.67329 | -42.86678 | 2024-10-25 15:33:00 | NPP-375 | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 3.9 |
| dc13d7b3-725f-3867-b11b-8366d048aa40 | -9.36621 | -43.37864 | 2024-10-25 15:33:00 | NPP-375 | CAMPO ALEGRE DE LOURDES | BAHIA | Brasil | 2905909 | 29 | 33 | nan | nan | nan | Caatinga | 24.1 |
| 8d7d6cd8-dd76-3c1d-a753-7d4a1b82f404 | -9.36552 | -43.3728 | 2024-10-25 15:33:00 | NPP-375 | CAMPO ALEGRE DE LOURDES | BAHIA | Brasil | 2905909 | 29 | 33 | nan | nan | nan | Caatinga | 30.3 |
| 37927dc5-57db-3580-ac32-86ead5f211d3 | -9.36393 | -43.38168 | 2024-10-25 15:33:00 | NPP-375 | CAMPO ALEGRE DE LOURDES | BAHIA | Brasil | 2905909 | 29 | 33 | nan | nan | nan | Caatinga | 30.9 |
| eab58058-2ba1-30ad-a427-638ea53c386f | 2.0529 | -50.8803 | 2024-10-25 15:34:54 | GOES-16 | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 72.1 |
| ba7d57c7-6a1f-3c89-a365-bb1cd5dc20f9 | 2.0345 | -50.8806 | 2024-10-25 15:34:54 | GOES-16 | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 72.4 |
| 1a447936-f168-3b0f-8a1d-64f6070e0dce | 1.8143 | -50.4883 | 2024-10-25 15:34:55 | GOES-16 | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 60.4 |
| c93145ea-d3ea-3854-a35d-39524bead41e | 1.8144 | -50.4673 | 2024-10-25 15:34:55 | GOES-16 | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 76.4 |
| 388e40a5-77a5-3024-b49a-c8cfb7a84bfa | -3.5506 | -43.99789 | 2024-10-25 15:35:00 | NPP-375 | VARGEM GRANDE | MARANHÃO | Brasil | 2112704 | 21 | 33 | nan | nan | nan | Cerrado | 15.4 |
| 9cef58e8-7109-3c24-92e8-6b9da48729c6 | -3.52367 | -43.62193 | 2024-10-25 15:35:00 | NPP-375 | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 20.0 |
| 1d305c3d-724d-3d2c-a149-fb697fcdd0a7 | -3.52294 | -43.61681 | 2024-10-25 15:35:00 | NPP-375 | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 43.2 |
| dc0753eb-266b-331a-9225-d021962a3377 | -3.52088 | -43.62075 | 2024-10-25 15:35:00 | NPP-375 | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 29.2 |
| b695c6ec-aafa-3c36-b9b4-db88e8e02ab0 | -3.52012 | -43.61563 | 2024-10-25 15:35:00 | NPP-375 | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 36.3 |
| 836a4d08-abd1-3f26-9bd7-7611a26ce9db | -3.30997 | -43.51828 | 2024-10-25 15:35:00 | NPP-375 | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 11.7 |


[Clique aqui para ver as próximas entradas](README127.md)
