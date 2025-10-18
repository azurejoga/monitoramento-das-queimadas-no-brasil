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

## Dados Diários - Página 46

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| dd5a0f1e-5201-312c-bd72-e2999c30116b | -8.09463 | -44.10905 | 2025-10-18 04:29:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 4.3 |
| de7651e9-dd73-3557-a831-8689604b635d | -9.25751 | -43.74453 | 2025-10-18 04:29:00 | NPP-375D | GUARIBAS | PIAUÍ | Brasil | 2204550 | 22 | 33 | nan | nan | nan | Caatinga | 0.4 |
| 7ae03f81-d07c-34bf-9949-48e247528af2 | -4.87602 | -46.70732 | 2025-10-18 04:29:00 | NPP-375D | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1628f265-422d-3746-9828-7e6819da0b03 | -8.71632 | -49.59956 | 2025-10-18 04:29:00 | NPP-375D | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2e6dafdf-a849-320e-8b99-88926aae9827 | -9.90946 | -48.13935 | 2025-10-18 04:29:00 | NPP-375D | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| bd3a6296-5096-3aea-91f3-9e86416bd7a2 | -5.90411 | -44.75996 | 2025-10-18 04:29:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 6af35eee-3e64-390b-89d0-b5193aae9f76 | -4.69263 | -48.62389 | 2025-10-18 04:29:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| f529c556-2ab6-3d29-a704-c1c12efdef30 | -7.45742 | -42.69035 | 2025-10-18 04:29:00 | NPP-375D | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 9e9bbe17-dc65-3875-84a9-983d9ac3645b | -8.44548 | -44.17228 | 2025-10-18 04:29:00 | NPP-375D | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 194d8f8c-e8a6-3b36-b88c-83c58d547e01 | -5.89569 | -42.79781 | 2025-10-18 04:29:00 | NPP-375D | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 3.8 |
| 6cccede5-ad72-3987-b12a-9c747ae0f6bc | -10.23528 | -44.04745 | 2025-10-18 04:29:00 | NPP-375D | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 5.2 |
| aacfcc0a-1134-3de2-93c4-0053f7258217 | -4.93786 | -47.3005 | 2025-10-18 04:29:00 | NPP-375D | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 377fafdf-c71a-3535-8bf9-0c113a0e88c4 | -10.71516 | -44.53958 | 2025-10-18 04:29:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| cd8ca780-a987-3378-a652-aba14f370ae7 | -8.19213 | -43.30944 | 2025-10-18 04:29:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| c9e8aab4-27ad-3218-a01e-5296971b1377 | -5.89168 | -44.70602 | 2025-10-18 04:29:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 8ee0afa3-c423-301c-8ca5-0e877701e76c | -9.64502 | -47.12392 | 2025-10-18 04:29:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 8a575bb0-0ee3-3a10-aef8-507bdca0cad7 | -7.36705 | -44.23137 | 2025-10-18 04:29:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| dd4c2822-0787-3235-a7b9-2fe349cf404b | -9.29747 | -49.66148 | 2025-10-18 04:29:00 | NPP-375D | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 25b0cbe0-a732-3c56-8bf4-60b15c799d8d | -6.58764 | -47.07254 | 2025-10-18 04:29:00 | NPP-375D | SÃO JOÃO DO PARAÍSO | MARANHÃO | Brasil | 2111052 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 7573b775-209f-3923-aff2-fd3ee40e5bd2 | -5.72311 | -43.81829 | 2025-10-18 04:29:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 5dd5419e-e820-3767-8ad4-4b1f9b3db9d6 | -10.49332 | -43.42956 | 2025-10-18 04:29:00 | NPP-375D | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 11.7 |
| 8475840b-7c45-32d5-8ca6-e11f834ab03d | -6.33455 | -46.34325 | 2025-10-18 04:29:00 | NPP-375D | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| d5b3d46e-29fd-34da-9954-6fd753dd0125 | -9.68435 | -47.80717 | 2025-10-18 04:29:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 0.4 |
| cdc77820-ca1f-30d9-9f87-055e534f6370 | -6.87111 | -44.68984 | 2025-10-18 04:29:00 | NPP-375D | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 1a813746-e969-399f-b365-10cd51d8fa29 | -6.58914 | -44.1611 | 2025-10-18 04:29:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 4230fb1d-d0ff-346c-89b5-6b2b52e5eac6 | -10.62575 | -42.30501 | 2025-10-18 04:29:00 | NPP-375D | ITAGUAÇU DA BAHIA | BAHIA | Brasil | 2915353 | 29 | 33 | nan | nan | nan | Caatinga | 3.6 |
| 31ade640-d3cd-3674-be33-b8cb8d26ba06 | -7.16149 | -42.37359 | 2025-10-18 04:29:00 | NPP-375D | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 5.1 |
| b54ea6bf-d44e-3fac-9164-e048d9038292 | -6.5852 | -48.77027 | 2025-10-18 04:29:00 | NPP-375D | PIÇARRA | PARÁ | Brasil | 1505635 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 5175dcd7-f373-3320-b5c3-04442617cf4c | -10.22728 | -44.07607 | 2025-10-18 04:29:00 | NPP-375D | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c6e19809-8ffa-335a-a4d2-050944ba6ce7 | -10.23167 | -44.04683 | 2025-10-18 04:29:00 | NPP-375D | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 5.2 |
| e9838222-8bdc-36a9-b95a-ebbb1601f31f | -7.44148 | -44.74554 | 2025-10-18 04:29:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 01384ec2-1d1a-3868-a819-84b791d3e8cc | -9.88384 | -49.1217 | 2025-10-18 04:29:00 | NPP-375D | DIVINÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1707108 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a31db90b-120c-33a7-abd2-dde75391b9ac | -6.52828 | -41.48956 | 2025-10-18 04:29:00 | NPP-375D | LAGOA DO SÍTIO | PIAUÍ | Brasil | 2205599 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| a6d789f3-0eaf-3b37-be88-075a65539513 | -5.407 | -46.41311 | 2025-10-18 04:29:00 | NPP-375D | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 8baea7b4-2521-31bd-9273-18b5e7e247a9 | -10.71665 | -44.54732 | 2025-10-18 04:29:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 9ec60229-c7ab-3253-aec6-8f7bc14eaf02 | -10.23936 | -44.06957 | 2025-10-18 04:29:00 | NPP-375D | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 801fd00b-2fe9-3eca-a456-98ff8759da50 | -10.58107 | -43.82304 | 2025-10-18 04:29:00 | NPP-375D | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 5dee72eb-71f4-3ab8-b798-036d68424e20 | -5.20678 | -45.75666 | 2025-10-18 04:29:00 | NPP-375D | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 729959ad-748a-3e5e-a5e7-3ca4b5ad5900 | -4.42163 | -47.75356 | 2025-10-18 04:29:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 64b3381a-d118-37f2-97b6-764ad801d703 | -7.75834 | -42.50808 | 2025-10-18 04:29:00 | NPP-375D | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 87547c13-57ab-3f5f-8241-3c0b3ea0215c | -6.88776 | -45.45333 | 2025-10-18 04:29:00 | NPP-375D | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| fcc3db77-8b4c-3cd3-88f4-2d16dd3dcebf | -8.81047 | -49.68437 | 2025-10-18 04:29:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 84e0f322-0c55-391f-b362-61aa3ad9328a | -6.1735 | -47.87018 | 2025-10-18 04:29:00 | NPP-375D | LUZINÓPOLIS | TOCANTINS | Brasil | 1712454 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 9e162896-b3ab-3543-8312-b713b3ac1b1c | -5.92244 | -45.44415 | 2025-10-18 04:29:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 5.2 |
| df358a39-375b-35b0-8fc7-9ddaf53707b6 | -10.51093 | -43.41419 | 2025-10-18 04:29:00 | NPP-375D | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 9976dd53-37fb-377c-9dc6-0ac930d7a8c1 | -7.26877 | -47.36134 | 2025-10-18 04:29:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| cf320ce1-d66d-3118-aa17-c3ca8339b9cc | -9.254 | -44.34684 | 2025-10-18 04:29:00 | NPP-375D | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| acba1721-cbf8-3659-8fbb-f18c8d5ed03f | -7.83567 | -45.44291 | 2025-10-18 04:29:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 566fc339-f073-3bde-a51f-d73d70397091 | -10.53921 | -44.5096 | 2025-10-18 04:29:00 | NPP-375D | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 4a78950b-9e69-3589-904f-8777ceaea598 | -5.25525 | -50.90604 | 2025-10-18 04:29:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 50280cf8-52a2-3b7a-bce5-042398cb21a2 | -8.69412 | -47.06483 | 2025-10-18 04:29:00 | NPP-375D | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 6b8e8bfa-67d7-3289-9224-598b4483a5ba | -10.15939 | -44.52597 | 2025-10-18 04:29:00 | NPP-375D | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 3d63d2f0-1dd8-37b0-8123-37598ca75ce1 | -5.18287 | -46.18215 | 2025-10-18 04:29:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 2bc10199-011f-3bea-bf5d-9c486a887b61 | -10.1245 | -44.54129 | 2025-10-18 04:29:00 | NPP-375D | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 80f1ecc7-1386-38d1-8fb4-4ebf4147c037 | -7.01735 | -41.83576 | 2025-10-18 04:29:00 | NPP-375D | SÃO JOÃO DA VARJOTA | PIAUÍ | Brasil | 2209955 | 22 | 33 | nan | nan | nan | Caatinga | 7.2 |
| 23cf69f2-f4b0-35c4-977e-10d11020e673 | -9.88945 | -47.65279 | 2025-10-18 04:29:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 9b950c07-c6f1-39cd-8fb1-dad557a15323 | -8.02509 | -48.19445 | 2025-10-18 04:29:00 | NPP-375D | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| abab82dc-8440-3466-a9e0-bff63e5fb13c | -10.62477 | -45.23912 | 2025-10-18 04:29:00 | NPP-375D | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 52f8d325-c02f-3fdc-baa9-7fbbf057116c | -8.15581 | -49.29379 | 2025-10-18 04:29:00 | NPP-375D | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b15d7b73-5f6c-3185-bd36-589687866371 | -5.00851 | -46.02357 | 2025-10-18 04:29:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 0f63e263-2004-3c49-b734-3c094b7d992d | -5.12568 | -45.12554 | 2025-10-18 04:29:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 160ad331-6c56-3feb-9f89-7579427e12ed | -4.91618 | -45.40881 | 2025-10-18 04:29:00 | NPP-375D | LAGOA GRANDE DO MARANHÃO | MARANHÃO | Brasil | 2105963 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| fe9d5613-4b14-372d-833e-64ded812312c | -10.6288 | -45.23583 | 2025-10-18 04:29:00 | NPP-375D | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 4c4d9a4d-0fe5-3ba4-9d54-353e76818905 | -6.31479 | -44.32163 | 2025-10-18 04:29:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| e0512271-3677-36c2-af22-ff9fffa67c4d | -8.35671 | -46.22016 | 2025-10-18 04:29:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 1db51bd7-fc0a-34c1-8181-2f42acc4e62c | -5.15587 | -46.26657 | 2025-10-18 04:29:00 | NPP-375D | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4a866d92-0125-3702-a2ab-7f93efda2308 | -4.91896 | -45.41283 | 2025-10-18 04:29:00 | NPP-375D | LAGOA GRANDE DO MARANHÃO | MARANHÃO | Brasil | 2105963 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 17860f41-c2e9-3c23-b207-086c5c92f20a | -5.20345 | -45.75613 | 2025-10-18 04:29:00 | NPP-375D | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 427c7b7d-6588-3d04-b25e-23d5a592d73c | -4.69093 | -45.8494 | 2025-10-18 04:29:00 | NPP-375D | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 406cb45c-eea5-35b9-93ab-eaf630fdb4b4 | -7.34815 | -43.86024 | 2025-10-18 04:29:00 | NPP-375D | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 17.3 |
| 0326ff4a-92f9-3606-910e-07a5e5e95924 | -5.92163 | -44.75893 | 2025-10-18 04:29:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| e1f3e427-6430-3937-8024-2209c3eddc09 | -6.64917 | -43.67032 | 2025-10-18 04:29:00 | NPP-375D | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 5.0 |
| a0cba2ea-209e-3ef7-9fdd-92d0ed0ae0e7 | -4.53602 | -48.41095 | 2025-10-18 04:29:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 10691f92-2c2a-3ac9-87bb-267e01a4f235 | -5.30479 | -44.84815 | 2025-10-18 04:29:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 0440da4b-096f-3f86-85cf-695f88efc343 | -10.81407 | -43.92855 | 2025-10-18 04:29:00 | NPP-375D | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 6ed7837b-6685-3089-9f8e-7a6884ce4f79 | -6.14629 | -44.30027 | 2025-10-18 04:29:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 47163b60-454b-3aa5-971a-f946e7602064 | -10.50246 | -43.36668 | 2025-10-18 04:29:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 98df1053-d88c-3939-be8a-31ad5ee1ca7b | -5.94666 | -51.59681 | 2025-10-18 04:29:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ff33d4a2-2e8f-3403-ae91-29424b3c5f6c | -5.89677 | -44.76251 | 2025-10-18 04:29:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 0.2 |
| 09e826df-104c-3b1b-a6e2-187514c9e859 | -10.09402 | -47.66389 | 2025-10-18 04:29:00 | NPP-375D | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 241040ee-6508-303b-b258-d117fe133684 | -6.53723 | -55.04775 | 2025-10-18 04:29:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 6a8d109d-a627-3d97-84c4-0955ea9abb04 | -5.88695 | -43.92479 | 2025-10-18 04:29:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 2d8b7ea5-bbf8-305e-bf66-16a1f50435a0 | -8.45317 | -44.1693 | 2025-10-18 04:29:00 | NPP-375D | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 6610f9d6-f109-3226-8969-f1e9dcbeae7f | -8.10348 | -45.4285 | 2025-10-18 04:29:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 483b4486-ff81-3660-abdd-3a8c928ce0a0 | -4.53953 | -48.41152 | 2025-10-18 04:29:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 5725c8e7-9611-365b-8ba1-0c7521084bf0 | -8.91237 | -47.30431 | 2025-10-18 04:29:00 | NPP-375D | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f36e3dec-c0eb-3c7f-a473-a5e9e376ead0 | -6.88832 | -45.44978 | 2025-10-18 04:29:00 | NPP-375D | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 4850b8a0-67ca-39a6-9368-68c4e81da8b8 | -8.10794 | -49.82789 | 2025-10-18 04:29:00 | NPP-375D | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 34031d59-75f8-36fb-81fa-35acb4b5fd73 | -6.47822 | -44.57031 | 2025-10-18 04:29:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 9afa8d2a-0aa9-3db3-90eb-6f24d20e0ea8 | -10.0774 | -47.63955 | 2025-10-18 04:29:00 | NPP-375D | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e9e4dc08-c917-3772-b5bd-52eaadf3bceb | -6.86997 | -44.6972 | 2025-10-18 04:29:00 | NPP-375D | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| d2b6edb0-cb3b-3d92-89b5-ef7771288613 | -10.51222 | -43.40532 | 2025-10-18 04:29:00 | NPP-375D | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 966f8d7c-1d0f-3f71-9005-a41b8b19b017 | -4.9725 | -48.36646 | 2025-10-18 04:29:00 | NPP-375D | ABEL FIGUEIREDO | PARÁ | Brasil | 1500131 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 0e2f487f-5848-3ac3-8f22-ca4ca67c733f | -5.25039 | -50.96133 | 2025-10-18 04:29:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| a5e8e38b-4656-3655-9bc9-03da6c179289 | -10.41929 | -47.74564 | 2025-10-18 04:29:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f0941d3d-978c-31b3-8cf1-64dd1e528862 | -5.60099 | -46.38324 | 2025-10-18 04:29:00 | NPP-375D | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 2e88c449-fc09-3481-858e-dbf2fa7209ac | -6.37358 | -44.70464 | 2025-10-18 04:29:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 1b21bd6f-ad7f-3e5a-a010-c30594238148 | -6.29781 | -44.71927 | 2025-10-18 04:29:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 13.6 |
| 2f94e100-ba02-3e50-8293-3d96dcaf0f34 | -5.56301 | -44.15146 | 2025-10-18 04:29:00 | NPP-375D | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 4b9ac201-eabc-3222-8718-3dcf64765ff1 | -4.96472 | -44.60904 | 2025-10-18 04:29:00 | NPP-375D | SÃO JOSÉ DOS BASÍLIOS | MARANHÃO | Brasil | 2111250 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |


[Clique aqui para ver as próximas entradas](README47.md)
