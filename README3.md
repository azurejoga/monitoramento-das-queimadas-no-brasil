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

## Dados Diários - Página 3

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 050a7612-103b-3536-86f9-7ef3fd515312 | -12.003 | -46.7644 | 2025-11-15 00:18:00 | METOP-C | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 4b36eff8-57f0-3216-b4c8-e4515e85ace3 | -3.7015 | -47.642399 | 2025-11-15 00:18:00 | METOP-C | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b619f39e-cbef-3fa7-aa8a-a560f41a53eb | -11.8368 | -49.203602 | 2025-11-15 00:18:00 | METOP-C | CARIRI DO TOCANTINS | TOCANTINS | Brasil | 1703867 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| b05c6249-7a84-3b58-9026-497532ac1220 | -3.4683 | -45.648701 | 2025-11-15 00:18:00 | METOP-C | GOVERNADOR NEWTON BELLO | MARANHÃO | Brasil | 2104651 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| d90196e5-f609-38b5-85c5-c454ac99fa07 | -4.2899 | -45.550098 | 2025-11-15 00:18:00 | METOP-C | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 410167ee-4d56-3b35-ba13-948f7e69ee09 | -4.1912 | -48.550098 | 2025-11-15 00:18:00 | METOP-C | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f334d85b-4f0f-3ccd-91d6-8ba13e8251ff | -5.2313 | -44.3391 | 2025-11-15 00:18:00 | METOP-C | GONÇALVES DIAS | MARANHÃO | Brasil | 2104404 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| cf7f75dc-2066-35fd-98ce-bd35507db547 | -7.4487 | -42.757301 | 2025-11-15 00:18:00 | METOP-C | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 1877df21-8b6d-3ff2-aa95-3d22ee966e78 | -3.9862 | -44.254299 | 2025-11-15 00:18:00 | METOP-C | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| d977190d-1db5-30d0-9f91-586c1c9fb25a | -2.7106 | -47.392502 | 2025-11-15 00:18:00 | METOP-C | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0a199e2b-3139-3173-a51e-7d6ecb29cae9 | -3.0054 | -49.431198 | 2025-11-15 00:18:00 | METOP-C | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c151dcf2-1289-30bc-8f1f-357b65a52d64 | -4.6602 | -45.0476 | 2025-11-15 00:18:00 | METOP-C | LAGO DO JUNCO | MARANHÃO | Brasil | 2105807 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 0d98f03b-8325-3bae-8ec2-fd7d34a364a7 | -4.6087 | -41.747299 | 2025-11-15 00:18:00 | METOP-C | MILTON BRANDÃO | PIAUÍ | Brasil | 2206357 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 215e1242-de73-37c3-9257-ccd5fd320435 | -8.2999 | -46.220299 | 2025-11-15 00:18:00 | METOP-C | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 8bf01905-e4c4-3623-897d-95b28545b886 | -4.5553 | -43.2234 | 2025-11-15 00:18:00 | METOP-C | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 924e6d26-9d6c-3c72-9d29-54a00a375ae7 | -10.9901 | -47.7304 | 2025-11-15 00:18:00 | METOP-C | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 0e7a0fc1-eff6-3087-8e69-8e52fce99a52 | -5.8919 | -46.046902 | 2025-11-15 00:18:00 | METOP-C | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 39e3ac87-c9b9-394d-9978-6178601c5e80 | -5.3287 | -43.0434 | 2025-11-15 00:18:00 | METOP-C | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 7007a8d1-59b2-3c6a-a1cd-f6d5d95b4c9f | -3.3883 | -45.431702 | 2025-11-15 00:18:00 | METOP-C | MONÇÃO | MARANHÃO | Brasil | 2106904 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 762149bc-ff12-3571-b0df-c0bc78776acb | -4.4578 | -45.381901 | 2025-11-15 00:18:00 | METOP-C | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 43f6b169-317b-3998-a442-15ab0430cda2 | -3.9927 | -44.2826 | 2025-11-15 00:18:00 | METOP-C | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| b532ef5e-b4f0-3a1a-86f6-80919b866d1d | -5.5743 | -46.143299 | 2025-11-15 00:18:00 | METOP-C | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 8218a6d9-5f56-3531-a6ed-76aa36fd7d1a | -9.6617 | -43.907398 | 2025-11-15 00:18:00 | METOP-C | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 4a151abb-cac0-3fe9-8b11-590553973e20 | -3.2256 | -45.214298 | 2025-11-15 00:18:00 | METOP-C | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| be1a224c-39fe-3f4a-bfda-6f65c3f59f91 | -9.0027 | -44.181099 | 2025-11-15 00:18:00 | METOP-C | SANTA LUZ | PIAUÍ | Brasil | 2209302 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| d731289a-5b27-3d6f-87c6-c1d9dc816b6b | -7.4518 | -42.771099 | 2025-11-15 00:18:00 | METOP-C | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| d4b48f8d-4868-32b0-9fb6-83d485a681ad | -5.4196 | -43.2616 | 2025-11-15 00:18:00 | METOP-C | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| bd67b47d-3344-3f92-a255-34e37a768fdd | -2.5167 | -47.807701 | 2025-11-15 00:18:00 | METOP-C | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f109251c-4857-3061-a856-f34ab9f50016 | -17.2652 | -42.668999 | 2025-11-15 00:18:00 | METOP-C | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 5c81d697-67aa-3ea5-9389-6ad6875ecc00 | -6.3058 | -41.815498 | 2025-11-15 00:18:00 | METOP-C | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| dd7c2bf4-1fd7-3840-9e0c-a303099c58dc | -5.8219 | -46.471901 | 2025-11-15 00:18:00 | METOP-C | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 22872690-f753-3529-99ac-1f7978de7251 | -1.4874 | -47.800499 | 2025-11-15 00:18:00 | METOP-C | SÃO MIGUEL DO GUAMÁ | PARÁ | Brasil | 1507607 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9b7aca74-6a12-33b4-a8b6-765ba00522ff | -4.8202 | -47.091099 | 2025-11-15 00:18:00 | METOP-C | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 28ee35c5-d22e-3c8d-b771-47dfc67b8c9a | -7.104 | -39.078701 | 2025-11-15 00:18:00 | METOP-C | AURORA | CEARÁ | Brasil | 2301703 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| 3f83cc97-7ce9-345a-9eb8-5b5bbfd0b572 | -5.7397 | -42.7211 | 2025-11-15 00:18:00 | METOP-C | AGRICOLÂNDIA | PIAUÍ | Brasil | 2200103 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 6e5e6fb2-af2c-3f69-80df-9d999d809de3 | -4.3315 | -47.5686 | 2025-11-15 00:18:00 | METOP-C | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 269b5cf7-1d00-3a14-b1b9-b52a2133ae0c | -10.373 | -47.7505 | 2025-11-15 00:18:00 | METOP-C | SANTA TEREZA DO TOCANTINS | TOCANTINS | Brasil | 1719004 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 2c9f279e-4bfb-32ba-a6e7-9ab766e84823 | -9.1533 | -45.194599 | 2025-11-15 00:18:00 | METOP-C | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 67ef972f-6adc-374e-8ae3-69145f4a347e | -9.6766 | -37.092701 | 2025-11-15 00:18:00 | METOP-C | BATALHA | ALAGOAS | Brasil | 2700706 | 27 | 33 | nan | nan | nan | Caatinga | nan |
| de83114f-2941-321c-9c8c-f6d73002dc80 | -10.6963 | -44.506001 | 2025-11-15 00:18:00 | METOP-C | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| cbadfff3-7a0a-35f6-b2ec-a6df33541334 | -8.7461 | -44.229301 | 2025-11-15 00:18:00 | METOP-C | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 84c9a873-7d2b-3c27-b2f0-8d219405d9f5 | -7.3463 | -43.352299 | 2025-11-15 00:18:00 | METOP-C | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 926da059-b76b-3d45-9894-35579d6eef13 | -6.1381 | -48.047199 | 2025-11-15 00:18:00 | METOP-C | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| ef470973-faf0-348a-b6ca-2f818034d888 | -3.3167 | -45.888699 | 2025-11-15 00:18:00 | METOP-C | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| c6ad8006-9ab7-30b0-9b5c-edd3e91c6566 | -7.4389 | -42.759499 | 2025-11-15 00:18:00 | METOP-C | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| aa344e2d-6ba8-3446-88dd-a0216f33754b | -2.9453 | -48.570301 | 2025-11-15 00:18:00 | METOP-C | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1e99e580-18d3-3367-be31-71f0b229cb49 | -5.5228 | -41.7747 | 2025-11-15 00:18:00 | METOP-C | SÃO JOÃO DA SERRA | PIAUÍ | Brasil | 2209906 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| f0d6f970-8638-3ad1-87ed-bc05d45132c5 | -5.7158 | -42.345501 | 2025-11-15 00:18:00 | METOP-C | PASSAGEM FRANCA DO PIAUÍ | PIAUÍ | Brasil | 2207751 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 536f62ad-aa15-3d95-94e0-9355b026e959 | -4.5748 | -43.3993 | 2025-11-15 00:18:00 | METOP-C | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 0d2f4cb1-a2fd-33fe-82d3-d85fe0dc0644 | -3.1039 | -45.494499 | 2025-11-15 00:18:00 | METOP-C | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 5c9f580e-3421-3d97-aa7b-ad836f640e52 | -4.7899 | -45.440201 | 2025-11-15 00:18:00 | METOP-C | LAGOA GRANDE DO MARANHÃO | MARANHÃO | Brasil | 2105963 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 2c9f0f6e-5307-3c33-8f15-795c833ba14b | -4.2881 | -45.542301 | 2025-11-15 00:18:00 | METOP-C | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 172d1ad3-a3c9-33bb-a578-ca624033230d | -6.296 | -41.817799 | 2025-11-15 00:18:00 | METOP-C | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 64cc389a-d860-3f02-b61d-f0f93d486bd5 | -5.2362 | -44.360901 | 2025-11-15 00:18:00 | METOP-C | GONÇALVES DIAS | MARANHÃO | Brasil | 2104404 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 0d8952fb-d117-3738-b734-a67facb04cd9 | -4.5424 | -43.211899 | 2025-11-15 00:18:00 | METOP-C | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| e50ea277-e5eb-3716-96c2-cf0b30494c06 | -4.531 | -43.207199 | 2025-11-15 00:18:00 | METOP-C | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 680bd479-536f-34bd-9cef-c7902a0a220e | -4.421 | -47.6022 | 2025-11-15 00:18:00 | METOP-C | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a6026c8d-9584-363c-a605-dcbbd0ef9e59 | -1.4972 | -47.798401 | 2025-11-15 00:18:00 | METOP-C | SÃO MIGUEL DO GUAMÁ | PARÁ | Brasil | 1507607 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a193a680-9a20-3cd3-a208-e6d02c5082e0 | -3.2786 | -45.447899 | 2025-11-15 00:18:00 | METOP-C | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 1fa0b18a-a501-35cd-8e4e-bd07a1b20557 | -7.4864 | -42.5602 | 2025-11-15 00:18:00 | METOP-C | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| b6f0754e-310a-341a-ae42-554caa72922e | -3.2273 | -45.221802 | 2025-11-15 00:18:00 | METOP-C | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 102782ff-d49b-3f84-8fa3-bb8699cd4b2f | -12.7589 | -43.653702 | 2025-11-15 00:18:00 | METOP-C | SERRA DOURADA | BAHIA | Brasil | 2930303 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 5a9d50e5-4470-3a6d-aec0-e6bada36d957 | -4.0973 | -45.609001 | 2025-11-15 00:18:00 | METOP-C | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 351e5839-1e2c-38bf-8310-f4e419166ae6 | -9.8573 | -44.705799 | 2025-11-15 00:18:00 | METOP-C | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 761476a0-0333-3621-9037-62dbe6dc9f0f | -9.1172 | -43.955502 | 2025-11-15 00:18:00 | METOP-C | SANTA LUZ | PIAUÍ | Brasil | 2209302 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 3cacae0b-264a-3087-b6c0-ced52aecabd7 | -6.3105 | -41.836201 | 2025-11-15 00:18:00 | METOP-C | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 8ddd4aab-d13d-3673-b01a-ae5cce421e3a | -9.66 | -43.899799 | 2025-11-15 00:18:00 | METOP-C | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 4972293e-dff6-392b-8f2c-345b2afd7fb5 | -5.337 | -43.034401 | 2025-11-15 00:18:00 | METOP-C | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 3db0bdf1-4e55-3a12-96df-845fa764f89e | -4.5907 | -41.758801 | 2025-11-15 00:18:00 | METOP-C | CAPITÃO DE CAMPOS | PIAUÍ | Brasil | 2202406 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 7d3a2cf3-564e-35e6-b80e-dc3e375a6476 | -14.6604 | -46.567402 | 2025-11-15 00:18:00 | METOP-C | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 145bda68-9596-3442-8d77-a376b27447dd | -10.7079 | -44.512199 | 2025-11-15 00:18:00 | METOP-C | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 5559f041-2b98-3c0e-a892-db1a9d89e08a | -4.1071 | -45.6068 | 2025-11-15 00:18:00 | METOP-C | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 250cebcb-f78b-302c-b0bd-5d804c501845 | -3.9828 | -44.284698 | 2025-11-15 00:18:00 | METOP-C | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 10bd1a75-7688-30f4-9677-53e61b20479a | -5.4812 | -40.968899 | 2025-11-15 00:18:00 | METOP-C | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 36ac0063-8aba-3ee0-ad58-f438b9491672 | -5.9654 | -42.987701 | 2025-11-15 00:18:00 | METOP-C | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 4f521f3b-fd1a-3f19-827b-7535f7c30d8b | -6.0675 | -43.255199 | 2025-11-15 00:18:00 | METOP-C | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | nan |
| 85f62443-5226-3983-a5f5-e9d5aa8a1aa2 | -5.1612 | -44.850101 | 2025-11-15 00:18:00 | METOP-C | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| f93c6e1a-d86c-36b4-9691-0a7ab1070d34 | -2.6384 | -45.485802 | 2025-11-15 00:18:00 | METOP-C | SANTA HELENA | MARANHÃO | Brasil | 2109809 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| cfa5e798-46c3-3d50-99ae-e040c128b95c | -3.0978 | -41.681198 | 2025-11-15 00:18:00 | METOP-C | BOM PRINCÍPIO DO PIAUÍ | PIAUÍ | Brasil | 2201919 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 74582511-db33-303f-9a93-ee0ddc912aad | -5.2346 | -44.3536 | 2025-11-15 00:18:00 | METOP-C | GONÇALVES DIAS | MARANHÃO | Brasil | 2104404 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| f9c6e044-05d9-3814-a582-f956625e981a | -6.5248 | -39.073601 | 2025-11-15 00:18:00 | METOP-C | CEDRO | CEARÁ | Brasil | 2303808 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| 1bdb9311-625b-333d-912c-bf13dda02df7 | -4.6315 | -44.601501 | 2025-11-15 00:18:00 | METOP-C | PEDREIRAS | MARANHÃO | Brasil | 2108207 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 5b27e062-a1a9-3625-9c02-2c774a30eba3 | -5.6579 | -49.2187 | 2025-11-15 00:18:00 | METOP-C | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 87947982-2f7d-314f-89b9-ee4f0609a871 | -5.1792 | -44.1092 | 2025-11-15 00:18:00 | METOP-C | GONÇALVES DIAS | MARANHÃO | Brasil | 2104404 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| d0bcc582-da89-3fc4-b919-146fb3af00a4 | -10.3496 | -48.917999 | 2025-11-15 00:18:00 | METOP-C | PUGMIL | TOCANTINS | Brasil | 1718451 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 7ad1cbaa-ba33-3b6b-a106-83b7462e6268 | -3.2151 | -45.485901 | 2025-11-15 00:18:00 | METOP-C | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 82beef8c-f8ce-3d93-860f-a9314b2ca2cd | -6.011 | -41.969002 | 2025-11-15 00:18:00 | METOP-C | SANTA CRUZ DOS MILAGRES | PIAUÍ | Brasil | 2209153 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 82912217-1b60-3ba0-a097-dc93a4e83e6a | -6.2688 | -41.744202 | 2025-11-15 00:18:00 | METOP-C | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| b4f51817-01e6-3f71-851c-cfe82856844f | -7.8778 | -48.390999 | 2025-11-15 00:18:00 | METOP-C | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 807b9b7a-9952-3831-9a41-61211f1f8c2b | -3.8926 | -46.207001 | 2025-11-15 00:18:00 | METOP-C | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 6147f167-e70e-3ddd-a878-12c3c9f2ccad | -4.1938 | -48.561699 | 2025-11-15 00:18:00 | METOP-C | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 657d848f-95f8-3e2d-8e68-884d003c26a2 | -3.4516 | -50.1003 | 2025-11-15 00:18:00 | METOP-C | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 231dc40b-6ad3-3cda-ad74-50046f8d7deb | -6.2704 | -41.751099 | 2025-11-15 00:18:00 | METOP-C | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| b684d320-034f-3f9d-bf8c-bdc735a143f7 | -10.9803 | -47.732399 | 2025-11-15 00:18:00 | METOP-C | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 5fb68d89-f2cb-39e9-a18e-81cf4585c252 | -3.8875 | -43.820599 | 2025-11-15 00:18:00 | METOP-C | VARGEM GRANDE | MARANHÃO | Brasil | 2112704 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| ca9f0d58-1b97-3806-9964-b03a7d138a41 | -12.842 | -46.433701 | 2025-11-15 00:18:00 | METOP-C | COMBINADO | TOCANTINS | Brasil | 1705557 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| a79b2142-56e9-3f25-b511-05fdada492c0 | -10.6981 | -44.514301 | 2025-11-15 00:18:00 | METOP-C | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 9afa297d-bd18-3390-b7eb-e6bd8061b20b | -3.9894 | -44.268398 | 2025-11-15 00:18:00 | METOP-C | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| e0b5853b-4a67-3755-bc6c-2ead3b6c62a0 | -7.1015 | -42.7262 | 2025-11-15 00:18:00 | METOP-C | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| a7eb4709-cf25-3324-bf15-78a9b91f0823 | -9.0044 | -44.188801 | 2025-11-15 00:18:00 | METOP-C | SANTA LUZ | PIAUÍ | Brasil | 2209302 | 22 | 33 | nan | nan | nan | Cerrado | nan |


[Clique aqui para ver as próximas entradas](README4.md)
