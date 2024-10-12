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
| 5605980f-6cd2-3a26-a965-4002e1102145 | -12.14357 | -59.88185 | 2024-10-12 05:25:00 | NPP-375D | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 9cdc7ede-41bf-3bc5-a08a-3ee653272ed4 | -12.1434 | -59.72742 | 2024-10-12 05:25:00 | NPP-375D | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 158b31fb-1d05-35c3-8b4b-d8b62fc9a390 | -12.11408 | -58.73465 | 2024-10-12 05:25:00 | NPP-375D | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b20c2512-1446-3074-a40d-0a5c08021a3c | -12.11049 | -58.73413 | 2024-10-12 05:25:00 | NPP-375D | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 4879c446-fee1-3271-a0dc-f05a18237502 | -12.10751 | -58.72942 | 2024-10-12 05:25:00 | NPP-375D | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 3738686d-414e-32da-b7dc-6ef75659d15b | -12.10273 | -58.71164 | 2024-10-12 05:25:00 | NPP-375D | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 94e09d7a-dca4-35d3-8180-3f16189ad3fe | -12.09913 | -58.71109 | 2024-10-12 05:25:00 | NPP-375D | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 2c6061f8-dd7b-3599-a09e-efcecb93ec00 | -12.09839 | -58.70844 | 2024-10-12 05:25:00 | NPP-375D | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 28680f6f-9f38-386e-9a68-2669bf2d14c7 | -11.89341 | -59.01737 | 2024-10-12 05:25:00 | NPP-375D | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 402383f4-d458-3ff5-b2fa-2028a6020f95 | -11.89167 | -59.00469 | 2024-10-12 05:25:00 | NPP-375D | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 1dd7026a-19d9-3d7b-b0a6-87d336cb0d63 | -11.89107 | -59.00876 | 2024-10-12 05:25:00 | NPP-375D | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 2dc0ddac-c486-37e3-a655-bdf5e5c0a329 | -11.89048 | -59.01281 | 2024-10-12 05:25:00 | NPP-375D | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 64705c9d-6087-3546-8b1c-003268154d20 | -11.88814 | -59.00412 | 2024-10-12 05:25:00 | NPP-375D | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 192b17de-9553-3fd9-b6cb-ba008be5a425 | -11.88754 | -59.0082 | 2024-10-12 05:25:00 | NPP-375D | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 14e2b8b5-ba64-3aa6-9759-20db586d1566 | -11.88578 | -58.99558 | 2024-10-12 05:25:00 | NPP-375D | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ef99f35c-abdd-356c-85cc-a152e394d5ff | -11.88519 | -58.99961 | 2024-10-12 05:25:00 | NPP-375D | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 7d3fd1ca-836d-3a0f-87ae-f613febb3748 | -11.8846 | -59.00365 | 2024-10-12 05:25:00 | NPP-375D | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 3.4 |
| fc12bd74-cdf7-33f2-9302-ece81615d23c | -11.88283 | -58.99109 | 2024-10-12 05:25:00 | NPP-375D | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| eb704999-b7a4-3c7b-b33a-da7de9da8bec | -11.88224 | -58.99512 | 2024-10-12 05:25:00 | NPP-375D | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 13692b78-ed11-37fc-99ff-b5c4e179f878 | -11.88164 | -58.99917 | 2024-10-12 05:25:00 | NPP-375D | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 539a8b9e-eebb-3e7d-873f-cc2c0f29dc9c | -11.87869 | -58.99463 | 2024-10-12 05:25:00 | NPP-375D | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 11b4d6a4-f889-34c6-b2dd-b5e8089a007f | -11.8781 | -58.99867 | 2024-10-12 05:25:00 | NPP-375D | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 210d1034-bc72-3d0b-b770-38959c1ea88f | -11.87516 | -58.99405 | 2024-10-12 05:25:00 | NPP-375D | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| feaf3086-0244-3494-b1f4-2a3923ed1306 | -11.87457 | -58.99809 | 2024-10-12 05:25:00 | NPP-375D | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 48ee621e-b705-3727-84a4-7a87ae08545b | -11.87453 | -59.04742 | 2024-10-12 05:25:00 | NPP-375D | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 7606e49f-2593-3a11-a510-acbd017190d5 | -11.87394 | -59.05145 | 2024-10-12 05:25:00 | NPP-375D | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e0ba0045-ae23-3aee-ab9d-61b7f8f81411 | -11.871 | -59.04692 | 2024-10-12 05:25:00 | NPP-375D | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 9d9652ae-7cd0-3891-84c3-a9a7c9589150 | -11.87045 | -59.00151 | 2024-10-12 05:25:00 | NPP-375D | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| db838986-49ec-3496-817f-a8d6baf2fc3b | -11.87041 | -59.05092 | 2024-10-12 05:25:00 | NPP-375D | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| aedfae16-c437-3037-85a7-86f9d62e63ee | -11.86986 | -59.00553 | 2024-10-12 05:25:00 | NPP-375D | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| fda7064c-31c3-3c6f-80c5-10a0bb3996d2 | -11.86983 | -59.05491 | 2024-10-12 05:25:00 | NPP-375D | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 943946fc-2703-3b0b-b2e2-06b8e3ca72e8 | -11.86571 | -59.05836 | 2024-10-12 05:25:00 | NPP-375D | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 83e7db37-2595-35d8-a6e5-420d4008b600 | -11.86218 | -59.05785 | 2024-10-12 05:25:00 | NPP-375D | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| fda61bd0-67bb-3e16-a4d0-9b765076522a | -11.86042 | -58.89644 | 2024-10-12 05:25:00 | NPP-375D | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| e8ca10fe-6927-338b-bc02-ce733008d454 | -11.85041 | -58.87512 | 2024-10-12 05:25:00 | NPP-375D | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d552b79a-5205-3de1-863f-c75431fdfba5 | -11.84562 | -58.88282 | 2024-10-12 05:25:00 | NPP-375D | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 5a65503b-e83a-3cae-a946-3fcb22ad4083 | -11.84039 | -58.84468 | 2024-10-12 05:25:00 | NPP-375D | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| bcdc8e5d-09fe-39a0-a872-06ab22726fd8 | -11.83743 | -58.84013 | 2024-10-12 05:25:00 | NPP-375D | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 57483271-492f-3367-9584-6846daafe577 | -11.83683 | -58.84418 | 2024-10-12 05:25:00 | NPP-375D | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 7ab555cb-6f42-3937-8e4e-3fc618a95e12 | -11.83622 | -58.84824 | 2024-10-12 05:25:00 | NPP-375D | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 71245500-57fe-3d60-8f0b-6842623f4297 | -11.83562 | -58.85231 | 2024-10-12 05:25:00 | NPP-375D | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 4f05a4b0-a8ea-3c53-bb54-586d2d65ab67 | -11.83387 | -58.8396 | 2024-10-12 05:25:00 | NPP-375D | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 708514d1-8ba2-3f94-b9df-365a1e074020 | -11.83326 | -58.84367 | 2024-10-12 05:25:00 | NPP-375D | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 170ba985-80e8-3585-aad5-b58f51bcde97 | -11.83266 | -58.84774 | 2024-10-12 05:25:00 | NPP-375D | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 4cc8f048-60f2-34c4-ab11-0297deed6104 | -11.83205 | -58.85181 | 2024-10-12 05:25:00 | NPP-375D | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 06de3234-82bb-3475-a931-f60dd0558e1b | -11.83145 | -58.8559 | 2024-10-12 05:25:00 | NPP-375D | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 15d34d8f-76c3-3d32-a9a7-91d98d78676c | -11.83031 | -58.83907 | 2024-10-12 05:25:00 | NPP-375D | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 12.3 |
| bf1e1400-f45a-3460-8f1b-051d2bc5f17c | -11.8297 | -58.84315 | 2024-10-12 05:25:00 | NPP-375D | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 12.3 |
| 6d82c300-c924-3b28-920f-acc3b50c44f4 | -11.8291 | -58.84724 | 2024-10-12 05:25:00 | NPP-375D | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 79d16424-f1f0-34db-b73a-ee2b5af35165 | -11.82849 | -58.85131 | 2024-10-12 05:25:00 | NPP-375D | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 34cea66d-06b5-3cbe-a020-1c5c6a2e445e | -11.82789 | -58.85538 | 2024-10-12 05:25:00 | NPP-375D | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| b03d3b07-e39f-3666-aae0-8bb992e88481 | -11.82675 | -58.83853 | 2024-10-12 05:25:00 | NPP-375D | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 12.3 |
| f01b1a51-f45e-381e-8a9d-1b6206b30f1c | -11.82614 | -58.84261 | 2024-10-12 05:25:00 | NPP-375D | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 12.3 |
| 662346b1-4a44-3fcc-9d29-d5c758aa7e99 | -11.82554 | -58.84669 | 2024-10-12 05:25:00 | NPP-375D | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 1287e089-c03b-3ddb-b448-edc1ad71b966 | -11.82494 | -58.85076 | 2024-10-12 05:25:00 | NPP-375D | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 747aa427-bf52-37ab-aee1-8a5f9d5aa196 | -11.82433 | -58.85482 | 2024-10-12 05:25:00 | NPP-375D | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 916e3082-213d-3827-aae1-1a889d6d8ded | -11.82258 | -58.84207 | 2024-10-12 05:25:00 | NPP-375D | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 1b067e47-62e8-3a37-8b94-2ac8206fa95f | -11.82198 | -58.84614 | 2024-10-12 05:25:00 | NPP-375D | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 83465fb5-ef42-3710-94ad-1e9a1d3a1ca7 | -9.91078 | -60.72834 | 2024-10-12 05:25:00 | NPP-375D | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| edf4b637-0990-3253-a69b-148d851ec88d | -9.88321 | -60.81754 | 2024-10-12 05:25:00 | NPP-375D | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 6294bfbf-a75f-37b6-a1d0-6c13fc1fe375 | -9.88266 | -60.82104 | 2024-10-12 05:25:00 | NPP-375D | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 6d0be8f9-d97e-35f0-95e5-ef88bf789e00 | -9.87934 | -60.82051 | 2024-10-12 05:25:00 | NPP-375D | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6c9c66a6-3349-3ebb-bb99-1e7ec8936cd5 | -9.86808 | -60.73957 | 2024-10-12 05:25:00 | NPP-375D | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 1427a644-8eaf-33a4-aa3a-9fb12298ed10 | -9.85794 | -60.67308 | 2024-10-12 05:25:00 | NPP-375D | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 5a7db033-6637-3e52-8d01-4176ecd609c9 | -9.85755 | -60.7415 | 2024-10-12 05:25:00 | NPP-375D | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0bd5cb87-b84b-388c-9e7a-92ea625db4a4 | -9.85422 | -60.74097 | 2024-10-12 05:25:00 | NPP-375D | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f2d8231a-b26a-3172-8953-5eced4dedc0a | -9.8321 | -60.73767 | 2024-10-12 05:25:00 | NPP-375D | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 35fdaf14-33ac-3e4c-9182-4d3f89299b40 | -9.72634 | -60.74257 | 2024-10-12 05:25:00 | NPP-375D | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 55551fab-966a-378b-9bfe-5cafbe5bb59c | -9.71635 | -60.74099 | 2024-10-12 05:25:00 | NPP-375D | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 6f0fcafb-f48a-37e5-882f-5439e3e46162 | -9.70249 | -60.74237 | 2024-10-12 05:25:00 | NPP-375D | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 635ba81e-3573-32fc-b6a0-ea0a2c320635 | -9.70194 | -60.74588 | 2024-10-12 05:25:00 | NPP-375D | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d637ad5a-a366-3fa7-b8d0-89c90496039e | -9.69529 | -60.74482 | 2024-10-12 05:25:00 | NPP-375D | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 46e1e57f-03fb-398b-99c0-75ae40e26bea | -9.93034 | -60.17297 | 2024-10-12 05:25:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 257634ae-9c40-39ea-9fc8-9de2cc5218da | -9.92699 | -60.17244 | 2024-10-12 05:25:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c4029a6b-1b06-3430-859e-116ea8cabaf5 | -9.92363 | -60.17192 | 2024-10-12 05:25:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e94f16d6-84b1-338e-8d54-e8b7507f7764 | -9.90928 | -60.30848 | 2024-10-12 05:25:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 333fa3ab-0618-36c5-9fc6-fafdfc3dca0d | -9.8896 | -60.21412 | 2024-10-12 05:25:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f3910537-8e73-3214-8c34-4bf06878b53c | -9.88625 | -60.2136 | 2024-10-12 05:25:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6b6e7940-aa69-3c1a-ada3-80117513be4b | -9.88234 | -60.21663 | 2024-10-12 05:25:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| cbfdf1e0-5b1f-3a15-a51b-975c03e78718 | -9.86812 | -60.10818 | 2024-10-12 05:25:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| bae04cd6-0b55-3b49-a517-3d039498d3ac | -9.86691 | -60.31633 | 2024-10-12 05:25:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6efd3cee-6c29-32d4-8b14-d691b3fac445 | -9.86531 | -60.10407 | 2024-10-12 05:25:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 1abcbb3c-57e7-30f6-a875-5ade3ccbb825 | -9.86475 | -60.10766 | 2024-10-12 05:25:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 2cc9ea31-9a7c-3e71-bd8a-5fbe80b39357 | -9.86357 | -60.3158 | 2024-10-12 05:25:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 79ba0ad6-15e4-3e9d-a123-ef4c2a283055 | -9.862 | -60.12558 | 2024-10-12 05:25:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 4cd28620-4bd0-341c-906d-b7ceac81fc84 | -9.86187 | -60.30462 | 2024-10-12 05:25:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 145d1051-52c1-35fa-ad2e-da29ad6b9618 | -9.86145 | -60.12917 | 2024-10-12 05:25:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 219af547-ee8d-3fe5-9b0c-e24c5a95f2df | -9.86127 | -60.28633 | 2024-10-12 05:25:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 6fd40385-467e-390c-b302-9c7c31b3e9d3 | -9.86084 | -60.11072 | 2024-10-12 05:25:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 08c70965-5dc0-3625-907c-a444baeb2c96 | -9.86029 | -60.11431 | 2024-10-12 05:25:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 3b081f32-e433-39a9-a300-2349c3840630 | -9.85974 | -60.11789 | 2024-10-12 05:25:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| bc1cf7af-ff87-3760-9cbf-f0651c45108d | -9.85919 | -60.12147 | 2024-10-12 05:25:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 735372e2-0c76-3d98-a8ae-03e8bfa1d3ad | -9.85864 | -60.12506 | 2024-10-12 05:25:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b1e4fb1c-6101-3ffd-ac36-e46c7fec71cf | -9.85857 | -60.32594 | 2024-10-12 05:25:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c0722943-2524-3f47-b753-04fd97e0bbf0 | -9.85847 | -60.28224 | 2024-10-12 05:25:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| e143899b-f50b-3654-8564-0b32ad85ab82 | -9.85809 | -60.12864 | 2024-10-12 05:25:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| dd823b9a-4b39-3de8-bf9a-2d16c8e66002 | -9.85802 | -60.32949 | 2024-10-12 05:25:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 849f761b-be80-3b9a-9301-25c9a2e5589d | -9.85792 | -60.2858 | 2024-10-12 05:25:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 06f692c3-3d84-314d-9447-71a1ebd857a2 | -9.85748 | -60.11019 | 2024-10-12 05:25:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a692eef7-2e9c-3c66-8c78-99c89df6ae51 | -9.85522 | -60.32541 | 2024-10-12 05:25:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |


[Clique aqui para ver as próximas entradas](README127.md)
