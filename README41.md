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

## Dados Diários - Página 41

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| dc9b2765-d249-3da4-b2c2-33cd9870ad81 | -5.73839 | -45.29582 | 2025-09-11 04:21:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 030b4713-e975-30fa-8cd2-908986ab0980 | -6.41386 | -44.49622 | 2025-09-11 04:21:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 779675a9-5e18-3017-8b86-15db8b044337 | -6.62134 | -43.9928 | 2025-09-11 04:21:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| e86e7289-eefe-3d1d-8e4a-6aef0899a135 | -7.77859 | -50.98876 | 2025-09-11 04:21:00 | NPP-375D | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 848e2a9b-4f42-3550-b34f-d99a0367cd7d | -8.03733 | -48.68128 | 2025-09-11 04:21:00 | NPP-375D | BANDEIRANTES DO TOCANTINS | TOCANTINS | Brasil | 1703057 | 17 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7fd2e98a-c74b-3c4f-b35c-4f3428ff52e5 | -7.45085 | -44.97128 | 2025-09-11 04:21:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 537a3ca4-deda-325e-b32c-760243653c27 | -5.90055 | -45.76722 | 2025-09-11 04:21:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 07b6dee1-cd52-385f-ad92-c4ed2a06e551 | -9.00344 | -46.0818 | 2025-09-11 04:21:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 70504b92-de37-3252-8f09-d23667671432 | -6.66732 | -44.12915 | 2025-09-11 04:21:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| fb0a43a1-c5da-3a7d-a879-fdc04b71406a | -7.25892 | -44.44867 | 2025-09-11 04:21:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 3dc70309-239d-3ac4-b2f6-41bb47f703c5 | -8.47618 | -47.28835 | 2025-09-11 04:21:00 | NPP-375D | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 42950fac-1eb7-3983-93f8-b23417349da1 | -3.35086 | -42.16114 | 2025-09-11 04:21:00 | NPP-375D | MAGALHÃES DE ALMEIDA | MARANHÃO | Brasil | 2106300 | 21 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 24fec176-b07a-3733-813d-027f12faf51f | -6.35144 | -43.03724 | 2025-09-11 04:21:00 | NPP-375D | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| cc7b333d-903b-3323-994e-b0ac1136fef1 | -7.20494 | -44.96439 | 2025-09-11 04:21:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 9aa6d2ce-7241-3201-98cf-5a20bb3e3372 | -5.33626 | -44.80621 | 2025-09-11 04:21:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 38da326c-926f-345c-9bf6-6656f06f0bac | -7.62542 | -46.54714 | 2025-09-11 04:21:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b80d15d4-2301-3d02-8308-b2c8fba91f86 | -7.50153 | -48.24415 | 2025-09-11 04:21:00 | NPP-375D | NOVA OLINDA | TOCANTINS | Brasil | 1714880 | 17 | 33 | nan | nan | nan | Cerrado | 4.9 |
| e2eb7c23-9982-38c8-b6b1-1cfff20d0294 | -6.28701 | -42.41003 | 2025-09-11 04:21:00 | NPP-375D | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| d287eca3-07e8-30ab-ad7a-abefa0113cef | -6.16814 | -53.50475 | 2025-09-11 04:21:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6bd22255-31f1-37f6-a99d-042d6d1d52df | -7.77898 | -50.77994 | 2025-09-11 04:21:00 | NPP-375D | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 4ed529ca-3ed4-34a5-8793-35a998c8858e | -5.33958 | -44.80674 | 2025-09-11 04:21:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 4b6ff44a-0ac8-3b70-96ac-5d0ba980fdc9 | -5.94337 | -45.7154 | 2025-09-11 04:21:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 2676b8f9-f742-3cfa-a5d2-e9545be8aaad | -5.77542 | -44.85424 | 2025-09-11 04:21:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| cf693b21-056f-3147-ba6b-ad57695b2af1 | -6.82816 | -45.61354 | 2025-09-11 04:21:00 | NPP-375D | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 270bbf85-b39e-3f6c-b7cf-84809ebbbb23 | -7.86383 | -46.04773 | 2025-09-11 04:21:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c17f3d3f-9e2f-378f-94a0-358f64c7e88d | -7.3934 | -44.366 | 2025-09-11 04:21:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 286a913b-a2b3-3243-8fec-404598a237b8 | -5.92551 | -46.17886 | 2025-09-11 04:21:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 2e390719-169b-3192-bf80-95b847422f78 | -8.46008 | -47.27788 | 2025-09-11 04:21:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d674e092-a108-33d5-87ec-cd825cf0d1ec | -6.9966 | -44.7847 | 2025-09-11 04:21:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 8af86549-0335-3a0e-9c1b-952a3958233d | -5.5171 | -45.45225 | 2025-09-11 04:21:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 307ce831-19da-33d1-bcf1-28c61c2e8ae8 | -6.24263 | -43.49281 | 2025-09-11 04:21:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 33cb99a0-a71d-324b-b447-cad0dfe1ead5 | -4.58442 | -45.60781 | 2025-09-11 04:21:00 | NPP-375D | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 484bd1ff-fb9e-37e5-8359-1bc55580de76 | -5.72688 | -49.21942 | 2025-09-11 04:21:00 | NPP-375D | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| d65a2d90-80c4-3dfe-b76c-36f7e07a92b8 | -5.47364 | -43.43278 | 2025-09-11 04:21:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 4c831c2d-a60f-38f3-ba53-37931725a234 | -7.15142 | -39.41415 | 2025-09-11 04:21:00 | NPP-375D | CRATO | CEARÁ | Brasil | 2304202 | 23 | 33 | nan | nan | nan | Caatinga | 0.5 |
| dee53647-c3cc-37a2-8864-bf69478329e4 | -9.5209 | -43.06115 | 2025-09-11 04:21:00 | NPP-375D | CAMPO ALEGRE DE LOURDES | BAHIA | Brasil | 2905909 | 29 | 33 | nan | nan | nan | Caatinga | 1.0 |
| a16621a4-8ba1-3b93-9074-6044606b46db | -6.55422 | -42.92074 | 2025-09-11 04:21:00 | NPP-375D | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 3803d721-7a17-329a-bbff-b2f6304dd627 | -8.73938 | -47.08949 | 2025-09-11 04:21:00 | NPP-375D | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 25f6ee73-c3ca-35a1-a7b6-6ed71f94f185 | -5.12091 | -44.66929 | 2025-09-11 04:21:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 02c188c3-8ab4-31a5-a622-a071fa2d34ff | -5.89481 | -45.80302 | 2025-09-11 04:21:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 28ab3fa9-c1b1-3dad-84a7-8308d7ee15c2 | -6.26337 | -43.49235 | 2025-09-11 04:21:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 2215f6b4-a0f4-3741-9690-3c6b9265c43a | -7.78949 | -50.76965 | 2025-09-11 04:21:00 | NPP-375D | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 14.1 |
| d5a0d595-ff99-3f2b-a234-b2b48384ea2f | -6.40524 | -47.32821 | 2025-09-11 04:21:00 | NPP-375D | PORTO FRANCO | MARANHÃO | Brasil | 2109007 | 21 | 33 | nan | nan | nan | Cerrado | 0.4 |
| bdf6baa4-8939-32ca-a783-026ea797253e | -5.81966 | -44.20714 | 2025-09-11 04:21:00 | NPP-375D | JATOBÁ | MARANHÃO | Brasil | 2105450 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 85a625e0-6073-37e2-bdcd-04316265ff35 | -8.08924 | -48.23282 | 2025-09-11 04:21:00 | NPP-375D | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 69c1a325-e846-3feb-93a8-21f60407dcf7 | -8.35218 | -45.41101 | 2025-09-11 04:21:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ccacca2a-102f-3f38-b73a-3f83d42d5eb7 | -6.85625 | -47.87671 | 2025-09-11 04:21:00 | NPP-375D | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 22891c5a-6e4a-3714-8c75-2de286a692dc | -6.79967 | -44.78953 | 2025-09-11 04:21:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 47ed8ee4-e8cd-320c-a878-d4e70ddc58b9 | -6.85555 | -47.88092 | 2025-09-11 04:21:00 | NPP-375D | WANDERLÂNDIA | TOCANTINS | Brasil | 1722081 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 57ed2a9e-9884-3342-a817-3245b0a03a6c | -5.69294 | -45.33172 | 2025-09-11 04:21:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 7f0e6a21-5b9b-3a1d-98cd-ba95e4a62326 | -7.20161 | -44.96387 | 2025-09-11 04:21:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 3012758d-5bb2-3f48-b60c-f9f20b488148 | -6.47421 | -41.75353 | 2025-09-11 04:21:00 | NPP-375D | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 292a06fe-1538-33b1-a5eb-c3cb14fb350e | -7.48961 | -54.95214 | 2025-09-11 04:21:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 4f8008f1-1651-35c0-a790-87ed7afca84e | -7.92025 | -44.87082 | 2025-09-11 04:21:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| cb46fa3e-ac84-36ea-86ce-87aca80c18c7 | -8.10165 | -48.24802 | 2025-09-11 04:21:00 | NPP-375D | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 1abc8043-e4b8-3831-81af-fa2f0734f919 | -8.71162 | -45.27908 | 2025-09-11 04:21:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 35d1260e-173d-3344-bdeb-29c606af53db | -7.32995 | -49.60583 | 2025-09-11 04:21:00 | NPP-375D | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f35a38af-b681-3883-9e8b-c912575c4d66 | -7.22987 | -43.98398 | 2025-09-11 04:21:00 | NPP-375D | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f9c9ed82-105e-3c04-a5a5-95e386d573a8 | -6.69902 | -44.93632 | 2025-09-11 04:21:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| eb820390-2fc3-3aad-8a47-846f765d036d | -6.27556 | -43.39182 | 2025-09-11 04:21:00 | NPP-375D | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 12f491dc-8609-32b3-be3c-a8aef078c881 | -5.9563 | -45.69926 | 2025-09-11 04:21:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| c9136b06-a61d-3f75-9078-096d59de41d9 | -5.9691 | -44.72112 | 2025-09-11 04:21:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 328ebc93-602b-357a-b49b-6d647a1329d7 | -6.42307 | -44.39444 | 2025-09-11 04:21:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| d5116d22-7348-3741-ae4f-0f666678ecc3 | -7.84641 | -45.40218 | 2025-09-11 04:21:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| e1189384-f7ea-3064-acf6-329d4b1aaac0 | -7.49102 | -54.94437 | 2025-09-11 04:21:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 879666aa-fffa-3b21-94e4-50ba4b62ebc6 | -7.50572 | -48.26084 | 2025-09-11 04:21:00 | NPP-375D | NOVA OLINDA | TOCANTINS | Brasil | 1714880 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 8f02a5d4-cf97-3953-8226-44bb460a7af0 | -5.93725 | -45.68887 | 2025-09-11 04:21:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 827028d7-71d3-3cbc-8e66-c6ca6acebd97 | -3.74094 | -49.04374 | 2025-09-11 04:21:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 6a946fe3-1599-34ff-a59a-b39b603af401 | -5.91952 | -45.82163 | 2025-09-11 04:21:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 0a733ab8-8996-3a2a-8740-c43994c57981 | -7.31913 | -44.60808 | 2025-09-11 04:21:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| dbe7cc67-d215-3dae-a746-63e4f045e9b9 | -8.16583 | -46.0745 | 2025-09-11 04:21:00 | NPP-375D | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| cb5698b8-8bdb-3a8e-9051-d7cb8e5dac94 | -7.54082 | -44.67501 | 2025-09-11 04:21:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f9e17d72-846f-3961-94ad-6f8e0eb9db25 | -9.05748 | -45.72177 | 2025-09-11 04:21:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 3.1 |
| b3077282-b534-3051-a161-67c3bdbb28a5 | -5.72509 | -45.61596 | 2025-09-11 04:21:00 | NPP-375D | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 83b74701-3950-3d68-a720-820dce5631f6 | -7.53962 | -44.66787 | 2025-09-11 04:21:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| cff17256-3263-38de-8a93-7efdcc609b6d | -6.37139 | -44.48883 | 2025-09-11 04:21:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ccbfc236-acea-3071-b5a0-1546c7de1126 | -5.70244 | -45.45614 | 2025-09-11 04:21:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b9ac0fae-3eab-3deb-b15c-b5b09bb5a68f | -8.02229 | -49.05309 | 2025-09-11 04:21:00 | NPP-375D | BERNARDO SAYÃO | TOCANTINS | Brasil | 1703206 | 17 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 9eff60a5-6bb9-3c35-881b-854af705c59a | -2.07688 | -47.14515 | 2025-09-11 04:21:00 | NPP-375D | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ab020e90-13e4-3b67-b40b-41db50127c00 | -8.06886 | -50.179 | 2025-09-11 04:21:00 | NPP-375D | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| b4cf925c-e251-3999-9a0f-42802b60778b | -5.08085 | -41.14907 | 2025-09-11 04:21:00 | NPP-375D | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 37bc65bb-05b5-39a3-b912-2fa8371e37c8 | -7.47108 | -45.28848 | 2025-09-11 04:21:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 1dd7a6b2-8cb5-3326-ab1f-2665d4321eb6 | -7.85904 | -48.15855 | 2025-09-11 04:21:00 | NPP-375D | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 9ca5efaa-40ba-395f-a7f6-b6cf1926cf4d | -6.57248 | -42.93864 | 2025-09-11 04:21:00 | NPP-375D | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 1b3d1949-698d-3ede-a4d9-b0c888db72c8 | -6.73012 | -43.02298 | 2025-09-11 04:21:00 | NPP-375D | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 0a1d5e49-c4ed-3689-8395-9722f0832b4d | -6.38576 | -42.58694 | 2025-09-11 04:21:00 | NPP-375D | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 3.3 |
| a7b710af-8309-3f80-a1d5-83c9e6342508 | -7.16434 | -48.88944 | 2025-09-11 04:21:00 | NPP-375D | SANTA FÉ DO ARAGUAIA | TOCANTINS | Brasil | 1718865 | 17 | 33 | nan | nan | nan | Amazônia | 1.9 |
| e06d4c5c-a37e-30ea-a5c7-45a480749014 | -7.85854 | -45.51155 | 2025-09-11 04:21:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 888b6a57-560b-39b8-bbf3-ca96100f3e64 | -3.60389 | -42.85817 | 2025-09-11 04:21:00 | NPP-375D | BREJO | MARANHÃO | Brasil | 2102101 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 410cea4b-57fa-3619-af8a-f7f0ea3168d2 | -5.34291 | -44.80727 | 2025-09-11 04:21:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 52ee07b1-1e4c-3add-b26e-95d4d45b56eb | -7.53797 | -44.67834 | 2025-09-11 04:21:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 24fb79a0-d405-3f4a-b603-af33f844550b | -8.02233 | -49.02911 | 2025-09-11 04:21:00 | NPP-375D | BERNARDO SAYÃO | TOCANTINS | Brasil | 1703206 | 17 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 7e002529-ba9c-3add-a2fa-144b3dbe5c89 | -6.47011 | -44.11641 | 2025-09-11 04:21:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| c9369933-86b5-3677-93ef-aa5fe2008adf | -5.84488 | -45.39534 | 2025-09-11 04:21:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 0.4 |
| e7b0897e-1013-3fa3-ada8-338b2482e318 | -5.7058 | -45.45667 | 2025-09-11 04:21:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 3da2695b-3e7e-39ea-9f09-5167951c6658 | -7.86041 | -44.88277 | 2025-09-11 04:21:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 143ce588-b374-3a44-8de1-c2ef57bf2437 | -8.72847 | -47.09148 | 2025-09-11 04:21:00 | NPP-375D | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 0c564261-4ed8-30a7-818b-4a56505cfeed | -5.69408 | -43.33996 | 2025-09-11 04:21:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 6bd2a878-42cd-3150-886c-1210d714bcdd | -5.35735 | -43.40797 | 2025-09-11 04:21:00 | NPP-375D | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 0965e978-9d66-3572-aad0-e096c28f2109 | -7.83642 | -45.40062 | 2025-09-11 04:21:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 0.6 |


[Clique aqui para ver as próximas entradas](README42.md)
