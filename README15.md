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

## Dados Diários - Página 15

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| a8396a08-ca75-3046-9c18-b3ed5e4d8b60 | -6.56856 | -55.16751 | 2026-08-05 04:46:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| d5c275bb-bbc4-378c-bf82-0fff45263ab0 | -7.7455 | -45.04798 | 2026-08-05 04:46:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 8.3 |
| ddf05ce9-b1c3-3944-97ec-8b0e316948a3 | -4.74453 | -48.83459 | 2026-08-05 04:46:00 | NOAA-21 | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| aa74080f-c3fa-39ee-b138-354be9c8e45b | -11.52407 | -43.24741 | 2026-08-05 04:46:00 | NOAA-21 | MORPARÁ | BAHIA | Brasil | 2921609 | 29 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 0ee7bdde-3adc-3f6d-92a5-1a90b8a23f48 | -10.46181 | -50.22577 | 2026-08-05 04:46:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 2ed40361-5e70-36fc-9828-149c3c0692f2 | -7.45199 | -44.89573 | 2026-08-05 04:46:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 5636bf51-4384-314d-bfec-6d1f3b894514 | -6.52844 | -55.15171 | 2026-08-05 04:46:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 04feb692-8cc8-3cfc-b51d-6cc546faf299 | -6.93075 | -41.92855 | 2026-08-05 04:46:00 | NOAA-21 | SÃO JOÃO DA VARJOTA | PIAUÍ | Brasil | 2209955 | 22 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 3591f1a3-1576-373f-8b9b-cf273b853dcb | -10.85484 | -50.33464 | 2026-08-05 04:46:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e46363c4-8c5b-3970-9701-9729e1ef36a3 | -8.35279 | -45.98482 | 2026-08-05 04:46:00 | NOAA-21 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 85378e44-05b4-344e-99f9-7f15dc1bfb29 | -6.55494 | -55.15585 | 2026-08-05 04:46:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 7621b85e-b687-3676-a17e-456cbe35986d | -6.72113 | -58.94991 | 2026-08-05 04:46:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.3 |
| af8cf1a6-109f-326b-82ce-cf81839bb85e | -6.57158 | -55.17278 | 2026-08-05 04:46:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b76dbdbf-d555-383c-a794-23d274468dbc | -7.18399 | -40.17333 | 2026-08-05 04:46:00 | NOAA-21 | ARARIPE | CEARÁ | Brasil | 2301307 | 23 | 33 | nan | nan | nan | Caatinga | 23.7 |
| 80df8a6e-fe3a-3c07-b6a2-b75bf67ebe20 | -10.45841 | -50.22524 | 2026-08-05 04:46:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| c2390bbb-54c3-3abc-9b17-40fbbdcf6383 | -3.29498 | -52.72547 | 2026-08-05 04:46:00 | NOAA-21 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 9a280013-b383-3ec7-b1cf-1bd47715b0e2 | -6.65361 | -56.4203 | 2026-08-05 04:46:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7cbad0aa-93a4-396c-8f37-bcb4a8633a24 | -10.60877 | -46.38119 | 2026-08-05 04:46:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f6078c2b-c0f0-39ab-9e47-88f7590466ca | -6.55418 | -55.16046 | 2026-08-05 04:46:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 7969abb1-d15f-3278-8238-1c12cec9a4b0 | -9.60512 | -47.76703 | 2026-08-05 04:46:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 8bb72276-2063-367e-b7e9-b37b7426086c | -6.33404 | -55.73499 | 2026-08-05 04:46:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 98954169-7dce-37d5-8286-cce1dc597802 | -9.60822 | -47.77222 | 2026-08-05 04:46:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| aa120da3-3215-341e-bb5e-b6a45dff8183 | -7.22609 | -45.77354 | 2026-08-05 04:46:00 | NOAA-21 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 62607782-f7d9-3639-95d7-637d0687af33 | -11.1907 | -54.86487 | 2026-08-05 04:49:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 76fc25a2-5790-372f-b6d9-26507969ebfd | -11.18891 | -54.89761 | 2026-08-05 04:49:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| e75a68d0-f480-336c-b9bb-8437e1f31a16 | -13.24932 | -54.268 | 2026-08-05 04:49:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 89a0d807-58b9-3c95-8c11-a9fe9d2d18b3 | -11.16844 | -54.88994 | 2026-08-05 04:49:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 7146389c-c87b-327a-9a38-18396749a8ca | -11.18739 | -54.8849 | 2026-08-05 04:49:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 3d7e2339-8d81-38d6-b51a-9eb2d2aa64f2 | -11.32137 | -54.47409 | 2026-08-05 04:49:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8984b7ba-cfdc-330e-9c51-a56908de382b | -15.43963 | -41.37873 | 2026-08-05 04:49:00 | NOAA-21 | CÂNDIDO SALES | BAHIA | Brasil | 2906709 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 2d7a59dc-804c-39c1-b987-08657e0387ba | -12.58933 | -46.95201 | 2026-08-05 04:49:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 6.4 |
| c76aa7fe-2c21-3c62-aa4d-882c6e788649 | -14.18535 | -54.41293 | 2026-08-05 04:49:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| a622f8fc-2783-3276-8058-04fdc2930459 | -16.52364 | -47.74178 | 2026-08-05 04:49:00 | NOAA-21 | LUZIÂNIA | GOIÁS | Brasil | 5212501 | 52 | 33 | nan | nan | nan | Cerrado | 0.5 |
| aa85b44f-7748-3e96-ae43-7c3b6cb2c9df | -11.17482 | -54.8952 | 2026-08-05 04:49:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 026c3acb-9a65-39f5-91f4-d2ceba331c3e | -12.59404 | -46.91671 | 2026-08-05 04:49:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 59ba489a-841e-3b33-b2b0-62ac7621a6a4 | -12.59603 | -46.93354 | 2026-08-05 04:49:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 7.9 |
| be3f09a9-b771-3a5e-bc28-4396c55b99fa | -11.17062 | -54.89864 | 2026-08-05 04:49:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 6.7 |
| c427f60e-db0b-34de-8200-0a64ed4b283f | -11.19881 | -54.90345 | 2026-08-05 04:49:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| f2067739-959a-3232-b65d-dca78bb92998 | -11.16792 | -54.91487 | 2026-08-05 04:49:00 | NOAA-21 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 8cafc570-334b-330e-8e6e-c121c4939977 | -12.93125 | -49.48441 | 2026-08-05 04:49:00 | NOAA-21 | ARAGUAÇU | TOCANTINS | Brasil | 1702000 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 26672501-e42d-3da4-a8c8-8848cf768407 | -11.18843 | -54.92247 | 2026-08-05 04:49:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 5.4 |
| ef42bb0b-a0eb-3ada-8e29-cf74f8217898 | -12.59765 | -46.92144 | 2026-08-05 04:49:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| aa41f9b7-e651-3604-bb83-41e52ae648e9 | -12.5955 | -46.9375 | 2026-08-05 04:49:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 90c50cda-1406-3f0d-92d0-50f4474f3e79 | -12.14333 | -48.26745 | 2026-08-05 04:49:00 | NOAA-21 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 71091159-6999-3e9e-a938-af34a8f0550a | -12.14392 | -48.26055 | 2026-08-05 04:49:00 | NOAA-21 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| de0b714d-4ff7-34d1-8913-4cd487d3d791 | -11.1852 | -54.87626 | 2026-08-05 04:49:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| fafa869b-c831-3b58-bd0c-374b80129c33 | -11.17986 | -54.90851 | 2026-08-05 04:49:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 4.4 |
| e13434c8-7197-3512-933f-83f981d30579 | -11.2193 | -54.91111 | 2026-08-05 04:49:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 7641665f-0276-3bca-8dbd-85fdd5029661 | -11.21005 | -54.9012 | 2026-08-05 04:49:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 6837c623-0556-33c1-ad96-4513021dd468 | -12.59966 | -46.93804 | 2026-08-05 04:49:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 32130a7c-6669-381d-89bc-61e07395e621 | -11.20939 | -54.90522 | 2026-08-05 04:49:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 9e74cdbb-d7f8-3e81-8700-316ed3682347 | -12.58724 | -46.93599 | 2026-08-05 04:49:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 9ae981d3-d5cc-3808-9da6-0f5496c160f3 | -13.68762 | -51.98497 | 2026-08-05 04:49:00 | NOAA-21 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 4311ee16-0d12-3b14-a27e-792f4a8dbea0 | -12.58155 | -46.94701 | 2026-08-05 04:49:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 54c1697f-2160-3018-834f-2d610e87fd8a | -17.33787 | -42.63623 | 2026-08-05 04:49:00 | NOAA-21 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 13.6 |
| cf13d6c0-30d5-3511-ad23-d3ced99b7b50 | -14.1792 | -54.40806 | 2026-08-05 04:49:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 6a500f40-0f57-3d41-ba13-804b2f46549d | -12.59246 | -46.92859 | 2026-08-05 04:49:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 8ca2c397-7161-379c-9e40-9e10572b176d | -11.18586 | -54.87225 | 2026-08-05 04:49:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ba11e5f9-0ffc-39a5-a28c-616c822c4b9d | -11.21225 | -54.90987 | 2026-08-05 04:49:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| c5b9b3c3-cabc-36c7-8b97-9fb274d80f8e | -13.25331 | -54.26487 | 2026-08-05 04:49:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| fb5f886d-2f82-3165-a830-f6f063afa17a | -11.21995 | -54.90708 | 2026-08-05 04:49:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 5.2 |
| c0c9b983-304c-3198-ad8c-7f2756bd0457 | -12.58518 | -46.95148 | 2026-08-05 04:49:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 26dea32f-8bb3-3168-b995-0aa5f9aa87c0 | -11.203 | -54.89999 | 2026-08-05 04:49:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| c57cf5ce-0b4a-39cf-a5c6-71ed58a7e8b4 | -12.59352 | -46.9206 | 2026-08-05 04:49:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 5.3 |
| b8bc924f-c520-3c2a-8cff-3068ca136679 | -17.33633 | -42.63691 | 2026-08-05 04:49:00 | NOAA-21 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 16.9 |
| 1505171d-ce68-3339-bc2f-c4516ee22140 | -12.16994 | -59.75611 | 2026-08-05 04:49:00 | NOAA-21 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 440092e7-147b-3594-a6b9-ffa87bd6f9df | -11.17834 | -54.8958 | 2026-08-05 04:49:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 1e8b630e-1453-30f0-86a8-7c4237209377 | -11.18976 | -54.91436 | 2026-08-05 04:49:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 5.0 |
| a4d5eb39-1bcc-3f60-84b1-d0a4e4b81bff | -11.18958 | -54.89357 | 2026-08-05 04:49:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 9de27d4c-0aec-3b68-8295-3daac862574f | -11.18718 | -54.86428 | 2026-08-05 04:49:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 02320d16-d63a-30b2-a951-6687c05796e8 | -11.91391 | -55.9102 | 2026-08-05 04:49:00 | NOAA-21 | IPIRANGA DO NORTE | MATO GROSSO | Brasil | 5104526 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 67725c99-9205-3c01-ba45-c395cd997dd5 | -13.43692 | -43.85593 | 2026-08-05 04:49:00 | NOAA-21 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 6184277c-55d4-3fc8-a399-b850c0e57f19 | -11.21071 | -54.8972 | 2026-08-05 04:49:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 38defb79-53a2-359c-b401-d5712ac375f9 | -11.1984 | -54.86204 | 2026-08-05 04:49:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| bacf0516-165b-3d3b-b939-2ebca34d7615 | -12.59711 | -46.92548 | 2026-08-05 04:49:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| d7b077bd-0ac8-37b4-b996-5c9756e182a3 | -11.16575 | -54.90617 | 2026-08-05 04:49:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 10.7 |
| 2cc2dac0-184b-3d97-8da8-a73d5a800789 | -11.17397 | -54.87845 | 2026-08-05 04:49:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 02fa9a6a-40f7-3e22-96ad-ec5ff76a3640 | -14.35559 | -47.51746 | 2026-08-05 04:49:00 | NOAA-21 | ALTO PARAÍSO DE GOIÁS | GOIÁS | Brasil | 5200605 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| a66dc985-9470-3a36-8af8-4497a9528674 | -11.92491 | -55.91219 | 2026-08-05 04:49:00 | NOAA-21 | IPIRANGA DO NORTE | MATO GROSSO | Brasil | 5104526 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 9c9a5a46-4235-3c8a-9d4c-24dec8e3ff86 | -17.34264 | -42.63329 | 2026-08-05 04:49:00 | NOAA-21 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 3.0 |
| fde17200-e79d-3304-8e04-2b2d3a724027 | -14.37495 | -53.38161 | 2026-08-05 04:49:00 | NOAA-21 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 0a7d5779-a1e2-3291-a70e-bf5d9765f132 | -11.17566 | -54.91198 | 2026-08-05 04:49:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| eb7a9015-dbaa-3cb8-a88a-0e4cc0179166 | -14.19462 | -54.44119 | 2026-08-05 04:49:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 7137189b-2011-3ef8-9c28-e32f7a03d5a2 | -17.98261 | -47.16122 | 2026-08-05 04:49:00 | NOAA-21 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 5ed15209-d8c5-33bf-939f-9df281fcf036 | -17.33675 | -42.63261 | 2026-08-05 04:49:00 | NOAA-21 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 16.9 |
| a2ddc9c7-9f56-3107-97ba-b71a1ca6bd83 | -11.1911 | -54.90628 | 2026-08-05 04:49:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 4.1 |
| ddc3aad2-ac0f-316d-a03c-ce69deb42763 | -11.22303 | -54.86619 | 2026-08-05 04:49:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e852eb3b-f9a7-3e44-86c8-a441b294ca73 | -12.32132 | -53.18121 | 2026-08-05 04:49:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 5938fe62-f6a1-3db8-bb8c-fcfb02b0c343 | -14.17583 | -54.40747 | 2026-08-05 04:49:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 71a5eb34-0d99-3aba-9ae7-05b16807aec4 | -14.14764 | -47.06898 | 2026-08-05 04:49:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 818ba2c7-6656-3564-926b-4cc26ad439d8 | -11.19243 | -54.89822 | 2026-08-05 04:49:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 1e9753ee-9517-3d37-83e9-36ca8d80c307 | -12.59456 | -46.91283 | 2026-08-05 04:49:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 5d9b165e-be85-3a81-a128-19a4515fac8e | -11.18557 | -54.91782 | 2026-08-05 04:49:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 0965b5e0-e1e1-3e2f-9aff-fa2ef6485f52 | -12.32819 | -48.54121 | 2026-08-05 04:49:00 | NOAA-21 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 6.7 |
| eb72ebcf-3dba-30ee-acdd-135065d2ee88 | -12.59086 | -46.94061 | 2026-08-05 04:49:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 1616ef0c-a40f-393d-9e1b-0d8a39d24d91 | -11.19748 | -54.91153 | 2026-08-05 04:49:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| ea649369-a73a-3bd8-81e2-6527f8f6c040 | -13.43768 | -43.84965 | 2026-08-05 04:49:00 | NOAA-21 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 878962d9-6345-39c5-a7f2-1170d967aac7 | -14.19365 | -54.42588 | 2026-08-05 04:49:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 30.6 |
| c075a9a4-2c32-3d99-bc73-04795e06595a | -11.23805 | -54.03948 | 2026-08-05 04:49:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3c867a72-e343-39c7-8fe0-fefc0af08aae | -11.1775 | -54.87904 | 2026-08-05 04:49:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |


[Clique aqui para ver as próximas entradas](README16.md)
