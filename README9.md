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
| 62b559c6-835c-35b6-ad65-235a21dd3f88 | -4.00771 | -43.24244 | 2025-06-19 03:55:00 | NPP-375D | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| f1ccc21a-3e30-32ae-87b0-081c225c93eb | -7.28037 | -49.99743 | 2025-06-19 03:55:00 | NPP-375D | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| bd24c845-44d2-3872-9e0f-5963d68a3f45 | -6.00952 | -42.2453 | 2025-06-19 03:55:00 | NPP-375D | ELESBÃO VELOSO | PIAUÍ | Brasil | 2203503 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 2544f733-6847-3f5b-a037-b6e6925c5cf3 | -8.12516 | -46.08694 | 2025-06-19 03:55:00 | NPP-375D | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| ff8af3bb-f4f4-336f-8a1c-097f3ce321a0 | -3.77899 | -41.66629 | 2025-06-19 03:55:00 | NPP-375D | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| f1979865-3aed-33fb-9505-9d476c539840 | -4.7744 | -47.57188 | 2025-06-19 03:55:00 | NPP-375D | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 914820b1-ce96-308d-a126-e70dc2a5a06b | -7.2045 | -43.20785 | 2025-06-19 03:55:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 04dd9060-eb37-30b2-a5f0-dfebd36d3bb6 | -6.12487 | -42.53538 | 2025-06-19 03:55:00 | NPP-375D | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| a1d49ad0-9330-3a8f-8d6a-2b62818ef406 | -7.23324 | -43.10225 | 2025-06-19 03:55:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 3.4 |
| e33d4f5b-387a-37d1-a0f7-8babab0f70aa | -6.6611 | -42.49152 | 2025-06-19 03:55:00 | NPP-375D | ARRAIAL | PIAUÍ | Brasil | 2201002 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 93b38c9e-52be-39e5-8b75-f4767f2164f4 | -6.29525 | -44.2344 | 2025-06-19 03:55:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 45bd7859-8029-3d47-934a-22311b0a6eec | -6.69064 | -43.20681 | 2025-06-19 03:55:00 | NPP-375D | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 43796820-1a96-35fd-8772-c172d9dd4254 | -3.00554 | -46.72357 | 2025-06-19 03:55:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ffce790a-bedd-313c-af24-88388d0d8d65 | -7.27917 | -47.09916 | 2025-06-19 03:55:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 4c595ad1-6507-3ad6-9e28-7a658c16965c | -8.01148 | -46.78328 | 2025-06-19 03:55:00 | NPP-375D | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| a01e104d-0f1c-3e65-b1ed-69390aff04d2 | -5.77516 | -43.45414 | 2025-06-19 03:55:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e5dbc4cc-fb58-3a94-a896-60ea7aad86bb | -9.33157 | -37.98046 | 2025-06-19 03:55:00 | NPP-375D | ÁGUA BRANCA | ALAGOAS | Brasil | 2700102 | 27 | 33 | nan | nan | nan | Caatinga | 0.9 |
| e1948d2f-e8c0-3c06-b346-747ee3ae3deb | -7.2898 | -47.09862 | 2025-06-19 03:55:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 1e7a7f6c-bc24-303d-90d9-a1710db7e55d | -2.91455 | -48.23583 | 2025-06-19 03:55:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 1be8e52d-13ef-3c27-9b39-32be90b3bae9 | -7.14277 | -43.28599 | 2025-06-19 03:55:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 057b9de1-75c7-3435-be5f-fc8dd905170d | -6.67874 | -43.20473 | 2025-06-19 03:55:00 | NPP-375D | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 52a9979f-2e2b-319c-b8bb-352526996d8a | -6.29028 | -44.23771 | 2025-06-19 03:55:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 9589ed78-0c2c-35ef-905d-bbe6a4c25b5b | -6.67237 | -42.48551 | 2025-06-19 03:55:00 | NPP-375D | ARRAIAL | PIAUÍ | Brasil | 2201002 | 22 | 33 | nan | nan | nan | Caatinga | 8.7 |
| 4d6c630a-024f-3974-829d-05ba2be35811 | -8.12663 | -43.12868 | 2025-06-19 03:55:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 8.3 |
| 6e245590-fd7e-3f9e-b97e-6c83a269c1e6 | -6.29098 | -44.23362 | 2025-06-19 03:55:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 75353ade-a03b-3830-b7c9-4278905196ec | -7.28196 | -47.09764 | 2025-06-19 03:55:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 29411016-ef2f-3848-9550-9c58b2e3ae6c | -6.67389 | -43.20919 | 2025-06-19 03:55:00 | NPP-375D | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Caatinga | 3.5 |
| 6421e26c-1484-3f1b-b1b4-fd3fc6bd503e | -4.40925 | -47.65971 | 2025-06-19 03:55:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 7e09b8c2-5abb-36ee-ac46-68ccfd0d57c5 | -5.2914 | -44.71739 | 2025-06-19 03:55:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| ef66928c-e564-36c5-b03c-590786c0fcae | -5.77455 | -43.45775 | 2025-06-19 03:55:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 3957d904-68c0-38bd-b42c-bc135b3f124a | -3.00609 | -46.72025 | 2025-06-19 03:55:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 38a36722-36c7-3c07-b73d-af6dde108b26 | -6.6619 | -42.4866 | 2025-06-19 03:55:00 | NPP-375D | ARRAIAL | PIAUÍ | Brasil | 2201002 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 6c286ad3-d489-39a6-bfb7-b45d26553985 | -2.91734 | -48.23794 | 2025-06-19 03:55:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 9c401304-722d-3c74-95e0-7e6f132c497b | -6.68492 | -43.21643 | 2025-06-19 03:55:00 | NPP-375D | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Caatinga | 4.9 |
| 5926edfb-6930-3ed5-b4a6-87b066e33118 | -2.91386 | -48.24007 | 2025-06-19 03:55:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| cb68d4f8-4aa2-3bdd-873d-fa44b4b9c276 | -7.36494 | -47.04507 | 2025-06-19 03:55:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| d48832ba-c7ee-3630-a060-fc8be26fc434 | -7.23052 | -43.07377 | 2025-06-19 03:55:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 16547d6d-a314-3b12-842f-ff37c3fee9ea | -8.07803 | -43.11037 | 2025-06-19 03:55:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 4.5 |
| d56913f8-e2ed-38c3-9417-83f05d57b454 | -4.28154 | -48.18301 | 2025-06-19 03:55:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 32116927-8afe-3b2b-9928-706f07d30677 | -6.70281 | -43.25594 | 2025-06-19 03:55:00 | NPP-375D | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 72fa94ea-ddc6-341b-8b3a-e4b76cc60850 | -3.07916 | -40.07858 | 2025-06-19 03:55:00 | NPP-375D | ACARAÚ | CEARÁ | Brasil | 2300200 | 23 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 43a61fc1-080d-33be-8673-1b7e30a1a3c3 | -7.23966 | -43.08814 | 2025-06-19 03:55:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 5.2 |
| 5c2bfae0-b6f0-39aa-bcf0-73785b348db8 | -6.66859 | -42.48479 | 2025-06-19 03:55:00 | NPP-375D | ARRAIAL | PIAUÍ | Brasil | 2201002 | 22 | 33 | nan | nan | nan | Caatinga | 8.7 |
| 989b9a09-3d11-32dd-afde-6b6bb793b0a3 | -6.12795 | -42.54074 | 2025-06-19 03:55:00 | NPP-375D | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 0e348430-1ca5-3cdf-9309-576ddd7672ed | -7.20267 | -43.21011 | 2025-06-19 03:55:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 300c3fdc-6e22-3ac4-b693-060804acebc6 | -7.53827 | -43.80398 | 2025-06-19 03:55:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 819d4cc7-5c6b-3007-ae77-a2d64f53f70c | -3.31778 | -48.71973 | 2025-06-19 03:55:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6128861f-cb52-35be-95da-86f683df5e42 | -7.23744 | -43.07756 | 2025-06-19 03:55:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 14.9 |
| 61610345-6042-3ca3-b4b0-b0b604e0c40b | -7.23882 | -43.09308 | 2025-06-19 03:55:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 5.2 |
| 3780864b-6ec5-3062-bbe6-6fbed0db3232 | -8.12501 | -43.13826 | 2025-06-19 03:55:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 22.7 |
| 623ce3a0-08ee-351a-a0c6-31f937adf79a | -3.3246 | -48.71627 | 2025-06-19 03:55:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ec1f0177-e27d-3273-9969-882cefa892d7 | -7.21983 | -43.22844 | 2025-06-19 03:55:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| f2d5d9b4-ee92-39f1-a4cb-a361dfd9cd1b | -7.14673 | -43.28666 | 2025-06-19 03:55:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 6649fd10-0266-39a7-bd3f-30d5625a9cf4 | -7.23443 | -43.07442 | 2025-06-19 03:55:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| c37b3599-bd6a-3537-8f40-10a8640eadae | -4.83508 | -43.18421 | 2025-06-19 03:55:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 7a7b44a5-bdc7-3240-8bd9-0078dc31492c | -6.68889 | -43.21713 | 2025-06-19 03:55:00 | NPP-375D | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Caatinga | 4.9 |
| 8230919c-addf-3665-88b5-786793fc390e | -5.90905 | -43.44977 | 2025-06-19 03:55:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 1c439541-096f-3fcc-82e9-7577ec92466e | -6.15851 | -47.2715 | 2025-06-19 03:55:00 | NPP-375D | CAMPESTRE DO MARANHÃO | MARANHÃO | Brasil | 2102556 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 8c9f4c5a-9bb4-35bb-beac-824ed49cb8f2 | -6.67477 | -43.20404 | 2025-06-19 03:55:00 | NPP-375D | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Caatinga | 3.5 |
| e00ad512-8512-31d5-bb75-2aa46c3b7871 | -4.77499 | -47.56845 | 2025-06-19 03:55:00 | NPP-375D | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 2c931ea7-496d-3a88-bdfc-5fc35b82bb15 | -6.67019 | -42.47533 | 2025-06-19 03:55:00 | NPP-375D | CAJAZEIRAS DO PIAUÍ | PIAUÍ | Brasil | 2202075 | 22 | 33 | nan | nan | nan | Caatinga | 3.2 |
| 73141354-1105-31d6-96bc-0f1c5bf0966d | -7.23353 | -43.07692 | 2025-06-19 03:55:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 14.9 |
| 96dc1a70-7729-3c11-a42f-579d78357a4f | -7.54147 | -43.80382 | 2025-06-19 03:55:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 2ae30965-fc1d-36ac-950d-85221917443f | -6.84251 | -42.80595 | 2025-06-19 03:55:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| c82afd04-0eab-3168-8415-6c45357bcaea | -4.41055 | -47.6603 | 2025-06-19 03:55:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 591d0cd9-5c4d-3eb3-823d-ff984d790b0e | -7.23362 | -43.07939 | 2025-06-19 03:55:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 10.7 |
| f17c3db3-bd31-36e7-820b-2467ba5cf706 | -5.90844 | -43.45343 | 2025-06-19 03:55:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ed2f8887-3709-371a-b37b-166dc3797746 | -8.12969 | -43.13416 | 2025-06-19 03:55:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 5342c4fb-9285-3bee-833d-631aa9dbaa20 | -6.15907 | -47.26826 | 2025-06-19 03:55:00 | NPP-375D | CAMPESTRE DO MARANHÃO | MARANHÃO | Brasil | 2102556 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| bbbb3d1e-11be-3f84-bc39-421a1cccc0d9 | -7.23281 | -43.08435 | 2025-06-19 03:55:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 10.7 |
| 3add5a67-0895-323a-8d17-aa18af8d4b03 | -7.16256 | -43.21629 | 2025-06-19 03:55:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 05f0cd5c-b8a7-3177-bee1-69bc240a2ac1 | -3.77896 | -41.66378 | 2025-06-19 03:55:00 | NPP-375D | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| da50acc3-3564-3104-8a9e-5f0e4060b3c5 | -6.67786 | -43.2099 | 2025-06-19 03:55:00 | NPP-375D | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 709dd2bb-2c73-3efb-98fa-29dd8a2e8860 | -4.83916 | -43.18488 | 2025-06-19 03:55:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 4bc3a1b2-d053-3115-9932-fce3b77c097f | -4.54889 | -48.00755 | 2025-06-19 03:55:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 7a85b6a2-eae9-3f9a-a79a-44ef96eebb86 | -6.65807 | -42.48616 | 2025-06-19 03:55:00 | NPP-375D | ARRAIAL | PIAUÍ | Brasil | 2201002 | 22 | 33 | nan | nan | nan | Caatinga | 4.4 |
| 5e896651-e936-3ea7-aae2-ab0769cb9d4f | -5.13454 | -37.84913 | 2025-06-19 03:55:00 | NPP-375D | QUIXERÉ | CEARÁ | Brasil | 2311504 | 23 | 33 | nan | nan | nan | Caatinga | 2.9 |
| e66604ea-02ea-3e8a-b3ee-f43d7af7b733 | -6.34259 | -43.74674 | 2025-06-19 03:55:00 | NPP-375D | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| ad49c93c-8413-3fe7-855c-a49fc050be30 | -6.67029 | -42.48303 | 2025-06-19 03:55:00 | NPP-375D | ARRAIAL | PIAUÍ | Brasil | 2201002 | 22 | 33 | nan | nan | nan | Caatinga | 17.5 |
| 9e6454e4-3275-3033-8b2f-891de604682b | -7.28018 | -47.09332 | 2025-06-19 03:55:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 52e5024d-033a-3dd5-985e-f119cb589053 | -4.83977 | -43.1813 | 2025-06-19 03:55:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| f412d322-0eaa-35f5-bbf9-c054b48cc6a5 | -5.91313 | -43.45047 | 2025-06-19 03:55:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 76d6b943-7548-30ad-af86-84abd20a0578 | -2.73562 | -47.33544 | 2025-06-19 03:55:00 | NPP-375D | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 7560119a-87cc-3afd-9b39-9f640fb14570 | -7.14984 | -43.29247 | 2025-06-19 03:55:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 1fac8952-9ec3-31e2-8090-b3af2de9ade9 | -7.28295 | -49.99204 | 2025-06-19 03:55:00 | NPP-375D | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 647ee389-5db0-3f05-a894-97323cf7ac33 | -4.55145 | -48.00474 | 2025-06-19 03:55:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 141761f0-eaf5-30ed-bc10-2a5057a7e31a | -4.83856 | -43.18846 | 2025-06-19 03:55:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 82827090-4c67-3a0c-bf9e-f2fb191fe6ea | -6.70679 | -43.25663 | 2025-06-19 03:55:00 | NPP-375D | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Caatinga | 1.5 |
| f9704d40-7995-3e78-9b8d-c9b9dadfb01c | -8.07001 | -43.10711 | 2025-06-19 03:55:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 21.7 |
| 31833147-f502-32ff-beed-9c790f5748e3 | -7.2297 | -43.07875 | 2025-06-19 03:55:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 10.7 |
| 4c25baeb-bea0-34fe-bc1a-f97fdd905a63 | -7.23659 | -43.08253 | 2025-06-19 03:55:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 14.9 |
| aae23b7f-29b5-3046-b2e0-1d4aae182b7c | -6.68271 | -43.20542 | 2025-06-19 03:55:00 | NPP-375D | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 19553c5c-414a-3230-8291-36846f3ad1ca | -7.00805 | -43.69281 | 2025-06-19 03:55:00 | NPP-375D | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 74e30235-0612-3450-a437-641eff329204 | -2.87609 | -40.37961 | 2025-06-19 03:55:00 | NPP-375D | CRUZ | CEARÁ | Brasil | 2304251 | 23 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 47c986aa-a506-37b4-a79d-22aa227ded4e | -6.67211 | -43.20716 | 2025-06-19 03:55:00 | NPP-375D | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 221693dc-0f09-3107-a32d-649c90c6519c | -2.73343 | -47.33622 | 2025-06-19 03:55:00 | NPP-375D | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b30a17c1-24c5-3467-b70c-ea05059b7eae | -11.33355 | -45.21045 | 2025-06-19 03:57:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| aa692e10-e279-38c6-bbff-071baba6bd3e | -12.76692 | -44.4138 | 2025-06-19 03:57:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 05ea32d9-25ce-3c74-902b-2c09fe80c914 | -9.33314 | -47.83652 | 2025-06-19 03:57:00 | NPP-375D | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 5d8ae050-eff8-36cb-b1da-b4957dcb3266 | -11.90923 | -44.1773 | 2025-06-19 03:57:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |


[Clique aqui para ver as próximas entradas](README10.md)
