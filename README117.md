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

## Dados Diários - Página 117

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| b1f0010b-c56a-3ae2-b45f-b441a662f67f | -19.9289 | -46.91034 | 2024-10-02 04:51:00 | AQUA_M-M | TAPIRA | MINAS GERAIS | Brasil | 3168101 | 31 | 33 | nan | nan | nan | Cerrado | 23.0 |
| fbc7105b-1088-3ec5-b972-e302ae0e9e70 | -22.90109 | -45.09716 | 2024-10-02 04:51:00 | AQUA_M-M | GUARATINGUETÁ | SÃO PAULO | Brasil | 3518404 | 35 | 33 | nan | nan | nan | Mata Atlântica | 70.5 |
| abddc7b9-acdc-3a79-a875-1d142d68f2cb | -22.89329 | -45.08324 | 2024-10-02 04:51:00 | AQUA_M-M | GUARATINGUETÁ | SÃO PAULO | Brasil | 3518404 | 35 | 33 | nan | nan | nan | Mata Atlântica | 14.5 |
| 4e2ddd28-6939-317d-9b17-3c9937ad538f | -22.89116 | -45.09564 | 2024-10-02 04:51:00 | AQUA_M-M | GUARATINGUETÁ | SÃO PAULO | Brasil | 3518404 | 35 | 33 | nan | nan | nan | Mata Atlântica | 48.8 |
| 55169677-0961-3fb8-a431-86faecd48c12 | -22.77093 | -44.65518 | 2024-10-02 04:51:00 | AQUA_M-M | SÃO JOSÉ DO BARREIRO | SÃO PAULO | Brasil | 3549607 | 35 | 33 | nan | nan | nan | Mata Atlântica | 8.8 |
| 296eada0-3c0e-39f4-b014-766b315e4988 | -22.7613 | -44.65337 | 2024-10-02 04:51:00 | AQUA_M-M | SÃO JOSÉ DO BARREIRO | SÃO PAULO | Brasil | 3549607 | 35 | 33 | nan | nan | nan | Mata Atlântica | 6.9 |
| 8bb72661-247e-3f3b-b6c9-d3a29f2dd95a | -20.23663 | -56.51785 | 2024-10-02 04:51:00 | NOAA-21 | MIRANDA | MATO GROSSO DO SUL | Brasil | 5005608 | 50 | 33 | nan | nan | nan | Pantanal | 1.2 |
| a7a5fff4-9ff9-3ebc-a74a-4d04fc1581f5 | -20.38279 | -58.06715 | 2024-10-02 04:51:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.4 |
| 9f6bdf73-10dc-3be8-866b-7a97cc2df1a7 | -20.38196 | -58.07176 | 2024-10-02 04:51:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.4 |
| 10065756-e78b-321b-8adc-18bfcad4bbe0 | -19.58683 | -56.53207 | 2024-10-02 04:51:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 2.1 |
| 54a0d336-446f-3636-ac6b-4f30392be384 | -17.2091 | -56.16671 | 2024-10-02 04:51:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.1 |
| 248bc1d7-108b-33ab-b6fe-e441e336ac8d | -17.20767 | -56.15389 | 2024-10-02 04:51:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.5 |
| 902bd6dc-aa7d-3aa2-af58-aab44d648f38 | -17.20706 | -56.19989 | 2024-10-02 04:51:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.1 |
| 0893b118-3f24-31cc-b547-c7c190abb030 | -17.20698 | -56.15795 | 2024-10-02 04:51:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.8 |
| 4f9bd697-c211-3fb8-bfb3-ac741f95acee | -17.20629 | -56.16201 | 2024-10-02 04:51:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.8 |
| 190fc4e6-25a7-3301-8b28-072e31721f46 | -17.2056 | -56.16607 | 2024-10-02 04:51:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.1 |
| 8d69b900-fdc2-32f3-91b8-6a696ccf14e4 | -17.20418 | -56.15325 | 2024-10-02 04:51:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.6 |
| d70c3357-f977-37c3-a207-8344192ab527 | -17.20349 | -56.15731 | 2024-10-02 04:51:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 6.4 |
| d9460614-5184-3fbb-a9d1-b9c53810ce31 | -17.20214 | -56.18639 | 2024-10-02 04:51:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.6 |
| 872e3ede-370e-30d1-ac8b-5fc1842eed5d | -17.20003 | -56.17761 | 2024-10-02 04:51:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.5 |
| 9544b7bc-7eb2-3f7b-a3b4-368f2084cc61 | -17.2 | -56.15667 | 2024-10-02 04:51:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 6.4 |
| 5b1f8829-1fe4-35e5-9910-958597ba6434 | -17.19927 | -56.13981 | 2024-10-02 04:51:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.1 |
| 1710b98a-87ed-30d4-8c1c-c051c49b7516 | -17.19861 | -56.16479 | 2024-10-02 04:51:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.5 |
| 08ea20bf-11e0-3bf5-9d4f-2f0baece5251 | -17.19577 | -56.13917 | 2024-10-02 04:51:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.1 |
| fca348b7-5791-3710-8a70-8f08ecb605e7 | -22.83018 | -42.70441 | 2024-10-02 04:51:00 | NOAA-21 | TANGUÁ | RIO DE JANEIRO | Brasil | 3305752 | 33 | 33 | nan | nan | nan | Mata Atlântica | 3.0 |
| b9ff51e7-86f2-3379-873c-bc19ff7bf63b | -20.04811 | -55.96538 | 2024-10-02 04:51:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 8.5 |
| 4318fb76-8aa7-33f5-a41d-d73e3b92b5d1 | -20.04747 | -55.96923 | 2024-10-02 04:51:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 8.5 |
| c080693e-bfea-3168-89f1-b2ef8d0b178d | -20.04682 | -55.97309 | 2024-10-02 04:51:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 6.6 |
| 93d6956f-d264-3ade-85d4-a0d024f00bc7 | -20.04473 | -55.96475 | 2024-10-02 04:51:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 4.8 |
| 1855ce96-a2a8-34f3-8bb9-a0e7c4b21e68 | -20.04408 | -55.9686 | 2024-10-02 04:51:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 4.8 |
| b85f6e88-bb22-37c9-b085-ccbbcb175da8 | -19.65657 | -56.51101 | 2024-10-02 04:51:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 1.2 |
| 170e8817-edfb-3d53-9e09-7192521d8bed | -19.65651 | -56.46953 | 2024-10-02 04:51:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 4.1 |
| 3cd3e0c4-eab8-3dd2-a8fb-65be484c07bc | -19.65583 | -56.47354 | 2024-10-02 04:51:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 4.1 |
| bb8f2911-54b6-3b19-9b45-fc311e3be2d2 | -19.65237 | -56.47289 | 2024-10-02 04:51:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 16.0 |
| beaff36a-bba5-3ae6-b21c-0aefd64b6950 | -19.65169 | -56.47691 | 2024-10-02 04:51:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 2.4 |
| 86fe2a50-f061-3a31-b361-b1e768c50587 | -19.64965 | -56.50971 | 2024-10-02 04:51:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 2.2 |
| 01da6692-bce8-37eb-9317-8f2fad846bcc | -19.64347 | -56.56682 | 2024-10-02 04:51:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 1.7 |
| 276b82f0-fabf-33e4-abf6-c4ad9b9fee8a | -19.64 | -56.56617 | 2024-10-02 04:51:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 1.7 |
| 5a35e3cc-20d9-3923-98c9-2e98ab1b5364 | -19.58336 | -56.53141 | 2024-10-02 04:51:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 2.6 |
| 30eee733-9a97-3712-a1fb-6f3b694a8cc1 | -20.02988 | -55.96995 | 2024-10-02 04:51:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 2.8 |
| 58521a50-edca-342c-9452-2b2742035f41 | -20.02858 | -55.97766 | 2024-10-02 04:51:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 2.6 |
| 879460b6-89a3-3202-8675-cef36b29cf72 | -20.02584 | -55.97318 | 2024-10-02 04:51:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 2.8 |
| da6c2f8c-f939-33aa-9fa5-55e13898e45b | -20.02454 | -55.9809 | 2024-10-02 04:51:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 2.6 |
| 97345d89-21c1-3c99-8d74-2790eafbcb7c | -17.23082 | -56.18747 | 2024-10-02 04:51:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 11.4 |
| 610ab054-0345-3b6f-8f38-19d0982bfa60 | -17.23076 | -56.16648 | 2024-10-02 04:51:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.8 |
| 5bd0213a-9eb0-38a7-85b3-232568d7bf22 | -17.23013 | -56.19154 | 2024-10-02 04:51:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 11.4 |
| 012d4f8a-d02a-3f25-888a-787499b41e03 | -17.23007 | -56.17054 | 2024-10-02 04:51:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.0 |
| 67778e23-5c26-3e7a-8a62-af78d483c7f0 | -17.22732 | -56.18682 | 2024-10-02 04:51:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.0 |
| 64b15482-8e72-3cd7-980f-38651cecb7a6 | -17.22726 | -56.16584 | 2024-10-02 04:51:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.8 |
| b5ab22bf-3933-30f4-9b0d-e0251262bf26 | -17.22663 | -56.1909 | 2024-10-02 04:51:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.0 |
| a571b150-24cd-321b-8874-c2aa0f59e363 | -17.22658 | -56.16991 | 2024-10-02 04:51:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.0 |
| 4b227b64-66b3-376b-ae3a-25fb08b48883 | -17.18671 | -56.15004 | 2024-10-02 04:51:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.5 |
| 7b8b12f7-ee66-32d3-8ed2-20e1415a8889 | -20.01583 | -55.46193 | 2024-10-02 04:51:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 11e483b1-c20e-3346-839c-7a291e7a5cd3 | -20.01248 | -55.46131 | 2024-10-02 04:51:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 1245680d-39e2-3e9f-a6c6-f442250d10b7 | -20.01187 | -55.46504 | 2024-10-02 04:51:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c09bea33-7490-3e25-a117-358c1f3fd596 | -20.01125 | -55.46877 | 2024-10-02 04:51:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 0497c6d8-4351-3f6b-a801-962d2a3093f3 | -20.01064 | -55.4725 | 2024-10-02 04:51:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Cerrado | 2.6 |
| c0735572-bb4e-3405-b8eb-20cbc48539cb | -20.00852 | -55.46442 | 2024-10-02 04:51:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 862f95c5-2546-38b6-87f6-c32be0325928 | -20.00791 | -55.46815 | 2024-10-02 04:51:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c2fe40f5-6b6f-3391-9c17-5c10d5725190 | -20.00518 | -55.46381 | 2024-10-02 04:51:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 624da752-d0d4-358a-a0b8-47e8b631d124 | -20.00456 | -55.46754 | 2024-10-02 04:51:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 5fc32eae-32f3-3faa-a8cc-47aa3d3e6ce5 | -20.00183 | -55.46322 | 2024-10-02 04:51:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 0921612b-043c-3637-a899-de50efcfbdc2 | -20.00121 | -55.46695 | 2024-10-02 04:51:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Cerrado | 3.0 |
| dbb516c8-8ce7-3fd4-a543-d907e8140b7c | -20.0006 | -55.47069 | 2024-10-02 04:51:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 1171b927-226b-3d1e-a432-f3d9c4acf178 | -19.99785 | -55.46638 | 2024-10-02 04:51:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Cerrado | 2.3 |
| eda8110d-6a42-324e-9dd2-935b564a7354 | -19.99724 | -55.47012 | 2024-10-02 04:51:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 7a8a328f-076a-3c12-8d3a-e12109b953ad | -20.71869 | -46.9024 | 2024-10-02 04:51:00 | NOAA-21 | CÁSSIA | MINAS GERAIS | Brasil | 3115102 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 31595778-232b-30d0-9052-bf040af47e84 | -21.28017 | -47.33028 | 2024-10-02 04:51:00 | NOAA-21 | CAJURU | SÃO PAULO | Brasil | 3509403 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 669f6d5d-3901-34f9-8181-a45e500edd4a | -20.64148 | -48.75051 | 2024-10-02 04:51:00 | NOAA-21 | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| de938d01-c61f-3119-a758-6d023fe323b6 | -20.641 | -48.75448 | 2024-10-02 04:51:00 | NOAA-21 | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 86296740-f0a8-323c-920f-d153e563480e | -20.63758 | -48.75476 | 2024-10-02 04:51:00 | NOAA-21 | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| 71f17376-4187-3621-add4-573e2f9f89b3 | -20.95324 | -49.11113 | 2024-10-02 04:51:00 | NOAA-21 | TABAPUÃ | SÃO PAULO | Brasil | 3552601 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| 64df7663-fd4e-3f5c-9587-1ac3655cf5d1 | -20.94921 | -49.11049 | 2024-10-02 04:51:00 | NOAA-21 | TABAPUÃ | SÃO PAULO | Brasil | 3552601 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 85f58d20-a978-39ba-976e-a10e91d71262 | -20.94875 | -49.11422 | 2024-10-02 04:51:00 | NOAA-21 | TABAPUÃ | SÃO PAULO | Brasil | 3552601 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 265c484f-342c-3ac2-a120-c71b396651b5 | -20.94473 | -49.11361 | 2024-10-02 04:51:00 | NOAA-21 | TABAPUÃ | SÃO PAULO | Brasil | 3552601 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 20866696-c364-320a-bbb9-23c5a27a540a | -21.58888 | -50.79519 | 2024-10-02 04:51:00 | NOAA-21 | OSVALDO CRUZ | SÃO PAULO | Brasil | 3534609 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 773f1bf3-b346-334a-be88-70276893be2e | -20.79979 | -51.61506 | 2024-10-02 04:51:00 | NOAA-21 | CASTILHO | SÃO PAULO | Brasil | 3511003 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 4520a1e6-e536-328e-bd32-688af8651e6a | -20.79979 | -51.61253 | 2024-10-02 04:51:00 | NOAA-21 | CASTILHO | SÃO PAULO | Brasil | 3511003 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| cdb49270-8783-3880-9dbd-d409deb0feeb | -20.76696 | -51.59021 | 2024-10-02 04:51:00 | NOAA-21 | CASTILHO | SÃO PAULO | Brasil | 3511003 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| af9bb3de-59d5-3d35-ad01-ed5f17e10e40 | -20.74639 | -51.65963 | 2024-10-02 04:51:00 | NOAA-21 | TRÊS LAGOAS | MATO GROSSO DO SUL | Brasil | 5008305 | 50 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| a2c053a9-7e65-31cf-adca-69fa709f7729 | -22.93622 | -43.73584 | 2024-10-02 04:51:00 | NOAA-21 | RIO DE JANEIRO | RIO DE JANEIRO | Brasil | 3304557 | 33 | 33 | nan | nan | nan | Mata Atlântica | 4.7 |
| 23920170-ffa1-3f61-9327-cb8d2d471074 | -22.93116 | -43.72633 | 2024-10-02 04:51:00 | NOAA-21 | RIO DE JANEIRO | RIO DE JANEIRO | Brasil | 3304557 | 33 | 33 | nan | nan | nan | Mata Atlântica | 5.8 |
| 114abc04-0450-3ced-89c9-9d9fa0ed706d | -22.93077 | -43.73075 | 2024-10-02 04:51:00 | NOAA-21 | RIO DE JANEIRO | RIO DE JANEIRO | Brasil | 3304557 | 33 | 33 | nan | nan | nan | Mata Atlântica | 7.0 |
| 03aba73e-3a80-386f-a3bd-45669ce8a4d3 | -22.9304 | -43.73518 | 2024-10-02 04:51:00 | NOAA-21 | RIO DE JANEIRO | RIO DE JANEIRO | Brasil | 3304557 | 33 | 33 | nan | nan | nan | Mata Atlântica | 7.0 |
| c659d1f1-f485-3113-9ed9-773141e1709e | -22.92533 | -43.72568 | 2024-10-02 04:51:00 | NOAA-21 | RIO DE JANEIRO | RIO DE JANEIRO | Brasil | 3304557 | 33 | 33 | nan | nan | nan | Mata Atlântica | 5.8 |
| 467ef76b-adc4-3535-b3dc-b347f120d307 | -23.11824 | -46.26362 | 2024-10-02 04:51:00 | NOAA-21 | NAZARÉ PAULISTA | SÃO PAULO | Brasil | 3532405 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.9 |
| cc1c9bdf-ac70-39e9-a8f3-b99b83a0f48a | -22.77852 | -43.79476 | 2024-10-02 04:51:00 | NOAA-21 | SEROPÉDICA | RIO DE JANEIRO | Brasil | 3305554 | 33 | 33 | nan | nan | nan | Mata Atlântica | 2.8 |
| 149c3bae-3bef-3074-9ea3-1986d0aefa8a | -22.7781 | -43.79976 | 2024-10-02 04:51:00 | NOAA-21 | ITAGUAÍ | RIO DE JANEIRO | Brasil | 3302007 | 33 | 33 | nan | nan | nan | Mata Atlântica | 3.4 |
| 9135ae05-b8e9-305f-9f7a-18bee4847eb7 | -22.77254 | -43.79631 | 2024-10-02 04:51:00 | NOAA-21 | SEROPÉDICA | RIO DE JANEIRO | Brasil | 3305554 | 33 | 33 | nan | nan | nan | Mata Atlântica | 5.9 |
| 97a87201-26df-3f0c-a4eb-9e4bf65da80f | -22.77215 | -43.79769 | 2024-10-02 04:51:00 | NOAA-21 | ITAGUAÍ | RIO DE JANEIRO | Brasil | 3302007 | 33 | 33 | nan | nan | nan | Mata Atlântica | 6.4 |
| a63e8260-805d-3828-acde-477c512bfb60 | -22.77209 | -43.80176 | 2024-10-02 04:51:00 | NOAA-21 | ITAGUAÍ | RIO DE JANEIRO | Brasil | 3302007 | 33 | 33 | nan | nan | nan | Mata Atlântica | 5.3 |
| 26ddf51a-8bdb-302b-855c-a96ea9e1b385 | -22.77163 | -43.80337 | 2024-10-02 04:51:00 | NOAA-21 | ITAGUAÍ | RIO DE JANEIRO | Brasil | 3302007 | 33 | 33 | nan | nan | nan | Mata Atlântica | 4.2 |
| b0af3f05-f90d-3d80-b77d-994d004db7d4 | -22.67465 | -43.70598 | 2024-10-02 04:51:00 | NOAA-21 | SEROPÉDICA | RIO DE JANEIRO | Brasil | 3305554 | 33 | 33 | nan | nan | nan | Mata Atlântica | 4.8 |
| d44dbefa-6d11-3218-806a-47a6c5fa118f | -22.67457 | -43.70618 | 2024-10-02 04:51:00 | NOAA-21 | SEROPÉDICA | RIO DE JANEIRO | Brasil | 3305554 | 33 | 33 | nan | nan | nan | Mata Atlântica | 4.7 |
| 5a9057a8-a455-3689-87ba-a4aafcc88112 | -22.66919 | -43.70137 | 2024-10-02 04:51:00 | NOAA-21 | SEROPÉDICA | RIO DE JANEIRO | Brasil | 3305554 | 33 | 33 | nan | nan | nan | Mata Atlântica | 8.5 |
| 03f5a602-0d12-3215-a389-274a07e7fe7d | -22.66908 | -43.70152 | 2024-10-02 04:51:00 | NOAA-21 | SEROPÉDICA | RIO DE JANEIRO | Brasil | 3305554 | 33 | 33 | nan | nan | nan | Mata Atlântica | 4.7 |
| 31fe083e-8b45-3084-90d4-69bc1bd90bd3 | -22.66885 | -43.70513 | 2024-10-02 04:51:00 | NOAA-21 | SEROPÉDICA | RIO DE JANEIRO | Brasil | 3305554 | 33 | 33 | nan | nan | nan | Mata Atlântica | 4.8 |
| 174be759-3c9f-39d4-9d73-edb46a0fe0e9 | -22.775 | -44.23462 | 2024-10-02 04:51:00 | NOAA-21 | RIO CLARO | RIO DE JANEIRO | Brasil | 3304409 | 33 | 33 | nan | nan | nan | Mata Atlântica | 11.8 |
| c6a1b5d3-e15c-3c53-b48b-1da075b5d217 | -22.77448 | -44.24047 | 2024-10-02 04:51:00 | NOAA-21 | RIO CLARO | RIO DE JANEIRO | Brasil | 3304409 | 33 | 33 | nan | nan | nan | Mata Atlântica | 23.4 |
| 8be92d38-0696-3d6a-84af-76c5a68bc2c7 | -20.69761 | -41.97871 | 2024-10-02 04:51:00 | NOAA-21 | CARANGOLA | MINAS GERAIS | Brasil | 3113305 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.7 |


[Clique aqui para ver as próximas entradas](README118.md)
