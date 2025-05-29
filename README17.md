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
| 4ae41fb8-0684-374e-b2fa-ea06000d7d8f | -12.42447 | -53.32061 | 2025-05-29 05:31:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| bb99ecc9-5617-3ade-b321-74db322227b2 | -11.80139 | -55.07506 | 2025-05-29 05:31:00 | NPP-375D | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 9a4da0ba-f703-3080-ab13-8caeb54ec723 | -8.01907 | -49.68763 | 2025-05-29 05:31:00 | NPP-375D | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 8b249355-7359-31f4-b70c-89a29031961a | -12.41952 | -53.32623 | 2025-05-29 05:31:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 83d8c921-7530-3f4c-b09e-ef8a936eb35a | -12.10656 | -54.66423 | 2025-05-29 05:31:00 | NPP-375D | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 420e9867-ba11-335c-87d1-d22b6995ffe2 | -8.75226 | -49.76444 | 2025-05-29 05:31:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| a698b4b7-afaf-3f24-b4f2-3ecf05987dbf | -8.7447 | -49.76965 | 2025-05-29 05:31:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 39b784d4-db3c-32b2-a936-c8788f4cad8a | -12.39178 | -49.97305 | 2025-05-29 05:31:00 | NPP-375D | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| ad64b322-9464-3ead-944b-151137d557a7 | -8.19887 | -49.81573 | 2025-05-29 05:31:00 | NPP-375D | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 882b490a-8f0a-3233-9b78-55eed4d37d7c | -11.78294 | -54.77931 | 2025-05-29 05:31:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8df813db-5abc-3a71-af8d-57c246fa30fb | -12.32572 | -49.99155 | 2025-05-29 05:31:00 | NPP-375D | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 71952f7f-fa57-3c5f-8700-5c6ec9bc90f6 | -12.39161 | -53.25553 | 2025-05-29 05:31:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1969e67a-4f05-3edf-a40c-3c81a5b5eb68 | -9.81185 | -54.71881 | 2025-05-29 05:31:00 | NPP-375D | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 8bc2fd0f-8d09-3559-b077-2d0695397b99 | -8.75184 | -49.76478 | 2025-05-29 05:31:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 30352f38-06e3-343d-af50-f11612006874 | -11.78808 | -54.78012 | 2025-05-29 05:31:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4dac4bf8-ddc6-3e70-a3c0-0aac0195f5a5 | -11.14083 | -53.94191 | 2025-05-29 05:31:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4f346877-8c93-3d91-8aad-8ea4dd6b144e | -12.42618 | -53.31899 | 2025-05-29 05:31:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 144d5f39-565d-32fd-aa36-efcba09c8226 | -10.82492 | -54.04364 | 2025-05-29 05:31:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 80bb2b46-6003-322b-8a8e-e84fb540619d | -9.19892 | -49.47585 | 2025-05-29 05:31:00 | NPP-375D | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| dc2c65be-0c0d-3ad0-a8dc-70d6954cae33 | -10.81957 | -54.04298 | 2025-05-29 05:31:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 18b9b88a-4a35-36d5-866d-80e3e005ad7b | -11.80216 | -55.06925 | 2025-05-29 05:31:00 | NPP-375D | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| af8c2c9c-2690-393e-a724-e5cc9832263c | -10.83564 | -54.04485 | 2025-05-29 05:31:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| bae9e252-23e6-31cd-9b9d-aa73d947c121 | -8.74503 | -49.76384 | 2025-05-29 05:31:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| abb6230a-3f6e-3bc9-81e0-b4aa4e3c92a3 | -8.7515 | -49.77069 | 2025-05-29 05:31:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 82e6043f-b32a-3a5b-a6bf-0604da19788d | -12.4138 | -53.32547 | 2025-05-29 05:31:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 49f2fa11-32a4-33d8-9f31-31684245fd57 | -11.81116 | -55.07082 | 2025-05-29 05:31:00 | NPP-375D | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| e6d70d7f-83bc-3e31-b666-af3bb6a3d1db | -12.39018 | -49.97108 | 2025-05-29 05:31:00 | NPP-375D | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 4.9 |
| c7b9296f-7e82-3a61-91ee-93e86b1097ba | -10.19714 | -52.65062 | 2025-05-29 05:31:00 | NPP-375D | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 57512813-96ca-390b-afed-6217f297cc7b | -11.03865 | -50.78283 | 2025-05-29 05:31:00 | NPP-375D | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 192e1f65-5b5c-3b61-9ba9-01b8ebe8b784 | -12.11178 | -54.66489 | 2025-05-29 05:31:00 | NPP-375D | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d9e12d0c-c773-3829-8590-06095ecc8b79 | -10.33118 | -57.49366 | 2025-05-29 05:31:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3d0fb176-5419-32b0-bb4f-6ae0eabd44f5 | -11.97735 | -52.46077 | 2025-05-29 05:31:00 | NPP-375D | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 7b2c3654-ac79-35d3-bca7-3d3883b7cc15 | -11.97081 | -52.46435 | 2025-05-29 05:31:00 | NPP-375D | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 8ca7a5a4-302c-3180-9e6d-54915bd0985e | -11.80538 | -55.07588 | 2025-05-29 05:31:00 | NPP-375D | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| ce94ad7c-49a8-3098-8da3-dec97ad6c2af | -10.19131 | -52.65001 | 2025-05-29 05:31:00 | NPP-375D | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 4ba40ab9-99ae-3492-8cd2-b4be202fe576 | -11.97135 | -52.45985 | 2025-05-29 05:31:00 | NPP-375D | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 6fc60aa8-6355-39f9-8a56-4757610d6e25 | -11.14578 | -53.94616 | 2025-05-29 05:31:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c01c21a8-4a76-3b58-b1f2-6432ca698231 | -11.90944 | -54.41322 | 2025-05-29 05:31:00 | NPP-375D | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a3b224de-5d8f-347d-b156-28c7737180d3 | -12.38477 | -49.97208 | 2025-05-29 05:31:00 | NPP-375D | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| c1dceb11-d2e6-35d5-9794-cc93cf4929d3 | -9.20778 | -49.47795 | 2025-05-29 05:31:00 | NPP-375D | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 2af73be9-0d82-3c02-a517-58632243c956 | -9.35326 | -57.54722 | 2025-05-29 05:31:00 | NPP-375D | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 77649c16-703c-37f2-9b1e-789af489262e | -9.35273 | -57.55094 | 2025-05-29 05:31:00 | NPP-375D | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 48d6c0c3-327b-3810-a2f0-c4ad60bdb7f8 | -12.43191 | -53.31974 | 2025-05-29 05:31:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 96f8ec3d-820b-3026-a5f3-a14c506055f6 | -10.32699 | -57.49305 | 2025-05-29 05:31:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 027a7a6e-5599-31f5-a406-f4e9f3f57cae | -11.07755 | -55.05566 | 2025-05-29 05:31:00 | NPP-375D | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| e3adb06a-e78f-3437-bba1-0b27897f44b3 | -11.13803 | -53.92063 | 2025-05-29 05:31:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| b19f44de-9022-38cf-a5df-29b97c92ff3e | -12.11097 | -54.67129 | 2025-05-29 05:31:00 | NPP-375D | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 02b338a3-0713-3b6b-9028-3551ebd841a1 | -12.41999 | -53.32224 | 2025-05-29 05:31:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 200f3706-e2a2-390f-8eb5-bdcf486c1fca | -8.02093 | -49.68796 | 2025-05-29 05:31:00 | NPP-375D | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 71d1fa4d-e675-3754-b377-c19394575c61 | -12.42397 | -53.3246 | 2025-05-29 05:31:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| b29c2598-a65f-3ce2-9b34-41f28674ccb9 | -11.1376 | -53.9241 | 2025-05-29 05:31:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| bd0f0d3f-f9ee-3bc2-9961-528df46717ef | -8.0123 | -49.6866 | 2025-05-29 05:31:00 | NPP-375D | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d8707960-11de-311c-887f-a2a089535a16 | -12.11138 | -54.66809 | 2025-05-29 05:31:00 | NPP-375D | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| af001998-2236-3327-b895-87426a630655 | -12.41203 | -53.32711 | 2025-05-29 05:31:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 4.6 |
| fbc55e52-01a3-379b-8b39-c46a518ac27c | -6.21751 | -57.7749 | 2025-05-29 05:53:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| bac63712-dee2-3113-83ac-3a2ca4d35c10 | -9.36027 | -57.54392 | 2025-05-29 05:55:00 | NOAA-20 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| b0153457-554d-317e-acb4-569bce5ccd7f | -9.35277 | -57.55301 | 2025-05-29 05:55:00 | NOAA-20 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| fcd90a82-eb44-3251-a9c4-6ea4e2f2af97 | -9.35341 | -57.54802 | 2025-05-29 05:55:00 | NOAA-20 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 6b1c3d0a-4f3a-35d3-a8b8-9c7ed7cc788c | -14.2182 | -47.7167 | 2025-05-29 06:10:00 | GOES-19 | ALTO PARAÍSO DE GOIÁS | GOIÁS | Brasil | 5200605 | 52 | 33 | nan | nan | nan | Cerrado | 103.1 |
| a710cb2b-6c38-3bba-82b3-ac53902daf23 | -14.1988 | -47.7198 | 2025-05-29 06:10:00 | GOES-19 | ALTO PARAÍSO DE GOIÁS | GOIÁS | Brasil | 5200605 | 52 | 33 | nan | nan | nan | Cerrado | 75.1 |
| 5816a125-faf1-3665-af1d-699c9eae9bf6 | -14.2182 | -47.7167 | 2025-05-29 06:20:00 | GOES-19 | ALTO PARAÍSO DE GOIÁS | GOIÁS | Brasil | 5200605 | 52 | 33 | nan | nan | nan | Cerrado | 67.6 |
| 390b1871-0943-3d64-b3d3-358f8abfb754 | -9.20537 | -49.4585 | 2025-05-29 06:20:00 | AQUA_M-M | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 19.7 |
| 484ab671-6f4d-33cf-940a-446103ca1a68 | -9.2027 | -49.47977 | 2025-05-29 06:20:00 | AQUA_M-M | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 17.3 |
| 4e2d75ef-04cb-3aa1-893f-4a1f3cb6a6ea | -9.20488 | -49.47491 | 2025-05-29 06:20:00 | AQUA_M-M | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 28.6 |
| c69b45f3-aa89-37a3-8598-2092c92626ef | -6.21329 | -57.77467 | 2025-05-29 06:20:00 | AQUA_M-M | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| f1fbfd8d-52e3-3254-9d48-1a62581607d9 | -9.35388 | -57.54792 | 2025-05-29 06:20:00 | AQUA_M-M | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 5.7 |
| f753dd91-6e73-38e2-bbe0-cfbb2d0e2327 | -14.19892 | -47.70075 | 2025-05-29 06:22:00 | AQUA_M-M | ALTO PARAÍSO DE GOIÁS | GOIÁS | Brasil | 5200605 | 52 | 33 | nan | nan | nan | Cerrado | 47.0 |
| e73c0b3c-eee4-393e-8272-c1306735b453 | -14.21518 | -47.70284 | 2025-05-29 06:22:00 | AQUA_M-M | ALTO PARAÍSO DE GOIÁS | GOIÁS | Brasil | 5200605 | 52 | 33 | nan | nan | nan | Cerrado | 48.3 |
| e5a0b880-81cb-34b6-a6bc-1128ccfa9eec | -11.8032 | -55.0666 | 2025-05-29 06:22:00 | AQUA_M-M | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 8.0 |
| 21213273-0f18-3443-bd48-1887ecc15e2d | -14.19518 | -47.73516 | 2025-05-29 06:22:00 | AQUA_M-M | ALTO PARAÍSO DE GOIÁS | GOIÁS | Brasil | 5200605 | 52 | 33 | nan | nan | nan | Cerrado | 61.4 |
| d15d32f4-6119-3604-978a-a9cd2dc40eec | -12.3894 | -50.0002 | 2025-05-29 10:50:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 120.9 |
| ef06e16f-c0a8-3b67-88f1-804d4d927a8d | -6.3348 | -43.3832 | 2025-05-29 11:10:00 | GOES-19 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 88.7 |
| e3c97b3a-dc95-3927-86d1-25ecafe6f385 | -12.4086 | -49.9978 | 2025-05-29 11:10:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 143.2 |
| cd9bebf4-6b73-38df-857e-4112de005301 | -12.4086 | -49.9978 | 2025-05-29 11:20:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 136.5 |
| 2222765d-80b1-3039-86ad-904f0677d01e | -6.3348 | -43.3832 | 2025-05-29 11:20:00 | GOES-19 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 104.2 |
| 5ab75306-7863-377f-9fbe-f2cd62eedd53 | -6.3351 | -43.3598 | 2025-05-29 11:20:00 | GOES-19 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 96.0 |
| 9a212165-3051-35c6-abf6-f6e2884ced33 | -12.4086 | -49.9978 | 2025-05-29 11:30:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 207.5 |
| fb69f702-b224-3254-abeb-85905f568646 | -6.3348 | -43.3832 | 2025-05-29 11:30:00 | GOES-19 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 103.5 |
| 02cb3132-aad3-3d44-9467-8d650cac1f5d | -6.3348 | -43.3832 | 2025-05-29 11:40:00 | GOES-19 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 82.2 |
| 64d512e1-969d-3045-92c6-bdb0875217d5 | -12.4086 | -49.9978 | 2025-05-29 11:40:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 291.8 |
| 91516711-573a-3076-af6b-b6e1a7fe5b1a | -6.22633 | -43.33214 | 2025-05-29 11:42:00 | TERRA_M-M | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 32.2 |
| 778f5729-6705-3de1-9448-d5bc75c15fe4 | -7.34264 | -43.71968 | 2025-05-29 11:45:00 | TERRA_M-M | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 29.8 |
| a62c6e07-3e68-3996-84eb-37cbe68a1798 | -16.70433 | -44.21552 | 2025-05-29 11:45:00 | TERRA_M-M | SÃO JOÃO DA LAGOA | MINAS GERAIS | Brasil | 3162252 | 31 | 33 | nan | nan | nan | Cerrado | 21.7 |
| 15056b79-10f9-335a-9ccc-9552cc442024 | -7.08261 | -44.91723 | 2025-05-29 11:45:00 | TERRA_M-M | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 37.1 |
| 037a6090-bbf7-3d91-aebb-2639b7e1efb5 | -10.67531 | -44.40899 | 2025-05-29 11:45:00 | TERRA_M-M | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 58.4 |
| 48eff92b-834c-3dab-8a9e-6c26562ec524 | -13.71691 | -45.24489 | 2025-05-29 11:45:00 | TERRA_M-M | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 65.1 |
| 74610669-c765-3d79-8278-041edb372696 | -12.24487 | -43.31905 | 2025-05-29 11:45:00 | TERRA_M-M | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 12.4 |
| c159ac44-ea9a-39b5-9cab-681a0de0bc1e | -11.81238 | -44.259 | 2025-05-29 11:45:00 | TERRA_M-M | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 27.4 |
| 203d1c5d-a17a-35a0-8794-1bfbda955f74 | -7.54504 | -43.3418 | 2025-05-29 11:45:00 | TERRA_M-M | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Cerrado | 35.5 |
| 795d273a-397d-3de7-9ecb-d0cb4738c7f3 | -13.09866 | -45.27962 | 2025-05-29 11:45:00 | TERRA_M-M | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 21.7 |
| a8e53ed4-bf6b-3a55-8cea-d5d43a09b4e7 | -16.70231 | -44.20841 | 2025-05-29 11:45:00 | TERRA_M-M | SÃO JOÃO DA LAGOA | MINAS GERAIS | Brasil | 3162252 | 31 | 33 | nan | nan | nan | Cerrado | 36.0 |
| 5f96338e-ca39-3c76-8f88-7500aeeadf15 | -13.09726 | -45.27374 | 2025-05-29 11:45:00 | TERRA_M-M | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 20.6 |
| 202d2e7c-291e-3e8d-93da-5b8a74dd41e3 | -7.54909 | -43.35998 | 2025-05-29 11:45:00 | TERRA_M-M | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Cerrado | 77.5 |
| d5ec38eb-9bc8-3b78-9d92-006966de4d23 | -7.54123 | -43.36487 | 2025-05-29 11:45:00 | TERRA_M-M | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Cerrado | 60.3 |
| c13939fc-8ecb-363a-b11f-ec7de152dfe7 | -12.4086 | -49.9978 | 2025-05-29 11:50:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 238.3 |
| 986853d4-ccc0-34cc-b30c-c7138c06f518 | -12.4086 | -49.9978 | 2025-05-29 12:00:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 346.1 |
| 2c0cacf0-9d52-326b-a423-bb864a9778a1 | -12.3898 | -49.9786 | 2025-05-29 12:00:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 98.9 |
| bc3d1ca1-1cf0-380e-8553-59037f2a07f9 | -12.3898 | -49.9786 | 2025-05-29 12:10:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 142.2 |
| 19ef0c54-7793-3537-9139-5f1a28833f33 | -12.4086 | -49.9978 | 2025-05-29 12:10:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 386.6 |
| b3313945-d438-3d4b-b4d3-e0383eb3a3e7 | -12.3901 | -49.9569 | 2025-05-29 12:10:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 150.3 |


[Clique aqui para ver as próximas entradas](README18.md)
