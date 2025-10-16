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

## Dados Diários - Página 45

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| df5ce53e-e6a4-3b4f-a192-a75251e01e28 | -4.10189 | -48.02209 | 2025-10-16 04:38:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 2ff6d92e-41ce-34a5-9f1f-657d8eb90966 | -3.611 | -48.91861 | 2025-10-16 04:38:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 0a4e67b5-1cf4-39fa-a082-6c257ae0b549 | -7.95949 | -44.14441 | 2025-10-16 04:38:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| eee8be40-17fd-3e1a-a26a-578dfa4aa68c | -4.37062 | -43.38902 | 2025-10-16 04:38:00 | NOAA-21 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 16.3 |
| 02333ef3-7b6c-38f4-97b7-08c60f1a62d2 | -5.05249 | -45.90445 | 2025-10-16 04:38:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 0bffdb78-ba9f-3d88-98a6-b9aea2a6bd10 | -5.13669 | -46.1042 | 2025-10-16 04:38:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f5be3a36-3a54-345a-9ece-4f230b2c9d4f | -2.8696 | -50.73722 | 2025-10-16 04:38:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 8cee0ae5-538d-3d38-a2e4-d0775850c110 | -3.51051 | -50.21164 | 2025-10-16 04:38:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 2c662714-d504-3cb2-bfcc-e09d35b5e947 | -4.88141 | -48.63348 | 2025-10-16 04:38:00 | NOAA-21 | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| df96c0be-4aa1-357a-9ef3-ae070280ebad | -2.28561 | -48.362 | 2025-10-16 04:38:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 32ec73e0-5a23-3400-a9eb-0ee64bdf0fde | -3.08112 | -49.47701 | 2025-10-16 04:38:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7fa5e001-63c6-3792-845f-e10446a6e06a | -7.54341 | -42.06326 | 2025-10-16 04:38:00 | NOAA-21 | SANTO INÁCIO DO PIAUÍ | PIAUÍ | Brasil | 2209500 | 22 | 33 | nan | nan | nan | Caatinga | 3.1 |
| ca057a1b-e198-39e6-a221-faf9e09b9a35 | -4.10853 | -48.02311 | 2025-10-16 04:38:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 119.7 |
| 7632d784-117e-3f35-8dd5-ee4995490e21 | -8.23202 | -43.3244 | 2025-10-16 04:38:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| e4a24e41-e223-3082-bb33-fce382df2bed | -5.47232 | -42.92979 | 2025-10-16 04:38:00 | NOAA-21 | NAZÁRIA | PIAUÍ | Brasil | 2206720 | 22 | 33 | nan | nan | nan | Caatinga | 8.7 |
| 996bb52a-67bd-31dc-8a40-f9715a131845 | -4.37423 | -43.39347 | 2025-10-16 04:38:00 | NOAA-21 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 236.7 |
| d6df00c2-4739-3e4d-b032-cecd4875aeae | -4.00075 | -48.34335 | 2025-10-16 04:38:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 9dfb5b62-4b3b-3ad4-a220-43e8c0a5b766 | -6.16547 | -40.90368 | 2025-10-16 04:38:00 | NOAA-21 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| faf995ed-3f60-39bf-a035-7e59924c71cb | -8.29406 | -43.42498 | 2025-10-16 04:38:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 3.6 |
| 9f4cbd0b-1e7c-3954-816c-e5dec7b46542 | -6.57048 | -42.96226 | 2025-10-16 04:38:00 | NOAA-21 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| b4a3bf6a-1a89-3a2a-983f-57c419fb150e | -2.88392 | -50.73563 | 2025-10-16 04:38:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8e8d3acc-8f6a-37e9-b06d-30e27704b299 | -6.57558 | -42.95839 | 2025-10-16 04:38:00 | NOAA-21 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 2358d93b-f305-39c2-aa64-0038593f5151 | -4.96194 | -44.82127 | 2025-10-16 04:38:00 | NOAA-21 | JOSELÂNDIA | MARANHÃO | Brasil | 2105609 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 0fc37829-5045-38ee-a883-abae382a4584 | -4.67039 | -44.0912 | 2025-10-16 04:38:00 | NOAA-21 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 29c10ee1-ac8c-3a79-a2d6-6d1d91ccd894 | -4.50683 | -46.34297 | 2025-10-16 04:38:00 | NOAA-21 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1b63db0e-5de8-3015-9f63-900d7ce97568 | -8.228 | -44.01739 | 2025-10-16 04:38:00 | NOAA-21 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 3.5 |
| e24ef244-2bf9-3e37-8254-463b2d7d7cfd | -5.45815 | -41.02165 | 2025-10-16 04:38:00 | NOAA-21 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| cebb6083-832f-3761-8557-990b7cf65c16 | -4.1096 | -48.01616 | 2025-10-16 04:38:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| aca18312-b9a6-308d-9235-4b8262c945c3 | -6.7538 | -44.37425 | 2025-10-16 04:38:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| f1428a21-8338-3a33-bdf8-04f58d666519 | -8.07233 | -45.43556 | 2025-10-16 04:38:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 3bbedeae-7d88-3f23-b687-30c2752e8c11 | -3.56301 | -43.50442 | 2025-10-16 04:38:00 | NOAA-21 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| df18c1d5-a85b-3018-95e7-bdc4eb3d3c9d | -4.10628 | -48.01564 | 2025-10-16 04:38:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 4bd2639f-6ab2-3638-8293-4acd5e7bdcea | -7.67397 | -42.56376 | 2025-10-16 04:38:00 | NOAA-21 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 3.1 |
| 50c8c520-49a1-39a6-8b06-8317a760ad17 | -4.37533 | -43.38595 | 2025-10-16 04:38:00 | NOAA-21 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 64.2 |
| fdb6c090-cc18-3b55-aaff-a532b19a4b32 | -4.11014 | -48.01267 | 2025-10-16 04:38:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| c3849cd6-dcb9-37c5-9842-7c6bdf7a0d0b | -6.2262 | -42.49532 | 2025-10-16 04:38:00 | NOAA-21 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 3.8 |
| 122c02c0-c28c-39b4-962c-1c5042ef44a7 | -6.14816 | -44.21556 | 2025-10-16 04:38:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 0.4 |
| e79b8020-65d7-3696-b733-30e8c41447fe | -7.00856 | -43.74882 | 2025-10-16 04:38:00 | NOAA-21 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 6.1 |
| adf20869-47d2-3400-b89d-6c8c1f460d38 | -6.15532 | -40.90199 | 2025-10-16 04:38:00 | NOAA-21 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| a4736e52-5c89-31fa-b7a5-ddd75f8403be | -3.12534 | -50.21037 | 2025-10-16 04:38:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 13d3e169-a715-36ea-ad30-2d37db89e0cb | -6.75483 | -44.36715 | 2025-10-16 04:38:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 12.0 |
| 96710dfb-62de-306b-af8f-64f04ad0e424 | -7.04161 | -43.49425 | 2025-10-16 04:38:00 | NOAA-21 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 55af9e48-87b6-3e50-a022-73098a6e4a02 | -7.85239 | -45.40389 | 2025-10-16 04:38:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 20951a0b-3ade-36f5-a00a-ca6e2c7620de | -3.22213 | -48.92761 | 2025-10-16 04:38:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| f1b2aa6e-2a4d-3d2d-9f58-058f79f81e01 | -6.53554 | -44.68952 | 2025-10-16 04:38:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 8ea9d19e-6e77-3c06-9a26-e1d653f4784b | -6.32876 | -44.31959 | 2025-10-16 04:38:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| e1f3824b-f119-301e-9552-63d0d9910fe5 | -5.13875 | -43.34265 | 2025-10-16 04:38:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| cf67e84e-9898-335c-b1f8-a77a12a68eeb | -8.24154 | -43.41567 | 2025-10-16 04:38:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 0e27662f-1148-3dcf-ae81-48c1eae9c872 | -8.29333 | -43.39793 | 2025-10-16 04:38:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| dffc23d0-bd59-3566-ab43-7e18369fd6d5 | -7.39598 | -39.69918 | 2025-10-16 04:38:00 | NOAA-21 | EXU | PERNAMBUCO | Brasil | 2605301 | 26 | 33 | nan | nan | nan | Caatinga | 8.4 |
| 47aa2224-6c43-39f9-8eef-8d4af59c0a95 | -6.40227 | -43.48325 | 2025-10-16 04:38:00 | NOAA-21 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 0b901163-c711-3630-986d-5316150deb98 | -5.102 | -44.94399 | 2025-10-16 04:38:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 15cc47f4-e0d5-34a6-93ef-cb804ef70a5a | -7.20542 | -45.4917 | 2025-10-16 04:38:00 | NOAA-21 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| ed96f054-9c5c-3ed5-a7e1-f2629f5b18de | -2.87362 | -50.73402 | 2025-10-16 04:38:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 4420c73c-9fdf-3e03-9ed4-2b4a7d354134 | -5.38832 | -42.79622 | 2025-10-16 04:38:00 | NOAA-21 | NAZÁRIA | PIAUÍ | Brasil | 2206720 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 09f28ea1-09a0-3761-9eb1-95bd9bb6edb3 | -4.42617 | -47.75274 | 2025-10-16 04:38:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| ae0092ad-7ff5-34f5-9efe-c0fc7607726e | -1.95919 | -50.80818 | 2025-10-16 04:38:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ed10ea75-53bd-3b65-870e-2f504149d304 | -5.12393 | -50.42137 | 2025-10-16 04:38:00 | NOAA-21 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d2747cde-5c83-33dd-bc08-96d33b209712 | -6.1119 | -47.29402 | 2025-10-16 04:38:00 | NOAA-21 | CAMPESTRE DO MARANHÃO | MARANHÃO | Brasil | 2102556 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 48bbdcfd-f8a1-3f6d-9c77-582923f4c97e | -5.91773 | -42.83923 | 2025-10-16 04:38:00 | NOAA-21 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 501fb67f-4de1-3a8a-b873-3354f54d2e79 | -5.7325 | -48.97859 | 2025-10-16 04:38:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5afdb650-b780-3214-8394-ac5afe1150f0 | -8.20601 | -43.3161 | 2025-10-16 04:38:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 5.7 |
| a840dacd-c19c-3b7b-8de1-95893700d3a6 | -6.19718 | -44.10965 | 2025-10-16 04:38:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| aa131326-198f-3c4b-bc1e-b2a93ad84620 | -4.16062 | -46.79404 | 2025-10-16 04:38:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.7 |
| aea506fc-2c9e-32d7-81f2-171f3cdf312a | -4.15718 | -46.79351 | 2025-10-16 04:38:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 2bc9af1e-0964-3a79-8b65-6e7e7398f6cd | -6.26395 | -42.89901 | 2025-10-16 04:38:00 | NOAA-21 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| a0b2f079-670f-3939-a47e-492db213620d | -6.12492 | -44.28915 | 2025-10-16 04:38:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| ffd4b95c-f33c-3791-8cd9-e6eb2992cda7 | -5.42736 | -40.98362 | 2025-10-16 04:38:00 | NOAA-21 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 3.3 |
| 504ee011-cb9c-3e52-9091-31fdf427d265 | -7.22719 | -41.2148 | 2025-10-16 04:38:00 | NOAA-21 | FRANCISCO SANTOS | PIAUÍ | Brasil | 2204204 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| db1b7718-dd2e-3f99-94c4-764fe0912215 | -8.18333 | -43.96602 | 2025-10-16 04:38:00 | NOAA-21 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| e0870a02-ef2d-35a3-8e62-f8e28284b117 | -7.40812 | -44.7492 | 2025-10-16 04:38:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 7516736f-e691-3f6a-90be-561aafa7f971 | -4.67681 | -44.10275 | 2025-10-16 04:38:00 | NOAA-21 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| dad6d1e1-066a-3f13-95cc-621e5e3bcfa3 | -5.70119 | -49.30846 | 2025-10-16 04:38:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5dae4a90-38b7-3d38-9a0a-c5aee66744b3 | -8.19974 | -43.97255 | 2025-10-16 04:38:00 | NOAA-21 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b8fd7efb-209a-34bf-be51-baa248e636a5 | -7.39832 | -44.74455 | 2025-10-16 04:38:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 8bdad297-f8a6-3afc-b32b-c52355da6d38 | -8.21078 | -43.98641 | 2025-10-16 04:38:00 | NOAA-21 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| ef48fcf9-9160-391e-8870-f18b560d1782 | -4.28687 | -48.6246 | 2025-10-16 04:38:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 2f63685d-2932-3f1e-8e61-ca1ed5034c08 | -5.68395 | -45.09573 | 2025-10-16 04:38:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 14.4 |
| a5fb3df4-c844-38cd-bf61-4da3f42a5518 | -8.25653 | -44.09324 | 2025-10-16 04:38:00 | NOAA-21 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| b3e2e04c-494f-320c-8fbc-314cd921fa11 | -4.64229 | -43.12785 | 2025-10-16 04:38:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 92764abe-b357-394d-aa84-d8944b399ce3 | -4.67177 | -44.10906 | 2025-10-16 04:38:00 | NOAA-21 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| d9e8b300-bb24-3bcf-ac10-ca3dd6158b79 | -5.87265 | -42.8063 | 2025-10-16 04:38:00 | NOAA-21 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| c3f165d7-e722-30f4-86eb-fb90a2fe9537 | -5.13818 | -43.34659 | 2025-10-16 04:38:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 1b77048f-c429-3c59-bddc-507799c8868d | -1.48636 | -55.44181 | 2025-10-16 04:38:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| f969958f-f563-3540-b4ed-2dfc58bb4e5e | -7.62716 | -44.08204 | 2025-10-16 04:38:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 6416e6b6-5c43-3cf5-ae9f-c9ce33bf8a3f | -7.06897 | -44.74546 | 2025-10-16 04:38:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| c7f2f4dd-b38d-30e1-9217-5bb14fbfd893 | -5.43471 | -44.22949 | 2025-10-16 04:38:00 | NOAA-21 | GRAÇA ARANHA | MARANHÃO | Brasil | 2104701 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 2dc2af57-52ea-3185-9862-4373b1bb3eac | -7.96533 | -44.13324 | 2025-10-16 04:38:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 4ac2751f-2c44-3b63-a87a-de88e21cb411 | -3.96579 | -50.06446 | 2025-10-16 04:38:00 | NOAA-21 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2872ad8d-4342-3601-ad0f-91eeb1c99266 | -7.11626 | -44.7197 | 2025-10-16 04:38:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 740a2d22-879d-3d0e-82e0-ca074b6ee70e | -3.29237 | -50.14798 | 2025-10-16 04:38:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f5190290-b0d6-3506-bef7-9223aed87b8c | -7.20513 | -43.64491 | 2025-10-16 04:38:00 | NOAA-21 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 8e0a370b-9b53-3188-9a4c-b1acd40e0547 | -4.95963 | -45.09622 | 2025-10-16 04:38:00 | NOAA-21 | LAGO DA PEDRA | MARANHÃO | Brasil | 2105708 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 6233fd56-c17f-35fe-8230-2609b3d25b5f | -7.55469 | -43.92012 | 2025-10-16 04:38:00 | NOAA-21 | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 8f929546-664c-38d0-8a0b-71b11a66e458 | -3.48821 | -50.09129 | 2025-10-16 04:38:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 5c262acd-6fb2-3d5b-a9d5-53632b74395d | -2.72979 | -48.59359 | 2025-10-16 04:38:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e5fd8a82-658a-3138-8046-d84e2a8965e7 | -4.4206 | -40.18103 | 2025-10-16 04:38:00 | NOAA-21 | SANTA QUITÉRIA | CEARÁ | Brasil | 2312205 | 23 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 7f8a615d-cd57-3714-bb73-433dcd7f28d3 | -6.06503 | -44.30485 | 2025-10-16 04:38:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 286f0eae-1c4e-311f-a848-fbbcd480872c | -6.25231 | -44.01504 | 2025-10-16 04:38:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 0c50cc15-06d9-3e68-8193-4614a4c1214c | -5.17334 | -46.41476 | 2025-10-16 04:38:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |


[Clique aqui para ver as próximas entradas](README46.md)
