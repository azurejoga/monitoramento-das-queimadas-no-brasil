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

## Dados Diários - Página 5

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| be30447e-9eb2-3381-8a11-68e210d8c0e8 | -9.44026 | -48.88782 | 2026-05-28 03:51:00 | NOAA-20 | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 8d598ff6-79bd-34db-a781-49b1a88e88a1 | -5.30691 | -43.05461 | 2026-05-28 03:51:00 | NOAA-20 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 80dc6907-33ab-358b-b06f-797cdf13144d | -8.72554 | -48.32748 | 2026-05-28 03:51:00 | NOAA-20 | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Cerrado | 8.9 |
| d81493a4-0977-37cb-bcbc-1b049f058d7f | -11.59385 | -47.43547 | 2026-05-28 03:51:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 1dd31d57-c814-3c0c-b775-7a3bbb688305 | -6.29323 | -43.62396 | 2026-05-28 03:51:00 | NOAA-20 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 0c6cd0d7-434a-32ff-8581-7f6bddc3d22d | -11.61534 | -47.90436 | 2026-05-28 03:51:00 | NOAA-20 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 96d33913-4b0d-3481-a946-3b9771e2be62 | -9.13855 | -40.11005 | 2026-05-28 03:51:00 | NOAA-20 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 61df55d0-99a7-302c-b7ee-76d79484c4d3 | -9.05584 | -46.30302 | 2026-05-28 03:51:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 69f9b19c-aa2b-3c4a-9b03-ffe9ddfc9c95 | -8.72979 | -48.32618 | 2026-05-28 03:51:00 | NOAA-20 | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Cerrado | 4.6 |
| ce5208a1-bf23-3d24-9d0c-5c4459af9c05 | -9.34542 | -45.47272 | 2026-05-28 03:51:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 4.7 |
| ef0206e1-53f7-3f7d-a445-454926704482 | -10.62029 | -46.90723 | 2026-05-28 03:51:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| be058402-b7c9-38d7-bf4d-8e5f417e2210 | -5.92306 | -43.47744 | 2026-05-28 03:51:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 56c93e6b-2e59-3bfe-8f11-b5c5d414ded6 | -6.53811 | -44.68871 | 2026-05-28 03:51:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| d352077b-0115-3aee-9a2b-c9a17fc99dc7 | -9.27667 | -48.58543 | 2026-05-28 03:51:00 | NOAA-20 | RIO DOS BOIS | TOCANTINS | Brasil | 1718709 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 727827f3-a9b7-307b-91dd-a53b01e54e06 | -11.59652 | -47.45036 | 2026-05-28 03:51:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ec34c667-5ec4-35b3-b1f4-e76b42fda7fe | -9.28865 | -48.58806 | 2026-05-28 03:51:00 | NOAA-20 | RIO DOS BOIS | TOCANTINS | Brasil | 1718709 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 01bb2adc-0290-3806-8400-460b28672369 | -10.95391 | -44.17418 | 2026-05-28 03:51:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 32365332-b9fe-395b-bedf-6df33210aab7 | -9.28952 | -48.58347 | 2026-05-28 03:51:00 | NOAA-20 | RIO DOS BOIS | TOCANTINS | Brasil | 1718709 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 4db2887d-845a-3130-ad4f-bbd400a3a435 | -11.59719 | -47.44691 | 2026-05-28 03:51:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 86d5b69b-5ad5-3ac8-a42b-035c39481c9b | -11.58712 | -47.44128 | 2026-05-28 03:51:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 51055f5f-b517-307b-a426-80234cc5ef4b | -5.48167 | -45.11633 | 2026-05-28 03:51:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 469c3082-ddd4-3671-af6e-1c152326873f | -9.2818 | -48.59122 | 2026-05-28 03:51:00 | NOAA-20 | MIRANORTE | TOCANTINS | Brasil | 1713304 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c3449f3d-1858-3815-a78c-1f6c86296734 | -7.59553 | -46.46003 | 2026-05-28 03:51:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 0fc3c54d-dd21-3cdc-b001-af799e5a9ec3 | -11.59047 | -47.44117 | 2026-05-28 03:51:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 1d438102-c530-3fd1-83eb-4054422ea906 | -9.73881 | -49.21257 | 2026-05-28 03:51:00 | NOAA-20 | DIVINÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1707108 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 419cd7d4-02f5-30d1-9276-734767e8d93a | -5.79192 | -45.13427 | 2026-05-28 03:51:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 903d2860-7541-3ded-bba9-33f434d07727 | -7.5949 | -46.4635 | 2026-05-28 03:51:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| fff207bf-3d24-3637-b202-3898bbaafa35 | -5.95327 | -43.49246 | 2026-05-28 03:51:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 1c9b5f40-5969-326f-8962-d998a3ceafef | -9.73786 | -49.21752 | 2026-05-28 03:51:00 | NOAA-20 | DIVINÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1707108 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 3f532934-dcee-3730-a089-b64196a6b301 | -11.59649 | -47.43884 | 2026-05-28 03:51:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ffe843b0-dd1b-3c9e-8060-d708626fb5df | -10.63134 | -46.90018 | 2026-05-28 03:51:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| b3c45a18-60f0-3f30-bd1e-65dfaaa10c0e | -9.35131 | -45.46814 | 2026-05-28 03:51:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 4.5 |
| bd891171-27ba-389b-ad5e-170c1f630780 | -6.29174 | -43.63272 | 2026-05-28 03:51:00 | NOAA-20 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 065017da-16a1-30e8-8e2c-e1fedd5810c8 | -9.94156 | -48.01625 | 2026-05-28 03:51:00 | NOAA-20 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 1f629cda-8ffd-3d79-9fe6-a851a9f2aa78 | -7.47566 | -36.6065 | 2026-05-28 03:51:00 | NOAA-20 | SERRA BRANCA | PARAÍBA | Brasil | 2515500 | 25 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 657c114c-c8b8-3191-9f99-67f61bb205f5 | -10.95314 | -44.17848 | 2026-05-28 03:51:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 6b67dfdc-04a1-3ce1-89d9-5fd885fe9766 | -12.602 | -44.52323 | 2026-05-28 03:51:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 48770149-4d45-3649-94bc-c563ea39c81d | -9.35622 | -45.46909 | 2026-05-28 03:51:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 4.5 |
| d31f6870-f427-3a39-bb16-fa8dc5dfc17d | -9.35367 | -45.46504 | 2026-05-28 03:51:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 538789da-9433-393c-8ab4-afc3dc7e74d6 | -9.13922 | -40.10601 | 2026-05-28 03:51:00 | NOAA-20 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 9f931ccf-dc21-32d4-8184-0f9f11a87429 | -9.14459 | -51.28674 | 2026-05-28 03:51:00 | NOAA-20 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| be3b220a-243a-3cd0-9830-3c1b84666e11 | -8.72637 | -48.32313 | 2026-05-28 03:51:00 | NOAA-20 | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Cerrado | 8.9 |
| 6716be18-6cb2-3587-8b9d-fff08a768685 | -5.79808 | -45.12907 | 2026-05-28 03:51:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 233ed9fb-4585-34a6-a9c1-0ca06e17fd78 | -8.707 | -47.80053 | 2026-05-28 03:51:00 | NOAA-20 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 6af94e09-2532-38ac-a0fd-0b5de8a3dcc4 | -11.59111 | -47.43775 | 2026-05-28 03:51:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f1526d92-b442-3afa-b91e-efaf7dfe9f1f | -9.39268 | -48.44379 | 2026-05-28 03:51:00 | NOAA-20 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 37d4b57b-1947-345d-b5fa-4c5b0134f6db | -10.77629 | -46.90778 | 2026-05-28 03:51:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a2bb0770-6592-3544-b26b-f35ff179c320 | -10.62478 | -46.90581 | 2026-05-28 03:51:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 4b25dfeb-8cc9-3f02-a778-2afaf0f26399 | -14.78436 | -45.62312 | 2026-05-28 03:53:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| d597f482-f901-3c5d-a4f9-fa5e238bf892 | -12.32251 | -47.9007 | 2026-05-28 03:53:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 77c9da41-f626-3a7b-95c5-491dfcdfea39 | -14.39498 | -43.5187 | 2026-05-28 03:53:00 | NOAA-20 | IUIU | BAHIA | Brasil | 2917334 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| cb9392bf-7fc8-3708-ad32-058f71975599 | -14.39684 | -43.52066 | 2026-05-28 03:53:00 | NOAA-20 | IUIU | BAHIA | Brasil | 2917334 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| d02bb7ea-4cbd-3004-91ab-0268d4697192 | -12.68936 | -44.78727 | 2026-05-28 03:53:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 427b1e45-c68d-371e-81dc-250aa7787523 | -12.69378 | -44.78817 | 2026-05-28 03:53:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 37d8ca5c-5c61-3741-819f-d00070e1c223 | -12.6982 | -44.78902 | 2026-05-28 03:53:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| fc6ea70e-f606-3e1a-b6fa-7f2c58ec928d | -12.69018 | -44.78281 | 2026-05-28 03:53:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 31ef1c0f-e57e-39a2-95bc-81b1ce4cba92 | -18.76102 | -40.99633 | 2026-05-28 03:53:00 | NOAA-20 | MANTENA | MINAS GERAIS | Brasil | 3139607 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| ec6005f2-af25-388f-8b85-1beec6a2c825 | -12.32324 | -47.89695 | 2026-05-28 03:53:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| e48e9d79-d7c0-397f-bbde-e466ee69b6a5 | -12.32868 | -47.89822 | 2026-05-28 03:53:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 86784077-982f-35d5-ae1c-c27ae20e81b5 | -12.81509 | -44.87013 | 2026-05-28 03:53:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e05f3a39-19f7-3e43-9da2-498a556404ad | -19.08785 | -40.08157 | 2026-05-28 03:53:00 | NOAA-20 | SOORETAMA | ESPÍRITO SANTO | Brasil | 3205010 | 32 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 5fb87fda-a23c-3f60-8094-ab1930097e24 | -16.35298 | -47.34598 | 2026-05-28 03:53:00 | NOAA-20 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| b2381f37-661a-3a6d-b134-25701ab4bd47 | -17.92772 | -51.33975 | 2026-05-28 03:55:00 | NOAA-20 | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 22501809-faa8-36be-a14a-01a751a617e5 | -21.54231 | -48.89771 | 2026-05-28 03:55:00 | NOAA-20 | ITÁPOLIS | SÃO PAULO | Brasil | 3522703 | 35 | 33 | nan | nan | nan | Cerrado | 1.9 |
| ab2ed381-5e11-3698-a5c7-fb903a86d7ca | -21.53926 | -47.04545 | 2026-05-28 03:55:00 | NOAA-20 | MOCOCA | SÃO PAULO | Brasil | 3530508 | 35 | 33 | nan | nan | nan | Cerrado | 2.4 |
| d4b3a1c0-34a6-32e8-8a6c-8ec6b526e087 | -21.42898 | -47.07361 | 2026-05-28 03:55:00 | NOAA-20 | MOCOCA | SÃO PAULO | Brasil | 3530508 | 35 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c27a6ada-aa00-3d1d-867d-2c47a9b7cb34 | -21.43077 | -47.06454 | 2026-05-28 03:55:00 | NOAA-20 | MOCOCA | SÃO PAULO | Brasil | 3530508 | 35 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 01fa0451-8c03-3a5a-875b-026681f6f610 | -17.93144 | -51.35155 | 2026-05-28 03:55:00 | NOAA-20 | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| b1c8e532-2678-3113-87d0-61e93bd9b140 | -20.91257 | -46.78732 | 2026-05-28 03:55:00 | NOAA-20 | FORTALEZA DE MINAS | MINAS GERAIS | Brasil | 3126307 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 287df3fe-414e-3837-a812-165a22b3dce6 | -21.42206 | -47.06249 | 2026-05-28 03:55:00 | NOAA-20 | MOCOCA | SÃO PAULO | Brasil | 3530508 | 35 | 33 | nan | nan | nan | Cerrado | 1.8 |
| fd409dbb-03c7-3e18-9619-51eb465c10ff | -17.93375 | -51.34137 | 2026-05-28 03:55:00 | NOAA-20 | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 8a197bfe-f2cc-3619-acc6-7e5a1f602b18 | -21.42642 | -47.0635 | 2026-05-28 03:55:00 | NOAA-20 | MOCOCA | SÃO PAULO | Brasil | 3530508 | 35 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 597919a7-6969-30d7-879f-47082c84e799 | -21.54361 | -47.04644 | 2026-05-28 03:55:00 | NOAA-20 | MOCOCA | SÃO PAULO | Brasil | 3530508 | 35 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 71ac56ba-c0e2-3cd5-9c21-21abed44f889 | -21.41936 | -47.07608 | 2026-05-28 03:55:00 | NOAA-20 | MOCOCA | SÃO PAULO | Brasil | 3530508 | 35 | 33 | nan | nan | nan | Cerrado | 2.9 |
| a1cb4799-8610-3fc9-a30f-3ccf855e5d08 | -17.92844 | -51.33627 | 2026-05-28 03:55:00 | NOAA-20 | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a00db148-e3f3-3a2b-9435-c7f487143387 | -21.42461 | -47.07264 | 2026-05-28 03:55:00 | NOAA-20 | MOCOCA | SÃO PAULO | Brasil | 3530508 | 35 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 701b2271-ce55-35f7-9d09-40ffff4e88bb | -21.54015 | -47.04092 | 2026-05-28 03:55:00 | NOAA-20 | MOCOCA | SÃO PAULO | Brasil | 3530508 | 35 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 027668ae-b738-3ba0-9dc4-0cd88f8f089e | -20.91687 | -46.78843 | 2026-05-28 03:55:00 | NOAA-20 | FORTALEZA DE MINAS | MINAS GERAIS | Brasil | 3126307 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| d3e51210-4e8f-3c7f-a643-5daf4b9b6fb7 | -17.9262 | -51.34647 | 2026-05-28 03:55:00 | NOAA-20 | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| b583102b-626c-35de-a2e2-5ce2790bc93d | -21.54841 | -48.89316 | 2026-05-28 03:55:00 | NOAA-20 | ITÁPOLIS | SÃO PAULO | Brasil | 3522703 | 35 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 1bb0ed54-965b-3a23-8537-e4f67aa2b2f4 | -17.93334 | -51.34304 | 2026-05-28 03:55:00 | NOAA-20 | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| fb324e70-7f47-35d1-bdd1-c390d654affc | -17.92731 | -51.3414 | 2026-05-28 03:55:00 | NOAA-20 | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e9173da7-5e83-398f-ac4b-1c70698a99c5 | -17.92657 | -51.34483 | 2026-05-28 03:55:00 | NOAA-20 | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 7c2f63d7-51a1-3d19-a37f-c20b98ca9cc7 | -22.24221 | -46.58061 | 2026-05-28 03:55:00 | NOAA-20 | JACUTINGA | MINAS GERAIS | Brasil | 3134905 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| b58c41e5-95e9-30d0-ab8a-2b84f2af6400 | -21.54718 | -48.89893 | 2026-05-28 03:55:00 | NOAA-20 | ITÁPOLIS | SÃO PAULO | Brasil | 3522703 | 35 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 4e352672-9db4-3357-b55d-eb460d697e3a | -21.29623 | -48.58363 | 2026-05-28 03:55:00 | NOAA-20 | MONTE ALTO | SÃO PAULO | Brasil | 3531308 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| ed3924cf-3080-39d2-848a-f65ab8da7aee | -21.42024 | -47.07163 | 2026-05-28 03:55:00 | NOAA-20 | MOCOCA | SÃO PAULO | Brasil | 3530508 | 35 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c5d81bba-f5cb-3d9a-85df-f5dfc3d850b3 | -21.30106 | -48.58467 | 2026-05-28 03:55:00 | NOAA-20 | MONTE ALTO | SÃO PAULO | Brasil | 3531308 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| abb85a1c-e8d1-3a08-9fce-52681e059383 | -13.2186 | -54.5182 | 2026-05-28 04:00:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 79.8 |
| 25553d4e-7cbf-3b83-bdba-a6aecb5208fc | -13.2189 | -54.4975 | 2026-05-28 04:00:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 86.3 |
| f1607fe4-88b3-344e-a546-b1b2e64e227a | -11.591 | -47.4496 | 2026-05-28 04:00:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 52.9 |
| e4f307b2-ec85-3547-a46c-ecd8285563df | -13.2189 | -54.4975 | 2026-05-28 04:10:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 87.1 |
| 6cf7cfc4-1a2c-3717-ac75-f364091eeb69 | -11.591 | -47.4496 | 2026-05-28 04:10:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 95.5 |
| 83f20554-9610-373f-be10-ce7e383896fb | -13.2186 | -54.5182 | 2026-05-28 04:10:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 77.2 |
| 74dc906f-2879-3e04-9cde-23adb9e0b423 | -11.591 | -47.4496 | 2026-05-28 04:20:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 106.6 |
| 5796eb07-1aee-3d8e-a6a3-da3c62a932b0 | -13.2186 | -54.5182 | 2026-05-28 04:20:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 66.0 |
| d438f547-9b4e-3b35-92a5-22b257864576 | -13.2189 | -54.4975 | 2026-05-28 04:20:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 78.8 |
| 39b5c085-85cc-31e5-ac2d-74c83f1fcf5e | -11.591 | -47.4496 | 2026-05-28 04:30:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 98.7 |
| f4a36959-b4f6-3296-b873-1d80bcb1bd6d | -5.34007 | -42.68554 | 2026-05-28 04:38:00 | NOAA-21 | DEMERVAL LOBÃO | PIAUÍ | Brasil | 2203305 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| ee4a496b-0bce-3879-8f7c-1bec449ca7f4 | -4.38363 | -43.29397 | 2026-05-28 04:38:00 | NOAA-21 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |


[Clique aqui para ver as próximas entradas](README6.md)
