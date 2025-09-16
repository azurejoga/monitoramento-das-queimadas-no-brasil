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

## Dados Diários - Página 36

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 23975338-4ed2-3d5d-9fdb-811020725e6a | -5.77567 | -45.8991 | 2025-09-16 04:27:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 89867d17-0a4b-3526-9184-987f79d79e42 | -4.60088 | -43.31925 | 2025-09-16 04:27:00 | NPP-375D | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 10961d9f-87ca-341c-9d4f-4e0afa87ca01 | -6.83236 | -47.84702 | 2025-09-16 04:27:00 | NPP-375D | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| a8626404-61d9-3f2e-bef5-ccb2a20949d6 | -6.82262 | -47.86423 | 2025-09-16 04:27:00 | NPP-375D | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Cerrado | 0.3 |
| 7fbe52e5-149b-34b5-abba-34426dfa76a6 | -7.42222 | -44.85798 | 2025-09-16 04:27:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 3ecb3f94-ef72-36e3-a813-4843177edbba | -5.86261 | -45.86292 | 2025-09-16 04:27:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| e3cb5bed-15a9-3781-8dfe-e6fac5dab307 | -5.68552 | -45.07507 | 2025-09-16 04:27:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e3a7e3b6-1646-3a90-bf14-f53a99baae4a | -5.34433 | -44.83006 | 2025-09-16 04:27:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| e6d1c28e-dd55-3314-979e-2b190fab3914 | -5.19187 | -45.58708 | 2025-09-16 04:27:00 | NPP-375D | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d363e401-7f06-3ff5-9467-29443d6c69c7 | -5.93725 | -45.19025 | 2025-09-16 04:27:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 470ca51b-339d-388d-970b-7923be8ac176 | -6.25007 | -43.4632 | 2025-09-16 04:27:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| f3cbdc6c-9260-3617-adef-35925fde2af3 | -6.92255 | -44.79776 | 2025-09-16 04:27:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| eb9cfa30-c70d-3fe9-b8dd-8acd606ade54 | -5.94328 | -45.71145 | 2025-09-16 04:27:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 6e4a481a-a7e8-3624-bcc4-e16181f64270 | -5.11997 | -46.12973 | 2025-09-16 04:27:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e4dda7d6-3846-3d59-ad7b-645c71b0f9bf | -5.93274 | -45.71338 | 2025-09-16 04:27:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 6a1e847a-aff5-3c9d-abbc-2f6e5017a3a3 | -5.80557 | -44.86813 | 2025-09-16 04:27:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 4828f394-b527-3259-959d-a50cec5beba8 | -6.42593 | -43.31839 | 2025-09-16 04:27:00 | NPP-375D | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 32c46f14-2523-39fb-9251-0b21540d433e | -7.51427 | -44.66733 | 2025-09-16 04:27:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 2a24b590-3018-36f4-a96f-6791a4cccfc7 | -6.19068 | -43.47067 | 2025-09-16 04:27:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| c9a32eb2-635b-3597-a668-4328624c4ee9 | -7.36888 | -44.29575 | 2025-09-16 04:27:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 12057994-c38b-3b08-a1f8-85b71be8f8a3 | -3.1291 | -48.59311 | 2025-09-16 04:27:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| dfaad93a-007b-3c2b-b150-598ea5ce274e | -6.96621 | -44.44893 | 2025-09-16 04:27:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| f624970a-d3f8-3f02-8a95-0114f7ced743 | -3.73524 | -49.04452 | 2025-09-16 04:27:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 0b598031-43d4-3fe4-9695-fea74aeb993e | -7.2063 | -39.96382 | 2025-09-16 04:27:00 | NPP-375D | ARARIPE | CEARÁ | Brasil | 2301307 | 23 | 33 | nan | nan | nan | Caatinga | 2.1 |
| e939ad82-66c6-3b08-89ee-84737df7a5fa | -6.46934 | -46.00444 | 2025-09-16 04:27:00 | NPP-375D | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 8dd04858-ff91-3458-9c42-4af495cc8fc1 | -6.96737 | -44.44142 | 2025-09-16 04:27:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 0488dcfb-08d5-366e-a9a7-6b0f8e2f9954 | -6.00008 | -43.70637 | 2025-09-16 04:27:00 | NPP-375D | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 0a8549dc-a49e-3edf-9405-9c47a04b3ddc | -6.15711 | -43.66865 | 2025-09-16 04:27:00 | NPP-375D | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 7601b9a6-bb01-3984-9406-073d2d95149b | -4.01249 | -43.23406 | 2025-09-16 04:27:00 | NPP-375D | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 8fd699f6-3fb5-319b-84ec-cd560041d9f5 | -6.52 | -51.18994 | 2025-09-16 04:27:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| edfb71ea-b79f-3984-9150-70305b1f388e | -7.08527 | -44.55384 | 2025-09-16 04:27:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| c7a37e82-2eb7-334f-ac41-c7dd8e0e3d03 | -6.90373 | -44.55768 | 2025-09-16 04:27:00 | NPP-375D | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| f05a707d-bec1-31e9-a2c3-58c3c824f177 | -6.26013 | -43.46881 | 2025-09-16 04:27:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 5c1a23c3-4a01-3bff-a817-b95e9e143f88 | -5.66643 | -43.31826 | 2025-09-16 04:27:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 91b8fc01-b5c5-3cfe-9c19-0efba6a4b6f2 | -6.24341 | -44.38267 | 2025-09-16 04:27:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| a62f51e2-d123-3b4e-8bee-083cefa168b9 | -6.96663 | -44.53696 | 2025-09-16 04:27:00 | NPP-375D | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| af366ede-fde3-317e-9dbf-079493317044 | -5.52751 | -45.32829 | 2025-09-16 04:27:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 2554025a-9498-3940-bea8-3fc550800bfe | -5.77555 | -43.92146 | 2025-09-16 04:27:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 0a4ee59c-4d69-3692-8290-afae9f94e959 | -5.14158 | -45.39029 | 2025-09-16 04:27:00 | NPP-375D | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d7056d6b-dc01-38c0-9014-7b042fdaff1e | -4.48772 | -48.10976 | 2025-09-16 04:27:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f7989070-cab6-38a6-9ff0-f14f87802995 | -7.06385 | -44.16882 | 2025-09-16 04:27:00 | NPP-375D | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| c1edd1d1-82d4-3f0d-9d96-ffe96b85defb | -6.89429 | -43.88679 | 2025-09-16 04:27:00 | NPP-375D | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 5e5e8657-4a01-398c-b4b3-8815a791d346 | -5.55979 | -44.96863 | 2025-09-16 04:27:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 555462eb-c4f6-3398-8e70-533107455c0f | -5.65183 | -45.80514 | 2025-09-16 04:27:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 19fe90af-9a3a-3dbf-8016-e3a17937653e | -5.79126 | -45.9264 | 2025-09-16 04:27:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 561fa345-67a1-32ea-a1b1-efbfaf0f0db9 | -6.97538 | -44.54143 | 2025-09-16 04:27:00 | NPP-375D | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 26d8048b-ee3b-3630-b3a0-d3e118e8bb63 | -5.91833 | -45.72567 | 2025-09-16 04:27:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 24e64d3d-cdeb-3274-a542-34381ae2b0b2 | -5.55643 | -44.96809 | 2025-09-16 04:27:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 52c5120a-8b68-31f0-9be2-f76192b655c5 | -5.11942 | -46.13319 | 2025-09-16 04:27:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 522f6f59-f102-3aa1-a096-f837c5d4ff3c | -5.79599 | -44.86303 | 2025-09-16 04:27:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 503b9281-6fae-3866-89c2-d5f37bf68425 | -6.66012 | -44.6452 | 2025-09-16 04:27:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| dcf799a4-e525-331b-a5ea-df8764c067a7 | -5.55754 | -44.96098 | 2025-09-16 04:27:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 364fe441-0ec2-3de4-a6e1-7c4350877b6d | -6.17271 | -46.81301 | 2025-09-16 04:27:00 | NPP-375D | LAJEADO NOVO | MARANHÃO | Brasil | 2105989 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 304946eb-91d8-3a17-9a15-c20fb4d1b966 | -2.646 | -48.05357 | 2025-09-16 04:27:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 56100404-bfb7-3e01-833f-9fca233ff90f | -7.56428 | -43.9553 | 2025-09-16 04:27:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 1c2ff4a8-0005-3f46-9fca-81e03103c7b4 | -5.77513 | -45.90256 | 2025-09-16 04:27:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 0cf3cdc8-a6db-3a94-8488-c872906f3a4d | -7.32894 | -44.05824 | 2025-09-16 04:27:00 | NPP-375D | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 553db8f3-e7ab-3567-8d15-18052577fa37 | -7.1656 | -44.35106 | 2025-09-16 04:27:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| fead444f-a2be-384a-b34b-92bed2d9c317 | -6.63187 | -44.73839 | 2025-09-16 04:27:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| ad37c4b1-a1da-3570-88eb-f52811700e1d | -2.29645 | -48.57458 | 2025-09-16 04:27:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 21698920-4f20-3ac7-9c2a-bd08cacb2d9a | -2.26082 | -47.847 | 2025-09-16 04:27:00 | NPP-375D | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 6b572cdb-91f4-3cf0-bb3a-090e1974832e | -7.27774 | -46.60608 | 2025-09-16 04:27:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 3c4a6559-ae0e-3127-a4e1-35251f7ecc1d | -5.76126 | -43.69086 | 2025-09-16 04:27:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 1e3121f6-4fc4-3ac7-b97f-66f8af4648d2 | -5.98508 | -45.79286 | 2025-09-16 04:27:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 75d530d5-e115-31b8-8ad4-34f6d6499897 | -5.98298 | -45.84952 | 2025-09-16 04:27:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| fb974177-45f1-3b8a-aaba-e7b55b60d75e | -4.06493 | -46.93867 | 2025-09-16 04:27:00 | NPP-375D | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6d64d10d-62e3-3a6e-8bcb-e8fe6edfc66e | -7.37117 | -44.3507 | 2025-09-16 04:27:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 947865b0-ea2d-30a3-a738-83a9c217fd2c | -4.59736 | -43.3187 | 2025-09-16 04:27:00 | NPP-375D | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 9855d170-9f07-350a-a4db-56eb06cca4a1 | -6.34878 | -44.31529 | 2025-09-16 04:27:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| f4320d08-7b1c-389b-af45-5fcad74b5b63 | -6.16598 | -48.10408 | 2025-09-16 04:27:00 | NPP-375D | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 8f249a25-5514-3099-b8e1-3c1d0cda4b48 | -6.00129 | -43.69857 | 2025-09-16 04:27:00 | NPP-375D | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 45c7a71a-d24f-3cc1-9c1e-a01b6808e289 | -7.26942 | -46.59406 | 2025-09-16 04:27:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 9.7 |
| d51c4c07-0156-3db6-997d-85e963890755 | -6.27476 | -44.00233 | 2025-09-16 04:27:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 13124464-e0da-3665-acc8-a085d56fe2a5 | -6.52644 | -41.83273 | 2025-09-16 04:27:00 | NPP-375D | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| a5167440-97fd-3b29-bbc3-96200c7ee8d3 | -6.62506 | -44.73735 | 2025-09-16 04:27:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 6eff98ce-a25d-323c-afbd-e2f90322564a | -6.44576 | -43.3087 | 2025-09-16 04:27:00 | NPP-375D | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d94ca46e-5850-3406-99f2-4df05ea817a0 | -6.41587 | -45.84994 | 2025-09-16 04:27:00 | NPP-375D | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| b0133e13-b045-3c79-b164-d467e667538f | -5.90391 | -45.73053 | 2025-09-16 04:27:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| ee3910c6-e6e5-3259-9e6e-c7c1063d7d9c | -6.44873 | -43.31342 | 2025-09-16 04:27:00 | NPP-375D | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 616c5e3c-3d4a-3efe-a2b0-610e253a8bdf | -2.64381 | -44.64701 | 2025-09-16 04:27:00 | NPP-375D | BACURITUBA | MARANHÃO | Brasil | 2101350 | 21 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 45c9d260-bffe-3386-96d6-24ab3c103a70 | -4.74122 | -50.94047 | 2025-09-16 04:27:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 0fdb5835-77e2-34f3-8d86-d3ea30631b0a | -4.17452 | -48.56932 | 2025-09-16 04:27:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a569c94b-46b0-3e09-a72d-80762b7a1cda | -3.13836 | -44.42851 | 2025-09-16 04:27:00 | NPP-375D | SANTA RITA | MARANHÃO | Brasil | 2110203 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 37b82ba8-be20-394a-bee9-914e0efac8af | -5.54971 | -44.96704 | 2025-09-16 04:27:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| b1ac45f5-5cc0-3148-a973-3bff74405270 | -7.13883 | -47.98145 | 2025-09-16 04:27:00 | NPP-375D | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 467355aa-e117-3537-b525-0c6d9a1906d5 | -5.78287 | -45.89668 | 2025-09-16 04:27:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| c08d1956-dff9-3812-9df3-d774f1a18288 | -6.18749 | -45.12777 | 2025-09-16 04:27:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| baaddfbf-6488-3b86-bd5e-1828e2b2d583 | -7.27164 | -46.60154 | 2025-09-16 04:27:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d6b9e423-7294-3f20-9d98-ea03bdabecdf | -7.00176 | -44.57568 | 2025-09-16 04:27:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 5d14643c-2da4-3863-a702-bf7ea0e23647 | -7.68908 | -44.48268 | 2025-09-16 04:27:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f29eb2c2-b1b2-3278-a88c-774c17bfd2c2 | -5.89452 | -45.74685 | 2025-09-16 04:27:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 0cff9675-0f85-380b-9d78-116e987b6d69 | -5.54599 | -46.41038 | 2025-09-16 04:27:00 | NPP-375D | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| e1b666a2-cd73-3176-a90b-898494fed49a | -7.20936 | -44.38875 | 2025-09-16 04:27:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f1c6c79e-cb79-3512-8058-594e5f19c4f8 | -5.97081 | -45.86186 | 2025-09-16 04:27:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 5a15da74-21f8-3236-ba54-5c5504d7aff9 | -5.77445 | -43.93598 | 2025-09-16 04:27:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 7339040e-ac1d-3c84-938f-7dc77c487cb8 | -5.98243 | -45.853 | 2025-09-16 04:27:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 4763ad34-be6f-3322-9c18-f952f4b9a870 | -5.34598 | -44.81939 | 2025-09-16 04:27:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 62abf647-b5c3-3807-b7b1-baab3776199c | -6.87774 | -45.62134 | 2025-09-16 04:27:00 | NPP-375D | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 525718c7-93ea-3702-af18-6db685ff2204 | -3.81332 | -41.555 | 2025-09-16 04:27:00 | NPP-375D | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 6.8 |
| e96ec7d7-309f-32c0-b55f-21a008bf96cf | -7.42215 | -40.08046 | 2025-09-16 04:27:00 | NPP-375D | BODOCÓ | PERNAMBUCO | Brasil | 2602001 | 26 | 33 | nan | nan | nan | Caatinga | 1.2 |


[Clique aqui para ver as próximas entradas](README37.md)
