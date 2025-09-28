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
| 27597aae-55b4-33af-9fe1-09e02793b4e0 | -11.01911 | -50.71333 | 2025-09-28 00:52:00 | TERRA_M-M | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 15.0 |
| 1cc5453b-b698-3e3b-a085-3ae60a9f709a | -10.1372 | -51.63239 | 2025-09-28 00:52:00 | TERRA_M-M | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 7.3 |
| 5375b80e-28b1-3231-bb33-80ecd42def77 | -12.32538 | -51.52148 | 2025-09-28 00:52:00 | TERRA_M-M | BOM JESUS DO ARAGUAIA | MATO GROSSO | Brasil | 5101852 | 51 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 8d756809-73b8-3f98-bbe9-80029fc9baa1 | -9.65029 | -62.82708 | 2025-09-28 00:52:00 | TERRA_M-M | RIO CRESPO | RONDÔNIA | Brasil | 1100262 | 11 | 33 | nan | nan | nan | Amazônia | 113.2 |
| 782cf826-f3f5-37c3-84a4-a12b0313b0da | -7.75682 | -46.97942 | 2025-09-28 00:52:00 | TERRA_M-M | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 26.4 |
| e3bde6f3-9614-398e-b337-3516344beb3e | -11.57506 | -46.91466 | 2025-09-28 00:52:00 | TERRA_M-M | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 11.9 |
| 69ab9ce9-4222-3c87-a4dc-5a99f76305e9 | -10.82833 | -47.62002 | 2025-09-28 00:52:00 | TERRA_M-M | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 14.6 |
| 32d9e15a-40a9-31ba-bee2-c3a314b7186c | -13.60733 | -48.08149 | 2025-09-28 00:52:00 | TERRA_M-M | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 15.5 |
| a7d7211c-e100-335e-a35c-296bcb89a30b | -11.42741 | -46.65708 | 2025-09-28 00:52:00 | TERRA_M-M | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 15.5 |
| eebc0fd7-1ae0-3fe7-a1ce-241448f21627 | -10.79174 | -49.59433 | 2025-09-28 00:52:00 | TERRA_M-M | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 14.5 |
| a3dbecdd-4090-37bb-a7dc-c0e470378b19 | -12.88675 | -47.10903 | 2025-09-28 00:52:00 | TERRA_M-M | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 21.9 |
| 2aa4c743-69cb-311a-9840-342d50606584 | -13.62092 | -48.07378 | 2025-09-28 00:52:00 | TERRA_M-M | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 17.4 |
| ac016512-200c-3843-b392-f87a35c16d89 | -7.75032 | -47.0233 | 2025-09-28 00:52:00 | TERRA_M-M | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 81.0 |
| e0f591f2-c83d-329a-b123-76f9f3730e2a | -11.42352 | -46.64471 | 2025-09-28 00:52:00 | TERRA_M-M | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 28.4 |
| 1ad2c880-82bf-3446-89fc-e0d9b06efca5 | -12.68321 | -46.88047 | 2025-09-28 00:52:00 | TERRA_M-M | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 18.1 |
| e2df90c1-db67-3e01-b98b-ca602c9f08b3 | -10.99302 | -57.07322 | 2025-09-28 00:52:00 | TERRA_M-M | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 34.3 |
| a114b96a-31cf-3691-b651-e3a5e1b4997a | -12.01293 | -47.97314 | 2025-09-28 00:52:00 | TERRA_M-M | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 11.0 |
| 3b6f0d60-4721-3b4a-879a-e0b087636518 | -10.85646 | -47.80018 | 2025-09-28 00:52:00 | TERRA_M-M | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 12.3 |
| 4d14ef20-5481-3019-8dc0-e832057f79da | -11.36265 | -44.95699 | 2025-09-28 00:52:00 | TERRA_M-M | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 36.1 |
| 754173d9-fd59-3ac4-8b99-8588f4659daf | -10.91275 | -45.75692 | 2025-09-28 00:52:00 | TERRA_M-M | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 19.7 |
| a09688e7-f419-3111-ace4-f9b04a697e07 | -10.9825 | -44.31716 | 2025-09-28 00:52:00 | TERRA_M-M | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 60.7 |
| e4c2f9ff-c9ca-3042-b59a-fbaafb05b7a2 | -11.52348 | -54.31529 | 2025-09-28 00:52:00 | TERRA_M-M | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 82ca39f2-309c-3152-8c9e-82158e1c54dd | -8.72045 | -48.00029 | 2025-09-28 00:52:00 | TERRA_M-M | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 9.9 |
| f8e12580-cf7f-3c38-8cbf-40a4cee82bac | -12.95023 | -45.1534 | 2025-09-28 00:52:00 | TERRA_M-M | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 20.7 |
| 0e4230e0-71c4-3a7d-bb60-46bb37e8235f | -13.29199 | -50.68121 | 2025-09-28 00:52:00 | TERRA_M-M | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 878093c0-e42e-3aa3-9be8-c6d3127d0835 | -9.0449 | -46.72797 | 2025-09-28 00:52:00 | TERRA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 20.5 |
| 14fd3df9-380f-35f6-8a54-75ff620c7f29 | -11.41799 | -44.91357 | 2025-09-28 00:52:00 | TERRA_M-M | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 28.8 |
| b19b8433-a5c6-333a-8e0f-f99e774ac9b5 | -10.1281 | -51.63375 | 2025-09-28 00:52:00 | TERRA_M-M | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 243d4116-2816-3b25-a483-9ec694224a6e | -10.51398 | -51.94505 | 2025-09-28 00:52:00 | TERRA_M-M | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 4.6 |
| ef83fa96-197e-3f4c-b85c-32222de54f26 | -10.16422 | -49.3708 | 2025-09-28 00:52:00 | TERRA_M-M | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 9.8 |
| 1efa7e08-d614-3706-a8ee-31f2886b4530 | -8.90767 | -51.68017 | 2025-09-28 00:52:00 | TERRA_M-M | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 10.1 |
| 3dd6698e-85d4-337e-a7de-4b836f85a5e8 | -7.81297 | -47.00711 | 2025-09-28 00:52:00 | TERRA_M-M | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 24.2 |
| 6cc0f8bf-6e98-3fc2-9023-eb5463c6a7cf | -13.28279 | -50.68264 | 2025-09-28 00:52:00 | TERRA_M-M | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 330e9e74-421e-3769-8757-8fca96916cb5 | -11.98213 | -48.00011 | 2025-09-28 00:52:00 | TERRA_M-M | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 10.1 |
| 2dcd333f-d50e-307b-97f2-0634639a8da0 | -11.98935 | -47.03937 | 2025-09-28 00:52:00 | TERRA_M-M | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 37.3 |
| f2fe6662-4a2e-396c-a893-276c542742d5 | -11.15522 | -54.31509 | 2025-09-28 00:52:00 | TERRA_M-M | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 87a6c29f-3876-3bf3-8e82-705c801e2d8a | -11.15397 | -54.30576 | 2025-09-28 00:52:00 | TERRA_M-M | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 15.3 |
| 0569b4fd-e0fe-30e8-81c8-61a8b45d7e2d | -12.01453 | -47.91172 | 2025-09-28 00:52:00 | TERRA_M-M | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 13.3 |
| 93b5c20b-5230-3bc6-9e45-b6242513267d | -11.40507 | -44.9087 | 2025-09-28 00:52:00 | TERRA_M-M | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 84.5 |
| f2169c85-4bc5-3e98-9776-4a3a9eeb1482 | -11.59175 | -54.48318 | 2025-09-28 00:52:00 | TERRA_M-M | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 5a9c03e2-ec6c-3ed8-bc28-d3ab4b8b0eb8 | -7.79654 | -46.98837 | 2025-09-28 00:52:00 | TERRA_M-M | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 48.2 |
| 3f4577f3-6e55-3ab7-bc16-5059e0427bbf | -10.99664 | -57.06522 | 2025-09-28 00:52:00 | TERRA_M-M | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 88.5 |
| 7d749183-577f-331c-9381-36f2cf3d223a | -11.40336 | -44.91468 | 2025-09-28 00:52:00 | TERRA_M-M | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 60.4 |
| a8ecbb54-3d39-39fb-8b7a-7ff45204723c | -9.55124 | -47.7772 | 2025-09-28 00:52:00 | TERRA_M-M | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 10.6 |
| ae05a082-a8c4-3a28-8098-51427a555f09 | -7.79989 | -47.0091 | 2025-09-28 00:52:00 | TERRA_M-M | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 84.7 |
| 6ba759d9-9ee9-3b90-85c5-586828f2bf47 | -7.76339 | -47.02124 | 2025-09-28 00:52:00 | TERRA_M-M | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 17.3 |
| 0b1e3b18-f2d1-30ff-83e2-1ef5e55c8592 | -10.04792 | -49.21072 | 2025-09-28 00:52:00 | TERRA_M-M | MONTE SANTO DO TOCANTINS | TOCANTINS | Brasil | 1713700 | 17 | 33 | nan | nan | nan | Cerrado | 23.5 |
| d7cac847-f0eb-3f7d-9cf1-85125f7bad0b | -10.45789 | -50.85759 | 2025-09-28 00:52:00 | TERRA_M-M | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 14.0 |
| 314b828d-e2e0-3a0e-a963-33a22868926e | -10.53997 | -43.6527 | 2025-09-28 00:52:00 | TERRA_M-M | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 23.6 |
| 3e478645-f73f-3196-b793-c5de289e9275 | -7.73669 | -47.00982 | 2025-09-28 00:52:00 | TERRA_M-M | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 14.8 |
| 25f1221d-37d0-3dc0-9545-8549ac000ab3 | -7.54094 | -46.10524 | 2025-09-28 00:52:00 | TERRA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 45.5 |
| eb5e6222-5610-33db-8d13-1eb65115f391 | -12.01057 | -47.95852 | 2025-09-28 00:52:00 | TERRA_M-M | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 13.9 |
| 4c45fbfb-23e0-3c55-94a4-841f71d63c90 | -12.98622 | -46.85609 | 2025-09-28 00:52:00 | TERRA_M-M | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 38.6 |
| 7259a3ab-f5c4-3f16-8009-5281b8f99382 | -13.00775 | -49.46554 | 2025-09-28 00:52:00 | TERRA_M-M | ARAGUAÇU | TOCANTINS | Brasil | 1702000 | 17 | 33 | nan | nan | nan | Cerrado | 21.0 |
| 2ae2db50-76f3-3df0-bed8-1feee79ed685 | -12.90308 | -45.16761 | 2025-09-28 00:52:00 | TERRA_M-M | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 18.7 |
| 26f1f9cd-1331-3ce4-bc79-694e6884dbb0 | -5.89847 | -46.05229 | 2025-09-28 00:52:00 | TERRA_M-M | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 21.7 |
| d6998890-e0b5-3d99-9150-60a438915392 | -9.54367 | -50.78197 | 2025-09-28 00:52:00 | TERRA_M-M | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 20.8 |
| d3ba8b18-b6df-3120-88fc-c1ac9f65c18d | -11.97096 | -48.00191 | 2025-09-28 00:52:00 | TERRA_M-M | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 15.9 |
| 397beaca-59e7-34ac-9af1-539a6df2e6c6 | -8.62324 | -54.66207 | 2025-09-28 00:52:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| ec2bdaa0-179a-31c8-9fcc-d7ccf2e1c94d | -10.13584 | -51.62283 | 2025-09-28 00:52:00 | TERRA_M-M | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 430623d2-f656-3f9b-b94a-6885c0b0e5f5 | -9.94253 | -55.16236 | 2025-09-28 00:52:00 | TERRA_M-M | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 85a97bd2-bb82-353c-b706-e30163df873a | -8.68116 | -49.93472 | 2025-09-28 00:52:00 | TERRA_M-M | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 38.7 |
| 45e9cd41-9a8e-335b-9953-3328bebf1370 | -12.65096 | -51.67199 | 2025-09-28 00:52:00 | TERRA_M-M | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 699799b5-b8a3-3d0b-8d2d-d2912bf02e44 | -8.49623 | -47.00169 | 2025-09-28 00:52:00 | TERRA_M-M | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 24.9 |
| c41499f7-b98f-3aa6-8905-92e879dcfafe | -6.4434 | -43.93264 | 2025-09-28 00:52:00 | TERRA_M-M | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 52.1 |
| 6953bce4-24f1-3451-a259-e2f787fe7bef | -10.85395 | -47.78411 | 2025-09-28 00:52:00 | TERRA_M-M | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 15.4 |
| 23e7413c-82fe-35dd-a7a2-49f67d7d2b6b | -11.14497 | -54.30705 | 2025-09-28 00:52:00 | TERRA_M-M | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 18.3 |
| 94c24bd0-1709-3dfa-9d45-3207051143ba | -11.14622 | -54.31638 | 2025-09-28 00:52:00 | TERRA_M-M | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 23.1 |
| 368161b8-1f7c-3cd9-a7f4-075c297b5cf7 | -9.64697 | -62.86819 | 2025-09-28 00:52:00 | TERRA_M-M | RIO CRESPO | RONDÔNIA | Brasil | 1100262 | 11 | 33 | nan | nan | nan | Amazônia | 80.8 |
| 7cf8ac68-ff95-35f1-9864-5eca0ec7fa1f | -8.47361 | -47.79361 | 2025-09-28 00:52:00 | TERRA_M-M | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 18.7 |
| 4f55cdb2-5967-33c8-9f00-00395cf5bf97 | -12.00139 | -47.03736 | 2025-09-28 00:52:00 | TERRA_M-M | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 34.2 |
| 1d9aea4d-d68c-3ceb-83d4-94882bcc5f7b | -8.7193 | -50.05224 | 2025-09-28 00:52:00 | TERRA_M-M | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 6.8 |
| fd6f06e9-cb44-3746-88c3-1ca7e42b1a6a | -6.89954 | -44.75278 | 2025-09-28 00:52:00 | TERRA_M-M | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 29.6 |
| 38a4ccaf-ddf0-3460-bff1-ff19a2005409 | -12.76788 | -50.49268 | 2025-09-28 00:52:00 | TERRA_M-M | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 8.2 |
| af3b67e9-c6c1-3ba6-9d38-8edad4cc30f1 | -13.00607 | -49.45456 | 2025-09-28 00:52:00 | TERRA_M-M | ARAGUAÇU | TOCANTINS | Brasil | 1702000 | 17 | 33 | nan | nan | nan | Cerrado | 26.9 |
| 956a67cc-538e-3bd8-95e2-7e701fc95d76 | -12.65988 | -51.6706 | 2025-09-28 00:52:00 | TERRA_M-M | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 15.7 |
| 0f1106b8-3497-3a1c-b8eb-d18230c47679 | -11.05659 | -51.74149 | 2025-09-28 00:52:00 | TERRA_M-M | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Cerrado | 5.5 |
| e8f52e4d-91ec-3257-bfee-d1c1d5f956c2 | -11.42424 | -46.63809 | 2025-09-28 00:52:00 | TERRA_M-M | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 25.9 |
| bdedde7a-84ef-3db2-9b0f-22057d76e108 | -6.89801 | -44.77948 | 2025-09-28 00:52:00 | TERRA_M-M | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 23.3 |
| 2cdc3ea1-7a6f-3e0b-b12b-77dcac9546f8 | -9.31709 | -48.96131 | 2025-09-28 00:52:00 | TERRA_M-M | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | 10.5 |
| c6260571-1ec3-37bd-b4af-320ef3dddaf6 | -14.38547 | -54.94622 | 2025-09-28 00:52:00 | TERRA_M-M | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 11.0 |
| 26a6052a-dec6-3418-a1d2-1cad33aa046d | -10.97946 | -54.10077 | 2025-09-28 00:52:00 | TERRA_M-M | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 5.0 |
| b90ea885-c020-3bf6-b1fc-ab6cedeeeb9e | -11.62611 | -52.84683 | 2025-09-28 00:52:00 | TERRA_M-M | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 11.7 |
| 960415ff-89ae-311b-9ae8-702c855beb65 | -12.69446 | -45.48695 | 2025-09-28 00:52:00 | TERRA_M-M | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 18.9 |
| 4ad5e1fd-0241-3add-b043-7c56291595c5 | -11.09624 | -54.28541 | 2025-09-28 00:52:00 | TERRA_M-M | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 9.7 |
| ec010b7f-22f3-3702-924d-6b94c0e332a0 | -8.48573 | -47.79177 | 2025-09-28 00:52:00 | TERRA_M-M | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 12.3 |
| 290d1558-0a43-3bc7-a21e-6c80a39742cc | -10.12673 | -51.6242 | 2025-09-28 00:52:00 | TERRA_M-M | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 9.6 |
| 96444966-fbc5-33df-a10e-48f828c560b3 | -6.15249 | -47.30176 | 2025-09-28 00:52:00 | TERRA_M-M | CAMPESTRE DO MARANHÃO | MARANHÃO | Brasil | 2102556 | 21 | 33 | nan | nan | nan | Cerrado | 27.3 |
| d467e6ca-cf66-3b0f-8843-59b23ef9a1e6 | -12.00423 | -47.05495 | 2025-09-28 00:52:00 | TERRA_M-M | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 21.9 |
| 1a065675-8ffd-389a-b9fe-d31e74c05fdf | -8.49274 | -47.80233 | 2025-09-28 00:52:00 | TERRA_M-M | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 17.1 |
| c995c2e3-40fa-3e96-8726-82c3fab43508 | -10.96353 | -49.57352 | 2025-09-28 00:52:00 | TERRA_M-M | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 14.3 |
| 1e8e6cca-187f-327e-ad67-83a29b8b3b82 | -11.44763 | -44.9836 | 2025-09-28 00:52:00 | TERRA_M-M | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 19.4 |
| 402fffdc-f4de-3a51-9bc7-2514f14dde05 | -7.81254 | -46.99243 | 2025-09-28 00:52:00 | TERRA_M-M | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 21.1 |
| a84137ab-cac6-34cb-8294-28854abb2ddc | -9.31927 | -48.95528 | 2025-09-28 00:52:00 | TERRA_M-M | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | 22.2 |
| ff1a40d8-6ce2-3757-abd1-959558151dc9 | -11.44545 | -44.9904 | 2025-09-28 00:52:00 | TERRA_M-M | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 27.9 |
| 019df09e-eb9d-3e6c-a31e-2e5045d479a5 | -11.65011 | -52.87343 | 2025-09-28 00:52:00 | TERRA_M-M | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 7.3 |
| 4823972c-6afd-3399-8055-c9b90d8bd968 | -7.81272 | -46.90517 | 2025-09-28 00:52:00 | TERRA_M-M | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 30.8 |
| e1ffa35c-5099-3c64-9545-2a0d2e36c25b | -7.86775 | -44.54916 | 2025-09-28 00:52:00 | TERRA_M-M | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 32.4 |
| 7179709c-ec62-350f-b74c-9831a717833f | -12.93624 | -45.11215 | 2025-09-28 00:52:00 | TERRA_M-M | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 30.9 |
| 2ac4c56a-0986-3e0d-9e98-88156f784df4 | -8.49944 | -47.02196 | 2025-09-28 00:52:00 | TERRA_M-M | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 21.8 |


[Clique aqui para ver as próximas entradas](README6.md)
