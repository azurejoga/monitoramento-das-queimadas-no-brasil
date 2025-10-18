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

## Dados Diários - Página 95

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 234889df-2204-3810-8efb-5dd4d54918b0 | -6.2668 | -42.685 | 2025-10-18 14:20:00 | GOES-19 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 62.7 |
| 41725295-f18b-36f8-95d2-11e0b175b730 | -6.3679 | -45.7609 | 2025-10-18 14:20:00 | GOES-19 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 90.9 |
| c6d31bd1-426c-3acc-8511-4f819d661454 | -10.4754 | -43.4106 | 2025-10-18 14:20:00 | GOES-19 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 99.9 |
| d75822d4-d892-33fc-ab89-0dbe6a986736 | -4.6509 | -43.1337 | 2025-10-18 14:20:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 81.3 |
| b56e3bac-9417-3359-b498-3d3a95cdfcf3 | -12.9897 | -47.3892 | 2025-10-18 14:20:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 97.8 |
| 1c549bbd-4bfe-39fa-92f4-99e7c59a1b42 | -12.1485 | -45.08 | 2025-10-18 14:20:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 98.3 |
| 70f50ecf-223a-38d7-bfae-fb39943802b6 | -11.4193 | -44.0731 | 2025-10-18 14:20:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 119.4 |
| de1c62bd-267b-3c64-9e50-62a035e4a1a0 | -11.3576 | -44.316 | 2025-10-18 14:20:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 88.8 |
| d22f5e03-1222-348e-a7e2-3156763de3d3 | -10.236 | -44.0766 | 2025-10-18 14:20:00 | GOES-19 | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 65.7 |
| cf9d7b7b-0b85-3541-a775-1a8bf7f59396 | -13.0488 | -47.3131 | 2025-10-18 14:20:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 88.9 |
| 79f07c7a-e5fb-3216-9faa-1a9bc708f89a | -10.2741 | -44.0715 | 2025-10-18 14:20:00 | GOES-19 | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 79.5 |
| 20ba5164-4726-324c-aa77-740acb9e08f8 | -4.0963 | -42.2021 | 2025-10-18 14:20:00 | GOES-19 | BATALHA | PIAUÍ | Brasil | 2201507 | 22 | 33 | nan | nan | nan | Caatinga | 119.4 |
| 03581110-61aa-378c-9a2f-62eda14f72cb | -10.5331 | -43.3788 | 2025-10-18 14:20:00 | GOES-19 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 93.7 |
| 709e6975-b712-3dd9-9612-b97d0d162a20 | -10.133 | -44.5777 | 2025-10-18 14:20:00 | GOES-19 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 58.8 |
| 6884d8a6-ffc1-3d72-b7c5-8e315d445ea1 | -16.4783 | -43.057 | 2025-10-18 14:20:00 | GOES-19 | GRÃO MOGOL | MINAS GERAIS | Brasil | 3127800 | 31 | 33 | nan | nan | nan | Cerrado | 331.4 |
| af46530e-2559-36a7-82e9-eef16b294fee | -13.0299 | -47.2935 | 2025-10-18 14:20:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 84.4 |
| c5de1433-ee7d-3bd5-b1c8-9d158fa76e01 | -10.255 | -44.074 | 2025-10-18 14:20:00 | GOES-19 | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 72.2 |
| a2879469-6b39-39bb-8f77-57aa31ae0d81 | -10.1136 | -44.6033 | 2025-10-18 14:20:00 | GOES-19 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 67.0 |
| 9041d542-a34e-3749-be96-2b5858ac292d | -4.1525 | -42.1989 | 2025-10-18 14:20:00 | GOES-19 | BATALHA | PIAUÍ | Brasil | 2201507 | 22 | 33 | nan | nan | nan | Caatinga | 94.3 |
| ae9886d4-6318-3d0a-a022-3f5e75688b1c | -11.9709 | -45.3603 | 2025-10-18 14:20:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 83.9 |
| 9256ba7a-d116-3de0-bcf1-bd16835ee813 | -11.5152 | -44.0588 | 2025-10-18 14:20:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 167.3 |
| d5565d5b-9c49-35dc-9952-2030b3585499 | -10.5136 | -43.4052 | 2025-10-18 14:20:00 | GOES-19 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 175.9 |
| b2758c87-ac2a-3f5e-848a-549f9583441a | -12.1678 | -45.0771 | 2025-10-18 14:20:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 226.0 |
| 760b520b-453f-39d0-930a-676982508261 | -10.8101 | -43.9275 | 2025-10-18 14:20:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 129.9 |
| 4fb971ef-736e-3a22-8ae6-6683439b1bd0 | -6.1737 | -42.5985 | 2025-10-18 14:20:00 | GOES-19 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 75.5 |
| db1cc454-1ba0-311b-a2a8-87b8458a5959 | -10.1139 | -44.5801 | 2025-10-18 14:20:00 | GOES-19 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 75.7 |
| 2c95e477-dcca-31a4-9ef7-e9f5cc43f74d | -4.171 | -42.2215 | 2025-10-18 14:20:00 | GOES-19 | BATALHA | PIAUÍ | Brasil | 2201507 | 22 | 33 | nan | nan | nan | Caatinga | 100.8 |
| b08005a3-e7d4-303c-bf5f-7dcc37a6fd42 | -6.22 | -41.7372 | 2025-10-18 14:20:00 | GOES-19 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 75.7 |
| 59fe800a-7cec-33de-acaa-d2b33391fec3 | -11.4389 | -44.0468 | 2025-10-18 14:20:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 123.9 |
| 7b23707f-84b1-3cb1-95d9-c20fafee5d55 | -4.1149 | -42.2248 | 2025-10-18 14:20:00 | GOES-19 | BATALHA | PIAUÍ | Brasil | 2201507 | 22 | 33 | nan | nan | nan | Caatinga | 103.9 |
| 5fb600b9-01d7-32f3-87c7-9dde73e036c0 | -6.4446 | -41.8608 | 2025-10-18 14:20:00 | GOES-19 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 91.9 |
| f23c8ba5-29eb-3892-a2ef-68096da3df75 | -10.1333 | -44.5545 | 2025-10-18 14:20:00 | GOES-19 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 72.1 |
| 11e691f6-3e23-3ad9-9e3c-a835d0c1bd5d | -13.6373 | -43.9208 | 2025-10-18 14:20:00 | GOES-19 | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 62.6 |
| 3a6c4824-43c5-3e42-8744-03c6359ac710 | -10.1143 | -44.557 | 2025-10-18 14:20:00 | GOES-19 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 85.3 |
| 57cc2950-efc9-327d-8738-4defc383e54c | -6.0644 | -42.2522 | 2025-10-18 14:20:00 | GOES-19 | ELESBÃO VELOSO | PIAUÍ | Brasil | 2203503 | 22 | 33 | nan | nan | nan | Caatinga | 60.6 |
| 1c21d641-18f2-3b33-abb2-e14d02c739a6 | -13.0303 | -47.2709 | 2025-10-18 14:20:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 89.8 |
| bd80eb28-e949-3226-aa8c-2aaef55d1168 | -11.3767 | -44.3131 | 2025-10-18 14:20:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 175.8 |
| f56a7d64-1497-3396-8699-3d83ec32e279 | -6.4255 | -41.8865 | 2025-10-18 14:20:00 | GOES-19 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 73.1 |
| f291986e-609c-3c6b-9ac6-e456f87190cb | -13.1807 | -46.4343 | 2025-10-18 14:20:00 | GOES-19 | DIVINÓPOLIS DE GOIÁS | GOIÁS | Brasil | 5208301 | 52 | 33 | nan | nan | nan | Cerrado | 75.2 |
| d40ab77c-d996-34c4-96cc-973f08ded768 | -11.4768 | -44.0645 | 2025-10-18 14:20:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 136.5 |
| 64191df4-a005-3fe3-b303-0772fab0ceb7 | -13.0295 | -47.316 | 2025-10-18 14:20:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 97.4 |
| 4f2304b6-c1d3-32c0-9231-cd6db0fa2a28 | -13.6368 | -43.9446 | 2025-10-18 14:20:00 | GOES-19 | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 128.6 |
| 86dea4bc-4bfb-313d-ac5f-375aa16189d9 | -6.2198 | -41.7612 | 2025-10-18 14:20:00 | GOES-19 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 76.9 |
| a3d97103-4983-315a-a682-2f2da92fd1b8 | -6.3677 | -45.7833 | 2025-10-18 14:20:00 | GOES-19 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 57.4 |
| 60af2476-263c-32ad-ba3d-da85a263937d | -10.4945 | -43.4079 | 2025-10-18 14:20:00 | GOES-19 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 189.9 |
| 5ed4f147-b7e3-331a-8c01-016b05bf70db | -11.4576 | -44.0674 | 2025-10-18 14:20:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 138.7 |
| a27ac328-8ffb-3a7f-8e4a-688e0a03fd46 | -15.7923 | -43.643 | 2025-10-18 14:20:00 | GOES-19 | CAPITÃO ENÉAS | MINAS GERAIS | Brasil | 3112703 | 31 | 33 | nan | nan | nan | Cerrado | 124.3 |
| a6c0551a-c115-3be1-917c-65bf19b8a9b0 | -12.8501 | -44.5973 | 2025-10-18 14:30:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 76.3 |
| 068e7626-c23e-33e5-9f53-d5da7b77787b | -11.3794 | -45.2619 | 2025-10-18 14:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 579.2 |
| ff4ab0a5-b870-3193-b8e2-98654e543141 | -5.7035 | -42.6841 | 2025-10-18 14:30:00 | GOES-19 | MIGUEL LEÃO | PIAUÍ | Brasil | 2206308 | 22 | 33 | nan | nan | nan | Caatinga | 64.1 |
| 757a20c6-5792-30f2-8971-6544632ec30a | -4.4054 | -43.4746 | 2025-10-18 14:30:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 70.2 |
| 49fba8f5-f6cb-3b4e-ae0d-20634ecad238 | -5.7784 | -42.7018 | 2025-10-18 14:30:00 | GOES-19 | AGRICOLÂNDIA | PIAUÍ | Brasil | 2200103 | 22 | 33 | nan | nan | nan | Caatinga | 75.6 |
| 01b04a4c-e7d5-3728-8ed4-c97caa369702 | -11.4184 | -44.1201 | 2025-10-18 14:30:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 124.8 |
| f702346b-ffd3-3f01-be7f-2802aae904f3 | -13.0299 | -47.2935 | 2025-10-18 14:30:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 89.6 |
| cff6124f-2ffe-3f58-a7a0-bb12132a1716 | -5.7782 | -42.7254 | 2025-10-18 14:30:00 | GOES-19 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 64.0 |
| ebb3a289-8f7c-3416-aaed-bff22d87303e | -10.514 | -43.3815 | 2025-10-18 14:30:00 | GOES-19 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 112.9 |
| c60e6287-2b19-371f-a880-5a02e9a661b6 | -6.3679 | -45.7609 | 2025-10-18 14:30:00 | GOES-19 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 72.5 |
| bec60aa7-3fc6-3f89-9ed3-1cc48a2f26aa | -7.0082 | -41.9986 | 2025-10-18 14:30:00 | GOES-19 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 75.8 |
| 513ee46f-6a75-3228-9469-41b0d477a33f | -13.6368 | -43.9446 | 2025-10-18 14:30:00 | GOES-19 | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 138.5 |
| 025e749a-3042-3db3-8924-df439ff345cc | -15.8019 | -43.2548 | 2025-10-18 14:30:00 | GOES-19 | PORTEIRINHA | MINAS GERAIS | Brasil | 3152204 | 31 | 33 | nan | nan | nan | Cerrado | 101.5 |
| 58747b17-73ec-3f93-8fd8-b2dd54e9509a | -7.9817 | -44.1342 | 2025-10-18 14:30:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 97.9 |
| 7eafab68-7a54-3f29-a649-d326d3719e36 | -4.4845 | -42.8631 | 2025-10-18 14:30:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 73.8 |
| ae475611-bbe5-32c6-befe-77440d7d5d94 | -4.8916 | -43.4446 | 2025-10-18 14:30:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 63.1 |
| 07618bd2-f3d9-330c-88fe-0524ddf9994c | -10.2367 | -44.0298 | 2025-10-18 14:30:00 | GOES-19 | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 73.2 |
| b1d20d91-6363-3cca-bb15-a6688b549d19 | -5.7596 | -42.7033 | 2025-10-18 14:30:00 | GOES-19 | AGRICOLÂNDIA | PIAUÍ | Brasil | 2200103 | 22 | 33 | nan | nan | nan | Caatinga | 69.0 |
| d12bb45c-1acd-3cb9-8d9d-0ba3d4eff6b7 | -6.4443 | -41.8848 | 2025-10-18 14:30:00 | GOES-19 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 81.7 |
| 8521e9f5-83c6-343b-978a-20065bc2a6d4 | -6.333 | -45.4934 | 2025-10-18 14:30:00 | GOES-19 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 56.3 |
| 505e40af-6391-3c0c-8d86-2d284595bf72 | -10.4754 | -43.4106 | 2025-10-18 14:30:00 | GOES-19 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 118.3 |
| c8b11baa-377e-3d0e-9178-594559c1958c | -7.1736 | -42.3638 | 2025-10-18 14:30:00 | GOES-19 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 110.1 |
| b22bb28e-bf54-3be3-b574-970ec2fdd1f1 | -12.1678 | -45.0771 | 2025-10-18 14:30:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 165.2 |
| 4d8aeb03-31fe-303a-9e98-9379d50909ee | -6.314 | -45.5174 | 2025-10-18 14:30:00 | GOES-19 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 64.8 |
| 24ef35c7-636e-3f7b-bcfd-987d0a6af814 | -4.115 | -42.2011 | 2025-10-18 14:30:00 | GOES-19 | BATALHA | PIAUÍ | Brasil | 2201507 | 22 | 33 | nan | nan | nan | Caatinga | 99.0 |
| c00d6c1c-8520-3b14-b8a6-50f332b3d6d3 | -6.3328 | -45.516 | 2025-10-18 14:30:00 | GOES-19 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 64.6 |
| 5627c3f1-146f-3a50-bcfe-e77c2e937430 | -10.1136 | -44.6033 | 2025-10-18 14:30:00 | GOES-19 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 69.6 |
| e59f0e28-6fac-350d-9039-20ec4d943771 | -10.2363 | -44.0532 | 2025-10-18 14:30:00 | GOES-19 | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 132.0 |
| 748d222d-b844-3cf4-b032-9b456882c86e | -6.3492 | -45.7623 | 2025-10-18 14:30:00 | GOES-19 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 73.3 |
| d4cbb914-e2b5-30f3-b8f8-21da675eeccc | -10.5136 | -43.4052 | 2025-10-18 14:30:00 | GOES-19 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 245.4 |
| 4aaee380-967e-3e5f-8421-17788b534987 | -6.1737 | -42.5985 | 2025-10-18 14:30:00 | GOES-19 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 77.8 |
| 4a7ff8b7-b03c-3cf3-b92b-01241a91f1d5 | -12.7196 | -50.8622 | 2025-10-18 14:30:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 90.6 |
| 5d354f95-8e66-3e37-adbb-474139778224 | -11.4376 | -44.1172 | 2025-10-18 14:30:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 111.6 |
| eacf50e4-0d83-3cba-a730-5fe779963c73 | -4.8729 | -43.4458 | 2025-10-18 14:30:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 65.2 |
| e957cb19-5da9-3a74-a803-cb747bd79ffa | -5.9518 | -42.2379 | 2025-10-18 14:30:00 | GOES-19 | SÃO FÉLIX DO PIAUÍ | PIAUÍ | Brasil | 2209609 | 22 | 33 | nan | nan | nan | Caatinga | 71.9 |
| 1930a239-acf1-3fe8-9905-9287f3015fff | -10.5335 | -43.3552 | 2025-10-18 14:30:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 95.5 |
| 71bf7f9d-b846-3fa6-b1ad-3f4b1c3bf596 | -5.9103 | -42.644 | 2025-10-18 14:30:00 | GOES-19 | ÁGUA BRANCA | PIAUÍ | Brasil | 2200202 | 22 | 33 | nan | nan | nan | Caatinga | 74.3 |
| 06c64407-3996-35df-b42c-94759be4c4ce | -10.5331 | -43.3788 | 2025-10-18 14:30:00 | GOES-19 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 108.8 |
| 4b6866e7-e57e-37e3-b7e8-02ac53211f35 | -4.171 | -42.2215 | 2025-10-18 14:30:00 | GOES-19 | BATALHA | PIAUÍ | Brasil | 2201507 | 22 | 33 | nan | nan | nan | Caatinga | 105.1 |
| 9ba68488-30c0-30ac-a5f1-7423ab2d4f35 | -6.0301 | -41.9214 | 2025-10-18 14:30:00 | GOES-19 | SANTA CRUZ DOS MILAGRES | PIAUÍ | Brasil | 2209153 | 22 | 33 | nan | nan | nan | Caatinga | 87.3 |
| 7da7028f-1c0f-3b0c-ab43-9ecbad8990ef | -4.5033 | -42.862 | 2025-10-18 14:30:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 75.9 |
| 4d0fdbde-17e5-34a0-9084-964e1c32555c | -4.1523 | -42.2226 | 2025-10-18 14:30:00 | GOES-19 | BATALHA | PIAUÍ | Brasil | 2201507 | 22 | 33 | nan | nan | nan | Caatinga | 86.6 |
| 5a6075a2-e209-30c8-b256-4c8fc8c45164 | -8.2182 | -43.3403 | 2025-10-18 14:30:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 69.5 |
| 4ce63555-2cb6-3489-9926-e83932b46417 | -4.1149 | -42.2248 | 2025-10-18 14:30:00 | GOES-19 | BATALHA | PIAUÍ | Brasil | 2201507 | 22 | 33 | nan | nan | nan | Caatinga | 106.0 |
| 2c42e20c-099f-3294-9834-22ddd2150791 | -11.8544 | -45.4464 | 2025-10-18 14:30:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 230.4 |
| 8aebe11c-7c36-376f-abf0-99b367e061f1 | -13.6363 | -43.9684 | 2025-10-18 14:30:00 | GOES-19 | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 80.2 |
| 7456a84b-1bbf-35cc-94ec-6456bc013a16 | -5.839 | -42.2472 | 2025-10-18 14:30:00 | GOES-19 | SÃO MIGUEL DA BAIXA GRANDE | PIAUÍ | Brasil | 2210383 | 22 | 33 | nan | nan | nan | Caatinga | 72.1 |
| 5e438b3d-ec8a-3631-a48f-e250dceee007 | -6.4446 | -41.8608 | 2025-10-18 14:30:00 | GOES-19 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 100.5 |
| 308c67cc-b318-3830-970d-b162c5b7721d | -11.3992 | -44.1229 | 2025-10-18 14:30:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 132.8 |
| 2073bcba-62b1-38a8-a863-1205564e4b57 | -4.1525 | -42.1989 | 2025-10-18 14:30:00 | GOES-19 | BATALHA | PIAUÍ | Brasil | 2201507 | 22 | 33 | nan | nan | nan | Caatinga | 94.2 |
| b15df29b-6a4c-3351-9ad0-f7920462d3d9 | -4.4633 | -43.2152 | 2025-10-18 14:40:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 68.5 |
| b060f8b8-e41b-3b2d-9fff-5d4b039ad490 | -8.2095 | -44.0176 | 2025-10-18 14:40:00 | GOES-19 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 99.2 |
| fee162c5-b1d7-3b6e-85be-a4706fb9f205 | -12.1678 | -45.0771 | 2025-10-18 14:40:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 132.1 |


[Clique aqui para ver as próximas entradas](README96.md)
