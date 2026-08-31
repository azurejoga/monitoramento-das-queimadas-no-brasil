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

## Dados Diários - Página 131

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 91bb2a81-822d-3bc4-902e-eb2c70a9360e | -7.64714 | -46.73787 | 2026-08-31 16:33:00 | NPP-375 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 7185b965-1f0e-326f-9964-561dcfff1f9b | -7.09925 | -45.78603 | 2026-08-31 16:33:00 | NPP-375 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 07274a11-7dcc-3183-a213-aadbe4f2991b | -8.39302 | -46.4633 | 2026-08-31 16:33:00 | NPP-375 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 76.8 |
| 9ed46110-9690-321d-a4f7-c2e2ec35e3d3 | -6.21984 | -53.57961 | 2026-08-31 16:33:00 | NPP-375 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 8.5 |
| 6f427c80-1934-3d53-bd74-da0a51aa3c46 | -7.60585 | -44.99659 | 2026-08-31 16:33:00 | NPP-375 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 8.1 |
| d1cde03f-8122-3530-9226-21b076b916e7 | -6.25748 | -42.87491 | 2026-08-31 16:33:00 | NPP-375 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 3599cd56-f130-35fb-b253-73ab1bcf3aaa | -7.79492 | -44.07568 | 2026-08-31 16:33:00 | NPP-375 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 18.1 |
| 9dbc7ea2-6540-3c0c-81be-5f1580f23710 | -6.76971 | -52.92601 | 2026-08-31 16:33:00 | NPP-375 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 131e3251-d910-3bb2-ad73-fba6a1cc5244 | -5.88793 | -52.06046 | 2026-08-31 16:33:00 | NPP-375 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 19.5 |
| e04a0505-ef61-3f1e-9212-f3b07fb8d513 | -3.3227 | -49.86909 | 2026-08-31 16:33:00 | NPP-375 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 13.6 |
| bf07b0f8-7102-340a-8ad7-02ef07af755d | -1.94637 | -50.64978 | 2026-08-31 16:33:00 | NPP-375 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 38.9 |
| 185125ec-45af-33c7-a68f-5f7f01e19e0b | -7.89059 | -47.08495 | 2026-08-31 16:33:00 | NPP-375 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 03bf83ef-a72e-3576-a4c7-d0703d85ee64 | -5.4069 | -45.88511 | 2026-08-31 16:33:00 | NPP-375 | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 565b9cdc-ca3e-3e3a-9e81-b35616319570 | -4.91808 | -40.669 | 2026-08-31 16:33:00 | NPP-375 | IPAPORANGA | CEARÁ | Brasil | 2305654 | 23 | 33 | nan | nan | nan | Caatinga | 7.9 |
| c6b61b01-b407-3ac4-983f-094344db9dbb | -3.54486 | -51.11492 | 2026-08-31 16:33:00 | NPP-375 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 13.3 |
| fcb52228-9bd4-3a0e-b6e2-3c02081cb19d | -6.93661 | -44.1838 | 2026-08-31 16:33:00 | NPP-375 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| eaa27d4c-50cf-377c-9097-c3d201e9cc8e | -7.09134 | -45.78286 | 2026-08-31 16:33:00 | NPP-375 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 15.8 |
| 6793fee5-861e-31ff-9184-cab170b930f0 | -5.88938 | -47.73261 | 2026-08-31 16:33:00 | NPP-375 | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 9.6 |
| b3504f9a-ac01-398e-9ea5-db92a419b655 | -5.89175 | -52.24668 | 2026-08-31 16:33:00 | NPP-375 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| bf7802e8-1d60-3711-abfc-695628a2c97b | -7.97846 | -44.2802 | 2026-08-31 16:33:00 | NPP-375 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 13.6 |
| a489dbc0-4de8-3ea9-aafa-49aa820e6dc9 | -7.85491 | -45.17706 | 2026-08-31 16:33:00 | NPP-375 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 6b3d54c2-74d8-365b-b73e-3629ec2382ae | -7.99258 | -44.32782 | 2026-08-31 16:33:00 | NPP-375 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 75.4 |
| 1c66fe04-5815-375f-bd23-3286a9c1babc | -7.22373 | -42.76114 | 2026-08-31 16:33:00 | NPP-375 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 11.9 |
| 8d74020c-f15f-39f6-9968-b8a9da51a191 | -7.41698 | -44.24999 | 2026-08-31 16:33:00 | NPP-375 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 4.7 |
| ac28af03-e710-37b7-b9f9-e03993c14770 | -7.63581 | -46.71782 | 2026-08-31 16:33:00 | NPP-375 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 175bdb6b-6ae5-30ce-ac44-52fe8c86a0b0 | -6.26942 | -53.35966 | 2026-08-31 16:33:00 | NPP-375 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| b0bd7d5a-7769-3c13-9baf-7d24890fae88 | -5.76385 | -44.12468 | 2026-08-31 16:33:00 | NPP-375 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 9.1 |
| b2e04e11-f2ce-37d9-b6eb-973c74169f57 | -7.63128 | -44.92392 | 2026-08-31 16:33:00 | NPP-375 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 29.5 |
| 03255c13-81b9-3991-a690-dbd41e92c63d | -4.97237 | -37.3392 | 2026-08-31 16:33:00 | NPP-375 | MOSSORÓ | RIO GRANDE DO NORTE | Brasil | 2408003 | 24 | 33 | nan | nan | nan | Caatinga | 6.9 |
| d187218d-2e89-3469-af90-f406c1822f07 | -7.42096 | -44.2532 | 2026-08-31 16:33:00 | NPP-375 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 23.3 |
| a6df494b-7ab0-3299-8d81-33f85caeca9d | -3.05429 | -45.17698 | 2026-08-31 16:33:00 | NPP-375 | VIANA | MARANHÃO | Brasil | 2112803 | 21 | 33 | nan | nan | nan | Amazônia | 2.7 |
| ed187413-a5a7-3983-86d7-320543442056 | -7.11296 | -42.21523 | 2026-08-31 16:33:00 | NPP-375 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 3.8 |
| 1121135d-0f93-3272-9398-e775d97f7cf9 | -6.20739 | -53.58801 | 2026-08-31 16:33:00 | NPP-375 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 13.8 |
| 8ed75513-0605-3936-b220-bad4571933d3 | -6.33321 | -47.3042 | 2026-08-31 16:33:00 | NPP-375 | PORTO FRANCO | MARANHÃO | Brasil | 2109007 | 21 | 33 | nan | nan | nan | Cerrado | 43.2 |
| 4bb3ab48-6df5-306f-8434-891c133597b4 | -5.59226 | -42.32899 | 2026-08-31 16:33:00 | NPP-375 | BENEDITINOS | PIAUÍ | Brasil | 2201606 | 22 | 33 | nan | nan | nan | Caatinga | 7.3 |
| c49c89ac-5d7c-3e15-9cea-51ff347a294c | -7.51881 | -44.44884 | 2026-08-31 16:33:00 | NPP-375 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.3 |
| cb5f8c76-90e2-38cf-b8d8-6b3111f69e65 | -6.8728 | -41.6829 | 2026-08-31 16:33:00 | NPP-375 | IPIRANGA DO PIAUÍ | PIAUÍ | Brasil | 2204808 | 22 | 33 | nan | nan | nan | Caatinga | 4.4 |
| 806b016c-4824-3f75-ab24-a4f358b88032 | -6.34412 | -44.09068 | 2026-08-31 16:33:00 | NPP-375 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 8dbb1162-0a2e-3101-a1e3-685b2dce6b9e | -8.17356 | -54.93428 | 2026-08-31 16:33:00 | NPP-375 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 30.4 |
| 6f6e4a72-6ee5-3db1-996a-7777b4e84d32 | -7.64646 | -46.73302 | 2026-08-31 16:33:00 | NPP-375 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 629dad76-622d-30ee-b1d3-197c83d503c1 | -6.84755 | -41.7193 | 2026-08-31 16:33:00 | NPP-375 | IPIRANGA DO PIAUÍ | PIAUÍ | Brasil | 2204808 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 18323ba4-2182-3b30-b1c2-055d47f89b07 | -6.86103 | -41.69553 | 2026-08-31 16:33:00 | NPP-375 | IPIRANGA DO PIAUÍ | PIAUÍ | Brasil | 2204808 | 22 | 33 | nan | nan | nan | Caatinga | 12.7 |
| 7ef960b0-67dd-3c8e-8562-587821e109c6 | -7.99314 | -44.33159 | 2026-08-31 16:33:00 | NPP-375 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 75.4 |
| f00fbbf9-a6fd-3647-9d08-b0be53886817 | -1.08978 | -46.58719 | 2026-08-31 16:33:00 | NPP-375 | AUGUSTO CORRÊA | PARÁ | Brasil | 1500909 | 15 | 33 | nan | nan | nan | Amazônia | 40.7 |
| 882c6cca-a36d-39d0-8b86-222d16bbf73a | -7.10857 | -42.76104 | 2026-08-31 16:33:00 | NPP-375 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 10.3 |
| 4d7b5832-3fd1-302f-9c2e-4559b2b49b38 | -7.96675 | -44.32014 | 2026-08-31 16:33:00 | NPP-375 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 11.0 |
| b20b169c-777d-3c4c-89a2-0ab94b964edd | -7.98558 | -44.35201 | 2026-08-31 16:33:00 | NPP-375 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 6.1 |
| a8761945-cf5b-38c0-9eba-41a49cee2133 | -4.30006 | -49.09859 | 2026-08-31 16:33:00 | NPP-375 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 12.6 |
| 0617d91e-4920-32e7-8333-f628f72965bf | -5.86445 | -52.09015 | 2026-08-31 16:33:00 | NPP-375 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 9.6 |
| aea9d584-b584-3d15-97d1-eb9f513d387f | -2.48183 | -49.06134 | 2026-08-31 16:33:00 | NPP-375 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 08586dde-e492-32e5-a650-bced7a9a45b1 | -1.06684 | -47.80241 | 2026-08-31 16:33:00 | NPP-375 | SÃO FRANCISCO DO PARÁ | PARÁ | Brasil | 1507409 | 15 | 33 | nan | nan | nan | Amazônia | 7.6 |
| 694f15e0-2daf-39fe-9dfe-294d84e925fb | -7.60289 | -45.00105 | 2026-08-31 16:33:00 | NPP-375 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 14f1c684-23f8-34aa-a658-0760eec92ae2 | -6.94136 | -55.64407 | 2026-08-31 16:33:00 | NPP-375 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 20.7 |
| 586c1685-180b-3182-873b-e089b2de99a9 | -6.93285 | -55.62862 | 2026-08-31 16:33:00 | NPP-375 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 34.2 |
| 1b2bf4fb-b7c8-332d-8de2-4eef0145ca5d | -7.99334 | -44.28552 | 2026-08-31 16:33:00 | NPP-375 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 0.0 |
| a327c013-0edf-31a5-a4fb-2bf941a580fd | -8.82635 | -50.59452 | 2026-08-31 16:33:00 | NPP-375 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 8.8 |
| 1241c35b-e7ef-387c-9c7f-d3d98b9ca4e0 | -8.12974 | -45.56357 | 2026-08-31 16:33:00 | NPP-375 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 19.1 |
| d8304c2f-3a7c-3033-8076-61a876d5016f | -6.69042 | -44.83956 | 2026-08-31 16:33:00 | NPP-375 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 7088a198-8b3b-3f56-a497-6dec6dae70c8 | -5.58171 | -42.32704 | 2026-08-31 16:33:00 | NPP-375 | BENEDITINOS | PIAUÍ | Brasil | 2201606 | 22 | 33 | nan | nan | nan | Caatinga | 9.5 |
| ea8a80ea-af0c-3435-aad2-404f35cfe762 | -7.56241 | -44.33852 | 2026-08-31 16:33:00 | NPP-375 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 21.2 |
| 759a6a3e-e562-3499-abb1-daa8b851596e | -6.84366 | -41.7163 | 2026-08-31 16:33:00 | NPP-375 | IPIRANGA DO PIAUÍ | PIAUÍ | Brasil | 2204808 | 22 | 33 | nan | nan | nan | Caatinga | 19.1 |
| e081bac3-912a-389a-8d00-6f3e499580b9 | -5.59118 | -42.32203 | 2026-08-31 16:33:00 | NPP-375 | BENEDITINOS | PIAUÍ | Brasil | 2201606 | 22 | 33 | nan | nan | nan | Caatinga | 4.9 |
| 9f288f0b-9401-3f72-9c06-acebe6922c85 | -7.10751 | -42.75407 | 2026-08-31 16:33:00 | NPP-375 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 11.8 |
| 179a559c-1341-350a-9d8a-89153e34fcb9 | -6.78215 | -45.21574 | 2026-08-31 16:33:00 | NPP-375 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 89992d6f-7f12-3552-97aa-8aac8fbee655 | -1.8724 | -50.6542 | 2026-08-31 16:33:00 | NPP-375 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 8.1 |
| 69ffd96b-44e2-3422-8277-4a5b6d3a7663 | -1.89163 | -48.28803 | 2026-08-31 16:33:00 | NPP-375 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 68e9c99c-1bdb-31f1-9a9b-f7f0df656aaf | -6.25062 | -53.67807 | 2026-08-31 16:33:00 | NPP-375 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 9.1 |
| f9bb3976-9466-36af-9585-0d2c77badd49 | -8.71086 | -52.3675 | 2026-08-31 16:33:00 | NPP-375 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 7.8 |
| 042ec02a-0621-334a-9fd2-0f0598022aff | -5.89616 | -52.2382 | 2026-08-31 16:33:00 | NPP-375 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 6.8 |
| ff749243-33a5-310d-8eeb-701bc82d7881 | -7.64441 | -46.71852 | 2026-08-31 16:33:00 | NPP-375 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 68f6c04c-7fb8-3423-8b6d-f71f1f3ebe1a | -6.25731 | -53.68186 | 2026-08-31 16:33:00 | NPP-375 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 8.6 |
| 07977f0e-18cc-36b6-b5de-ff00368cd11f | -7.1147 | -42.75653 | 2026-08-31 16:33:00 | NPP-375 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 12.7 |
| 3227f3fe-7417-3c7d-b6d7-711d00401cd4 | -7.10698 | -42.75059 | 2026-08-31 16:33:00 | NPP-375 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 5.4 |
| aa20efdd-27ad-3e30-b09e-52d870d4103d | -7.37392 | -45.07803 | 2026-08-31 16:33:00 | NPP-375 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 9a3b8e66-e483-37ab-b2c7-528a1584ee88 | -4.30929 | -49.10141 | 2026-08-31 16:33:00 | NPP-375 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| dbd48161-e909-3559-b957-fda6a16eb608 | -2.56657 | -48.93734 | 2026-08-31 16:33:00 | NPP-375 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 7.3 |
| c9be22fe-ef20-37c6-8698-ae5db6c10249 | -5.76615 | -44.11701 | 2026-08-31 16:33:00 | NPP-375 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| c377fa6b-3773-3d29-81d3-bf6dc7220bbd | -6.29444 | -53.58755 | 2026-08-31 16:33:00 | NPP-375 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 9.2 |
| 3c4556b1-a979-3b18-a26c-8501c069f158 | -7.92303 | -44.29998 | 2026-08-31 16:33:00 | NPP-375 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 8.4 |
| 91d02f4e-adfc-3384-8e37-387db8d796d3 | -6.15886 | -52.63996 | 2026-08-31 16:33:00 | NPP-375 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 12.0 |
| c0d43b62-a343-37ee-8731-64175a6a2f3a | -7.43293 | -44.94438 | 2026-08-31 16:33:00 | NPP-375 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 8.5 |
| a8ce2580-e349-3d65-a88d-c930a570a510 | -8.08851 | -45.48214 | 2026-08-31 16:33:00 | NPP-375 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 31febcb5-8b1a-3adb-8cc4-03b6f79253cf | -7.35682 | -45.08458 | 2026-08-31 16:33:00 | NPP-375 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 7a0ac367-7695-320a-a7d0-b63f5e5711a3 | -7.59877 | -44.99755 | 2026-08-31 16:33:00 | NPP-375 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 339b5622-e054-3e6b-a122-4f90fcb08c61 | -4.32025 | -45.23368 | 2026-08-31 16:33:00 | NPP-375 | VITORINO FREIRE | MARANHÃO | Brasil | 2113009 | 21 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 0b716866-d073-3b87-9ad3-a3db6c0e6f10 | -6.20654 | -52.9876 | 2026-08-31 16:33:00 | NPP-375 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 7.0 |
| dcfd2036-b865-35d1-a540-4a37efa3782f | -7.91564 | -44.23607 | 2026-08-31 16:33:00 | NPP-375 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 15.8 |
| 59a2f0ab-aa0a-3b4d-8425-b0d277793448 | -5.85853 | -52.08729 | 2026-08-31 16:33:00 | NPP-375 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| a0b4df61-daea-3190-b1be-6c2cfde65c0a | -6.16539 | -44.84706 | 2026-08-31 16:33:00 | NPP-375 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 763c67b2-282a-3dd8-8af2-5bc04dfb32bc | -7.92252 | -44.235 | 2026-08-31 16:33:00 | NPP-375 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 30.3 |
| b8a374d2-e994-3bb9-95c2-f129ed9b74ab | -3.73142 | -44.37638 | 2026-08-31 16:33:00 | NPP-375 | MATÕES DO NORTE | MARANHÃO | Brasil | 2106631 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 8d173a10-3a3a-31d2-bc38-ee870e2017ad | -7.36507 | -45.06713 | 2026-08-31 16:33:00 | NPP-375 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 5.7 |
| bceda775-e5eb-398e-bbf9-13637eb8135f | -7.98578 | -44.30583 | 2026-08-31 16:33:00 | NPP-375 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 14.9 |
| a3dd4d28-ce59-3c00-992d-35f1f20e667d | -7.64373 | -46.7137 | 2026-08-31 16:33:00 | NPP-375 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 5b213b27-ecba-32cf-8ce1-a39eb02c046e | -7.82371 | -44.47688 | 2026-08-31 16:33:00 | NPP-375 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 6d5acc2c-c133-3862-93a3-b15eb2c6fb46 | -7.22533 | -42.77159 | 2026-08-31 16:33:00 | NPP-375 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 12.5 |
| ca5c5139-9c61-33d9-9332-d17aa68e0a85 | -6.7257 | -45.07495 | 2026-08-31 16:33:00 | NPP-375 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 0a35ee83-d0fe-31e0-ac57-e25b259185b3 | -6.16499 | -56.11187 | 2026-08-31 16:33:00 | NPP-375 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| a3e7c40a-7d53-358e-9a70-cba9ac5946a4 | -2.03939 | -48.23256 | 2026-08-31 16:33:00 | NPP-375 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 09771e2e-5e56-3ef1-8ede-2892c096f39a | -1.53477 | -50.49516 | 2026-08-31 16:33:00 | NPP-375 | BREVES | PARÁ | Brasil | 1501808 | 15 | 33 | nan | nan | nan | Amazônia | 7.5 |


[Clique aqui para ver as próximas entradas](README132.md)
