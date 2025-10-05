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

## Dados Diários - Página 76

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 55bf3c48-3cda-3af9-b878-6c16f2071dcc | -6.64062 | -42.77914 | 2025-10-05 04:44:00 | NOAA-21 | FRANCISCO AYRES | PIAUÍ | Brasil | 2204105 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| bac99350-94ec-3d6f-9846-009b800a9d93 | -6.10667 | -43.47597 | 2025-10-05 04:44:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 52c3d5d2-f866-37ef-ac9a-e1d6682a2c42 | -5.79107 | -42.92939 | 2025-10-05 04:44:00 | NOAA-21 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 47a019c3-c400-3479-8273-591a1280946e | -5.85295 | -45.82579 | 2025-10-05 04:44:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ab546510-df0f-3fe8-8621-562c27a5cac6 | -6.25244 | -45.3396 | 2025-10-05 04:44:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 8e673ef1-ec2c-3e5c-91ef-aa00f23655b3 | -5.87017 | -43.55525 | 2025-10-05 04:44:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| c68f248f-62a1-3079-b045-176bc5957704 | -6.27505 | -44.03522 | 2025-10-05 04:44:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| fc838b2e-5b53-315d-9c45-371477bea203 | -5.47407 | -43.17449 | 2025-10-05 04:44:00 | NOAA-21 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 5e05b489-666d-3754-bd87-293d5d63d1fe | -5.83431 | -45.81177 | 2025-10-05 04:44:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 8355bee6-2d6d-320e-bd99-391ef308c5e0 | -6.40778 | -43.04861 | 2025-10-05 04:44:00 | NOAA-21 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 19.9 |
| 271f98d2-615a-34be-b426-8a6f652de7ae | -6.33442 | -43.45761 | 2025-10-05 04:44:00 | NOAA-21 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| e3109fdf-6c49-3792-961c-5417db5d75b6 | -4.82328 | -42.77043 | 2025-10-05 04:44:00 | NOAA-21 | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Cerrado | 4.9 |
| e4a76df2-70d8-3d91-8515-61362bb7a496 | -5.53992 | -45.15174 | 2025-10-05 04:44:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 6ee29102-7aad-3597-ae4c-e23d914a7185 | -6.1605 | -44.66449 | 2025-10-05 04:44:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 30.4 |
| a782ec85-fd5c-309b-baef-a6154532a2f5 | -4.44823 | -43.23024 | 2025-10-05 04:44:00 | NOAA-21 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 16.3 |
| e02573ea-358c-3309-8533-f46f354bf83f | -5.85186 | -42.78321 | 2025-10-05 04:44:00 | NOAA-21 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 7f8132dd-8a0f-3c0e-bada-429938a6e805 | -6.65466 | -41.58635 | 2025-10-05 04:44:00 | NOAA-21 | INHUMA | PIAUÍ | Brasil | 2204709 | 22 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 8378c5e8-42a0-3070-8eb6-a98ca49219b9 | -6.25608 | -45.34417 | 2025-10-05 04:44:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 5.0 |
| f2250d8d-58f6-3deb-9ce2-6ccb0925e2f9 | -2.8918 | -50.72937 | 2025-10-05 04:44:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1ef5c22f-a6b2-3329-92e2-53ca5dd0eae1 | -5.74212 | -42.54182 | 2025-10-05 04:44:00 | NOAA-21 | BARRO DURO | PIAUÍ | Brasil | 2201408 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 0bd416f9-2d15-3b59-8c1b-65ef2856044e | -5.21514 | -46.18182 | 2025-10-05 04:44:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 50555a13-71ef-3cbd-be42-c13ef0b44853 | -2.9017 | -50.7309 | 2025-10-05 04:44:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 1d1f01af-8eff-350d-802f-7c015e9e0835 | -5.12664 | -46.23661 | 2025-10-05 04:44:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 93dde727-1745-3463-be19-dc95290127dc | -5.00787 | -47.21574 | 2025-10-05 04:44:00 | NOAA-21 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| fb6a91cc-bc78-3666-9ed6-4ee9e9ba08ef | -5.90337 | -45.65228 | 2025-10-05 04:44:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 146a43c1-b589-3962-8c44-513e63f21945 | -4.25278 | -48.56008 | 2025-10-05 04:44:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 00c6307e-73be-3d46-b5cf-a215f7e9d46c | -5.09063 | -37.60695 | 2025-10-05 04:44:00 | NOAA-21 | BARAÚNA | RIO GRANDE DO NORTE | Brasil | 2401453 | 24 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 3659ef50-a48b-31a9-b91c-1851140b94ba | -6.23346 | -44.3827 | 2025-10-05 04:44:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 172a917a-e804-3495-b168-1cc692e2f33d | -5.90297 | -43.75873 | 2025-10-05 04:44:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 1c1ff7f1-70e2-3f64-bbcd-6b63839cb5f0 | -2.57153 | -48.96416 | 2025-10-05 04:44:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 4ff18562-1640-3d83-b77a-2d78a08f30cf | -3.60895 | -51.03981 | 2025-10-05 04:44:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 91f99c9e-951b-3551-9b27-b8f9bf3d9e21 | -6.33088 | -43.90271 | 2025-10-05 04:44:00 | NOAA-21 | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 4b404ef7-76a7-38ab-854b-461a9fdd9206 | -3.84637 | -41.58535 | 2025-10-05 04:44:00 | NOAA-21 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 3.9 |
| e94ddf37-8493-376d-b923-f3a31e68b727 | -6.40177 | -42.69247 | 2025-10-05 04:44:00 | NOAA-21 | AMARANTE | PIAUÍ | Brasil | 2200509 | 22 | 33 | nan | nan | nan | Caatinga | 4.2 |
| 7ac999b8-ddac-30ee-a039-3afd2d764121 | -5.85348 | -45.82222 | 2025-10-05 04:44:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f024d72f-cd5d-3947-b646-bac88cb57adb | -6.42733 | -44.47105 | 2025-10-05 04:44:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 4ce813fa-356c-3f2c-9951-c63d78938717 | -5.43743 | -45.50545 | 2025-10-05 04:44:00 | NOAA-21 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 743067a9-4292-3c7f-ac3b-98ebfa5f477d | -5.7643 | -45.80553 | 2025-10-05 04:44:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ab05b329-b8a0-3ce5-aecb-65af737c304a | -4.64065 | -43.18188 | 2025-10-05 04:44:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 20.9 |
| b7810166-b415-33b6-b650-adc287e40173 | -3.95363 | -49.90038 | 2025-10-05 04:44:00 | NOAA-21 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| fdf03026-e513-3d1d-a1f3-2d822f4fd3da | -6.52774 | -43.36946 | 2025-10-05 04:44:00 | NOAA-21 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| e85a9f62-8aec-398b-8604-b8b70b9308a5 | -3.3955 | -50.27449 | 2025-10-05 04:44:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 588f205e-15b4-3126-834d-250fa6386954 | -6.70125 | -41.95354 | 2025-10-05 04:44:00 | NOAA-21 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 261d7059-28b8-3d09-a686-b2e6dcbd6e2e | -4.56883 | -48.6037 | 2025-10-05 04:44:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6cd6b0cd-5116-3484-aaa4-1c3ce274fff5 | -3.54158 | -49.50935 | 2025-10-05 04:44:00 | NOAA-21 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4c2d32de-1389-380e-a48e-64725f79719f | -6.29189 | -43.91956 | 2025-10-05 04:44:00 | NOAA-21 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 8aef82dc-65e2-3254-8c85-10f332004c08 | -3.78529 | -52.11756 | 2025-10-05 04:44:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 074aab1c-9fb8-3e93-9606-95a45d83e953 | -2.89732 | -50.73727 | 2025-10-05 04:44:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 638abfb4-f3d4-3ef4-a8b5-4d38f8577a58 | -5.85449 | -42.80071 | 2025-10-05 04:44:00 | NOAA-21 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 206b5b8c-c189-3157-86ae-1aff8d88df5e | -6.15357 | -44.65031 | 2025-10-05 04:44:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 4fa7648c-4a74-3005-a108-f3da44f3c1c3 | -5.78614 | -45.79778 | 2025-10-05 04:44:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 2e4821fc-a4a1-3995-8143-11464fe98a26 | -7.00996 | -40.3164 | 2025-10-05 04:44:00 | NOAA-21 | CAMPOS SALES | CEARÁ | Brasil | 2302701 | 23 | 33 | nan | nan | nan | Caatinga | 3.2 |
| 782659dd-0d6e-3c2a-bf23-3207251dfebe | -6.70938 | -42.17163 | 2025-10-05 04:44:00 | NOAA-21 | TANQUE DO PIAUÍ | PIAUÍ | Brasil | 2210979 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 27f29328-171d-3d65-a30c-e7fd31e8d3d5 | -3.05114 | -51.1007 | 2025-10-05 04:44:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 802c795e-497a-3a96-b8a6-c06c27f4e8d6 | -2.6915 | -48.39373 | 2025-10-05 04:44:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| f0e2eefb-5a26-3d91-9372-30bd49f5e609 | -5.82165 | -45.81355 | 2025-10-05 04:44:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 52e5f76f-3f53-36ef-9b61-1b384febea14 | -5.92798 | -43.32201 | 2025-10-05 04:44:00 | NOAA-21 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 968b2a62-3c06-33da-9783-fc903d2ba4a5 | -6.21309 | -44.07485 | 2025-10-05 04:44:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 6eaee269-c847-3ef9-91c7-5444d508e4d6 | -5.00486 | -47.21078 | 2025-10-05 04:44:00 | NOAA-21 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| d69b841d-0344-3519-9811-bfdc58c6eb63 | -5.79231 | -45.78415 | 2025-10-05 04:44:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 795b1cea-be07-3213-90d4-dbb6a8afaaf8 | -6.02359 | -44.02284 | 2025-10-05 04:44:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 5076e074-6053-3955-ba74-9c7d9b6d60c4 | -4.64541 | -43.18258 | 2025-10-05 04:44:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 20.9 |
| 7e61b7eb-8955-3355-84aa-91df7f6570eb | -5.6102 | -43.11237 | 2025-10-05 04:44:00 | NOAA-21 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Caatinga | 1.8 |
| c5ec6bbf-c525-3f49-8880-ae1287105281 | -6.13146 | -42.86556 | 2025-10-05 04:44:00 | NOAA-21 | AMARANTE | PIAUÍ | Brasil | 2200509 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| ba51ebe5-e799-3783-a3e8-8d9f6fe097a8 | -6.66836 | -42.83733 | 2025-10-05 04:44:00 | NOAA-21 | AMARANTE | PIAUÍ | Brasil | 2200509 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 5208b389-3d48-3e6a-a05d-89a620d3b0bf | -4.36471 | -50.86274 | 2025-10-05 04:44:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| abee6ab3-502a-3290-b3b5-44c2b0b93fc7 | -6.03735 | -42.66702 | 2025-10-05 04:44:00 | NOAA-21 | SÃO GONÇALO DO PIAUÍ | PIAUÍ | Brasil | 2209807 | 22 | 33 | nan | nan | nan | Caatinga | 0.5 |
| a43dd677-3832-3d35-bd35-684bdb902426 | -5.55045 | -42.66998 | 2025-10-05 04:44:00 | NOAA-21 | MONSENHOR GIL | PIAUÍ | Brasil | 2206407 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 0123059c-b6cb-383f-ad96-e10a2116cfe8 | -6.08216 | -43.47705 | 2025-10-05 04:44:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| fc28b475-2b9c-3f1f-81a6-2bc3156f21b7 | -5.4668 | -42.78643 | 2025-10-05 04:44:00 | NOAA-21 | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Caatinga | 3.1 |
| 6595b5c5-1019-3461-8105-b56b57bfad02 | -5.35015 | -45.3023 | 2025-10-05 04:44:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 0efa2198-36f9-30ef-8852-f14b126d1775 | -6.15294 | -44.65464 | 2025-10-05 04:44:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 415c8a5a-9c01-3813-970e-99e4088377f1 | -5.90446 | -45.64481 | 2025-10-05 04:44:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 38850bb7-063c-31fd-bba0-db8b0a60b731 | -5.79442 | -48.45661 | 2025-10-05 04:44:00 | NOAA-21 | BREJO GRANDE DO ARAGUAIA | PARÁ | Brasil | 1501758 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8f113201-eea1-3936-8090-0c3f4fe277a1 | -3.54336 | -52.22501 | 2025-10-05 04:44:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ce43ef94-171a-325d-afc7-3834ef22985f | -3.80673 | -51.77252 | 2025-10-05 04:44:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 85824178-4988-3e63-8862-d4b670cb3dc3 | -5.3439 | -45.30167 | 2025-10-05 04:44:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 5555adc2-d90d-39c6-b9ca-6492eefaa5fb | -4.22401 | -46.7561 | 2025-10-05 04:44:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 5ad5ac3d-dd13-3e90-83cb-82874041ad8b | -6.15106 | -44.63655 | 2025-10-05 04:44:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 2810244a-a4ca-3a8f-b8c6-95a6bb585d03 | -5.93125 | -43.33331 | 2025-10-05 04:44:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 9.5 |
| a85b711c-d15a-3b17-870d-08226b548e8e | -6.03693 | -42.66992 | 2025-10-05 04:44:00 | NOAA-21 | SÃO GONÇALO DO PIAUÍ | PIAUÍ | Brasil | 2209807 | 22 | 33 | nan | nan | nan | Caatinga | 0.5 |
| d3c8f073-30fe-3fa5-bcf9-55cf634471bf | -5.78538 | -42.93417 | 2025-10-05 04:44:00 | NOAA-21 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 8.5 |
| 3ea7a552-08f2-348e-a8f9-7d6f5ffc969e | -5.23069 | -43.76617 | 2025-10-05 04:44:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| e571564f-94da-3dbb-aec1-17ee714fb74a | -5.88679 | -43.70636 | 2025-10-05 04:44:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 0e394489-58cf-3df6-be3b-650e5f760f1d | -5.1756 | -46.12223 | 2025-10-05 04:44:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e47704bd-4f4b-3365-ba92-fde3daadb850 | -4.44634 | -43.23417 | 2025-10-05 04:44:00 | NOAA-21 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 12.7 |
| 4be49600-2b77-3186-b973-2c516314f2ca | -6.13228 | -42.8599 | 2025-10-05 04:44:00 | NOAA-21 | AMARANTE | PIAUÍ | Brasil | 2200509 | 22 | 33 | nan | nan | nan | Caatinga | 3.1 |
| 3abca832-a471-31f4-81f1-797f1d0f1878 | -6.11732 | -42.85788 | 2025-10-05 04:44:00 | NOAA-21 | AMARANTE | PIAUÍ | Brasil | 2200509 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| b33e1ab3-15fe-3333-bc00-60b829d87d7b | -3.61226 | -51.04031 | 2025-10-05 04:44:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| a37db010-b699-3f89-b962-820974361a2a | -5.87579 | -42.5379 | 2025-10-05 04:44:00 | NOAA-21 | OLHO D'ÁGUA DO PIAUÍ | PIAUÍ | Brasil | 2207108 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 9aec14d3-737e-306b-897e-4ca0221f7ede | -5.90147 | -43.75621 | 2025-10-05 04:44:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| d0799d60-05ec-3b23-8064-9e7c3a8a9876 | -5.82923 | -45.81828 | 2025-10-05 04:44:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| cf0d4e72-d73b-3ee4-b0ab-0ba88a47a418 | -5.90391 | -45.64854 | 2025-10-05 04:44:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 6bb54020-ec0f-3a04-a57f-433f63928fff | -5.84327 | -42.88051 | 2025-10-05 04:44:00 | NOAA-21 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 4.6 |
| 226262cb-2221-3a0a-bc8f-dfbabe9d164e | -5.99523 | -45.7923 | 2025-10-05 04:44:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| cb7189ff-701a-319c-929b-50d718f8d7c8 | -5.6453 | -43.91447 | 2025-10-05 04:44:00 | NOAA-21 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 23.6 |
| af2196cf-9678-3e32-ac2f-ae0594df0aa0 | -3.84864 | -41.56939 | 2025-10-05 04:44:00 | NOAA-21 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 6.4 |
| 95c233c6-e53e-323f-a792-8b3a3b533cbc | -5.51933 | -44.20825 | 2025-10-05 04:44:00 | NOAA-21 | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 97206a9c-51aa-3020-977a-0230c1481f27 | -4.89478 | -45.06612 | 2025-10-05 04:44:00 | NOAA-21 | POÇÃO DE PEDRAS | MARANHÃO | Brasil | 2108900 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 7ff258ec-6b13-3353-a45c-84352181570c | -5.89831 | -43.75798 | 2025-10-05 04:44:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |


[Clique aqui para ver as próximas entradas](README77.md)
