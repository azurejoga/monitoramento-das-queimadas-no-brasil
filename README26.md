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

## Dados Diários - Página 26

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 19e84efd-4586-3f8e-9282-d1388bc5a377 | -14.52267 | -47.36676 | 2025-09-16 04:04:00 | NOAA-21 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 6dcd2166-70d6-38a9-86c6-2b643eed0fa9 | -16.58764 | -42.91104 | 2025-09-16 04:04:00 | NOAA-21 | GRÃO MOGOL | MINAS GERAIS | Brasil | 3127800 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b021a490-0197-3979-b67d-acd290fdd7c3 | -12.77776 | -47.9578 | 2025-09-16 04:04:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 2db7f484-ed3b-3a96-a80e-22f1b68b29f0 | -13.23508 | -40.94257 | 2025-09-16 04:04:00 | NOAA-21 | ITAETÉ | BAHIA | Brasil | 2915007 | 29 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 91297c19-2a09-3d19-89fb-56784066203f | -12.69475 | -47.73351 | 2025-09-16 04:04:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 0d3e012b-f437-3e8a-a608-8c1958dc42e1 | -12.93105 | -47.96186 | 2025-09-16 04:04:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 898c26c5-36ad-36f1-8626-624ffb66012f | -12.54952 | -45.63643 | 2025-09-16 04:04:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 5c392b1c-27fa-39fc-a604-6d2a9dcf5445 | -13.21044 | -47.30424 | 2025-09-16 04:04:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 8dfbdb55-9898-3a97-8cb2-aa8a9271c22c | -20.48737 | -42.25385 | 2025-09-16 04:04:00 | NOAA-21 | SANTA MARGARIDA | MINAS GERAIS | Brasil | 3157906 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 7a1aa712-c8f8-3024-8a4a-4d96cc5196ef | -14.30236 | -49.52608 | 2025-09-16 04:04:00 | NOAA-21 | SANTA TEREZINHA DE GOIÁS | GOIÁS | Brasil | 5219704 | 52 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 07e6ec87-9956-3113-94bd-2a51c3d0fc31 | -19.00809 | -49.92955 | 2025-09-16 04:04:00 | NOAA-21 | GURINHATÃ | MINAS GERAIS | Brasil | 3129103 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 5d6c758d-9325-3d8b-9af1-2592c94406e3 | -14.63905 | -46.38343 | 2025-09-16 04:04:00 | NOAA-21 | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 7e9af000-c25a-31e2-87ba-6fbfaee0045b | -12.97517 | -47.96664 | 2025-09-16 04:04:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 3dcc6fd7-6307-3297-9603-e3f7e2ef4f0b | -14.47657 | -46.35986 | 2025-09-16 04:04:00 | NOAA-21 | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 989cc603-f9c1-329c-921e-adedd35a483e | -16.65968 | -49.75635 | 2025-09-16 04:04:00 | NOAA-21 | PALMEIRAS DE GOIÁS | GOIÁS | Brasil | 5215702 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 8a20c708-ea9e-33df-829c-adf65e8fdb6c | -14.60654 | -46.38823 | 2025-09-16 04:04:00 | NOAA-21 | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| e3d3c207-f2a6-37af-9ce5-8aa527638fe5 | -16.58821 | -42.90746 | 2025-09-16 04:04:00 | NOAA-21 | GRÃO MOGOL | MINAS GERAIS | Brasil | 3127800 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 4f2a95f8-d378-3c10-b920-78058e83f7c9 | -18.58636 | -48.14347 | 2025-09-16 04:04:00 | NOAA-21 | ARAGUARI | MINAS GERAIS | Brasil | 3103504 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f85ba629-394f-33f3-8256-22bb2ca49c7a | -13.7646 | -48.75647 | 2025-09-16 04:04:00 | NOAA-21 | CAMPINORTE | GOIÁS | Brasil | 5204706 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 07dde6ea-5203-3ea5-9b84-54aeccbdf02a | -13.7585 | -48.76404 | 2025-09-16 04:04:00 | NOAA-21 | CAMPINORTE | GOIÁS | Brasil | 5204706 | 52 | 33 | nan | nan | nan | Cerrado | 8.6 |
| 02912dd8-2de7-32ac-9b71-72f0e4119c9f | -14.82265 | -51.66278 | 2025-09-16 04:04:00 | NOAA-21 | ARAGUAIANA | MATO GROSSO | Brasil | 5101001 | 51 | 33 | nan | nan | nan | Cerrado | 8.5 |
| dffece9d-c6ad-32fa-bd35-f2f2f94218ce | -20.09844 | -41.55365 | 2025-09-16 04:04:00 | NOAA-21 | LAJINHA | MINAS GERAIS | Brasil | 3137700 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 3a0c3205-51b7-3bdf-9767-3d52d3fbd0d6 | -14.1597 | -46.14213 | 2025-09-16 04:04:00 | NOAA-21 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 0cc84ec1-c184-39a9-9144-0c9a67f8b2a6 | -13.95313 | -44.92781 | 2025-09-16 04:04:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 2cff096a-5274-3bf1-9df7-d993dfc82f2e | -14.30039 | -49.53651 | 2025-09-16 04:04:00 | NOAA-21 | SANTA TEREZINHA DE GOIÁS | GOIÁS | Brasil | 5219704 | 52 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 22cd5e8d-2fc5-3327-8235-9144cbba02a7 | -16.68897 | -49.77519 | 2025-09-16 04:04:00 | NOAA-21 | PALMEIRAS DE GOIÁS | GOIÁS | Brasil | 5215702 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 03bea9fb-bdb6-32f2-8ce7-04226a8e24c1 | -17.07937 | -45.82578 | 2025-09-16 04:04:00 | NOAA-21 | BRASILÂNDIA DE MINAS | MINAS GERAIS | Brasil | 3108552 | 31 | 33 | nan | nan | nan | Cerrado | 5.4 |
| b34d66b1-47c1-3578-bd6e-0fcfddf42d22 | -12.62104 | -45.73944 | 2025-09-16 04:04:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 8.3 |
| a76949f7-1748-37b4-bf64-d9437fd129f7 | -12.61383 | -47.98445 | 2025-09-16 04:04:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 10.9 |
| e6a06783-10a5-39fa-9d90-8a319f58bb99 | -15.69495 | -47.01299 | 2025-09-16 04:04:00 | NOAA-21 | CABECEIRAS | GOIÁS | Brasil | 5204003 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 2e73d5dd-04cf-3967-b2ca-c65d21e234c8 | -14.51846 | -47.36913 | 2025-09-16 04:04:00 | NOAA-21 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a8ac1567-749c-3626-abeb-b3efab3b2e0b | -17.16315 | -49.37911 | 2025-09-16 04:04:00 | NOAA-21 | CROMÍNIA | GOIÁS | Brasil | 5206503 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| d5f7e07d-1d2b-3486-9d2d-28e18233f8ac | -16.67357 | -49.75835 | 2025-09-16 04:04:00 | NOAA-21 | PALMEIRAS DE GOIÁS | GOIÁS | Brasil | 5215702 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| efa8d42a-a69c-35ff-aded-fa0d22071c83 | -12.6378 | -48.00241 | 2025-09-16 04:04:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 3b97faee-ae63-3abf-9971-3a29726aaec8 | -14.51522 | -47.38751 | 2025-09-16 04:04:00 | NOAA-21 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 3eeaf817-6119-3b4c-9b83-23ab333b2566 | -17.94848 | -45.25196 | 2025-09-16 04:04:00 | NOAA-21 | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a0080784-89e7-3cb1-8bff-db33f57113dd | -14.97102 | -46.55965 | 2025-09-16 04:04:00 | NOAA-21 | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 58743a06-a15b-39b1-beef-537f56d6bc2e | -19.6218 | -43.90319 | 2025-09-16 04:04:00 | NOAA-21 | LAGOA SANTA | MINAS GERAIS | Brasil | 3137601 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 3fdbd271-5fd2-3ed7-b986-7153f85a5660 | -12.82052 | -47.22571 | 2025-09-16 04:04:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 7c1719d8-f53b-3e44-82d0-96b86a456ecf | -12.77889 | -47.92733 | 2025-09-16 04:04:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 8b6f9c8e-7ffe-36ba-83a3-ae7a3236c302 | -14.52677 | -47.36739 | 2025-09-16 04:04:00 | NOAA-21 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 80785216-44ba-3c4c-87ac-8610f58dd720 | -13.20202 | -47.30341 | 2025-09-16 04:04:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 5.4 |
| aa564c17-3eb8-3154-9a24-95b26ed1f342 | -15.72351 | -39.31957 | 2025-09-16 04:04:00 | NOAA-21 | CANAVIEIRAS | BAHIA | Brasil | 2906303 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 4219e495-9dca-3b2e-ad68-d3984257dd32 | -14.64845 | -42.71221 | 2025-09-16 04:04:00 | NOAA-21 | URANDI | BAHIA | Brasil | 2932606 | 29 | 33 | nan | nan | nan | Caatinga | 4.1 |
| 1ef238bb-4814-38ca-86e2-289ec2248fa8 | -13.9229 | -44.80181 | 2025-09-16 04:04:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 4.6 |
| c203d2a9-6327-305e-be88-feb618a2761d | -13.21603 | -47.29678 | 2025-09-16 04:04:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 1f4d6b41-6d80-38d6-ac25-34b595470305 | -13.91792 | -44.80954 | 2025-09-16 04:04:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| e86181bd-8b46-352e-a7b9-9789213d983e | -12.8392 | -47.21733 | 2025-09-16 04:04:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| beaddbc6-6748-306c-9e96-515c9244f43e | -15.61824 | -47.36662 | 2025-09-16 04:04:00 | NOAA-21 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 45e79087-0e44-3b90-9b62-7ceab3d42987 | -12.76823 | -47.96048 | 2025-09-16 04:04:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 390b6dfa-494e-315e-a114-2aa7d19c5ae7 | -12.76591 | -47.97296 | 2025-09-16 04:04:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 7ef4fcee-9938-3302-82d7-b0cdfde3abd4 | -12.8035 | -47.9405 | 2025-09-16 04:04:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| b2385460-1cfe-3b71-871f-6feda15efdf1 | -17.72668 | -46.77391 | 2025-09-16 04:04:00 | NOAA-21 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 414fa55c-170c-397d-87f1-8bf334e147f3 | -12.29218 | -46.40892 | 2025-09-16 04:04:00 | NOAA-21 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 8.2 |
| 6a6e5244-3d8d-3d5e-b929-4edcefbc5a1b | -11.91333 | -48.56175 | 2025-09-16 04:04:00 | NOAA-21 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 11.9 |
| a817cd2f-c185-368a-9214-914b7b4a24db | -14.42254 | -47.36329 | 2025-09-16 04:04:00 | NOAA-21 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 0c0188af-57f7-3195-ae31-bab70279cc94 | -16.70588 | -54.94492 | 2025-09-16 04:04:00 | NOAA-21 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 1710895a-637d-3863-971e-92f7a1021af3 | -12.67321 | -48.00794 | 2025-09-16 04:04:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 04dd626e-7ecb-3172-b2a0-aab1b259de18 | -12.97154 | -47.96182 | 2025-09-16 04:04:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 7.8 |
| f959dd52-4fc8-3fbf-b5db-8c9d2b7bcd78 | -12.70049 | -47.73851 | 2025-09-16 04:04:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 1568a2e8-5294-3ce7-b74a-c1d5b279b59f | -14.34601 | -47.09363 | 2025-09-16 04:04:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 50498c5a-2728-3461-bb34-b5e53e8fb056 | -12.62822 | -45.7655 | 2025-09-16 04:04:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 4.2 |
| b3b475d8-f03e-3b4e-ab76-297f19db72d2 | -17.39806 | -42.12274 | 2025-09-16 04:04:00 | NOAA-21 | NOVO CRUZEIRO | MINAS GERAIS | Brasil | 3145307 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 46d51ea5-415f-3cdc-8e86-c6c4aa71ca38 | -18.90382 | -49.57793 | 2025-09-16 04:04:00 | NOAA-21 | ITUIUTABA | MINAS GERAIS | Brasil | 3134202 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| adcea5a3-4ef1-3738-9260-15236f194bb2 | -12.74111 | -47.20393 | 2025-09-16 04:04:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 33fb011b-798d-3d0b-92e8-749e3f7a4510 | -14.8515 | -45.50842 | 2025-09-16 04:04:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 3a2eb43c-6467-323e-b838-0595212915eb | -16.47769 | -55.11429 | 2025-09-16 04:04:00 | NOAA-21 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 4.5 |
| da451b9e-05fe-3cee-8c1f-3588e3cdd5ab | -12.2895 | -46.41114 | 2025-09-16 04:04:00 | NOAA-21 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 374ff12e-ece2-3d80-bbf4-2251e5619600 | -15.62222 | -47.36749 | 2025-09-16 04:04:00 | NOAA-21 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 12.5 |
| d367a05e-427f-3814-a5a1-950590dedd34 | -12.81498 | -47.23258 | 2025-09-16 04:04:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 18f90e03-e813-3f82-b8e0-ae731bcca740 | -12.6464 | -47.95439 | 2025-09-16 04:04:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| d094cae3-748b-3d14-923b-4f5003e2ef1d | -13.20966 | -43.42317 | 2025-09-16 04:04:00 | NOAA-21 | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a694a7a7-9d35-3ba9-bea8-8e1c6ed67fca | -15.81789 | -53.46566 | 2025-09-16 04:04:00 | NOAA-21 | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 2b8cb4be-4cf3-3acc-a2b9-b293df42c140 | -12.61934 | -45.74908 | 2025-09-16 04:04:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 17.3 |
| 71a4c80c-cde6-389b-a6e8-09872cf7e1c0 | -14.5086 | -53.27829 | 2025-09-16 04:04:00 | NOAA-21 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 94017ef0-75cd-3d61-9817-9e59ab9f4600 | -14.83802 | -51.66965 | 2025-09-16 04:04:00 | NOAA-21 | ARAGUAIANA | MATO GROSSO | Brasil | 5101001 | 51 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 9fc2cf76-51b3-3e1c-b0cc-e9595a0b56ab | -16.48004 | -55.10379 | 2025-09-16 04:04:00 | NOAA-21 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 4.3 |
| 1649e05b-43ee-3c5c-b6f0-cebfd2af80e7 | -18.17117 | -45.19286 | 2025-09-16 04:04:00 | NOAA-21 | TRÊS MARIAS | MINAS GERAIS | Brasil | 3169356 | 31 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 8205ed2a-165f-3f73-a7f3-c779daf18455 | -12.53913 | -45.87666 | 2025-09-16 04:04:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 25.5 |
| cc8129e2-a2f3-36af-b22c-e08f9b9cda31 | -12.66579 | -47.92579 | 2025-09-16 04:04:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 7.4 |
| dbb09bd9-a6d0-3a3f-bcd1-d13b3e682317 | -15.8205 | -53.46376 | 2025-09-16 04:04:00 | NOAA-21 | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ef0c3ff7-d153-3236-a502-ca6ebb100c3f | -14.52204 | -47.3702 | 2025-09-16 04:04:00 | NOAA-21 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 37fef526-72f4-3a51-b5aa-4d44467af390 | -12.59985 | -47.98649 | 2025-09-16 04:04:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 48a6a68d-8f43-3216-82a1-db6a72962050 | -15.83458 | -53.47392 | 2025-09-16 04:04:00 | NOAA-21 | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 3.5 |
| a59548b7-7b8b-36b5-97c0-57ec5e0aa85e | -16.43228 | -45.67424 | 2025-09-16 04:04:00 | NOAA-21 | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 70b26d77-1a2d-358e-8f1e-e0fbf2249a7b | -16.67807 | -49.758 | 2025-09-16 04:04:00 | NOAA-21 | PALMEIRAS DE GOIÁS | GOIÁS | Brasil | 5215702 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| c45eaa66-a372-3e29-8a02-1536d6b753bb | -16.37075 | -42.64609 | 2025-09-16 04:04:00 | NOAA-21 | GRÃO MOGOL | MINAS GERAIS | Brasil | 3127800 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 31b8733b-d1e3-3fbb-bcc9-8267237f61ff | -14.6016 | -46.32716 | 2025-09-16 04:04:00 | NOAA-21 | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| ca32b91f-4bfb-3ef3-a2f3-03e62364147d | -14.50953 | -47.32457 | 2025-09-16 04:04:00 | NOAA-21 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 24c885c6-d3f1-3eeb-9895-a393836b3c3a | -14.83266 | -51.66853 | 2025-09-16 04:04:00 | NOAA-21 | ARAGUAIANA | MATO GROSSO | Brasil | 5101001 | 51 | 33 | nan | nan | nan | Cerrado | 5.1 |
| cf69cfdf-add1-309b-9548-19f011e88997 | -16.66896 | -49.75757 | 2025-09-16 04:04:00 | NOAA-21 | PALMEIRAS DE GOIÁS | GOIÁS | Brasil | 5215702 | 52 | 33 | nan | nan | nan | Cerrado | 4.3 |
| e3210e0c-0d66-320a-a44d-cf7b647bf8fe | -13.00625 | -47.94973 | 2025-09-16 04:04:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 0b1c1f4e-ae4f-3b67-96f8-95b4fe99abbd | -12.79972 | -47.24563 | 2025-09-16 04:04:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 57f49112-d347-31b7-add9-a81d98933219 | -14.53017 | -47.3949 | 2025-09-16 04:04:00 | NOAA-21 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 515b1c20-cbff-3f48-bce8-cb3143f7706b | -14.51769 | -47.32594 | 2025-09-16 04:04:00 | NOAA-21 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 6.4 |
| de24bf5a-3f2f-3bd2-8f13-97ca6566858d | -18.55935 | -49.26291 | 2025-09-16 04:04:00 | NOAA-21 | CENTRALINA | MINAS GERAIS | Brasil | 3115805 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.6 |
| 221c1181-41aa-3e8c-88d9-4e16012ac7ed | -12.79683 | -47.25331 | 2025-09-16 04:04:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 4.8 |
| fe44bc90-45c7-37af-8d4e-b4311695125f | -18.01319 | -43.9341 | 2025-09-16 04:04:00 | NOAA-21 | BUENÓPOLIS | MINAS GERAIS | Brasil | 3109204 | 31 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 12979c3e-261d-35c1-b0a6-22965ff289c4 | -13.80048 | -43.55289 | 2025-09-16 04:04:00 | NOAA-21 | MALHADA | BAHIA | Brasil | 2920205 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| cbccdacc-31dd-35b5-8c17-3a1df663f4d1 | -12.62019 | -45.74426 | 2025-09-16 04:04:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 17.3 |


[Clique aqui para ver as próximas entradas](README27.md)
