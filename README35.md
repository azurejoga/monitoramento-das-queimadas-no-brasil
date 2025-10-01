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

## Dados Diários - Página 35

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| ae190569-d12e-3fc2-843f-afda7132e652 | -6.27573 | -43.65439 | 2025-10-01 04:19:00 | NOAA-21 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| afcfe107-7415-3a4c-83c8-7c2dc2f320d9 | -3.46231 | -50.09808 | 2025-10-01 04:19:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 7.6 |
| 396a13ff-abf4-3edb-9bf6-932902f5ece5 | -6.55426 | -43.94186 | 2025-10-01 04:19:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 003cbf57-65ae-32c3-9604-57ca64b0aa6c | -9.93775 | -43.64221 | 2025-10-01 04:19:00 | NOAA-21 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 3545b3cc-1f18-3ee0-a4d5-2743c6b9fcbe | -9.26555 | -45.69345 | 2025-10-01 04:19:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f786e9cf-a42d-3cf6-a280-44c976790965 | -5.20534 | -45.45054 | 2025-10-01 04:19:00 | NOAA-21 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |
| a512f31f-8382-3789-b0fd-45e2313aacf1 | -3.97949 | -43.25883 | 2025-10-01 04:19:00 | NOAA-21 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 8e9d5aac-100e-37cd-ad3e-607d8e30d2aa | -5.50133 | -42.76078 | 2025-10-01 04:19:00 | NOAA-21 | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Caatinga | 4.3 |
| 38ebba51-a0fa-307e-853e-fb27abfa5a3a | -6.99279 | -42.80154 | 2025-10-01 04:19:00 | NOAA-21 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 2a818b4f-077e-3be3-8dd3-2bc4422afaf6 | -6.46254 | -43.94133 | 2025-10-01 04:19:00 | NOAA-21 | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 6ebe3e9a-767b-3ecc-9a3b-633a3245b2fe | -6.97568 | -45.34049 | 2025-10-01 04:19:00 | NOAA-21 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| de595213-a386-3157-aa86-77fd32af78c4 | -7.47154 | -47.27947 | 2025-10-01 04:19:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 66489235-05e9-3164-9efd-5d30ab3e64d5 | -2.29907 | -48.57248 | 2025-10-01 04:19:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| d4bd1f7b-020e-3225-9fe3-822e01da1ae2 | -5.64381 | -43.93479 | 2025-10-01 04:19:00 | NOAA-21 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 308f986c-f72d-3f72-abde-a01094814de0 | -5.15816 | -49.82385 | 2025-10-01 04:19:00 | NOAA-21 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 644d9b6a-4940-34f7-9acd-5b4b02e2790c | -6.12057 | -43.48885 | 2025-10-01 04:19:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 81bfc6d0-d61f-3bf7-b080-63380571d156 | -6.3042 | -43.47019 | 2025-10-01 04:19:00 | NOAA-21 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 8d7b28b6-733f-343c-bd2a-4bbe5411193c | -5.68131 | -42.63702 | 2025-10-01 04:19:00 | NOAA-21 | MONSENHOR GIL | PIAUÍ | Brasil | 2206407 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 11b5f06a-e2c9-3d67-9c07-28b6258c3cca | -6.08825 | -42.47551 | 2025-10-01 04:19:00 | NOAA-21 | HUGO NAPOLEÃO | PIAUÍ | Brasil | 2204600 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 508fb4b8-fc2b-3f0d-afbd-1712256f8bf4 | -8.87338 | -47.64672 | 2025-10-01 04:19:00 | NOAA-21 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 3945de15-ae0e-34cf-84f2-01a4a1a58bdf | -4.00704 | -42.36332 | 2025-10-01 04:19:00 | NOAA-21 | BARRAS | PIAUÍ | Brasil | 2201200 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| e2cca784-f401-3722-a6f1-eeeaeff3ee03 | -9.80616 | -45.93355 | 2025-10-01 04:19:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ec470ce8-1ff9-3d4e-a017-b119c38422ad | -4.73898 | -43.60487 | 2025-10-01 04:19:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 9b58fe59-d9f4-33c7-b27d-3bb60ae04e99 | -4.81182 | -42.7649 | 2025-10-01 04:19:00 | NOAA-21 | JOSÉ DE FREITAS | PIAUÍ | Brasil | 2205508 | 22 | 33 | nan | nan | nan | Cerrado | 13.5 |
| bf3a4d0d-9691-305d-ba9d-84e6cbc33984 | -6.36988 | -44.57934 | 2025-10-01 04:19:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 2103dbd6-628c-3678-b134-9ca3b6383a2e | -5.90133 | -43.91855 | 2025-10-01 04:19:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 7fc424b8-f99c-30da-8c33-7d665b4d1146 | -6.69724 | -42.80775 | 2025-10-01 04:19:00 | NOAA-21 | FRANCISCO AYRES | PIAUÍ | Brasil | 2204105 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 4f770fdc-62c1-322f-9738-058b7920125a | -3.09735 | -47.01547 | 2025-10-01 04:19:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 83.5 |
| 9e876bcc-2792-3207-ab76-8d05cab132d2 | -7.07019 | -46.84509 | 2025-10-01 04:19:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 5ce1fc20-059b-31a5-b1f8-ad7dfbca425e | -9.33043 | -45.68948 | 2025-10-01 04:19:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 39a712b2-1ab7-3b91-8c5b-f7db3f62e9b9 | -6.73901 | -43.75783 | 2025-10-01 04:19:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 1e9280a8-7a5b-351d-8d41-13af2574889d | -7.51473 | -45.4405 | 2025-10-01 04:19:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| b431e237-ef6a-382f-a814-ee9142b7d55b | -7.95524 | -41.40665 | 2025-10-01 04:19:00 | NOAA-21 | JACOBINA DO PIAUÍ | PIAUÍ | Brasil | 2205151 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 96dbbdc5-ad71-3390-a811-f747fc1f3391 | -6.56744 | -43.39716 | 2025-10-01 04:19:00 | NOAA-21 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Caatinga | 1.2 |
| b6417fc9-c8e9-3677-a779-7f2f6ee704fb | -8.54066 | -44.68878 | 2025-10-01 04:19:00 | NOAA-21 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f3c22937-c5a9-3f65-a148-8ee7ec078d31 | -6.28457 | -43.6414 | 2025-10-01 04:19:00 | NOAA-21 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 0d011287-bb94-3e42-96b4-03529a479c2b | -6.27627 | -43.65089 | 2025-10-01 04:19:00 | NOAA-21 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 473a88c8-575c-3853-baa9-b49f4f072288 | -9.7957 | -45.93544 | 2025-10-01 04:19:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 356dfa9e-6f2f-3634-aa71-738ce15c4183 | -5.83889 | -42.80054 | 2025-10-01 04:19:00 | NOAA-21 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 5afeb94a-4fd7-3d0e-982a-c27b85dfec14 | -7.63509 | -45.41048 | 2025-10-01 04:19:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 401f88b3-3632-3645-88de-630348afc06d | -6.21127 | -44.2438 | 2025-10-01 04:19:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 56581fbd-51bf-3a3d-b37d-de0936ff641a | -6.56576 | -43.42279 | 2025-10-01 04:19:00 | NOAA-21 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Caatinga | 1.6 |
| e83d0beb-9225-34f9-9942-5a5d12b87060 | -5.91774 | -43.70303 | 2025-10-01 04:19:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| b145beab-8226-3111-af9e-dc8a52b5efc8 | -3.94672 | -41.5916 | 2025-10-01 04:19:00 | NOAA-21 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| cfd893a5-9de7-399d-96f7-60fc107b50c8 | -8.66566 | -43.98636 | 2025-10-01 04:19:00 | NOAA-21 | CRISTINO CASTRO | PIAUÍ | Brasil | 2203107 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 59b1d4e1-2b1f-30b6-8c89-e7551df81a62 | -5.77854 | -43.28352 | 2025-10-01 04:19:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 1763e512-f741-3693-9bea-2e4220a182f1 | -6.21835 | -44.2201 | 2025-10-01 04:19:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 13b6c186-cce2-37eb-927a-bc35cfcb7636 | -5.89326 | -45.87798 | 2025-10-01 04:19:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 7c966182-2954-3c59-8b74-245a958f6461 | -5.7322 | -42.87812 | 2025-10-01 04:19:00 | NOAA-21 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 4.8 |
| 942b0481-28e0-3a50-bb55-229e91d4c9ba | -5.70522 | -42.69012 | 2025-10-01 04:19:00 | NOAA-21 | AGRICOLÂNDIA | PIAUÍ | Brasil | 2200103 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 25d014d4-eef1-3b26-8ca5-c2eccbcb69bb | -8.22928 | -45.78705 | 2025-10-01 04:19:00 | NOAA-21 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 15edd3bb-acb9-39be-8470-58dae2a91eda | -6.28014 | -43.64792 | 2025-10-01 04:19:00 | NOAA-21 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| ef92ed43-af9f-330d-84dc-489afb15eaa9 | -6.45922 | -43.94079 | 2025-10-01 04:19:00 | NOAA-21 | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 3a739229-17bc-3b35-b28f-491d41bfcaea | -6.0443 | -43.61088 | 2025-10-01 04:19:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 78575c77-748d-3d01-ae75-a7096c821e15 | -5.04325 | -42.91084 | 2025-10-01 04:19:00 | NOAA-21 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 8711ca7b-31e1-3d2f-959c-7989618da518 | -5.27526 | -42.7711 | 2025-10-01 04:19:00 | NOAA-21 | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 1673f4ad-1440-3794-a222-c136e3fc9c18 | -5.27377 | -43.16203 | 2025-10-01 04:19:00 | NOAA-21 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b3fecc7c-5a65-3d4a-9187-2564b78ce559 | -7.0212 | -44.4842 | 2025-10-01 04:19:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| bbb005a4-6b37-32e5-b247-932b4a93015c | -5.95737 | -45.86251 | 2025-10-01 04:19:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 946d303c-76c2-37a4-9554-25e382e2df23 | -3.34961 | -43.19667 | 2025-10-01 04:19:00 | NOAA-21 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 8b4466d9-3150-3268-b532-a4e34f804e06 | -7.5616 | -42.4057 | 2025-10-01 04:19:00 | NOAA-21 | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 5368bcbb-562d-3414-81df-10b3c6d16ec7 | -8.61671 | -50.40181 | 2025-10-01 04:19:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c4371956-9f92-30b2-aa68-aa9a6569091b | -8.38066 | -48.65039 | 2025-10-01 04:19:00 | NOAA-21 | ITAPORÃ DO TOCANTINS | TOCANTINS | Brasil | 1711100 | 17 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 5f6cfca5-7c08-31b1-8530-e149bb7bb23b | -7.46869 | -47.2751 | 2025-10-01 04:19:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 755c5d8f-59f4-3985-88ed-7b45a64b37b8 | -5.50242 | -42.73083 | 2025-10-01 04:19:00 | NOAA-21 | LAGOA DO PIAUÍ | PIAUÍ | Brasil | 2205581 | 22 | 33 | nan | nan | nan | Caatinga | 3.5 |
| 7038826b-a41a-3eb4-a28e-53c394a24225 | -7.48221 | -47.27281 | 2025-10-01 04:19:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| c628658a-e119-3d0e-94a7-d8fb602efce5 | -8.58839 | -44.66778 | 2025-10-01 04:19:00 | NOAA-21 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 10fbf702-bb9e-3d7a-a8fc-ce1a02a45386 | -8.55509 | -44.75166 | 2025-10-01 04:19:00 | NOAA-21 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| a892fb83-f339-37e8-9f94-646d41d25c67 | -5.71752 | -42.8834 | 2025-10-01 04:19:00 | NOAA-21 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 5.3 |
| 01f73437-0272-3e64-a3b7-fbdecd0fb417 | -5.73049 | -42.86671 | 2025-10-01 04:19:00 | NOAA-21 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 4.6 |
| fb866fcd-485e-3e16-80aa-ece5ec5619a4 | -5.98342 | -43.60897 | 2025-10-01 04:19:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 921a990a-3079-3276-8e80-39bfcb5b1ef8 | -5.93938 | -43.54082 | 2025-10-01 04:19:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| dd50afcb-ac1a-38bb-8345-4f31b8a606f0 | -9.94232 | -43.65823 | 2025-10-01 04:19:00 | NOAA-21 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 5cb202ff-318a-3448-a02d-eacaac4f92e9 | -5.88725 | -43.83428 | 2025-10-01 04:19:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ae48907c-5209-3f5b-be25-ff9005eb3187 | -7.56101 | -42.4096 | 2025-10-01 04:19:00 | NOAA-21 | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| d7023d7c-3350-3cc1-9355-4a7cb9b2ee24 | -9.38239 | -45.8367 | 2025-10-01 04:19:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| eb454db1-d4a3-3685-9692-c6d53ddcf740 | -7.76989 | -47.38941 | 2025-10-01 04:19:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f168e48c-3a82-3a2b-89bc-34a56c928c4f | -8.55417 | -44.64813 | 2025-10-01 04:19:00 | NOAA-21 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 1bd92b7b-2fb2-3d1e-a29b-fb2aa1bb8482 | -5.70466 | -42.69378 | 2025-10-01 04:19:00 | NOAA-21 | MIGUEL LEÃO | PIAUÍ | Brasil | 2206308 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 2e516c31-193c-3e30-9d71-256109db8cf9 | -7.41012 | -49.72515 | 2025-10-01 04:19:00 | NOAA-21 | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a1950aa6-b941-3b11-972d-a585fe9ce404 | -5.05158 | -45.13034 | 2025-10-01 04:19:00 | NOAA-21 | SÃO RAIMUNDO DO DOCA BEZERRA | MARANHÃO | Brasil | 2111631 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 5eec9b18-dc9e-3ca1-8865-f3b4603d72a7 | -3.49218 | -48.93928 | 2025-10-01 04:19:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 70d4c4b9-35cb-3d69-8c68-ca92e5048b87 | -8.91547 | -46.07651 | 2025-10-01 04:19:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 89bedd59-3aaf-3ece-ad35-38ac914af78b | -5.49902 | -42.73032 | 2025-10-01 04:19:00 | NOAA-21 | LAGOA DO PIAUÍ | PIAUÍ | Brasil | 2205581 | 22 | 33 | nan | nan | nan | Caatinga | 4.2 |
| d3169b81-6d9d-3aaa-963f-9f7a5ec8b340 | -5.82985 | -42.81423 | 2025-10-01 04:19:00 | NOAA-21 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 4.6 |
| a030184d-1d24-39cf-b0b9-13be8cffdb57 | -8.89815 | -46.67336 | 2025-10-01 04:19:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| d7aebd92-d12f-3b07-bc27-58e9ed50ff69 | -5.89574 | -42.52004 | 2025-10-01 04:19:00 | NOAA-21 | OLHO D'ÁGUA DO PIAUÍ | PIAUÍ | Brasil | 2207108 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 668359b9-d29f-33b2-9e42-61569fe1f8ca | -5.83834 | -42.80417 | 2025-10-01 04:19:00 | NOAA-21 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 05177035-2c4a-3a1c-bb68-db9e81a53fca | -9.4452 | -45.48005 | 2025-10-01 04:19:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| cc55b7bc-46ae-3ca6-8f0a-deb88293ac3c | -9.92986 | -43.67159 | 2025-10-01 04:19:00 | NOAA-21 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 1b418203-ea3f-373f-a283-5ff7062e04a7 | -8.92484 | -47.59215 | 2025-10-01 04:19:00 | NOAA-21 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| d9ced9eb-fdaf-3cd2-9b23-d13875f945ec | -7.54827 | -46.28017 | 2025-10-01 04:19:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 932c324b-f1d2-3c8a-80f1-b7a8e06dca1a | -5.49227 | -42.75183 | 2025-10-01 04:19:00 | NOAA-21 | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Caatinga | 4.2 |
| 087c0e34-2618-3ce2-8909-7760cad2ba68 | -6.08768 | -42.4793 | 2025-10-01 04:19:00 | NOAA-21 | HUGO NAPOLEÃO | PIAUÍ | Brasil | 2204600 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| ca9b108e-cbbe-3210-8a1a-75588c7d56c8 | -5.80962 | -42.87851 | 2025-10-01 04:19:00 | NOAA-21 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 0a1d28ee-eda2-39b2-bf23-1ac96550281e | -7.60431 | -45.41266 | 2025-10-01 04:19:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| ad3d0e1b-912f-3e70-b35c-2343a609666b | -8.24207 | -42.9123 | 2025-10-01 04:19:00 | NOAA-21 | TAMBORIL DO PIAUÍ | PIAUÍ | Brasil | 2210953 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 28f3086a-f40f-3661-81f8-93edb3170712 | -5.27542 | -43.15135 | 2025-10-01 04:19:00 | NOAA-21 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| e8a38977-05a1-33ca-8345-28d6253d5c2a | -5.75234 | -42.65576 | 2025-10-01 04:19:00 | NOAA-21 | AGRICOLÂNDIA | PIAUÍ | Brasil | 2200103 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| ad028ad5-3dda-34f1-8ee6-6fa2114e6e18 | -7.45832 | -47.27345 | 2025-10-01 04:19:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |


[Clique aqui para ver as próximas entradas](README36.md)
