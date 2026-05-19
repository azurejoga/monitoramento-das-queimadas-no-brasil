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
| ae19ae01-9444-3993-860a-42afd99bae60 | -9.3045 | -45.4809 | 2026-05-19 00:00:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 76.6 |
| 7060ce56-5614-362f-9e6f-56f8e8378d9b | -14.1442 | -52.8926 | 2026-05-19 00:00:00 | GOES-19 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 73.8 |
| 2b3a0d59-8d08-32f0-9b63-7840d089cc1f | -8.0761 | -44.1244 | 2026-05-19 00:00:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 67.4 |
| 2c893502-1354-3e37-8576-0eecca1d7c73 | -14.1638 | -52.8691 | 2026-05-19 00:00:00 | GOES-19 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 97.2 |
| d6487c54-dfea-3e48-8538-91974fba1695 | -8.0764 | -44.1012 | 2026-05-19 00:00:00 | GOES-19 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 86.7 |
| 2e93fa21-cf60-30e3-981a-fef394118054 | -10.443 | -47.945 | 2026-05-19 00:00:00 | GOES-19 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 55.8 |
| cffb6937-ef8f-39f2-82b2-42ba2883d29c | -8.7211 | -48.3222 | 2026-05-19 00:00:00 | GOES-19 | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Cerrado | 88.6 |
| c1394aa4-9aa0-313a-a198-08406bc39d09 | -14.1635 | -52.8902 | 2026-05-19 00:00:00 | GOES-19 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 123.9 |
| 34ba852d-3237-3c86-b1f4-9d8d78e81fc5 | -10.462 | -47.9428 | 2026-05-19 00:00:00 | GOES-19 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 71.2 |
| afa36eb4-b6e9-37a5-b615-4be35f241009 | -9.3045 | -45.4809 | 2026-05-19 00:10:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 93.7 |
| 8f8c566b-e874-3ec9-97ed-6ecaff93b46f | -8.7211 | -48.3222 | 2026-05-19 00:10:00 | GOES-19 | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Cerrado | 78.6 |
| 3051c081-1fe5-3ee0-8c08-827d7bdb0b46 | -14.1635 | -52.8902 | 2026-05-19 00:10:00 | GOES-19 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 121.2 |
| 8577fdf3-8a4d-3cf9-a9ac-b2df019f6ff6 | -14.1638 | -52.8691 | 2026-05-19 00:10:00 | GOES-19 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 85.7 |
| 288a1316-c6da-30d5-a129-e4178210be19 | -10.462 | -47.9428 | 2026-05-19 00:10:00 | GOES-19 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 68.1 |
| 47169408-b781-3bfa-bb0e-f1f45ae819d7 | -8.0952 | -44.0993 | 2026-05-19 00:10:00 | GOES-19 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 72.1 |
| cca24018-1b52-3494-b427-525e2fef9d4b | -8.0764 | -44.1012 | 2026-05-19 00:10:00 | GOES-19 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 72.2 |
| 862927c4-146d-35a8-9944-22992155eadc | -14.1442 | -52.8926 | 2026-05-19 00:10:00 | GOES-19 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 72.5 |
| a5c0d181-f4cf-3797-ba2a-247c565f92f5 | -8.0761 | -44.1244 | 2026-05-19 00:10:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 66.4 |
| 5c0543a5-20a1-3044-933d-ffaf8384e11a | -8.7208 | -48.3441 | 2026-05-19 00:10:00 | GOES-19 | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Cerrado | 56.8 |
| 031b6c1f-5be4-325f-a057-c0e4a362f959 | -11.4447 | -55.1199 | 2026-05-19 00:20:00 | GOES-19 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 42.0 |
| 1199662b-6bb6-3bd5-9959-d7f9b1798f34 | -11.4636 | -55.1182 | 2026-05-19 00:20:00 | GOES-19 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 51.2 |
| 4f55f82e-8a2e-3cc9-a904-249df00348f8 | -14.1638 | -52.8691 | 2026-05-19 00:20:00 | GOES-19 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 95.1 |
| 0909698f-a5c5-39c3-92b4-2ecd75200c9f | -10.462 | -47.9428 | 2026-05-19 00:20:00 | GOES-19 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 64.5 |
| c173b944-5aee-33d4-8680-f1922544d44e | -14.1442 | -52.8926 | 2026-05-19 00:20:00 | GOES-19 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 75.2 |
| 3faf7ac3-0d28-3142-8b17-4a6ffae337e8 | -8.7211 | -48.3222 | 2026-05-19 00:20:00 | GOES-19 | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Cerrado | 84.3 |
| 1b816417-25ce-39ba-912c-7fab833ee95f | -14.1635 | -52.8902 | 2026-05-19 00:20:00 | GOES-19 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 111.9 |
| 216af834-03f7-3bbd-b34a-e47319b61e15 | -8.0764 | -44.1012 | 2026-05-19 00:20:00 | GOES-19 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 74.6 |
| 5db84627-2451-320a-a4f6-32f3138c59b9 | -9.3045 | -45.4809 | 2026-05-19 00:20:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 85.9 |
| 834d025c-8a37-3863-abf9-44a96d69bd44 | -8.7211 | -48.3222 | 2026-05-19 00:30:00 | GOES-19 | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Cerrado | 80.9 |
| 881c4067-ca14-399e-9658-03bc455be917 | -14.1635 | -52.8902 | 2026-05-19 00:30:00 | GOES-19 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 111.5 |
| 8cdc997d-b927-3e97-a879-84a98319005d | -10.462 | -47.9428 | 2026-05-19 00:30:00 | GOES-19 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 65.1 |
| 22248662-35d7-374a-a301-27c10ca0ae04 | -11.4636 | -55.1182 | 2026-05-19 00:30:00 | GOES-19 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 47.2 |
| eb1e8a26-d069-3537-a6b3-647fa2bae2cd | -14.1638 | -52.8691 | 2026-05-19 00:30:00 | GOES-19 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 91.0 |
| be50ff8c-7f56-34ca-b82d-cae5c5522b4c | -9.3045 | -45.4809 | 2026-05-19 00:30:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 98.9 |
| d2a8a0c9-e51b-3ea8-9219-a4f20b595498 | -14.1442 | -52.8926 | 2026-05-19 00:30:00 | GOES-19 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 71.4 |
| d8a6e8c7-a5a3-355d-9c0e-be2a11251457 | -14.1635 | -52.8902 | 2026-05-19 00:40:00 | GOES-19 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 118.1 |
| ade17369-2cc2-364b-befe-373f159e7614 | -8.7211 | -48.3222 | 2026-05-19 00:40:00 | GOES-19 | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Cerrado | 64.3 |
| 2bdcb8b7-705a-3802-9bc6-c9430abdbed6 | -14.1638 | -52.8691 | 2026-05-19 00:40:00 | GOES-19 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 81.9 |
| 94cfb336-c2e4-36cb-b342-36689014853a | -10.462 | -47.9428 | 2026-05-19 00:40:00 | GOES-19 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 59.4 |
| a26d0eda-ca7c-33c5-a219-4ea3943e4d8e | -9.3045 | -45.4809 | 2026-05-19 00:40:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 90.7 |
| e8f8f8f0-66e1-34ae-b73b-69449bf521c8 | -8.7211 | -48.3222 | 2026-05-19 00:50:00 | GOES-19 | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Cerrado | 63.5 |
| 86197521-08fc-3ed8-833e-f5312bc8b6f8 | -14.1638 | -52.8691 | 2026-05-19 00:50:00 | GOES-19 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 81.8 |
| 4bf4be4e-449d-31ad-b714-bbe64d1cb093 | -10.462 | -47.9428 | 2026-05-19 00:50:00 | GOES-19 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 59.5 |
| ba8b6b39-f57e-3f56-87bc-43f4837772c6 | -9.3045 | -45.4809 | 2026-05-19 00:50:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 79.8 |
| 85c2b58c-eed0-3777-a6ef-a1fa71f23241 | -14.1635 | -52.8902 | 2026-05-19 00:50:00 | GOES-19 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 116.5 |
| c936d9a0-d6a4-3221-bb56-19326ff1d1c7 | -14.1442 | -52.8926 | 2026-05-19 00:50:00 | GOES-19 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 70.6 |
| fc378cc8-7b59-3412-8f53-da9aa3ff570a | -14.16398 | -52.89344 | 2026-05-19 00:50:00 | TERRA_M-M | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 53.0 |
| 9881d094-16cb-33d9-8b7c-17d42ce86031 | -14.15074 | -52.88078 | 2026-05-19 00:50:00 | TERRA_M-M | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 15.3 |
| d870b044-7a83-3f92-b167-ebea1c541ce7 | -10.45937 | -47.95892 | 2026-05-19 00:50:00 | TERRA_M-M | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 67.0 |
| 27532feb-1d5f-3fa1-9de0-049eb603471a | -11.60221 | -55.33431 | 2026-05-19 00:50:00 | TERRA_M-M | SINOP | MATO GROSSO | Brasil | 5107909 | 51 | 33 | nan | nan | nan | Amazônia | 7.3 |
| 1509ba86-86a2-3be2-b000-0ce536d6f25d | -11.44654 | -55.10594 | 2026-05-19 00:50:00 | TERRA_M-M | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 12.3 |
| 942e2cfd-645f-3ffb-b4b5-2c8496bbcb53 | -14.16169 | -52.87891 | 2026-05-19 00:50:00 | TERRA_M-M | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 88.2 |
| be2ff68f-6408-3ce2-9fad-bd51ff23300d | -10.45046 | -47.92348 | 2026-05-19 00:50:00 | TERRA_M-M | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 48.3 |
| 1819b1a8-6fb0-3631-806c-0df22574c9ce | -10.45728 | -47.96396 | 2026-05-19 00:50:00 | TERRA_M-M | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 60.5 |
| 828cc572-8993-364e-bda0-78aa85402b45 | -14.17491 | -52.89151 | 2026-05-19 00:50:00 | TERRA_M-M | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 7.5 |
| ae26e36c-c789-39cb-909f-0dc61434a41e | -14.15304 | -52.89537 | 2026-05-19 00:50:00 | TERRA_M-M | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 53.3 |
| 70625856-6bdb-3b9d-89b7-e40dca226d54 | -11.45872 | -52.92121 | 2026-05-19 00:50:00 | TERRA_M-M | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 30.8 |
| fa238cf3-0906-364d-b5be-d98d128e87ab | -11.74966 | -54.80025 | 2026-05-19 00:50:00 | TERRA_M-M | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 6.9 |
| a5be4932-c610-3d0a-9a35-676d86291581 | -11.4482 | -55.11713 | 2026-05-19 00:50:00 | TERRA_M-M | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 20.3 |
| 1c1dbb90-6e7b-3f52-9ee5-44e1bbdeafc7 | -10.66957 | -49.71049 | 2026-05-19 00:50:00 | TERRA_M-M | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 19.6 |
| c60595e8-eafb-324f-b4e6-28270617cd5e | -11.45798 | -55.11562 | 2026-05-19 00:50:00 | TERRA_M-M | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 31.6 |
| 2aeb2010-f8c3-3335-a61f-a70cefe6d42a | -8.71685 | -48.34332 | 2026-05-19 00:52:00 | TERRA_M-M | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Cerrado | 106.8 |
| 14091067-c040-3622-ba15-ed8bcb50eaf0 | -6.57168 | -51.12382 | 2026-05-19 00:52:00 | TERRA_M-M | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 22.5 |
| cf5a3965-c828-3166-bbe0-d999aea4de1d | -8.71525 | -48.351 | 2026-05-19 00:52:00 | TERRA_M-M | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Cerrado | 74.0 |
| 56170a6b-c8db-3bd3-a4eb-6a28cc065267 | 3.40612 | -60.95027 | 2026-05-19 00:54:00 | TERRA_M-M | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 86e9313b-bfda-3590-ad00-0e704484e84b | 3.40732 | -60.94151 | 2026-05-19 00:54:00 | TERRA_M-M | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 13.7 |
| 9f3a1562-936f-30b3-975e-38ec2b5d7db8 | -8.7131 | -48.3307 | 2026-05-19 00:58:00 | METOP-B | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| dcc80c85-27b4-399c-b66b-591adbf52c4a | -14.1411 | -52.8843 | 2026-05-19 00:58:00 | METOP-B | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 85eace32-9819-3874-acda-7c806a49a742 | -10.4383 | -47.926201 | 2026-05-19 00:58:00 | METOP-B | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 32c2e2c0-435c-38f2-b0f4-be5a633d1c01 | 3.4064 | -60.928398 | 2026-05-19 00:58:00 | METOP-B | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| 5e708b1b-20e9-3c27-a839-cb52365f636b | -14.1508 | -52.881699 | 2026-05-19 00:58:00 | METOP-B | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 91171313-fa69-38b4-9dce-8ba98d59f8e0 | -11.4532 | -55.105099 | 2026-05-19 00:58:00 | METOP-B | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 583126a1-6ccd-3b0c-9cbe-49bd3844793e | -14.1605 | -52.879101 | 2026-05-19 00:58:00 | METOP-B | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 72c0afb2-3e6b-341d-beaf-7448b7554740 | -10.4478 | -47.923599 | 2026-05-19 00:58:00 | METOP-B | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| b12c3353-8543-3609-b543-6e702a71af07 | -14.1475 | -52.868401 | 2026-05-19 00:58:00 | METOP-B | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 019695e9-eb0a-3f35-a687-32b0f4687c1e | -8.7044 | -48.2976 | 2026-05-19 00:58:00 | METOP-B | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| f1346955-4dc3-3203-9bbb-48bbd4e4dc61 | 3.4047 | -60.9361 | 2026-05-19 00:58:00 | METOP-B | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| 68aa5b0f-f9cb-3aa9-b778-bf83ec1feb38 | -14.1572 | -52.865799 | 2026-05-19 00:58:00 | METOP-B | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 41c2ef74-f7bf-36a2-8797-ec3af0f88962 | -11.4507 | -55.094501 | 2026-05-19 00:58:00 | METOP-B | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 59fb4e87-9ff7-3325-bfd3-78f9b08e1237 | -6.5627 | -51.074402 | 2026-05-19 00:58:00 | METOP-B | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 23b9ee43-1ccb-3c3e-bfee-b4b70b7b7077 | -14.1638 | -52.8691 | 2026-05-19 01:00:00 | GOES-19 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 84.4 |
| e0f1dfce-d698-3fe3-a4e5-8e859533b8f9 | -14.1635 | -52.8902 | 2026-05-19 01:00:00 | GOES-19 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 104.4 |
| 8066c034-fdee-332e-9405-9ce7775292f9 | -9.3045 | -45.4809 | 2026-05-19 01:00:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 79.0 |
| 5feea064-6c02-3e5c-a47a-22a6fa025aed | -10.462 | -47.9428 | 2026-05-19 01:00:00 | GOES-19 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 53.5 |
| e5d06400-7517-3cee-96af-9b44dd82b661 | -8.7211 | -48.3222 | 2026-05-19 01:00:00 | GOES-19 | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Cerrado | 63.6 |
| c31f1434-af56-3da9-bae9-d987afa3d28a | -10.462 | -47.9428 | 2026-05-19 01:10:00 | GOES-19 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 56.1 |
| 12eb85f9-e10f-3c92-b077-f899554b6aae | -6.3833 | -44.1674 | 2026-05-19 01:10:00 | GOES-19 | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 72.3 |
| 21d6c030-3de0-3077-bdde-86ca0c496a17 | -9.3045 | -45.4809 | 2026-05-19 01:10:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 63.1 |
| f11077a7-7dd3-3f50-a475-ab856a4a1beb | -6.4021 | -44.1658 | 2026-05-19 01:10:00 | GOES-19 | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 89.6 |
| a1653ed4-bb82-37d0-8460-ace5cd1e610c | -14.1638 | -52.8691 | 2026-05-19 01:10:00 | GOES-19 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 78.8 |
| 785aad45-5e75-377e-ad6c-ca441190970a | -8.7211 | -48.3222 | 2026-05-19 01:10:00 | GOES-19 | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Cerrado | 66.2 |
| be181445-2876-3483-b067-0ff7afac9783 | -14.1635 | -52.8902 | 2026-05-19 01:10:00 | GOES-19 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 110.7 |
| 48219430-1d1c-3e8f-ab5d-ea058573048c | -14.1638 | -52.8691 | 2026-05-19 01:20:00 | GOES-19 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 80.1 |
| 3a007fc7-25ef-37c5-9c46-26e354043fd6 | -8.7211 | -48.3222 | 2026-05-19 01:20:00 | GOES-19 | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Cerrado | 66.4 |
| 140aedb6-e11e-3a8e-ba4f-a39cb215c3dd | -6.3833 | -44.1674 | 2026-05-19 01:20:00 | GOES-19 | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 71.3 |
| 902dd84c-bca4-3f96-ab71-18786e9f359e | -14.1635 | -52.8902 | 2026-05-19 01:20:00 | GOES-19 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 106.3 |
| f2222b60-9465-36ae-ae69-2a91319a91e6 | -10.462 | -47.9428 | 2026-05-19 01:20:00 | GOES-19 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 60.1 |
| d1718bc4-04b2-3b56-9042-26b20b0022b1 | -6.4021 | -44.1658 | 2026-05-19 01:20:00 | GOES-19 | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 74.6 |
| 7296b05c-4958-3caa-b280-bea74d5f83ec | -14.1635 | -52.8902 | 2026-05-19 01:30:00 | GOES-19 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 93.4 |
| 65074622-2c55-3ed0-b3a2-f7a578e9ddbb | -14.1638 | -52.8691 | 2026-05-19 01:30:00 | GOES-19 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 81.5 |


[Clique aqui para ver as próximas entradas](README2.md)
