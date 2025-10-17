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

## Dados Diários - Página 50

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 4824aed7-111e-303d-864a-8fc7fc195e5b | -11.49989 | -44.06298 | 2025-10-17 04:19:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| bbf7fe26-b561-39ef-9b2d-0d8ededbfca2 | -7.28304 | -42.93991 | 2025-10-17 04:19:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| aa11c829-f170-38e1-b18d-beac267bc8ab | -7.0784 | -44.94535 | 2025-10-17 04:19:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 7.5 |
| d543c8ba-bba2-30b8-b391-6289d738b8c6 | -5.25021 | -43.0082 | 2025-10-17 04:19:00 | NOAA-21 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 5.3 |
| a4ca9e3d-4c07-375e-a0d8-1c7cb3da0506 | -6.22044 | -44.4242 | 2025-10-17 04:19:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 932aa1ab-1ff7-3ea9-a8ef-f99befbedf9f | -6.51635 | -46.5171 | 2025-10-17 04:19:00 | NOAA-21 | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d4715dac-b06b-3fb5-aa9d-52464187d8ff | -6.22743 | -42.50065 | 2025-10-17 04:19:00 | NOAA-21 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 2ba519c3-88de-3a73-a58b-79b400086f5d | -7.4811 | -42.74321 | 2025-10-17 04:19:00 | NOAA-21 | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 5fe2890c-2cdd-3c93-b760-072c86df33de | -9.06721 | -48.84824 | 2025-10-17 04:19:00 | NOAA-21 | GOIANORTE | TOCANTINS | Brasil | 1708304 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| aa8a24e2-0e40-334a-8700-601a5a6fa1eb | -5.84787 | -44.93736 | 2025-10-17 04:19:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 41adba43-c6ba-3360-889a-7357ffd90461 | -8.52461 | -44.5757 | 2025-10-17 04:19:00 | NOAA-21 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 10739d7a-0df5-3c17-8f31-d874f3024a65 | -8.46375 | -44.17563 | 2025-10-17 04:19:00 | NOAA-21 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 84335b6b-f3cd-30bf-8160-0116f33abde3 | -7.90869 | -50.38681 | 2025-10-17 04:19:00 | NOAA-21 | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 44ad7b7f-8024-36d4-8abe-be600dc843d1 | -11.3795 | -44.18467 | 2025-10-17 04:19:00 | NOAA-21 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| fcfc8047-7a32-3ea5-bed4-999f8f0871cb | -5.8806 | -43.90052 | 2025-10-17 04:19:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 70275c91-c473-3eae-8967-bc6c8357edad | -5.50044 | -47.30698 | 2025-10-17 04:19:00 | NOAA-21 | SENADOR LA ROCQUE | MARANHÃO | Brasil | 2111763 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| eed82738-24b7-3898-b35e-628c21966e55 | -6.75425 | -42.36057 | 2025-10-17 04:19:00 | NOAA-21 | CAJAZEIRAS DO PIAUÍ | PIAUÍ | Brasil | 2202075 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 545c3aed-e32b-3894-b57a-c99fdc3eded5 | -8.84247 | -45.9761 | 2025-10-17 04:19:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 4fe5256a-b6f5-35aa-859a-8d972ca4859c | -10.14911 | -44.53641 | 2025-10-17 04:19:00 | NOAA-21 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| fad8c2ef-0c1d-3c8a-9f27-5bc89c27396b | -5.48366 | -48.65209 | 2025-10-17 04:19:00 | NOAA-21 | SÃO JOÃO DO ARAGUAIA | PARÁ | Brasil | 1507508 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 7bb3d108-dcb5-3b89-a2cf-bc4facd7a0c6 | -5.87027 | -41.23355 | 2025-10-17 04:19:00 | NOAA-21 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 3.9 |
| d1d3a27d-1aaf-3a36-b045-7cb804f0b8bd | -4.72223 | -46.15615 | 2025-10-17 04:19:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 8799ee9c-2209-38d0-85ba-144faf38dd27 | -6.11572 | -44.85561 | 2025-10-17 04:19:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| cb971fd8-101f-3a4a-8454-adb7c97bd98f | -7.00921 | -41.99623 | 2025-10-17 04:19:00 | NOAA-21 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 6800d4be-0c09-3699-97fc-d10cc15fefde | -3.35382 | -49.94447 | 2025-10-17 04:19:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 3d1369bf-5d90-37ad-ad68-ef5060ac81b4 | -9.69046 | -48.93996 | 2025-10-17 04:19:00 | NOAA-21 | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f00310bc-7fc8-3cff-9cae-f7419d357826 | -10.51814 | -43.39072 | 2025-10-17 04:19:00 | NOAA-21 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| e6abbbad-6490-301d-97c4-351ca10fa72b | -5.88704 | -44.75282 | 2025-10-17 04:19:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 4a9e22bd-0488-3c19-8a1e-84fcdd92ad41 | -9.24282 | -44.37267 | 2025-10-17 04:19:00 | NOAA-21 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 6ae49b01-0225-3aef-8a6e-86dc0470a502 | -4.50739 | -46.00599 | 2025-10-17 04:19:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 12.0 |
| 970dbcc7-5ed2-3010-a61c-c28522c1bc7f | -5.84163 | -43.88723 | 2025-10-17 04:19:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 5c5e6855-9b6a-37fd-b69e-4ba16a1c930e | -7.61843 | -47.83529 | 2025-10-17 04:19:00 | NOAA-21 | FILADÉLFIA | TOCANTINS | Brasil | 1707702 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| e4ff945f-544b-3ba3-8958-882d7286ea62 | -4.22082 | -48.36743 | 2025-10-17 04:19:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| c47d44d5-903d-3006-908a-4c39aa6a7748 | -8.62939 | -45.68715 | 2025-10-17 04:19:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a527a228-c828-3660-af2f-075a2fc52d14 | -9.14513 | -46.643 | 2025-10-17 04:19:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 8.6 |
| a4f2e8fd-edf2-3936-b074-d0344a9439b6 | -10.30098 | -44.03503 | 2025-10-17 04:19:00 | NOAA-21 | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 4bf2cdf1-a6af-3036-af39-4fd1c7485ef0 | -6.74614 | -42.36723 | 2025-10-17 04:19:00 | NOAA-21 | CAJAZEIRAS DO PIAUÍ | PIAUÍ | Brasil | 2202075 | 22 | 33 | nan | nan | nan | Caatinga | 3.1 |
| cce9904c-bb3b-329e-b0d7-aeeeebadd3a1 | -6.39529 | -41.4778 | 2025-10-17 04:19:00 | NOAA-21 | LAGOA DO SÍTIO | PIAUÍ | Brasil | 2205599 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 115adb9c-91b5-3d31-9629-2b033763521d | -6.08714 | -42.38697 | 2025-10-17 04:19:00 | NOAA-21 | PASSAGEM FRANCA DO PIAUÍ | PIAUÍ | Brasil | 2207751 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 118a75d8-bd5e-3db1-be8a-12e16fdcdd7b | -7.18227 | -42.35899 | 2025-10-17 04:19:00 | NOAA-21 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| a38a03eb-6f92-3200-9c61-6234959f9052 | -5.54698 | -41.31697 | 2025-10-17 04:19:00 | NOAA-21 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 3.6 |
| b522057e-1026-3547-a0bb-3f1db449c942 | -8.08595 | -45.44294 | 2025-10-17 04:19:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 22.0 |
| fa0b0af7-c2b8-3c31-bbb6-76007439d609 | -4.01379 | -47.42033 | 2025-10-17 04:19:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 8bba0c59-a159-3546-b060-3e076736f5b3 | -5.69943 | -53.64284 | 2025-10-17 04:19:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0810a449-e070-3553-bb61-dfdc260c686c | -6.15833 | -41.70732 | 2025-10-17 04:19:00 | NOAA-21 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| b6f0169f-8480-3223-84fd-7ae228b89e06 | -7.54701 | -42.05585 | 2025-10-17 04:19:00 | NOAA-21 | SANTO INÁCIO DO PIAUÍ | PIAUÍ | Brasil | 2209500 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 629090e0-10ea-3051-baec-f959f7f1a471 | -10.64784 | -45.24896 | 2025-10-17 04:19:00 | NOAA-21 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 1e8562d8-c118-3591-8e6f-2e59689e4e5d | -6.42435 | -44.03561 | 2025-10-17 04:19:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| a2b7375a-5744-324f-894c-761c5d110516 | -8.16762 | -43.30693 | 2025-10-17 04:19:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 7.0 |
| 22195398-1612-3a16-9041-10590319e1dd | -7.02524 | -41.81794 | 2025-10-17 04:19:00 | NOAA-21 | SÃO JOÃO DA VARJOTA | PIAUÍ | Brasil | 2209955 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 504914f7-7113-3261-b32a-4e3e78ec4c48 | -11.46228 | -44.21952 | 2025-10-17 04:19:00 | NOAA-21 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 6a0037b2-6dd8-3f6f-a668-3e223e43dce5 | -5.54052 | -44.48584 | 2025-10-17 04:19:00 | NOAA-21 | SANTA FILOMENA DO MARANHÃO | MARANHÃO | Brasil | 2109759 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 6e0e0852-3ee8-356a-b119-c6eb2597912a | -6.19371 | -41.73737 | 2025-10-17 04:19:00 | NOAA-21 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 98f1e3af-e3ba-332f-a898-09300c555e23 | -7.17203 | -42.51902 | 2025-10-17 04:19:00 | NOAA-21 | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | 3.9 |
| d8dd7511-d02f-3c1d-8ecd-526c8e0af6f9 | -3.51035 | -52.48583 | 2025-10-17 04:19:00 | NOAA-21 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 14.4 |
| 10695eed-a3bd-30f6-ac5d-0a28fcdf9d65 | -7.43826 | -43.74482 | 2025-10-17 04:19:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| edf0aee3-5384-3284-a7b8-acc8a843296f | -5.58082 | -47.46012 | 2025-10-17 04:19:00 | NOAA-21 | IMPERATRIZ | MARANHÃO | Brasil | 2105302 | 21 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 5520a175-f90b-3252-806b-20dc53e3dd0c | -10.23818 | -49.86989 | 2025-10-17 04:19:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 979c0523-f11b-362c-8897-56c32be9dd20 | -10.91865 | -47.87284 | 2025-10-17 04:19:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 30f764b1-ab9c-36bd-a215-0242240e9338 | -7.13225 | -45.72636 | 2025-10-17 04:19:00 | NOAA-21 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 40621e39-6532-3e92-8792-80f498163422 | -3.53934 | -49.00747 | 2025-10-17 04:19:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 91869bee-a7fb-3eb3-82b3-0712f8080410 | -7.35613 | -41.90504 | 2025-10-17 04:19:00 | NOAA-21 | SANTO INÁCIO DO PIAUÍ | PIAUÍ | Brasil | 2209500 | 22 | 33 | nan | nan | nan | Caatinga | 4.2 |
| 4b6d7850-34b6-34f0-abeb-b313994c5e58 | -5.33832 | -41.18621 | 2025-10-17 04:19:00 | NOAA-21 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 80765bc5-c94e-3824-b073-ee63df29397a | -6.92992 | -44.08597 | 2025-10-17 04:19:00 | NOAA-21 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| ac77a9c8-a136-3a91-8ee1-70ef8ded4cc5 | -10.26228 | -44.04032 | 2025-10-17 04:19:00 | NOAA-21 | AVELINO LOPES | PIAUÍ | Brasil | 2201101 | 22 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 9f2b9a7f-19d5-308c-b207-d9cabb9d0963 | -10.46543 | -45.06548 | 2025-10-17 04:19:00 | NOAA-21 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 9a62896b-4891-3f6c-951e-977c662209b4 | -6.06753 | -49.38698 | 2025-10-17 04:19:00 | NOAA-21 | ELDORADO DO CARAJÁS | PARÁ | Brasil | 1502954 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 587a04e2-1e4b-35d6-bd41-5ad6fc1e8244 | -8.30301 | -43.40609 | 2025-10-17 04:19:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 3.1 |
| bff1121a-21b0-3379-814f-8266de8855fa | -5.60621 | -49.03402 | 2025-10-17 04:19:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 4b741b46-350e-36c6-a96c-d35644d2dc7a | -8.32954 | -46.8894 | 2025-10-17 04:19:00 | NOAA-21 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 33bc9b80-1267-3aa8-9fa0-daff902fb87c | -5.4828 | -42.94791 | 2025-10-17 04:19:00 | NOAA-21 | NAZÁRIA | PIAUÍ | Brasil | 2206720 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| cc24377c-d8ac-3014-b1ef-296d0c5f246e | -7.21132 | -45.46344 | 2025-10-17 04:19:00 | NOAA-21 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 9d0faa63-bb2a-38ba-9421-f5f8dda3b2c9 | -5.26318 | -44.21305 | 2025-10-17 04:19:00 | NOAA-21 | GONÇALVES DIAS | MARANHÃO | Brasil | 2104404 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a071ebf4-f393-322c-8f29-762332b28e1a | -8.19644 | -46.93189 | 2025-10-17 04:19:00 | NOAA-21 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| cde7e1cd-6575-31ca-aa31-f011ea778f08 | -5.88266 | -44.75919 | 2025-10-17 04:19:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 84d9a847-44ec-3e50-a4c8-dad2f7c57481 | -10.50789 | -43.43526 | 2025-10-17 04:19:00 | NOAA-21 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 13.1 |
| e76548cb-a691-3a8e-b138-6c466322789e | -9.235 | -45.27594 | 2025-10-17 04:19:00 | NOAA-21 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 8d8af644-4853-3a14-8d98-aecee926f5fe | -10.10676 | -44.56976 | 2025-10-17 04:19:00 | NOAA-21 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 853c6733-826e-3361-b027-af6783acf994 | -4.09048 | -43.17951 | 2025-10-17 04:19:00 | NOAA-21 | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 7026a85a-16b9-35fa-8dd7-94f9f9e721f3 | -9.06947 | -42.45525 | 2025-10-17 04:19:00 | NOAA-21 | SÃO RAIMUNDO NONATO | PIAUÍ | Brasil | 2210607 | 22 | 33 | nan | nan | nan | Caatinga | 3.6 |
| 27676ff7-cc06-3a31-9555-d00416a5fdc4 | -4.93827 | -47.07781 | 2025-10-17 04:19:00 | NOAA-21 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 29b43cc6-1342-3d4a-a151-bf128c23d6b1 | -10.53136 | -43.36835 | 2025-10-17 04:19:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.9 |
| c6eebe34-c5f1-3d7d-aa61-d4bafb2637cd | -7.17979 | -42.18652 | 2025-10-17 04:19:00 | NOAA-21 | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 20a2522b-f2c0-3807-a9c2-5a31f68234ba | -9.35294 | -46.91129 | 2025-10-17 04:19:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 78506ad0-2b9c-3b20-b81d-7bd712163961 | -7.33808 | -43.86693 | 2025-10-17 04:19:00 | NOAA-21 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| ec237ab6-e2a5-3597-9b90-b9e12f4d5e0c | -7.66904 | -42.59161 | 2025-10-17 04:19:00 | NOAA-21 | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| dfdc9d1d-fabf-3a3e-b788-6bb2d0d08cd3 | -10.11963 | -44.61865 | 2025-10-17 04:19:00 | NOAA-21 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 8ab7b25f-291c-3606-ae0e-91761a5505b5 | -7.1075 | -44.73798 | 2025-10-17 04:19:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| ee72467a-f053-39dd-af98-adb771b322e5 | -5.25288 | -42.85788 | 2025-10-17 04:19:00 | NOAA-21 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 035f42b8-c3a3-375f-b7dd-0d5fa7b90253 | -6.15598 | -40.92231 | 2025-10-17 04:19:00 | NOAA-21 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| a7c1de75-70ae-358d-bd8c-78c11956e3f0 | -7.1732 | -42.51137 | 2025-10-17 04:19:00 | NOAA-21 | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| e5dbb95e-2fbd-371c-adf8-32eb4aee7a00 | -11.50045 | -44.05927 | 2025-10-17 04:19:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| cb957d09-bbef-3f69-970a-e3257b0d2980 | -7.68412 | -42.56238 | 2025-10-17 04:19:00 | NOAA-21 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| c6109d46-9fa0-3cbd-951b-9b94bca7343d | -8.82508 | -47.30525 | 2025-10-17 04:19:00 | NOAA-21 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 6.9 |
| ebefe966-86fc-3a65-a44d-0d322e1e4580 | -10.35969 | -47.72388 | 2025-10-17 04:19:00 | NOAA-21 | SANTA TEREZA DO TOCANTINS | TOCANTINS | Brasil | 1719004 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ea6dd3a2-8daa-34b3-8796-fbe19c0b6222 | -9.19581 | -46.87791 | 2025-10-17 04:19:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d9fc9142-51f3-32e9-9ce0-359c484a7c25 | -9.14455 | -46.6466 | 2025-10-17 04:19:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 6.0 |
| df50934f-139f-3630-b6c3-2ac48cc71f13 | -4.93215 | -41.55286 | 2025-10-17 04:19:00 | NOAA-21 | JUAZEIRO DO PIAUÍ | PIAUÍ | Brasil | 2205516 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| ce695711-7386-39b3-9c7a-87c2a62e432f | -9.27978 | -45.2972 | 2025-10-17 04:19:00 | NOAA-21 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 12ea16b5-6d0e-3c64-83c6-5bbc8f881834 | -8.05718 | -48.16822 | 2025-10-17 04:19:00 | NOAA-21 | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |


[Clique aqui para ver as próximas entradas](README51.md)
