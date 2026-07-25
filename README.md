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

## Dados Diários - Página 1

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| f7c6c912-6dc0-35d2-8175-a8dd1b01b5d9 | -4.3772 | -47.7844 | 2026-07-25 00:00:00 | GOES-19 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 64.3 |
| 546688d6-2901-388e-b944-91954db7230b | -12.8543 | -44.386 | 2026-07-25 00:00:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 70.0 |
| 5f328b15-7c88-3f2b-a88b-8d4c84f66d47 | -4.3774 | -47.7627 | 2026-07-25 00:00:00 | GOES-19 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 145.7 |
| 44f6e6f0-95f5-3df8-afce-2222503dba30 | -10.8235 | -50.5026 | 2026-07-25 00:00:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 69.3 |
| 91c29828-625d-380d-8483-6b784ea1b31d | -11.807 | -47.0858 | 2026-07-25 00:00:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 108.1 |
| bf4187f1-d737-3ec0-aca2-c8cce6044b66 | -5.082 | -47.9433 | 2026-07-25 00:00:00 | GOES-19 | CIDELÂNDIA | MARANHÃO | Brasil | 2103257 | 21 | 33 | nan | nan | nan | Amazônia | 75.8 |
| 6487ac4b-7f8f-3cf3-9ceb-2cb6bf6b9321 | -4.3588 | -47.7636 | 2026-07-25 00:00:00 | GOES-19 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 75.4 |
| 54e621e0-35c2-3382-9a7c-469967d834d3 | -4.373 | -47.763699 | 2026-07-25 00:03:00 | METOP-C | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8922396e-2bef-3528-865f-a53390dcb631 | -4.3672 | -47.783901 | 2026-07-25 00:03:00 | METOP-C | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 57c5a5b9-ddc1-3551-a830-c4e67af6076c | -4.0491 | -43.247299 | 2026-07-25 00:03:00 | METOP-C | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 1b3354eb-a0a5-3783-87ba-d67a72174d7f | -4.0589 | -43.245098 | 2026-07-25 00:03:00 | METOP-C | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 3a48d51b-d16e-3623-b913-48e12a738a93 | -11.7964 | -47.089802 | 2026-07-25 00:03:00 | METOP-C | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 1475e12e-05e8-33b9-8a96-0ce09fc5d610 | -5.079 | -47.9244 | 2026-07-25 00:03:00 | METOP-C | CIDELÂNDIA | MARANHÃO | Brasil | 2103257 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| c1bd4442-b777-31cf-ab34-d37fa9ef7726 | -11.7923 | -47.068699 | 2026-07-25 00:03:00 | METOP-C | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 980d59cf-49e8-36a3-aa8e-250e50e85b01 | -11.428 | -40.765099 | 2026-07-25 00:03:00 | METOP-C | MIGUEL CALMON | BAHIA | Brasil | 2921203 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| 000bc295-e8d4-3b6f-bbed-ae3ce0e960b4 | -12.8336 | -44.392399 | 2026-07-25 00:03:00 | METOP-C | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| c7e34487-d89a-31a1-a1d1-e1efe1e7acf5 | -4.3536 | -47.767899 | 2026-07-25 00:03:00 | METOP-C | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 62bbd592-d605-359a-8e9f-161419dfd387 | -11.7867 | -47.091702 | 2026-07-25 00:03:00 | METOP-C | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| a46f99b3-d6ec-3553-bbd2-69da289d4fc4 | -11.4298 | -40.773399 | 2026-07-25 00:03:00 | METOP-C | MIGUEL CALMON | BAHIA | Brasil | 2921203 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| d4b83bb6-8b99-3644-b1f7-de3bf5ed990b | -3.1174 | -40.9869 | 2026-07-25 00:03:00 | METOP-C | GRANJA | CEARÁ | Brasil | 2304707 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| 29c91ac1-7ed8-3db3-95a2-c431cc0a523e | -12.3337 | -48.218399 | 2026-07-25 00:03:00 | METOP-C | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 4080d7b7-57dd-32ac-95d0-6f59855aaa82 | -4.3593 | -47.747799 | 2026-07-25 00:03:00 | METOP-C | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e3142d1f-17b1-3aa8-a8a4-647e37a845d5 | -5.0692 | -47.926498 | 2026-07-25 00:03:00 | METOP-C | CIDELÂNDIA | MARANHÃO | Brasil | 2103257 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| fb1727d5-e2da-3b57-8533-3afab455d952 | -11.7826 | -47.070599 | 2026-07-25 00:03:00 | METOP-C | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 71730b60-8048-3795-9c68-96635dbd5ba1 | -4.3633 | -47.7658 | 2026-07-25 00:03:00 | METOP-C | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9ab956a8-14bf-3bbd-a32c-5a3b3ef12330 | -5.0831 | -47.943401 | 2026-07-25 00:03:00 | METOP-C | CIDELÂNDIA | MARANHÃO | Brasil | 2103257 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| be95816a-8ef6-355d-8a1d-1296784d6103 | -5.0733 | -47.945499 | 2026-07-25 00:03:00 | METOP-C | CIDELÂNDIA | MARANHÃO | Brasil | 2103257 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 0e039b9e-63ce-3c45-a098-dc2276319729 | -15.5712 | -46.811298 | 2026-07-25 00:03:00 | METOP-C | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 7f4d1c8b-73b9-3cd0-a979-7ad2264e646b | -12.8433 | -44.3904 | 2026-07-25 00:03:00 | METOP-C | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| ee146e19-7093-383d-a71d-57f807054ac2 | -3.9943 | -43.278099 | 2026-07-25 00:03:00 | METOP-C | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| b31bf4b4-d496-3eb5-9af8-c49fcfd6ee1f | -10.8046 | -50.5046 | 2026-07-25 00:10:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 62.6 |
| 60e2c479-74ae-3eea-b724-cf0259980a03 | -4.3774 | -47.7627 | 2026-07-25 00:10:00 | GOES-19 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 124.3 |
| 82befefc-907b-379d-9283-89ecd7050d9e | -4.3588 | -47.7636 | 2026-07-25 00:10:00 | GOES-19 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 71.1 |
| ff4a21db-d37d-3419-a6f6-b175ca607fc1 | -4.3772 | -47.7844 | 2026-07-25 00:10:00 | GOES-19 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 68.0 |
| 259c2322-b275-32f2-9c23-d83092ca3c81 | -11.807 | -47.0858 | 2026-07-25 00:10:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 78.4 |
| 04a73b22-a90a-3ec7-b1ef-db3adc81808a | -12.8543 | -44.386 | 2026-07-25 00:10:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 66.4 |
| a96a898d-0eef-3042-9cbb-63041542b178 | -5.1006 | -47.9422 | 2026-07-25 00:10:00 | GOES-19 | VILA NOVA DOS MARTÍRIOS | MARANHÃO | Brasil | 2112852 | 21 | 33 | nan | nan | nan | Amazônia | 66.1 |
| 1f30548d-ccca-3634-876f-ebf32eab845a | -15.25431 | -43.93874 | 2026-07-25 00:13:00 | TERRA_M-M | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Cerrado | 13.5 |
| 10e6e28e-8abe-3ac3-8099-8f0b39f9f80f | -18.41577 | -49.92689 | 2026-07-25 00:13:00 | TERRA_M-M | INACIOLÂNDIA | GOIÁS | Brasil | 5209937 | 52 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 582eddc2-190c-39cd-a49a-8b487c7a5eef | -18.40817 | -49.93754 | 2026-07-25 00:13:00 | TERRA_M-M | INACIOLÂNDIA | GOIÁS | Brasil | 5209937 | 52 | 33 | nan | nan | nan | Cerrado | 9.9 |
| 5f04ca37-2f7c-380a-aaca-4606d8fbda37 | -16.34075 | -49.50327 | 2026-07-25 00:13:00 | TERRA_M-M | INHUMAS | GOIÁS | Brasil | 5210000 | 52 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 331ab2a7-7a10-3795-aea5-948706bd3d48 | -15.57534 | -46.81719 | 2026-07-25 00:13:00 | TERRA_M-M | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 30.0 |
| 9ab0d76c-9aaf-382d-b8cc-58ac466142a0 | -16.44117 | -49.90031 | 2026-07-25 00:13:00 | TERRA_M-M | ANICUNS | GOIÁS | Brasil | 5201306 | 52 | 33 | nan | nan | nan | Cerrado | 20.0 |
| da774b80-090c-3ae0-8b72-3091e3add352 | -15.62023 | -48.2734 | 2026-07-25 00:13:00 | TERRA_M-M | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 5.2 |
| e3498b2e-4bca-361d-869d-e92f61bb2d9b | -18.48578 | -51.57662 | 2026-07-25 00:13:00 | TERRA_M-M | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 4.6 |
| e207e5b4-3d8b-3c85-bd64-1c75993f5801 | -16.34205 | -49.51249 | 2026-07-25 00:13:00 | TERRA_M-M | INHUMAS | GOIÁS | Brasil | 5210000 | 52 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 9e6b764e-3591-3317-be42-f53c5d995f18 | -18.81115 | -53.14045 | 2026-07-25 00:13:00 | TERRA_M-M | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 9cd3d160-a7d8-3df6-938e-f33f09729e0a | -15.58534 | -46.81564 | 2026-07-25 00:13:00 | TERRA_M-M | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 46.0 |
| f1e5e275-1686-3816-b632-cf3aeb12aaae | -18.40691 | -49.92823 | 2026-07-25 00:13:00 | TERRA_M-M | INACIOLÂNDIA | GOIÁS | Brasil | 5209937 | 52 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 98e8c66e-a710-3949-b6f4-813feb10af54 | -18.41703 | -49.9362 | 2026-07-25 00:13:00 | TERRA_M-M | INACIOLÂNDIA | GOIÁS | Brasil | 5209937 | 52 | 33 | nan | nan | nan | Cerrado | 14.0 |
| 24e40900-95a3-3917-bd32-5b048238a5bd | -13.29687 | -54.33165 | 2026-07-25 00:16:00 | TERRA_M-M | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 9.0 |
| db12d46b-d1b0-38e5-91b3-5501c2b081b7 | -12.0189 | -50.49036 | 2026-07-25 00:16:00 | TERRA_M-M | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 19.1 |
| ce5b26f3-f791-3f22-8c6d-5ed343691bb9 | -11.79838 | -47.10388 | 2026-07-25 00:16:00 | TERRA_M-M | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 24.2 |
| 265b69dc-f620-3c34-b494-97020c0b7548 | -12.13709 | -50.40537 | 2026-07-25 00:16:00 | TERRA_M-M | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 15.4 |
| 87b33af1-7f8e-3b15-b458-3ba3f99ea579 | -11.79647 | -47.09113 | 2026-07-25 00:16:00 | TERRA_M-M | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 98.9 |
| 35fcf4c2-107e-3a9f-93ce-10325e19eb7f | -14.17184 | -51.9004 | 2026-07-25 00:16:00 | TERRA_M-M | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 883e4e95-0753-3ef9-aaef-bd835e4e3839 | -13.30715 | -54.33031 | 2026-07-25 00:16:00 | TERRA_M-M | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 7.9 |
| bfd471b5-cc48-3eca-9166-aead85b6884e | -12.84238 | -44.40223 | 2026-07-25 00:16:00 | TERRA_M-M | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 31.1 |
| 9614ee6c-ba6a-3850-9582-b80382537498 | -12.03628 | -50.53675 | 2026-07-25 00:16:00 | TERRA_M-M | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 5.5 |
| fa116885-9d30-35d5-acd2-a3b7ea8e8ca4 | -13.40061 | -48.16443 | 2026-07-25 00:16:00 | TERRA_M-M | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 12.4 |
| 3424606d-17d7-3fbd-a336-c9957dcb6c95 | -12.85107 | -44.38644 | 2026-07-25 00:16:00 | TERRA_M-M | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 45.0 |
| 3e3c5a1c-9f89-30ea-b118-396531856f52 | -11.93183 | -51.79328 | 2026-07-25 00:16:00 | TERRA_M-M | BOM JESUS DO ARAGUAIA | MATO GROSSO | Brasil | 5101852 | 51 | 33 | nan | nan | nan | Amazônia | 9.3 |
| 11891cf8-a80b-39b6-9872-721927863bba | -12.85418 | -44.4058 | 2026-07-25 00:16:00 | TERRA_M-M | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 44.3 |
| 2c0eac69-698d-34c2-9aa9-3b0b642949d6 | -11.93061 | -51.78415 | 2026-07-25 00:16:00 | TERRA_M-M | BOM JESUS DO ARAGUAIA | MATO GROSSO | Brasil | 5101852 | 51 | 33 | nan | nan | nan | Amazônia | 5.5 |
| fa27efab-d29c-3f12-bcf9-26cb5fae6105 | -12.04387 | -50.52643 | 2026-07-25 00:16:00 | TERRA_M-M | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 41a1f3d4-e876-3322-aa24-ee81552944e4 | -12.34165 | -48.2198 | 2026-07-25 00:16:00 | TERRA_M-M | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 36.5 |
| 528dec34-f50d-3776-81bc-a1d248719259 | -12.02015 | -50.49939 | 2026-07-25 00:16:00 | TERRA_M-M | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 16.9 |
| ba1c18e2-4687-391d-abbd-46bf6376cc18 | -12.85493 | -44.39997 | 2026-07-25 00:16:00 | TERRA_M-M | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 52.1 |
| 2e9bd623-2865-37bd-9da1-1c39e378fa09 | -11.64426 | -49.46448 | 2026-07-25 00:16:00 | TERRA_M-M | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 5f2c37d0-7910-3ef2-a948-7ff322ddfa3a | -11.80877 | -47.10215 | 2026-07-25 00:16:00 | TERRA_M-M | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 14.5 |
| 77e72300-1d8b-3383-8b59-f820780d46e3 | -11.80217 | -47.08435 | 2026-07-25 00:16:00 | TERRA_M-M | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 56.3 |
| 13ad81c6-c239-3024-afd2-1635d301cba1 | -12.12696 | -50.33295 | 2026-07-25 00:16:00 | TERRA_M-M | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 13.6 |
| 85dacf72-a90c-3704-8f6e-329920aadb6c | -11.64563 | -49.47404 | 2026-07-25 00:16:00 | TERRA_M-M | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 34bc85a1-9020-340a-9db5-e0a0cdd2cdc9 | -11.80416 | -47.09711 | 2026-07-25 00:16:00 | TERRA_M-M | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 104.4 |
| 25cb2f3b-8435-3ded-9d67-343498cd6b72 | -11.6849 | -50.46561 | 2026-07-25 00:16:00 | TERRA_M-M | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 5.0 |
| e0d74c6c-4e83-32da-960d-27fc3a8d2c47 | -14.1731 | -51.90999 | 2026-07-25 00:16:00 | TERRA_M-M | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 9d9d4f66-042b-30a2-b058-76997f6fa14c | -11.00391 | -47.47893 | 2026-07-25 00:16:00 | TERRA_M-M | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 8.3 |
| f22c98e6-3de7-37dc-b532-adc054e26a64 | -11.2364 | -50.48862 | 2026-07-25 00:16:00 | TERRA_M-M | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 10.3 |
| b2dc0dcc-13c4-34d4-acf4-e06add56c0c4 | -11.70104 | -49.0219 | 2026-07-25 00:16:00 | TERRA_M-M | GURUPI | TOCANTINS | Brasil | 1709500 | 17 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 4d87bc40-1ace-3d0c-8ce9-e444fd0905cf | -11.9936 | -50.5033 | 2026-07-25 00:16:00 | TERRA_M-M | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 987251e9-3b88-330d-8ad4-ec9baa4ebf46 | -12.12444 | -50.37954 | 2026-07-25 00:16:00 | TERRA_M-M | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 9ba8e5d0-098d-3ce5-81ba-376696ec5b22 | -13.47905 | -44.04008 | 2026-07-25 00:16:00 | TERRA_M-M | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 51.3 |
| e01556e0-ed36-343d-9d42-5048b696ddc2 | -12.34451 | -48.21345 | 2026-07-25 00:16:00 | TERRA_M-M | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 12.1 |
| beee7651-4ca4-3a83-a3ca-8033f971dfb1 | -12.34612 | -48.22416 | 2026-07-25 00:16:00 | TERRA_M-M | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 13.1 |
| 6b4b6beb-92d0-360b-ad7e-c208ea2060dc | -11.80687 | -47.08938 | 2026-07-25 00:16:00 | TERRA_M-M | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 36.0 |
| 53008792-cc2b-39dd-a56a-5172be9649ac | -12.04513 | -50.53544 | 2026-07-25 00:16:00 | TERRA_M-M | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 24abd2aa-7e24-3e07-913e-d9b78a0d8a5a | -10.81332 | -50.49806 | 2026-07-25 00:18:00 | TERRA_M-M | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 115.1 |
| 9c78d910-cae7-30b6-a071-983053e7a22f | -10.81458 | -50.50712 | 2026-07-25 00:18:00 | TERRA_M-M | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 16.4 |
| 22a2d02c-39b3-30ef-a438-c40850983c57 | -11.35894 | -55.44143 | 2026-07-25 00:18:00 | TERRA_M-M | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 9.3 |
| 1d8145f4-f902-3a75-b3e3-48d00ecd0902 | -4.17712 | -48.58355 | 2026-07-25 00:18:00 | TERRA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 7.8 |
| 2164b532-5d54-3030-b82f-1823b0614ca7 | -9.47497 | -57.31317 | 2026-07-25 00:18:00 | TERRA_M-M | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 18.2 |
| 14e0a243-481f-3977-94d3-1c16716e55de | -9.86818 | -47.10365 | 2026-07-25 00:18:00 | TERRA_M-M | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 8.8 |
| ba61d64f-3146-3fae-aa70-13ae6e3b9747 | -9.88312 | -49.97647 | 2026-07-25 00:18:00 | TERRA_M-M | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 7.5 |
| d9e992e1-590e-3d62-ab1b-a044d71b3429 | -8.38027 | -48.21937 | 2026-07-25 00:18:00 | TERRA_M-M | TUPIRATINS | TOCANTINS | Brasil | 1721307 | 17 | 33 | nan | nan | nan | Cerrado | 12.4 |
| 881744c3-27f7-3eee-b8b2-384a586095b3 | -5.15546 | -47.54472 | 2026-07-25 00:18:00 | TERRA_M-M | CIDELÂNDIA | MARANHÃO | Brasil | 2103257 | 21 | 33 | nan | nan | nan | Amazônia | 11.8 |
| 122361e4-c70b-31cc-9eca-a0033176fd80 | -9.86298 | -47.09695 | 2026-07-25 00:18:00 | TERRA_M-M | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 12.1 |
| 40998d5f-4d8d-3b54-92bd-f5608a7521ec | -6.56809 | -55.15319 | 2026-07-25 00:18:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 9e64be40-102c-3aa6-975c-6461aa83db50 | -9.99989 | -51.47192 | 2026-07-25 00:18:00 | TERRA_M-M | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 11.7 |
| f3437f21-2604-3dbb-92e5-1020cea5f2b1 | -7.89671 | -48.2743 | 2026-07-25 00:18:00 | TERRA_M-M | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 7.3 |
| c5b92cf9-c951-3810-baa5-71430e33e98b | -4.37216 | -47.77113 | 2026-07-25 00:18:00 | TERRA_M-M | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 210.1 |


[Clique aqui para ver as próximas entradas](README2.md)
