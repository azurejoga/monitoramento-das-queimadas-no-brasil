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

## Dados Diários - Página 44

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 63e085c9-f24f-3a24-b9bc-dd3bc94fa0e2 | -9.165 | -44.6273 | 2025-09-19 14:20:00 | GOES-19 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 102.9 |
| 18cc1ae7-f33b-3c79-9806-1d0265e147d0 | -4.676 | -37.6366 | 2025-09-19 14:30:00 | GOES-19 | ARACATI | CEARÁ | Brasil | 2301109 | 23 | 33 | nan | nan | nan | Caatinga | 294.9 |
| 0f7eef7d-02a5-30e7-89ed-0f0be4b0e2ac | -8.9911 | -46.3059 | 2025-09-19 14:30:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 142.7 |
| 4c26794b-2914-330f-9f1f-58d140571b36 | -26.8573 | -50.7066 | 2025-09-19 14:30:00 | GOES-19 | LEBON RÉGIS | SANTA CATARINA | Brasil | 4209706 | 42 | 33 | nan | nan | nan | Mata Atlântica | 130.3 |
| 2da536eb-c1a8-35f5-b77c-d45fffae7528 | -7.1886 | -44.3503 | 2025-09-19 14:30:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 72.1 |
| f0d5f2bf-6a92-3842-8a29-08bdfb50f2fc | -9.0857 | -44.8893 | 2025-09-19 14:30:00 | GOES-19 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 135.0 |
| bdd338fc-7fd9-34c0-98b7-3ced0dafa475 | -8.9722 | -46.3079 | 2025-09-19 14:30:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 116.7 |
| 4f84a88f-8664-3cdf-bf9d-1a1b4ed2e5a4 | -6.6321 | -45.5374 | 2025-09-19 14:30:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 102.1 |
| 7a2e5c2b-6315-339b-ba82-6b733fd82c5a | -8.3709 | -44.6697 | 2025-09-19 14:30:00 | GOES-19 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 91.7 |
| 9e6594ad-a248-3e73-9825-f92ca5633a09 | -3.4366 | -43.1532 | 2025-09-19 14:30:00 | GOES-19 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 82.5 |
| ec852f2c-0981-3445-905a-a600327b9e9e | -9.0469 | -44.9625 | 2025-09-19 14:30:00 | GOES-19 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 134.0 |
| c372e00b-f6d2-30c6-ad87-4df9951afe67 | -6.1688 | -41.2357 | 2025-09-19 14:30:00 | GOES-19 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 100.7 |
| 54b9118c-f365-3e0d-a4f9-ff37c3ceb306 | -19.5861 | -57.8181 | 2025-09-19 14:30:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 65.5 |
| 540e9c89-0c1f-35af-a5a9-aa10be76bbce | -7.5598 | -44.7743 | 2025-09-19 14:30:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 74.2 |
| dfade21c-83c1-3799-96a9-44a103f6955f | -9.0668 | -44.8914 | 2025-09-19 14:30:00 | GOES-19 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 134.6 |
| fd09bc08-0b55-3226-a0df-719b4f4964fa | -7.8509 | -45.6105 | 2025-09-19 14:30:00 | GOES-19 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 87.6 |
| 9ad48ce9-4af4-3761-9112-9373354f6878 | -8.6076 | -45.3302 | 2025-09-19 14:30:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 112.7 |
| 4970d208-561d-3b9f-be6b-4914532807f9 | -7.6949 | -44.486 | 2025-09-19 14:30:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 295.3 |
| acff6802-0141-39be-9273-0c7d2f6006ad | -9.0671 | -44.8685 | 2025-09-19 14:30:00 | GOES-19 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 124.3 |
| f9c4bb46-e362-3e53-b751-0e9279b80f05 | -6.9022 | -44.7885 | 2025-09-19 14:30:00 | GOES-19 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 72.6 |
| b0c85aad-ff9a-3cb0-91ce-7a0a29fdc7fb | -8.5944 | -46.3695 | 2025-09-19 14:30:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 94.2 |
| ea0bc277-7ff7-3a50-9ce5-e61b44a07be3 | -19.5672 | -57.7584 | 2025-09-19 14:30:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 87.4 |
| db39b6f3-522e-3aaf-bc85-099daefcaefe | -7.3479 | -38.9606 | 2025-09-19 14:30:00 | GOES-19 | MILAGRES | CEARÁ | Brasil | 2308302 | 23 | 33 | nan | nan | nan | Caatinga | 120.8 |
| 1ad07e85-5735-3e7c-9bcb-bb01146cf004 | -6.169 | -41.2114 | 2025-09-19 14:30:00 | GOES-19 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 205.7 |
| a22e34e2-fa9f-3511-9bb6-03cec5a77787 | -9.0478 | -44.8936 | 2025-09-19 14:30:00 | GOES-19 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 132.0 |
| fcb0fc24-516b-3e55-a7d4-162afd33116a | -7.3366 | -44.5663 | 2025-09-19 14:30:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 68.7 |
| ba366dfe-aa7d-3b08-a0b3-0fd2ea737d34 | -9.1615 | -44.8806 | 2025-09-19 14:30:00 | GOES-19 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 113.3 |
| 4ea3edcb-b993-3472-9570-e061f3299f92 | -6.1438 | -47.8342 | 2025-09-19 14:30:00 | GOES-19 | CACHOEIRINHA | TOCANTINS | Brasil | 1703826 | 17 | 33 | nan | nan | nan | Cerrado | 72.1 |
| 01c3a5ed-9bfd-34db-bcf8-dbfdeb57b5aa | -9.028 | -44.9646 | 2025-09-19 14:30:00 | GOES-19 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 124.4 |
| 1d3719eb-e289-3169-9e45-c1b019c08ff4 | -7.6574 | -44.4667 | 2025-09-19 14:30:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 77.8 |
| 23c24cac-da32-3f16-8950-cda7dd177b2b | -7.7148 | -44.392 | 2025-09-19 14:30:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 147.9 |
| 63fc1c89-e31d-39b6-8aba-8011b18d558b | -6.1878 | -41.2097 | 2025-09-19 14:30:00 | GOES-19 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 748.2 |
| 748d433e-36a8-3141-b5f5-3ed03ae45e4d | -9.1937 | -45.2886 | 2025-09-19 14:30:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 227.3 |
| e4e3fca2-2c0b-34de-aadc-bdd2dfdcaa35 | -9.0289 | -44.8958 | 2025-09-19 14:30:00 | GOES-19 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 111.4 |
| 495c30de-7ed1-3765-a9dc-d5e15eee8f4f | -4.6948 | -37.6351 | 2025-09-19 14:30:00 | GOES-19 | ARACATI | CEARÁ | Brasil | 2301109 | 23 | 33 | nan | nan | nan | Caatinga | 117.3 |
| 89275135-0f04-3eec-be6b-1677ba2bc16e | -8.9892 | -45.0376 | 2025-09-19 14:30:00 | GOES-19 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 144.1 |
| 880c4349-f744-3ada-9e1c-a68033a74458 | -9.1744 | -45.3135 | 2025-09-19 14:30:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 153.7 |
| 704ac382-a5f7-3724-82de-977570907b98 | -7.4503 | -46.1647 | 2025-09-19 14:30:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 72.8 |
| b7629067-bdd8-33aa-8447-7a0cbf60e191 | -7.6685 | -45.129 | 2025-09-19 14:30:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 75.2 |
| 48050fcd-f0e5-3355-bae9-b069befdaab3 | -7.4531 | -42.644 | 2025-09-19 14:30:00 | GOES-19 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 127.3 |
| b5190cd8-e3c4-35dc-bf32-09481b716803 | -9.0472 | -44.9395 | 2025-09-19 14:30:00 | GOES-19 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 108.5 |
| 7e9266f9-f5fb-36c7-8d45-d5e9fb9072aa | -4.6951 | -37.6092 | 2025-09-19 14:30:00 | GOES-19 | ARACATI | CEARÁ | Brasil | 2301109 | 23 | 33 | nan | nan | nan | Caatinga | 106.5 |
| 951b56dc-d404-3b94-8beb-a53468469bde | -8.6265 | -45.3282 | 2025-09-19 14:30:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 132.6 |
| 049ffbb0-6314-3f01-9862-2554b39b02d2 | -7.5705 | -45.4786 | 2025-09-19 14:30:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 74.9 |
| d05c4f85-09cd-3dd7-94cb-32accf813359 | -19.5872 | -57.7557 | 2025-09-19 14:30:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 72.4 |
| 6d91a7e1-dbbf-3f52-9c8b-95a50b0f4f29 | -8.3898 | -44.6677 | 2025-09-19 14:30:00 | GOES-19 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 89.0 |
| bd06060c-70cf-382d-8f69-c8dd9dec9e96 | -8.828 | -43.0113 | 2025-09-19 14:30:00 | GOES-19 | SÃO BRAZ DO PIAUÍ | PIAUÍ | Brasil | 2209559 | 22 | 33 | nan | nan | nan | Caatinga | 152.1 |
| 6d5b9d60-aa45-3ca7-8b04-26415ca62a50 | -6.9212 | -44.764 | 2025-09-19 14:30:00 | GOES-19 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 107.0 |
| 0acd6c69-89aa-39ef-a82f-db540d30015e | -7.5601 | -44.7514 | 2025-09-19 14:30:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 101.4 |
| 2a642b67-bb1d-31e1-91b1-178936d983c3 | -6.1881 | -41.1855 | 2025-09-19 14:30:00 | GOES-19 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 179.0 |
| 472f0dcb-d22b-3ce9-bdba-fea471d7c6ed | -6.1048 | -48.0327 | 2025-09-19 14:30:00 | GOES-19 | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 64.5 |
| fd59ca08-7276-3c0d-9360-1879db2a2715 | -8.019 | -45.7072 | 2025-09-19 14:30:00 | GOES-19 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 64.3 |
| c2296650-679c-3ad5-8510-b8fc2aae529d | -8.8277 | -43.0349 | 2025-09-19 14:30:00 | GOES-19 | SÃO BRAZ DO PIAUÍ | PIAUÍ | Brasil | 2209559 | 22 | 33 | nan | nan | nan | Caatinga | 128.6 |
| 3dfcd64d-cfc9-3f95-ab77-cbfd36427018 | -6.6508 | -45.5359 | 2025-09-19 14:30:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 91.7 |
| 4e3b136c-6b6c-3bcb-a6d7-45a702106eea | -8.6699 | -46.3618 | 2025-09-19 14:30:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 87.6 |
| 5b3c07e4-bfc4-30a9-b1e6-404f66323036 | -9.1236 | -44.8849 | 2025-09-19 14:30:00 | GOES-19 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 131.9 |
| f177e2a3-ba2d-3e54-8733-55ab566e5fcb | -19.5676 | -57.7376 | 2025-09-19 14:30:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 68.0 |
| ace2849a-8bb7-3ac7-8895-c3751ae3b1f9 | -7.5789 | -44.7496 | 2025-09-19 14:30:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 70.4 |
| b876e43c-4e24-3cb0-b0dd-aba36ba5d327 | -9.1747 | -45.2907 | 2025-09-19 14:30:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 149.4 |
| 7004feae-480d-3ed7-aa45-f128d290f088 | -6.921 | -44.7869 | 2025-09-19 14:30:00 | GOES-19 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 70.6 |
| 15e4e42c-4ef1-3c1b-96e2-430134302c7b | -8.9892 | -45.0376 | 2025-09-19 14:40:00 | GOES-19 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 199.7 |
| fe7cc78a-9180-37b3-bdfa-971ea2924c6f | -8.5947 | -46.3471 | 2025-09-19 14:40:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 93.0 |
| 0af01793-ae58-3fe3-b94e-2b8c1c3587d8 | -8.0281 | -44.957 | 2025-09-19 14:40:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 123.4 |
| 751607d8-7027-3666-b5c4-69f886e4909e | -8.3334 | -44.6507 | 2025-09-19 14:40:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 103.7 |
| 967b1a10-d442-381e-ae91-3cf1c668efa8 | -7.5601 | -44.7514 | 2025-09-19 14:40:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 101.4 |
| 7523c742-3075-3ba0-9b49-d593951252c5 | -6.1438 | -47.8342 | 2025-09-19 14:40:00 | GOES-19 | CACHOEIRINHA | TOCANTINS | Brasil | 1703826 | 17 | 33 | nan | nan | nan | Cerrado | 84.2 |
| a2f5e7da-485f-312b-b048-6361e4b7b5d4 | -19.5869 | -57.7765 | 2025-09-19 14:40:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 71.7 |
| 9ede3f81-5a52-3785-90b6-fdcef07ee7c3 | -4.5819 | -47.709 | 2025-09-19 14:40:00 | GOES-19 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 82.8 |
| af0cfcfe-731f-301f-b7aa-a1493e386709 | -8.9911 | -46.3059 | 2025-09-19 14:40:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 131.0 |
| 5669ebe6-30b9-3094-a260-bd2d4304fa70 | -6.9976 | -44.6429 | 2025-09-19 14:40:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 80.6 |
| dddfdd5b-39b6-34d5-ac01-f4e361774c2b | -19.5676 | -57.7376 | 2025-09-19 14:40:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 76.0 |
| 4978675d-4120-3129-8743-5fa958cfc551 | -6.1881 | -41.1855 | 2025-09-19 14:40:00 | GOES-19 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 208.6 |
| 9fda1169-e504-345c-8ad6-5c5eb852c9b5 | -6.9024 | -44.7656 | 2025-09-19 14:40:00 | GOES-19 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 91.4 |
| 73aadb00-cf4d-3aa3-a72f-3f947ef288c8 | -8.828 | -43.0113 | 2025-09-19 14:40:00 | GOES-19 | SÃO BRAZ DO PIAUÍ | PIAUÍ | Brasil | 2209559 | 22 | 33 | nan | nan | nan | Caatinga | 266.5 |
| 05ff6f1a-7c21-39ce-9da4-139d79122f20 | -8.8277 | -43.0349 | 2025-09-19 14:40:00 | GOES-19 | SÃO BRAZ DO PIAUÍ | PIAUÍ | Brasil | 2209559 | 22 | 33 | nan | nan | nan | Caatinga | 284.5 |
| af696710-8892-31e9-96fe-f8f8a95e1e40 | -7.8509 | -45.6105 | 2025-09-19 14:40:00 | GOES-19 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 75.9 |
| ff0d585a-ccc2-32b2-9b78-f0c0859fead5 | -8.019 | -45.7072 | 2025-09-19 14:40:00 | GOES-19 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 75.8 |
| d129ccf5-518e-3b70-a4ec-ab81c35769ee | -6.9212 | -44.764 | 2025-09-19 14:40:00 | GOES-19 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 98.5 |
| c2acd8a1-33ee-3a52-a7cc-c9850c4a2751 | -7.2923 | -45.1639 | 2025-09-19 14:40:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 77.1 |
| dbaf096b-3ca3-3a53-acf6-68a1d93892d5 | -19.5861 | -57.8181 | 2025-09-19 14:40:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 62.2 |
| c34a6ba3-e6a6-325a-a30a-6430e8f2458d | -6.1436 | -47.856 | 2025-09-19 14:40:00 | GOES-19 | CACHOEIRINHA | TOCANTINS | Brasil | 1703826 | 17 | 33 | nan | nan | nan | Cerrado | 74.5 |
| ed600f96-d592-3c2e-95b9-b8511917ac28 | -19.5672 | -57.7584 | 2025-09-19 14:40:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 102.1 |
| 7ea79c91-8ea4-3b06-b4a4-3f9e624593c1 | -6.6696 | -45.5344 | 2025-09-19 14:40:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 92.3 |
| 657270bb-3552-3cf5-89ec-a655ea89bb71 | -3.4366 | -43.1532 | 2025-09-19 14:40:00 | GOES-19 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 88.0 |
| 9169b092-e233-3968-ac90-f481536df388 | -7.5598 | -44.7743 | 2025-09-19 14:40:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 80.5 |
| dcccb577-8201-316c-ac6d-4eb8e7c8a88e | -9.175 | -45.2679 | 2025-09-19 14:40:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 107.5 |
| 0108763a-71e3-3a33-9a58-7c4af21d680e | -8.0188 | -45.7298 | 2025-09-19 14:40:00 | GOES-19 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 61.8 |
| bdc8321f-f19b-331a-a32c-4fa38f35fbd8 | -19.5872 | -57.7557 | 2025-09-19 14:40:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 77.3 |
| 3a7b2342-b137-32be-9672-e41fdfedc458 | -7.676 | -44.4879 | 2025-09-19 14:40:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 90.4 |
| 39d5ae44-587b-3eb7-a1f6-82710a7b91c9 | -7.3235 | -44.0608 | 2025-09-19 14:40:00 | GOES-19 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 82.0 |
| 34a5904f-9e45-3c09-813f-ce680e6b2b85 | -7.6949 | -44.486 | 2025-09-19 14:40:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 177.5 |
| 2fcc9ecd-dab9-3811-85a2-6bfdd6428652 | -9.0469 | -44.9625 | 2025-09-19 14:40:00 | GOES-19 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 110.5 |
| 33321df3-8044-39cf-89da-e5910a8e48e5 | -6.6319 | -45.56 | 2025-09-19 14:40:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 82.6 |
| 8d4fdaec-597e-389b-b164-cad760faa85e | -7.6574 | -44.4667 | 2025-09-19 14:40:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 86.7 |
| 065639f7-e903-3f70-8250-d07ed13adba4 | -8.6265 | -45.3282 | 2025-09-19 14:40:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 113.4 |


