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

## Dados Diários - Página 31

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| e4a4fe79-80fa-3c96-b063-98d0ee0a96db | -18.87827 | -46.97737 | 2026-09-12 04:36:00 | NOAA-21 | PATROCÍNIO | MINAS GERAIS | Brasil | 3148103 | 31 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 86f0b5cf-af25-3756-a48e-b8d42f624d25 | -18.66281 | -42.00355 | 2026-09-12 04:36:00 | NOAA-21 | GOVERNADOR VALADARES | MINAS GERAIS | Brasil | 3127701 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.9 |
| 630171f1-184e-3fd7-add4-833a66c3306d | -16.03322 | -47.91276 | 2026-09-12 04:36:00 | NOAA-21 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 95880ac1-744f-30dd-baef-87c30d5904ba | -18.40685 | -46.05131 | 2026-09-12 04:36:00 | NOAA-21 | VARJÃO DE MINAS | MINAS GERAIS | Brasil | 3170750 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 6d52ce6a-0301-3522-8af0-4fa60472b00b | -14.95686 | -47.52405 | 2026-09-12 04:36:00 | NOAA-21 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 4b2e789f-aad2-3ae0-ae73-22b9122bd906 | -18.87698 | -53.23396 | 2026-09-12 04:38:00 | NOAA-21 | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 2ae9d879-a9f6-3d4c-a272-4650e094c167 | -20.27955 | -44.70223 | 2026-09-12 04:38:00 | NOAA-21 | CARMO DO CAJURU | MINAS GERAIS | Brasil | 3114204 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 99b668ff-2732-32ec-933e-807cdcf4b64b | -19.67451 | -54.33842 | 2026-09-12 04:38:00 | NOAA-21 | BANDEIRANTES | MATO GROSSO DO SUL | Brasil | 5001508 | 50 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 4e9ff885-f307-37d7-8bbe-519a8ae54687 | -3.7462 | -61.7552 | 2026-09-12 04:40:00 | GOES-19 | ANORI | AMAZONAS | Brasil | 1300102 | 13 | 33 | nan | nan | nan | Amazônia | 52.4 |
| 6fc1c31d-8560-32ee-b78f-4d532a8bbdd3 | -3.33313 | -42.29558 | 2026-09-12 05:08:00 | NPP-375D | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 396b59d2-dc87-36d0-bce5-8c8a2cdf81d8 | -2.95235 | -50.41519 | 2026-09-12 05:08:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 16.2 |
| e60816e4-d40c-3cf3-8cd4-3ba4fddccdab | -2.96445 | -50.40862 | 2026-09-12 05:08:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 58.9 |
| f32ca9f7-e3ef-3c41-94cf-b889f9e1740b | -1.79232 | -47.83992 | 2026-09-12 05:08:00 | NPP-375D | SÃO DOMINGOS DO CAPIM | PARÁ | Brasil | 1507201 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0ebd940f-30ab-32d9-bb24-70ee6aef05d6 | 1.22877 | -50.72236 | 2026-09-12 05:08:00 | NPP-375D | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 187b90eb-84ed-3745-b74f-228c110f869a | -2.95021 | -50.38105 | 2026-09-12 05:08:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 92533304-508a-34d0-ba81-57b7587ee520 | -2.91382 | -54.11575 | 2026-09-12 05:08:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| a9439bea-aa91-3962-8f1e-9e6d4d91abc7 | 0.29386 | -51.08245 | 2026-09-12 05:08:00 | NPP-375D | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 5c3a3b93-1b27-3c5c-91ed-845054d19bd6 | -2.90072 | -51.93957 | 2026-09-12 05:08:00 | NPP-375D | VITÓRIA DO XINGU | PARÁ | Brasil | 1508357 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| aa1fd283-8fba-3de4-beb5-b1b1fa7a63aa | -2.94641 | -50.4058 | 2026-09-12 05:08:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 35.2 |
| f365df21-89e4-31d5-b862-f20fef91477f | -2.86509 | -49.62626 | 2026-09-12 05:08:00 | NPP-375D | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| ba1f3bec-3b77-3efb-a91c-e1bd138731d9 | -2.95957 | -50.41631 | 2026-09-12 05:08:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 72f0ef3f-2220-34c5-b954-289794439038 | -2.67647 | -54.59023 | 2026-09-12 05:08:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| cf7f8a4c-e4f0-3cb6-9b8f-afd2023b85a3 | -2.84235 | -53.99057 | 2026-09-12 05:08:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 4d1c1064-30d4-3598-80d2-030c639540bb | -2.94288 | -50.4767 | 2026-09-12 05:08:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f1c99868-c3cf-31ad-944d-40255bb7f044 | -2.96041 | -50.38685 | 2026-09-12 05:08:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 23bf5f0d-c30e-364a-9274-c4c9adfdb75f | -1.77558 | -54.9413 | 2026-09-12 05:08:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| dbd8d32b-24a1-3c67-b096-5a4f22174e3e | -2.95743 | -50.38216 | 2026-09-12 05:08:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 954ff418-83c4-3492-bfae-3f9cd2c99c35 | 3.99049 | -61.0417 | 2026-09-12 05:08:00 | NPP-375D | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 44f88f36-188f-3436-8ab5-f5b064cf5eea | -3.16086 | -48.61119 | 2026-09-12 05:08:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 1b53a10b-1a8f-3b69-aa10-ece122b9ffd7 | -2.96996 | -50.39682 | 2026-09-12 05:08:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| c2707efe-5375-36f1-82c8-22a6bbe2349c | -2.96084 | -50.40807 | 2026-09-12 05:08:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 58.9 |
| 8e954e9a-c9a7-3299-8af8-12b2edfa52e0 | 2.51479 | -50.8539 | 2026-09-12 05:08:00 | NPP-375D | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c8968546-e877-3be2-b5e8-fa409bcd8f2b | -2.96317 | -50.41686 | 2026-09-12 05:08:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 3d01096c-79d9-3106-aeb3-d9b26cf7ecd0 | 1.2051 | -50.78998 | 2026-09-12 05:08:00 | NPP-375D | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 7b9aa311-ee48-3df1-ae3e-0a591423d9d9 | -1.77042 | -54.95177 | 2026-09-12 05:08:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 67e97345-83e5-31db-99e3-300b1f99da4b | -2.94957 | -50.38519 | 2026-09-12 05:08:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 5bd54eff-39ef-31e5-8694-2ea22c8bbcad | -1.72693 | -57.15692 | 2026-09-12 05:08:00 | NPP-375D | FARO | PARÁ | Brasil | 1503002 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| d2ece044-4080-3099-ad5f-9ff9fed5eef5 | -2.94045 | -50.39647 | 2026-09-12 05:08:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 87aa1038-ff86-3c7a-926d-0c3fedddf952 | -2.94875 | -50.41462 | 2026-09-12 05:08:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 28.8 |
| 784eb848-6f57-3091-8364-c2806a427e0c | -2.9585 | -50.39926 | 2026-09-12 05:08:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 20.0 |
| 32f893f1-feaf-39b3-a836-97099056e729 | -2.93992 | -50.47206 | 2026-09-12 05:08:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 61c9d977-261d-3be1-ac70-cff670a1a421 | -3.38223 | -50.76353 | 2026-09-12 05:08:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| a702c32e-e8fd-3642-8282-729e2b10468c | -1.72766 | -57.1523 | 2026-09-12 05:08:00 | NPP-375D | FARO | PARÁ | Brasil | 1503002 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| e018a762-4d5d-3f54-8202-78651a3ad4c9 | -2.95192 | -50.394 | 2026-09-12 05:08:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 4de1995e-e657-3af7-b941-423201d7fbaa | -2.5834 | -54.62304 | 2026-09-12 05:08:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 42283119-c422-3759-bf6f-0ae101de38cd | -2.78757 | -47.61966 | 2026-09-12 05:08:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 6946edb8-fe67-3deb-9147-d2f3078168de | -3.22733 | -46.95057 | 2026-09-12 05:08:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 14.9 |
| 41a66bb7-fb79-3b09-86c6-7be33fbc915b | -2.81556 | -46.71289 | 2026-09-12 05:08:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e9794954-545a-3649-ad68-da6487155d1c | -3.46312 | -51.62721 | 2026-09-12 05:08:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| dc32780b-235c-3aec-9115-ffbc5ac74d04 | -2.94767 | -50.39758 | 2026-09-12 05:08:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 13.6 |
| c82347c7-f1ec-36aa-bd8d-c18f5b44181c | -2.95659 | -50.41164 | 2026-09-12 05:08:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 28.5 |
| ead76617-5cf3-3515-9f73-ade7ca470e02 | -2.96805 | -50.40918 | 2026-09-12 05:08:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 35.2 |
| 056489c4-73d1-302e-9a6a-dda802de77c2 | -2.72291 | -53.97566 | 2026-09-12 05:08:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| eed8ef2e-b0cb-3722-8a4b-24a858af3b4c | -2.94217 | -50.40936 | 2026-09-12 05:08:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 67d5f4fb-d19c-3147-bd14-4981cc06caf1 | -2.26609 | -48.43877 | 2026-09-12 05:08:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 6e32e11e-71d2-32ac-b312-781bdfd3b956 | -3.37153 | -50.76191 | 2026-09-12 05:08:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4c0a203a-5c36-30c8-a5c1-39217517f701 | -2.96381 | -50.41274 | 2026-09-12 05:08:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 58.9 |
| ff447400-3f1d-34e7-aaba-c750f238823d | -1.02731 | -53.74019 | 2026-09-12 05:08:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 0ce1db12-ded9-3ed0-91c8-349bc9c012ec | -2.93929 | -50.47614 | 2026-09-12 05:08:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1ca95aaf-d468-3b53-8173-56a09e02d62e | -2.95065 | -50.40225 | 2026-09-12 05:08:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 13.6 |
| 01b15732-534d-3d44-9fa8-7f7b1eaf93ec | -2.46926 | -48.03777 | 2026-09-12 05:08:00 | NPP-375D | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 905848e4-04b4-3efc-91bc-730f6b662fc3 | -3.19817 | -51.0196 | 2026-09-12 05:08:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 94c382f4-29ec-3a9f-a81f-dee93e0bf9f6 | -2.58396 | -54.61948 | 2026-09-12 05:08:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 752df7cc-2c60-32a5-9653-683b787c71a1 | -3.38348 | -50.75554 | 2026-09-12 05:08:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 13d86d5e-71f3-3271-876f-d24a821c0257 | -3.53759 | -48.1774 | 2026-09-12 05:08:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| dcd2cd29-4bfd-3b0e-be61-872dabb85929 | -2.9602 | -50.41219 | 2026-09-12 05:08:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 58.9 |
| c4c4e87d-8ee7-3128-911a-a15438360a94 | -2.95255 | -50.38987 | 2026-09-12 05:08:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| f1362ce2-c681-3b1e-997b-400c1adedd3d | -1.19095 | -55.71979 | 2026-09-12 05:08:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5ed0eafe-e282-3a09-a028-03e6219298a7 | -3.36504 | -50.75677 | 2026-09-12 05:08:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 14b1cc61-3fe1-39b5-844b-49346df6f3a4 | -2.94585 | -50.48133 | 2026-09-12 05:08:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ee84cd53-5bb4-36ed-a760-f8df256fd62e | -3.38579 | -50.76408 | 2026-09-12 05:08:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 066c0d7e-c6db-353e-bfdf-b0030607842c | -3.38517 | -50.76807 | 2026-09-12 05:08:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 85c7efff-9d13-3a80-be8c-1e96431bd853 | -2.95553 | -50.39455 | 2026-09-12 05:08:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 9.6 |
| 69249676-62f4-3209-8631-cebd162d3b37 | 1.22595 | -50.72657 | 2026-09-12 05:08:00 | NPP-375D | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 28f57819-fe02-3359-94ce-6c942df06a33 | -3.53702 | -48.18115 | 2026-09-12 05:08:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| b979ae8a-ece2-3e30-985d-c240dd0796c9 | -2.78818 | -47.61569 | 2026-09-12 05:08:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 4a7d0e5c-d9fd-3e20-8f09-cc581cd436b2 | -2.94514 | -50.41405 | 2026-09-12 05:08:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 28.8 |
| 239a9636-7734-3199-9594-1319107d07c5 | -2.95128 | -50.39812 | 2026-09-12 05:08:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 13.6 |
| 821d1456-b2f7-3a16-b082-45878b2f6d44 | -3.23184 | -46.95121 | 2026-09-12 05:08:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 14.9 |
| 40463a94-9793-3330-8391-c7cfff9bc141 | -2.94108 | -50.39235 | 2026-09-12 05:08:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| b7ca0e06-246f-338b-864d-6366407d2598 | -1.79291 | -47.8362 | 2026-09-12 05:08:00 | NPP-375D | SÃO DOMINGOS DO CAPIM | PARÁ | Brasil | 1507201 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1bf84c7c-859b-3f8a-bfc7-11c1f582dcd5 | -2.94938 | -50.4105 | 2026-09-12 05:08:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 35.2 |
| b2fefedf-f0f5-3e59-be22-486ac6cecd49 | -2.94532 | -50.38877 | 2026-09-12 05:08:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 7d53d002-4b1f-3a77-8e60-a137aeac2654 | -2.82352 | -51.33994 | 2026-09-12 05:08:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 85530ad3-07dd-3ccf-bdad-83e2b1ccfcac | -2.95319 | -50.38573 | 2026-09-12 05:08:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 0d66b75a-768c-35ad-990f-38826f52158e | -3.22803 | -46.94605 | 2026-09-12 05:08:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 12.9 |
| 819f1710-971b-397a-b9b2-9690866cecd3 | -2.4855 | -49.41346 | 2026-09-12 05:08:00 | NPP-375D | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 4add7de2-9c26-3822-b813-2b907589fbf5 | -3.37991 | -50.755 | 2026-09-12 05:08:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 82d130d1-5c00-399b-957f-bdcb470a8ff8 | -2.96338 | -50.39156 | 2026-09-12 05:08:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 21.7 |
| 98f659c4-a1d8-3afe-b662-f037ef40cb7f | -3.05848 | -51.24347 | 2026-09-12 05:08:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 8d7ad12c-48b9-331d-8310-d79dca0001ef | -2.90326 | -54.16051 | 2026-09-12 05:08:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 6dc2bfc3-20af-3861-bc0c-46624bd7fc58 | -2.82293 | -51.3437 | 2026-09-12 05:08:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| de53db35-282b-3fd7-8566-7402cec3b2b8 | -3.36797 | -50.76135 | 2026-09-12 05:08:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| fdc3b6d9-4e08-32bb-ba0d-86564865c9c0 | -2.94469 | -50.3929 | 2026-09-12 05:08:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| d179355f-3890-3df5-81d3-3e54000efe7d | -2.95426 | -50.40281 | 2026-09-12 05:08:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 20.0 |
| 144f16e3-5bb7-3846-8c39-8ed83306a2e9 | -3.23563 | -46.95647 | 2026-09-12 05:08:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 6ca1547c-8e8f-31f8-91da-16ad150edccd | -2.46869 | -48.04149 | 2026-09-12 05:08:00 | NPP-375D | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| b37c0737-a8e2-3a9a-9703-730615398d3b | -3.23114 | -46.95574 | 2026-09-12 05:08:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 14.9 |
| e092f2f4-b8e8-3217-b29f-fb4df4edfbc2 | -2.96466 | -50.38328 | 2026-09-12 05:08:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 78ae7430-90cb-3da6-a82f-a4863a491f43 | 2.51422 | -50.85032 | 2026-09-12 05:08:00 | NPP-375D | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 1.4 |


[Clique aqui para ver as próximas entradas](README32.md)
