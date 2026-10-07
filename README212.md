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

## Dados Diários - Página 212

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| c8d644e8-a732-30bf-948c-2b2f0923db22 | -4.17296 | -42.04138 | 2026-10-07 16:37:00 | NPP-375 | BATALHA | PIAUÍ | Brasil | 2201507 | 22 | 33 | nan | nan | nan | Caatinga | 4.9 |
| e556e4ad-8285-3bbb-af72-0b866f7d8c7c | -5.96991 | -40.93016 | 2026-10-07 16:37:00 | NPP-375 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 9.2 |
| ec419a28-6dc3-3b85-ac29-37588e601291 | -9.03615 | -46.8759 | 2026-10-07 16:37:00 | NPP-375 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 25.9 |
| ae808325-9315-3b4c-bdd4-e8370934e902 | -4.97789 | -50.56952 | 2026-10-07 16:37:00 | NPP-375 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 7151234a-959a-347d-8478-ca18008c8182 | -11.20037 | -49.42405 | 2026-10-07 16:37:00 | NPP-375 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 16.8 |
| 241edcb2-dfcd-32f3-bc66-40de2ef0e107 | -5.68704 | -53.48242 | 2026-10-07 16:37:00 | NPP-375 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 36.2 |
| 68fda688-3333-3aff-aeab-5cd1b6179dd0 | -5.98083 | -40.92844 | 2026-10-07 16:37:00 | NPP-375 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 22.2 |
| 1a78c758-e16e-3312-a819-8d38ca3c2226 | -10.34612 | -40.4626 | 2026-10-07 16:37:00 | NPP-375 | CAMPO FORMOSO | BAHIA | Brasil | 2906006 | 29 | 33 | nan | nan | nan | Caatinga | 12.9 |
| 44f6e642-92e6-3ef9-ba3f-862d717b04a2 | -6.42436 | -44.83734 | 2026-10-07 16:37:00 | NPP-375 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 6.6 |
| d02ff26c-22f4-3e01-a356-30c3b14c158b | -9.91381 | -46.28706 | 2026-10-07 16:37:00 | NPP-375 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| c095f851-83c7-3d46-95c4-3b421d80a0dd | -16.05697 | -39.85777 | 2026-10-07 16:37:00 | NPP-375 | ITAGIMIRIM | BAHIA | Brasil | 2915304 | 29 | 33 | nan | nan | nan | Mata Atlântica | 47.1 |
| 118d1c98-5bf0-3cfa-8616-f35f818087d4 | -6.39668 | -52.72209 | 2026-10-07 16:37:00 | NPP-375 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 769d4b40-d6c1-3f69-8328-a9d98df8ac95 | -10.95605 | -45.38799 | 2026-10-07 16:37:00 | NPP-375 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 66f0aa14-fdaa-3e05-b3f9-7256420dbc0d | -7.74922 | -54.95123 | 2026-10-07 16:37:00 | NPP-375 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 37.0 |
| d8207450-48a3-3d39-bd80-56c8845ef38f | -11.14185 | -46.11219 | 2026-10-07 16:37:00 | NPP-375 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 18.2 |
| 7f6260e8-ed95-3edc-80c0-fedff4c06a1b | -9.15604 | -45.24809 | 2026-10-07 16:37:00 | NPP-375 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 2a1dc4da-b915-35fa-b6a7-39911480a84b | -4.23696 | -49.98801 | 2026-10-07 16:37:00 | NPP-375 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 17.5 |
| 26630b38-dba6-34be-8dc4-c71567a35313 | -5.67728 | -53.49133 | 2026-10-07 16:37:00 | NPP-375 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 8251d85e-724c-3cee-8141-af5d616050d2 | -9.14896 | -45.82338 | 2026-10-07 16:37:00 | NPP-375 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 14545a38-762a-3a7a-9081-99e37664ae53 | -14.56875 | -41.38459 | 2026-10-07 16:37:00 | NPP-375 | CARAÍBAS | BAHIA | Brasil | 2906899 | 29 | 33 | nan | nan | nan | Caatinga | 8.6 |
| ef24e370-d065-34ee-b77c-27950da76eb3 | -3.81311 | -40.45982 | 2026-10-07 16:37:00 | NPP-375 | SOBRAL | CEARÁ | Brasil | 2312908 | 23 | 33 | nan | nan | nan | Caatinga | 10.3 |
| 21aed020-6b5b-3150-a49d-c32699fb52c9 | -8.53337 | -54.62112 | 2026-10-07 16:37:00 | NPP-375 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 8.6 |
| 401fe736-eea0-35af-9828-9e0b97b4662b | -6.67675 | -44.96338 | 2026-10-07 16:37:00 | NPP-375 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 1892159c-f4dd-3613-bcc3-8c0817c291f0 | -4.94794 | -42.73045 | 2026-10-07 16:37:00 | NPP-375 | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Cerrado | 15.8 |
| c3954ce2-446b-3dd3-9fb2-2cfee9b1a7ae | -8.12267 | -42.0036 | 2026-10-07 16:37:00 | NPP-375 | NOVA SANTA RITA | PIAUÍ | Brasil | 2207959 | 22 | 33 | nan | nan | nan | Caatinga | 33.0 |
| 23a39834-fb7e-363b-ad6c-76323a1e20fe | -15.78642 | -47.97403 | 2026-10-07 16:37:00 | NPP-375 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 26ae05c3-a1dc-3d97-a3db-6b63f81ec338 | -8.80032 | -47.21987 | 2026-10-07 16:37:00 | NPP-375 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 67.9 |
| 89fbba96-ff0c-34dc-bf80-d007bd385e79 | -9.03371 | -46.88492 | 2026-10-07 16:37:00 | NPP-375 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 38.5 |
| 912f3f37-f7bc-3167-b813-679f65c95225 | -8.20585 | -46.33696 | 2026-10-07 16:37:00 | NPP-375 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 6ff06177-3cb4-3040-8478-7352b47209ea | -6.16232 | -53.30798 | 2026-10-07 16:37:00 | NPP-375 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 9.1 |
| d138a87d-a2b4-3283-97a2-0246fb15abb8 | -3.77046 | -41.79196 | 2026-10-07 16:37:00 | NPP-375 | SÃO JOSÉ DO DIVINO | PIAUÍ | Brasil | 2210052 | 22 | 33 | nan | nan | nan | Caatinga | 36.1 |
| 1c3ac0d0-8e07-38f3-8ca8-3fafee7d3f79 | -4.29086 | -38.57996 | 2026-10-07 16:37:00 | NPP-375 | BARREIRA | CEARÁ | Brasil | 2301950 | 23 | 33 | nan | nan | nan | Caatinga | 3.6 |
| 213eb216-c1be-38df-aa47-ac60d5b353ef | -6.0862 | -53.73 | 2026-10-07 16:37:00 | NPP-375 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 675407ed-f696-3676-b5dd-cdf93dde18be | -7.11003 | -48.0396 | 2026-10-07 16:37:00 | NPP-375 | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 26.9 |
| 186b2981-5eb1-3218-a85e-b77d0539c64c | -14.70417 | -41.27246 | 2026-10-07 16:37:00 | NPP-375 | CARAÍBAS | BAHIA | Brasil | 2906899 | 29 | 33 | nan | nan | nan | Caatinga | 8.3 |
| 675e7690-9e82-3c20-98c2-0a6239eff1a3 | -5.86854 | -40.72076 | 2026-10-07 16:37:00 | NPP-375 | QUITERIANÓPOLIS | CEARÁ | Brasil | 2311264 | 23 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 397be8a2-359a-3670-981f-84458b2eb0b2 | -17.02 | -45.91101 | 2026-10-07 16:37:00 | NPP-375 | BRASILÂNDIA DE MINAS | MINAS GERAIS | Brasil | 3108552 | 31 | 33 | nan | nan | nan | Cerrado | 22.4 |
| 0fb94730-597f-3b24-ac93-f27cff03c321 | -6.28683 | -44.90626 | 2026-10-07 16:37:00 | NPP-375 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 4.6 |
| a2237983-3702-37bc-a32d-0aa3d38e2827 | -11.01752 | -47.97595 | 2026-10-07 16:37:00 | NPP-375 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 6d9fd225-e392-3fa4-a111-e838854feab6 | -7.28775 | -43.86665 | 2026-10-07 16:37:00 | NPP-375 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 3.7 |
| b1fa83ba-bb69-3a40-abee-bf0fa04bf792 | -15.11397 | -43.62587 | 2026-10-07 16:37:00 | NPP-375 | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Caatinga | 11.5 |
| 58d08c74-a3a4-3daa-8398-443011f5c7a2 | -17.02968 | -45.92466 | 2026-10-07 16:37:00 | NPP-375 | BRASILÂNDIA DE MINAS | MINAS GERAIS | Brasil | 3108552 | 31 | 33 | nan | nan | nan | Cerrado | 5.5 |
| a883b1e4-c59a-33e4-b135-3316bd48ff4d | -3.75833 | -40.04326 | 2026-10-07 16:37:00 | NPP-375 | SOBRAL | CEARÁ | Brasil | 2312908 | 23 | 33 | nan | nan | nan | Caatinga | 13.2 |
| 440374ab-9f07-34db-a10f-16d53b03a990 | -11.13808 | -46.16664 | 2026-10-07 16:37:00 | NPP-375 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 5.9 |
| d17cfdbb-94ed-3f50-9f44-bf464d24d150 | -4.2625 | -42.29317 | 2026-10-07 16:37:00 | NPP-375 | BARRAS | PIAUÍ | Brasil | 2201200 | 22 | 33 | nan | nan | nan | Caatinga | 5.3 |
| ad15ccb7-7bce-366a-af4a-311b375bc5d6 | -3.73864 | -44.97824 | 2026-10-07 16:37:00 | NPP-375 | CONCEIÇÃO DO LAGO-AÇU | MARANHÃO | Brasil | 2103554 | 21 | 33 | nan | nan | nan | Amazônia | 19.2 |
| 07e56c41-a520-3659-ac51-58dd8402689a | -6.46499 | -55.44956 | 2026-10-07 16:37:00 | NPP-375 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 8.5 |
| 6fd5452d-79e8-369a-8c46-bb869167c009 | -3.76857 | -41.79242 | 2026-10-07 16:37:00 | NPP-375 | SÃO JOSÉ DO DIVINO | PIAUÍ | Brasil | 2210052 | 22 | 33 | nan | nan | nan | Caatinga | 32.1 |
| e123d685-4349-3ab6-a5ab-4b925113532a | -7.84241 | -45.50753 | 2026-10-07 16:37:00 | NPP-375 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 0b09dac7-0f4e-334d-84f5-40cddc534f14 | -3.36649 | -43.33518 | 2026-10-07 16:37:00 | NPP-375 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 22.6 |
| f59f738d-589a-3993-95f2-6afdc2f71343 | -4.46048 | -37.81091 | 2026-10-07 16:37:00 | NPP-375 | FORTIM | CEARÁ | Brasil | 2304459 | 23 | 33 | nan | nan | nan | Caatinga | 4.9 |
| 43c488ad-44a6-3268-991c-44f77cacedcc | -3.73443 | -39.53316 | 2026-10-07 16:37:00 | NPP-375 | ITAPAJÉ | CEARÁ | Brasil | 2306306 | 23 | 33 | nan | nan | nan | Caatinga | 6.9 |
| ca576ff9-642f-3977-83ad-19d23e0ee77a | -10.85403 | -47.93595 | 2026-10-07 16:37:00 | NPP-375 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 7ea3fa6c-8a5f-350c-aad1-02666c1d3b95 | -3.2328 | -40.03012 | 2026-10-07 16:37:00 | NPP-375 | MORRINHOS | CEARÁ | Brasil | 2308906 | 23 | 33 | nan | nan | nan | Caatinga | 5.9 |
| aa3a2542-e33a-3ccf-9a18-8c973929bf13 | -11.10519 | -45.95627 | 2026-10-07 16:37:00 | NPP-375 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 37.4 |
| be2ea0a9-32ac-336f-a883-c4126e150164 | -10.12557 | -46.85177 | 2026-10-07 16:37:00 | NPP-375 | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 18.0 |
| 0159f498-5cb6-3635-b54f-554c18ba94da | -7.591 | -55.73152 | 2026-10-07 16:37:00 | NPP-375 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 10.5 |
| 66fea2f9-7d34-30fe-9030-fc41d868cee1 | -3.90811 | -44.11696 | 2026-10-07 16:37:00 | NPP-375 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 155.1 |
| b15a04f7-65be-36c0-b0a1-9a96e3a358cf | -9.58702 | -54.63921 | 2026-10-07 16:37:00 | NPP-375 | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 32.9 |
| 607aa68d-b089-3925-bc41-06707a52afa7 | -6.0922 | -55.72727 | 2026-10-07 16:37:00 | NPP-375 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 10.5 |
| 2ae8ac79-75a9-3918-b01a-2a2fe7fec19b | -10.85223 | -47.93911 | 2026-10-07 16:37:00 | NPP-375 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 10.5 |
| 44373ece-209f-32d4-b725-0f25ec530fa5 | -3.47471 | -44.77688 | 2026-10-07 16:37:00 | NPP-375 | ARARI | MARANHÃO | Brasil | 2101004 | 21 | 33 | nan | nan | nan | Amazônia | 7.0 |
| f13f7b39-45cb-358a-bac4-e946c9d2f1bf | -16.8703 | -41.13079 | 2026-10-07 16:37:00 | NPP-375 | JOAÍMA | MINAS GERAIS | Brasil | 3136009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 6.2 |
| 410aec2e-c149-36c2-a52f-35e86e10beae | -7.21799 | -44.29772 | 2026-10-07 16:37:00 | NPP-375 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 3.5 |
| e552ec52-f952-3cac-8715-f425e25a5c12 | -8.74572 | -47.88015 | 2026-10-07 16:37:00 | NPP-375 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 8.6 |
| ab3efc65-569b-3c1e-bdd9-f8a7ac258f36 | -6.63871 | -43.77853 | 2026-10-07 16:37:00 | NPP-375 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 9a212c86-40a3-3f9b-915a-00d9c8ab9914 | -10.4937 | -49.27685 | 2026-10-07 16:37:00 | NPP-375 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 59681f5a-a623-3116-abe2-d2991fc8e2f2 | -11.11892 | -45.94992 | 2026-10-07 16:37:00 | NPP-375 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 54.4 |
| 6270779b-e12d-3526-9ae6-30cdc1f1b798 | -6.41882 | -54.97001 | 2026-10-07 16:37:00 | NPP-375 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| b1cc1cb7-e3fa-32af-843d-d5bef8d3ddd2 | -3.55725 | -39.14127 | 2026-10-07 16:37:00 | NPP-375 | SÃO GONÇALO DO AMARANTE | CEARÁ | Brasil | 2312403 | 23 | 33 | nan | nan | nan | Caatinga | 35.5 |
| 5c216ae7-99c8-3def-b420-f9fa64138ec5 | -6.82158 | -38.52658 | 2026-10-07 16:37:00 | NPP-375 | CAJAZEIRAS | PARAÍBA | Brasil | 2503704 | 25 | 33 | nan | nan | nan | Caatinga | 4.5 |
| d61dc26d-4cdc-3de7-b64b-635596863fe5 | -9.82628 | -46.24868 | 2026-10-07 16:37:00 | NPP-375 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 18.3 |
| a8b5d921-ac4c-3443-9141-a7b59bbadd0c | -9.81739 | -47.47597 | 2026-10-07 16:37:00 | NPP-375 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 12.9 |
| d813eaad-b6f4-3392-9acd-9b66caff139a | -3.73907 | -39.53593 | 2026-10-07 16:37:00 | NPP-375 | ITAPAJÉ | CEARÁ | Brasil | 2306306 | 23 | 33 | nan | nan | nan | Caatinga | 5.7 |
| d6edf5ac-67f0-3f36-9979-a209f47e4992 | -11.20153 | -49.43281 | 2026-10-07 16:37:00 | NPP-375 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 3ece6de0-cfd8-34e3-ab1b-87449d94d40e | -7.74969 | -54.95239 | 2026-10-07 16:37:00 | NPP-375 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 33.7 |
| e2b3c8ab-1791-3e2f-b4a8-e2e394228873 | -3.63086 | -44.80452 | 2026-10-07 16:37:00 | NPP-375 | ARARI | MARANHÃO | Brasil | 2101004 | 21 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 4f46a850-7a93-3f2d-83c3-2b0dd876fe3b | -2.91889 | -40.32393 | 2026-10-07 16:37:00 | NPP-375 | CRUZ | CEARÁ | Brasil | 2304251 | 23 | 33 | nan | nan | nan | Caatinga | 5.6 |
| f3300cb5-6332-3b6e-adcc-a93cfe731dde | -10.85686 | -50.69444 | 2026-10-07 16:37:00 | NPP-375 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 17.0 |
| 1049ac34-2035-36e0-8579-d6329c86107f | -6.70529 | -44.0133 | 2026-10-07 16:37:00 | NPP-375 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 6.8 |
| da93af3a-fdfe-3a63-af3a-097b5b8945c8 | -7.28908 | -47.28823 | 2026-10-07 16:37:00 | NPP-375 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 47d04dff-9b9b-34e4-92d8-2d76990b2b0f | -4.29077 | -43.64444 | 2026-10-07 16:37:00 | NPP-375 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 240351e5-7f0e-334b-8f20-73a9b800b687 | -3.86366 | -44.13794 | 2026-10-07 16:37:00 | NPP-375 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 12.2 |
| 98f99a54-43df-33ce-a077-dc22ecd31413 | -7.20683 | -46.56557 | 2026-10-07 16:37:00 | NPP-375 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 48.4 |
| 0cc35d2d-b492-3600-8c6c-a88bf0021b42 | -5.18031 | -46.18857 | 2026-10-07 16:37:00 | NPP-375 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 16.3 |
| ee3c158d-3a7f-3797-83be-413ffddf112c | -3.1467 | -42.95537 | 2026-10-07 16:37:00 | NPP-375 | BARREIRINHAS | MARANHÃO | Brasil | 2101707 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 1fee9cbe-c574-3d1a-8312-0e8a40e0eea7 | -17.19359 | -43.51393 | 2026-10-07 16:37:00 | NPP-375 | BOCAIÚVA | MINAS GERAIS | Brasil | 3107307 | 31 | 33 | nan | nan | nan | Cerrado | 3.0 |
| b3d407e0-0312-30f7-b921-8dd606c4a941 | -3.19544 | -42.95523 | 2026-10-07 16:37:00 | NPP-375 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 10.8 |
| 3d983f7e-9b64-32be-a361-c8d6c04b0d08 | -6.94173 | -45.26491 | 2026-10-07 16:37:00 | NPP-375 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 10.1 |
| a5dbd193-c7fc-36dd-911a-9f2d5e5a315a | -7.03324 | -43.44104 | 2026-10-07 16:37:00 | NPP-375 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 1274858b-491a-3e5b-a88a-3a6fbc9f235c | -6.13965 | -51.93979 | 2026-10-07 16:37:00 | NPP-375 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 20.2 |
| 4ca98b25-e59f-3193-bcb0-e052415f677c | -6.63637 | -43.98482 | 2026-10-07 16:37:00 | NPP-375 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 23.0 |
| 6d6bfe52-43f6-34cc-aaac-3af912ec6bdf | -11.07856 | -45.64068 | 2026-10-07 16:37:00 | NPP-375 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 9.0 |
| 1d65feee-472c-3566-821c-44c991b0ec77 | -5.75751 | -42.04524 | 2026-10-07 16:37:00 | NPP-375 | SANTA CRUZ DOS MILAGRES | PIAUÍ | Brasil | 2209153 | 22 | 33 | nan | nan | nan | Caatinga | 23.1 |
| 2c1ef4a0-681e-36d4-b887-9b154a1e4978 | -3.85234 | -40.63171 | 2026-10-07 16:37:00 | NPP-375 | CARIRÉ | CEARÁ | Brasil | 2303105 | 23 | 33 | nan | nan | nan | Caatinga | 28.4 |
| 7ca3b25b-023b-3f94-b4a5-f3918c4c8ed7 | -6.94334 | -45.27567 | 2026-10-07 16:37:00 | NPP-375 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 14.5 |
| 6590d44d-3067-31f4-8209-79863b5e8199 | -3.75722 | -40.83307 | 2026-10-07 16:37:00 | NPP-375 | FRECHEIRINHA | CEARÁ | Brasil | 2304509 | 23 | 33 | nan | nan | nan | Caatinga | 16.6 |
| 4917f054-86f4-3da6-858d-f372f4e235ce | -16.98001 | -45.47219 | 2026-10-07 16:37:00 | NPP-375 | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 10.6 |
| 08de07eb-bff8-3e49-86d7-05586775ca87 | -6.59541 | -47.40517 | 2026-10-07 16:37:00 | NPP-375 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 69.6 |
| e41e7cbd-1ac3-3655-ab6a-e7e12603a14a | -5.95293 | -46.36373 | 2026-10-07 16:37:00 | NPP-375 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 8.1 |


[Clique aqui para ver as próximas entradas](README213.md)
