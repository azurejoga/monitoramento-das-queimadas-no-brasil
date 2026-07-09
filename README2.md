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

## Dados Diários - Página 2

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 6d333d05-c612-38d4-b57c-0e8dfc47d436 | -8.3444 | -45.3974 | 2026-07-09 00:06:00 | METOP-B | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 7b82ecd6-bd70-3a0d-b566-c5f12f765a8f | -4.3491 | -47.7631 | 2026-07-09 00:06:00 | METOP-B | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8ecdbee2-2ec3-3440-8331-d415734d565b | -7.8274 | -49.301498 | 2026-07-09 00:06:00 | METOP-B | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2b714bcd-103d-3801-a01d-7a9b596ed3a0 | -14.9181 | -43.4314 | 2026-07-09 00:06:00 | METOP-B | GAMELEIRAS | MINAS GERAIS | Brasil | 3127339 | 31 | 33 | nan | nan | nan | Caatinga | nan |
| 860f4d29-499b-3b2a-8882-fc3c896b6f0a | -21.027 | -43.2999 | 2026-07-09 00:06:00 | METOP-B | ALTO RIO DOCE | MINAS GERAIS | Brasil | 3102100 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| abbc5db7-c1cf-3c9b-af6f-7655dc68d5ee | -10.8636 | -47.585201 | 2026-07-09 00:06:00 | METOP-B | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 7b662e1a-cfd4-3848-a6f9-f81bd244ffe9 | -8.3524 | -45.387299 | 2026-07-09 00:06:00 | METOP-B | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 8668b6af-1b55-3a8f-a974-3dbcdf25bc8d | -7.7249 | -44.553902 | 2026-07-09 00:06:00 | METOP-B | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| d365756e-e273-3882-be0f-675557673b8c | -14.9142 | -43.414799 | 2026-07-09 00:06:00 | METOP-B | GAMELEIRAS | MINAS GERAIS | Brasil | 3127339 | 31 | 33 | nan | nan | nan | Caatinga | nan |
| 1a5b6062-c0c0-36ae-a040-cfc5d19b597d | -12.3498 | -47.415798 | 2026-07-09 00:06:00 | METOP-B | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 97fda5da-fca7-39ed-86ad-6a7594a2f4ef | -12.9277 | -49.460999 | 2026-07-09 00:06:00 | METOP-B | ARAGUAÇU | TOCANTINS | Brasil | 1702000 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| b066adb1-1c17-3256-8c0d-af584f77b6a6 | -1.8222 | -54.467899 | 2026-07-09 00:06:00 | METOP-B | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 99e2be11-68af-3285-9ca1-8578861de508 | -14.1449 | -52.862 | 2026-07-09 00:06:00 | METOP-B | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| f8a4f3b2-2f4b-3f0a-98fa-e9f2215e9e0c | -14.1474 | -52.874802 | 2026-07-09 00:06:00 | METOP-B | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| b14c1e09-643e-34be-8e46-53ff2a506ba9 | -8.7241 | -47.829498 | 2026-07-09 00:06:00 | METOP-B | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 19297937-a68a-32b9-bfd7-a7afd75143a6 | -9.372 | -44.7127 | 2026-07-09 00:06:00 | METOP-B | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 7e191e85-ef07-3f83-9fce-07749f009bf1 | -12.1738 | -43.452202 | 2026-07-09 00:06:00 | METOP-B | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| fe2d1274-bfba-3827-9617-f24b9319f055 | -11.8311 | -48.237202 | 2026-07-09 00:06:00 | METOP-B | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 75020fa6-fc1c-3839-8416-1287f6465f2f | -14.9162 | -43.4231 | 2026-07-09 00:06:00 | METOP-B | GAMELEIRAS | MINAS GERAIS | Brasil | 3127339 | 31 | 33 | nan | nan | nan | Caatinga | nan |
| e46f961a-0100-367a-bd25-c9e20d76d746 | -12.841 | -44.356899 | 2026-07-09 00:06:00 | METOP-B | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 1da6a23f-9d34-3cff-bd4b-87b65463b8bb | -9.3765 | -48.490601 | 2026-07-09 00:06:00 | METOP-B | RIO DOS BOIS | TOCANTINS | Brasil | 1718709 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| c07d7308-1b1e-3b9a-9949-3199ce6f146a | -8.9697 | -48.006001 | 2026-07-09 00:06:00 | METOP-B | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| a6c51ae2-7058-346d-810b-2f723b43de28 | -10.012 | -48.525501 | 2026-07-09 00:06:00 | METOP-B | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| e9f597ad-a41e-3e32-8b46-b61c9abf4712 | -3.1969 | -49.045601 | 2026-07-09 00:06:00 | METOP-B | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 57589c97-34be-3b1e-9c09-725c6e5f6857 | -20.6528 | -50.097301 | 2026-07-09 00:06:00 | METOP-B | FLOREAL | SÃO PAULO | Brasil | 3515905 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 326833d9-bbee-3023-b2cd-deee3e1fc99a | -11.8296 | -48.230099 | 2026-07-09 00:06:00 | METOP-B | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| febc4352-f881-3860-a3e4-10a4f08bad31 | -9.375 | -48.483601 | 2026-07-09 00:06:00 | METOP-B | RIO DOS BOIS | TOCANTINS | Brasil | 1718709 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| f99b3138-cb30-3d18-ad3d-377ae988b8d8 | -8.1231 | -47.085899 | 2026-07-09 00:06:00 | METOP-B | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 501992ed-5980-3a0a-9a0b-24853bb29908 | -12.6695 | -48.214802 | 2026-07-09 00:06:00 | METOP-B | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 8d4f7f5b-65a6-33f6-b95a-19f189b7d0b0 | -22.920601 | -49.186699 | 2026-07-09 00:06:00 | METOP-B | ÁGUAS DE SANTA BÁRBARA | SÃO PAULO | Brasil | 3500550 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| f2c40dc6-3733-3561-a726-c74bdadc5031 | -11.9293 | -44.699402 | 2026-07-09 00:06:00 | METOP-B | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 0766ba63-ce73-32f0-babb-76afcea0518b | -8.7054 | -54.526299 | 2026-07-09 00:06:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7c48302f-d413-3069-a387-6a6b083e26b4 | -12.7582 | -44.533501 | 2026-07-09 00:06:00 | METOP-B | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| b5a23004-306b-3df4-a4f5-963235715779 | -1.8198 | -54.457298 | 2026-07-09 00:06:00 | METOP-B | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b8eef15b-54f0-3130-aae1-7536903a236a | -8.1149 | -47.0951 | 2026-07-09 00:06:00 | METOP-B | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| b0922ca5-155b-3885-9de3-852a8b370e75 | -12.3483 | -47.408798 | 2026-07-09 00:06:00 | METOP-B | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 78bf813f-edd6-3d91-9a99-53a8fa4f8dbf | -12.7564 | -44.5257 | 2026-07-09 00:06:00 | METOP-B | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 0fea7493-c9c5-3a2e-afc8-0a365c84334f | -12.7741 | -44.5396 | 2026-07-09 00:10:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 81.2 |
| ac30daf3-7e19-3faf-9f2f-922c4d00bc13 | -9.0156 | -63.5223 | 2026-07-09 00:10:00 | GOES-19 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 41.9 |
| 63a9b822-1813-3355-a64e-4822095a882c | -12.7746 | -44.5162 | 2026-07-09 00:10:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 102.8 |
| 3702323c-6217-3613-b652-5eda3b52c4c3 | -14.9147 | -43.4152 | 2026-07-09 00:10:00 | GOES-19 | GAMELEIRAS | MINAS GERAIS | Brasil | 3127339 | 31 | 33 | nan | nan | nan | Caatinga | 92.9 |
| 920014de-50c3-3f86-abab-f63825172b0e | -12.7548 | -44.5428 | 2026-07-09 00:10:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 131.2 |
| b0b0020b-14be-350b-9e36-6b45a7167e71 | -12.3561 | -47.413 | 2026-07-09 00:10:00 | GOES-19 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 64.2 |
| f836866e-5f42-3a0f-9323-afd761bbd060 | -9.0155 | -63.5411 | 2026-07-09 00:10:00 | GOES-19 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 95.3 |
| 8e424219-aaf9-3a93-bd57-248a3d604ec9 | -12.7553 | -44.5194 | 2026-07-09 00:10:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 164.7 |
| 67f8bb6c-11dc-3df5-9472-cf4824d426d5 | -14.9141 | -43.4394 | 2026-07-09 00:10:00 | GOES-19 | GAMELEIRAS | MINAS GERAIS | Brasil | 3127339 | 31 | 33 | nan | nan | nan | Caatinga | 106.1 |
| 54a9ba9f-6d17-31e7-adf9-817179e93668 | -14.9147 | -43.4152 | 2026-07-09 00:20:00 | GOES-19 | GAMELEIRAS | MINAS GERAIS | Brasil | 3127339 | 31 | 33 | nan | nan | nan | Caatinga | 51.4 |
| 9699fa30-4fb3-3c38-8efd-71dde2f041dc | -9.0155 | -63.5411 | 2026-07-09 00:20:00 | GOES-19 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 52.8 |
| d78c76fd-79f1-36e1-a094-90dcf59b6130 | -12.7746 | -44.5162 | 2026-07-09 00:20:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 51.0 |
| 0d1960ee-4c5c-37b6-b5f0-c5c983367f0e | -12.7553 | -44.5194 | 2026-07-09 00:20:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 247.4 |
| 2b208c7f-267a-3ae7-b48d-3596a49ba15d | -12.7548 | -44.5428 | 2026-07-09 00:20:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 157.7 |
| 3622657a-65bc-3c47-814c-a2ab7f09dcb3 | -9.0155 | -63.5411 | 2026-07-09 00:30:00 | GOES-19 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 41.2 |
| 367f19a6-6fbc-3270-ace8-eccd2b7c50cc | -12.7553 | -44.5194 | 2026-07-09 00:30:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 204.1 |
| eb2f758b-f196-315c-a8a9-059b9b0c0a1e | -12.7746 | -44.5162 | 2026-07-09 00:30:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 50.3 |
| 669d1378-82ab-3d86-b4fe-36fa0f024d8f | -12.7548 | -44.5428 | 2026-07-09 00:30:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 125.0 |
| b6689fda-5a56-39bf-b9ba-581716f0ebd4 | -9.3665 | -44.722198 | 2026-07-09 00:33:00 | METOP-C | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 9e648712-2f9e-36ef-a6fc-1974ae379ed4 | -8.7209 | -48.339699 | 2026-07-09 00:33:00 | METOP-C | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 68dfc5be-a22b-3e97-b654-3fd478c25db4 | -22.285 | -46.859699 | 2026-07-09 00:33:00 | METOP-C | MOGI GUAÇU | SÃO PAULO | Brasil | 3530706 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| b98a07de-2763-36ea-b168-97a4c912c034 | -11.8407 | -48.235802 | 2026-07-09 00:33:00 | METOP-C | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| c5a60e5b-50d4-319c-99f4-1ba768ca06d5 | -7.7141 | -45.161701 | 2026-07-09 00:33:00 | METOP-C | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| a56f7363-5ac3-3e7c-9720-89710bce15c4 | -12.8431 | -44.362999 | 2026-07-09 00:33:00 | METOP-C | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 9211bd24-9044-3591-8860-a53280a9c727 | -19.6064 | -47.5994 | 2026-07-09 00:33:00 | METOP-C | SACRAMENTO | MINAS GERAIS | Brasil | 3156908 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| b827364e-0d83-3876-9262-db948e94e16b | -4.3511 | -47.7682 | 2026-07-09 00:33:00 | METOP-C | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7c13db90-9cd5-3d2d-a0c0-e967c061f3a7 | -12.758 | -44.532101 | 2026-07-09 00:33:00 | METOP-C | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 5c9bbf59-0c3e-34a9-b7d7-166772619c00 | -8.9684 | -48.0186 | 2026-07-09 00:33:00 | METOP-C | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 255d7e11-3df0-3889-836e-727260b75f08 | -7.731 | -44.5658 | 2026-07-09 00:33:00 | METOP-C | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 57d557e1-1e31-3612-b216-558ec8b8ffe4 | -15.8131 | -41.899899 | 2026-07-09 00:33:00 | METOP-C | TAIOBEIRAS | MINAS GERAIS | Brasil | 3168002 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| ab0d3b2c-e6b2-393f-94e9-1dfb3811ead9 | -12.35 | -47.413101 | 2026-07-09 00:33:00 | METOP-C | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| d97ae3c5-a426-3085-90c2-0066bf286d5b | -11.8326 | -48.245899 | 2026-07-09 00:33:00 | METOP-C | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| f0b6dd6f-9a05-35a1-8ca9-a39f97096b59 | -9.3681 | -44.729301 | 2026-07-09 00:33:00 | METOP-C | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 6cdd778d-db27-358a-bae6-514f167bd57e | -7.7157 | -45.1688 | 2026-07-09 00:33:00 | METOP-C | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 5b7912f7-b412-39ab-848e-2e8a1fcba8a1 | -12.9325 | -49.470798 | 2026-07-09 00:33:00 | METOP-C | ARAGUAÇU | TOCANTINS | Brasil | 1702000 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 315f5c03-b028-3791-b1f6-6b60f9d65647 | -4.3413 | -47.770401 | 2026-07-09 00:33:00 | METOP-C | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9181af29-e09f-30d5-8458-131750a73425 | -17.7927 | -43.8652 | 2026-07-09 00:33:00 | METOP-C | BUENÓPOLIS | MINAS GERAIS | Brasil | 3109204 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 59b3b85c-06b7-3237-bc0f-097d48032fd2 | -7.7293 | -44.558498 | 2026-07-09 00:33:00 | METOP-C | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 0916f23b-f036-35b4-b590-78dbccb481d2 | -12.3533 | -47.428299 | 2026-07-09 00:33:00 | METOP-C | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| eb577913-bd0c-31f9-99c5-e400925ef5bf | -10.8528 | -45.040699 | 2026-07-09 00:33:00 | METOP-C | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 66d4ce64-cab1-3af3-b996-12acec676d48 | -17.5881 | -46.675201 | 2026-07-09 00:33:00 | METOP-C | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| ca548d96-10b8-3fdb-b769-f84afbad3682 | -8.7273 | -48.322399 | 2026-07-09 00:33:00 | METOP-C | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 72ca6c29-0300-3b2a-ae93-f5c37aca732c | -12.3517 | -47.4207 | 2026-07-09 00:33:00 | METOP-C | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 357f7928-57e8-3252-aeb1-d7aaf00d6dc8 | -10.8684 | -47.591301 | 2026-07-09 00:33:00 | METOP-C | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 04753035-1a93-36bc-ba66-d1654cd1dcf9 | -12.1777 | -43.447701 | 2026-07-09 00:33:00 | METOP-C | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 31d0abb8-20d6-3505-af74-87ebd76d3d9f | -8.3568 | -45.399899 | 2026-07-09 00:33:00 | METOP-C | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| b08e9b17-c104-3228-8519-5d3995d2a5df | -5.622 | -47.103199 | 2026-07-09 00:33:00 | METOP-C | BURITIRANA | MARANHÃO | Brasil | 2102358 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| b39af0ce-3b18-3b3b-922e-1341246553fe | -2.9587 | -48.986599 | 2026-07-09 00:33:00 | METOP-C | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 830ac424-c07e-3e59-bb7c-52e25363ceee | -8.957 | -48.013401 | 2026-07-09 00:33:00 | METOP-C | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| dd7f51b6-fdbd-3f2b-98b3-47e6debf8e25 | -13.3132 | -43.714802 | 2026-07-09 00:33:00 | METOP-C | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 815a99b7-47c0-351c-8fb1-4bbd7ad71b2a | -6.6748 | -47.520302 | 2026-07-09 00:33:00 | METOP-C | PALMEIRAS DO TOCANTINS | TOCANTINS | Brasil | 1713809 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| f4c50a53-a759-34c2-a979-2989a1b62881 | -10.9762 | -44.678902 | 2026-07-09 00:33:00 | METOP-C | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 8399f36d-94f8-347b-90f8-b79fcd0470f2 | -17.7959 | -43.879601 | 2026-07-09 00:33:00 | METOP-C | BUENÓPOLIS | MINAS GERAIS | Brasil | 3109204 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 72a4ce90-26b2-3a34-8168-2d3d8593a0bf | -10.8701 | -47.598701 | 2026-07-09 00:33:00 | METOP-C | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 5cd2d12e-7881-3126-9ea3-83e13d487232 | -5.726 | -44.5065 | 2026-07-09 00:33:00 | METOP-C | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| e790c5f6-f26d-3f5a-9be2-63569c39eb91 | -7.2841 | -46.2547 | 2026-07-09 00:33:00 | METOP-C | NOVA COLINAS | MARANHÃO | Brasil | 2107258 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 63452eea-ff6c-3a10-8741-2c42ad9521b3 | -22.913799 | -49.2034 | 2026-07-09 00:33:00 | METOP-C | ÁGUAS DE SANTA BÁRBARA | SÃO PAULO | Brasil | 3500550 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 8dfe9b8c-4678-36cf-bfa4-89c694390ac9 | -7.8998 | -48.254101 | 2026-07-09 00:33:00 | METOP-C | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 3e75b359-02e8-3ab8-bfe7-3d108ceb21ec | -15.8112 | -41.8918 | 2026-07-09 00:33:00 | METOP-C | TAIOBEIRAS | MINAS GERAIS | Brasil | 3168002 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 19f990dc-d6bd-3922-93c7-d7dfa2be5c55 | -8.114 | -47.097099 | 2026-07-09 00:33:00 | METOP-C | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| f12eef14-1daf-3da9-a47d-5e6f614f1e65 | -7.5389 | -46.016201 | 2026-07-09 00:33:00 | METOP-C | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| b0dcd841-ec5f-38d3-9214-0fad54666327 | -13.943 | -53.8806 | 2026-07-09 00:33:00 | METOP-C | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 1f622f04-d2aa-30f1-8ae6-1e7a01cd3edf | -8.9668 | -48.0112 | 2026-07-09 00:33:00 | METOP-C | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | nan |


[Clique aqui para ver as próximas entradas](README3.md)
