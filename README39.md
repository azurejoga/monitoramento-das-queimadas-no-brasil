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

## Dados Diários - Página 39

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 4264d1a8-c09f-33c0-892d-8c80b6a15b09 | -13.52109 | -48.11364 | 2025-10-10 04:53:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 11000eee-3f39-3959-819f-45145c1c84b9 | -12.03175 | -62.94569 | 2025-10-10 04:53:00 | NOAA-21 | SÃO MIGUEL DO GUAPORÉ | RONDÔNIA | Brasil | 1100320 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e6bc304f-5aef-3f93-9a25-0d30547c894a | -14.42174 | -48.3399 | 2025-10-10 04:53:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 64c4c296-cb59-314f-95ae-58cb8d08e718 | -18.07534 | -44.4747 | 2025-10-10 04:53:00 | NOAA-21 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c28a4bcb-0f72-38ed-a71e-f6ce6217cd97 | -15.09288 | -46.59973 | 2025-10-10 04:53:00 | NOAA-21 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 6.1 |
| e2690077-7d02-31d0-89ce-42458b52e9eb | -14.83745 | -48.45731 | 2025-10-10 04:53:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 3a14a6c9-de20-31f5-9c3d-79fd5b910ba6 | -13.05015 | -47.93543 | 2025-10-10 04:53:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 6f3425fa-1ebd-3d73-bc01-7e75f07d982b | -13.41366 | -47.63297 | 2025-10-10 04:53:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| b2612e2e-0ddb-309f-967d-60f9ff791f9e | -13.27262 | -48.03113 | 2025-10-10 04:53:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 19383487-dbb3-3a11-815f-7cf865074766 | -14.9297 | -46.78539 | 2025-10-10 04:53:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 3a34d37d-0282-30fb-be7a-d75b266f08ff | -15.4286 | -47.98893 | 2025-10-10 04:53:00 | NOAA-21 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 9.2 |
| fdbb7199-7b4e-3ffd-ba34-2f8577634950 | -15.91342 | -43.29549 | 2025-10-10 04:53:00 | NOAA-21 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 0e3953ab-e66e-34ff-a1ae-44c2876d360d | -17.71474 | -56.78368 | 2025-10-10 04:53:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.9 |
| 926067d4-d8c4-3aca-828a-60be75fa7c63 | -18.77872 | -44.62157 | 2025-10-10 04:53:00 | NOAA-21 | CURVELO | MINAS GERAIS | Brasil | 3120904 | 31 | 33 | nan | nan | nan | Cerrado | 7.8 |
| a5436995-8537-3c04-8df7-58bb8ce4b54c | -18.77842 | -44.62273 | 2025-10-10 04:53:00 | NOAA-21 | CURVELO | MINAS GERAIS | Brasil | 3120904 | 31 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 950b40c9-c3be-3505-b8e5-23d15fa25bb2 | -17.85185 | -57.65294 | 2025-10-10 04:53:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.5 |
| a4238a1f-b90e-3584-8564-7be6c4971bed | -17.84118 | -57.58989 | 2025-10-10 04:53:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.8 |
| 8a4741e6-ca33-3ccc-b211-0b0904dbd5ac | -13.32768 | -47.74011 | 2025-10-10 04:53:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e234fc23-fdaf-3562-8514-5aa173376dd6 | -14.94654 | -46.76349 | 2025-10-10 04:53:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 27249261-2ec8-3d5c-80b6-ad65b7009442 | -14.37855 | -46.00527 | 2025-10-10 04:53:00 | NOAA-21 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 696659ea-3bac-3062-a4d8-e0031e866549 | -13.26754 | -48.01994 | 2025-10-10 04:53:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 2c1e54c4-6557-3b9b-8318-1fef57a418e6 | -14.43217 | -48.00604 | 2025-10-10 04:53:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| d816ace6-cc14-39c1-88e2-ea54b04ab5f0 | -15.23066 | -46.3813 | 2025-10-10 04:53:00 | NOAA-21 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 2.9 |
| ae2ab851-10ac-3236-b33e-7f0080599747 | -17.89155 | -57.50157 | 2025-10-10 04:53:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.1 |
| be3114bc-feef-346c-b399-b544fbf02ffc | -17.84185 | -57.58595 | 2025-10-10 04:53:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.8 |
| 7aa9a680-7eb1-35e9-a0be-7a550c58f206 | -14.93234 | -46.76434 | 2025-10-10 04:53:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 18.2 |
| 7b9a3aae-9322-31a3-92b6-772efcabc30f | -13.29784 | -47.12842 | 2025-10-10 04:53:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 5fd92480-275e-3ef8-8e8e-418d53eed11e | -13.84391 | -45.83544 | 2025-10-10 04:53:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| fd2bfba4-a186-36a8-b91c-7ec648690140 | -15.3831 | -47.29403 | 2025-10-10 04:53:00 | NOAA-21 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| d4e17746-6ae4-316e-8ccc-77c1591df273 | -12.09418 | -64.23174 | 2025-10-10 04:53:00 | NOAA-21 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ef5ce086-c331-373a-8a4e-03790c86943c | -14.27089 | -45.88756 | 2025-10-10 04:53:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 687817ec-d28b-3be9-9824-e3a4482e9ca8 | -11.72125 | -62.98211 | 2025-10-10 04:53:00 | NOAA-21 | SÃO MIGUEL DO GUAPORÉ | RONDÔNIA | Brasil | 1100320 | 11 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 824eeb32-bd9a-31a1-a648-39390683e07d | -14.26822 | -45.90931 | 2025-10-10 04:53:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 4.3 |
| e7a92d65-6153-3656-a669-25dc4fc49db4 | -15.42521 | -47.99147 | 2025-10-10 04:53:00 | NOAA-21 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 5d537a00-4a40-35d5-bbf2-760d0a9d7b17 | -17.90969 | -57.52011 | 2025-10-10 04:53:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 8.2 |
| d8cdf667-f799-3e14-b918-3087f5c20cc0 | -16.67956 | -47.59437 | 2025-10-10 04:53:00 | NOAA-21 | CRISTALINA | GOIÁS | Brasil | 5206206 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| d19bb213-116b-3c89-9027-bebd12ce9aab | -14.42998 | -47.98854 | 2025-10-10 04:53:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| b3709028-fc94-3190-ad98-7d7d556894eb | -17.90748 | -57.51215 | 2025-10-10 04:53:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 7.2 |
| e61ec932-cd8e-39f6-bbff-cf8c873fb6ff | -15.73302 | -47.78215 | 2025-10-10 04:53:00 | NOAA-21 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 99570692-44ca-3627-99d8-0ee7064e3b53 | -15.52517 | -47.9664 | 2025-10-10 04:53:00 | NOAA-21 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 55508dfa-b6c1-3232-b84e-f47a92e070dd | -17.9006 | -57.51093 | 2025-10-10 04:53:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.2 |
| 3ffbc424-9122-3b54-9124-0af19a5f4ecd | -13.23284 | -51.15562 | 2025-10-10 04:53:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 6263f143-5432-37e3-8370-d5c23e4b64af | -15.33299 | -43.191 | 2025-10-10 04:53:00 | NOAA-21 | PAI PEDRO | MINAS GERAIS | Brasil | 3146552 | 31 | 33 | nan | nan | nan | Caatinga | 5.7 |
| d37ac081-2465-379c-99f6-ac3d5cdf3593 | -16.27681 | -47.16779 | 2025-10-10 04:53:00 | NOAA-21 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 3.2 |
| ab680a03-2aa1-3db9-ac6a-6887b53a2e6e | -16.02128 | -59.52454 | 2025-10-10 04:53:00 | NOAA-21 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 62dce179-d6f8-3fb9-9cfa-21de1df96455 | -14.98708 | -47.20205 | 2025-10-10 04:53:00 | NOAA-21 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 976b7985-6933-35f0-8d6c-5cb84992abe6 | -15.42804 | -47.9935 | 2025-10-10 04:53:00 | NOAA-21 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 9.2 |
| a4c29df9-1c58-37ee-8469-40013fc688aa | -15.08446 | -46.58713 | 2025-10-10 04:53:00 | NOAA-21 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 3d640805-ed22-3169-86be-088ae593caf1 | -15.29907 | -46.14724 | 2025-10-10 04:53:00 | NOAA-21 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a0db5207-c6ad-3945-9096-9734f3b673a0 | -15.39503 | -47.29796 | 2025-10-10 04:53:00 | NOAA-21 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 8653e3d3-73a9-3edb-ac42-b9f511978bc2 | -13.84355 | -45.83836 | 2025-10-10 04:53:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| a9d99f0a-ea93-32b7-8c94-30a30790b1a6 | -13.82886 | -45.79061 | 2025-10-10 04:53:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| b57a83b4-191b-3431-93d1-e5f2e15f36f9 | -16.29833 | -47.14949 | 2025-10-10 04:53:00 | NOAA-21 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 90bb2425-89e5-3d19-a491-4c249bdc9ec2 | -15.40216 | -48.02972 | 2025-10-10 04:53:00 | NOAA-21 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 40bc07b4-2f28-3dfe-9784-b0dc4fc23bf3 | -13.37472 | -47.75749 | 2025-10-10 04:53:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ba2caa9a-1906-39e0-b550-a08e95134d3d | -13.84604 | -45.85973 | 2025-10-10 04:53:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 1c35d8d9-7667-3b7a-b606-2b67264efcab | -13.26936 | -48.02226 | 2025-10-10 04:53:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 5cb5e966-6e18-3f34-a824-7600e0d5a445 | -14.57368 | -47.45605 | 2025-10-10 04:53:00 | NOAA-21 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 2527477c-bd58-38ef-8c89-c158fce280f7 | -17.94844 | -45.031 | 2025-10-10 04:53:00 | NOAA-21 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| cc04dad3-c9cd-3a0a-9e7d-4dde548fdcf3 | -13.30797 | -47.99602 | 2025-10-10 04:53:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 8fa409aa-276c-3337-96a2-ccb4d4903f0e | -14.73083 | -48.36076 | 2025-10-10 04:53:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 3f5ac4ee-b3fd-3142-b99d-2deba2ee3bbf | -13.8249 | -45.78088 | 2025-10-10 04:53:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| f3a09659-c740-3582-a105-b9324922fa46 | -16.26728 | -47.16641 | 2025-10-10 04:53:00 | NOAA-21 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 134be0c0-8409-31c1-a0e6-8aa6d74f94f7 | -16.2971 | -47.16 | 2025-10-10 04:53:00 | NOAA-21 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| e4668f8d-671b-37f6-b2bf-1891664052fe | -14.89075 | -47.22878 | 2025-10-10 04:53:00 | NOAA-21 | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 4d9d8e0b-6787-3fe0-a550-a2b881f22427 | -17.6655 | -44.45464 | 2025-10-10 04:53:00 | NOAA-21 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| b1bde27b-9c9c-38c4-bcc2-29409a9836ed | -15.00829 | -46.28117 | 2025-10-10 04:53:00 | NOAA-21 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 77bb3398-2e07-3114-9aed-536d7ea3379c | -17.8248 | -57.62357 | 2025-10-10 04:53:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.3 |
| 079fd270-1eb5-31cf-b4ce-899a3f436e81 | -14.93777 | -46.76007 | 2025-10-10 04:53:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 1613f20a-a1fc-3233-a9a9-2b2d8f896da4 | -15.75191 | -48.9889 | 2025-10-10 04:53:00 | NOAA-21 | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| e0f589cc-6064-339b-8456-e38c6946c085 | -18.08873 | -44.69515 | 2025-10-10 04:53:00 | NOAA-21 | CORINTO | MINAS GERAIS | Brasil | 3119104 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 8fddc3ac-964d-3976-83e6-04c8b0dd2315 | -15.09221 | -46.60533 | 2025-10-10 04:53:00 | NOAA-21 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 6.1 |
| d2496d86-cfa3-3ef1-87af-29ada9267076 | -14.93107 | -46.77018 | 2025-10-10 04:53:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 5.8 |
| adb0e1ab-931d-34cf-b3ac-aa0eb6e63b05 | -17.88746 | -57.50486 | 2025-10-10 04:53:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 5.5 |
| d42bc3dc-2e7d-30a6-80e7-3293d146b5ee | -15.28872 | -46.14813 | 2025-10-10 04:53:00 | NOAA-21 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 79e3409a-24c8-36c0-ae9f-f0c255d898df | -17.82095 | -57.64627 | 2025-10-10 04:53:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.2 |
| 005c0bd0-8792-3b4c-bbc9-934e3184cb29 | -15.06744 | -46.60529 | 2025-10-10 04:53:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 0a18ab59-9d8c-39d7-9e57-351df5882538 | -15.31463 | -46.18595 | 2025-10-10 04:53:00 | NOAA-21 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 9f900a37-5da9-3bf3-a2d6-30b71fb649bd | -16.29638 | -47.08249 | 2025-10-10 04:53:00 | NOAA-21 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| bf906acf-26c7-37c8-a104-88a0f759a58f | -13.36026 | -47.62655 | 2025-10-10 04:53:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| adedb86f-1365-3416-bd1c-8c28d2c2cd1c | -15.73864 | -43.95008 | 2025-10-10 04:53:00 | NOAA-21 | VARZELÂNDIA | MINAS GERAIS | Brasil | 3170909 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 9d2c8187-492c-3992-ba97-3736129e0227 | -16.6848 | -47.59013 | 2025-10-10 04:53:00 | NOAA-21 | CRISTALINA | GOIÁS | Brasil | 5206206 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 677476a0-5136-3c01-b4c7-3fed8929bbf1 | -15.00448 | -47.55853 | 2025-10-10 04:53:00 | NOAA-21 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| c7f3a994-0661-34b9-afcd-87c89e1f70f5 | -14.95009 | -46.77481 | 2025-10-10 04:53:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 8bf80a4c-d6ab-3f72-8478-1329c9624e6f | -16.00416 | -59.55307 | 2025-10-10 04:53:00 | NOAA-21 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 4.2 |
| c014eb4b-c5c1-3586-a523-c3a94ae97514 | -13.32207 | -47.98923 | 2025-10-10 04:53:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| d5676617-0a9f-3d41-95f7-75f24dbffb3c | -11.76357 | -61.06805 | 2025-10-10 04:53:00 | NOAA-21 | PIMENTA BUENO | RONDÔNIA | Brasil | 1100189 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 17d6ad37-6911-32ba-a621-eed84e67f5b6 | -13.52543 | -48.11399 | 2025-10-10 04:53:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d0c0cbec-5964-30e9-a2a1-2f4392f2d376 | -17.93788 | -45.02309 | 2025-10-10 04:53:00 | NOAA-21 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 11.5 |
| 260d914f-b8e0-3ed6-ae37-435bc412845a | -17.08784 | -45.49043 | 2025-10-10 04:53:00 | NOAA-21 | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| d6b1ff5a-0d65-3e5f-8d46-f614d15a8733 | -13.29675 | -47.13699 | 2025-10-10 04:53:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| bfa3c261-48f0-336b-be63-79f8fb9e89f9 | -17.08862 | -45.48338 | 2025-10-10 04:53:00 | NOAA-21 | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 32f31222-4947-31bc-8bd7-9691a7cc62d3 | -13.84567 | -45.86267 | 2025-10-10 04:53:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 94ac4afa-6061-306c-8ce7-75352bbffdd7 | -17.39329 | -46.87007 | 2025-10-10 04:53:00 | NOAA-21 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 8f3b8f68-95b3-346d-a417-42ba3a62386d | -15.56986 | -44.42432 | 2025-10-10 04:53:00 | NOAA-21 | JANUÁRIA | MINAS GERAIS | Brasil | 3135209 | 31 | 33 | nan | nan | nan | Caatinga | 1.4 |
| e58dec51-4db2-300a-8086-54c631c738da | -15.24075 | -46.38111 | 2025-10-10 04:53:00 | NOAA-21 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 2a351891-8c4a-3b76-a47e-79383c37c7e1 | -17.89844 | -57.50273 | 2025-10-10 04:53:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.0 |
| 0c930f4f-0c6d-34a6-8ae9-ef0a1d615314 | -17.83326 | -57.65755 | 2025-10-10 04:53:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 6.1 |
| 7e8c2133-0383-380f-a7fb-9e3ee614c2c1 | -13.31865 | -48.47603 | 2025-10-10 04:53:00 | NOAA-21 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 63f6c323-cc88-380f-8b78-53db6bf0c6d3 | -15.57509 | -44.42901 | 2025-10-10 04:53:00 | NOAA-21 | JANUÁRIA | MINAS GERAIS | Brasil | 3135209 | 31 | 33 | nan | nan | nan | Caatinga | 1.9 |


[Clique aqui para ver as próximas entradas](README40.md)
