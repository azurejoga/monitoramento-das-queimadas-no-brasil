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

## Dados Diários - Página 41

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| c1fd3c91-3a14-3cad-ac17-26654bee4bf6 | -9.22531 | -36.7902 | 2024-12-10 12:21:00 | TERRA_M-T | BOM CONSELHO | PERNAMBUCO | Brasil | 2602100 | 26 | 33 | nan | nan | nan | Caatinga | 39.7 |
| d161fce0-d695-3fcf-924e-c0f6e08c5a67 | -8.37686 | -39.66411 | 2024-12-10 12:21:00 | TERRA_M-T | OROCÓ | PERNAMBUCO | Brasil | 2609808 | 26 | 33 | nan | nan | nan | Caatinga | 9.5 |
| f9e22623-d18b-347b-80f4-09f1e257ab07 | -8.37584 | -36.87139 | 2024-12-10 12:21:00 | TERRA_M-T | PESQUEIRA | PERNAMBUCO | Brasil | 2610905 | 26 | 33 | nan | nan | nan | Caatinga | 33.9 |
| e3710ca1-d26a-3142-bc2f-1e1b5c7cbf1f | -5.18917 | -39.34174 | 2024-12-10 12:21:00 | TERRA_M-T | QUIXERAMOBIM | CEARÁ | Brasil | 2311405 | 23 | 33 | nan | nan | nan | Caatinga | 28.7 |
| d4a2dda8-50a9-32b7-83aa-02caa8b55037 | -5.00469 | -39.99217 | 2024-12-10 12:21:00 | TERRA_M-T | MONSENHOR TABOSA | CEARÁ | Brasil | 2308609 | 23 | 33 | nan | nan | nan | Caatinga | 15.4 |
| 1c6e559e-d8e4-38fc-9e26-2e023abfa9bb | -9.6491 | -37.06149 | 2024-12-10 12:21:00 | TERRA_M-T | JARAMATAIA | ALAGOAS | Brasil | 2703700 | 27 | 33 | nan | nan | nan | Caatinga | 16.1 |
| f5a637d4-944f-389a-a51e-73b47600ca0b | -5.58184 | -35.34998 | 2024-12-10 12:21:00 | TERRA_M-T | CEARÁ-MIRIM | RIO GRANDE DO NORTE | Brasil | 2402600 | 24 | 33 | nan | nan | nan | Mata Atlântica | 20.3 |
| c6791e90-7025-3b32-8e91-b45e04bd79e1 | -6.2956 | -43.83358 | 2024-12-10 12:21:00 | TERRA_M-T | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 9.3 |
| f1f8deda-b854-3773-a9f3-e329acfe190c | -8.28992 | -41.20073 | 2024-12-10 12:21:00 | TERRA_M-T | PAULISTANA | PIAUÍ | Brasil | 2207801 | 22 | 33 | nan | nan | nan | Caatinga | 8.5 |
| 1d9ab02e-b618-341d-b0c9-c07cc34a5960 | -8.64262 | -40.85519 | 2024-12-10 12:21:00 | TERRA_M-T | AFRÂNIO | PERNAMBUCO | Brasil | 2600203 | 26 | 33 | nan | nan | nan | Caatinga | 18.2 |
| 50852618-b8cb-35db-bee1-f545ca42eab5 | -6.28968 | -42.17215 | 2024-12-10 12:21:00 | TERRA_M-T | ELESBÃO VELOSO | PIAUÍ | Brasil | 2203503 | 22 | 33 | nan | nan | nan | Caatinga | 9.1 |
| 88cfd27b-bc07-3c35-b74a-1b907e6adbe1 | -11.02397 | -40.34219 | 2024-12-10 12:21:00 | TERRA_M-T | CALDEIRÃO GRANDE | BAHIA | Brasil | 2905503 | 29 | 33 | nan | nan | nan | Caatinga | 16.0 |
| 05cf0f5e-c4d3-3d4e-a88c-67085b442a90 | -10.78732 | -42.76945 | 2024-12-10 12:21:00 | TERRA_M-T | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 10.9 |
| 45c6c6f7-4fd5-3dff-9ac4-a88731bad141 | -8.37842 | -39.65285 | 2024-12-10 12:21:00 | TERRA_M-T | OROCÓ | PERNAMBUCO | Brasil | 2609808 | 26 | 33 | nan | nan | nan | Caatinga | 16.3 |
| 0aed845b-fb6b-30ca-984d-c31cf59220d9 | -8.98064 | -41.00608 | 2024-12-10 12:21:00 | TERRA_M-T | CASA NOVA | BAHIA | Brasil | 2907202 | 29 | 33 | nan | nan | nan | Caatinga | 7.7 |
| 70295a58-5749-3731-bba3-d3c88eb46e28 | -11.75258 | -43.04975 | 2024-12-10 12:21:00 | TERRA_M-T | MORPARÁ | BAHIA | Brasil | 2921609 | 29 | 33 | nan | nan | nan | Caatinga | 10.8 |
| f38cf27c-6533-3b4b-9abc-130002ed6081 | -8.37339 | -36.89003 | 2024-12-10 12:21:00 | TERRA_M-T | PESQUEIRA | PERNAMBUCO | Brasil | 2610905 | 26 | 33 | nan | nan | nan | Caatinga | 37.8 |
| 30f91154-8410-3fb8-87d3-77141de595f9 | -9.22397 | -36.78373 | 2024-12-10 12:21:00 | TERRA_M-T | BOM CONSELHO | PERNAMBUCO | Brasil | 2602100 | 26 | 33 | nan | nan | nan | Caatinga | 29.4 |
| 9ac762c4-a1f6-38e7-a93d-61e848f5226d | -5.45709 | -35.70732 | 2024-12-10 12:21:00 | TERRA_M-T | PUREZA | RIO GRANDE DO NORTE | Brasil | 2410405 | 24 | 33 | nan | nan | nan | Caatinga | 24.3 |
| 5ca7a6c2-7446-3605-8e6f-10f36df0d17e | -8.71982 | -35.52014 | 2024-12-10 12:21:00 | TERRA_M-T | ÁGUA PRETA | PERNAMBUCO | Brasil | 2600401 | 26 | 33 | nan | nan | nan | Mata Atlântica | 34.8 |
| 9a7d5d26-bdc4-3178-82f6-59a2356c7ae7 | -7.78677 | -41.88664 | 2024-12-10 12:21:00 | TERRA_M-T | SIMPLÍCIO MENDES | PIAUÍ | Brasil | 2210805 | 22 | 33 | nan | nan | nan | Caatinga | 12.2 |
| b9afa0bd-b230-3638-9412-8778932483e1 | -12.18675 | -40.50905 | 2024-12-10 12:21:00 | TERRA_M-T | RUY BARBOSA | BAHIA | Brasil | 2927200 | 29 | 33 | nan | nan | nan | Caatinga | 10.3 |
| a5a4d145-8d01-3290-89a0-6368fe2f3f80 | -6.51226 | -44.67405 | 2024-12-10 12:21:00 | TERRA_M-T | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 17.3 |
| 496a8a9e-d765-39cc-86f5-0e4a598a2480 | -6.29424 | -43.84289 | 2024-12-10 12:21:00 | TERRA_M-T | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 27.5 |
| 1fea3a06-51cf-3ec7-81d2-aa908778701a | -9.02044 | -35.70031 | 2024-12-10 12:21:00 | TERRA_M-T | COLÔNIA LEOPOLDINA | ALAGOAS | Brasil | 2702108 | 27 | 33 | nan | nan | nan | Mata Atlântica | 69.9 |
| 6f505d4d-efca-392c-b6c6-886f5d722d49 | -8.75718 | -40.89709 | 2024-12-10 12:21:00 | TERRA_M-T | AFRÂNIO | PERNAMBUCO | Brasil | 2600203 | 26 | 33 | nan | nan | nan | Caatinga | 10.2 |
| 5fffe513-dbe8-31a4-884a-bbd2ba837002 | -8.11046 | -38.17486 | 2024-12-10 12:21:00 | TERRA_M-T | SERRA TALHADA | PERNAMBUCO | Brasil | 2613909 | 26 | 33 | nan | nan | nan | Caatinga | 14.8 |
| 01e7de99-96d7-36be-9af2-f19867253bb2 | -6.63812 | -41.98746 | 2024-12-10 12:21:00 | TERRA_M-T | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 6.6 |
| 3ac6ebf6-c226-3d16-b486-899a8d54c82f | -18.67214 | -44.37013 | 2024-12-10 12:23:00 | TERRA_M-T | INIMUTABA | MINAS GERAIS | Brasil | 3131109 | 31 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 35e5923a-2948-31f7-b9c6-c4e05466e190 | -15.54674 | -43.13803 | 2024-12-10 12:23:00 | TERRA_M-T | PAI PEDRO | MINAS GERAIS | Brasil | 3146552 | 31 | 33 | nan | nan | nan | Caatinga | 7.2 |
| dff31d51-26d8-39aa-b29a-15de4f200f74 | -15.06708 | -44.12179 | 2024-12-10 12:23:00 | TERRA_M-T | ITACARAMBI | MINAS GERAIS | Brasil | 3132107 | 31 | 33 | nan | nan | nan | Cerrado | 14.4 |
| 2f9b2415-9ac2-3648-94dc-4bba94d226a5 | -12.86443 | -44.47674 | 2024-12-10 12:23:00 | TERRA_M-T | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 16.2 |
| 69c48384-8775-3e7f-924e-98dba0f36b81 | -14.34751 | -42.95216 | 2024-12-10 12:23:00 | TERRA_M-T | GUANAMBI | BAHIA | Brasil | 2911709 | 29 | 33 | nan | nan | nan | Caatinga | 8.7 |
| 9955b255-8b51-383e-9f92-dc9c015357e3 | -15.73223 | -46.10811 | 2024-12-10 12:23:00 | TERRA_M-T | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 30.0 |
| c9cffaa0-6b62-3378-a8bb-5026e593fd45 | -14.00912 | -42.80226 | 2024-12-10 12:23:00 | TERRA_M-T | IGAPORÃ | BAHIA | Brasil | 2913408 | 29 | 33 | nan | nan | nan | Caatinga | 11.7 |
| 50017a16-89ac-3bd3-a87b-a00294911a95 | -15.38168 | -39.84342 | 2024-12-10 12:23:00 | TERRA_M-T | ITAPETINGA | BAHIA | Brasil | 2916401 | 29 | 33 | nan | nan | nan | Mata Atlântica | 16.8 |
| b218aa0c-00cd-3f06-9cb1-ab5e593a75c1 | -12.26437 | -44.97949 | 2024-12-10 12:23:00 | TERRA_M-T | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 13.9 |
| b02e5f5a-e965-3288-a0f9-61c2531dce33 | -15.06839 | -44.11271 | 2024-12-10 12:23:00 | TERRA_M-T | ITACARAMBI | MINAS GERAIS | Brasil | 3132107 | 31 | 33 | nan | nan | nan | Cerrado | 6.5 |
| e2dc6d63-8e16-335c-a55a-e0916322cfb9 | -12.71927 | -43.25747 | 2024-12-10 12:23:00 | TERRA_M-T | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Cerrado | 6.1 |
| a84fbdc9-c700-3501-bd6c-84788c848055 | -13.2056 | -43.39625 | 2024-12-10 12:23:00 | TERRA_M-T | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Cerrado | 14.4 |
| 3113d205-9430-3f16-b263-f220c38fac85 | -17.61938 | -42.29578 | 2024-12-10 12:23:00 | TERRA_M-T | CAPELINHA | MINAS GERAIS | Brasil | 3112307 | 31 | 33 | nan | nan | nan | Mata Atlântica | 8.7 |
| bfb756e9-863c-3f40-b3c7-b4e175b2afca | -12.68253 | -42.86641 | 2024-12-10 12:23:00 | TERRA_M-T | BOQUIRA | BAHIA | Brasil | 2904100 | 29 | 33 | nan | nan | nan | Caatinga | 6.1 |
| 89611c9d-721a-3847-8292-b4ea302d62c8 | -12.86577 | -44.46762 | 2024-12-10 12:23:00 | TERRA_M-T | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 36.4 |
| fafac9c8-d830-3edf-b4de-39aa2653630b | -13.87774 | -45.24197 | 2024-12-10 12:23:00 | TERRA_M-T | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 11.0 |
| 74d2d83b-6e2f-31e2-b12c-1820fe71381f | -12.68381 | -42.85733 | 2024-12-10 12:23:00 | TERRA_M-T | BOQUIRA | BAHIA | Brasil | 2904100 | 29 | 33 | nan | nan | nan | Caatinga | 9.6 |
| 6d5a3b23-1f3e-3e5b-958a-2961a88b43b0 | -15.82209 | -42.53548 | 2024-12-10 12:23:00 | TERRA_M-T | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.9 |
| 66268626-7fe9-3a50-87d8-09c2dfc792f9 | -12.26295 | -44.98895 | 2024-12-10 12:23:00 | TERRA_M-T | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 47.7 |
| bbf5688a-1e3a-3a38-84c4-fdf20fa6758c | -12.68729 | -45.11382 | 2024-12-10 12:23:00 | TERRA_M-T | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 11.8 |
| 1191ff65-6405-3e4f-9092-2119068508d7 | -12.50637 | -44.27753 | 2024-12-10 12:23:00 | TERRA_M-T | TABOCAS DO BREJO VELHO | BAHIA | Brasil | 2930907 | 29 | 33 | nan | nan | nan | Cerrado | 19.3 |
| 59689b0f-69a2-390d-bcb4-980853b7bdb7 | -12.77576 | -44.58493 | 2024-12-10 12:23:00 | TERRA_M-T | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 11.1 |
| 532da2da-e880-3765-8dca-987c938590f7 | -8.1242 | -47.9843 | 2024-12-10 13:00:00 | GOES-16 | ITAPIRATINS | TOCANTINS | Brasil | 1710904 | 17 | 33 | nan | nan | nan | Cerrado | 141.5 |
| 2b5fdece-dfa9-3ee0-926d-05efd794338c | -9.1755 | -35.4943 | 2024-12-10 13:30:00 | GOES-16 | MATRIZ DE CAMARAGIBE | ALAGOAS | Brasil | 2705101 | 27 | 33 | nan | nan | nan | Mata Atlântica | 103.8 |
| e9edaa92-c753-3140-8493-6cb52ba08536 | -6.9088 | -47.8446 | 2024-12-10 13:40:00 | GOES-16 | WANDERLÂNDIA | TOCANTINS | Brasil | 1722081 | 17 | 33 | nan | nan | nan | Cerrado | 120.8 |
| 1f237adf-70a3-3e49-92b0-8413554d41fb | -9.1755 | -35.4943 | 2024-12-10 14:00:00 | GOES-16 | MATRIZ DE CAMARAGIBE | ALAGOAS | Brasil | 2705101 | 27 | 33 | nan | nan | nan | Mata Atlântica | 114.0 |


