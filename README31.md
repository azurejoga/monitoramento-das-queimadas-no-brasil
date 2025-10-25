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

## Dados Diários - Página 31

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| b5242d93-7701-3cc4-a07c-bf828ee4ccb1 | -4.25119 | -44.57267 | 2025-10-25 04:17:00 | NOAA-20 | BACABAL | MARANHÃO | Brasil | 2101202 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 176d5842-7edd-3bb7-ade9-844bc7043c06 | -4.22004 | -48.3631 | 2025-10-25 04:17:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| a5fd90a8-7ecd-357c-9a95-1b13e96dfd4c | -3.08962 | -49.25896 | 2025-10-25 04:17:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| e0bde0f8-0bc0-3c6b-861a-d70beabecb6e | -3.51612 | -51.10159 | 2025-10-25 04:17:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 3953beaf-681e-3c2f-abd0-e7fd5327b6ab | -2.45843 | -49.03695 | 2025-10-25 04:17:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 46760bda-db0e-3c8a-81b1-be6ddc3dc7ce | -2.96109 | -49.57048 | 2025-10-25 04:17:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f2c71726-f197-3fb5-9698-dba8cebccad7 | -5.13713 | -41.20058 | 2025-10-25 04:17:00 | NOAA-20 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 6cc21de9-60bb-32d6-98e1-db37d1787768 | -5.08777 | -47.86512 | 2025-10-25 04:17:00 | NOAA-20 | CIDELÂNDIA | MARANHÃO | Brasil | 2103257 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 05fb0fe5-c3df-3680-88e6-a45cd96d9ccf | -3.49161 | -50.05893 | 2025-10-25 04:17:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 98106b36-ed2a-3bd3-b249-935fe664e080 | -5.29382 | -48.36547 | 2025-10-25 04:17:00 | NOAA-20 | ARAGUATINS | TOCANTINS | Brasil | 1702208 | 17 | 33 | nan | nan | nan | Amazônia | 2.8 |
| d4ee20db-a191-3da5-bde6-96a4c98ef167 | -2.96045 | -49.57444 | 2025-10-25 04:17:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4511b539-96ce-3658-8440-ace91ae48c0e | -6.60117 | -42.6552 | 2025-10-25 04:17:00 | NOAA-20 | FRANCISCO AYRES | PIAUÍ | Brasil | 2204105 | 22 | 33 | nan | nan | nan | Caatinga | 3.3 |
| b39d9ab6-04c6-3c41-9c23-584ca3dfcc8e | -5.62679 | -42.59215 | 2025-10-25 04:17:00 | NOAA-20 | MONSENHOR GIL | PIAUÍ | Brasil | 2206407 | 22 | 33 | nan | nan | nan | Caatinga | 3.9 |
| bd096aff-5cee-36a5-9a9b-1a553eb1e765 | -4.24788 | -44.57215 | 2025-10-25 04:17:00 | NOAA-20 | BACABAL | MARANHÃO | Brasil | 2101202 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 7f3ba776-8d10-30c7-9eaf-8b0854b1eb0f | -3.92123 | -47.69195 | 2025-10-25 04:17:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 782b8ae1-6586-3179-af7f-306e4889f431 | -2.26075 | -47.84726 | 2025-10-25 04:17:00 | NOAA-20 | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 173de1e8-0e8a-3af5-bd53-c98f85417330 | -3.81112 | -51.91599 | 2025-10-25 04:17:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| e1a54c68-c9af-34e6-a3eb-bd746971ad48 | -4.55746 | -46.68291 | 2025-10-25 04:17:00 | NOAA-20 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 692f7d2b-08b0-3a97-8b8a-3d3aa3c6ee9c | -6.31441 | -41.84938 | 2025-10-25 04:17:00 | NOAA-20 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 6b9891eb-317a-335e-822a-d097f8398f5e | -5.03618 | -41.19867 | 2025-10-25 04:17:00 | NOAA-20 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| cecc669c-9f99-3dea-8d45-7dff8f91d136 | -2.77101 | -48.60023 | 2025-10-25 04:17:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 3e6b1ec4-e799-31a5-95b2-cf0438d43b63 | -3.12314 | -49.10473 | 2025-10-25 04:17:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 112e5c3f-e4d1-310d-929f-ef50dbc49902 | -4.9079 | -47.65648 | 2025-10-25 04:17:00 | NOAA-20 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 1cd1062d-1851-36e8-b520-39dc621049d7 | -4.96307 | -47.59417 | 2025-10-25 04:17:00 | NOAA-20 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 7520e9f8-046c-3a88-8a75-e10b58fecab2 | -3.69181 | -49.94473 | 2025-10-25 04:17:00 | NOAA-20 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| bd6cc3b3-2e54-3d6f-bfb9-b3660ec261ed | -4.83781 | -50.93861 | 2025-10-25 04:17:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| e6b2eafd-e7e0-3fe9-907b-3a30aa63c1b0 | -5.03257 | -41.19828 | 2025-10-25 04:17:00 | NOAA-20 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 2de776f4-cb3f-33cd-8aba-46884bbd337f | -2.86944 | -50.7221 | 2025-10-25 04:17:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e58b16ec-37c0-370d-ade8-dd6ed2c46dec | -6.11288 | -41.74786 | 2025-10-25 04:17:00 | NOAA-20 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 5f400663-cd3e-363d-a37b-c0f0d1b33351 | -2.80577 | -54.3843 | 2025-10-25 04:17:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 16eadfa3-0975-34cb-91d3-75f2a2f03373 | -4.22081 | -48.35839 | 2025-10-25 04:17:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 2e242ac6-7c76-331f-9a6d-c9656fc23775 | -6.55381 | -43.23428 | 2025-10-25 04:17:00 | NOAA-20 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Caatinga | 4.6 |
| 4216c02d-8eba-36c9-adc9-f26664092706 | -2.79492 | -48.89207 | 2025-10-25 04:17:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 90537800-a2ff-370f-b1bb-d410e5abb351 | -3.12373 | -49.10106 | 2025-10-25 04:17:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 8.1 |
| 98b74f77-6ed9-3240-91f9-992d34671aeb | -5.82497 | -40.8066 | 2025-10-25 04:17:00 | NOAA-20 | QUITERIANÓPOLIS | CEARÁ | Brasil | 2311264 | 23 | 33 | nan | nan | nan | Caatinga | 1.9 |
| c2473f02-6ebf-3307-bca7-8ce83611ee99 | -2.73151 | -49.16098 | 2025-10-25 04:17:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 44d55f7d-d412-3785-bfe5-1bce776ba889 | -4.82878 | -50.93707 | 2025-10-25 04:17:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| d5762b8b-7067-3cf0-93d4-5e41bd0a354e | -4.93841 | -49.9602 | 2025-10-25 04:17:00 | NOAA-20 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| bef374eb-dada-3a93-99ac-4edbe062162d | -4.00155 | -48.32307 | 2025-10-25 04:17:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 9512311e-7f4e-3b46-8713-897f6c59ef99 | -4.55618 | -46.60283 | 2025-10-25 04:17:00 | NOAA-20 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5284d433-8dde-3027-9333-269d292ea9df | -2.80489 | -49.1412 | 2025-10-25 04:17:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 26.0 |
| 46cc351c-305b-37b8-8500-8ed5a796399a | -3.13468 | -50.62152 | 2025-10-25 04:17:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 46b4b72b-0a1f-3990-9fe2-fbd4521469fd | -4.82587 | -50.92699 | 2025-10-25 04:17:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| e42f7535-fcd9-386d-b071-de282237a01c | -2.72913 | -49.1633 | 2025-10-25 04:17:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| d1d1480d-7ad5-399e-9a6c-6ab5aa5de863 | -6.1277 | -41.72174 | 2025-10-25 04:17:00 | NOAA-20 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| a25382be-6ab2-3e99-bdef-be2e5348c43e | -3.11396 | -51.21093 | 2025-10-25 04:17:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 331027ba-948e-3315-a841-bbed3e8eb3d3 | -2.86485 | -50.72133 | 2025-10-25 04:17:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 4da5c3ac-cb8e-3a42-81ff-ed374f0349bb | -5.54123 | -46.52826 | 2025-10-25 04:17:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 803e7dee-5713-3dee-8b96-2a2802476310 | -6.13004 | -41.73015 | 2025-10-25 04:17:00 | NOAA-20 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 96531f90-5d31-3c73-8134-a181095da2dd | -5.6087 | -41.12304 | 2025-10-25 04:17:00 | NOAA-20 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 139c2de4-9678-3dcb-a20d-408b8f100c8b | -2.72437 | -49.16634 | 2025-10-25 04:17:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 45da4334-c964-399d-85fb-a72b81b99af0 | -5.33171 | -48.37177 | 2025-10-25 04:17:00 | NOAA-20 | ARAGUATINS | TOCANTINS | Brasil | 1702208 | 17 | 33 | nan | nan | nan | Amazônia | 0.9 |
| aa30589e-b480-33c9-943f-e66b8dd6d3fc | -3.11871 | -51.21168 | 2025-10-25 04:17:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 6a13b72a-b2ae-3332-86e0-77fa6afd497e | -6.54511 | -41.6859 | 2025-10-25 04:17:00 | NOAA-20 | INHUMA | PIAUÍ | Brasil | 2204709 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 9cdb83b6-d653-3c74-b505-64e676bc9748 | -3.43528 | -50.26292 | 2025-10-25 04:17:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 64cbd2bf-c3d7-3c59-9873-742d7e849b5b | -2.26309 | -47.85727 | 2025-10-25 04:17:00 | NOAA-20 | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9741b77c-b7af-34fd-8920-5285f723e759 | -2.89572 | -49.17049 | 2025-10-25 04:17:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| fac9904a-b692-3b95-a9fd-b5874664e57d | -5.14177 | -43.73081 | 2025-10-25 04:17:00 | NOAA-20 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| fe898fff-4b28-35d3-b8ee-ec775d41a76f | -3.08786 | -49.48182 | 2025-10-25 04:17:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 930a42db-7091-37e9-8a6a-d8b704757104 | -5.60543 | -46.25863 | 2025-10-25 04:17:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 128553c8-927b-3154-8773-a7b7ff08759d | -3.26021 | -50.14886 | 2025-10-25 04:17:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9b435a6a-1506-3acb-9dd2-d06be0202cac | -5.4577 | -46.47606 | 2025-10-25 04:17:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 5af1b7eb-4f49-3166-bd1b-f2699c56bfd1 | -3.22583 | -49.35084 | 2025-10-25 04:17:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 099ab5fc-62f3-35fa-8004-e61a699a273d | -6.40947 | -43.76904 | 2025-10-25 04:17:00 | NOAA-20 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 2d0cb7e6-cf15-39e9-b440-3a740810e642 | -4.09421 | -51.04907 | 2025-10-25 04:17:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 6a8b1813-3956-35e9-a7b4-ac97f1d5df09 | -4.80162 | -46.73984 | 2025-10-25 04:17:00 | NOAA-20 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c0755672-296f-3488-bb3e-0bf889c6fde6 | -3.98858 | -50.51997 | 2025-10-25 04:17:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 6012afa4-d800-38cf-a2da-63baad854cf4 | -3.72235 | -52.43847 | 2025-10-25 04:17:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 71e3f79b-9012-3a48-b144-0958b9208a3c | -3.4781 | -49.89987 | 2025-10-25 04:17:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 0d093ddf-e269-3ca6-964c-4367a0676172 | -3.60604 | -45.97403 | 2025-10-25 04:17:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 054bfb9d-5b00-3ebc-8e67-6aa702577d26 | -4.82507 | -50.93163 | 2025-10-25 04:17:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| fa8e971f-f197-3cb3-a7ad-a9d43ea143c1 | -4.83408 | -50.93323 | 2025-10-25 04:17:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| e10bdbe3-d263-363d-805f-4cc67652a871 | -5.45416 | -45.40635 | 2025-10-25 04:17:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 1ce08740-d2a2-3a5d-b220-7e11799901b8 | -2.55093 | -48.39363 | 2025-10-25 04:17:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 0096cffd-360c-3909-8a65-7ecbd0d774fe | -1.92128 | -52.14124 | 2025-10-25 04:17:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 67d341ff-1d2d-3a0c-b145-4f34cd3c967a | -6.83346 | -41.55194 | 2025-10-25 04:17:00 | NOAA-20 | SÃO JOSÉ DO PIAUÍ | PIAUÍ | Brasil | 2210201 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 2c3aee4d-9a35-374e-a2fd-7bcb83ba5902 | -3.60963 | -51.15958 | 2025-10-25 04:17:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 69ae8971-95a2-37c3-b219-1fca6b4ee6bb | -4.30104 | -42.32885 | 2025-10-25 04:17:00 | NOAA-20 | BARRAS | PIAUÍ | Brasil | 2201200 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 18f8359e-e012-30e7-800c-6e74abf3931b | -4.56707 | -46.45941 | 2025-10-25 04:17:00 | NOAA-20 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 0.4 |
| cc06f47a-5708-367f-837f-dccae9bdc3a6 | -6.06568 | -42.15157 | 2025-10-25 04:17:00 | NOAA-20 | ELESBÃO VELOSO | PIAUÍ | Brasil | 2203503 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 46b8e6cf-6382-3f91-93e4-9bd71bb57be9 | -3.09023 | -49.2552 | 2025-10-25 04:17:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 8d84b6ee-6f3f-3bec-8a20-6907fc4909f7 | -4.95874 | -47.59774 | 2025-10-25 04:17:00 | NOAA-20 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 844a4ef7-70f8-3a13-a5d6-466c378940e1 | -5.13846 | -43.7303 | 2025-10-25 04:17:00 | NOAA-20 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 30ee8389-fd92-3b88-95bc-c64125265698 | -2.87557 | -50.71339 | 2025-10-25 04:17:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| dde9fb80-8a29-37e0-a9aa-30edb9b9faab | -6.36097 | -44.27393 | 2025-10-25 04:17:00 | NOAA-20 | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 67720d70-19b4-3547-8326-b25c06e58368 | -2.85639 | -50.74424 | 2025-10-25 04:17:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b1d37d46-d94f-34e9-9042-6eeeaa663f93 | -3.13354 | -48.62311 | 2025-10-25 04:17:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| bf829e93-69a1-3186-8e05-e9b57ef1bc59 | -3.6893 | -49.94512 | 2025-10-25 04:17:00 | NOAA-20 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 8545810b-22fc-3075-8253-ef3d98ef725e | -6.59482 | -42.07467 | 2025-10-25 04:17:00 | NOAA-20 | BARRA D'ALCÂNTARA | PIAUÍ | Brasil | 2201176 | 22 | 33 | nan | nan | nan | Caatinga | 4.5 |
| fd52a56c-2770-37ef-8c37-27d7653c7466 | -4.0926 | -51.05872 | 2025-10-25 04:17:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| cda1b25d-6426-38a4-9a57-4514c482ae43 | 1.43139 | -50.89824 | 2025-10-25 04:17:00 | NOAA-20 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 130267df-52c8-372a-b68a-dbc612805002 | -4.82326 | -50.93298 | 2025-10-25 04:17:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 546dd925-07f5-3287-a0c8-126ca8b6d189 | -2.80137 | -49.13676 | 2025-10-25 04:17:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 2a322256-d859-39c8-9184-f69d92cf6c5f | -5.89367 | -41.28949 | 2025-10-25 04:17:00 | NOAA-20 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| c3198241-088a-3510-b3c0-9bb345c403d7 | -4.8333 | -50.93784 | 2025-10-25 04:17:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| c0ef133d-a940-33f0-8694-b170ea95407a | -5.55251 | -46.39114 | 2025-10-25 04:17:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| d1f01f54-3d48-3f41-94b5-14e05e6d8465 | -4.80878 | -45.5779 | 2025-10-25 04:17:00 | NOAA-20 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| c7a3ff13-a4f6-32cd-bec0-68eee58901ec | -5.40937 | -46.36487 | 2025-10-25 04:17:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 046f5809-e82b-333a-be84-3186a7d5ad99 | -3.22167 | -49.35016 | 2025-10-25 04:17:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 561890c6-86ad-3a67-976c-bf2d88073521 | -6.83408 | -41.54785 | 2025-10-25 04:17:00 | NOAA-20 | SÃO JOSÉ DO PIAUÍ | PIAUÍ | Brasil | 2210201 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |


[Clique aqui para ver as próximas entradas](README32.md)
