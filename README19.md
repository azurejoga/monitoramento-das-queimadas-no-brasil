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

## Dados Diários - Página 19

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| d113ba29-035b-3553-ac8b-bfa6ab58eb36 | -3.43234 | -50.24309 | 2025-11-05 04:12:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c0bc37a8-a158-332c-ae25-9e0b602eb749 | -4.04659 | -43.47748 | 2025-11-05 04:12:00 | NOAA-20 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f34752a0-5cc4-38e5-b1ce-6196a6b3dea7 | -3.82272 | -48.67092 | 2025-11-05 04:12:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 46c6ff4d-ffac-348f-b9de-4499e34f0406 | -2.62045 | -49.23053 | 2025-11-05 04:12:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 123ce9bb-e65b-3bac-a856-82be77ed62e1 | -5.15033 | -41.21372 | 2025-11-05 04:12:00 | NOAA-20 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| b3c5f2b6-859d-369e-a003-f2f60f2d8506 | -2.8149 | -54.35858 | 2025-11-05 04:12:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 08ef7aaa-85fe-356e-85cc-3bc4543e92b1 | -2.27084 | -47.85689 | 2025-11-05 04:12:00 | NOAA-20 | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 5d5d37bb-1fbf-3a36-9c81-9485df45fe38 | -5.14753 | -41.20953 | 2025-11-05 04:12:00 | NOAA-20 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 0.5 |
| be72ab2d-d355-3f52-a35a-d7d0ea4e9965 | -4.28235 | -47.17858 | 2025-11-05 04:12:00 | NOAA-20 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 59501f81-2b38-3f67-88c3-c5967935333b | -3.57054 | -50.64172 | 2025-11-05 04:12:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| fe4db185-3816-3d47-a2f7-fac726727661 | -4.72036 | -48.30707 | 2025-11-05 04:12:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| c99f9c84-488b-3293-b458-d4beb07c9d6f | -4.55658 | -45.59335 | 2025-11-05 04:12:00 | NOAA-20 | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| c7e8c57b-d6a9-33f0-93e9-4cf428792597 | -3.84206 | -49.91034 | 2025-11-05 04:12:00 | NOAA-20 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| b09880df-2796-3e72-8089-1fcb8b31bbde | -3.41309 | -44.43903 | 2025-11-05 04:12:00 | NOAA-20 | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 7.0 |
| ce2b32a7-1ebf-3ad0-850b-82f94ac9327a | -4.46155 | -43.21819 | 2025-11-05 04:12:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 155bb7ce-1b36-3028-a114-6fd3cd26be9a | -3.57028 | -50.64426 | 2025-11-05 04:12:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| af9f8457-0b9e-3b2c-81e5-454325318b49 | -4.28321 | -45.66585 | 2025-11-05 04:12:00 | NOAA-20 | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c59d4197-1ece-3050-a236-025af20cd3fb | -4.45437 | -43.22062 | 2025-11-05 04:12:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 25.8 |
| 3b61f922-0d50-3b82-ac58-3f68529ac773 | -4.51011 | -45.43404 | 2025-11-05 04:12:00 | NOAA-20 | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2ccd18a6-8ecf-3d39-9432-ab4b565189ed | -4.38014 | -46.26949 | 2025-11-05 04:12:00 | NOAA-20 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ee83277d-f296-37e8-b1e4-6b733a3174f5 | -4.71008 | -45.63404 | 2025-11-05 04:12:00 | NOAA-20 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 26ac82e2-fa10-3fea-bb3a-2728075c395a | -3.48098 | -43.63789 | 2025-11-05 04:12:00 | NOAA-20 | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| c20740b0-a77f-372a-9c58-222b74e65fbc | -3.12927 | -44.4839 | 2025-11-05 04:12:00 | NOAA-20 | ANAJATUBA | MARANHÃO | Brasil | 2100709 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 85b528d5-0c0d-38be-8b5f-cba1602df5b8 | -2.82034 | -45.15245 | 2025-11-05 04:12:00 | NOAA-20 | PALMEIRÂNDIA | MARANHÃO | Brasil | 2107605 | 21 | 33 | nan | nan | nan | Amazônia | 27.1 |
| e5d40a35-ccf6-325e-a745-61aac8f89f04 | -3.48489 | -43.63487 | 2025-11-05 04:12:00 | NOAA-20 | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 5c637f8c-efd0-3924-b274-62c446b1abc7 | -5.32201 | -41.24014 | 2025-11-05 04:12:00 | NOAA-20 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 5.1 |
| a8b77a16-2020-32ac-a4e0-6ad812b65593 | -3.61226 | -40.37698 | 2025-11-05 04:12:00 | NOAA-20 | MERUOCA | CEARÁ | Brasil | 2308203 | 23 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 1a24dc88-b5e2-3262-8f79-dd1db79cca94 | -5.51881 | -41.14041 | 2025-11-05 04:12:00 | NOAA-20 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 0e3a8ddb-f40c-313a-b7bc-b047f80ab5c5 | -5.4778 | -43.58243 | 2025-11-05 04:12:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 43.8 |
| 5e527a70-f117-34a2-9245-6660aac84e83 | -3.49049 | -43.62123 | 2025-11-05 04:12:00 | NOAA-20 | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| bf91c137-52f6-391a-9f10-696f3edf5fec | -3.64507 | -44.43635 | 2025-11-05 04:12:00 | NOAA-20 | CANTANHEDE | MARANHÃO | Brasil | 2102705 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 0c5c0774-870e-35dd-b268-07186b44fb6a | -4.4737 | -43.22721 | 2025-11-05 04:12:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 18.2 |
| 33396a0d-65b0-3382-9806-4d4f45c53616 | -4.36443 | -48.35989 | 2025-11-05 04:12:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| dbc9e0cb-7407-30f4-945a-417bcf6ebf56 | -5.3782 | -44.74068 | 2025-11-05 04:12:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 7b006c5b-c623-3aca-bf37-dc61012b8058 | -3.48196 | -45.40377 | 2025-11-05 04:12:00 | NOAA-20 | MONÇÃO | MARANHÃO | Brasil | 2106904 | 21 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 3d9b9f73-e952-33f9-8e39-55816426ba89 | -4.36175 | -50.8885 | 2025-11-05 04:12:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 823f415d-230f-383a-9e69-efb778131d3d | -5.06374 | -44.73392 | 2025-11-05 04:12:00 | NOAA-20 | JOSELÂNDIA | MARANHÃO | Brasil | 2105609 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 7afc8dc3-dea6-374d-a08a-07d1362016be | -2.72853 | -47.38972 | 2025-11-05 04:12:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| f201f59e-6da1-363f-a30d-ebfceea120fa | -2.82896 | -49.41442 | 2025-11-05 04:12:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 82885bf4-a987-33d3-b77d-9648d24fb836 | -6.1055 | -41.70512 | 2025-11-05 04:12:00 | NOAA-20 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 12df9afc-a89d-367d-a0ab-701ac6bf10ae | -4.29284 | -43.78713 | 2025-11-05 04:12:00 | NOAA-20 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 0b205208-0581-3adf-bc04-11db0f85ecd5 | -4.29784 | -43.79879 | 2025-11-05 04:12:00 | NOAA-20 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 032ad9e8-d10a-3de6-8784-8f6c07d3d7a3 | -4.61391 | -45.70655 | 2025-11-05 04:12:00 | NOAA-20 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2fd090e6-984e-3e6a-8b15-4936de082110 | -6.09704 | -41.70059 | 2025-11-05 04:12:00 | NOAA-20 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| e9a8a9ff-d37f-3862-b880-aec61195dc5b | -5.26668 | -44.14125 | 2025-11-05 04:12:00 | NOAA-20 | GOVERNADOR EUGÊNIO BARROS | MARANHÃO | Brasil | 2104602 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 44804c55-f289-3b38-b538-ed1a178f0c62 | -3.87004 | -44.43338 | 2025-11-05 04:12:00 | NOAA-20 | MATÕES DO NORTE | MARANHÃO | Brasil | 2106631 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 29677da5-c9be-3ab6-8214-8ade40e642f0 | -4.50656 | -45.43351 | 2025-11-05 04:12:00 | NOAA-20 | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 7f8d8304-fd42-3b66-9547-303f41d965ad | -3.06448 | -47.77886 | 2025-11-05 04:12:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 80c286a4-bbd9-31e7-a1ad-37a82934e79d | -4.30661 | -41.46028 | 2025-11-05 04:12:00 | NOAA-20 | PEDRO II | PIAUÍ | Brasil | 2207900 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 432352a1-ff47-33e6-96ca-289e60218d6f | -3.96375 | -43.78267 | 2025-11-05 04:12:00 | NOAA-20 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 9.7 |
| fc56bac7-8cb2-31d6-92b2-3c96e9995f96 | -5.46784 | -43.58086 | 2025-11-05 04:12:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| c7659572-a43e-3910-9ecb-4d82f89e0dd2 | -3.66693 | -44.79997 | 2025-11-05 04:12:00 | NOAA-20 | VITÓRIA DO MEARIM | MARANHÃO | Brasil | 2112902 | 21 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 7f106eac-ec68-39be-8063-fb79fabdb870 | -4.15583 | -46.79483 | 2025-11-05 04:12:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 932a9ddc-8e38-32e3-a11a-7bf1df9c64cf | -3.49551 | -43.6329 | 2025-11-05 04:12:00 | NOAA-20 | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 5.1 |
| b1f46ef9-7f7c-3a46-82eb-15b8d5e2d803 | -6.1016 | -41.70813 | 2025-11-05 04:12:00 | NOAA-20 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 6291b8bf-4274-3b50-b6b9-23dc15522259 | -1.29428 | -49.15272 | 2025-11-05 04:12:00 | NOAA-20 | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | 7.9 |
| 125f3f62-499c-3a29-969e-e11ab53b6c9e | -3.49328 | -43.62529 | 2025-11-05 04:12:00 | NOAA-20 | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 522cf254-04e5-3797-a7f8-8e7f2ca4b853 | -5.0336 | -43.6194 | 2025-11-05 04:12:00 | NOAA-20 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 51.4 |
| 4990a52e-4771-31d5-9b91-857e17c16ac3 | -3.49187 | -50.46381 | 2025-11-05 04:12:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 12a3d27c-be21-31dd-bed0-a67aef1e7431 | -4.76546 | -42.6517 | 2025-11-05 04:12:00 | NOAA-20 | JOSÉ DE FREITAS | PIAUÍ | Brasil | 2205508 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| abe0ddc0-1cf6-3918-b1b6-3704cdd487dd | -3.42445 | -49.16996 | 2025-11-05 04:12:00 | NOAA-20 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 5c149e36-567c-39f9-a463-a2a89ac3ca10 | -5.03027 | -43.61888 | 2025-11-05 04:12:00 | NOAA-20 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 1ba30e45-0ad1-3364-aeba-dbb0438ae713 | -2.44819 | -49.0154 | 2025-11-05 04:12:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 4cbc5d51-47a8-368a-8c2c-481f6543aa02 | -4.66193 | -44.52633 | 2025-11-05 04:12:00 | NOAA-20 | PEDREIRAS | MARANHÃO | Brasil | 2108207 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 0070b76d-6186-3c67-9717-cb11f7777144 | -3.86418 | -41.01149 | 2025-11-05 04:12:00 | NOAA-20 | UBAJARA | CEARÁ | Brasil | 2313609 | 23 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 00e9e876-c957-373e-a690-9fcaca0af93e | -4.86695 | -45.4229 | 2025-11-05 04:12:00 | NOAA-20 | LAGOA GRANDE DO MARANHÃO | MARANHÃO | Brasil | 2105963 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| b0400669-e634-3c7f-85bc-3d617eed4130 | -4.91969 | -46.72466 | 2025-11-05 04:12:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 0dd5e5a0-874d-377a-acec-c7061815bebc | -2.55512 | -45.33906 | 2025-11-05 04:12:00 | NOAA-20 | PRESIDENTE SARNEY | MARANHÃO | Brasil | 2109270 | 21 | 33 | nan | nan | nan | Amazônia | 6.0 |
| b293cf60-f3f3-35da-95d3-9c42a613f7b5 | -2.8352 | -48.83372 | 2025-11-05 04:12:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 631a74a2-e339-3f65-aefa-5e1c6dd66641 | -4.52723 | -40.35155 | 2025-11-05 04:12:00 | NOAA-20 | HIDROLÂNDIA | CEARÁ | Brasil | 2305209 | 23 | 33 | nan | nan | nan | Caatinga | 0.7 |
| a4e4d617-9bc8-3fe5-b6f4-6613c3ac960b | -3.49216 | -43.63238 | 2025-11-05 04:12:00 | NOAA-20 | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 90d805fb-c00d-3cb9-91ad-50976f1b3dfb | -4.21834 | -48.35197 | 2025-11-05 04:12:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 15560c43-0d25-33cd-b30f-76a24f839ebe | -4.22227 | -45.82872 | 2025-11-05 04:12:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 72d6924d-d3a3-3348-a814-c68d141df28f | -5.93151 | -41.34747 | 2025-11-05 04:12:00 | NOAA-20 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 8af19840-814a-3664-957e-50982b31f3b6 | -5.54718 | -40.52478 | 2025-11-05 04:12:00 | NOAA-20 | INDEPENDÊNCIA | CEARÁ | Brasil | 2305605 | 23 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 1e3cfd25-0cb3-309c-8315-8e2702a684ef | -3.28636 | -42.1826 | 2025-11-05 04:12:00 | NOAA-20 | MAGALHÃES DE ALMEIDA | MARANHÃO | Brasil | 2106300 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| b41ceb37-10f6-35ab-acf1-1601fb45bbe6 | -4.50947 | -45.43802 | 2025-11-05 04:12:00 | NOAA-20 | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| b133dda4-c9f7-35d5-b96b-d99164bde5c9 | -5.51765 | -44.05364 | 2025-11-05 04:12:00 | NOAA-20 | GOVERNADOR LUIZ ROCHA | MARANHÃO | Brasil | 2104628 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| f99105a9-b90c-3218-9e78-a0cded902d36 | -3.96711 | -43.78319 | 2025-11-05 04:12:00 | NOAA-20 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 6e78bc7d-c387-3097-9906-786b15552513 | -5.57327 | -37.89315 | 2025-11-05 04:12:00 | NOAA-20 | APODI | RIO GRANDE DO NORTE | Brasil | 2401008 | 24 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 2d8f95fc-5018-3515-ba9a-3080b170e3e4 | -5.78873 | -40.82509 | 2025-11-05 04:12:00 | NOAA-20 | QUITERIANÓPOLIS | CEARÁ | Brasil | 2311264 | 23 | 33 | nan | nan | nan | Caatinga | 1.9 |
| cdca1c20-2e52-3625-84a2-ffbc85c18232 | -2.4873 | -45.98226 | 2025-11-05 04:12:00 | NOAA-20 | MARANHÃOZINHO | MARANHÃO | Brasil | 2106375 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c0609a79-5816-36cf-a8c4-d6383f34d3f0 | -3.30942 | -53.84412 | 2025-11-05 04:12:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 8ddef481-eeb7-3815-868d-183e500b2985 | -2.48399 | -49.22993 | 2025-11-05 04:12:00 | NOAA-20 | MOCAJUBA | PARÁ | Brasil | 1504604 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9f790b66-d2cf-35cc-bcf8-2de216d5803b | -2.78176 | -50.31919 | 2025-11-05 04:12:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 9.2 |
| 3f9f6266-cf00-3d65-a55c-6661038f749d | -4.11282 | -43.87577 | 2025-11-05 04:12:00 | NOAA-20 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f1cd0ff4-c9f1-3605-a014-a438c171697b | -4.51075 | -45.43007 | 2025-11-05 04:12:00 | NOAA-20 | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| cb40f936-69f1-36ec-89bd-80692c4c3965 | -5.37137 | -44.73958 | 2025-11-05 04:12:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 85050ce9-39bf-3416-92bd-1a073dec4d5d | -3.24203 | -50.79115 | 2025-11-05 04:12:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| a858cf02-f020-35f1-ad2d-59acdd5ab6d9 | -6.07754 | -41.78129 | 2025-11-05 04:12:00 | NOAA-20 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 4e19f10e-b322-3f36-b161-b34944b7e21f | -6.11597 | -41.63711 | 2025-11-05 04:12:00 | NOAA-20 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| f1a8310d-2480-3e9f-b2e5-f6b996f67f54 | -1.27083 | -49.14888 | 2025-11-05 04:12:00 | NOAA-20 | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 36ef14c4-3aa5-3638-bcaf-02ff54d0276d | -3.23836 | -46.876 | 2025-11-05 04:12:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 7557b5bf-98ef-3f36-8a87-291f3f46a355 | -3.88028 | -49.1151 | 2025-11-05 04:12:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 02ae47c2-26a6-3f80-b927-8cbb425f4e49 | -5.96317 | -42.72768 | 2025-11-05 04:12:00 | NOAA-20 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 83962458-b091-39c0-878b-0be1948c4a5d | -3.60454 | -50.62336 | 2025-11-05 04:12:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 66b72e21-b24a-3284-ab22-60ac6111b8f5 | -2.31934 | -48.5955 | 2025-11-05 04:12:00 | NOAA-20 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| f9a8ad25-8eb0-3ea4-9525-c34a55e2cf9f | -3.49749 | -50.46583 | 2025-11-05 04:12:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 06caef7c-9054-3b67-9557-54f88381f067 | -3.78925 | -51.31705 | 2025-11-05 04:12:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 389c63cd-b417-38f1-9390-04c405fd738a | -4.59487 | -45.62872 | 2025-11-05 04:12:00 | NOAA-20 | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |


[Clique aqui para ver as próximas entradas](README20.md)
