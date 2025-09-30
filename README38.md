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

## Dados Diários - Página 38

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 1e6065b7-4eaf-320a-8dcd-59d063a88786 | -13.21842 | -47.31332 | 2025-09-30 03:49:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 6.5 |
| c75595ff-941f-3314-857e-144e1ee2824f | -6.25542 | -43.66063 | 2025-09-30 03:49:00 | NOAA-20 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| c7e92edb-bdf2-3200-876a-ac23dc9eb40e | -15.92597 | -46.2146 | 2025-09-30 03:49:00 | NOAA-20 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 9.6 |
| 61cb4a03-af51-34bc-8a46-7102120640b0 | -6.15608 | -43.90476 | 2025-09-30 03:49:00 | NOAA-20 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 5.7 |
| da87a617-84bc-3bc3-acb4-99a1611c4887 | -13.34085 | -47.81743 | 2025-09-30 03:49:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a8d3c571-dd3e-3643-989e-8263d36dac85 | -6.45733 | -44.00174 | 2025-09-30 03:49:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 8.6 |
| db93043c-f37a-3ea3-bb72-14c4fd0b707c | -6.83768 | -44.83638 | 2025-09-30 03:49:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 13dee95f-5d79-3b8e-8d4e-171a5d84f682 | -6.50164 | -44.2643 | 2025-09-30 03:49:00 | NOAA-20 | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 19.9 |
| 3984ae23-6c55-3df5-ad4f-dd3747d43bea | -12.86377 | -46.90842 | 2025-09-30 03:49:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| f7724fdc-0f93-3c3a-a2ce-2e665dfcc256 | -12.23224 | -47.80058 | 2025-09-30 03:49:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 65d0b6d7-cdce-3301-9222-2876206d4d23 | -17.88708 | -44.31557 | 2025-09-30 03:49:00 | NOAA-20 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 1ba8ba28-804a-31d8-8175-9132719fae10 | -14.61315 | -48.29814 | 2025-09-30 03:49:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 0a6e258e-3438-38d3-8c3a-68ad81ee3a75 | -19.50593 | -41.70572 | 2025-09-30 03:49:00 | NOAA-20 | INHAPIM | MINAS GERAIS | Brasil | 3130903 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 5a938222-fc39-3b50-9a73-1a7be785c33b | -13.41849 | -48.19876 | 2025-09-30 03:49:00 | NOAA-20 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| b6bf2e02-3921-3ac3-8ccb-65d9e0903206 | -13.79908 | -47.97455 | 2025-09-30 03:49:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| b16fd7f3-3503-35c2-9602-20fb4142121c | -11.78553 | -47.60685 | 2025-09-30 03:49:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f892b152-12d9-3860-bbee-3196cc474455 | -14.53268 | -48.24194 | 2025-09-30 03:49:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 6d7132c6-d83f-30fb-b183-76902c408de4 | -16.24267 | -44.05643 | 2025-09-30 03:49:00 | NOAA-20 | MIRABELA | MINAS GERAIS | Brasil | 3142007 | 31 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 5d1d45f0-b767-34b3-854a-95fa32297294 | -17.17024 | -42.83374 | 2025-09-30 03:49:00 | NOAA-20 | TURMALINA | MINAS GERAIS | Brasil | 3169703 | 31 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 0d8d1043-b20a-3265-9e60-e52a199410d1 | -7.11342 | -45.55061 | 2025-09-30 03:49:00 | NOAA-20 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| af783e74-d5ff-3ccc-b89e-7a1cbee32f81 | -13.80512 | -47.88744 | 2025-09-30 03:49:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 8d833c60-b392-3c33-b8fb-161a8474d166 | -15.05516 | -46.96832 | 2025-09-30 03:49:00 | NOAA-20 | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 651f2507-8b17-3925-a18e-d89d7e922bfd | -7.01299 | -44.46489 | 2025-09-30 03:49:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 844ac27a-7042-3f87-a6b5-29a4ff64e303 | -6.24707 | -43.65402 | 2025-09-30 03:49:00 | NOAA-20 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 5e1a8f5b-dec1-3d39-988b-0676eaef44be | -13.06871 | -47.07956 | 2025-09-30 03:49:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 441698d9-8dfa-3f06-961b-ff7b1f467e9c | -6.86294 | -45.62541 | 2025-09-30 03:49:00 | NOAA-20 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 8eaa1d40-e2c9-3b8c-bafe-99b978e4ff8a | -14.72073 | -45.21208 | 2025-09-30 03:49:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 2e93ef26-3bdb-32fe-9897-fc6b0ce39bce | -12.94465 | -46.7619 | 2025-09-30 03:49:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 68e3768b-386f-3f66-b451-3282bfdaad31 | -19.30433 | -43.81404 | 2025-09-30 03:49:00 | NOAA-20 | BALDIM | MINAS GERAIS | Brasil | 3105004 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| e56afd5d-4d53-36a0-89c6-2b174f132820 | -16.39195 | -47.03553 | 2025-09-30 03:49:00 | NOAA-20 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 158d7d1b-49d8-3c81-91e8-839e909e50a5 | -15.26918 | -47.88751 | 2025-09-30 03:49:00 | NOAA-20 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 5be5a009-b95f-3c89-9808-b3cc108518eb | -14.56328 | -48.23881 | 2025-09-30 03:49:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 121ba370-a3a0-3adb-a795-e97829332e63 | -17.91094 | -42.18008 | 2025-09-30 03:49:00 | NOAA-20 | MALACACHETA | MINAS GERAIS | Brasil | 3139201 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| fe720653-397f-35d8-a7bb-f3cb128c50e3 | -19.30806 | -43.81662 | 2025-09-30 03:49:00 | NOAA-20 | BALDIM | MINAS GERAIS | Brasil | 3105004 | 31 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 4fe56758-7fd3-374b-b33d-2fb42d9593cb | -18.11897 | -42.19498 | 2025-09-30 03:49:00 | NOAA-20 | ÁGUA BOA | MINAS GERAIS | Brasil | 3100609 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| 75933253-e1d4-3874-bba7-70f1967d048f | -6.32256 | -44.13253 | 2025-09-30 03:49:00 | NOAA-20 | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| df649de5-e7c8-3594-9d2e-718721e3b4ac | -13.80906 | -47.89564 | 2025-09-30 03:49:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 4b3741b4-7d6f-311f-834b-683044cc7e1a | -6.49722 | -44.26236 | 2025-09-30 03:49:00 | NOAA-20 | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| ed981f60-bfdd-3520-8b35-38c6efe0098e | -6.55733 | -43.41356 | 2025-09-30 03:49:00 | NOAA-20 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Caatinga | 4.3 |
| ac14653e-cbda-3bd0-af4e-b65b0b10a540 | -16.84371 | -48.90392 | 2025-09-30 03:49:00 | NOAA-20 | BELA VISTA DE GOIÁS | GOIÁS | Brasil | 5203302 | 52 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 6f919bf3-31f6-3807-8abf-d4cb719d3949 | -6.2517 | -43.65461 | 2025-09-30 03:49:00 | NOAA-20 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 2762bf2b-ba72-3154-b38c-a5f2ad4050b2 | -15.48716 | -48.55288 | 2025-09-30 03:49:00 | NOAA-20 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 93515684-ee0b-382a-b23b-b669bfeeb56c | -15.29206 | -46.40989 | 2025-09-30 03:49:00 | NOAA-20 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 7b24e2e3-cce7-37e4-964e-cc074753b563 | -15.49112 | -48.56104 | 2025-09-30 03:49:00 | NOAA-20 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| c639a56e-9a7e-3146-a1f1-64396a233e27 | -14.58986 | -48.19044 | 2025-09-30 03:49:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 31a0feb9-1c4f-3433-8536-47f0ad576a99 | -11.75704 | -44.75294 | 2025-09-30 03:49:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 4f013bf4-b664-3f9e-8802-00e1a3f04e64 | -18.53274 | -46.04564 | 2025-09-30 03:49:00 | NOAA-20 | VARJÃO DE MINAS | MINAS GERAIS | Brasil | 3170750 | 31 | 33 | nan | nan | nan | Cerrado | 10.1 |
| c5bc22c0-a99a-3a92-a0f1-80284853bffe | -13.72625 | -48.65134 | 2025-09-30 03:49:00 | NOAA-20 | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 9f26ddd5-9aa3-3f01-b571-d94530e97ece | -13.21767 | -50.93829 | 2025-09-30 03:49:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 51389790-abd1-3874-8c00-830b8c223531 | -14.58702 | -48.28816 | 2025-09-30 03:49:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e1c93b87-89bb-3024-8b7c-f0b3b3b7c585 | -11.0718 | -47.82267 | 2025-09-30 03:49:00 | NOAA-20 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 5c9f5b03-0b12-3418-88f1-be70938e2556 | -14.57273 | -43.72567 | 2025-09-30 03:49:00 | NOAA-20 | MALHADA | BAHIA | Brasil | 2920205 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 6eee9887-4b76-3155-9e4f-a9547ee47a83 | -14.70389 | -48.16231 | 2025-09-30 03:49:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 4.5 |
| a269a1d5-ffe0-3a88-9fb1-cd0f2ddfe3b1 | -6.69078 | -42.79828 | 2025-09-30 03:49:00 | NOAA-20 | FRANCISCO AYRES | PIAUÍ | Brasil | 2204105 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 0f639bde-7bbd-3232-a137-849662366610 | -13.38818 | -48.06583 | 2025-09-30 03:49:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 0c61ae3d-8570-31c7-af28-e325f24fa399 | -11.21936 | -47.20424 | 2025-09-30 03:49:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 12.9 |
| c5081fe3-5929-3cb0-bc44-e2ad415232fb | -18.02044 | -44.37551 | 2025-09-30 03:49:00 | NOAA-20 | BUENÓPOLIS | MINAS GERAIS | Brasil | 3109204 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| f0b57d7c-36c9-3307-ba2b-3d996b349102 | -7.012 | -44.47071 | 2025-09-30 03:49:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| c1bc5b05-3a7e-33e9-bfb2-a1e0c2728137 | -14.50286 | -46.19502 | 2025-09-30 03:49:00 | NOAA-20 | DAMIANÓPOLIS | GOIÁS | Brasil | 5206701 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 3ed50dbd-0564-3160-8946-2e84e0b323e3 | -11.06225 | -47.82354 | 2025-09-30 03:49:00 | NOAA-20 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 90c8cdda-0512-387b-865e-53359c907d9e | -14.70607 | -48.23474 | 2025-09-30 03:49:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 213c2205-fb88-33ef-b57a-ad5f654229e2 | -14.70988 | -48.16023 | 2025-09-30 03:49:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| b72a9a07-3c99-3def-b072-e9981b8ebe50 | -13.21657 | -50.93888 | 2025-09-30 03:49:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 9.7 |
| 01e5e158-c429-309e-a9aa-8917e41a92c2 | -13.21588 | -47.32622 | 2025-09-30 03:49:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 80952cba-5e05-3876-a4e4-71e7466c47c3 | -15.71835 | -47.59425 | 2025-09-30 03:49:00 | NOAA-20 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 13.9 |
| 781979b1-ddc6-3c37-bb5f-0180987648e3 | -14.03258 | -47.8334 | 2025-09-30 03:49:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 92624b72-84c3-3776-a6e4-7f8536b7c831 | -12.83589 | -46.99677 | 2025-09-30 03:49:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| d128475d-2890-386b-bd32-fd0e6a88b84d | -5.82739 | -43.8722 | 2025-09-30 03:49:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 3eb998db-ad8d-32e5-b5d4-dff111bea06a | -6.05615 | -42.45205 | 2025-09-30 03:49:00 | NOAA-20 | HUGO NAPOLEÃO | PIAUÍ | Brasil | 2204600 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 43e6fd71-cf5f-3055-8a3e-0caa8e448e7c | -6.20128 | -44.21087 | 2025-09-30 03:49:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 6efe7964-c44a-3242-a115-88ac4e823528 | -13.79995 | -47.88545 | 2025-09-30 03:49:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 0324da6c-b0e8-3c8b-9860-1bf41f8aaa84 | -14.71876 | -45.67025 | 2025-09-30 03:49:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 9324015d-d34a-32cc-b73f-c60002e68616 | -14.50546 | -48.46704 | 2025-09-30 03:49:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 7e2631d2-c658-3b4a-be39-d5538eb005bd | -14.56399 | -48.45919 | 2025-09-30 03:49:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 74880ddf-bc4c-3de4-9bec-7edc2ff5ea39 | -13.8097 | -47.89235 | 2025-09-30 03:49:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| a7f20e1b-76c1-3955-ab48-72b79a45cf9c | -12.77531 | -46.85926 | 2025-09-30 03:49:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 548d1905-a566-3f9d-b819-da33270c05ac | -15.4621 | -47.9273 | 2025-09-30 03:49:00 | NOAA-20 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ba590cdd-a2d8-362a-a42c-5b7cbbbb56d1 | -6.81673 | -48.71088 | 2025-09-30 03:49:00 | NOAA-20 | ARAGOMINAS | TOCANTINS | Brasil | 1701309 | 17 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 7c55d805-9067-3407-b549-8bea6ec4c8e3 | -12.87873 | -44.68774 | 2025-09-30 03:49:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 8e789b0a-8caf-3dbc-9517-da7bb6d90660 | -12.7514 | -46.87339 | 2025-09-30 03:49:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 23cb1942-dd75-3c43-ace8-a69de2613686 | -13.59813 | -48.04417 | 2025-09-30 03:49:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| fd328ead-5b3b-303a-939e-5e645849e234 | -14.59302 | -48.28633 | 2025-09-30 03:49:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 7e8b130f-7e9c-3b1a-91da-3e39786cb2b2 | -6.36828 | -45.64664 | 2025-09-30 03:49:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 4c0f34df-602e-336a-9c89-16f0cf376f2e | -7.42336 | -45.19223 | 2025-09-30 03:49:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 46d03921-bc07-3e62-8640-77ded01294e7 | -11.94507 | -43.91604 | 2025-09-30 03:49:00 | NOAA-20 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| b545cda8-5d5e-3662-acf4-9995a0fc012f | -13.83153 | -47.47782 | 2025-09-30 03:49:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 17ada9a1-2d63-3cf4-927d-417c1f0bf959 | -5.82433 | -42.79313 | 2025-09-30 03:49:00 | NOAA-20 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 2d03b4e3-905d-3439-a662-0d25e34e2224 | -15.84867 | -46.24305 | 2025-09-30 03:49:00 | NOAA-20 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 4d348909-e093-3211-8878-2aeee53ad1b4 | -6.49154 | -44.2669 | 2025-09-30 03:49:00 | NOAA-20 | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| c3efbd02-b101-3b47-bb97-dbb27aedb371 | -14.56187 | -48.46975 | 2025-09-30 03:49:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 19851ec0-a07f-31d6-85d3-c5b428d568b7 | -7.0441 | -45.18115 | 2025-09-30 03:49:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 4658742c-17d5-3181-9dc8-4d8e53bfa95e | -12.8405 | -46.99 | 2025-09-30 03:49:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 8d1a3d21-f3ad-312e-aa6d-ea9b2a0c5297 | -6.42987 | -43.08213 | 2025-09-30 03:49:00 | NOAA-20 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 6af781b6-08c6-3892-9ac2-885c3f3192a7 | -12.84227 | -46.99136 | 2025-09-30 03:49:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 57f02f76-03ba-3617-86ae-12347e36259a | -13.23662 | -43.37888 | 2025-09-30 03:49:00 | NOAA-20 | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Caatinga | 4.5 |
| a2465fa1-f2a4-36ae-83b1-5307b6eb2427 | -7.11801 | -45.55477 | 2025-09-30 03:49:00 | NOAA-20 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d7ecdac8-cedd-36b1-8c86-bbeeef95af30 | -7.56434 | -42.40516 | 2025-09-30 03:49:00 | NOAA-20 | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 403d6318-d2b8-3bfb-86d9-50510e722836 | -14.57885 | -48.21729 | 2025-09-30 03:49:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| c7a56916-d1ca-3c98-8bda-c849aad2d045 | -6.72686 | -39.11628 | 2025-09-30 03:49:00 | NOAA-20 | LAVRAS DA MANGABEIRA | CEARÁ | Brasil | 2307502 | 23 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 9bb61ed4-6560-37eb-a00c-90b43de8311b | -12.88593 | -44.69821 | 2025-09-30 03:49:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |


[Clique aqui para ver as próximas entradas](README39.md)
