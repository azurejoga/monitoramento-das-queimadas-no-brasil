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

## Dados Diários - Página 39

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| b61ff634-4939-3968-adaf-8ab60bcb4c97 | -13.75403 | -47.92048 | 2025-09-30 03:49:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 3d41c519-c443-304a-9f03-b2b5b4e29559 | -12.86891 | -46.90922 | 2025-09-30 03:49:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 8a48856a-e1eb-3063-9087-d1d076bdd537 | -11.97726 | -46.57998 | 2025-09-30 03:49:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 62d10875-fcc5-3c42-a6cf-b039dc92a5be | -11.88349 | -48.04744 | 2025-09-30 03:49:00 | NOAA-20 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 5e8f8dc7-a264-36d0-9a8e-19c18db968c8 | -13.60501 | -48.03149 | 2025-09-30 03:49:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 44d9c5ca-510b-32ac-a6de-0e07edacf823 | -13.00977 | -49.4503 | 2025-09-30 03:49:00 | NOAA-20 | ARAGUAÇU | TOCANTINS | Brasil | 1702000 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| de1f1a96-3486-35b6-bccf-ce06dde768a0 | -12.84114 | -46.99717 | 2025-09-30 03:49:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f4cef72c-5861-34f9-bf52-de7cdfd1461c | -12.852 | -46.99611 | 2025-09-30 03:49:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 8c011496-2bbb-3578-8f7a-17994217d3cb | -15.27641 | -47.85405 | 2025-09-30 03:49:00 | NOAA-20 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 33254291-e450-385b-9ede-68e297357842 | -15.32916 | -46.26691 | 2025-09-30 03:49:00 | NOAA-20 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 3bdd279e-2ba6-379a-93c4-b9c9adcb8efc | -12.74805 | -46.84977 | 2025-09-30 03:49:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d6723100-e265-3e73-a17c-5203215b93ce | -12.74877 | -46.87398 | 2025-09-30 03:49:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 7bafc5d3-41b5-3235-bc3f-f2baa784ffa0 | -14.52843 | -48.49425 | 2025-09-30 03:49:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 4c56f6f8-8638-3131-b70c-8b2196bc2b58 | -6.2508 | -43.65992 | 2025-09-30 03:49:00 | NOAA-20 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 35dd1b1b-65a2-3963-a7ba-a0583bee4c54 | -11.06079 | -47.83132 | 2025-09-30 03:49:00 | NOAA-20 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 000b6489-8c71-35b0-9c21-de74eacefea6 | -14.53607 | -48.2621 | 2025-09-30 03:49:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 4.5 |
| c9bbb5f7-b6d5-34dc-850d-94ea758966ee | -13.22135 | -47.32587 | 2025-09-30 03:49:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 52d07ace-7ac7-35cb-a095-cbd8219395c8 | -6.89328 | -44.5253 | 2025-09-30 03:49:00 | NOAA-20 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 4d3e7a5d-fa81-3ab8-ac8c-2f7418030a20 | -18.11821 | -42.19942 | 2025-09-30 03:49:00 | NOAA-20 | ÁGUA BOA | MINAS GERAIS | Brasil | 3100609 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| ea4f9a1d-b84e-35c7-ae0b-03e8de5676c5 | -11.71074 | -44.43763 | 2025-09-30 03:49:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 98fb7cb4-79d3-359c-bb64-0d10b9cd8bd9 | -13.57085 | -48.09098 | 2025-09-30 03:49:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| df7846f7-e3ae-3788-839a-f5d8e6d70a2b | -11.88227 | -48.04225 | 2025-09-30 03:49:00 | NOAA-20 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| d044de58-58b9-3a54-873f-e5917e77c15f | -14.56617 | -48.22458 | 2025-09-30 03:49:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 4c288da2-a960-34e9-9207-f662941ce045 | -13.09429 | -47.03001 | 2025-09-30 03:49:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a6504a53-5f88-37a5-8122-5151c087ef10 | -6.33043 | -43.35443 | 2025-09-30 03:49:00 | NOAA-20 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| da0575e0-c810-3e78-86ff-240372bde73c | -15.71956 | -47.58814 | 2025-09-30 03:49:00 | NOAA-20 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 4.7 |
| fbfa377a-42aa-3404-8044-e57a7fe1ed63 | -13.22952 | -50.9418 | 2025-09-30 03:49:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ebee887e-edb4-339e-8980-e5ca52cc5a6c | -15.27346 | -49.49674 | 2025-09-30 03:49:00 | NOAA-20 | SANTA ISABEL | GOIÁS | Brasil | 5219357 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 37a28fb4-6956-3cae-88d8-dc34008a5db8 | -13.79543 | -47.88022 | 2025-09-30 03:49:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 3b8dddd0-8bc2-300f-b52d-9200189d9f74 | -15.46378 | -47.92183 | 2025-09-30 03:49:00 | NOAA-20 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 21c42992-1059-3494-8050-c75354773daf | -5.83488 | -43.94092 | 2025-09-30 03:49:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 9375ac32-4f63-3d62-bb23-5507b68089ec | -14.56477 | -48.23146 | 2025-09-30 03:49:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| a45de0af-7116-34e2-9516-3fe86c3d7261 | -13.80058 | -47.88227 | 2025-09-30 03:49:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 2bbb9514-8952-3d1b-9425-7d9839db1180 | -14.5344 | -48.38091 | 2025-09-30 03:49:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| d3ead3df-746d-3124-b726-df0e9c7867b9 | -7.2797 | -42.86045 | 2025-09-30 03:49:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| e5d37d5a-837a-30da-b2eb-57fd2b675218 | -6.74743 | -43.3674 | 2025-09-30 03:49:00 | NOAA-20 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Caatinga | 1.8 |
| abd126fa-f469-321a-b130-adf05fceda0d | -12.95476 | -46.40604 | 2025-09-30 03:49:00 | NOAA-20 | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| d22ff3a2-8125-3b8d-95fd-3e0b62549dd6 | -18.12173 | -42.20012 | 2025-09-30 03:49:00 | NOAA-20 | ÁGUA BOA | MINAS GERAIS | Brasil | 3100609 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| b4d6aa4b-b420-3440-b014-68cf3fa732db | -13.85872 | -44.41647 | 2025-09-30 03:49:00 | NOAA-20 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 5869e954-a793-39ee-8780-dc9b974dc0e6 | -6.05223 | -42.47584 | 2025-09-30 03:49:00 | NOAA-20 | HUGO NAPOLEÃO | PIAUÍ | Brasil | 2204600 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| f1c2e5d3-533a-366f-98b6-cc5f7e2f672a | -18.613 | -43.36773 | 2025-09-30 03:49:00 | NOAA-20 | SERRO | MINAS GERAIS | Brasil | 3167103 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| e22b1880-1a69-34f4-881f-33b9801ca1e9 | -5.81704 | -42.78314 | 2025-09-30 03:49:00 | NOAA-20 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| 79a0e07e-bf2a-337f-b724-71d28d0cb619 | -5.76895 | -43.83549 | 2025-09-30 03:49:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 139b6ac4-189b-33dc-b2d2-5ea7ed110a33 | -14.56116 | -48.47327 | 2025-09-30 03:49:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 6.5 |
| eb7d9bc4-2178-38d2-a572-d0986345b8e0 | -14.5478 | -48.25969 | 2025-09-30 03:49:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 2ed981a1-d35e-3950-bb75-0c723cf3becf | -15.48957 | -48.56861 | 2025-09-30 03:49:00 | NOAA-20 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 68af371a-f371-3f49-9f4c-4c9ae7197140 | -11.87922 | -48.05764 | 2025-09-30 03:49:00 | NOAA-20 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 4766290d-6b7b-33e6-9b99-74613b47c3b4 | -13.37458 | -43.73038 | 2025-09-30 03:49:00 | NOAA-20 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| c4baacc3-4f0f-35cc-97fc-e38cfd9d9709 | -6.37059 | -45.63162 | 2025-09-30 03:49:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| ce74af5e-d71e-3b3a-a4d2-395f2ef52082 | -15.54765 | -44.3504 | 2025-09-30 03:49:00 | NOAA-20 | PEDRAS DE MARIA DA CRUZ | MINAS GERAIS | Brasil | 3149150 | 31 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 36ebcfdd-b8e1-3ace-8c17-c20dcccdfac4 | -18.77275 | -39.76938 | 2025-09-30 03:49:00 | NOAA-20 | SÃO MATEUS | ESPÍRITO SANTO | Brasil | 3204906 | 32 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| a39dc329-37f1-3d16-b2db-81b342815139 | -6.31058 | -43.47292 | 2025-09-30 03:49:00 | NOAA-20 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 77b8a047-0550-386a-aa9f-8945c23456fb | -12.96345 | -46.42083 | 2025-09-30 03:49:00 | NOAA-20 | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 22faf0b7-47ad-3663-b125-62de98cd4ab6 | -12.83009 | -46.99915 | 2025-09-30 03:49:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 9b541406-3db6-35ad-9f53-dc4d40a3bc60 | -6.4122 | -43.75982 | 2025-09-30 03:49:00 | NOAA-20 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 4f0d17b5-8167-3d6a-b2fb-eb051ec08af6 | -14.70469 | -48.15834 | 2025-09-30 03:49:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 64bf9af8-1895-3263-8f6f-6ffbd4cb8bbb | -14.70814 | -45.70219 | 2025-09-30 03:49:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 6b85c21c-79af-3575-bab9-dcc20b7eb1fa | -7.18317 | -41.69691 | 2025-09-30 03:49:00 | NOAA-20 | PAQUETÁ | PIAUÍ | Brasil | 2207553 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 9fabb22a-8899-30b1-8294-60a1a6fc67f6 | -14.38929 | -47.14733 | 2025-09-30 03:49:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 72b878f4-bd0c-32a9-9ee1-939fb1643d08 | -19.12355 | -44.76143 | 2025-09-30 03:49:00 | NOAA-20 | POMPÉU | MINAS GERAIS | Brasil | 3152006 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 2249f5e9-5e04-3127-b531-b8792e97925c | -12.85436 | -46.984 | 2025-09-30 03:49:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| afb83141-cd24-3e85-a843-aa81a585862f | -6.33878 | -43.7515 | 2025-09-30 03:49:00 | NOAA-20 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 5d6ee54d-dd69-394b-8666-c75fec67d456 | -17.72052 | -46.67069 | 2025-09-30 03:49:00 | NOAA-20 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 28027f48-b7d3-377c-a4db-00af78357644 | -13.39209 | -48.07151 | 2025-09-30 03:49:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 1c99d7fc-38f4-3e93-ab30-1f3653391227 | -11.10557 | -49.77848 | 2025-09-30 03:49:00 | NOAA-20 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 6caf8f19-308a-30b2-aadb-bbbaf5b72f45 | -13.66627 | -44.30865 | 2025-09-30 03:49:00 | NOAA-20 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 19.7 |
| d9a4a4c1-4231-3c29-b3a2-b185f79c1773 | -12.43455 | -44.11761 | 2025-09-30 03:49:00 | NOAA-20 | TABOCAS DO BREJO VELHO | BAHIA | Brasil | 2930907 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c624baa1-3813-3004-9cbe-8855ce432162 | -13.37074 | -44.3516 | 2025-09-30 03:49:00 | NOAA-20 | SANTA MARIA DA VITÓRIA | BAHIA | Brasil | 2928109 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 4b9b45d8-2bda-3c22-8749-4dbeaf1639a9 | -6.88465 | -44.51789 | 2025-09-30 03:49:00 | NOAA-20 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 5f0bfb92-147c-32c7-9ece-93d4f5497356 | -14.54076 | -48.26666 | 2025-09-30 03:49:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 60f8d712-17cb-3dc6-8485-1fbfadff2e11 | -12.86957 | -46.90583 | 2025-09-30 03:49:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| ff18cc40-612e-3e8d-98cb-3ada173f16b6 | -14.78617 | -48.32043 | 2025-09-30 03:49:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| b5c4f629-6592-3238-be1d-796c151194a5 | -16.42094 | -47.04107 | 2025-09-30 03:49:00 | NOAA-20 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 5.2 |
| a1ec6cb3-2d73-362f-80d4-4555a3dea00c | -12.84458 | -46.96828 | 2025-09-30 03:49:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| a69d70b1-0544-3715-93de-9c7385cfa498 | -11.19809 | -47.22822 | 2025-09-30 03:49:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 8.7 |
| cda12089-cca9-3ee4-882b-6801245364d1 | -13.63716 | -48.04613 | 2025-09-30 03:49:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 69eda2b4-3d84-3f01-8530-c5a28445c82d | -11.88493 | -48.03987 | 2025-09-30 03:49:00 | NOAA-20 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| a1fdea3f-7401-337c-b20b-c8fc6326a212 | -5.71948 | -42.87846 | 2025-09-30 03:49:00 | NOAA-20 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 848756c0-26cd-3e87-9360-c6ddf3612ae7 | -16.49716 | -46.04206 | 2025-09-30 03:49:00 | NOAA-20 | BONFINÓPOLIS DE MINAS | MINAS GERAIS | Brasil | 3108206 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ab4eab48-988c-3d68-ace7-24dfcb8764a2 | -6.88274 | -44.52856 | 2025-09-30 03:49:00 | NOAA-20 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| b89e4f84-c2f7-3dda-a139-f09923fe55aa | -15.92611 | -46.20694 | 2025-09-30 03:49:00 | NOAA-20 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 9fb29cb6-3aaf-36d9-891d-f680be89dc2c | -7.17833 | -41.70135 | 2025-09-30 03:49:00 | NOAA-20 | PAQUETÁ | PIAUÍ | Brasil | 2207553 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 5ae374b5-b4d9-3f82-9318-1a7b03a8a562 | -13.80853 | -47.95492 | 2025-09-30 03:49:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 106cdbb7-5d0a-3181-a8af-f1bbee2e1cbd | -14.51378 | -48.39486 | 2025-09-30 03:49:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 11d8b075-3467-3f4d-8d7c-a27c3d88de42 | -13.21655 | -47.32281 | 2025-09-30 03:49:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| c7aa6998-f00f-3fbe-b674-11fee1cf03ca | -11.74146 | -46.84929 | 2025-09-30 03:49:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b483d38a-67b6-3d5b-a7d9-60d8c2e5d7fd | -6.14511 | -42.79211 | 2025-09-30 03:49:00 | NOAA-20 | ANGICAL DO PIAUÍ | PIAUÍ | Brasil | 2200608 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 7f3cbb04-ba6e-33af-b75e-01f51cb3293d | -12.37922 | -43.89487 | 2025-09-30 03:49:00 | NOAA-20 | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f1e8cce4-5a5d-3bab-acef-28eb6151c882 | -14.5159 | -48.38827 | 2025-09-30 03:49:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 9445d852-ad46-3319-8329-a33290140a9d | -14.7233 | -45.6712 | 2025-09-30 03:49:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 8c30144c-fa9a-31de-9222-6d77c31bac15 | -12.82485 | -46.99867 | 2025-09-30 03:49:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 9e674907-82df-34e8-9ec7-1df94b957b0a | -18.47286 | -44.02267 | 2025-09-30 03:49:00 | NOAA-20 | SANTO HIPÓLITO | MINAS GERAIS | Brasil | 3160603 | 31 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 591574f1-ede6-3aaa-a16c-317dbf41825b | -15.15416 | -46.43422 | 2025-09-30 03:49:00 | NOAA-20 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 82bcb2b5-45ee-3a83-be80-e552692870d6 | -12.85077 | -47.00238 | 2025-09-30 03:49:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| e85a53a1-5dcd-3c75-99d5-b38729e8b950 | -11.18935 | -47.24475 | 2025-09-30 03:49:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 8.2 |
| 4db3fc16-d730-3f89-9af4-7af7c6839ba4 | -18.47345 | -43.80112 | 2025-09-30 03:49:00 | NOAA-20 | GOUVEIA | MINAS GERAIS | Brasil | 3127602 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 713b0a55-e52b-3a27-9e2a-866df00a90d4 | -6.03634 | -43.81837 | 2025-09-30 03:49:00 | NOAA-20 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 0810ff59-b2ff-3a14-8ada-36709f4d10c3 | -12.95868 | -46.41241 | 2025-09-30 03:49:00 | NOAA-20 | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| c5b699bf-64d6-3a82-8733-692ab32b3fda | -5.72667 | -43.96865 | 2025-09-30 03:49:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| f8333b7b-e711-305e-bf50-6ee1262c6144 | -13.22298 | -50.9454 | 2025-09-30 03:49:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 15.4 |


[Clique aqui para ver as próximas entradas](README40.md)
