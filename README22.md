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

## Dados Diários - Página 22

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| ba77c50c-fe44-393d-b8a3-0b3c32e34b57 | -12.12999 | -48.96078 | 2026-09-12 04:34:00 | NOAA-21 | FIGUEIRÓPOLIS | TOCANTINS | Brasil | 1707652 | 17 | 33 | nan | nan | nan | Cerrado | 4.7 |
| b36708c1-e877-31f2-9ba7-e1969d5592a8 | -9.70539 | -54.34735 | 2026-09-12 04:34:00 | NOAA-21 | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 9cc89eba-1565-361b-8a5e-6011991b8fd9 | -7.18562 | -45.92607 | 2026-09-12 04:34:00 | NOAA-21 | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 3ca6dea5-430e-3f74-b205-aa0b2ffc924f | -6.07115 | -53.49638 | 2026-09-12 04:34:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 3be828da-5f29-3f22-b832-48da4a37ce45 | -11.41291 | -43.94265 | 2026-09-12 04:34:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 8.1 |
| a422167c-0779-3733-b7ff-c328fcb8f19d | -6.51345 | -47.59976 | 2026-09-12 04:34:00 | NOAA-21 | PALMEIRAS DO TOCANTINS | TOCANTINS | Brasil | 1713809 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 0084d218-38da-3db8-a371-f84c21859b55 | -13.43954 | -43.81395 | 2026-09-12 04:34:00 | NOAA-21 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |
| f9cfd3c4-5d86-306d-8237-45db1f0a0bb2 | -7.19254 | -45.92714 | 2026-09-12 04:34:00 | NOAA-21 | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 4b74bc22-57c8-367b-ae05-308aa64a772f | -5.81353 | -47.22308 | 2026-09-12 04:34:00 | NOAA-21 | MONTES ALTOS | MARANHÃO | Brasil | 2107001 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 299d51c6-5f62-3f6e-9527-8d348ec2f2e9 | -9.72125 | -48.09265 | 2026-09-12 04:34:00 | NOAA-21 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 6541935e-5ec0-3583-8abd-cfc9e7b4e894 | -12.44382 | -49.58781 | 2026-09-12 04:34:00 | NOAA-21 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 12.1 |
| 74b86696-9f0a-3ed2-97e5-30f4d56c5c7f | -7.15234 | -46.6503 | 2026-09-12 04:34:00 | NOAA-21 | FEIRA NOVA DO MARANHÃO | MARANHÃO | Brasil | 2104073 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 6ab3994a-33f6-32df-84b7-e277f20b6f11 | -8.5346 | -54.70075 | 2026-09-12 04:34:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| d69593d9-b627-3f37-8638-7a018e8669f9 | -8.9752 | -49.66496 | 2026-09-12 04:34:00 | NOAA-21 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 6c707167-6f36-3ce7-8297-daeba98f349e | -8.80625 | -46.93748 | 2026-09-12 04:34:00 | NOAA-21 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 19c75d27-dd8c-3fe1-aa0f-9606ed210bd4 | -11.0967 | -50.82729 | 2026-09-12 04:34:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 59eeb478-e8ec-3248-9337-c3bfc20a26a2 | -6.62119 | -51.14584 | 2026-09-12 04:34:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 446805db-10ca-3ea6-84ff-8d52e99b1da4 | -10.50453 | -51.31209 | 2026-09-12 04:34:00 | NOAA-21 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 9214d88e-cbf0-395a-928e-5f4190d18e47 | -8.11951 | -54.79537 | 2026-09-12 04:34:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 80db4663-fce1-3d70-9571-836e145165ce | -5.82063 | -53.8047 | 2026-09-12 04:34:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 4c6aabf5-99c7-3453-8e25-5fcc0be8bd36 | -6.09632 | -57.68502 | 2026-09-12 04:34:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 717041d7-fcd0-3a33-a872-05c559032769 | -6.23076 | -51.69545 | 2026-09-12 04:34:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 9.2 |
| d0c7ee21-911c-32d2-a812-948516c9e300 | -7.27526 | -46.80587 | 2026-09-12 04:34:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 6.6 |
| d2892dc2-e7da-3aa9-a46d-8af63f089130 | -5.79176 | -53.82031 | 2026-09-12 04:34:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 29a4e190-c7af-3317-b0f0-2d603f2e26f8 | -10.06513 | -45.4735 | 2026-09-12 04:34:00 | NOAA-21 | SÃO GONÇALO DO GURGUÉIA | PIAUÍ | Brasil | 2209757 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| d964a403-e042-3a94-ade6-3e59d2ccc0a9 | -6.61206 | -58.85532 | 2026-09-12 04:34:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 6.4 |
| a9cf6a7d-96f2-333d-b67a-598b1d4de082 | -8.71002 | -49.61849 | 2026-09-12 04:34:00 | NOAA-21 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 32e3c447-a825-3b39-89a1-89b2ef8ddb39 | -6.52124 | -47.61517 | 2026-09-12 04:34:00 | NOAA-21 | PALMEIRAS DO TOCANTINS | TOCANTINS | Brasil | 1713809 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 40946220-4610-3475-97f0-3f4d07870a89 | -11.53721 | -44.89725 | 2026-09-12 04:34:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| aa906355-5a66-3eab-b058-8cf871e55927 | -6.72778 | -45.43525 | 2026-09-12 04:34:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 3409a4a0-3c9c-33ac-b7cd-31053b5a8388 | -10.55157 | -45.21576 | 2026-09-12 04:34:00 | NOAA-21 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 6428cc54-ed5f-39fb-8a9c-41aee9c44164 | -6.16449 | -47.08461 | 2026-09-12 04:34:00 | NOAA-21 | CAMPESTRE DO MARANHÃO | MARANHÃO | Brasil | 2102556 | 21 | 33 | nan | nan | nan | Cerrado | 6.0 |
| d0bdda8b-e5ad-3fc6-a68c-6c27a71e1a9f | -6.20991 | -55.26281 | 2026-09-12 04:34:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 1e2b08d8-e099-36c7-aa45-953087f95b29 | -9.92663 | -48.50119 | 2026-09-12 04:34:00 | NOAA-21 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 084a6ae0-3f4f-30de-b725-c9b45c37d525 | -9.90866 | -46.23975 | 2026-09-12 04:34:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 6c04192b-cbaf-336f-b067-108a3830dabc | -11.66917 | -50.67518 | 2026-09-12 04:34:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 258763c3-38d9-34c0-80be-6630b2f7d830 | -6.20828 | -55.27246 | 2026-09-12 04:34:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| a0da0a2b-ce44-379c-b622-c193a4d9794d | -10.63124 | -46.12216 | 2026-09-12 04:34:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 72ca7d87-83bf-3c0c-995d-ef901c03ece0 | -8.50446 | -50.14726 | 2026-09-12 04:34:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 52ccef19-aa30-3688-8e38-a193f332d8c0 | -9.71236 | -54.35648 | 2026-09-12 04:34:00 | NOAA-21 | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| df0b4187-d9c6-3afd-bc13-91906198dd1c | -10.90961 | -47.83449 | 2026-09-12 04:34:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 690bb72d-5d91-37a3-8346-def6693d4037 | -9.93385 | -48.52021 | 2026-09-12 04:34:00 | NOAA-21 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| dea63c21-7985-3219-ab3e-484f30478bfd | -9.24437 | -48.25367 | 2026-09-12 04:34:00 | NOAA-21 | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 4ca00240-8348-3dce-a665-26da70f79a68 | -11.08412 | -50.84047 | 2026-09-12 04:34:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 4.7 |
| bee0124f-5b5e-3107-9a98-28147deab662 | -9.03916 | -49.81763 | 2026-09-12 04:34:00 | NOAA-21 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| a302b026-0a96-3ff4-b488-c205804fc39c | -9.71301 | -54.35267 | 2026-09-12 04:34:00 | NOAA-21 | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 7472cc92-2f90-3a84-991b-df4aaa1e58bd | -6.22858 | -51.70876 | 2026-09-12 04:34:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| cc18a281-19f4-3963-b63d-35e424e61477 | -7.25988 | -46.68122 | 2026-09-12 04:34:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f6b6dcfa-1497-35be-8141-87488f784cf4 | -10.6354 | -46.1186 | 2026-09-12 04:34:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| a20277c6-a9bc-30d6-aec8-149560af883c | -6.24858 | -51.70296 | 2026-09-12 04:34:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5048f1ff-c4ef-3c88-9c55-ab936c3f11e9 | -10.28195 | -45.26739 | 2026-09-12 04:34:00 | NOAA-21 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 1ae28f85-1c1e-338a-82ce-ae8e437871cf | -6.04019 | -52.21707 | 2026-09-12 04:34:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 7d99a35c-a890-3317-8ac9-4a0fed48e31e | -5.9835 | -46.65188 | 2026-09-12 04:34:00 | NOAA-21 | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 45ca4a0c-a77b-3d82-b346-3bb5a7432e0f | -5.8477 | -52.11247 | 2026-09-12 04:34:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 3517da6f-dce1-34df-8362-8a2aae79c2b2 | -9.15599 | -49.984 | 2026-09-12 04:34:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0e28df01-c9b3-3b8b-a7ca-11236a43eca7 | -10.72976 | -46.14017 | 2026-09-12 04:34:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 06f378b7-7b88-372b-a522-32867ecdbb4e | -12.12014 | -47.29245 | 2026-09-12 04:34:00 | NOAA-21 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 8a64c927-dc1d-398d-996e-baca64bce83a | -6.20524 | -55.26199 | 2026-09-12 04:34:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 094bf8af-6020-358f-b346-223f29c41256 | -9.52729 | -40.33067 | 2026-09-12 04:34:00 | NOAA-21 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 1.5 |
| fc6c849b-9204-3931-890e-9c7fbea93fda | -10.72875 | -53.99731 | 2026-09-12 04:34:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| d956f6a2-6483-35d1-be10-f77b3298beec | -11.28311 | -47.56856 | 2026-09-12 04:34:00 | NOAA-21 | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| fb3ab3f2-4558-32f8-9231-77d7f7330e8b | -12.33079 | -46.7635 | 2026-09-12 04:34:00 | NOAA-21 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 7bf4eb96-8023-3ba6-b5e6-28fd123e2480 | -4.86705 | -56.0178 | 2026-09-12 04:34:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 8fb3871e-fa49-369f-be96-55f9a389769c | -6.87992 | -55.63893 | 2026-09-12 04:34:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| e89119d7-28ce-3006-9a6f-d1becbf639a3 | -10.89956 | -47.83293 | 2026-09-12 04:34:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 6e5d7ad9-591e-33cd-ab2f-8d489c8a076a | -12.11952 | -48.96263 | 2026-09-12 04:34:00 | NOAA-21 | FIGUEIRÓPOLIS | TOCANTINS | Brasil | 1707652 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 564c5e62-ab19-3c95-9a08-fa74faef47e7 | -7.2082 | -43.69021 | 2026-09-12 04:34:00 | NOAA-21 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| aed84c12-cb6c-3497-9cef-8da5d7d6a681 | -7.92555 | -49.73468 | 2026-09-12 04:34:00 | NOAA-21 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 82b20043-ec09-3c81-87fa-0a5986c2cea5 | -11.25462 | -54.12795 | 2026-09-12 04:34:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 3caa6962-b2dc-3d6b-9755-72bcdd96e065 | -10.68768 | -54.16145 | 2026-09-12 04:34:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 8.0 |
| 83cbafcc-18b9-39e6-bffd-c4f1c0230d7d | -10.56466 | -51.35841 | 2026-09-12 04:34:00 | NOAA-21 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 67fda22e-c788-3925-89fa-0c8ba8a06b2e | -9.16271 | -49.98508 | 2026-09-12 04:34:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| cd4811a9-0746-34c9-935b-6c6673417cfa | -11.37051 | -46.79889 | 2026-09-12 04:34:00 | NOAA-21 | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a3f003fb-8608-38b9-a0ca-83563806faff | -7.96388 | -44.01364 | 2026-09-12 04:34:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 0aad4cc2-41f9-3695-88e6-b1b00b89690e | -6.11363 | -55.65615 | 2026-09-12 04:34:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| b209010a-87f1-38b1-bd6c-985b6dd70956 | -5.85574 | -53.87696 | 2026-09-12 04:34:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4c47b9a4-1d4c-3663-9a46-048bc07d9ae2 | -6.88165 | -55.62894 | 2026-09-12 04:34:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f80e9ec8-4a39-3bfc-8228-8f5db985feaa | -9.8854 | -47.59499 | 2026-09-12 04:34:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d3cd6fc4-a7c2-37c1-ab1e-ae9139942410 | -6.16782 | -47.08513 | 2026-09-12 04:34:00 | NOAA-21 | CAMPESTRE DO MARANHÃO | MARANHÃO | Brasil | 2102556 | 21 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 1535c6fe-2b63-3987-9f75-6988d5413ab0 | -8.58908 | -54.56564 | 2026-09-12 04:34:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ec8a121d-e4f2-3fa1-946e-a771ef924199 | -11.39421 | -43.9585 | 2026-09-12 04:34:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 1ab24ae7-6c68-344f-879f-eca38bda72bf | -8.92072 | -50.86113 | 2026-09-12 04:34:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 5f6b8ee7-4ad4-368d-a6e2-aa2fe3dacbb0 | -9.784 | -42.00105 | 2026-09-12 04:34:00 | NOAA-21 | SENTO SÉ | BAHIA | Brasil | 2930204 | 29 | 33 | nan | nan | nan | Caatinga | 4.6 |
| fa927d3e-5a42-3795-b16e-6d768c3acd9f | -11.37978 | -46.83208 | 2026-09-12 04:34:00 | NOAA-21 | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 40b12eea-ded6-303c-90cd-a99dc9269d38 | -7.94399 | -46.23834 | 2026-09-12 04:34:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d9104d2c-ab3d-35de-aa46-e7603f8a26b3 | -10.89567 | -47.83592 | 2026-09-12 04:34:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| dbc37b6d-40fe-38a9-8639-6a50b492a1b1 | -11.39128 | -43.98026 | 2026-09-12 04:34:00 | NOAA-21 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 96fcec2e-1a91-3304-abe7-4d932ae8523b | -9.32341 | -45.64204 | 2026-09-12 04:34:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 724e31a3-90f0-348c-98d8-450888931e4b | -9.80365 | -43.47614 | 2026-09-12 04:34:00 | NOAA-21 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 84adc7d9-85cb-3820-9d3d-dde52f3eaa59 | -10.17521 | -45.33351 | 2026-09-12 04:34:00 | NOAA-21 | SÃO GONÇALO DO GURGUÉIA | PIAUÍ | Brasil | 2209757 | 22 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 0e5cf1dd-ef2b-3b4b-9880-6010a49eb12d | -11.24142 | -54.13285 | 2026-09-12 04:34:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 09ed7db0-7a1e-36af-8b08-6049963add2d | -9.72897 | -48.08667 | 2026-09-12 04:34:00 | NOAA-21 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| ba85e340-e9b6-3fa0-8673-6eb4dc18cd3a | -6.50612 | -47.60144 | 2026-09-12 04:34:00 | NOAA-21 | PALMEIRAS DO TOCANTINS | TOCANTINS | Brasil | 1713809 | 17 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 03d476ea-9885-38df-8f1a-908e16eba1a3 | -6.87539 | -47.43554 | 2026-09-12 04:34:00 | NOAA-21 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| be475676-3674-3f4c-8fd7-e015c13ec5d8 | -9.52223 | -40.32996 | 2026-09-12 04:34:00 | NOAA-21 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 1.5 |
| d04c647e-1b8f-3686-bd03-7cfec671e229 | -8.46129 | -47.53465 | 2026-09-12 04:34:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| c1776447-9769-3726-b214-b82a76b5763d | -11.41648 | -43.9469 | 2026-09-12 04:34:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 24c60307-99be-30f8-8004-5d132c067ca3 | -9.03303 | -49.81298 | 2026-09-12 04:34:00 | NOAA-21 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 7ef661e4-a42a-3f7d-b3c7-2c95f0d0a52b | -10.22666 | -45.18763 | 2026-09-12 04:34:00 | NOAA-21 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 9e256f1d-5298-372b-accd-ff9f6745c9f2 | -12.12174 | -48.97019 | 2026-09-12 04:34:00 | NOAA-21 | FIGUEIRÓPOLIS | TOCANTINS | Brasil | 1707652 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |


[Clique aqui para ver as próximas entradas](README23.md)
