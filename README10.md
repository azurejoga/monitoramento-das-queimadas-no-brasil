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

## Dados Diários - Página 10

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| ef1d5035-0168-3b28-b6f2-3e5421aa7eec | -4.41702 | -42.91199 | 2025-11-26 03:57:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 0.4 |
| e72ef52d-c8bd-3515-9cf9-2e14b31c8639 | -2.54388 | -45.39019 | 2025-11-26 03:57:00 | NPP-375D | PRESIDENTE SARNEY | MARANHÃO | Brasil | 2109270 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2bba3036-a10c-33c4-815b-a70c941fb3fe | -2.47536 | -47.83364 | 2025-11-26 03:57:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 81830989-5772-3be0-b843-3b1cee04cba7 | -5.42058 | -43.05589 | 2025-11-26 03:57:00 | NPP-375D | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 46e8d356-4b1b-3fd1-9ea7-234f82fd735f | -4.16257 | -43.72516 | 2025-11-26 03:57:00 | NPP-375D | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 982a3011-7fef-3703-8234-8b55502a6c34 | -3.25761 | -51.17485 | 2025-11-26 03:57:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 11065cb3-b8a1-323a-8b3b-5513b98e732f | -5.21559 | -42.98906 | 2025-11-26 03:57:00 | NPP-375D | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 6de533b6-0d00-3e9e-9c48-fb455551eccb | -6.68733 | -42.47409 | 2025-11-26 03:57:00 | NPP-375D | CAJAZEIRAS DO PIAUÍ | PIAUÍ | Brasil | 2202075 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| fafbfb11-4688-34f1-b9ff-f6b13c7b45cd | -4.37357 | -49.76836 | 2025-11-26 03:57:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 272e2cee-f6b7-326c-80e4-305f545550ed | -6.56419 | -44.03635 | 2025-11-26 03:57:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| d2e2f06b-edec-3903-beac-f38e51a18cb3 | -4.16718 | -49.87897 | 2025-11-26 03:57:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 32f14be4-1efa-36f8-8b20-6e99d387a7bd | -5.27839 | -43.6384 | 2025-11-26 03:57:00 | NPP-375D | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 4503a96e-ce08-3f41-8ed3-b27135e974cb | -2.47415 | -47.83564 | 2025-11-26 03:57:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e4458da2-70fc-3da7-9110-b76a4c0b226b | -3.3613 | -49.50289 | 2025-11-26 03:57:00 | NPP-375D | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 48bc21af-830e-3553-bad2-49f7772fd262 | -6.7676 | -46.5199 | 2025-11-26 03:57:00 | NPP-375D | SÃO PEDRO DOS CRENTES | MARANHÃO | Brasil | 2111573 | 21 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 7307b5e3-b6b1-3d07-8d86-6af86a674d1a | -4.70941 | -43.98458 | 2025-11-26 03:57:00 | NPP-375D | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| d0d4e9a0-e29c-3444-8bce-5a34e620b852 | -6.76361 | -46.51335 | 2025-11-26 03:57:00 | NPP-375D | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 4ffa9c35-1082-33e5-ba95-d1a4fe040e24 | -4.56593 | -43.29514 | 2025-11-26 03:57:00 | NPP-375D | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| bca3ec96-cd12-333c-97e9-9a2801d15bcf | -6.99181 | -38.943 | 2025-11-26 03:57:00 | NPP-375D | AURORA | CEARÁ | Brasil | 2301703 | 23 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 7d31ac52-7618-3956-bbbc-d26c49cd918f | -2.54787 | -45.39655 | 2025-11-26 03:57:00 | NPP-375D | PRESIDENTE SARNEY | MARANHÃO | Brasil | 2109270 | 21 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 1fe0498b-4637-3fa2-b505-1bb253a0623a | -6.75368 | -35.32817 | 2025-11-26 03:57:00 | NPP-375D | CURRAL DE CIMA | PARAÍBA | Brasil | 2505279 | 25 | 33 | nan | nan | nan | Caatinga | 1.4 |
| be47a4d0-ec51-3881-94b7-1f6902118988 | -4.84066 | -38.61172 | 2025-11-26 03:57:00 | NPP-375D | MORADA NOVA | CEARÁ | Brasil | 2308708 | 23 | 33 | nan | nan | nan | Caatinga | 0.7 |
| ebbf36bc-68ac-330b-ac76-96a7d2ae6a92 | -5.22999 | -45.42455 | 2025-11-26 03:57:00 | NPP-375D | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 0d740581-2dd8-3bdb-9496-e084be428f41 | -5.29508 | -43.64133 | 2025-11-26 03:57:00 | NPP-375D | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| f4c0a064-a1c4-3649-b369-69b5198feeaf | -7.11721 | -39.34287 | 2025-11-26 03:57:00 | NPP-375D | CRATO | CEARÁ | Brasil | 2304202 | 23 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 76c473ac-7eec-372e-adb5-66f5df69fa55 | -4.25657 | -45.12911 | 2025-11-26 03:57:00 | NPP-375D | OLHO D'ÁGUA DAS CUNHÃS | MARANHÃO | Brasil | 2107407 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 1011069e-26a7-36b3-af97-f8b4876ef7a6 | -4.56532 | -43.29882 | 2025-11-26 03:57:00 | NPP-375D | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| e7d5b5d0-e00d-33c7-83c9-d58b75f56f61 | -3.22963 | -51.18346 | 2025-11-26 03:57:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 32f66de1-6a3c-306b-b627-1b20faf0cd4a | -4.56119 | -43.29814 | 2025-11-26 03:57:00 | NPP-375D | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| ccd353df-2b9d-393a-8950-9482e56ff301 | -3.43392 | -50.18525 | 2025-11-26 03:57:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| f9facf98-6bf2-3cdc-918a-6ab339d03d13 | -7.20175 | -39.37086 | 2025-11-26 03:57:00 | NPP-375D | CRATO | CEARÁ | Brasil | 2304202 | 23 | 33 | nan | nan | nan | Caatinga | 0.7 |
| b2bf47f1-28d9-33c4-b694-c407a8f7cab3 | -4.6572 | -48.48129 | 2025-11-26 03:57:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ebb544b5-b4b7-3569-9c1c-2a640a3880a2 | -4.26681 | -45.12569 | 2025-11-26 03:57:00 | NPP-375D | OLHO D'ÁGUA DAS CUNHÃS | MARANHÃO | Brasil | 2107407 | 21 | 33 | nan | nan | nan | Amazônia | 5.2 |
| ffa4b022-9b92-397a-96f6-1bce638927e9 | -3.27739 | -46.0267 | 2025-11-26 03:57:00 | NPP-375D | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 0.5 |
| eb99c68c-c851-3eac-bc69-cdd7c33bc294 | -6.76857 | -46.51423 | 2025-11-26 03:57:00 | NPP-375D | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| c27c7082-3104-3569-aa40-3787bf15596f | -5.32832 | -43.56895 | 2025-11-26 03:57:00 | NPP-375D | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 7ba6f049-d516-36dc-ac9b-e9e1cf2fa807 | -7.61368 | -42.98469 | 2025-11-26 03:57:00 | NPP-375D | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 9264d02e-a4ac-3416-935f-a1dad09fef27 | -3.60209 | -40.95035 | 2025-11-26 03:57:00 | NPP-375D | TIANGUÁ | CEARÁ | Brasil | 2313401 | 23 | 33 | nan | nan | nan | Caatinga | 1.1 |
| dfdbe0ef-05bf-3ab0-a389-ad83cedc77c8 | -2.46953 | -47.83277 | 2025-11-26 03:57:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 967e39d6-21e1-3a72-8ed0-412d73dd642c | -4.15403 | -43.72368 | 2025-11-26 03:57:00 | NPP-375D | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| fa3eeab3-0789-3036-a9e8-a8489e9fce17 | -5.65519 | -38.95897 | 2025-11-26 03:57:00 | NPP-375D | SOLONÓPOLE | CEARÁ | Brasil | 2313005 | 23 | 33 | nan | nan | nan | Caatinga | 0.9 |
| e599dfcd-d4df-37ea-aea3-416cf5183d9f | -3.67118 | -43.56285 | 2025-11-26 03:57:00 | NPP-375D | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 2b8ddc29-acad-329e-b603-be1cb691ae39 | -2.86092 | -42.44161 | 2025-11-26 03:57:00 | NPP-375D | TUTÓIA | MARANHÃO | Brasil | 2112506 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| ebc0bba9-7a2a-3463-b28f-2a1566b16fa2 | -5.71799 | -39.50181 | 2025-11-26 03:57:00 | NPP-375D | MOMBAÇA | CEARÁ | Brasil | 2308500 | 23 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 9862ceee-3566-3c22-8b1b-0524905e1b3e | -3.46948 | -43.42246 | 2025-11-26 03:57:00 | NPP-375D | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| fc3d2d7f-8221-3db4-bf86-682a39597dc1 | -5.49888 | -42.37162 | 2025-11-26 03:57:00 | NPP-375D | BENEDITINOS | PIAUÍ | Brasil | 2201606 | 22 | 33 | nan | nan | nan | Caatinga | 3.2 |
| 608ce0a0-d253-3a58-b09e-eb6926697aeb | -4.56368 | -43.80404 | 2025-11-26 03:57:00 | NPP-375D | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 3ddd6c66-ce5a-3cda-9beb-629a0d13d5a7 | -4.00463 | -45.20166 | 2025-11-26 03:57:00 | NPP-375D | OLHO D'ÁGUA DAS CUNHÃS | MARANHÃO | Brasil | 2107407 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 02008b41-555b-3755-a83a-228b22d892d7 | -4.5618 | -43.29446 | 2025-11-26 03:57:00 | NPP-375D | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 6b7a4a24-3c50-3dcb-912a-520da0ec58e8 | -3.26466 | -51.17598 | 2025-11-26 03:57:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 1f8cbb12-d040-3937-a729-32b1e2edbdea | -4.56654 | -43.29147 | 2025-11-26 03:57:00 | NPP-375D | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 0451f5f2-a1b7-3dd2-8152-7d7116d29e83 | -6.0796 | -39.55165 | 2025-11-26 03:57:00 | NPP-375D | ACOPIARA | CEARÁ | Brasil | 2300309 | 23 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 75aa2b9c-e659-3a23-a1f4-2e3d77667c8d | -2.42012 | -48.598 | 2025-11-26 03:57:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| e0a03e3e-b5ca-329f-be82-46dbf3a92be7 | -7.16436 | -44.99416 | 2025-11-26 03:57:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| f28d02a3-510a-3d3d-a327-13a947afedb9 | -4.70802 | -43.99269 | 2025-11-26 03:57:00 | NPP-375D | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 636a5ccf-b891-3bab-a68d-32d7fd526dc1 | -4.94085 | -44.71175 | 2025-11-26 03:57:00 | NPP-375D | JOSELÂNDIA | MARANHÃO | Brasil | 2105609 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 24129904-521d-301a-9377-145786778e92 | -4.14426 | -42.55022 | 2025-11-26 03:57:00 | NPP-375D | BARRAS | PIAUÍ | Brasil | 2201200 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 9a1fcd26-6b27-3aaf-9707-14ee7f32fd7e | -6.07623 | -39.55109 | 2025-11-26 03:57:00 | NPP-375D | ACOPIARA | CEARÁ | Brasil | 2300309 | 23 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 3255adb2-210d-34c5-a762-44e737a160c8 | -4.17837 | -43.73593 | 2025-11-26 03:57:00 | NPP-375D | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 15.3 |
| 603c7afc-faba-35dc-9b38-8e4297440d36 | -2.48853 | -47.82119 | 2025-11-26 03:57:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 3751b538-a37c-320d-b795-5c21a4cc9766 | -3.32274 | -49.7213 | 2025-11-26 03:57:00 | NPP-375D | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 358b1f32-81e9-304f-9447-bfd121ddc52f | -6.06589 | -43.24993 | 2025-11-26 03:57:00 | NPP-375D | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 1.4 |
| fa25fa36-edf4-382f-8187-aec5b60d86dd | -3.59918 | -38.78164 | 2025-11-26 03:57:00 | NPP-375D | CAUCAIA | CEARÁ | Brasil | 2303709 | 23 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 1868a452-65d9-3414-86ba-6365e50bacb3 | -3.04087 | -45.11277 | 2025-11-26 03:57:00 | NPP-375D | MATINHA | MARANHÃO | Brasil | 2106508 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| a8cda055-a98f-37d6-bf5c-36e107835c3a | -4.56795 | -43.80477 | 2025-11-26 03:57:00 | NPP-375D | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 9bcb91e5-defd-320d-94d7-95fb866a6b5a | -2.71303 | -45.69631 | 2025-11-26 03:57:00 | NPP-375D | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 543d4d43-8f50-351f-8183-5f7d91c2aabb | -5.45929 | -43.22109 | 2025-11-26 03:57:00 | NPP-375D | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 2ddbb419-c368-3be9-91fb-b13f24439a0d | -3.68335 | -43.56885 | 2025-11-26 03:57:00 | NPP-375D | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 511a6baa-0994-39c6-b685-22a3e41b5ae7 | -4.66453 | -43.97736 | 2025-11-26 03:57:00 | NPP-375D | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| c47bbe0a-e250-314e-8eb2-6316708b73e5 | -4.71948 | -46.46009 | 2025-11-26 03:57:00 | NPP-375D | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 3.4 |
| bbc685f1-ca5a-3fc6-bd15-8068112653e9 | -3.47245 | -43.43094 | 2025-11-26 03:57:00 | NPP-375D | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 7922d181-73a6-332d-a1fd-af4f66bba78e | -2.28696 | -47.04467 | 2025-11-26 03:57:00 | NPP-375D | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 7aef6e0b-2e5f-3dc1-83cf-c1cb01916300 | -5.32942 | -43.56834 | 2025-11-26 03:57:00 | NPP-375D | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 11.6 |
| ebe9b67c-687c-3a8f-9c89-b91feb11b010 | -3.58992 | -40.98065 | 2025-11-26 03:57:00 | NPP-375D | VIÇOSA DO CEARÁ | CEARÁ | Brasil | 2314102 | 23 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 7b640dcc-af95-3891-af24-4d87a2dba8fc | -4.71775 | -47.15638 | 2025-11-26 03:57:00 | NPP-375D | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| dcfb1bee-9f2f-3295-9bc7-55492445924d | -4.17409 | -43.73521 | 2025-11-26 03:57:00 | NPP-375D | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 15.3 |
| ae9653b6-216b-3ef6-8a8e-7a43ce268b6d | -3.45244 | -50.55182 | 2025-11-26 03:57:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| f2d18752-700d-36ac-82e3-942ac2d7ab9f | -5.27776 | -43.64222 | 2025-11-26 03:57:00 | NPP-375D | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 2d93f3a3-2bbd-3bfb-b30d-676bd9513635 | -4.17451 | -49.87498 | 2025-11-26 03:57:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 9e83e1ef-3e2c-35bc-a251-3399514b1420 | -3.44223 | -50.19159 | 2025-11-26 03:57:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 1e3cd4b9-8616-3e30-b818-0fd016ef7fe8 | -3.22343 | -50.56822 | 2025-11-26 03:57:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| ffb03357-2da3-306c-9333-03582c043dfb | -6.76237 | -46.51943 | 2025-11-26 03:57:00 | NPP-375D | SÃO PEDRO DOS CRENTES | MARANHÃO | Brasil | 2111573 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 0e4c59e8-5f8b-3957-b95a-b710d873eea0 | -4.16884 | -43.71379 | 2025-11-26 03:57:00 | NPP-375D | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 7bea3ff1-cab0-30bb-b386-0b5992de6a7d | -4.71 | -43.9976 | 2025-11-26 03:57:00 | NPP-375D | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| aa02599a-2071-33a9-82f0-19001bde17ed | -2.49946 | -47.82716 | 2025-11-26 03:57:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| af9734ca-222c-33b0-b4ff-fdc4b92c2856 | -5.57119 | -44.97591 | 2025-11-26 03:57:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| eeddd06b-ac14-3bea-bc10-f745a45c9300 | -3.66627 | -43.56614 | 2025-11-26 03:57:00 | NPP-375D | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| b24ada5c-1853-3a70-8559-edb120b4622e | -5.74094 | -42.36927 | 2025-11-26 03:57:00 | NPP-375D | PASSAGEM FRANCA DO PIAUÍ | PIAUÍ | Brasil | 2207751 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| 24ec2742-1e5d-36ce-bf34-e70426d6f834 | -2.50013 | -47.82313 | 2025-11-26 03:57:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 6e09d4e4-8f84-3269-b6d6-273f472d8ad6 | -2.47998 | -47.83644 | 2025-11-26 03:57:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| eaa4e15d-90a3-36f3-adcb-4d90f043084b | -4.72 | -46.45696 | 2025-11-26 03:57:00 | NPP-375D | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| bb93c608-2648-35ea-9cc3-421a85380662 | -3.98347 | -46.02406 | 2025-11-26 03:57:00 | NPP-375D | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 4fc780ba-28d0-33a4-ba24-27ff237493ed | -6.47924 | -40.80037 | 2025-11-26 03:57:00 | NPP-375D | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 0ac2802c-bfe1-30ee-a5b6-fe3b41215b75 | -2.46903 | -47.83057 | 2025-11-26 03:57:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c60ccb2d-a2d9-337f-a1a4-a8014a97f288 | -4.65454 | -43.98408 | 2025-11-26 03:57:00 | NPP-375D | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 5.7 |
| ea4a09b6-80b5-39bb-a94c-2f60368c727b | -4.17343 | -43.73923 | 2025-11-26 03:57:00 | NPP-375D | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 15.3 |
| 0553041b-4349-3cc4-b112-6735da27e6df | -5.28256 | -43.63912 | 2025-11-26 03:57:00 | NPP-375D | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 2eebca51-810a-33ae-83a4-dc832335b936 | -3.18213 | -48.62203 | 2025-11-26 03:57:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| bb1bce67-fb78-37a3-bb67-cb57799944eb | -4.27233 | -45.12153 | 2025-11-26 03:57:00 | NPP-375D | OLHO D'ÁGUA DAS CUNHÃS | MARANHÃO | Brasil | 2107407 | 21 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 90f97417-2bef-38be-8759-e10a06382b05 | -3.46885 | -43.42634 | 2025-11-26 03:57:00 | NPP-375D | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |


[Clique aqui para ver as próximas entradas](README11.md)
