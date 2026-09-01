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

## Dados Diários - Página 87

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 90f3d3a3-d383-3497-9814-9b843ff996f1 | -7.5895 | -60.4636 | 2026-09-01 06:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 44.7 |
| ccb64971-aac1-3cb8-8cd7-7abed2b06f9c | -7.3487 | -60.5883 | 2026-09-01 06:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 58.2 |
| a7e8822f-5657-3384-b739-1335c1080f31 | -8.111 | -54.9684 | 2026-09-01 06:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 47.2 |
| 5452f5aa-348c-364f-a222-cd04ae7415e2 | -8.1296 | -54.9672 | 2026-09-01 06:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 44.4 |
| 87ff443c-20e3-3264-a58e-7aea7de9b6b6 | -7.571 | -60.4643 | 2026-09-01 06:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 49.0 |
| acc7ee22-bb08-3f88-bbb6-5931d4f2f8ca | -7.5895 | -60.4636 | 2026-09-01 06:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 52.0 |
| 0576e2b7-53f8-3768-9e07-d76b80ea299a | -7.5709 | -60.4835 | 2026-09-01 06:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 57.5 |
| a7d02a15-f4ae-3616-b668-24c1b6ef2dc8 | -7.3487 | -60.5883 | 2026-09-01 06:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 57.8 |
| 1f83d533-97a0-3714-959b-74d03dfe762e | -7.5894 | -60.4827 | 2026-09-01 06:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 86.3 |
| 67669ad6-33f9-3111-8908-f0acc3be832a | 0.01165 | -60.59869 | 2026-09-01 06:18:00 | NOAA-21 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 8f222ef7-5f1e-3eb5-b9c2-52e3f02de565 | 0.0049 | -60.59996 | 2026-09-01 06:18:00 | NOAA-21 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 626da522-3b9c-3410-8eb8-b732bc78c09a | -8.2788 | -54.9376 | 2026-09-01 06:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 46.2 |
| cd9b43b0-eda6-3a34-9e0d-48cbbb150736 | -7.5895 | -60.4636 | 2026-09-01 06:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 60.2 |
| c32b6c40-9434-387c-859e-3ab2d3a2af3d | -7.3487 | -60.5883 | 2026-09-01 06:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 50.3 |
| d40797a6-44b6-3010-a26f-77143a52b7a8 | -7.5709 | -60.4835 | 2026-09-01 06:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 55.2 |
| 649db835-909d-323f-8737-28d39f182cc1 | -7.571 | -60.4643 | 2026-09-01 06:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 54.4 |
| f4942433-92d0-3069-a617-da90c3739934 | -7.5894 | -60.4827 | 2026-09-01 06:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 75.7 |
| c2df7723-114a-3279-bbed-d18ed184b901 | -3.20906 | -61.13755 | 2026-09-01 06:20:00 | NOAA-21 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 3315103f-1897-3779-975b-b548526c3f69 | -7.53845 | -61.38113 | 2026-09-01 06:20:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| e049b477-3d83-39cb-85b0-0aecd7416968 | -7.5304 | -61.38738 | 2026-09-01 06:20:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 3.1 |
| c7830f78-1b18-3430-bbe2-4c99ba2a6b46 | -7.53131 | -61.38012 | 2026-09-01 06:20:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 5.1 |
| c942c24b-57e0-35a4-84e2-11af0509704d | -3.63773 | -60.55606 | 2026-09-01 06:20:00 | NOAA-21 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 571264e3-ffe5-3c52-b414-132a97c4d0de | -3.12481 | -61.22887 | 2026-09-01 06:20:00 | NOAA-21 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d87ef193-1b96-3166-b110-047687cc0fc4 | -3.62147 | -60.56804 | 2026-09-01 06:20:00 | NOAA-21 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 4.6 |
| f3a97378-1fa7-3f04-9942-fe54fb18c2a4 | -7.53754 | -61.38829 | 2026-09-01 06:20:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 52682a69-5b07-3259-bbca-1de6e08d5538 | -3.62959 | -60.56212 | 2026-09-01 06:20:00 | NOAA-21 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 3.3 |
| d4704c95-34fe-3f2b-b587-349f885d6790 | -3.62859 | -60.5691 | 2026-09-01 06:20:00 | NOAA-21 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 9b8bb7cc-66d9-36ef-95d2-6228fa443af2 | -3.13203 | -61.17927 | 2026-09-01 06:20:00 | NOAA-21 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| af94f9a3-b4fb-355d-886e-e563d9c9ff1e | -3.62246 | -60.56101 | 2026-09-01 06:20:00 | NOAA-21 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 67337bc7-1325-323c-908b-98ef9d1d5a27 | -3.11709 | -61.23408 | 2026-09-01 06:20:00 | NOAA-21 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 5.5 |
| b4b991db-c4f1-3817-9337-7f04bb5d9ff9 | -3.62346 | -60.55399 | 2026-09-01 06:20:00 | NOAA-21 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 4bface9c-8c70-3664-91c2-54c44cd82db0 | -3.1239 | -61.23509 | 2026-09-01 06:20:00 | NOAA-21 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 59d3298e-ee32-33aa-a260-4dda5059654c | -9.62683 | -68.60355 | 2026-09-01 06:22:00 | NOAA-21 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 2.4 |
| bc8a9985-02d1-3462-9a98-122f81859068 | -9.62222 | -68.60281 | 2026-09-01 06:22:00 | NOAA-21 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 9e509e77-16ad-3fe8-ad17-13f2b2d5b0be | -10.22376 | -69.04097 | 2026-09-01 06:22:00 | NOAA-21 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 1.3 |
| de50e8cb-f4f3-369e-bb10-9570af6db166 | -8.27415 | -70.08897 | 2026-09-01 06:22:00 | NOAA-21 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c93fe4f6-5b70-37b2-9d95-7bdcf5d13901 | -8.41995 | -71.12235 | 2026-09-01 06:22:00 | NOAA-21 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c74b5c23-9e82-313e-88fc-9c747bd7cb84 | -9.61834 | -68.60106 | 2026-09-01 06:22:00 | NOAA-21 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 40e98c1b-f5d0-3b0c-b830-16b0b688ef71 | -8.77575 | -69.33559 | 2026-09-01 06:22:00 | NOAA-21 | MANOEL URBANO | ACRE | Brasil | 1200344 | 12 | 33 | nan | nan | nan | Amazônia | 1.9 |
| f0df655d-d91c-335e-a6bf-eccb95ef27e7 | -8.5908 | -70.23098 | 2026-09-01 06:22:00 | NOAA-21 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a8709016-e3d9-3fcb-b843-e29675f93ce8 | -8.6051 | -70.21824 | 2026-09-01 06:22:00 | NOAA-21 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 36748fcc-efe3-3a40-8925-8a69d039a448 | -8.77349 | -69.34046 | 2026-09-01 06:22:00 | NOAA-21 | MANOEL URBANO | ACRE | Brasil | 1200344 | 12 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 857c6812-c31f-37cf-976d-aaee6c7ca332 | -8.60102 | -70.21766 | 2026-09-01 06:22:00 | NOAA-21 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 26ccf844-0fd5-3de6-8224-5f4dce5e2aa4 | -7.81456 | -73.00081 | 2026-09-01 06:22:00 | NOAA-21 | RODRIGUES ALVES | ACRE | Brasil | 1200427 | 12 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 0ba88355-2e9f-35c5-b58c-6f85ad01acfb | -8.5431 | -67.15662 | 2026-09-01 06:22:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 30882151-cec2-3105-87ed-11125c11bb5f | -9.06893 | -65.48692 | 2026-09-01 06:22:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 47ad4b1e-522a-311d-a46a-b3cc74059c52 | -8.88045 | -66.89482 | 2026-09-01 06:22:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 3da24107-48f3-3f14-a65a-97729cb4afbc | -10.13933 | -68.58807 | 2026-09-01 06:22:00 | NOAA-21 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 623b94c5-8c64-3059-8384-db1b99e6ddb5 | -9.45243 | -67.46051 | 2026-09-01 06:22:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 10.3 |
| 7f1d2b55-3e3e-3e54-a93f-b1a3c2182626 | -8.9308 | -72.83871 | 2026-09-01 06:22:00 | NOAA-21 | MARECHAL THAUMATURGO | ACRE | Brasil | 1200351 | 12 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 42892d75-8828-36de-8031-b3de7c65f76c | -8.82527 | -71.37119 | 2026-09-01 06:22:00 | NOAA-21 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f5908b7f-053e-3612-b5c5-d1276d168615 | -8.4565 | -70.72366 | 2026-09-01 06:22:00 | NOAA-21 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 5cca112d-789a-3916-b78a-2aa138056469 | -8.51505 | -67.13808 | 2026-09-01 06:22:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b602545f-13b2-3fe3-b497-ee04d85dceb4 | -9.62756 | -68.60249 | 2026-09-01 06:22:00 | NOAA-21 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 2.0 |
| accd646a-0d98-369c-a247-2be292c008bb | -8.25933 | -70.84124 | 2026-09-01 06:22:00 | NOAA-21 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 772ebd94-a6c6-39ac-885d-71ec2d36931b | -8.71803 | -67.11002 | 2026-09-01 06:22:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 7ed05566-bb8b-36a7-9513-d70930c38fe4 | -9.32609 | -68.88944 | 2026-09-01 06:22:00 | NOAA-21 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 80552785-87f0-31da-a906-5ce86d061939 | -9.46003 | -70.43226 | 2026-09-01 06:22:00 | NOAA-21 | SANTA ROSA DO PURUS | ACRE | Brasil | 1200435 | 12 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 28e69aeb-cd63-344d-8f82-b0612ec1e148 | -8.00936 | -71.31719 | 2026-09-01 06:22:00 | NOAA-21 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 11947838-a47d-34c1-a6c4-9e2239dbc24e | -9.45819 | -67.45553 | 2026-09-01 06:22:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 593320ae-2a9c-3ca9-89fe-df2454f10efc | -9.41467 | -71.22381 | 2026-09-01 06:22:00 | NOAA-21 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 0.6 |
| ac65aef6-33b1-324a-8efa-c585ff4eeb45 | -9.00081 | -65.43381 | 2026-09-01 06:22:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| d4b52c75-f8d3-3334-84c9-95075ac2a617 | -8.80372 | -71.06672 | 2026-09-01 06:22:00 | NOAA-21 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 4c9126b4-bc81-318b-b74b-687583357257 | -8.87614 | -66.88805 | 2026-09-01 06:22:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 9063a86f-909c-3f13-85b2-6a4d8202c354 | -7.59707 | -67.41819 | 2026-09-01 06:22:00 | NOAA-21 | PAUINI | AMAZONAS | Brasil | 1303502 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 9ae4556a-4579-3a61-bf6d-1867ca127220 | -8.51002 | -67.13733 | 2026-09-01 06:22:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| eed63ade-d2c5-374a-86ad-1e3169604eda | -8.58747 | -66.97601 | 2026-09-01 06:22:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 863a0a98-8307-33f7-9290-0a7d75978bbc | -9.00131 | -65.42987 | 2026-09-01 06:22:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 0d6ecded-6695-30bf-b3c9-2cb94ede86d8 | -7.87472 | -69.94643 | 2026-09-01 06:22:00 | NOAA-21 | ENVIRA | AMAZONAS | Brasil | 1301506 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 32c71dee-268b-3cd2-9808-f89ed5420195 | -8.81309 | -71.29211 | 2026-09-01 06:22:00 | NOAA-21 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 2d26e95b-4624-3cec-b7d3-109746bd0e0e | -8.77894 | -69.34465 | 2026-09-01 06:22:00 | NOAA-21 | MANOEL URBANO | ACRE | Brasil | 1200344 | 12 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f8765568-8f66-34c3-9506-5681beb33357 | -8.79287 | -62.48445 | 2026-09-01 06:22:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 2.4 |
| c1d186ed-8e0e-3566-8e81-a26bcd02dcbf | -8.93238 | -62.36396 | 2026-09-01 06:22:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 5f46aee4-49fc-3a55-9565-4182afc30891 | -8.54348 | -67.15373 | 2026-09-01 06:22:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 27dced94-8a9c-391f-8e5c-ec80178e45a1 | -8.89031 | -66.83607 | 2026-09-01 06:22:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 2fee582a-82f9-32a2-9574-c0639a6e7128 | -9.45285 | -67.46088 | 2026-09-01 06:22:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 4edbab83-fa7a-3117-a0fc-02f458c10471 | -8.93843 | -62.37137 | 2026-09-01 06:22:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 26388bff-5ca5-3d3a-b18d-feceafb7247e | -8.37026 | -70.84924 | 2026-09-01 06:22:00 | NOAA-21 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 267bcd3e-75b6-3908-aeba-8e7713e760f6 | -8.79877 | -71.04607 | 2026-09-01 06:22:00 | NOAA-21 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.1 |
| fc3c5599-bdde-34bc-aae9-6e7c61645cae | -8.90228 | -70.91199 | 2026-09-01 06:22:00 | NOAA-21 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 2f629e81-c79e-38bc-9a93-9d2a68bb96fd | -9.05762 | -65.48531 | 2026-09-01 06:22:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 4bbdf39a-aa3f-3111-b46a-4bf562ddeb6a | -8.60719 | -70.20363 | 2026-09-01 06:22:00 | NOAA-21 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f7633a6d-84f0-3af8-b8d7-4409c124e6ae | -8.45595 | -70.72495 | 2026-09-01 06:22:00 | NOAA-21 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 1e795cf0-d6ca-3aca-b7d3-1a8b991c2dd8 | -8.87013 | -66.77645 | 2026-09-01 06:22:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 73f7e33c-bf60-3c46-ba55-e842ef1ae22b | -9.27818 | -68.34824 | 2026-09-01 06:22:00 | NOAA-21 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 2.5 |
| c0f21f31-f8bb-3694-b167-4c39df6578db | -9.02767 | -65.44949 | 2026-09-01 06:22:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 13d6bbb8-82ab-3adb-8651-9d34028417dd | -8.59539 | -70.22797 | 2026-09-01 06:22:00 | NOAA-21 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b2ffe99a-7b6e-3ce6-91bd-cf1a32b01dcf | -8.91773 | -69.28053 | 2026-09-01 06:22:00 | NOAA-21 | MANOEL URBANO | ACRE | Brasil | 1200344 | 12 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9e65d78b-acd3-39db-ac60-b406b5785864 | -8.87842 | -66.88801 | 2026-09-01 06:22:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 4d51bdee-e277-3cd4-9b82-792a6d1f6668 | -8.79183 | -62.47956 | 2026-09-01 06:22:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 4bbf96da-22ba-3029-9fd6-2fd44065e587 | -9.61761 | -68.6021 | 2026-09-01 06:22:00 | NOAA-21 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 1.1 |
| df031e8e-1832-3526-974a-79c0c642c72b | -10.42163 | -64.45555 | 2026-09-01 06:22:00 | NOAA-21 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| ce96aa86-3183-3b3a-970b-5646d11bd14f | -8.93923 | -62.36498 | 2026-09-01 06:22:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 11042a23-c437-3e34-8edc-c622b51db9b8 | -9.02668 | -65.45723 | 2026-09-01 06:22:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 9a5493cc-48da-3819-92c1-007961c4cdbe | -8.88087 | -66.8918 | 2026-09-01 06:22:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 1033bf15-c767-3006-b8a2-a9ba0c8fc9c5 | -10.41547 | -64.45474 | 2026-09-01 06:22:00 | NOAA-21 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 511bbd86-002a-30b3-b9da-644a369e1b5e | -8.87573 | -66.89107 | 2026-09-01 06:22:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 4.4 |
| acac0614-6ca1-3977-9a36-8866b6732b9d | -8.86537 | -66.77255 | 2026-09-01 06:22:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d4eeb47f-11ba-3fb8-b3ba-cb85999b1180 | -10.42103 | -64.4605 | 2026-09-01 06:22:00 | NOAA-21 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 2.5 |
| c9b92a33-ccbe-315a-843a-fcea6e591581 | -10.13467 | -68.58743 | 2026-09-01 06:22:00 | NOAA-21 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 1.5 |


[Clique aqui para ver as próximas entradas](README88.md)
