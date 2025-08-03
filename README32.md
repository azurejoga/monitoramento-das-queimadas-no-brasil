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

## Dados Diários - Página 32

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 1d605069-d341-3922-89ab-f349315fd45c | -10.78769 | -48.8098 | 2025-08-03 12:32:00 | TERRA_M-T | FÁTIMA | TOCANTINS | Brasil | 1707553 | 17 | 33 | nan | nan | nan | Cerrado | 7.2 |
| ffa5853a-52f0-3e0f-8c31-800ae1578f97 | -6.96982 | -43.15246 | 2025-08-03 12:32:00 | TERRA_M-T | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 13.9 |
| 4cf9997f-8d68-31ef-8936-ad0847370e58 | -8.03487 | -43.09711 | 2025-08-03 12:32:00 | TERRA_M-T | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 26.2 |
| 562be516-7546-3994-94f3-5627e1055c4a | -7.65575 | -47.47381 | 2025-08-03 12:32:00 | TERRA_M-T | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 12.8 |
| 1ab67baa-27b4-38c0-81d4-a51b6739f8b4 | -7.63823 | -45.28575 | 2025-08-03 12:32:00 | TERRA_M-T | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 13.1 |
| 55306e8f-2387-3d99-a67b-f2105826729a | -8.374 | -46.93443 | 2025-08-03 12:32:00 | TERRA_M-T | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 83.8 |
| e2667ab5-3178-3042-85f1-df2bf8056343 | -7.59901 | -44.9941 | 2025-08-03 12:32:00 | TERRA_M-T | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 12.4 |
| 196de2eb-398f-31af-9b49-e90eb0a19fc1 | -10.70869 | -48.71547 | 2025-08-03 12:32:00 | TERRA_M-T | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 11.3 |
| 4f720d25-e8ba-3b7a-bff2-c6ce1aba01d6 | -8.0159 | -43.15056 | 2025-08-03 12:32:00 | TERRA_M-T | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 249.4 |
| 8d633b0a-30de-3ee4-a7f4-d9f185a55fd2 | -6.96727 | -43.17206 | 2025-08-03 12:32:00 | TERRA_M-T | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 15.1 |
| 6e304366-bed5-3734-bfb2-397828539d08 | -8.37547 | -46.92352 | 2025-08-03 12:32:00 | TERRA_M-T | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 0e383edf-dca1-37af-9a96-18397079cf61 | -7.59829 | -44.98744 | 2025-08-03 12:32:00 | TERRA_M-T | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 15.2 |
| 6ac18eba-66f5-35b5-8c6c-f774682ca959 | -10.48441 | -46.96977 | 2025-08-03 12:32:00 | TERRA_M-T | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 24.8 |
| a0dde841-fe50-30a5-8735-f57e0b2663d0 | -9.4464 | -46.32019 | 2025-08-03 12:32:00 | TERRA_M-T | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 23.9 |
| df877243-17ad-3dfa-a65f-b9509a229aeb | -7.99771 | -43.18913 | 2025-08-03 12:32:00 | TERRA_M-T | PAVUSSU | PIAUÍ | Brasil | 2207850 | 22 | 33 | nan | nan | nan | Caatinga | 31.6 |
| 99230f89-8bee-3700-870b-d9e16b3fe1c8 | -6.20686 | -44.999 | 2025-08-03 12:32:00 | TERRA_M-T | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 18.9 |
| 8f73f9e8-7f2d-390f-84c9-48c4e4298985 | -7.96208 | -45.11061 | 2025-08-03 12:32:00 | TERRA_M-T | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 35.6 |
| 00e54dad-2af6-37c1-94e8-78de81c0bf05 | -7.68469 | -45.12734 | 2025-08-03 12:32:00 | TERRA_M-T | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 16.2 |
| e03c3b79-7ce3-3c83-a325-fa88eb73f43d | -8.14092 | -49.58728 | 2025-08-03 12:32:00 | TERRA_M-T | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 8.7 |
| 4ccd312d-192d-304a-bd5d-68b8bd0d149e | -8.01062 | -43.19082 | 2025-08-03 12:32:00 | TERRA_M-T | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 211.0 |
| e4a0bdb0-e310-3df8-b224-47b7c4a651b7 | -10.48289 | -46.98127 | 2025-08-03 12:32:00 | TERRA_M-T | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 47.0 |
| 066da361-518f-325f-84bc-106ca60162de | -10.47749 | -46.94511 | 2025-08-03 12:32:00 | TERRA_M-T | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 34.0 |
| ed1bf822-f775-3cca-8f64-a7bc9107f539 | -8.00929 | -43.19721 | 2025-08-03 12:32:00 | TERRA_M-T | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 61.2 |
| 294dd093-3fae-3933-b41d-3429e8016ab5 | -10.12026 | -48.30584 | 2025-08-03 12:32:00 | TERRA_M-T | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 46.6 |
| 95c9b89e-61bb-3ed4-adc7-2decf1e756f8 | -5.13657 | -42.86555 | 2025-08-03 12:32:00 | TERRA_M-T | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 14.7 |
| 1368fb6a-5e2e-3f7e-8ecf-c2868e328443 | -8.33304 | -46.92291 | 2025-08-03 12:32:00 | TERRA_M-T | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 12.8 |
| 781aed71-5be5-3b10-9d5b-c1417e9e79cb | -11.18173 | -45.74897 | 2025-08-03 12:32:00 | TERRA_M-T | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 16.8 |
| b03ec084-983a-3846-95a0-3b0fffedfd03 | -8.00295 | -43.14887 | 2025-08-03 12:32:00 | TERRA_M-T | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 399.2 |
| 9a348948-01e0-3d9c-9271-965d52b51b13 | -10.47982 | -47.00451 | 2025-08-03 12:32:00 | TERRA_M-T | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 8.2 |
| b88ce2fc-0408-3a51-b8c2-da78bf37f1ca | -7.64114 | -45.29198 | 2025-08-03 12:32:00 | TERRA_M-T | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 16.0 |
| 3920393b-3725-3f64-9755-d5d565ce1d1b | -10.47596 | -46.95675 | 2025-08-03 12:32:00 | TERRA_M-T | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 13.4 |
| be40f7ed-a474-3de4-a023-2c4f35ccfe64 | -8.03231 | -43.11771 | 2025-08-03 12:32:00 | TERRA_M-T | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 57.3 |
| 25c2f7e7-3975-348b-bcd1-91a54183f688 | -11.17992 | -45.76342 | 2025-08-03 12:32:00 | TERRA_M-T | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 12.4 |
| e71bc529-7ca4-3676-8f12-b04080bf65d3 | -10.1216 | -48.29609 | 2025-08-03 12:32:00 | TERRA_M-T | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 10.0 |
| 1d1f4554-8adb-386b-a5c4-abebc59eadf9 | -9.4448 | -46.33248 | 2025-08-03 12:32:00 | TERRA_M-T | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 872b1684-fc9c-3988-a36e-333c89b3143c | -8.00132 | -43.15519 | 2025-08-03 12:32:00 | TERRA_M-T | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 305.1 |
| ba9b4836-fd47-3521-b25b-7aa271404b6d | -8.00033 | -43.16895 | 2025-08-03 12:32:00 | TERRA_M-T | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 223.8 |
| 0829c19e-274a-3cd3-9d20-b58e22fdeb86 | -8.37253 | -46.94529 | 2025-08-03 12:32:00 | TERRA_M-T | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 59.4 |
| f8e34e33-8f8c-369b-8c7a-76b5336c8a9a | -10.71778 | -48.71674 | 2025-08-03 12:32:00 | TERRA_M-T | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 14.9 |
| 7b8f0fb3-39f9-3237-a7db-a4d40d5246c1 | -8.01178 | -43.17706 | 2025-08-03 12:32:00 | TERRA_M-T | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 355.1 |
| 98022572-fdea-3a13-aa03-a158bd44cd34 | -10.11892 | -48.31559 | 2025-08-03 12:32:00 | TERRA_M-T | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 17.6 |
| ed88dc89-4bf8-3ee1-a5dc-2082db6c5074 | -7.65713 | -47.46382 | 2025-08-03 12:32:00 | TERRA_M-T | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 15.9 |
| 59ecf4dc-89f8-359d-896a-0ff907391453 | -8.00381 | -43.13477 | 2025-08-03 12:32:00 | TERRA_M-T | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 64.3 |
| 1f4bef0c-62b4-33d3-b759-90f5a36945d1 | -6.35287 | -46.15792 | 2025-08-03 12:32:00 | TERRA_M-T | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 572dc557-b359-3e48-813d-78e511dad392 | -12.62626 | -44.50437 | 2025-08-03 12:34:00 | TERRA_M-T | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 35.5 |
| 1eedcf2e-6fcb-3545-950d-10f78d513c41 | -21.00305 | -45.97966 | 2025-08-03 12:34:00 | TERRA_M-T | CARMO DO RIO CLARO | MINAS GERAIS | Brasil | 3114402 | 31 | 33 | nan | nan | nan | Cerrado | 22.7 |
| 96729ba7-a6f9-3043-867d-b2488e065d9f | -13.03035 | -47.40725 | 2025-08-03 12:34:00 | TERRA_M-T | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 11.7 |
| 97f376b5-5a87-3a87-8838-743a736bcc51 | -15.54444 | -47.29615 | 2025-08-03 12:34:00 | TERRA_M-T | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 82fa58b4-3e07-37bd-8c26-e4ac457faf2f | -12.49035 | -47.165 | 2025-08-03 12:34:00 | TERRA_M-T | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 12.8 |
| 80b69fbd-e4da-371b-8854-dd15f42e71cc | -12.65295 | -45.04659 | 2025-08-03 12:34:00 | TERRA_M-T | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 34.9 |
| 85d8e322-ba74-3a00-9dcd-6a5528569d66 | -12.45927 | -47.01834 | 2025-08-03 12:34:00 | TERRA_M-T | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 16.7 |
| 3a9cf3be-272e-3dae-b957-bf31f547d3b2 | -11.7705 | -44.98113 | 2025-08-03 12:34:00 | TERRA_M-T | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 21.1 |
| 2bfcde7b-5be5-3462-8c71-c5cf879e15fe | -11.96542 | -46.72006 | 2025-08-03 12:34:00 | TERRA_M-T | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 2a01f6d7-8a79-3580-afaa-9d31991f47d3 | -21.01502 | -45.9742 | 2025-08-03 12:34:00 | TERRA_M-T | CARMO DO RIO CLARO | MINAS GERAIS | Brasil | 3114402 | 31 | 33 | nan | nan | nan | Cerrado | 27.0 |
| 6246560e-1ce2-3dbf-8718-67583803d31c | -14.38133 | -50.3302 | 2025-08-03 12:34:00 | TERRA_M-T | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 9.8 |
| 11849406-0797-353f-9958-f93852ad0e28 | -13.45828 | -51.61653 | 2025-08-03 12:34:00 | TERRA_M-T | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 26.9 |
| 0cd04150-17dc-35fe-a24a-efba4c9d099d | -19.15399 | -49.12866 | 2025-08-03 12:34:00 | TERRA_M-T | PRATA | MINAS GERAIS | Brasil | 3152808 | 31 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 6301a15f-52f4-3992-8037-44530aacfb48 | -11.92991 | -44.97658 | 2025-08-03 12:34:00 | TERRA_M-T | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 16.5 |
| 489bedf9-c32a-3ba7-9d51-40a6be095737 | -13.46363 | -51.58002 | 2025-08-03 12:34:00 | TERRA_M-T | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 13.3 |
| 72468aad-aa8f-3376-8751-1a12bc3d12e4 | -13.45962 | -51.6074 | 2025-08-03 12:34:00 | TERRA_M-T | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 31.7 |
| 326997dc-95ea-3f36-abdc-1d0620833dc1 | -14.30595 | -57.76456 | 2025-08-03 12:34:00 | TERRA_M-T | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Amazônia | 61.0 |
| 0a39ec9a-fbcd-3d2f-9dd7-07fd8024cacc | -11.93181 | -44.96098 | 2025-08-03 12:34:00 | TERRA_M-T | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 19.1 |
| 44d27f08-5e92-3c56-897c-ef4d88bc41a1 | -17.3301 | -42.60219 | 2025-08-03 12:34:00 | TERRA_M-T | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 30.7 |
| 9408003b-0dd9-3024-b7cb-4981e8d8bffb | -11.78028 | -44.99922 | 2025-08-03 12:34:00 | TERRA_M-T | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 13.4 |
| dc1070cc-f933-3ab0-8db2-50f9b5541686 | -14.1199 | -45.41265 | 2025-08-03 12:34:00 | TERRA_M-T | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 79.7 |
| a2c14a87-83d1-34b2-b83f-6defa113836d | -17.32545 | -42.6088 | 2025-08-03 12:34:00 | TERRA_M-T | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 35.5 |
| c6fd80fc-6f0c-3c54-97b7-519fd0296cc6 | -14.122 | -45.39548 | 2025-08-03 12:34:00 | TERRA_M-T | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 15.9 |
| 9556fff4-7f26-3c76-856c-1a8ab37db0e7 | -16.75241 | -49.07838 | 2025-08-03 12:34:00 | TERRA_M-T | SENADOR CANEDO | GOIÁS | Brasil | 5220454 | 52 | 33 | nan | nan | nan | Cerrado | 9.1 |
| ffb4bdda-de40-31bb-8834-bdfdc0d35aa7 | -18.73657 | -47.53726 | 2025-08-03 12:34:00 | TERRA_M-T | MONTE CARMELO | MINAS GERAIS | Brasil | 3143104 | 31 | 33 | nan | nan | nan | Cerrado | 28.3 |
| dc8782ad-5645-34b4-ad08-8be01ec6415e | -12.41036 | -47.07416 | 2025-08-03 12:34:00 | TERRA_M-T | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 9.9 |
| 70480515-a6b0-3e3c-8b79-e3d041be7f27 | -11.21819 | -51.5355 | 2025-08-03 12:34:00 | TERRA_M-T | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Cerrado | 69.2 |
| 079c973b-9eca-38ab-af04-e1a5d85ef5fb | -13.46497 | -51.5709 | 2025-08-03 12:34:00 | TERRA_M-T | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 12.6 |
| 099358db-d8fe-37b6-a3f8-489bda23d58c | -11.21682 | -51.54473 | 2025-08-03 12:34:00 | TERRA_M-T | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Cerrado | 13.6 |
| c8cc369d-545f-34fe-ab66-b2f3c4f53b5f | -21.0157 | -45.98103 | 2025-08-03 12:34:00 | TERRA_M-T | CARMO DO RIO CLARO | MINAS GERAIS | Brasil | 3114402 | 31 | 33 | nan | nan | nan | Cerrado | 33.7 |
| e9f94281-4279-37c2-9a48-49bae18e87b6 | -12.22029 | -44.18774 | 2025-08-03 12:34:00 | TERRA_M-T | CRISTÓPOLIS | BAHIA | Brasil | 2909703 | 29 | 33 | nan | nan | nan | Cerrado | 38.7 |
| 61157e57-6c78-3f2b-bbd3-9d5390161abd | -11.9437 | -44.96266 | 2025-08-03 12:34:00 | TERRA_M-T | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 18.5 |
| 0ccf7339-63f7-3a00-994b-6725d3b1329d | -11.21198 | -51.5157 | 2025-08-03 12:34:00 | TERRA_M-T | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Cerrado | 6.1 |
| d60a1c9a-74b2-34a5-9e64-1ea1cad7785c | -12.69191 | -48.09787 | 2025-08-03 12:34:00 | TERRA_M-T | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 12.8 |
| a0d8bff6-46d8-30be-b5d6-6ead31d5c65a | -13.45476 | -51.57869 | 2025-08-03 12:34:00 | TERRA_M-T | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 10.7 |
| cc18f376-809f-371c-b0a5-e294a0f52843 | -12.68376 | -48.08606 | 2025-08-03 12:34:00 | TERRA_M-T | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 12.6 |
| 173098b1-6472-304e-939c-59908e8cec85 | -14.10801 | -45.41116 | 2025-08-03 12:34:00 | TERRA_M-T | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 136.8 |
| da77b2bd-acdd-3d98-9199-b09eff784bae | -18.73824 | -47.52291 | 2025-08-03 12:34:00 | TERRA_M-T | MONTE CARMELO | MINAS GERAIS | Brasil | 3143104 | 31 | 33 | nan | nan | nan | Cerrado | 10.7 |
| 81bfa028-e103-3ca3-904c-48b10d688878 | -15.5461 | -47.28314 | 2025-08-03 12:34:00 | TERRA_M-T | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 8.4 |
| 3d5548b2-62d7-339e-be41-898bc6c192ca | -12.69657 | -48.09431 | 2025-08-03 12:34:00 | TERRA_M-T | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 12.6 |
| b28bfef4-3d8d-3836-93db-99179ecd6d53 | -4.5684 | -44.2036 | 2025-08-03 12:50:00 | GOES-19 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 86.3 |
| 1fcb2234-d198-341f-b77c-68007a152fe4 | -11.9395 | -44.9729 | 2025-08-03 12:50:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 127.0 |
| 4a6491a0-f7dd-319b-a8e7-de2ac45b1024 | -10.4767 | -46.943 | 2025-08-03 12:50:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 69.4 |
| 3e3258d3-55a5-3a16-8e31-3cc0b7a1eb4d | -8.0324 | -43.1022 | 2025-08-03 13:00:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 81.1 |
| a3607470-af80-3958-a863-44c4ecc66879 | -4.5684 | -44.2036 | 2025-08-03 13:00:00 | GOES-19 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 104.4 |
| c67cd683-5e5c-3d75-816d-ac46ce5d87e6 | -11.9395 | -44.9729 | 2025-08-03 13:00:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 238.5 |
| 6c50476a-15ee-3617-8ba2-25bc2a247e84 | -7.6873 | -45.1272 | 2025-08-03 13:00:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 143.9 |
| f34093d4-abc1-3b1d-be64-01f6250c6690 | -7.6876 | -45.1044 | 2025-08-03 13:00:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 73.0 |
| 811efb2f-2468-344c-a8f0-2a9d947c4c04 | -10.4764 | -46.9654 | 2025-08-03 13:00:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 65.3 |
| 190285a9-04c1-3643-a729-bd18f419c045 | -11.9399 | -44.9497 | 2025-08-03 13:00:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 101.1 |
| 6076d151-77d8-3292-af46-a4045d0a17f3 | -4.5497 | -44.2047 | 2025-08-03 13:00:00 | GOES-19 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 100.4 |
| 2c274674-8c4d-3805-b1f3-c3c4ff97a3a8 | -8.0513 | -43.1001 | 2025-08-03 13:00:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 89.6 |
| 26a7d838-11e4-3eb7-a641-e6ce0d8b79d1 | -4.5497 | -44.2047 | 2025-08-03 13:10:00 | GOES-19 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 132.5 |
| b765ab1b-bbea-39ea-ab7d-c7786e86bc59 | -4.5684 | -44.2036 | 2025-08-03 13:10:00 | GOES-19 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 107.5 |
| 3ed644c4-4d38-32b6-8e93-a97ab6676e9d | -12.4588 | -47.0173 | 2025-08-03 13:10:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 128.9 |
| 15215798-9d1b-3e3f-9184-b109e20c9a90 | -11.9395 | -44.9729 | 2025-08-03 13:10:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 212.8 |


[Clique aqui para ver as próximas entradas](README33.md)
