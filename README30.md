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

## Dados Diários - Página 30

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 50f06e79-1c9e-37f5-81b4-36d65128c592 | -17.22441 | -45.95118 | 2025-09-19 04:49:00 | NOAA-21 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 54385e09-3f70-3619-beda-db57f4e7b263 | -13.66751 | -44.22092 | 2025-09-19 04:49:00 | NOAA-21 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 4b428a78-c1e0-33a5-a694-0f2f0d45f9c6 | -15.32561 | -42.05842 | 2025-09-19 04:49:00 | NOAA-21 | SÃO JOÃO DO PARAÍSO | MINAS GERAIS | Brasil | 3162708 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| 1040a947-bc5f-32ea-9ae7-9b5e1f183273 | -13.95905 | -44.54616 | 2025-09-19 04:49:00 | NOAA-21 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c8869527-212e-3dec-b529-3d72e502ae9b | -17.22032 | -45.94518 | 2025-09-19 04:49:00 | NOAA-21 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 3.4 |
| a554dbfb-510a-391d-9897-1c32cd8d9f48 | -17.17726 | -45.90126 | 2025-09-19 04:49:00 | NOAA-21 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 811fa9a0-a93f-3935-aae0-634ee610a35b | -15.91156 | -59.43853 | 2025-09-19 04:49:00 | NOAA-21 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 71a0a8a0-8698-3dc2-a7d1-055e3efd2885 | -12.92937 | -50.56388 | 2025-09-19 04:49:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 10e24ab5-9da8-3290-a509-1529ed419579 | -15.79601 | -59.40192 | 2025-09-19 04:49:00 | NOAA-21 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 7f87deac-d813-3fbd-9dc1-364ec9e8144f | -17.22132 | -45.9458 | 2025-09-19 04:49:00 | NOAA-21 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 8e487d92-45d8-364d-a60b-1e464393005e | -16.69183 | -54.96956 | 2025-09-19 04:49:00 | NOAA-21 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 71ae9f54-875c-3576-865b-bec036788cf9 | -15.32607 | -42.05395 | 2025-09-19 04:49:00 | NOAA-21 | SÃO JOÃO DO PARAÍSO | MINAS GERAIS | Brasil | 3162708 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| b300d250-8a60-3fb7-ac47-34980856ca4e | -16.80202 | -45.89803 | 2025-09-19 04:49:00 | NOAA-21 | BRASILÂNDIA DE MINAS | MINAS GERAIS | Brasil | 3108552 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| cbf5da12-8a47-342a-9646-86fb80234b56 | -13.95945 | -44.53782 | 2025-09-19 04:49:00 | NOAA-21 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 58621ec5-87e1-370e-a299-b6de981192e5 | -17.23912 | -45.95879 | 2025-09-19 04:49:00 | NOAA-21 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 46644ccc-8988-3b23-92c3-8f271c949e9c | -16.69368 | -54.95818 | 2025-09-19 04:49:00 | NOAA-21 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 22e62590-501d-3cdc-a2fe-ab76e88f7e87 | -17.86304 | -44.30699 | 2025-09-19 04:49:00 | NOAA-21 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 50bdcf8c-0f35-3f89-9967-dcdcf835321a | -15.01008 | -55.31944 | 2025-09-19 04:49:00 | NOAA-21 | CHAPADA DOS GUIMARÃES | MATO GROSSO | Brasil | 5103007 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ce978d8b-43de-363c-af4f-4c15730465bf | -11.81265 | -57.63553 | 2025-09-19 04:49:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| addad54e-03ed-3bdb-92ce-9ad70ab82f44 | -17.23328 | -45.95757 | 2025-09-19 04:49:00 | NOAA-21 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 0752323b-aa4b-30df-a030-f1ad51cfdf87 | -17.23436 | -45.95821 | 2025-09-19 04:49:00 | NOAA-21 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 35e9698a-6ad1-3886-a7a3-a14f796eb2da | -15.32852 | -42.05841 | 2025-09-19 04:49:00 | NOAA-21 | SÃO JOÃO DO PARAÍSO | MINAS GERAIS | Brasil | 3162708 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.1 |
| 391e9409-495b-30ae-8d61-f08c0495a727 | -18.63099 | -43.90955 | 2025-09-19 04:49:00 | NOAA-21 | GOUVEIA | MINAS GERAIS | Brasil | 3127602 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 218ae2e9-186c-32d8-ba36-a35b787974fa | -12.8796 | -50.54444 | 2025-09-19 04:49:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| c1f7f888-ca94-35d4-a48c-d9ebb1543cab | -14.99788 | -55.32906 | 2025-09-19 04:49:00 | NOAA-21 | CHAPADA DOS GUIMARÃES | MATO GROSSO | Brasil | 5103007 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c5cebf01-fea3-3157-ad32-10d3b88d60df | -19.00364 | -47.89571 | 2025-09-19 04:49:00 | NOAA-21 | INDIANÓPOLIS | MINAS GERAIS | Brasil | 3130705 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 3165fff3-3394-378d-bbb1-351b3daef44c | -15.79173 | -59.40129 | 2025-09-19 04:49:00 | NOAA-21 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 90ec77c9-0f4c-36c4-80fe-5ed62a9262dd | -15.03105 | -55.33868 | 2025-09-19 04:49:00 | NOAA-21 | CHAPADA DOS GUIMARÃES | MATO GROSSO | Brasil | 5103007 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 2df3eecf-c506-3dca-ab5d-04b30c047960 | -12.92194 | -50.56663 | 2025-09-19 04:49:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 6c4eb9d9-993f-3041-8a86-ed589f5b022e | -13.67258 | -44.2217 | 2025-09-19 04:49:00 | NOAA-21 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 0.3 |
| bc618e55-fe4b-3c35-b518-422b2fcea5b8 | -16.51559 | -43.54822 | 2025-09-19 04:49:00 | NOAA-21 | FRANCISCO SÁ | MINAS GERAIS | Brasil | 3126703 | 31 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 1cc9b5cd-d837-3fb9-b5e9-3604900cadb9 | -12.93452 | -50.55296 | 2025-09-19 04:49:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 3499455a-076a-32c6-8277-af8d2dc6d8b8 | -15.03233 | -55.33099 | 2025-09-19 04:49:00 | NOAA-21 | CHAPADA DOS GUIMARÃES | MATO GROSSO | Brasil | 5103007 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| dd040cd8-fc1f-3b40-9735-464bb96a32f9 | -17.16142 | -44.78948 | 2025-09-19 04:49:00 | NOAA-21 | VÁRZEA DA PALMA | MINAS GERAIS | Brasil | 3170800 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 6db1b02c-1187-3b26-bac4-b156fb5e825c | -12.88017 | -50.54061 | 2025-09-19 04:49:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ca3e3c45-c813-35f0-8d21-015ebe24b483 | -12.92594 | -50.56335 | 2025-09-19 04:49:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 5.3 |
| a7081e22-12b2-378e-a288-f105fbc76a43 | -14.99724 | -55.33295 | 2025-09-19 04:49:00 | NOAA-21 | CHAPADA DOS GUIMARÃES | MATO GROSSO | Brasil | 5103007 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 333d3418-6556-36a3-8eb0-6a1188b7947d | -17.1725 | -45.90058 | 2025-09-19 04:49:00 | NOAA-21 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d82a8b30-5b8f-3181-980c-ec31934387ee | -20.5176 | -42.39097 | 2025-09-19 04:51:00 | NOAA-21 | SERICITA | MINAS GERAIS | Brasil | 3166303 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| bc0eaebb-c483-3f8b-86ce-50cdfd848ee6 | -19.57146 | -57.74866 | 2025-09-19 04:51:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.0 |
| e4c1a6cc-48a3-3d20-930e-4695760c8f40 | -20.7471 | -56.94636 | 2025-09-19 04:51:00 | NOAA-21 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 1.7 |
| eb1bab95-240b-322a-9613-3a53915ee03a | -22.32718 | -54.41425 | 2025-09-19 04:51:00 | NOAA-21 | FÁTIMA DO SUL | MATO GROSSO DO SUL | Brasil | 5003801 | 50 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 12f40d9b-6ec7-33c3-a731-b2b2d1f75750 | -19.57871 | -57.75008 | 2025-09-19 04:51:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.3 |
| de1482f8-d74f-32b7-854a-b9cf8f00e411 | -21.04891 | -48.43716 | 2025-09-19 04:51:00 | NOAA-21 | TAQUARAL | SÃO PAULO | Brasil | 3553658 | 35 | 33 | nan | nan | nan | Cerrado | 3.9 |
| ed03b3f6-167f-39e5-a38d-30d8f367e687 | -23.31039 | -47.14534 | 2025-09-19 04:51:00 | NOAA-21 | CABREÚVA | SÃO PAULO | Brasil | 3508405 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| dbd1462e-9bf3-380a-ad64-ff4c1e47ae3b | -22.93678 | -46.95581 | 2025-09-19 04:51:00 | NOAA-21 | VALINHOS | SÃO PAULO | Brasil | 3556206 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.1 |
| e0038a0f-61df-34ea-aee4-0bc0f07e3b43 | -19.58949 | -57.81712 | 2025-09-19 04:51:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.6 |
| f5feebac-43ca-3843-8139-083b23d73962 | -22.34039 | -46.76695 | 2025-09-19 04:51:00 | NOAA-21 | ITAPIRA | SÃO PAULO | Brasil | 3522604 | 35 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 7de0c9cb-39d3-3d4f-be43-ad7a957eb80c | -21.29349 | -54.80728 | 2025-09-19 04:51:00 | NOAA-21 | SIDROLÂNDIA | MATO GROSSO DO SUL | Brasil | 5007901 | 50 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 6e582046-afc3-35e2-922d-67e9b04b3ca0 | -20.53356 | -55.17678 | 2025-09-19 04:51:00 | NOAA-21 | TERENOS | MATO GROSSO DO SUL | Brasil | 5008008 | 50 | 33 | nan | nan | nan | Cerrado | 0.5 |
| a8933cda-7a14-3f30-959d-a2c5029d5494 | -23.60343 | -51.05188 | 2025-09-19 04:51:00 | NOAA-21 | LONDRINA | PARANÁ | Brasil | 4113700 | 41 | 33 | nan | nan | nan | Mata Atlântica | 3.5 |
| 135bfad2-8db0-3505-98c9-a1d2bddafb5a | -20.42836 | -46.48244 | 2025-09-19 04:51:00 | NOAA-21 | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 98dc9d66-b0bb-37b3-879a-c64eb8bf7b88 | -22.26074 | -54.79956 | 2025-09-19 04:51:00 | NOAA-21 | DOURADOS | MATO GROSSO DO SUL | Brasil | 5003702 | 50 | 33 | nan | nan | nan | Cerrado | 0.6 |
| dd7d4641-5b8f-31c0-beb6-c962564f87a8 | -21.29449 | -48.79687 | 2025-09-19 04:51:00 | NOAA-21 | SANTA ADÉLIA | SÃO PAULO | Brasil | 3545605 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 34a83dd7-a51b-3132-8d1c-f983846a4206 | -22.2512 | -55.98832 | 2025-09-19 04:51:00 | NOAA-21 | ANTÔNIO JOÃO | MATO GROSSO DO SUL | Brasil | 5000906 | 50 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 73364f61-6394-33f2-8ed1-aac9f2766399 | -23.40702 | -50.69059 | 2025-09-19 04:51:00 | NOAA-21 | SÃO SEBASTIÃO DA AMOREIRA | PARANÁ | Brasil | 4126009 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 61f3b2bb-b42c-38d9-aebd-f2828206862d | -22.28095 | -55.97443 | 2025-09-19 04:51:00 | NOAA-21 | ANTÔNIO JOÃO | MATO GROSSO DO SUL | Brasil | 5000906 | 50 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 10988f53-8ed6-3bef-906e-c61c4b22e655 | -21.29031 | -48.79647 | 2025-09-19 04:51:00 | NOAA-21 | SANTA ADÉLIA | SÃO PAULO | Brasil | 3545605 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 5c4fe1d7-7ede-308c-ad63-4cfe1869e3eb | -22.66802 | -53.12077 | 2025-09-19 04:51:00 | NOAA-21 | MARILENA | PARANÁ | Brasil | 4115002 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 0ab7290d-c3ca-3c54-b7ff-79be447b9582 | -19.59234 | -57.82234 | 2025-09-19 04:51:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.6 |
| 5a282c90-f72e-3398-945b-2b6c2cbb5886 | -22.04632 | -45.59013 | 2025-09-19 04:51:00 | NOAA-21 | HELIODORA | MINAS GERAIS | Brasil | 3129202 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| cef505d6-c021-371a-826d-c2b689d9501f | -22.67085 | -53.1253 | 2025-09-19 04:51:00 | NOAA-21 | SÃO PEDRO DO PARANÁ | PARANÁ | Brasil | 4125902 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 3c633738-8ccf-32f0-aceb-f0f93691dadf | -21.28614 | -48.79602 | 2025-09-19 04:51:00 | NOAA-21 | SANTA ADÉLIA | SÃO PAULO | Brasil | 3545605 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| a5894118-d664-3bc4-8336-59724cb7f918 | -21.28358 | -54.80551 | 2025-09-19 04:51:00 | NOAA-21 | SIDROLÂNDIA | MATO GROSSO DO SUL | Brasil | 5007901 | 50 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 4d33dd0c-9012-34eb-8af3-d914376000df | -22.34521 | -46.76752 | 2025-09-19 04:51:00 | NOAA-21 | ITAPIRA | SÃO PAULO | Brasil | 3522604 | 35 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 60e59335-a8d1-325f-85e8-bba9b22504e8 | -19.58312 | -57.74632 | 2025-09-19 04:51:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.7 |
| 17117d67-a110-3b90-a33b-654b6f3b5baf | -23.67698 | -51.72149 | 2025-09-19 04:51:00 | NOAA-21 | BOM SUCESSO | PARANÁ | Brasil | 4103206 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 9227bec1-e070-3ca1-8bee-67020dcf5a09 | -22.3398 | -46.77248 | 2025-09-19 04:51:00 | NOAA-21 | ITAPIRA | SÃO PAULO | Brasil | 3522604 | 35 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 01ccd884-fd7d-39ff-8d3d-5108a9be79f0 | -21.29019 | -54.80669 | 2025-09-19 04:51:00 | NOAA-21 | SIDROLÂNDIA | MATO GROSSO DO SUL | Brasil | 5007901 | 50 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 23c27cba-9624-3c90-a44a-696bd2ddd75f | -22.75376 | -51.40444 | 2025-09-19 04:51:00 | NOAA-21 | PORECATU | PARANÁ | Brasil | 4120002 | 41 | 33 | nan | nan | nan | Mata Atlântica | 7.9 |
| 5f86ad1d-7240-3fb4-84ec-f4245dd877bc | -23.23746 | -47.62438 | 2025-09-19 04:51:00 | NOAA-21 | BOITUVA | SÃO PAULO | Brasil | 3507001 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 1e62f59a-a411-3b71-aca7-aa3104d28507 | -21.12408 | -45.72244 | 2025-09-19 04:51:00 | NOAA-21 | CAMPO DO MEIO | MINAS GERAIS | Brasil | 3111309 | 31 | 33 | nan | nan | nan | Mata Atlântica | 11.5 |
| 9e32e530-1b59-3be0-8962-00cc101a8d57 | -23.14694 | -46.59903 | 2025-09-19 04:51:00 | NOAA-21 | ATIBAIA | SÃO PAULO | Brasil | 3504107 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| 7c00906f-b473-3b56-ab49-ddb433f5fe66 | -21.2147 | -46.93886 | 2025-09-19 04:51:00 | NOAA-21 | MONTE SANTO DE MINAS | MINAS GERAIS | Brasil | 3143203 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| ec478a08-dd61-347a-9d86-8bb59f9be444 | -20.16775 | -41.48052 | 2025-09-19 04:51:00 | NOAA-21 | LAJINHA | MINAS GERAIS | Brasil | 3137700 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 597a0a05-6844-3879-a5fa-c74831aa0797 | -22.04116 | -45.58936 | 2025-09-19 04:51:00 | NOAA-21 | HELIODORA | MINAS GERAIS | Brasil | 3129202 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.7 |
| 211ae14e-ab44-3f88-88c4-6b9add5948dc | -21.29407 | -54.8036 | 2025-09-19 04:51:00 | NOAA-21 | SIDROLÂNDIA | MATO GROSSO DO SUL | Brasil | 5007901 | 50 | 33 | nan | nan | nan | Cerrado | 1.0 |
| fa687499-3f60-3e95-bfc0-efde7838d957 | -23.41082 | -50.69131 | 2025-09-19 04:51:00 | NOAA-21 | SÃO SEBASTIÃO DA AMOREIRA | PARANÁ | Brasil | 4126009 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 3685d21c-50ea-3bec-9e62-41192fac3e67 | -21.28891 | -48.79399 | 2025-09-19 04:51:00 | NOAA-21 | SANTA ADÉLIA | SÃO PAULO | Brasil | 3545605 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| 221b262f-c3a9-395d-840e-90ad23eb8ec2 | -22.75437 | -51.39987 | 2025-09-19 04:51:00 | NOAA-21 | PORECATU | PARANÁ | Brasil | 4120002 | 41 | 33 | nan | nan | nan | Mata Atlântica | 7.9 |
| cc0dcb51-a2ad-3fcf-870e-7cbc3a23afcb | -21.2863 | -54.80978 | 2025-09-19 04:51:00 | NOAA-21 | SIDROLÂNDIA | MATO GROSSO DO SUL | Brasil | 5007901 | 50 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 03b40c61-7141-3b6b-a220-541059af3dea | -22.35003 | -46.76795 | 2025-09-19 04:51:00 | NOAA-21 | ITAPIRA | SÃO PAULO | Brasil | 3522604 | 35 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 82459b26-bbe9-392d-8568-c162ead4a69b | -24.93948 | -50.10942 | 2025-09-19 04:51:00 | NOAA-21 | CARAMBEÍ | PARANÁ | Brasil | 4104659 | 41 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| 9862ef7c-8898-325a-8eff-a66bca0e8c1b | -21.28662 | -48.79189 | 2025-09-19 04:51:00 | NOAA-21 | SANTA ADÉLIA | SÃO PAULO | Brasil | 3545605 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| b66db803-214f-3c5d-baaf-e53ae071bd56 | -19.5795 | -57.7456 | 2025-09-19 04:51:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.7 |
| fcabeb3f-7abe-3b70-be6c-ed38917ffb38 | -20.22941 | -50.90379 | 2025-09-19 04:51:00 | NOAA-21 | TRÊS FRONTEIRAS | SÃO PAULO | Brasil | 3554904 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| ee255a63-c308-3084-b8b9-5ce108cc162f | -22.00125 | -56.0358 | 2025-09-19 04:51:00 | NOAA-21 | PONTA PORÃ | MATO GROSSO DO SUL | Brasil | 5006606 | 50 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 188a2825-80b4-3686-a5e5-1b8b3c77cb82 | -22.33618 | -46.76073 | 2025-09-19 04:51:00 | NOAA-21 | ITAPIRA | SÃO PAULO | Brasil | 3522604 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| d8980b51-5bdf-3221-8327-f5a0e4c32f03 | -21.28688 | -54.8061 | 2025-09-19 04:51:00 | NOAA-21 | SIDROLÂNDIA | MATO GROSSO DO SUL | Brasil | 5007901 | 50 | 33 | nan | nan | nan | Cerrado | 2.8 |
| b65f9911-2a33-385b-b73c-3bc56bdfea53 | -21.2194 | -46.93931 | 2025-09-19 04:51:00 | NOAA-21 | MONTE SANTO DE MINAS | MINAS GERAIS | Brasil | 3143203 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 972156a6-9996-31c3-a85d-3310e8960dfb | -22.93149 | -46.96001 | 2025-09-19 04:51:00 | NOAA-21 | VALINHOS | SÃO PAULO | Brasil | 3556206 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.1 |
| c15255f6-07b3-3e4d-b674-8de96cfd49e7 | -19.81841 | -44.21808 | 2025-09-19 04:51:00 | NOAA-21 | ESMERALDAS | MINAS GERAIS | Brasil | 3124104 | 31 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 95770ed8-45e5-38ae-9b16-8738b011bd2e | -20.21496 | -44.61005 | 2025-09-19 04:51:00 | NOAA-21 | CARMO DO CAJURU | MINAS GERAIS | Brasil | 3114204 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 07153f1f-c146-3b2a-9317-008509ca06de | -22.04083 | -45.59261 | 2025-09-19 04:51:00 | NOAA-21 | HELIODORA | MINAS GERAIS | Brasil | 3129202 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.5 |
| 31070865-8418-3d01-bb85-7db1e5e48109 | -21.28961 | -54.81038 | 2025-09-19 04:51:00 | NOAA-21 | SIDROLÂNDIA | MATO GROSSO DO SUL | Brasil | 5007901 | 50 | 33 | nan | nan | nan | Cerrado | 2.3 |
| b0a1cf6d-6bf9-3217-909e-244d2404bbd4 | -22.7501 | -51.40393 | 2025-09-19 04:51:00 | NOAA-21 | PORECATU | PARANÁ | Brasil | 4120002 | 41 | 33 | nan | nan | nan | Mata Atlântica | 7.9 |
| b257ec25-337b-30f1-a17e-318060b25168 | -20.71374 | -56.74434 | 2025-09-19 04:51:00 | NOAA-21 | BODOQUENA | MATO GROSSO DO SUL | Brasil | 5002159 | 50 | 33 | nan | nan | nan | Cerrado | 2.5 |
| d576963c-6624-3d8a-a897-5428297327e0 | -23.13335 | -49.64573 | 2025-09-19 04:51:00 | NOAA-21 | TIMBURI | SÃO PAULO | Brasil | 3554607 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 9ff9d7cb-4d19-309e-bbbd-9eed4e1313d5 | -20.34898 | -48.78724 | 2025-09-19 04:51:00 | NOAA-21 | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 3.9 |
| eab6c4dd-51ee-325b-bccd-9b1d858b92ef | -20.79538 | -47.23744 | 2025-09-19 04:51:00 | NOAA-21 | PATROCÍNIO PAULISTA | SÃO PAULO | Brasil | 3536307 | 35 | 33 | nan | nan | nan | Cerrado | 7.7 |


[Clique aqui para ver as próximas entradas](README31.md)
