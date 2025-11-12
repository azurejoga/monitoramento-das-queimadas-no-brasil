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

## Dados Diários - Página 9

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 759e76c2-8583-3cbc-acc8-63c0d56d0401 | -15.45548 | -43.08519 | 2025-11-12 03:44:00 | NOAA-20 | PAI PEDRO | MINAS GERAIS | Brasil | 3146552 | 31 | 33 | nan | nan | nan | Caatinga | 0.3 |
| 3970e410-4c6f-34d7-931a-691d55a4832e | -16.83552 | -46.0837 | 2025-11-12 03:44:00 | NOAA-20 | BRASILÂNDIA DE MINAS | MINAS GERAIS | Brasil | 3108552 | 31 | 33 | nan | nan | nan | Cerrado | 4.4 |
| c934a3f9-1bfb-3c6d-b024-18b716ae0f4f | -14.39976 | -44.38394 | 2025-11-12 03:44:00 | NOAA-20 | MONTALVÂNIA | MINAS GERAIS | Brasil | 3142700 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 27fcc206-2d94-3dbc-b414-92548bc8e6ae | -10.18698 | -44.90125 | 2025-11-12 03:44:00 | NOAA-20 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 0.6 |
| e97d9fb4-da52-360d-be39-59f912b74312 | -16.83093 | -46.08353 | 2025-11-12 03:44:00 | NOAA-20 | BRASILÂNDIA DE MINAS | MINAS GERAIS | Brasil | 3108552 | 31 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 85571695-b4ad-372e-b2b8-8eb8b42f4f35 | -16.83059 | -46.08259 | 2025-11-12 03:44:00 | NOAA-20 | BRASILÂNDIA DE MINAS | MINAS GERAIS | Brasil | 3108552 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 79e98b4c-6920-3cf7-b1b8-b014e2ade6e7 | -10.32368 | -44.27208 | 2025-11-12 03:44:00 | NOAA-20 | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 86bf36d6-ee01-397a-b293-e4f4164ceed9 | -10.5937 | -44.89899 | 2025-11-12 03:44:00 | NOAA-20 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| dd0a7c11-64a0-3cca-b87c-4468ab3196bf | -10.55306 | -44.83315 | 2025-11-12 03:44:00 | NOAA-20 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 5.2 |
| a026587f-f67f-3778-83ad-b6f5094b5bf8 | -10.50358 | -44.94523 | 2025-11-12 03:44:00 | NOAA-20 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 8.5 |
| 0c435149-7595-3c1a-acde-56fe19217300 | -10.49726 | -44.95058 | 2025-11-12 03:44:00 | NOAA-20 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 7.6 |
| f61ba400-ce04-3390-83de-787d534b2e63 | -10.3277 | -44.27792 | 2025-11-12 03:44:00 | NOAA-20 | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 3.8 |
| ba509c64-87fb-3200-8bd9-6544e29e1d3a | -10.60005 | -44.89343 | 2025-11-12 03:44:00 | NOAA-20 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 9508c449-af15-3bfa-bd97-0debbce4344a | -10.55546 | -44.83627 | 2025-11-12 03:44:00 | NOAA-20 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 6acbe113-b196-32b9-b3d4-69eb4e2eda4f | -9.86153 | -47.87165 | 2025-11-12 03:44:00 | NOAA-20 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 8751cf57-0643-37ee-8a6a-49c6f3f7b48a | -10.4996 | -44.9379 | 2025-11-12 03:44:00 | NOAA-20 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 9e55e272-7c3a-3e0c-8c97-972144d3a403 | -14.40437 | -44.38496 | 2025-11-12 03:44:00 | NOAA-20 | MONTALVÂNIA | MINAS GERAIS | Brasil | 3142700 | 31 | 33 | nan | nan | nan | Cerrado | 8.4 |
| f31498e9-7e3b-356c-8aa4-6b77133ff3b6 | -11.00189 | -38.32618 | 2025-11-12 03:44:00 | NOAA-20 | RIBEIRA DO AMPARO | BAHIA | Brasil | 2926509 | 29 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 7930a68b-fbc9-3d9c-9a31-03c5112d5429 | -10.45584 | -44.972 | 2025-11-12 03:44:00 | NOAA-20 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 1400028b-f369-345b-add4-e91cbcb2140d | -10.5943 | -44.89577 | 2025-11-12 03:44:00 | NOAA-20 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 13cd6f80-9692-3d45-8bd5-8f4b82989d75 | -10.49385 | -44.94015 | 2025-11-12 03:44:00 | NOAA-20 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 6facf7e8-7568-39b6-9e13-8ab0fa6bdaf5 | -15.85109 | -43.34627 | 2025-11-12 03:44:00 | NOAA-20 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 7b0e66f8-ea09-305b-b6a2-419d0936508b | -14.00719 | -44.08315 | 2025-11-12 03:44:00 | NOAA-20 | FEIRA DA MATA | BAHIA | Brasil | 2910776 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 21ddf5c3-3663-3810-a392-8d1f0ad8a03b | -10.55036 | -44.83521 | 2025-11-12 03:44:00 | NOAA-20 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 98caf3fc-1b26-3258-bc4b-8e134f31795f | -14.40072 | -44.37888 | 2025-11-12 03:44:00 | NOAA-20 | MONTALVÂNIA | MINAS GERAIS | Brasil | 3142700 | 31 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 8418564d-1995-32f8-b704-913b41972341 | -20.45455 | -42.51213 | 2025-11-12 03:46:00 | NOAA-20 | SERICITA | MINAS GERAIS | Brasil | 3166303 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| ebb1390c-551f-3a61-8b04-52255370498c | -17.67323 | -46.76654 | 2025-11-12 03:46:00 | NOAA-20 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 91ccd96d-8628-3ee2-ae3b-e92df250e1a7 | -16.8806 | -51.65987 | 2025-11-12 03:46:00 | NOAA-20 | CAIAPÔNIA | GOIÁS | Brasil | 5204409 | 52 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 1e8d9824-5d23-3b86-a302-a09d431970e2 | -21.17163 | -48.6922 | 2025-11-12 03:46:00 | NOAA-20 | VISTA ALEGRE DO ALTO | SÃO PAULO | Brasil | 3556909 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 747f7326-99c2-3382-b2c1-b455efe640fb | -21.30253 | -48.55519 | 2025-11-12 03:46:00 | NOAA-20 | MONTE ALTO | SÃO PAULO | Brasil | 3531308 | 35 | 33 | nan | nan | nan | Cerrado | 3.3 |
| c3427d3e-9e5a-3270-a369-b009c6c0b7ea | -20.88469 | -50.10796 | 2025-11-12 03:46:00 | NOAA-20 | TURIÚBA | SÃO PAULO | Brasil | 3555208 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| 36479dc7-92a6-345f-811c-20a8eea2b6ae | -18.39867 | -47.11163 | 2025-11-12 03:46:00 | NOAA-20 | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 0.3 |
| 978aba55-9f47-30c3-b068-f2bbe5e41a2a | -17.62264 | -46.70248 | 2025-11-12 03:46:00 | NOAA-20 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| dd054064-e61c-3420-b910-9deffad237d4 | -20.51088 | -47.2665 | 2025-11-12 03:46:00 | NOAA-20 | FRANCA | SÃO PAULO | Brasil | 3516200 | 35 | 33 | nan | nan | nan | Cerrado | 1.8 |
| e68c4f49-2ff8-39fb-9b3b-e86555591b65 | -19.91605 | -46.09868 | 2025-11-12 03:46:00 | NOAA-20 | TAPIRAÍ | MINAS GERAIS | Brasil | 3168200 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 9706b98a-d85c-3251-9bb7-08300c70673e | -21.06333 | -47.25654 | 2025-11-12 03:46:00 | NOAA-20 | ALTINÓPOLIS | SÃO PAULO | Brasil | 3501004 | 35 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 5d4d72b2-33b6-3e16-9bab-1d5688523950 | -21.4154 | -48.65483 | 2025-11-12 03:46:00 | NOAA-20 | TAQUARITINGA | SÃO PAULO | Brasil | 3553708 | 35 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 3a4ea6ae-67af-3e3d-bab7-c5ff7e132f10 | -22.47231 | -49.14367 | 2025-11-12 03:46:00 | NOAA-20 | PIRATININGA | SÃO PAULO | Brasil | 3539400 | 35 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 5691d818-ff15-3450-a114-0c668518f73e | -22.47314 | -49.13993 | 2025-11-12 03:46:00 | NOAA-20 | PIRATININGA | SÃO PAULO | Brasil | 3539400 | 35 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 41b34730-50f5-3651-81ed-4b33ca248387 | -17.96205 | -44.93507 | 2025-11-12 03:46:00 | NOAA-20 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 0ed1ef69-30a9-3b2c-a8ec-a40c4208a6f9 | -21.41294 | -48.6517 | 2025-11-12 03:46:00 | NOAA-20 | TAQUARITINGA | SÃO PAULO | Brasil | 3553708 | 35 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 8decf74d-62db-34fa-9861-2f7c8c830af2 | -20.22424 | -50.91133 | 2025-11-12 03:46:00 | NOAA-20 | SANTA FÉ DO SUL | SÃO PAULO | Brasil | 3546603 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.0 |
| e05155d4-89b1-32de-b5eb-0ea62189a45d | -18.22275 | -44.20047 | 2025-11-12 03:46:00 | NOAA-20 | AUGUSTO DE LIMA | MINAS GERAIS | Brasil | 3104809 | 31 | 33 | nan | nan | nan | Cerrado | 5.6 |
| e1771e96-a1fc-3836-b71d-d2a92d671a9a | -20.22544 | -50.90615 | 2025-11-12 03:46:00 | NOAA-20 | TRÊS FRONTEIRAS | SÃO PAULO | Brasil | 3554904 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.0 |
| 41f47858-4abb-3bfb-99a1-4d3d1a79a698 | -17.6321 | -46.70798 | 2025-11-12 03:46:00 | NOAA-20 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 96cfad26-ed5a-3404-ba0c-4bdec340df1b | -22.36746 | -47.06643 | 2025-11-12 03:46:00 | NOAA-20 | MOGI MIRIM | SÃO PAULO | Brasil | 3530805 | 35 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 48bc7434-896d-3587-8110-1d56817e084c | -21.16865 | -48.69494 | 2025-11-12 03:46:00 | NOAA-20 | VISTA ALEGRE DO ALTO | SÃO PAULO | Brasil | 3556909 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| 0f5bc0a1-cae5-3b5b-a298-52a4e0d36424 | -18.2278 | -44.19725 | 2025-11-12 03:46:00 | NOAA-20 | AUGUSTO DE LIMA | MINAS GERAIS | Brasil | 3104809 | 31 | 33 | nan | nan | nan | Cerrado | 5.6 |
| aeb7ade8-9329-381d-8f5b-8b350610ec3c | -21.30776 | -48.55671 | 2025-11-12 03:46:00 | NOAA-20 | MONTE ALTO | SÃO PAULO | Brasil | 3531308 | 35 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 39d3ca15-2e12-30c9-ad20-02e60aa8599c | -21.17086 | -41.86555 | 2025-11-12 03:46:00 | NOAA-20 | ITAPERUNA | RIO DE JANEIRO | Brasil | 3302205 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 3b13b40a-8fcc-3920-95af-768030399906 | -21.30699 | -48.56029 | 2025-11-12 03:46:00 | NOAA-20 | MONTE ALTO | SÃO PAULO | Brasil | 3531308 | 35 | 33 | nan | nan | nan | Cerrado | 4.9 |
| c6928b6a-5a13-319f-a020-d0702804f414 | -20.456 | -42.51014 | 2025-11-12 03:46:00 | NOAA-20 | SERICITA | MINAS GERAIS | Brasil | 3166303 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 908c819e-f169-3155-99e2-57a5750c58c8 | -22.36858 | -47.06105 | 2025-11-12 03:46:00 | NOAA-20 | MOGI MIRIM | SÃO PAULO | Brasil | 3530805 | 35 | 33 | nan | nan | nan | Cerrado | 11.3 |
| d53efee3-b9b6-34db-a21d-a9ecbad42d6d | -23.59943 | -49.0155 | 2025-11-12 03:46:00 | NOAA-20 | ITAÍ | SÃO PAULO | Brasil | 3521804 | 35 | 33 | nan | nan | nan | Cerrado | 2.2 |
| c1cbc994-487b-319d-9359-67735e594f4c | -20.89051 | -50.10949 | 2025-11-12 03:46:00 | NOAA-20 | TURIÚBA | SÃO PAULO | Brasil | 3555208 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| 649ee2e3-05c8-318f-8545-2bc8ccaa1136 | -18.39358 | -47.11037 | 2025-11-12 03:46:00 | NOAA-20 | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 0.3 |
| 1553c41e-141c-3cf1-bf2d-b02fe3f68808 | -24.52688 | -48.11272 | 2025-11-12 03:46:00 | NOAA-20 | ELDORADO | SÃO PAULO | Brasil | 3514809 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 7eabc037-6347-314d-9f40-34ca3ec07c45 | -17.8838 | -43.99099 | 2025-11-12 03:46:00 | NOAA-20 | BUENÓPOLIS | MINAS GERAIS | Brasil | 3109204 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| cba22900-c66a-3303-ae39-c026549b7236 | -19.91709 | -46.09355 | 2025-11-12 03:46:00 | NOAA-20 | TAPIRAÍ | MINAS GERAIS | Brasil | 3168200 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 62ccd128-9aec-3d11-b674-ddcbd9e72b38 | -19.91917 | -46.08332 | 2025-11-12 03:46:00 | NOAA-20 | TAPIRAÍ | MINAS GERAIS | Brasil | 3168200 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| e1a0c01c-048c-3ad5-86e0-78ea4f82ab00 | -18.22355 | -44.19628 | 2025-11-12 03:46:00 | NOAA-20 | AUGUSTO DE LIMA | MINAS GERAIS | Brasil | 3104809 | 31 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 5b0de424-d349-3c16-ae97-22a397374a22 | -19.9124 | -46.09269 | 2025-11-12 03:46:00 | NOAA-20 | TAPIRAÍ | MINAS GERAIS | Brasil | 3168200 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 14880b5f-0324-320c-8a48-a29c51b88816 | -21.3033 | -48.55163 | 2025-11-12 03:46:00 | NOAA-20 | MONTE ALTO | SÃO PAULO | Brasil | 3531308 | 35 | 33 | nan | nan | nan | Cerrado | 3.3 |
| ac2ace7e-1eaf-3267-82bc-0357fbacaa19 | -21.20924 | -46.50158 | 2025-11-12 03:46:00 | NOAA-20 | JURUAIA | MINAS GERAIS | Brasil | 3136900 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 08aba90a-e1fc-3546-897c-1e096226b611 | -20.89151 | -50.10518 | 2025-11-12 03:46:00 | NOAA-20 | TURIÚBA | SÃO PAULO | Brasil | 3555208 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| 581e507e-6169-34bb-b45a-354374e4c693 | -23.59425 | -49.01418 | 2025-11-12 03:46:00 | NOAA-20 | ITAÍ | SÃO PAULO | Brasil | 3521804 | 35 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 04e93cf5-eb97-3c3d-a8d4-9c8771716fa5 | -23.5927 | -49.02113 | 2025-11-12 03:46:00 | NOAA-20 | ITAÍ | SÃO PAULO | Brasil | 3521804 | 35 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 6fac7450-7f40-3357-842f-5f8f531f2c53 | -18.227 | -44.20143 | 2025-11-12 03:46:00 | NOAA-20 | AUGUSTO DE LIMA | MINAS GERAIS | Brasil | 3104809 | 31 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 33bca102-9cb1-3567-9564-f74c8348b79a | -20.88569 | -50.10365 | 2025-11-12 03:46:00 | NOAA-20 | MONÇÕES | SÃO PAULO | Brasil | 3531001 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| 9e442d43-ceb4-3394-8c47-50f70ab9a25b | -17.88221 | -43.99347 | 2025-11-12 03:46:00 | NOAA-20 | BUENÓPOLIS | MINAS GERAIS | Brasil | 3109204 | 31 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 4794f464-5ba8-3d5f-97a7-75cac651e636 | -20.51118 | -47.2658 | 2025-11-12 03:46:00 | NOAA-20 | FRANCA | SÃO PAULO | Brasil | 3516200 | 35 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 9bbf585c-3690-3c7d-93a2-92ae13180a24 | -17.88302 | -43.9893 | 2025-11-12 03:46:00 | NOAA-20 | BUENÓPOLIS | MINAS GERAIS | Brasil | 3109204 | 31 | 33 | nan | nan | nan | Cerrado | 0.4 |
| ba57d77f-2a67-35ab-a303-164f7659872b | -20.22245 | -50.90854 | 2025-11-12 03:46:00 | NOAA-20 | SANTA FÉ DO SUL | SÃO PAULO | Brasil | 3546603 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.0 |
| 33996660-1e88-3430-8bd5-5ea72a87bd31 | -21.52386 | -42.27019 | 2025-11-12 03:46:00 | NOAA-20 | SANTO ANTÔNIO DE PÁDUA | RIO DE JANEIRO | Brasil | 3304706 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 75a95b6e-1957-344a-8aa2-8ad819646321 | -21.41618 | -48.65133 | 2025-11-12 03:46:00 | NOAA-20 | TAQUARITINGA | SÃO PAULO | Brasil | 3553708 | 35 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 4037e0dd-f3aa-3f6a-8e86-cb8a8b3ba543 | -19.92281 | -46.08937 | 2025-11-12 03:46:00 | NOAA-20 | TAPIRAÍ | MINAS GERAIS | Brasil | 3168200 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| d0384ad8-9cdc-3912-8efe-f73cbaf761da | -21.41821 | -48.65311 | 2025-11-12 03:46:00 | NOAA-20 | TAQUARITINGA | SÃO PAULO | Brasil | 3553708 | 35 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ac792d2f-c652-385c-a379-3745e5aa6a1d | -20.22857 | -50.91041 | 2025-11-12 03:46:00 | NOAA-20 | TRÊS FRONTEIRAS | SÃO PAULO | Brasil | 3554904 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.0 |
| 327aa914-a3ac-362a-872f-05428a851e74 | -21.30407 | -48.54808 | 2025-11-12 03:46:00 | NOAA-20 | MONTE ALTO | SÃO PAULO | Brasil | 3531308 | 35 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 2c906ecd-a411-383a-af0e-3faf74f5fe75 | -23.59347 | -49.01767 | 2025-11-12 03:46:00 | NOAA-20 | ITAÍ | SÃO PAULO | Brasil | 3521804 | 35 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 37851ddd-4268-3d67-b509-cb6f631072d2 | -21.1708 | -48.69589 | 2025-11-12 03:46:00 | NOAA-20 | VISTA ALEGRE DO ALTO | SÃO PAULO | Brasil | 3556909 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 541910fa-2751-3f57-b166-85e729d474a0 | -19.91814 | -46.08839 | 2025-11-12 03:46:00 | NOAA-20 | TAPIRAÍ | MINAS GERAIS | Brasil | 3168200 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 185ffabe-c9ab-3037-a17b-21bfaae30eff | -17.62705 | -46.7068 | 2025-11-12 03:46:00 | NOAA-20 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 3c0f71bf-61e3-3bfd-8d67-d86c09a5594e | -20.89251 | -50.10084 | 2025-11-12 03:46:00 | NOAA-20 | TURIÚBA | SÃO PAULO | Brasil | 3555208 | 35 | 33 | nan | nan | nan | Mata Atlântica | 5.4 |
| fce6fe00-c7fa-3e4a-9bad-c67ac4990d48 | -21.41218 | -48.65522 | 2025-11-12 03:46:00 | NOAA-20 | TAQUARITINGA | SÃO PAULO | Brasil | 3553708 | 35 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 40c07885-450a-396a-8e52-28849615c67e | -21.0642 | -47.25857 | 2025-11-12 03:46:00 | NOAA-20 | ALTINÓPOLIS | SÃO PAULO | Brasil | 3501004 | 35 | 33 | nan | nan | nan | Cerrado | 2.2 |
| c35195c8-f0ac-3adb-b410-fe7bed80ab19 | -17.6277 | -46.70365 | 2025-11-12 03:46:00 | NOAA-20 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| e57c6cf2-b74b-3be1-b5be-e08ac028684d | -21.41745 | -48.65667 | 2025-11-12 03:46:00 | NOAA-20 | TAQUARITINGA | SÃO PAULO | Brasil | 3553708 | 35 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 95724fe1-7376-394e-b8be-39cc402eae67 | -27.71519 | -50.06754 | 2025-11-12 03:49:00 | NOAA-20 | LAGES | SANTA CATARINA | Brasil | 4209300 | 42 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 78a8f207-b00a-3971-9b31-a3020cc84ee6 | -26.01791 | -51.65823 | 2025-11-12 03:49:00 | NOAA-20 | BITURUNA | PARANÁ | Brasil | 4102901 | 41 | 33 | nan | nan | nan | Mata Atlântica | 2.7 |
| 79699341-3451-3190-b2af-50ca08059a92 | -27.44511 | -48.44765 | 2025-11-12 03:49:00 | NOAA-20 | FLORIANÓPOLIS | SANTA CATARINA | Brasil | 4205407 | 42 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 6aa2b558-16fe-3c57-86c9-cbdd3f0f7ed9 | -4.9643 | -43.7182 | 2025-11-12 03:50:00 | GOES-19 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 135.2 |
| 8b97c91a-a3fd-353b-b220-ebffe5558b02 | -4.0976 | -48.0144 | 2025-11-12 03:50:00 | GOES-19 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 52.0 |
| 205c6526-b8c2-3b28-a392-472565a40256 | -4.9454 | -43.7425 | 2025-11-12 03:50:00 | GOES-19 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 41.2 |
| abfb0b5e-cc32-3cc3-9a6e-84806501944b | -4.1161 | -48.0136 | 2025-11-12 03:50:00 | GOES-19 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 42.2 |
| a7f94f83-7157-3029-85bd-7e273f00d488 | -4.9641 | -43.7413 | 2025-11-12 03:50:00 | GOES-19 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 70.9 |
| 0ae61007-3185-31f3-a951-0ba6b521aa73 | -4.9456 | -43.7194 | 2025-11-12 03:50:00 | GOES-19 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 77.8 |
| 5a00cbe4-ac9f-3d18-a89a-f6c31ab960e9 | -4.1161 | -48.0136 | 2025-11-12 04:00:00 | GOES-19 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 52.2 |
| 0ceabf7b-dcf5-363d-afc1-5a35f8a60d8c | -4.0976 | -48.0144 | 2025-11-12 04:00:00 | GOES-19 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 88.9 |
| 9f058a0c-a892-3a1f-8a2d-79050a53f32b | -4.0974 | -48.0361 | 2025-11-12 04:00:00 | GOES-19 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 39.3 |


[Clique aqui para ver as próximas entradas](README10.md)
