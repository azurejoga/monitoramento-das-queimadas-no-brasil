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

## Dados Diários - Página 53

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| e3b61660-a7f8-3d18-921e-7809f021fdaa | -7.07055 | -44.73096 | 2025-10-18 04:29:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 9eb20c0c-b190-340f-8b3e-3bfea66c408f | -5.06189 | -45.85812 | 2025-10-18 04:29:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 72dfd041-62c1-3745-a359-b8436ce394fe | -6.72741 | -46.27751 | 2025-10-18 04:29:00 | NPP-375D | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 66ce3e14-b45a-3534-b356-6fe3d319a6a1 | -10.42681 | -45.01424 | 2025-10-18 04:29:00 | NPP-375D | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 11111092-3c0a-3f20-9a85-6c8fb8fba94c | -9.64834 | -47.12446 | 2025-10-18 04:29:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| fd3dfe3b-03cc-3ae3-ab07-1844706baf9b | -10.49028 | -43.39761 | 2025-10-18 04:29:00 | NPP-375D | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| c29fc221-45e8-354d-b0f1-ca7476d002e2 | -6.90105 | -47.99305 | 2025-10-18 04:29:00 | NPP-375D | WANDERLÂNDIA | TOCANTINS | Brasil | 1722081 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 8c888c85-0619-305f-b432-46727052a395 | -8.22409 | -47.84535 | 2025-10-18 04:29:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| ad9c22b6-068b-38a9-b83c-5dd2205733cf | -7.23531 | -45.73504 | 2025-10-18 04:29:00 | NPP-375D | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 4716dd99-18d2-396b-abeb-3e645e554d7e | -5.55918 | -46.37331 | 2025-10-18 04:29:00 | NPP-375D | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| a5588361-7817-39bb-b77c-da980e61298b | -6.29384 | -44.72236 | 2025-10-18 04:29:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 6398abec-039f-353a-813f-46daf95e5c1e | -9.19776 | -46.86936 | 2025-10-18 04:29:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 5f0b4eae-9fba-3a69-bfbe-e7f03c71b8b9 | -10.49951 | -43.28021 | 2025-10-18 04:29:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 6adf19d3-9e27-3a9a-9d1e-6a6d082a7e89 | -7.44287 | -43.75834 | 2025-10-18 04:29:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 2e20d0d8-60d2-30b0-8878-e430f3f78b25 | -7.11959 | -44.73093 | 2025-10-18 04:29:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 9b628a67-dcc2-3419-b4a1-42d0c669f975 | -5.1718 | -46.1875 | 2025-10-18 04:29:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 33aa22fc-445a-31a2-9d68-e583ced72d48 | -7.75451 | -42.50753 | 2025-10-18 04:29:00 | NPP-375D | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 37225b0b-2afc-301f-92fc-d7d90dd9b4c3 | -10.49267 | -43.43406 | 2025-10-18 04:29:00 | NPP-375D | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 11.7 |
| c60e2ef0-a06e-327a-874f-6cd4746a9e37 | -7.10836 | -44.82286 | 2025-10-18 04:29:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 7a51467c-6068-3d2c-9ba7-6e1c11f040ef | -4.94281 | -49.76068 | 2025-10-18 04:29:00 | NPP-375D | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d6add86b-d2b9-3159-9542-6d272921d0c9 | -4.82151 | -45.23642 | 2025-10-18 04:29:00 | NPP-375D | LAGO DA PEDRA | MARANHÃO | Brasil | 2105708 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 4bb6e607-ca18-3578-929a-0b16a221ef94 | -5.92764 | -45.44477 | 2025-10-18 04:29:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| ad7d5499-04eb-3569-827b-6ae00c5c1c2b | -7.35354 | -41.90177 | 2025-10-18 04:29:00 | NPP-375D | SANTO INÁCIO DO PIAUÍ | PIAUÍ | Brasil | 2209500 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| acc5c797-21fb-38b9-bf8c-599574ef2405 | -10.49952 | -43.43971 | 2025-10-18 04:29:00 | NPP-375D | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| db89d1c5-9698-37b9-a47c-9fdcf871d5f7 | -8.61207 | -40.20107 | 2025-10-18 04:29:00 | NPP-375D | LAGOA GRANDE | PERNAMBUCO | Brasil | 2608750 | 26 | 33 | nan | nan | nan | Caatinga | 5.5 |
| 603554f0-b889-36c4-a9ac-f5d51dc122f3 | -6.4559 | -46.28055 | 2025-10-18 04:29:00 | NPP-375D | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 04be8a41-4ac2-330d-a21a-e21eaef1c5e1 | -6.36232 | -45.78159 | 2025-10-18 04:29:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 0d8384fa-6807-3175-bf54-4beb77a05622 | -5.91088 | -44.76103 | 2025-10-18 04:29:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 05516f38-0b30-3ebc-ac4d-e182a7340daa | -6.72795 | -46.27404 | 2025-10-18 04:29:00 | NPP-375D | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 254c353e-666b-39b4-a594-70012a0e86c8 | -10.69431 | -44.55721 | 2025-10-18 04:29:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 4d89c144-f666-3fc8-aefc-84310bdf06e9 | -5.85106 | -44.34015 | 2025-10-18 04:29:00 | NPP-375D | JATOBÁ | MARANHÃO | Brasil | 2105450 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| c3b7a4ed-237d-3542-9f44-f25ff3068c65 | -8.53683 | -50.08018 | 2025-10-18 04:29:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 445faad2-fc4c-3644-ba69-65c3b40e345b | -5.11802 | -49.26163 | 2025-10-18 04:29:00 | NPP-375D | NOVA IPIXUNA | PARÁ | Brasil | 1504976 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5d657ebf-ac26-3732-a838-8ec8439eca04 | -10.12923 | -44.53391 | 2025-10-18 04:29:00 | NPP-375D | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 1255a969-1d5d-318e-b1f2-72918d850f55 | -6.33945 | -44.00298 | 2025-10-18 04:29:00 | NPP-375D | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 59833c00-425a-336e-8a1c-53dd10de1363 | -9.66938 | -44.55251 | 2025-10-18 04:29:00 | NPP-375D | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| b0732e0a-bc3a-3e2d-85ed-cfb976912d78 | -7.6605 | -44.63687 | 2025-10-18 04:29:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d8b57c66-6440-315d-895b-d32f9543ff16 | -10.42622 | -45.0181 | 2025-10-18 04:29:00 | NPP-375D | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 627aff2b-ea08-3e56-a111-a8c366907a0e | -10.61431 | -47.32264 | 2025-10-18 04:29:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| a928911b-3b45-39ac-81ef-7a2fed9ff5d1 | -7.18386 | -42.18507 | 2025-10-18 04:29:00 | NPP-375D | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 315ced22-8c4f-33c0-b6c5-5035c73edbb6 | -8.54615 | -44.58085 | 2025-10-18 04:29:00 | NPP-375D | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 991b262d-4267-3131-9124-ef5e6a4f5086 | -10.68453 | -45.33396 | 2025-10-18 04:29:00 | NPP-375D | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 30687c21-1c98-3fc1-843d-ce86d8b37d7f | -6.1428 | -44.45953 | 2025-10-18 04:29:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 38e8994c-ab2a-3c2d-8eeb-bee5bfd1e0d0 | -10.53565 | -44.50906 | 2025-10-18 04:29:00 | NPP-375D | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 8d612446-19d1-3fd2-a36f-741c971f979e | -8.19581 | -43.31001 | 2025-10-18 04:29:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 0f22c42d-8f72-3e1a-a7e8-42c730912448 | -9.91375 | -47.66371 | 2025-10-18 04:29:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 99818202-65d3-386b-a337-57186cc92bda | -5.71493 | -43.82488 | 2025-10-18 04:29:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 2384ad8f-bc35-3a63-aac2-233a9e9478a0 | -5.07414 | -49.8537 | 2025-10-18 04:29:00 | NPP-375D | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| d7da5962-3f0e-376f-ad4e-9ec240249500 | -6.23777 | -44.15562 | 2025-10-18 04:29:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 20ae6773-8161-3932-b221-3f5674b0f6d5 | -5.16547 | -45.22182 | 2025-10-18 04:29:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 6c91d532-2521-3693-a892-8de537e823fe | -7.16532 | -42.37416 | 2025-10-18 04:29:00 | NPP-375D | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 5.1 |
| 4a9fe6f2-7a87-3513-86e8-f445b456566a | -6.17978 | -46.74253 | 2025-10-18 04:29:00 | NPP-375D | LAJEADO NOVO | MARANHÃO | Brasil | 2105989 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 3df25ddb-7bc8-3a42-bc48-87b2f1d064b8 | -6.13138 | -44.30555 | 2025-10-18 04:29:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a989a18d-4edd-3b33-acbc-731afcbf192b | -7.70958 | -47.85116 | 2025-10-18 04:29:00 | NPP-375D | FILADÉLFIA | TOCANTINS | Brasil | 1707702 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ce9e8335-5e30-3fb7-8ba9-639b2002825a | -8.21125 | -46.92669 | 2025-10-18 04:29:00 | NPP-375D | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| df8d806d-c61a-3988-bbee-199af10be022 | -10.48826 | -43.43801 | 2025-10-18 04:29:00 | NPP-375D | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 10.6 |
| d51a4c17-128f-3651-9898-26fb8b37f309 | -6.89838 | -45.45134 | 2025-10-18 04:29:00 | NPP-375D | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| befe8e73-53b6-3edb-92d4-345f5b343c66 | -10.24414 | -44.03838 | 2025-10-18 04:29:00 | NPP-375D | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d16cde17-0b55-3e4d-a787-1954aad80039 | -6.89167 | -45.4503 | 2025-10-18 04:29:00 | NPP-375D | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 00413dea-f05c-31ed-ba43-79d0fe42d160 | -10.53857 | -44.05839 | 2025-10-18 04:29:00 | NPP-375D | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 0.4 |
| b2d3b5f0-c91c-3a83-b8f9-0f9cf937ba71 | -9.72036 | -44.57252 | 2025-10-18 04:29:00 | NPP-375D | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 13ffaa34-40a8-3a32-8b38-2dadabcfd954 | -7.98664 | -44.15857 | 2025-10-18 04:29:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 884efdda-a08a-380c-8dd1-78549a02c80e | -10.53708 | -43.36706 | 2025-10-18 04:29:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 640a2d8d-39d5-3192-b87c-da1a5b56b222 | -7.80388 | -54.93409 | 2025-10-18 04:29:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| b340c062-3a30-3273-bf27-b5bb828389f7 | -6.27252 | -44.56982 | 2025-10-18 04:29:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 3c4fdc9c-69c3-378d-bb07-c05baf42321f | -6.13482 | -44.30612 | 2025-10-18 04:29:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a2930400-e657-34fd-bbc9-243ad079ee5c | -10.4207 | -44.91406 | 2025-10-18 04:29:00 | NPP-375D | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 9b35618d-3142-316f-b945-9fb891f6a57f | -7.65992 | -44.64064 | 2025-10-18 04:29:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 0a8bf4f3-d2b6-3de9-8b36-5b63e6b62dd3 | -6.36565 | -45.78213 | 2025-10-18 04:29:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 6ddb8c65-4928-3fdd-b654-4a13466a2cfd | -7.21562 | -43.80858 | 2025-10-18 04:29:00 | NPP-375D | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| fdc39e67-785b-3839-a04d-e5b12610cbbe | -6.03751 | -43.40704 | 2025-10-18 04:29:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 7bdc6df1-0629-38f7-9df6-bf948b9c5d86 | -9.24694 | -44.34572 | 2025-10-18 04:29:00 | NPP-375D | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| b80303e1-150f-3f86-a6f4-b2a8cf7d8dac | -5.01293 | -46.01716 | 2025-10-18 04:29:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 31.4 |
| 62216a7e-d0d3-3f95-a297-da6b27367836 | -5.57959 | -44.18085 | 2025-10-18 04:29:00 | NPP-375D | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 95cf5935-9b04-3298-bacf-7c3348a4c991 | -6.35616 | -45.75558 | 2025-10-18 04:29:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| a3b86d61-6141-3e8a-92ef-100887cca11f | -5.58071 | -41.32125 | 2025-10-18 04:29:00 | NPP-375D | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| a4e11221-d9e1-3588-a136-14248f6cc1cb | -7.18982 | -47.58483 | 2025-10-18 04:29:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 55f58bbd-ef2f-3b9c-a496-a146e2a1b840 | -6.40154 | -41.47167 | 2025-10-18 04:29:00 | NPP-375D | LAGOA DO SÍTIO | PIAUÍ | Brasil | 2205599 | 22 | 33 | nan | nan | nan | Caatinga | 3.6 |
| fdba67a2-25a8-32b4-854d-0aafe0964482 | -5.63577 | -50.03165 | 2025-10-18 04:29:00 | NPP-375D | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 1c1832f2-193e-3143-b924-4adb58efec97 | -6.45373 | -44.2029 | 2025-10-18 04:29:00 | NPP-375D | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d36880c0-6256-3f66-ac6d-4af2ac1233b2 | -6.41446 | -43.46902 | 2025-10-18 04:29:00 | NPP-375D | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| eca26c71-7c80-385f-a667-e8a86950c330 | -5.45713 | -45.41102 | 2025-10-18 04:29:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 4adb8800-bb2e-34ee-8aeb-44a855442e30 | -8.23623 | -44.00705 | 2025-10-18 04:29:00 | NPP-375D | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 4fe2d271-0cf9-3100-b1ee-b0d2543ff350 | -6.94663 | -47.77356 | 2025-10-18 04:29:00 | NPP-375D | WANDERLÂNDIA | TOCANTINS | Brasil | 1722081 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 3f7a63b9-afe0-313a-88cc-27d02b3bc8cb | -5.01129 | -46.02755 | 2025-10-18 04:29:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 7.9 |
| 69126d1d-5e32-3d14-9de4-90f0b7297ed0 | -7.14608 | -46.41146 | 2025-10-18 04:29:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| b88e831c-6421-32ef-99d7-826e1f61558f | -4.24981 | -48.3712 | 2025-10-18 04:29:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f16b9d39-e1ff-31b8-9483-b2101a51ae97 | -10.50063 | -43.45838 | 2025-10-18 04:29:00 | NPP-375D | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 99ed7db1-f93e-3dbc-9c1e-f27a27a55955 | -5.33313 | -45.78756 | 2025-10-18 04:29:00 | NPP-375D | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 6a76ecfe-66eb-34bf-8c61-878e9291827c | -7.06805 | -45.6184 | 2025-10-18 04:29:00 | NPP-375D | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 74411060-1cb0-3878-9f5d-a59053711953 | -10.48123 | -47.73745 | 2025-10-18 04:29:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| fcded80c-7f9c-364c-9cd7-82969c3faa1c | -8.18914 | -42.35052 | 2025-10-18 04:29:00 | NPP-375D | SÃO JOÃO DO PIAUÍ | PIAUÍ | Brasil | 2210003 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 65c3eb13-1a85-3b0d-9560-057b3362e520 | -6.56482 | -44.43515 | 2025-10-18 04:29:00 | NPP-375D | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| f735e12d-3d3f-3b56-8d3f-f355ec93cb30 | -10.42319 | -47.74264 | 2025-10-18 04:29:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 9cba16f7-dc52-3e6e-9939-e2d0aba6d529 | -3.59321 | -53.95649 | 2025-10-18 04:29:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 6631b89d-fd80-3f03-b8c7-bcacf7edb844 | -8.16338 | -43.30062 | 2025-10-18 04:29:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 833e497a-c7cb-3da1-8986-231fd4d864bb | -10.50504 | -43.45445 | 2025-10-18 04:29:00 | NPP-375D | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 10.0 |
| 1b2029d9-1d56-3111-b1db-f85dabeb8084 | -8.35726 | -46.21664 | 2025-10-18 04:29:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 83b0cdeb-f218-3fa3-899c-f2181db9dee0 | -10.71546 | -44.55544 | 2025-10-18 04:29:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 107d8b4a-2c33-3fae-b75a-50214cd9ad85 | -7.765 | -42.48985 | 2025-10-18 04:29:00 | NPP-375D | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 3.1 |


[Clique aqui para ver as próximas entradas](README54.md)
