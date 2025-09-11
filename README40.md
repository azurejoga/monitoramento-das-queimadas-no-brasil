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

## Dados Diários - Página 40

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 897316d7-2805-3eb5-960e-7a4d49b7d70a | -6.85262 | -47.87616 | 2025-09-11 04:21:00 | NPP-375D | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 3be49749-31b5-36b8-8e95-d5ae16ab8a7b | -6.28849 | -42.20607 | 2025-09-11 04:21:00 | NPP-375D | ELESBÃO VELOSO | PIAUÍ | Brasil | 2203503 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| f893b4ac-9eed-3e28-aa34-cc90f90e59f4 | -6.16811 | -53.50176 | 2025-09-11 04:21:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 6ecf2300-993c-3c46-8af7-c23b99f1dceb | -7.77791 | -50.99278 | 2025-09-11 04:21:00 | NPP-375D | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 7f19a85c-6a8d-3bbd-a1f2-521dde8b71c7 | -7.26093 | -44.60962 | 2025-09-11 04:21:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 7e2a2a83-ee9d-34c6-8232-2fee07b3d04b | -9.03859 | -45.73312 | 2025-09-11 04:21:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 8870168b-e48f-3a22-9c3f-d496ab17e263 | -7.37484 | -47.42202 | 2025-09-11 04:21:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| ea8df165-6d26-3329-95bc-72c2fccb7bdd | -5.68405 | -43.34969 | 2025-09-11 04:21:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| ed2c6b06-2158-3406-a669-438680c9772e | -8.74949 | -47.11416 | 2025-09-11 04:21:00 | NPP-375D | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 64c17b4b-fa06-3df2-a26f-86e5ddba83d1 | -8.04064 | -49.05462 | 2025-09-11 04:21:00 | NPP-375D | BERNARDO SAYÃO | TOCANTINS | Brasil | 1703206 | 17 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 8e9221b7-007c-3c8f-b72a-08541bd0034b | -7.20106 | -44.96734 | 2025-09-11 04:21:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 49acf48e-49d6-3027-aaa6-550baeab4b3f | -8.93635 | -46.11458 | 2025-09-11 04:21:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 57e1deb7-debe-3b71-8d21-8a17884d8f44 | -8.20179 | -50.10675 | 2025-09-11 04:21:00 | NPP-375D | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| bd82752f-e5ea-35a6-935f-3ee73864c755 | -5.66203 | -43.8975 | 2025-09-11 04:21:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 17fa899d-0e55-3fc4-a059-c4b3e7b6d643 | -5.67282 | -43.33335 | 2025-09-11 04:21:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| af607d62-ae34-3372-a630-9c118a771269 | -5.69462 | -45.32117 | 2025-09-11 04:21:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b4903709-9292-3b54-ba7a-cb2e5994e051 | -5.74117 | -45.29986 | 2025-09-11 04:21:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| a2830d10-d671-3864-9fcc-72f03553c9c0 | -3.7369 | -49.04311 | 2025-09-11 04:21:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| c01295bf-d8c7-3e7f-8fb7-b387c20540f8 | -6.47483 | -41.74954 | 2025-09-11 04:21:00 | NPP-375D | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 31a60860-5148-3cf5-8cfe-2330d39088da | -5.51948 | -42.68361 | 2025-09-11 04:21:00 | NPP-375D | LAGOA DO PIAUÍ | PIAUÍ | Brasil | 2205581 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 063da0b1-718a-3273-a6e5-b6ad7dbc4ffd | -5.99354 | -43.31618 | 2025-09-11 04:21:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Caatinga | 3.9 |
| 1b7d63bc-3f54-367a-b714-b34efd627138 | -8.08317 | -50.19324 | 2025-09-11 04:21:00 | NPP-375D | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 50525147-f2b2-35b7-8dc9-59758318a4f2 | -6.56293 | -44.21305 | 2025-09-11 04:21:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 9f483e39-ad3a-3494-ad87-c95b65855b34 | -4.72927 | -44.45107 | 2025-09-11 04:21:00 | NPP-375D | SANTO ANTÔNIO DOS LOPES | MARANHÃO | Brasil | 2110302 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| bf0e841d-d8dd-36d1-bb9d-3d961174b477 | -8.04277 | -48.15345 | 2025-09-11 04:21:00 | NPP-375D | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| b587e07a-e23e-33b4-b2ef-333dda13fe82 | -5.95675 | -45.83461 | 2025-09-11 04:21:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 5c578717-d03f-3941-b41b-a9de67da0548 | -7.39438 | -47.36861 | 2025-09-11 04:21:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 7b2d087f-e8a2-395e-992a-cabcf12311d7 | -6.85763 | -47.86831 | 2025-09-11 04:21:00 | NPP-375D | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 4ac5220c-0d5d-30b4-89bf-19d0de51d37a | -8.02556 | -48.66016 | 2025-09-11 04:21:00 | NPP-375D | BANDEIRANTES DO TOCANTINS | TOCANTINS | Brasil | 1703057 | 17 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 1e376356-b6f9-33d1-8695-1215b734fc92 | -8.19655 | -50.11301 | 2025-09-11 04:21:00 | NPP-375D | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| f8e3e865-f59d-32e2-97d9-07a8fb4deef8 | -8.0367 | -48.66203 | 2025-09-11 04:21:00 | NPP-375D | BANDEIRANTES DO TOCANTINS | TOCANTINS | Brasil | 1703057 | 17 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 15fcf946-6658-32a2-b6c7-f2ad0bb53ac0 | -6.40646 | -42.61334 | 2025-09-11 04:21:00 | NPP-375D | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| d837101c-5136-3d84-802c-479232aa633c | -4.7279 | -43.53337 | 2025-09-11 04:21:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 887d9063-5ac0-30c6-9d65-bf71ee9f4288 | -6.27023 | -42.40335 | 2025-09-11 04:21:00 | NPP-375D | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 51d90a4d-f552-3a84-8467-1ca150b082f1 | -6.44134 | -43.65047 | 2025-09-11 04:21:00 | NPP-375D | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 85d82a7d-6525-3490-81a3-b3da564676ac | -6.35881 | -43.05713 | 2025-09-11 04:21:00 | NPP-375D | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 3bbf2693-436f-31b4-857a-9c831fdd0128 | -5.65536 | -43.89646 | 2025-09-11 04:21:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 3a5bd524-91c7-32ea-9f57-660631e93c0d | -4.57988 | -45.61448 | 2025-09-11 04:21:00 | NPP-375D | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 548ad91f-6e29-3bc0-82b5-f5a12e971313 | -8.55606 | -45.55453 | 2025-09-11 04:21:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 0cb7ed54-cfd6-37a7-88c0-4d454255bae8 | -5.86122 | -44.20299 | 2025-09-11 04:21:00 | NPP-375D | JATOBÁ | MARANHÃO | Brasil | 2105450 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| dfe8d11a-3890-3ef6-b638-7a0f4908b4fa | -7.86662 | -46.05183 | 2025-09-11 04:21:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| bce06163-bc1e-3e7a-ab3c-776a7037cf2b | -5.39174 | -42.63036 | 2025-09-11 04:21:00 | NPP-375D | LAGOA DO PIAUÍ | PIAUÍ | Brasil | 2205581 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 0b93e398-2822-3ab7-9a1f-566a3c1d72ef | -6.56109 | -43.14721 | 2025-09-11 04:21:00 | NPP-375D | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 52cd760f-c9ad-32c0-a7b7-8f047e3f9458 | -6.1881 | -41.06091 | 2025-09-11 04:21:00 | NPP-375D | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 9ded2c2f-1ef9-3160-841c-01cca3104358 | -6.40301 | -42.6128 | 2025-09-11 04:21:00 | NPP-375D | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 50a0ac9b-beab-384f-992f-159ef4ff361a | -5.65482 | -43.89994 | 2025-09-11 04:21:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 5ccb7753-a94c-376a-ae14-b2a32bb1599e | -5.55795 | -42.91011 | 2025-09-11 04:21:00 | NPP-375D | CURRALINHOS | PIAUÍ | Brasil | 2203255 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 89df2350-c329-326e-9c77-bbfbb6bc7b38 | -5.84544 | -45.39181 | 2025-09-11 04:21:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| c9791470-8605-3a16-95df-e2e74c6b5198 | -6.17374 | -41.08104 | 2025-09-11 04:21:00 | NPP-375D | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| cc9c3512-fde9-3ccc-859f-1d3d8b1dfb58 | -6.31349 | -43.8224 | 2025-09-11 04:21:00 | NPP-375D | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 21d6f78a-402d-3ab5-a8d8-e251f065b264 | -3.40178 | -42.99729 | 2025-09-11 04:21:00 | NPP-375D | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 6a6188ef-4a15-3a35-9ecd-e8614e3e3d4e | -7.2625 | -44.90221 | 2025-09-11 04:21:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 18af1b8b-a3cc-3032-b426-d9b41494315d | -3.32074 | -48.70983 | 2025-09-11 04:21:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 3f475ab6-0fce-35e0-8b9d-dfe84a3009de | -6.41495 | -44.48928 | 2025-09-11 04:21:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 11cea382-057b-3ce2-bd97-a0b3ddad899a | -8.42585 | -49.08857 | 2025-09-11 04:21:00 | NPP-375D | COUTO MAGALHÃES | TOCANTINS | Brasil | 1706001 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 3a9146e6-9653-3f64-af3f-30c6625c04ba | -6.5469 | -43.104 | 2025-09-11 04:21:00 | NPP-375D | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 6eaadac5-4f72-37a6-bcef-6ac5503b4fef | -7.62479 | -47.68054 | 2025-09-11 04:21:00 | NPP-375D | FILADÉLFIA | TOCANTINS | Brasil | 1707702 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 3af8c11d-9a8d-31db-9f1c-c2cd085ec8ec | -6.53857 | -44.779 | 2025-09-11 04:21:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 0429ed0b-b4f2-3e7e-a289-5334065b32b0 | -6.81532 | -44.88454 | 2025-09-11 04:21:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 90654454-6271-3fe5-970c-f223960f6e17 | -7.80885 | -46.07922 | 2025-09-11 04:21:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 88b5544e-6183-3c46-829d-a85974abf1c7 | -7.32702 | -44.38432 | 2025-09-11 04:21:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 572e5971-3d27-3fea-82c7-9a3c6855d785 | -6.66945 | -44.09362 | 2025-09-11 04:21:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 25687899-a974-366f-88b6-0ce142ceedd0 | -8.03748 | -48.65735 | 2025-09-11 04:21:00 | NPP-375D | BANDEIRANTES DO TOCANTINS | TOCANTINS | Brasil | 1703057 | 17 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 54eae456-7bfa-31aa-8736-642812783578 | -7.04745 | -44.7001 | 2025-09-11 04:21:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 41d3b2b1-8055-3297-b291-ccadc38ce22b | -5.43096 | -45.88175 | 2025-09-11 04:21:00 | NPP-375D | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 8bb43ec8-2666-36b9-9ec5-ee31c5df4077 | -8.7329 | -47.10762 | 2025-09-11 04:21:00 | NPP-375D | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 9df50dd5-c2da-39f6-a1fc-60bd52e99689 | -5.19769 | -45.72311 | 2025-09-11 04:21:00 | NPP-375D | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 6fceb8c5-1cf3-322a-ae0a-f7e5714e7df5 | -6.32334 | -43.4176 | 2025-09-11 04:21:00 | NPP-375D | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 91ae2795-30af-3f40-9042-66c6af744890 | -8.20583 | -50.10747 | 2025-09-11 04:21:00 | NPP-375D | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 28b7d5cd-d9e3-3287-a874-d3a3de6d6f06 | -5.43318 | -43.41588 | 2025-09-11 04:21:00 | NPP-375D | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| eeecd458-b1c7-3a47-a3ca-1f204b4130b4 | -3.35036 | -39.27844 | 2025-09-11 04:21:00 | NPP-375D | TRAIRI | CEARÁ | Brasil | 2313500 | 23 | 33 | nan | nan | nan | Caatinga | 5.2 |
| fbb8ec96-9bb0-33da-991d-f751a2239e10 | -6.35541 | -43.05659 | 2025-09-11 04:21:00 | NPP-375D | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| adf7b964-7bdf-32d3-9eee-9d57826f8a85 | -7.23204 | -44.47254 | 2025-09-11 04:21:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| fc5bced4-68b2-3d59-ae70-312b09d5f223 | -8.74483 | -47.12112 | 2025-09-11 04:21:00 | NPP-375D | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 584079d5-d9cd-34d2-89e9-7959626da1d3 | -8.42196 | -47.27153 | 2025-09-11 04:21:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| b96482a4-658a-3570-8e12-4d3f5e381ec6 | -6.25566 | -44.85467 | 2025-09-11 04:21:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| f282a513-1446-358f-abf5-a142b7ecee30 | -7.14695 | -46.04722 | 2025-09-11 04:21:00 | NPP-375D | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f31c2b37-2bb7-303f-aa82-7548ac67b82b | -6.83933 | -45.60812 | 2025-09-11 04:21:00 | NPP-375D | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| a2b037cf-9356-3603-9659-6b25464537b6 | -5.91014 | -45.75047 | 2025-09-11 04:21:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 75790004-ef13-3e62-ae8b-0d08fb2d7afa | -4.58499 | -45.60424 | 2025-09-11 04:21:00 | NPP-375D | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 502f327d-501c-3850-ae89-704f79f9addf | -6.12281 | -43.91885 | 2025-09-11 04:21:00 | NPP-375D | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 4609ca78-3eb7-3d7d-90ad-8c65536f781f | -6.56789 | -43.14824 | 2025-09-11 04:21:00 | NPP-375D | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| dce19e19-bd8b-34c3-b30b-f216d5f64bb5 | -6.41054 | -44.4957 | 2025-09-11 04:21:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 6ffab222-2ec2-3257-a6c2-a18bdc788b2d | -6.74857 | -46.35453 | 2025-09-11 04:21:00 | NPP-375D | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 32649a04-a980-312c-b8f0-d7d6f2a680f1 | -6.6712 | -44.12616 | 2025-09-11 04:21:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 95c66598-2089-39ae-a145-a1145f09e80a | -5.38849 | -43.43788 | 2025-09-11 04:21:00 | NPP-375D | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 36d45f43-e5ad-33f5-ae73-11a1411477fb | -8.31838 | -44.89816 | 2025-09-11 04:21:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e89fdfc0-e0e6-332a-868f-fa955e6ece15 | -6.30177 | -44.58455 | 2025-09-11 04:21:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 026abc39-10d8-397c-8b55-ffdd3a7b4ea0 | -8.16805 | -46.08215 | 2025-09-11 04:21:00 | NPP-375D | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 6f3e517c-063a-37ee-a0e4-bec2a9287b00 | -7.082 | -44.13758 | 2025-09-11 04:21:00 | NPP-375D | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 1e1a98e7-e5c2-3d1f-aa84-6dbfd1497e6b | -5.57949 | -42.9284 | 2025-09-11 04:21:00 | NPP-375D | CURRALINHOS | PIAUÍ | Brasil | 2203255 | 22 | 33 | nan | nan | nan | Caatinga | 4.5 |
| 0e6ac8e5-c067-3c40-a736-bc13ab29ca10 | -5.65706 | -43.90743 | 2025-09-11 04:21:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f50e9fa1-2128-3c7b-8be1-01537db8cb3c | -6.70208 | -43.54159 | 2025-09-11 04:21:00 | NPP-375D | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 372f75df-67a0-302f-8885-eba0a370f8c8 | -6.69792 | -44.94326 | 2025-09-11 04:21:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 917693cd-98a3-346c-b64f-54bd4484105d | -8.01865 | -49.04607 | 2025-09-11 04:21:00 | NPP-375D | BERNARDO SAYÃO | TOCANTINS | Brasil | 1703206 | 17 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 87972cf4-fc32-3bda-95c8-b4cda0d92a0a | -6.41974 | -44.39391 | 2025-09-11 04:21:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a163a98c-e58f-3a2e-a323-8eb642de1441 | -6.24641 | -43.424 | 2025-09-11 04:21:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 75748f1a-d545-3635-82bb-4a3719cad90e | -7.9213 | -44.84247 | 2025-09-11 04:21:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 3f521008-3c73-33c4-9115-a6b81e8c70fe | -6.1757 | -41.0679 | 2025-09-11 04:21:00 | NPP-375D | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 599be77b-1b95-38d0-a913-3fd1b5b27756 | -5.81583 | -45.68483 | 2025-09-11 04:21:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |


[Clique aqui para ver as próximas entradas](README41.md)
