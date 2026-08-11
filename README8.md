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

## Dados Diários - Página 8

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| efa54b19-7c64-3be0-95c5-351d228edf77 | -14.46816 | -45.68849 | 2026-08-11 03:49:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 8.6 |
| 24aeb06f-2834-3a53-8114-a56519fdb46d | -11.25659 | -44.89575 | 2026-08-11 03:49:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 3f7c9af4-6cf8-3d97-b341-0a4b71199ebb | -13.57038 | -46.28112 | 2026-08-11 03:49:00 | NOAA-20 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 20.2 |
| a335d711-22ae-30fd-8e94-e2f41bd24d2b | -12.49821 | -45.29239 | 2026-08-11 03:49:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 11.3 |
| 51405f41-3d42-3e86-aaf8-e059f76e331c | -14.4524 | -45.68974 | 2026-08-11 03:49:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 7438029e-281b-3f25-b3d5-52aeba833759 | -4.26854 | -48.18826 | 2026-08-11 03:49:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 13.4 |
| 2d3441a6-c670-310b-83b6-1b7000f182e2 | -12.47922 | -45.30993 | 2026-08-11 03:49:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 2782474c-f334-3c8c-866d-f47940a41b0a | -14.2824 | -45.30654 | 2026-08-11 03:49:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 7b28c3e7-feb2-3b4d-a5ae-dffde4aa1380 | -14.63804 | -47.66743 | 2026-08-11 03:49:00 | NOAA-20 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 1e5b4922-33cc-33df-9204-f0fdcfc3d4e4 | -14.27268 | -45.3045 | 2026-08-11 03:49:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| bc9778ba-c1ca-3498-a243-fe0895010dcd | -18.02127 | -44.43495 | 2026-08-11 03:49:00 | NOAA-20 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 75d4da6e-ae99-3064-869b-4edbf544da54 | -14.27649 | -45.31111 | 2026-08-11 03:49:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 3eb16931-4c1e-3c88-a052-67a6ddce63df | -11.32387 | -45.22606 | 2026-08-11 03:49:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| c05c81a7-edb9-3aa1-8ffe-94534ff482c8 | -12.47235 | -45.3459 | 2026-08-11 03:49:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 94f4eefc-2223-3d37-a6bb-c18edaef70b6 | -17.99827 | -44.36837 | 2026-08-11 03:49:00 | NOAA-20 | BUENÓPOLIS | MINAS GERAIS | Brasil | 3109204 | 31 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 2095869a-6e9e-3eae-baab-c05e5c79d421 | -17.56932 | -47.50311 | 2026-08-11 03:49:00 | NOAA-20 | CATALÃO | GOIÁS | Brasil | 5205109 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| ed3308a6-cb01-356c-9440-f1aae2819ada | -13.57105 | -46.27776 | 2026-08-11 03:49:00 | NOAA-20 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 24.8 |
| 0da01562-1098-35e5-a343-1be564a320d8 | -11.02184 | -45.65219 | 2026-08-11 03:49:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 1ed246d0-7706-3428-82ae-c9e24807baa2 | -14.12217 | -45.63298 | 2026-08-11 03:49:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 80953fc0-80eb-32db-ad6b-790be4e9c016 | -12.46512 | -45.32897 | 2026-08-11 03:49:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a9fbeaf1-f3c0-36b9-94a9-aa99172fd108 | -18.0286 | -44.39608 | 2026-08-11 03:49:00 | NOAA-20 | AUGUSTO DE LIMA | MINAS GERAIS | Brasil | 3104809 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| c32b7b30-5c52-37b9-ae2c-9f1e9298358f | -12.46397 | -45.33495 | 2026-08-11 03:49:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 2dd989e7-7949-37d7-b5e4-267b036c2f31 | -11.47988 | -46.62059 | 2026-08-11 03:49:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 02a94f17-9e11-37da-8eb6-0a4e43609011 | -16.55061 | -43.70192 | 2026-08-11 03:49:00 | NOAA-20 | FRANCISCO SÁ | MINAS GERAIS | Brasil | 3126703 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ed07f5c4-480f-310b-87bf-f305a6063b38 | -18.00402 | -44.40826 | 2026-08-11 03:49:00 | NOAA-20 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 0.2 |
| 3a7db2ac-e6b0-3b78-90d0-e99d000c9d10 | -4.26166 | -48.18692 | 2026-08-11 03:49:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 25.0 |
| 70001ed8-9ee6-375e-976c-f713423c6099 | -18.0221 | -44.43058 | 2026-08-11 03:49:00 | NOAA-20 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 420fb5a1-a2de-3957-9fce-26e514dc51b5 | -10.41949 | -46.64076 | 2026-08-11 03:49:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 10929633-0adf-3f2a-b397-0d4a19deb3e1 | -14.634 | -47.65845 | 2026-08-11 03:49:00 | NOAA-20 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 9935d975-1f09-3281-b6bc-cb6d24d98c44 | -14.46673 | -45.69581 | 2026-08-11 03:49:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 83ef2ace-5eb2-3c87-a3f2-5d7ed67c54ba | -13.05564 | -43.06663 | 2026-08-11 03:49:00 | NOAA-20 | PARATINGA | BAHIA | Brasil | 2923704 | 29 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 02dfdd36-44c9-3fd7-bb89-578264c74c03 | -14.27754 | -45.30552 | 2026-08-11 03:49:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 16f4e9fd-c78a-3f8d-9e6d-e16fc275c8ae | -15.04484 | -46.56184 | 2026-08-11 03:49:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 91ebaa00-007b-3d76-8e6a-d506e5106d42 | -11.02245 | -45.649 | 2026-08-11 03:49:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| a0ddef4c-30a2-3ffe-a879-8aab15a8c113 | -15.01071 | -46.59628 | 2026-08-11 03:49:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 117e4ada-374d-3086-ad3d-95f2a8aec256 | -13.57497 | -46.28558 | 2026-08-11 03:49:00 | NOAA-20 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 9106eb10-b90c-3eca-94c3-933098189498 | -14.45823 | -45.68641 | 2026-08-11 03:49:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 7.5 |
| a2be482a-cb77-37bf-98ba-49a433a5eece | -12.47361 | -45.31194 | 2026-08-11 03:49:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 10.2 |
| 3184670b-ce8e-3527-9b0a-09251b62165a | -14.44829 | -45.68431 | 2026-08-11 03:49:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 8418213d-72f2-3b67-9546-ab629aa4f724 | -12.48368 | -45.31391 | 2026-08-11 03:49:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 4.7 |
| f153c954-fd5c-32e3-b986-d1c1f1c3225b | -14.47171 | -45.69685 | 2026-08-11 03:49:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| e62d8452-7c12-323d-b92e-e106977f980b | -14.2786 | -45.29994 | 2026-08-11 03:49:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 922bdd07-ac7d-3641-8233-5d2299a6e490 | -10.41198 | -46.68038 | 2026-08-11 03:49:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 75eb8874-6faa-3535-bed6-e1b46dcf7d32 | -10.41843 | -46.6464 | 2026-08-11 03:49:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 687f278d-6922-3a4f-aa3c-7f228ffcd2cf | -12.49432 | -45.28546 | 2026-08-11 03:49:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 25b3a275-2d6f-3250-b1ba-19e2dfb216fb | -15.0155 | -46.57271 | 2026-08-11 03:49:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 4b7b5344-7908-3476-b3d6-d5f8d647edf8 | -14.64679 | -47.65326 | 2026-08-11 03:49:00 | NOAA-20 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 3405a155-db10-31bf-a3e4-ff3c5d2f0d30 | -12.47132 | -45.32391 | 2026-08-11 03:49:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 102.0 |
| 3a9ae01b-8443-3a28-b132-52b79d51a347 | -13.56646 | -46.27337 | 2026-08-11 03:49:00 | NOAA-20 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 24.8 |
| b0df3998-a29c-39b3-813d-cc18e25236d3 | -14.6355 | -47.6511 | 2026-08-11 03:49:00 | NOAA-20 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ab690139-7b1f-3719-a4ff-d7974eb69542 | -4.45201 | -47.91844 | 2026-08-11 03:49:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 944fdd75-3d98-3d27-9654-823eadc86fa1 | -11.46604 | -44.5714 | 2026-08-11 03:49:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 0d6447f7-4b2b-392c-9e67-80992e555237 | -10.42724 | -46.67072 | 2026-08-11 03:49:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 6.0 |
| f4922ea4-1d7d-3557-82fa-fb2f0110ca4a | -14.11658 | -45.63507 | 2026-08-11 03:49:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 13.1 |
| 4fff2305-665a-365b-a7e8-5921dcfda525 | -14.99806 | -46.60494 | 2026-08-11 03:49:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| e3abd4c2-9d78-3ff7-b428-18aae86e9999 | -11.46678 | -46.65821 | 2026-08-11 03:49:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 369e40c0-b94c-31e6-8eef-1b6d42c50902 | -12.48429 | -45.28337 | 2026-08-11 03:49:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 21979818-c3dc-300d-87b6-b10e7087ebec | -13.56512 | -46.28008 | 2026-08-11 03:49:00 | NOAA-20 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 20.2 |
| b24f941f-259d-3b11-a8be-e3f4ff266a90 | -12.45444 | -45.33014 | 2026-08-11 03:49:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 3810d4bf-62d2-3335-8348-cecb50370cfc | -10.89091 | -50.37363 | 2026-08-11 03:49:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 3187e43d-ebf3-3401-88b1-39446c82302a | -10.42491 | -46.67459 | 2026-08-11 03:49:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 9.0 |
| 1ff6b707-c2a2-3942-b765-2bbf2b74edcb | -14.99892 | -46.60074 | 2026-08-11 03:49:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 04b01a13-fcf6-3a94-8d91-7c1ab8bdc8b6 | -14.46234 | -45.69184 | 2026-08-11 03:49:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 287fb34a-84ef-332a-bec4-4813d0e2a0eb | -11.01853 | -45.64077 | 2026-08-11 03:49:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 5f92dc36-083a-3cfe-8fb3-e47e2e947f4a | -11.31877 | -45.22506 | 2026-08-11 03:49:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| a3de706c-80b7-31f6-ac78-3aa352bd9cbd | -16.66003 | -43.63172 | 2026-08-11 03:49:00 | NOAA-20 | FRANCISCO SÁ | MINAS GERAIS | Brasil | 3126703 | 31 | 33 | nan | nan | nan | Cerrado | 17.9 |
| 9b39054c-2b23-38e0-ab10-e9d08014c8e2 | -12.48987 | -45.28146 | 2026-08-11 03:49:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 89cd5bc5-c338-37b3-8d70-ba6e75db026e | -13.56713 | -46.26999 | 2026-08-11 03:49:00 | NOAA-20 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 10.8 |
| 4d9fe1ea-d770-3707-9621-0ce3c0da41d3 | -13.6474 | -46.247 | 2026-08-11 03:49:00 | NOAA-20 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 9ef2bb8e-a5bb-30ee-b74b-9e2d4cc5fce2 | -10.42565 | -46.67879 | 2026-08-11 03:49:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 11.6 |
| 9e9f2021-19e3-34f1-a5cc-4db1fa69c2de | -14.46176 | -45.69476 | 2026-08-11 03:49:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 5.9 |
| cce07290-5f7c-36db-ba7e-f8cd3aea6560 | -11.47354 | -46.62341 | 2026-08-11 03:49:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 5c496a9c-44ea-3e40-898d-3f8e7ebbc85e | -13.56823 | -46.3196 | 2026-08-11 03:49:00 | NOAA-20 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 8bdb613e-1681-355a-a2e9-27e502cf22f7 | -14.99938 | -46.59939 | 2026-08-11 03:49:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 152936a7-265a-3456-8951-015ebaf3f584 | -11.02881 | -45.64432 | 2026-08-11 03:49:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| da2af745-4d8c-316b-9833-c5d453ea71d3 | -13.60774 | -46.31367 | 2026-08-11 03:49:00 | NOAA-20 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 365c6e7e-98fb-381b-b5bf-3ddfacd9540a | -13.56244 | -46.29356 | 2026-08-11 03:49:00 | NOAA-20 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 40372764-ed89-3313-a659-bdc4f5d0d54b | -15.01494 | -46.57545 | 2026-08-11 03:49:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 7821c96c-c336-3074-b2c3-d27fc1b74c86 | -15.0215 | -46.56991 | 2026-08-11 03:49:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| eb4253f3-ed32-34ec-bfe1-fcea2a37604a | -13.64605 | -46.25372 | 2026-08-11 03:49:00 | NOAA-20 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f8c8dc97-e565-3069-8acc-da3f702a2fbb | -6.12466 | -42.95221 | 2026-08-11 03:49:00 | NOAA-20 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 169e44b0-f39a-36b6-a42e-01e938311833 | -13.59266 | -46.25133 | 2026-08-11 03:49:00 | NOAA-20 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ff5d1a41-7b45-3cd1-b377-5723ab2e03e1 | -18.00055 | -44.4031 | 2026-08-11 03:49:00 | NOAA-20 | BUENÓPOLIS | MINAS GERAIS | Brasil | 3109204 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| a9247a21-65e9-32c7-9f45-598da6262d44 | -11.0282 | -45.64752 | 2026-08-11 03:49:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 4b24aeda-93ff-3c36-9f06-313e74015f77 | -12.11828 | -43.21976 | 2026-08-11 03:49:00 | NOAA-20 | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c225764e-34b0-3eaf-85bb-40cd014d72f0 | -15.75613 | -47.77521 | 2026-08-11 03:49:00 | NOAA-20 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 38a056cf-a50c-38f5-8fc5-08c464c65714 | -14.46559 | -45.70165 | 2026-08-11 03:49:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 4.3 |
| bf0de4b4-e7f7-36b7-81fd-7115d340322e | -15.43649 | -41.38076 | 2026-08-11 03:49:00 | NOAA-20 | CÂNDIDO SALES | BAHIA | Brasil | 2906709 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| e27bbdf4-8c04-378f-acbb-30c770668e94 | -14.99135 | -39.52524 | 2026-08-11 03:49:00 | NOAA-20 | ITAPÉ | BAHIA | Brasil | 2916203 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| a379ebd8-32eb-34ad-be7c-c342f65a10df | -14.62117 | -47.6638 | 2026-08-11 03:49:00 | NOAA-20 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 43b75934-da49-37cc-831b-d0447f8f2e83 | -12.47694 | -45.32188 | 2026-08-11 03:49:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 32.0 |
| 8e0bd916-4997-30a0-b799-38aef1c74443 | -15.03496 | -46.58395 | 2026-08-11 03:49:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| b83a4af1-43b7-322a-b8bc-f0e963e89f60 | -14.49728 | -49.29515 | 2026-08-11 03:49:00 | NOAA-20 | URUAÇU | GOIÁS | Brasil | 5221601 | 52 | 33 | nan | nan | nan | Cerrado | 5.6 |
| fc4ed77b-99e1-39fd-9b11-72bc0e3f19c0 | -15.00162 | -46.58745 | 2026-08-11 03:49:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 038aea1f-097e-3204-95b4-1315a55cf2f0 | -14.27576 | -45.30058 | 2026-08-11 03:49:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e288a0a4-525f-3dde-967b-a61229028406 | -18.00332 | -44.36525 | 2026-08-11 03:49:00 | NOAA-20 | BUENÓPOLIS | MINAS GERAIS | Brasil | 3109204 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 3b604c85-7ef6-3926-9e36-da80b539df64 | -13.51671 | -44.14275 | 2026-08-11 03:49:00 | NOAA-20 | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 47c200ad-4bf4-3c29-ac05-740c35db3586 | -12.47751 | -45.31889 | 2026-08-11 03:49:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 32.0 |
| 23fae117-b67c-32ca-b425-baed88aeaae0 | -15.52036 | -42.66331 | 2026-08-11 03:49:00 | NOAA-20 | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| 6daec463-4f8e-3652-925d-dec39daa3221 | -16.6594 | -43.6322 | 2026-08-11 03:49:00 | NOAA-20 | FRANCISCO SÁ | MINAS GERAIS | Brasil | 3126703 | 31 | 33 | nan | nan | nan | Cerrado | 12.4 |


[Clique aqui para ver as próximas entradas](README9.md)
