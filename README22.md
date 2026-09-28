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
| b25b228c-cdad-3928-a25b-81515cac570b | -11.78468 | -48.31639 | 2026-09-28 03:49:00 | NOAA-20 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 0d9bb19d-f043-3aa5-9c07-b5244ea36334 | -9.31941 | -45.3665 | 2026-09-28 03:49:00 | NOAA-20 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 97be62c8-be32-34a2-bd49-38db4829f959 | -9.07534 | -43.13032 | 2026-09-28 03:49:00 | NOAA-20 | JUREMA | PIAUÍ | Brasil | 2205532 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| ecf6e0b3-6fb9-3b76-882b-e9713e3a0344 | -8.13673 | -44.45111 | 2026-09-28 03:49:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 16bc86d6-40f4-31a9-be35-5784366b0cc8 | -10.256 | -44.6167 | 2026-09-28 03:49:00 | NOAA-20 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| d3f0d02d-db4c-3368-ad1a-d29aa2d48eb3 | -11.19041 | -44.80803 | 2026-09-28 03:49:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 123.2 |
| 74195c7c-862a-3fa9-aa5b-fc4f9213d149 | -13.07604 | -47.44082 | 2026-09-28 03:49:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| b89ef1c1-3d0f-308f-92a5-e70e16c3d346 | -9.98469 | -50.13887 | 2026-09-28 03:49:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| fdd6b16c-bda7-33bf-a488-3c3b9811908f | -11.18961 | -44.81286 | 2026-09-28 03:49:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 28.5 |
| 1e5b0feb-0a91-35eb-a47f-9baf5ba056d3 | -8.23169 | -45.44173 | 2026-09-28 03:49:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 991dda72-27f8-35fd-84c8-fa0c3a940b20 | -12.10506 | -45.21655 | 2026-09-28 03:49:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 961603db-dfe1-38ad-a35d-aecabf82e1f1 | -7.7116 | -39.34893 | 2026-09-28 03:49:00 | NOAA-20 | SERRITA | PERNAMBUCO | Brasil | 2614006 | 26 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 476ad8b3-9ba0-3a98-b7a0-c32cff9de7c0 | -6.76782 | -45.37349 | 2026-09-28 03:49:00 | NOAA-20 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 5867e4eb-bbed-34f3-984f-f90b4cacf90d | -8.43716 | -44.87488 | 2026-09-28 03:49:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 91a47827-bc73-3cfc-92f0-abf47c64a411 | -9.99313 | -50.13349 | 2026-09-28 03:49:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 7810a970-eddb-32b1-99ee-bb2e3408b816 | -7.3778 | -47.02274 | 2026-09-28 03:49:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 7d77b414-adfb-3ca0-84ab-c425e7cb10ac | -8.58651 | -39.44549 | 2026-09-28 03:49:00 | NOAA-20 | CURAÇÁ | BAHIA | Brasil | 2909901 | 29 | 33 | nan | nan | nan | Caatinga | 0.9 |
| f3685a8d-ba51-3b36-8cd1-0e235003fdfe | -7.34022 | -42.07897 | 2026-09-28 03:49:00 | NOAA-20 | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 0d35874b-dfde-3cfc-b167-6a5009256d2d | -9.83041 | -44.94147 | 2026-09-28 03:49:00 | NOAA-20 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 881696b2-54c3-331e-925e-b9e5e610ef05 | -11.18906 | -44.81581 | 2026-09-28 03:49:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 28.5 |
| 741f32f9-7046-3109-a2ad-e3daf180e516 | -13.74101 | -41.28254 | 2026-09-28 03:49:00 | NOAA-20 | ITUAÇU | BAHIA | Brasil | 2917201 | 29 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 57e32698-5014-33b2-9c87-99835ecfa1ca | -11.69417 | -50.60096 | 2026-09-28 03:49:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| edbde6eb-8f73-3fad-b938-393e948950a4 | -12.60291 | -38.04433 | 2026-09-28 03:49:00 | NOAA-20 | CAMAÇARI | BAHIA | Brasil | 2905701 | 29 | 33 | nan | nan | nan | Mata Atlântica | 2.8 |
| cb1e5dbc-932a-3a9a-8371-fb1ec768d2aa | -10.26093 | -44.61804 | 2026-09-28 03:49:00 | NOAA-20 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 60d49f2a-4ce1-3c6c-8009-0127dd0faccb | -13.56603 | -46.36303 | 2026-09-28 03:49:00 | NOAA-20 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 4b8ea32c-b6a7-3925-aceb-299af110d3e2 | -7.71022 | -39.34707 | 2026-09-28 03:49:00 | NOAA-20 | SERRITA | PERNAMBUCO | Brasil | 2614006 | 26 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 45b8f626-2921-3db2-9984-f6f434ae779d | -11.7015 | -44.53745 | 2026-09-28 03:49:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 407812f8-f142-3409-a607-ee801cb9d6e3 | -10.21238 | -50.01143 | 2026-09-28 03:49:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 57135b24-71f2-32ab-ba18-f7968ba3cd9b | -13.55942 | -46.36869 | 2026-09-28 03:49:00 | NOAA-20 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 85274bab-34d0-3b37-bd59-efd6e7dc2ffa | -8.36396 | -45.46231 | 2026-09-28 03:49:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 70cce6db-6da6-3460-971d-e45a5c787117 | -11.78271 | -48.32623 | 2026-09-28 03:49:00 | NOAA-20 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| cd005728-0020-32bf-b264-9dd0f8acb1ad | -12.68392 | -47.32778 | 2026-09-28 03:49:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| f0d293a0-cdd4-3950-822a-729ec2c3013e | -11.68213 | -44.53365 | 2026-09-28 03:49:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 19b97fe2-fd9a-300c-9fd8-52ca43c4aa74 | -10.21956 | -50.00176 | 2026-09-28 03:49:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| f5b21d66-e514-37cb-99b8-8a3d9e05b0d2 | -9.8244 | -45.26354 | 2026-09-28 03:49:00 | NOAA-20 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 948b0159-5e9e-3d7f-91fc-78f46be82715 | -8.45046 | -44.68338 | 2026-09-28 03:49:00 | NOAA-20 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 3.4 |
| f634d364-e9ad-3841-9175-254a34cd0182 | -11.19406 | -44.81671 | 2026-09-28 03:49:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 28.5 |
| 682bce95-ac63-3949-8f92-3fe055b1309c | -7.28589 | -44.31457 | 2026-09-28 03:49:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 662a6e85-9924-397b-b9d1-e7bfb4205628 | -8.369 | -45.46895 | 2026-09-28 03:49:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 9f98838e-609e-3a0d-8db2-ca6d76245518 | -7.3777 | -42.11855 | 2026-09-28 03:49:00 | NOAA-20 | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 99b08f50-b927-3939-b33e-986871e4636c | -9.77283 | -44.83878 | 2026-09-28 03:49:00 | NOAA-20 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 5e31221a-213a-3c1d-af6c-2d2d96d5dd3f | -8.4156 | -44.87397 | 2026-09-28 03:49:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 9cf982f5-d72a-3c48-98f2-5b907216d9d6 | -10.20704 | -49.99203 | 2026-09-28 03:49:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 8e52862b-d768-32de-990f-99864d2a697f | -7.7079 | -39.34827 | 2026-09-28 03:49:00 | NOAA-20 | SERRITA | PERNAMBUCO | Brasil | 2614006 | 26 | 33 | nan | nan | nan | Caatinga | 1.0 |
| b62f2707-8921-3305-ac8f-04dc56246d91 | -9.13253 | -45.60925 | 2026-09-28 03:49:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 9c42c0cb-132a-387f-9682-87cbc4ae902f | -11.44625 | -44.92966 | 2026-09-28 03:49:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 3938261c-1d70-335c-b154-414164be0bb9 | -11.37841 | -43.41265 | 2026-09-28 03:49:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 4b0f052a-7cd3-3ac7-9d79-297a214f46b6 | -11.18931 | -44.81377 | 2026-09-28 03:49:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 123.2 |
| 2d557984-bbca-3f33-9553-78fccdb05076 | -10.89256 | -50.69234 | 2026-09-28 03:49:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 1cdbf277-5fae-378e-a06e-8c7f54d3782b | -8.96307 | -44.16095 | 2026-09-28 03:49:00 | NOAA-20 | SANTA LUZ | PIAUÍ | Brasil | 2209302 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| e08f0a24-e178-3388-bdfb-63e4362676f7 | -11.18432 | -44.81286 | 2026-09-28 03:49:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 123.2 |
| dbe90c79-9ef5-3453-bcf5-9eadba8ef73e | -10.00016 | -50.13502 | 2026-09-28 03:49:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| d4b5ec3f-b049-35b1-b943-b99c108f6e9d | -7.38482 | -47.01918 | 2026-09-28 03:49:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 2a1d4af5-58f3-38fc-9c99-5c142ce6d85a | -11.44842 | -44.91815 | 2026-09-28 03:49:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 7c2c31f5-f0f2-396e-a4e5-db7720caef9f | -9.13449 | -47.98513 | 2026-09-28 03:49:00 | NOAA-20 | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 44c5978f-1b6a-3237-ad74-6db8af4a5ab1 | -8.36883 | -45.46661 | 2026-09-28 03:49:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 372fdeaf-2817-3ccc-939c-3a0dca409e50 | -11.18544 | -44.80705 | 2026-09-28 03:49:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 123.2 |
| a5e9d36e-c003-3333-9054-4258440938fe | -13.45002 | -46.31847 | 2026-09-28 03:49:00 | NOAA-20 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e917a3a7-c17e-3ca8-82a4-fe7c5c65c112 | -7.33428 | -42.08701 | 2026-09-28 03:49:00 | NOAA-20 | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 48511f9f-8ac2-31dd-b727-5dcc35f9646c | -12.74135 | -47.7888 | 2026-09-28 03:49:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| c2223e08-e142-37f5-8036-f7dcfd2533f8 | -9.32749 | -45.38266 | 2026-09-28 03:49:00 | NOAA-20 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 28507417-ffc6-3c3b-9b02-7667bfa78821 | -12.31464 | -46.41061 | 2026-09-28 03:49:00 | NOAA-20 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 578b23b0-9707-36ae-9281-fc9e46a4b7ae | -10.12331 | -45.1408 | 2026-09-28 03:49:00 | NOAA-20 | SÃO GONÇALO DO GURGUÉIA | PIAUÍ | Brasil | 2209757 | 22 | 33 | nan | nan | nan | Cerrado | 7.1 |
| c9bf8a02-5060-30d0-9343-2bdef25c6e84 | -10.9141 | -43.86523 | 2026-09-28 03:49:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 5e53bf6b-76ad-39f2-a2cf-23cfa8d3dcca | -12.10893 | -45.21767 | 2026-09-28 03:49:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c98df638-e7fc-3968-9a22-bc99c1b6055e | -9.14961 | -45.6386 | 2026-09-28 03:49:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 29.0 |
| 22c0fd65-b539-3b34-9140-ba17fd3efeb2 | -6.6627 | -55.1112 | 2026-09-28 03:50:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 48.9 |
| 8b432acb-d794-35ab-b8d1-49ad81a0cf8c | -6.0741 | -47.2703 | 2026-09-28 03:50:00 | GOES-19 | RIBAMAR FIQUENE | MARANHÃO | Brasil | 2109551 | 21 | 33 | nan | nan | nan | Cerrado | 136.0 |
| be449cff-6ee9-3683-9915-45009f783a43 | -11.1958 | -44.8269 | 2026-09-28 03:50:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 116.3 |
| 58d937fc-e793-3ee9-b9fb-62a53225aad4 | -6.0739 | -47.2922 | 2026-09-28 03:50:00 | GOES-19 | RIBAMAR FIQUENE | MARANHÃO | Brasil | 2109551 | 21 | 33 | nan | nan | nan | Cerrado | 112.0 |
| 33a1f7be-c813-3907-bfe4-a0a2c1ac1dbe | -3.1471 | -54.0849 | 2026-09-28 03:50:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 51.6 |
| e911bc40-839e-33d0-8acb-4d956535ca6f | -11.1966 | -44.7805 | 2026-09-28 03:50:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 114.7 |
| 0281f779-a95d-3b2d-a71c-19c4316103bb | -9.1584 | -61.4082 | 2026-09-28 03:50:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 73.3 |
| ceae054a-d924-3248-aa12-e72d8a77491a | -9.1511 | -45.6344 | 2026-09-28 03:50:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 69.4 |
| 4dedd907-cb1f-3c01-a4d1-370f29be2542 | -3.4287 | -48.3441 | 2026-09-28 03:50:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 68.3 |
| b2c649e3-505f-3f3f-9f01-3a00ff28b8b0 | -11.1775 | -44.7832 | 2026-09-28 03:50:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 124.3 |
| a3505389-6db7-3ef1-af8d-ec117f0eb0ed | -11.1771 | -44.8064 | 2026-09-28 03:50:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 305.1 |
| ed3cd3bc-5a5c-3e5b-a515-349754097354 | -11.1767 | -44.8296 | 2026-09-28 03:50:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 78.6 |
| 8be75c7a-9d61-3203-818d-288ca3734615 | -10.8238 | -60.744 | 2026-09-28 03:50:00 | GOES-19 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 61.2 |
| 96df9235-617b-3a3a-8d84-fd0384138806 | -9.177 | -61.4073 | 2026-09-28 03:50:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 54.5 |
| b560f17b-e558-33c7-897d-5bea5242c43d | -11.1962 | -44.8037 | 2026-09-28 03:50:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 342.5 |
| 01896dcb-d48e-3a79-a13f-1cae426b0cfe | -3.4102 | -48.3448 | 2026-09-28 03:50:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 80.8 |
| 88ec5885-60fb-34e8-adb6-75f6c70704a5 | -18.1151 | -44.3745 | 2026-09-28 03:50:00 | GOES-19 | AUGUSTO DE LIMA | MINAS GERAIS | Brasil | 3104809 | 31 | 33 | nan | nan | nan | Cerrado | 79.6 |
| 84cd39a8-221e-31db-9f76-b918ee3bd3b7 | -15.17475 | -46.16643 | 2026-09-28 03:51:00 | NOAA-20 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| b7eb918f-c7df-325f-b9a9-abf94485a882 | -16.39468 | -42.56744 | 2026-09-28 03:51:00 | NOAA-20 | PADRE CARVALHO | MINAS GERAIS | Brasil | 3146255 | 31 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 6b037f67-d2d3-3c3c-a46d-6ed17c977ab3 | -15.14945 | -43.62747 | 2026-09-28 03:51:00 | NOAA-20 | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Caatinga | 1.6 |
| db6e26d5-f090-3b2a-b708-6fde8729a4d4 | -15.13228 | -43.62408 | 2026-09-28 03:51:00 | NOAA-20 | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Caatinga | 1.9 |
| c8752ff0-e51b-3eb1-bc12-da9b2cdc4356 | -15.16718 | -46.16125 | 2026-09-28 03:51:00 | NOAA-20 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 731e4f6f-14d2-33be-9ab4-3dd53301e9bb | -17.82689 | -44.39721 | 2026-09-28 03:51:00 | NOAA-20 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 240b7dfc-f95e-3e28-832e-b11809ca6d67 | -19.10301 | -43.95805 | 2026-09-28 03:51:00 | NOAA-20 | SANTANA DE PIRAPAMA | MINAS GERAIS | Brasil | 3158508 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 3e6d5024-96fd-31fc-a7fd-ef7c98b07365 | -14.79686 | -45.9613 | 2026-09-28 03:51:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 6c683c89-c860-3a42-9fce-448920ede36f | -16.7859 | -39.41836 | 2026-09-28 03:51:00 | NOAA-20 | PORTO SEGURO | BAHIA | Brasil | 2925303 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 3848fd07-34de-350f-9576-0cd469b90796 | -15.15926 | -43.59886 | 2026-09-28 03:51:00 | NOAA-20 | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 6e0acb6e-7bfc-33ef-8b44-f05eacaa9a1b | -14.52254 | -48.30671 | 2026-09-28 03:51:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 19236815-0fab-3de2-ab69-721fb3d92ad8 | -16.39173 | -42.56136 | 2026-09-28 03:51:00 | NOAA-20 | PADRE CARVALHO | MINAS GERAIS | Brasil | 3146255 | 31 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 50bc69a2-9526-34aa-81ae-71795f3f6afc | -15.16652 | -46.16468 | 2026-09-28 03:51:00 | NOAA-20 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 4.5 |
| b807c923-f84d-3df0-b937-ca9a0bd56d6f | -14.90479 | -49.49514 | 2026-09-28 03:51:00 | NOAA-20 | ITAPACI | GOIÁS | Brasil | 5210901 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e34d365e-d450-34b1-a959-2235b877665b | -18.54876 | -43.58469 | 2026-09-28 03:51:00 | NOAA-20 | SERRO | MINAS GERAIS | Brasil | 3167103 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 99bec6d9-d1dd-3e1e-a2f3-441ec274f7da | -14.80189 | -45.96236 | 2026-09-28 03:51:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 51d90ec0-2080-3419-ac4f-99c4ee400d1c | -15.82707 | -42.56601 | 2026-09-28 03:51:00 | NOAA-20 | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |


[Clique aqui para ver as próximas entradas](README23.md)
