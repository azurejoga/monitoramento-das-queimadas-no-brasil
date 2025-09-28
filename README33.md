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

## Dados Diários - Página 33

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| c64147a5-a6da-3a53-b6c8-c4c7fc666b33 | -5.78529 | -42.8432 | 2025-09-28 04:04:00 | NPP-375D | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 4.5 |
| f323d9b2-28ba-335a-9a20-4bbb5de53408 | -5.75251 | -42.88462 | 2025-09-28 04:04:00 | NPP-375D | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 4.4 |
| 4f4ca013-c516-3b9b-98e2-9672525e414a | -4.79427 | -50.80972 | 2025-09-28 04:04:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9131d188-9249-35cd-8843-92efa386aa1a | -5.707 | -42.65926 | 2025-09-28 04:04:00 | NPP-375D | MIGUEL LEÃO | PIAUÍ | Brasil | 2206308 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 50519940-3c25-3a28-9e1a-41005574d898 | -6.06785 | -44.86311 | 2025-09-28 04:04:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e89a8bff-185f-3560-a7c8-593ac6d5d230 | -6.24221 | -44.48349 | 2025-09-28 04:04:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 1f5390ef-34e6-38ac-8265-4920d2d22993 | -5.79972 | -42.84539 | 2025-09-28 04:04:00 | NPP-375D | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 10.0 |
| 1c9daf5d-d411-367a-b38b-c70fb3d25f0f | -7.6318 | -43.80153 | 2025-09-28 04:04:00 | NPP-375D | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 03549821-2e0f-3c51-98de-ca83aa8406e7 | -4.14303 | -47.65117 | 2025-09-28 04:04:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6ae98a3b-f161-324e-812b-f49939037c0f | -7.38081 | -47.03504 | 2025-09-28 04:04:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 20.0 |
| 8a715b83-6439-303b-9bae-64758bb771b8 | -7.05543 | -46.41797 | 2025-09-28 04:04:00 | NPP-375D | NOVA COLINAS | MARANHÃO | Brasil | 2107258 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 07c8713c-df40-3e13-8b33-9de9f3c8f2b3 | -9.1122 | -46.67596 | 2025-09-28 04:04:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f7c0afa0-198b-394e-a856-f725434b1f25 | -8.107 | -49.085 | 2025-09-28 04:04:00 | NPP-375D | JUARINA | TOCANTINS | Brasil | 1711803 | 17 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 012a26e3-2521-32b2-ab4e-6a630e5de2fa | -7.49979 | -46.68138 | 2025-09-28 04:04:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 0cd2feda-c450-3e12-b615-7c1391af1dcf | -6.61111 | -44.94598 | 2025-09-28 04:04:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| dc78ff34-f9b9-33ad-b7ca-433f20d41d53 | -7.09939 | -44.23895 | 2025-09-28 04:04:00 | NPP-375D | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 04f1a39b-68d3-3bb6-ab6f-d819b47305ab | -5.73646 | -42.84032 | 2025-09-28 04:04:00 | NPP-375D | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 4.3 |
| 90cead07-1b94-3295-853e-c4e228e9b204 | -7.15488 | -45.51001 | 2025-09-28 04:04:00 | NPP-375D | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 00a74fed-1b6d-3598-9a34-faf9106d18e3 | -7.03088 | -45.19269 | 2025-09-28 04:04:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 74a8bd1c-bce2-3d05-b559-de18ff96fd88 | -6.83589 | -42.28983 | 2025-09-28 04:04:00 | NPP-375D | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 50531b2a-a995-36cd-a0a2-68283116eb8e | -6.95341 | -45.3993 | 2025-09-28 04:04:00 | NPP-375D | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 02c568d0-048d-3800-b3d7-9375d1ab7057 | -8.4937 | -44.72149 | 2025-09-28 04:04:00 | NPP-375D | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 14.8 |
| b938333d-e624-3c3b-9fc7-d7a8ba6efac6 | -3.21014 | -51.27386 | 2025-09-28 04:04:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| c94e8944-b901-3121-b65a-19674c0b7946 | -7.15901 | -45.51075 | 2025-09-28 04:04:00 | NPP-375D | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 9f13726b-706b-3bb5-aa2f-765bad359a38 | -8.28115 | -45.44676 | 2025-09-28 04:04:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 1118ce44-46f2-394f-951a-1c629b7ba926 | -5.76645 | -42.82294 | 2025-09-28 04:04:00 | NPP-375D | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| c03ed9fc-0f5f-3d10-ac82-0ad60d259095 | -8.27871 | -45.46099 | 2025-09-28 04:04:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 1f9e8922-65ce-349f-bd10-82c784105e44 | -7.04314 | -44.76993 | 2025-09-28 04:04:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 1651f0d2-ae8a-3d04-b865-40a0f3ec373a | -6.70679 | -42.77186 | 2025-09-28 04:04:00 | NPP-375D | FRANCISCO AYRES | PIAUÍ | Brasil | 2204105 | 22 | 33 | nan | nan | nan | Caatinga | 11.5 |
| 1fde8121-6d08-3428-ad15-7e2b49a7a955 | -5.73444 | -42.85284 | 2025-09-28 04:04:00 | NPP-375D | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 6.9 |
| 20b867e0-eba5-318b-a164-7fdaaa0a4887 | -6.58559 | -44.43669 | 2025-09-28 04:04:00 | NPP-375D | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ddb90927-6609-36ff-8d20-441a3031e9c1 | -7.75169 | -47.00919 | 2025-09-28 04:04:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| bb659fe2-135b-3c5a-9acd-3b45ef23f6c0 | -8.67853 | -49.9338 | 2025-09-28 04:04:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 14.6 |
| d72e9c5f-d029-3e15-84f1-e24b7b186658 | -5.75871 | -42.83997 | 2025-09-28 04:04:00 | NPP-375D | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 21.2 |
| eeb00d7e-55a6-3cc5-9148-5438c3ce5642 | -3.80145 | -41.56921 | 2025-09-28 04:04:00 | NPP-375D | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 4.2 |
| befc079d-de9f-3c93-85b2-827a050c6329 | -5.75567 | -42.88207 | 2025-09-28 04:04:00 | NPP-375D | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 3.4 |
| bdfd96dd-a702-323e-b562-c6c2a3d65495 | -5.95021 | -42.90266 | 2025-09-28 04:04:00 | NPP-375D | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 2da92f5f-e37f-36f6-a3fe-0d712d644454 | -8.28743 | -45.45873 | 2025-09-28 04:04:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 01f8183d-874b-31e4-b7ce-b90918526913 | -5.69867 | -42.62078 | 2025-09-28 04:04:00 | NPP-375D | MONSENHOR GIL | PIAUÍ | Brasil | 2206407 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 57a12c1c-21dc-3157-a0d4-5db25ac08ec9 | -5.73376 | -42.85704 | 2025-09-28 04:04:00 | NPP-375D | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 6.9 |
| 39748c2f-67ba-381a-bedd-a0d9c30c209a | -6.61256 | -45.08401 | 2025-09-28 04:04:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 6000b112-52af-337a-aa1c-9ee0c829c93c | -6.43044 | -43.07238 | 2025-09-28 04:04:00 | NPP-375D | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 5.1 |
| c8411d87-9a30-3246-bac0-016aa49f1d86 | -7.8729 | -44.55364 | 2025-09-28 04:04:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 65187deb-288d-33b4-ac50-1093a0002ea4 | -5.7029 | -42.61734 | 2025-09-28 04:04:00 | NPP-375D | MONSENHOR GIL | PIAUÍ | Brasil | 2206407 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| aed56e3a-face-361e-a921-e7406ee7513f | -5.76194 | -42.80555 | 2025-09-28 04:04:00 | NPP-375D | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 4.6 |
| 25b0b94f-f41d-3341-a713-3804ecb680da | -6.57312 | -45.09957 | 2025-09-28 04:04:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 30072c24-a0d5-3dc7-bd49-848541c61882 | -5.75188 | -42.81346 | 2025-09-28 04:04:00 | NPP-375D | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 4.1 |
| a7705b31-dc04-3fad-a65f-93c6c02d3d19 | -7.93752 | -45.68353 | 2025-09-28 04:04:00 | NPP-375D | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 043c61a7-e885-3efc-9ea8-480f0a12bd58 | -9.67935 | -44.52782 | 2025-09-28 04:04:00 | NPP-375D | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ff50c52c-1422-3f7f-b607-d9f48e3ee37f | -6.61781 | -45.07761 | 2025-09-28 04:04:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 0f96c3ff-ae2b-3712-bbfe-6bcb393c831c | -6.76655 | -41.75478 | 2025-09-28 04:04:00 | NPP-375D | INHUMA | PIAUÍ | Brasil | 2204709 | 22 | 33 | nan | nan | nan | Caatinga | 4.4 |
| 22629e08-05f6-3bcc-816b-68b24694fc72 | -5.28616 | -42.81143 | 2025-09-28 04:04:00 | NPP-375D | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 453c8b67-d604-343b-b194-6a80583b8511 | -9.29794 | -45.70339 | 2025-09-28 04:04:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| da47a705-52dd-39e1-a256-e7c6893ceb52 | -6.05462 | -44.86792 | 2025-09-28 04:04:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 096a332c-cb13-3d8e-a569-2500391341ce | -8.48444 | -47.81555 | 2025-09-28 04:04:00 | NPP-375D | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 2d6c5eb8-d2f1-374f-8d81-475e47973ad6 | -6.31449 | -43.45557 | 2025-09-28 04:04:00 | NPP-375D | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 3514a37b-76d6-3ba2-a5ce-d13db1596740 | -5.70845 | -42.60584 | 2025-09-28 04:04:00 | NPP-375D | MONSENHOR GIL | PIAUÍ | Brasil | 2206407 | 22 | 33 | nan | nan | nan | Caatinga | 3.9 |
| 9d673a74-6a27-3aa4-b50b-8d8b52dc7012 | -4.77526 | -41.04482 | 2025-09-28 04:04:00 | NPP-375D | PORANGA | CEARÁ | Brasil | 2311009 | 23 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 402eaf16-884e-3575-a64c-098b33668a6f | -9.07251 | -45.53879 | 2025-09-28 04:04:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| e19d2b4b-8e3f-3e8d-89e6-064a10ed327c | -5.82013 | -42.63126 | 2025-09-28 04:04:00 | NPP-375D | LAGOINHA DO PIAUÍ | PIAUÍ | Brasil | 2205540 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| be31b621-2f3e-3700-80cb-6a6c269fabef | -5.74762 | -42.81697 | 2025-09-28 04:04:00 | NPP-375D | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 4.1 |
| 09f4f6bb-eda8-3e84-8e7d-109c425c969d | -7.03047 | -44.77286 | 2025-09-28 04:04:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 42.8 |
| d4f597cd-9196-39d5-90f4-fecdc2690710 | -5.92384 | -43.80108 | 2025-09-28 04:04:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |
| ff899482-6097-36e6-b09f-40e0406f9e39 | -7.30434 | -42.95477 | 2025-09-28 04:04:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 807e6694-a956-334c-9f13-c970cea50eea | -4.6291 | -43.10888 | 2025-09-28 04:04:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 24803db6-d15f-3e0d-ac99-7d4de87bfdd9 | -6.31211 | -43.45704 | 2025-09-28 04:04:00 | NPP-375D | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 5aae783c-8702-38e5-9e4f-ea0ce62be130 | -5.75353 | -42.82618 | 2025-09-28 04:04:00 | NPP-375D | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 4.0 |
| 0db797cd-d2e1-3724-ba64-c464e27b1e12 | -6.40629 | -44.28957 | 2025-09-28 04:04:00 | NPP-375D | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 453eeb6b-65cf-3a71-befe-109bba365def | -5.80331 | -42.84606 | 2025-09-28 04:04:00 | NPP-375D | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 10.0 |
| c2aea36c-4380-3a0c-b8b2-7eeaa7bb437c | -4.87589 | -45.85642 | 2025-09-28 04:04:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 112ed543-5488-35cc-b8fa-0a41921dc914 | -6.34426 | -43.34515 | 2025-09-28 04:04:00 | NPP-375D | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 30a2b45a-b52f-3ad5-82e0-6fb3e13dfb36 | -5.30325 | -44.79049 | 2025-09-28 04:04:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| ceaff7ab-30ad-3daa-bb41-4cf692369681 | -9.29765 | -45.68126 | 2025-09-28 04:04:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 6f2b968c-0ae9-3b50-9696-2f34bde56839 | -7.81508 | -46.60771 | 2025-09-28 04:04:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| c86ff372-2626-353f-9352-8763448fb21e | -6.70541 | -44.58181 | 2025-09-28 04:04:00 | NPP-375D | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 95ea8c45-d18e-3b54-8f21-65919344b8ca | -9.10155 | -45.82911 | 2025-09-28 04:04:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 0be01b30-eed3-30f6-a327-e1cf3a485aa8 | -8.9054 | -46.09162 | 2025-09-28 04:04:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 512afb8c-3a81-38e6-a002-2545df333faf | -5.8103 | -42.82593 | 2025-09-28 04:04:00 | NPP-375D | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| e3c1b277-f0ab-331d-a402-64cb59fcacd8 | -6.08708 | -42.63551 | 2025-09-28 04:04:00 | NPP-375D | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| c11fb8c8-1dc2-3c8f-858c-cceae0e66892 | -5.62513 | -43.36369 | 2025-09-28 04:04:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| b3c2bd43-37ce-39a7-9b06-b69add946bde | -6.98936 | -43.78289 | 2025-09-28 04:04:00 | NPP-375D | MARCOS PARENTE | PIAUÍ | Brasil | 2206001 | 22 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 1c4ac43b-0d93-3f6e-9887-0142bda40827 | -7.62075 | -43.79932 | 2025-09-28 04:04:00 | NPP-375D | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 1d6e2d47-e151-3d0d-8945-f63942a52a7f | -7.78172 | -47.02412 | 2025-09-28 04:04:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 7.1 |
| a3126b62-f5ea-3416-8a4b-05393f72d925 | -5.28865 | -42.77329 | 2025-09-28 04:04:00 | NPP-375D | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 5b809f7a-5e07-3673-9911-c91267766bfe | -5.79613 | -42.84473 | 2025-09-28 04:04:00 | NPP-375D | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 27e82829-5597-306c-84e0-ca40d68c3628 | -3.80591 | -41.57314 | 2025-09-28 04:04:00 | NPP-375D | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 6.7 |
| a705afbc-7389-3cbe-bf15-741f10e1ff38 | -7.75947 | -45.74108 | 2025-09-28 04:04:00 | NPP-375D | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 85cac674-568c-385b-ab5f-5859a099d4f6 | -6.1276 | -41.79906 | 2025-09-28 04:04:00 | NPP-375D | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 8fd18ba3-9b3d-3dff-abdb-81015ac2fc66 | -5.16194 | -45.01783 | 2025-09-28 04:04:00 | NPP-375D | SÃO RAIMUNDO DO DOCA BEZERRA | MARANHÃO | Brasil | 2111631 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 359e7ae0-f825-3bfe-b7a1-59ae0f320244 | -6.77813 | -44.07692 | 2025-09-28 04:04:00 | NPP-375D | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 5.9 |
| fb27da96-fcb7-35be-9d24-6b40bee1604b | -3.91631 | -42.18669 | 2025-09-28 04:04:00 | NPP-375D | BATALHA | PIAUÍ | Brasil | 2201507 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| e85bf3d7-c40c-34bf-8ca5-82fe0e704751 | -9.777 | -47.76077 | 2025-09-28 04:04:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| dcb34c6d-e659-347c-b9c3-4b65bc48da03 | -8.86631 | -48.56734 | 2025-09-28 04:04:00 | NPP-375D | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1823d14a-3999-3331-9bd9-3c8cfa8a57d4 | -3.74604 | -39.52131 | 2025-09-28 04:04:00 | NPP-375D | ITAPAJÉ | CEARÁ | Brasil | 2306306 | 23 | 33 | nan | nan | nan | Caatinga | 0.4 |
| 45c4c72c-d128-3466-9890-af60a003fa86 | -7.55055 | -46.10078 | 2025-09-28 04:04:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 02c61148-0fa7-367c-9fca-2cde904174ee | -8.43546 | -46.87214 | 2025-09-28 04:04:00 | NPP-375D | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 12e117e7-94aa-3c21-815b-802dd83cb0db | -8.48936 | -47.81784 | 2025-09-28 04:04:00 | NPP-375D | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c1a8a61f-0f29-3bb7-bb10-6c0ca05fd87d | -5.39287 | -37.28997 | 2025-09-28 04:04:00 | NPP-375D | MOSSORÓ | RIO GRANDE DO NORTE | Brasil | 2408003 | 24 | 33 | nan | nan | nan | Caatinga | 1.6 |
| f0ac2756-974b-3999-81d2-d52abeae27bd | -8.49757 | -44.7221 | 2025-09-28 04:04:00 | NPP-375D | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 14.8 |
| 5fd0cc81-b789-3b1f-86b1-db9264492d7a | -7.75087 | -47.0138 | 2025-09-28 04:04:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |


[Clique aqui para ver as próximas entradas](README34.md)
