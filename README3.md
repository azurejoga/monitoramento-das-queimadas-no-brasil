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
| 1e6b0fa9-a470-349a-af17-90de81c5a09f | -7.38462 | -35.2749 | 2025-11-21 03:21:00 | NOAA-21 | ITAMBÉ | PERNAMBUCO | Brasil | 2607653 | 26 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| eae9a82d-127a-352d-bb74-d83a46ef0193 | -4.14518 | -43.67192 | 2025-11-21 03:21:00 | NOAA-21 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 5.5 |
| b9105ca3-f037-3ff2-bab5-1df74cd6d830 | -5.42873 | -40.66745 | 2025-11-21 03:21:00 | NOAA-21 | CRATEÚS | CEARÁ | Brasil | 2304103 | 23 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 16dc7078-001d-393f-8257-375b3560a7d0 | -6.24135 | -37.23409 | 2025-11-21 03:21:00 | NOAA-21 | JARDIM DE PIRANHAS | RIO GRANDE DO NORTE | Brasil | 2405603 | 24 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 1d1feb0d-7671-36ae-98d0-f6ec968839d2 | -4.14023 | -43.70024 | 2025-11-21 03:21:00 | NOAA-21 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 71eb05e1-7d4b-3fa7-9fe7-67abf1583285 | -6.79595 | -39.55072 | 2025-11-21 03:21:00 | NOAA-21 | FARIAS BRITO | CEARÁ | Brasil | 2304301 | 23 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 81c586dd-b2c7-3308-a084-456dd39e52d2 | -4.14491 | -43.69398 | 2025-11-21 03:21:00 | NOAA-21 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 5.2 |
| e5137348-1ace-3ea2-8a2b-3d03dea30c77 | -6.76646 | -35.44907 | 2025-11-21 03:21:00 | NOAA-21 | PIRPIRITUBA | PARAÍBA | Brasil | 2511806 | 25 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 843528c6-0bc1-3c51-8c6f-c3be09c299a4 | -3.14166 | -40.18371 | 2025-11-21 03:21:00 | NOAA-21 | MARCO | CEARÁ | Brasil | 2307809 | 23 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 81840701-9162-3b81-84c5-08fa84b40f8f | -4.14035 | -43.67871 | 2025-11-21 03:21:00 | NOAA-21 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| fc36c51f-5aa4-35d2-9f38-364f78ab8d91 | -6.79707 | -39.54429 | 2025-11-21 03:21:00 | NOAA-21 | FARIAS BRITO | CEARÁ | Brasil | 2304301 | 23 | 33 | nan | nan | nan | Caatinga | 3.0 |
| 36111fdc-6404-3828-bca7-1a32bcd5a1b7 | -6.23768 | -37.23111 | 2025-11-21 03:21:00 | NOAA-21 | JARDIM DE PIRANHAS | RIO GRANDE DO NORTE | Brasil | 2405603 | 24 | 33 | nan | nan | nan | Caatinga | 2.0 |
| d8bfab6d-18fb-3ca1-866e-da8f38cd8480 | -7.11254 | -35.11932 | 2025-11-21 03:21:00 | NOAA-21 | CRUZ DO ESPÍRITO SANTO | PARAÍBA | Brasil | 2504900 | 25 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| 065c0d35-3b6f-3c95-b0bc-ec54e46c797d | -4.62686 | -37.9409 | 2025-11-21 03:21:00 | NOAA-21 | ARACATI | CEARÁ | Brasil | 2301109 | 23 | 33 | nan | nan | nan | Caatinga | 1.6 |
| e903931b-5a70-3d1b-bf4a-f1954bbf333d | -4.14271 | -43.68607 | 2025-11-21 03:21:00 | NOAA-21 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 4.6 |
| a69f5b2b-b288-3803-8895-f8284a171117 | -4.17007 | -43.67655 | 2025-11-21 03:21:00 | NOAA-21 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 23.4 |
| dfe46663-c470-373d-b72b-30ee74ba5a09 | -4.16651 | -43.67567 | 2025-11-21 03:21:00 | NOAA-21 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 19.2 |
| 2afd77da-f56a-3784-afac-47af22782d35 | -4.14361 | -43.70119 | 2025-11-21 03:21:00 | NOAA-21 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 6.5 |
| e3d74e94-084a-399d-b895-7d9d8f6a5214 | -6.03924 | -36.78716 | 2025-11-21 03:21:00 | NOAA-21 | SANTANA DO MATOS | RIO GRANDE DO NORTE | Brasil | 2411403 | 24 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 41fcd4fa-e423-3c59-ab0c-f44f0586fc5c | -6.79651 | -39.5475 | 2025-11-21 03:21:00 | NOAA-21 | FARIAS BRITO | CEARÁ | Brasil | 2304301 | 23 | 33 | nan | nan | nan | Caatinga | 2.4 |
| b8047523-7a2f-3ac8-8b97-18aad3cc6bf3 | -3.14764 | -40.17868 | 2025-11-21 03:21:00 | NOAA-21 | MARCO | CEARÁ | Brasil | 2307809 | 23 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 2ba89398-8606-3686-9038-9e2d4eed6bdf | -4.16297 | -43.67528 | 2025-11-21 03:21:00 | NOAA-21 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 9.4 |
| c8677066-11be-345f-aca5-361e6b82f2de | -2.93956 | -41.0584 | 2025-11-21 03:21:00 | NOAA-21 | CAMOCIM | CEARÁ | Brasil | 2302602 | 23 | 33 | nan | nan | nan | Caatinga | 2.5 |
| d3e50166-5703-3c59-8325-a23c081b5c92 | -4.2431 | -39.74396 | 2025-11-21 03:21:00 | NOAA-21 | CANINDÉ | CEARÁ | Brasil | 2302800 | 23 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 67d4375e-baf3-39a0-a3c1-fb1c6e5ab49a | -5.17049 | -35.85818 | 2025-11-21 03:21:00 | NOAA-21 | PEDRA GRANDE | RIO GRANDE DO NORTE | Brasil | 2409506 | 24 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 5941e667-eee5-3ba4-9790-18cce6805a4e | -6.31299 | -43.81581 | 2025-11-21 03:23:00 | NOAA-21 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| a60d139d-36a3-32aa-a8b4-45b654b508a5 | -8.92062 | -35.17568 | 2025-11-21 03:23:00 | NOAA-21 | MARAGOGI | ALAGOAS | Brasil | 2704500 | 27 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| fe058e5c-f517-33a4-aa24-dba07698f470 | -8.28916 | -35.26102 | 2025-11-21 03:23:00 | NOAA-21 | ESCADA | PERNAMBUCO | Brasil | 2605202 | 26 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 24009f13-7729-377e-9bd2-780e85b70882 | -10.14153 | -36.38583 | 2025-11-21 03:23:00 | NOAA-21 | PENEDO | ALAGOAS | Brasil | 2706703 | 27 | 33 | nan | nan | nan | Mata Atlântica | 7.1 |
| 51e33021-a931-397a-be11-214b047e294f | -10.13747 | -36.38518 | 2025-11-21 03:23:00 | NOAA-21 | PENEDO | ALAGOAS | Brasil | 2706703 | 27 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| e1fb7edc-fb4a-39d7-95f6-83103f563f35 | -8.28838 | -35.2657 | 2025-11-21 03:23:00 | NOAA-21 | ESCADA | PERNAMBUCO | Brasil | 2605202 | 26 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| eaf37fb5-bd56-3d9a-9831-e3ef30eb9510 | -8.18304 | -35.24542 | 2025-11-21 03:23:00 | NOAA-21 | VITÓRIA DE SANTO ANTÃO | PERNAMBUCO | Brasil | 2616407 | 26 | 33 | nan | nan | nan | Mata Atlântica | 0.3 |
| 872b7439-2b03-3356-971e-20b4f0e89c2c | -10.14091 | -36.38943 | 2025-11-21 03:23:00 | NOAA-21 | PENEDO | ALAGOAS | Brasil | 2706703 | 27 | 33 | nan | nan | nan | Mata Atlântica | 7.1 |
| d0332f3f-bf9d-3d1e-bea1-73bebc6ae578 | -20.06559 | -40.84234 | 2025-11-21 03:25:00 | NOAA-21 | SANTA MARIA DE JETIBÁ | ESPÍRITO SANTO | Brasil | 3204559 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 56713179-b168-396c-8569-750252af5282 | -18.76335 | -45.28286 | 2025-11-21 03:25:00 | NOAA-21 | MORADA NOVA DE MINAS | MINAS GERAIS | Brasil | 3143500 | 31 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 53a90b0a-9f25-3f32-9f5d-0b982b612061 | -17.07313 | -46.5984 | 2025-11-21 03:25:00 | NOAA-21 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 54222479-2e3a-3556-889d-4314689c093d | -18.61284 | -44.26295 | 2025-11-21 03:25:00 | NOAA-21 | INIMUTABA | MINAS GERAIS | Brasil | 3131109 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| e920f66b-0a35-33d4-91fe-4b5fccc37e99 | -18.27433 | -42.37643 | 2025-11-21 03:25:00 | NOAA-21 | SANTA MARIA DO SUAÇUÍ | MINAS GERAIS | Brasil | 3158201 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 12026575-4f12-36ca-b292-62636c322952 | -17.40112 | -44.47313 | 2025-11-21 03:25:00 | NOAA-21 | JEQUITAÍ | MINAS GERAIS | Brasil | 3135605 | 31 | 33 | nan | nan | nan | Cerrado | 4.4 |
| fc260025-5a2b-3d12-bc9a-195f518d8d6c | -17.64287 | -43.88343 | 2025-11-21 03:25:00 | NOAA-21 | BOCAIÚVA | MINAS GERAIS | Brasil | 3107307 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 91884b14-136a-3665-b743-19b8a5e322e6 | -18.65716 | -42.13125 | 2025-11-21 03:25:00 | NOAA-21 | GOVERNADOR VALADARES | MINAS GERAIS | Brasil | 3127701 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.1 |
| 6d45c015-03e0-37c6-bd2a-466da453f13e | -17.81013 | -44.30825 | 2025-11-21 03:25:00 | NOAA-21 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 6d8ee45f-1984-3cd7-ad48-5d01835dfb94 | -17.6486 | -43.88471 | 2025-11-21 03:25:00 | NOAA-21 | BOCAIÚVA | MINAS GERAIS | Brasil | 3107307 | 31 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 55374962-1732-314e-8ee5-64008fde7708 | -17.58073 | -46.67595 | 2025-11-21 03:25:00 | NOAA-21 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 3d7c63d6-7402-3861-ba71-8efa256121a8 | -17.81357 | -44.34848 | 2025-11-21 03:25:00 | NOAA-21 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 274cbd67-c0ea-3f12-8745-2443e9611679 | -18.76228 | -45.28768 | 2025-11-21 03:25:00 | NOAA-21 | MORADA NOVA DE MINAS | MINAS GERAIS | Brasil | 3143500 | 31 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 2402d184-4ac5-3fba-9179-ad3b1b0a22ff | -16.41267 | -43.1274 | 2025-11-21 03:25:00 | NOAA-21 | GRÃO MOGOL | MINAS GERAIS | Brasil | 3127800 | 31 | 33 | nan | nan | nan | Cerrado | 2.7 |
| e0da4b93-d644-37a0-b50d-df8e4ac48cd4 | -17.07986 | -46.60007 | 2025-11-21 03:25:00 | NOAA-21 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 16192bcc-08b2-36ac-8be4-27e96635b7c6 | -18.28016 | -42.37436 | 2025-11-21 03:25:00 | NOAA-21 | SANTA MARIA DO SUAÇUÍ | MINAS GERAIS | Brasil | 3158201 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 4d718587-4ea6-3542-8be2-c638102b9450 | -17.83127 | -46.99873 | 2025-11-21 03:25:00 | NOAA-21 | GUARDA-MOR | MINAS GERAIS | Brasil | 3128600 | 31 | 33 | nan | nan | nan | Cerrado | 3.1 |
| a6a54be6-49b1-3a78-b8dd-19a9c37eb208 | -17.58599 | -46.68398 | 2025-11-21 03:25:00 | NOAA-21 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 98ea6af4-94de-38db-83ca-e891eb15c1b3 | -17.40028 | -44.47698 | 2025-11-21 03:25:00 | NOAA-21 | JEQUITAÍ | MINAS GERAIS | Brasil | 3135605 | 31 | 33 | nan | nan | nan | Cerrado | 4.4 |
| ab5cf7eb-4698-33e6-a8e2-be2cfbf82710 | -17.64769 | -43.889 | 2025-11-21 03:25:00 | NOAA-21 | BOCAIÚVA | MINAS GERAIS | Brasil | 3107307 | 31 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 5854ea2b-9a82-3cb6-a3c0-50d8162de02b | -17.64196 | -43.88771 | 2025-11-21 03:25:00 | NOAA-21 | BOCAIÚVA | MINAS GERAIS | Brasil | 3107307 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c25e4ab3-ff75-3397-9507-0b94d5924bbe | -17.80906 | -44.3131 | 2025-11-21 03:25:00 | NOAA-21 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| c9adc8e4-3c90-3198-bb97-7816951a5634 | -18.27952 | -42.37744 | 2025-11-21 03:25:00 | NOAA-21 | SANTA MARIA DO SUAÇUÍ | MINAS GERAIS | Brasil | 3158201 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 897e7483-3bae-32a8-9fc8-3a4d24086c5f | -18.76269 | -45.28506 | 2025-11-21 03:25:00 | NOAA-21 | MORADA NOVA DE MINAS | MINAS GERAIS | Brasil | 3143500 | 31 | 33 | nan | nan | nan | Cerrado | 4.9 |
| eebd02e6-4d89-3f47-9418-b360e1e79e58 | -18.27888 | -42.38053 | 2025-11-21 03:25:00 | NOAA-21 | SANTA MARIA DO SUAÇUÍ | MINAS GERAIS | Brasil | 3158201 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 3ceba5d5-7607-3a7f-a84e-0ca9e3cd8f42 | -16.4105 | -43.12609 | 2025-11-21 03:25:00 | NOAA-21 | GRÃO MOGOL | MINAS GERAIS | Brasil | 3127800 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 9842866e-e7ad-34ab-8877-c856afef14d5 | -17.58254 | -46.67708 | 2025-11-21 03:25:00 | NOAA-21 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 6.1 |
| c4049e9e-153e-341e-b8cb-578eddc2975b | -17.58775 | -46.68508 | 2025-11-21 03:25:00 | NOAA-21 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 8.5 |
| f6e0ae8a-cc0d-3691-b85c-f5e18e93cc7e | -16.4161 | -43.12731 | 2025-11-21 03:25:00 | NOAA-21 | GRÃO MOGOL | MINAS GERAIS | Brasil | 3127800 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| d7edff22-dff5-3468-9697-8c4e2c508ced | -17.64896 | -43.88601 | 2025-11-21 03:25:00 | NOAA-21 | BOCAIÚVA | MINAS GERAIS | Brasil | 3107307 | 31 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 260fd8ea-e7eb-32d6-b700-0c2a4ab45980 | -17.80578 | -44.3091 | 2025-11-21 03:25:00 | NOAA-21 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 1118b822-87e2-3350-9935-da5054a19238 | -21.24243 | -44.0827 | 2025-11-21 03:27:00 | NOAA-21 | SÃO JOÃO DEL REI | MINAS GERAIS | Brasil | 3162500 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.7 |
| b0f183ec-ef6e-38b6-b231-9199c18b971b | -19.85603 | -46.30545 | 2025-11-21 03:27:00 | NOAA-21 | TAPIRAÍ | MINAS GERAIS | Brasil | 3168200 | 31 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 23574cd9-1636-309e-8850-bd5c6385be31 | -19.85476 | -46.31097 | 2025-11-21 03:27:00 | NOAA-21 | TAPIRAÍ | MINAS GERAIS | Brasil | 3168200 | 31 | 33 | nan | nan | nan | Cerrado | 3.8 |
| da374c3a-e985-3fb0-818f-f9eeef632e1a | -21.04302 | -48.55965 | 2025-11-21 03:27:00 | NOAA-21 | BEBEDOURO | SÃO PAULO | Brasil | 3506102 | 35 | 33 | nan | nan | nan | Mata Atlântica | 6.2 |
| 8836cbfe-ecc7-3e14-9830-6a23b8996387 | -21.04106 | -48.55875 | 2025-11-21 03:27:00 | NOAA-21 | BEBEDOURO | SÃO PAULO | Brasil | 3506102 | 35 | 33 | nan | nan | nan | Mata Atlântica | 7.0 |
| ff328975-9e23-3101-ac16-eb8699fd8762 | -22.03805 | -47.19161 | 2025-11-21 03:27:00 | NOAA-21 | AGUAÍ | SÃO PAULO | Brasil | 3500303 | 35 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 80761740-d392-309e-a9d8-36d7f3a1b8ff | -22.92155 | -48.68397 | 2025-11-21 03:27:00 | NOAA-21 | BOTUCATU | SÃO PAULO | Brasil | 3507506 | 35 | 33 | nan | nan | nan | Cerrado | 9.7 |
| 9460488e-fe25-397c-bdb3-dbc44a83bd64 | -22.51866 | -44.32253 | 2025-11-21 03:27:00 | NOAA-21 | BARRA MANSA | RIO DE JANEIRO | Brasil | 3300407 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 7e39cbd9-3fca-3518-808f-24b80dc6df76 | -19.85709 | -46.31011 | 2025-11-21 03:27:00 | NOAA-21 | TAPIRAÍ | MINAS GERAIS | Brasil | 3168200 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 56bbe04e-e4fc-3290-84c4-dd928fbffa1f | -22.92323 | -48.67738 | 2025-11-21 03:27:00 | NOAA-21 | BOTUCATU | SÃO PAULO | Brasil | 3507506 | 35 | 33 | nan | nan | nan | Cerrado | 9.7 |
| 6c420a0f-908e-33c3-a3ab-5c4f246ad484 | -21.24865 | -44.08029 | 2025-11-21 03:27:00 | NOAA-21 | SÃO JOÃO DEL REI | MINAS GERAIS | Brasil | 3162500 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 66a9facf-861c-30d1-a188-01305ec1bbf8 | -22.51702 | -44.32985 | 2025-11-21 03:27:00 | NOAA-21 | RESENDE | RIO DE JANEIRO | Brasil | 3304201 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| e7062cb9-83a7-3c3b-99ad-1da75908c91c | -19.85066 | -46.30907 | 2025-11-21 03:27:00 | NOAA-21 | TAPIRAÍ | MINAS GERAIS | Brasil | 3168200 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 0b82fc4b-932a-376d-8577-7509fb853d01 | -23.42159 | -45.68964 | 2025-11-21 03:27:00 | NOAA-21 | PARAIBUNA | SÃO PAULO | Brasil | 3535606 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 5fec0991-f877-3181-a70e-90d1f8df2590 | -27.17624 | -51.2468 | 2025-11-21 03:29:00 | NOAA-21 | IBIAM | SANTA CATARINA | Brasil | 4206751 | 42 | 33 | nan | nan | nan | Mata Atlântica | 10.9 |
| 0ed82279-d684-3788-bb61-a471ac4050ac | -2.88997 | -41.68862 | 2025-11-21 03:51:00 | NPP-375D | PARNAÍBA | PIAUÍ | Brasil | 2207702 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| d55a881f-9e76-30d0-80a3-735d90177dee | -3.14375 | -40.18267 | 2025-11-21 03:51:00 | NPP-375D | MARCO | CEARÁ | Brasil | 2307809 | 23 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 871606dc-acfc-3a2a-bae4-762ba181f48d | -3.43558 | -44.36693 | 2025-11-21 03:51:00 | NPP-375D | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 85b85bc8-caab-3fd4-bbcf-b65a008020e6 | -3.94745 | -42.86699 | 2025-11-21 03:51:00 | NPP-375D | BURITI | MARANHÃO | Brasil | 2102200 | 21 | 33 | nan | nan | nan | Caatinga | 2.5 |
| e056ae55-a5ad-3c11-bd85-ef267995fcc0 | -3.43508 | -44.36987 | 2025-11-21 03:51:00 | NPP-375D | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 75a560e1-8bfc-3443-92ca-50598d2cb6f3 | -8.9212 | -35.17658 | 2025-11-21 03:51:00 | NPP-375D | MARAGOGI | ALAGOAS | Brasil | 2704500 | 27 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 220cc32e-5e32-3fd5-b013-7950a27f8c21 | -2.89324 | -41.68886 | 2025-11-21 03:51:00 | NPP-375D | PARNAÍBA | PIAUÍ | Brasil | 2207702 | 22 | 33 | nan | nan | nan | Cerrado | 3.0 |
| ae6c6f7a-5369-3e6b-8d7b-cfa7ea9ed666 | -6.51917 | -39.26867 | 2025-11-21 03:51:00 | NPP-375D | IGUATU | CEARÁ | Brasil | 2305506 | 23 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 4a3e5897-d774-3066-bf0b-0f3fab82af5d | -6.79527 | -39.54647 | 2025-11-21 03:51:00 | NPP-375D | FARIAS BRITO | CEARÁ | Brasil | 2304301 | 23 | 33 | nan | nan | nan | Caatinga | 3.9 |
| e6344151-e983-3f4b-a9ca-a1fc33766804 | -7.11343 | -35.12268 | 2025-11-21 03:51:00 | NPP-375D | CRUZ DO ESPÍRITO SANTO | PARAÍBA | Brasil | 2504900 | 25 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 54294e3a-fca9-3f37-9813-123e810d4fa8 | -6.22292 | -46.249 | 2025-11-21 03:51:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 1d6b98cb-c9d3-3de7-82f1-ea15b7130055 | -4.14333 | -43.6879 | 2025-11-21 03:51:00 | NPP-375D | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| ee0d00ef-5bf8-361f-ac21-879643c172ae | -5.49705 | -46.36222 | 2025-11-21 03:51:00 | NPP-375D | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 3ec80d8a-51cb-3aff-a93e-021d26728049 | -3.4319 | -44.36685 | 2025-11-21 03:51:00 | NPP-375D | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 42a0fa3c-02ce-3c7c-b5e8-8ba6919ed0a0 | -6.22324 | -48.0761 | 2025-11-21 03:51:00 | NPP-375D | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 6396a0ae-af90-3656-84b3-d3672a5a3192 | -3.63446 | -43.9478 | 2025-11-21 03:51:00 | NPP-375D | VARGEM GRANDE | MARANHÃO | Brasil | 2112704 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 7cc9f7bb-4f2c-3a11-a6df-0463a26806f2 | -2.95857 | -41.55608 | 2025-11-21 03:51:00 | NPP-375D | LUÍS CORREIA | PIAUÍ | Brasil | 2205706 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 25198ac9-868e-3fe1-8d91-484df4aa8cff | -4.63192 | -43.3969 | 2025-11-21 03:51:00 | NPP-375D | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 84c32f96-2fc8-318f-9807-af2b9fcbdd2e | -6.79817 | -39.55099 | 2025-11-21 03:51:00 | NPP-375D | FARIAS BRITO | CEARÁ | Brasil | 2304301 | 23 | 33 | nan | nan | nan | Caatinga | 4.5 |
| dbe2c299-096a-339f-b856-8efe2c06328e | -4.15933 | -43.68007 | 2025-11-21 03:51:00 | NPP-375D | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 6.8 |
| c9e07872-fe47-39f0-a1bf-e273479879cb | -6.31503 | -43.81387 | 2025-11-21 03:51:00 | NPP-375D | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |


[Clique aqui para ver as próximas entradas](README4.md)
