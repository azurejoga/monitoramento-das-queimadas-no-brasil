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

## Dados Diários - Página 144

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| d1cd2e57-fd2e-39ed-b0dc-4c849f779189 | -17.1584 | -57.3377 | 2024-10-07 07:16:43 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 103.6 |
| 8e9bb222-91c0-3b24-b7ac-90de6f8f3ad0 | -17.1777 | -57.3559 | 2024-10-07 07:16:43 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 90.7 |
| 3cbd6ea0-b00d-374d-8db9-e4f65788273e | -17.178 | -57.3354 | 2024-10-07 07:16:43 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 106.4 |
| 90f71c5a-b494-3a55-878b-b5fdb433a22f | -17.7918 | -53.8102 | 2024-10-07 07:16:46 | GOES-16 | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | 63.7 |
| 56c08d21-c191-3172-86e7-91cd9f305d2f | -20.3525 | -48.8186 | 2024-10-07 07:16:59 | GOES-16 | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 74.2 |
| 7b16fa65-e7b0-3571-ae85-5e738bebea1d | -20.5848 | -48.5137 | 2024-10-07 07:17:00 | GOES-16 | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Cerrado | 78.7 |
| f208275b-a6fd-3ff1-b5c6-399b0d3c9b22 | -21.605 | -47.9485 | 2024-10-07 07:17:05 | GOES-16 | RINCÃO | SÃO PAULO | Brasil | 3543709 | 35 | 33 | nan | nan | nan | Cerrado | 96.5 |
| bc7fad0e-4d30-3c1d-91dc-7d8f977755c3 | -21.5698 | -47.746 | 2024-10-07 07:17:05 | GOES-16 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 72.9 |
| ad902c70-867d-3177-bd8a-33f638a65c44 | -21.5843 | -47.9536 | 2024-10-07 07:17:05 | GOES-16 | GUATAPARÁ | SÃO PAULO | Brasil | 3518859 | 35 | 33 | nan | nan | nan | Cerrado | 57.7 |
| 4cb670dc-4761-30cd-b62e-335a1079118f | -21.5906 | -47.7409 | 2024-10-07 07:17:05 | GOES-16 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 114.9 |
| 912d0bc6-ec12-3881-a0ce-284a179fa175 | -21.5913 | -47.7172 | 2024-10-07 07:17:05 | GOES-16 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 83.3 |
| 80b5d284-a171-30e1-9a39-e6747351dd92 | -15.878 | -52.3003 | 2024-10-07 07:26:36 | GOES-16 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 92.0 |
| daf0e9fb-2b22-3e83-856c-d9503e86d581 | -16.5072 | -57.7387 | 2024-10-07 07:26:39 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 56.5 |
| a9adc1ca-8c37-3e54-8677-bbacf9cc3e7c | -16.6335 | -57.1328 | 2024-10-07 07:26:40 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 57.8 |
| d58113cf-7544-387c-9e3e-7da7509f4c05 | -16.6332 | -57.1533 | 2024-10-07 07:26:40 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 58.4 |
| 0509858c-c618-34fa-b2c1-af1a6fb5783f | -16.614 | -57.135 | 2024-10-07 07:26:40 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 54.2 |
| ae7c30a3-25a7-3e3d-b64f-5dfedf1b0c30 | -16.5267 | -57.7365 | 2024-10-07 07:26:40 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 63.6 |
| 65a33439-15d5-3633-b147-b751e6a6f644 | -17.0323 | -56.6543 | 2024-10-07 07:26:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 72.0 |
| abe17fb7-6866-3acf-9d5a-b41ace82d1d2 | -17.0319 | -56.6749 | 2024-10-07 07:26:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 229.4 |
| 94caa461-c631-36b3-8489-c435497d49fb | -17.0316 | -56.6956 | 2024-10-07 07:26:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 99.9 |
| 2f7e7a7c-8df5-32cc-be83-af0ac439a7e2 | -17.0127 | -56.6567 | 2024-10-07 07:26:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 74.4 |
| 9611c7d0-3b73-36ee-9caf-1e0788e2a972 | -17.0123 | -56.6773 | 2024-10-07 07:26:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 231.4 |
| ca8abfff-0443-3b90-9f55-8106aa6eaef8 | -17.012 | -56.698 | 2024-10-07 07:26:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 118.3 |
| 73201ae3-0677-34e6-9f62-39dd9225baed | -16.9744 | -56.5996 | 2024-10-07 07:26:42 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 94.2 |
| 1b7233e0-fb78-324c-84dc-75b36cba311d | -16.9741 | -56.6202 | 2024-10-07 07:26:42 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 75.3 |
| a024cbd2-dc9b-306f-b429-0820bdca2528 | -16.9721 | -56.744 | 2024-10-07 07:26:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 58.3 |
| 378554a0-ad1c-382c-897d-5b84b2908274 | -16.9717 | -56.7646 | 2024-10-07 07:26:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 77.9 |
| e6acf762-161c-30ff-bc49-0f3382f9125d | -17.178 | -57.3354 | 2024-10-07 07:26:43 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 115.1 |
| 843d6073-f268-3815-923f-ee334d009f65 | -17.1777 | -57.3559 | 2024-10-07 07:26:43 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 86.7 |
| d85e3230-be28-3b6a-8820-385425b15b14 | -17.1584 | -57.3377 | 2024-10-07 07:26:43 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 108.8 |
| 376c9c99-18a7-353d-a626-0110ab6dcfc6 | -17.1581 | -57.3582 | 2024-10-07 07:26:43 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 89.3 |
| 680648e2-9a14-3100-b016-d304c2dbd65e | -17.1375 | -57.4221 | 2024-10-07 07:26:43 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 53.1 |
| 00463483-fcc5-378c-a478-37da42072ca4 | -17.0982 | -57.4267 | 2024-10-07 07:26:43 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 74.4 |
| 700aa916-d60e-3a9f-9226-61a89595df9f | -17.0985 | -57.4062 | 2024-10-07 07:26:43 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 64.3 |
| 643ab899-5b35-3f5e-af14-3cd9265a20dc | -20.3525 | -48.8186 | 2024-10-07 07:26:59 | GOES-16 | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 66.8 |
| ec35609a-74d3-3863-b9d0-1612514ed74c | -21.3274 | -47.5939 | 2024-10-07 07:27:04 | GOES-16 | SERRA AZUL | SÃO PAULO | Brasil | 3551405 | 35 | 33 | nan | nan | nan | Cerrado | 53.1 |
| b21428da-8778-38be-acfe-0bd97ff5e76a | -21.605 | -47.9485 | 2024-10-07 07:27:05 | GOES-16 | RINCÃO | SÃO PAULO | Brasil | 3543709 | 35 | 33 | nan | nan | nan | Cerrado | 100.3 |
| 70bb3419-6cfe-3435-a66f-ea970f3f190d | -21.6043 | -47.9721 | 2024-10-07 07:27:05 | GOES-16 | RINCÃO | SÃO PAULO | Brasil | 3543709 | 35 | 33 | nan | nan | nan | Cerrado | 47.6 |
| f64bb881-f54b-3080-9415-2b48a2bd0fcc | -21.5913 | -47.7172 | 2024-10-07 07:27:05 | GOES-16 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 92.2 |
| 23695742-7136-3fd5-a38e-17160c048a26 | -21.5906 | -47.7409 | 2024-10-07 07:27:05 | GOES-16 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 138.6 |
| 4d2780fb-4a6c-387d-b978-f74a0921c6a5 | -21.5843 | -47.9536 | 2024-10-07 07:27:05 | GOES-16 | GUATAPARÁ | SÃO PAULO | Brasil | 3518859 | 35 | 33 | nan | nan | nan | Cerrado | 56.0 |
| 871fcdb2-d11b-3b27-b7d5-bd02101bae1b | -21.5698 | -47.746 | 2024-10-07 07:27:05 | GOES-16 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 69.4 |
| d286bcdf-ef98-3ed3-8c39-e4d31f5e3a50 | -16.5072 | -57.7387 | 2024-10-07 07:36:39 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 56.0 |
| 69c9bae9-2d96-3b6a-86d9-5caa1400004a | -16.6332 | -57.1533 | 2024-10-07 07:36:40 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 58.2 |
| e8cf03b5-aa2f-3911-8443-3e0c175e302b | -16.6335 | -57.1328 | 2024-10-07 07:36:40 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 57.7 |
| 3786c34d-0ce4-37dc-bdf0-03bd0ea2655f | -16.6535 | -55.8958 | 2024-10-07 07:36:40 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 83.5 |
| e081a432-c439-3ee8-b2c4-b0901a26d325 | -16.5267 | -57.7365 | 2024-10-07 07:36:40 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 66.5 |
| aeef033b-d6b0-37ed-b04a-e115f43df616 | -17.0123 | -56.6773 | 2024-10-07 07:36:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 192.1 |
| 649fae4f-cb0e-376e-b7ad-18378433ec1c | -17.0127 | -56.6567 | 2024-10-07 07:36:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 55.3 |
| 1be3a7de-40aa-3540-9506-91f37242fbdd | -17.0316 | -56.6956 | 2024-10-07 07:36:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 96.4 |
| a5300572-7ce6-3859-9a0e-9ef778b484ca | -17.0319 | -56.6749 | 2024-10-07 07:36:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 202.6 |
| de13ae4f-3b44-3154-a808-4cec3eb526e4 | -16.9717 | -56.7646 | 2024-10-07 07:36:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 69.7 |
| f4d35362-0138-39ae-87f6-2e9e342d8d9d | -17.0323 | -56.6543 | 2024-10-07 07:36:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 58.9 |
| c51c6e88-5336-31cd-98b5-956d4a20dcc8 | -16.9741 | -56.6202 | 2024-10-07 07:36:42 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 71.2 |
| 0098749d-2861-394a-8e2b-88fd594ef915 | -16.9744 | -56.5996 | 2024-10-07 07:36:42 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 99.1 |
| 0f57a11f-3a08-319c-bf63-0898a9a798b1 | -17.012 | -56.698 | 2024-10-07 07:36:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 108.6 |
| 02e8a6bf-ecaf-391b-91c5-9697cf1ebfac | -17.1584 | -57.3377 | 2024-10-07 07:36:43 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 116.0 |
| 1df5c5f9-3ef0-3f77-b58c-6334d5a8d017 | -17.1581 | -57.3582 | 2024-10-07 07:36:43 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 102.9 |
| a10948b2-8f8a-34a9-8d90-ad0601bbc944 | -17.178 | -57.3354 | 2024-10-07 07:36:43 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 111.1 |
| 3f4bc6ff-de62-394d-be24-b2ff9c537151 | -17.0982 | -57.4267 | 2024-10-07 07:36:43 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 86.8 |
| 80befaa0-bc87-3bee-91b0-c0aba36db2c9 | -17.0985 | -57.4062 | 2024-10-07 07:36:43 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 69.2 |
| ea0dc325-15d0-3b1c-a92a-6188b037aca6 | -17.1078 | -56.8304 | 2024-10-07 07:36:43 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 67.7 |
| acca38a9-f963-375e-9859-15ccfeb6beb5 | -17.1274 | -56.828 | 2024-10-07 07:36:43 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 101.4 |
| 4569d69e-4960-3e93-b227-4b1b6d9e4524 | -17.1278 | -56.8074 | 2024-10-07 07:36:43 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 131.0 |
| 5c1ff6e7-aa89-3419-bde4-9b271adc6268 | -17.1281 | -56.7868 | 2024-10-07 07:36:43 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 75.8 |
| ba7b7178-4625-3ac7-8f75-ad7d62896701 | -17.1471 | -56.8256 | 2024-10-07 07:36:43 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 69.3 |
| f77f2617-ef9a-3f57-a62e-a03128f9d84f | -17.1474 | -56.805 | 2024-10-07 07:36:43 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 91.4 |
| 5307bab3-c2ef-3834-8f0d-4ccf79a3d4f8 | -17.1777 | -57.3559 | 2024-10-07 07:36:43 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 81.6 |
| 1c50f2e0-7f95-3941-b86d-afa1226db2d0 | -21.5906 | -47.7409 | 2024-10-07 07:37:05 | GOES-16 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 110.4 |
| 5244587e-5673-3719-8806-eadcc9448bc6 | -21.5913 | -47.7172 | 2024-10-07 07:37:05 | GOES-16 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 84.1 |
| 18297f02-63d7-33a5-85fb-99861ddfd7a7 | -21.5698 | -47.746 | 2024-10-07 07:37:05 | GOES-16 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 62.7 |
| f6884be1-a547-310a-8aba-180853b77246 | -16.5072 | -57.7387 | 2024-10-07 07:46:39 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 56.7 |
| 9ad004a2-63a4-364c-8b27-bda59850b926 | -16.5267 | -57.7365 | 2024-10-07 07:46:40 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 62.0 |
| ef69076e-b291-39ea-b776-d5e9130d3d85 | -16.5749 | -57.1395 | 2024-10-07 07:46:40 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 54.0 |
| c0ae3d8d-3568-39d6-bec2-04258c5e25dd | -16.6335 | -57.1328 | 2024-10-07 07:46:40 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 55.0 |
| 5144f1ce-fe6a-30b7-9df2-55f715c9e45b | -17.0123 | -56.6773 | 2024-10-07 07:46:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 190.4 |
| c0b0bab6-52e8-3225-bf46-18972047e317 | -16.9717 | -56.7646 | 2024-10-07 07:46:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 61.3 |
| 9e13393c-5e64-36ed-803f-6991d8c12a57 | -16.9744 | -56.5996 | 2024-10-07 07:46:42 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 79.5 |
| 0ac4ae52-4b0a-3998-b822-c84d3f46231f | -17.012 | -56.698 | 2024-10-07 07:46:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 97.7 |
| 90155b8a-b502-3195-9864-0bbd40ac3cd3 | -17.0316 | -56.6956 | 2024-10-07 07:46:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 92.1 |
| ea4b77f0-7221-3cfa-a00c-0995735c6541 | -17.0319 | -56.6749 | 2024-10-07 07:46:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 221.0 |
| 3fb38e70-588e-34bc-99dd-9d77ed000449 | -17.0323 | -56.6543 | 2024-10-07 07:46:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 56.9 |
| 1808586c-dcf5-3fa4-a22b-7250e63143a1 | -17.178 | -57.3354 | 2024-10-07 07:46:43 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 116.3 |
| 3d7f2c92-339e-3883-8ba0-65d063200dd8 | -17.1584 | -57.3377 | 2024-10-07 07:46:43 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 139.1 |
| 7512f40b-1f32-36ef-a6fd-858607ecad70 | -17.0982 | -57.4267 | 2024-10-07 07:46:43 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 88.8 |
| b6b265e4-a8cc-3638-8253-1a7d0ed00fb1 | -17.0985 | -57.4062 | 2024-10-07 07:46:43 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 74.0 |
| 7fa236a4-4db0-35d8-9350-ce9f328981a1 | -17.1078 | -56.8304 | 2024-10-07 07:46:43 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 69.6 |
| 795ec1b9-4217-3ae9-8fdc-9b6c4766f259 | -17.1274 | -56.828 | 2024-10-07 07:46:43 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 107.2 |
| 7494acf7-df28-3722-9696-ce9fdc4002f5 | -17.1278 | -56.8074 | 2024-10-07 07:46:43 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 137.8 |
| c756d919-ecc1-36c9-88e8-882a896a6437 | -17.1281 | -56.7868 | 2024-10-07 07:46:43 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 79.5 |
| 1668d387-d939-35b3-a3ba-933b44494b6a | -17.1471 | -56.8256 | 2024-10-07 07:46:43 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 73.6 |
| 5cb023c4-ecaa-366f-a285-f59fe72d36cf | -17.1474 | -56.805 | 2024-10-07 07:46:43 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 103.9 |
| ea949772-8934-3498-a801-1ff18414e41e | -17.1777 | -57.3559 | 2024-10-07 07:46:43 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 86.2 |
| 12fc355a-4795-3f26-9e57-01987b70398f | -17.1581 | -57.3582 | 2024-10-07 07:46:43 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 106.4 |
| 4b316092-af68-31b8-b059-e0775b7d289c | -21.5906 | -47.7409 | 2024-10-07 07:47:05 | GOES-16 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 102.8 |
| 365f5088-9f79-36d9-8ff6-1b23724c95bc | -21.5913 | -47.7172 | 2024-10-07 07:47:05 | GOES-16 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 82.7 |
| 2a890878-d56d-30f5-8e73-0893dbe95a6e | -16.5072 | -57.7387 | 2024-10-07 07:56:39 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 65.3 |
| 9cbdd3fc-8849-3b48-9b01-c39a44cc8212 | -16.5944 | -57.1373 | 2024-10-07 07:56:40 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 58.4 |
| 3d28131a-836a-3964-9f0b-c2a1041704df | -16.5749 | -57.1395 | 2024-10-07 07:56:40 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 70.5 |
| 667226dd-fc27-3e3d-bd98-34aa47f5cf61 | -16.5745 | -57.16 | 2024-10-07 07:56:40 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 53.7 |


[Clique aqui para ver as próximas entradas](README145.md)
