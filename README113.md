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

## Dados Diários - Página 113

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 96be5a77-3784-3f90-8e4b-117033c19606 | -15.02825 | -48.76049 | 2025-10-17 05:12:00 | NOAA-20 | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 5e0229da-efe9-3ef5-9228-593fc1586b34 | -14.92282 | -46.73117 | 2025-10-17 05:12:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 4f32d6ed-2b1d-3fa5-bbd4-8bc4cd291be9 | -18.26932 | -51.30661 | 2025-10-17 05:12:00 | NOAA-20 | APARECIDA DO RIO DOCE | GOIÁS | Brasil | 5201454 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 1e470859-f478-3e83-a398-37059079da86 | -16.49161 | -49.43292 | 2025-10-17 05:12:00 | NOAA-20 | GOIANIRA | GOIÁS | Brasil | 5208806 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| fa9a7224-3278-3de8-9b77-fbbbb415b266 | -14.93026 | -46.72153 | 2025-10-17 05:12:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| d7b74493-d90e-3490-bbfe-3ed07ba6f36f | -16.81487 | -53.92471 | 2025-10-17 05:12:00 | NOAA-20 | PEDRA PRETA | MATO GROSSO | Brasil | 5106372 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 051f0e50-e342-36c6-98a5-983729fe289d | -19.4484 | -55.9207 | 2025-10-17 05:12:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 2.3 |
| aa24f62f-6f11-3b17-a8d3-835b75bab790 | -14.91632 | -46.72919 | 2025-10-17 05:12:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| df214c94-5f4a-3762-aa60-c12c58226acf | -16.81071 | -53.9242 | 2025-10-17 05:12:00 | NOAA-20 | PEDRA PRETA | MATO GROSSO | Brasil | 5106372 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| af013e5c-21c2-3345-855f-3e233f972da2 | -16.80551 | -53.93163 | 2025-10-17 05:12:00 | NOAA-20 | PEDRA PRETA | MATO GROSSO | Brasil | 5106372 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e6c29ab5-fdb7-37b3-b10a-f6514abec528 | -19.44394 | -55.92504 | 2025-10-17 05:12:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 2.3 |
| 6f66aa3a-1863-3261-b008-73cae65c92c5 | -14.24183 | -54.89879 | 2025-10-17 05:12:00 | NOAA-20 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 1026dbff-05d1-3ac2-beb3-1f9ce476d02c | -16.81019 | -53.92819 | 2025-10-17 05:12:00 | NOAA-20 | PEDRA PRETA | MATO GROSSO | Brasil | 5106372 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e48e8f1b-8f6c-3934-9454-aecc7090fef7 | -18.38747 | -55.46598 | 2025-10-17 05:12:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.4 |
| 23c74122-9844-3e5a-a00a-e1deaea6dfb6 | -16.80603 | -53.92765 | 2025-10-17 05:12:00 | NOAA-20 | PEDRA PRETA | MATO GROSSO | Brasil | 5106372 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b5686586-3de6-365c-a1b4-8831e5ff1c9e | -17.57131 | -45.60843 | 2025-10-17 05:12:00 | NOAA-20 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| cfc30156-5582-3368-a2a6-a1f5776bf922 | -19.45221 | -55.92126 | 2025-10-17 05:12:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 1.4 |
| 518166a5-20e5-3b89-ad9c-d4f0c7896a96 | -15.03914 | -47.3124 | 2025-10-17 05:12:00 | NOAA-20 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 0cc90804-0f8d-31cf-875e-b93ba1da0d23 | -16.81122 | -53.92019 | 2025-10-17 05:12:00 | NOAA-20 | PEDRA PRETA | MATO GROSSO | Brasil | 5106372 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| b282ea6c-a94b-34a4-8700-07e93927c839 | -14.91584 | -46.73539 | 2025-10-17 05:12:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ddc257b2-472b-3dc7-bf09-d74c8e629310 | -14.23602 | -54.91245 | 2025-10-17 05:12:00 | NOAA-20 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| f97d6c21-ef29-3b69-ba27-fb17743b8580 | -14.92328 | -46.72547 | 2025-10-17 05:12:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| fadb37fa-f7ef-3d6f-894c-16cb0248e419 | -21.43355 | -54.15794 | 2025-10-17 05:14:00 | NOAA-20 | NOVA ALVORADA DO SUL | MATO GROSSO DO SUL | Brasil | 5006002 | 50 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 5e664a78-9993-3800-8294-3580e8151c49 | -21.4379 | -54.15864 | 2025-10-17 05:14:00 | NOAA-20 | NOVA ALVORADA DO SUL | MATO GROSSO DO SUL | Brasil | 5006002 | 50 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 21a609c5-5d03-3024-b12c-1ccb08478855 | -3.5028 | -52.4938 | 2025-10-17 05:20:00 | GOES-19 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 51.0 |
| f81c544f-a785-331e-b5a3-91a4a45286ab | -8.38474 | -46.24773 | 2025-10-17 05:44:00 | AQUA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 14.6 |
| f28e33a2-5ca4-31ab-a444-bd4cfb617285 | -9.71862 | -44.55084 | 2025-10-17 05:44:00 | AQUA_M-M | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 29af9d9c-4249-34f8-b9c8-c1ca6813f4fa | -7.17444 | -42.36706 | 2025-10-17 05:44:00 | AQUA_M-M | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 14.5 |
| 0ee2a773-939c-364e-8fe1-40b461a4df9d | -10.08613 | -45.34052 | 2025-10-17 05:44:00 | AQUA_M-M | SÃO GONÇALO DO GURGUÉIA | PIAUÍ | Brasil | 2209757 | 22 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 06bca96c-4f8c-37fb-a415-a4b56bea8686 | -6.58646 | -47.07737 | 2025-10-17 05:44:00 | AQUA_M-M | SÃO JOÃO DO PARAÍSO | MARANHÃO | Brasil | 2111052 | 21 | 33 | nan | nan | nan | Cerrado | 12.9 |
| 7047d38a-0410-38f2-8d79-754d600a0c0a | -10.29382 | -44.04313 | 2025-10-17 05:44:00 | AQUA_M-M | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 46.8 |
| 2100038c-e272-397c-b399-e016d8e3cbd6 | -10.28771 | -44.02399 | 2025-10-17 05:44:00 | AQUA_M-M | AVELINO LOPES | PIAUÍ | Brasil | 2201101 | 22 | 33 | nan | nan | nan | Cerrado | 21.7 |
| db5bd097-316d-319d-a056-687bdc854a9c | -4.42096 | -43.40308 | 2025-10-17 05:44:00 | AQUA_M-M | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 22.3 |
| d31c8e30-7936-36ba-a271-cc6ebf19fdcc | -10.27011 | -44.02129 | 2025-10-17 05:44:00 | AQUA_M-M | AVELINO LOPES | PIAUÍ | Brasil | 2201101 | 22 | 33 | nan | nan | nan | Cerrado | 17.3 |
| 0f1d95cb-65cc-315e-80f4-be99858a604d | -8.4569 | -46.2438 | 2025-10-17 05:44:00 | AQUA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 9.9 |
| be30b98d-45c0-32e4-8a7a-5138ffb97242 | -5.98395 | -42.7913 | 2025-10-17 05:44:00 | AQUA_M-M | ANGICAL DO PIAUÍ | PIAUÍ | Brasil | 2200608 | 22 | 33 | nan | nan | nan | Caatinga | 8.7 |
| 65ba19e3-0805-37db-8010-1efad39cc0ec | -6.18583 | -42.61843 | 2025-10-17 05:44:00 | AQUA_M-M | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 8.2 |
| e58e9823-8fe6-3945-a884-97d0a188eeb0 | -10.50761 | -43.43378 | 2025-10-17 05:44:00 | AQUA_M-M | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 35.5 |
| 066f3616-012d-3d8b-93a1-05f9629e8c97 | -11.47552 | -45.0892 | 2025-10-17 05:44:00 | AQUA_M-M | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 7.9 |
| c980cafa-2e3d-3c07-981d-c97a5d2ac55b | -8.30785 | -43.43389 | 2025-10-17 05:44:00 | AQUA_M-M | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 6.1 |
| d8565d71-0c35-3349-b0b0-abfe7fb28966 | -10.43149 | -45.02056 | 2025-10-17 05:44:00 | AQUA_M-M | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 17.8 |
| c5f04684-f988-32df-93f0-1cd89b431154 | -10.50894 | -43.4249 | 2025-10-17 05:44:00 | AQUA_M-M | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 31.6 |
| e5071411-df08-30f6-b3ce-1795e3103293 | -10.64732 | -45.29831 | 2025-10-17 05:44:00 | AQUA_M-M | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 6f9e9ce0-236b-36d8-8ea9-f0d146412d89 | -10.16383 | -44.53895 | 2025-10-17 05:44:00 | AQUA_M-M | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 8.4 |
| 1432bcf6-211b-3d5e-8c55-206f92974c06 | -8.30306 | -43.40609 | 2025-10-17 05:44:00 | AQUA_M-M | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 4.5 |
| 6363b7af-1062-36b2-b761-322925c90966 | -7.95405 | -44.11935 | 2025-10-17 05:44:00 | AQUA_M-M | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 20.2 |
| 695f68dc-b660-36a9-ab9f-bc7dc67bca33 | -9.0653 | -42.45554 | 2025-10-17 05:44:00 | AQUA_M-M | SÃO RAIMUNDO NONATO | PIAUÍ | Brasil | 2210607 | 22 | 33 | nan | nan | nan | Caatinga | 6.9 |
| 33db9812-a9ee-3715-950e-986711d32141 | -9.16011 | -41.05058 | 2025-10-17 05:44:00 | AQUA_M-M | CASA NOVA | BAHIA | Brasil | 2907202 | 29 | 33 | nan | nan | nan | Caatinga | 18.9 |
| 91890e06-f945-3133-a4bc-b4144ac499a7 | -2.74805 | -49.3813 | 2025-10-17 05:44:00 | AQUA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 15.6 |
| ad65a145-49ac-3465-bef8-4846d67092a8 | -10.64879 | -45.28881 | 2025-10-17 05:44:00 | AQUA_M-M | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 4.7 |
| a287ec1d-5e36-3d02-bc22-d4f5f2de8884 | -7.34522 | -43.86425 | 2025-10-17 05:44:00 | AQUA_M-M | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 28.0 |
| be828597-3d59-3030-862e-af97d762f1d5 | -4.72073 | -46.44486 | 2025-10-17 05:44:00 | AQUA_M-M | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 11.5 |
| 9ccece78-1e93-3769-9ec6-69892972b6b3 | -10.14746 | -44.52705 | 2025-10-17 05:44:00 | AQUA_M-M | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 9.5 |
| 3b028184-c962-329a-9ea5-0aa0d42cdb4e | -6.20204 | -41.75813 | 2025-10-17 05:44:00 | AQUA_M-M | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 4.7 |
| dbfd6e43-b7ef-344a-8091-e731c2516bf4 | -6.03453 | -41.90094 | 2025-10-17 05:44:00 | AQUA_M-M | SANTA CRUZ DOS MILAGRES | PIAUÍ | Brasil | 2209153 | 22 | 33 | nan | nan | nan | Caatinga | 12.6 |
| fc97a437-2827-3b52-ad28-457f1c88c15c | -5.88903 | -43.90436 | 2025-10-17 05:44:00 | AQUA_M-M | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 9.3 |
| 3164ed51-8912-3420-aedd-88fa9f4b553e | -7.04633 | -42.72922 | 2025-10-17 05:44:00 | AQUA_M-M | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 4.6 |
| 91b29638-50ae-31e5-a40d-849955822fbf | -7.34659 | -43.85524 | 2025-10-17 05:44:00 | AQUA_M-M | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 52.6 |
| e0574a86-685e-3eca-bbd8-44e84820962c | -10.12576 | -44.54481 | 2025-10-17 05:44:00 | AQUA_M-M | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 6.5 |
| b61c1f77-95b1-3239-8a23-bb02d845197e | -8.19859 | -43.31153 | 2025-10-17 05:44:00 | AQUA_M-M | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 32.6 |
| 97cb24ab-acdf-34c9-9b9a-0f78e3634c16 | -8.37485 | -46.24664 | 2025-10-17 05:44:00 | AQUA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 12.2 |
| 676f6914-8a81-3638-8ee6-981999c6b42f | -4.40451 | -43.39137 | 2025-10-17 05:44:00 | AQUA_M-M | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 8.9 |
| 8fb052a9-d1d7-30f9-aa56-8742aad62fa2 | -12.31116 | -45.60141 | 2025-10-17 05:44:00 | AQUA_M-M | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 10.8 |
| cb9037cc-0b75-3d19-9679-ce44814b333e | -7.32983 | -44.15546 | 2025-10-17 05:44:00 | AQUA_M-M | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 23.6 |
| 6744f480-9bba-36df-982a-e46de568d9be | -8.45435 | -44.17693 | 2025-10-17 05:44:00 | AQUA_M-M | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 31.4 |
| 27b87fd6-23ae-324d-a85d-0d148089cb78 | -12.16284 | -45.06181 | 2025-10-17 05:44:00 | AQUA_M-M | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 400ea78f-649a-35e7-bbe5-081ee8174b65 | -12.30966 | -45.61095 | 2025-10-17 05:44:00 | AQUA_M-M | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 4a94490e-ac04-392e-8387-c12ad9c44495 | -10.1404 | -44.57269 | 2025-10-17 05:44:00 | AQUA_M-M | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 9.1 |
| 43288b11-c589-3209-b25d-b1f0fb498a85 | -2.87044 | -50.74131 | 2025-10-17 05:44:00 | AQUA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 20.5 |
| 8dadc14a-cfeb-3c8c-b09c-f0f7b9842e69 | -6.42855 | -44.71494 | 2025-10-17 05:44:00 | AQUA_M-M | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 153.3 |
| d023cfd4-7a54-3105-b5ca-b511f177d951 | -7.4655 | -42.65166 | 2025-10-17 05:44:00 | AQUA_M-M | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 5.4 |
| 91f029f9-e782-3295-97c0-92278c9c259a | -6.42704 | -44.72462 | 2025-10-17 05:44:00 | AQUA_M-M | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 61.5 |
| ff7022dd-5ee0-3ef3-af1a-aea329edbf77 | -3.40775 | -43.62471 | 2025-10-17 05:44:00 | AQUA_M-M | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 51c7de6e-cba6-305c-bab1-15f8ede35630 | -8.19725 | -43.32035 | 2025-10-17 05:44:00 | AQUA_M-M | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 8.7 |
| f0442708-91f2-38e8-808b-43bb9160d21f | -7.27413 | -42.93486 | 2025-10-17 05:44:00 | AQUA_M-M | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 4.9 |
| 5ec4340d-b777-3a27-9f43-cec0ef1e17ec | -9.0857 | -48.02859 | 2025-10-17 05:44:00 | AQUA_M-M | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 35.7 |
| e4dd6d5b-fbff-3489-9e6e-7086397b6fcb | -6.4398 | -43.38292 | 2025-10-17 05:44:00 | AQUA_M-M | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 68e6b951-f62b-32f6-9220-1c6262829df7 | -6.31558 | -40.93474 | 2025-10-17 05:44:00 | AQUA_M-M | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 4.9 |
| c6debaa5-1c87-352c-837c-5163df89609a | -3.97742 | -42.49306 | 2025-10-17 05:44:00 | AQUA_M-M | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 11.4 |
| ac6f9161-5ba5-34db-b728-9536f723350f | -11.48519 | -44.18468 | 2025-10-17 05:44:00 | AQUA_M-M | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 542f0b16-97b4-3e8a-b1a2-73a689013a8f | -4.39282 | -43.40812 | 2025-10-17 05:44:00 | AQUA_M-M | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 8.0 |
| b2bab765-4d45-3a0b-b0b1-c9961844fbac | -5.8352 | -42.23918 | 2025-10-17 05:44:00 | AQUA_M-M | SÃO MIGUEL DA BAIXA GRANDE | PIAUÍ | Brasil | 2210383 | 22 | 33 | nan | nan | nan | Caatinga | 8.0 |
| 85382319-c755-389c-a8e8-84f68549e1fb | -10.13717 | -44.53472 | 2025-10-17 05:44:00 | AQUA_M-M | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 5.3 |
| e56f8b0a-a304-3b74-a90e-725f8c40834b | -7.2084 | -45.48998 | 2025-10-17 05:44:00 | AQUA_M-M | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 9.7 |
| e6e9243a-9852-3c9e-8ebf-8b9d001b3afa | -10.139 | -44.58178 | 2025-10-17 05:44:00 | AQUA_M-M | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 8.2 |
| 2936ff61-2a98-395a-b967-b6cae51875ff | -11.95212 | -45.35471 | 2025-10-17 05:44:00 | AQUA_M-M | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 4.6 |
| ff152a86-72f3-3d01-a4c2-f6837aef4e9a | -6.23015 | -44.15024 | 2025-10-17 05:44:00 | AQUA_M-M | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 8.8 |
| 6d764bc1-2607-3227-bbe3-41af83e50cfe | -10.81125 | -43.93155 | 2025-10-17 05:44:00 | AQUA_M-M | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 5.5 |
| c765ec9c-abcf-3c8d-bf2d-8ab99fb01a88 | -6.43778 | -44.71635 | 2025-10-17 05:44:00 | AQUA_M-M | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 194.2 |
| 10c77563-eca0-376d-a257-8585b8dd1180 | -6.32332 | -40.94559 | 2025-10-17 05:44:00 | AQUA_M-M | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 19.6 |
| 6c4f8b71-e314-3105-b599-14f4a85e6425 | -9.24941 | -44.35502 | 2025-10-17 05:44:00 | AQUA_M-M | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 4bfd12c2-c2ed-375f-bd42-03f9cdb983c2 | -11.35503 | -45.26546 | 2025-10-17 05:44:00 | AQUA_M-M | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 60537a39-db17-3a14-a1d8-890345904c86 | -7.95543 | -44.1103 | 2025-10-17 05:44:00 | AQUA_M-M | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 17.3 |
| f56c1c78-95e3-3bbd-a4e8-6b999c85c93f | -6.58868 | -47.06382 | 2025-10-17 05:44:00 | AQUA_M-M | SÃO JOÃO DO PARAÍSO | MARANHÃO | Brasil | 2111052 | 21 | 33 | nan | nan | nan | Cerrado | 16.5 |
| 343c777b-940f-3ff3-abb7-11a15025e95b | -5.8879 | -44.74649 | 2025-10-17 05:44:00 | AQUA_M-M | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 04f63c4a-4fed-3593-b28d-ba8cd2311bee | -12.16895 | -45.08145 | 2025-10-17 05:44:00 | AQUA_M-M | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 15.5 |
| 863f094c-35f6-3dba-a438-4a31d3796481 | -8.39818 | -46.23356 | 2025-10-17 05:44:00 | AQUA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 19.0 |
| 75854f75-dcc9-36bc-884f-13bd7c3f8f59 | -10.6191 | -42.305 | 2025-10-17 05:44:00 | AQUA_M-M | ITAGUAÇU DA BAHIA | BAHIA | Brasil | 2915353 | 29 | 33 | nan | nan | nan | Caatinga | 5.6 |
| 1aa32002-2bd5-37ff-b3dc-de69d6a71e54 | -10.53572 | -49.5409 | 2025-10-17 05:44:00 | AQUA_M-M | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 63.2 |
| 3eab8637-f22d-3b58-adff-88301a3ef468 | -12.17035 | -45.07236 | 2025-10-17 05:44:00 | AQUA_M-M | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 29.0 |


[Clique aqui para ver as próximas entradas](README114.md)
