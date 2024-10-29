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

## Dados Diários - Página 57

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 81ad4519-1407-3ca6-a31a-aec1505805a8 | -7.41861 | -44.79793 | 2024-10-29 04:40:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 963b2ca1-cb48-3272-be1c-30f8ea66c9cd | -7.41465 | -44.79727 | 2024-10-29 04:40:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 4b6ab595-d7d9-3057-a1e3-6567b11ae929 | -7.40995 | -44.80172 | 2024-10-29 04:40:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 5e92200a-592a-3874-9e49-dda4434bb968 | -7.256 | -44.19659 | 2024-10-29 04:40:00 | NOAA-21 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| a5f111fb-edc8-30b0-8c21-32fd5c5199f6 | -7.18455 | -44.02921 | 2024-10-29 04:40:00 | NOAA-21 | MARCOS PARENTE | PIAUÍ | Brasil | 2206001 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 6fcfcfc2-9e2d-33ff-a248-a0cf770664e0 | -6.62753 | -43.99624 | 2024-10-29 04:40:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 0b2ce088-b82f-3879-9bca-e2317d795a32 | -7.18816 | -44.72667 | 2024-10-29 04:40:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 0aedbb9e-466d-3538-9bbc-91d79fe4c9a0 | -7.07299 | -44.80272 | 2024-10-29 04:40:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| f9370e64-d015-3f7a-a9e6-10bb991f1dd8 | -6.97373 | -44.6278 | 2024-10-29 04:40:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c526b938-d9cb-3d0f-9761-197725ac0f9e | -7.87314 | -45.39367 | 2024-10-29 04:40:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 1fa17d86-a52c-3359-84cd-c24706000797 | -7.8693 | -45.39305 | 2024-10-29 04:40:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 30457f29-1558-3ee5-95ea-745a3c13097d | -7.86546 | -45.39244 | 2024-10-29 04:40:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 96a4397b-80f8-3abb-9a51-bc6f59450d7e | -9.12476 | -44.42183 | 2024-10-29 04:40:00 | NOAA-21 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| eba25d3c-f199-39b8-b2c8-829699bc0334 | -9.12421 | -44.42568 | 2024-10-29 04:40:00 | NOAA-21 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 132410cc-e1de-35e7-a6be-aff89c5b0085 | -9.12003 | -44.42514 | 2024-10-29 04:40:00 | NOAA-21 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 2f085c53-76cf-3b8a-96da-bcc765ecb255 | -9.19008 | -45.21561 | 2024-10-29 04:40:00 | NOAA-21 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 3f6c34da-e2fd-341f-a16a-9f69aeb5fb3b | -9.1868 | -45.21021 | 2024-10-29 04:40:00 | NOAA-21 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 1276bfdf-c604-3fc9-a523-d3fdcc2ec36e | -8.77064 | -44.71408 | 2024-10-29 04:40:00 | NOAA-21 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 12d77a96-b72d-39f1-bcc8-1f5c688852b8 | -8.76552 | -44.7207 | 2024-10-29 04:40:00 | NOAA-21 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 52b2b17e-d285-32ba-bb2d-a3e683be784b | -8.765 | -44.72431 | 2024-10-29 04:40:00 | NOAA-21 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| d1540acf-4b95-3e8b-9707-99adfd7808bd | -8.75896 | -44.70869 | 2024-10-29 04:40:00 | NOAA-21 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| d68102fa-ff7b-3074-8baf-7320c56bf933 | -8.75843 | -44.7123 | 2024-10-29 04:40:00 | NOAA-21 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 14183227-3122-3f12-9219-d94d3be5494f | -8.75791 | -44.71591 | 2024-10-29 04:40:00 | NOAA-21 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 55d5a829-a64e-3b68-a372-8b4aee72f73f | -8.75489 | -44.7081 | 2024-10-29 04:40:00 | NOAA-21 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 92dca489-9421-389d-a3ea-5061754b2ec9 | -8.75436 | -44.71171 | 2024-10-29 04:40:00 | NOAA-21 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 5cbbeb8b-35b4-3abc-8a11-0734fdcff4e1 | -8.75384 | -44.71532 | 2024-10-29 04:40:00 | NOAA-21 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 8c33006b-5444-3ce4-b101-8f11f0345d17 | -8.75332 | -44.71892 | 2024-10-29 04:40:00 | NOAA-21 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 61f6dabb-cb42-3e49-b7c0-06228f8b691b | -8.54392 | -44.61327 | 2024-10-29 04:40:00 | NOAA-21 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 53ef28ff-80f1-3c7d-907c-ac44c74db45e | -8.25566 | -44.85551 | 2024-10-29 04:40:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| bb27ca53-69a6-3008-b132-b57cff5fa934 | -8.25268 | -44.84774 | 2024-10-29 04:40:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 9aa85615-a3ac-3ac5-873f-af7605e4c9fa | -8.25217 | -44.85132 | 2024-10-29 04:40:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 38110a21-f005-3792-a514-6f6442af11d7 | -8.25166 | -44.85489 | 2024-10-29 04:40:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| dfd2ebd9-901a-3aad-bc7a-056dd8a5f789 | -8.24867 | -44.84712 | 2024-10-29 04:40:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f4cb384b-2787-3026-9105-af7b90dceed7 | -9.8603 | -44.32318 | 2024-10-29 04:40:00 | NOAA-21 | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 7855c99b-a7b8-3d4f-aab4-ec54532ddc42 | -9.85606 | -44.32254 | 2024-10-29 04:40:00 | NOAA-21 | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| b438716d-322f-38e7-8828-fadfba534074 | -10.87506 | -44.53817 | 2024-10-29 04:40:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 07397789-583e-33d2-bdc1-abf14bfb7cd2 | -10.80945 | -45.26215 | 2024-10-29 04:40:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 44e26215-359a-330c-a608-ba4309c22e8f | -10.74251 | -44.56213 | 2024-10-29 04:40:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 107b0bd2-ec8b-336c-9b0e-ee1af2627730 | -10.74223 | -44.56284 | 2024-10-29 04:40:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 64fe0a08-ca27-3c07-8c84-dd5264aa8f11 | -10.7383 | -44.56137 | 2024-10-29 04:40:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 8cdfb6df-b5d1-35da-b0bf-b3f9519b7cc3 | -10.73802 | -44.5621 | 2024-10-29 04:40:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a33ad72d-a3e6-34cc-8d3c-9ddaec1ba38c | -10.68306 | -45.30552 | 2024-10-29 04:40:00 | NOAA-21 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 79571fe9-79aa-3afa-b75a-2bd3f42a8748 | -10.68256 | -45.30909 | 2024-10-29 04:40:00 | NOAA-21 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 3410ddb6-1be5-3b9a-9e6c-cf0612c4d9a2 | -10.54404 | -45.13835 | 2024-10-29 04:40:00 | NOAA-21 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 4.7 |
| f84c2459-243e-3455-9df3-9f07963b4e5f | -10.54352 | -45.14203 | 2024-10-29 04:40:00 | NOAA-21 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 4.7 |
| aae75292-67e7-3e1f-abb5-2d21b12e7a99 | -10.51804 | -44.84635 | 2024-10-29 04:40:00 | NOAA-21 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 4.2 |
| e1973858-521d-3dfd-a718-608fa051306f | -10.51753 | -44.85009 | 2024-10-29 04:40:00 | NOAA-21 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 4.2 |
| f841145c-8100-3a3c-aac3-04911b012beb | -10.51391 | -44.84574 | 2024-10-29 04:40:00 | NOAA-21 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 316f7601-5962-31e3-b907-613e48c9d038 | -10.5134 | -44.84947 | 2024-10-29 04:40:00 | NOAA-21 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 6cca0eae-47a0-3f53-9f45-920cfcb4881e | -10.49842 | -45.10911 | 2024-10-29 04:40:00 | NOAA-21 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 6057d265-f768-30eb-a98e-58d2dd8312e3 | -10.48763 | -44.59281 | 2024-10-29 04:40:00 | NOAA-21 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 93abd6b5-4eaf-3b14-9fba-0bd77e05548c | -10.48709 | -44.59671 | 2024-10-29 04:40:00 | NOAA-21 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 3746b8e6-7c51-39f8-a51f-54dbef15ebb9 | -10.45356 | -44.89608 | 2024-10-29 04:40:00 | NOAA-21 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 5ef706af-afd0-3659-abe4-2a01638c9916 | -10.44997 | -44.89169 | 2024-10-29 04:40:00 | NOAA-21 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 60a470ee-2d8b-392f-8f02-2496b9205ec8 | -10.44944 | -44.89548 | 2024-10-29 04:40:00 | NOAA-21 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 8671cde7-2e3d-3954-98e5-50c275cfdf69 | -10.35519 | -45.09326 | 2024-10-29 04:40:00 | NOAA-21 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| dabced4a-13df-3b15-aa6a-40e1f46c4eed | -10.23472 | -44.79619 | 2024-10-29 04:40:00 | NOAA-21 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 54007b8d-7dda-390c-aaa9-ac40d863ae83 | -11.40837 | -45.1411 | 2024-10-29 04:40:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 3a3f3fcf-78e8-3bde-b0fd-cb5e6700e32d | -11.40785 | -45.1448 | 2024-10-29 04:40:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a70694f6-6660-350d-be1a-f46d96b5fdff | -11.40529 | -45.13316 | 2024-10-29 04:40:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 13ab13d0-e38d-35e2-94c7-41c4450a77d8 | -11.40478 | -45.13682 | 2024-10-29 04:40:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| ea2462f1-c215-3150-aa70-24eb069a88d5 | -11.40426 | -45.14048 | 2024-10-29 04:40:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b98f0b3d-9611-3aa0-807b-f39d6a858089 | -11.40375 | -45.14414 | 2024-10-29 04:40:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 0c5d42c4-7321-346b-9c01-7dd0546986c5 | -11.40323 | -45.1478 | 2024-10-29 04:40:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e11f54b2-3cbc-3329-8492-66039fe4134f | -11.40067 | -45.13622 | 2024-10-29 04:40:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 9ff24188-c75e-3dba-be5c-c44bcc7b7f00 | -11.40016 | -45.13987 | 2024-10-29 04:40:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 21b22699-3ce3-3697-88f4-7583eddc27ef | -11.39914 | -45.14716 | 2024-10-29 04:40:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b777a630-7307-35bf-ab70-b983d63f1486 | -11.39862 | -45.15082 | 2024-10-29 04:40:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b9ee989a-7eb1-3597-a5d1-b696b7511723 | -11.39811 | -45.15449 | 2024-10-29 04:40:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 72ad4162-a953-3ad4-80e5-c12f12628934 | -11.39555 | -45.14287 | 2024-10-29 04:40:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 28ea5df1-e3de-3ee0-932b-d5b888599038 | -11.33898 | -45.03473 | 2024-10-29 04:40:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 587ed302-ab6d-38af-a943-7cafcd3fb820 | -11.33537 | -45.03023 | 2024-10-29 04:40:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.6 |
| d0e3a6f5-438e-33b9-a92e-9b4284ee20ec | -11.33488 | -45.03383 | 2024-10-29 04:40:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 7388b22e-3aaa-3ddc-8d31-ea75c5b997f2 | -11.33439 | -45.03743 | 2024-10-29 04:40:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 5.3 |
| df670d70-cd8c-309d-91f1-e216b76aa86f | -11.1003 | -45.0858 | 2024-10-29 04:40:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 7ca9ef45-94f3-313e-9a47-68356c188435 | -11.09968 | -45.08448 | 2024-10-29 04:40:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 8da802f6-7bd9-3d29-80a3-aaa7a1ee32c2 | -11.05627 | -45.36602 | 2024-10-29 04:40:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 30753ba4-b8e7-3fb9-9c8e-e3b01c34fe2c | -11.05575 | -45.36966 | 2024-10-29 04:40:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| b8173c44-e92e-3668-8879-93d1d1a2e2b8 | -11.05172 | -45.36911 | 2024-10-29 04:40:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| cc79d023-dda9-3186-9e35-e3afbb8f638f | -10.92612 | -44.76957 | 2024-10-29 04:40:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 5fe4d0e7-3374-36f7-8435-b6f6f89e07a4 | -10.91711 | -45.17601 | 2024-10-29 04:40:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 8a42306d-d711-3084-9a3a-0f255442cf3a | -10.91304 | -45.17536 | 2024-10-29 04:40:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 83f5fc40-b07d-3f5a-b4c5-b5c9f4122f40 | -11.86074 | -44.8101 | 2024-10-29 04:40:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 687dd39d-0588-3343-9743-ef3fc9fe744a | -11.85761 | -44.80151 | 2024-10-29 04:40:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ae6e5c6b-8166-3c47-b14e-ed612f91dda1 | -11.85706 | -44.80552 | 2024-10-29 04:40:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 04ca9982-2a12-38e2-8735-6b8f4c81e239 | -4.61594 | -46.12796 | 2024-10-29 04:40:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 4c57355e-eac2-3a8c-8c42-5b091cb8091f | -4.86227 | -45.76715 | 2024-10-29 04:40:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 68536b21-4e35-31ca-ba6b-ca0ff8078d1b | -5.05276 | -45.52317 | 2024-10-29 04:40:00 | NOAA-21 | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 54b23a6f-7a2b-342c-8db5-bae795208c13 | -5.05211 | -45.52744 | 2024-10-29 04:40:00 | NOAA-21 | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| c2c3dca3-3e0e-3f7c-9ed8-53dbefe902e1 | -5.00211 | -45.4841 | 2024-10-29 04:40:00 | NOAA-21 | LAGOA GRANDE DO MARANHÃO | MARANHÃO | Brasil | 2105963 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 00c876ce-1f76-357a-88a5-58aa75414514 | -4.94356 | -45.42736 | 2024-10-29 04:40:00 | NOAA-21 | LAGOA GRANDE DO MARANHÃO | MARANHÃO | Brasil | 2105963 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 318bcd90-4480-3dda-b125-6424259759fe | -4.94289 | -45.43176 | 2024-10-29 04:40:00 | NOAA-21 | LAGOA GRANDE DO MARANHÃO | MARANHÃO | Brasil | 2105963 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| c595d181-115b-3132-8bb0-cb9fa00eceff | -4.94222 | -45.43623 | 2024-10-29 04:40:00 | NOAA-21 | LAGOA GRANDE DO MARANHÃO | MARANHÃO | Brasil | 2105963 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| bd79a591-c860-330b-97d3-471f182cfed3 | -4.93988 | -45.42672 | 2024-10-29 04:40:00 | NOAA-21 | LAGOA GRANDE DO MARANHÃO | MARANHÃO | Brasil | 2105963 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 307b312f-f997-3c3f-b6ea-74ff954e71a6 | -4.93921 | -45.43112 | 2024-10-29 04:40:00 | NOAA-21 | LAGOA GRANDE DO MARANHÃO | MARANHÃO | Brasil | 2105963 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| dcc032a9-6dca-336f-940d-92e1e9f65f3c | -4.93853 | -45.43564 | 2024-10-29 04:40:00 | NOAA-21 | LAGOA GRANDE DO MARANHÃO | MARANHÃO | Brasil | 2105963 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| c96b02c3-375f-3f93-a5c2-69c9b2d82443 | -4.93619 | -45.42609 | 2024-10-29 04:40:00 | NOAA-21 | LAGOA GRANDE DO MARANHÃO | MARANHÃO | Brasil | 2105963 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 6f044f6b-f4b0-3dc8-b219-b38ae1547cf1 | -4.93552 | -45.43049 | 2024-10-29 04:40:00 | NOAA-21 | LAGOA GRANDE DO MARANHÃO | MARANHÃO | Brasil | 2105963 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| e273dc57-4085-378e-b237-4a9b44e68ac0 | -4.93485 | -45.43496 | 2024-10-29 04:40:00 | NOAA-21 | LAGOA GRANDE DO MARANHÃO | MARANHÃO | Brasil | 2105963 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 8c177aff-94dc-3694-89d0-ab91bfb944b9 | -4.93184 | -45.42988 | 2024-10-29 04:40:00 | NOAA-21 | LAGOA GRANDE DO MARANHÃO | MARANHÃO | Brasil | 2105963 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |


[Clique aqui para ver as próximas entradas](README58.md)
