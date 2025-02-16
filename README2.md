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

## Dados Diários - Página 2

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| ac1db282-b3b6-34ed-b01b-c35b4ececc53 | -9.87631 | -41.80425 | 2025-02-16 04:01:00 | NPP-375D | SENTO SÉ | BAHIA | Brasil | 2930204 | 29 | 33 | nan | nan | nan | Caatinga | 3.3 |
| b947f25d-a60a-320e-97ea-7e6b52c49258 | -5.25698 | -45.24445 | 2025-02-16 04:01:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f897527c-23ef-35ad-87ba-8debee5548b9 | -10.73837 | -37.60326 | 2025-02-16 04:01:00 | NPP-375D | SÃO DOMINGOS | SERGIPE | Brasil | 2806800 | 28 | 33 | nan | nan | nan | Caatinga | 1.7 |
| bf965510-1077-3b90-9734-f2dd89a99d96 | -10.73287 | -37.61501 | 2025-02-16 04:01:00 | NPP-375D | SÃO DOMINGOS | SERGIPE | Brasil | 2806800 | 28 | 33 | nan | nan | nan | Caatinga | 3.1 |
| 6fa8227b-34b3-36fc-8980-e39545de1cef | -4.81275 | -43.00806 | 2025-02-16 04:01:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 65af33f4-53bb-37bb-94e1-cbd2aef94166 | -12.4378 | -38.15835 | 2025-02-16 04:01:00 | NPP-375D | MATA DE SÃO JOÃO | BAHIA | Brasil | 2921005 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| dc8f0c24-0c02-38b8-ba4f-f180177ad714 | -7.23491 | -44.71881 | 2025-02-16 04:01:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 43aab524-17f3-388c-bd5f-3047ba1de6c3 | -10.67307 | -44.49868 | 2025-02-16 04:01:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 3fefb1d0-1935-3364-806a-5a367d555bb0 | -6.7479 | -38.74617 | 2025-02-16 04:01:00 | NPP-375D | BAIXIO | CEARÁ | Brasil | 2301802 | 23 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 6bed1d76-8f49-3272-891d-b46dff5c642c | -5.03939 | -39.03084 | 2025-02-16 04:01:00 | NPP-375D | QUIXADÁ | CEARÁ | Brasil | 2311306 | 23 | 33 | nan | nan | nan | Caatinga | 0.5 |
| b4738996-fc82-31fd-a298-245259570376 | -6.74452 | -38.74566 | 2025-02-16 04:01:00 | NPP-375D | BAIXIO | CEARÁ | Brasil | 2301802 | 23 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 302c0ec0-b746-3808-81ac-079df3828c9c | -10.73409 | -37.6068 | 2025-02-16 04:01:00 | NPP-375D | SÃO DOMINGOS | SERGIPE | Brasil | 2806800 | 28 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 59b24165-2e8e-3f6f-8718-9e8eda896567 | -10.73348 | -37.61089 | 2025-02-16 04:01:00 | NPP-375D | SÃO DOMINGOS | SERGIPE | Brasil | 2806800 | 28 | 33 | nan | nan | nan | Caatinga | 2.6 |
| e2c191aa-d08f-3168-9473-f6c44d94dde0 | -10.47379 | -42.46 | 2025-02-16 04:01:00 | NPP-375D | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 2.6 |
| a959ad36-11be-3277-9ad4-482b5c2c8477 | -10.47718 | -42.46054 | 2025-02-16 04:01:00 | NPP-375D | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 12e28f7a-c436-3a6a-a089-be632e62df47 | -7.72565 | -39.93381 | 2025-02-16 04:01:00 | NPP-375D | BODOCÓ | PERNAMBUCO | Brasil | 2602001 | 26 | 33 | nan | nan | nan | Caatinga | 0.6 |
| ce3d1e0e-4978-3953-a089-7c1776715c33 | -10.32924 | -41.80105 | 2025-02-16 04:01:00 | NPP-375D | SENTO SÉ | BAHIA | Brasil | 2930204 | 29 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 4b3294bf-a031-3d1e-914d-8f447a621c3c | -9.87687 | -41.80068 | 2025-02-16 04:01:00 | NPP-375D | SENTO SÉ | BAHIA | Brasil | 2930204 | 29 | 33 | nan | nan | nan | Caatinga | 1.9 |
| da2871bb-635e-3db7-8d91-4da3b446bb38 | -6.33132 | -37.89464 | 2025-02-16 04:01:00 | NPP-375D | ALEXANDRIA | RIO GRANDE DO NORTE | Brasil | 2400505 | 24 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 657afd00-df08-3fc6-a5fc-a597d8f50129 | -5.36433 | -46.26201 | 2025-02-16 04:01:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 83858414-88e5-3d93-a62b-cdd1b178f6a4 | -10.47659 | -42.46421 | 2025-02-16 04:01:00 | NPP-375D | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 4.5 |
| 317122da-0f92-356b-9808-65e2e9adcc9f | -4.96129 | -43.88266 | 2025-02-16 04:01:00 | NPP-375D | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| fd5eea55-ad30-3b2d-a176-33bb0d8a7e03 | -5.63462 | -39.76773 | 2025-02-16 04:01:00 | NPP-375D | MOMBAÇA | CEARÁ | Brasil | 2308500 | 23 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 60a11e76-72d1-3944-aab5-10dd8767651c | -5.63408 | -39.77119 | 2025-02-16 04:01:00 | NPP-375D | MOMBAÇA | CEARÁ | Brasil | 2308500 | 23 | 33 | nan | nan | nan | Caatinga | 1.3 |
| b6de0959-9f37-3eb3-b326-c2ae37939fb1 | -4.95669 | -43.88671 | 2025-02-16 04:01:00 | NPP-375D | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| d6c7ba72-90d9-3118-b55b-1c6f4bf318de | -4.69226 | -44.38192 | 2025-02-16 04:01:00 | NPP-375D | CAPINZAL DO NORTE | MARANHÃO | Brasil | 2102754 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| bfb46ad1-80da-327b-87ad-7d26d5092ce0 | -5.67762 | -45.23663 | 2025-02-16 04:01:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 89bdf0a3-8abe-3ab0-8996-f348ed213d3f | -8.14145 | -43.14182 | 2025-02-16 04:01:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 0c2b0663-a97e-36de-b6ee-adc70c82546a | -8.40509 | -37.03364 | 2025-02-16 04:01:00 | NPP-375D | ARCOVERDE | PERNAMBUCO | Brasil | 2601201 | 26 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 378f080d-85f4-3928-a134-7bc6bc5893fa | -4.8091 | -43.00744 | 2025-02-16 04:01:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| d457ba76-527b-30eb-8f50-d39ed65b4469 | -10.4732 | -42.46366 | 2025-02-16 04:01:00 | NPP-375D | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 4.5 |
| 64272fff-d2ce-3640-aab0-55e28796d6c8 | -7.08653 | -44.37481 | 2025-02-16 04:01:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| b030f6c4-9259-37d0-bb0b-28d9ae38bed5 | -5.70747 | -38.41407 | 2025-02-16 04:01:00 | NPP-375D | IRACEMA | CEARÁ | Brasil | 2306009 | 23 | 33 | nan | nan | nan | Caatinga | 1.0 |
| fef637ac-83d1-3d40-9657-56f153c4b587 | -7.08834 | -44.37736 | 2025-02-16 04:01:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 0.4 |
| e189546b-e490-38ac-95b6-144f18fc5f2b | -18.12191 | -39.69209 | 2025-02-16 04:04:00 | NPP-375D | MUCURI | BAHIA | Brasil | 2922003 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| be5eecaf-4bde-3f28-bc88-e10d1186ca1b | -18.51872 | -39.93349 | 2025-02-16 04:04:00 | NPP-375D | CONCEIÇÃO DA BARRA | ESPÍRITO SANTO | Brasil | 3201605 | 32 | 33 | nan | nan | nan | Mata Atlântica | 4.0 |
| 80abe13d-4eed-331b-beb9-8c8667c53b2a | -16.86736 | -40.6132 | 2025-02-16 04:04:00 | NPP-375D | SANTA HELENA DE MINAS | MINAS GERAIS | Brasil | 3157658 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 26d19a0a-1941-35a4-bce2-6dd049c8937e | -16.81135 | -42.51693 | 2025-02-16 04:04:00 | NPP-375D | BERILO | MINAS GERAIS | Brasil | 3106507 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 7f150fb7-102f-30bd-b675-687e2408e477 | -18.52289 | -39.92982 | 2025-02-16 04:04:00 | NPP-375D | CONCEIÇÃO DA BARRA | ESPÍRITO SANTO | Brasil | 3201605 | 32 | 33 | nan | nan | nan | Mata Atlântica | 4.0 |
| fe84848e-316f-3a16-ad75-36b539c08933 | -15.82916 | -42.62482 | 2025-02-16 04:04:00 | NPP-375D | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Mata Atlântica | 10.2 |
| 73119b13-2c73-3054-98b9-06c5fde1bdf6 | -19.8135 | -40.28162 | 2025-02-16 04:04:00 | NPP-375D | ARACRUZ | ESPÍRITO SANTO | Brasil | 3200607 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 2f14cada-daca-3369-a1ee-da0526a841d3 | -14.11884 | -41.67832 | 2025-02-16 04:04:00 | NPP-375D | BRUMADO | BAHIA | Brasil | 2904605 | 29 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 55dbb324-1d30-35f9-adbd-e9c751866a26 | -18.74477 | -40.4451 | 2025-02-16 04:04:00 | NPP-375D | NOVA VENÉCIA | ESPÍRITO SANTO | Brasil | 3203908 | 32 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| bbcdbd62-db11-3faf-be96-4f6c72246c52 | -19.83779 | -40.08382 | 2025-02-16 04:04:00 | NPP-375D | ARACRUZ | ESPÍRITO SANTO | Brasil | 3200607 | 32 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| c3b2916f-0472-3ba8-baf5-96b6a447d98c | -17.12203 | -39.56224 | 2025-02-16 04:04:00 | NPP-375D | ITAMARAJU | BAHIA | Brasil | 2915601 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| 3a3e02c3-e9f0-3aa7-9c1b-fc976def9823 | -14.22598 | -41.59698 | 2025-02-16 04:04:00 | NPP-375D | BRUMADO | BAHIA | Brasil | 2904605 | 29 | 33 | nan | nan | nan | Caatinga | 3.2 |
| 0de10b7c-1c53-3cd6-afff-91a6624769c6 | -17.50039 | -45.17909 | 2025-02-16 04:04:00 | NPP-375D | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 8f6efc8d-53da-391b-b96f-dbc6995f7af8 | -17.30712 | -39.25328 | 2025-02-16 04:04:00 | NPP-375D | PRADO | BAHIA | Brasil | 2925501 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 0bca8fa1-7c57-37a7-8d4a-a02acadbb718 | -18.5223 | -39.93406 | 2025-02-16 04:04:00 | NPP-375D | CONCEIÇÃO DA BARRA | ESPÍRITO SANTO | Brasil | 3201605 | 32 | 33 | nan | nan | nan | Mata Atlântica | 4.0 |
| 9075a28d-e281-3934-abdd-0d9ed0ac130f | -19.71803 | -40.35057 | 2025-02-16 04:04:00 | NPP-375D | JOÃO NEIVA | ESPÍRITO SANTO | Brasil | 3203130 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| b6288763-5daf-37d5-9b35-f78858b0cfc0 | -12.03885 | -43.83434 | 2025-02-16 04:04:00 | NPP-375D | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 9595d80f-5dde-3060-8689-740ef1f792dd | -12.86093 | -38.36811 | 2025-02-16 04:04:00 | NPP-375D | SALVADOR | BAHIA | Brasil | 2927408 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 7ef9f808-ff8e-3ecc-869f-72e4bb4ac84b | -16.79862 | -42.51107 | 2025-02-16 04:04:00 | NPP-375D | BERILO | MINAS GERAIS | Brasil | 3106507 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| d6a7fa6b-a3ac-30e7-b7cd-3a383236ec3e | -15.68261 | -42.44159 | 2025-02-16 04:04:00 | NPP-375D | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| c6e25e93-92f2-359d-830f-1e28043ef045 | -16.81078 | -42.52053 | 2025-02-16 04:04:00 | NPP-375D | BERILO | MINAS GERAIS | Brasil | 3106507 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 9ac33654-895c-3c0e-bcc1-8677a2c927d2 | -19.7443 | -40.11533 | 2025-02-16 04:04:00 | NPP-375D | ARACRUZ | ESPÍRITO SANTO | Brasil | 3200607 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 87eda281-76fe-3283-98db-ca271f1beb15 | -15.82584 | -42.62426 | 2025-02-16 04:04:00 | NPP-375D | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 61202139-7a6e-3f68-80fc-837bb2ed482e | -17.67426 | -42.7437 | 2025-02-16 04:04:00 | NPP-375D | ITAMARANDIBA | MINAS GERAIS | Brasil | 3132503 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 6f93cc2c-ea65-3803-9e94-811670d27244 | -15.36655 | -43.16785 | 2025-02-16 04:04:00 | NPP-375D | PAI PEDRO | MINAS GERAIS | Brasil | 3146552 | 31 | 33 | nan | nan | nan | Caatinga | 0.9 |
| bd714c3e-45ff-35d5-b88f-4c59d23d977d | -16.8047 | -42.5158 | 2025-02-16 04:04:00 | NPP-375D | BERILO | MINAS GERAIS | Brasil | 3106507 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| ddd34079-6dca-3c17-90be-e1c1d9883ba2 | -14.47616 | -45.81904 | 2025-02-16 04:04:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 2ff7be01-c08f-304d-9b28-adeaf73a4fae | -16.81302 | -42.52043 | 2025-02-16 04:04:00 | NPP-375D | BERILO | MINAS GERAIS | Brasil | 3106507 | 31 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 0860e616-ed2b-36a1-ace8-67a5fd0400a8 | -17.11559 | -39.50495 | 2025-02-16 04:04:00 | NPP-375D | ITAMARAJU | BAHIA | Brasil | 2915601 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 450d2e09-3756-376c-9c73-53bc7630b194 | -15.82641 | -42.62066 | 2025-02-16 04:04:00 | NPP-375D | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| d9e082a5-78aa-383c-8a7b-a851f43b87d6 | -16.80802 | -42.51637 | 2025-02-16 04:04:00 | NPP-375D | BERILO | MINAS GERAIS | Brasil | 3106507 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| b894374a-7898-3426-aa1f-b8fca73ec9a8 | -17.09447 | -43.80392 | 2025-02-16 04:04:00 | NPP-375D | BOCAIÚVA | MINAS GERAIS | Brasil | 3107307 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 6f7cd5cc-216a-3da4-b4f5-91283c7e51ab | -17.67758 | -42.74427 | 2025-02-16 04:04:00 | NPP-375D | ITAMARANDIBA | MINAS GERAIS | Brasil | 3132503 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 5381ec2b-bafb-32ee-b345-64c26d82854b | -15.68318 | -42.43801 | 2025-02-16 04:04:00 | NPP-375D | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 02b0d719-4bc1-362c-ac85-21f819460d18 | -17.11918 | -39.50551 | 2025-02-16 04:04:00 | NPP-375D | ITAMARAJU | BAHIA | Brasil | 2915601 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| b7e91eb2-9276-3a61-adc5-ea83c73ddfab | -16.80195 | -42.51163 | 2025-02-16 04:04:00 | NPP-375D | BERILO | MINAS GERAIS | Brasil | 3106507 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 42a9c4e2-3e08-35da-9029-632f81d38e50 | -18.51932 | -39.92926 | 2025-02-16 04:04:00 | NPP-375D | CONCEIÇÃO DA BARRA | ESPÍRITO SANTO | Brasil | 3201605 | 32 | 33 | nan | nan | nan | Mata Atlântica | 4.0 |
| 8eb4a0e9-4e9b-379f-9a4c-4c0924928211 | -17.75202 | -42.89438 | 2025-02-16 04:04:00 | NPP-375D | ITAMARANDIBA | MINAS GERAIS | Brasil | 3132503 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 888a6f3a-874d-3770-ab30-0ceb846e77ba | -17.73695 | -39.52501 | 2025-02-16 04:04:00 | NPP-375D | CARAVELAS | BAHIA | Brasil | 2906907 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| dc33473a-a1d4-3819-929c-60dd81ab21d7 | -16.35044 | -43.6951 | 2025-02-16 04:04:00 | NPP-375D | CAPITÃO ENÉAS | MINAS GERAIS | Brasil | 3112703 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| b975d9c5-0e7f-3e08-8737-82e772dd41cd | -22.95329 | -43.32793 | 2025-02-16 04:06:00 | NPP-375D | RIO DE JANEIRO | RIO DE JANEIRO | Brasil | 3304557 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| a9f4cb16-972e-3941-b1c7-d7ea32f2d534 | -20.32977 | -55.01194 | 2025-02-16 04:06:00 | NPP-375D | TERENOS | MATO GROSSO DO SUL | Brasil | 5008008 | 50 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 556ae58d-c4eb-30df-b9f4-ba6e221afa39 | -23.34002 | -46.77142 | 2025-02-16 04:06:00 | NPP-375D | CAIEIRAS | SÃO PAULO | Brasil | 3509007 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 519ec904-f588-38e1-a5cb-564f5a0b3aa8 | -22.85695 | -42.97961 | 2025-02-16 04:06:00 | NPP-375D | SÃO GONÇALO | RIO DE JANEIRO | Brasil | 3304904 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 0dece486-0af9-30a9-9fe0-35915ad1c28b | -21.43447 | -43.71561 | 2025-02-16 04:06:00 | NPP-375D | ANTÔNIO CARLOS | MINAS GERAIS | Brasil | 3102902 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 6eb10efc-0661-3a80-b45d-7ee30823aa5c | -21.03564 | -48.28551 | 2025-02-16 04:06:00 | NPP-375D | PITANGUEIRAS | SÃO PAULO | Brasil | 3539509 | 35 | 33 | nan | nan | nan | Cerrado | 3.4 |
| df5c4b5e-8c41-3ace-94f5-280b929691a1 | -20.41562 | -43.55169 | 2025-02-16 04:06:00 | NPP-375D | OURO PRETO | MINAS GERAIS | Brasil | 3146107 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.1 |
| a33976e1-4c6e-3912-83ec-2999454d84a9 | -20.91959 | -56.54102 | 2025-02-16 04:06:00 | NPP-375D | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | 4.3 |
| e20b4614-9023-3101-935f-07f9bfc9ea8d | -20.41894 | -43.55228 | 2025-02-16 04:06:00 | NPP-375D | OURO PRETO | MINAS GERAIS | Brasil | 3146107 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| 08a14a46-b091-336e-a80f-d5eedc561112 | -20.33081 | -55.0074 | 2025-02-16 04:06:00 | NPP-375D | TERENOS | MATO GROSSO DO SUL | Brasil | 5008008 | 50 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 2db14ec2-5e74-3af2-9e7e-667f941ed79d | -20.91954 | -56.54205 | 2025-02-16 04:06:00 | NPP-375D | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 5b149c5f-9a8c-33ca-862c-dadf14bb5da3 | -20.8977 | -44.21225 | 2025-02-16 04:06:00 | NPP-375D | RESENDE COSTA | MINAS GERAIS | Brasil | 3154200 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 9258f421-7244-32bf-88f0-776cf8189492 | -21.19428 | -44.93838 | 2025-02-16 04:06:00 | NPP-375D | IJACI | MINAS GERAIS | Brasil | 3130408 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 0b4fcc3e-d4e2-3f9e-a840-172152d36ee5 | -23.9835 | -48.91645 | 2025-02-16 04:06:00 | NPP-375D | ITAPEVA | SÃO PAULO | Brasil | 3522406 | 35 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 26d2d3d2-5153-3ced-bc27-b4b9ff68de38 | -20.92078 | -56.53692 | 2025-02-16 04:06:00 | NPP-375D | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 5aa74953-9711-3d55-ac2a-9325ec670084 | -22.58647 | -43.64259 | 2025-02-16 04:06:00 | NPP-375D | PARACAMBI | RIO DE JANEIRO | Brasil | 3303609 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 76c79e6c-1140-3e0f-a0bf-799655d71633 | -22.6767 | -42.85568 | 2025-02-16 04:06:00 | NPP-375D | ITABORAÍ | RIO DE JANEIRO | Brasil | 3301900 | 33 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| 59175711-c6f2-3144-9730-8f6a6366eb6b | -20.8971 | -44.21597 | 2025-02-16 04:06:00 | NPP-375D | RESENDE COSTA | MINAS GERAIS | Brasil | 3154200 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 0f2d7f34-7358-32d4-aa51-75ce20d00004 | -23.4067 | -46.55777 | 2025-02-16 04:06:00 | NPP-375D | SÃO PAULO | SÃO PAULO | Brasil | 3550308 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 110f2312-05f4-34f3-8550-0b1b1bc2fee8 | -20.7643 | -46.76995 | 2025-02-16 04:06:00 | NPP-375D | ITAÚ DE MINAS | MINAS GERAIS | Brasil | 3133758 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 525214ad-e615-3eaa-8a99-9c121260e1e0 | -20.35853 | -40.89109 | 2025-02-16 04:06:00 | NPP-375D | DOMINGOS MARTINS | ESPÍRITO SANTO | Brasil | 3201902 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| ebf5f868-ca07-334c-95f8-ae1c8fe1a96e | -21.62647 | -43.4673 | 2025-02-16 04:06:00 | NPP-375D | JUIZ DE FORA | MINAS GERAIS | Brasil | 3136702 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 3ad3bfb7-3647-393a-a203-00eb00bed0a1 | -20.89437 | -44.21163 | 2025-02-16 04:06:00 | NPP-375D | RESENDE COSTA | MINAS GERAIS | Brasil | 3154200 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 7f4f7df3-bcf4-3c89-987f-3c66ba3ee835 | -21.91219 | -42.26136 | 2025-02-16 04:06:00 | NPP-375D | CANTAGALO | RIO DE JANEIRO | Brasil | 3301108 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 355c80ec-76f3-313b-9f85-4b0c86491cef | -22.58885 | -43.64231 | 2025-02-16 04:06:00 | NPP-375D | PARACAMBI | RIO DE JANEIRO | Brasil | 3303609 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 251eb4f4-3058-3b5a-bb85-93f37390dc49 | -21.03674 | -48.28351 | 2025-02-16 04:06:00 | NPP-375D | PITANGUEIRAS | SÃO PAULO | Brasil | 3539509 | 35 | 33 | nan | nan | nan | Cerrado | 3.1 |


[Clique aqui para ver as próximas entradas](README3.md)
