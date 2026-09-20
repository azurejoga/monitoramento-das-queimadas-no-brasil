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

## Dados Diários - Página 51

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| e20778bd-7183-322a-bb14-6450650c5257 | -6.35661 | -43.3641 | 2026-09-20 04:38:00 | NOAA-20 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| ca57b591-5753-38d9-8f7b-2dc0a4330192 | -3.81349 | -50.76308 | 2026-09-20 04:38:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d97afe7e-a2c3-3d35-8150-b9a39ee7cb09 | -3.00312 | -54.16569 | 2026-09-20 04:38:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| d8bd4ff8-9e8f-3547-a27c-7c642fd0ff0a | -6.29818 | -47.615 | 2026-09-20 04:38:00 | NOAA-20 | TOCANTINÓPOLIS | TOCANTINS | Brasil | 1721208 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 0ca26cae-caf4-394d-af03-ad3713de3fcc | -2.87866 | -57.81099 | 2026-09-20 04:38:00 | NOAA-20 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 7.6 |
| caa64de1-e600-3fad-97e1-6f5ef49f8097 | -5.82805 | -47.77473 | 2026-09-20 04:38:00 | NOAA-20 | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| b354c880-de8b-3836-93ae-7ffbb3ada01f | -5.85472 | -51.93636 | 2026-09-20 04:38:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| cb584b87-b938-31fc-9ef9-7dd3fa4cfe4a | -5.8877 | -46.58979 | 2026-09-20 04:38:00 | NOAA-20 | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ea219761-229f-3b5e-a1fa-72ff1941c03c | -5.76126 | -43.69617 | 2026-09-20 04:38:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 24af1dbc-70f6-3006-b62d-a0e0171a36cc | -3.08205 | -48.67572 | 2026-09-20 04:38:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 6f37f2c9-c1ad-32b1-af8b-f84da41f1a8b | -3.73629 | -51.81826 | 2026-09-20 04:38:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 9.6 |
| 54a6e2d6-fe50-398e-a4dd-aad36a195ab4 | -3.73549 | -51.82307 | 2026-09-20 04:38:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 9.6 |
| 8795d856-7a57-3da1-bf0a-901a22c8b186 | -4.68313 | -46.39692 | 2026-09-20 04:38:00 | NOAA-20 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 6d4cb6c8-41b8-373b-8608-1aa119d951d4 | -4.29224 | -48.62942 | 2026-09-20 04:38:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| f8cc30e4-cc27-3bf1-a50e-de1cce3e877e | -6.30648 | -47.62697 | 2026-09-20 04:38:00 | NOAA-20 | TOCANTINÓPOLIS | TOCANTINS | Brasil | 1721208 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 482f241c-c8ce-30bf-953c-758bd2deee99 | -0.83902 | -48.57846 | 2026-09-20 04:38:00 | NOAA-20 | SALVATERRA | PARÁ | Brasil | 1506302 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 467456ed-a776-335d-8024-4cb244d67b77 | -6.54347 | -44.93073 | 2026-09-20 04:38:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 85c4d67e-9ac2-3aa5-8122-bbd849e22a23 | -3.00238 | -54.17027 | 2026-09-20 04:38:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| bdbe9547-95d4-3286-a407-06af111ca403 | -6.35707 | -43.39292 | 2026-09-20 04:38:00 | NOAA-20 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 463d5b39-14c7-3fac-b2c2-c4063e52ecc6 | -4.68153 | -40.14531 | 2026-09-20 04:38:00 | NOAA-20 | CATUNDA | CEARÁ | Brasil | 2303659 | 23 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 51489aba-6e06-39ed-a217-029f72d8a0f9 | -3.15024 | -47.69303 | 2026-09-20 04:38:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| aa7668c2-50a5-3a15-9be7-23bf9d4e8c00 | -3.34083 | -57.86332 | 2026-09-20 04:38:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 8e4d6fbd-6d79-3be3-85ab-536b9575944a | -6.7391 | -45.46811 | 2026-09-20 04:38:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| df812f5c-71e5-386f-991b-30cd48172788 | -2.87795 | -57.81515 | 2026-09-20 04:38:00 | NOAA-20 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 7.6 |
| b77e8ab5-9c44-3ca5-9745-63d7aa86b753 | -3.13466 | -44.47669 | 2026-09-20 04:38:00 | NOAA-20 | ANAJATUBA | MARANHÃO | Brasil | 2100709 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 98a55387-52ca-3831-8ef2-71701e1fda0a | -3.68853 | -60.57743 | 2026-09-20 04:38:00 | NOAA-20 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 02cd1114-be14-3089-ba10-956d4cd3d1c1 | -6.30208 | -47.63338 | 2026-09-20 04:38:00 | NOAA-20 | TOCANTINÓPOLIS | TOCANTINS | Brasil | 1721208 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| cb27ee4f-8549-3c29-9225-f3852bf28271 | -5.73571 | -51.7643 | 2026-09-20 04:38:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| cd5b4bcc-cd7b-383f-9c40-6d53d9badd36 | -5.9203 | -42.68092 | 2026-09-20 04:38:00 | NOAA-20 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 7784af3d-26d8-3a33-977f-d5e594391524 | -2.30153 | -48.54965 | 2026-09-20 04:38:00 | NOAA-20 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| a71aa78e-41ce-32d5-b92f-5911a5627cae | -3.51924 | -50.79784 | 2026-09-20 04:38:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 76237e95-9fcc-39f7-aca2-1290a45a0a99 | -2.82086 | -54.71735 | 2026-09-20 04:38:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d106a331-e91a-3b5a-86e7-e5d9f108cba1 | -3.72435 | -60.61663 | 2026-09-20 04:38:00 | NOAA-20 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| fff0fa76-4394-374d-8902-3b827a76dd98 | -5.23024 | -47.58084 | 2026-09-20 04:38:00 | NOAA-20 | IMPERATRIZ | MARANHÃO | Brasil | 2105302 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a20fe233-dc75-30d5-98db-9f923e98ca99 | -3.89644 | -49.06482 | 2026-09-20 04:38:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 7ebd831d-0cba-34d8-89c4-c7807d0a98a3 | -5.21977 | -47.58273 | 2026-09-20 04:38:00 | NOAA-20 | IMPERATRIZ | MARANHÃO | Brasil | 2105302 | 21 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 93a39e95-86e6-3df2-8b5d-6a0ce8a0f0a9 | -6.29927 | -47.60806 | 2026-09-20 04:38:00 | NOAA-20 | TOCANTINÓPOLIS | TOCANTINS | Brasil | 1721208 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 71e8664f-8124-3b0b-b474-40dcedc9a07c | -6.56255 | -45.5794 | 2026-09-20 04:38:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 17fc620a-e92c-3c1c-af24-6c6bcd35b172 | -3.08424 | -51.28222 | 2026-09-20 04:38:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 24af9ada-e500-3671-a72b-d7d332a92741 | -3.90263 | -49.06949 | 2026-09-20 04:38:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 21.9 |
| fbeeeaa5-68c5-3989-8d96-a26f0d6f8d16 | -3.43762 | -58.2326 | 2026-09-20 04:38:00 | NOAA-20 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 11676524-7e32-3bc0-8bc5-68e4e8d764d9 | -2.30782 | -48.40075 | 2026-09-20 04:38:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 382c8e14-ceee-39a6-b07e-603016620d80 | -5.67216 | -45.305 | 2026-09-20 04:38:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 7334e405-16e8-3ea4-a3a9-a7e8dc856108 | -5.40654 | -44.27372 | 2026-09-20 04:38:00 | NOAA-20 | GRAÇA ARANHA | MARANHÃO | Brasil | 2104701 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 09527e8d-5ea5-34df-8cc5-827ba51e7809 | -5.41022 | -44.27432 | 2026-09-20 04:38:00 | NOAA-20 | GRAÇA ARANHA | MARANHÃO | Brasil | 2104701 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 48b7f1f3-c3c4-371d-b3e7-3660533414fb | -5.64697 | -43.37117 | 2026-09-20 04:38:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| b343e589-578d-3cab-a75d-d569cd66310a | -6.19296 | -45.32821 | 2026-09-20 04:38:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b7b50683-0df0-3cf6-a420-68c4fc1620c3 | -5.22308 | -47.58326 | 2026-09-20 04:38:00 | NOAA-20 | IMPERATRIZ | MARANHÃO | Brasil | 2105302 | 21 | 33 | nan | nan | nan | Amazônia | 12.7 |
| 5a517d7f-a6cd-3ffe-8a45-1ad0fb71d966 | -3.45271 | -50.60678 | 2026-09-20 04:38:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| d8bf2d8e-c783-359f-ae6a-b7bb882c2785 | -2.36409 | -48.3622 | 2026-09-20 04:38:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| faae5c79-b444-33a7-bb7b-25481d999d0a | -2.96256 | -50.41505 | 2026-09-20 04:38:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| bfea6f74-0f29-3229-a8b1-5b00cc8ca0e8 | -6.91403 | -42.89851 | 2026-09-20 04:38:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 3.2 |
| 7ac2bc59-06d8-370c-b0fc-b953931861ae | -6.19416 | -47.52008 | 2026-09-20 04:38:00 | NOAA-20 | TOCANTINÓPOLIS | TOCANTINS | Brasil | 1721208 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| a4e8e89e-8e3e-3392-a914-4efc750dac2c | -5.58021 | -45.54594 | 2026-09-20 04:38:00 | NOAA-20 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 4c4bf8e6-4fdb-359a-9b21-5427fcfbbd64 | -5.28073 | -44.26521 | 2026-09-20 04:38:00 | NOAA-20 | GONÇALVES DIAS | MARANHÃO | Brasil | 2104404 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| fa0ed5ae-a681-33d7-852e-f437b631d6dc | -6.98784 | -43.72948 | 2026-09-20 04:38:00 | NOAA-20 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 55b408b5-97ca-3274-8751-d9d524671753 | -6.29734 | -41.76637 | 2026-09-20 04:38:00 | NOAA-20 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 22133da6-b3e7-31a6-86f0-25e35df43b4d | -6.30262 | -47.62991 | 2026-09-20 04:38:00 | NOAA-20 | TOCANTINÓPOLIS | TOCANTINS | Brasil | 1721208 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| b8b92aa2-0bdf-3066-bbdf-7b5730afe413 | -3.56531 | -43.48188 | 2026-09-20 04:38:00 | NOAA-20 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| d4caa168-0740-30c2-a63c-80381a997c4f | -5.28536 | -49.34632 | 2026-09-20 04:38:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 518d2786-38f9-3f78-945c-c4a3a882c60f | -1.80434 | -48.06101 | 2026-09-20 04:38:00 | NOAA-20 | CONCÓRDIA DO PARÁ | PARÁ | Brasil | 1502756 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 9f473b55-52cf-31b4-8ee8-106254cae50b | -5.22564 | -49.30069 | 2026-09-20 04:38:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| ec0cd993-9567-3a09-8992-006dd5d95d11 | -3.38553 | -50.44023 | 2026-09-20 04:38:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8d8982dd-c861-35bb-9f87-d482e4bb60b2 | -5.43291 | -47.60961 | 2026-09-20 04:38:00 | NOAA-20 | IMPERATRIZ | MARANHÃO | Brasil | 2105302 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 3ce4760d-6a25-364e-85bf-4fb7ff414aea | -6.31642 | -47.62853 | 2026-09-20 04:38:00 | NOAA-20 | TOCANTINÓPOLIS | TOCANTINS | Brasil | 1721208 | 17 | 33 | nan | nan | nan | Cerrado | 7.4 |
| d45516b2-0dea-3736-9173-4f07da9e14c1 | -2.96809 | -49.56328 | 2026-09-20 04:38:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4ecf85ed-c793-32be-a77c-069532d0bd9f | -3.35839 | -50.44846 | 2026-09-20 04:38:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| bd18d8d7-e983-304f-93a7-3e2d15ef7a37 | -6.29234 | -41.76998 | 2026-09-20 04:38:00 | NOAA-20 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 7be937d1-4ac3-39a7-9680-d319ab8695bb | -6.02143 | -45.40821 | 2026-09-20 04:38:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 6c851f3d-4793-3e86-8093-b18262e12a2f | -3.46223 | -50.61693 | 2026-09-20 04:38:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 65310ac7-c92a-3eb3-b2f0-0c14b9c113ec | -3.73446 | -51.82167 | 2026-09-20 04:38:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 20.0 |
| bb16e56f-e69e-3d11-9e49-78868fa8cb46 | -3.37981 | -39.20562 | 2026-09-20 04:38:00 | NOAA-20 | PARAIPABA | CEARÁ | Brasil | 2310258 | 23 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 602f4236-5168-36f5-8abd-f8303f0e3ad3 | -5.43237 | -47.61306 | 2026-09-20 04:38:00 | NOAA-20 | IMPERATRIZ | MARANHÃO | Brasil | 2105302 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| be3ac5cf-51f2-3a49-81a0-3ea85f150324 | -3.97627 | -48.93347 | 2026-09-20 04:38:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f52c9c33-45a6-3a05-880c-a28cc5a6b6bd | -3.01154 | -54.17162 | 2026-09-20 04:38:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 8b759062-ec22-3552-a177-1010c66a8c96 | -3.44498 | -50.26852 | 2026-09-20 04:38:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 73b9aa20-0c83-32f5-b221-2bdbcf3fe70a | -3.70911 | -39.43782 | 2026-09-20 04:38:00 | NOAA-20 | UMIRIM | CEARÁ | Brasil | 2313757 | 23 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 9be3c6f3-5774-3760-b604-569b0a5c1816 | -7.12822 | -42.07714 | 2026-09-20 04:38:00 | NOAA-20 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 58b795b7-b171-3ceb-831c-b8ff5b82008b | -5.57447 | -45.53712 | 2026-09-20 04:38:00 | NOAA-20 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c16c4ec2-1d82-3442-8998-72ebda7be75c | -2.58818 | -59.99694 | 2026-09-20 04:38:00 | NOAA-20 | MANAUS | AMAZONAS | Brasil | 1302603 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 624a1e49-9e54-3bad-8c3c-2dad2aac15ed | -6.17355 | -47.71567 | 2026-09-20 04:38:00 | NOAA-20 | MAURILÂNDIA DO TOCANTINS | TOCANTINS | Brasil | 1712801 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 03e4174d-a3a2-32f0-b244-a34f49bde80a | -6.70012 | -46.02299 | 2026-09-20 04:38:00 | NOAA-20 | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 773ed1ba-2dd6-3f2b-879e-a22ed1d6905f | -6.72304 | -46.07636 | 2026-09-20 04:38:00 | NOAA-20 | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| f9fdb071-8a98-3ea2-b48d-c8711eccc3d7 | -6.28212 | -47.58761 | 2026-09-20 04:38:00 | NOAA-20 | TOCANTINÓPOLIS | TOCANTINS | Brasil | 1721208 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 4d84e72d-6fbd-3b8e-a59b-652cf5acd3a5 | -4.29836 | -48.634 | 2026-09-20 04:38:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 90a6b9ae-f69c-36dc-acf3-cafaa1f92039 | -3.68074 | -60.62152 | 2026-09-20 04:38:00 | NOAA-20 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 02be8781-e4dc-37a8-adc4-f2702bb17508 | -4.84439 | -40.5246 | 2026-09-20 04:38:00 | NOAA-20 | NOVA RUSSAS | CEARÁ | Brasil | 2309300 | 23 | 33 | nan | nan | nan | Caatinga | 1.7 |
| c9228d0d-9825-3ed5-a0c1-83b352453d70 | -3.50396 | -43.35275 | 2026-09-20 04:38:00 | NOAA-20 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 10.0 |
| 84da8ba4-1f17-3088-8303-a8beb6eb91c2 | -5.18944 | -49.33195 | 2026-09-20 04:38:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 1746f66a-05f5-3715-b673-3b41e4012c9c | -6.2006 | -45.32547 | 2026-09-20 04:38:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| a0b847eb-63eb-3399-b295-b34d1800250e | -3.38127 | -50.44376 | 2026-09-20 04:38:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| c6d9f294-63c2-366e-8025-a782fe2fb82f | -3.79662 | -60.72812 | 2026-09-20 04:38:00 | NOAA-20 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 1228f989-f61c-3fa0-bd06-feece42b3d70 | -2.98244 | -54.77844 | 2026-09-20 04:38:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 42c40717-196e-3790-8a38-314694f6d1bf | -3.3456 | -42.76556 | 2026-09-20 04:38:00 | NOAA-20 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 5.4 |
| dbe2260e-621a-38f1-8cf2-19e02dc55247 | -2.14614 | -50.89973 | 2026-09-20 04:38:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| bb1133ae-8993-3f51-83f6-27d58918326a | -4.25583 | -48.54141 | 2026-09-20 04:38:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 00cd75db-e562-311b-af78-222620d15399 | -3.44615 | -50.60143 | 2026-09-20 04:38:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 6920c357-1dbe-3dd4-96aa-9f848e450710 | -0.71631 | -47.85091 | 2026-09-20 04:38:00 | NOAA-20 | CURUÇÁ | PARÁ | Brasil | 1502905 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e6a6686f-9e3c-32ce-801b-76f162d34d71 | -6.36128 | -43.35969 | 2026-09-20 04:38:00 | NOAA-20 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 39222cfd-f99a-30e5-8618-8365a6dfff34 | -6.56194 | -45.58329 | 2026-09-20 04:38:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |


[Clique aqui para ver as próximas entradas](README52.md)
