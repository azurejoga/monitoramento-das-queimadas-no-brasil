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

## Dados Diários - Página 9

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 5bead961-07d1-324c-925f-9f81e8fe9707 | -3.71991 | -41.69752 | 2024-12-28 04:14:00 | NOAA-21 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 3.3 |
| 30ce95b8-b7d9-360f-b560-7d0672e4a101 | -3.91984 | -46.66497 | 2024-12-28 04:14:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.8 |
| f6d677b3-569c-39c9-94f9-171b1b3d397e | -3.87978 | -47.01345 | 2024-12-28 04:14:00 | NOAA-21 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 10c2a13b-80ed-30f4-84ae-108d2f9f7fb2 | -3.99696 | -46.74147 | 2024-12-28 04:14:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d3bba682-f806-34c3-a152-43b1e603a087 | -3.84353 | -47.0424 | 2024-12-28 04:14:00 | NOAA-21 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| db8d6027-f736-3b23-8f1f-e69e5e216274 | -2.47937 | -54.16978 | 2024-12-28 04:14:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 11b5a522-e77f-3334-bebe-9bec465d25cd | -3.86416 | -46.67479 | 2024-12-28 04:14:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 2d5ab825-a5cb-3c30-b356-d4a90d2d4580 | -4.00536 | -46.57054 | 2024-12-28 04:14:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 8a053f5c-debf-3af9-8c4f-0511f8f6c859 | -3.81248 | -46.72983 | 2024-12-28 04:14:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 758d7622-e90e-335e-8490-b189de0ae2c1 | -4.73907 | -44.65338 | 2024-12-28 04:14:00 | NOAA-21 | BERNARDO DO MEARIM | MARANHÃO | Brasil | 2101939 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 81a5b802-92f0-3d89-b6b1-77d6f6c7a02a | -1.70265 | -46.23154 | 2024-12-28 04:14:00 | NOAA-21 | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| befc179f-2bb4-3b79-add5-e429cc65af5a | -4.57088 | -41.29775 | 2024-12-28 04:14:00 | NOAA-21 | MILTON BRANDÃO | PIAUÍ | Brasil | 2206357 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| cf88ae11-6335-38cc-b5b0-1c674795c848 | -6.0065 | -39.2767 | 2024-12-28 04:14:00 | NOAA-21 | ACOPIARA | CEARÁ | Brasil | 2300309 | 23 | 33 | nan | nan | nan | Caatinga | 3.1 |
| 7c12fc00-ac7f-3f39-80db-e9e686dc94d8 | -4.0617 | -46.98899 | 2024-12-28 04:14:00 | NOAA-21 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 6129dce7-9c56-3c8f-a512-63dc4489ef81 | -3.99431 | -46.92762 | 2024-12-28 04:14:00 | NOAA-21 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 043493e4-69f0-30f1-997d-e491814bc2e7 | -2.33577 | -45.82986 | 2024-12-28 04:14:00 | NOAA-21 | PRESIDENTE MÉDICI | MARANHÃO | Brasil | 2109239 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e1dd396f-e981-32c8-916c-ae4580d65df4 | -5.91102 | -43.48501 | 2024-12-28 04:14:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 9345033f-633e-3fac-bdcc-95e2d7addd74 | -3.82473 | -46.62872 | 2024-12-28 04:14:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 733b4989-9dde-3ed2-998d-89d21583acd3 | -3.96503 | -46.67211 | 2024-12-28 04:14:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 596fe42e-b32c-3560-81f0-109277103c20 | -5.46827 | -39.55457 | 2024-12-28 04:14:00 | NOAA-21 | SENADOR POMPEU | CEARÁ | Brasil | 2312700 | 23 | 33 | nan | nan | nan | Caatinga | 3.0 |
| 492cafd1-514e-34f1-9c42-7b320d5df24e | -4.01651 | -46.7162 | 2024-12-28 04:14:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 082baa17-0c87-3e97-a298-61b2f67b7809 | -3.94983 | -46.76875 | 2024-12-28 04:14:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ab3d6e35-f1a2-33a2-a13f-020a1789fa93 | -3.80491 | -46.72864 | 2024-12-28 04:14:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 59417187-7794-3c48-96d0-82557973797d | -4.04291 | -46.72041 | 2024-12-28 04:14:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.8 |
| cf39121d-4b0e-35c7-9616-f7f31476a6c9 | -3.91205 | -46.98384 | 2024-12-28 04:14:00 | NOAA-21 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 64693f8b-8bf1-3720-852b-b2b9d876caec | -3.71325 | -41.6965 | 2024-12-28 04:14:00 | NOAA-21 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 5.4 |
| 3bc0d2dd-3bde-39e9-8036-d5f2a4caa0da | -3.96053 | -46.67616 | 2024-12-28 04:14:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 3.9 |
| f9e3bbe1-5f2a-3903-8ac0-7c4b56064c9d | -3.98068 | -46.55729 | 2024-12-28 04:14:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f2881829-27e1-3ed8-a945-8007b1653f8b | -3.99975 | -46.94263 | 2024-12-28 04:14:00 | NOAA-21 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 4.6 |
| fa7144be-4e68-3a5a-b614-1ccba8a05313 | -5.74055 | -44.43309 | 2024-12-28 04:14:00 | NOAA-21 | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 3b1acbbb-5d0e-3a2e-8ee3-35b6840a369c | -4.56926 | -44.12103 | 2024-12-28 04:14:00 | NOAA-21 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 968c308f-e223-3a92-975d-72cf09096dab | -6.08572 | -43.54055 | 2024-12-28 04:14:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| dad25171-3399-3db5-bca4-498f8a18a0ac | -1.72228 | -46.22992 | 2024-12-28 04:14:00 | NOAA-21 | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 95c74aa1-a3b0-34c3-86aa-d8ec9c82524d | -6.64511 | -41.99921 | 2024-12-28 04:14:00 | NOAA-21 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| a118f94b-9069-3bf0-980a-45e0a08e62c9 | -3.81553 | -46.7351 | 2024-12-28 04:14:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 1174c104-4fb2-312c-843d-a1b0046ebb1f | -4.03828 | -46.70091 | 2024-12-28 04:14:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.6 |
| b94a46dd-b9ea-3da2-bd39-87502221110b | -6.44623 | -44.38479 | 2024-12-28 04:14:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 6240f9fb-bb60-32cb-a85d-1655f759e354 | -3.53651 | -40.92982 | 2024-12-28 04:14:00 | NOAA-21 | VIÇOSA DO CEARÁ | CEARÁ | Brasil | 2314102 | 23 | 33 | nan | nan | nan | Caatinga | 1.2 |
| d5211886-24cf-362b-ae02-263f4c7add11 | -3.93953 | -46.3523 | 2024-12-28 04:14:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 77b2d85d-82e0-3cba-b2d9-a5844779d5ca | -2.84212 | -48.10429 | 2024-12-28 04:14:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b14af9e4-dd9d-3858-a964-a557c69347da | -3.80796 | -46.73388 | 2024-12-28 04:14:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| f63f9bda-9f08-32f6-9326-7bb6f0a916bb | -2.04855 | -46.56882 | 2024-12-28 04:14:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e288b3da-1bd1-3d23-8b49-41f0b58019df | -4.53146 | -41.55204 | 2024-12-28 04:14:00 | NOAA-21 | PEDRO II | PIAUÍ | Brasil | 2207900 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 3cbb027f-a96b-3f9f-bb2c-90d08798f95f | -3.88457 | -46.69201 | 2024-12-28 04:14:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 7cc8b240-1845-345f-9bb9-7f4af5620145 | -3.75894 | -47.21603 | 2024-12-28 04:14:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 5ae70ffd-3de4-3c6d-b69a-03f7c398a842 | -4.72911 | -45.61703 | 2024-12-28 04:14:00 | NOAA-21 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 4651e9f5-b04a-3d91-ad7d-87a46c41a245 | -5.63847 | -43.7255 | 2024-12-28 04:14:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c93c1c58-b492-389a-9cc0-58544c47c4a3 | -3.97766 | -46.55227 | 2024-12-28 04:14:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c14f475f-2424-3782-bce2-29e82f196365 | -4.04594 | -46.72567 | 2024-12-28 04:14:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 1e2d917d-d39d-34bc-95ab-2ce5f7b613ce | -4.76218 | -45.12181 | 2024-12-28 04:14:00 | NOAA-21 | POÇÃO DE PEDRAS | MARANHÃO | Brasil | 2108900 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 66b64edf-5aad-3967-bd77-fdbdeef5ddd6 | -4.33995 | -46.4962 | 2024-12-28 04:14:00 | NOAA-21 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ccc207a4-775d-38dd-a762-d6d26a463c20 | -3.89441 | -47.02069 | 2024-12-28 04:14:00 | NOAA-21 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 2.3 |
| ddbbac82-95c8-3af1-bdb1-c5d62681b6af | -3.55971 | -40.84754 | 2024-12-28 04:14:00 | NOAA-21 | COREAÚ | CEARÁ | Brasil | 2304004 | 23 | 33 | nan | nan | nan | Caatinga | 1.6 |
| e559bbcb-0262-3ab3-a279-e031e49779f7 | -3.91252 | -46.90633 | 2024-12-28 04:14:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 2.4 |
| a703e016-7eb8-30cf-8ca5-715e324a9a71 | -2.2192 | -53.64993 | 2024-12-28 04:14:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| b469b03e-192c-36dc-a07b-b3ff09bc952e | -3.70992 | -41.69598 | 2024-12-28 04:14:00 | NOAA-21 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 6ef0d4bf-1c03-3d14-b7c9-92882e8a8fc5 | -3.96212 | -46.67036 | 2024-12-28 04:14:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.8 |
| be1d0865-e238-3ad2-ae6c-bc3346839754 | -5.48571 | -46.44186 | 2024-12-28 04:14:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 198992e2-a358-3d9e-bd3b-704293041e5e | -3.53706 | -40.92624 | 2024-12-28 04:14:00 | NOAA-21 | VIÇOSA DO CEARÁ | CEARÁ | Brasil | 2314102 | 23 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 26a95e40-021c-3fd3-ba80-7a6c40ec4721 | -4.12044 | -46.72176 | 2024-12-28 04:14:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.7 |
| d54b307f-3d8c-30de-8c95-bd989292288f | -3.77396 | -46.82456 | 2024-12-28 04:14:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 2099a22b-95ac-3717-917a-af397029c189 | -3.95833 | -46.66988 | 2024-12-28 04:14:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 13e7f203-98dc-366a-afe9-e4b3341ea074 | -3.86744 | -47.01657 | 2024-12-28 04:14:00 | NOAA-21 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 4ff323e1-f6ea-3b58-ba1d-d4f06ddebaf1 | -6.40007 | -35.22978 | 2024-12-28 04:14:00 | NOAA-21 | CANGUARETAMA | RIO GRANDE DO NORTE | Brasil | 2402204 | 24 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 11461074-ad2e-3c6d-a4a2-392a88e3f890 | -4.72111 | -44.3426 | 2024-12-28 04:14:00 | NOAA-21 | CAPINZAL DO NORTE | MARANHÃO | Brasil | 2102754 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 337bf54d-73a0-3175-afa6-16152b8717c8 | -2.52047 | -51.86346 | 2024-12-28 04:14:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ce5bcb78-123e-3087-8f23-44275fe63ce0 | -3.81627 | -46.73044 | 2024-12-28 04:14:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 6570c64c-fe50-39fd-a514-08647cd38e30 | -5.57861 | -46.12943 | 2024-12-28 04:14:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 17.9 |
| 03bd7d62-1cae-30b5-bad2-4832055799d6 | -3.95091 | -49.44428 | 2024-12-28 04:14:00 | NOAA-21 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 8f1d5ecf-858f-3caf-887c-dd0c92524741 | -4.73509 | -44.6565 | 2024-12-28 04:14:00 | NOAA-21 | BERNARDO DO MEARIM | MARANHÃO | Brasil | 2101939 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 32887b69-a618-38c3-8938-905f220f729f | -4.0299 | -46.68085 | 2024-12-28 04:14:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 159a49d8-b562-3b76-b32f-18cd6a5c4e25 | -5.57432 | -46.13314 | 2024-12-28 04:14:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 15.4 |
| 07e1bdd6-080e-3559-ac02-3470af292f0c | -3.93948 | -46.7609 | 2024-12-28 04:14:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 4.6 |
| a3702b27-449f-374f-a68a-51d4c39e3364 | -3.97253 | -46.58355 | 2024-12-28 04:14:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.3 |
| dc4969a7-d33e-3713-a363-2b9eb5da8d7e | -4.03851 | -47.05897 | 2024-12-28 04:14:00 | NOAA-21 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 561a60a1-89f1-3f84-8cce-565d1eac0a3a | -4.06158 | -47.1118 | 2024-12-28 04:14:00 | NOAA-21 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 88cdcb7e-5892-3050-a94c-1217be588fb9 | -4.13007 | -46.68579 | 2024-12-28 04:14:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 7.0 |
| f82280e6-c053-35b0-ab12-5a2547e93b5c | -5.09461 | -40.58473 | 2024-12-28 04:14:00 | NOAA-21 | CRATEÚS | CEARÁ | Brasil | 2304103 | 23 | 33 | nan | nan | nan | Caatinga | 3.7 |
| 2171aaf8-12e3-3380-b07d-f417a233c75c | -5.24908 | -41.38909 | 2024-12-28 04:14:00 | NOAA-21 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 3.2 |
| 77bb692b-18ff-3ef0-bc6d-b24897416855 | -5.97782 | -41.69152 | 2024-12-28 04:14:00 | NOAA-21 | SANTA CRUZ DOS MILAGRES | PIAUÍ | Brasil | 2209153 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 30f550e1-b7f8-36a8-8adb-6b324a47d48b | -2.28336 | -45.59573 | 2024-12-28 04:14:00 | NOAA-21 | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3eab8dea-72b0-30b6-98fd-8e5b9a72c9e5 | -4.13082 | -46.68114 | 2024-12-28 04:14:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 67df847a-ee19-344a-acff-efbe23ed51c0 | -3.97981 | -46.55376 | 2024-12-28 04:14:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 8ada0f65-3d34-3a73-a909-317f4220c980 | -4.00519 | -46.71441 | 2024-12-28 04:14:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| c101b395-f0ac-38e0-8cd3-9148777ca19e | -4.78082 | -38.55273 | 2024-12-28 04:14:00 | NOAA-21 | MORADA NOVA | CEARÁ | Brasil | 2308708 | 23 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 930fcc1d-c997-3091-8c3c-14f89ae13d9c | -5.51836 | -41.73897 | 2024-12-28 04:14:00 | NOAA-21 | CASTELO DO PIAUÍ | PIAUÍ | Brasil | 2202604 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 73d3d5a6-fd1e-3750-92e9-204c69d659f3 | -3.90953 | -46.9252 | 2024-12-28 04:14:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 08bc306c-9450-338e-9cc1-dcf86e9309f5 | -2.49203 | -54.17177 | 2024-12-28 04:14:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 1947f0d0-25ec-3ed2-9a36-4caa93812d6e | -3.72045 | -41.69402 | 2024-12-28 04:14:00 | NOAA-21 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| c983a2e6-7c26-3525-a13a-f7a79c275117 | -5.93418 | -45.56961 | 2024-12-28 04:14:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 6a282daa-b75e-3a21-868e-7012f9baee75 | -6.08626 | -43.53709 | 2024-12-28 04:14:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 63a94e18-7911-3c3a-9837-543ff7b8d965 | -3.8423 | -46.69012 | 2024-12-28 04:14:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 5d42b193-14a8-36ce-8f52-4db0e095cc79 | -3.84208 | -45.85915 | 2024-12-28 04:14:00 | NOAA-21 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3d42a68c-1822-37dd-922b-499aaff3642b | -2.72907 | -45.62293 | 2024-12-28 04:14:00 | NOAA-21 | SANTA HELENA | MARANHÃO | Brasil | 2109809 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b38c0092-cc0e-3605-83a0-8db993a26e36 | -5.74168 | -44.42599 | 2024-12-28 04:14:00 | NOAA-21 | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a0b6de47-122f-3ffe-ac9c-65693b8ecc4e | -5.94696 | -44.09957 | 2024-12-28 04:14:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 0459d53b-3f02-349e-a354-4751ac3195a7 | -2.3883 | -51.90985 | 2024-12-28 04:14:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 51840c18-be35-396e-aa44-fea7b0bbaa36 | -6.01025 | -39.27726 | 2024-12-28 04:14:00 | NOAA-21 | ACOPIARA | CEARÁ | Brasil | 2300309 | 23 | 33 | nan | nan | nan | Caatinga | 3.1 |
| f105accf-a504-3eda-93a4-f41f92e32975 | -5.94363 | -44.09905 | 2024-12-28 04:14:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| bff54700-fc63-39df-b564-e77e9c882d5a | -4.01951 | -46.55419 | 2024-12-28 04:14:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |


[Clique aqui para ver as próximas entradas](README10.md)
